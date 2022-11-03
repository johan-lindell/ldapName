import pandas as pd

# get table with names and the corresponding usernames
table = pd.read_csv('./fulldump.csv')

newTable = pd.DataFrame(table, columns=['name', 'username'])

newTable['name'] = table['preferred_name'] + ' ' + table['surname']

newTable['username'] = "- " + newTable['username']

names = pd.read_csv('namn.csv', header=None).to_numpy().flatten()

existingNames = newTable[newTable['name'].isin(names)]

for name in names:
  if name not in existingNames['name'].values:
    print("could not find username for: " + name)

existingNames['username'].to_csv('ldapOutput.csv', index=False)