#!/usr/bin/env python3
"""
SPIRIT GUIDE - COMPLETE GLOBAL MARKET AUTOMATION
Handles all markets: Asia, Europe, Americas, Middle East, Africa
"""

import json
import time
import webbrowser
from datetime import datetime

class GlobalMarkets:
    def __init__(self):
        self.tokens = {
            "PIDX": {"address": "0x95c7e2d53f4b615a50d4468dfd5aff850dc17f0c"},
            "SGUIDE": {"address": "0xb50DCEb0570557B9B7FE43D8cBDc9B3457D3dc5a"},
            "VDOO": {"address": "0x38e4f08D08b4D772A7B75669C356b4749dd2d30b"},
            "PENNIES": {"address": "0x2a92CAA3b01E64634e2E95AA533a5570a76c19A7"}
        }
        
        self.markets = {
            "Asia": {
                "exchanges": [
                    {"name": "OKX", "url": "https://www.okx.com/apply-listing", "country": "China"},
                    {"name": "Gate.io", "url": "https://www.gate.io/listing-application", "country": "China"},
                    {"name": "HTX", "url": "https://www.htx.com/en-us/apply-listing", "country": "China"},
                    {"name": "bitFlyer", "url": "https://bitflyer.com/apply-listing", "country": "Japan"},
                    {"name": "Coincheck", "url": "https://coincheck.com/apply", "country": "Japan"},
                    {"name": "GMO Coin", "url": "https://coin.z.com/apply", "country": "Japan"},
                    {"name": "Upbit", "url": "https://upbit.com/apply", "country": "Korea"},
                    {"name": "Bithumb", "url": "https://bithumb.com/apply", "country": "Korea"},
                    {"name": "Coinone", "url": "https://coinone.co.kr/apply", "country": "Korea"},
                    {"name": "Crypto.com", "url": "https://crypto.com/apply", "country": "Singapore"},
                    {"name": "Coinhako", "url": "https://coinhako.com/apply", "country": "Singapore"},
                    {"name": "OSL", "url": "https://osl.com/apply", "country": "Hong Kong"},
                    {"name": "HashKey", "url": "https://hashkey.com/apply", "country": "Hong Kong"}
                ]
            },
            "Europe": {
                "exchanges": [
                    {"name": "Binance", "url": "https://www.binance.com/en/apply-listing", "country": "Global"},
                    {"name": "Kraken", "url": "https://www.kraken.com/apply-listing", "country": "UK"},
                    {"name": "Bitstamp", "url": "https://www.bitstamp.net/apply-listing", "country": "UK"},
                    {"name": "Coinbase", "url": "https://www.coinbase.com/apply-listing", "country": "USA"},
                    {"name": "eToro", "url": "https://www.etoro.com/apply-listing", "country": "UK"},
                    {"name": "Revolut", "url": "https://www.revolut.com/apply-listing", "country": "UK"},
                    {"name": "Bybit", "url": "https://www.bybit.com/apply-listing", "country": "Global"},
                    {"name": "KuCoin", "url": "https://www.kucoin.com/apply-listing", "country": "Global"},
                    {"name": "Bitfinex", "url": "https://www.bitfinex.com/apply-listing", "country": "Global"},
                    {"name": "Crypto.com", "url": "https://crypto.com/apply", "country": "Global"}
                ]
            },
            "Americas": {
                "exchanges": [
                    {"name": "Coinbase", "url": "https://www.coinbase.com/apply-listing", "country": "USA"},
                    {"name": "Kraken", "url": "https://www.kraken.com/apply-listing", "country": "USA"},
                    {"name": "Gemini", "url": "https://www.gemini.com/apply-listing", "country": "USA"},
                    {"name": "Bitstamp", "url": "https://www.bitstamp.net/apply-listing", "country": "USA"},
                    {"name": "Robinhood", "url": "https://www.robinhood.com/apply-listing", "country": "USA"},
                    {"name": "Crypto.com", "url": "https://crypto.com/apply", "country": "USA"},
                    {"name": "OKX", "url": "https://www.okx.com/apply-listing", "country": "USA"},
                    {"name": "Binance.US", "url": "https://www.binance.us/apply-listing", "country": "USA"}
                ]
            },
            "Middle East": {
                "exchanges": [
                    {"name": "Binance", "url": "https://www.binance.com/en/apply-listing", "country": "UAE"},
                    {"name": "Bitoasis", "url": "https://www.bitoasis.net/apply-listing", "country": "UAE"},
                    {"name": "Rain", "url": "https://www.rain.com/apply-listing", "country": "Bahrain"},
                    {"name": "CoinMENA", "url": "https://www.coinmena.com/apply-listing", "country": "Bahrain"}
                ]
            },
            "Africa": {
                "exchanges": [
                    {"name": "Binance", "url": "https://www.binance.com/en/apply-listing", "country": "Nigeria"},
                    {"name": "Luno", "url": "https://www.luno.com/apply-listing", "country": "South Africa"},
                    {"name": "Valr", "url": "https://www.valr.com/apply-listing", "country": "South Africa"}
                ]
            }
        }

    def show_all_markets(self):
        """Show all markets and exchanges"""
        print("\n🌍 COMPLETE GLOBAL MARKET COVERAGE")
        print("=" * 60)
        print(f"⏰ {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("")
        
        total = 0
        for region, data in self.markets.items():
            print(f"🌏 {region} ({len(data['exchanges'])} exchanges):")
            for ex in data['exchanges']:
                print(f"    🇨🇳 {ex['country']}: {ex['name']} - {ex['url']}")
                total += 1
            print("")
        
        print(f"📊 TOTAL EXCHANGES: {total}")
        return total

    def open_all_links(self):
        """Open all exchange links"""
        print("\n🔗 OPENING ALL GLOBAL EXCHANGE LINKS")
        print("=" * 60)
        
        total = 0
        for region, data in self.markets.items():
            print(f"\n🌏 {region}:")
            for ex in data['exchanges']:
                print(f"  Opening {ex['name']} ({ex['country']})...")
                try:
                    webbrowser.open(ex['url'])
                    print(f"    ✅ Opened {ex['name']}")
                    time.sleep(1)
                    total += 1
                except:
                    print(f"    ⚠️ Could not open {ex['name']}")
        
        print(f"\n✅ Opened {total} exchange links")

    def generate_report(self):
        """Generate complete market report"""
        report = {
            "timestamp": datetime.now().isoformat(),
            "tokens": self.tokens,
            "markets": self.markets,
            "total_exchanges": sum(len(data['exchanges']) for data in self.markets.values()),
            "status": "READY"
        }
        
        with open("global_markets_report.json", "w") as f:
            json.dump(report, f, indent=2)
        
        print("\n✅ Global markets report saved: global_markets_report.json")
        return report

def main():
    print("🌍 SPIRIT GUIDE - COMPLETE GLOBAL MARKET AUTOMATION")
    print("====================================================")
    print("✅ Covers all markets: Asia, Europe, Americas, Middle East, Africa")
    print("")
    
    markets = GlobalMarkets()
    
    print("📊 Choose an option:")
    print("  1. Show all global markets")
    print("  2. Open all exchange links")
    print("  3. Generate global report")
    print("  4. Full automation (all steps)")
    print("")
    
    choice = input("Enter choice (1-4): ").strip()
    
    if choice == "1":
        markets.show_all_markets()
    elif choice == "2":
        markets.open_all_links()
    elif choice == "3":
        markets.generate_report()
    elif choice == "4":
        print("\n🚀 RUNNING FULL GLOBAL AUTOMATION...")
        markets.show_all_markets()
        markets.open_all_links()
        markets.generate_report()
        print("\n✅ FULL GLOBAL AUTOMATION COMPLETE!")
    else:
        print("❌ Invalid choice")

if __name__ == "__main__":
    main()
