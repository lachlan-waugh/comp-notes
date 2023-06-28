# Memory forensics

> Malware can hide (encrypting, rootkits, packing), but at some point it needs to execute (run)

- Particularly in the case of remote access, it must continue to run (to receive commands) 
- It's therefore a critical gateway for attacking success, and a good place to look 

&nbsp;

### What's in memory 

- Fragments of non-volatile data (MFT, files , registry, event logs) 
- Recently executed terminal commands 
- Running processes 
- Drivers, daemons, system code 
- Passwords, keys, security information 
- Clear text fragments 

&nbsp;

### Memory (RAM)

> is volatile, you can't capture it after the computer is shut down 

- Create a plan of action before attending site/commencing response (consider if memory needed) 
- There are alternate sources of memory on cold machine image, but not reliable 

&nbsp;

### Physical and virtual memory 

- vmem provides a consistent view of memory, regardless of # of processes running 
- Non-resident memory is stored in the pagefile 

&nbsp;
&nbsp;

## Other sources of memory 

### Hiber files

> when a computer hibernates, it dumps copy of physical memory to disk to  allow restoration to same state as when it initiated hibernation. 

- This dump is stored in hiberfil.sys (not deleted when machine restored to running state) 
- (stored in proprietary format, tools can convert to raw format for other applications) 

&nbsp;

### Page file (swap file)

> on disk location holding memory that's been paged out of physical 

- Not a memory dump, doesn't retain structure present of a physical memory dump 
- A collection of the gaps in physical memory 
- Can't parse like regular memory dump, can contain important info (e.g. fragments) 

&nbsp;

### Virtualization 

- Many provide mechanism to obtain copy of memory without running program on host 
- e.g. VMWare machine suspended -> raw memory written to disk in .vmem file 

&nbsp;

### Acquiring memory

> hard to do when the machine is live, as you don't want to change the state 

- Therefore, you need to document, it's impossible not to change, but explain that/how you did 
- Follow a stringent methodology to ensure you don't modify it too much 

&nbsp;
&nbsp;

### tools 

| Tool              | Usage |
| ----------------- | ----- |
| FTK imager        | TODO  |
| redline collector | TODO  |
| dd/windd          | TODO  |
| powershell        | TODO  |

&nbsp;

### considerations 

- Need admin privileges 
- Taking full disk image after memory, don't run forensic tools/store image on that drive 
- Ensure memory storage device (e.g. USB) has more space than RAM (it isn't compressed) 

&nbsp;

### FTK Imager Lite (GUI-based tool) 

- Creates standard raw dd style images that can be used in most analysis tools 
- Suitable for most cases, but not the smallest footprint 

&nbsp;
&nbsp;

## Redline 

### Collectors

>  deployed as a set list of commands to run (gives you a portable package) 

- More replicable, so easy to prove how you obtained any evidence found 
- Can do a lot more than just acquire memory 

&nbsp;

### Analysis approach

> Redline is good for first 3, but use volatility for 4, 5 (if not all)

| Step                         | Process                                                      |
| ---------------------------- | ------------------------------------------------------------ |
| Processes                    | Investigate and  look for  processes that  are out of place. |
| Handles & DLLs               | Identify  suspicious  handles to files,  registry, etc       |
| Ports & Network              | Look for  suspicious  connections to  unknown or  external  network  locations. |
| Signs of Code  Injection     | Look for signs  that code has  been injected  into legitimate  processes |
| Signs Of  Rootkits           | Look for signs  of Rootkit hiding  techniques.               |
| Export for  Further Analysis | Export out any  processes or DLL that were identified during  the previous  steps for in-depth malware  analysis. |

&nbsp;

### processes in memory

> stored in EPROCESS blocks in memory (containing metadata about them) 

- Process name, ID, parent ID, creation time, exit time, addresses of resources 
- Stored as a doubly linked list 
- Terminated processes are unlinked, can remain in memory for a time (to recover them) 
- Malware/rootkit authors manually unlike process (Direct Kernel Object Manipulation) 
  - Therefore you can search for unlinked processes 

&nbsp;
&nbsp;

## looking for suspicious stuff 

### processes

- Obfuscate names/paths (drop malware in system location and give it a legitimate name) 
- Misspelled versions of proper system processes 
- Processes with proper system names, that have spawned from the wrong location 
- Duplicate processes that should only be spawned once 
- Processes that have a parent they shouldn't 
- Sys processes with start time much later in life (find processes started at same time) 
- System processes running under a user account (check the SID) 
- Cheat sheet [here](https://digital-forensics.sans.org/media/poster_2014_find_evil.pdf)

&nbsp;

### memory objects

> malware authors may hijack processes rather than start their own 

- DLLs: can side-load/inject DLLs into existing process
- Handlers: malware keeps handles to files, directories, sockets, registry keys,  mutexs and semaphores it needs to run. Check if any of these are  abnormal
- Threads: may create new threads within process space of running process
- Indicators of compromise: redline can load IOCs to assist in analysis process. (e.g. artefacts)
- Frequency of least occurrence: highly likely that MOs referenced by malware will  be referenced far less than normal system objects. Count the amount of  references to MOs

&nbsp;

### network activity 

- processes
- ports
- connections
- connection time
- external IP addresses
- internal IP

&nbsp;
&nbsp;

## volatility 

### process hollowing

> when a legitimate process is duplicated in a suspend state, and has its executable memory replaced with malicious code, then resumes process 
