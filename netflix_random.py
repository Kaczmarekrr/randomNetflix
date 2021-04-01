# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 19:24:13 2021

@author: kaczm
"""

import numpy as np
import pandas as pd
import time
from directkeys import *

    
import subprocess

def copy2clip(txt):
    cmd='echo '+txt.strip()+'|clip'
    return subprocess.check_call(cmd, shell=True)
    
def main():    
    netflix_df = pd.read_csv("netflix_titles.csv")
    
    typ = ["Horror Movies", "International Movies","Dramas", "Romance"] #etc, do zrobienia aby była pełna lista
    
    #filtracja danych
    
    filtered_data = netflix_df.loc[
        lambda netflix_df: netflix_df.listed_in.apply(
            lambda l: 'Dramas' in l
        )
    ]
    #print(filtered_data)
    
    
    lista = filtered_data.values.tolist()
    #wybieranie tytułu
    
    random_num = np.random.randint(0,len(lista))
    random_title = lista[random_num][2]
    random_type = lista[random_num][1]
    print(random_title,random_type)
    
    
    #printowanie 
    name = random_title
    copy2clip(name)
    print(f'twój {random_type} to', name)
    print('wklejam!')
    time.sleep(3)
# Wklejanie do wyszukiwarki
def paste():
    PressKey(0x11)
    PressKey(0x56)
    time.sleep(0.1)
    ReleaseKey(0x11)
    ReleaseKey(0x56)
    PressKey(0x0D)
    ReleaseKey(0x0D)

print(f"Miłego seansu!")


if __name__ == "__main__":
    main()
    paste()


