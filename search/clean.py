import pandas as pd
import re


def elim_comma(a):
    for i in range(len(a)):
        a[i] = float(a[i].replace(',', ''))

    return a


z = open("input.txt", 'r', encoding='utf-8')
product = z.read()

f = open('temp.csv', 'r', encoding='UTF-8')

# Formatting and cleaning the data
r = f.read()
r = r.replace("Name,Price", ",")
r = r[3:-2]
temp = ''

for i in r:
    if i == '\n':
        pass
    else:
        temp += i

r = temp

a = r.split('","')

########################################################### Flipkart

names_fk = []
website_fk = []

x = ''
for i in a[0]:
    if x.endswith(')'):
        names_fk.append(x)
        x = ''
    else:
        x += i
names_fk.append(x)
a[1] = a[1][1:]
price_fk = re.split(',₹', a[1])
price_fk = elim_comma(price_fk)

for i in price_fk:
    website_fk.append("Flipkart")

########################################################### Amazon

names_az = []
website_az = []
a[3] = a[3][1:]
x = ''
names_az = re.split(',', a[2])

price_az = re.split(',₹', a[3])
price_az = elim_comma(price_az)
for i in price_az:
    website_az.append("Amazon")

"""
for i in names_az:
    if product.lower() not in i.strip().lower():
        price_az.remove(names_az.index(i))
        website_az.remove(names_az.index(i))
        names_az.remove(i)
"""
########################################################### Reliance Digital
"""
names_rd = []
website_rd = []
#print(a[4])
x = ''
#for i
a[5] = a[5][1:]
price_rd = re.split(',₹', a[5])
for i in price_rd:
    website_rd.append("Reliance Digital")

"""
###########################################################Combine

names = []
price = []
website = []

names.extend(names_fk)
names.extend(names_az)
# names.extend(names_rd)

price.extend(price_fk)
price.extend(price_az[:len(names_az)])
# price.extend(price_rd)

website.extend(website_fk)
website.extend(website_az[:len(names_az)])
# website.extend(website_rd)

print(len(names), len(price), len(website))

df = pd.DataFrame({'Name': names, 'Price': price, 'Website': website})
print(df.sort_values('Price'))
