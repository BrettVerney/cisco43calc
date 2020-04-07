import sys
import ipaddress
from ipaddress import AddressValueError
import socket

# User executes script with IPs specified as arguments at CLI
def arg_mode():
    try:
        ip_args = (sys.argv[1::])
        iplist = []
        for wlc_ip in ip_args:
            # Validate IP addresses and convert to hex
            wlc_ip = ipaddress.IPv4Address(wlc_ip)
            wlc_ip = str(wlc_ip)
            wlc_ip = socket.inet_aton(wlc_ip).hex()
            # Ignore duplicate entries, convert to list and join on a single line with no spacing
            if wlc_ip not in iplist:
                iplist.append(wlc_ip)
            else:
                continue
            hexlist = (''.join(iplist))
        # Convert IP count to hex/base 16, remove leading '0xf'. Print =< 2 digits or add leading '0' as required by Cisco
        hexcount = int(hex(len(iplist)*4), 16)
        hexcount = '{:02X}'.format(hexcount)
        # Combine and print output to screen for user
        print ('f1' + hexcount + hexlist)
    except AddressValueError:
        sys.exit('Error: One or more specified arguments are not Valid IPv4 Addresses')

# User runs script without any arguments specified at CLI
def interactive_mode():
    try:
        count = int(0)
        user_input = int(input('\n' + 'Number of WLCs in network: '))
        assert 0 < user_input < 17
    except AssertionError:
        print ('\n' + 'Please enter a number between 1 and 16, or press CTRL+C to exit.')
        main()
    except KeyboardInterrupt:
        sys.exit(0)
    except:
        print ('\n' + 'Not a valid number. Try again or press CTRL+C to exit.')
        main()
    else:
        iplist = []
        while count < user_input:
            count += 1
            try:
                # Present user with required number of 'input' prompt. Validate IP addresses and convert to hex
                wlc_ip = ipaddress.IPv4Address(input('WLC #' + str(count) + ' IP Address: '))
                wlc_ip = str(wlc_ip)
                wlc_ip = socket.inet_aton(wlc_ip).hex()
                # Don't allow duplicate entries and append to list
                if wlc_ip not in iplist:
                    iplist.append(wlc_ip)
                else:
                    count -= 1
                    print ('\n' + 'IP Address already entered. Try again or press CTRL+C to exit.')
            except KeyboardInterrupt:
                sys.exit(0)
            except:
                count -= 1
                print ('\n' + 'Not a valid IP Address. Try again or press CTRL+C to exit.')
            else:
                pass
        # Join hex formatted IP addresses together in single line, with no spacing
        hexlist = (''.join(iplist))
       # Convert IP count to hex/base 16, remove leading '0xf'. Print =< 2 digits or add leading '0' as required by Cisco
        hexcount = int(hex(len(iplist)*4), 16)
        hexcount = '{:02X}'.format(hexcount)
        # Combine and print output to screen for user
        print ('\n' + 'Your DHCP Option 43 value is: ' + 'f1' + hexcount + hexlist)

def main():
    if len(sys.argv) > 1:
        arg_mode()
    else:
        interactive_mode()
        
# Start Here

# Script is executed as main program
if __name__ == "__main__":
    main()
# Script has been imported from within another module
else:
    arg_mode()
