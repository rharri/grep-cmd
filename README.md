## Description
A Python implementation of the grep command line program. 
This is a partial implementation that only supports matching 
a pattern for a single file.

## Requirements
- Python >=3.12

## Simple Example
```
$ python3 -m grep_cmd '\d{3}-\d{3}-\d{4}' grep_cmd/data/test1.txt
Phone number: 455-733-4242
Phone number: 189-677-3290
Phone number: 555-838-2800
```
