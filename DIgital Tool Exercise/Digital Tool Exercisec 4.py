import pandas as pd
import matplotlib.pyplot as plt

file_path = ("D:/Desktop/学习资料/HIstory 1354 Digital HIstoy/Sicheng-Wu-History-1354-Project/DIgital Tool Exercise/census_data.csv")

try:
    df = pd.read_csv(file_path)
    print("File loaded successfully!")
except FileNotFoundError:
    print("File not found. Please check the file path.")
    exit()

print(type(df))
print(df.head())

davidson_county_value = 54

print("Columns in the dataset:", df.columns)

try:
    total_pop_1820 = df[(df['year'] == 1820) & (df['county'] == davidson_county_value)]['citypop'].sum()
    total_pop_1830 = df[(df['year'] == 1830) & (df['county'] == davidson_county_value)]['citypop'].sum()
    total_pop_1840 = df[(df['year'] == 1840) & (df['county'] == davidson_county_value)]['citypop'].sum()

except KeyError as e:
    print(f"Missing column in the dataset: {e}")
    exit()

print("Total population of Davidson County:")
print("1820:", total_pop_1820)
print("1830:", total_pop_1830)
print("1840:", total_pop_1840)

years = [1820, 1830, 1840]
pops = [total_pop_1820, total_pop_1830, total_pop_1840]

plt.figure(figsize=(6, 4))
plt.plot(years, pops, marker='o', linestyle='-', color='blue')
plt.title("Population of Davidson County (1820-1840)")
plt.xlabel("Year")
plt.ylabel("Population")
plt.grid(True)
plt.show()


