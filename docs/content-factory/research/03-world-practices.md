# 03. Мировые практики: системы контент-маркетинга и контент-операций

> Исследование для проектирования внутреннего «контент-кабинета» APEC Center. Дата: октябрь 2026.
> Метод: веб-поиск по официальным сайтам, справочным центрам и обзорам. **Ограничения:** WebFetch к `planable.io` и `jasper.ai` заблокирован прокси, поэтому по ним используются выдержки из поисковой выдачи и сторонние обзоры. Пометка **[не проверено]** стоит там, где возможность продукта не подтверждена первоисточником.

---

## Краткий вывод: что взять в наш кабинет

1. **Бренд-ДНК как структурированный объект, а не PDF.** У всех AI-платформ «бренд» разложен на 3 слоя: голос (как звучим), база знаний (факты и продукт), стайлгайд и термины (правила и запреты). Jasper: Voice / Knowledge / Style Guide; Writer: voice profiles + Knowledge Graph + terms; Copy.ai: Brand Voice + Infobase. Повторяем эту схему, данные о продукте и FAQ подтягиваем из базы знаний CRM.
2. **Message house — центр стратегического экрана.** Главное сообщение («крыша»), 3–4 опоры и доказательства под каждой. Опоры становятся контент-пилларами, доказательства используются в генерации и в оценке LLM-судьёй.
3. **Матрица «стадия осознанности × персона × угол» как отдельная сущность.** Лестница Шварца/Ханта задаёт ось Y, персоны/JTBD — ось X, в ячейке лежат углы, хуки и рекомендуемые форматы. Каждая идея обязана ссылаться на ячейку, иначе её нельзя утвердить.
4. **Кампания как контейнер.** HubSpot, CoSchedule, StoryChief и Jasper группируют материалы по кампании: бриф → набор единиц для разных каналов → общая аналитика. У нас кампания = тема периода (например, «сезон ноябрь–декабрь, Таиланд 90 дней»).
5. **Одна «единица контента» и много «публикаций».** Идея/сценарий — одна сущность, адаптации под Reels, карусель, Telegram и vc.ru — дочерние публикации со своими статусами, датами и UTM. Так устроены StoryChief (один материал на много каналов) и Jasper Campaigns (один бриф на много ассетов).
6. **Согласование настраивается по типу контента и по стадиям.** Planable поддерживает режимы от «без согласования» до многоуровневого с фиксированным порядком, а Contentful позволяет задавать отдельный workflow для каждого типа контента. У нас три ворот: темы на период → тезисы и хуки → финальный сценарий. Перед каждыми воротами работает автоматический LLM-судья.
7. **Четыре вида одного списка.** Календарь, канбан по статусам, таблица и лента-превью (Planable: calendar/feed/list/grid; Notion: calendar/board/table/timeline). Для 30+ единиц в неделю нужнее всего канбан и лента-превью «как в Instagram».
8. **Карта каналов по модели PESO (Paid / Earned / Shared / Owned).** На ней видно, где мы присутствуем, где нет и как дела в каждом канале. Пульс строится на уровне канала, а не на уровне поста.
9. **Атрибуция замыкается на CRM.** HubSpot считает influenced contacts и attributed revenue через взаимодействия с ассетами кампании. У нас UTM-словарь + `utm_content=<publication_id>` + промокод или реф-ссылка на автора → заявка → оплата в CRM.
10. **Кабинет креатора — это лента брифов и одобренных материалов, персональные ссылки и коды, лидерборд** (GRIN, Aspire, Sprout Employee Advocacy, DSMN8, StoryChief Ambassadors).
11. **Медиатека — это метаданные плюс «где использовано».** Frame.io V4 предлагает кастомные поля и Collections (сохранённые фильтры), Brandfolder — аналитику использования, Bynder — таксономию и права. Каждый ассет связан с публикациями, а каждая генерация хранит промпт, модель, seed и стоимость.
12. **AI-движок — оркестрация асинхронных задач.** n8n вызывает LLM, затем kie.ai (задача с callback и статусами pending/processing/completed/failed), результат складывается в медиатеку. Кабинет показывает очередь задач и их стоимость.
13. **Гардрейлы — это рубрика, а не промпт.** LLM-as-judge оценивает по явной шкале: голос, точность фактов относительно базы знаний, соответствие стадии осознанности, запрещённые обещания. Порог прохождения хранится в настройках.
14. **Стратегия версионируется.** Ежемесячный пересмотр создаёт новую версию бренд-платформы, а каждая единица контента помнит, на какой версии она сгенерирована.

