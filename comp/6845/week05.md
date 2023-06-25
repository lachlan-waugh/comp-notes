# Network Forensics and Windows Artefacts

## Network forensics

### Uses

* command and control (c2) traffic
* breach detection
* finding what was stolen
* finding patient zero



### Barriers

* Encryption
* data size + retention
* Where to perform the capture



### Output

* pcap (packet capture, or libpcap) API capturing live packets from OSI 2-7 pcapng is pcap next generation (contains a bit more information)

 

### WireShark

> A packet sniffer/analysis tool. Captures traffic on LAN and stores for analysis Can have billions of queries, need to use filters to limit amount of data



### Virus total

> Can be useful to find malicious IPs ([found here](https://www.virustotal.com/gui/))

 

### MAC address

> Media Access Control: a unique ID assigned to NIC for use within network segment Can be spoofed, not definitive proof User agent of packet can say the OS



### Cloud

> Cloud logging adds a rich source of data (VPC flow logs, network telemetry, network watcher) 



### Registry Hives

> In general, there are the following registry files, known as "hives" on a Windows machine.

| Hive       | Description                                                  |
| ---------- | ------------------------------------------------------------ |
| SAM        | Security Accounts Manager, contains user and group membership info. |
| SYSTEM     | contains information about the Windows system setup, the list of currently  mounted devices containing a filesystem, configurations for system hardware drivers and  services running on the local system. |
| SOFTWARE   | contains software and Windows settings. It is mostly modified by application  and system installers |
| SECURITY   | The kernel will access it to read and enforce the security policy applicable to the  current user and all applications or operations executed by this user.  The is also a per user hive |
| NTUSER.dat | A per-user hive                                              |



### Hive locations 

- NTUSER.dat is stored in C:\Users\<username>\NTUSER.dat 
- The other hives are in C:\Windows\System32\config\<hivename> 



### OS version

> HKLM\Software\Microsoft\WindowsNT\CurrentVersion 

- if OS installed recently, could indicate it was wiped 
- Keys of note: Product name, Registered Organisation, Registered Owner, System Root, Install Date (UNIX) 



### Control set

> HKLM\System\ControlSet###\ControlKey 

- Says which configuration that the computer is running under 



### Timezones

> HKLM\SYSTEM\ControlSet###\Control\TimeZoneInformation 

- Keys of note: TimeZoneKeyName, Bias, DaylightBias, ActiveTimeBias 
- Time information is also stored in BIOS time (helps account for BIOS time skew)



### Computer name

> HKLM\SYSTEM\ControlSet###\Control\ComputerName\ComputerName
>
> HKLM\SYSTEM\ControlSet###\Services\Tcpip\Parameters 

- TCP/IP key contains network information which may help determine what network settings were in use at the time of imaging. 

 

### User accounts

> HKLM\SAM\Domains\Accounts\Users 

* SAM isn't accessible to users normally 



### SAM stores F and V keys 

|        | F value                     |        | V value               |
| ------ | --------------------------- | ------ | --------------------- |
| Field  | Name                        | Field  | Name                  |
| `0x00` | Time of lockout             | `0x00` | Account offset        |
| `0x08` | Time of account creation    | `0x04` | Account length        |
| `0x10` | Time of last login          | `0x08` | Full username         |
| `0x18` | RID                         | `0x0C` | Full username length  |
| `0x1C` | Account type of status      | `0x10` | Comment               |
| `0x1E` | Count of failed logins      | `0x14` | Comment length        |
| `0x20` | Total logins since creation | `0x18` | Home directory        |
|        |                             | `0x1C` | Home directory length |
|        |                             | `0x28` | LM hash offset        |
|        |                             | `0x2C` | LM hash length        |
|        |                             | `0x30` | NTLM hash offset      |
|        |                             | `0x34` | NTLM hash length      |



## Evidence of USB usage 

> Where to look



### USBStor

> SYSTEM\ControlSet###\Enum\USBSTOR (non storage are in \USB). 

- All devices plugged into system 
- shows connect time, model, serial, and mount points 

 

### Plug and play log

> C:\Windows\setupapi.log (XP)
>
> C:\Windows\inf\setupapi.dev.log (W7) 

- Searching USB serial number in USBSTOR will locate its installation log 
- Shows when device was first attached 



### MountedDevices

> SYSTEM\ControlSet###\MountedDevices 

- Mapping between USB Device/Logoical Volume GUIDs, or USB Device/DOS Drive letters 
- We can see what drive letter the USB device was assigned to 

 

### MountPoints2

> NTUSER.DAT\Software\Microsoft\Windows\CurrentVersion\Explorer\MountPoints2

- See which user loaded the device 

 

### Link files

> small shortcut files used by windows for features like "Recent files" 

- Created when a file is opened with Windows Explorer, and have a .lnk extension.

- Contain original full path/filename (drive letter/network)

- Timestamps of target file

- External drives shows volume serial number of drive

- Find them in "recents" folder:

  > C:\Users\<user>\AppData\Roaming\Microsoft\Windows\Recent 



### Evidence of execution 

> Prefetch files: C:\Windows\Prefetch 

- Contains name of exe, unicode list of DLLs, # of runs, timestamp of last run 

 

### UserAsst
> NTUSER.DAT\Software\Microsoft\Windows\CurrentVersion\Explorer\UserAssist\{GUID}\Count 

- Contains: number of executions, last execution date and time 
- *Only contains data about applications launched by windows explorer* 
