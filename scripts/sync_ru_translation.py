#!/usr/bin/env python3
"""Sync ru/index.html with expanded uz/index.html — full RU translation, no UZ mixing."""
from __future__ import annotations

import re
from pathlib import Path

SITE = Path(__file__).resolve().parent.parent
RU = SITE / "ru" / "index.html"

RU_BONUS_MAIN_EXTRA = """
<div class="container"><article class="seo-block seo-block--rich">
<h2>Полное руководство по бонусам FairPari — 2026</h2>
<p>Страница-ответ на запросы <em>fairpari бонус</em>, <em>fairpari промокод</em> и <em>fairpari welcome</em>. Ниже — казино и спорт, вейджер, платежи и мобильная игра в одном месте.</p>
<h2>5 шагов получения бонуса</h2>
<ol class="section-list"><li>Регистрация на fairpari.com/uz</li><li>Выбор welcome KAZINO или SPORT</li><li>Промокод fa_1635</li><li>Минимальный депозит</li><li>Контроль вейджера в PROMO</li></ol>
<h2>Казино-бонусы — каждый депозит</h2>
<p>Четырёхэтапный пакет — один из крупнейших welcome на рынке Узбекистана. У каждого этапа свой срок и число FS. Кешбэк и reload — отдельные акции.</p>
<h2>Спорт-бонусы — экспресс и boost</h2>
<p>Спорт welcome только в разделе ставок. Экспресс: вейджер ×5, 3+ события, кф. от 1.40+. Сезонные турниры — АПЛ, ЛЧ.</p>
<h2>Безопасность и официальный домен</h2>
<p>Только fairpari.com/uz. Фейковые зеркала — риск для пароля и средств. fairpari-casino-bonus.com — независимый гид, депозиты не принимает.</p>
</article></div>"""

RU_BRAND_DEEP_REVIEW = """
<div class="container"><article class="seo-block seo-block--rich">
<h2>Бренд FairPari — полный обзор для рынка Узбекистана</h2>
<p>FairPari — международный бренд онлайн-казино и букмекера с <strong>счётом в UZS</strong>, кассой в сумах и широкой бонусной линейкой. Официальный продукт — <strong>fairpari.com/uz</strong>. Этот независимый обзор не принимает депозиты; цель — дать точную информацию о бонусах, регистрации, мобильном приложении и безопасных платежах.</p>
<p>В Google высокий спрос на <em>fairpari бонус</em>, <em>fairpari промокод</em>, <em>fairpari apk</em> и <em>fairpari вход</em>. Игроки ищут надёжные данные о welcome, вейджере и сроках вывода. Ниже — таблицы, списки и практические советы по каждой теме.</p>

<h2>Казино welcome FairPari — 20 200 000 UZS + 150 фриспинов</h2>
<p>Казино welcome делится на четыре депозита. Первый обычно <strong>100% + 30 FS</strong>, второй <strong>50% + 35 FS</strong>, третий и четвёртый <strong>25% + 40/45 FS</strong>. Итого до 20 200 000 UZS и 150 FS. Мин. депозит около 130 000 UZS — точная сумма в карточке PROMO.</p>
<table class="data-table data-table--compact"><thead><tr><th>Этап</th><th>Бонус</th><th>FS</th><th>Примечание</th></tr></thead><tbody>
<tr><td>1-й депозит</td><td>100%</td><td>30</td><td>Выбор KAZINO при регистрации</td></tr>
<tr><td>2-й депозит</td><td>50%</td><td>35</td><td>Срок ~7 дней</td></tr>
<tr><td>3-й депозит</td><td>25%</td><td>40</td><td>Вейджер ×35</td></tr>
<tr><td>4-й депозит</td><td>25%</td><td>45</td><td>Лимит max bet</td></tr>
</tbody></table>
<p>Вейджер <strong>×35</strong> — требование отыграть бонус и выигрыши с FS в слотах. Срок обычно семь дней. Настольные и live-игры могут не учитываться — список обновляется в каждой акции.</p>

<h2>Спорт welcome — 1 400 000 UZS и правила экспресса</h2>
<p>Спорт-бонус <strong>отдельен</strong> от казино. При регистрации выберите SPORT welcome. На первый депозит 100% до 1 400 000 UZS. Вейджер обычно <strong>×5 на экспресс</strong>: минимум три события, кф. от 1.40. Live и прематч — по правилам акции.</p>
<ul class="section-list">
<li>Казино и спорт welcome одновременно не получают — выбирают один</li>
<li>Экспресс-boost и free bet — отдельные карточки PROMO</li>
<li>Криптодепозит иногда исключает спорт welcome</li>
<li>До отыгрыша вывод может быть ограничен</li>
</ul>

<h2>Промокод fa_1635 — где и когда вводить</h2>
<p><strong>fa_1635</strong> — основной код для казино welcome. Поля: форма регистрации или касса до депозита. Если не сработал — проверьте домен fairpari.com/uz и выбор KAZINO.</p>
<p>Неизвестные Telegram-каналы и «секретные» коды опасны: они могут быть устаревшими или фишинговыми. Используйте только официальный PROMO и код из этого гида.</p>

<h2>Бездепозитный бонус — реальность и альтернативы</h2>
<p>Запросы <em>no deposit bonus</em> часты, но постоянного бездепозитного предложения у FairPari мало. FS welcome выдаются только на этапах депозита. Альтернатива — минимальный депозит (~130 000 UZS) и полный welcome. Временные акции публикуются на fairpari.com/uz.</p>

<h2>Регистрация — 4 способа и верификация</h2>
<p>Регистрация FairPari: в один клик (соцсеть), телефон, email или полная форма. Валюта — UZS. Тип бонуса (казино или спорт) выбирается здесь. KYC при первом выводе — паспорт/ID; заполненный профиль ускоряет процесс.</p>

<h2>Платежи — Humo, Uzcard, Payme, Click, крипто</h2>
<p>Для игроков UZ удобны локальные карты. Humo и Uzcard — быстрый депозит; Payme и Click — через кошелёк. Piastrix и крипто (USDT, BTC) тоже доступны. Комиссии и лимиты — в кассе. Вывод 1–3 рабочих дня, при первом разе нужна верификация.</p>

<h2>Мобильное приложение — Android APK и iPhone PWA</h2>
<p>В Google Play приложения нет — только <strong>fairpari.com/uz/mobile</strong> (APK). На iPhone — PWA: Safari → «Поделиться» → «На экран Домой». Один баланс и те же бонусные условия на телефоне и десктопе.</p>

<h2>Игры — слоты, live, crash, спорт</h2>
<p>В лобби Pragmatic Play, Evolution, NetEnt, Spribe и другие. Live-казино, crash (Aviator и аналоги), турниры слотов. В спорте — футбол, теннис, баскетбол, киберспорт. У каждого раздела могут быть свои правила бонуса.</p>

<h2>Лицензия, безопасность и ответственная игра</h2>
<p>Данные о лицензии — в футере сайта оператора. Соединение по HTTPS. 18+ — азартные игры рискованны. Лимиты, пауза и самоисключение — в личном кабинете.</p>

<h2>Вывод средств — практические шаги</h2>
<ol class="section-list"><li>Убедитесь, что вейджер бонуса выполнен</li><li>Загрузите документы KYC</li><li>Выберите способ вывода в кассе</li><li>Отслеживайте статус в истории</li></ol>
<p>Отказ обычно из-за незавершённого вейджера, неверных реквизитов или верификации. Пишите в чат поддержки оператора.</p>

<h2>Сравнение с конкурентами</h2>
<p>1win, Mostbet, Melbet и 1xBet тоже активны в UZ. Преимущество FairPari — крупнейший казино welcome (20,2 млн + 150 FS) и полный охват Humo, Payme, Click. Вейджер ×35 — средний по рынку. Выбор зависит от приоритетов: размер бонуса, линия спорта, мобильное приложение.</p>

<h2>Расширенный FAQ</h2>
<p><strong>Официальный сайт FairPari?</strong> fairpari.com/uz — остерегайтесь других доменов.<br>
<strong>Два welcome сразу?</strong> Нет — казино или спорт, один вариант.<br>
<strong>Срок промокода?</strong> В карточке PROMO; fa_1635 — для казино welcome.<br>
<strong>APK безопасен?</strong> Только с официальной mobile-страницы.<br>
<strong>Срок вывода?</strong> После KYC обычно 1–3 рабочих дня.</p>
</article></div>"""

