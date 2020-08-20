"""
Tipe data dictionary sekedar menghubungkan KEY dan VALUE
KVP = Key Value Pair
"""

kamus_id_en = {'Anak': 'Son', 'Bapak': 'Father', 'Ibu': 'Mother'}

print(kamus_id_en)
print(kamus_id_en['Anak'])
print(kamus_id_en['Ibu'])

# Contoh
print('\nData ini dikirimkan oleh server Gojek untuk memberikan informasi mengenai Driver Gojek')
data_server_gojek = {
    'Tanggal': '2020-08-20',
    'data_list': [
        {'nama': 'Anugrah', 'jarak': 10},
        {'nama': 'Kevin', 'jarak': 40},
        {'nama': 'Tony', 'jarak': 100},
        {'nama': 'John', 'jarak ': 1000}
    ]
}
print(data_server_gojek)
print(f'Driver di sekitar sini {data_server_gojek["data_list"]}')
print(f"Driver #1 {data_server_gojek['data_list'][0]}")
print(f"Driver terdekat berada di {data_server_gojek['data_list'][0]['jarak']} meter")
