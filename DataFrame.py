import pandas as pd
#from io import StringIO

data = {'Chips':['Simba', 'Lays'],
        'CoolDrinks':['Coke', 'Fanta'],
        'Chocolates':['Cadbury', 'Tex'],
        'Pies':['Papper Steak', 'Chicken']}
data2 = {'Fruit':['Pear','Apple','Orange'],
         'Cupcakes':['Vanilla','Chocolate'],
        'Veggies':['Spinach','Cabbage']}

df = pd.DataFrame(data)
print(df)
