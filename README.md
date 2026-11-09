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
shipped from [`device/xiaomi/iris-kernel`](https://github.com/turbo-boo/android_device_xiaomi_iris-kernel).
`kernel/oneplus/sm4350` (same SoC, msm-5.4) is only used to generate the UAPI
headers needed by the `hardware/qcom-caf` HALs; it is not compiled.

The stock kernel is built without `CONFIG_USERFAULTFD`, so the userfaultfd GC
is disabled.

## Source patches

Android 17 expects a 5.10+ kernel, so a few projects are patched to run on the
stock 5.4 kernel. The patches are `git format-patch` files under
`patches/<project>/`, where `<project>` is the project path with `/` replaced
by `_`:

| Project | Patch | Author |
| :------ | :---- | :----- |
| `bionic` | Revert of [bf8fc35](https://github.com/LineageOS/android_bionic/commit/bf8fc35b7e165d2f12d5a854640bc6808ab81225) (`posix_spawn()` without `close_range()`, for clatd and dnsmasq) | turbo-boo |
| `packages/modules/Connectivity` | [5c298de](https://github.com/xbill9/android_packages_modules_Connectivity/commit/5c298deab55ce7cfefec3b1cc9c79e9898f669e7) (NetBpfLoad, netd BPF programs and ConnectivityService below 5.10) | xbill9 |
| `system/bpf` | Skip the ring buffer test program below 5.10 | turbo-boo |
| `system/zygote` | [d6dadb5](https://github.com/xbill9/android_system_zygote/commit/d6dadb5e56c821e8dd44b13725d9de6e3085c733) (skip capabilities the kernel does not know) | xbill9 |

`source build/envsetup.sh` runs `vendorsetup.sh`, which applies them with
`patches/apply-patches.sh` on top of each project's manifest revision. Projects
that already contain the patches are left alone, as are projects with other
local changes, which are reported instead. `repo sync` drops the applied
commits; the next `source build/envsetup.sh` applies them again.

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

## Credits

This tree started from [rabin-tech/device_xiaomi_iris](https://github.com/rabin-tech/device_xiaomi_iris)
(initial device tree by rabin-tech, mialgocontrol size fix by Jabiyeff); those
commits are kept in the history.

The LineageOS 23.2 rewrite took the following files from other trees. Their full
history and authors are in the linked repositories.

| File(s) in this tree | Taken from | Authors |
| :------------------- | :--------- | :------ |
| `configs/powerhint.json` | [LineageOS/android_device_oneplus_dre](https://github.com/LineageOS/android_device_oneplus_dre) `configs/powerhint.json` | Vivekachooz, Nick Reuter, DennySPB, karthick111, Sugakesshaa, Subhajeet Muhuri and others |
| `rootdir/etc/fstab.qcom` | oneplus/dre `init/fstab.qcom` | Albert Tang, Alexander Koskovich, LuK1337, Randall Huang |
| `audio/audio_policy_configuration.xml` | oneplus/dre `configs/audio/audio_policy_configuration.xml` | LuK1337, Albert Tang, chandu078 and the CodeAurora authors (Zhou Song, Sujin Panicker, Meng Wang, ...) |
| `overlay/FrameworkOverlayIris/res/xml/power_profile.xml` (layout) | oneplus/dre `overlay/OPlusFrameworksResTarget/res/xml/power_profile.xml` | Albert Tang, Georg Veichtlbauer |
| `BoardConfig.mk`, `device.mk`, `config.fs`, `lineage.dependencies` (structure) | oneplus/dre | LuK1337, Bruno Martins, Albert Tang, Alexander Koskovich, Luca Stefani, Michael Bestas and others |
| `rootdir/etc/init.qcom.rc` | [LineageOS/android_device_oneplus_sm6375-common](https://github.com/LineageOS/android_device_oneplus_sm6375-common) `init/init.qcom.rc` | Vivekachooz, Alexander Koskovich, dianlujitao and others |
| `configs/qti_whitelist.xml`, `configs/telephony_system-ext_privapp-permissions-qti.xml` | [LineageOS/android_device_xiaomi_sm8350-common](https://github.com/LineageOS/android_device_xiaomi_sm8350-common) | Arian |
| `rootdir/bin/vendor_modprobe.sh`, `sepolicy/vendor/mi_thermald.te` | xiaomi/sm8350-common | Cosmin Tanislav |
| RRO boilerplate (`overlay/*/Android.bp`, `AndroidManifest.xml`) | [LineageOS/android_device_xiaomi_lisa](https://github.com/LineageOS/android_device_xiaomi_lisa), oneplus/sm6375-common, [LineageOS/android_device_motorola_sm6375-common](https://github.com/LineageOS/android_device_motorola_sm6375-common) | maintainers of those trees |
| `ro.product.cert` in `product.prop`, FeliCa app and config list | [reindex-ot/magisk-module-iris-felica](https://github.com/reindex-ot/magisk-module-iris-felica) | Re\*Index.(ot_inc) |
| NFC off-host routes for FeliCa (`extract-files.py`) | [felica-droid/android_device_xiaomi_renoir](https://github.com/felica-droid/android_device_xiaomi_renoir/commit/57845480c2ec806e1a98d014e65170738ba25dae) | Maitani-Sakura |

Files that are identical to the stock MIUI V14.0.26.0.TKRJPKD firmware (Qualcomm
init scripts, media profiles and codecs, WCNSS config, task profiles, ...) come
from that firmware.
