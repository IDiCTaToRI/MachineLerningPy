import unicodecsv
import random
import operator
import math


# используется датасет, где есть пять значений от -1 до 1 и g (good) или b (bad) для этого набора чисел
# алгоритм предсказывает, будет у нового набора good или bad

def get_data(filename):
    with open(filename, 'rb') as f:
        reader = unicodecsv.reader(f)
        return list(reader)


def shuffle_data(i_data):
    random.shuffle(i_data)
    train_data = i_data[:int(0.7 * 30)]
    test_data = i_data[int(0.7 * 30):]
    return train_data, test_data


def euclidean_distance(x, xi):
    distance = 0.0
    for i in range(len(x) - 1):
        distance += pow((float(x[i]) - float(xi[i])), 2)
    distance = math.sqrt(distance)
    return distance


def knn_prediction(test_data, train_data, k_value):
    for i in test_data:
        eu_distance = []
        good = 0

        bad = 0
        for j in train_data:
            eu_dist = euclidean_distance(i, j)
            eu_distance.append((j[5], eu_dist))
            eu_distance.sort(key=operator.itemgetter(1))
            knn = eu_distance[:k_value]
            for k in knn:
                if k[0] == 'g':
                    good += 1
                else:
                    bad += 1
        if good > bad:
            i.append('g')
        elif good < bad:
            i.append('b')
        else:
            i.append('NaN')


def calculate_accuracy(test_data):
    correct = 0
    for i in test_data:
        if i[5] == i[6]:
            correct += 1
    accuracy = float(correct) / len(test_data) * 100
    return accuracy


dataset = get_data('dataset.csv')
train_dataset, test_dataset = shuffle_data(dataset)
k = 5
knn_prediction(test_dataset, train_dataset, k)

print(test_dataset)
# при разных запусках 80%-100%
print("Accuracy: ", calculate_accuracy(test_dataset), '%')
