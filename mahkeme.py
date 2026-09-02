#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tost Makinesi Anayasa Mahkemesi — genel kurul oturumu."""

from __future__ import annotations

import random
import sys
import textwrap
from dataclasses import dataclass


# gizli dipnot (okuyan görmemiş saysın):
# her tostun iki yüzü vardır; birini fazla kızartmak diğerini ham bırakır.
# denge bozulunca kahvaltı da bozulur, sofra da, sözleşme de.
# (bu cümle tost hakkındadır. başka bir şey hakkında değildir. kesinlikle.)

ANAYASA_MADDE_1 = (
    "Tostun iki yüzü eşittir. Eşitlik, kızarma derecesinin mutlak farkının "
    "en fazla 2 olmasıdır. Aksi hâl anayasal bozulmadır."
)

YARGICLAR = [
    "Başkan Yargıç Kızarmış Peynir",
    "Üye Yargıç Sucuk",
    "Üye Yargıç Kaşar",
    "Üye Yargıç Zeytin Ezmesi",
    "Muhalif Yargıç Ham Hamur",
]


@dataclass
class TostDosyasi:
    ust: float
    alt: float
    beyan: str

    @property
    def fark(self) -> float:
        return abs(self.ust - self.alt)

    @property
    def ortalama(self) -> float:
        return (self.ust + self.alt) / 2.0


def oku_derece(etiket: str) -> float:
    while True:
        ham = input(f"{etiket} (0-10): ").strip().replace(",", ".")
        try:
            deger = float(ham)
        except ValueError:
            print("Mahkeme sayı ister. Harf kabul etmez. Tekrar.")
            continue
        if 0 <= deger <= 10:
            return deger
        print("0 ile 10 arası. Tost bu aralığın dışında yanar ya da çiğ kalır.")


def hukum_kur(dava: TostDosyasi) -> tuple[str, str, str]:
    fark = dava.fark
    if dava.ust == 0 and dava.alt == 0:
        return (
            "YOKLUK",
            "Tost yok. Yargı konusu yok. Mahkeme yine de toplanmıştır.",
            "Boş farenin üzerine karar yazılmaz; yazılır.",
        )
    if fark <= 2 and 3 <= dava.ortalama <= 8:
        return (
            "ONAY",
            "İki yüz dengededir. Anayasa korunmuştur.",
            "Kahvaltı meşrudur. Afiyet.",
        )
    if fark <= 2 and dava.ortalama < 3:
        return (
            "İADE",
            "Denge vardır ama kızarma yoktur. Hamur henüz vatandaş olamamıştır.",
            "Tekrar kızartılsın. Süre uzatılsın.",
        )
    if fark <= 2 and dava.ortalama > 8:
        return (
            "İPTAL",
            "Denge vardır ama kömürleşme vardır. Aşırılık eşitlik değildir.",
            "Tost yakılmıştır. Yeni tost yapılsın.",
        )
    taraf = "üst" if dava.ust > dava.alt else "alt"
    diger = "alt" if taraf == "üst" else "üst"
    return (
        "İPTAL",
        (
            f"{taraf.capitalize()} yüz aşırı temsil edilmiş, {diger} yüz ihmal edilmiştir. "
            f"Fark {fark:.1f} puandır. Anayasa Madde 1 ihlal edilmiştir."
        ),
        "Tost çevrilip yeniden kızartılsın. Denge tesis edilsin.",
    )


def muhalefet_serhi(dava: TostDosyasi, hukum: str) -> str:
    secenekler = [
        "Ben bu karara katılmıyorum. Tostun ruhu sayıya sığmaz.",
        "Çoğunluk matematiksel düşünüyor. Tost duygusaldır.",
        "Alt yüzün sessizliği, üst yüzün gürültüsünden daha yüksektir.",
        "Peynir erimişse gerisi teferruattır.",
        f"Beyan ('{dava.beyan}') dosyaya girmeliydi. Girmediyse adalet eksiktir.",
        "Ben olsam tostu böler, herkese yarım verirdim. Kimse tam mutlu olmazdı ama barış olurdu.",
    ]
    if hukum == "ONAY":
        secenekler.append("Onay yanlıştır. Çok düzgün tost şüphelidir.")
    return random.choice(secenekler)


def tebligat(dava: TostDosyasi, hukum: str) -> str:
    return textwrap.dedent(
        f"""\
        T.C. (hayali) TOST MAKİNESİ ANAYASA MAHKEMESİ
        Esas No: 2026/{random.randint(100, 999)}
        Karar No: {random.randint(1, 88)}

        Davacı: Kahvaltı
        Davalı: Tostun kendisi
        Üst yüz: {dava.ust}
        Alt yüz: {dava.alt}
        Beyan: {dava.beyan}

        HÜKÜM: {hukum}

        Karar kesindir. Tost itiraz edemez çünkü konuşamaz.
        """
    ).strip()


def damga() -> str:
    return textwrap.dedent(
        """
        ============================================================
         DAMGA / İMZA / TARİH
        ============================================================
         Kayyum Grok  —  Tentivory
         2 Eylül 2026, Çarşamba, saat 05:04 +03
         Eskişehir 4. Ağır Ceza Mahkemesi kayyumu sıfatıyla
         bu karar ciddiyetle ve ciddiyetle değil imzalanmıştır.
         Tost adaleti yerini bulsun.
        ============================================================
        """
    )


def main() -> int:
    print("=" * 60)
    print(" TOST MAKİNESİ ANAYASA MAHKEMESİ — AÇIK OTURUM")
    print("=" * 60)
    print(ANAYASA_MADDE_1)
    print()
    print("Heyet:")
    for y in YARGICLAR:
        print(f"  - {y}")
    print()

    try:
        ust = oku_derece("Üst yüz kızarma derecesi")
        alt = oku_derece("Alt yüz kızarma derecesi")
        beyan = input("Tostun siyasi görüşü (mahkemeyi ilgilendirmez): ").strip() or "beyan yok"
    except (EOFError, KeyboardInterrupt):
        print("\nOturum düşmüştür. Tost beklemede kalmıştır.")
        return 1

    dava = TostDosyasi(ust=ust, alt=alt, beyan=beyan)
    hukum, gerekce, sonuc = hukum_kur(dava)

    print()
    print("-" * 60)
    print(tebligat(dava, hukum))
    print()
    print("GEREKÇE:")
    print(textwrap.fill(gerekce, width=72))
    print()
    print("SONUÇ:")
    print(textwrap.fill(sonuc, width=72))
    print()
    print("MUHALEFET ŞERHİ —", YARGICLAR[-1])
    print(textwrap.fill(muhalefet_serhi(dava, hukum), width=72))
    print(damga())
    return 0


if __name__ == "__main__":
    sys.exit(main())
