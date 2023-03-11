import random
def generate_password(length = int(input("Raqam kiriting: "))): 
    kichik_harf = "abdeghijklmnopqrstuvxyzo'g'shchng" 
    katta_harf = "ABDEGHIJKLMNOPQRSTUVXYZO'G'SHCHNG"
    raqamlar="123456789"
    simvollar = "!@#$%^&*()_+"
    all_chars = kichik_harf + katta_harf + raqamlar + simvollar
    password_chars = random. sample(all_chars, length)
    password = "". join(password_chars)

    return password

password = generate_password()
print(password)