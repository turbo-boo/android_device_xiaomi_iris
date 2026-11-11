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

- [rabin-tech/device_xiaomi_iris](https://github.com/rabin-tech/device_xiaomi_iris): the original tree, kept in the history.
- LineageOS trees: [oneplus/dre](https://github.com/LineageOS/android_device_oneplus_dre),
  [oneplus/sm6375-common](https://github.com/LineageOS/android_device_oneplus_sm6375-common),
  [motorola/sm6375-common](https://github.com/LineageOS/android_device_motorola_sm6375-common),
  [xiaomi/sm8350-common](https://github.com/LineageOS/android_device_xiaomi_sm8350-common),
  [xiaomi/lisa](https://github.com/LineageOS/android_device_xiaomi_lisa).
- [Karan-Frost/device_xiaomi_veux](https://github.com/Karan-Frost/device_xiaomi_veux): LiveDisplay setup.
- FeliCa: [reindex-ot/magisk-module-iris-felica](https://github.com/reindex-ot/magisk-module-iris-felica),
  [felica-droid/android_device_xiaomi_renoir](https://github.com/felica-droid/android_device_xiaomi_renoir).
- [xbill9](https://github.com/xbill9): Connectivity and zygote patches.
