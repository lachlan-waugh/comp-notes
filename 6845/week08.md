# mobile foreniscs and metadata

## Role of an investigator 
* Investigators are expected to make a reasonable effort to discover both incriminating and exculpatory evidence 
* Courts have come to expectation that common digital forensic capabilities are reasonable (especially for police and agencies) 
* Most jurisdictions have rules for disclosure (both for criminal and civil cases), you shouldn't just show up with new evidence on the day 
* Experts are expected to be able to explain mobile evidence, and persuade decision maker 

&nbsp;

### Types of phones 
![](./img/week02/mobiles.png)

&nbsp;

### Challenges of having many phones
> most times you won't just be given one phone
* Typically you'll have multiple types of phones (not always in corporate e-discovery) 
* Data consistency (data elements, meaning of messages, time formats)
* Working out why something is missing, or doesn't match 

&nbsp;
&nbsp;

## Extracting data from iPhones and iPads

| iTunes backup           | Generally the best method<br />Then extract artefacts        |
| ----------------------- | ------------------------------------------------------------ |
| **Logical extraction**  | PhoneView<br />iPhone Explorer                               |
| **Physical extraction** | Cellebrite have stopped supporting physical extraction for iPhones<br />1. Jailbreak<br />2. connect to shell<br />3. dd copy<br />Still not uncommon to forensically examine phones where this works |

&nbsp;

### iPhone backups 
* Discover them on computer, storage, or iCloud (subpoena Apple) 
* Create backup onto pre-pared forensic workstation 
* Many tools to view/save artefacts 
* Reincubate iPhone Backup Extractor (Windows), PhoneView (Mac) 
* iExplorer 
* Forensic Explorer 

&nbsp;

### Key artefacts

| .sqlite, .sqlitedb, .db         | notes                          | voicemail                  |
| ------------------------------- | ------------------------------ | -------------------------- |
| accounts3, truststore           | bookmarks (safari),            | photos (e.g. in DCIM)      |
| addressbook(images)?            | mobilesafari history           | locationd                  |
| calendar, extras, notifications | cfurl - spotlight autocomplete | cellular usage, data usage |
| callhiostorydb                  | sms, mms, facetime             | app specific dbs           |

* Forensic software has tools to parse iOS artefacts (Encase, FTK, Forensic explorer) 
* Cheap/opensource tools exist ($50-300 range if you provide the correct license) 
* Open source (e.g. Santuko Linux) 
* ILEAP/ALEAP 

&nbsp;

### Extracting data from Android phones 
1. Connect to the phone: with ADB (Android developer/debug bridge), or toolkits
2. Must root the phone (equivalent of jailbreaking)
> Framaroot, TowelRoot, ActiveRoot, KingoRoot, SuperOneClick 

3. Then copy the data through a shell (e.g. partition with dd, or only selected artefacts)

&nbsp;

### Key artefacts 
> Usually .db, but brand (sometimes model) specific

* Many manufacturers back their phones up to the Cloud (e.g. Samsung & HTC) 
* Backup software: e.g. Samsung Kies or Smartswitch, or 3rd party (Easy backup/Titanium)

&nbsp;

### Common files
* mms/sms
* telephony
* contacts, contacts2
* photos, pictures
* app specific ones (e.g. /data/data/com.android/chrome)
* cached files

&nbsp;

Allows extraction and analysis
> The manufacturer worries data consistency, reliability and providing up-to-date jailbreak or root

Popular commercial tools
* cellebrite uFED
* MSAB xay
* Encase mobile investigator
* Oxygen Detective
* Axiom Magnet
* Elcommsott
* Blackbag Blacklight

&nbsp;

Need to decide whether you are going to rely on output of a process, machine or device
> Even so, can you withstand a challenge by an expert engaged by the adversary?

&nbsp;

Make a habit of using two tools: the one used by the other expert, and another ones, allows you to:
1. arrive at the same result (reliable)
2. explain the differences
3. use as evidence of unreliable evidence

&nbsp;

### Spoiling and tampering with phone evidence 
* Spoiling: accidentally ruining evidence 
* Tampering: intentionally ruining evidence 
* Deletion, and editing photos is common 
* Fake messages, or sender/recipients (e.g. by editing contacts)



&nbsp;

&nbsp;

# Extended
> Seizing/analysing mobiles devices is often done regardless of the focus of the investigation 

&nbsp;

## Types of mobile devices

### Dumb phones
> from 80s - 00s (those without capability of modern smart devices) 

