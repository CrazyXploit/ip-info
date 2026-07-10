<div align="center">

# 🌐 IP Info Script

### *Multi-Provider IP Geolocation Tool*

**Created by [k1xtreme](https://github.com/CrazyXploit)**

[![Python](https://img.shields.io/badge/Python-3.6+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![GitHub stars](https://img.shields.io/ github/stars/CrazyXploit/ip-info.svg)](https://github.com/CrazyXploit/ip-info/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/CrazyXploit/ip-info.svg)](https://github.com/CrazyXploit/ip-info/network)
[![Made with Termux](https://img.shields.io/badge/Made%20with-Termux-black.svg)](https://termux.com/)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/CrazyXploit/ip-info/graphs/commit-activity)

**No API Keys • No Signup • Completely Free**

</div>

---

## 📋 Table of Contents

- [✨ Features](#-features)
- [📸 Screenshots](#-screenshots)
- [🚀 Quick Start](#-quick-start)
- [📦 Providers Used](#-providers-used)
- [🔧 Installation](#-installation)
- [💻 Usage Examples](#-usage-examples)
- [📁 Output Format](#-output-format)
- [🛠️ Development](#️-development)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)
- [👨‍💻 Author](#-author)

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| 🔍 **IP Lookup** | Query any IPv4 address or auto-detect your own |
| 📡 **Multi-Provider** | Combines **6 different** geolocation services |
| 🚫 **No Authentication** | Zero API keys, tokens, or signup required |
| 💾 **JSON Export** | Save results to JSON for further analysis |
| ⭐ **Smart Ranking** | Shows the best result from all providers |
| 📊 **Detailed Output** | Country, city, coordinates, ISP, ASN, timezone |
| 🔄 **Redundancy** | If one provider fails, others still work |
| 🎯 **Termux Ready** | Optimized for Termux and command-line use |

---

## 📸 Screenshots

<div align="center">

**Running the Script**

```

╔═══════════════════════════════════════════════════════════════════════╗
║                   🌐 IP INFO SCRIPT v2.0                             ║
║         Multi-Provider IP Geolocation Tool                           ║
║         No signup | No API tokens | Free                             ║
║         Created by: k1xtreme                                         ║
╚═══════════════════════════════════════════════════════════════════════╝

📝 Enter IP address (press Enter for your own IP): 8.8.8.8

🔍 Fetching info from all providers...

```

**Sample Output**

```

======================================================================
🌐 IP INFORMATION FOR: 8.8.8.8
======================================================================
📅 Timestamp: 2026-07-10 14:30:25
======================================================================

📡 Total Providers: 6 | ✅ Successful: 6 | ❌ Failed: 0

======================================================================

⭐ BEST RESULT (from ip-api.com)

---

🌍 Country: United States
🏙️  City: Ashburn
📍 Coordinates: 39.03, -77.5
🏢 ISP: Google LLC
🏛️  Organization: Google Public DNS
🔢 ASN: AS15169 Google LLC
🕐 Timezone: America/New_York

======================================================================

📋 ALL PROVIDERS DETAILS

---

🔹 IP-API.COM

---

🌍 Country: United States
🏙️  City: Ashburn
📍 Coordinates: 39.03, -77.5
🏢 ISP: Google LLC
🏛️  Organization: Google Public DNS
🔢 ASN: AS15169 Google LLC
🕐 Timezone: America/New_York

🔹 IPWHO.IS

---

🌍 Country: United States
🏙️  City: Mountain View
📍 Coordinates: 37.3860517, -122.0838511
🏢 ISP: Google LLC
🏛️  Organization: Google LLC
🔢 ASN: 15169
🕐 Timezone: America/Los_Angeles

```

</div>

---

## 🚀 Quick Start

```bash
# Clone the repository
git clone https://github.com/CrazyXploit/ip-info.git
cd ip-info

# Run the script
python3 main.py
```

---

📦 Providers Used

This script leverages 6 different geolocation providers for maximum reliability:

# Provider HTTPS Rate Limit Data Provided
1 ip-api.com ❌ 45/min Country, City, Lat/Lon, ISP, ASN, Timezone
2 ipwho.is ❌ 250k/day Country, City, Lat/Lon, ISP, ASN, Proxy Detection
3 ipinfo.io ✅ 1k/day Country, City, Lat/Lon, ISP, Hostname
4 ipapi.co ✅ 1k/day Country, City, Lat/Lon, ISP, ASN
5 geo.wp-statistics.com ✅ Unlimited Country, City, Lat/Lon, ISP, Timezone
6 jaiho.ip ✅ Unlimited Country, City, ISP, Device Info

Note: Multiple providers ensure you always get results even if some services are down.

---

🔧 Installation

📱 Termux (Android)

```bash
# Update packages
pkg update && pkg upgrade -y

# Install Python and Git
pkg install python git -y

# Clone and run
git clone https://github.com/CrazyXploit/ip-info.git
cd ip-info
python3 main.py
```

🐧 Linux / macOS

```bash
# Install Python 3.6+ if not already installed
sudo apt-get install python3 git  # Ubuntu/Debian
# OR
brew install python3 git  # macOS

# Clone and run
git clone https://github.com/CrazyXploit/ip-info.git
cd ip-info
python3 main.py
```

🪟 Windows (WSL/Cygwin)

```bash
# Using WSL or Git Bash
git clone https://github.com/CrazyXploit/ip-info.git
cd ip-info
python main.py
```

---

💻 Usage Examples

Basic Usage

```bash
python3 main.py
```

Query Specific IP

```bash
# Enter this when prompted
8.8.8.8
```

Save Results to JSON

```bash
# When prompted after results
💾 Save results to JSON? (y/n): y
# Saves as: ip_info_8_8_8_8_20260710_143025.json
```

One-Liner (Detect Own IP)

```bash
echo "" | python3 main.py
```

With Custom IP via Pipe

```bash
echo "1.1.1.1" | python3 main.py
```

---

📁 Output Format

Console Output

· ⭐ Best Result: Smartly selected from all providers
· 📋 All Providers: Complete details from each service
· 📊 Statistics: Success/failure count per provider

JSON Output

```json
{
  "ip": "8.8.8.8",
  "timestamp": "2026-07-10T14:30:25.123456",
  "results": {
    "ip-api.com": {
      "status": "success",
      "country": "United States",
      "city": "Ashburn",
      "latitude": 39.03,
      "longitude": -77.5,
      "isp": "Google LLC",
      "org": "Google Public DNS",
      "asn": "AS15169 Google LLC",
      "timezone": "America/New_York"
    }
  }
}
```

---

🛠️ Development

Project Structure

```
ip-info-script/
├── main.py          # Main script
├── README.md        # This file
```

Dependencies

Zero external dependencies! Uses only Python standard library:

· json - JSON parsing
· urllib.request - HTTP requests
· sys - System operations
· datetime - Timestamps
· typing - Type hints

Adding New Providers

```python
PROVIDERS = {
    # ... existing providers ...
    "new-provider.com": {
        "url": "https://new-provider.com/api/{ip}",
        "parser": lambda data: {
            "status": "success",
            "country": data.get("country"),
            "city": data.get("city"),
            # ... map other fields
        }
    }
}
```

---

🤝 Contributing

Contributions are welcome! Here's how:

1. Fork the repository
2. Create a feature branch: git checkout -b feature/amazing-feature
3. Commit changes: git commit -m 'Add amazing feature'
4. Push to branch: git push origin feature/amazing-feature
5. Open a Pull Request

Guidelines

· Follow PEP 8 style guide
· Add comments for complex logic
· Test with multiple IP addresses
· Update README if adding features

---

📄 License

```
MIT License

Copyright (c) 2026 CrazyXploit (k1xtreme)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

👨‍💻 Author

CrazyXploit (k1xtreme)

· 🌐 GitHub: @CrazyXploit
· 📧 Email: k1xtreme@proton.me

---

⭐ Star History

If you find this tool useful, please consider giving it a star ⭐ on GitHub!

https://api.star-history.com/svg?repos=CrazyXploit/ip-info&type=Date

---

<div align="center">

Made with ❤️ by k1xtreme / Claude 

Last Updated: July 2026

</div>
