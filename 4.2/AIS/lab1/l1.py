# Это было юпитером
#
# Вариант 3
#
# Датасет: CIFAR10
# Задача: Класифікація
# Модель: K - найближчих сусідів





# Загрузка датасета
# x - картинка (массив 32*32*3)
# y - подпись (массив 1)

from keras.datasets import cifar10

(x_train, y_train), (x_test, y_test) = cifar10.load_data()



# Хоть посмотрю на это

print("Train cnt", len(y_train))
print("Test cnt", len(y_test))

import matplotlib.pyplot as plt

for x, y in list(zip(x_train, y_train))[:5]:
    plt.title("label:" + str(y[0]))
    plt.imshow(x)
    plt.show()




# Преобразование *размерности* денных для использования в sklearn
# Картинки преобразовываем с n*32*32*3 в n*3072
# Подписи преобразовываем с n*1 в n

def reshape_(dataset):
    nsamples, nx, ny, nz = dataset.shape
    return dataset.reshape((nsamples, nx * ny * nz))


x_train_ = reshape_(x_train)
x_test_ = reshape_(x_test)
y_train_ = y_train[:, 0]
y_test_ = y_test[:, 0]


# KNeighborsClassifier с выбором k

from sklearn.neighbors import KNeighborsClassifier


def get_classifier(k):
    classifier = KNeighborsClassifier(n_neighbors=k)
    classifier.fit(x_train_, y_train_)
    return classifier



import pickle


# # Выбираем наилучший k (очень долго)

from sklearn.metrics import accuracy_score

k_accuracy = {}

for k in range(1, 10):
    try:
        classifier = pickle.load(open(f'lab1/data/k_{k}.sav', 'rb'))
    except FileNotFoundError:
        print("getting new classifier for k", k)
        classifier = get_classifier(k)
        pickle.dump(classifier, open(f'lab1/data/k_{k}.sav', 'wb'))

    predict = classifier.predict(x_test_)
    accuracy = accuracy_score(y_test_, predict)

    k_accuracy[k] = accuracy
    print('k=', k, 'accuracy=', accuracy)


plt.plot(k_accuracy.keys(), k_accuracy.values())
plt.title('Determining the Optimal Number of Neighbors')
plt.xlabel('K - Number of Neighbors')
plt.ylabel('Accuracy')
plt.show()


# Сортируем по точности
best_k = sorted(k_accuracy.items(), key=lambda i: -i[1])[0][0]
print("Лучший K", best_k)


# Тут можно загрузить с файла что бы не ждать n лет
# best_k = 1
best_classifier = pickle.load(open(f'lab1/data/k_{best_k}.sav', 'rb'))



# Предиктим с наилучшим k
predict = best_classifier.predict(x_test_)

from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

print(confusion_matrix(y_test_, predict))
print(classification_report(y_test_, predict))
print(accuracy_score(y_test_, predict))