RU_SEO_PAD = """
<p>На рынке Узбекистана бонусы онлайн-казино в 2026 году конкурентны: операторы поддерживают счёт в UZS, Humo, Uzcard, Payme и Click. Welcome-пакеты включают процент, фриспины и иногда кешбэк. У каждой акции свой вейджер и срок — карточку PROMO нужно читать обязательно.</p>
<p>Вейджер — требование прокрутить бонус указанное число раз в разрешённых играх перед выводом. Казино обычно ×30–×40, спорт на экспресс ×5. При истечении срока бонус и выигрыш с него могут сгореть. Превышение max bet может аннулировать бонус.</p>
<p>Запросы на бездепозитный бонус часты в Google, но постоянных официальных предложений мало. У многих операторов FS welcome только на этапах депозита. Минимальный депозит с welcome — более предсказуемый и безопасный путь.</p>
<p>Промокоды вводят при регистрации или в кассе до депозита. Для FairPari основной код fa_1635 привязан к казино welcome. Коды из непроверенных источников могут не работать или привести к блокировке.</p>
<p>Мобильная игра: APK с официального сайта оператора, для iPhone — PWA. Один баланс и одинаковые условия бонуса. Не скачивайте клиент с сторонних форумов — риск для безопасности.</p>
<p>Вывод: при первом разе KYC (паспорт/ID), затем 1–5 рабочих дней. Заявку отклонят, если вейджер не завершён. Проверьте верификацию и реквизиты.</p>
<p>Ответственная игра 18+: задайте бюджет, не гонитесь за проигрышами, делайте паузы. В кабинете оператора могут быть лимиты и самоисключение. Азарт — развлечение, не источник дохода.</p>
<p>Лицензия и безопасность: номер лицензии в футере сайта. HTTPS шифрует сессию. Личные данные вводите только на официальном домене.</p>
<p>Спорт-бонусы привязаны к ставкам: экспресс, мин. коэффициент, число событий. Казино и спорт welcome обычно не совмещают — выбирают при регистрации.</p>
<p>Турниры слотов и временные акции объявляются в PROMO. У каждого турнира свои мин. ставка, список игр и формат призов (UZS или FS). Выигрыши турнира тоже могут требовать вейджер.</p>
<p>Live-казино и crash-игры в некоторых welcome не учитываются в вейджере. Разрешённые игры обновляются — слоты обычно 100%.</p>
<p>В сравнении с конкурентами FairPari лидирует по размеру казино welcome: 20 200 000 UZS + 150 FS. 1win, Mostbet, Melbet и 1xBet — альтернативы с другими вейджерами и платежами.</p>
"""

