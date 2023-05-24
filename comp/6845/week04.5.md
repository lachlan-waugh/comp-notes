## Processing and Timeline Analysis

### Pre-analysis

**Background intel**

* What occurred, and when did it occur?
* What analysis techniques are most likely to uncover relevant information?
* Which should be a priority, which order does it make sense to run them?

> You don't have an unlimited amount of time to run your investigation 

 

**Processing**: *If these are necessary, do this before any other analysis (e.g. on another image)* 

 

*File signature*: "magic" bytes at the start indicating what type of file it is 

*You can't just rely on the file extension, as this can be easily modified* 

- TSK: sorter command runs analysis of file types, creating a listing of files in multiple categories. Also detects type smismatches during the  process. 
- Autopsy: Extension mismatch detector module, however this can be very slow 

 

*Hash sets*: comparing files to a database of known hashes 

Quick way to locate specific files among large datasets (and prevents hiding by name)  

Helpful to lookup known files 

| Good | Ignore system files, and ones you know aren't going to be relevant |
| ---- | ------------------------------------------------------------ |
| Bad  | Identify malware, or incriminating documents already discovered elsewhere |

 

- **TSK**: hfind can index and search hash databases (first need to create hash db from image) 
  - `imageMounter.py <image> <mount_point>`
  - `md5deep —r > database. hash`
  - `hfind -i md5sum database. hash`
  - `hfind database.hash 9255CAC249D539252S3457E7E2B34116  9255CAC249D53925253457E7E2B34116  2326-chrome.7z`

- **Autopsy**: add hash sets to ingest modules: bads are results -> hashtree hits 

 

*Full text indexing and raw searching* 

- RS: grep, find. Easy, but not good for non-text files (pdf, zip, exe, embedded files) 
- FTI: slower upfront, later searches are faster. Can expand and understand content (zip)

- *Use good keyboards for indexing, otherwise you'll pick up bad data. Find  keywords from the specific investigation (e.g. Lingo), that will  possibly give important results.* 
- *Better to use full words as acronyms can appear randomly in HEX* 

 

### Timeline analysis 

**FAT32** 

- FAT32 stores: Create, Modify date/time, only Access data (NO TIME) 
- *Time is stored in local timezone of OS, there are no timezone flags (can't confirm it)* 

 

**NTFS** 

- Stores Create, Last Modified, Last Accessed and Change date/time 
- Timestamps are in UTC 
- Changed refers to the last time the MFT entry was changed (e.g. file moved) 
- ![](/home/melon/todo/uni/notes/comp/6845/img/week04/image0.png)

 

| **Fls**     | file listing similar to ls, shows a bunch of timestamps -m strips out the formatting, just leaving data importable to other tools -r to recurse entire file system fls uses unix timestamps |
| ----------- | ------------------------------------------------------------ |
| **Mactime** | takes body file and moves 4 columns from body files into one column, applies timezone offset to date-times limit output to particular data range formats into human readable data and exports into csv |

 

| **NTFS dates** | \$Filename has its own set of MACB times separate to \$Standard_Information MACB times (which can be vulnerable to time-stomping) |
| -------------- | ------------------------------------------------------------ |
|                | \$Filename timestamps are much more difficult to manipulate directly, comparisons between $\$F$ and $\$S\_I$ can reveal traces of timestomping. |

> Timestomping: attempt to hide tracks by changing timestamps of files in the MFT* 