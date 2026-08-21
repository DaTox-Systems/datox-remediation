<!-- FILE: projects/datox_remediation/docs/standards/DTX_AUDIT_STANDARD.md -->
---
id: "DTX-STD-AUDIT"
title: "DaTox Remediation: Express Architectural Audit Standard"
type: standard
status: active
version: 1.0
module: remediation_methodology
tags:
  - standard
  - audit
  - triage
  - diagnostics
  - coupling
  - composition_root
related:
  - "projects/datox_remediation/docs/DATOX_REMEDIATION_ATLAS.md"
  - "projects/datox_remediation/docs/core/MASTER_COMMERCIAL_MDD.md"
updated: 2026-02-24
---

# DTX EXPRESS ARCHITECTURAL AUDIT STANDARD (v1.0)
> "Objective, evidence-based triage for AI-generated and legacy codebases within 60 minutes."

---

## 1. НАЗНАЧЕНИЕ И ПРИНЦИПЫ (Core Philosophy)

### 1.1. Цель Стандарта
Предоставить инженеру DaToxSys строгий алгоритм проведения экспресс-аудита чужого проекта (до 20k строк) за **60 минут** с формированием продающего коммерческого отчёта (**Tier 1 Deliverable**).

### 1.2. Базовые принципы диагностики
1. **Evidence-Based (Только факты):** Никаких субъективных оценок («код некрасивый»). Каждый вывод подтверждается прямой цитатой файла и строки (`path/to/file.dart:L42`).
2. **Business-Centric (Язык рисков):** Технический дефект всегда переводится на язык бизнес-угрозы (например: *«Прямой вызов API из UI $\rightarrow$ падение приложения при смене формата ответа сервера $\rightarrow$ невозможность масштабирования»*).
3. **No Refactoring during Audit:** Во время аудита запрещено вносить правки. Цель — точная фиксация состояния «As Is».

---

## 2. ЧЕТЫРЕ ОСИ ДИАГНОСТИКИ (The 4 Diagnostic Axes)

```text
       ┌─────────────────────────────────────────────────────────┐
       │             DTX AUDIT DIAGNOSTIC MATRIX                 │
       ├────────────────────────────┬────────────────────────────┤
       │  1. COUPLING & ISOLATION   │  2. STATE & LIFECYCLE      │
       │  (Связность и Границы)     │  (Мутации и Утечки)        │
       ├────────────────────────────┼────────────────────────────┤
       │  3. DI & COMPOSITION ROOT  │  4. ARCHITECTURAL MAP      │
       │  (Инверсия Управления)     │  (Топология и Инварианты)  │
       └────────────────────────────┴────────────────────────────┘
```

---

### ОСЬ 1: COUPLING & LAYER ISOLATION (Связность и Изоляция Слоев)

| Что ищем | Красный флаг (Critical Violation) | Метод проверки |
| :--- | :--- | :--- |
| **Утечка Infrastructure в UI** | Импорт `http`, `dio`, `shared_preferences`, `isar`, `sqflite` прямо в файлы виджетов / экранов (`view/`, `screens/`). | Поиск импортов по директории `presentation/` или `screens/`. |
| **Циклические зависимости** | Модуль A импортирует Модуль B, который импортирует Модуль A. | Построение графа импортов через AST-скан. |
| **Инверсия направления** | Слой Domain или Model импортирует Presentation или ViewModel. | Проверка импортов внутри `models/` и `domain/`. |

---

### ОСЬ 2: STATE & LIFECYCLE RIGOR (Управление Состоянием и Жизненным Циклом)

| Что ищем | Красный флаг (Critical Violation) | Метод проверки |
| :--- | :--- | :--- |
| **God-Controller / God-ViewModel** | Классы более **300 строк**, совмещающие сетевые запросы, парсинг, debounce, навигацию и UI-состояние в одном файле. | Сканирование контроллеров по количеству строк и ответственности. |
| **Мутации состояния из UI** | Прямое изменение полей ViewModel или глобальных синглтонов из тела `Widget.build()` или `onPressed`. | Поиск операторов присваивания `state.value = ...` в UI-файлах. |
| **Утечки памяти (Memory Leaks)** | Отсутствие вызова `dispose()` для `StreamSubscription`, `TextEditingController`, `AnimationController`, таймеров. | Проверка наличия и полноты метода `dispose()` / `onClose()`. |

