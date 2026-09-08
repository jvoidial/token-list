#!/usr/bin/env python3
"""
SPIRIT GUIDE - WHAT'S LEFT VERIFICATION
Shows exactly what remains for eToro
"""

import json
import time
import requests
from datetime import datetime

class WhatsLeftVerification:
    def __init__(self):
        self.tokens = {
            "PIDX": {"address": "0x95c7e2d53f4b615a50d4468dfd5aff850dc17f0c"},
            "SGUIDE": {"address": "0xb50DCEb0570557B9B7FE43D8cBDc9B3457D3dc5a"},
            "VDOO": {"address": "0x38e4f08D08b4D772A7B75669C356b4749dd2d30b"},
            "PENNIES": {"address": "0x2a92CAA3b01E64634e2E95AA533a5570a76c19A7"}
        }
        
        self.requirements = {
            "coingecko": {"status": "✅ DONE", "need": "Already confirmed"},
            "superchain": {"status": "✅ DONE", "need": "Already added"},
            "token_lists": {"status": "✅ DONE", "need": "Already added"},
            "pancakeswap": {"status": "✅ DONE", "need": "Already added"},
            "geckoterminal": {"status": "✅ DONE", "need": "Auto-sync active"},
            "liquidity": {"status": "✅ DONE", "need": "Pools confirmed"},
            "dexscreener": {"status": "⏳ PENDING", "need": "Wait 24-48 hours"},
            "volume": {"status": "❌ NEEDED", "need": "Start trading"},
            "audit": {"status": "❌ NEEDED", "need": "Plan budget $15k-50k"},
            "community": {"status": "❌ NEEDED", "need": "Build 10k+ members"},
            "time": {"status": "❌ NEEDED", "need": "Need 6 months track record"}
        }

    def check_dexscreener(self):
        """Check current DexScreener status"""
        print("\n📊 CHECKING DEXSCREENER STATUS...")
        found = 0
        for symbol, info in self.tokens.items():
            try:
                response = requests.get(
                    f"https://api.dexscreener.com/latest/dex/tokens/{info['address']}",
                    timeout=10
                )
                if response.status_code == 200:
                    data = response.json()
                    if data.get("pairs"):
                        print(f"  ✅ {symbol}: FOUND")
                        found += 1
                    else:
                        print(f"  ⏳ {symbol}: Pending")
                else:
                    print(f"  ⚠️ {symbol}: API error")
            except:
                print(f"  ⚠️ {symbol}: Connection error")
        
        if found == len(self.tokens):
            self.requirements["dexscreener"]["status"] = "✅ DONE"
            print(f"\n✅ ALL {found} TOKENS FOUND ON DEXSCREENER!")
        else:
            print(f"\n⏳ {found}/{len(self.tokens)} tokens found")
        
        return found

    def show_whats_left(self):
        """Show what's left clearly"""
        print("\n" + "="*60)
        print("🔍 WHAT'S LEFT FOR ETORO")
        print("="*60)
        print(f"⏰ {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("")
        
        # Check DexScreener first
        self.check_dexscreener()
        
        print("\n📋 COMPLETE REQUIREMENTS STATUS")
        print("-" * 40)
        
        for req, data in self.requirements.items():
            print(f"  {data['status']} {req.upper()}: {data['need']}")
        
        print("\n" + "="*60)
        print("🎯 WHAT YOU NEED TO DO:")
        print("-" * 40)
        
        needs = []
        for req, data in self.requirements.items():
            if "NEEDED" in data['status'] or "PENDING" in data['status']:
                if data['status'] == "❌ NEEDED":
                    needs.append(f"  - {req.upper()}: {data['need']}")
                elif data['status'] == "⏳ PENDING":
                    needs.append(f"  - {req.upper()}: {data['need']}")
        
        if needs:
            for need in needs:
                print(need)
        else:
            print("  ✅ EVERYTHING IS DONE! Ready for eToro!")
        
        print("\n" + "="*60)
        print("🚀 PRIORITY ACTIONS:")
        print("-" * 40)
        
        # Priority order
        priorities = [
            ("DexScreener", "⏳ PENDING"),
            ("Volume", "❌ NEEDED"),
            ("Audit", "❌ NEEDED"),
            ("Community", "❌ NEEDED"),
            ("Time", "❌ NEEDED")
        ]
        
        for name, status in priorities:
            current = self.requirements[name.lower()]['status']
            if current == status:
                print(f"  🔴 {name}: {self.requirements[name.lower()]['need']}")
        
        print("")
        print("✅ Verification complete!")

def main():
    verify = WhatsLeftVerification()
    verify.show_whats_left()

if __name__ == "__main__":
    main()
