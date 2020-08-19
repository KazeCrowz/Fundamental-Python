# tipe data skalar = tipe data sederhana
anak1 = 'Anugrah'
anak2 = 'Jason'
anak3 = 'Felix'
anak4 = 'Daniel'

print('anak1')
print('anak2')
print('anak3')
print('anak4')

# tipe data list/array
print('\ntipe data list')
anak = ['Anugrah', 'Jason', 'Felix', 'Daniel']
print(anak)
# untuk menambahkan anak lagi
anak.append('Nathan')
print(anak)

# sapa anak ke-2
print('\nsapa anak kedua')
print(f'Hai {anak[1]}!')

# sapa semua anak
print('\nSapa semuanya: cara mudah(sederhana)')

for a in anak:
    print(f'hai {a}!')

print('\nSapa semuanya: cara ribet')

for a in range(0, len(anak)):
    print(f'{a + 1}. Hai {anak[a]}!')
