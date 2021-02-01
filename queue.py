"""first = -1
last = -1
queue = [None] * 5
maximum = len(queue)


def is_empty():
    if last == -1:
        return 1
    else:
        return 0


def is_full():
    if last == max:
        return 1
    else:
        return 0


def enqueue(elem):
    global last
    if is_full():
        print("The queue is full, you can't add elements\n")
    else:
        last += 1
        queue[last] = elem


def dequeue():
    global first
    if is_empty():
        print("Th queue is empty, you can't delete elements\n")
    else:
        print("Element dequeue: ", queue[first])
        first += 1


def front():
    return queue[first]


def display():
    for i in range(first, last + 1):
        print(queue[i])

enqueue(2)

enqueue(7)

enqueue(10)

enqueue(1)

#enqueue(5)

print("Elements after enqueue: ")
display()

f = front()
print("First element after enqueue: ", f)

dequeue()

print("Elements after dequeue: ")
display()


f = front()
print("First element after dequeue: ", f)
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
# un obiect este o instanta a clasei. O clasa este instantiata de catre obiect. O clasa poate avea mai multe obiete.
    def __init__(self): #constructor
        self.start = None #start si end sunt proprietati ale clasei
        self.end = None

    def push(self, value): # push este o metoda a clasei si are ca parametri pe self si pe value. Self este echivalent cu this in C sau in java, se foloseste pentru a lucra cu obiectul meu.
        node = Node(value)

        if self.start is None and self.end is None:
            self.start = node
            self.end = node
        else:
            self.end.next = node
            self.end = node

    def front(self):
        if self.start is None:
            return None
        else:
            return self.start.value

    def pop(self):
        if self.start is not None: # daca coada nu e goala
            node = self.start     # nod = start
            self.start = self.start.next  # nodul de la start ia valorea urmatorului nod, adica al doilea nod devine primul
            if self.start is None:        # daca nodul de la start e none , atunci nodul de la start = nodul de la end = none => coada e goala
                self.end = None
            del node
            return node.value             # returneaza valorea nodului initial de la start
        else:
            return None                   # daca e goala, returneaza none


queue = Queue()
queue.push(3)
queue.push(5)
queue.push(8)
queue.push(2)
queue.push(10)
queue.push(9)

print(queue.front())

queue.pop()
print(queue.front())

