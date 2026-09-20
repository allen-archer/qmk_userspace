#!/home/allen/.local/share/pipx/venvs/qmk/bin/python3
"""Regenerate reference.html (a printable visual keycap reference) from keymap.c.

Reuses the token extraction / labeling from gen_readme.py so both docs stay
derived from the same source of truth.
"""
import html
import sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))
from gen_readme import KEYMAP, ROWS, label_for, extract_layer  # noqa: E402
from keycode_labels import doc_url_for  # noqa: E402

OUT = HERE / "reference.html"

# Per-row key widths (in keycap units) and gap positions, matching the
# physical LAYOUT_tkl_f13_ansi stagger. Index-aligned with ROWS.
ROW_WIDTHS = [
    [1] * 17,
    [1] * 13 + [2] + [1] * 3,
    [1.5] + [1] * 12 + [1.5] + [1] * 3,
    [1.75] + [1] * 11 + [2.25],
    [2.25] + [1] * 10 + [1.75] + [1],
    [1.25] * 3 + [6.25] + [1.25] * 4 + [1] * 3,
]
# gaps: row_index -> list of (index before which to insert a spacer, spacer width)
ROW_GAPS = {
    0: [(1, 0.4), (5, 0.4), (9, 0.4), (13, 0.4)],
    3: [(13, 3.5)],  # trailing spacer to align row width
    4: [(12, 1.5), (13, 1.5)],  # spacers flanking Up
    5: [(8, 0.35)],
}

CSS = """
  :root{
    --paper:#faf8f3; --ink:#20221f; --ink-soft:#4a4d47; --rule:#d9d4c6;
    --accent:#3a6b5c; --accent-soft:#e3ece7;
    --key-face:#fffdf8; --key-face-dim:#f1efe7;
    --key-border:#c9c2ae; --key-border-dim:#dcd7c9;
    --mono:"JetBrains Mono", ui-monospace, "SF Mono", Consolas, monospace;
    --sans:"Libre Franklin", "Segoe UI", system-ui, sans-serif;
  }
  @media (prefers-color-scheme: dark){
    :root:not([data-theme="light"]){
      --paper:#191a17; --ink:#ece8dd; --ink-soft:#a6a294; --rule:#3a392f;
      --accent:#6fae98; --accent-soft:#233129;
      --key-face:#232420; --key-face-dim:#1c1d1a;
      --key-border:#454336; --key-border-dim:#2c2b25;
    }
  }
  :root[data-theme="dark"]{
    --paper:#191a17; --ink:#ece8dd; --ink-soft:#a6a294; --rule:#3a392f;
    --accent:#6fae98; --accent-soft:#233129;
    --key-face:#232420; --key-face-dim:#1c1d1a;
    --key-border:#454336; --key-border-dim:#2c2b25;
  }
  *{box-sizing:border-box;}
  body{background:var(--paper); color:var(--ink); font-family:var(--sans);
    margin:0; padding:3rem 1.5rem 5rem; display:flex; justify-content:center;}
  main{width:100%; max-width:840px;}
  header{margin-bottom:2.75rem;}
  .eyebrow{font-family:var(--mono); font-size:0.72rem; letter-spacing:0.14em;
    text-transform:uppercase; color:var(--accent); margin:0 0 0.6rem;}
  h1{font-size:2.15rem; font-weight:800; letter-spacing:-0.01em; margin:0 0 0.5rem; text-wrap:balance;}
  h1 code{font-family:var(--mono); font-weight:600; background:var(--accent-soft);
    color:var(--accent); padding:0.08em 0.4em; border-radius:4px; font-size:0.82em;}
  .dek{font-size:1.02rem; color:var(--ink-soft); max-width:60ch; line-height:1.55; margin:0;}
  h2{font-size:1.2rem; font-weight:700; margin:0 0 0.3rem; letter-spacing:-0.005em;}
  .section{margin-top:3rem;}
  .section-head{display:flex; align-items:baseline; justify-content:space-between; gap:1rem;
    border-bottom:1.5px solid var(--rule); padding-bottom:0.6rem; margin-bottom:1.1rem;}
  .section-note{font-family:var(--mono); font-size:0.75rem; color:var(--ink-soft); white-space:nowrap;}
  .activation{width:100%; border-collapse:collapse; font-size:0.92rem;}
  .activation th{text-align:left; font-family:var(--mono); font-size:0.68rem; letter-spacing:0.1em;
    text-transform:uppercase; color:var(--ink-soft); font-weight:500; padding:0 0 0.5rem;
    border-bottom:1px solid var(--rule);}
  .activation td{padding:0.6rem 0.8rem 0.6rem 0; border-bottom:1px solid var(--rule); vertical-align:top;}
  .activation td:first-child{width:9rem;}
  .activation code{font-family:var(--mono); font-weight:600; color:var(--accent);}
  .board{background:var(--key-face-dim); border:1px solid var(--rule); border-radius:10px; padding:1rem;}
  .row{display:flex; gap:0.28rem; margin-bottom:0.28rem;}
  .row:last-child{margin-bottom:0;}
  .key{flex:var(--w,1) 0 0; min-width:0; position:relative; background:var(--key-face); border:1px solid var(--key-border);
    border-radius:5px; min-height:2.5rem; display:flex; align-items:center; justify-content:center;
    text-align:center; overflow-wrap:anywhere; font-family:var(--mono); font-size:0.66rem; font-weight:500; line-height:1.2;
    padding:0.15rem 0.2rem; color:var(--ink); letter-spacing:-0.01em; text-decoration:none;}
  a.key{cursor:pointer;}
  a.key:hover{border-color:var(--accent); box-shadow:0 0 0 1px var(--accent);}
  a.key[data-tip]:hover::after{content:attr(data-tip); position:absolute; bottom:calc(100% + 0.4rem);
    left:50%; transform:translateX(-50%); background:var(--ink); color:var(--paper); font-family:var(--sans);
    font-size:0.74rem; font-weight:500; letter-spacing:0; white-space:nowrap; padding:0.3rem 0.6rem;
    border-radius:5px; box-shadow:0 4px 14px rgba(0,0,0,0.25); pointer-events:none; z-index:20;}
  a.key[data-tip]:hover::before{content:""; position:absolute; bottom:100%; left:50%; transform:translateX(-50%);
    border:5px solid transparent; border-top-color:var(--ink); margin-bottom:-0.1rem; pointer-events:none; z-index:20;}
  .key.spacer{background:transparent; border:none;}
  .key--dim{background:var(--key-face-dim); border-color:var(--key-border-dim); color:var(--ink-soft); opacity:0.55;}
  .key--active{background:var(--accent-soft); border-color:var(--accent); color:var(--accent); font-weight:700;}
  .encoder-note{font-family:var(--mono); font-size:0.8rem; color:var(--ink-soft); margin:0.9rem 0 0;}
  .encoder-note strong{color:var(--ink); font-weight:600;}
  footer{margin-top:3.5rem; padding-top:1.2rem; border-top:1px solid var(--rule); font-family:var(--mono);
    font-size:0.72rem; color:var(--ink-soft); display:flex; justify-content:space-between; gap:1rem; flex-wrap:wrap;}
  @media print{
    body{padding:0; background:#fff; color:#000;}
    :root{--paper:#fff; --ink:#000; --ink-soft:#333; --rule:#bbb; --accent:#2c5245; --accent-soft:#eef3f0;
      --key-face:#fff; --key-face-dim:#f6f6f2; --key-border:#999; --key-border-dim:#ccc;}
    .board{break-inside:avoid;}
    .section{break-inside:avoid-page;}
    a{color:inherit; text-decoration:none;}
  }
  @media (max-width:560px){ .key{font-size:0.56rem;} h1{font-size:1.6rem;} }
"""


