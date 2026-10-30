# Device tree for Redmi Note 10 JE (iris / XIG02)

LineageOS 23.2 / crDroid 16.0 (Android 16 QPR2) device configuration for the
au (KDDI) Redmi Note 10 JE, `XIG02`, codename `iris`.

| Basic                   | Spec Sheet                                         |
| ----------------------: | :------------------------------------------------- |
| SoC                     | Qualcomm SM4350 Snapdragon 480 5G (`holi`)         |
| CPU                     | 2x 2.0 GHz Cortex-A76 + 6x 1.8 GHz Cortex-A55      |
| GPU                     | Adreno 619                                         |
| Memory                  | 4 GB                                               |
| Shipped Android version | 11 (MIUI 12.5), last update MIUI 14 V14.0.26.0     |
| Storage                 | 64 GB                                              |
| Display                 | 6.5" 1080 x 2400, 90 Hz                            |
| Fingerprint             | Side-mounted (FPC)                                 |
| NFC                     | NXP SN100 with eSE (Osaifu-Keitai / Mobile FeliCa) |

## Requirements

- Stock firmware **MIUI V14.0.26.0.TKRJPKD** must be installed before flashing.
  The vendor blobs, the prebuilt kernel and the kernel modules are all taken from
  that release, and the security patch level is pinned to its 2024-08-01 so that
  keymaster keeps working.
- Proprietary files are extracted from a dump of the same release:

  ```bash
  ./extract-files.py /path/to/V14.0.26.0.TKRJPKD-dump
  ```

## Kernel

Xiaomi has not published the iris kernel source. The stock
`5.4.259-perf` kernel, its DTBs, DTBO and the 40 vendor modules it loads are
shipped from `prebuilts/`. `kernel/oneplus/sm4350` (same SoC, msm-5.4) is only
used to generate the UAPI headers needed by the `hardware/qcom-caf` HALs; it
is not compiled.

The stock kernel is built without `CONFIG_USERFAULTFD`, so the userfaultfd GC
is disabled.

## FeliCa

Mobile FeliCa works through the eSE of the SN100 using the stock NXP NFC HAL
and the stock QTI secure element HAL (`eSE1`) over OMAPI. The Mobile FeliCa
apps and `/vendor/etc/felica/*.cfg` come from the stock firmware, and the
product model is kept as `XIG02` because the apps check it.

## Status

The tree has only been checked statically (makefile/blob/VINTF/sepolicy
consistency); it has not been built or booted yet. Items that need a device:

- The stock 5.4 kernel has not been run under Android 16.
- The side fingerprint sensor position is not reported to the framework yet.
  Measure the power button and set
  `persist.vendor.fingerprint.sensor_location=<x>|<y>|<radius>` in `vendor.prop`
  (y is the top edge of the sensor in pixels, the sensor length is 2 * radius).
- `power_profile.xml` and the powerhint frequency values are taken from the stock
  firmware and from `oneplus/dre` (same SoC); they are not measured on iris.
- Recovery does not mount `/vendor/firmware_mnt`, as on stock.
- Double tap to wake goes through the power HAL (`power/PowerModeExtension.cpp`)
  to the xiaomi_touch mode ioctl on `/dev/xiaomi-touch`. The mode number (14) is
  the common `xiaomi_touch.h` value; it has not been confirmed on either iris
  touch panel (Novatek or FocalTech).
