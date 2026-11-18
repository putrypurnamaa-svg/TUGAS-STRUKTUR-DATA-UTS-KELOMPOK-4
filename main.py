
from linked_stack import LinkedStack

stack = LinkedStack()

stack.push("Data 1")
stack.push("Data 2")
stack.push("Data 3")

stack.display()

print("Data teratas:", stack.peek())
print("Data diambil:", stack.pop())
print("Jumlah data:", stack.size())
