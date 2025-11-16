# HouseHoldBudget Package — 全部可调用类别与函数总表

以下列表汇总了当前 package 中所有可调用的 **类（Classes）** 与 **方法/函数（Methods / Functions）**，按模块结构清晰分组，便于组员查阅和使用。

---

# 1. BudgetSystem（主控模块）

## Class: `BudgetSystem`

| 方法名 | 参数 | 功能说明 |
|--------|------|-----------|
| `__init__(members, current_fund, address, household_name='')` | 成员列表、初始基金、地址、家庭名称 | 初始化整个系统 |
| `add_member(new_member)` | 成员对象 | 添加一个成员 |
| `remove_member(ID)` | 成员 ID | 删除成员（根据 ID 匹配） |
| `list_member()` | 无 | 打印所有成员信息 |
| **`add_fund(amount, description='')`** | 金额、描述 | 增加家庭基金 |
| **`sub_fund(amount, description='')`** | 金额、描述 | 减少家庭基金 |
| **`validate_fund(amount=0)`** | 金额 | 检查余额是否足够 |
| **`print_fund_log()`** | 无 | 打印所有基金日志 |
| **`search_fund_log(keyword)`** | 字符串 | 搜索 description 中包含关键字 |
| **`filter_fund_status(status)`** | True/False | 筛选成功/失败日志 |
| `add_income(...)`（预留） | incomes 子包扩展 | 收入模块接口 |
| `add_expense(...)`（预留） | expenses 子包扩展 | 支出模块接口 |

---

# 2. budgetfund 子包（家庭基金模块）

## Class: `budgetfund`

| 方法名 | 参数 | 功能说明 |
|---------|-------|-----------|
| `__init__(opening_balance, name='')` | 初始金额、家庭名称 | 初始化基金池 |
| `validate(amount=0)` | 金额 | 检查余额是否足够 |
| `add(amount, description='')` | 金额、描述 | 增加余额并记录成功日志 |
| `sub(amount, description='')` | 金额、描述 | 减少余额，不足则记录失败日志 |
| `get()` | 无 | 返回当前余额 |
| `get_log()` | 无 | 返回 `[log_title, log_rows]` |
| `__str__()` | 无 | 返回基金信息字符串 |

---

## Module: `fund_utils.py`

（以下函数已在 BudgetSystem 内被封装成方法）

| 函数名 | 参数 | 功能说明 |
|--------|-------|-----------|
| `print_log(budgetfund_obj)` | budgetfund 对象 | 打印所有日志 |
| `search_log(budgetfund_obj, keyword)` | budgetfund 对象、关键字 | 搜索 description 字段 |
| `filter_status(budgetfund_obj, status)` | budgetfund 对象、True/False | 返回成功或失败的记录 |

---

# 3. member 子包（成员模块）

## Class: `member`（基类）

| 方法名 | 参数 | 功能说明 |
|---------|-------|-----------|
| `__init__(name, ID, DOB='')` | 姓名、ID、出生日期 | 初始化成员 |
| `new_name(new_name)` | 字符串 | 更新姓名 |
| `new_DOB(new_DOB)` | 字符串 | 更新 DOB |
| `new_ID(new_ID)` | 字符串 | 更新成员 ID |

---

## Class: `guardian(member)`（继承自 member）

| 方法名 | 参数 | 功能说明 |
|---------|-------|-----------|
| `__init__(name, ID, DOB, income, job_title='')` | 成员基础属性 + 收入/职业 | 创建监护人 |
| `new_job(job)` | 字符串 | 更新职业 |
| `new_income(income)` | 数值 | 更新收入 |
| `get_income()` | 无 | 返回收入 |
| `__str__()` | 无 | 返回成员信息 |

---

## Class: `dependant(member)`（继承自 member）

| 方法名 | 参数 | 功能说明 |
|---------|-------|-----------|
| `__init__(name, ID, DOB)` | 基类属性 | 初始化被抚养人 |
| `__str__()` | 无 | 返回成员信息 |

---

# 4. Package 可调用接口总览（快速参考）

```text
BudgetSystem
├── add_member
├── remove_member
├── list_member
├── add_fund
├── sub_fund
├── validate_fund
├── print_fund_log
├── search_fund_log
├── filter_fund_status
├── add_income (预留)
└── add_expense (预留)

budgetfund
├── validate
├── add
├── sub
├── get
├── get_log
└── __str__

fund_utils
├── print_log
├── search_log
└── filter_status

member
├── new_name
├── new_DOB
└── new_ID

guardian
├── new_job
├── new_income
├── get_income
└── __str__

dependant
└── __str__
