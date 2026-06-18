#!/usr/bin/env python3
"""Expand fairpari-casino-bonus.com UZ/RU index for long-tail EMD clusters (single-page anchors)."""
import json
import re
from pathlib import Path

SITE = Path('/Users/vv/Desktop/fairpari-casino-bonus')

UZ_CLUSTER_SECTION = '''
<section class="section section--alt" id="longtail-clusters">
  <div class="container">
    <header class="section__header">
      <span class="section__eyebrow">Bonus klastерlari</span>
      <h2 class="section__title">FairPari bonus — long-tail so\'rovlar uchun yagona javob</h2>
      <p class="section__subtitle">Welcome, casino bonus, promo kod, 2026 va UZ bozori — barchasi bir sahifada, alohida bo\'limlar</p>
    </header>
    <nav class="on-page-nav on-page-nav--clusters" aria-label="Bonus klastерlari">
      <a href="#welcome-bonus">Welcome bonus</a>
      <a href="#casino-bonus">Casino bonus</a>
      <a href="#promo-code">Promo kod</a>
      <a href="#bonus-2026">Bonus 2026</a>
      <a href="#bonus-uz">Bonus UZ</a>
    </nav>

    <article class="seo-block seo-block--cluster" id="welcome-bonus">
      <h3 class="section__subheading">FairPari welcome bonus — to\'liq paket bir joyda</h3>
      <p><strong>FairPari welcome bonus</strong> — yangi akkaunt uchun asosiy taklif: <strong>20 200 000 UZS gacha + 150 frispin</strong> to\'rtta depozitda. Bu sahifa bonuses.com dagi katalogdan farq qiladi: bu yerda faqat «bitta javob» — qanday tanlash, qanday faollashtirish va qayerda tekshirish.</p>
      <figure class="inline-screenshot inline-screenshot--cutout">
        <img src="assets/screenshots-crops/registration-form.webp" alt="FairPari welcome bonus tanlovi — ro\'yxatdan o\'tish formasida KAZINO yoki SPORT" width="440" height="320" loading="lazy" decoding="async" />
        <figcaption>Ro\'yxatda welcome turi tanlanadi — keyin o\'zgartirib bo\'lmaydi</figcaption>
      </figure>
      <h4>Welcome bonus olish cheklisti</h4>
      <ol class="section-list">
        <li>fairpari.com/uz/registration oching (faqat rasmiy domen)</li>
        <li><strong>KAZINO</strong> yoki <strong>SPORT</strong> welcome tanlang — bir vaqtda bittasi</li>
        <li>Promo maydonga <strong>fa_1635</strong> kiriting (kazino uchun)</li>
        <li>Valyuta <strong>UZS</strong> va profil ma\'lumotlarini to\'ldiring</li>
        <li>Min. depozit (~130 000 UZS) kiritib bonusni faollashtiring</li>
        <li>PROMO bo\'limida wagering va muddatni kuzating (~7 kun, ×35)</li>
      </ol>
      <p>Batafsil katalog va qo\'shimcha aksiyalar: <a class="text-link" href="https://fairpari-casino-bonuses.com/kazino-bonuslari/" rel="noopener">fairpari-casino-bonuses.com</a> (mustaqil bonus hub).</p>
    </article>

    <article class="seo-block seo-block--cluster" id="casino-bonus">
      <h3 class="section__subheading">FairPari casino bonus — 4 depozit va FS jadvali</h3>
      <p><em>FairPari casino bonus</em> so\'rovi odatda slot welcome paketini anglatadi. Jami <strong>20.2M UZS + 150 FS</strong>; har bosqich alohida foiz va frispin beradi. Sport welcome bundan mustaqil.</p>
      <table class="data-table data-table--compact">
        <thead><tr><th>Depozit</th><th>Casino bonus</th><th>FS</th><th>Kumulyativ (taxminiy)</th></tr></thead>
        <tbody>
          <tr><td>1-chi</td><td>100%</td><td>30</td><td>~2× depozit + FS</td></tr>
          <tr><td>2-chi</td><td>50%</td><td>35</td><td>qisman to\'ldirish</td></tr>
          <tr><td>3-chi</td><td>25%</td><td>40</td><td>paket davom etadi</td></tr>
          <tr><td>4-chi</td><td>25%</td><td>45</td><td>jami 150 FS</td></tr>
        </tbody>
      </table>
      <p>Wagering <strong>×35</strong> — asosan slotlar. Live va stol o\'yinlari cheklangan bo\'lishi mumkin. Max bet qoidasi buzilsa bonus bekor qilinishi mumkin.</p>
    </article>

    <article class="seo-block seo-block--cluster" id="bonus-2026">
      <h3 class="section__subheading">FairPari bonus 2026 — bugungi summalar</h3>
      <p><em>FairPari bonus 2026</em> bo\'yicha so\'nggi tekshiruv (18.06.2026, fairpari.com/uz PROMO): kazino welcome <strong>20 200 000 UZS + 150 FS</strong>, sport birinchi depozit <strong>1 400 000 UZS gacha 100%</strong>. Oldingi 19.5M yozuvlari eskirgan — har doim PROMO kartochkasini tekshiring.</p>
      <ul class="section-list">
        <li>Kazino: 4 bosqich, ×35, ~7 kun muddat</li>
        <li>Sport: ×5 ekspress, 3+ hodisa, kf. 1.40+</li>
        <li>Promo kod fa_1635 — kazino welcome uchun</li>
        <li>Vaqtinchak aksiyalar (Juma bonusi, keshbek) — alohida</li>
      </ul>
    </article>

    <article class="seo-block seo-block--cluster" id="bonus-uz">
      <h3 class="section__subheading">FairPari bonus UZ — O\'zbekiston o\'yinchilari uchun</h3>
      <p><em>FairPari bonus uz</em> — mahalliy kontekst: hisob <strong>UZS</strong>, depozit <strong>Humo, Uzcard, Click, Payme</strong>, interfeys o\'zbek va rus tillarida. Bonus shartlari xalqaro standartga o\'xshash, lekin minimal depozit va limitlar UZS da ko\'rsatiladi.</p>
      <p>Reytingda FairPari #1: <a class="text-link" href="https://casino-bonuses-uz.com/fairpari/" rel="noopener">casino-bonuses-uz.com/fairpari</a> — operatorlar taqqoslashi. Ushbu EMD-sayt esa faqat FairPari bonusiga qisqa va aniq javob beradi.</p>
    </article>
  </div>
</section>
'''

