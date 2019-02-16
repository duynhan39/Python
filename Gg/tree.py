class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None
	self.left = None
	self.right = None
        
class Tree(object):

    def __init__(self, head):
        self.head = Node(head)
        
    def append(self, new_value):
	self.append_helper(self.head, new_value)


    def append_helper(self, head, new_value):
	if new_value < head.value:
	  if head.left:
	    self.append_helper(head.left, new_value)
	  else:
	    head.left = Node(new_value)
	else:
	  if head.right:
	    self.append_helper(head.right, new_value)
	  else:
	    head.right = Node(new_value)


    def draw(self):
	tree = []
	l = [self.head] 
#	self.draw_helper(0, l)
	self.draw_helper(self.head, 0)
    
    def draw_helper(self, head, level):
	if head.right:
	  self.draw_helper(head.right, level+1)
	print (" "*6*level),
	print head.value
	if head.left:                      
          self.draw_helper(head.left, level+1) 
	

    def delete_first(self):
        if self.head:
            temp = self.head
            self.head = self.head.next
            return temp
        else:
            return None

t = Tree(5)

t.append(9)
t.append(-2)
t.append(3)
t.append(0)
t.append(8)
for i in range(-4, 7):
  if i != -2 and i != 3 and i != 0:
    t.append(i)

print t.head.left.right.value
print t.head.right.value

t.draw(

