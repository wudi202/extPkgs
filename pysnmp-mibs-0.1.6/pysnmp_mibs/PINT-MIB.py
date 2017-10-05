#
# PySNMP MIB module PINT-MIB (http://pysnmp.sf.net)
# ASN.1 source http://mibs.snmplabs.com:80/asn1/PINT-MIB
# Produced by pysmi-0.0.7 at Sun Feb 14 00:23:46 2016
# On host bldfarm platform Linux version 4.1.13-100.fc21.x86_64 by user goose
# Using Python version 3.5.0 (default, Jan  5 2016, 17:11:52) 
#
( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( NamedValues, ) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
( ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ) = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
( SnmpAdminString, ) = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
( ObjectGroup, NotificationGroup, ModuleCompliance, ) = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
( Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Gauge32, TimeTicks, ObjectIdentity, Counter32, MibIdentifier, mib_2, IpAddress, Integer32, Counter64, iso, Bits, ModuleIdentity, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Gauge32", "TimeTicks", "ObjectIdentity", "Counter32", "MibIdentifier", "mib-2", "IpAddress", "Integer32", "Counter64", "iso", "Bits", "ModuleIdentity")
( TextualConvention, DisplayString, ) = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
( sysApplInstallPkgEntry, ) = mibBuilder.importSymbols("SYSAPPL-MIB", "sysApplInstallPkgEntry")
pintMib = ModuleIdentity((1, 3, 6, 1, 2, 1, 93)).setRevisions(("2001-02-01 00:00",))
if mibBuilder.loadTexts: pintMib.setLastUpdated('200102010000Z')
if mibBuilder.loadTexts: pintMib.setOrganization('IETF PINT Working Group')
if mibBuilder.loadTexts: pintMib.setContactInfo('\n        Chairs:  Steve Bellovin\n                    E-mail: smb@research.att.com\n\n                    Igor Faynberg\n                    E-mail: faynberg@lucent.com\n\n        Authors: Murali Krishnaswamy\n                     Postal: 20 Corporate Place South\n                                Piscataway, NJ 08854\n                                Tel:    +1 (732)465-1000\n\n                                E-mail: murali@photuris.com\n\n                                Dan Romascanu\n                                Postal: Atidim Technology Park, Bldg 3\n                                Tel Aviv, Israel\n                                Tel:    +972 3 6458414\n                                E-mail: dromasca@avaya.com\n\n        General Discussion:pint@lists.bell-labs.com\n        To Subscribe: pint-request@lists.bell-labs.com\n        In Body: subscribe your-email-addres\n        Archive: http://www.bell-labs.com/mailing-lists/pint/\n        ')
if mibBuilder.loadTexts: pintMib.setDescription('This MIB defines the objects necessary to monitor\n     PINT Services')
class PintServiceType(Integer32, TextualConvention):
    subtypeSpec = Integer32.subtypeSpec+ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4,))
    namedValues = NamedValues(("r2C", 1), ("r2F", 2), ("r2FB", 3), ("r2HC", 4),)

class PintPerfStatPeriod(Integer32, TextualConvention):
    subtypeSpec = Integer32.subtypeSpec+ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4,))
    namedValues = NamedValues(("last30sec", 1), ("last15min", 2), ("last24Hr", 3), ("sinceReboot", 4),)

