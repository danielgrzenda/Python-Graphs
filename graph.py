class Node(object):
	def __init__(self, node_dict):
		if not isinstance(node_dict,dict):
			raise TypeError(f'input must be a dictionary but was given {type(node_dict)}')
		if len(node_dict)>1:
			raise Error(f'the node dictionary can only contain one node but was given {len(node_dict)}')
		for key in node_dict:
			if not isinstance(node_dict[key],list):
				raise TypeError(f'the node dictionary must contain a list as values not {type(node_dict.values())}')
			self.name = key
			self.connections = node_dict[key]

	def get_name(self):
		return self.name

	def get_connections(self):
		return self.connections

	def __eq__(self, other):
		if self.name == other.name:
			if self.connections == other.connections:
				return True
		return False

	def __str__(self):
		return f"{{'{self.name}':{self.connections}}}"
	
class Graph(object):
	def __init__(self, node_list):
		if not isinstance(node_list, list):
			raise TypeError(f'must be initialized with a list of nodes but was {type(node_list)}')
		self.node_list = []
		for entry in node_list:
			if not isinstance(entry, Node):
				raise TypeError(f'each entry in node list must be of type node but found {type(entry)}')
			self.node_list.append(entry)

	def __len__(self):
		return len(self.node_list)

	def add(self, node):
		if not isinstance(node, Node):
			raise TypeError(f'input must be of type node but was {type(node)}')
		self.node_list.append(node)
		return None

	def delete(self, node):
		if not isinstance(node, Node):
			raise TypeError(f'input must be of type node but was {type(node)}')
		for n in self.node_list:
			if n == node:
				self.node_list.remove(n)
				return None
		raise TypeError(f'Node of key {node.get_name()} is not in the graph')		

	def find_path_dfs(self, start_node, end_node):
		self.check_node_inputs(start_node, end_node)
		if start_node == end_node:
			return [start_node]
		stack = []
		visited = []
		stack = stack + start_node.get_connections()
		visited.append(start_node)
		while len(stack)>0:
			node_name = stack.pop()
			new_node = self.get_node_by_label(node_name)
			print(new_node)
			if new_node in visited:
				continue
			visited.append(new_node)
			stack = stack + new_node.get_connections()
			if new_node == end_node:
				return visited
		return None


	# def find_path_bi(self, start_node, end_node):
	# 	self.check_node_inputs(start_node, end_node)
	# 	pass

	def find_all_paths(self, start_node, end_node, path=[]):
		self.check_node_inputs(start_node, end_node)
		path = path + [start_node]
		if start_node == end_node:
			return [path]
		paths = []	
		for label in start_node.connections:
			next_node = self.get_node_by_label(label)
			if next_node not in path:
				next_paths = self.find_all_paths(next_node, end_node, path)
				for a_path in next_paths:
	  				paths.append(a_path)
		return paths

	def find_all_paths_helper(self, start_node, end_node, path=[]):
		pass
	
	def find_shortest_path(self, start_node, end_node):
		self.check_node_inputs(start_node, end_node)
		if start_node == end_node:
			return [start_node]
		queue = []
		visited = []
		for entry in start_node.connections:
			queue.insert(0, entry)
		visited.append(start_node)
		while len(queue)>0:
			node_name = queue.pop()
			new_node = self.get_node_by_label(node_name)
			if new_node in visited:
				continue
			visited.append(new_node)
			for entry in new_node.connections:
				queue.insert(0,entry)
			if new_node == end_node:
				return visited
		return None

	def has_route(self, start_node, end_node):
		self.check_node_inputs(start_node, end_node)
		path = self.find_shortest_path(start_node, end_node)
		return not path==None

	def print_path(self, path):
		return ', '.join([node.get_name() for node in path])

	def __str__(self):
		s = ', '. join([str(node) for node in self.node_list])
		return '['+s+']'

	@staticmethod
	def check_node_inputs(start_node, end_node):
		if not isinstance(start_node, Node):
			raise TypeError(f'start_node must be of type Node not {type(start_node)}')
		if not isinstance(end_node, Node):
			raise TypeError(f'end_node must be of type Node not {type(end_node)}')
		return None

	def get_node_by_label(self, label):
		for node in self.node_list:
			if node.name == label:
				return node
		return None

class NoPathError(Exception):
    def __init___(self,dErrorArguments):
        Exception.__init__(self, f'my exception was raised with arguments {dErrorArguments}')
        self.dErrorArguments = dErrorArguements
