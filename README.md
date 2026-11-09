# Device tree for Redmi Note 10 JE (iris / XIG02)

LineageOS 24.0 (Android 17) device configuration for the
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
| `patches/packages_modules_Connectivity/` | [xbill9/android_packages_modules_Connectivity@5c298de](https://github.com/xbill9/android_packages_modules_Connectivity/commit/5c298deab55ce7cfefec3b1cc9c79e9898f669e7) | xbill9 |
| `patches/system_zygote/` | [xbill9/android_system_zygote@d6dadb5](https://github.com/xbill9/android_system_zygote/commit/d6dadb5e56c821e8dd44b13725d9de6e3085c733) | xbill9 |

Files that are identical to the stock MIUI V14.0.26.0.TKRJPKD firmware (Qualcomm
init scripts, media profiles and codecs, WCNSS config, task profiles, ...) come
from that firmware.
