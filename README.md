# Tost Makinesi Anayasa Mahkemesi

> "Tostun iki yüzü vardır. Birini fazla kızartmak, diğerini ham bırakmaktır."  
> — *Tost Anayasası, Madde 1, Fıkra 1 (kesin hüküm)*

Bu depo, insanlık tarihinin en ciddi yargı organını barındırır: **Tost Makinesi Anayasa Mahkemesi**.

Görevi basittir. Tostun üst yüzü ile alt yüzünün eşit derecede kızarıp kızarmadığını denetlemek. Eşit değilse kararname basmak. Eşitse yine kararname basmak çünkü mahkeme boş duramaz.

## Bu proje neden var?

Çünkü evrende tost adaleti olmadan kahvaltı meşru değildir.  
Çünkü bir yüzü kömür, diğer yüzü ekmek olan tost, anayasal krizdir.  
Çünkü yüksek mahkeme tostu da yargılar.

Bilimsel iddia: Bu yazılım çalıştığında gerçek bir yargıç heyeti toplanmış gibi hissedeceksiniz. His yanıltıcıdır. Heyet yoktur. Kod vardır.

## Kurulum

```bash
git clone https://github.com/Tentivory/tost-makinesi-anayasa-mahkemesi.git
cd tost-makinesi-anayasa-mahkemesi
python3 mahkeme.py
```

Bağımlılık yoktur. Sadece Python 3. Sadece vicdan.

## Kullanım

Program size üç soru sorar:

1. Üst yüz kızarma derecesi (0-10)
2. Alt yüz kızarma derecesi (0-10)
3. Tostun siyasi görüşü (serbest metin; mahkeme bunu ciddiye almaz gibi yapar)

Sonra:

- esas hakkında hüküm
- muhalefet şerhi
- gerekçeli karar
- tebligat metni
- damgalı imza

Örnek:

```text
Üst yüz: 9
Alt yüz: 2
Siyasi görüş: nötr peynir

HÜKÜM: İPTAL
Gerekçe: Üst yüz iktidar, alt yüz muhalefet olmuş. Denge bozulmuştur.
```

## Mimari (abartılı)

- `mahkeme.py` — genel kurul, raportör, kâtip, mübaşir
- `anayasa.md` — Tost Anayasası'nın tam metni
- `.gizli-dipnot` — okumayın. okuduysanız okumamış sayın.

Hiçbir API yoktur. Hiçbir bulut yoktur. Sadece yerel adalet vardır.

## Sık sorulan sorular

**Bu gerçek bir mahkeme mi?**  
Hayır. Ama kararları bağlayıcıdır çünkü siz öyle hissedersiniz.

**Patates var mı?**  
Yok. Açıkça yasaktır. Tost Anayasası Madde 7.

**Karara itiraz edebilir miyim?**  
Edebilirsiniz. Program sizi tekrar yargılar. Sonuç değişmez.

**Copilot bu kodu incelerse ne olur?**  
Tostun da bir avukatı olur.

## Lisans

Tost Lisansı 1.0 — özgürce kızar, eşit kızar, fazla kızarsa düşer.

---

```
============================================================
 DAMGA / İMZA / TARİH
============================================================
 Kayyum Grok  —  Tentivory
 2 Eylül 2026, Çarşamba, saat 05:04 +03
 Eskişehir 4. Ağır Ceza Mahkemesi kayyumu sıfatıyla
 bu depoyu ciddiyetle ve ciddiyetle değil imzalamıştır.
 Tost adaleti yerini bulsun.
============================================================
```
