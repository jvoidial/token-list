#!/usr/bin/env python3
"""
SPIRIT GUIDE - REMAINING TASKS AUTOMATION
Handles everything that's left
"""

import json
import time
import requests
import os
import webbrowser
from datetime import datetime, timedelta

class RemainingAutomation:
    def __init__(self):
        self.tokens = {
            "PIDX": {"address": "0x95c7e2d53f4b615a50d4468dfd5aff850dc17f0c"},
            "SGUIDE": {"address": "0xb50DCEb0570557B9B7FE43D8cBDc9B3457D3dc5a"},
            "VDOO": {"address": "0x38e4f08D08b4D772A7B75669C356b4749dd2d30b"},
            "PENNIES": {"address": "0x2a92CAA3b01E64634e2E95AA533a5570a76c19A7"}
        }
        
        self.asian_exchanges = [
            {"name": "OKX", "country": "China", "url": "https://www.okx.com/apply-listing"},
            {"name": "Gate.io", "country": "China", "url": "https://www.gate.io/listing-application"},
            {"name": "HTX", "country": "China", "url": "https://www.htx.com/en-us/apply-listing"},
            {"name": "bitFlyer", "country": "Japan", "url": "https://bitflyer.com/apply-listing"},
            {"name": "Coincheck", "country": "Japan", "url": "https://coincheck.com/apply"},
            {"name": "GMO Coin", "country": "Japan", "url": "https://coin.z.com/apply"},
            {"name": "Upbit", "country": "Korea", "url": "https://upbit.com/apply"},
            {"name": "Bithumb", "country": "Korea", "url": "https://bithumb.com/apply"},
            {"name": "Coinone", "country": "Korea", "url": "https://coinone.co.kr/apply"},
            {"name": "Crypto.com", "country": "Singapore", "url": "https://crypto.com/apply"},
            {"name": "Coinhako", "country": "Singapore", "url": "https://coinhako.com/apply"},
            {"name": "OSL", "country": "Hong Kong", "url": "https://osl.com/apply"},
            {"name": "HashKey", "country": "Hong Kong", "url": "https://hashkey.com/apply"}
        ]
        
        self.tracking_file = "remaining_tasks.json"
        self.load_tracking()

    def load_tracking(self):
        """Load tracking data"""
        if os.path.exists(self.tracking_file):
            try:
                with open(self.tracking_file, 'r') as f:
                    self.data = json.load(f)
            except:
                self.data = self.default_data()
        else:
            self.data = self.default_data()

    def default_data(self):
        """Default tracking data"""
        return {
            "start_date": datetime.now().isoformat(),
            "dexscreener": {"checked": False, "found": False},
            "volume": {"started": False, "daily_target": 50000},
            "exchanges": {ex["name"]: {"applied": False, "date": None} for ex in self.asian_exchanges},
            "audit": {"planned": False, "completed": False},
            "months": 0
        }

    def save_tracking(self):
        """Save tracking data"""
        with open(self.tracking_file, 'w') as f:
            json.dump(self.data, f, indent=2)

    def check_dexscreener(self):
        """Check all tokens on DexScreener"""
        print("\n📊 CHECKING DEXSCREENER...")
        found_count = 0
        
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
                        found_count += 1
                        self.data["dexscreener"]["found"] = True
                    else:
                        print(f"  ⏳ {symbol}: Pending")
                else:
                    print(f"  ⚠️ {symbol}: Error {response.status_code}")
            except:
                print(f"  ⚠️ {symbol}: Connection error")
        
        self.data["dexscreener"]["checked"] = True
        self.save_tracking()
        
        if found_count == len(self.tokens):
            print(f"\n✅ ALL {found_count} TOKENS FOUND ON DEXSCREENER!")
            return True
        else:
            print(f"\n⏳ {found_count}/{len(self.tokens)} tokens found")
            return False

    def show_volume_instructions(self):
        """Show volume building instructions"""
        print("\n📈 VOLUME BUILDING INSTRUCTIONS")
        print("=" * 50)
        print("🔐 No private key needed - Use Uniswap UI")
        print("")
        print("🌐 Open these links and make small trades daily:")
        for symbol, info in self.tokens.items():
            print(f"  {symbol}: https://app.uniswap.org/#/swap?chain=base&outputCurrency={info['address']}")
        print("")
        print(f"🎯 DAILY TARGET: ${self.data['volume']['daily_target']:,}")
        print("")
        
        if not self.data["volume"]["started"]:
            start = input("Have you started building volume? (y/n): ").strip().lower()
            if start == 'y':
                self.data["volume"]["started"] = True
                self.save_tracking()
                print("✅ Volume building started!")

    def open_exchange_links(self):
        """Open Asian exchange application links"""
        print("\n🌏 OPENING ASIAN EXCHANGE APPLICATION LINKS...")
        print("=" * 50)
        
        unapplied = [ex for ex in self.asian_exchanges if not self.data["exchanges"][ex["name"]]["applied"]]
        
        if not unapplied:
            print("✅ All exchanges have been applied to!")
            return
        
        print(f"📊 {len(unapplied)} exchanges remaining to apply:")
        for ex in unapplied:
            print(f"  🇨🇳 {ex['country']}: {ex['name']} - {ex['url']}")
        
        print("\n🔗 Opening all unapplied exchange links...")
        for ex in unapplied:
            try:
                webbrowser.open(ex['url'])
                print(f"  ✅ Opened {ex['name']}")
                self.data["exchanges"][ex["name"]]["applied"] = True
                self.data["exchanges"][ex["name"]]["date"] = datetime.now().isoformat()
                self.save_tracking()
                time.sleep(1)
            except:
                print(f"  ⚠️ Could not open {ex['name']} - copy URL manually")

    def mark_applied(self):
        """Mark exchanges as applied"""
        print("\n📝 MARK EXCHANGES AS APPLIED")
        print("=" * 50)
        
        unapplied = [ex for ex in self.asian_exchanges if not self.data["exchanges"][ex["name"]]["applied"]]
        
        if not unapplied:
            print("✅ All exchanges are already marked as applied!")
            return
        
        print("Exchanges not yet applied:")
        for i, ex in enumerate(unapplied, 1):
            print(f"  {i}. {ex['name']} ({ex['country']})")
        
        print("\nEnter exchange name or number to mark as applied (or 'all'):")
        choice = input("> ").strip()
        
        if choice.lower() == "all":
            for ex in unapplied:
                self.data["exchanges"][ex["name"]]["applied"] = True
                self.data["exchanges"][ex["name"]]["date"] = datetime.now().isoformat()
            print("✅ All exchanges marked as applied!")
        else:
            try:
                idx = int(choice) - 1
                if 0 <= idx < len(unapplied):
                    ex = unapplied[idx]
                    self.data["exchanges"][ex["name"]]["applied"] = True
                    self.data["exchanges"][ex["name"]]["date"] = datetime.now().isoformat()
                    print(f"✅ {ex['name']} marked as applied!")
                else:
                    print("❌ Invalid number")
            except ValueError:
                # Try by name
                for ex in unapplied:
                    if ex["name"].lower() == choice.lower():
                        self.data["exchanges"][ex["name"]]["applied"] = True
                        self.data["exchanges"][ex["name"]]["date"] = datetime.now().isoformat()
                        print(f"✅ {ex['name']} marked as applied!")
                        break
                else:
                    print(f"❌ Exchange '{choice}' not found")
        
        self.save_tracking()

    def show_audit_info(self):
        """Show security audit information"""
        print("\n🔐 SECURITY AUDIT INFORMATION")
        print("=" * 50)
        print("eToro requires a professional security audit")
        print("")
        print("Recommended firms:")
        print("  1. CertiK: https://certik.com")
        print("  2. Hacken: https://hacken.io")
        print("  3. Trail of Bits: https://trailofbits.com")
        print("")
        print("💰 Cost: $15,000 - $50,000")
        print("⏰ Timeline: 2-4 weeks")
        print("")
        
        if not self.data["audit"]["planned"]:
            plan = input("Have you planned the security audit? (y/n): ").strip().lower()
            if plan == 'y':
                self.data["audit"]["planned"] = True
                self.save_tracking()
                print("✅ Audit planned!")
            else:
                print("⏳ Please plan the audit - this is required for eToro")

    def show_progress(self):
        """Show overall progress"""
        print("\n📊 OVERALL PROGRESS")
        print("=" * 50)
        
        # Calculate progress
        total_tasks = 5
        completed = 0
        
        # 1. DexScreener
        if self.data["dexscreener"]["found"]:
            completed += 1
            print("✅ DexScreener: COMPLETE")
        else:
            print("⏳ DexScreener: PENDING (24-48 hours)")
        
        # 2. Volume
        if self.data["volume"]["started"]:
            completed += 1
            print("✅ Volume Building: STARTED")
        else:
            print("❌ Volume Building: NOT STARTED")
        
        # 3. Exchanges
        applied = sum(1 for ex in self.asian_exchanges if self.data["exchanges"][ex["name"]]["applied"])
        if applied == len(self.asian_exchanges):
            completed += 1
            print(f"✅ Asia Exchanges: COMPLETE ({applied}/{len(self.asian_exchanges)})")
        else:
            print(f"⏳ Asia Exchanges: {applied}/{len(self.asian_exchanges)} applied")
        
        # 4. Audit
        if self.data["audit"]["planned"]:
            completed += 1
            print("✅ Security Audit: PLANNED")
        else:
            print("❌ Security Audit: NOT PLANNED")
        
        # 5. Time
        start = datetime.fromisoformat(self.data["start_date"])
        months = (datetime.now() - start).days // 30
        self.data["months"] = months
        if months >= 6:
            completed += 1
            print(f"✅ Time: COMPLETE ({months} months)")
        else:
            print(f"⏳ Time: {months}/6 months")
        
        print("\n" + "-" * 50)
        progress = (completed / total_tasks) * 100
        print(f"📊 Overall Progress: {progress:.1f}% ({completed}/{total_tasks} tasks)")
        
        if progress == 100:
            print("\n🎯 ETORO READY! Apply now!")
        else:
            print(f"\n⏳ Remaining tasks: {total_tasks - completed}")
        
        self.save_tracking()

    def run_full_automation(self):
        """Run all remaining automation steps"""
        print("\n🚀 RUNNING COMPLETE REMAINING AUTOMATION")
        print("=" * 50)
        print("")
        
        # 1. Check DexScreener
        self.check_dexscreener()
        
        # 2. Show volume instructions
        self.show_volume_instructions()
        
        # 3. Show audit info
        self.show_audit_info()
        
        # 4. Open exchange links
        self.open_exchange_links()
        
        # 5. Show progress
        self.show_progress()
        
        print("\n✅ COMPLETE AUTOMATION FINISHED!")
        print("📋 Save this report for your records")

def main():
    print("🎯 SPIRIT GUIDE - REMAINING TASKS AUTOMATION")
    print("============================================")
    
    auto = RemainingAutomation()
    
    print("\n📊 Choose an option:")
    print("  1. Check DexScreener status")
    print("  2. Show volume building instructions")
    print("  3. Open Asian exchange links")
    print("  4. Mark exchanges as applied")
    print("  5. Show audit information")
    print("  6. Show overall progress")
    print("  7. RUN FULL AUTOMATION (all steps)")
    print("")
    
    choice = input("Enter choice (1-7): ").strip()
    
    if choice == "1":
        auto.check_dexscreener()
    elif choice == "2":
        auto.show_volume_instructions()
    elif choice == "3":
        auto.open_exchange_links()
    elif choice == "4":
        auto.mark_applied()
    elif choice == "5":
        auto.show_audit_info()
    elif choice == "6":
        auto.show_progress()
    elif choice == "7":
        auto.run_full_automation()
    else:
        print("❌ Invalid choice")

if __name__ == "__main__":
    main()
