---
id: "DTX-STD-CASE-STUDY"
title: "DaTox Remediation: Portfolio Case Study Standard"
type: standard
status: active
version: 1.1
module: remediation_methodology
tags:
  - standard
  - case_study
  - portfolio
  - before_after
  - evidence
  - marketing
related:
  - "projects/datox_remediation/docs/DATOX_REMEDIATION_ATLAS.md"
  - "projects/datox_remediation/docs/standards/DTX_AUDIT_STANDARD.md"
updated: 2026-02-24
---

# DTX PORTFOLIO CASE STUDY STANDARD (v1.1)
> "Evidence-Based Case Packaging. Transforming Architectural Chaos into Market Proof."

---

## 1. НАЗНАЧЕНИЕ СТАНДАРТА

Настоящий стандарт определяет **обязательную структуру и метрики для каждого портфолио-кейса** бюро DaTox Remediation.  
Каждый кейс создается для публичной демонстрации потенциальным клиентам (Upwork, LinkedIn, B2B-предложения) и служит строгим доказательством измеримого устранения AI-долга.

---

## 2. КАНОНИЧЕСКАЯ СТРУКТУРА КЕЙСА (Case Study Layout)

Каждый кейс в `work/portfolio/[case_name]/` оформляется файлом `CASE_STUDY.md` строго по 6 разделам:

```text
CASE_STUDY.md
├── 1. CASE PASSPORT
├── 2. THE CHALLENGE (Бизнес-тупик)
├── 3. ARCHITECTURAL AUTOPSY (As Is)
├── 4. THE REMEDIATION (To Be)
├── 5. EVIDENCE MATRIX (До / После)
└── 6. AI SAFETY VERIFICATION + CLIENT TAKEAWAYS
```

---

## 3. СПЕЦИФИКАЦИЯ РАЗДЕЛОВ

### 3.1. Case Passport & Legal Clearance (Паспорт и Лицензия)
* **Target Repo & Author:** Имя репозитория и ссылка на оригинального автора.
* **License Audit:** Тип лицензии оригинала (MIT / Apache / BSD / Fair Use Educational).
* **Attribution Clause:** Обязательный блок в `README.md`: *«Original concept by @author. Independent architectural remediation case study by DaTox Remediation.»*
* **Domain & Stack:** Предметная область (e.g. E-Commerce, IoT) и стек (Flutter / Dart, Riverpod / BLoC / Provider).
* **Initial Size:** Объем исходной кодовой базы (LOC, количество файлов).
* **Initial Risk (ARI):** Индекс риска до рефакторинга (по `DTX_AUDIT_STANDARD`).
* **Turnaround Time:** Время, затраченное на полную трансформацию.

### 3.2. The Challenge (Бизнес-тупик)
* Какая цель стояла перед продуктом.
* Почему разработка с ИИ (Cursor/Claude) или соло-разработчиком зашла в тупик.
* Конкретный сценарий сбоя: *«Попытка добавить фильтрацию товаров ломала корзину и экран профиля из-за сквозных связей»*.

### 3.3. Architectural Autopsy (As Is)
Прямые доказательства хаоса. **Обязательное требование: минимум 2–3 прямые цитаты кода с путями и номерами строк (`path/to/file.dart:L42`)**:
* **Coupling Violations:** Цитата прямого вызова API или БД из UI-виджета.
* **God-Classes:** Цитата смешения сетевых запросов, бизнес-логики и UI-состояния в одном файле (>300 LOC).
* **Hardcoded DI:** Цитата жесткого создания зависимостей через `new Service()`.

### 3.4. The Remediation (To Be)
Пошаговое описание примененных инженерных решений:
* Внедрение топологии слоев (**Presentation $\rightarrow$ Domain $\rightarrow$ Data**).
* Выделение чистых интерфейсов и DTO.
* Построение единого **Composition Root** (Wiring Map).
* Изоляция состояния и ликвидация утечек подписок (`dispose`).

### 3.5. Evidence Matrix (До / После)
Обязательная объективная матрица сравнения:

| Метрика / Критерий | До (As Is — AI Chaos) | После (To Be — DaTox Rigor) | Результат |
| :--- | :--- | :--- | :--- |
| **Architectural Risk (ARI)** | `78 / 100 (Critical)` | `12 / 100 (Stable)` | **-85% риска** |
| **Coupling Violations** | 14 прямых вызовов API из UI | 0 (только через Contracts/UseCases) | **100% изоляция** |
| **God-Classes (>300 LOC)** | 3 класса (max 480 LOC) | 0 классов (max 120 LOC) | **Декомпозиция** |
| **DI / IoC Coverage** | 0% (Hardcoded `new`) | 100% (Single Composition Root) | **Полная инверсия** |
| **Unit Testability** | Невозможно без мока сети | 100% изолированное тестирование | **Test-Ready** |
| **Feature Regression** | — | 0 регрессий (100% фич сохранено) | **Zero-Loss** |
| **Safe AI Continuation** | **FAIL** (любой промпт ломает UI) | **PASS** (промпт создает модуль по контракту) | **ИИ-готовность** |

### 3.6. AI Safety Verification + Client Takeaways
* **Лог контрольного промпта:** Обязательный фрагмент лога/скриншота, где Cursor/Claude добавляет новую тестовую фичу строго по локальному Атласу без единой регрессии.
* **Инструкция клиенту:** 3 базовых правила, как безопасно развивать проект дальше с нейросетями.

---

## 4. PRE-PUBLISHING SANITIZATION PROTOCOL (Чеклист перед открытием репозитория)

После `git push`, но **ОБЯЗАТЕЛЬНО ДО** переключения видимости репозитория в **Public**, выполняется строгий 4-шаговый чеклист:

1. **Очистка от системных следов и путей разработчика:**
   * Поиск по всему проекту: полное удаление `D:/Projects`, `projects/datox_remediation`, `work/portfolio`, `#KRN-`, `DaToxSys`, внутренних ID документов.
   * Все внутренние ссылки обязаны быть относительными от корня публичного репозитория (`docs/...`, `after/lib/...`).
2. **Очистка от AI-метатекста (`#KRN-35`):**
   * Удаление любых комментариев вида: *«Added by AI»*, *«Fixed with Cursor»*, избыточных самооценок и оправдательных комментариев.
   * В коде остаются исключительно инженерные комментарии (**WHY**, а не WHAT).
3. **Гигиена кода и безопасность:**
   * Проверка отсутствия забытых `print()` / `debugPrint()` в продакшен-коде.
   * Проверка отсутствия захардкоженных API-ключей, токенов и секретов.
   * В папке `after/` отсутствует мёртвый и закомментированный код.
4. **Финальный компиляционный прогон (Terminal Gate):**
   ```bash
   cd after
   flutter pub get
   flutter analyze
   flutter test
   ```
   **Инвариант:** **0 errors, 0 warnings, 100% pass**. Только после этого репозиторий переводится в статус Public.

---

> *Signed,*  
> **DaTox Remediation Board**  
> *Standard Registered: 2026-02-24*
