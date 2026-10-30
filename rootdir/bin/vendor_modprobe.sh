#! /vendor/bin/sh
#=============================================================================
# Copyright (c) 2019-2020 Qualcomm Technologies, Inc.
# All Rights Reserved.
# Confidential and Proprietary - Qualcomm Technologies, Inc.
#=============================================================================

MODULES_PATH="/vendor/lib/modules/"

MODPROBE="/vendor/bin/modprobe"
MODULES=`${MODPROBE} -d ${MODULES_PATH} -l`

# Iterate over module list and modprobe them in the background.
# Only the perf kernel modules shipped in /vendor/lib/modules are used; the
# 5.4-gki variant present in the stock dump is not part of this build.
for MODULE in ${MODULES}; do
	${MODPROBE} -a -b -d ${MODULES_PATH} ${MODULE} &
done

# Wait until all the modprobes are finished
wait