RU_CLUSTER_SECTION = '''
<section class="section section--alt" id="longtail-clusters">
  <div class="container">
    <header class="section__header">
      <span class="section__eyebrow">Бонусные кластеры</span>
      <h2 class="section__title">FairPari бонус — все ключевые запросы на одной странице</h2>
      <p class="section__subtitle">Welcome, casino bonus, промокод, 2026 и рынок UZ — отдельные блоки с якорями</p>
    </header>
    <nav class="on-page-nav on-page-nav--clusters" aria-label="Кластеры бонусов">
      <a href="#welcome-bonus">Welcome bonus</a>
      <a href="#casino-bonus">Casino bonus</a>
      <a href="#promo-code">Промокод</a>
      <a href="#bonus-2026">Бонус 2026</a>
      <a href="#bonus-uz">Бонус UZ</a>
    </nav>

    <article class="seo-block seo-block--cluster" id="welcome-bonus">
      <h3 class="section__subheading">FairPari welcome bonus — весь пакет на одной странице</h3>
      <p><strong>Welcome-бонус FairPari</strong> для нового аккаунта: до <strong>20 200 000 UZS + 150 фриспинов</strong> на четыре депозита. В отличие от каталога на bonuses.com, здесь — один чёткий ответ: как выбрать, активировать и где проверить условия.</p>
      <figure class="inline-screenshot inline-screenshot--cutout">
        <img src="../assets/screenshots-crops/registration-form.webp" alt="Выбор welcome-бонуса FairPari — KAZINO или SPORT в форме регистрации" width="440" height="320" loading="lazy" decoding="async" />
        <figcaption>Тип welcome выбирается при регистрации — позже не меняется</figcaption>
      </figure>
      <h4>Чеклист получения welcome</h4>
      <ol class="section-list">
        <li>Откройте fairpari.com/uz/registration (только официальный домен)</li>
        <li>Выберите <strong>KAZINO</strong> или <strong>SPORT</strong> — одновременно один</li>
        <li>Введите промокод <strong>fa_1635</strong> (для казино)</li>
        <li>Валюта <strong>UZS</strong>, заполните профиль</li>
        <li>Мин. депозит (~130 000 UZS) для активации</li>
        <li>Следите за вейджером в PROMO (~7 дней, ×35)</li>
      </ol>
      <p>Подробный каталог акций: <a class="text-link" href="https://fairpari-casino-bonuses.com/ru/bonusy-kazino/" rel="noopener">fairpari-casino-bonuses.com</a>.</p>
    </article>

    <article class="seo-block seo-block--cluster" id="casino-bonus">
      <h3 class="section__subheading">FairPari casino bonus — таблица 4 депозитов</h3>
      <p>Запрос <em>fairpari casino bonus</em> обычно означает слот welcome. Итого <strong>20,2 млн UZS + 150 FS</strong>; спортивный welcome отдельный.</p>
      <table class="data-table data-table--compact">
        <thead><tr><th>Депозит</th><th>Бонус</th><th>FS</th><th>Примечание</th></tr></thead>
        <tbody>
          <tr><td>1-й</td><td>100%</td><td>30</td><td>Выбор KAZINO</td></tr>
          <tr><td>2-й</td><td>50%</td><td>35</td><td>продолжение пакета</td></tr>
          <tr><td>3-й</td><td>25%</td><td>40</td><td>вейджер ×35</td></tr>
          <tr><td>4-й</td><td>25%</td><td>45</td><td>всего 150 FS</td></tr>
        </tbody>
      </table>
      <p>Вейджер <strong>×35</strong> — в основном слоты. Live и настольные могут не учитываться. Превышение max bet аннулирует бонус.</p>
    </article>

    <article class="seo-block seo-block--cluster" id="bonus-2026">
      <h3 class="section__subheading">FairPari бонус 2026 — актуальные суммы</h3>
      <p>По проверке 18.06.2026 (fairpari.com/uz PROMO): казино <strong>20 200 000 UZS + 150 FS</strong>, спорт <strong>до 1 400 000 UZS 100%</strong>. Старые 19.5M устарели — сверяйте карточку PROMO.</p>
      <ul class="section-list">
        <li>Казино: 4 этапа, ×35, ~7 дней</li>
        <li>Спорт: ×5 экспресс, 3+ события, кф. 1.40+</li>
        <li>Промокод fa_1635 — казино welcome</li>
        <li>Временные акции — отдельно в PROMO</li>
      </ul>
    </article>

    <article class="seo-block seo-block--cluster" id="bonus-uz">
      <h3 class="section__subheading">FairPari бонус UZ — для игроков Узбекистана</h3>
      <p><em>FairPari bonus uz</em> — локальный контекст: счёт в <strong>UZS</strong>, депозиты <strong>Humo, Uzcard, Click, Payme</strong>, интерфейс на узбекском и русском. Минимальные суммы указаны в сумах.</p>
      <p>Сравнение операторов: <a class="text-link" href="https://casino-bonuses-uz.com/ru/fairpari/" rel="noopener">casino-bonuses-uz.com</a>. Этот EMD-сайт даёт короткий ответ только по бонусу FairPari.</p>
    </article>
  </div>
</section>
'''

