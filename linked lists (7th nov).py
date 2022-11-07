from typing import Callable, Generic, TypeVar

T = TypeVar("T")

class ListNode(Generic[T]):
	def __init__(self, value: T, next: "ListNode[T] | None" = None):
		self.value = value
		self.next = next

	def __str__(self) -> str:
		return str(self.value)# + (", next={}".format(self.next) if self.next else "")

class LinkedList(Generic[T]):
	def __init__(self, head: T | None = None):
		if head:
			self.head = ListNode(head)
		else:
			self.head = None

	def insert(self, node: T):
		if self.head:
			current = self.head # start at root of list
			while current.next:
				current = current.next
			# at this point current is the last node in the chain
			current.next = ListNode(node)
		else:
			self.head = ListNode(node)

	def __str__(self) -> str:
		result = "["
		current = self.head
		while current:
			result += str(current)
			if current.next:
				result += ", "
			current = current.next
		result += "]"
		return result

	def __contains__(self, item: T) -> bool:
		current = self.head
		while current:
			if current.value is item:
				return True
			current = current.next
		return False

	def find(self, condition: Callable[[T], bool]) -> int | None:
		index = 0
		current = self.head
		while current:
			if condition(current.value):
				return index
			index += 1
			current = current.next
		return None

	def __getitem__(self, index: int) -> T:
		current = self.head
		for i in range(index):
			if current == None:
				raise IndexError
			current = current.next
		if current == None:
			raise IndexError
		return current.value


class Student:
	def __init__(self, name: str, id: int):
		self.name = name
		self.id = id
	
	def __str__(self) -> str:
		return "{} ({})".format(self.name, self.id)


students = LinkedList(Student("Lily", 889681))
students.insert(Student("Declan", 752986))
students.insert(5) # if your code editor is good, this line should be an error, since `students` is specifically a list of Students, so it can't hold an int.

print(students)