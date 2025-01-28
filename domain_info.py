import dns.resolver
import whois
import requests

def get_dns_info(domain):
    # Obtain Cname info
    try:
        cname_records = dns.resolver.resolve(domain, 'CNAME')
        print(f"CNAME Records: {[str(record) for record in cname_records]}")
    except Exception as e:
        print(f"No CNAME records found: {e}")

    # 获取A记录（IP地址）
    try:
        a_records = dns.resolver.resolve(domain, 'A')
        ip_addresses = [str(record) for record in a_records]
        print(f"IP Addresses: {ip_addresses}")
        return ip_addresses
    except Exception as e:
        print(f"No A records found: {e}")
        return []

def get_whois_info(domain):
    try:
        domain_info = whois.whois(domain)
        print("Domain Ownership Info:")
        print(f"Domain Name: {domain_info.domain_name}")
        print(f"Registrar: {domain_info.registrar}")
        print(f"Creation Date: {domain_info.creation_date}")
        print(f"Expiration Date: {domain_info.expiration_date}")
        print(f"Name Servers: {domain_info.name_servers}")
    except Exception as e:
        print(f"Error retrieving WHOIS info: {e}")

def get_ip_location(ip):
    try:
        response = requests.get(f"https://ipinfo.io/{ip}/json")
        location_info = response.json()
        print(f"Location Info for {ip}:")
        print(location_info)
    except Exception as e:
        print(f"Error retrieving location info: {e}")

def main():
    domain = input("Please enter the domain: ")
    
    # 获取DNS信息
    ip_addresses = get_dns_info(domain)

    # 获取WHOIS信息
    get_whois_info(domain)

    # 获取IP地址的地理位置
    for ip in ip_addresses:
        get_ip_location(ip)

if __name__ == "__main__":
    main() 
