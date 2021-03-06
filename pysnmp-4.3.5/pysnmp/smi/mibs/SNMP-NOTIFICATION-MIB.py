#
# This file is part of pysnmp software.
#
# Copyright (c) 2005-2017, Ilya Etingof <etingof@gmail.com>
# License: http://pysnmp.sf.net/license.html
#
# PySNMP MIB module SNMP-NOTIFICATION-MIB (http://pysnmp.sf.net)
# ASN.1 source file:///usr/share/snmp/mibs/SNMP-NOTIFICATION-MIB.txt
# Produced by pysmi-0.0.5 at Sat Sep 19 23:00:18 2015
# On host grommit.local platform Darwin version 14.4.0 by user ilya
# Using Python version 2.7.6 (default, Sep  9 2014, 15:04:36) 
#
(Integer, ObjectIdentifier, OctetString,) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier",
                                                                     "OctetString")
(NamedValues,) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
(ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint,
 ValueRangeConstraint,) = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint",
                                                   "ConstraintsIntersection", "ValueSizeConstraint",
                                                   "ValueRangeConstraint")
(SnmpAdminString,) = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
(snmpTargetParamsName, SnmpTagValue,) = mibBuilder.importSymbols("SNMP-TARGET-MIB", "snmpTargetParamsName",
                                                                 "SnmpTagValue")
(NotificationGroup, ModuleCompliance, ObjectGroup,) = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup",
                                                                               "ModuleCompliance", "ObjectGroup")
(Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, MibIdentifier, IpAddress, TimeTicks,
 Counter64, Unsigned32, ModuleIdentity, Gauge32, snmpModules, iso, ObjectIdentity, Bits,
 Counter32,) = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "MibScalar", "MibTable", "MibTableRow",
                                        "MibTableColumn", "NotificationType", "MibIdentifier", "IpAddress", "TimeTicks",
                                        "Counter64", "Unsigned32", "ModuleIdentity", "Gauge32", "snmpModules", "iso",
                                        "ObjectIdentity", "Bits", "Counter32")
(StorageType, DisplayString, RowStatus, TextualConvention,) = mibBuilder.importSymbols("SNMPv2-TC", "StorageType",
                                                                                       "DisplayString", "RowStatus",
                                                                                       "TextualConvention")
snmpNotificationMIB = ModuleIdentity((1, 3, 6, 1, 6, 3, 13)).setRevisions(
    ("2002-10-14 00:00", "1998-08-04 00:00", "1997-07-14 00:00",))
if mibBuilder.loadTexts:
    snmpNotificationMIB.setLastUpdated('200210140000Z')
if mibBuilder.loadTexts:
    snmpNotificationMIB.setOrganization('IETF SNMPv3 Working Group')
if mibBuilder.loadTexts:
    snmpNotificationMIB.setContactInfo(
        'WG-email:   snmpv3@lists.tislabs.com\n         Subscribe:  majordomo@lists.tislabs.com\n                     In message body:  subscribe snmpv3\n\n         Co-Chair:   Russ Mundy\n                     Network Associates Laboratories\n         Postal:     15204 Omega Drive, Suite 300\n                     Rockville, MD 20850-4601\n                     USA\n         EMail:      mundy@tislabs.com\n         Phone:      +1 301-947-7107\n\n         Co-Chair:   David Harrington\n                     Enterasys Networks\n         Postal:     35 Industrial Way\n                     P. O. Box 5004\n                     Rochester, New Hampshire 03866-5005\n                     USA\n         EMail:      dbh@enterasys.com\n         Phone:      +1 603-337-2614\n\n         Co-editor:  David B. Levi\n                     Nortel Networks\n         Postal:     3505 Kesterwood Drive\n                     Knoxville, Tennessee 37918\n         EMail:      dlevi@nortelnetworks.com\n         Phone:      +1 865 686 0432\n\n         Co-editor:  Paul Meyer\n                     Secure Computing Corporation\n         Postal:     2675 Long Lake Road\n                     Roseville, Minnesota 55113\n         EMail:      paul_meyer@securecomputing.com\n         Phone:      +1 651 628 1592\n\n         Co-editor:  Bob Stewart\n                     Retired')
if mibBuilder.loadTexts:
    snmpNotificationMIB.setDescription(
        'This MIB module defines MIB objects which provide\n         mechanisms to remotely configure the parameters\n         used by an SNMP entity for the generation of\n         notifications.\n\n         Copyright (C) The Internet Society (2002). This\n         version of this MIB module is part of RFC 3413;\n         see the RFC itself for full legal notices.\n        ')
