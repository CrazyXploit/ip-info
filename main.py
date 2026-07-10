#!/usr/bin/env python3
"""
IP Info Script - Multi-Provider IP Geolocation Tool
Created by k1xtreme
GitHub: https://github.com/CrazyXploit/ip-info
"""

import json
import urllib.request
import urllib.error
import sys
from datetime import datetime
from typing import Dict, Optional, Any

PROVIDERS = {
    "ip-api.com": {
        "url": "http://ip-api.com/json/{ip}?fields=status,country,city,lat,lon,isp,org,as,timezone",
        "parser": lambda data: {
            "status": data.get("status"),
            "country": data.get("country"),
            "city": data.get("city"),
            "latitude": data.get("lat"),
            "longitude": data.get("lon"),
            "isp": data.get("isp"),
            "org": data.get("org"),
            "asn": data.get("as"),
            "timezone": data.get("timezone"),
            "provider": "ip-api.com"
        }
    },
    "ipwho.is": {
        "url": "http://ipwho.is/{ip}",
        "parser": lambda data: {
            "status": "success" if data.get("success") else "fail",
            "country": data.get("country"),
            "city": data.get("city"),
            "latitude": data.get("latitude"),
            "longitude": data.get("longitude"),
            "isp": data.get("connection", {}).get("isp"),
            "org": data.get("connection", {}).get("org"),
            "asn": data.get("connection", {}).get("asn"),
            "timezone": data.get("timezone", {}).get("id"),
            "provider": "ipwho.is"
        }
    },
    "ipinfo.io": {
        "url": "https://ipinfo.io/{ip}",
        "parser": lambda data: {
            "status": "success" if data.get("ip") else "fail",
            "country": data.get("country"),
            "city": data.get("city"),
            "latitude": data.get("loc", "").split(",")[0] if data.get("loc") else None,
            "longitude": data.get("loc", "").split(",")[1] if data.get("loc") else None,
            "isp": data.get("org"),
            "org": data.get("org"),
            "asn": None,
            "timezone": data.get("timezone"),
            "provider": "ipinfo.io"
        }
    },
    "ipapi.co": {
        "url": "https://ipapi.co/{ip}/json/",
        "parser": lambda data: {
            "status": "success" if data.get("ip") else "fail",
            "country": data.get("country_name"),
            "city": data.get("city"),
            "latitude": data.get("latitude"),
            "longitude": data.get("longitude"),
            "isp": data.get("org"),
            "org": data.get("org"),
            "asn": data.get("asn"),
            "timezone": data.get("timezone"),
            "provider": "ipapi.co"
        }
    },
    "geo.wp-statistics.com": {
        "url": "https://geo.wp-statistics.com/{ip}?format=json",
        "parser": lambda data: {
            "status": "success" if data.get("country") else "fail",
            "country": data.get("country"),
            "city": data.get("city"),
            "latitude": data.get("latitude"),
            "longitude": data.get("longitude"),
            "isp": data.get("isp"),
            "org": None,
            "asn": None,
            "timezone": data.get("timezone"),
            "provider": "geo.wp-statistics.com"
        }
    },
    "jaiho.ip": {
        "url": "https://jaiho-ip.vercel.app/api/json",
        "parser": lambda data: {
            "status": "success" if data.get("success") else "fail",
            "country": data.get("location", {}).get("country"),
            "city": data.get("location", {}).get("city"),
            "latitude": None,
            "longitude": None,
            "isp": data.get("isp", {}).get("name"),
            "org": data.get("isp", {}).get("org"),
            "asn": None,
            "timezone": None,
            "provider": "jaiho.ip"
        }
    }
}

def get_own_ip() -> str:
    services = [
        "https://api.ipify.org",
        "http://ifconfig.me/ip",
        "https://icanhazip.com"
    ]
    for service in services:
        try:
            req = urllib.request.Request(service, headers={"User-Agent": "IP-Info-Script/1.0"})
            with urllib.request.urlopen(req, timeout=5) as response:
                ip = response.read().decode("utf-8").strip()
                if ip:
                    return ip
        except:
            continue
    raise Exception("Could not detect your IP automatically")

def fetch_ip_info(ip: str) -> Dict[str, Any]:
    results = {}
    for name, provider in PROVIDERS.items():
        try:
            url = provider["url"].format(ip=ip)
            req = urllib.request.Request(url, headers={"User-Agent": "IP-Info-Script/1.0"})
            with urllib.request.urlopen(req, timeout=5) as response:
                data = json.loads(response.read().decode("utf-8"))
                results[name] = provider["parser"](data)
        except Exception as e:
            results[name] = {"status": "error", "message": str(e), "provider": name}
    return results

