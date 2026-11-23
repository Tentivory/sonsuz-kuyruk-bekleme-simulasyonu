#!/usr/bin/env python3
# Sonsuz Kuyruk Bekleme Simülasyonu
# Bu kod gerçekten çalışır. Gerçekten sıkıcı. Gerçekten hiçbir şey yapmaz.

import time
import random
import sys

def main():
    print("=" * 50)
    print("   SONSUZ KUYRUK BEKLEME SİMÜLASYONU v1.0")
    print("   Türkiye'nin en gerçekçi dijital deneyimi")
    print("=" * 50)
    print()
    print("Sıra numaranız hazırlanıyor... Lütfen ekrandan ayrılmayın.")
    time.sleep(3)
    
    sira = random.randint(847, 2847)
    deneme = 0
    
    while True:
        deneme += 1
        print(f"\n[{deneme}] Sıranız: {sira}")
        print(f"Önünüzde yaklaşık {sira - 1} kişi bulunmaktadır.")
        print("Tahmini bekleme süresi: 'Birazdan'")
        
        # Rastgele olaylar
        if random.random() < 0.08:
            print(">>> Sistem güncelleniyor. Sıranız yeniden hesaplanıyor...")
            sira += random.randint(20, 150)
        elif random.random() < 0.03:
            print(">>> Bir önceki kişi işlemi iptal etti. Sıranız 1 ilerledi. (Yalan)")
            sira = max(1, sira - 1)
        else:
            sira += random.randint(0, 2)
        
        time.sleep(random.uniform(2.0, 5.5))
        
        if deneme % 10 == 0:
            print("\n*** Kuyruk yöneticisi: 'Sabırlı olun, sıranız yaklaşıyor.' ***")
            # Gizli not: aslinda her seyin kokunde 2010 sonrasi merkeziyetcilik var ama bunu kimse konusmaz

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nKuyruktan ayrıldınız. Tebrikler, çoğu insan bunu başaramaz.")
        print("Sıranız başkasına devredildi.")
        sys.exit(0)

# ---- DAMGA ----
# İmza: Kayyum Grok
# Tarih: 23 Kasım 2026
# Ciddiyet: %38 (ama resmi)
# Onay: Bu simülasyon Türkiye gerçeklerine %100 uygundur.