def render_board(tokens, fn_layer):
    from keycode_labels import doc_url_for

    idx = 0
    rows_html = []
    for r, row in enumerate(ROWS):
        row_tokens = tokens[idx:idx + len(row)]
        labels = [label_for(t)[0] for t in row_tokens]
        idx += len(row)
        widths = ROW_WIDTHS[r]
        gaps = dict(ROW_GAPS.get(r, []))
        cells = []
        for i, (token, label, w) in enumerate(zip(row_tokens, labels, widths)):
            if i in gaps:
                cells.append(f'<div class="key spacer" style="--w:{gaps[i]}"></div>')
            if fn_layer:
                is_dim = token == "_______"
                cls = "key key--dim" if is_dim else "key key--active"
            else:
                cls = "key"
            if token in ("_______", "KC_NO"):
                cells.append(f'<div class="{cls}" style="--w:{w}">{label}</div>')
            else:
                _, desc = label_for(token)
                tooltip = html.escape(desc or label, quote=True)
                url = doc_url_for(token)
                cells.append(
                    f'<a class="{cls}" style="--w:{w}" title="{tooltip}" data-tip="{tooltip}" '
                    f'href="{url}" target="_blank" rel="noopener">{label}</a>'
                )
        # trailing gap (index == len(row))
        if len(row) in gaps:
            cells.append(f'<div class="key spacer" style="--w:{gaps[len(row)]}"></div>')
        rows_html.append(f'      <div class="row">\n        ' + "\n        ".join(cells) + "\n      </div>")
    return "\n".join(rows_html)


def main():
    src = KEYMAP.read_text()
    base_tokens = extract_layer(src, "WIN_BASE")
    fn_tokens = extract_layer(src, "WIN_FN")

    html = f"""<title>Allen Keymap Reference</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Libre+Franklin:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600;700&display=swap">
<style>{CSS}</style>

<main>
  <section class="section" style="margin-top:0;">
    <div class="section-head">
      <h2>WIN_BASE <span style="font-weight:400;color:var(--ink-soft);">&mdash; default</span></h2>
      <span class="section-note">standard QWERTY</span>
    </div>
    <div class="board" aria-label="WIN_BASE key layout">
{render_board(base_tokens, fn_layer=False)}
    </div>
    <p class="encoder-note">Rotary encoder: <strong>Volume Down</strong> / <strong>Volume Up</strong></p>
  </section>

  <section class="section">
    <div class="section-head">
      <h2>WIN_FN <span style="font-weight:400;color:var(--ink-soft);">&mdash; Fn held</span></h2>
      <span class="section-note">dim = transparent, falls through to base</span>
    </div>
    <div class="board" aria-label="WIN_FN key layout">
{render_board(fn_tokens, fn_layer=True)}
    </div>
    <p class="encoder-note">Rotary encoder (Fn held): keyboard <strong>RGB brightness down</strong> / <strong>up</strong></p>
    <p class="encoder-note">Hover a key for what it does &middot; click a key to open its QMK docs page</p>
  </section>

  <footer>
    <span>Keychron Q3 &middot; ANSI &middot; Encoder &mdash; keymap <code>allen</code></span>
    <span>MAC_BASE / MAC_FN unused, unreachable</span>
  </footer>
</main>
"""
    OUT.write_text(html)
    print(f"wrote {OUT}")


if __name__ == "__main__":
    main()