def get_best_result(results: Dict[str, Any]) -> Optional[Dict[str, Any]]:
    best = None
    best_score = -1
    for provider, data in results.items():
        if data.get("status") == "error":
            continue
        score = 0
        if data.get("country"): score += 1
        if data.get("city"): score += 1
        if data.get("latitude") and data.get("longitude"): score += 2
        if data.get("isp"): score += 1
        if data.get("asn"): score += 1
        if score > best_score:
            best_score = score
            best = data
            best["_provider"] = provider
    return best

def print_results(ip: str, results: Dict[str, Any]):
    print("\n" + "="*70)
    print(f"🌐 IP INFORMATION FOR: {ip}")
    print("="*70)
    print(f"📅 Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("="*70 + "\n")
    successful = sum(1 for data in results.values() if data.get("status") != "error")
    print(f"📡 Total Providers: {len(results)} | ✅ Successful: {successful} | ❌ Failed: {len(results) - successful}")
    print("\n" + "="*70 + "\n")
    
    best = get_best_result(results)
    if best:
        print("⭐ BEST RESULT (from {})".format(best.get("_provider", "Unknown")))
        print("-"*70)
        print(f"  🌍 Country: {best.get('country', 'N/A')}")
        print(f"  🏙️  City: {best.get('city', 'N/A')}")
        print(f"  📍 Coordinates: {best.get('latitude', 'N/A')}, {best.get('longitude', 'N/A')}")
        print(f"  🏢 ISP: {best.get('isp', 'N/A')}")
        print(f"  🏛️  Organization: {best.get('org', 'N/A')}")
        print(f"  🔢 ASN: {best.get('asn', 'N/A')}")
        print(f"  🕐 Timezone: {best.get('timezone', 'N/A')}")
        print("\n" + "="*70 + "\n")
    
    print("📋 ALL PROVIDERS DETAILS")
    print("-"*70)
    for provider, data in results.items():
        print(f"\n🔹 {provider.upper()}")
        print("  " + "-"*50)
        if data.get("status") == "error":
            print(f"  ❌ Error: {data.get('message')}")
        else:
            print(f"  🌍 Country: {data.get('country', 'N/A')}")
            print(f"  🏙️  City: {data.get('city', 'N/A')}")
            print(f"  📍 Coordinates: {data.get('latitude', 'N/A')}, {data.get('longitude', 'N/A')}")
            print(f"  🏢 ISP: {data.get('isp', 'N/A')}")
            print(f"  🏛️  Organization: {data.get('org', 'N/A')}")
            print(f"  🔢 ASN: {data.get('asn', 'N/A')}")
            print(f"  🕐 Timezone: {data.get('timezone', 'N/A')}")

def save_json_output(ip: str, results: Dict[str, Any], filename: str = None):
    if not filename:
        filename = f"ip_info_{ip.replace('.', '_')}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    output = {"ip": ip, "timestamp": datetime.now().isoformat(), "results": results}
    try:
        with open(filename, 'w') as f:
            json.dump(output, f, indent=2)
        print(f"\n💾 Results saved to: {filename}")
    except Exception as e:
        print(f"\n⚠️  Could not save JSON: {e}")

def main():
    print("""
╔═══════════════════════════════════════════════════════════════════════╗
║                   🌐 IP INFO SCRIPT v2.0                             ║
║         Multi-Provider IP Geolocation Tool                           ║
║         No signup | No API tokens | Free                             ║
║         Created by: k1xtreme                                         ║
╚═══════════════════════════════════════════════════════════════════════╝
    """)
    ip = input("📝 Enter IP address (press Enter for your own IP): ").strip()
    if not ip:
        print("\n🔍 Detecting your IP address...")
        try:
            ip = get_own_ip()
            print(f"✅ Your IP: {ip}")
        except Exception as e:
            print(f"❌ Error: {e}")
            sys.exit(1)
    print(f"\n🔍 Fetching info from all providers...")
    results = fetch_ip_info(ip)
    print_results(ip, results)
    save = input("\n💾 Save results to JSON? (y/n): ").strip().lower()
    if save == 'y':
        save_json_output(ip, results)
    print("\n✅ Done! Thanks for using IP Info Script.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Goodbye!")
        sys.exit(0)
