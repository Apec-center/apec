# Контент-завод и система управления контент-маркетингом: практики Рунета

Исследование для APEC Center. Дата: 2026-10-06.

> **Ограничение методики.** Исследование делалось из облачной среды, где egress-прокси закрыл почти все нужные домены: habr.com, vc.ru, texterra.ru, cossa.ru, spark.ru, sostav.ru, unisender.com, t.me, teletype.in, dzen.ru, rutube.ru, sozai.app (транскрипты Анарбаевой), anarbaeva.pro, а также зеркала (web.archive.org, r.jina.ai, braintools.ru, netlify.app). Полный текст статей прочитать не удалось. Ниже собраны выдержки из поисковой выдачи: аннотации и фрагменты конкретных статей. Каждое утверждение привязано к URL статьи, из которой взята выдержка. Прежде чем опираться на цифры в решениях, откройте первоисточник: с обычного компьютера все ссылки доступны.

---

## Краткий вывод: что взять в систему APEC

1. **Контент-завод — это конвейер «стратегия → идеи → бриф → производство → редактура → публикация → аналитика» с ролями и статусами, а не просто генератор.** На входе стратегия, на выходе контент по графику и разбор результатов ([Weeek](https://weeek.net/ru/blog/content-factory)). Без человека в контуре не работает ни одна известная система ([Хабр 1039432](https://habr.com/ru/articles/1039432/)).
2. **Одна основная модель на старте.** Варианты: «переупаковка живой съёмки», «ИИ-генерация из смыслов», «свои инфлюенсеры/аватары». Если делать всё сразу, проект гарантированно провалится ([Sostav, 30 дней](https://www.sostav.ru/blogs/283819/76160)). Для APEC основной будет модель A (Дима и Алекс в кадре), а B (Veo/Nano Banana) пойдёт на B-roll и производные форматы.
3. **Редакционная матрица не равна контент-плану.** Матрица служит генератором тем: сегмент × уровень осознанности × угол подачи × формат. План — это расписание ([Unisender](https://www.unisender.com/ru/glossary/matricza-kontenta/)). У Анарбаевой ключевое измерение матрицы — «угол», то есть с какой стороны смотрим на тему ([sozai/Анарбаева](https://sozai.app/transcript/content-zavod-building-system-guide/)).
4. **Ось осознанности — лестница Ханта:** безразличие → осознание проблемы → решения → продукта → готовность купить ([Kokoc](https://kokoc.com/blog/lestnica-bena-hanta/), [svoe.media](https://svoe.media/media/tpost/b8zz9p30d1-kontent-po-lestnitse-hanta-kak-vesti-kli)). Для APEC: «не знаю, что есть 90 дней без визаранов» → «визараны надоели» → «какие есть варианты (DTV, ED, APEC)» → «почему APEC Center» → «как оформить».
5. **Рубрикатор плюс баланс рубрик (экспертиза / доверие / продажи) по дням недели,** реалистичная частота, шаблон плана с полем «статус» ([anarbaeva.pro/content-system](https://anarbaeva.pro/content-system)).
6. **Редпроцесс в шесть этапов по образцу Т—Ж:** заявка → «мясо» (факты) → черновик → чистовик → оформление → публикация и первый посев ([Ильяхов](http://maximilyahov.ru/blog/all/tinkoff-bootcamp-8/)). Для видео нужно добавить «хук/тезисы» и «сценарий», причём всех, кто принимает решения, собирать на этапе сценария ([mc.today](https://mc.today/blogs/5-etapov-kontent-marketinga-ot-planirovaniya-k-analitike-i-kto-voobshhe-etim-vse-zanimaetsya/amp/)).
7. **Редполитика и одностраничный гайд по ToV** (зачем пишем, для кого, 3–4 принципа голоса, «вы» или «ты») обязательны до масштабирования, особенно когда пишут ИИ и амбассадоры ([advertisingforum](https://advertisingforum.ru/blog/tone-of-voice/), [Kokoc редполитика](https://kokoc.com/blog/redpolitika/)).
8. **ИИ берёт около 70% рутины** (сбор данных, структура, черновик), **эксперт закрывает около 30%** (фактчек, редактура) ([Хабр 955108](https://habr.com/ru/articles/955108/)). Для русского текста в 2026 году лидируют Claude Sonnet 4.6 и Opus 4.7. Фактчек на 5/5 не обеспечивает ни один сервис ([Хабр 1028530](https://habr.com/ru/articles/1028530/)).
9. **Мультиагентность только с жёстким оркестратором и узкими ролями.** «Рой агентов» без структуры превращается в «бесконечное совещание» ([Хабр 1026856](https://habr.com/ru/articles/1026856/)). Хорошо работает конвейер «один воркер — одна задача» с отдельным HITL-воркером ([Хабр 1023446](https://habr.com/ru/articles/1023446/)).
10. **Техника без стратегии не продаёт.** Пример: «построил контент-завод на n8n, он работает, но не зарабатывает» ([Хабр 966144](https://habr.com/ru/articles/966144/)).
11. **Таск-трекер с канбаном, родительскими и дочерними карточками и базой знаний ТТ** заменяет ручной диспетчинг. Медиапродакшен с 400 задачами в месяц сэкономил «4 продюсера» ([Kaiten](https://kaiten.ru/blog/case-media-production/), [Хабр Kaiten](https://habr.com/ru/companies/kaiten/articles/1057092/)). В нашем случае это CRM и n8n с карточкой «тема» и дочерними карточками «единица под канал».
12. **Медиатека строится на тегах, а не на папках.** Нужны единый нейминг `ГГГГММДД_тема`, мастер-аккаунт и смарт-коллекции ([Picvario](https://picvario.ru/kak-organizovat-komandnuyu-rabotu/), [Mediaquad](https://mediaquad.ru/blog/dam/chto-takoe-dam-sistema-podrobnoe-rukovodstvo/)).
13. **Атрибуция в каждой единице контента:** UTM с `utm_content` = ID единицы, уникальный промокод на канал или амбассадора, кодовое слово в директ → бот ([Callibri/Reels](https://callibri.ru/blog/chto-takoe-instagram-reels), [OneSpot UTM TG](https://onespot.one/all-posts/utm-metki-dlya-telegram)). Без сквозной аналитики продажа уйдёт в «прямой заход» ([Roistat](https://roistat.com/rublog/skvoznaya-marketingovaya-analitika/)).
14. **Амбассадоры: лучше 10 горящих, чем 100 за выгоду.** Нужно письменное согласие на использование UGC и реферальная ссылка или промокод ([Kokoc](https://kokoc.com/blog/ambassador-brenda-chto-eto/), [Callibri](https://callibri.ru/blog/ambassador-brenda-kak-najti-i-rabotat)).
15. **Ритм пересмотра:** стратегия раз в 1–3 года, план раз в квартал, тактика еженедельно ([Яндекс Директ](https://direct.yandex.ru/base/articles/marketingovaya-strategiya)). Редакционный портфель тем пополняется непрерывно ([Texterra](https://texterra.ru/blog/realizatsiya-kontent-marketingovoy-strategii.html)).

---

## 1. Контент-завод: определение, архитектура, масштаб

**Определение.** Это организованная система массового выпуска материалов по принципу производства: процессы, разделение труда, шаблоны и автоматизация. Объём измеряется десятками и сотнями единиц в месяц ([Click.ru](https://blog.click.ru/glossary/kontent-zavod/), [Unisender](https://www.unisender.com/ru/glossary/kontent-marketing/chto-takoe-kontent-zavod/)). В трактовке Анарбаевой это повторяемый цикл со стратегией, аналитикой, трендвотчингом, производством, публикацией, ретроспективой и воронкой продаж ([sozai](https://sozai.app/transcript/content-zavod-building-system-guide/)).

**Архитектура (Weeek).** На входе стратегия и идеи. В процессе этапы «брифование → создание → редактура → оформление», закреплённые за участниками. На выходе публикация по графику и анализ. Рекомендованный инструмент — канбан-доски, календарь, база знаний и чек-листы ([Weeek](https://weeek.net/ru/blog/content-factory)). Типовой видеоцикл: сценарий → съёмка → монтаж → публикация → аналитика. Производственные шаги: ресёрч/факты → создание → редактура и корректура → обработка (монтаж, звук, цвет) ([vc.ru/marketing](https://vc.ru/marketing/2716970-kontent-zavod-kak-instrument-brendov-dlya-privlecheniya-klientov), [kerubini](https://kerubini.ru/blog/detail/kontent-zavod/)).

**Ключевая роль — продюсер (контент-стратег).** Он пишет ТЗ, ставит задачи и отвечает за регулярность, объём, качество и соответствие целям бренда ([1seller](https://1seller.ru/prodyuser-kontent-zavoda), [vc.ru/gdekurs](https://vc.ru/gdekurs/2666565-kontent-zavod-sozdanie-zapusk-avtomatizatsiya)).

**Три модели (Sostav, «за 30 дней»):** A — переупаковка живой съёмки в десятки единиц; B — ИИ-генерация из смыслов; C — собственные инфлюенсеры или аватары. Основную модель выбирают одну ([Sostav](https://www.sostav.ru/blogs/283819/76160)).

**Когда завод оправдан** (из выдачи по материалам Анарбаевой и Martin Media): бюджет на контент от $5k в месяц, присутствие в трёх и более каналах, стратегия на горизонте от 12 месяцев ([mmedia.by](https://mmedia.by/blog/kak-postroit-content-zavod/)).

**Масштаб и цифры из кейсов:**
- Т—Ж выпускает около 150 статей в неделю, у него больше 15 млн читателей в месяц ([t-j.ru/about](https://t-j.ru/about/)).
- Медиапродакшен ТВ-канала обрабатывает около 400 видеозадач в месяц в Kaiten ([Хабр](https://habr.com/ru/companies/kaiten/articles/1057092/)).
- «Блогеры на зарплате»: один человек снимает 70–90 роликов в месяц, бюджет около 50 тыс. ₽ ([Яндекс Маркет, «Что на счёт»](https://partner.market.yandex.ru/chtojournal/content-zavod-dlya-brenda/)).
- Mixit: микроблогеры (до 10K) на окладе с KPI на просмотры, 2 ролика в день на 4–5 площадок, итог 57 млн просмотров при CPV 0,11 ₽ ([vc.ru](https://vc.ru/marketing/2731925-keis-kontent-zavoda-57-mln-prosmotrov-i-cpv-11-kopeek)).
- KoBolt (агентство А-РЕКС): больше 90 роликов в месяц, 3–12 млн просмотров, CPV 0,068 ₽. Старт с аудита ниши, болей, ToV и визуального стиля ([workspace](https://workspace.ru/cases/kak-kobolt-poluchil-3-12-mln-prosmotrov-i-cpv-0-068-s-pomoschyu-kontent-zavoda/)).
- ТД «Грейс»: бюджет 150 тыс. ₽, 2 месяца, 47 продаж. Клиент снимает на смартфон, команда монтирует и брендирует, ИИ делает вариации ([Рейтинг Рунета](https://ratingruneta.ru/cases/case-16139/)).
- Полюшко (UGC): больше 23 млн просмотров в месяц, +8 млн ₽ продаж ([marketing-tech](https://marketing-tech.ru/cases/polushko/rost_prodazh_dlya_brenda_uhodovoy_kosmetiki_na_8_mln_%E2%82%BD/)).

**Переупаковка.** Из одного эфира получается минимум 7 форматов: статья из расшифровки, нарезка на Reels/Shorts, цитаты-посты, карточки и схемы, рассылка ([vc.ru, Шубин](https://vc.ru/id3193770/2263876-repurpozhing-kontenta-sovety)). Клипы по 15–60 секунд, каждый самостоятелен ([Promopult](https://blog.promopult.ru/content/kak-ispolzovat-kontent-povtorno.html)). Связка «нарезчик → RSS → автопостинг» описана у SMMplanner и РилсБосс ([SMMplanner](https://smmplanner.com/blog/kontient-zavod-dlia-korotkikh-vidieo/)).
→ *Для APEC:* одна «тема-якорь» (например, «сколько стоят визараны за сезон») раскладывается так: длинное видео Димы на YouTube → 3–5 Shorts/Reels → карусель → пост в TG → SEO-статья на сайт → материал для vc.ru и Дзена → креатив для партнёров.

## 2. Редакционная матрица, рубрикатор, редполитика

**Матрица как конструктор.** Параметры комбинируются, в ячейке пишется идея, а не готовая тема. Заполнять все ячейки не обязательно. Идеи берутся у конкурентов (парсинг) и из Вордстата. Матрица служит источником тем для контент-плана ([Unisender](https://www.unisender.com/ru/glossary/matricza-kontenta/), [Texterra: матрицы](https://texterra.ru/blog/matritsy-kontenta-kak-bystro-pridumyvat-idei-dlya-statey.html)).

**Подход Наты Анарбаевой** (найдено только в выдаче; транскрипты и курсы недоступны напрямую):
- В редакционной матрице, в отличие от контент-плана, кроме тем есть **«углы»**: как мы расскажем, с какой стороны смотрим на тему ([sozai](https://sozai.app/transcript/content-zavod-building-system-guide/)).
- Матрица соединяет маркетинг и журналистику для бренд-медиа. Её дополняет **«лестница внимания»** для работы с **горячим и формирующимся спросом**. Сегментация может идти по болям, цене, возрасту. Структура: контент-единицы, углы подачи, хуки ([sozai: конструктор тем](https://sozai.app/transcript/content-theme-builder-1-million-views/)).
- Матрица по уровням осознанности: сформировать представление о решении, объяснить проблему, показать, почему продукт лучший и почему вы лучше конкурентов ([выдача по Анарбаевой / Martin Media](https://mmedia.by/blog/kak-postroit-content-zavod/)).
- В курсе «Система ведения контента» 8 модулей: рубрики под цели и продукты, шаблон рубрикации, шаблон контент-плана (дата, соцсеть, рубрика, формат, идея, **статус**), шаблон «фантограммы» для генерации идей, чек-лист аналитики, раскладка рубрик по дням недели, баланс «экспертиза / доверие / продажи» ([anarbaeva.pro](https://anarbaeva.pro/content-system)).
- Видео «Контент-план, который приводит клиентов. Вся стратегия контента в одной таблице» (51 мин, июнь 2026) ([Rutube](https://rutube.ru/video/2782ebd61e64f518a42dc7c23ba8dcd1/)).
- **Не найдено:** публичного шаблона матрицы Анарбаевой с названиями колонок. Есть только пересказы.

**Рубрикатор:** название, цель (продать, развлечь, проинформировать), суть, соцсеть, визуал и формат, периодичность ([Texterra](https://texterra.ru/blog/realizatsiya-kontent-marketingovoy-strategii.html), [st-lt](https://st-lt.ru/blog/useful/sostavlyaem-matriczu-kontenta.html)).

**Документы контент-стратегии:** исследования, ToV, рубрики (пиллары), канальный план, роли и процессы. Результат — документ стратегии, матрица и редполитика ([Kokoc](https://kokoc.com/blog/kontent-strategiya/), [Madcats шаблон](https://madcats.ru/content-marketing/content-strategy-template/)).

**Редполитика:** общая характеристика ToV, принципы (сложное объяснять просто, не заискивать, без двусмысленных шуток), формулировки, типографика ([Kokoc](https://kokoc.com/blog/redpolitika/), [sidorinlab](https://sidorinlab.ru/blog/kak-razrabotat-tone-of-voice-brenda-obyasnyaem-i-pokazyivaem)). Есть открытый образец — PDF «Редполитика Т—Ж» ([1ps.ru](https://1ps.ru/files/blog/2024/redpolitika-chto-eto-takoe-zachem-ona-nuzhna-kompanii/%D0%A0%D0%B5%D0%B4%D0%BF%D0%BE%D0%BB%D0%B8%D1%82%D0%B8%D0%BA%D0%B0%20%D0%A2%E2%80%94%D0%96.pdf)).

→ *Матрица APEC (предложение):* сегмент (зимовщик / живущий на Пхукете / предприниматель с бизнес-поездками / номад) × ступень Ханта (5) × угол (цифры и деньги — Дима; быт и опыт — Алекс; миф/разоблачение; кейс клиента; сравнение DTV/ED/APEC; новость или изменение правил) × формат (Reels, карусель, TG, Shorts, long, SEO, vc/Дзен, креатив) × цель (охват / доверие / заявка).

## 3. Контент-журналистика и бренд-медиа

- Бренд-медиа рассказывает не только о продукте. Порядок запуска: цели в связке с бизнес-стратегией → исследование аудитории → формат → команда и редпроцесс → продвижение ([sdelaem.agency](https://sdelaem.agency/blog/kak-sozdat-krutoe-brend-media-i-komu-voobshhe-stoit-ego-zapuskat/)).
- Роли: **главред** (стратегия, финальное решение о публикации), автор, дизайнер, SMM. Бренд-медиа — отдельный проект с отдельным лидером ([sdelaem.agency](https://sdelaem.agency/blog/kak-sozdat-krutoe-brend-media-i-komu-voobshhe-stoit-ego-zapuskat/), [ADPASS](https://adpass.ru/chto-takoe-brend-media-kak-ego-sozdat-i-prodvigat/)).
- **Экономика по Ильяхову и Скрябину:** производство контента — около 20% бюджета, 80% уходит на трафик, продвижение и поддержку ([maximilyahov.ru](https://maximilyahov.ru/blog/all/better-call-rodion/)). Книга Скрябина «Как сделать крутое бренд-медиа» ([Литрес](https://litres.com/book/rodion-skryabin/kak-sdelat-krutoe-brend-media-71606902/read/)).
- **Т—Ж:** запущен в 2014 году как блог на WordPress. Автор пишет сам, у каждого есть личный редактор, авторский стиль сохраняется. С гострайтерами и агентами редакция не работает. Пользовательские рубрики вроде «Дневника трат» сделали сообщество в 3 млн человек ([t-j.ru/about](https://t-j.ru/about/)). → *Для APEC:* рубрика «Дневник зимовки / сколько стоил сезон на Пхукете» от клиентов и амбассадоров.
- **TexTerra:** главред обеспечивает «бесперебойные поставки» (график, авторы, гостевые статьи, дистрибуция). За 9 лет вышло больше 2000 статей ([ЦереброТаргет](https://blog.xn--90aha1bhc1b.xn--p1ai/kak_rabotaet_blog_texterra)).
- **Инфоповоды** бывают плановые (календарь, сезон, выставки) и реактивные (ньюсджекинг через комментарий эксперта или пояснение). В плане оставляют окно под ситуативку ([Texterra: ньюсджекинг](https://texterra.ru/blog/chto-takoe-nyusdzheking-rossiyskie-primery-sovety-i-chek-listy.html), [Cossa/Pressfeed](https://www.cossa.ru/pressfeed/350439/)). → *Для APEC:* изменения визовых правил Таиланда, начало сезона, ТДАС, новости о картах APEC — реактивная полоса с SLA 24–48 часов.

## 4. Маркетинговая стратегия как основа

- Состав: анализ рынка и конкурентов, ЦА и сегменты с **JTBD**, позиционирование и **УТП**, цели и KPI (SMART/OKR), каналы и единая воронка, бюджет ([Яндекс Директ](https://direct.yandex.ru/base/articles/marketingovaya-strategiya), [magnetto](https://magnetto.pro/media/article/marketingovaia-strategiia-i-plan-razrabotka-vidy-elementy-avtomatizatsiia-i-primery/)).
- **ToV-гайд на одну страницу:** зачем коммуникация, для кого, 3–4 принципа голоса, обращение («вы» или «ты»), персонализация ([advertisingforum](https://advertisingforum.ru/blog/tone-of-voice/)). Пример Тинькофф: неформально, но уважительно, сервисные тексты серьёзные, в историях допустим юмор ([там же](https://advertisingforum.ru/blog/tone-of-voice/)).
- **Частота пересмотра:** стратегия раз в 1–3 года, план раз в квартал, тактика еженедельно. Внепланово — при изменении рынка или продукта ([Яндекс Директ](https://direct.yandex.ru/base/articles/marketingovaya-strategiya)).
- Кейс KoBolt подтверждает, что завод начинается с аудита ниши, болей и триггеров, ToV и визуального стиля ([workspace](https://workspace.ru/cases/kak-kobolt-poluchil-3-12-mln-prosmotrov-i-cpv-0-068-s-pomoschyu-kontent-zavoda/)).
- **Не найдено:** русскоязычного канваса, который сводит стратегию и редматрицу в один артефакт. Есть шаблон контент-стратегии у Madcats ([madcats](https://madcats.ru/content-marketing/content-strategy-template/)).

## 5. Процессы согласования и роли

**Редпроцесс Т—Ж (6 этапов):** заявка (редактор может отклонить, сузить или попросить переделать) → «мясо» (факты, материал) → черновик → чистовик → оформление и вёрстка → публикация и первый посев. Работа идёт в Google Docs, у автора личный редактор, финальную вычитку делает второй человек ([Ильяхов](http://maximilyahov.ru/blog/all/tinkoff-bootcamp-8/)).

**Общая схема:** драфт → редактура → корректура → вёрстка → публикация. В плане фиксируются тема, дата, площадка, **статус**, исполнитель, результат. ЛПР подключаются на этапе сценария ([mc.today](https://mc.today/blogs/5-etapov-kontent-marketinga-ot-planirovaniya-k-analitike-i-kto-voobshhe-etim-vse-zanimaetsya/amp/)). Сценарий короткого видео: хук в первые секунды → суть или история → CTA ([edugusarov](https://edugusarov.by/kak-snimat-reels-i-shorts-kotorye-zaletyat-v-trendy-format-tema-sczenarij-sekrety/)).

**Инструментальная поддержка (Kaiten):** родительские и дочерние карточки, двухнедельные спринты, метки, база знаний с ТТ и параметрами видео. Автоматизация сняла ручной диспетчинг («кто что делает, где застряли правки, какие дедлайны»), экономия больше 600 тыс. ₽ в месяц ([Kaiten](https://kaiten.ru/blog/case-media-production/)).

→ *Предлагаемые статусы для CRM APEC:* `идея → тема утверждена (главред) → тезисы/хуки → сценарий → утверждён спикером → производство (съёмка/генерация) → монтаж → QA/фактчек → готово → запланировано → опубликовано → аналитика 7д/30д`. Тема — родительская карточка, единицы под каналы — дочерние.

**Амбассадоры и кабинеты авторов:** платформы для поиска (GetBlogger, LabelUp, Perfluence) или лояльные клиенты. Обязательно письменное согласие на использование UGC (штраф до 5 млн ₽). Качество важнее количества. Реферальная механика: промокод или ссылка, вознаграждение бывает до 50% ([Kokoc](https://kokoc.com/blog/ambassador-brenda-chto-eto/), [Callibri](https://callibri.ru/blog/ambassador-brenda-kak-najti-i-rabotat)). Т—Ж показывает модель «автор пишет сам + личный редактор» ([t-j.ru](https://t-j.ru/about/)). **Не найдено:** русскоязычного разбора интерфейса «кабинета амбассадора».

## 6. Медиатека / DAM

- DAM хранит, описывает (метаданные), ищет и распространяет. Смарт-коллекции строятся по тегам. Есть проверка перед публикацией и выгрузка в соцсети «в один клик» ([Mediaquad](https://mediaquad.ru/blog/dam/chto-takoe-dam-sistema-podrobnoe-rukovodstvo/), [Brandquad: DAM или фотобанк](https://brandquad.ru/blog/dam/dam-ili-fotobank-chto-vybrat/)).
- Практика для небольших команд: нейминг `ГГГГММДД_тема`, подпапки по типу, каталог на тегах вместо файловой системы, мастер-аккаунт с раздачей доступов, единая миграция со всех носителей ([Picvario](https://picvario.ru/kak-organizovat-komandnuyu-rabotu/), [Хабр 188094](https://habr.com/ru/articles/188094/)). Сравнение Яндекс Диска и корпоративного DAM есть на [vc.ru](https://vc.ru/services/146297-gde-biznesu-rabotat-s-foto-i-video-sravnivaem-yandeksdisk-i-korporativnyi-soft-dlya-upravleniya-mediakontentom).
- База знаний с ТТ на видео (кодеки, форматы) лежит рядом с задачами ([Kaiten](https://kaiten.ru/blog/case-media-production/)).
- → *Для APEC:* таблица ассетов в CRM (тип: A-roll/B-roll/фото/ген; спикер; локация Пхукета; тема; права: своё/амбассадор/сток/ИИ; модель генерации и промпт; использования). Сгенерированные в Veo/Nano Banana B-роллы складывать туда же с промптом, чтобы переиспользовать.

## 7. Метрики, дашборды, атрибуция

- Telegram: **ERR** = средние просмотры последних 10–20 постов / подписчики × 100. Нормальный охват 20–40% подписчиков. **ER** = реакции / подписчики × 100. Инструменты TGStat и Telega.in ([vc.ru ERR](https://vc.ru/telegram/2976805-err-v-telegram-nakrutka-reaktsiy), [Labelup](https://help.labelup.ru/article/4727), [eLama](https://elama.ru/blog/servisy-analitiki-telegram/)). Отдельно о том, что просмотры не главная метрика: [vc.ru](https://vc.ru/marketing/1980340-metriky-telegram-kanala-v-2025-godu).
- Метрики контент-маркетинга (охват → вовлечение → конверсия → CPA, CAC, ROMI) ([Roistat](https://roistat.com/rublog/metriki-kontent-marketinga/), [Callibri](https://callibri.ru/blog/metriki-v-kontent-marketinge)). Для заводов с UGC и блогерами базовая метрика — **CPV**: 0,068–0,11 ₽ в кейсах выше.
- **Сквозная аналитика:** без неё продажа после чтения статьи уходит в «прямой заход». Нужна связка сайт → CRM → продажи ([Roistat](https://roistat.com/rublog/skvoznaya-marketingovaya-analitika/), [Хабр 989460](https://habr.com/ru/articles/989460/)).
- **Атрибуция соцсетей:** `utm_source=instagram&utm_medium=social&utm_content=<формат/ID>` ([Callibri](https://callibri.ru/blog/chto-takoe-instagram-reels), [metrium](https://metrium.kz/blog/tpost/a4gpp7s221-utm-metki-dlya-sotssetei-avtomatiziruite)). Уникальный промокод на канал. Кодовое слово в директ → TG-бот ([там же](https://callibri.ru/blog/chto-takoe-instagram-reels)). UTM для Telegram: [OneSpot](https://onespot.one/all-posts/utm-metki-dlya-telegram).
- → *Для APEC:* у каждой единицы контента свой `content_id`, который попадает в UTM, deeplink бота (`/start=cid`) и промокод амбассадора. В CRM заявка получает `first_touch_content_id` и `last_touch_content_id`. Дашборд «тема → единицы → охват → лиды → оплаты».

## 8. ИИ в контент-заводе: кейсы и грабли (Хабр, vc.ru)

- **Без человека нельзя.** Ни один работающий завод (включая Jasper и «заводы под ключ») не обходится без людей: те фильтруют темы на входе и редактируют на выходе. Jasper сам переименовал подход в «главред синтетической рабочей силы». У ИИ нет этики и ответственности ([Хабр 1039432](https://habr.com/ru/articles/1039432/)).
- **Разделение труда:** ИИ делает около 70% (данные, структура, черновик), эксперт около 30% (фактчек, редактура). В одном кейсе 40 статей в месяц вместо 10. Архитектура SEO-агента в четыре слоя: Perception (GSC, Вебмастер, SERP раз в 6 часов) → Reasoning (LLM) → Action (WordPress REST, JSON-LD) → Memory (граф знаний) ([Хабр 955108](https://habr.com/ru/articles/955108/)). Эволюция «YAML-оркестратор → Dify+Tavily → офис ИИ-сотрудников» описана в [Хабр 1091084](https://habr.com/ru/articles/1091084/).
- **Мультиагентный пайплайн для текста:** поиск фактов → анализ источника → черновик → критика → правка (Mastra, n8n). Фактчек через Perplexity, веб-поиск, Claude Projects и вручную ([Хабр 1028530](https://habr.com/ru/articles/1028530/)). Подборка из 62 инструментов для редакций: [Хабр 1031982](https://habr.com/ru/articles/1031982/).
- **Конвейер воркеров** (новостная система): collector (160 источников, раз в 15 минут) → scraper → **deduplicator** → ai_filter → translator (локальный Qwen ради экономии) → llm_editor → image_worker → publisher, плюс **hitl**-воркер ([Хабр 1023446](https://habr.com/ru/articles/1023446/)).
- **Видео через kie.ai на n8n:** Sora 2 через Kie.ai (`portrait`, `n_frames: 10`). Совет: не просить GPT «придумать вирусное», а делать «контролируемый хаос», то есть комбинировать заданные массивы параметров в ноде Code ([Хабр 988522](https://habr.com/ru/articles/988522/)). Для нас это прямо применимо к промптам Veo и Nano Banana: шаблоны сцен Пхукета × действия × стиль.
- **Стоимость Reels-аватарного конвейера:** Telegram-триггер → LLM (сценарий) → ElevenLabs (клон голоса) → HeyGen (аватар) → GPT Image (фоны) → ffmpeg. Около $1,87 за ролик, 100 роликов — около $187 в месяц ([vc.ru 2266833](https://vc.ru/ai/2266833-kak-postroit-kontent-zavod-dlya-sozdaniya-reels-247-bez-uchastiya)). Шаблоны n8n для Veo-3 и Shorts с ffmpeg-приведением к 1080×1920 есть в каталоге ([n8n 8429](https://n8n.io/workflows/8429-ai-video-automation-engine-generate-and-publish-yt-shorts-with-veo-3-or-sora-2/)).
- **Где ИИ реально эффективен:** однотипные структурные форматы (карточки, короткие новости, FAQ) ([vc.ru 2301761](https://vc.ru/marketing/2301761-kontent-zavody-s-ii-agentami)).
- **Грабли:**
  - Мультиагентная система на CrewAI в демо работала, а на произвольных входах превратилась в «бесконечное совещание» ([Хабр 1026856](https://habr.com/ru/articles/1026856/)).
  - Технически рабочий завод на n8n не зарабатывает без понимания ЦА и боли ([Хабр 966144](https://habr.com/ru/articles/966144/)).
  - Бесплатные модели галлюцинируют чаще. Нужен обязательный фактчек цифр, а у нас цифры — главный актив Димы ([Хабр 947964](https://habr.com/ru/articles/947964/), [Хабр 1028530](https://habr.com/ru/articles/1028530/)).
  - «Навайбкоженный» workflow на 127 нод трудно поддерживать ([Хабр 1076084](https://habr.com/ru/articles/1076084/)).
- **Экономика ИИ-видео:** 30–60 полностью сгенерированных роликов в месяц, около 103 ₽ за 5-минутное слайд-видео ([Sostav](https://www.sostav.ru/blogs/283819/76058), [Sostav 98054](https://www.sostav.ru/blogs/287070/98054)). Цифры авторские, не проверены.

---

## Лучшие источники (20)

1. https://habr.com/ru/articles/1039432/ — почему автономный завод не работает без человека, AI slop, HITL.
2. https://habr.com/ru/articles/955108/ — четырёхслойная архитектура SEO-агента, распределение 70/30 между ИИ и экспертом.
3. https://habr.com/ru/articles/1023446/ — конвейер из 11 воркеров с дедупликацией и HITL.
4. https://habr.com/ru/articles/988522/ — n8n и kie.ai (Sora 2), «контролируемый хаос» в промптах.
5. https://habr.com/ru/articles/1028530/ — модели для русского текста в 2026 году, мультиагентная редактура, фактчек.
6. https://habr.com/ru/articles/1026856/ — грабли мультиагентности.
7. https://habr.com/ru/articles/966144/ — завод без PMF не зарабатывает.
8. https://habr.com/ru/companies/kaiten/articles/1057092/ и https://kaiten.ru/blog/case-media-production/ — 400 видеозадач в месяц, процесс и карточки.
9. http://maximilyahov.ru/blog/all/tinkoff-bootcamp-8/ — редпроцесс Т—Ж в 6 этапов.
10. https://maximilyahov.ru/blog/all/better-call-rodion/ — экономика бренд-медиа 20/80.
11. https://t-j.ru/about/ — масштаб и принципы Т—Ж, пользовательские рубрики.
12. https://www.sostav.ru/blogs/283819/76160 — три модели завода, план на 30 дней.
13. https://weeek.net/ru/blog/content-factory — вход, процесс и выход, роли, канбан.
14. https://anarbaeva.pro/content-system — рубрикация, шаблон плана со статусами, баланс рубрик.
15. https://rutube.ru/video/2782ebd61e64f518a42dc7c23ba8dcd1/ — Анарбаева: «вся стратегия контента в одной таблице».
16. https://sozai.app/transcript/content-zavod-building-system-guide/ — транскрипт Анарбаевой о заводе и углах подачи.
17. https://vc.ru/marketing/2731925-keis-kontent-zavoda-57-mln-prosmotrov-i-cpv-11-kopeek — модель «блогеры на окладе с KPI» для амбассадоров.
18. https://partner.market.yandex.ru/chtojournal/content-zavod-dlya-brenda/ — 70–90 роликов на человека в месяц.
19. https://vc.ru/ai/2266833-kak-postroit-kontent-zavod-dlya-sozdaniya-reels-247-bez-uchastiya — стек и себестоимость ИИ-Reels.
20. https://texterra.ru/blog/realizatsiya-kontent-marketingovoy-strategii.html — рубрикатор, редкалендарь, редакционный портфель.
21. https://kokoc.com/blog/redpolitika/ — 11 примеров редполитик.
22. https://roistat.com/rublog/skvoznaya-marketingovaya-analitika/ — сквозная аналитика и атрибуция контента.
23. https://picvario.ru/kak-organizovat-komandnuyu-rabotu/ — организация медиатеки команды.

**Что не нашлось или не удалось проверить:** полный текст и шаблон редакционной матрицы Анарбаевой (только пересказы в выдаче; транскрипты sozai.app и сайт закрыты прокси); русскоязычные разборы кабинетов амбассадоров; дашборды контента с конкретными макетами; кейсы контент-заводов в визовой или релокационной нише.