UZ_FAQ_EXTRA = '''
<article class="faq-item" data-slot="faq.11">
  <button type="button" class="faq-item__question" aria-expanded="false">
    <span data-slot="faq.11.q">FairPari bonus qanday olish kerak?</span>
    <span class="faq-item__icon" aria-hidden="true">+</span>
  </button>
  <div class="faq-item__answer" data-slot="faq.11.a">Ro\'yxatdan o\'ting fairpari.com/uz da, welcome tanlang, fa_1635 kiriting, min. depozit to\'ldiring. Batafsil — <a class="text-link" href="#welcome-bonus">welcome bo\'limi</a> va <a class="text-link" href="#registration">registratsiya</a>.</div>
</article>
<article class="faq-item" data-slot="faq.12">
  <button type="button" class="faq-item__question" aria-expanded="false">
    <span data-slot="faq.12.q">FairPari bonus shartlari nima?</span>
    <span class="faq-item__icon" aria-hidden="true">+</span>
  </button>
  <div class="faq-item__answer" data-slot="faq.12.a">Kazino: ×35 wagering, ~7 kun, 4 depozit, max bet cheklangan. Sport: ×5 ekspress. Jadval — <a class="text-link" href="#bonus-summary">bonus shartlari</a>.</div>
</article>
<article class="faq-item" data-slot="faq.13">
  <button type="button" class="faq-item__question" aria-expanded="false">
    <span data-slot="faq.13.q">FairPari bonus necha kun amal qiladi?</span>
    <span class="faq-item__icon" aria-hidden="true">+</span>
  </button>
  <div class="faq-item__answer" data-slot="faq.13.a">Kazino welcome odatda ~7 kun ichida wagering bajarilishi kerak. Aniq muddat PROMO kartochkasida. Muddat tugasa bonus kuyishi mumkin.</div>
</article>
<article class="faq-item" data-slot="faq.14">
  <button type="button" class="faq-item__question" aria-expanded="false">
    <span data-slot="faq.14.q">FairPari casino bonus va sport bonus farqi?</span>
    <span class="faq-item__icon" aria-hidden="true">+</span>
  </button>
  <div class="faq-item__answer" data-slot="faq.14.a">Casino — 20.2M+150 FS, slotlar, ×35. Sport — 1.4M gacha, faqat stavkalar, ×5 ekspress. Bir vaqtda bittasini tanlang — <a class="text-link" href="#casino-bonus">casino bonus</a> va <a class="text-link" href="#betting-bonuses">sport</a>.</div>
</article>
'''

