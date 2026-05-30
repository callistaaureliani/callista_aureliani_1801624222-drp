for baris in range(8):
    for kolom in range(8):

        if (baris + kolom) % 2 == 0:
            print("⬜", end="")
        else:
            print("⬛", end="")

    print()
aktivitas_list = []

jumlah = int(input("Berapa aktivitas yang ingin diinput? "))

for i in range(jumlah):
    print(f"\nAktivitas ke-{i+1}")

    aktivitas = input("Nama aktivitas: ")
    waktu = input("Waktu pelaksanaan: ")
    prioritas = input("Prioritas (Tinggi/Sedang/Rendah): ")

    data = {
        "aktivitas": aktivitas,
        "waktu": waktu,
        "prioritas": prioritas
    }

    aktivitas_list.append(data)

print("\n===== DAFTAR AKTIVITAS =====")

for nomor, item in enumerate(aktivitas_list, start=1):
    print(f"\nAktivitas {nomor}")
    print(f"Nama      : {item['aktivitas']}")
    print(f"Waktu     : {item['waktu']}")
    print(f"Prioritas : {item['prioritas']}")