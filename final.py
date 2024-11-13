with open('server_log.txt', 'r') as file:
    logs = file.readlines()
ip_count = {}
for line in logs:
    ip = line.split()[0]  # La IP está al inicio de cada línea
    if ip in ip_count:
        ip_count[ip] += 1
    else:
        ip_count[ip] = 1
print("IPs y número de accesos:")
for ip, count in ip_count.items():
    print(ip, ":", count)
page_count = {}
for line in logs:
    page = line.split()[6]  # La URL está en la columna 6
    if page in page_count:
        page_count[page] += 1
    else:
        page_count[page] = 1

most_visited = sorted(page_count.items(), key=lambda x: x[1], reverse=True)[:3]
print("\nLas 3 páginas más visitadas:")
for page, count in most_visited:
    print(page, ":", count)

total_accesses = len(logs)
success_count = sum(1 for line in logs if " 200 " in line)
success_percentage = (success_count / total_accesses) * 100
print(f"\nPorcentaje de accesos exitosos (código 200): {success_percentage:.2f}%")