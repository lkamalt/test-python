import numpy as np

from funcs import get_mean_custom, get_mean_np, get_std_custom, get_std_np, get_median_custom, get_median_np

arr = np.array([1, 2, 3, 5, 6, 7])
arr_nan = np.array([1, 2, 3, 5, 6, 7, 8, 10, np.nan])
arr_empty = np.array([])
arr_all_nan = np.array([np.nan, np.nan, np.nan])
arr1 = np.array([3, 7, 1, 5, 9])
arr2 = np.array([1, 5, 8, 4, 3, 9])
arr_1elem = np.array([np.nan, 2, np.nan])
arr_2elem = np.array([np.nan, 1, np.nan, 2, np.nan])

mean_arr = 4.0
mean_arr_nan = 5.25
mean_arr_1elem = 2.0
mean_arr_2elem = 1.5

std_arr = 2.16024689947
std_arr_nan = 2.90473750966
std_arr_1elem = 0.0
std_arr_2elem = 0.5

median_arr = 4.0
median_arr_nan = 5.5
median_arr1 = 5.0
median_arr2 = 4.5
median_arr_1elem = 2.0
median_arr_2elem = 1.5


# Тестирование функции mean_custom() --------------------------------------------------------------
def test_mean_custom():
    mean_c = get_mean_custom(arr)
    assert np.isclose(mean_c, mean_arr)


def test_mean_custom_nan():
    mean_c = get_mean_custom(arr_nan)
    assert np.isclose(mean_c, mean_arr_nan)


def test_mean_custom_empty():
    mean_c = get_mean_custom(arr_empty)
    assert np.isnan(mean_c)


def test_mean_custom_all_nan():
    mean_c = get_mean_custom(arr_all_nan)
    assert np.isnan(mean_c)


def test_mean_custom_1elem():
    mean_c = get_mean_custom(arr_1elem)
    assert np.isclose(mean_c, mean_arr_1elem)


def test_mean_custom_2elem():
    mean_c = get_mean_custom(arr_2elem)
    assert np.isclose(mean_c, mean_arr_2elem)


# Тестирование функции mean_np() ------------------------------------------------------------------
def test_mean_np():
    mean_np = get_mean_np(arr)
    assert np.isclose(mean_np, mean_arr)


def test_mean_np_nan():
    mean_np = get_mean_np(arr_nan)
    assert np.isclose(mean_np, mean_arr_nan)


def test_mean_np_empty():
    mean_np = get_mean_np(arr_empty)
    assert np.isnan(mean_np)


def test_mean_np_all_nan():
    mean_np = get_mean_np(arr_all_nan)
    assert np.isnan(mean_np)


def test_mean_np_1elem():
    mean_np = get_mean_np(arr_1elem)
    assert np.isclose(mean_np, mean_arr_1elem)


def test_mean_np_2elem():
    mean_np = get_mean_np(arr_2elem)
    assert np.isclose(mean_np, mean_arr_2elem)


# Тестирование функции std_custom() ---------------------------------------------------------------
def test_std_custom():
    std_c = get_std_custom(arr)
    assert np.isclose(std_c, std_arr)


def test_std_custom_nan():
    std_c = get_std_custom(arr_nan)
    assert np.isclose(std_c, std_arr_nan)


def test_std_custom_empty():
    std_c = get_std_custom(arr_empty)
    assert np.isnan(std_c)


def test_std_custom_all_nan():
    std_c = get_std_custom(arr_all_nan)
    assert np.isnan(std_c)


def test_std_custom_1elem():
    std_c = get_std_custom(arr_1elem)
    assert np.isclose(std_c, std_arr_1elem)


def test_std_custom_2elem():
    std_c = get_std_custom(arr_2elem)
    assert np.isclose(std_c, std_arr_2elem)


# Тестирование функции std_np() -------------------------------------------------------------------
def test_std_np():
    std_np = get_std_np(arr)
    assert np.isclose(std_np, std_arr)


def test_std_np_nan():
    std_np = get_std_np(arr_nan)
    assert np.isclose(std_np, std_arr_nan)


def test_std_np_empty():
    std_np = get_std_np(arr_empty)
    assert np.isnan(std_np)


def test_std_np_all_nan():
    std_np = get_std_np(arr_all_nan)
    assert np.isnan(std_np)


def test_std_np_1elem():
    std_np = get_std_np(arr_1elem)
    assert np.isclose(std_np, std_arr_1elem)


def test_std_np_2elem():
    std_np = get_std_np(arr_2elem)
    assert np.isclose(std_np, std_arr_2elem)


# Тестирование функции median_custom() ------------------------------------------------------------
def test_median_custom():
    median_c = get_median_custom(arr)
    assert np.isclose(median_c, median_arr)


def test_median_custom_nan():
    median_c = get_median_custom(arr_nan)
    assert np.isclose(median_c, median_arr_nan)


def test_median_custom_empty():
    median_c = get_median_custom(arr_empty)
    assert np.isnan(median_c)


def test_median_custom_all_nan():
    median_c = get_median_custom(arr_all_nan)
    assert np.isnan(median_c)


def test_median_custom1():
    median_c = get_median_custom(arr1)
    assert np.isclose(median_c, median_arr1)


def test_median_custom2():
    median_c = get_median_custom(arr2)
    assert np.isclose(median_c, median_arr2)


def test_median_custom_1elem():
    median_c = get_median_custom(arr_1elem)
    assert np.isclose(median_c, median_arr_1elem)


def test_median_custom_2elem():
    median_c = get_median_custom(arr_2elem)
    assert np.isclose(median_c, median_arr_2elem)


# Тестирование функции median_np() ----------------------------------------------------------------
def test_median_np():
    median_np = get_median_np(arr)
    assert np.isclose(median_np, median_arr)


def test_median_np_nan():
    median_np = get_median_np(arr_nan)
    assert np.isclose(median_np, median_arr_nan)


def test_median_np_empty():
    median_np = get_median_np(arr_empty)
    assert np.isnan(median_np)


def test_median_np_all_nan():
    median_np = get_median_np(arr_all_nan)
    assert np.isnan(median_np)


def test_median_np1():
    median_np = get_median_np(arr1)
    assert np.isclose(median_np, median_arr1)


def test_median_np2():
    median_np = get_median_np(arr2)
    assert np.isclose(median_np, median_arr2)


def test_median_np_1elem():
    median_np = get_median_np(arr_1elem)
    assert np.isclose(median_np, median_arr_1elem)


def test_median_np_2elem():
    median_np = get_median_np(arr_2elem)
    assert np.isclose(median_np, median_arr_2elem)
