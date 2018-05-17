class Node(object):

  def __init__(self, data):
    self.data = data
    self.nextNode = None # NULL ? =)

class LinkedList(object):

  def __init__(self):
    self.head = Node
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

  # O(1)
  def size(self):
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
    while lastNode.nextNode in not None:
      lastNode = lastNode.nextNode

    lastNode.nextNode = newNode # переприсваиваем nextNode на newNode

  # O(N)
  def traverseList(self): # выводит весь список
    actualNode = self.head

    while actualNode is not None:
      print("%d " % actualNode.data)
      actualNode = actualNode.nextNode
