data_panen = {
    'lokasi1': {
        'nama_lokasi': 'Kebun A',
        'hasil_panen': {
            'padi': 1200,
            'jagung': 800,
            'kedelai': 500
        }
    },
    'lokasi2': {
        'nama_lokasi': 'Kebun B',
        'hasil_panen': {
            'padi': 1500,
            'jagung': 900,
            'kedelai': 450
        }
    },
    'lokasi3': {
        'nama_lokasi': 'Kebun C',
        'hasil_panen': {
            'padi': 1100,
            'jagung': 750,
            'kedelai': 600
        }
    },
    'lokasi4': {
        'nama_lokasi': 'Kebun D',
        'hasil_panen': {
            'padi': 1300,
            'jagung': 850,
            'kedelai': 550
        }
    },
    'lokasi5': {
        'nama_lokasi': 'Kebun E',
        'hasil_panen': {
            'padi': 1400,
            'jagung': 950,
            'kedelai': 480
        }
    }
}

print("-----No.1-----")
for lok, d in data_panen.items():
    print(f"Lokasi: {d['nama_lokasi']}")
    print("Hasil Panen:")
    for a, jumlah in d['hasil_panen'].items():
        print(f"~ {a}: {jumlah} kg")
    print("\n")

print("-----No.2-----")
for a, jumlah in data_panen['lokasi2']['hasil_panen'].items():
    print(f"~ {a}: {jumlah} kg")
print("\n")

print("-----No.3-----")
nama = data_panen['lokasi3']['nama_lokasi']
print(f"Nama lokasi lokasi3 adalah {nama}")
print("\n")


print("-----No.4-----")
hasilpadi = {}
hasilkeledai = {}

for lok, data in data_panen.items():
    hasilpadi[lok] = data['hasil_panen']['padi']
    hasilkeledai[lok] = data['hasil_panen']['kedelai']

print("Hasil panen padi:")
for lok, jumlah in hasilpadi.items():
    print(f"~ {lok}: {jumlah} kg")

print("\nHasil panen kedelai:")
for lok, jumlah in hasilkeledai.items():
    print(f"~ {lok}: {jumlah} kg")
print("\n")

print("-----No.5-----")
totalpadi = sum(data['hasil_panen']['padi'] for data in data_panen.values())
totalkedelai = sum(data['hasil_panen']['kedelai'] for data in data_panen.values())

print(f"Hasil panen padi dari semua lokasi adalah {totalpadi} kg")
print(f"Hasil panen kedelai dari semua lokasi adalah {totalkedelai} kg")

print("\n")

print("-----No.6-----")
for lok, data in data_panen.items():
    padi = data['hasil_panen']['padi']
    jagung = data['hasil_panen']['jagung']
    if padi > 1300 or jagung > 800:
        status = "memerlukan perhatian khusus"
    else:
        status = "baik....."
    
    print(f"Kondisi {data['nama_lokasi']} {status}")
