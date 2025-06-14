def caesar_encrypt(text, shift):
    hasil = ""
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            hasil += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            hasil += char
    return hasil

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

teksawal = "Informatika"
shift = 5

hasilenkripsi = caesar_encrypt(teksawal, shift)
print(f"Teks terenkripsi dari \"{teksawal}\" menjadi \"{hasilenkripsi}\"")

hasildekripsi = caesar_decrypt(hasilenkripsi, shift)
print(f"Teks terdekripsi dari \"{hasilenkripsi}\" menjadi \"{hasildekripsi}\"")