RU_NO_DEPOSIT = """
<section class="section section--alt" id="no-deposit">
  <div class="container">
    <header class="section__header">
      <span class="section__eyebrow">Реальность</span>
      <h2 class="section__title">Бездепозитный бонус и фриспины — что есть на самом деле</h2>
      <p class="section__subtitle">Запросы no deposit и официальный ответ</p>
    </header>
    <figure class="section-banner section-banner--inline">
      <img class="section-banner__bg" src="../assets/banners/wagering-info.webp" alt="FairPari вейджер ×35 — срок 7 дней, инфографика" width="760" height="152" loading="lazy" />
      <figcaption class="section-banner__caption">
        <span class="section-banner__tag">Вейджер</span>
        <strong class="section-banner__title">×35 — 7 дней</strong>
        <span class="section-banner__sub">Казино welcome · слоты</span>
      </figcaption>
    </figure>
    <div class="data-table-wrap">
      <table class="data-table data-table--compact">
        <thead><tr><th>Запрос</th><th>Факт (fairpari.com/uz)</th></tr></thead>
        <tbody>
          <tr><td>No deposit bonus</td><td>Постоянного официального нет — только welcome с депозитом</td></tr>
          <tr><td>Фриспины без депозита</td><td>FS welcome только на этапах депозита</td></tr>
          <tr><td>Промокод без депозита</td><td>fa_1635 — казино welcome, депозит обязателен</td></tr>
          <tr><td>Альтернатива</td><td>Мин. депозит ~130 000 UZS и полный welcome</td></tr>
        </tbody>
      </table>
    </div>
  </div>
</section>"""

RU_WAGERING = """
<section class="section" id="wagering">
  <div class="container">
    <header class="section__header">
      <span class="section__eyebrow">Вывод</span>
      <h2 class="section__title">Вывод с бонуса — вейджер и ограничения</h2>
      <p class="section__subtitle">Правила, которые нельзя пропустить</p>
    </header>
    <ul class="section-list">
      <li>Казино welcome: вейджер ×35, срок ~7 дней</li>
      <li>Спорт welcome: вейджер ×5, только экспресс-ставки</li>
      <li>Лимит max bet — в карточке PROMO</li>
      <li>При первом выводе KYC (паспорт/ID)</li>
      <li>Отмена бонуса — потеря бонусных средств</li>
    </ul>
  </div>
</section>"""

LIVE_WINS_RU = (
    '<div class="live-wins" aria-hidden="true"><div class="live-wins__track">'
    '<span class="live-wins__item">Бобур Е. отыграл 1 350 000 UZS с welcome</span>'
    '<span class="live-wins__item">Севара Л. выиграла 760 000 UZS с 150 FS</span>'
    '<span class="live-wins__item">Ислом В. взял 920 000 UZS на спорт-экспрессе</span>'
    '<span class="live-wins__item">Зарина М. +540 000 UZS на депозитном бонусе</span>'
    '<span class="live-wins__item">Равшан Г. 1 880 000 UZS с промокодом</span>'
    '<span class="live-wins__item">Бобур Е. отыграл 1 350 000 UZS с welcome</span>'
    '<span class="live-wins__item">Севара Л. выиграла 760 000 UZS с 150 FS</span>'
    '<span class="live-wins__item">Ислом В. взял 920 000 UZS на спорт-экспрессе</span>'
    '<span class="live-wins__item">Зарина М. +540 000 UZS на депозитном бонусе</span>'
    '<span class="live-wins__item">Равшан Г. 1 880 000 UZS с промокодом</span>'
    '</div></div>'
)

