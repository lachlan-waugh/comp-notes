# Processing and Timeline Analysis

* [Processing](#processing)
* [Timeline analysis](#timeline-analysis)



## Pre-analysis

### Background intel
* What occurred, and when did it occur?
* What analysis techniques are most likely to uncover relevant information?
* Which should be a priority, which order does it make sense to run them?

> You don't have an unlimited amount of time to run your investigation

&nbsp;

### Processing
* If these are necessary, do this before any other analysis (e.g. on another image)
* File signature*: "magic" bytes at the start indicating what type of file it is 
* You can't just rely on the file extension, as this can be easily modified

&nbsp;

#### Processing with tools

- **TSK**: sorter command runs analysis of file types, creating a listing of files in multiple categories. Also detects type smismatches during the  process. 
- **Autopsy**: Extension mismatch detector module, however this can be very slow 

&nbsp;

#### Hash sets
* comparing files to a database of known hashes 
* Quick way to locate specific files among large datasets (and prevents hiding by name)  
* Helpful to lookup known files 

| Good | Ignore system files, and ones you know aren't going to be relevant |
| ---- | ------------------------------------------------------------ |
| Bad  | Identify malware, or incriminating documents already discovered elsewhere |

&nbsp;

#### Processing with tools 2
- **TSK**: hfind can index and search hash databases (first need to create hash db from image) 
```bash
imageMounter.py <image> <mount_point>
md5deep —r > database.hash
hfind -i md5sum database.hash
hfind database.hash 9255CAC249D53925253457E7E2B34116  2326-chrome.7z
```

- **Autopsy**: add hash sets to ingest modules: bads are results -> hashtree hits

&nbsp;

### Full text indexing and raw searching 

- **RS**: grep, find. Easy, but not good for non-text files (pdf, zip, exe, embedded files) 

- **FTI**: slower upfront, later searches are faster. Can expand and understand content (zip)

  > Use good keyboards for indexing, otherwise you'll pick up bad data. Find  keywords from the specific investigation (e.g. Lingo), that will  possibly give important results.

  > Better to use full words as acronyms can appear randomly in HEX

&nbsp;

## Timeline analysis 

### FAT32
- FAT32 stores: Create, Modify date/time, only Access data (NO TIME) 
- *Time is stored in local timezone of OS, there are no timezone flags (can't confirm it)* 

&nbsp;

### NTFS
* Stores Create, Last Modified, Last Accessed and Change date/time 
* Timestamps are in UTC 
* Changed refers to the last time the MFT entry was changed (e.g. file moved) 

![](/home/melon/todo/uni/notes/comp/6845/img/week04/image0.png)

&nbsp;

| **Fls**     | file listing similar to ls, shows a bunch of timestamps -m strips out the formatting, just leaving data importable to other tools -r to recurse entire file system fls uses unix timestamps |
| ----------- | ------------------------------------------------------------ |
| **Mactime** | takes body file and moves 4 columns from body files into one column, applies timezone offset to date-times limit output to particular data range formats into human readable data and exports into csv |

&nbsp;

### NTFS dates
* `$Filename` has its own set of MACB times separate to `$Standard_Information` MACB times (which can be vulnerable to time-stomping)
* `$Filename` timestamps are much more difficult to manipulate directly, comparisons between `$F$` and `$S_I` can reveal traces of timestomping.

> Timestomping: attempt to hide tracks by changing timestamps of files in the MFT

&nbsp;
&nbsp;

# Time and Telco Data
## Challenges of and interpreting time 
* When time is used to contextualise events, interpreting correct time is essential 
* Time is the anchor data for sequencing events, however also causes much confusion 

&nbsp;

## Time synch:
> official AUS time source provided by National Measurement Institute NTP servers 
* Servers in Adelaide, Brisbane, Melbourne, Perth and Sydney 
* Most commonly, people use Google and Pool 

&nbsp;

## Problems 
* Windows/Mac devices stores dates in different formats, which can cause large discrepancies 
* Determine between dd-mm-yyyy and mm-dd-yyyy (ask for a month's worth of data) 
* Daylight saving time (AEST vs AEDT) 
* Multiple people adjusting for time-zones (first, then second, etc) 
* The same source which has timestamps in different formats 
* 1904 and 1900 serials. 
* For a long event, what is the timestamp (start or end)? 

> Proving an email has been received is not the same as proving it has been read

 &nbsp;

Coordinated Universal Time (shortened to UTC as a compromise to the French speakers) is a standard adopted in 1967 for calculating date and time based on the International Atomic Clock and is maintained by the Bureau Intemational des Poids et Mesures (BIPM) in France. It includes ways of representing date and time which have since also been standardised as ISO 8016. UTC is not adjusted for daylight savings.

&nbsp;

Greenwich Mean Time (or GMT) is a time zone that is at the Greenwich meridian, which is also the zero meridian. Zulu (or Z) refers to the timezone at the zero meridian and for practical purposes is equivalent to GMT. Local times are shown are For example, a timestamp affixed in Sydney will show as +10:00 meaning 10 hours ahead of Zulu/GMT (or +11 in daylight savings).

&nbsp;

The difference between UTC and GMT varies according to the year but is always < 1 second. "Leap seconds" are inserted into UTC to keep UTC and GMT is synch with the next one being inserted on 31 December 2021. Many timestamps use UTC, GMT and Z interchangeably. For the purposes of my report I will use GMT (pick one and stick to it).
