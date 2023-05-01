import urllib.request
external_ip1 = urllib.request.urlopen('https://v4.ident.me/ ').read().decode('utf8')
print(external_ip1)