- Uncommon but still exist (they're cheap), usually in criminal not corporate scenarios 
- Evidence: SMS, Call logs, contacts, basic internet/calendar/email/photos 

&nbsp;

### Early model smartphones

> from early 00's (pre-iPhone smartphones) 

- Multiple platforms: Symbian, Windows CE, Palm pilot, Blackberry 
- Evidence: As above + user files, GPS location data. Limited 3rd party App data 

&nbsp;

### Current era smartphones

> iPhone onwards 

- 99% of them are either Android or iPhone (72% android globally, varying by region) 
- Corporate scenarios, you may have a fleet (everyone has the same style of phone) 
- Evidence: As above + cell/assistive location data, **extensive** 3rd party app data 

&nbsp;

### Other smart devices

> tablets (e.g. iPad, Android tablets) 

- No different to regular mobile devices with larger screens 
- Less obvious: point of sale smart terminals, in car systems, GPS units 

&nbsp;

### Preparing for seizure 

- Mobile devices have wireless radios, physical isolation isn't sufficient (remote wipe?) 
  - Android Device Manager and Find My iPhone can remote wipe 
  - Someone could send a text message (e.g. overwriting other data) or call the device 
  - The device could sync with online accounts 
- Many phones can be difficult to completely power down (e.g. they start up for alarms) 
- Encryption is typically always enabled for modern smartphones 

&nbsp;

### Isolation techniques 

| **Approach** | **Power down** | **Remove SIM** | **Airplane mode** | **Faraday bag** |
| ------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| **Desc**     | Powering off the device completely                           | Removing the SIM card from the device                        | Disable wireless radios using mobile settings                | Using a big which blocks wireless radio frequencies          |
| **Pros**     | Good chain of custody, phone isn't running in possession     | Ensure phone can't connect to mobile networks                | Alternative when faraday bags are unavailable/not practical  | Useful when device can't be turned off. Often have windows that allow analysis to be undertaken |
| **Cons**     | Mobile devices need to be powered on to acquire. Risk device will reconnect. Not all devices can be easily shut off | Doesn't deal with secondary radio Some phones can't operate with SIM Phone mightn't use a physical SIM (eg. eSIM) | Requires you to handle phone at seizure, adding a little more to process to record/document those changes You're changing the device state | Size of the mouth of the bag. You need a bag larger than the device How many do you bring If the device is removed, it may reconnect |
| **Consider** | Ensure removing power doesn't cause adverse affects on phone Is phone powered down, or in low power state? |                                                              | Make sure you know what's disabled with Airplane mode. You may need to disable some separately. | Test it before use, make sure it blocks all radios, not just mobile call/data. Cheaper bags may not be as good |

 

## Types of acquisitions 

### Logical acquisitions

>  normally taken when physical disk isn't available for bit-by-bit copy 

- Method used to obtain it varies from phone to phone 
  - Phone backups (Android/iPhone) 
  - Agents (Java enabled dumbphones, symbian, some android phones) 
  - Manufacturer interface (Dumbphones) 
- Deleted files are generally not available (you're using the phone to get its own data) 

 

### Physical acquisition

> obtaining full sector-by-sector image of the flash memory on the phone 

- Preferred if possible, they contain deleted data from unallocated space (the entire FS) 
- Impossible to acquire without jailbreaking/rooting (techniques: bootloaders & chip off) 

 

### SIM acquisition and SIM cloning 

- Most modern devices don't store information on the SIM (some older ones do) 
- For phones that require SIM to operate, may need to create a clone of the SIM 
- Clone mirrors information stored on it, without network connectivity (can then boot) 



### Memory card acquisition 

- Can be larger than the onboard storage (adding a lot of time to the process) 
- Removing it and acquiring through normal means can be a better option 
- If it's encrypted, you'll have to acquire with it in 

 

## Challenges 

### Passwords and encryption

> the largest challenge facing mobile investigations 

- iPhones now require: phone pin, iTunes backup password, and making PC trusted device 
- e.g. The San Bernardino Case 

 

### Forensic process

the phone needs to be powered on, and code needs to be run on it 

- Changes the state of the device (can't use a write-blocker) 
- what counts as a mobile devices (the lines are a bit blurred) 

 

### Analysis approaches 

| **High level** | Analyse entire phone image using tools which parse system/app data Good as a starting point, shows you multiple evidence locations Essentially push-button forensics |
| -------------- | ------------------------------------------------------------ |
| **Targeted**   | Low level analysis of particular app/database Focus on internals of specific app Mostly used in malware investigations/incident response More focused on workings of app, not communications |

 

## High level analysis 

### Application data 

- Installed applications 

 q

### Location data

> many applications/the OS store location metadata 

- Camera images, tweets/social media, cell tower data, Wi-Fi locations 
