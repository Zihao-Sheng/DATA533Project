# HouseHoldBudget Package 使用说明书（中文版，目前为了方便开发，暂时使用中文，开发完成上交时将翻译成英文）

**版本：1.0**  
**作者：负责 `budgetfund` / `member` / `BudgetSystem` 部分的组员**

---

## 1. 项目简介

**HouseHoldBudget** 是一个用于家庭预算管理的 Python 包（package）。

本系统主要实现以下功能：

- 家庭基金（fund）的管理：包括余额、增减操作与日志记录  
- 家庭成员（guardian / dependant）的信息管理  
- 通过 `BudgetSystem` 对家庭信息、成员、基金进行统一管理  
- 为 `incomes` / `expenses` 子包的扩展预留接口，方便其他组员在此基础上继续开发

本说明书主要面向 **本组其他组员**，用于说明：

- 该 package 的整体结构  
- 各模块与类的功能  
- 如何导入与调用当前已实现的功能  
- incomes / expenses 子包应如何与现有结构对接  

---

## 2. 包目录结构

当前项目的主要目录结构如下（只列出与本说明书相关的部分）：

```text
HouseHoldBudget/
└── budget_system/
    ├── __init__.py
    ├── budget_system.py              ← 主控类 BudgetSystem 所在文件
    │
    ├── budgetfund/
    │   ├── __init__.py
    │   ├── budgetfund.py             ← 家庭基金类 budgetfund
    │   └── fund_utils.py             ← 基金日志相关工具函数
    │
    ├── member/
    │   ├── __init__.py
    │   ├── member.py                 ← 基类 member
    │   └── member_type.py            ← 子类 guardian / dependant
    │
    ├── incomes/                      ← 预留扩展（目前为空）
    └── expenses/                     ← 预留扩展（目前为空）
