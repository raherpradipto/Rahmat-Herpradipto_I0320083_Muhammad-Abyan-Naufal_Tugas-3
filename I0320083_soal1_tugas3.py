print("------------------------------------------------------------------------------")
print("PROGRAM LIST")
print("------------------------------------------------------------------------------")

list = ['rafi','ariq','dannar','fakhrul','anom','erdian','gensa','hendra','atha','era']

print("list indeks nomor empat: ",list[4])
print("list indeks nomor enam: ",list[6])
print("list indeks nomor tujuh: ",list[7])

list[3] = 'arinaa'
list[5] = 'herliana'
list[9] = 'marshanda'

list.append('ica')
list.append('karin')

for repetition in list:
    print(repetition, "is my support system")

print("panjang list: ",len(list))

print("------------------------------------------------------------------------------")
print("------------------------------------------------------------------------------")