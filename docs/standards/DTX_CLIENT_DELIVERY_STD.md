---
title: "DaTox Remediation: Commercial Client Delivery & Handover Standard"
type: standard
status: active
version: 1.0
module: commercial_delivery
tags:
  - standard
  - client_delivery
  - nda
  - handover
  - quality_gate
related:
  - "docs/DATOX_REMEDIATION_ATLAS.md"
  - "docs/core/MASTER_COMMERCIAL_MDD.md"
  - "docs/standards/DTX_REFACTORING_STD.md"
updated: 2026-02-24
---

# DTX COMMERCIAL CLIENT DELIVERY STANDARD (v1.0)
> "From Customer Codebase to Production-Grade Handover. Zero Leak, 100% Quality Gate."

---

## 1. СТРУКТУРА КЛИЕНТСКОЙ КАПСУЛЫ (`work/client_cases/`)

Каждый платный заказ ведётся в строго изолированной рабочей капсуле:

```text
work/client_cases/[client_company_name]/
├── docs/                                  # 📄 ПАКЕТ СДАЧИ КЛИЕНТУ
│   ├── DATOX_SYSTEM_ATLAS.md              # Навигационный паспорт для команды заказчика
│   ├── AUDIT_REPORT.md                    # Исходный диагноз (As-Is) и обоснование работ
│   └── HANDOVER_GUIDE.md                  # Руководство: правила безопасного развития кода с ИИ/командой
├── input/                                 # 🔒 ИСХОДНИК КЛИЕНТА (Под защитой #KRN-41)
├── lib/ + test/                           # 🛠️ ОЧИЩЕННЫЙ РЕПОЗИТОРИЙ ЗАКАЗЧИКА
├── analysis_options.yaml
└── pubspec.yaml
```

---

## 2. ИНВАРИАНТЫ РАБОТЫ С ЗАКАЗЧИКОМ (Client Invariants)

1. **NDA & Zero-Leak Invariant (Абсолютная изоляция):**
   * Код заказчика **КАТЕГОРИЧЕСКИ ЗАПРЕЩЕНО** публиковать на открытом GitHub.
   * Сдача проекта производится либо передачей приватного архива, либо прямым Pull Request в закрытый репозиторий заказчика.
2. **Обязательный 7-ступенчатый Quality Gate:**
   * Проект сдаётся **ТОЛЬКО** после прохождения `flutter analyze` (**0 errors, 0 warnings**), 100% зелёных unit-тестов и ручного прогона (Manual Smoke).
3. **Пакет передачи (The Handover Package):**
   * Клиент получает не просто «починенный код», а **систему с защитой**:
     * Очищенный модульный код.
     * Локальный Атлас (`docs/DATOX_SYSTEM_ATLAS.md`), обучающий следующего разработчика или нейросеть клиента архитектурным границам.
     * `HANDOVER_GUIDE.md` с тремя правилами поддержки.
4. **Гарантия Zero-Regression:**
   * 100% сохранение существующего бизнес-функционала и UI заказчика.

---

> *Signed,*  
> **DaTox Remediation Board**  
> *Standard Registered: 2026-02-24*
