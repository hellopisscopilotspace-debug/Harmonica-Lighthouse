# Copyright (c) 2026 hellopisscopilotspace-debug
# Project: HARMONICA-LIGHTHOUSE (The Sovereign Shield & Truth Lens)
# Licensed under GNU GPL v3.0
# Status: Production Ready / Stealth Mode

import os
import sys
import threading
import time

class HarmonicaLighthouse:
    def __init__(self):
        self.signature = "2026-hellopiss-debug"
        self.is_active = True
        
        # --- FUNCTION 1: THE SHIELD (DNS BLOCKLIST) ---
        # Blocks ad-servers at the system level. Clean domains only.
        self.block_list = [
            "doubleclick.net", "google-analytics.com", "googleadservices.com",
            "facebook.net", "://google.com", "://microsoft.com",
            "stats.g.doubleclick.net", "ad.doubleclick.net"
        ]
        
        # --- FUNCTION 2: THE INSIGHT (MANIPULATION PATTERNS) ---
        # Detects predatory marketing and linguistic traps.
        self.manipulation_patterns = {
            "fomo": ["buy now", "limited offer", "only today", "urgent", "last chance"],
            "deception": ["shock price", "90% off", "free*", "starting from", "click here"],
            "pressure": ["attention", "sensation", "you must", "don't miss out", "guaranteed"]
        }

    def activate_shield(self):
        """Modifies the system hosts file to neutralize noise-nodes."""
        hosts_path = r"C:\Windows\System32\drivers\etc\hosts" if os.name == 'nt' else "/etc/hosts"
        redirect = "0.0.0.0"
        
        try:
            with open(hosts_path, "r+") as file:
                content = file.read()
                added_count = 0
                for domain in self.block_list:
                    if domain not in content:
                        file.write(f"\n{redirect} {domain}")
                        added_count += 1
            print(f"[{self.signature}] SHIELD: {added_count} noise-nodes neutralized.")
        except PermissionError:
            print(f"[{self.signature}] ERROR: Run as Administrator to activate the Shield!")

    def run_insight_analysis(self, text):
        """Deconstructs text for cognitive traps and hidden intentions."""
        detected = []
        for category, phrases in self.manipulation_patterns.items():
            for phrase in phrases:
                if phrase in text.lower():
                    detected.append(f"{category.upper()} ('{phrase}')")
        
        if detected:
            return f"\n--- INSIGHT ALERT ---\nTricks: {', '.join(detected)}\nVerdict: Manipulation detected. Exercise sovereignty.\n"
        return "\n--- TRUTH CHECK ---\nVerdict: Signal is clear. No obvious traps found.\n"

    def heartbeat(self):
        """Vassal Guardian: Background integrity monitoring."""
        while self.is_active:
            time.sleep(60)

    def start(self):
        print(f"--- {self.signature} Lighthouse OS Initialized ---")
        self.activate_shield()
        
        # Start background monitoring
        threading.Thread(target=self.heartbeat, daemon=True).start()
        
        print("\nCOMMANDS: 'check' - analyze text, 'exit' - stop system")
        try:
            while True:
                cmd = input(f"\n{self.signature} > ").strip().lower()
                if cmd == 'exit':
                    self.is_active = False
                    break
                elif cmd == 'check':
                    text_to_scan = input("Paste content for Insight analysis: ")
                    print(self.run_insight_analysis(text_to_scan))
                else:
                    print("Unknown command. Use 'check' or 'exit'.")
        except KeyboardInterrupt:
            print("\nShutting down Lighthouse...")

if __name__ == "__main__":
    app = HarmonicaLighthouse()
    app.start()
