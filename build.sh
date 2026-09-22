#!/usr/bin/env bash
set -euo pipefail

export PATH="$HOME/.local/opt/arm-gnu-toolchain-13.2.Rel1-x86_64-arm-none-eabi/bin:$PATH"
qmk compile -kb keychron/q3/ansi_encoder -km allen
./keyboards/keychron/q3/ansi_encoder/keymaps/allen/gen_readme.py
./keyboards/keychron/q3/ansi_encoder/keymaps/allen/gen_reference_html.py
