class Node(object):

  def __init__(self, data):
    self.data = data
    self.nextNode = None # NULL ? =)

class LinkedList(object):

  def __init__(self):
    self.head = None
    self.size = 0


  # O(1) !!!
  def insertStart(self, data):
    self.size = self.size + 1
    newNode = Node(data)

    if not self.head:
      self.head = newNode # если список пуст то [N] -> NULL
    else:
      newNode.nextNode = self.head # если не пуст
      self.head =   newNode # [N] -> [H] -> NULL

  def remove(self, data):
    if self.head is None:
      return

    self.size = self.size - 1

    currentNode = self.head
    previousNode = None
    while currentNode.data != data:
      previousNode = currentNode
      currentNode = currentNode.nextNode

    if previousNode is None: # если сразу нашли элемент первый
      self.head = currentNode.nextNode
    else: # если не первый эелемент нашли
      previousNode.nextNode = currentNode.nextNode


  # O(1)
  def size1(self):
    return self.size

  # O(N) not so good !!!
  def size2(self):
    actualNode = self.head
    size = 0

    while actualNode is not None:
      size += 1
      actualNode = actualNode.nextNode

    return size

  # O(N)
  def insertEnd(self, data):
    self.size += 1
    newNode = Node(data)

    lastNode = self.head # доходим до последнего элемента перед NULL
    while lastNode.nextNode is not None:
      lastNode = lastNode.nextNode

    lastNode.nextNode = newNode # переприсваиваем nextNode на newNode

  # O(N)
  def traverseList(self): # выводит весь список
    actualNode = self.head

    while actualNode is not None:
      print("%d " % actualNode.data)
      actualNode = actualNode.nextNode



linkedList = LinkedList()

linkedList.insertStart(12)
linkedList.insertStart(122)
linkedList.insertStart(3)
linkedList.insertEnd(31)

linkedList.traverseList()
print("size1 %i " % linkedList.size1())
print("size2 %d " % linkedList.size2())

linkedList.remove(3)
linkedList.remove(31)
linkedList.traverseList()
print("size1 %i " % linkedList.size1())
linkedList.remove(122)
linkedList.remove(12)
linkedList.traverseList()
print("size1 %i " % linkedList.size1())