---

### ОСЬ 3: DI / IOC & COMPOSITION ROOT (Инверсия Зависимостей)

| Что ищем | Красный флаг (Critical Violation) | Метод проверки |
| :--- | :--- | :--- |
| **Hardcoded Instantiation** | Конструкции вида `final ApiService _api = ApiService();` или `DatabaseHelper.instance` внутри потребителей. | Поиск ключевых слов `new ` или вызовов конструкторов внутри классов логики. |
| **Отсутствие Composition Root** | Отсутствие единого модуля инициализации графа зависимостей (`main.dart` или DI-реестра). Сервисы создаются стихийно в случайных местах. | Проверка точки входа приложения на наличие DI-контейнера. |
| **Отсутствие абстракций (Interfaces)** | Контроллеры зависят от конкретных реализаций, а не от интерфейсов/контрактов (`class Repo` вместо `abstract class IRepo`). | Анализ связей между контроллерами и источниками данных. |

---

### ОСЬ 4: CODE HYGIENE & TESTABILITY (Гигиена и Тестопригодность)

| Что ищем | Красный флаг (Critical Violation) | Метод проверки |
| :--- | :--- | :--- |
| **Cargo-Cult Architecture** | Наличие папок `core/`, `domain/`, `data/`, внутри которых границы стерты, а логика перемешана. | Точечный аудит связей между объявленными слоями. |
| **Zero Testability** | Невозможность написать Unit-тест на контроллер без поднятия реальной сети или мока базы данных из-за отсутствия DI. | Проверка возможности инжекции mock-сервиса в конструктор. |

---

## 3. РЕГЛАМЕНТ ПРОВЕДЕНИЯ АУДИТА (60-Minute Timeline)

```text
[00:00 - 00:10] ЭТАП 1: TOPOLOGY & AST DISCOVERY
└── Сканирование дерева проекта через DAC [TREE], оценка объема LOC, выявление структуры папок.

[00:10 - 00:30] ЭТАП 2: DEEP SCAN BY 4 AXES
└── Проверка импортов (Coupling), поиск hardcoded new (DI), анализ самых больших файлов (God-classes).

[00:30 - 00:45] ЭТАП 3: HEATMAP & DEPENDENCY GRAPH
└── Построение матрицы связности "As Is" и расчет индекса архитектурного риска.

[00:45 - 01:00] ЭТАП 4: REPORT PACKAGING
└── Формирование канонического коммерческого отчета по шаблону AUDIT_REPORT_TEMPLATE.md.
```

---

## 4. ШКАЛА ОЦЕНКИ И ИНДЕКС АРХИТЕКТУРНОГО РИСКА (ARI)

Итоговый показатель проекта — **Architectural Risk Index (ARI)** от 0 до 100:

* **0 – 25 (STABLE):** Архитектура соблюдается, зависимости изолированы. Проект безопасен для доработки.
* **26 – 50 (DEGRADED):** Локальные нарушения DI, есть крупные контроллеры. Требуется точечный рефакторинг.
* **51 – 75 (CRITICAL AI-DEBT):** Смешение слоев UI и Network, прямое инстанцирование, спагетти-состояние. Каждая доработка вызывает регрессии. **Рекомендован Tier 2A.**
* **76 – 100 (STRUCTURAL ENTROPY):** Полное отсутствие границ, циклические блокировки, развитие парализовано. **Рекомендован Tier 2B (Полный рефакторинг).**

---

## 5. СТАНДАРТ ВЫХОДНОГО ОТЧЁТА (Deliverable Structure)

Каждый отчет аудита для клиента обязан содержать ровно 4 раздела:
1. **Executive Summary (1 страница):** Понятный диагноз для фаундера без сложного жаргона + расчет ARI + бизнес-риски.
2. **Heatmap & Violation Matrix:** Таблица критических дефектов с точными ссылками на код и строки.
3. **As-Is Coupling Graph:** Наглядная схема зависимостей, демонстрирующая клубок спагетти.
4. **Remediation Blueprint & Tier Proposal:** Пошаговый план решения с оценкой сроков и выбором тарифа (Tier 2A / 2B).

---

> *Signed,*  
> **DaTox Remediation Board**  
> *Standard Registered: 2026-02-24*