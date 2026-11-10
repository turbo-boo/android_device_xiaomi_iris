/*
 * SPDX-FileCopyrightText: The LineageOS Project
 * SPDX-License-Identifier: Apache-2.0
 */

#include <aidl/android/hardware/power/BnPower.h>
#include <android-base/file.h>
#include <android-base/logging.h>
#include <unistd.h>

#define NVT_GESTURE_MODE_PATH "/proc/nvt_gesture_mode"

namespace aidl::google::hardware::power::impl::pixel {

using ::aidl::android::hardware::power::Mode;

bool isDeviceSpecificModeSupported(Mode type, bool* _aidl_return) {
    switch (type) {
        case Mode::DOUBLE_TAP_TO_WAKE:
            *_aidl_return = access(NVT_GESTURE_MODE_PATH, F_OK) == 0;
            return true;
        default:
            return false;
    }
}

bool setDeviceSpecificMode(Mode type, bool enabled) {
    switch (type) {
        case Mode::DOUBLE_TAP_TO_WAKE:
            // The Novatek driver enables the gesture on "5" and disables it on anything else
            if (!::android::base::WriteStringToFile(enabled ? "5" : "4", NVT_GESTURE_MODE_PATH)) {
                PLOG(ERROR) << "Failed to set double tap to wake to " << enabled;
            }
            return true;
        default:
            return false;
    }
}

}  // namespace aidl::google::hardware::power::impl::pixel