pintServerConfig = MibIdentifier((1, 3, 6, 1, 2, 1, 93, 1))
pintServerMonitor = MibIdentifier((1, 3, 6, 1, 2, 1, 93, 2))
pintMibConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 93, 3))
pintReleaseNumber = MibScalar((1, 3, 6, 1, 2, 1, 93, 1, 1), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pintReleaseNumber.setDescription('An indication of version of the PINT protocol supported\n     by this agent.')
pintSysContact = MibScalar((1, 3, 6, 1, 2, 1, 93, 1, 2), SnmpAdminString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pintSysContact.setDescription('Contact information related to the administration of the PINT\n     services.')
pintApplInstallPkgTable = MibTable((1, 3, 6, 1, 2, 1, 93, 1, 3), )
if mibBuilder.loadTexts: pintApplInstallPkgTable.setDescription('Table describing the PINT applications that are installed.')
pintApplInstallPkgEntry = MibTableRow((1, 3, 6, 1, 2, 1, 93, 1, 3, 1), )
sysApplInstallPkgEntry.registerAugmentions(("PINT-MIB", "pintApplInstallPkgEntry"))
pintApplInstallPkgEntry.setIndexNames(*sysApplInstallPkgEntry.getIndexNames())
if mibBuilder.loadTexts: pintApplInstallPkgEntry.setDescription('Entries per PINT Application.')
pintApplInstallPkgDescription = MibTableColumn((1, 3, 6, 1, 2, 1, 93, 1, 3, 1, 1), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pintApplInstallPkgDescription.setDescription('Textual description of the installed PINT application.')
pintRegisteredGatewayTable = MibTable((1, 3, 6, 1, 2, 1, 93, 1, 4), )
if mibBuilder.loadTexts: pintRegisteredGatewayTable.setDescription('Table describing the registered gateway applications.')
pintRegisteredGatewayEntry = MibTableRow((1, 3, 6, 1, 2, 1, 93, 1, 4, 1), )
sysApplInstallPkgEntry.registerAugmentions(("PINT-MIB", "pintRegisteredGatewayEntry"))
pintRegisteredGatewayEntry.setIndexNames(*sysApplInstallPkgEntry.getIndexNames())
if mibBuilder.loadTexts: pintRegisteredGatewayEntry.setDescription('Entries per Registered Gateway Application.')
pintRegisteredGatewayName = MibTableColumn((1, 3, 6, 1, 2, 1, 93, 1, 4, 1, 1), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pintRegisteredGatewayName.setDescription('Name of the registered gateway.')
pintRegisteredGatewayDescription = MibTableColumn((1, 3, 6, 1, 2, 1, 93, 1, 4, 1, 2), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pintRegisteredGatewayDescription.setDescription('Textual description of the registered gateway.')
pintServerGlobalPerf = MibIdentifier((1, 3, 6, 1, 2, 1, 93, 2, 1))
pintServerClientPerf = MibIdentifier((1, 3, 6, 1, 2, 1, 93, 2, 2))
pintServerUserIdPerf = MibIdentifier((1, 3, 6, 1, 2, 1, 93, 2, 3))
pintServerGatewayPerf = MibIdentifier((1, 3, 6, 1, 2, 1, 93, 2, 4))
pintServerGlobalStatsTable = MibTable((1, 3, 6, 1, 2, 1, 93, 2, 1, 1), )
if mibBuilder.loadTexts: pintServerGlobalStatsTable.setDescription('Table displaying the monitored global server statistics.')
pintServerGlobalStatsEntry = MibTableRow((1, 3, 6, 1, 2, 1, 93, 2, 1, 1, 1), ).setIndexNames((0, "PINT-MIB", "pintServerServiceTypeIndex"), (0, "PINT-MIB", "pintServerPerfStatPeriodIndex"))
if mibBuilder.loadTexts: pintServerGlobalStatsEntry.setDescription('Entries in the global statistics table.\n     One entry is defined for each monitored service type and\n     performance statistics collection period.')
pintServerServiceTypeIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 93, 2, 1, 1, 1, 1), PintServiceType())
if mibBuilder.loadTexts: pintServerServiceTypeIndex.setDescription('The unique identifier of the monitored service.')
pintServerPerfStatPeriodIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 93, 2, 1, 1, 1, 2), PintPerfStatPeriod())
if mibBuilder.loadTexts: pintServerPerfStatPeriodIndex.setDescription('Time period for which the performance statistics are requested\n     from the pint server.')
pintServerGlobalCallsReceived = MibTableColumn((1, 3, 6, 1, 2, 1, 93, 2, 1, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pintServerGlobalCallsReceived.setDescription('Number of received global calls.')
pintServerGlobalSuccessfulCalls = MibTableColumn((1, 3, 6, 1, 2, 1, 93, 2, 1, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pintServerGlobalSuccessfulCalls.setDescription('Number of global successful calls.')
pintServerGlobalDisconnectedCalls = MibTableColumn((1, 3, 6, 1, 2, 1, 93, 2, 1, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pintServerGlobalDisconnectedCalls.setDescription('Number of global disconnected (failed) calls.')
pintServerGlobalDisCUAutFCalls = MibTableColumn((1, 3, 6, 1, 2, 1, 93, 2, 1, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pintServerGlobalDisCUAutFCalls.setDescription('Number of global calls that were disconnected because of client\n    or user authorization failure.')
pintServerGlobalDisServProbCalls = MibTableColumn((1, 3, 6, 1, 2, 1, 93, 2, 1, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pintServerGlobalDisServProbCalls.setDescription('Number of global calls that were disconnected because of\n     server problems.')
pintServerGlobalDisGatProbCalls = MibTableColumn((1, 3, 6, 1, 2, 1, 93, 2, 1, 1, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pintServerGlobalDisGatProbCalls.setDescription('Number of global calls that were disconnected because of\n     gateway problems.')
pintServerClientStatsTable = MibTable((1, 3, 6, 1, 2, 1, 93, 2, 2, 1), )
if mibBuilder.loadTexts: pintServerClientStatsTable.setDescription('Table displaying the monitored server client statistics.')
pintServerClientStatsEntry = MibTableRow((1, 3, 6, 1, 2, 1, 93, 2, 2, 1, 1), ).setIndexNames((0, "PINT-MIB", "pintServerClientAddress"), (0, "PINT-MIB", "pintServerServiceTypeIndex"), (0, "PINT-MIB", "pintServerPerfStatPeriodIndex"))
if mibBuilder.loadTexts: pintServerClientStatsEntry.setDescription('Entries in the client server statistics table.\n     One entry is defined for each client identified by name,\n     monitored service type and performance statistics collection\n     period.')
pintServerClientAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 93, 2, 2, 1, 1, 1), SnmpAdminString())
if mibBuilder.loadTexts: pintServerClientAddress.setDescription('The unique identifier of the monitored client\n     identified by its address represented as as a string.')
pintServerClientCallsReceived = MibTableColumn((1, 3, 6, 1, 2, 1, 93, 2, 2, 1, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pintServerClientCallsReceived.setDescription('Number of calls received from the specific client.')
pintServerClientSuccessfulCalls = MibTableColumn((1, 3, 6, 1, 2, 1, 93, 2, 2, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pintServerClientSuccessfulCalls.setDescription('Number of calls from the client successfully completed.')
pintServerClientDisconnectedCalls = MibTableColumn((1, 3, 6, 1, 2, 1, 93, 2, 2, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pintServerClientDisconnectedCalls.setDescription('Number of calls received from the client, and that were\n     disconnected (failed).')
pintServerClientDisCAutFCalls = MibTableColumn((1, 3, 6, 1, 2, 1, 93, 2, 2, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pintServerClientDisCAutFCalls.setDescription('Number of calls from the client that were disconnected because of\n    client authorization failure.')
pintServerClientDisEFProbCalls = MibTableColumn((1, 3, 6, 1, 2, 1, 93, 2, 2, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pintServerClientDisEFProbCalls.setDescription('Number of calls from the client that were disconnected because\n     of egress facility problems.')
pintServerUserIdStatsTable = MibTable((1, 3, 6, 1, 2, 1, 93, 2, 3, 1), )
if mibBuilder.loadTexts: pintServerUserIdStatsTable.setDescription('Table displaying the monitored Pint service user statistics.')
pintServerUserIdStatsEntry = MibTableRow((1, 3, 6, 1, 2, 1, 93, 2, 3, 1, 1), ).setIndexNames((0, "PINT-MIB", "pintServerUserIdName"), (0, "PINT-MIB", "pintServerServiceTypeIndex"), (0, "PINT-MIB", "pintServerPerfStatPeriodIndex"))
if mibBuilder.loadTexts: pintServerUserIdStatsEntry.setDescription('Entries in the user statistics table.\n     One entry is defined for each user identified by name,\n     each monitored service type and performance statistics collection\n     period.\n\n      It is assumed that the capabilities of the pint server\n      are enough to accommodate the number of entries in this table.\n      It is a local server implementation issue if an aging mechanism\n      Is implemented in order to avoid scalability problems.')
pintServerUserIdName = MibTableColumn((1, 3, 6, 1, 2, 1, 93, 2, 3, 1, 1, 1), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0,64)))
if mibBuilder.loadTexts: pintServerUserIdName.setDescription('The unique identifier of the monitored user\n     identified by its name.')
pintServerUserIdCallsReceived = MibTableColumn((1, 3, 6, 1, 2, 1, 93, 2, 3, 1, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pintServerUserIdCallsReceived.setDescription('Number of calls received from the specific user.')
pintServerUserIdSuccessfulCalls = MibTableColumn((1, 3, 6, 1, 2, 1, 93, 2, 3, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pintServerUserIdSuccessfulCalls.setDescription('Number of calls from the user successfully completed.')
pintServerUserIdDisconnectedCalls = MibTableColumn((1, 3, 6, 1, 2, 1, 93, 2, 3, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pintServerUserIdDisconnectedCalls.setDescription('Number of calls received from the user that were\n     disconnected (failed).')
pintServerUserIdDiscUIdAFailCalls = MibTableColumn((1, 3, 6, 1, 2, 1, 93, 2, 3, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pintServerUserIdDiscUIdAFailCalls.setDescription('Number of calls from the user that were disconnected because of\n    user authorization failure.')
pintServerUserIdEFProbCalls = MibTableColumn((1, 3, 6, 1, 2, 1, 93, 2, 3, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pintServerUserIdEFProbCalls.setDescription('Number of calls from the user that were disconnected because of\n     egress facility problems.')
pintServerGatewayStatsTable = MibTable((1, 3, 6, 1, 2, 1, 93, 2, 4, 1), )
if mibBuilder.loadTexts: pintServerGatewayStatsTable.setDescription('Table displaying the monitored gateway statistics.')
pintServerGatewayStatsEntry = MibTableRow((1, 3, 6, 1, 2, 1, 93, 2, 4, 1, 1), ).setIndexNames((0, "PINT-MIB", "pintRegisteredGatewayName"), (0, "PINT-MIB", "pintServerServiceTypeIndex"), (0, "PINT-MIB", "pintServerPerfStatPeriodIndex"))
if mibBuilder.loadTexts: pintServerGatewayStatsEntry.setDescription('Entries in the gateway table.\n     One entry is defined for each gateway identified by name,\n     each monitored service type and performance statistics collection\n     period.')
pintServerGatewayCallsReceived = MibTableColumn((1, 3, 6, 1, 2, 1, 93, 2, 4, 1, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pintServerGatewayCallsReceived.setDescription('Number of calls received at the specified gateway.')
pintServerGatewaySuccessfulCalls = MibTableColumn((1, 3, 6, 1, 2, 1, 93, 2, 4, 1, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pintServerGatewaySuccessfulCalls.setDescription('Number of calls successfully completed at the specified gateway.')
pintServerGatewayDisconnectedCalls = MibTableColumn((1, 3, 6, 1, 2, 1, 93, 2, 4, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pintServerGatewayDisconnectedCalls.setDescription('Number of calls that were disconnected (failed) at the specified\n     gateway.')
pintMibCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 93, 3, 1))
pintMibGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 93, 3, 2))
pintMibCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 93, 3, 1, 1)).setObjects(*(("PINT-MIB", "pintMibConfigGroup"), ("PINT-MIB", "pintMibMonitorGroup"),))
if mibBuilder.loadTexts: pintMibCompliance.setDescription('Describes the requirements for conformance to the\n    PINT MIB.')
pintMibConfigGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 93, 3, 2, 1)).setObjects(*(("PINT-MIB", "pintReleaseNumber"), ("PINT-MIB", "pintSysContact"), ("PINT-MIB", "pintApplInstallPkgDescription"), ("PINT-MIB", "pintRegisteredGatewayName"), ("PINT-MIB", "pintRegisteredGatewayDescription"),))
if mibBuilder.loadTexts: pintMibConfigGroup.setDescription('A collection of objects providing configuration\n    information\n    for a PINT Server.')
pintMibMonitorGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 93, 3, 2, 2)).setObjects(*(("PINT-MIB", "pintServerGlobalCallsReceived"), ("PINT-MIB", "pintServerGlobalSuccessfulCalls"), ("PINT-MIB", "pintServerGlobalDisconnectedCalls"), ("PINT-MIB", "pintServerGlobalDisCUAutFCalls"), ("PINT-MIB", "pintServerGlobalDisServProbCalls"), ("PINT-MIB", "pintServerGlobalDisGatProbCalls"), ("PINT-MIB", "pintServerClientCallsReceived"), ("PINT-MIB", "pintServerClientSuccessfulCalls"), ("PINT-MIB", "pintServerClientDisconnectedCalls"), ("PINT-MIB", "pintServerClientDisCAutFCalls"), ("PINT-MIB", "pintServerClientDisEFProbCalls"), ("PINT-MIB", "pintServerUserIdCallsReceived"), ("PINT-MIB", "pintServerUserIdSuccessfulCalls"), ("PINT-MIB", "pintServerUserIdDisconnectedCalls"), ("PINT-MIB", "pintServerUserIdDiscUIdAFailCalls"), ("PINT-MIB", "pintServerUserIdEFProbCalls"), ("PINT-MIB", "pintServerGatewayCallsReceived"), ("PINT-MIB", "pintServerGatewaySuccessfulCalls"), ("PINT-MIB", "pintServerGatewayDisconnectedCalls"),))
if mibBuilder.loadTexts: pintMibMonitorGroup.setDescription('A collection of objects providing monitoring\n    information\n    for a PINT Server.')
mibBuilder.exportSymbols("PINT-MIB", pintServerMonitor=pintServerMonitor, pintServerGatewayPerf=pintServerGatewayPerf, pintServerUserIdDiscUIdAFailCalls=pintServerUserIdDiscUIdAFailCalls, PintServiceType=PintServiceType, pintMib=pintMib, pintRegisteredGatewayTable=pintRegisteredGatewayTable, pintMibConfigGroup=pintMibConfigGroup, pintServerClientDisCAutFCalls=pintServerClientDisCAutFCalls, pintServerGatewayStatsTable=pintServerGatewayStatsTable, pintServerClientPerf=pintServerClientPerf, pintRegisteredGatewayDescription=pintRegisteredGatewayDescription, pintMibConformance=pintMibConformance, pintServerClientStatsTable=pintServerClientStatsTable, pintServerGlobalStatsEntry=pintServerGlobalStatsEntry, pintMibCompliances=pintMibCompliances, pintServerGlobalDisServProbCalls=pintServerGlobalDisServProbCalls, pintServerUserIdStatsTable=pintServerUserIdStatsTable, pintServerClientStatsEntry=pintServerClientStatsEntry, pintMibMonitorGroup=pintMibMonitorGroup, pintServerGatewayDisconnectedCalls=pintServerGatewayDisconnectedCalls, pintServerGlobalDisconnectedCalls=pintServerGlobalDisconnectedCalls, pintServerGatewayStatsEntry=pintServerGatewayStatsEntry, pintServerGatewayCallsReceived=pintServerGatewayCallsReceived, pintRegisteredGatewayName=pintRegisteredGatewayName, pintApplInstallPkgTable=pintApplInstallPkgTable, pintServerUserIdEFProbCalls=pintServerUserIdEFProbCalls, pintServerClientAddress=pintServerClientAddress, pintServerGlobalStatsTable=pintServerGlobalStatsTable, PintPerfStatPeriod=PintPerfStatPeriod, pintServerClientDisconnectedCalls=pintServerClientDisconnectedCalls, pintMibGroups=pintMibGroups, pintServerClientDisEFProbCalls=pintServerClientDisEFProbCalls, pintServerServiceTypeIndex=pintServerServiceTypeIndex, pintApplInstallPkgEntry=pintApplInstallPkgEntry, pintServerGlobalCallsReceived=pintServerGlobalCallsReceived, pintServerGlobalDisCUAutFCalls=pintServerGlobalDisCUAutFCalls, pintServerGlobalSuccessfulCalls=pintServerGlobalSuccessfulCalls, pintRegisteredGatewayEntry=pintRegisteredGatewayEntry, pintServerUserIdPerf=pintServerUserIdPerf, pintSysContact=pintSysContact, pintApplInstallPkgDescription=pintApplInstallPkgDescription, pintServerUserIdCallsReceived=pintServerUserIdCallsReceived, pintReleaseNumber=pintReleaseNumber, pintServerGlobalDisGatProbCalls=pintServerGlobalDisGatProbCalls, pintServerUserIdDisconnectedCalls=pintServerUserIdDisconnectedCalls, pintServerPerfStatPeriodIndex=pintServerPerfStatPeriodIndex, pintServerUserIdName=pintServerUserIdName, pintServerGatewaySuccessfulCalls=pintServerGatewaySuccessfulCalls, pintServerGlobalPerf=pintServerGlobalPerf, pintServerConfig=pintServerConfig, pintServerUserIdStatsEntry=pintServerUserIdStatsEntry, pintServerClientCallsReceived=pintServerClientCallsReceived, pintServerClientSuccessfulCalls=pintServerClientSuccessfulCalls, pintServerUserIdSuccessfulCalls=pintServerUserIdSuccessfulCalls, pintMibCompliance=pintMibCompliance, PYSNMP_MODULE_ID=pintMib)