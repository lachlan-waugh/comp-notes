# File systems
* [FAT32](#fat32)
* [NTFS](#ntfs)
* [File slack](#file)
* [The Sleuth Kit]()

&nbsp;

## what is a filesystems
* way in which OS manages files/folder structure on disk 
* another logical layer of abstraction on top of volumes 
* manage allocation of clusters to files, and usage of clusters (free/allocated) 

&nbsp;

## FAT32
* 3 main components: volume boot record, file allocation table (FAT), directory entries 
* logical improvement on FAT8/16 (number of bytes ...)

&nbsp;

### volume boot record
* sits at the beginning of the drive. contains:
* a jump to the boot code,
* OEM name,
* boot code and
* error messages BPB (BIOS Parameter Block) database of values to setup the FAT

&nbsp;

### BIOS parameter block (BPB)
* describes the physical layout of a data storage volume, contains:
* File system geometry (bytes per sector, sectors per cluster)
* FATs stored, root directory location, volume and type labels in ASCII

>  Very distinctive look in HEX/Text, easy to see 

&nbsp;

### directory entries (DEs)
* file information in FAT systems are organized into DE structures. 
* A pretty simple tree structure 
* each DE consists of file metadata (pointers to clusters containing data for file/folder) 
  * **files**: cluster contains content of file
  * **folder**: cluster contains another DE

&nbsp;

### file allocation table
> big linked list containing status of all clusters in the FS

| status       | indicates                                       |
| ------------ | ----------------------------------------------- |
| `0x?0000000` | free cluster                                    |
| `0x?0000002` | cluster in use (value is next cluster for file) |
| `0x?FFFFFFF` | cluster in use EOF marker                       |

&nbsp;

### deleting files
* first character in filename modified to `0xe5` (usually `_` or `!` in tools)
* all clusters in FAT replaced with `0x00` to set them as free
* hard to recover if file was split across the FAT

&nbsp;

## NTFS

* everything is a file (even meta-data structures)
* new features: sparse file support, disk use quotas, resparse points, distributed link tracking, file-level encryption

| **NTFS VBR**               | Similar to FAT VBR, but also contains a cluster with \$MFT (master file table) and a cluster with backup \$MFT (\$MFTMirr) |
| -------------------------- | ------------------------------------------------------------ |
| **$MFT**                   | Equivalent of DE in FAT.                                     |
|                            | Entries contains metadata about files, and their location of the data |
|                            | MFT Entry Bitmap: an attribute that tracks which MFT FILE entries are in-use/free |
| **$BITMAP**                | The equivalent of the FAT (much more efficient, tracks clusters with a single bit) |
|                            | Tracks usage of clusters in the filesystem, but not the next cluster in file |
| **FILE Records**           | Each file has its own within the $MFT (incl. \$MFT), contains a MFT header, file metadata attributes: |
|                            | \$STANDARD_INFORMATION - creation, modification, changed, access time |
|                            | \$FILENAME                                                   |
|                            | \$DATA - content of the file                                 |
| **resident data**          | attribute data initially starts resident (all contained within the $MFT), but moved into clusters if it becomes too large if file become non-resident, *it doesn't get zeroed out* once an attribute becomes non-resident, it never becomes resident again |
| **cluster runs**           | \$Data attributes store location of file using cluster runs  |
|                            | header: single byte describing number of bytes used for this attribute |
|                            | length: number of contiguous clusters in this run            |
|                            | offset: offset from starting point of previous run (0 if this is first run) |
| **alternate data streams** | can add a secondary data stream with `file1:file2`<br />generally, windows doesn't honour this, use notepad `file1:file2` or `dir /r` |
| **deleted files**          | MFT marks FILE entry as available                            |
|                            | \$DATA attribute read, \$BITMAP updated to show cluster runs no longer used |
|                            | nothing is wiped/deleted from MFT or clusters                |
|                            | therefore: until the FILE entry is overwritten, the data is still there |

&nbsp;

### file slack
* occurs because data can only be allocated to files at cluster level 
* in Windows, RAM slack is padded with 0s while drive slack is left untouched 

| drive slack | if file doesn't fill entire cluster, remaining slack can contain residual data |
| ----------- | ------------------------------------------------------------ |
| RAM slack   | you can't address part of a sector, so there's slack at the end of the sector |

&nbsp;

## unallocated clusters
* file carving is scanning unallocated clusters for traces of deleted files
* does this by looking for File Signatures (tell-tale byte structures)

&nbsp;

## the sleuthkit (TSK)
> Autopsy is just a GUI for TSK

| **img_stat** | shows basic information about the image (type, hash, etc). A good starting point |
| ------------ | ------------------------------------------------------------ |
| **mmls**     | decodes partition table (shows partit. types, starting/ending clusters, size) the partition offsets are useful for later commands |
| **fsstat**   | shows partition details of particular offset (type, geometry, MFT/FAT locations) one place to use the above offset using the -o switch |
| **istat**    | shows FAT/MFT entry for a file (quite similar to ffstat), also requires -o offset files are identified by inode number. lists out the cluster runs of a file |
| **icat**     | similar to cat, shows the data for a file. also requires -o offset files identified by an inode number |

&nbsp;

### More commands

| **command**      | description                                                  |
| ---------------- | ------------------------------------------------------------ |
| **blkcalc**      | Converts between unallocated disk unit numbers and regular disk unit numbers. |
| **blkcat**       | Display the contents of file system data unit in a disk image |
| **blkls**        | List or output file system data units.                       |
| **blkstat**      | Display details of a file system data unit (i.e. block or sector). |
| **fcat**         | Output the contents of a file based on its name.             |
| **ffind**        | Finds the name of the file or directory using a given inode. |
| **fls**          | List file and directory names in a disk image.               |
| **fsstat**       | Display general details of a file system.                    |
| **icat**         | Output the contents of a file based on its inode number.     |
| **ifind**        | Find the meta-data structure that has allocated a given disk unit or file name. |
| **ils**          | List inode information.                                      |
| **img_stat**     | Display details of an image file.                            |
| **istat**        | Display details of a meta-data structure (i.e. inode).       |
| **mactime**      | Create an ASCII time line of file activity.                  |
| **mmcat**        | Output the contents of a partition to stdout.                |
| **mmls**         | Display the partition layout of a volume system (partition tables). |
| **mmstat**       | Display details about the volume system (partition tables).  |
| **sorter**       | Sort files in an image into categories based on file type.   |
| **srch_strings** | Display printable strings in files.                          |