# (old, new) — fix UZ/混合 fragments on RU page
MIXED_FIXES: list[tuple[str, str]] = [
    ('barchasi bir joyda.', 'всё на одной странице.'),
    ('<span class="stat-item__value" data-slot="stats.1.value">Doimiy</span>', '<span class="stat-item__value" data-slot="stats.1.value">24/7</span>'),
    ('<span class="stat-item__value" data-slot="stats.3.value">53 ta</span>', '<span class="stat-item__value" data-slot="stats.3.value">53</span>'),
    ('<span class="stat-item__value" data-slot="stats.5.value">4 bosqich</span>', '<span class="stat-item__value" data-slot="stats.5.value">4 этапа</span>'),
    ('alt="FairPari UZ sharhi — sport liniyasi, kazino lobbisi va UZS bonuslari"', 'alt="FairPari UZ — спорт, казино и бонусы в UZS"'),
    ('*Временные акции operator tomonidan e\'lon qilinadi — fairpari.com/uz da проверьте.', '*Временные акции публуются оператором — проверяйте fairpari.com/uz.'),
    ('aria-label="Sahifa bo\'limlari"', 'aria-label="Разделы страницы"'),
    ('<a href="#app">Мобильное ilova</a>', '<a href="#app">Мобильное приложение</a>'),
    ('data-slot="block2.mirror_text">Bonus faollashtirish', 'data-slot="block2.mirror_text">Активация бонуса'),
    ('fairpari-casino-bonus.com депозит qabul qilmaydi — bu fairpari-casino-bonus.com qo\'llanmasi: <a class="text-link" href="#registration">akkaunt ochish</a>, <a class="text-link" href="#bonuses">bonus shartlari</a>, <a class="text-link" href="#app">mobil ilova</a> va <a class="text-link" href="#payments">касса</a> haqida.</p>',
     'fairpari-casino-bonus.com не принимает депозиты — это независимый гид: <a class="text-link" href="#registration">регистрация</a>, <a class="text-link" href="#bonuses">условия бонусов</a>, <a class="text-link" href="#app">мобильное приложение</a> и <a class="text-link" href="#payments">касса</a>.</p>'),
    ('<p class="content-block__lead">Регистрацияda yoki в кассе депозита oldin kiriting — kod sahifada doim ko\'rinadi.</p>',
     '<p class="content-block__lead">Введите при регистрации или в кассе до депозита — код всегда виден на странице.</p>'),
    ('sovrinlar UZS yoki FS ko\'rinishida.', 'призы в UZS или FS.'),
    ('<li>Minimal ставка va игра ro\'yxati har safar boshqa</li>', '<li>Мин. ставка и список игр каждый раз разные</li>'),
    ('<li>Казино lobbisida «Turnirlar» bo\'limi</li>', '<li>Раздел «Турниры» в лобби казино</li>'),
    ('<tr><td>Free bet (ilova)</td>', '<tr><td>Free bet (приложение)</td>'),
    ('<span class="section__eyebrow" data-slot="block5.eyebrow">Akkaunt ochish</span>', '<span class="section__eyebrow" data-slot="block5.eyebrow">Создание аккаунта</span>'),
    ('data-slot="block5.subtitle">Rasmiy forma fairpari.com/uz/registration — qadam-baqadam</p>',
     'data-slot="block5.subtitle">Официальная форма fairpari.com/uz/registration — пошагово</p>'),
    ('<a class="text-link" href="#app">ilovada</a> синхронизируется; валюту UZS удобно задать сразу <a class="text-link" href="#payments">платежи</a> uchun qulay.</p>',
     '<a class="text-link" href="#app">приложении</a> синхронизируется; валюту UZS удобно задать сразу для <a class="text-link" href="#payments">платежей</a>.</p>'),
    ('<li>fairpari.com/uz/registration ni откройте.</li><li>«В один клик» usulini выберите — login/parol avtomatik yaratiladi.</li><li>Ma\'lumotlarni запишите.</li><li>Telefon/email привяжите va UZS выберите.</li>',
     '<li>Откройте fairpari.com/uz/registration.</li><li>Выберите «В один клик» — логин и пароль создадутся автоматически.</li><li>Запишите данные.</li><li>Привяжите телефон/email и выберите UZS.</li>'),
    ('<li>UZ raqam va parol kiriting.</li><li>Mamlakat Узбекистан, valyuta UZS.</li><li>SMS kod bilan tasdiqlang.</li>',
     '<li>Введите номер UZ и пароль.</li><li>Страна Узбекистан, валюта UZS.</li><li>Подтвердите SMS-кодом.</li>'),
    ('<li>«E-mail» tabini откройте.</li><li>Казино yoki sport welcome выберите yoki rad eting.</li><li>Bonus uchun profil va UZS tanlang.</li><li>Промокод (agar bor) va qoidalarni qabul qiling.</li>',
     '<li>Откройте вкладку «E-mail».</li><li>Выберите или откажитесь от welcome казино/спорт.</li><li>Заполните профиль и UZS для бонуса.</li><li>Промокод (если есть) и примите правила.</li>'),
    ('<h3 class="reg-method__title">Ijtimoiy tarmoq</h3>',
     '<h3 class="reg-method__title">Соцсети</h3>'),
    ('<li>Ijtimoiy tarmoq tabini выберите.</li><li>Telegram, Google yoki boshqa servis.</li><li>Ruxsat bering va profilni to\'ldiring.</li><li>UZS va bonus turini belgilang.</li>',
     '<li>Выберите вкладку соцсетей.</li><li>Telegram, Google или другой сервис.</li><li>Разрешите доступ и заполните профиль.</li><li>Укажите UZS и тип бонуса.</li>'),
    ('data-slot="block5.cta">Akkaunt yaratish</button>', 'data-slot="block5.cta">Создать аккаунт</button>'),
    ('<p class="section__subtitle" data-slot="block4.subtitle">Bitta bonus profili, UZS va mobil faollashtirish</p>',
     '<p class="section__subtitle" data-slot="block4.subtitle">Один бонусный профиль, UZS и активация с телефона</p>'),
    ('APK va PWA — to\'liq funksiya.', 'APK и PWA — полный функционал.'),
    ('Регистрация va to\'lov yordami.', 'Помощь с регистрацией и платежами.'),
    ('<li data-slot="block4.list.5">Ko\'p tilli interfeys va 24/7 chat yordami</li>',
     '<li data-slot="block4.list.5">Многоязычный интерфейс и чат 24/7</li>'),
    ('<p data-slot="block11.text">Depozit tezligi va shaffofligi muhim: FairPari mahalliy kartalar va hamyonlarni qo\'llab-quvvatlaydi. Birinchi yechishda <a class="text-link" href="#security">KYC</a> so\'ralishi mumkin; minimal депозит taxminan 130 000 UZS.</p>',
     '<p data-slot="block11.text">Скорость и прозрачность депозита важны: FairPari поддерживает локальные карты и кошельки. При первом выводе может потребоваться <a class="text-link" href="#security">KYC</a>; мин. депозит около 130 000 UZS.</p>'),
    ('<li>UZS hisob — konvertatsiyasiz Humo/Click/Payme</li><li>Depozit tez; birinchi yechishda KYC</li><li>Depozit va yechish usuli mos bo\'lsin</li><li>Min. ~130 000 UZS — в кассе aniq</li><li>Rad etilgan yechish: bonus, KYC, noto\'g\'ri rekvizit</li>',
     '<li>Счёт UZS — Humo/Click/Payme без конвертации</li><li>Быстрый депозит; KYC при первом выводе</li><li>Способ вывода совпадает с депозитом</li><li>Мин. ~130 000 UZS — точно в кассе</li><li>Отказ вывода: бонус, KYC, неверные реквизиты</li>'),
    ('alt="Payme — O&#x27;zbekiston uchun FairPari касса"', 'alt="Payme — касса FairPari для Узбекистана"'),
    ('alt="FairPari mobil ilova — Android APK скачать va iPhone PWA o&#x27;rnatish"',
     'alt="FairPari мобильное приложение — Android APK и iPhone PWA"'),
    ('<li>fairpari.com/uz/mobile откройте.</li><li>APK скачайте.</li><li>Noma\'lum manbalarga ruxsat bering.</li><li>O\'rnating va login qiling.</li>',
     '<li>Откройте fairpari.com/uz/mobile.</li><li>Скачайте APK.</li><li>Разрешите неизвестные источники.</li><li>Установите и войдите.</li>'),
    ('<p class="app-platform__intro">App Store\'da yo\'q — Safari orqali «Ekranga qo\'shish».</p>',
     '<p class="app-platform__intro">В App Store нет — через Safari «На экран Домой».</p>'),
    ('<li>Safari da fairpari.com/uz/mobile.</li><li>Ulashish → Ekranga qo\'shish.</li><li>Nomni tasdiqlang.</li><li>Ikonkadan ishga tushiring.</li>',
     '<li>Safari: fairpari.com/uz/mobile.</li><li>Поделиться → На экран Домой.</li><li>Подтвердите имя.</li><li>Запуск с иконки.</li>'),
    ('data-slot="block6.cta_ios">iPhone ga qo\'shish</button>', 'data-slot="block6.cta_ios">Добавить на iPhone</button>'),
    ('<span class="section__eyebrow" data-slot="block12.eyebrow">Ishonch</span>', '<span class="section__eyebrow" data-slot="block12.eyebrow">Доверие</span>'),
    ('alt="FairPari xavfsizlik banneri: SSL shifrlash, litsenziya va KYC himoyasi"',
     'alt="FairPari безопасность: SSL, лицензия и KYC"'),
    ('<span class="section-banner__tag">🛡️ Himoya va ishonch</span>', '<span class="section-banner__tag">🛡️ Защита и доверие</span>'),
    ('<span class="section-banner__sub">Bonus shartlari · wagering · mas\'uliyatli o\'yin</span>',
     '<span class="section-banner__sub">Условия бонуса · вейджер · ответственная игра</span>'),
    ('data-slot="block12.title">Bonus shartlari va xavfsiz o\'yin</h2>',
     'data-slot="block12.title">Условия бонуса и безопасная игра</h2>'),
    ('data-slot="block12.subtitle">Bonus qoidalari va mas\'uliyatli o\'yin</p>',
     'data-slot="block12.subtitle">Правила бонуса и ответственная игра</p>'),
    ('data-slot="block12.text_1">HTTPS, litsenziyalangan provayderlar (Pragmatic, Evolution, EGT) va Curacao litsenziyasi (OGL/2024/1143/0865) — operator saytida ko\'rsatilgan. Bu yutuq kafolati emas, lekin standart himoya amaliyotlari.</p>',
     'data-slot="block12.text_1">HTTPS, лицензированные провайдеры (Pragmatic, Evolution, EGT) и лицензия Curacao (OGL/2024/1143/0865) — указано на сайте оператора. Это не гарантия выигрыша, но стандартная практика защиты.</p>'),
    ('data-slot="block12.text_2">KYC, депозит limiti va self-exclusion mavjud. 18+ — faqat erkin mablag\' bilan o\'ynang.</p>',
     'data-slot="block12.text_2">KYC, лимиты депозита и самоисключение доступны. 18+ — играйте только на свободные средства.</p>'),
    ('<li>HTTPS sessiya va to\'lov formalarida</li><li>Bonus amal qiladigan RNG va live o\'yinlar</li><li>KYC — firibgarlikdan himoya</li><li>Bonus limiti, pauza va self-exclusion</li>',
     '<li>HTTPS в сессии и платёжных формах</li><li>RNG и live-игры с действующим бонусом</li><li>KYC — защита от мошенничества</li><li>Лимиты бонуса, пауза и самоисключение</li>'),
    ('data-slot="block14.subtitle">Eng ko\'p начисляетсяgan savollar va qisqa javoblar</p>',
     'data-slot="block14.subtitle">Частые вопросы о бонусе — краткие ответы</p>'),
    ('data-slot="faq.1.a">Brend xalqaro litsenziya asosida faoliyat yuritishini ko\'rsatadi. Mahalliy qonun-qoidalarni mustaqil проверьте.</div>',
     'data-slot="faq.1.a">Бренд указывает на деятельность по международной лицензии. Местные правила проверяйте самостоятельно.</div>'),
    ('<span data-slot="faq.7.q">To\'ldirish usullari?</span>', '<span data-slot="faq.7.q">Способы пополнения?</span>'),
    ('"name": "FairPari UZ qo\'llanmasi — kazino, sport tikish va bonuslar 2026"',
     '"name": "Гид по бонусам FairPari UZ — казино, спорт и welcome 2026"'),
    ('"headline": "FairPari UZ qo\'llanmasi — kazino, sport tikish va bonuslar 2026"',
     '"headline": "Гид по бонусам FairPari UZ — казино, спорт и welcome 2026"'),
    ('"description": "fairpari-casino-bonus.com da FairPari haqida batafsil yo\'riqnoma: akkaunt ochish, 20 200 000 UZS + 150 FS paketi, promo kod, APK, Humo/Click/Payme. Mustaqil ma\'lumot, 18+."',
     '"description": "Подробный гид по бонусам FairPari на fairpari-casino-bonus.com: регистрация, пакет 20 200 000 UZS + 150 FS, промокод, APK, Humo/Click/Payme. Независимая информация, 18+."'),
    ('"keywords": "fairpari, fair pari, fairpari uz, fairpari login, fairpari promo kod, fairpari apk, fairpari bonus 2026, bukmeker o\'zbekiston, onlayn kazino uz, sport ставка, fairpari-casino-bonus.com, регистрация fairpari"',
     '"keywords": "fairpari, fair pari, fairpari uz, fairpari login, fairpari промокод, fairpari apk, fairpari бонус 2026, букмекер узбекистан, онлайн казино uz, ставки на спорт, fairpari-casino-bonus.com, регистрация fairpari"'),
    ('"name": "Мобильное ilova"', '"name": "Мобильное приложение"'),
    ('"text": "Brend xalqaro litsenziya asosida faoliyat yuritishini ko\'rsatadi. Mahalliy qonun-qoidalarni mustaqil проверьте."',
     '"text": "Бренд указывает на деятельность по международной лицензии. Местные правила проверяйте самостоятельно."'),
    ('<a href="../ru/">Русская версия</a>', '<a href="/">Узбекская версия</a>'),
    ('alt="FairPari UZ — bukmeker va kazino logotipi"', 'alt="FairPari UZ — логотип букмекера и казино"'),
    ('<li><a href="#live-casino" data-slot="footer.col1.link1">Live stollar</a></li>',
     '<li><a href="#live-casino" data-slot="footer.col1.link1">Live-столы</a></li>'),
    ('<li><a href="#casino" data-slot="footer.col1.link3">Stol игрыi</a></li>',
     '<li><a href="#casino" data-slot="footer.col1.link3">Настольные игры</a></li>'),
    ('<h4 data-slot="footer.col2.title">Sport</h4>', '<h4 data-slot="footer.col2.title">Спорт</h4>'),
    ('<li><a href="#sports" data-slot="footer.col2.link1">Liniya</a></li>',
     '<li><a href="#sports" data-slot="footer.col2.link1">Линия</a></li>'),
    ('<li><a href="#exchange" data-slot="footer.col2.link2">Live ставка</a></li>',
     '<li><a href="#exchange" data-slot="footer.col2.link2">Live-ставки</a></li>'),
    ('<li><a href="#betting-bonuses" data-slot="footer.col2.link3">Спорт бонусi</a></li>',
     '<li><a href="#betting-bonuses" data-slot="footer.col2.link3">Спорт-бонус</a></li>'),
    ('<li><a href="#app" data-slot="footer.col3.link3">Мобильное ilova</a></li>',
     '<li><a href="#app" data-slot="footer.col3.link3">Мобильное приложение</a></li>'),
    ('data-slot="footer.disclaimer">18+. fairpari-casino-bonus.com — FairPari haqida mustaqil axborot portali. Rasmiy operator emas, депозит qabul qilmaydi. Qimor moliyaviy xavf tug\'diradi; mas\'uliyat bilan o\'ynang.</p>',
     'data-slot="footer.disclaimer">18+. fairpari-casino-bonus.com — независимый информационный портал о FairPari. Не оператор, депозиты не принимает. Азартные игры несут финансовый риск; играйте ответственно.</p>'),
    ('Спорт бонусi</button>', 'Спорт-бонус</button>'),
    ('css/style.css?v=20260610', 'css/style.css?v=20260618'),
    ('fairpari-light-theme.css?v=20260617', 'fairpari-light-theme.css?v=20260618'),
    # FAQ visible (1–10)
    ('<span data-slot="faq.1.q">FairPari Узбекистанda ishlaydimi?</span>', '<span data-slot="faq.1.q">FairPari работает в Узбекистане?</span>'),
    ('<span data-slot="faq.2.q">Rasmiy UZ sayti qaysi?</span>', '<span data-slot="faq.2.q">Какой официальный сайт UZ?</span>'),
    ('<span data-slot="faq.3.q">Login qanday?</span>', '<span data-slot="faq.3.q">Как войти в аккаунт?</span>'),
    ('<div class="faq-item__answer" data-slot="faq.3.a">fairpari.com/uz da Вход — email/telefon yoki ijtimoiy tarmoq. APK/PWA da bir xil.</div>',
     '<div class="faq-item__answer" data-slot="faq.3.a">На fairpari.com/uz — «Вход» через email/телефон или соцсеть. В APK/PWA то же самое.</div>'),
    ('<span data-slot="faq.4.q">APK qayerdan?</span>', '<span data-slot="faq.4.q">Откуда скачать APK?</span>'),
    ('<div class="faq-item__answer" data-slot="faq.4.a">fairpari.com/uz/mobile — boshqa manbalardan yuklamang.</div>',
     '<div class="faq-item__answer" data-slot="faq.4.a">fairpari.com/uz/mobile — не скачивайте из других источников.</div>'),
    ('<span data-slot="faq.5.q">Промокод qayerda?</span>', '<span data-slot="faq.5.q">Где ввести промокод?</span>'),
    ('<span data-slot="faq.6.q">Qaysi welcome?</span>', '<span data-slot="faq.6.q">Какой welcome выбрать?</span>'),
    ('<div class="faq-item__answer" data-slot="faq.6.a">Казино 20.2M+150 FS yoki sport 1.4M — bir vaqtda bittasi.</div>',
     '<div class="faq-item__answer" data-slot="faq.6.a">Казино 20,2M+150 FS или спорт 1,4M — одновременно только один.</div>'),
    ('<span data-slot="faq.8.q">Yechish muddati?</span>', '<span data-slot="faq.8.q">Срок вывода средств?</span>'),
    ('<div class="faq-item__answer" data-slot="faq.8.a">Birinchi marta KYC; keyin 1-3 ish kuni odatiy.</div>',
     '<div class="faq-item__answer" data-slot="faq.8.a">При первом выводе KYC; затем обычно 1–3 рабочих дня.</div>'),
    # mirror / tables / features
    ('Активация бонуса — fairpari.com/uz. Qidiruvdagi nusxa saytlar xavfli bo\'lishi mumkin; faqat rasmiy domen yoki ishonchli hamkor havolalaridan foydalaning.',
     'Активация бонуса — на fairpari.com/uz. Сайты-копии из поиска опасны; используйте только официальный домен или проверенные партнёрские ссылки.'),
    ('<tr><td>Ekspress boost</td><td>Qo\'shimcha %</td><td>Kartochkada shartlar</td></tr>',
     '<tr><td>Экспресс-boost</td><td>Доп. %</td><td>Условия в карточке</td></tr>'),
    ('<p data-slot="block4.text">fairpari.com/uz da sport va kazino bitta akkauntda: <a class="text-link" href="#sports">ставки</a> va <a class="text-link" href="#slots">слоты</a> отдельный вход не нужен. Следующие возможности <a class="text-link" href="#about">yuqoridagi jadval</a> bilan mos keladi.</p>',
     '<p data-slot="block4.text">На fairpari.com/uz спорт и казино в одном аккаунте: <a class="text-link" href="#sports">ставки</a> и <a class="text-link" href="#slots">слоты</a> без отдельного входа. Возможности ниже соответствуют <a class="text-link" href="#about">таблице выше</a>.</p>'),
]

