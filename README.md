# expdftable
extract tables from pdf to excel powered by PyMuPDF

## Install

```
$ git clone https://github.com/yasumichi/expdftable.git
$ cd expdftable
$ pip install .
```

## Usage of CUI interface

```
$ expdftable pdf excel start end [join]
```

| argument | comment |
| -------- | ------- |
| pdf | pdf file path (input) |
| excel | excel file path (output) |
| start | start page number of pdf file |
| end | end page number of pdf file |
| join | Specify whether to join tables as True or False. |

## Usage of GUI interface

```
$ expdftableTk
```

![expdftableTk](https://github.com/user-attachments/assets/1109e0c4-7834-41e9-b3f7-58c4b9d209c3)

1. Select pdf file.
2. Change start and end.
3. Select excel file if necessary.
4. Check `Join all tables` if necessary.
5. Click `Extract`
