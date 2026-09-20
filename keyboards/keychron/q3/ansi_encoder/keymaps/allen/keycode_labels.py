"""Keycode -> (short label, long description), both derived from QMK's own
keycode data (data/constants/keycodes/*.hjson in qmk_firmware) — no
per-keycode dict to maintain. The long description is QMK's own "label" text
(or a humanized fallback when a keycode has none). The short label is that
same text run through a small, general abbreviation ruleset (common word
shortenings, a Left/Right-strip, an Up/Down-to-+/- suffix) — the ruleset is
generic English-abbreviation knowledge, not a table of keycodes, so it
applies to any keycode QMK ships, including ones not yet used in this
keymap.
"""
import os
import re
import sys
from pathlib import Path

ACRONYMS = {"RGB", "KB", "USB", "LED", "DM", "MS", "CW", "AL", "AC"}

# word (lowercased) -> abbreviation, used when building short labels.
WORD_ABBR = {
    "brightness": "Brt", "volume": "Vol", "print": "Prt", "screen": "Scr",
    "control": "Ctrl", "windows": "Win", "gui": "Win", "backspace": "Bksp",
    "insert": "Ins", "delete": "Del", "previous": "Prev", "next": "Nxt",
    "toggle": "Tog", "saturation": "Sat", "speed": "Spd", "value": "Val",
    "effect": "Fx", "record": "Rec", "spacebar": "Space", "wheel": "Whl",
    "application": "App",
}
# filler words dropped entirely when building a short label.
DROP_WORDS = {"mouse", "track", "lock", "start", "dynamic", "matrix", "mode"}
# a trailing Up/Down becomes a +/- suffix instead of its own word.
SUFFIX_WORDS = {"up": "+", "down": "-"}


def _abbreviate(label):
    words = label.replace("/", " ").split()
    if words and words[0].lower() in ("left", "right"):
        words = words[1:]
    suffix = ""
    if words and words[-1].lower() in SUFFIX_WORDS and len(words) > 1:
        suffix = SUFFIX_WORDS[words[-1].lower()]
        words = words[:-1]
    words = [w for w in words if w.lower() not in DROP_WORDS]
    parts = []
    for w in words:
        lw = w.lower()
        if lw in WORD_ABBR:
            parts.append(WORD_ABBR[lw])
        elif len(w) > 5:
            parts.append(w[:4])
        else:
            parts.append(w)
    result = "".join(parts) + suffix
    return result if result else label


def _find_qmk_firmware():
    if "QMK_HOME" in os.environ:
        return Path(os.environ["QMK_HOME"]).expanduser()
    return Path.home() / "qmk_firmware"


def _humanize(key):
    name = key
    for prefix in ("QK_", "KC_"):
        if name.startswith(prefix):
            name = name[len(prefix):]
            break
    words = [w if w in ACRONYMS else w.capitalize() for w in name.split("_")]
    return " ".join(words)


def _load_lookup():
    qmk_firmware = _find_qmk_firmware()
    lib_path = qmk_firmware / "lib" / "python"
    if str(lib_path) not in sys.path:
        sys.path.insert(0, str(lib_path))
    from qmk.keycodes import load_spec  # noqa: E402

    # qmk.keycodes resolves its data files relative to cwd, assuming it's
    # run from inside qmk_firmware.
    cwd = Path.cwd()
    os.chdir(qmk_firmware)
    try:
        spec = load_spec("latest")
    finally:
        os.chdir(cwd)
    lookup = {}
    for entry in spec["keycodes"].values():
        long_label = entry.get("label") or _humanize(entry["key"])
        for name in [entry["key"]] + entry.get("aliases", []):
            lookup[name] = (long_label, entry.get("group", ""))
    return lookup


_LOOKUP = None

# QMK keycode "group" -> docs.qmk.fm page. A few groups (dynamic macros,
# caps word) are lumped under "quantum" in the data but actually documented
# on their own feature page, so those are matched by token prefix first.
PREFIX_DOCS = {
    "DM_": "features/dynamic_macros",
    "CW_": "features/caps_word",
}
GROUP_DOCS = {
    "basic": "keycodes_basic",
    "modifiers": "keycodes_basic",
    "media": "keycodes_basic",
    "mouse": "features/mouse_keys",
    "rgb_matrix": "features/rgb_matrix",
    "backlight": "features/backlight",
    "quantum": "quantum_keycodes",
}
DOCS_BASE = "https://docs.qmk.fm/"


def doc_url_for(token):
    for prefix, page in PREFIX_DOCS.items():
        if token.startswith(prefix):
            return DOCS_BASE + page

    m = re.fullmatch(r"MO\(\w+\)", token)
    if m:
        return DOCS_BASE + "feature_layers"

    # modifier-wrapped combos: link to whatever key they're wrapping.
    m = re.fullmatch(r"(?:L|R)(?:CTL|ALT|SFT|GUI)\((.+)\)", token)
    if m:
        return doc_url_for(m.group(1))

    global _LOOKUP
    if _LOOKUP is None:
        _LOOKUP = _load_lookup()
    if token in _LOOKUP:
        _, group = _LOOKUP[token]
        page = GROUP_DOCS.get(group, "keycodes")
        return DOCS_BASE + page
    return DOCS_BASE + "keycodes"


def label_for(token):
    global _LOOKUP
    if _LOOKUP is None:
        _LOOKUP = _load_lookup()

    if token == "_______":
        return ("_", None)
    if token == "KC_NO":
        return ("-", None)
    if token in _LOOKUP:
        long_label, _group = _LOOKUP[token]
        return (_abbreviate(long_label), long_label)

    m = re.fullmatch(r"MO\((\w+)\)", token)
    if m:
        return ("Fn", f"Momentary layer switch to {m.group(1)}")

    # modifier-wrapped combos, e.g. LCTL(LALT(KC_M)) or LCTL(KC_F9)
    mods = []
    inner = token
    while True:
        m = re.fullmatch(r"(L|R)(CTL|ALT|SFT|GUI)\((.+)\)", inner)
        if not m:
            break
        mods.append({"CTL": "Ctrl", "ALT": "Alt", "SFT": "Shift", "GUI": "Win"}[m.group(2)])
        inner = m.group(3)
    if mods:
        inner_label = label_for(inner)[0]
        combo = "+".join(mods + [inner_label])
        return (combo, f"Sends {combo}")

    return (token.removeprefix("KC_"), token)
