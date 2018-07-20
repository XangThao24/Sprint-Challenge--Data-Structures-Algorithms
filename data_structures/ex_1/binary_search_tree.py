class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def depth_first_for_each(self, cb):
    print("This is the root root")
    root = self
    cb(root.value)
    cb(root.left.value)
    # current = self
    # prev = current
    # # go all the way to the smallest number
    # while current.left != None:
    #   if(current.left != None):

    #   prev = current
    #   current = current.left
    # cb(prev.value)


    def traverse():
      if root:
        self.traverse_depth(root)
    self.traverse()

    def traverse_depth(self, node):
      if(node.left != None):
        print("hit left")
        cb(node.value)
        self.traverse_depth(node.left)
      if(node.right != None):
        print("hit right")
        cb(node.value)
        self.traverse_depth(node.right)

    

  def breadth_first_for_each(self, cb):
    root = self
    print(self)
    cb(root.value)

    def traverse_breadth(self, node):
      if(node.left and node.right):
        cb(node.left.value)
        cb(node.right.value)
        self.traverse_breadth(node.left)
        self.traverse_breadth(node.right)
      elif(node.left and node.right == None):
        cb(node.left.value)
        self.traverse_breadth(node.left)
      elif(node.right and node.left == None):
        cb(node.right.value)
        self.traverse_breadth(node.right)
      else: 
        print("no more items left")

    def traverse(self):
      root = self
      if root:
        self.traverse_breadth( root)
  
    self.traverse()


  def insert(self, value):
    new_tree = BinarySearchTree(value)
    if (value < self.value):
      if not self.left:
        self.left = new_tree
      else:
        self.left.insert(value)
    elif value >= self.value:
      if not self.right:
        self.right = new_tree
      else:
        self.right.insert(value)

  def contains(self, target):
    if self.value == target:
      return True
    if self.left:
      if self.left.contains(target):
        return True
    if self.right:
      if self.right.contains(target):
        return True
    return False

  def get_max(self):
    if not self:
      return None
    max_value = self.value
    current = self
    while current:
      if current.value > max_value:
        max_value = current.value
      current = current.right
    return max_value
