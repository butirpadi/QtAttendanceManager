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
PySide6.QtXml, except for defaults which are replaced by "...".
"""

# Module `PySide6.QtXml`

from shiboken6 import Shiboken

from enum import Enum
from typing import Tuple, Union, overload

import PySide6.QtCore
import PySide6.QtXml


class QDomAttr(PySide6.QtXml.QDomNode):

    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, x:PySide6.QtXml.QDomAttr) -> None: ...

    @staticmethod
    def __copy__() -> None: ...
    def name(self) -> str: ...
    def nodeType(self) -> PySide6.QtXml.QDomNode.NodeType: ...
    def ownerElement(self) -> PySide6.QtXml.QDomElement: ...
    def setValue(self, arg__1:str) -> None: ...
    def specified(self) -> bool: ...
    def value(self) -> str: ...


class QDomCDATASection(PySide6.QtXml.QDomText):

    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, x:PySide6.QtXml.QDomCDATASection) -> None: ...

    @staticmethod
    def __copy__() -> None: ...
    def nodeType(self) -> PySide6.QtXml.QDomNode.NodeType: ...


class QDomCharacterData(PySide6.QtXml.QDomNode):

    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, x:PySide6.QtXml.QDomCharacterData) -> None: ...

    @staticmethod
    def __copy__() -> None: ...
    def appendData(self, arg:str) -> None: ...
    def data(self) -> str: ...
    def deleteData(self, offset:int, count:int) -> None: ...
    def insertData(self, offset:int, arg:str) -> None: ...
    def length(self) -> int: ...
    def nodeType(self) -> PySide6.QtXml.QDomNode.NodeType: ...
    def replaceData(self, offset:int, count:int, arg:str) -> None: ...
    def setData(self, arg__1:str) -> None: ...
    def substringData(self, offset:int, count:int) -> str: ...


class QDomComment(PySide6.QtXml.QDomCharacterData):

    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, x:PySide6.QtXml.QDomComment) -> None: ...

    @staticmethod
    def __copy__() -> None: ...
    def nodeType(self) -> PySide6.QtXml.QDomNode.NodeType: ...


class QDomDocument(PySide6.QtXml.QDomNode):

    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, doctype:PySide6.QtXml.QDomDocumentType) -> None: ...
    @overload
    def __init__(self, name:str) -> None: ...
    @overload
    def __init__(self, x:PySide6.QtXml.QDomDocument) -> None: ...

    @staticmethod
    def __copy__() -> None: ...
    def createAttribute(self, name:str) -> PySide6.QtXml.QDomAttr: ...
    def createAttributeNS(self, nsURI:str, qName:str) -> PySide6.QtXml.QDomAttr: ...
    def createCDATASection(self, data:str) -> PySide6.QtXml.QDomCDATASection: ...
    def createComment(self, data:str) -> PySide6.QtXml.QDomComment: ...
    def createDocumentFragment(self) -> PySide6.QtXml.QDomDocumentFragment: ...
    def createElement(self, tagName:str) -> PySide6.QtXml.QDomElement: ...
    def createElementNS(self, nsURI:str, qName:str) -> PySide6.QtXml.QDomElement: ...
    def createEntityReference(self, name:str) -> PySide6.QtXml.QDomEntityReference: ...
    def createProcessingInstruction(self, target:str, data:str) -> PySide6.QtXml.QDomProcessingInstruction: ...
    def createTextNode(self, data:str) -> PySide6.QtXml.QDomText: ...
    def doctype(self) -> PySide6.QtXml.QDomDocumentType: ...
    def documentElement(self) -> PySide6.QtXml.QDomElement: ...
    def elementById(self, elementId:str) -> PySide6.QtXml.QDomElement: ...
    def elementsByTagName(self, tagname:str) -> PySide6.QtXml.QDomNodeList: ...
    def elementsByTagNameNS(self, nsURI:str, localName:str) -> PySide6.QtXml.QDomNodeList: ...
    def implementation(self) -> PySide6.QtXml.QDomImplementation: ...
    def importNode(self, importedNode:PySide6.QtXml.QDomNode, deep:bool) -> PySide6.QtXml.QDomNode: ...
    def nodeType(self) -> PySide6.QtXml.QDomNode.NodeType: ...
    @overload
    def setContent(self, dev:PySide6.QtCore.QIODevice) -> Tuple[Tuple, str, int, int]: ...
    @overload
    def setContent(self, dev:PySide6.QtCore.QIODevice, namespaceProcessing:bool) -> Tuple[Tuple, str, int, int]: ...
    @overload
    def setContent(self, reader:PySide6.QtCore.QXmlStreamReader, namespaceProcessing:bool) -> Tuple[bool, str, int, int]: ...
    @overload
    def setContent(self, text:str) -> Tuple[Tuple, str, int, int]: ...
    @overload
    def setContent(self, text:str, namespaceProcessing:bool) -> Tuple[Tuple, str, int, int]: ...
    @overload
    def setContent(self, text:Union[PySide6.QtCore.QByteArray, bytes]) -> Tuple[Tuple, str, int, int]: ...
    @overload
    def setContent(self, text:Union[PySide6.QtCore.QByteArray, bytes], namespaceProcessing:bool) -> Tuple[Tuple, str, int, int]: ...
    def toByteArray(self, arg__1:int=...) -> PySide6.QtCore.QByteArray: ...
    def toString(self, arg__1:int=...) -> str: ...


class QDomDocumentFragment(PySide6.QtXml.QDomNode):

    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, x:PySide6.QtXml.QDomDocumentFragment) -> None: ...

    @staticmethod
    def __copy__() -> None: ...
    def nodeType(self) -> PySide6.QtXml.QDomNode.NodeType: ...


class QDomDocumentType(PySide6.QtXml.QDomNode):

    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, x:PySide6.QtXml.QDomDocumentType) -> None: ...

    @staticmethod
    def __copy__() -> None: ...
    def entities(self) -> PySide6.QtXml.QDomNamedNodeMap: ...
    def internalSubset(self) -> str: ...
    def name(self) -> str: ...
    def nodeType(self) -> PySide6.QtXml.QDomNode.NodeType: ...
    def notations(self) -> PySide6.QtXml.QDomNamedNodeMap: ...
    def publicId(self) -> str: ...
    def systemId(self) -> str: ...


class QDomElement(PySide6.QtXml.QDomNode):

    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, x:PySide6.QtXml.QDomElement) -> None: ...

    @staticmethod
    def __copy__() -> None: ...
    def attribute(self, name:str, defValue:str=...) -> str: ...
    def attributeNS(self, nsURI:str, localName:str, defValue:str=...) -> str: ...
    def attributeNode(self, name:str) -> PySide6.QtXml.QDomAttr: ...
    def attributeNodeNS(self, nsURI:str, localName:str) -> PySide6.QtXml.QDomAttr: ...
    def attributes(self) -> PySide6.QtXml.QDomNamedNodeMap: ...
    def elementsByTagName(self, tagname:str) -> PySide6.QtXml.QDomNodeList: ...
    def elementsByTagNameNS(self, nsURI:str, localName:str) -> PySide6.QtXml.QDomNodeList: ...
    def hasAttribute(self, name:str) -> bool: ...
    def hasAttributeNS(self, nsURI:str, localName:str) -> bool: ...
    def nodeType(self) -> PySide6.QtXml.QDomNode.NodeType: ...
    def removeAttribute(self, name:str) -> None: ...
    def removeAttributeNS(self, nsURI:str, localName:str) -> None: ...
    def removeAttributeNode(self, oldAttr:PySide6.QtXml.QDomAttr) -> PySide6.QtXml.QDomAttr: ...
    @overload
    def setAttribute(self, name:str, value:str) -> None: ...
    @overload
    def setAttribute(self, name:str, value:float) -> None: ...
    @overload
    def setAttribute(self, name:str, value:int) -> None: ...
    @overload
    def setAttributeNS(self, nsURI:str, qName:str, value:str) -> None: ...
    @overload
    def setAttributeNS(self, nsURI:str, qName:str, value:float) -> None: ...
    @overload
    def setAttributeNS(self, nsURI:str, qName:str, value:int) -> None: ...
    @overload
    def setAttributeNS(self, nsURI:str, qName:str, value:int) -> None: ...
    @overload
    def setAttributeNS(self, nsURI:str, qName:str, value:int) -> None: ...
    @overload
    def setAttributeNS(self, nsURI:str, qName:str, value:int) -> None: ...
    def setAttributeNode(self, newAttr:PySide6.QtXml.QDomAttr) -> PySide6.QtXml.QDomAttr: ...
    def setAttributeNodeNS(self, newAttr:PySide6.QtXml.QDomAttr) -> PySide6.QtXml.QDomAttr: ...
    def setTagName(self, name:str) -> None: ...
    def tagName(self) -> str: ...
    def text(self) -> str: ...


class QDomEntity(PySide6.QtXml.QDomNode):

    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, x:PySide6.QtXml.QDomEntity) -> None: ...

    @staticmethod
    def __copy__() -> None: ...
    def nodeType(self) -> PySide6.QtXml.QDomNode.NodeType: ...
    def notationName(self) -> str: ...
    def publicId(self) -> str: ...
    def systemId(self) -> str: ...


class QDomEntityReference(PySide6.QtXml.QDomNode):

    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, x:PySide6.QtXml.QDomEntityReference) -> None: ...

    @staticmethod
    def __copy__() -> None: ...
    def nodeType(self) -> PySide6.QtXml.QDomNode.NodeType: ...


class QDomImplementation(Shiboken.Object):

    AcceptInvalidChars       : QDomImplementation.InvalidDataPolicy = ... # 0x0
    DropInvalidChars         : QDomImplementation.InvalidDataPolicy = ... # 0x1
    ReturnNullNode           : QDomImplementation.InvalidDataPolicy = ... # 0x2

    class InvalidDataPolicy(Enum):

        AcceptInvalidChars       : QDomImplementation.InvalidDataPolicy = ... # 0x0
        DropInvalidChars         : QDomImplementation.InvalidDataPolicy = ... # 0x1
        ReturnNullNode           : QDomImplementation.InvalidDataPolicy = ... # 0x2


    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, arg__1:PySide6.QtXml.QDomImplementation) -> None: ...

    @staticmethod
    def __copy__() -> None: ...
    def createDocument(self, nsURI:str, qName:str, doctype:PySide6.QtXml.QDomDocumentType) -> PySide6.QtXml.QDomDocument: ...
    def createDocumentType(self, qName:str, publicId:str, systemId:str) -> PySide6.QtXml.QDomDocumentType: ...
    def hasFeature(self, feature:str, version:str) -> bool: ...
    @staticmethod
    def invalidDataPolicy() -> PySide6.QtXml.QDomImplementation.InvalidDataPolicy: ...
    def isNull(self) -> bool: ...
    @staticmethod
    def setInvalidDataPolicy(policy:PySide6.QtXml.QDomImplementation.InvalidDataPolicy) -> None: ...


class QDomNamedNodeMap(Shiboken.Object):

    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, arg__1:PySide6.QtXml.QDomNamedNodeMap) -> None: ...

    @staticmethod
    def __copy__() -> None: ...
    def contains(self, name:str) -> bool: ...
    def count(self) -> int: ...
    def isEmpty(self) -> bool: ...
    def item(self, index:int) -> PySide6.QtXml.QDomNode: ...
    def length(self) -> int: ...
    def namedItem(self, name:str) -> PySide6.QtXml.QDomNode: ...
    def namedItemNS(self, nsURI:str, localName:str) -> PySide6.QtXml.QDomNode: ...
    def removeNamedItem(self, name:str) -> PySide6.QtXml.QDomNode: ...
    def removeNamedItemNS(self, nsURI:str, localName:str) -> PySide6.QtXml.QDomNode: ...
    def setNamedItem(self, newNode:PySide6.QtXml.QDomNode) -> PySide6.QtXml.QDomNode: ...
    def setNamedItemNS(self, newNode:PySide6.QtXml.QDomNode) -> PySide6.QtXml.QDomNode: ...
    def size(self) -> int: ...


class QDomNode(Shiboken.Object):

    EncodingFromDocument     : QDomNode.EncodingPolicy = ... # 0x1
    EncodingFromTextStream   : QDomNode.EncodingPolicy = ... # 0x2
    ElementNode              : QDomNode.NodeType = ... # 0x1
    AttributeNode            : QDomNode.NodeType = ... # 0x2
    TextNode                 : QDomNode.NodeType = ... # 0x3
    CDATASectionNode         : QDomNode.NodeType = ... # 0x4
    EntityReferenceNode      : QDomNode.NodeType = ... # 0x5
    EntityNode               : QDomNode.NodeType = ... # 0x6
    ProcessingInstructionNode: QDomNode.NodeType = ... # 0x7
    CommentNode              : QDomNode.NodeType = ... # 0x8
    DocumentNode             : QDomNode.NodeType = ... # 0x9
    DocumentTypeNode         : QDomNode.NodeType = ... # 0xa
    DocumentFragmentNode     : QDomNode.NodeType = ... # 0xb
    NotationNode             : QDomNode.NodeType = ... # 0xc
    BaseNode                 : QDomNode.NodeType = ... # 0x15
    CharacterDataNode        : QDomNode.NodeType = ... # 0x16

    class EncodingPolicy(Enum):

        EncodingFromDocument     : QDomNode.EncodingPolicy = ... # 0x1
        EncodingFromTextStream   : QDomNode.EncodingPolicy = ... # 0x2

    class NodeType(Enum):

        ElementNode              : QDomNode.NodeType = ... # 0x1
        AttributeNode            : QDomNode.NodeType = ... # 0x2
        TextNode                 : QDomNode.NodeType = ... # 0x3
        CDATASectionNode         : QDomNode.NodeType = ... # 0x4
        EntityReferenceNode      : QDomNode.NodeType = ... # 0x5
        EntityNode               : QDomNode.NodeType = ... # 0x6
        ProcessingInstructionNode: QDomNode.NodeType = ... # 0x7
        CommentNode              : QDomNode.NodeType = ... # 0x8
        DocumentNode             : QDomNode.NodeType = ... # 0x9
        DocumentTypeNode         : QDomNode.NodeType = ... # 0xa
        DocumentFragmentNode     : QDomNode.NodeType = ... # 0xb
        NotationNode             : QDomNode.NodeType = ... # 0xc
        BaseNode                 : QDomNode.NodeType = ... # 0x15
        CharacterDataNode        : QDomNode.NodeType = ... # 0x16


    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, arg__1:PySide6.QtXml.QDomNode) -> None: ...

    @staticmethod
    def __copy__() -> None: ...
    def __lshift__(self, arg__1:PySide6.QtCore.QTextStream) -> PySide6.QtCore.QTextStream: ...
    def appendChild(self, newChild:PySide6.QtXml.QDomNode) -> PySide6.QtXml.QDomNode: ...
    def attributes(self) -> PySide6.QtXml.QDomNamedNodeMap: ...
    def childNodes(self) -> PySide6.QtXml.QDomNodeList: ...
    def clear(self) -> None: ...
    def cloneNode(self, deep:bool=...) -> PySide6.QtXml.QDomNode: ...
    def columnNumber(self) -> int: ...
    def firstChild(self) -> PySide6.QtXml.QDomNode: ...
    def firstChildElement(self, tagName:str=..., namespaceURI:str=...) -> PySide6.QtXml.QDomElement: ...
    def hasAttributes(self) -> bool: ...
    def hasChildNodes(self) -> bool: ...
    def insertAfter(self, newChild:PySide6.QtXml.QDomNode, refChild:PySide6.QtXml.QDomNode) -> PySide6.QtXml.QDomNode: ...
    def insertBefore(self, newChild:PySide6.QtXml.QDomNode, refChild:PySide6.QtXml.QDomNode) -> PySide6.QtXml.QDomNode: ...
    def isAttr(self) -> bool: ...
    def isCDATASection(self) -> bool: ...
    def isCharacterData(self) -> bool: ...
    def isComment(self) -> bool: ...
    def isDocument(self) -> bool: ...
    def isDocumentFragment(self) -> bool: ...
    def isDocumentType(self) -> bool: ...
    def isElement(self) -> bool: ...
    def isEntity(self) -> bool: ...
    def isEntityReference(self) -> bool: ...
    def isNotation(self) -> bool: ...
    def isNull(self) -> bool: ...
    def isProcessingInstruction(self) -> bool: ...
    def isSupported(self, feature:str, version:str) -> bool: ...
    def isText(self) -> bool: ...
    def lastChild(self) -> PySide6.QtXml.QDomNode: ...
    def lastChildElement(self, tagName:str=..., namespaceURI:str=...) -> PySide6.QtXml.QDomElement: ...
    def lineNumber(self) -> int: ...
    def localName(self) -> str: ...
    def namedItem(self, name:str) -> PySide6.QtXml.QDomNode: ...
    def namespaceURI(self) -> str: ...
    def nextSibling(self) -> PySide6.QtXml.QDomNode: ...
    def nextSiblingElement(self, taName:str=..., namespaceURI:str=...) -> PySide6.QtXml.QDomElement: ...
    def nodeName(self) -> str: ...
    def nodeType(self) -> PySide6.QtXml.QDomNode.NodeType: ...
    def nodeValue(self) -> str: ...
    def normalize(self) -> None: ...
    def ownerDocument(self) -> PySide6.QtXml.QDomDocument: ...
    def parentNode(self) -> PySide6.QtXml.QDomNode: ...
    def prefix(self) -> str: ...
    def previousSibling(self) -> PySide6.QtXml.QDomNode: ...
    def previousSiblingElement(self, tagName:str=..., namespaceURI:str=...) -> PySide6.QtXml.QDomElement: ...
    def removeChild(self, oldChild:PySide6.QtXml.QDomNode) -> PySide6.QtXml.QDomNode: ...
    def replaceChild(self, newChild:PySide6.QtXml.QDomNode, oldChild:PySide6.QtXml.QDomNode) -> PySide6.QtXml.QDomNode: ...
    def save(self, arg__1:PySide6.QtCore.QTextStream, arg__2:int, arg__3:PySide6.QtXml.QDomNode.EncodingPolicy=...) -> None: ...
    def setNodeValue(self, arg__1:str) -> None: ...
    def setPrefix(self, pre:str) -> None: ...
    def toAttr(self) -> PySide6.QtXml.QDomAttr: ...
    def toCDATASection(self) -> PySide6.QtXml.QDomCDATASection: ...
    def toCharacterData(self) -> PySide6.QtXml.QDomCharacterData: ...
    def toComment(self) -> PySide6.QtXml.QDomComment: ...
    def toDocument(self) -> PySide6.QtXml.QDomDocument: ...
    def toDocumentFragment(self) -> PySide6.QtXml.QDomDocumentFragment: ...
    def toDocumentType(self) -> PySide6.QtXml.QDomDocumentType: ...
    def toElement(self) -> PySide6.QtXml.QDomElement: ...
    def toEntity(self) -> PySide6.QtXml.QDomEntity: ...
    def toEntityReference(self) -> PySide6.QtXml.QDomEntityReference: ...
    def toNotation(self) -> PySide6.QtXml.QDomNotation: ...
    def toProcessingInstruction(self) -> PySide6.QtXml.QDomProcessingInstruction: ...
    def toText(self) -> PySide6.QtXml.QDomText: ...


class QDomNodeList(Shiboken.Object):

    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, arg__1:PySide6.QtXml.QDomNodeList) -> None: ...

    @staticmethod
    def __copy__() -> None: ...
    def at(self, index:int) -> PySide6.QtXml.QDomNode: ...
    def count(self) -> int: ...
    def isEmpty(self) -> bool: ...
    def item(self, index:int) -> PySide6.QtXml.QDomNode: ...
    def length(self) -> int: ...
    def size(self) -> int: ...


class QDomNotation(PySide6.QtXml.QDomNode):

    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, x:PySide6.QtXml.QDomNotation) -> None: ...

    @staticmethod
    def __copy__() -> None: ...
    def nodeType(self) -> PySide6.QtXml.QDomNode.NodeType: ...
    def publicId(self) -> str: ...
    def systemId(self) -> str: ...


class QDomProcessingInstruction(PySide6.QtXml.QDomNode):

    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, x:PySide6.QtXml.QDomProcessingInstruction) -> None: ...

    @staticmethod
    def __copy__() -> None: ...
    def data(self) -> str: ...
    def nodeType(self) -> PySide6.QtXml.QDomNode.NodeType: ...
    def setData(self, d:str) -> None: ...
    def target(self) -> str: ...


class QDomText(PySide6.QtXml.QDomCharacterData):

    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, x:PySide6.QtXml.QDomText) -> None: ...

    @staticmethod
    def __copy__() -> None: ...
    def nodeType(self) -> PySide6.QtXml.QDomNode.NodeType: ...
    def splitText(self, offset:int) -> PySide6.QtXml.QDomText: ...


# eof
