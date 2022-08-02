# Lesta_introductory_task
### 1 задание - number_is_even.py
Функция number_is_even(value) переводит десятичное число в двоичное число, и по последней цифре определяет чётность числа.

### 2 задание - fifo.py
Класс FifoList инициализирует пустой список fifo и имеет 2 метода: 
* put_in(element) - добавляет элемент в конец списка
* put_out() - забирает элемент в начале списка

FifoDeque это интерфейс класса deque с 2-мя методами:
* put_in(element) - добавляет элемент в конец списка
* put_out() - забирает элемент в начале списка

FifoDeque работает быстрее, чем FifoList. Это связано с тем, что методы deque append() и popleft() лучше оптимизированы, чем методы list append() и pop().

### 3 задание - sort_numbers.py
Функция quick_sort(numbers) сортирует список алгоритмом слияния, который работает быстрее всего (O(nlogn)).