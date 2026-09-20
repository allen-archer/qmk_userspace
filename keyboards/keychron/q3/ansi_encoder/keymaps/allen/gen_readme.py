#!/home/allen/.local/share/pipx/venvs/qmk/bin/python3
"""Regenerate README.md from keymap.c for the WIN_BASE/WIN_FN layers.

MAC_BASE/MAC_FN are intentionally skipped: unused legacy layers, not worth documenting.
"""
import re
import sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))
from keycode_labels import label_for  # noqa: E402

KEYMAP = HERE / "keymap.c"
README = HERE / "README.md"

# Physical key order for LAYOUT_tkl_f13_ansi, row by row. Fixed by hardware.
ROWS = [
    ["Esc", "F1", "F2", "F3", "F4", "F5", "F6", "F7", "F8", "F9", "F10", "F11", "F12",
     "Mute (2)", "PrtSc", "(unused)", "Knob Press"],
    ["`", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "-", "=",
     "Backspace", "Insert", "Home", "PgUp"],
    ["Tab", "Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P", "[", "]", "\\",
     "Delete", "End", "PgDn"],
    ["Caps Lock", "A", "S", "D", "F", "G", "H", "J", "K", "L", ";", "'", "Enter"],
    ["L Shift", "Z", "X", "C", "V", "B", "N", "M", ",", ".", "/", "R Shift", "Up"],
    ["L Ctrl", "L Win", "L Alt", "Space", "R Alt", "R Win", "Fn", "R Ctrl",
     "Left", "Down", "Right"],
]
KEY_NAMES = [name for row in ROWS for name in row]


def extract_layer(src, layer_name):
    m = re.search(rf"\[{layer_name}\]\s*=\s*LAYOUT_\w+\(", src)
    start = m.end()
    depth = 1
    i = start
    while depth:
        if src[i] == "(":
            depth += 1
        elif src[i] == ")":
            depth -= 1
        i += 1
    body = src[start:i - 1]
    tokens = []
    depth = 0
    current = ""
    for ch in body:
        if ch == "(":
            depth += 1
            current += ch
        elif ch == ")":
            depth -= 1
            current += ch
        elif ch == "," and depth == 0:
            tokens.append(current.strip())
            current = ""
        else:
            current += ch
    if current.strip():
        tokens.append(current.strip())
    return [t for t in tokens if t]


def render_grid(tokens):
    # Show the raw keycode, not the human-readable short label — the table
    # below already translates each one, so this stays a 1:1 mirror of
    # keymap.c that's easy to cross-reference against the source.
    labels = tokens
    width = max(len(c) for c in labels)
    out = []
    idx = 0
    for row in ROWS:
        cells = labels[idx:idx + len(row)]
        idx += len(row)
        out.append("  ".join(f"{c:<{width}}" for c in cells).rstrip())
    return "\n".join(out)


def render_table(base_tokens, fn_tokens):
    lines = ["| Key | Sends | Effect |", "|---|---|---|"]
    for name, base_tok, fn_tok in zip(KEY_NAMES, base_tokens, fn_tokens):
        if fn_tok == "_______":
            continue
        short, desc = label_for(fn_tok)
        lines.append(f"| Fn+{name} | `{fn_tok}` | {desc or short} |")
    return "\n".join(lines)


def main():
    src = KEYMAP.read_text()
    base_tokens = extract_layer(src, "WIN_BASE")
    fn_tokens = extract_layer(src, "WIN_FN")
    assert len(base_tokens) == len(KEY_NAMES), f"WIN_BASE token count {len(base_tokens)} != {len(KEY_NAMES)}"
    assert len(fn_tokens) == len(KEY_NAMES), f"WIN_FN token count {len(fn_tokens)} != {len(KEY_NAMES)}"

    doc = f"""# Keymap: `allen` — Keychron Q3 (ANSI, encoder)

The keymap defines four layers, but only **WIN_BASE** and **WIN_FN** are used day to day — the board is always left in Windows mode. **MAC_BASE**/**MAC_FN** are kept only as unused legacy layers; they're never switched into, since there's no keycode in this keymap that activates them.

This file is generated — run `./gen_readme.py` after editing `keymap.c` to refresh it.

## Layer activation

| Layer | How to reach it |
|---|---|
| `WIN_BASE` | Default layer, always active unless Fn is held |
| `WIN_FN` | Hold the bottom-right **Fn** key (momentary — release to return to `WIN_BASE`) |

## WIN_BASE (default)

```
{render_grid(base_tokens)}
```

Standard QWERTY layout. The only non-obvious key is **Fn** (bottom row) — a momentary hold that activates the Fn layer below.

**Rotary encoder:** Volume Down / Volume Up.

## WIN_FN (Fn held)

```
{render_grid(fn_tokens)}
```

Everything not listed below is transparent (`_______`) — it falls through and behaves exactly like `WIN_BASE`.

{render_table(base_tokens, fn_tokens)}

**Rotary encoder (while Fn held):** keyboard RGB brightness down / up.
"""
    README.write_text(doc)
    print(f"wrote {README}")


if __name__ == "__main__":
    main()
