import numpy as np


def delete_nans(arr):
    """
    Удаляет nan'ы в списке
    :param arr: исходный список, где могут быть nan'ы, np.array
    :return: исходный список без nan'ов, np.array
    """
    # Создаем маску, там где nan'ы будут false (для этого еще делаем инверсию с ~)
    mask = ~np.isnan(arr)
    # Применяя маску, в списке оставляем только те значения, которые не nan'ы
    return arr[mask]


# Расчет среднего значения списка чисел -----------------------------------------------------------
def get_mean_custom(arr):
    """
    Расчет среднего арифметического вручную
    :param arr: np.array
    :return: float
    """
    arr = delete_nans(arr)

    if len(arr) == 0:
        return np.nan

    # Можно через встроенную
    # sum = np.sum(arr)

    # Либо
    sum = 0
    for elem in arr:
        sum += elem

    return sum / len(arr)


def get_mean_np(arr):
    """
    Расчет среднего арифметического с numpy
    :param arr: np.array
    :return: float
    """
    arr = delete_nans(arr)

    if len(arr) == 0:
        return np.nan

    return np.mean(arr)


# Расчет среднеквадратичного отклонения списка чисел ----------------------------------------------
def get_std_custom(arr):
    """
    Расчет среднеквадратичного отклонения элементов списка вручную
    :param arr: np.array
    :return: float
    """
    arr = delete_nans(arr)

    if len(arr) == 0:
        return np.nan

    # Среднее арифметическое списка чисел arr
    mean_arr = get_mean_custom(arr)

    return np.sqrt(np.sum((arr - mean_arr) * (arr - mean_arr)) / len(arr))


def get_std_np(arr):
    """
    Расчет среднеквадратичного отклонения значения элементов списка с numpy
    :param arr: np.array
    :return: float
    """
    arr = delete_nans(arr)

    if len(arr) == 0:
        return np.nan

    return np.std(arr)


# Расчет медианы списка чисел ---------------------------------------------------------------------
def get_median_custom(arr):
    """
    Вычисляет медиану списка чисел вручную
    :param arr: np.array
    :return: float
    """
    arr = delete_nans(arr)

    if len(arr) == 0:
        return np.nan

    # Отсортированный по возрастанию массив
    arr_sorted = sorted(arr)

    if len(arr_sorted) == 1:
        return arr_sorted[0]

    # Индекс элемента, расположенного в середине списка
    mid_idx = int(len(arr_sorted) / 2)

    # Если в списке нечетное число элементов, то результат = элемент в середине отсортированного списка
    if len(arr_sorted) % 2 != 0:
        return arr_sorted[mid_idx]

    # Если в списке четное число элементов, то результат = полусумма двух средних чисел
    return 0.5 * (arr_sorted[mid_idx - 1] + arr_sorted[mid_idx])


def get_median_np(arr):
    """
    Вычисляет медиану списка чисел с помощью numpy
    :param arr: np.array
    :return: float
    """
    arr = delete_nans(arr)

    if len(arr) == 0:
        return np.nan

    return np.median(arr)
