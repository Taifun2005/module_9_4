from asyncore import write

first = 'Мама мыла раму'
second = 'Рамена мало бы ло'

# result = map(lambda x, y: x * y, list1, list2)
result = list(map(lambda x, y: x == y, first, second))
print(result)

def get_advanced_writer(file_name):
    def write_everything(*data_set):
        file = open(file_name, 'w', encoding='utf-8')
        for i in data_set:
            file.write(i)
        file.close()
    def get_advanced_writer():
        return write_everything


write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

