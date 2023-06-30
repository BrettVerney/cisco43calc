import sys
import ipaddress
from ipaddress import AddressValueError
import socket

# Function to validate and convert IP addresses to hexadecimal.
def ip_to_hex(wlc_ip):
    try:
        wlc_ip = ipaddress.IPv4Address(wlc_ip)
        wlc_ip = str(wlc_ip)
        wlc_ip = socket.inet_aton(wlc_ip).hex()
        return wlc_ip
    except AddressValueError:
        return None

# Function to print the list of IP addresses in the required format.
def print_hex_ips(iplist):
    hexlist = ''.join(iplist)
    hexcount = '{:02X}'.format(int(hex(len(iplist)*4), 16))
    print ('\n' + 'Your DHCP Option 43 value is: ' + 'f1' + hexcount + hexlist)

# Function to handle case when script is executed with command line arguments.
def arg_mode(ip_args):
    iplist = []
    for wlc_ip in ip_args:
        hex_ip = ip_to_hex(wlc_ip)
        if hex_ip is None:
            print('Error: One or more specified arguments are not Valid IPv4 Addresses')
            return
        if hex_ip not in iplist:
            iplist.append(hex_ip)
    print_hex_ips(iplist)

# Function to handle case when script is executed without command line arguments.
def interactive_mode(user_input):
    count = 0
    iplist = []
    while count < user_input:
        count += 1
        wlc_ip = input('WLC #' + str(count) + ' IP Address: ')
        hex_ip = ip_to_hex(wlc_ip)
        if hex_ip is None:
            print ('Not a valid IP Address. Try again.')
            count -= 1
        elif hex_ip in iplist:
            print ('IP Address already entered. Try again.')
            count -= 1
        else:
            iplist.append(hex_ip)
    print_hex_ips(iplist)

# Main function to handle the overall logic.
def main():
    if len(sys.argv) > 1:
        arg_mode(sys.argv[1::])
    else:
        try:
            user_input = int(input('\n' + 'Number of WLCs in network: '))
            if 0 < user_input < 17:
                interactive_mode(user_input)
            else:
                print ('Please enter a number between 1 and 16.')
        except ValueError:
            print ('Not a valid number. Try again.')

# Execution starts here.
if __name__ == "__main__":
    main()