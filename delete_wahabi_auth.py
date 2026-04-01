import json

# Daftar authno yang akan dihapus
wahabi_authno = {
    152, 172, 1015, 62, 67, 57, 47, 185, 128, 114,
    1523, 1524, 1526, 1527, 1528
}

with open("index.json", "r", encoding="utf-8") as f:
    data = json.load(f)

before = len(data)
filtered = [book for book in data if book["authno"] not in wahabi_authno]
after = len(filtered)

with open("index.json", "w", encoding="utf-8") as f:
    json.dump(filtered, f, ensure_ascii=False, indent=2)

print(f"Selesai. Dihapus: {before - after} buku. Sisa: {after} buku.")