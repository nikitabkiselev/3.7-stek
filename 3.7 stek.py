class Stack:
    def __init__(self, list_stack):
        self.list_stack = list_stack

    '''isEmpty - проверяет стека на пустоту. Возвращается True/False.'''
    def isEmpty(self):
        if not self.list_stack:
            return True
        else:
            return False

    '''push - добавляется новый элемент на вершину стека. Метод никакого значения не возвращает.'''
    def push(self, item_stack):
        self.list_stack = self.list_stack + item_stack
        return

    '''pop - удаляется верхний элемент стека. В результате стек изменяется. Возвращается верхний элемент стека'''
    def pop(self):
        self.list_stack = self.list_stack[0:-1]
        return self.list_stack[-1]

    '''peek - возвращается верхний элемент стека, без его удаления. Стек неизменяется.'''
    def peek(self):
        return self.list_stack[-1]

    '''size - возвращается количество элементов в стеке'''
    def size(self):
        return len(self.list_stack)

    def correct_stack(self, text):
        while '()' in text or '[]' in text or '{}' in text:
            text = text.replace('()', '')
            text = text.replace('[]', '')
            text = text.replace('{}', '')

        if not text:
            result = 'Последовательность скобок сбалансирована'
        else:
            result = 'Последовательность скобок не сбалансирована'

        return result

my_list = '{{[(])]}}'

stack = Stack(my_list)

print()
print('=== isEmpty ===')
print(stack.isEmpty())

print()
print('=== push ===')
stack.push('678')
print(stack.peek())

print()
print('=== pop ===')
print(stack.pop())


print()
print('=== peek ===')
print(stack.peek())

print()
print('=== size ===')
print(stack.size())

print()
print('=== correct ===')
text = input('Введите стек: ')
print(stack.correct_stack(text))