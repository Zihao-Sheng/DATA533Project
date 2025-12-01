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

The `BudgetSystem` class integrates all three sub-packages (member, budgetfund, property).  
It serves as the central interface that manages **members**, **funds**, and **assets** together.

---

## 👥 Member Management

| Method | Description |
|--------|-------------|
| `add_member(member)` | Add a new member (guardian or dependant). |
| `remove_member(ID)` | Remove a member by unique ID. |
| `list_member()` | Print all members in the system. |
| `get_member(ID)` | Retrieve a member object by ID. |
| `upgrade_member(ID)` | Convert a dependant into a guardian (promote role). |
| `__str__()` | Return formatted summary of the BudgetSystem state. |

---

## 💰 Fund Management

| Method | Description |
|--------|-------------|
| `add_fund(amount, description, date)` | Add income to the budget fund. |
| `sub_fund(amount, description, date)` | Subtract expenses; logs success/failed. |
| `validate_fund(amount)` | Check whether fund has enough balance. |
| `summarize_month(start, end)` | Generate monthly summary bar/pie charts. |
| `filter_fund_status(status)` | Filter logs by succeeded/failed status. |
| `search_fund_log(keyword)` | Search transaction logs by description keyword. |
| `get_df(start, end)` | Return fund logs as a DataFrame. |
| `print_fund_log(start, end)` | Pretty-print log using styled DataFrame. |

---

## 🏡 Property / Asset Management

| Method | Description |
|--------|-------------|
| `add_asset_for_member(id, name, type, value, date)` | Add an asset linked to a specific member. |
| `list_assets()` | Display all assets in table format. |
| `delete_asset(asset_id)` | Remove asset by ID. |
| `update_asset_value(asset_id, new_value)` | Change asset value with timestamp update. |
| `summarize_assets()` | Table summary grouped by type/owner. |
| `search_assets(keyword)` | Search assets by ID/name/type/owner. |
| `get_asset_visualization_data(group_by)` | Generate table + pie chart visualization. |

---

## 🖥️ CLI Interactive Menu System

| Method | Description |
|--------|-------------|
| `main_menu(system)` | Root menu for all operations. |
| `member_editor(system)` | Menu interface for adding/editing/deleting members. |
| `fund_editor(system)` | Menu for income/expense operations. |
| `property_editor(system)` | Menu for asset creation & modification. |
| `log_viewer(system)` | Menu for viewing/searching/filtering fund logs. |
| `initialization(system=None)` | Initialize a new system or re-enter menu. |

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
