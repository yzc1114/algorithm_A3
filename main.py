def func():
    n = int(input("输入n:"))
    m = int(input("输入m:"))
    assert n > m
    greedy_choice = n // m + 1
    smaller_choice = n // m
    num_of_greedy_choice = n % m
    num_of_smaller_choice = (n - num_of_greedy_choice * greedy_choice) // smaller_choice
    result = [smaller_choice] * num_of_smaller_choice + [greedy_choice] * num_of_greedy_choice
    print(result)


if __name__ == "__main__":
    while True:
        func()
