import pandas as pd
import scrypt
import getpass

hosts_file = open("./hosts.txt","wb")
salt = getpass.getpass('password: ')
df = pd.read_excel(r'./hosts.xlsx')
hosts_info = ""
for row in df.itertuples():
    host_info = str(getattr(row, 'IP')) + "\t" + str(getattr(row, 'url')) + "\t" + str(getattr(row, 'username')) + "\t" + str(getattr(row, 'password')) + "\t" + str(getattr(row, 'brand')) + "\t" + str(getattr(row, 'model')) + "\n"
    hosts_info += host_info
hosts_info=hosts_info.strip('\n')
ciphertext = scrypt.encrypt(hosts_info, salt, maxtime=1)
hosts_file.write(ciphertext)
hosts_file.close()