---

## 1. Платформы контент-операций и редакционных календарей

**CoSchedule Marketing Suite.** Главный экран — общий маркетинговый календарь: проекты и кампании в одном окне (Calendar Organizer). Есть Content Organizer для отбора, создания и продвижения контента, AI-ассистент Mia для черновиков и соцсообщений. Social Templates — переиспользуемые планы продвижения материала. ReQueue автоматически повторно публикует лучшие посты ([CoSchedule press](https://coschedule.com/press/coschedule-launches-two-new-ai-powered-marketing-calendars), [MarketingMonk](https://www.marketingmonk.so/products/coschedule)). Задачи создаются по шаблонам, в шаблоны встраиваются согласования и правила, а ожидающие ревью видны на дашбордах ([CoSchedule guide](https://coschedule.com/guide/getting-started-with-coschedule-for-power-users/task-management-in-coschedule), [rfp.wiki](https://www.rfp.wiki/marketing/content-marketing-platforms/coschedule)).
*Взять:* шаблон задач на тип единицы (например, «Reels спикера» = сценарий → съёмка → монтаж → обложка → публикация) и шаблон дистрибуции («статья vc.ru» → 3 поста в Telegram + карусель).

**StoryChief.** Визуальный календарь кампаний. Редактор поддерживает совместное редактирование, комментарии и историю правок. После шага согласования материал публикуется в CMS, соцсети и рассылки из одной карточки. Календарь можно расшарить для внешней обратной связи ([StoryChief](https://storychief.io/content-teams), [content workflow](https://www.storychief.io/content-workflow-software)).

**Planable.** Четыре вида: calendar, feed, list, grid. Работают drag-and-drop переноса дат и метки. Согласование настраивается от необязательного до многоуровневого. Стадии идут последовательно, пост переходит дальше автоматически, а запланировать его можно только после прохождения всех стадий. Внешний согласующий может работать по ссылке из письма без регистрации ([Planable blog](https://planable.io/blog/content-approval-workflow/), [Help Center](https://help.planable.io/hc/en-us/sections/21798857002780-Approval-process); сайт для WebFetch заблокирован, данные взяты из выдачи).

**Notion / Asana / Monday — шаблоны.** Канонический набор полей: Title, Status (Idea → Draft → Edit → Approved → Published), Channel, Owner, Publish date, Brief, Assets, Tags, Audience, Goal, Keywords, URL. Виды: calendar, board, table, timeline ([Notion guide](https://www.notion.com/help/guides/this-content-calendar-drives-high-performance-marketing-teamwork), [2sync](https://2sync.com/blog/best-content-calendar-templates-notion)). Asana использует секции Planning / Creation / Approval / Scheduling / Archive, кастомные поля Channel, Stage, Audience и правила вида «Stage = In review → назначить редактора» ([Asana Help](https://help.asana.com/s/article/content-calendar), [Asana template](https://asana.com/templates/editorial-calendar.md)). Monday устроен аналогично **[не проверено детально]**.

**Contentful.** Контент-модель — это набор content types, которые связаны reference-полями. Это позволяет переиспользовать блоки вместо копирования. На одном типе может работать несколько workflow с состояниями Draft → Review → Approved → Published ([Contentful Help](https://www.contentful.com/help/content-model-and-content-type/), [workflows](https://www.contentful.com/help/ai-automations/workflows/workflows-management/)).
*Взять:* хук, CTA, доказательство и оффер хранить как переиспользуемые блоки со ссылками, а не как текст внутри сценария.

**HubSpot.** Campaigns объединяют ассеты: посты, письма, лендинги, рекламу. По ним строятся отчёты о тратах, выручке, attributed revenue и influenced contacts ([HubSpot KB](https://knowledge.hubspot.com/campaigns/analyze-campaigns)). SEO Topics строят кластер: пиллар-страница и подстраницы. Встроенный краулер проверяет, что подстраница ссылается на пиллар, и тогда связь отмечается зелёной линией ([insidea](https://insidea.com/blog/hubspot/kb/how-to-attach-content-to-an-seo-topic-in-hubspot), [HubSpot KB topics](https://knowledge.hubspot.com/marketing-tools/topics)).
*Взять:* для SEO-статей и Дзена — кластер с автоматической проверкой перелинковки.

**Semrush Content Toolkit.** Topic Research выдаёт карточки тем с объёмом поиска, заголовками из топа и вопросами. SEO Writing Assistant проверяет читаемость, оригинальность, SEO и tone of voice. ContentShake стал частью Content Toolkit. Также есть генератор SEO-брифов и репёрпосинг ([Semrush blog](https://www.semrush.com/blog/best-content-marketing-tools/), [eesel](https://www.eesel.ai/blog/semrush-content-writer)).
*Взять:* у SEO-брифа должны быть поля «ключ, частотность, вопросы из выдачи, конкуренты в топе».

**Jasper / Writer / Typeface / Copy.ai** разобраны в разделах 2 и 8.

## 2. Слой стратегии: бренд-платформа и её «подмешивание» в генерацию

**Как продукты хранят бренд-ДНК:**
- **Jasper Brand Voice** — три опоры: *Voice* (описание тона и образцы из текста, файла или URL, включая лучшие посты), *Knowledge Base* (факты о компании и продукте, с тегами), *Style Guide* (грамматика, пунктуация, правила, задаются админом) ([Jasper blog](https://www.jasper.ai/blog/social-media-marketing-guide-jasper), [osher](https://osher.com.au/tools/jasper/)). С 2025 года слой называется Jasper IQ: он подмешивает голос, правила и контекст во все агенты ([Built In](https://builtin.com/company/jasper/faq/innovation-technology-agility)).
- **Writer.** Terms — словарь одобренных, ожидающих и запрещённых терминов. Snippets — готовые формулировки. Публикуемый styleguide со ссылками на правила. Voice profiles и Knowledge Graph отвечают за фактуру ([martech.zone](https://martech.zone/writer-brand-voice-style-guide-ai-writing-assistant), [growwstacks](https://growwstacks.com/blog/ai-brand-voice-knowledge-graphs)).
- **Typeface.** Несколько Brand Kits. Ассеты-изображения используются в AI-сценах, текстовые ассеты (PDF/Word) переупаковываются в посты. Brand Hub связывает ассеты с аудиториями и сигналами эффективности. Brand Agent проверяет визуальные гайды, комплаенс и юридические моменты ([Typeface Academy](https://typeface.ai/education/typeface-academy/getting-started-with-typeface), [Typeface brand teams](https://www.typeface.ai/use-cases/brand-and-creative/index.html)).
- **Copy.ai.** Brand Voice выводится из существующих текстов, Infobase — хранилище фактов и гайдлайнов ([eesel](https://www.eesel.ai/blog/copy-ai)).
- **HubSpot Breeze.** Brand voice настраивается с помощью AI, контент-агент использует персоны и данные CRM ([HubSpot KB](https://knowledge.hubspot.com/blog/set-up-brand-voice-using-ai)).

**Каркас стратегической панели (по общепринятым фреймворкам):**
- **Позиционирование:** для кого, категория, отличие, причина верить.
- **ICP/персоны + JTBD:** ситуация → мотивация → ожидаемый результат, а также страхи и возражения.
- **Message house:** крыша (одно предложение), 3–4 опоры, доказательства под каждой опорой: данные, кейсы, цитаты ([Umbrex](https://umbrex.com/?p=241777), [Atlassian template](https://www.atlassian.com/software/confluence/templates/message-house)).
- **Editorial mission** по Пулицци: кому служим, что даём, какой результат у читателя. Плюс «content tilt» — чем наш контент отличается от того, что аудитория уже потребляет ([dummies/Pulizzi](https://www.dummies.com/article/business-careers-money/business/marketing/how-to-craft-your-content-marketing-mission-statement-138486), [agorapulse](https://www.agorapulse.com/blog/social-media-marketing-world/content-marketing-strategy-joe-pulizzi/)).
- **ToV:** шкалы (формально↔разговорно и т. п.), «говорим / не говорим», примеры-эталоны. **Ценности. Продуктовая линейка:** берётся из CRM — услуги, цены, сроки.

*Механика подмешивания (общий паттерн):* генерация получает контекстный пакет: голос + релевантные факты из базы знаний + правила стайлгайда + выбранная ячейка матрицы. Проверка идёт против тех же правил. Отсюда требование: всё должно храниться **полями**, а не одним текстом, чтобы собирать пакет выборочно.

## 3. Омниканальный дашборд маркетинга

- **Карта каналов (PESO):** Paid (реклама, платные интеграции), Earned (СМИ, отзывы, упоминания), Shared (соцсети, UGC, амбассадоры), Owned (сайт, лендинги, блог, Telegram, база). Модель предложила Джини Дитрих в книге *Spin Sucks* ([thinkinsights](https://thinkinsights.net/index.php/consulting/peso-model), [Brandpoint](https://www.brandpoint.com/?p=17287)). Для APEC: Reels/карусели Instagram, YouTube, Дзен, Telegram — Shared/Owned; vc.ru — Owned/Earned; SEO и лендинги — Owned; реклама — Paid; рефералы и амбассадоры — Earned/Shared.
- **Пульс:** у каждого канала есть статус (активен / пауза / нет), плановая и фактическая частота, охват, вовлечённость, переходы, заявки, оплаты, CAC/ROMI для платных каналов, тренд за 4 недели и светофор.
- **Атрибуция:** HubSpot предлагает модели first touch, last interaction, linear, full-path, W- и U-shaped ([insidea](https://insidea.com/blog/hubspot/kb/how-hubspot-attribution-reporting-can-help-you-measure-the-impact-of-your-campaigns)). Influenced contacts — это контакты, взаимодействовавшие с ассетами кампании. Выручка сделки распределяется между взаимодействиями ([HubSpot KB](https://knowledge.hubspot.com/campaigns/analyze-campaigns)).
- **UTM-дисциплина:** нижний регистр, один разделитель, контролируемый словарь source и medium, обязательные source/medium/campaign. Значения medium выровнены с группировкой каналов GA4. `utm_content` используется для креатива или варианта, `utm_id` — для стабильности. Нужны живой словарь UTM и аудиты ([brandedagency](https://brandedagency.com/blog/utm-naming-conventions-ga4-playbook), [uplifter](https://uplifter.ai/article/utm-naming-conventions)).
  *Для нас:* `utm_campaign=<campaign_slug>`, `utm_content=<publication_id>`, `utm_term=<author_slug>`. Генератор ссылок встроен в карточку публикации. Для Instagram и Telegram, где ссылки неудобны, — кодовые слова ChatPlace и промокоды на публикацию или автора.

## 4. Редакционная матрица (messaging / editorial matrix)

- **Лестница осознанности:** Unaware → Problem aware → Solution aware → Product aware → Most aware (Шварц, *Breakthrough Advertising*, 1966). Правило: двигать человека на одну ступень и говорить с ним на его уровне ([aokmarketing](https://aokmarketing.com/the-five-stages-of-awareness-and-how-to-move-people-one-step/)). Бен Хант в книге *Convert!* (Wiley) переносит это в «Awareness Ladder» для веб-страниц: каждая страница нацелена на свою ступень ([OpenView](https://openviewpartners.com/?p=5931), [Goodreads](https://www.goodreads.com/book/show/11208710-convert)).
- **Content mapping matrix:** для каждой персоны строится таблица «стадия × тип контента × тема × канал» ([PMA](https://www.productmarketingalliance.com/content-mapping-template/), [Demand Metric](https://www.demandmetric.com/content/content-mapping-template)).
- **Пиллары и кластеры:** опоры message house превращаются в контент-пиллары, а пиллары — в SEO-кластеры (HubSpot topics, см. раздел 1).
- **Ячейка матрицы для APEC** (предложение): `ступень × персона/JTBD × пиллар` → углы (боль, выгода, миф, сравнение, кейс, процесс, срочность) + триггеры (страх отказа во въезде, экономия на визаранах, статус) + доказательства из книги продаж и рыночных данных + рекомендуемые форматы и каналы. Отчёт «покрытие матрицы» показывает, какие ячейки пусты за период. Аналогичную функцию выполняет «content gap» в Semrush.

## 5. Процесс: ideation → brief/hooks → draft → approval → production → publish → measure

- **Отраслевой минимум статусов:** Idea → Draft → Edit/Review → Approved → Scheduled → Published (Notion, Asana, Contentful). Planable и Canva добавляют жёсткое правило: публикация недоступна без пройденного согласования ([Canva design approval](https://www.canva.com/help/design-approval/)).
- **Многоуровневость:** последовательные стадии, на каждой свои согласующие, автопереход дальше; внешний согласующий может участвовать без аккаунта (Planable). В Canva Teams согласует только один человек, в Enterprise — несколько согласующих и группы.
- **Для APEC — три ворот вместо одного финального ревью:**
  1. **План периода** (неделя или две): список тем, каждая привязана к ячейке матрицы и кампании. Утверждается пакетом.
  2. **Тезисы и хуки:** по каждой теме 3–5 вариантов хука и структура. Пользователь выбирает или правит, LLM-судья предварительно фильтрует.
  3. **Финальный сценарий/текст** по каналам. После этого начинается продакшн: генерация медиа, съёмка спикеров, монтаж, затем проверка готового ассета.
- **Механика согласования:** решение (approve / request changes / reject) + комментарий к фрагменту + версия. При «request changes» объект откатывается в Draft, а сравнение версий доступно в StoryChief и Planable. Шаблоны задач с правилами автоназначения (CoSchedule, Asana rules) снимают ручную координацию.
- **Measure:** через 24 часа, 7 и 30 дней после публикации метрики подтягиваются в карточку и в ячейку матрицы. Так замыкается цикл «какие углы и хуки работают».

## 6. Кабинет креатора / амбассадора

- **GRIN:** у креатора свой портал с брифами, сроками и требованиями. Контент отправляется на ревью до публикации, команда может запросить правки, одобренный материал засчитывается в deliverables кампании. Уникальные ссылки и промокоды автора связываются с выручкой через интеграцию с магазином, выплаты делаются из системы ([vidpros](https://vidpros.com/grin-co-review/), [socialrevver](https://socialrevver.com/blog/grin-influencer-marketing-platform)).
- **Aspire:** брифы, задачи, deliverables и собственная статистика у креатора. Массовая генерация промокодов и ссылок на креатора (Shopify), ко-брендовые витрины ([Aspire](https://www.aspire.io/platform/convert), [Aspire help](https://help.aspireiq.com/en/collections/2579797-creator-resources)).
- **Later Influence + Mavely:** affiliate-deliverables и уникальные ссылки, трекинг продаж, выплаты 1-го и 15-го числа ([Later Help](https://help-influence.later.com/hc/en-us/articles/20462302820119-Affiliate-Marketing-With-Later-Influence), [eMarketer](https://www.emarketer.com/content/later-s--2-4-billion-creator-engine-shows-how-fast-creator-economy-growing)).
- **Sprout Social Employee Advocacy:** лента stories по темам, на которые подписан сотрудник, закреплённые материалы, еженедельный дайджест. Отчёты General / Content / Curator / User / Leaderboard / Distribution, очки за действия настраиваются ([Sprout support](https://advocacysupport.sproutsocial.com/hc/en-us/articles/46907079149965-Reporting-in-Employee-Advocacy-Sprout-Bites)).
- **DSMN8:** контент-хаб, AI-персонализация подписи под голос сотрудника, автоматические UTM с параметрами команды, группы, кампании и источника, интеграция с GA4, очки и лидерборды ([DSMN8](https://dsmn8.com/employee-advocacy/)).
- **StoryChief Ambassadors:** заранее одобренные соцсообщения, которые сотрудник персонализирует, лента компании ([StoryChief](https://storychief.io/ambassadors)).

*Для APEC:* профиль амбассадора (ник, каналы, реф-код из CRM, ставка). Лента «готово к публикации»: одобренный текст + медиа + персональная ссылка/код + вариант подписи «своим голосом». Задания-брифы со сдачей ссылки на пост и ревью. Личная статистика: клики → заявки → оплаты → начисления. Тот же кабинет подходит двум спикерам: у них есть брифы на съёмку, сценарии и телесуфлёр-версия текста **[функцию телесуфлёра предлагаем сами, в источниках её нет]**.

## 7. Медиатека / DAM

- **Bynder:** настраиваемая таксономия (бренд, регион, кампания, права, аудитория), AI-теги, версии, жизненный цикл и архив, workflow согласования ([Bynder blog](https://www.bynder.com/en/blog/dam-taxonomy-best-practices), [rfp.wiki](https://www.rfp.wiki/design-multimedia/bynder)).
- **Frame.io V4:** 32 встроенных поля метаданных + кастомные (текст, выпадающий список, дата, переключатель). Collections — динамические сохранённые выборки по метаданным. Переработанные комментарии на кадре для ревью видео ([Frame.io blog](https://blog.frame.io/2024/04/23/frame-io-v4-beta-metadata-collections/), [Adobe news](https://news.adobe.com/news/news-details/2024/adobe-introduces-next-generation-of-frame-io-to-accelerate-content-workflow-and-collaboration-for-every-creative-project)).
- **Brandfolder:** Brand Intelligence показывает, кто, где и сколько использует ассет, и выделяет топовые ассеты. Коллекции, права, сроки действия ([toolradar](https://toolradar.com/tools/brandfolder), [SoftwareOne](https://platform.softwareone.com/product/brandfolder/PCP-6880-7539)).
- **Canva Brand Kit:** несколько китов (логотипы, цвета, шрифты, фото, иконки), бренд-шаблоны с блокировкой элементов, Brand Controls ограничивают цвета и шрифты и требуют approval ([Canva Help](https://www.canva.com/help/brand-control/)).

*Для APEC:* ассет хранит тип (b-roll, фото спикера, обложка, слайд карусели, AI-изображение, AI-видео, музыка), источник (съёмка / kie.ai / сток), теги (локация: Пхукет, Бангкок, аэропорт; сцена; спикер; сезон), права и срок, версии. Для AI-ассетов дополнительно хранятся промпт, модель, seed, стоимость, родительский ассет. Обязательна связь «ассет ↔ публикации» и отметка «уже использовался N раз в Reels»: это защищает от повторов b-roll. Шаблоны каруселей по образцу Canva хранятся как бренд-шаблоны с залоченными элементами.

## 8. Архитектура AI content engine 2025–2026

- **Агентные платформы.** Jasper с 2025 года предлагает Agents (более 100 маркетинговых агентов), Canvas как рабочее пространство, content pipelines и слой Jasper IQ. В 2026 году анонсированы Jasper Grid для оркестрации масштабных workflow и поддержка MCP/API ([Built In](https://builtin.com/company/jasper/faq/innovation-technology-agility), [Jasper pipelines](https://www.jasper.ai/content-pipelines)). Typeface Spaces — канвас, где люди и агенты работают вместе. Copy.ai Workflows собираются из готовых Actions ([eesel](https://www.eesel.ai/blog/copy-ai)).
- **n8n-пайплайны.** Типовые шаблоны: идеи из таблицы → сценарий от LLM, разбитый на сцены (хук, удержание, CTA) → генерация изображений, видео и озвучки → сборка (например, Creatomate) → публикация на 5+ платформ, статус ведётся в таблице ([n8n workflow 8404](https://n8n.io/workflows/8404-automate-ai-video-creation-and-multi-platform-publishing-with-gemini-and-creatomate/), [growwstacks](https://growwstacks.com/case-studies/apps/automate-ai-viral-video-creation-multi-platform-publishing)).
- **kie.ai как агрегатор.** Работа асинхронная через task: можно опрашивать статус (pending / processing / completed / failed) или передать callback URL, на который придёт POST с результатом. Nano Banana стоит около $0.02 за изображение, Veo 3 Fast — примерно 20% от цены Quality, отдельный эндпоинт выдаёт 1080p-версию ([kie-ai MCP README](https://github.com/andrewlwn77/kie-ai-mcp-server), [breakingac](https://breakingac.com/news/2025/sep/23/evaluating-kieais-nano-banana-api-fast-affordable-ai-image-generation-solution/)). **[Цены меняются, сверять с прайсом kie.ai.]**
- **LLM-as-judge.** Отдельная модель оценивает выход по рубрике: конкретные критерии, описание каждого уровня оценки и примеры, единая шкала, связь с реальными метриками. Типовые критерии бренда: тон, терминология, соответствие аудитории, личность бренда ([Adaline](https://www.adaline.ai/docs/evaluate/llm-as-a-judge), [DigitalOcean](https://www.digitalocean.com/resources/articles/llm-as-a-judge), [respan](https://respan.ai/resources/llm-evaluation-content-generation)).
- **Гардрейлы для APEC:** запрет гарантий («100% одобрение»), юридическая точность (сроки и условия карты APEC и 90 дней в Таиланде — только из базы знаний CRM), стоп-слова и термины по образцу Writer Terms, проверка соответствия ступени лестницы, визуальная проверка (лица спикеров, логотип).

**Рекомендуемый контур:** Кабинет (UI + БД) → событие «тема утверждена» → n8n → Claude (хуки и сценарий с контекстным пакетом бренда) → Claude-judge (оценка и порог) → человек (ворота 2 и 3) → n8n → kie.ai (изображения и видео, callback) → медиатека → публикация или ChatPlace/Telegram → сбор метрик → CRM-атрибуция.

---

## Рекомендуемая модель данных

**Стратегический слой (версионируемый)**
- `BrandPlatform` (version, valid_from, status: draft/active/archived) — positioning, mission (кому / что / результат), tilt, values[].
- `Persona` — name, JTBD (situation / motivation / outcome), pains[], objections[], triggers[]; FK → BrandPlatform.
- `MessageHouse` → `MessagePillar` (title, description) → `ProofPoint` (type: data/case/quote/review, text, source_url, kb_entry_id → CRM).
- `VoiceProfile` — tone scales, do[] / dont[], reference_examples[]; `StyleRule`; `Term` (approved / pending / banned, replacement).
- `Product` — синхронизируется из CRM (услуга, цена, сроки, условия).

**Матрица**
- `AwarenessStage` (5 фиксированных значений).
- `MatrixCell` (stage × persona × pillar) — angles[], hooks_bank[], triggers[], recommended_formats[], proof_points[]; метрики покрытия и эффективности.
- `MarketInsight` / `SalesBookEntry` — источник, текст; M:N с MatrixCell.

**Производство**
- `Campaign` (тема периода / цель, даты, бюджет, utm_campaign).
- `Period` (неделя/спринт) → `PlanApproval`.
- `ContentItem` (идея / тема) — FK MatrixCell, Campaign, Period; status: idea → topic_approved → hooks_approved → script_approved → in_production → ready → published → measured; brand_platform_version.
- `Hook` / `Thesis` — варианты, selected flag, judge_score.
- `Script` / `Draft` — версии (version_no, body, author: human/AI, model, prompt_id).
- `Publication` — FK ContentItem + Channel + (Author); format (reels / carousel / post / article / longread / ad), scheduled_at, published_url, utm-набор, promo_code, status.
- `Approval` — object_type/object_id, gate (1/2/3/asset), approver, decision, comment, created_at.
- `JudgeEvaluation` — object, rubric_id, scores{criterion: score}, verdict, rationale, model.
- `Task` (шаблонные шаги продакшна: съёмка, монтаж, обложка).

**Каналы и аналитика**
- `Channel` — type (Paid/Earned/Shared/Owned), platform, account_id (FK → Integration), status (active/paused/absent), target_frequency.
- `MetricSnapshot` — publication_id или channel_id, date, reach, views, er, clicks, leads, payments, revenue, spend.
- `Attribution` — CRM lead/payment ↔ publication / author / campaign (через UTM, промокод, кодовое слово ChatPlace, реф-код), model.

**Креаторы**
- `Creator` (type: speaker / ambassador / employee; ref_code, payout_terms, channels[]).
- `CreatorBrief` (→ Campaign / ContentItem, deliverables, deadline) → `Submission` (url / файл, status, Approval).
- `Payout` (период, сумма, основание — оплаты в CRM).

**Медиа**
- `Asset` — kind, source (shoot / kie / stock / upload), storage_url, tags[], location, speaker, rights, expires_at, parent_asset_id, version.
- `GenerationJob` — provider (kie.ai), model (veo3 / nano-banana / …), prompt, params, seed, task_id, status, cost, result_asset_id.
- `AssetUsage` (asset ↔ publication).
- `Template` (тип карусели или обложки, залоченные элементы).

**Система**
- `Integration` (Instagram, Telegram, YouTube, Дзен, vc.ru, CRM, ChatPlace, kie.ai, n8n, GA4/Метрика — статус токена, последний sync).
- `Rubric`, `PromptTemplate` (версии), `User` / `Role` (owner, editor, speaker, ambassador, reviewer).

**Ключевые связи:** BrandPlatform 1—N Persona / Pillar → MatrixCell N—1 → ContentItem 1—N Hook / Script / Publication; Publication N—M Asset; Publication 1—N MetricSnapshot; Publication / Creator → Attribution → CRM.

## Рекомендуемая информационная архитектура

Левое меню сверху вниз, по иерархии пользователя:

1. **Стратегия.** Вкладки: Позиционирование и миссия · Персоны/JTBD · Message house (крыша → опоры → доказательства) · Голос и стайлгайд (шкалы, do/don't, термины) · Продукт (read-only из CRM) · История версий. Кнопка «Пересмотреть в диалоге» открывает чат с Claude, на выходе получается diff новой версии. Ежемесячное напоминание.
2. **Пульс.** Карта каналов PESO (плитки: есть / нет / пауза, светофор) · сводка за 7/30 дней: публикации, план и факт, охват, заявки, оплаты, выручка · воронка контент → заявка → оплата · топ публикаций и хуков · аномалии.
3. **Матрица.** Сетка «ступень × персона» с фильтром по пиллару, цвет ячейки показывает покрытие или эффективность. Карточка ячейки: углы, триггеры, банк хуков, доказательства, связанные публикации и их метрики. Вкладки «Рынок» и «Книга продаж».
4. **Производство.** Подразделы-ворота: *План периода* (пакетное утверждение тем) → *Хуки и тезисы* (выбор вариантов, оценки судьи) → *Сценарии* (редактор с версиями, превью по каналам) → *Продакшн* (канбан задач и генераций) → *Календарь* (виды календарь / лента-превью / таблица). Боковая панель карточки: ячейка матрицы, судья, согласования, ассеты, UTM.
5. **Креаторы.** Для команды: список креаторов, брифы, сдачи на ревью, лидерборд, выплаты. Для креатора — отдельный вход: «Готово к публикации», «Мои задания», «Мои ссылки и коды», «Моя статистика».
6. **Медиа-студия.** Библиотека (фильтры по тегам, сохранённые коллекции, «где использовано») · Генерация (изображение / видео / карусель по шаблону, очередь задач kie.ai со статусами и стоимостью) · Шаблоны и бренд-кит.
7. **Настройки** (внизу). Подключённые аккаунты и API, статусы токенов · UTM-словарь · рубрики судьи и пороги · промпт-шаблоны · роли и маршруты согласования · n8n-вебхуки.

**Сквозные элементы:** глобальный поиск по контенту и ассетам, inbox «ждёт моего решения» (по образцу дашборда согласований CoSchedule), лента активности, бейдж версии бренд-платформы на каждой карточке.
