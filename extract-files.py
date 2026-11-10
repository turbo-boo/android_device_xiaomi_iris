#!/usr/bin/env -S PYTHONPATH=../../../tools/extract-utils python3
#
# SPDX-FileCopyrightText: 2026 The LineageOS Project
# SPDX-License-Identifier: Apache-2.0
#

from extract_utils.fixups_blob import (
    blob_fixup,
    blob_fixups_user_type,
)
from extract_utils.fixups_lib import (
    lib_fixups,
    lib_fixups_user_type,
)
from extract_utils.main import (
    ExtractUtils,
    ExtractUtilsModule,
)

namespace_imports = [
    'device/xiaomi/iris',
    'hardware/qcom-caf/common/libqti-perfd-client',
    'hardware/qcom-caf/sm8350',
    'hardware/qcom-caf/wlan',
    'hardware/qcom-caf/wlan/qcwcn',
    'hardware/xiaomi',
    'vendor/qcom/opensource/commonsys/display',
    'vendor/qcom/opensource/commonsys-intf/display',
    'vendor/qcom/opensource/dataservices',
    'vendor/qcom/opensource/display',
]


# The vendor copies of these libraries are installed next to a system_ext copy
# with the same file name, so their modules carry the _vendor suffix.
def lib_fixup_vendor_suffix(lib: str, partition: str, *args, **kwargs):
    return f'{lib}_vendor' if partition in ['odm', 'vendor'] else None


lib_fixups: lib_fixups_user_type = {
    **lib_fixups,
    (
        'com.qualcomm.qti.bluetooth_audio@1.0',
        'com.qualcomm.qti.dpm.api@1.0',
        'com.qualcomm.qti.imscmservice@2.0',
        'com.qualcomm.qti.imscmservice@2.1',
        'com.qualcomm.qti.imscmservice@2.2',
        'com.qualcomm.qti.uceservice@2.0',
        'com.qualcomm.qti.uceservice@2.1',
        'com.qualcomm.qti.uceservice@2.2',
        'com.qualcomm.qti.uceservice@2.3',
        'vendor.display.color@1.0',
        'vendor.display.color@1.1',
        'vendor.display.color@1.2',
        'vendor.display.color@1.3',
        'vendor.qti.data.factory@2.0',
        'vendor.qti.data.factory@2.1',
        'vendor.qti.data.factory@2.2',
        'vendor.qti.data.mwqem@1.0',
        'vendor.qti.data.slm@1.0',
        'vendor.qti.diaghal@1.0',
        'vendor.qti.hardware.alarm@1.0',
        'vendor.qti.hardware.cvp@1.0',
        'vendor.qti.hardware.data.cne.internal.api@1.0',
        'vendor.qti.hardware.data.cne.internal.constants@1.0',
        'vendor.qti.hardware.data.cne.internal.server@1.0',
        'vendor.qti.hardware.data.connection@1.0',
        'vendor.qti.hardware.data.connection@1.1',
        'vendor.qti.hardware.data.dynamicdds@1.0',
        'vendor.qti.hardware.data.iwlan@1.0',
        'vendor.qti.hardware.data.latency@1.0',
        'vendor.qti.hardware.data.qmi@1.0',
        'vendor.qti.hardware.qccvndhal@1.0',
        'vendor.qti.hardware.qseecom@1.0',
        'vendor.qti.hardware.qteeconnector@1.0',
        'vendor.qti.hardware.radio.am@1.0',
        'vendor.qti.hardware.radio.ims@1.0',
        'vendor.qti.hardware.radio.ims@1.1',
        'vendor.qti.hardware.radio.ims@1.2',
        'vendor.qti.hardware.radio.ims@1.3',
        'vendor.qti.hardware.radio.ims@1.4',
        'vendor.qti.hardware.radio.ims@1.5',
        'vendor.qti.hardware.radio.ims@1.6',
        'vendor.qti.hardware.radio.ims@1.7',
        'vendor.qti.hardware.radio.internal.deviceinfo@1.0',
        'vendor.qti.hardware.radio.lpa@1.0',
        'vendor.qti.hardware.radio.lpa@1.1',
        'vendor.qti.hardware.radio.qcrilhook@1.0',
        'vendor.qti.hardware.radio.qtiradio@1.0',
        'vendor.qti.hardware.radio.qtiradio@2.0',
        'vendor.qti.hardware.radio.qtiradio@2.1',
        'vendor.qti.hardware.radio.qtiradio@2.2',
        'vendor.qti.hardware.radio.qtiradio@2.3',
        'vendor.qti.hardware.radio.qtiradio@2.4',
        'vendor.qti.hardware.radio.qtiradio@2.5',
        'vendor.qti.hardware.radio.qtiradio@2.6',
        'vendor.qti.hardware.radio.uim@1.0',
        'vendor.qti.hardware.radio.uim@1.1',
        'vendor.qti.hardware.radio.uim@1.2',
        'vendor.qti.hardware.seccam@1.0',
        'vendor.qti.hardware.slmadapter@1.0',
        'vendor.qti.hardware.wifidisplaysession@1.0',
        'vendor.qti.ims.callcapability@1.0',
        'vendor.qti.ims.callinfo@1.0',
        'vendor.qti.ims.factory@1.0',
        'vendor.qti.ims.factory@1.1',
        'vendor.qti.ims.rcsconfig@1.0',
        'vendor.qti.ims.rcsconfig@1.1',
        'vendor.qti.ims.rcsconfig@2.0',
        'vendor.qti.ims.rcsconfig@2.1',
        'vendor.qti.imsrtpservice@3.0',
        'vendor.qti.latency@2.0',
    ): lib_fixup_vendor_suffix,
    ('libmmosal',): lib_fixup_vendor_suffix,
}

