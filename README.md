# 🛠️ Network Automation & SNMP Monitoring (Python)

This project demonstrates basic network automation and SNMP monitoring using Python.  
It retrieves device information via SNMP and automates VLAN + IP configuration through SSH.

---

## ✅ Features

- SNMP GET system information (sysDescr OID)
- SSH login using Netmiko
- Create VLAN + assign IP
- Display VLAN and IP status

---

## 📦 Tech Used

- Python
- `pysnmp`
- `netmiko`
- `paramiko`
- Tested on HP ProCurve switch (compatible with MikroTik/Cisco with small changes)

---

## 🧪 What the script does

1. Polls device via SNMP (`1.3.6.1.2.1.1.1.0`)
2. Connects via SSH
3. Creates VLAN 20
4. Assigns IP `192.168.200.1/26`
5. Shows VLAN & IP info

---

## 🧯 Notes & Compatibility

- Designed for learning environment / lab use
- Device tested: HP ProCurve (compatible with MikroTik / Cisco with config adjustments)
- SNMPv2 used (not secure for production)
- SSH key negotiation adjustments included for older switches

## 👤 Author

Faith Greatfull Samuel Taressy
📧 faithtaressy043@gmail.com
🔗 LinkedIn: https://www.linkedin.com/in/faithtaressy
