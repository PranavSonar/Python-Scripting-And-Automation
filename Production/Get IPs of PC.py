import platform as pc
import socket as sk
import os
import time

print("\n\nTHIS PROGRAM IS MADE FOR GETTING IPS AND OTHER DETAILS OF PC")
print("ANALYZING YOUR PC ...")
pc_ip = sk.gethostbyname(sk.gethostname())
pc_user = os.environ.get('USERNAME')
cpc = pc.uname()
pc_detils = '\n System: \t\t{} {} \n Node: \t\t\t{}  \n Processor: \t\t{}'.format(
    cpc.system, cpc.release, cpc.node, cpc.processor)
file="T:\Vivek\System Details.txt"
detils_file = open(file, "w+")
detils_file.write("\n Last Updated Time :\t"+time.ctime())
detils_file.close()
detils_file = open(file, "a+")
detils_file.write(pc_detils)
detils_file.write('\n USER: \t\t\t'+pc_user)
detils_file.write('\n IP: \t\t\t'+pc_ip)
detils_file = open(file, "r+")
print(detils_file.read())
print(" File: \t\t\t"+file)
detils_file.close()
time.sleep(100)
