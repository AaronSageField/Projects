# Aaron Sage Field
# March 6th, 2025
# Display regional and quarterly sales in local currency

import locale as lc
lc.setlocale(lc.LC_ALL, '')
from decimal import Decimal
import sys

def formatTable(lcSales):
    regEntity = ''
    for i, row in enumerate(lcSales):
        for j, sale in enumerate(row):
            if j == 0:
                regEntity += f'{sale:<9}'
            else:
                regEntity += f'{sale:>11}'
        regEntity += '\n'
    return regEntity

def abrGen(atr):
    abbreviations = [atr[0]]
    for i in range(4):
        abbreviation = f'{atr[1][0]}{i + 1}'
        abbreviations.append(abbreviation)
    return abbreviations

def addSeq(lcSales, atrs):
    if atrs is None:
        for i, row in enumerate(lcSales):
            row.insert(0, str(i + 1))
    elif isinstance(atrs, str):
        for i, row in enumerate(lcSales):
            sequence = f'{atrs} {i + 1}:'
            row.insert(0, sequence)
    else:
        for i, row in enumerate(lcSales):
            sequence = f'{atrs[i]}:'
            row.insert(0, sequence)
    return lcSales
    
def conLc(decSales):
    newTable = []
    for row in decSales:
        newRow = []
        for decimal in row:
            newRow.append(lc.currency(decimal, grouping=True))
        newTable.append(newRow)
    return newTable

def calcTotals(decSales, atrs, boolean):
    if boolean == True:
        rowTotal = []
        for row in decSales:
            total = Decimal(0)
            for decimal in row:
                total += decimal
            rowTotal.append([total])
        return rowTotal
    elif boolean == False:
        colTotal = [Decimal(0)] * len(decSales[0])
        for row in decSales:
            for i in range(len(row)):
                colTotal[i] += row[i]
        return [[colTotal[i]] for i in range(len(colTotal))]
    elif boolean == None:
        total = Decimal(0)
        for row in decSales:
            for decimal in row:
                total += decimal
        return lc.currency(total, grouping=True)

def displayTotals(decSales, atrs):
    regTotals = formatTable(addSeq(conLc(calcTotals(decSales, atrs, True)), atrs[0]))
    qrtKeys = abrGen(atrs)[1:]
    qrtTotals = formatTable(addSeq(conLc(calcTotals(decSales, atrs, False)), qrtKeys))
    print(f'Sales by {atrs[0].lower()}:')
    print(regTotals)
    print(f'Sales by {atrs[1].lower()}:')
    print(qrtTotals)

def conDec(sales):
    newTable = []
    for row in sales:
        newRow = []
        for item in row:
            newRow.append(Decimal(str(round(item, 2))))
        newTable.append(newRow)
    return newTable

def main():
    sales = [[1540.0, 2010.0, 2450.0, 1845.0],  # Region 1
             [1130.0, 1168.0, 1847.0, 1491.0],  # Region 2
             [1580.0, 2305.0, 2710.0, 1284.0],  # Region 3
             [1105.0, 4102.0, 2391.0, 1576.0]]  # Region 4
    
    atrs = ['Region', 'Quarter']
    decSales = conDec(sales)
    seqSales = addSeq(conLc(decSales), None)
    regHeader = abrGen(atrs)
    seqSales.insert(0, regHeader)
    regTable = formatTable(seqSales)
    print('Sales Report\n')
    print(regTable)
    displayTotals(decSales, atrs)
    total = calcTotals(decSales, atrs, None)
    print(f'Total annual sales, all regions: {total}')
    sys.exit()

if __name__ == '__main__':
    main()
