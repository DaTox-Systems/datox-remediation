---
id: "DTX-REMEDIATION-CLIENT-PIPELINE"
title: "DaTox Remediation: Upwork Search Playbook & Client Pipeline"
type: product_spec
status: active
version: 1.0
module: commercial_pipeline
tags:
  - upwork
  - lead_generation
  - search_queries
  - sales_funnel
  - proposal_templates
related:
  - "projects/datox_remediation/docs/DATOX_REMEDIATION_ATLAS.md"
  - "projects/datox_remediation/docs/core/MASTER_COMMERCIAL_MDD.md"
  - "projects/datox_remediation/docs/product/CASE_REGISTRY.md"
updated: 2026-02-24
---

# UPWORK SEARCH PLAYBOOK & CLIENT PIPELINE (v1.0)
> "Systematic Lead Generation. From Targeted Search Queries to $950 Audit Conversion."

---

## 1. ПОИСКОВЫЕ ЗАПРОСЫ НА UPWORK (Search Query Matrix)

При поиске заказов на Upwork ИИ и Партнёр используют следующие проверенные запросы:

### 1.1. Базовые ключевые запросы (Перебирать по очереди)
* `Flutter offline`
* `Flutter sync`
* `Flutter data sync`
* `Flutter local database`
* `Flutter SQLite` / `Flutter Hive` / `Flutter Isar`
* `Flutter refactoring`
* `Flutter technical debt`
* `Flutter code cleanup`
* `Flutter architecture`
* `Flutter bug fix data`
* `Flutter offline first`

### 1.2. Высокоточные комбинации (Boolean Search)
* `Flutter "offline"`
* `Flutter "sync" OR "synchronization"`
* `Flutter "local database" OR Hive OR Isar OR SQLite`
* `Flutter refactor OR cleanup OR "technical debt"`
* `"existing Flutter" refactor`
* `"Flutter app" "data" (bug OR issue OR problem OR fix)`
* `Flutter "state management" (spaghetti OR messy OR refactor)`
* `Flutter "Cursor" OR "AI generated" OR "ChatGPT"`

### 1.3. Нишевые высокобюджетные запросы
* `Flutter Firebase offline`
* `Flutter conflict resolution`
* `Flutter production bug`

---

## 2. НАСТРОЙКИ ФИЛЬТРОВ UPWORK (Search Filters)

* **Experience Level:** `Intermediate` + `Expert` *(отсекает копеечные студенческие задачи)*.
* **Job Type:** И `Hourly` ($40–$75+/час), и `Fixed-Price` ($500 – $5,000).
* **Client History:** Предпочтительно клиенты с историей оплат (*Payment Verified, Total Spent > $1k*), но на старте можно откликаться и на свежих клиентов с чётким ТЗ.
* **Date Posted:** `Last 24 hours` – `Last 7 days` *(максимальный отклик в первые 2–4 часа после публикации)*.

---

## 3. КРИТЕРИИ КВАЛИФИКАЦИИ ЛИДА (Подходит / Не подходит)

| Признак идеального клиента (Наш лид) | Красный флаг (Пропускаем) |
| :--- | :--- |
| Есть работающий проект, но добавление фич вызывает баги | Просят "сделать клон Uber за $100" с нуля |
| В описании: "code is messy", "need refactoring", "AI generated" | Непонятное ТЗ в одну строчку без доступа к коду |
| Клиент понимает ценность архитектуры и ищет качество | Ищут самого дешевого кодера ради экономии $5 |
| Стек: Flutter, Provider / BLoC / SQLite / REST API | Стек не определён, хотят "на всём сразу" |

---

## 4. ШАБЛОН ОТКЛИКА НА UPWORK (Proposal Template)

```text
Hi [Client Name / there],

I read your description regarding [кратко назвать их проблему, например: unexpected bugs when adding new features to your Flutter app]. 

This is a classic symptom of Architectural Debt and UI-state coupling (often seen in rapidly-built or AI-assisted codebases where services are directly instantiated inside widgets, causing cascading regressions).

We specialize specifically in Architectural Remediation and Code Stabilization for Flutter apps:
1. We isolate your layers (Data -> Domain -> Presentation) so changing one screen never breaks another.
2. We eliminate BuildContext and state leaks that trigger asynchronous crashes.
3. We introduce 100% Dependency Injection and automated Unit Tests.

Here is a live open-source showcase of how we reduced Architectural Risk by 87% (ARI 83.5 -> 11.0) on a real Flutter codebase:
👉 https://github.com/DaTox-Systems/case-01-flutter-ai-market-list

I can perform an Express Architectural Audit (48h) on your codebase to provide an objective risk heatmap and a step-by-step remediation blueprint.

Let's discuss your project details.

Best regards,
KizTul / DaTox Remediation
```

---

## 5. ВОРОНКА СДЕЛКИ (Conversion Funnel)

```text
[Отклик по фильтрам Upwork с ссылкой на Case 01]
                       │
                       ▼
[15-минутный чат / диалог: "Давайте начнем с Аудита за $950"]
                       │
                       ▼
[ЭТАП 1: Оплачиваемый Express Audit ($950, 48 часов)]
   └── Выдача клиенту подробного AUDIT_REPORT.md с картой дефектов.
                       │
                       ▼
[ЭТАП 2: Конверсия в Full Remediation ($3,200 – $5,500)]
   └── 4 из 10 клиентов просят устранить найденные дефекты "под ключ".
```

---

> *Signed,*  
> **DaTox Remediation Board**  
> *Pipeline Playbook Registered: 2026-02-24*
