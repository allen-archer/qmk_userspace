# Keymap: `allen` — Keychron Q3 (ANSI, encoder)

The keymap defines four layers, but only **WIN_BASE** and **WIN_FN** are used day to day — the board is always left in Windows mode. **MAC_BASE**/**MAC_FN** are kept only as unused legacy layers; they're never switched into, since there's no keycode in this keymap that activates them.

This file is generated — run `./gen_readme.py` after editing `keymap.c` to refresh it.

## Layer activation

| Layer | How to reach it |
|---|---|
| `WIN_BASE` | Default layer, always active unless Fn is held |
| `WIN_FN` | Hold the bottom-right **Fn** key (momentary — release to return to `WIN_BASE`) |

## WIN_BASE (default)

```
KC_ESC               KC_F1                KC_F2                KC_F3                KC_F4                KC_F5                KC_F6                KC_F7                KC_F8                KC_F9                KC_F10               KC_F11               KC_F12               KC_MPLY              KC_PSCR              KC_MUTE              KC_F
KC_GRV               KC_1                 KC_2                 KC_3                 KC_4                 KC_5                 KC_6                 KC_7                 KC_8                 KC_9                 KC_0                 KC_MINS              KC_EQL               KC_BSPC              KC_INS               KC_HOME              KC_PGUP
KC_TAB               KC_Q                 KC_W                 KC_E                 KC_R                 KC_T                 KC_Y                 KC_U                 KC_I                 KC_O                 KC_P                 KC_LBRC              KC_RBRC              KC_BSLS              KC_DEL               KC_END               KC_PGDN
LT(WIN_FN, KC_CAPS)  KC_A                 KC_S                 KC_D                 KC_F                 KC_G                 KC_H                 KC_J                 KC_K                 KC_L                 KC_SCLN              KC_QUOT              KC_ENT
KC_LSFT              KC_Z                 KC_X                 KC_C                 KC_V                 KC_B                 KC_N                 KC_M                 KC_COMM              KC_DOT               KC_SLSH              KC_RSFT              KC_UP
KC_LCTL              KC_LWIN              KC_LALT              KC_SPC               KC_RALT              KC_RWIN              MO(WIN_FN)           KC_RCTL              KC_LEFT              KC_DOWN              KC_RGHT
```

Standard QWERTY layout. The only non-obvious key is **Fn** (bottom row) — a momentary hold that activates the Fn layer below.

**Rotary encoder:** Volume Down / Volume Up.

## WIN_FN (Fn held)

```
QK_BOOT           KC_BRID           KC_BRIU           LCTL(LALT(KC_M))  LCTL(KC_F9)       RM_VALD           RM_VALU           KC_MPRV           KC_MPLY           KC_MNXT           KC_MUTE           KC_VOLD           KC_VOLU           RM_TOGG           _______           _______           _______
_______           _______           _______           _______           _______           _______           _______           _______           _______           _______           _______           _______           _______           KC_BSPC           DM_REC1           DM_PLY1           MS_WHLU
RM_TOGG           RM_NEXT           RM_VALU           RM_HUEU           RM_SATU           RM_SPDU           DM_REC1           DM_PLY1           _______           _______           _______           _______           _______           _______           DM_REC2           DM_PLY2           MS_WHLD
_______           RM_PREV           RM_VALD           RM_HUED           RM_SATD           RM_SPDD           _______           _______           _______           _______           _______           _______           KC_ENT
_______           _______           _______           CW_TOGG           _______           _______           _______           _______           _______           _______           _______           _______           _______
_______           _______           _______           _______           _______           _______           _______           _______           _______           _______           _______
```

Everything not listed below is transparent (`_______`) — it falls through and behaves exactly like `WIN_BASE`.

| Key | Sends | Effect |
|---|---|---|
| Fn+Esc | `QK_BOOT` | Bootloader |
| Fn+F1 | `KC_BRID` | Brightness Down |
| Fn+F2 | `KC_BRIU` | Brightness Up |
| Fn+F3 | `LCTL(LALT(KC_M))` | Sends Ctrl+Alt+M |
| Fn+F4 | `LCTL(KC_F9)` | Sends Ctrl+F9 |
| Fn+F5 | `RM_VALD` | RGB Matrix Value Down |
| Fn+F6 | `RM_VALU` | RGB Matrix Value Up |
| Fn+F7 | `KC_MPRV` | Previous |
| Fn+F8 | `KC_MPLY` | Play/Pause Track |
| Fn+F9 | `KC_MNXT` | Next |
| Fn+F10 | `KC_MUTE` | Mute |
| Fn+F11 | `KC_VOLD` | Volume Down |
| Fn+F12 | `KC_VOLU` | Volume Up |
| Fn+Mute (2) | `RM_TOGG` | RGB Matrix Toggle |
| Fn+Backspace | `KC_BSPC` | Backspace |
| Fn+Insert | `DM_REC1` | Dynamic Macro Record Start 1 |
| Fn+Home | `DM_PLY1` | Dynamic Macro Play 1 |
| Fn+PgUp | `MS_WHLU` | Mouse wheel up |
| Fn+Tab | `RM_TOGG` | RGB Matrix Toggle |
| Fn+Q | `RM_NEXT` | RGB Matrix Mode Next |
| Fn+W | `RM_VALU` | RGB Matrix Value Up |
| Fn+E | `RM_HUEU` | RGB Matrix Hue Up |
| Fn+R | `RM_SATU` | RGB Matrix Saturation Up |
| Fn+T | `RM_SPDU` | RGB Matrix Speed Up |
| Fn+Y | `DM_REC1` | Dynamic Macro Record Start 1 |
| Fn+U | `DM_PLY1` | Dynamic Macro Play 1 |
| Fn+Delete | `DM_REC2` | Dynamic Macro Record Start 2 |
| Fn+End | `DM_PLY2` | Dynamic Macro Play 2 |
| Fn+PgDn | `MS_WHLD` | Mouse wheel down |
| Fn+A | `RM_PREV` | RGB Matrix Mode Previous |
| Fn+S | `RM_VALD` | RGB Matrix Value Down |
| Fn+D | `RM_HUED` | RGB Matrix Hue Down |
| Fn+F | `RM_SATD` | RGB Matrix Saturation Down |
| Fn+G | `RM_SPDD` | RGB Matrix Speed Down |
| Fn+Enter | `KC_ENT` | Enter |
| Fn+C | `CW_TOGG` | Caps Word Toggle |

**Rotary encoder (while Fn held):** keyboard RGB brightness down / up.
