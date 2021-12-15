import pandas as pd
import matplotlib.pyplot as plt
import math

def read_csv(filename):
    data = pd.read_csv(filename)
    return data


def draw(dataset):
    n = 25
    date = list(dataset.Date)
    sunspots = list(dataset['Monthly Mean Total Sunspot Number'])
    plt.figure(figsize=(40, 10))
    plt.plot(date, sunspots)
    #plt.scatter(date, sunspots)
    result = pd.DataFrame(sunspots)
    rolling_mean = result.rolling(window=n).mean()
    #plt.plot(rolling_mean, color = )
    plt.show()

if __name__ == '__main__':
        file = "Sunspots.csv"
        dataset = read_csv(file)
        draw(dataset)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
