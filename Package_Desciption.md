## 3. 模块与类功能说明

### 3.1 `budgetfund` 子包

#### 3.1.1 `budgetfund.py`：`budgetfund` 类

`budgetfund` 用于表示和管理家庭整体资金池，主要职责包括：

- 保存当前家庭基金余额  
- 执行资金的增加/减少操作  
- 检查余额是否充足  
- 记录资金变动日志（log），便于后续查询和分析  

**主要属性：**

- `opening_balance`：初始余额  
- `__balance`：当前余额（私有）  
- `household_name`：家庭名称  
- `log_title`：日志字段标题，例如  
  `['action', 'amount', 'description', 'balance', 'status']`
- `log`：日志记录列表，每条记录为 `[action, amount, description, new_balance, status]`

**主要方法：**

| 方法名                      | 功能说明                                                   |
|-----------------------------|------------------------------------------------------------|
| `validate(amount=0)`        | 判断当前余额是否足够                                       |
| `add(amount, description)`  | 增加余额并记录日志                                         |
| `sub(amount, description)`  | 减少余额，不足则记录失败                                   |
| `get()`                     | 返回当前余额                                               |
| `get_log()`                 | 返回 `[log_title, log]`                                   |
| `__str__()`                 | 返回基金及家庭名称的字符串描述                             |

---

### 3.1.2 `fund_utils.py`：基金日志工具函数

提供日志打印与查询功能，便于组员查看资金流动。

| 函数名                                  | 功能说明                                                   |
|-----------------------------------------|------------------------------------------------------------|
| `print_log(budgetfund_obj)`             | 打印基金的全部日志记录                                     |
| `search_log(budgetfund_obj, keyword)`   | 按关键字搜索 description 字段                              |
| `filter_status(budgetfund_obj, status)` | 按成功（True）或失败（False）筛选日志记录                 |

`BudgetSystem` 已封装这些函数，无需直接调用。

---

### 3.2 `member` 子包

#### 3.2.1 `member.py`：基类 `member`

**该类提供所有家庭成员的通用结构。**

属性：

- `name`
- `DOB`
- `ID`（主键）

方法：

- `new_name(new_name)`
- `new_DOB(new_DOB)`
- `new_ID(new_ID)`

---

#### 3.2.2 `member_type.py`：继承结构（guardian / dependant）

实现两类成员：

#### **1）guardian(member)**

代表家庭经济承担者。

额外属性：

- `type = 'guardian'`
- `income`
- `job_title`

额外方法：

- `new_job(job)`
- `new_income(income)`
- `get_income()`
- `__str__()` 返回成员详细信息

#### **2）dependant(member)**

代表家庭被抚养者。

额外属性：

- `type = 'dependant'`

方法：

- `__str__()` 返回成员基础信息

---

### 3.3 `budget_system.py`：主控类 `BudgetSystem`

**该类负责整个家庭系统的统一管理，包括：**

- 家庭信息（名称、地址）
- 成员列表
- 家庭基金 `budgetfund`
- 基金日志与查询
- 为 incomes / expenses 子包提供扩展入口

#### 构造函数：

```python
BudgetSystem(members, current_fund, address, household_name='')
## BudgetSystem — Methods Overview
```

| 方法名 | 参数 | 功能说明 |
|--------|------|-----------|
| `__init__(members, current_fund, address, household_name='')` | 成员列表、初始基金、地址、家庭名称 | 初始化整个系统，创建基金对象、存储成员与家庭信息 |
| `add_member(new_member)` | 成员对象 | 添加一个成员（guardian 或 dependant） |
| `remove_member(ID)` | 成员 ID | 按 ID 删除成员，成功返回 True，未找到返回 False |
| `list_member()` | 无 | 打印所有成员信息（调用成员的 `__str__()`） |
| `get_member(ID)` | 成员 ID | 返回对应的成员对象，若不存在返回 None |
| `__str__()` | 无 | 返回 BudgetSystem 的总体信息（家庭名称、地址、人数、基金余额） |
| `print_fund_log()` | 无 | 打印全部基金日志记录 |
| `search_fund_log(keyword)` | 关键字字符串 | 搜索日志中 description 字段包含关键字的记录 |
| `filter_fund_status(status)` | True / False | 筛选成功（True）或失败（False）的日志记录 |
| `add_fund(amount, description='')` | 金额、描述 | 增加基金余额并写入日志 |
| `sub_fund(amount, description='')` | 金额、描述 | 减少基金余额，不足则记录失败 |
| `validate_fund(amount=0)` | 金额 | 检查基金余额是否 ≥ amount，返回布尔值 |
