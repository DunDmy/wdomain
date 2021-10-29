import sys
import socket
from ipwhois import IPWhois

def main(argv):
    ips_text_file = argv[1]
    domain_out_file = argv[2]

    with open(ips_text_file, 'r') as reader:
            # handle a new line
            ips = (line.rstrip() for line in reader)
            domain_writer = open(domain_out_file, 'x') 
            # read line
            for ip in ips:
                print(ip)
                try:
                    domain_name = socket.gethostbyaddr(ip)
                    print("domain_name: " + str(domain_name))
                    domain_writer.write("domain_name: " + str(domain_name) + '\n')
                except:
                    print("domain_name: " + "REVERSE DNS FAILED!")
                    domain_writer.write("domain_name: " + "REVERSE DNS FAILED!\n")

                domain_obj = IPWhois(ip)
                # wrtie to file
                domain_writer.write(str(domain_obj.lookup_whois()))
                domain_writer.write('\n')
                # output to the screen
                print("asn_country_code: " + domain_obj.lookup_whois()['asn_country_code'])
                print("asn_description: " + domain_obj.lookup_whois()['asn_description'])
                print("name: " + domain_obj.lookup_whois()['nets'][0]['name'])
                print()
                
    reader.close()
    domain_writer.close()


if __name__ == "__main__":
    main(sys.argv)