import sys
import argparse
import datetime

from src.scripts.methods.iplook import iplook_part
from src.scripts.methods.ping import ping_part
from src.scripts.methods.http import http_part
from src.scripts.methods.tcp import tcp_part
from src.scripts.methods.udp import udp_part
from src.scripts.methods.dns import dns_part


def parser_help_trigger(parser):
    help_text = """
    iplook: website location search
    ...
    """
    return help_text


def parser_error_trigger(error_info):
    print(datetime.datetime.now().strftime("%H:%M:%S"), "{ error } inf:", error_info)
    sys.exit()


def logo_part():
    logo_text = """
              __           __       __            __ 
         ____/ /  ___ ____/ /______/ /  ___  ___ / /_
        / __/ _ \/ -_) __/  '_/___/ _ \/ _ \(_-</ __/
        \__/_//_/\__/\__/_/\_\   /_//_/\___/___/\__/ v1.2 / https://github.com/diasnull                                  
                            ــــــــﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ٨ــــ
    """
    return logo_text


def methods_part():
    while True:
        if args.iplook:
            iplook_part(args)
            break
        elif args.ping:
            ping_part(args)
            break
        elif args.http:
            http_part(args)
            break
        elif args.tcp:
            tcp_part(args)
            break
        elif args.udp:
            udp_part(args)
            break
        elif args.dns:
            dns_part(args)
            break
        print(datetime.datetime.now().strftime("%H:%M:%S"), "{ error } inf: no method selected.")
        break


def arg_parser_part():
    parser = argparse.ArgumentParser()
    parser.error = parser_error_trigger
    parser.format_help = lambda: parser_help_trigger(parser)
    parser.add_argument("-f", "--file", help="File containing list of IP addresses")
    parser.add_argument("-t", "--target", required=False, help="Target IP address or URL")
    parser.add_argument("--iplook", dest="iplook", action="store_true")
    parser.add_argument("--ping", dest="ping", action="store_true")
    parser.add_argument("--http", dest="http", action="store_true")
    parser.add_argument("--tcp", dest="tcp", action="store_true")
    parser.add_argument("--udp", dest="udp", action="store_true")
    parser.add_argument("--dns", dest="dns", action="store_true")
    return parser.parse_args()
if __name__ == '__main__':
    args = arg_parser_part()

    ip_address = None  # Initialize ip_address variable

    # Check if file argument is provided
    if args.file:
        with open(args.file, 'r') as file:
            ip_addresses = file.read().splitlines()


        # Perform ping check for each IP address
        for ip in ip_addresses:
            args.target = ip
            print(f"IP being checked: {ip}")  # Print the IP address being checked
            ip_address, status = ping_part(args)  # Get IP address and status
            print(f"Status: {status}")

    else:
        methods_part()