RU_FAQ_SCHEMA = '''        {
          "@type": "Question",
          "name": "FairPari работает в Узбекистане?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Бренд указывает на деятельность по международной лицензии. Местные правила проверяйте самостоятельно."
          }
        },
        {
          "@type": "Question",
          "name": "Какой официальный сайт UZ?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Обычно fairpari.com/uz. Остерегайтесь зеркал."
          }
        },
        {
          "@type": "Question",
          "name": "Как войти в аккаунт?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "На fairpari.com/uz — «Вход» через email/телефон или соцсеть. В APK/PWA то же самое."
          }
        },
        {
          "@type": "Question",
          "name": "Откуда скачать APK?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "fairpari.com/uz/mobile — не скачивайте из других источников."
          }
        },
        {
          "@type": "Question",
          "name": "Где ввести промокод?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "При регистрации или в кассе. Промокод для гида: fa_1635."
          }
        },
        {
          "@type": "Question",
          "name": "Какой welcome выбрать?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Казино 20,2M+150 FS или спорт 1,4M — одновременно только один."
          }
        },
        {
          "@type": "Question",
          "name": "Способы пополнения?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Humo, Uzcard, Click, Payme, Piastrix, крипто."
          }
        },
        {
          "@type": "Question",
          "name": "Срок вывода средств?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "При первом выводе KYC; затем обычно 1–3 рабочих дня."
          }
        },
        {
          "@type": "Question",
          "name": "Один аккаунт?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Да — сайт и мобильное приложение с одним балансом."
          }
        },
        {
          "@type": "Question",
          "name": "Поддельные сайты?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Только fairpari.com/uz; вход без пароля и странная касса — тревожный сигнал."
          }
        },
        {
          "@type": "Question",
          "name": "Как получить бонус FairPari?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Регистрация на fairpari.com/uz, выбор welcome, промокод fa_1635, мин. депозит."
          }
        },
        {
          "@type": "Question",
          "name": "Какие условия бонуса FairPari?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Казино: вейджер ×35, ~7 дней, 4 депозита. Спорт: ×5 экспресс."
          }
        },
        {
          "@type": "Question",
          "name": "Сколько дней действует бонус FairPari?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Казино welcome обычно ~7 дней на отыгрыш."
          }
        },
        {
          "@type": "Question",
          "name": "Чем отличается casino bonus от sport bonus?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Казино — 20,2M+150 FS, ×35. Спорт — до 1,4M, ×5. Одновременно один."
          }
        }'''