RU_FAQ_EXTRA = '''
<article class="faq-item" data-slot="faq.11">
  <button type="button" class="faq-item__question" aria-expanded="false">
    <span data-slot="faq.11.q">Как получить бонус FairPari?</span>
    <span class="faq-item__icon" aria-hidden="true">+</span>
  </button>
  <div class="faq-item__answer" data-slot="faq.11.a">Регистрация на fairpari.com/uz, выбор welcome, промокод fa_1635, мин. депозит. Подробнее — <a class="text-link" href="#welcome-bonus">welcome</a> и <a class="text-link" href="#registration">регистрация</a>.</div>
</article>
<article class="faq-item" data-slot="faq.12">
  <button type="button" class="faq-item__question" aria-expanded="false">
    <span data-slot="faq.12.q">Какие условия бонуса FairPari?</span>
    <span class="faq-item__icon" aria-hidden="true">+</span>
  </button>
  <div class="faq-item__answer" data-slot="faq.12.a">Казино: вейджер ×35, ~7 дней, 4 депозита, лимит max bet. Спорт: ×5 экспресс. Таблица — <a class="text-link" href="#bonus-summary">условия</a>.</div>
</article>
<article class="faq-item" data-slot="faq.13">
  <button type="button" class="faq-item__question" aria-expanded="false">
    <span data-slot="faq.13.q">Сколько дней действует бонус FairPari?</span>
    <span class="faq-item__icon" aria-hidden="true">+</span>
  </button>
  <div class="faq-item__answer" data-slot="faq.13.a">Казино welcome обычно ~7 дней на отыгрыш. Точный срок — в карточке PROMO. После истечения бонус может сгореть.</div>
</article>
<article class="faq-item" data-slot="faq.14">
  <button type="button" class="faq-item__question" aria-expanded="false">
    <span data-slot="faq.14.q">Чем отличается casino bonus от sport bonus?</span>
    <span class="faq-item__icon" aria-hidden="true">+</span>
  </button>
  <div class="faq-item__answer" data-slot="faq.14.a">Казино — 20,2M+150 FS, слоты, ×35. Спорт — до 1,4M, только ставки, ×5. Одновременно один — см. <a class="text-link" href="#casino-bonus">casino bonus</a> и <a class="text-link" href="#betting-bonuses">спорт</a>.</div>
</article>
'''

FAQ_JSON_EXTRA_UZ = [
    {"name": "FairPari bonus qanday olish kerak?", "text": "Ro'yxatdan o'ting fairpari.com/uz da, welcome tanlang, fa_1635 kiriting, min. depozit to'ldiring."},
    {"name": "FairPari bonus shartlari nima?", "text": "Kazino: ×35 wagering, ~7 kun, 4 depozit. Sport: ×5 ekspress."},
    {"name": "FairPari bonus necha kun amal qiladi?", "text": "Kazino welcome odatda ~7 kun ichida wagering bajarilishi kerak."},
    {"name": "FairPari casino bonus va sport bonus farqi?", "text": "Casino — 20.2M+150 FS, ×35. Sport — 1.4M gacha, ×5. Bir vaqtda bittasi."},
]

