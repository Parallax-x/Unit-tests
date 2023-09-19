import requests
import os
import sys

courses = ["Java-разработчик с нуля", "Fullstack-разработчик на Python", "Python-разработчик с нуля",
           "Frontend-разработчик с нуля"]
mentors = [
    ["Филипп Воронов", "Анна Юшина", "Иван Бочаров", "Анатолий Корсаков", "Юрий Пеньков", "Илья Сухачев",
     "Иван Маркитан", "Ринат Бибиков", "Вадим Ерошевичев", "Тимур Сейсембаев", "Максим Батырев", "Никита Шумский",
     "Алексей Степанов", "Денис Коротков", "Антон Глушков", "Сергей Индюков", "Максим Воронцов", "Евгений Грязнов",
     "Константин Виролайнен", "Сергей Сердюк", "Павел Дерендяев"],
    ["Евгений Шмаргунов", "Олег Булыгин", "Александр Бардин", "Александр Иванов", "Кирилл Табельский",
     "Александр Ульянцев", "Роман Гордиенко", "Адилет Асканжоев", "Александр Шлейко", "Алена Батицкая", "Денис Ежков",
     "Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Максим Филипенко", "Елена Никитина"],
    ["Евгений Шмаргунов", "Олег Булыгин", "Дмитрий Демидов", "Кирилл Табельский", "Александр Ульянцев",
     "Александр Бардин", "Александр Иванов", "Антон Солонилин", "Максим Филипенко", "Елена Никитина", "Азамат Искаков",
     "Роман Гордиенко"],
    ["Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Валерий Хаслер", "Татьяна Тен", "Александр Фитискин",
     "Александр Шлейко", "Алена Батицкая", "Александр Беспоясов", "Денис Ежков", "Николай Лопин", "Михаил Ларченко"]
]
durations = [14, 20, 12, 20]


def unique_name(peoples_list: list) -> str:
    all_list = []
    for m in peoples_list:
        all_list += m
    all_names_list = []
    for mentor in all_list:
        name = mentor.split()[0]
        all_names_list.append(name)
    unique_names = set(all_names_list)
    all_names_sorted = sorted(unique_names)
    all_names_sorted_str = ', '.join(all_names_sorted)
    return all_names_sorted_str


def sort_durations(course_list: list, mentors_list: list, durations_list: list) -> str:
    courses_list = []
    for course, mentor, dur in zip(course_list, mentors_list, durations_list):
        course_dict = {'title': course, 'mentors': mentor, 'duration': dur}
        courses_list.append(course_dict)
    durations_dict = {}
    for id_, course in enumerate(courses_list):
        key = course['duration']
        durations_dict.setdefault(key, [])
        durations_dict[key].append(id_)
    durations_dict = dict(sorted(durations_dict.items()))
    result = []
    for key, ids in durations_dict.items():
        for id_ in ids:
            result.append(f"{courses_list[id_]['title']} - {key} месяцев")
    return '\n'.join(result)


def namesake(course_list: list, mentors_list: list, durations_list: list) -> list:
    courses_list = []
    for course, mentor, duration in zip(course_list, mentors_list, durations_list):
        course_dict = {'title': course, 'mentors': mentor, 'duration': duration}
        courses_list.append(course_dict)
    result = []
    for course in courses_list:
        mentors_ = list(course['mentors'])
        mentors_name = []
        for m in mentors_:
            name = m.split()[0]
            mentors_name.append(name)
        mentors_name_set = set(mentors_name)
        same_name_list = []
        for name1 in mentors_name_set:
            if list(mentors_name).count(name1) > 1:
                for name2 in course['mentors']:
                    if name1 in name2:
                        same_name_list.append(name2)
        if len(same_name_list) > 0:
            result.append(f"На курсе {course['title']} есть тёзки: {', '.join(sorted(same_name_list))}")
    return result


token = os.getenv('token')


def create_folder(ya_token: str, folder: str) -> int:
    url_new_folder = 'https://cloud-api.yandex.net/v1/disk/resources'

    try:
        req = requests.put(url_new_folder, params={'path': f'/{folder}'}, headers={'Authorization': ya_token})
        return req.status_code
    except requests.ConnectionError as e:
        sys.exit(f'Ошибка подключения: {e}')
    except requests.Timeout as e:
        sys.exit(f'Ошибка тайм-аута: {e}')
    except requests.RequestException as e:
        sys.exit(f'Ошибка запроса: {e}')


def delete_folder(ya_token: str, folder: str) -> int:
    del_folder = 'https://cloud-api.yandex.net/v1/disk/resources'

    try:
        req = requests.delete(del_folder, params={'path': f'/{folder}'}, headers={'Authorization': ya_token})
        return req.status_code
    except requests.ConnectionError as e:
        sys.exit(f'Ошибка подключения: {e}')
    except requests.Timeout as e:
        sys.exit(f'Ошибка тайм-аута: {e}')
    except requests.RequestException as e:
        sys.exit(f'Ошибка запроса: {e}')