snmpNotifyObjects = MibIdentifier((1, 3, 6, 1, 6, 3, 13, 1))
snmpNotifyConformance = MibIdentifier((1, 3, 6, 1, 6, 3, 13, 3))
snmpNotifyTable = MibTable((1, 3, 6, 1, 6, 3, 13, 1, 1), )
if mibBuilder.loadTexts:
    snmpNotifyTable.setDescription(
        'This table is used to select management targets which should\n         receive notifications, as well as the type of notification\n         which should be sent to each selected management target.')
snmpNotifyEntry = MibTableRow((1, 3, 6, 1, 6, 3, 13, 1, 1, 1), ).setIndexNames(
    (1, "SNMP-NOTIFICATION-MIB", "snmpNotifyName"))
if mibBuilder.loadTexts:
    snmpNotifyEntry.setDescription(
        'An entry in this table selects a set of management targets\n         which should receive notifications, as well as the type of\n\n         notification which should be sent to each selected\n         management target.\n\n         Entries in the snmpNotifyTable are created and\n         deleted using the snmpNotifyRowStatus object.')
snmpNotifyName = MibTableColumn((1, 3, 6, 1, 6, 3, 13, 1, 1, 1, 1),
                                SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 32)))
if mibBuilder.loadTexts:
    snmpNotifyName.setDescription(
        'The locally arbitrary, but unique identifier associated\n         with this snmpNotifyEntry.')