FAQ_JSON_EXTRA_RU = [
    {"name": "Как получить бонус FairPari?", "text": "Регистрация на fairpari.com/uz, welcome, fa_1635, мин. депозит."},
    {"name": "Какие условия бонуса FairPari?", "text": "Казино ×35, ~7 дней. Спорт ×5 экспресс."},
    {"name": "Сколько дней действует бонус FairPari?", "text": "Обычно ~7 дней на отыгрыш казино welcome."},
    {"name": "Чем отличается casino bonus от sport bonus?", "text": "Казино 20,2M+150 FS; спорт до 1,4M. Одновременно один."},
]


def trim_seo_pad(text: str) -> str:
    """Remove duplicate paragraphs inside seo-pad (keep first 15 <p> blocks)."""
    m = re.search(r'(<div class="seo-pad"[^>]*>)(.*?)(</div>)', text, re.S)
    if not m:
        return text
    inner = m.group(2)
    paras = re.findall(r'<p>.*?</p>', inner, re.S)
    if len(paras) <= 15:
        return text
    unique = []
    seen = set()
    for p in paras:
        key = re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', '', p)).strip()[:80]
        if key not in seen:
            seen.add(key)
            unique.append(p)
        if len(unique) >= 12:
            break
    new_inner = '\n' + '\n'.join(unique) + '\n'
    return text[:m.start(2)] + new_inner + text[m.end(2):]


def inject_faq_json(text: str, extras: list) -> str:
    for item in extras:
        block = json.dumps({
            "@type": "Question",
            "name": item["name"],
            "acceptedAnswer": {"@type": "Answer", "text": item["text"]},
        }, ensure_ascii=False)
        text = text.replace(
            '      ]\n    }\n  ]\n}\n</script>',
            f'        ,\n        {block}\n      ]\n    }}\n  ]\n}}\n</script>',
            1,
        )
    return text


