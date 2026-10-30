/*
 * SPDX-FileCopyrightText: The LineageOS Project
 * SPDX-License-Identifier: Apache-2.0
 */

#include <aidl/android/hardware/power/BnPower.h>
#include <android-base/logging.h>
#include <android-base/unique_fd.h>
#include <fcntl.h>
#include <sys/ioctl.h>

// From drivers/input/touchscreen/xiaomi/xiaomi_touch.h: both touch drivers of iris (Novatek and
// FocalTech) register their wakeup gesture with xiaomi_touch, which exposes the mode ioctl.
#define TOUCH_DEV_PATH "/dev/xiaomi-touch"
#define TOUCH_ID 0
#define TOUCH_MAGIC 0x5400
#define SET_CUR_VALUE 0
#define TOUCH_IOC_SETMODE (TOUCH_MAGIC + SET_CUR_VALUE)
#define Touch_Doubletap_Mode 14

namespace aidl::google::hardware::power::impl::pixel {

using ::aidl::android::hardware::power::Mode;

bool isDeviceSpecificModeSupported(Mode type, bool* _aidl_return) {
    switch (type) {
        case Mode::DOUBLE_TAP_TO_WAKE:
            *_aidl_return = true;
            return true;
        default:
            return false;
    }
}

bool setDeviceSpecificMode(Mode type, bool enabled) {
    switch (type) {
        case Mode::DOUBLE_TAP_TO_WAKE: {
            ::android::base::unique_fd fd(
                    TEMP_FAILURE_RETRY(open(TOUCH_DEV_PATH, O_RDWR | O_CLOEXEC)));
            if (fd < 0) {
                PLOG(ERROR) << "Failed to open " << TOUCH_DEV_PATH;
                return true;
            }
            int arg[3] = {TOUCH_ID, Touch_Doubletap_Mode, enabled ? 1 : 0};
            if (ioctl(fd.get(), TOUCH_IOC_SETMODE, &arg) < 0) {
                PLOG(ERROR) << "Failed to set double tap to wake to " << enabled;
            }
            return true;
        }
        default:
            return false;
    }
}

}  // namespace aidl::google::hardware::power::impl::pixel
