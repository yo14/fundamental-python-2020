"""
Tipe data dictionary sekedar menghubungkan antara KEY dan VALUE
KVP = Key Value Pair
dictionary = kamus
"""

kamus_ind_eng = {'anak': 'child', 'istri': 'wife', 'ayah': 'father', 'ibu': 'mother'}

print(kamus_ind_eng)
print(kamus_ind_eng['ayah'])
print(kamus_ind_eng['ibu'])

print('\nData ini dikirimkan oleh server Gojek, untuk memberikan info driver di sekitar pemakai aplikasi')
data_dari_server_gojek = {
    'tanggal':'2020-06-18',
    'driver_list': [
        {'nama':'Eko', 'jarak': 10},
        {'nama':'Dwi', 'jarak': 30},
        {'nama':'Tri', 'jarak': 100},
        {'nama':'Catur', 'jarak': 1000}
    ]
}
print(data_dari_server_gojek)

print(f"\nDriver disekitar sini {data_dari_server_gojek['driver_list']}")
print(f"\nDriver #1 {data_dari_server_gojek['driver_list'][0]}")
print(f"\nDriver #4 {data_dari_server_gojek['driver_list'][3]}")
print(f"\nDriver terdekat berjarak {data_dari_server_gojek['driver_list'][0]['jarak']} meter")




