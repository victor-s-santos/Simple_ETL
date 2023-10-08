from csv import DictReader


def generate_list_of_dictionaries(file_path: str) -> list[dict]:
    """Generates a list of dictionaries of each value from the given file

    Args:
        file_path (str): The path of csv file.

    Returns:
        list[dict]: The list of dictionaries from each value in the given csv.
    """
    list_of_dictionaries = []
    with open(file_path, "r") as file:
        for i in DictReader(file):
            list_of_dictionaries.append(dict(i))
    return list_of_dictionaries


if __name__ == "__main__":
    filename = "FastFoodNutritionMenu.csv"
    list_of_dicts = generate_list_of_dictionaries(filename)
    print(list_of_dicts[0])
