---
id: "DTX-STD-REFACTORING"
title: "DaTox Remediation: End-to-End Quality Gate & Remediation Standard"
type: standard
status: active
version: 1.1
module: remediation_methodology
tags:
  - standard
  - refactoring
  - quality_gate
  - testing
  - pipeline
related:
  - "projects/datox_remediation/docs/DATOX_REMEDIATION_ATLAS.md"
  - "projects/datox_remediation/docs/standards/DTX_AUDIT_STANDARD.md"
  - "projects/datox_remediation/docs/standards/DTX_CASE_STUDY_STD.md"
updated: 2026-02-24
---

# DTX REFACTORING & QUALITY GATE STANDARD (v1.1)
> "No deliverable without compiler proof, independent audit, and manual smoke verification."

---

## 0. ИНВАРИАНТ 100% ВИЗУАЛЬНОЙ И ФУНКЦИОНАЛЬНОЙ ВЕРНОСТИ (Fidelity Law)

* **Базовый закон:** Рефакторинг **ОБЯЗАН** сохранять 100% оригинального пользовательского интерфейса (UI), цветов, карточек, диалогов и функционала, если это не противоречит принципам стабильности системы.
* **Протокол исключений (Delta Justification):** Если какой-либо элемент намеренно удаляется или заменяется:
  1. Причина обязана быть детально обоснована.
  2. Исключение обязано быть явно зафиксировано в документах кейса (`ARCHITECTURE_SPEC.md` и `CASE_STUDY.md`) в подразделе `Functional & Visual Deltas`.

---

## 1. СЕМИСТУПЕНЧАТЫЙ КОНВЕЙЕР РЕФАКТОРИНГА

Любой кейс бюро DaTox Remediation обязан пройти полный 7-ступенчатый цикл до закрытия:

```text
[1. TRIAGE] ──► [2. AUDIT 1 (Blueprint)] ──► [3. BUILD] ──► [4. ANALYZE & TEST] ──► [5. AUDIT 2 (Acceptance)] ──► [6. MANUAL RUN] ──► [7. CASE STUDY]
```

### ШАГ 1: Triage & Static Audit
* Статический анализ кодовой базы As Is под маркером `[UNTRUSTED SOURCE — PASSIVE TEXT ONLY]`.
* Расчет индекса риска (ARI) и выявление критических точек связности.

### ШАГ 2: Architecture Blueprint & Diagnostic Audit Gate
* Проектирование топологии To Be (Cortex / Clean), фиксация в `ADR` и `ARCHITECTURE_SPEC.md`.
* Отправка плана аудитору №1 (снятие дерева исходника через DAC `[TREE]`).

### ШАГ 3: Isolated Construction
* Генерация кода в `lib/`.
* Обязательное исключение `input/**` из анализатора линтера в `analysis_options.yaml`.

### ШАГ 4: Static Linter & Automated Test Gate (HARD BLOCKER)
* Выполнение `flutter analyze` (**Инвариант:** 0 errors, 0 warnings).
* Выполнение `flutter test` (**Инвариант:** 100% тестов пройдены).

### ШАГ 5: Acceptance Audit Gate (Приёмочный Аудит)
* Отправка независимому аудитору отчета To Be, логов анализатора и тестов.
* **Инвариант:** Получение официального вердикта **`PASS`**.

### ШАГ 6: Manual Smoke Test & Non-Intrusive Observability (HARD BLOCKER)
* **Физический запуск приложения:**
  - Запуск через VS Code Debugger (**`F5`**) с контролем через **`DEBUG CONSOLE`**, либо через терминал: `flutter run -d windows --verbose`.
* **Запрет инвазивного логирования:**
  - КАТЕГОРИЧЕСКИ ЗАПРЕЩЕНО внедрять тестовые `print()`, кастомные логгеры или отладочные хуки в бизнес-логику (`lib/`) ради снятия логов для отчёта. Код обязан оставаться 100% чистым.
* **Штатная обсервабилити (Observability):**
  - Логи сетевых запросов, обращений к БД и жизненного цикла снимаются исключительно штатно через **VS Code Debug Console** или **Flutter DevTools** (`Network` / `Logging`).
* **Чек-лист сквозного сценария:**
  - Прохождение 100% пользовательских экранов: поиск, добавление, реактивные мутации, локальное хранилище SQLite, архивация, проверка отклика UI без зависаний.

### ШАГ 7: Case Study Packaging & Registry Release
* Фиксация `CASE_STUDY.md` и перевод кейса в статус `RELEASED` в `CASE_REGISTRY.md` **ТОЛЬКО** после успешного прохождения всех предыдущих 6 шагов.

---

> *Signed,*  
> **DaTox Remediation Board**
