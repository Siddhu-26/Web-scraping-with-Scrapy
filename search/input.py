name = input("Please enter your Name:")
print(f"Welcome! {name}")

product_name = input(f"{name}, Please enter the mobile phone's name you are searching for:")

f = open('input.txt', 'w', encoding='utf-8')
f.write(f"{product_name} \n")