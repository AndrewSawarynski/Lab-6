#Andrew Sawarynski partnered with Cienna Perez

def main():
    while True:
        print("1. To encode")
        print("2. To decode")
        print("3. To exit")
        choice = input("Please enter an option: ")
        if choice == "1":
            password = input("Please enter your password to encode: ")
            print("Your password has been encoded and stored!")
        elif choice == "2":
            value = password
            print(f"The encoded password is {final_res} and the original password is {password}.")
        elif choice == "3":
            break
        else:
            print("Not an option")
        print()

def encode(password):
    final_res = ''
    for num in password:
        new_num = str((int(num) + 2) % 10)
        final_res += new_num
    return final_res

main()