import sys
import ipaddress
import socket

def main():
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
                # Present user with required number of input prompts & validate IP addresses
                wlc_ip = ipaddress.IPv4Address(input('WLC #' + str(count) + ' IP Address: '))
                # Convert IP address to string
                wlc_ip = str(wlc_ip)
                # Convert IP address strings to hex & append to list 
                wlc_ip = socket.inet_aton(wlc_ip).hex()
                if wlc_ip not in iplist:
                    iplist.append(wlc_ip)
                else:
                    if wlc_ip in iplist:
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
        # Convert IP count to hex/base 16, remove leading '0xf'
        hexcount = int(hex(len(iplist)*4), 16)
        # Print at least two digits, add leaging '0' where required
        hexcount = '{:02X}'.format(hexcount)
        # Combine and print output to screen for user
        print ('\n' + 'Your DHCP Option 43 value is: ' + 'f1' + hexcount + hexlist)

# Start Here
if __name__ == "__main__":
    main()