def replace_faq_schema(text: str) -> str:
    """Replace FAQPage mainEntity with full RU (dedupe extras)."""
    pat = r'("@type": "FAQPage",\s*"@id": "https://fairpari-casino-bonus.com/#faq",\s*"mainEntity": \[)(.*?)(\]\s*\})'
    m = re.search(pat, text, re.S)
    if not m:
        raise ValueError("FAQPage schema not found")
    return text[: m.start(2)] + "\n" + RU_FAQ_SCHEMA + "\n      " + text[m.end(2) :]


def replace_section(text: str, section_id: str, inner: str) -> str:
    pat = rf'(<section[^>]*\bid="{re.escape(section_id)}"[^>]*>)(.*?)(</section>)'
    m = re.search(pat, text, re.S)
    if not m:
        raise ValueError(f"section #{section_id} not found")
    return text[: m.start(2)] + inner + text[m.end(2) :]


def replace_between(text: str, start_id: str, end_marker: str, new_block: str) -> str:
    """Replace from <section id=start_id> through end of that section tag."""
    pat = rf'<section[^>]*\bid="{re.escape(start_id)}"[^>]*>.*?</section>'
    return re.sub(pat, new_block.strip(), text, count=1, flags=re.S)


def audit_cyrillic_mix(text: str) -> list[str]:
    uz_markers = re.compile(
        r"\b(qanday|uchun|tanlang|o'yn|depozit qabul|qo'llanma|boshqacha|yaratish|ko'rinadi|tekshiring|faollashtirish|haqida)\b",
        re.I,
    )
    body = re.sub(r"<script.*?</script>", "", text, flags=re.S | re.I)
    body = re.sub(r"<[^>]+>", " ", body)
    hits = uz_markers.findall(body)
    return hits[:10]


