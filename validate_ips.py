def validate_ip(ip):
    status = True
    for group in ip.split('.'): # [ '200', '134', ..]
        status &= validate_group(group)
    return status


def validate_group(group):
    group_int = int(group)
    return 0 <= group_int <= 255


ips_file = open("ips.txt", encoding='utf-8')
validos_file = open("validos.txt", 'w', encoding='utf-8')
invalidos_file = open("invalidos.txt", 'w', encoding='utf-8')

for ip in ips_file.readlines():
    ip = ip.strip()
    if validate_ip(ip):
        validos_file.write("%s\n" % ip)
    else:
        invalidos_file.write("%s\n" % ip)

ips_file.close()
validos_file.close()
invalidos_file.close()
