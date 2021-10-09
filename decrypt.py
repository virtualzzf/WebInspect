import scrypt
import getpass

salt = getpass.getpass('password: ')
hosts_file = open("./hosts.txt","rb")
hosts_info_cipher = hosts_file.read()
hosts_file.close()
hosts_info_plain = scrypt.decrypt(hosts_info_cipher, salt)
hosts_info_list = hosts_info_plain.split("\n")
for host_info in hosts_info_list:
    print(host_info)
