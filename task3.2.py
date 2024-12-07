# TODO Напишите функцию find_common_participants
def find_common_participants(first_group, second_group, delimiter="|"):

    first_list = first_group.split(delimiter)
    second_list = second_group.split(delimiter)
    first_set = set(first_list)
    second_set = set(second_list)
    common = first_set.intersection(second_set)

    return delimiter.join(sorted(common))

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
common_participants = find_common_participants(participants_first_group, participants_second_group, delimiter="|")
print(f"Общие участники: {common_participants}")