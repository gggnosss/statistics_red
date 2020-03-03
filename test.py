# coding: utf-8
import csv
import time

for user in user_data_reader:
    #最初の３列はkeysというリストに格納
    keys = user[:8]
    #4行目移行はis_in_hospitalというリストに格納
    is_in_hospital = user[8:]
    #リストdurationを初期化
    duration = []
    #リストis_in_hospitalを20140601~20150701まで見ていく
    for i in range(len(is_in_hospital)):
        #0番目が1であれば、その日付をdurationというリストに入れる
        if i == 0:
            if is_in_hospital[i] == '1':
                duration.append(header[8:][i])
        else:
            #1番目以降はn番目が1かつ、(n-1)番目が0であればその日付をdurationに入れる
            if is_in_hospital[i] == '1' and is_in_hospital[i-1] == '0':
                duration.append(header[8:][i])
            #1番目以降はn番目が0かつ、(n-1)番目が1であればその1日前の日付をdurationに入れる
            elif is_in_hospital[i] == '0' and is_in_hospital[i-1] == '1':
                duration.append(header[8:][i-1])
            else:
                pass
