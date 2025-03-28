from filter import filter_file

def main():
    f_path = input("Введіть шлях до файлу: ")
    kword = input("Введіть клюічове слово для фільтрації: ")
    filter_file(f_path, kword)

if __name__ == "__main__":
    main()