import pandas
import matplotlib.pyplot as plt

# 2a
miasta = pandas.read_csv('../Resources/miasta.csv')

print(miasta.to_string())
print(miasta.values)

# 2b
df2 = {'Rok': 2010, 'Gdansk': 460, 'Poznan': 555, 'Szczecin': 405}
miasta = miasta.append(df2, ignore_index=True)
print(miasta.to_string())

# 2c
YearsXPoints = miasta.values[:, 0]
GdanskYPoints = miasta.values[:, 1]
PoznanYPoints = miasta.values[:, 2]
SzczecinYPoints = miasta.values[:, 3]

plt.plot(YearsXPoints, GdanskYPoints, color='r', marker='o', label='Gdansk')
plt.plot(YearsXPoints, PoznanYPoints, color='b', marker='o', label='Poznan')
plt.plot(YearsXPoints, SzczecinYPoints, color='g', marker='o', label='Szczecin')
plt.ylabel('Liczba ludnosci w tys.')
plt.xlabel('Lata')
plt.title('Ludnosc w miastach Polski')
plt.legend()

plt.show()
