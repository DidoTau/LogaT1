from Node import *

class Splay:
	def __init__(self):
		self.root = None

	
	def __search_tree_helper(self, node, key):
		if node == None or key == node.val:
			return node

		if key < node.val:
			return self.__search_tree_helper(node.left, key)
		return self.__search_tree_helper(node.right, key)


	# rotate left at node x
	def __left_rotate(self, x):
		y = x.right
		x.right = y.left
		if y.left != None:
			y.left.parent = x

		y.parent = x.parent
		if x.parent == None:
			self.root = y
		elif x == x.parent.left:
			x.parent.left = y
		else:
			x.parent.right = y
		y.left = x
		x.parent = y


	def __right_rotate(self, x):
		y = x.left
		x.left = y.right
		if y.right != None:
			y.right.parent = x
		
		y.parent = x.parent;
		if x.parent == None:
			self.root = y
		elif x == x.parent.right:
			x.parent.right = y
		else:
			x.parent.left = y
		
		y.right = x
		x.parent = y

	
	def __splay(self, x):
		while x.parent != None:
			if x.parent.parent == None:
				if x == x.parent.left:
					# zig rotation
					self.__right_rotate(x.parent)
				else:
					# zag rotation
					self.__left_rotate(x.parent)
			elif x == x.parent.left and x.parent == x.parent.parent.left:
				# zig-zig rotation
				self.__right_rotate(x.parent.parent)
				self.__right_rotate(x.parent)
			elif x == x.parent.right and x.parent == x.parent.parent.right:
				# zag-zag rotation
				self.__left_rotate(x.parent.parent)
				self.__left_rotate(x.parent)
			elif x == x.parent.right and x.parent == x.parent.parent.left:
				# zig-zag rotation
				self.__left_rotate(x.parent)
				self.__right_rotate(x.parent)
			else:
				# zag-zig rotation
				self.__right_rotate(x.parent)
				self.__left_rotate(x.parent)




	def search(self, k):
		x = self.__search_tree_helper(self.root, k)
		if x != None:
			self.__splay(x)



	
	def insert(self, key):
		node =  Node(key)
		y = None
		x = self.root

		while x != None:
			y = x
			if node.val < x.val:
				x = x.left
			else:
				x = x.right

		# y is parent of x
		node.parent = y
		if y == None:
			self.root = node
		elif node.val < y.val:
			y.left = node
		else:
			y.right = node
		# splay the node
		self.__splay(node)
	
	def reset(self):
		self.root = None