blob_fixups: blob_fixups_user_type = {
    # Stock points the FeliCa web plugin at Chrome, which this build does not
    # ship. The plugin passes the package to Intent.setPackage() with no
    # fallback, so point it at the bundled browser.
    'vendor/etc/felica/common.cfg': blob_fixup()
        .regex_replace('(?m)^00000003,.*$', '00000003,org.lineageos.jelly'),
    'vendor/etc/init/android.hardware.drm@1.3-service.widevine.rc': blob_fixup()
        .regex_replace('    start vendor.move_data_sh\n', '')
        .regex_replace('service vendor.move_data_sh /system/bin/move_widevine_data.sh\n    class late_start\n    user media\n    group media mediadrm system\n    disabled\n    oneshot\n', '')
        .regex_replace('writepid /dev/cpuset/foreground/tasks', 'task_profiles ProcessCapacityHigh'),
    'vendor/etc/init/android.hardware.neuralnetworks@1.3-service-qti.rc': blob_fixup()
        .regex_replace('writepid /dev/stune/nnapi-hal/tasks', 'task_profiles NNApiHALPerformance'),
    'vendor/etc/init/vendor.qti.media.c2@1.0-service.rc': blob_fixup()
        .regex_replace('writepid /dev/cpuset/foreground/tasks', 'task_profiles ProcessCapacityHigh'),
    'vendor/etc/libnfc-nci.conf': blob_fixup()
        .regex_replace('NFC_DEBUG_ENABLED=1', 'NFC_DEBUG_ENABLED=0'),
    # The stock values are route locations for the NQ NFC stack (0x01 = eSE).
    # The AOSP stack reads NFCEE IDs instead, and without DEFAULT_NFCF_ROUTE it
    # routes NFC-F to the host, so the FeliCa applet in the eSE never sees a reader.
    (
        'vendor/etc/libnfc-mtp-SN100.conf',
        'vendor/etc/libnfc-mtp-SN100_38_4MHZ.conf',
        'vendor/etc/libnfc-qrd-SN100.conf',
        'vendor/etc/libnfc-qrd-SN100_38_4MHZ.conf',
    ): blob_fixup()
        .regex_replace('(?m)^DEFAULT_ISODEP_ROUTE=.*$', 'DEFAULT_ISODEP_ROUTE=0xC0')
        .regex_replace('(?m)^DEFAULT_SYS_CODE_ROUTE=.*$', 'DEFAULT_SYS_CODE_ROUTE=0xC0')
        .regex_replace('(?m)^DEFAULT_SYS_CODE_PWR_STATE=.*$', 'DEFAULT_SYS_CODE_PWR_STATE=0x3B')
        .regex_replace('(?m)^DEFAULT_OFFHOST_ROUTE=.*$', 'DEFAULT_OFFHOST_ROUTE=0xC0\n\n# NFC-F (FeliCa) route\nDEFAULT_NFCF_ROUTE=0xC0')
        .regex_replace('(?m)^OFFHOST_ROUTE_ESE=.*$', 'OFFHOST_ROUTE_ESE={C0}'),
    ('vendor/etc/media_codecs.xml',): blob_fixup()
        .regex_replace('\n    <Include href="media_codecs_google_audio.xml" />', '')
        .regex_replace('\n    <Include href="media_codecs_vendor_audio.xml" />', '')
        .regex_replace('\n    <Include href="media_codecs_google_telephony.xml" />', '')
        .regex_replace('\n    <Include href="media_codecs_c2_audio.xml" />', '')
        .regex_replace('\n    <Include href="media_codecs_google_c2.xml" />', '')
        .regex_replace('\n        <Setting name="max-video-encoder-input-buffers" value="11" />', '\n        <Domain name="telephony" enabled="true" />\n        <Setting name="max-video-encoder-input-buffers" value="11" />'),
    'vendor/bin/hw/android.hardware.lights-service.qti': blob_fixup()
        .replace_needed('android.hardware.light-V1-ndk_platform.so', 'android.hardware.light-V1-ndk.so'),
    (
        'vendor/lib/libdpps.so',
        'vendor/lib/libpowercallback.so',
        'vendor/lib/libpowercore.so',
        'vendor/lib/libsnapdragoncolor-manager.so',
        'vendor/lib/libvideooptfeature.so',
        'vendor/lib64/libdpps.so',
        'vendor/lib64/libpowercallback.so',
        'vendor/lib64/libpowercore.so',
        'vendor/lib64/libsnapdragoncolor-manager.so',
        'vendor/lib64/libvideooptfeature.so',
    ): blob_fixup()
        .replace_needed('libtinyxml2.so', 'libtinyxml2-v34.so'),
    (
        'vendor/lib/libboot_control_qti.so',
        'vendor/lib/nfc_nci.nqx.default.hw.so',
        'vendor/lib64/libboot_control_qti.so',
        'vendor/lib64/nfc_nci.nqx.default.hw.so',
    ): blob_fixup()
        .add_needed('libbase_shim.so'),
    (
        'vendor/lib/mediadrm/libwvdrmengine.so',
        'vendor/lib64/libwvhidl.so',
        'vendor/lib64/mediadrm/libwvdrmengine.so',
    ): blob_fixup()
        .add_needed('libcrypto_shim.so'),
    'vendor/lib64/camera/components/com.qti.node.mialgocontrol.so': blob_fixup()
        .strip_debug_sections()
        .add_needed('libpiex_shim.so'),
    (
        'vendor/lib/libalLDC.so',
        'vendor/lib/libalhLDC.so',
        'vendor/lib64/libalLDC.so',
        'vendor/lib64/libalhLDC.so',
    ): blob_fixup()
        .clear_symbol_version('AHardwareBuffer_allocate')
        .clear_symbol_version('AHardwareBuffer_describe')
        .clear_symbol_version('AHardwareBuffer_lock')
        .clear_symbol_version('AHardwareBuffer_release')
        .clear_symbol_version('AHardwareBuffer_unlock'),
    (
        'vendor/lib/libc++_shared_vf.so',
        'vendor/lib64/libc++_shared_vf.so',
    ): blob_fixup()
        .fix_soname(),
    'vendor/lib/libmmcamera_faceproc.so': blob_fixup()
        .clear_symbol_version('__aeabi_memcpy')
        .clear_symbol_version('__aeabi_memset')
        .clear_symbol_version('__gnu_Unwind_Find_exidx'),
}  # fmt: skip

module = ExtractUtilsModule(
    'iris',
    'xiaomi',
    blob_fixups=blob_fixups,
    lib_fixups=lib_fixups,
    namespace_imports=namespace_imports,
)

if __name__ == '__main__':
    utils = ExtractUtils.device(module)
    utils.run()
