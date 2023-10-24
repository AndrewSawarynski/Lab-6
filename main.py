#Andrew Sawarynski partnered with Cienna Perez

def main():
    while True:
        print("1. To encode")
        print("2. To decode")
        print("3. To exit")
        choice = input("Enter your choice (1 or 2 or 3): ")
        if choice == "1":
            password = input("Enter an 8-digit password: ")
            print("Encoded password is", encode(password))
        elif choice == "2":
            value = input("Enter an already encoded 8-digit password: ")
            print("Decoded password is", decode(password))
        elif choice == "3":
            break
        else:
            print("Not availible option")
        print()

def encode(password):
    final_res = ''
    for num in password:
        new_num = str((int(num) + 3) % 10)
        final_res += new_num
    return final_res

main()