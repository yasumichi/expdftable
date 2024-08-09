# -*- coding: utf-8 -*-
"""
Created on Sun Aug  4 18:41:10 2024

@author: y_aka
"""

import re
from sys import argv, exit
from os import path
import fitz
import pandas as pd
from styleframe import StyleFrame

def to_float(obj):
    """
    convert from digit string to float.

    Parameters
    ----------
    obj : str
        digit string.

    Returns
    -------
    float
        float.

    """
    try:
        value = float(str(obj).replace(',', ''))    
        return value
    except:
        return obj

def expdftable(pdf, excel, start, end, join=False):
    """
    extract tables from pdf and convert to excel book.

    Parameters
    ----------
    pdf : str
        pdf file path.
    excel : str
        excel file path.
    start : int
        start page number of pdf.
    end : int
        end page number of pdf.
    join : bool, optional
        Whether to join all tables to one sheet. The default is False.

    Returns
    -------
    None.

    """
    
    if not path.exists(pdf):
        raise Exception(f"{pdf}: No such file")
    
    doc = fitz.open(pdf)
    
    dataFrames = []
    
    for page in doc[start-1:end]:
        for table in page.find_tables(strategy="lines_strict"):
            dataFrames.append(table.to_pandas().map(to_float))
    
    if len(dataFrames) == 0:
        raise Exception('Tables not found.')
            
    if join:
        sf = StyleFrame(pd.concat(dataFrames, ignore_index=True))
        with StyleFrame.ExcelWriter(excel) as writer:
            sf.to_excel(writer)
    else:
        shnum = 1
        with StyleFrame.ExcelWriter(excel) as writer:
            for df in dataFrames:
                sf = StyleFrame(df)
                sf.to_excel(writer, sheet_name= f"Sheet{shnum}")
                shnum = shnum + 1
                
    
    doc.close()
    

def usage():
    """
    Show Usage and exit

    Returns
    -------
    None.

    """
    print(f"Usage: {argv[0]} pdf excel start end [join]")
    exit()

if __name__ == '__main__':
    if len(argv) != 5 and len(argv) != 6:
        usage()
        
    pdf = argv[1]
    excel = argv[2]
    start = int(argv[3])
    end = int(argv[4])
    
    join = False
    if len(argv) == 6:
        join = eval(argv[5])
    
    expdftable(pdf, excel, start, end, join)