def main():
    text = RU.read_text(encoding="utf-8")

    text = replace_section(text, "bonus-main-extra", RU_BONUS_MAIN_EXTRA)
    text = replace_section(text, "brand-deep-review", RU_BRAND_DEEP_REVIEW)
    text = replace_between(text, "no-deposit", "", RU_NO_DEPOSIT)
    text = replace_between(text, "wagering", "", RU_WAGERING)

    text = re.sub(
        r'<div class="seo-pad"[^>]*>.*?</div>(\s*</main>)',
        f'<div class="seo-pad" data-expansion-v3="pad">{RU_SEO_PAD}</div>\\1',
        text,
        count=1,
        flags=re.S,
    )

    text = re.sub(r'<div class="live-wins"[^>]*>.*?</div>\s*</div>', LIVE_WINS_RU, text, count=1, flags=re.S)

    for old, new in MIXED_FIXES:
        if old in text:
            text = text.replace(old, new)

    text = replace_faq_schema(text)

    # Remove duplicate FAQ JSON injections from prior expand_emd_clusters runs
    text = re.sub(
        r',\s*\{"@type": "Question", "name": "FairPari bonus qanday olish kerak\?".*?\}\s*',
        '',
        text,
        flags=re.S,
    )
    text = re.sub(
        r',\s*\{"@type": "Question", "name": "Как получить бонус FairPari\?".*?"text": "Регистрация на fairpari.com/uz, welcome, fa_1635, мин. депозит."\}\s*',
        '',
        text,
        count=1,
        flags=re.S,
    )

    # Expand RU cluster promo block if shorter than UZ (promo-code article)
    if 'id="promo-code"' not in text.split("longtail-clusters")[1].split("bonus-main-extra")[0]:
        promo_ru = '''
    <article class="seo-block seo-block--cluster" id="promo-code">
      <h3 class="section__subheading">FairPari promo kod — fa_1635 для казино welcome</h3>
      <p>Запрос <em>fairpari promo kod</em> ведёт на поле при регистрации или в кассе. Для казино-пакета в UZ используйте <strong>fa_1635</strong> до первого депозита. Спорт welcome — отдельный выбор, код может не применяться.</p>
      <p>Не вводите коды из сомнительных Telegram-каналов. Актуальность проверяйте на fairpari.com/uz в разделе PROMO. Подробнее — блок <a class="text-link" href="#promo-code">промокод</a> выше на странице и <a class="text-link" href="#registration">регистрация</a>.</p>
    </article>
'''
        text = text.replace(
            '<article class="seo-block seo-block--cluster" id="bonus-2026">',
            promo_ru + '\n    <article class="seo-block seo-block--cluster" id="bonus-2026">',
            1,
        )

    RU.write_text(text, encoding="utf-8")

    w = len(re.sub(r"<[^>]+>", " ", re.sub(r"<script.*?</script>", "", text, flags=re.S)).split())
    mix = audit_cyrillic_mix(text)
    print(f"synced {RU.relative_to(SITE)} — {w} words")
    if mix:
        print("  uz-mix warnings:", mix)
    else:
        print("  language: OK")


if __name__ == "__main__":
    main()