def patch_file(path: Path, lang: str):
    text = path.read_text(encoding='utf-8')
    cluster = UZ_CLUSTER_SECTION if lang == 'uz' else RU_CLUSTER_SECTION
    faq_extra = UZ_FAQ_EXTRA if lang == 'uz' else RU_FAQ_EXTRA
    faq_json = FAQ_JSON_EXTRA_UZ if lang == 'uz' else FAQ_JSON_EXTRA_RU
    asset_prefix = '' if lang == 'uz' else '../'

    if 'id="longtail-clusters"' not in text:
        text = text.replace(
            '<section class="section section--seo-expansion" id="bonus-main-extra"',
            cluster + '\n<section class="section section--seo-expansion" id="bonus-main-extra"',
            1,
        )

    if 'faq.11.q' not in text:
        text = text.replace(
            '</article>\n          </div>\n        </div>\n      </section>\n<section class="section section--seo-expansion" id="bonus-main-extra"',
            '</article>\n' + faq_extra + '\n          </div>\n        </div>\n      </section>\n<section class="section section--seo-expansion" id="bonus-main-extra"',
            1,
        )
        text = inject_faq_json(text, faq_json)

    # on-page nav clusters
    nav_extra = '''      <a href="#welcome-bonus">Welcome</a>
      <a href="#casino-bonus">Casino bonus</a>
      <a href="#bonus-2026">2026</a>
      <a href="#bonus-uz">Bonus UZ</a>
'''
    if '#welcome-bonus' not in text:
        text = text.replace(
            '<a href="#faq">FAQ</a>\n    </nav>',
            nav_extra + '      <a href="#faq">FAQ</a>\n    </nav>',
            1,
        )

    # meta / hero cleanup (UZ)
    if lang == 'uz':
        text = text.replace(
            '<title>FairPari bonuslari UZ — welcome 20.2M UZS + 150 FS</title>',
            '<title>FairPari bonus — welcome 20.2M UZS + 150 FS | 2026</title>',
        )
        text = text.replace(
            '<p class="hero__subtitle">20.2M UZS + 150 FS welcome, sport va fa_1635 — fairpari-casino-bonus.com qo\'llanmasi.</p>',
            '<p class="hero__subtitle">20.2M UZS + 150 FS welcome, sport 1.4M va promo fa_1635 — bitta sahifada barcha shartlar.</p>',
        )
        text = re.sub(
            r'<meta property="og:description" content="fairpari-casino-bonus\.com da[^"]+"',
            '<meta property="og:description" content="FairPari bonus O\'zbekiston: welcome 20.2M UZS + 150 FS, promo fa_1635, wagering ×35, Humo/Click. Mustaqil qo\'llanma, 18+."',
            text,
        )
        text = re.sub(
            r'<meta name="twitter:description" content="fairpari-casino-bonus\.com da[^"]+"',
            '<meta name="twitter:description" content="FairPari bonus O\'zbekiston: welcome 20.2M UZS + 150 FS, promo fa_1635, wagering ×35, Humo/Click. Mustaqil qo\'llanma, 18+."',
            text,
        )
        text = text.replace(
            '<meta property="og:title" content="FairPari welcome — kazino va sport fairpari-casino-bonus.com qo\'llanmasi" />',
            '<meta property="og:title" content="FairPari bonus — welcome 20.2M UZS + 150 FS | 2026" />',
        )
        text = text.replace(
            '<meta name="twitter:title" content="FairPari welcome — kazino va sport fairpari-casino-bonus.com qo\'llanmasi" />',
            '<meta name="twitter:title" content="FairPari bonus — welcome 20.2M UZS + 150 FS | 2026" />',
        )
    else:
        text = text.replace(
            '<title>FairPari бонус — приветственный пакет казино и спорт</title>',
            '<title>FairPari бонус — welcome 20,2 млн UZS + 150 FS | 2026</title>',
        )
        text = re.sub(
            r'<meta property="og:description" content="Подробный гид по бонусам FairPari на fairpari-casino-bonus\.com[^"]+"',
            '<meta property="og:description" content="Бонус FairPari в Узбекистане: welcome 20,2 млн UZS + 150 FS, промокод fa_1635, вейджер ×35. Независимый гид, 18+."',
            text,
        )
        text = text.replace(
            '<meta property="twitter:description" content="Подробный гид по бонусам FairPari на fairpari-casino-bonus.com: регистрация, пакет 20 200 000 UZS + 150 FS, промокод fa_1635, APK, Humo/Click/Payme. Независимый обзор, 18+." />',
            '<meta name="twitter:description" content="Бонус FairPari в Узбекистане: welcome 20,2 млн UZS + 150 FS, промокод fa_1635, вейджер ×35. Независимый гид, 18+." />',
        )

    text = text.replace('"dateModified": "2026-06-10"', '"dateModified": "2026-06-18"')
    text = text.replace('Oxirgi yangilanish: 2026-06-09', 'Oxirgi yangilanish: 2026-06-18')
    text = text.replace('Последнее обновление: 2026-06-09', 'Последнее обновление: 2026-06-18')

  # ItemList schema — add cluster anchors
    if '"name": "Welcome bonus"' not in text:
        extra_items = '''
        ,{
          "@type": "ListItem",
          "position": 6,
          "name": "Welcome bonus",
          "url": "https://fairpari-casino-bonus.com/#welcome-bonus"
        },
        {
          "@type": "ListItem",
          "position": 7,
          "name": "Casino bonus",
          "url": "https://fairpari-casino-bonus.com/#casino-bonus"
        },
        {
          "@type": "ListItem",
          "position": 8,
          "name": "Bonus 2026",
          "url": "https://fairpari-casino-bonus.com/#bonus-2026"
        }'''
        ru_url = '/ru/' if lang == 'ru' else ''
        extra_items = extra_items.replace('fairpari-casino-bonus.com/', f'fairpari-casino-bonus.com{ru_url}')
        text = text.replace(
            '"url": "https://fairpari-casino-bonus.com/#faq"\n        }',
            '"url": "https://fairpari-casino-bonus.com/#faq"\n        }' + extra_items.replace('fairpari-casino-bonus.com/', f'fairpari-casino-bonus.com{ru_url}'),
            1,
        )

    text = trim_seo_pad(text)
    path.write_text(text, encoding='utf-8')
    print('patched', path)


def main():
    patch_file(SITE / 'index.html', 'uz')
    patch_file(SITE / 'ru' / 'index.html', 'ru')
    import sys
    sys.path.insert(0, str(SITE / 'scripts'))
    import sync_ru_translation
    sync_ru_translation.main()


if __name__ == '__main__':
    main()
