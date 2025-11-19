from .budgetfund import budgetfund

def fmt(x):
        s = str(x)
        return s if len(s) <= 15 else s[:12] + "..."

def print_log(budgetfund):  # print the whole log
    num = 0
    temp = budgetfund.get_log()
    title = temp[0]
    rows = temp[1]
    for item in title:
        print(f"|{fmt(item):^15}|", end="")
    print()
    for record in rows:
        for item in record:
            print(f"|{fmt(item):<15}|", end="")
        print()
        num += 1
    print()
    return [rows, 'Total Record #:' + str(num)]


def search_log(budgetfund, keyword=''):  # find log with certain keyword
    num = 0
    temp = budgetfund.get_log()
    title = temp[0]
    rows = temp[1]
    des = title.index('description')
    found = []
    for row in rows:
        desc = row[des] if row[des] is not None else ""
        if keyword.lower() in str(desc).lower():
            found.append(row)
            num += 1
    if len(found) == 0:
        return ['No record found']

    for item in title:
        print(f"|{fmt(item):^15}|", end="")
    print()
    for record in found:
        for item in record:
            print(f"|{fmt(item):<15}|", end="")
        print()
    print()
    return [found,'Total # of Record Found is: ' + str(num)]
    

def filter_status(budgetfund, status=True):  
    # If status=True → return all succeeded
    # If status=False → return all failed
    num = 0
    temp = budgetfund.get_log()
    title = temp[0]
    rows = temp[1]
    status_index = title.index('status')
    target = 'succeeded' if status else 'failed'
    found = []
    for row in rows:
        if row[status_index] == target:
            found.append(row)
            num += 1
    if len(found) == 0:
        return 'No record found'
    for item in title:
        print(f"|{fmt(item):^15}|", end="")
    print()
    for record in found:
        for item in record:
            print(f"|{fmt(item):<15}|", end="")
        print()
    print()
    return [found,'Total # of Record Found is: ' + str(num)]

