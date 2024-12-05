# SOME MORE S
def IS_PRIME(N):
    if N in [2, 3]:
        return True
    if (N == 1) or (N % 2 == 0):
        return False
    R = 3
    while R * R <= N:
        if N % R == 0:
            return False
        R += 2
    return True

# Tambahkan kode ini untuk menguji fungsi IS_PRIME
number = int(input("Masukkan sebuah angka: "))
if IS_PRIME(number):
    print(f"{number} adalah bilangan prima")
else:
    print(f"{number} bukan bilangan prima")
