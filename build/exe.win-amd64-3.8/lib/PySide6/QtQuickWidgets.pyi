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
PySide6.QtQuickWidgets, except for defaults which are replaced by "...".
"""

# Module `PySide6.QtQuickWidgets`

from shiboken6 import Shiboken

from enum import Enum
from typing import Any, Optional, Union, List, overload

import PySide6.QtCore
import PySide6.QtGui
import PySide6.QtWidgets
import PySide6.QtQml
import PySide6.QtQuick
import PySide6.QtQuickWidgets


class QQuickWidget(PySide6.QtWidgets.QWidget):

    SizeViewToRootObject     : QQuickWidget.ResizeMode = ... # 0x0
    SizeRootObjectToView     : QQuickWidget.ResizeMode = ... # 0x1
    Null                     : QQuickWidget.Status = ... # 0x0
    Ready                    : QQuickWidget.Status = ... # 0x1
    Loading                  : QQuickWidget.Status = ... # 0x2
    Error                    : QQuickWidget.Status = ... # 0x3

    class ResizeMode(Enum):

        SizeViewToRootObject     : QQuickWidget.ResizeMode = ... # 0x0
        SizeRootObjectToView     : QQuickWidget.ResizeMode = ... # 0x1

    class Status(Enum):

        Null                     : QQuickWidget.Status = ... # 0x0
        Ready                    : QQuickWidget.Status = ... # 0x1
        Loading                  : QQuickWidget.Status = ... # 0x2
        Error                    : QQuickWidget.Status = ... # 0x3


    @overload
    def __init__(self, engine:PySide6.QtQml.QQmlEngine, parent:PySide6.QtWidgets.QWidget) -> None: ...
    @overload
    def __init__(self, parent:Optional[PySide6.QtWidgets.QWidget]=...) -> None: ...
    @overload
    def __init__(self, source:Union[PySide6.QtCore.QUrl, str], parent:Optional[PySide6.QtWidgets.QWidget]=...) -> None: ...

    def dragEnterEvent(self, arg__1:PySide6.QtGui.QDragEnterEvent) -> None: ...
    def dragLeaveEvent(self, arg__1:PySide6.QtGui.QDragLeaveEvent) -> None: ...
    def dragMoveEvent(self, arg__1:PySide6.QtGui.QDragMoveEvent) -> None: ...
    def dropEvent(self, arg__1:PySide6.QtGui.QDropEvent) -> None: ...
    def engine(self) -> PySide6.QtQml.QQmlEngine: ...
    def errors(self) -> List[PySide6.QtQml.QQmlError]: ...
    def event(self, arg__1:PySide6.QtCore.QEvent) -> bool: ...
    def focusInEvent(self, event:PySide6.QtGui.QFocusEvent) -> None: ...
    def focusNextPrevChild(self, next:bool) -> bool: ...
    def focusOutEvent(self, event:PySide6.QtGui.QFocusEvent) -> None: ...
    def format(self) -> PySide6.QtGui.QSurfaceFormat: ...
    def grabFramebuffer(self) -> PySide6.QtGui.QImage: ...
    def hideEvent(self, arg__1:PySide6.QtGui.QHideEvent) -> None: ...
    def initialSize(self) -> PySide6.QtCore.QSize: ...
    def keyPressEvent(self, arg__1:PySide6.QtGui.QKeyEvent) -> None: ...
    def keyReleaseEvent(self, arg__1:PySide6.QtGui.QKeyEvent) -> None: ...
    def mouseDoubleClickEvent(self, arg__1:PySide6.QtGui.QMouseEvent) -> None: ...
    def mouseMoveEvent(self, arg__1:PySide6.QtGui.QMouseEvent) -> None: ...
    def mousePressEvent(self, arg__1:PySide6.QtGui.QMouseEvent) -> None: ...
    def mouseReleaseEvent(self, arg__1:PySide6.QtGui.QMouseEvent) -> None: ...
    def paintEvent(self, event:PySide6.QtGui.QPaintEvent) -> None: ...
    def quickWindow(self) -> PySide6.QtQuick.QQuickWindow: ...
    def resizeEvent(self, arg__1:PySide6.QtGui.QResizeEvent) -> None: ...
    def resizeMode(self) -> PySide6.QtQuickWidgets.QQuickWidget.ResizeMode: ...
    def rootContext(self) -> PySide6.QtQml.QQmlContext: ...
    def rootObject(self) -> PySide6.QtQuick.QQuickItem: ...
    def setClearColor(self, color:Union[PySide6.QtGui.QColor, PySide6.QtGui.QRgba64, Any, PySide6.QtCore.Qt.GlobalColor, str, int]) -> None: ...
    def setContent(self, url:Union[PySide6.QtCore.QUrl, str], component:PySide6.QtQml.QQmlComponent, item:PySide6.QtCore.QObject) -> None: ...
    def setFormat(self, format:Union[PySide6.QtGui.QSurfaceFormat, PySide6.QtGui.QSurfaceFormat.FormatOptions]) -> None: ...
    def setResizeMode(self, arg__1:PySide6.QtQuickWidgets.QQuickWidget.ResizeMode) -> None: ...
    def setSource(self, arg__1:Union[PySide6.QtCore.QUrl, str]) -> None: ...
    def showEvent(self, arg__1:PySide6.QtGui.QShowEvent) -> None: ...
    def sizeHint(self) -> PySide6.QtCore.QSize: ...
    def source(self) -> PySide6.QtCore.QUrl: ...
    def status(self) -> PySide6.QtQuickWidgets.QQuickWidget.Status: ...
    def timerEvent(self, arg__1:PySide6.QtCore.QTimerEvent) -> None: ...
    def wheelEvent(self, arg__1:PySide6.QtGui.QWheelEvent) -> None: ...


# eof
