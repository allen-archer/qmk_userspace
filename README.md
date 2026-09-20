# qmk_userspace

Personal QMK keymaps, built against upstream [qmk_firmware](https://github.com/qmk/qmk_firmware) via [QMK's external userspace feature](https://docs.qmk.fm/newbs_external_userspace).

## Keyboards

- `keychron/q3/ansi_encoder` — keymap `allen`

## Build / flash

```
qmk config user.overlay_dir="$(pwd)"
./build.sh
./flash.sh
```

## License

[Unlicense](UNLICENSE) — public domain, do whatever you want with it.
