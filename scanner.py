
PROJECT: Network Port Scanner
AUTHOR: Muhammadh Nuwaf
COURSE: Pearson BTEC HND in Computing (Cyber Security)
MODULE: Network Security / Python for Security
DATE: June 2026

PURPOSE:
This tool scans a target IP or domain to identify open ports.
In cybersecurity, port scanning helps understand a system's attack surface
- what services are running and potentially vulnerable.

DISCLAIMER:
This tool is for educational purposes and authorised testing only.
Unauthorised scanning violates computer misuse laws.

import socket
import time
from datetime import datetime

services = {
    20: "FTP-Data",
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    110: "POP3",
    143: "IMAP",
    53: "DNS",
    80: "HTTP",
    443: "HTTPS",
    8080: "HTTP-Alt",
    8443: "HTTPS-Alt",
    3306: "MySQL",
    5432: "PostgreSQL",
    3389: "RDP",
    445: "SMB",
    5900: "VNC",
}

def get_service(port):
    return services.get(port, "Unknown")

print("=" * 60)
print("    PROFESSIONAL PORT SCANNER")
print("    Muhammadh Nuwaf - HND Cyber Security")
print("=" * 60)

target = input("Enter IP or domain (e.g., scanme.nmap.org or 192.168.1.1): ")

try:
    socket.gethostbyname(target)
    print(f"✅ Target resolved successfully: {target}\n")
except:
    print("❌ Error: Could not resolve hostname. Please check the address.")
    input("Press Enter to exit...")
    exit()

while True:
    try:
        start_port = int(input("Enter START port (1-65535): "))
        end_port = int(input("Enter END port (1-65535): "))

        if start_port < 1 or end_port > 65535:
            print("❌ Error: Ports must be between 1 and 65535\n")
        elif start_port > end_port:
            print("❌ Error: Start port cannot be greater than end port\n")
        else:
            break
    except ValueError:
        print("❌ Error: Please enter valid numbers only\n")

print(f"\n🔍 Scanning {target} from port {start_port} to {end_port}")
print("⏳ Scanning in progress...")
print("💡 Tip: Scan smaller ranges like 1-100 for faster results\n")

open_ports = []
start_time = time.time()

for port in range(start_port, end_port + 1):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.3)

        result = sock.connect_ex((target, port))

        if result == 0:
            service = get_service(port)
            print(f"  ✅ Port {port:5d} - OPEN    ({service})")
            open_ports.append(port)

        sock.close()

        if port % 50 == 0:
            print(f"     [Progress: {port}/{end_port} ports scanned...]", end="\r")

    except KeyboardInterrupt:
        print("\n\n⚠️ Scan interrupted by user (Ctrl+C pressed)")
        break
    except:
        print("\n❌ Network error occurred - check your connection")
        break

end_time = time.time()
duration = end_time - start_time

print("\n" + "=" * 60)
print("SCAN COMPLETE")
print("=" * 60)

if open_ports:
    print(f"✅ Found {len(open_ports)} open port(s) in {duration:.2f} seconds:\n")
    print("   PORT    SERVICE")
    print("   " + "-" * 30)

    for port in open_ports:
        print(f"   {port:5d}    {get_service(port)}")
else:
    print("❌ No open ports found in the specified range")
    print("   Possible reasons:")
    print("   • A firewall is blocking the scan")
    print("   • The target is offline")
    print("   • All ports are filtered/closed")

print(f"\n⏱️  Total scan time: {duration:.2f} seconds")
print(f"📅 Scan completed: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

save = input("\n💾 Save results to file? (y/n): ").lower()

if save == 'y':
    safe_target = target.replace('.', '_')
    filename = f"port_scan_{safe_target}_{start_port}-{end_port}.txt"

    with open(filename, 'w') as f:
        f.write("=" * 60 + "\n")
        f.write("PORT SCAN REPORT\n")
        f.write("=" * 60 + "\n")
        f.write(f"Student: Muhammadh Nuwaf\n")
        f.write(f"Target: {target}\n")
        f.write(f"Date/Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"Port Range: {start_port} - {end_port}\n")
        f.write(f"Scan Duration: {duration:.2f} seconds\n")
        f.write(f"Open Ports Found: {len(open_ports)}\n\n")

        if open_ports:
            f.write("OPEN PORTS DETAILS:\n")
            f.write("-" * 40 + "\n")
            f.write(f"{'PORT':<8} {'SERVICE':<15} {'RISK NOTE':<20}\n")
            f.write("-" * 40 + "\n")

            for port in open_ports:
                service = get_service(port)

                if port in [21, 23, 25, 80, 110, 143, 445]:
                    risk = "Potential risk"
                elif port in [22, 443, 3389]:
                    risk = "Monitor access"
                else:
                    risk = "Investigate"

                f.write(f"{port:<8} {service:<15} {risk:<20}\n")
        else:
            f.write("No open ports were discovered.\n")

        f.write("\n" + "=" * 60 + "\n")
        f.write("DISCLAIMER: This scan was performed for educational purposes\n")
        f.write("on authorised targets only.\n")

    print(f"✅ Report saved to: {filename}")
    print(f"   Location: {__file__} folder")

print("\n" + "=" * 60)
print("📚 WHAT I LEARNED FROM THIS PROJECT:")
print("=" * 60)
print("  1. TCP handshake and how ports work")
print("  2. Python socket programming for network tools")
print("  3. Timeout management for performance tuning")
print("  4. Error handling for robust security tools")
print("  5. Common port numbers and their services")
print("  6. Why port scanning is the first step in reconnaissance")

print("\n🔐 Next steps for improvement:")
print("  • Add threading for faster scanning")
print("  • Add banner grabbing to identify service versions")
print("  • Create a GUI version using tkinter")
print("  • Add OS fingerprinting")

input("\nPress Enter to exit...")