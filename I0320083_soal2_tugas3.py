print("----------------------------------------------------------------------------------------------------------------")
print("PROGRAM DICTIONARY")
print("----------------------------------------------------------------------------------------------------------------")

dict = {'nama': ['Rahmat Herpradipto'],
        'hobi': ['Berenang','Lari','Bulu Tangkis'],
        'sosial media': ['Instagram: @raherpradipto','Id line: rahmat_herpradipto','linkedIn: Rahmat Herpradipto'],
        'lagu kesukaan': ['Takkan Ada Cinta Yang Lain','Kamulah Satu Satunya','Cinta Terakhir'],
        'makanan favorit': ['Satai Kambing','Satai Ayam','Sosis','Seafood']}

dict['hobi'][2] = 'Poker'
dict['sosial media'][0] = '@mas_herp'

del dict['makanan favorit'][1:2]

dict['hobi'].append('Lego')

print("Lebih Dekat Dengan Rahmat"
      "\n"
      "\nPerkenalkan nama saya", dict['nama'],
      "\nHobi saya diantaranya adalah", dict['hobi'],
      "\nUsername sosial media saya adalah", dict['sosial media'],
      "\nJudul lagu favorit saya adalah", dict['lagu kesukaan'],
      "\nMakanan favorit saya adalah", dict['makanan favorit'])

print("----------------------------------------------------------------------------------------------------------------")
print("----------------------------------------------------------------------------------------------------------------")