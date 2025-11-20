# Household Budget System – Project Plan (Design Overview)

---

## 1. Main Package: `budget_system` 
Coordinates all submodules and provides a unified interface.

### Functions
- Initialize with address, member, budgetfund, and property  
- Edit family member information  
- Add or reduce funds via the budget class  
- Plot monthly income and expense graphs  
- Edit household property records  

## 2. Subpackage 1: `budgetfund`

### Functions
- Initialize fund balance  
- Add or subtract amounts  
- Validate expenses  
- Log transactions  
- Export logs to DataFrame  
- Filter by date  
- Generate monthly summaries  

## 3. Subpackage 2: `member`

### Features
- Base `member` class: name, DOB, ID  
- `dependant`: inherits member and adds type  
- `guardian`: adds type, job, and income  

## 4. Subpackage 3: `property`

### Features：
- Manage assets: real estate, vehicles, investments
- Store basic info and values
- Category-specific extensions

Functions：
- Add, edit, or delete assets
- Update asset values
- Filter by category or owner
- Export records and generate summaries
