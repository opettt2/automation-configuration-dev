# from pysnmp.hlapi.v3arch.asyncio import *
# import time
from pysnmp.hlapi import *
import time

# Target device
COMMUNITY = 'lab'
OID = '1.3.6.1.2.1.1.1.0' 

#Test Settings
ITERATIONS = 5
DELAY = 1

for i in range (ITERATIONS):
    errorIndication, errorStatus, errorIndex, varBinds=next(getCmd(SnmpEngine(),
               CommunityData(COMMUNITY,mpModel=1),
               UdpTransportTarget(('192.168.100.1', 161), timeout=2, retries=1),
               ContextData(),
               ObjectType(ObjectIdentity(OID)))
    )

    if errorIndication:
        print(f"[{i+1}] Error: {errorIndication}")
    elif errorStatus:
        print(f"[{i+1}] SNMP Error: {errorStatus.prettyPrint()}")
    else:
        for varBind in varBinds:
            print(f"[{i+1}] Response: {varBind}")
    time.sleep(DELAY)