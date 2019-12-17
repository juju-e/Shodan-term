from termcolor import colored
import shodan
from subprocess import *

print(colored("___      ____  __   __   _    ___ __ __ _  _ ","green"))
print(colored("|__ |__| |  | |  \ /  \ | \ |  | |__|__||\/|   ","green"))
print(colored("___||  | |__| |__/ |--| |  \|  | |__|  \|  | ","green"))
print("")
sh_key=input("[*]please enter your shodan key---->")
api=shodan.Shodan(sh_key)
print(colored("1.What's my ip","green"))
print(colored("2.Ip scan","red"))
print(colored("3.Custom Search","yellow"))
opt=input(colored("[*]Enter the option you want to choose+-->","cyan"))
while opt!="0":
 if opt=="1":
   print("your ip is: ")
   print(colored(str(check_output(["shodan","myip"])),"green"))
   opt=input(colored("[@]reenter the same or an other option--->","red"))
 elif opt=="2":
  ip=input("ip to scan->")
  try: 
   host=api.host(ip)
   print(colored("""
   IP: {}
   Organization: {}
   OS: {} 
   City: {}
   country: {}
   Hostnames: {}
   Open ports: {}
   Ports: {}
   """.format(host['ip_str'],host.get('org','n/a'),host.get('os','n/a'),host['city'],host['country_name'],','.join(host['hostnames']),len(host['ports']),str(host['ports'])),'green'))
  except shodan.APIError, e:
        print('Error: {}'.format(e))
  opt=input(colored("[@]reenter the same or an other option--->","red"))
 elif opt=="3":
  search=input(colored("[#]enter the search to perform--->","cyan"))
  try:
   res=api.search(search)
   print(colored("Total results Found: "+str(res['total']),"green"))
   print("Please presss ctrl+c to stop the search")
   for result in res['matches']:
    host=api.host(result['ip_str'])
    print(colored(str(result['ip_str']),"green")+" "+colored(str(result['port']),"yellow")+" "+" "+colored(host.get('org','n/a'),"cyan")+" "+colored(str(','.join(result['hostnames'])),"red"))
  except shodan.APIError, e:
        print('Error: {}'.format(e))
  opt=input(colored("[@]reenter the same or an other option--->","red"))

