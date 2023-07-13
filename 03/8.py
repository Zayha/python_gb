f1 = {'Василий': ('топор', 'вилы', 'палатка', 'самогон', 'веревка')}
f2 = {'Федор': ('продукты', 'спиннинг', 'нож', 'самогон', 'примус', 'веревка')}
f3 = {'Акакий': ('продукты', 'самогон', 'ружье', 'топор', 'капкан')}
friends_list = [f1, f2, f3]

all_things = set()
for i in friends_list:
    val = list(i.values())[0]
    for j in val:
        all_things.add(j)
print(f'Все вещи: {all_things}')


unique_for_one = set()
set_for_two = set()
intersection_set = set()
for i in friends_list:
    i_val = set(list(i.values())[0])
    temp_friends_list = friends_list[::]
    temp_friends_list.remove(i)
    intersection_set = set(list(temp_friends_list[0].values())[0])
    print(intersection_set)
    for li in temp_friends_list[1:]:
        intersection_set &= set(list(li.values())[0])
    # print(f'>>>>{intersection_set}')
    not_for_li = intersection_set - i_val
    print(f'Только у {list(i.keys())[0]} нет {not_for_li}')
    for a in temp_friends_list:
        val = list(a.values())[0]
        for m in val:
            set_for_two.add(m)
    unique_for_one = i_val - set_for_two
    if len(unique_for_one) >= 1:
        unique_items = ', '.join(str(item) for item in unique_for_one)
        print(f'{list(i.keys())[0]} имеет при себе уникальные вещи: {unique_items}')
        unique_for_one.clear()
        set_for_two.clear()
        i_val.clear()
        intersection_set.clear()