snmpNotifyTag = MibTableColumn((1, 3, 6, 1, 6, 3, 13, 1, 1, 1, 2), SnmpTagValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts:
    snmpNotifyTag.setDescription(
        'This object contains a single tag value which is used\n         to select entries in the snmpTargetAddrTable.  Any entry\n         in the snmpTargetAddrTable which contains a tag value\n         which is equal to the value of an instance of this\n         object is selected.  If this object contains a value\n         of zero length, no entries are selected.')
snmpNotifyType = MibTableColumn((1, 3, 6, 1, 6, 3, 13, 1, 1, 1, 3),
                                Integer32().subtype(subtypeSpec=SingleValueConstraint(1, 2, )).clone(
                                    namedValues=NamedValues(("trap", 1), ("inform", 2), )).clone('trap')).setMaxAccess(
    "readcreate")
if mibBuilder.loadTexts:
    snmpNotifyType.setDescription(
        'This object determines the type of notification to\n\n         be generated for entries in the snmpTargetAddrTable\n         selected by the corresponding instance of\n         snmpNotifyTag.  This value is only used when\n         generating notifications, and is ignored when\n         using the snmpTargetAddrTable for other purposes.\n\n         If the value of this object is trap(1), then any\n         messages generated for selected rows will contain\n         Unconfirmed-Class PDUs.\n\n         If the value of this object is inform(2), then any\n         messages generated for selected rows will contain\n         Confirmed-Class PDUs.\n\n         Note that if an SNMP entity only supports\n         generation of Unconfirmed-Class PDUs (and not\n         Confirmed-Class PDUs), then this object may be\n         read-only.')
snmpNotifyStorageType = MibTableColumn((1, 3, 6, 1, 6, 3, 13, 1, 1, 1, 4),
                                       StorageType().clone('nonVolatile')).setMaxAccess("readcreate")
if mibBuilder.loadTexts:
    snmpNotifyStorageType.setDescription(
        "The storage type for this conceptual row.\n         Conceptual rows having the value 'permanent' need not\n         allow write-access to any columnar objects in the row.")
snmpNotifyRowStatus = MibTableColumn((1, 3, 6, 1, 6, 3, 13, 1, 1, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts:
    snmpNotifyRowStatus.setDescription(
        'The status of this conceptual row.\n\n         To create a row in this table, a manager must\n         set this object to either createAndGo(4) or\n         createAndWait(5).')
snmpNotifyFilterProfileTable = MibTable((1, 3, 6, 1, 6, 3, 13, 1, 2), )
if mibBuilder.loadTexts:
    snmpNotifyFilterProfileTable.setDescription(
        'This table is used to associate a notification filter\n         profile with a particular set of target parameters.')
snmpNotifyFilterProfileEntry = MibTableRow((1, 3, 6, 1, 6, 3, 13, 1, 2, 1), ).setIndexNames(
    (1, "SNMP-TARGET-MIB", "snmpTargetParamsName"))
if mibBuilder.loadTexts:
    snmpNotifyFilterProfileEntry.setDescription(
        'An entry in this table indicates the name of the filter\n         profile to be used when generating notifications using\n         the corresponding entry in the snmpTargetParamsTable.\n\n         Entries in the snmpNotifyFilterProfileTable are created\n         and deleted using the snmpNotifyFilterProfileRowStatus\n         object.')
snmpNotifyFilterProfileName = MibTableColumn((1, 3, 6, 1, 6, 3, 13, 1, 2, 1, 1), SnmpAdminString().subtype(
    subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readcreate")
if mibBuilder.loadTexts:
    snmpNotifyFilterProfileName.setDescription(
        'The name of the filter profile to be used when generating\n         notifications using the corresponding entry in the\n         snmpTargetAddrTable.')
snmpNotifyFilterProfileStorType = MibTableColumn((1, 3, 6, 1, 6, 3, 13, 1, 2, 1, 2),
                                                 StorageType().clone('nonVolatile')).setMaxAccess("readcreate")
if mibBuilder.loadTexts:
    snmpNotifyFilterProfileStorType.setDescription(
        "The storage type for this conceptual row.\n         Conceptual rows having the value 'permanent' need not\n         allow write-access to any columnar objects in the row.")
snmpNotifyFilterProfileRowStatus = MibTableColumn((1, 3, 6, 1, 6, 3, 13, 1, 2, 1, 3), RowStatus()).setMaxAccess(
    "readcreate")
if mibBuilder.loadTexts:
    snmpNotifyFilterProfileRowStatus.setDescription(
        "The status of this conceptual row.\n\n         To create a row in this table, a manager must\n         set this object to either createAndGo(4) or\n         createAndWait(5).\n\n         Until instances of all corresponding columns are\n         appropriately configured, the value of the\n         corresponding instance of the\n         snmpNotifyFilterProfileRowStatus column is 'notReady'.\n\n         In particular, a newly created row cannot be made\n         active until the corresponding instance of\n         snmpNotifyFilterProfileName has been set.")
snmpNotifyFilterTable = MibTable((1, 3, 6, 1, 6, 3, 13, 1, 3), )
if mibBuilder.loadTexts:
    snmpNotifyFilterTable.setDescription(
        'The table of filter profiles.  Filter profiles are used\n         to determine whether particular management targets should\n         receive particular notifications.\n\n         When a notification is generated, it must be compared\n         with the filters associated with each management target\n         which is configured to receive notifications, in order to\n         determine whether it may be sent to each such management\n         target.\n\n         A more complete discussion of notification filtering\n         can be found in section 6. of [SNMP-APPL].')
snmpNotifyFilterEntry = MibTableRow((1, 3, 6, 1, 6, 3, 13, 1, 3, 1), ).setIndexNames(
    (0, "SNMP-NOTIFICATION-MIB", "snmpNotifyFilterProfileName"),
    (1, "SNMP-NOTIFICATION-MIB", "snmpNotifyFilterSubtree"))
if mibBuilder.loadTexts:
    snmpNotifyFilterEntry.setDescription(
        'An element of a filter profile.\n\n         Entries in the snmpNotifyFilterTable are created and\n         deleted using the snmpNotifyFilterRowStatus object.')
snmpNotifyFilterSubtree = MibTableColumn((1, 3, 6, 1, 6, 3, 13, 1, 3, 1, 1), ObjectIdentifier())
if mibBuilder.loadTexts:
    snmpNotifyFilterSubtree.setDescription(
        'The MIB subtree which, when combined with the corresponding\n         instance of snmpNotifyFilterMask, defines a family of\n         subtrees which are included in or excluded from the\n         filter profile.')
snmpNotifyFilterMask = MibTableColumn((1, 3, 6, 1, 6, 3, 13, 1, 3, 1, 2),
                                      OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 16)).clone(
                                          hexValue="")).setMaxAccess("readcreate")
if mibBuilder.loadTexts:
    snmpNotifyFilterMask.setDescription(
        "The bit mask which, in combination with the corresponding\n         instance of snmpNotifyFilterSubtree, defines a family of\n         subtrees which are included in or excluded from the\n         filter profile.\n\n         Each bit of this bit mask corresponds to a\n         sub-identifier of snmpNotifyFilterSubtree, with the\n         most significant bit of the i-th octet of this octet\n         string value (extended if necessary, see below)\n         corresponding to the (8*i - 7)-th sub-identifier, and\n         the least significant bit of the i-th octet of this\n         octet string corresponding to the (8*i)-th\n         sub-identifier, where i is in the range 1 through 16.\n\n         Each bit of this bit mask specifies whether or not\n         the corresponding sub-identifiers must match when\n         determining if an OBJECT IDENTIFIER matches this\n         family of filter subtrees; a '1' indicates that an\n         exact match must occur; a '0' indicates 'wild card',\n         i.e., any sub-identifier value matches.\n\n         Thus, the OBJECT IDENTIFIER X of an object instance\n         is contained in a family of filter subtrees if, for\n         each sub-identifier of the value of\n         snmpNotifyFilterSubtree, either:\n\n           the i-th bit of snmpNotifyFilterMask is 0, or\n\n           the i-th sub-identifier of X is equal to the i-th\n           sub-identifier of the value of\n           snmpNotifyFilterSubtree.\n\n         If the value of this bit mask is M bits long and\n         there are more than M sub-identifiers in the\n         corresponding instance of snmpNotifyFilterSubtree,\n         then the bit mask is extended with 1's to be the\n         required length.\n\n         Note that when the value of this object is the\n         zero-length string, this extension rule results in\n         a mask of all-1's being used (i.e., no 'wild card'),\n         and the family of filter subtrees is the one\n         subtree uniquely identified by the corresponding\n         instance of snmpNotifyFilterSubtree.")
snmpNotifyFilterType = MibTableColumn((1, 3, 6, 1, 6, 3, 13, 1, 3, 1, 3),
                                      Integer32().subtype(subtypeSpec=SingleValueConstraint(1, 2, )).clone(
                                          namedValues=NamedValues(("included", 1), ("excluded", 2), )).clone(
                                          'included')).setMaxAccess("readcreate")
if mibBuilder.loadTexts:
    snmpNotifyFilterType.setDescription(
        'This object indicates whether the family of filter subtrees\n         defined by this entry are included in or excluded from a\n         filter.  A more detailed discussion of the use of this\n         object can be found in section 6. of [SNMP-APPL].')
snmpNotifyFilterStorageType = MibTableColumn((1, 3, 6, 1, 6, 3, 13, 1, 3, 1, 4),
                                             StorageType().clone('nonVolatile')).setMaxAccess("readcreate")
if mibBuilder.loadTexts:
    snmpNotifyFilterStorageType.setDescription(
        "The storage type for this conceptual row.\n         Conceptual rows having the value 'permanent' need not\n\n         allow write-access to any columnar objects in the row.")
snmpNotifyFilterRowStatus = MibTableColumn((1, 3, 6, 1, 6, 3, 13, 1, 3, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts:
    snmpNotifyFilterRowStatus.setDescription(
        'The status of this conceptual row.\n\n         To create a row in this table, a manager must\n         set this object to either createAndGo(4) or\n         createAndWait(5).')
snmpNotifyCompliances = MibIdentifier((1, 3, 6, 1, 6, 3, 13, 3, 1))
snmpNotifyGroups = MibIdentifier((1, 3, 6, 1, 6, 3, 13, 3, 2))
snmpNotifyBasicCompliance = ModuleCompliance((1, 3, 6, 1, 6, 3, 13, 3, 1, 1)).setObjects(
    *(("SNMP-TARGET-MIB", "snmpTargetBasicGroup"), ("SNMP-NOTIFICATION-MIB", "snmpNotifyGroup"),))
if mibBuilder.loadTexts:
    snmpNotifyBasicCompliance.setDescription(
        'The compliance statement for minimal SNMP entities which\n         implement only SNMP Unconfirmed-Class notifications and\n         read-create operations on only the snmpTargetAddrTable.')
snmpNotifyBasicFiltersCompliance = ModuleCompliance((1, 3, 6, 1, 6, 3, 13, 3, 1, 2)).setObjects(*(
    ("SNMP-TARGET-MIB", "snmpTargetBasicGroup"), ("SNMP-NOTIFICATION-MIB", "snmpNotifyGroup"),
    ("SNMP-NOTIFICATION-MIB", "snmpNotifyFilterGroup"),))
if mibBuilder.loadTexts:
    snmpNotifyBasicFiltersCompliance.setDescription(
        'The compliance statement for SNMP entities which implement\n         SNMP Unconfirmed-Class notifications with filtering, and\n         read-create operations on all related tables.')
snmpNotifyFullCompliance = ModuleCompliance((1, 3, 6, 1, 6, 3, 13, 3, 1, 3)).setObjects(*(
    ("SNMP-TARGET-MIB", "snmpTargetBasicGroup"), ("SNMP-TARGET-MIB", "snmpTargetResponseGroup"),
    ("SNMP-NOTIFICATION-MIB", "snmpNotifyGroup"), ("SNMP-NOTIFICATION-MIB", "snmpNotifyFilterGroup"),))
if mibBuilder.loadTexts:
    snmpNotifyFullCompliance.setDescription(
        'The compliance statement for SNMP entities which either\n         implement only SNMP Confirmed-Class notifications, or both\n         SNMP Unconfirmed-Class and Confirmed-Class notifications,\n         plus filtering and read-create operations on all related\n         tables.')
snmpNotifyGroup = ObjectGroup((1, 3, 6, 1, 6, 3, 13, 3, 2, 1)).setObjects(*(
    ("SNMP-NOTIFICATION-MIB", "snmpNotifyTag"), ("SNMP-NOTIFICATION-MIB", "snmpNotifyType"),
    ("SNMP-NOTIFICATION-MIB", "snmpNotifyStorageType"), ("SNMP-NOTIFICATION-MIB", "snmpNotifyRowStatus"),))
if mibBuilder.loadTexts:
    snmpNotifyGroup.setDescription(
        'A collection of objects for selecting which management\n         targets are used for generating notifications, and the\n         type of notification to be generated for each selected\n         management target.')
snmpNotifyFilterGroup = ObjectGroup((1, 3, 6, 1, 6, 3, 13, 3, 2, 2)).setObjects(*(
    ("SNMP-NOTIFICATION-MIB", "snmpNotifyFilterProfileName"),
    ("SNMP-NOTIFICATION-MIB", "snmpNotifyFilterProfileStorType"),
    ("SNMP-NOTIFICATION-MIB", "snmpNotifyFilterProfileRowStatus"), ("SNMP-NOTIFICATION-MIB", "snmpNotifyFilterMask"),
    ("SNMP-NOTIFICATION-MIB", "snmpNotifyFilterType"), ("SNMP-NOTIFICATION-MIB", "snmpNotifyFilterStorageType"),
    ("SNMP-NOTIFICATION-MIB", "snmpNotifyFilterRowStatus"),))
if mibBuilder.loadTexts:
    snmpNotifyFilterGroup.setDescription(
        'A collection of objects providing remote configuration\n         of notification filters.')
mibBuilder.exportSymbols("SNMP-NOTIFICATION-MIB", snmpNotifyBasicCompliance=snmpNotifyBasicCompliance,
                         snmpNotifyEntry=snmpNotifyEntry, snmpNotifyFilterType=snmpNotifyFilterType,
                         snmpNotifyConformance=snmpNotifyConformance, snmpNotifyFilterGroup=snmpNotifyFilterGroup,
                         snmpNotifyFilterTable=snmpNotifyFilterTable, PYSNMP_MODULE_ID=snmpNotificationMIB,
                         snmpNotifyFilterMask=snmpNotifyFilterMask, snmpNotifyFullCompliance=snmpNotifyFullCompliance,
                         snmpNotifyFilterProfileEntry=snmpNotifyFilterProfileEntry,
                         snmpNotifyFilterProfileRowStatus=snmpNotifyFilterProfileRowStatus,
                         snmpNotifyFilterProfileStorType=snmpNotifyFilterProfileStorType,
                         snmpNotifyFilterRowStatus=snmpNotifyFilterRowStatus,
                         snmpNotifyBasicFiltersCompliance=snmpNotifyBasicFiltersCompliance,
                         snmpNotifyFilterProfileTable=snmpNotifyFilterProfileTable, snmpNotifyType=snmpNotifyType,
                         snmpNotifyTag=snmpNotifyTag, snmpNotifyName=snmpNotifyName,
                         snmpNotifyObjects=snmpNotifyObjects, snmpNotifyGroup=snmpNotifyGroup,
                         snmpNotifyGroups=snmpNotifyGroups, snmpNotifyRowStatus=snmpNotifyRowStatus,
                         snmpNotifyFilterProfileName=snmpNotifyFilterProfileName,
                         snmpNotificationMIB=snmpNotificationMIB, snmpNotifyFilterSubtree=snmpNotifyFilterSubtree,
                         snmpNotifyStorageType=snmpNotifyStorageType, snmpNotifyCompliances=snmpNotifyCompliances,
                         snmpNotifyFilterStorageType=snmpNotifyFilterStorageType,
                         snmpNotifyFilterEntry=snmpNotifyFilterEntry, snmpNotifyTable=snmpNotifyTable)
