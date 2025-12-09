import xml.etree.ElementTree as ET 

def load_users_data(): 
    try: 
        users_tree = ET.parse('users.xml') 
        users = [] 
        for user_elem in users_tree.getroot().findall('user'): 
            user = { 
                'user_id': int(user_elem.find('user_id').text), 
                'name': user_elem.find('name').text, 
                'age': int(user_elem.find('age').text), 
                'weight': int(user_elem.find('weight').text), 
                #'fitness_lvl': user_elem.find('fitness_lvl').text, 
                'workouts': [] 
            } 
            users.append(user) 
        return users 
    except FileNotFoundError: 
        print("Файл не найден") 
        return [] 


def load_workouts_data(): 
    try: 
        workouts_tree = ET.parse('workouts.xml') 
        workouts = [] 
        for workout_element in workouts_tree.getroot().findall('workout'): 
            workout = { 
                'workout_id': int(workout_element.find('workout_id').text), 
                'user_id': int(workout_element.find('user_id').text), 
                'date': workout_element.find('date').text, 
                'type': workout_element.find('type').text, 
                'duration': int(workout_element.find('duration').text), 
                'distance': float(workout_element.find('distance').text), 
                'calories': int(workout_element.find('calories').text), 
                'avg_heart_rate': int(workout_element.find('avg_heart_rate').text), 
                'intensity': workout_element.find('intensity').text 
            } 
            workouts.append(workout) 
        return workouts 
    except FileNotFoundError: 
        print("Файл не найден") 
        return [] 


def get_stats(users, workouts):
    if not workouts:
        return {
            'total_workouts': 0,
            'total_users': 0,
            'total_calories': 0,
            'total_hours': 0,
            'total_distance': 0
        }

    total_workouts = len(workouts)
    total_users = len(set([w['user_id'] for w in workouts]))
    total_calories = sum(w['calories'] for w in workouts)
    total_minutes = sum(w['duration'] for w in workouts)
    total_hours = round(total_minutes / 60, 1)
    total_distance = round(sum(w['distance'] for w in workouts), 1)

    return {
        'total_workouts': total_workouts,
        'total_users': total_users,
        'total_calories': total_calories,
        'total_hours': total_hours,
        'total_distance': total_distance
    }


if __name__ == '__main__':
    users = load_users_data()
    workouts = load_workouts_data()

    stats = get_stats(users, workouts)

    print("ОБЩАЯ СТАТИСТИКА")
    print("===========")
    print(f"Всего тренировок: {stats['total_workouts']}")
    print(f"Всего пользователей: {stats['total_users']}")
    print(f"Сожжено калорий: {stats['total_calories']}")
    print(f"Общее время: {stats['total_hours']} часов")
    print(f"Пройдено дистанции: {stats['total_distance']} км")


# def get_stats(users, workouts):
#     total_calories = sum(workout['calories'] for workout in workouts)  #каллории
#     total_distance = sum(workout['distance'] for workout in workouts)  #дистанция
#     total_time = (sum(workout['duration'] for workout in workouts))/60  #все время
#
#     for workout in workouts:
#         work = 0
#         if workout['duration'] in workouts:
#             work += 1  #кол-во тренировок
#
#     for user in users:
#         count = 0
#         if user['user_id'] in users:
#             count += 1 #кол-во людей
#             #print(count)
#     print(f"Сожжено калорий: {total_calories}")
#     return total_calories, total_distance, total_time



