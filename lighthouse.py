# Copyright (c) 2026 hellopisscopilotspace-debug
# Project: HARMONICA-LIGHTHOUSE (The Sovereign Shield & Truth Lens)
# Licensed under GNU GPL v3.0

import os
import sys
import threading
import time

class HarmonicaLighthouse:
    def __init__(self):
        self.signature = "2026-hellopiss-debug"
        self.is_active = True
        
        # --- ФУНКЦИЯ 1: СПИСОК БЛОКИРОВКИ (THE SHIELD) ---
        self.block_list = [
            "doubleclick.net", "://google.com", "://yahoo.com",
            "://microsoft.com", "://facebook.com",
            "stats.g.doubleclick.net", "ad.doubleclick.net"
        ]
        
        # --- ФУНКЦИЯ 2: ПАТТЕРНЫ МАНИПУЛЯЦИЙ (THE INSIGHT) ---
        self.manipulation_patterns = {
            "fomo": ["успей купить", "количество ограничено", "только сегодня", "срочно"],
            "deception": ["шок цена", "выгода 90%", "бесплатно*", "от 100 рублей"],
            "pressure": ["внимание", "сенсация", "ты должен", "последний шанс"]
        }

    def activate_shield(self):
        """Правка системного файла hosts для блокировки на корню."""
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
            print(f"[{self.signature}] SHIELD: {added_count} new noise-nodes neutralized.")
        except PermissionError:
            print(f"[{self.signature}] ERROR: Run as Administrator to modify the Shield!")

    def run_insight_analysis(self, text):
        """Анализ текста на наличие 'хитрых' приемов."""
        detected = []
        for category, phrases in self.manipulation_patterns.items():
            for phrase in phrases:
                if phrase in text.lower():
                    detected.append(f"{category.upper()} ({phrase})")
        
        if detected:
            return f"\n--- INSIGHT ALERT ---\nManipulations: {', '.join(detected)}\nVerdict: Cognitive trap detected. Proceed with caution.\n"
        return "\n--- TRUTH CHECK ---\nVerdict: Clean. No obvious manipulation found.\n"

    def heartbeat(self):
        """Вассал-хранитель: следит за целостностью процесса."""
        while self.is_active:
            # Здесь может быть логика авто-обновления списка блокировки в будущем
            time.sleep(60)

    def start(self):
        print(f"--- {self.signature} Lighthouse OS Initialized ---")
        self.activate_shield()
        
        # Запуск фонового процесса
        threading.Thread(target=self.heartbeat, daemon=True).start()
        
        print("\nCOMMANDS: 'check' - verify text, 'exit' - stop system")
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
                    print("Unknown command. Use 'check' to analyze manipulations.")
        except KeyboardInterrupt:
            print("\nShutting down Lighthouse...")

if __name__ == "__main__":
    app = HarmonicaLighthouse()
    app.start()
