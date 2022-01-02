#############################################################################
##
## Copyright (C) 2021 The Qt Company Ltd.
## Contact: https://www.qt.io/licensing/
##
## This file is part of Qt for Python.
##
## $QT_BEGIN_LICENSE:LGPL$
## Commercial License Usage
## Licensees holding valid commercial Qt licenses may use this file in
## accordance with the commercial license agreement provided with the
## Software or, alternatively, in accordance with the terms contained in
## a written agreement between you and The Qt Company. For licensing terms
## and conditions see https://www.qt.io/terms-conditions. For further
## information use the contact form at https://www.qt.io/contact-us.
##
## GNU Lesser General Public License Usage
## Alternatively, this file may be used under the terms of the GNU Lesser
## General Public License version 3 as published by the Free Software
## Foundation and appearing in the file LICENSE.LGPL3 included in the
## packaging of this file. Please review the following information to
## ensure the GNU Lesser General Public License version 3 requirements
## will be met: https://www.gnu.org/licenses/lgpl-3.0.html.
##
## GNU General Public License Usage
## Alternatively, this file may be used under the terms of the GNU
## General Public License version 2.0 or (at your option) the GNU General
## Public license version 3 or any later version approved by the KDE Free
## Qt Foundation. The licenses are as published by the Free Software
## Foundation and appearing in the file LICENSE.GPL2 and LICENSE.GPL3
## included in the packaging of this file. Please review the following
## information to ensure the GNU General Public License requirements will
## be met: https://www.gnu.org/licenses/gpl-2.0.html and
## https://www.gnu.org/licenses/gpl-3.0.html.
##
## $QT_END_LICENSE$
##
#############################################################################
"""
This file contains the exact signatures for all functions in module
PySide6.QtConcurrent, except for defaults which are replaced by "...".
"""

# Module `PySide6.QtConcurrent`

from shiboken6 import Shiboken

from enum import Enum
from typing import Optional, overload

import PySide6.QtCore
import PySide6.QtConcurrent


class QFutureQString(Shiboken.Object):

    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, QFutureQString:PySide6.QtConcurrent.QFutureQString) -> None: ...

    @staticmethod
    def __copy__() -> None: ...
    def cancel(self) -> None: ...
    def isCanceled(self) -> bool: ...
    def isFinished(self) -> bool: ...
    def isPaused(self) -> bool: ...
    def isRunning(self) -> bool: ...
    def isStarted(self) -> bool: ...
    def isSuspended(self) -> bool: ...
    def isSuspending(self) -> bool: ...
    def isValid(self) -> bool: ...
    def pause(self) -> None: ...
    def progressMaximum(self) -> int: ...
    def progressMinimum(self) -> int: ...
    def progressText(self) -> str: ...
    def progressValue(self) -> int: ...
    def resultCount(self) -> int: ...
    def resume(self) -> None: ...
    def setPaused(self, paused:bool) -> None: ...
    def setSuspended(self, suspend:bool) -> None: ...
    def suspend(self) -> None: ...
    def togglePaused(self) -> None: ...
    def toggleSuspended(self) -> None: ...
    def waitForFinished(self) -> None: ...


class QFutureVoid(Shiboken.Object):

    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, QFutureVoid:PySide6.QtConcurrent.QFutureVoid) -> None: ...

    @staticmethod
    def __copy__() -> None: ...
    def cancel(self) -> None: ...
    def isCanceled(self) -> bool: ...
    def isFinished(self) -> bool: ...
    def isPaused(self) -> bool: ...
    def isRunning(self) -> bool: ...
    def isStarted(self) -> bool: ...
    def isSuspended(self) -> bool: ...
    def isSuspending(self) -> bool: ...
    def isValid(self) -> bool: ...
    def pause(self) -> None: ...
    def progressMaximum(self) -> int: ...
    def progressMinimum(self) -> int: ...
    def progressText(self) -> str: ...
    def progressValue(self) -> int: ...
    def resultCount(self) -> int: ...
    def resume(self) -> None: ...
    def setPaused(self, paused:bool) -> None: ...
    def setSuspended(self, suspend:bool) -> None: ...
    def suspend(self) -> None: ...
    def togglePaused(self) -> None: ...
    def toggleSuspended(self) -> None: ...
    def waitForFinished(self) -> None: ...


class QFutureWatcherQString(PySide6.QtCore.QObject):

    def __init__(self, _parent:Optional[PySide6.QtCore.QObject]=...) -> None: ...

    def future(self) -> PySide6.QtConcurrent.QFutureQString: ...
    def setFuture(self, future:PySide6.QtConcurrent.QFutureQString) -> None: ...


class QFutureWatcherVoid(PySide6.QtCore.QObject):

    def __init__(self, _parent:Optional[PySide6.QtCore.QObject]=...) -> None: ...


class QtConcurrent(Shiboken.Object):

    UnorderedReduce          : QtConcurrent.ReduceOption = ... # 0x1
    OrderedReduce            : QtConcurrent.ReduceOption = ... # 0x2
    SequentialReduce         : QtConcurrent.ReduceOption = ... # 0x4
    ThrottleThread           : QtConcurrent.ThreadFunctionResult = ... # 0x0
    ThreadFinished           : QtConcurrent.ThreadFunctionResult = ... # 0x1

    class ReduceOption(Enum):

        UnorderedReduce          : QtConcurrent.ReduceOption = ... # 0x1
        OrderedReduce            : QtConcurrent.ReduceOption = ... # 0x2
        SequentialReduce         : QtConcurrent.ReduceOption = ... # 0x4

    class ReduceOptions(object): ...

    class ThreadFunctionResult(Enum):

        ThrottleThread           : QtConcurrent.ThreadFunctionResult = ... # 0x0
        ThreadFinished           : QtConcurrent.ThreadFunctionResult = ... # 0x1


# eof
