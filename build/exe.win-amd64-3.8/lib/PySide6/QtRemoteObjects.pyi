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
PySide6.QtRemoteObjects, except for defaults which are replaced by "...".
"""

# Module `PySide6.QtRemoteObjects`

from shiboken6 import Shiboken

from enum import Enum
from typing import Any, Optional, Tuple, Union, Sequence, Dict, List, overload

import PySide6.QtCore
import PySide6.QtRemoteObjects


class QAbstractItemModelReplica(PySide6.QtCore.QAbstractItemModel):
    def availableRoles(self) -> List[int]: ...
    def columnCount(self, parent:Union[PySide6.QtCore.QModelIndex, PySide6.QtCore.QPersistentModelIndex]=...) -> int: ...
    def data(self, index:Union[PySide6.QtCore.QModelIndex, PySide6.QtCore.QPersistentModelIndex], role:int=...) -> Any: ...
    def flags(self, index:Union[PySide6.QtCore.QModelIndex, PySide6.QtCore.QPersistentModelIndex]) -> PySide6.QtCore.Qt.ItemFlags: ...
    def hasChildren(self, parent:Union[PySide6.QtCore.QModelIndex, PySide6.QtCore.QPersistentModelIndex]=...) -> bool: ...
    def hasData(self, index:Union[PySide6.QtCore.QModelIndex, PySide6.QtCore.QPersistentModelIndex], role:int) -> bool: ...
    def headerData(self, section:int, orientation:PySide6.QtCore.Qt.Orientation, role:int) -> Any: ...
    def index(self, row:int, column:int, parent:Union[PySide6.QtCore.QModelIndex, PySide6.QtCore.QPersistentModelIndex]=...) -> PySide6.QtCore.QModelIndex: ...
    def isInitialized(self) -> bool: ...
    @overload
    def parent(self) -> PySide6.QtCore.QObject: ...
    @overload
    def parent(self, index:Union[PySide6.QtCore.QModelIndex, PySide6.QtCore.QPersistentModelIndex]) -> PySide6.QtCore.QModelIndex: ...
    def roleNames(self) -> Dict[int, PySide6.QtCore.QByteArray]: ...
    def rootCacheSize(self) -> int: ...
    def rowCount(self, parent:Union[PySide6.QtCore.QModelIndex, PySide6.QtCore.QPersistentModelIndex]=...) -> int: ...
    def selectionModel(self) -> PySide6.QtCore.QItemSelectionModel: ...
    def setData(self, index:Union[PySide6.QtCore.QModelIndex, PySide6.QtCore.QPersistentModelIndex], value:Any, role:int=...) -> bool: ...
    def setRootCacheSize(self, rootCacheSize:int) -> None: ...


class QIntList(object): ...


class QRemoteObjectAbstractPersistedStore(PySide6.QtCore.QObject):

    def __init__(self, parent:Optional[PySide6.QtCore.QObject]=...) -> None: ...

    def restoreProperties(self, repName:str, repSig:Union[PySide6.QtCore.QByteArray, bytes]) -> List[Any]: ...
    def saveProperties(self, repName:str, repSig:Union[PySide6.QtCore.QByteArray, bytes], values:Sequence[Any]) -> None: ...


class QRemoteObjectDynamicReplica(PySide6.QtRemoteObjects.QRemoteObjectReplica): ...


class QRemoteObjectHost(PySide6.QtRemoteObjects.QRemoteObjectHostBase):

    @overload
    def __init__(self, address:Union[PySide6.QtCore.QUrl, str], parent:PySide6.QtCore.QObject) -> None: ...
    @overload
    def __init__(self, address:Union[PySide6.QtCore.QUrl, str], registryAddress:Union[PySide6.QtCore.QUrl, str]=..., allowedSchemas:PySide6.QtRemoteObjects.QRemoteObjectHostBase.AllowedSchemas=..., parent:Optional[PySide6.QtCore.QObject]=...) -> None: ...
    @overload
    def __init__(self, parent:Optional[PySide6.QtCore.QObject]=...) -> None: ...

    def hostUrl(self) -> PySide6.QtCore.QUrl: ...
    def setHostUrl(self, hostAddress:Union[PySide6.QtCore.QUrl, str], allowedSchemas:PySide6.QtRemoteObjects.QRemoteObjectHostBase.AllowedSchemas=...) -> bool: ...


class QRemoteObjectHostBase(PySide6.QtRemoteObjects.QRemoteObjectNode):

    BuiltInSchemasOnly       : QRemoteObjectHostBase.AllowedSchemas = ... # 0x0
    AllowExternalRegistration: QRemoteObjectHostBase.AllowedSchemas = ... # 0x1

    class AllowedSchemas(Enum):

        BuiltInSchemasOnly       : QRemoteObjectHostBase.AllowedSchemas = ... # 0x0
        AllowExternalRegistration: QRemoteObjectHostBase.AllowedSchemas = ... # 0x1


    def addHostSideConnection(self, ioDevice:PySide6.QtCore.QIODevice) -> None: ...
    def disableRemoting(self, remoteObject:PySide6.QtCore.QObject) -> bool: ...
    @overload
    def enableRemoting(self, model:PySide6.QtCore.QAbstractItemModel, name:str, roles:Sequence[int], selectionModel:Optional[PySide6.QtCore.QItemSelectionModel]=...) -> bool: ...
    @overload
    def enableRemoting(self, object:PySide6.QtCore.QObject, name:str=...) -> bool: ...
    def hostUrl(self) -> PySide6.QtCore.QUrl: ...
    def proxy(self, registryUrl:Union[PySide6.QtCore.QUrl, str], hostUrl:Union[PySide6.QtCore.QUrl, str]=...) -> bool: ...
    def reverseProxy(self) -> bool: ...
    def setHostUrl(self, hostAddress:Union[PySide6.QtCore.QUrl, str], allowedSchemas:PySide6.QtRemoteObjects.QRemoteObjectHostBase.AllowedSchemas=...) -> bool: ...
    def setName(self, name:str) -> None: ...


class QRemoteObjectNode(PySide6.QtCore.QObject):

    NoError                  : QRemoteObjectNode.ErrorCode = ... # 0x0
    RegistryNotAcquired      : QRemoteObjectNode.ErrorCode = ... # 0x1
    RegistryAlreadyHosted    : QRemoteObjectNode.ErrorCode = ... # 0x2
    NodeIsNoServer           : QRemoteObjectNode.ErrorCode = ... # 0x3
    ServerAlreadyCreated     : QRemoteObjectNode.ErrorCode = ... # 0x4
    UnintendedRegistryHosting: QRemoteObjectNode.ErrorCode = ... # 0x5
    OperationNotValidOnClientNode: QRemoteObjectNode.ErrorCode = ... # 0x6
    SourceNotRegistered      : QRemoteObjectNode.ErrorCode = ... # 0x7
    MissingObjectName        : QRemoteObjectNode.ErrorCode = ... # 0x8
    HostUrlInvalid           : QRemoteObjectNode.ErrorCode = ... # 0x9
    ProtocolMismatch         : QRemoteObjectNode.ErrorCode = ... # 0xa
    ListenFailed             : QRemoteObjectNode.ErrorCode = ... # 0xb

    class ErrorCode(Enum):

        NoError                  : QRemoteObjectNode.ErrorCode = ... # 0x0
        RegistryNotAcquired      : QRemoteObjectNode.ErrorCode = ... # 0x1
        RegistryAlreadyHosted    : QRemoteObjectNode.ErrorCode = ... # 0x2
        NodeIsNoServer           : QRemoteObjectNode.ErrorCode = ... # 0x3
        ServerAlreadyCreated     : QRemoteObjectNode.ErrorCode = ... # 0x4
        UnintendedRegistryHosting: QRemoteObjectNode.ErrorCode = ... # 0x5
        OperationNotValidOnClientNode: QRemoteObjectNode.ErrorCode = ... # 0x6
        SourceNotRegistered      : QRemoteObjectNode.ErrorCode = ... # 0x7
        MissingObjectName        : QRemoteObjectNode.ErrorCode = ... # 0x8
        HostUrlInvalid           : QRemoteObjectNode.ErrorCode = ... # 0x9
        ProtocolMismatch         : QRemoteObjectNode.ErrorCode = ... # 0xa
        ListenFailed             : QRemoteObjectNode.ErrorCode = ... # 0xb


    @overload
    def __init__(self, parent:Optional[PySide6.QtCore.QObject]=...) -> None: ...
    @overload
    def __init__(self, registryAddress:Union[PySide6.QtCore.QUrl, str], parent:Optional[PySide6.QtCore.QObject]=...) -> None: ...

    def acquireDynamic(self, name:str) -> PySide6.QtRemoteObjects.QRemoteObjectDynamicReplica: ...
    def acquireModel(self, name:str) -> PySide6.QtRemoteObjects.QAbstractItemModelReplica: ...
    def addClientSideConnection(self, ioDevice:PySide6.QtCore.QIODevice) -> None: ...
    def connectToNode(self, address:Union[PySide6.QtCore.QUrl, str]) -> bool: ...
    def heartbeatInterval(self) -> int: ...
    def instances(self, typeName:str) -> List[str]: ...
    def lastError(self) -> PySide6.QtRemoteObjects.QRemoteObjectNode.ErrorCode: ...
    def persistedStore(self) -> PySide6.QtRemoteObjects.QRemoteObjectAbstractPersistedStore: ...
    def registry(self) -> PySide6.QtRemoteObjects.QRemoteObjectRegistry: ...
    def registryUrl(self) -> PySide6.QtCore.QUrl: ...
    def setHeartbeatInterval(self, interval:int) -> None: ...
    def setName(self, name:str) -> None: ...
    def setPersistedStore(self, persistedStore:PySide6.QtRemoteObjects.QRemoteObjectAbstractPersistedStore) -> None: ...
    def setRegistryUrl(self, registryAddress:Union[PySide6.QtCore.QUrl, str]) -> bool: ...
    def timerEvent(self, arg__1:PySide6.QtCore.QTimerEvent) -> None: ...
    def waitForRegistry(self, timeout:int=...) -> bool: ...


class QRemoteObjectPendingCall(Shiboken.Object):

    NoError                  : QRemoteObjectPendingCall.Error = ... # 0x0
    InvalidMessage           : QRemoteObjectPendingCall.Error = ... # 0x1

    class Error(Enum):

        NoError                  : QRemoteObjectPendingCall.Error = ... # 0x0
        InvalidMessage           : QRemoteObjectPendingCall.Error = ... # 0x1


    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, other:PySide6.QtRemoteObjects.QRemoteObjectPendingCall) -> None: ...

    def error(self) -> PySide6.QtRemoteObjects.QRemoteObjectPendingCall.Error: ...
    @staticmethod
    def fromCompletedCall(returnValue:Any) -> PySide6.QtRemoteObjects.QRemoteObjectPendingCall: ...
    def isFinished(self) -> bool: ...
    def returnValue(self) -> Any: ...
    def waitForFinished(self, timeout:int=...) -> bool: ...


class QRemoteObjectPendingCallWatcher(PySide6.QtCore.QObject, PySide6.QtRemoteObjects.QRemoteObjectPendingCall):

    def __init__(self, call:PySide6.QtRemoteObjects.QRemoteObjectPendingCall, parent:Optional[PySide6.QtCore.QObject]=...) -> None: ...

    def isFinished(self) -> bool: ...
    def waitForFinished(self) -> None: ...


class QRemoteObjectRegistry(PySide6.QtRemoteObjects.QRemoteObjectReplica):
    def addSource(self, entry:Tuple[str, PySide6.QtRemoteObjects.QRemoteObjectSourceLocationInfo]) -> None: ...
    def initialize(self) -> None: ...
    def pushToRegistryIfNeeded(self) -> None: ...
    @staticmethod
    def registerMetatypes() -> None: ...
    def removeSource(self, entry:Tuple[str, PySide6.QtRemoteObjects.QRemoteObjectSourceLocationInfo]) -> None: ...
    def sourceLocations(self) -> Dict[str, PySide6.QtRemoteObjects.QRemoteObjectSourceLocationInfo]: ...


class QRemoteObjectRegistryHost(PySide6.QtRemoteObjects.QRemoteObjectHostBase):

    def __init__(self, registryAddress:Union[PySide6.QtCore.QUrl, str]=..., parent:Optional[PySide6.QtCore.QObject]=...) -> None: ...

    def setRegistryUrl(self, registryUrl:Union[PySide6.QtCore.QUrl, str]) -> bool: ...


class QRemoteObjectReplica(PySide6.QtCore.QObject):

    Uninitialized            : QRemoteObjectReplica.State = ... # 0x0
    Default                  : QRemoteObjectReplica.State = ... # 0x1
    Valid                    : QRemoteObjectReplica.State = ... # 0x2
    Suspect                  : QRemoteObjectReplica.State = ... # 0x3
    SignatureMismatch        : QRemoteObjectReplica.State = ... # 0x4

    class State(Enum):

        Uninitialized            : QRemoteObjectReplica.State = ... # 0x0
        Default                  : QRemoteObjectReplica.State = ... # 0x1
        Valid                    : QRemoteObjectReplica.State = ... # 0x2
        Suspect                  : QRemoteObjectReplica.State = ... # 0x3
        SignatureMismatch        : QRemoteObjectReplica.State = ... # 0x4


    def __init__(self) -> None: ...

    def initialize(self) -> None: ...
    def initializeNode(self, node:PySide6.QtRemoteObjects.QRemoteObjectNode, name:str=...) -> None: ...
    def isInitialized(self) -> bool: ...
    def isReplicaValid(self) -> bool: ...
    def node(self) -> PySide6.QtRemoteObjects.QRemoteObjectNode: ...
    def persistProperties(self, repName:str, repSig:Union[PySide6.QtCore.QByteArray, bytes], props:Sequence[Any]) -> None: ...
    def propAsVariant(self, i:int) -> Any: ...
    def retrieveProperties(self, repName:str, repSig:Union[PySide6.QtCore.QByteArray, bytes]) -> List[Any]: ...
    def send(self, call:PySide6.QtCore.QMetaObject.Call, index:int, args:Sequence[Any]) -> None: ...
    def sendWithReply(self, call:PySide6.QtCore.QMetaObject.Call, index:int, args:Sequence[Any]) -> PySide6.QtRemoteObjects.QRemoteObjectPendingCall: ...
    def setChild(self, i:int, arg__2:Any) -> None: ...
    def setNode(self, node:PySide6.QtRemoteObjects.QRemoteObjectNode) -> None: ...
    def state(self) -> PySide6.QtRemoteObjects.QRemoteObjectReplica.State: ...
    def waitForSource(self, timeout:int=...) -> bool: ...


class QRemoteObjectSettingsStore(PySide6.QtRemoteObjects.QRemoteObjectAbstractPersistedStore):

    def __init__(self, parent:Optional[PySide6.QtCore.QObject]=...) -> None: ...

    def restoreProperties(self, repName:str, repSig:Union[PySide6.QtCore.QByteArray, bytes]) -> List[Any]: ...
    def saveProperties(self, repName:str, repSig:Union[PySide6.QtCore.QByteArray, bytes], values:Sequence[Any]) -> None: ...


class QRemoteObjectSourceLocationInfo(Shiboken.Object):

    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, QRemoteObjectSourceLocationInfo:PySide6.QtRemoteObjects.QRemoteObjectSourceLocationInfo) -> None: ...
    @overload
    def __init__(self, typeName_:str, hostUrl_:Union[PySide6.QtCore.QUrl, str]) -> None: ...

    @staticmethod
    def __copy__() -> None: ...
    def __lshift__(self, stream:PySide6.QtCore.QDataStream) -> PySide6.QtCore.QDataStream: ...
    def __rshift__(self, stream:PySide6.QtCore.QDataStream) -> PySide6.QtCore.QDataStream: ...


# eof
