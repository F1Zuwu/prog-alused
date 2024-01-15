import csv


def read_file_contents(filename: str) -> str:
    with open(filename, 'r') as file:
        return file.read()


def read_file_contents_to_list(filename: str) -> list:
    with open(filename, 'r') as file:
        return file.read().splitlines()


def read_csv_file(filename: str) -> list:
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        return [row for row in reader]


def write_contents_to_file(filename: str, contents: str) -> None:
    with open(filename, 'w') as file:
        file.write(contents)


def write_lines_to_file(filename: str, lines: list) -> None:
    with open(filename, 'w') as file:
        file.write('\n'.join(lines))


def write_csv_file(filename: str, data: list) -> None:
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)


def merge_dates_and_towns_into_csv(dates_filename: str, towns_filename: str, csv_output_filename: str) -> None:
    dates_data = read_csv_file(dates_filename)
    towns_data = read_csv_file(towns_filename)

    merged_data = [["name", "town", "date"]]

    for date_info in dates_data:
        name = date_info[0]
        date = date_info[1] if len(date_info) > 1 else "-"
        town = "-"

        for town_info in towns_data:
            if town_info[0] == name:
                town = town_info[1] if len(town_info) > 1 else "-"
                break

        merged_data.append([name, town, date])

    write_csv_file(csv_output_filename, merged_data)


# Example usage:
# merge_dates_and_towns_into_csv('dates.txt', 'towns.txt', 'output.csv')
