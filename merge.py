from glob import iglob
import shutil
import os
import pandas

def mergeCsv():
    if os.path.exists("merge.xls"):
        os.remove("merge.xls")
    a1csv = pandas.read_excel("a1.xls")
    a2csv = pandas.read_excel("a2.xls")
    b1csv = pandas.read_excel("b1.xls")
    a1csv.append(a2csv, ignore_index=True) \
        .append(b1csv, ignore_index=True) \
        .to_excel("merge.xls", index=False, header=False)
    pass

def mergeMp3():
    if os.path.exists("merge.mp3"):
        os.remove("merge.mp3")
    with open('merge.mp3', 'wb') as f:
        a1mp3 = open('a1.mp3', 'rb')
        a2mp3 = open('a2.mp3', 'rb')
        b1mp3 = open('b1.mp3', 'rb')
        shutil.copyfileobj(a1mp3, f)
        shutil.copyfileobj(a2mp3, f)
        shutil.copyfileobj(b1mp3, f)
    pass

mergeCsv()
mergeMp3()

