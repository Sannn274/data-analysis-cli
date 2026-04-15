import pandas as pd

df = pd.read_csv('sample.csv')

print('=== DATA ===')
print(df)

print('\n=== UMUR > 22 ===')
print(df[df['umur'] >= 22])

print('\n=== RATA-RATA UMUR ===')
print(df['umur'].mean())
