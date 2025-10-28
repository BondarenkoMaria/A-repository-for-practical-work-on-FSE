def analyze_packet_loss():
    sequence = input("Введите последовательность из 0 и 1: ")

    if len(sequence) < 5:
        print("Ошибка: длина строки должна быть не меньше 5 символов")
        return

    for char in sequence:
        if char not in '01':
            print("Ошибка: строка должна содержать только символы 0 и 1")
            return

    total_packets = len(sequence)

    lost_packets = sequence.count('0')

    max_loss_streak = 0
    current_streak = 0

    for char in sequence:
        if char == '0':
            current_streak += 1
            max_loss_streak = max(max_loss_streak, current_streak)
        else:
            current_streak = 0

    loss_percentage = (lost_packets / total_packets) * 100

    if loss_percentage <= 1:
        quality = "Отличное качество"
    elif loss_percentage <= 5:
        quality = "Хорошее качество"
    elif loss_percentage <= 10:
        quality = "Удовлетворительное качество"
    elif loss_percentage <= 20:
        quality = "Плохое качество"
    else:
        quality = "Критическое состояние сети"

    print(f"Общее количество пакетов: {total_packets}")
    print(f"Количество потерянных пакетов: {lost_packets}")
    print(f"Длина самой длинной последовательности потерянных пакетов: {max_loss_streak}")
    print(f"Процент потерь: {loss_percentage:.1f}%")
    print(f"Качество связи: {quality}")


if __name__ == "__main__":
    analyze_packet_loss()