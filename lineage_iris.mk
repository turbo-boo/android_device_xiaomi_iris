#
# SPDX-FileCopyrightText: The LineageOS Project
# SPDX-License-Identifier: Apache-2.0
#

# Must precede the inherits below (default_art_config.mk sets it to true).
PRODUCT_ENABLE_UFFD_GC := false

# Inherit from those products. Most specific first.
$(call inherit-product, $(SRC_TARGET_DIR)/product/core_64_bit.mk)
TARGET_SUPPORTS_OMX_SERVICE := false
$(call inherit-product, $(SRC_TARGET_DIR)/product/full_base_telephony.mk)

# Inherit from iris device
$(call inherit-product, device/xiaomi/iris/device.mk)

# Inherit some common Lineage stuff.
$(call inherit-product, vendor/lineage/config/common_full_phone.mk)

# Mobile FeliCa checks ro.product.model, so keep the stock KDDI SKU identity.
PRODUCT_NAME := lineage_iris
PRODUCT_DEVICE := iris
PRODUCT_MANUFACTURER := Xiaomi
PRODUCT_BRAND := Redmi
PRODUCT_MODEL := XIG02

PRODUCT_GMS_CLIENTID_BASE := android-xiaomi

PRODUCT_BUILD_PROP_OVERRIDES += \
    BuildDesc="XIG02_jp_kdi-user 13 TKQ1.220905.001 V14.0.26.0.TKRJPKD release-keys" \
    BuildFingerprint=Redmi/XIG02_jp_kdi/XIG02:13/TKQ1.220905.001/V14.0.26.0.TKRJPKD:user/release-keys \
    DeviceName=XIG02 \
    DeviceProduct=XIG02_jp_kdi \
    SystemDevice=XIG02 \
    SystemName=XIG02_jp_kdi
