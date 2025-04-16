# Опишите, используя словарь, школьную нагрузку (фамилия преподавателя, класс, часы).
# Составьте программу, определяющую нагрузку каждого преподавателя.
# Определить, у какого преподавателя самая большая нагрузка и у кого самая низкая.


list_of_teachers = {
    "Анна": {
        "6B": 6,
        "11": 3
    },
    "Виктория": {
        "2A": 10,
        "2B": 10
    },
    "Василий": {
        "3B": 10,
        "5A": 11
    }
}


def find_min_max_load(teachers):
    loads = []
    for last_name in teachers:
        count = 0

        for i in teachers[last_name]:
            count += teachers[last_name][i]
        
        loads.append((count, last_name))

    return loads


if __name__ == "__main__":
    teacher_workload = find_min_max_load(list_of_teachers)
    print("Минимальная нагрузка на учителя {0[1]}: {0[0]} час(-ов)".format(min(teacher_workload)))
    print("Максимальная нагрузка на учителя {0[1]}: {0[0]} час(-ов)".format(max(teacher_workload)))