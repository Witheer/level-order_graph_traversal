from collections import deque

# Tree node class
class Node:
  def __init__(self, data, left=None, right=None):
    self.data = data
    self.left = left
    self.right = right

# Open instructions.md in the Markdown tab
def level_order_traversal(root):
  queue = deque()
  queue.append(root)

  while queue:
    temp = queue.popleft()
    print(temp.data, end=' ')
    if temp.left:
      queue.append(temp.left)
    if temp.right:
      queue.append(temp.right)

def find_path(root):
  queue = deque()
  queue.append(root)
  result = []

  while queue:
    temp = queue.popleft()
    result.append(temp.data)
    if temp.left:
      queue.append(temp.left)
    if temp.right:
      queue.append(temp.right)

  return result
