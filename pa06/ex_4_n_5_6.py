__all__ = ['riddle', 'riddle_base', 'show_counters']

__riddles = {
    'Зачем Герасим утопил му-му?': ['Я не пойму'],
    'Сколько будет 2 + 2 * 2 в bin': ['110'],
    'Что за цвет #FFFFFF': 'белый'
}
_answers_result = {}


def riddle(question: str, answers: list, number_of_attempts: int) -> int | None:
    counter = number_of_attempts
    while number_of_attempts > 0:
        number_of_attempts -= 1
        print(f'{question}?')
        if input('Введите ответ: ') in answers:
            print(f'Угадал! за {counter - number_of_attempts} попытку(ки)!')
            return counter - number_of_attempts
        print(f'Неудачная попытка, осталось ещё {number_of_attempts} попыток')
    print('Это фиаско, братан...')
    return 0


def riddle_base(rep: int):
    for k, v in __riddles.items():
        __set_answers(k, riddle(k, v, rep))


def __set_answers(question: str, num: int):
    _answers_result[question] = num


def show_counters():
    print(*(f'Загадка: {k}, {f"отгадана за {v} попыток" if v > 0 else "не отгадана..."} ' for k, v in
            _answers_result.items()), sep='\n')


if __name__ == '__main__':
    riddle_base(3)
    show_counters()
