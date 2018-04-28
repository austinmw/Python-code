from general import *
from domain_name import *
from ip_address import *
from nmap import *
from robots_txt import *
from whois import *

ROOT_DIR = 'targets'
create_dir(ROOT_DIR)

def gather_info(name, url):
	domain_name = get_domain_name(url)
	ip_address = get_ip_address(domain_name)
	nmap = get_nmap('-F', ip_address)  # ('-F', ip_address) - this is the linux version
	try:
		robots_txt = get_robots_txt(url)
	except:
		robots_txt = "blank"
	whois = get_whois(domain_name)
	create_report(name, url, domain_name, ip_address, nmap, robots_txt, whois)

def create_report(name, full_url, domain_name, ip_address, nmap, robots_txt, whois):
	project_dir = ROOT_DIR + '/' + name
	create_dir(project_dir)
	write_file(project_dir + '/full_url.txt', full_url)
	write_file(project_dir + '/domain_name.txt', domain_name)
	write_file(project_dir + '/ipaddress.txt', ip_address)
	write_file(project_dir + '/nmap.txt', nmap)
	if robots_txt != None:
		write_file(project_dir + '/robots.txt', robots_txt)
	write_file(project_dir + '/whois.txt', whois)


#gather_info('amwbot', 'https://www.amwbot.com/')
#to run: $ python3, >>> from main import *, >>> gather_info(...)



