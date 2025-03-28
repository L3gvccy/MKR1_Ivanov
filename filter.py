def filter_file(input_filename, keyword, output_filename="filtered.txt"):
    try:
        with open(input_filename, "r", encoding="utf-8") as infile, open(output_filename, "w", encoding="utf-8") as outfile:
            filtered_lines = [line for line in infile if keyword in line]
            outfile.writelines(filtered_lines)
        print(f"Фільтрація завершена. Результат записано у '{output_filename}'.")
    except FileNotFoundError:
        print("Помилка: Файл не знайдено.")
    except Exception as e:
        print(f"Сталася помилка: {e}")