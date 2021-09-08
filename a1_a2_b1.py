from glob import iglob
import shutil
import os
import pandas

def a1_a2_b1Csv():
    if os.path.exists("a1_a2_b1.xls"):
        os.remove("a1_a2_b1.xls")
    a1csv = pandas.read_excel("a1.xls")
    a2csv = pandas.read_excel("a2.xls")
    b1csv = pandas.read_excel("b1.xls")
    a1csv.append(a2csv, ignore_index=True) \
        .append(b1csv, ignore_index=True) \
        .to_excel("a1_a2_b1.xls", index=False, header=False)
    pass

def a1_a2_b1Mp3():
    if os.path.exists("a1_a2_b1.mp3"):
        os.remove("a1_a2_b1.mp3")
    with open('a1_a2_b1.mp3', 'wb') as f:
        a1mp3 = open('a1.mp3', 'rb')
        a2mp3 = open('a2.mp3', 'rb')
        b1mp3 = open('b1.mp3', 'rb')
        shutil.copyfileobj(a1mp3, f)
        shutil.copyfileobj(a2mp3, f)
        shutil.copyfileobj(b1mp3, f)
    pass

a1_a2_b1Csv()
a1_a2_b1Mp3()

