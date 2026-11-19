undangan = set()
webinar_a = set()
webinar_b = set()

data = input("Daftar undangan : ")
for nama in data.split(","):
    undangan.add(nama)

data = input("Peserta Webinar A : ")
for nama in data.split(","):
    webinar_a.add(nama)

data = input("Peserta Webinar B : ")
for nama in data.split(","):
    webinar_b.add(nama)

semuaPeserta = webinar_a | webinar_b
hadirKeduanya = webinar_a & webinar_b
hanyaSatu = webinar_a ^ webinar_b
tidakHadir = undangan - semuaPeserta

print("\n=== HASIL ===")
print("Semua peserta dari kedua webinar:", semuaPeserta)
print("Peserta hadir di keduanya:", hadirKeduanya)
print("Peserta hanya hadir di salah satu:", hanyaSatu)
print("Undangan yang tidak hadir di mana pun:", tidakHadir)