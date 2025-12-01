# Household Budget System – Package Documentation

This Python package provides a complete household financial management system, designed using object-oriented structures and modular sub-packages.  
It includes functionality for managing household members, budget funds, and assets/properties, combined with optional CLI menus for interaction.

---

# 📦 Package Overview

The package contains **three sub-packages**:

1. **`budgetfund`**  
   Handles all income/expense logs, balance updates, summaries, and visualizations.

2. **`member`**  
   Defines all household members (guardian, dependant), including editable attributes.

3. **`property`**  
   Manages household assets such as real estate, vehicles, and investments.

The main controller class is `BudgetSystem`, which ties all subcomponents together.

---

# 📘 Available Classes, Methods, and Functions

Below is a complete list of the important public methods and functions available in this package.

---

# 🧾 1. Subpackage: `member`

## ## Base Class: `member`
| Method | Description |
|--------|-------------|
| `__init__(name, ID, DOB)` | Create a basic member. |
| `new_name(name)` | Update member name. |
| `new_DOB(DOB)` | Update date of birth. |
| `new_ID(ID)` | Update member ID. |
| `get_age()` | Return member age based on DOB. |

---

## ## Class: `dependant(member)`
| Method | Description |
|--------|-------------|
| `__init__(...)` | Create a dependant member. |
| *(inherits all methods from `member`)* | — |
| `__str__()` | Pretty-print dependant information. |

---

## ## Class: `guardian(member)`
| Method | Description |
|--------|-------------|
| `__init__(..., income, job_title='')` | Create a guardian with job + income. |
| `new_job(job_title)` | Update job title (also used when upgrading). |
| `new_income(income)` | Update income. |
| `get_income()` | Return guardian income. |
| `__str__()` | Pretty-print guardian information. |

---

## ## Function: `member_edit(member_obj)`
Interactive CLI editor for modifying member properties.  
Depending on the member type:

### Dependant Options
- Edit name  
- Edit DOB  
- Exit  

### Guardian Options
- Edit name  
- Edit DOB  
- Edit job (also changes income)  
- Edit income  
- Exit  

---

# 💰 2. Subpackage: `budgetfund`

## ## Class: `budgetfund`
| Method | Description |
|--------|-------------|
| `__init__(opening_balance, name='')` | Create a fund account. |
| `validate(amount=0)` | Check if balance is sufficient. |
| `add(amount, description='', date=None)` | Add income; logs success. |
| `sub(amount, description='', date=None)` | Subtract expense; logs success/failed status. |
| `get()` | Return current balance. |
| `get_log()` | Return raw log list. |
| `get_df(start=None, end=None)` | Return logs as DataFrame (with year-month). |
| `summarize_month(start, end='')` | Create monthly bar chart & pie chart summary. |
| `__str__()` | Summary of current fund state. |

---

## ## Module: `fund_utils`

### `print_log(budgetfund, start, end)`
Display logs in a styled table (green = success, red = failed).

### `search_log(budgetfund, keyword='')`
Search in description field (case-insensitive).

### `filter_status(budgetfund, status=True)`
Filter only succeeded (`True`) or failed (`False`) logs.

---

# 🏡 3. Subpackage: `property`

## ## Class: `Asset`
| Method | Description |
|--------|-------------|
| `__init__(name, asset_type, owner, current_value, date_acquired)` | Create an asset with auto ID. |
| `_generate_id(asset_type)` | Internal auto-ID generator (A001R, A002V, etc). |
| `update_value(new_value)` | Change asset value (auto-updates timestamp). |
| `to_dict()` | Return dict representation for DataFrame. |
| `__str__()` | Human-readable asset format. |

---

## ## Class: `PropertyRegistry`
| Method | Description |
|--------|-------------|
| `add_asset(asset)` | Add new asset object. |
| `delete_asset(asset_id)` | Remove asset by ID. |
| `update_asset_value(asset_id, new_value)` | Update value of an existing asset. |
| `get_asset(asset_id)` | Return asset object. |
| `to_dataframe()` | Convert all assets to DataFrame with formatted currency. |
| `filter_assets(asset_type=None, owner=None)` | Filter asset list by type or owner. |
| `__iter__()` | Allow iteration over stored assets. |

---

## ## Module: `asset_utils`

### `summarize_total_value(registry)`
Return a table summarizing:
- Total value  
- Count  
- Average value  
grouped by Type and Owner.

### `search_assets(registry, keyword)`
Search by ID, name, type, or owner; return DataFrame.

### `get_visualization_data(registry, group_by='Type')`
Produce:
- Summary table  
- Pie chart  
- Grouped DataFrame  

---

# 🏠 4. Main Controller: `BudgetSystem`

This high-level class connects all three sub-packages.  
It manages members, funds, and assets together inside one object.

## ## Key Methods

### Members
- `add_member(member)`
- `remove_member(ID)`
- `list_member()`
- `get_member(ID)`
- `upgrade_member(ID)`  
- `__str__()`

### Funds
- `add_fund(amount, description, date)`
- `sub_fund(amount, description, date)`
- `validate_fund(amount)`
- `summarize_month(start, end)`
- `filter_fund_status(status)`
- `search_fund_log(keyword)`
- `get_df(start, end)`
- `print_fund_log(start, end)`

### Property
- `add_asset_for_member(id, name, type, value, date)`
- `list_assets()`
- `delete_asset(asset_id)`
- `update_asset_value(asset_id, new_value)`
- `summarize_assets()`
- `search_assets(keyword)`
- `get_asset_visualization_data(group_by)`

### CLI Menu
- `main_menu(system)`
- `member_editor(system)`
- `fund_editor(system)`
- `property_editor(system)`
- `log_viewer(system)`
- `initialization(system=None)`

---

# ✔ Summary

This package provides:

- Complete household management  
- Modular structure with 3 sub-packages  
- Inheritance-based member hierarchy  
- Full financial logging system  
- Asset management with summaries & visualizations  
- Optional menus for interactive use  

It fulfills the typical requirements for a multi-module Python package with sub-packages, OOP design, and documentation.

---
