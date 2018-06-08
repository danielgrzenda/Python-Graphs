import pytest
from graph import Node
from graph import Graph

def test_empty_node():
	"""
	tests creation of empty node
	"""
	a = Node({'A':[]})
	assert isinstance(a, Node)
	assert len(a.connections) == 0

def test_error_node():
    """
    tests creation of bad node
    Node({'a':'a'})
    have to pass since the test is written to test error
    """
    with pytest.raises(Exception):
    	a = Node({'a':'a'})

def test_good_node():
    """
    tests creation of good node
    Node({'A':['B','C']})
    """
    a = Node({'A':['B', 'C']})
    assert isinstance(a, Node)
    assert isinstance(a.connections, list)

def test_node_str():
	"""
	test that node representation of string is
	"{'name':['list','of','vertex']}"
	"""
	a = Node({'A':['B','C']})
	assert str(a) == "{'A':['B', 'C']}"

def test_empty_graph():
	"""
	tests creation of empty graph
	"""
	a = Graph([])
	assert isinstance(a, Graph)
	assert len(a) == 0

def test_graph_with_list():
	"""
	tests creation of the graph with a list of nodes
	"""
	node_list = []
	node_list.append(Node({'A':['B','C']}))
	node_list.append(Node({'B':['C','D']}))
	node_list.append(Node({'C':['D']}))
	node_list.append(Node({'D':['C']}))
	a = Graph(node_list)
	assert isinstance(a, Graph)
	assert len(a) == 4

def test_graph_with_list_fail():
	"""
	tests creation of the graph with a list
	this is an improper list and throws an error
	error should be raised
	"""  
	with pytest.raises(Exception) as e_info:
		node_list = ["slippery list"]
		node_list.append(Node({'A':"['B','C']"}))
		node_list.append(Node({'B':['C','D']}))
		node_list.append(Node({'C':['D']}))
		node_list.append(Node({'D':['C']}))
		Graph(node_list)

def test_graph_with_list_of_not_nodes():
	"""
	extra test added by me
	tests creation of graph by a proper list but not of type node
	error should be raised
	"""
	with pytest.raises(Exception):
		node_list = [1, 2, 3, 4]
		Graph(node_list)

def test_add_to_graph():
	"""
	create graph and add nodes in a loop
	"""
	a = Graph([])
	a.add(Node({'A':['B','C']}))
	a.add(Node({'B':['A','C']}))
	a.add(Node({'C':['B','A']}))
	assert isinstance(a, Graph)
	assert len(a) == 3

def test_add_not_type_node():
	"""
	test added by me
	tests type checking of what you are adding to the Graph
	error should be raised
	"""
	with pytest.raises(Exception):
		a = Graph([])
		a.add(1)

def test_graph_str():
	"""
	test string representation of the graphs
	should be
	"[{'A':"['B','C']"}, {'B':['C','D']}, {'C':['D']}]"
	"""
	node_list = []
	node_list.append(Node({'A':['B','C']}))
	node_list.append(Node({'B':['C','D']}))
	node_list.append(Node({'C':['D']}))
	a = Graph(node_list)
	assert str(a) == "[{'A':['B', 'C']}, {'B':['C', 'D']}, {'C':['D']}]"


def test_find_path_dfs():
	"""
	you should test with graphs that have 0, 1, 3 paths
	"""
	node_list = []
	a = Node({'A':['B','C']})
	b = Node({'B':['C','D']})
	c = Node({'C':['D']})
	d = Node({'D':[]})
	e = Node({'F':[]})
	node_list.append(a)
	node_list.append(b)
	node_list.append(c)
	node_list.append(d)
	node_list.append(e)
	g = Graph(node_list)
	assert g.find_path_dfs(a,e) == None
	assert g.print_path(g.find_path_dfs(a,b)) == 'A, C, D, B'
	assert g.print_path(g.find_path_dfs(a,c)) == 'A, C'
	assert g.print_path(g.find_path_dfs(a,a)) == 'A'

# def test_find_path_bi():
# 	"""
# 	you should test with graphs that have 0, 1, 3 paths
# 	"""
# 	pass

def test_find_all_paths(): 
	"""
	you should test with graphs that have 0, 1, 3 paths
	"""
	node_list = []
	a = Node({'A':['B','C']})
	b = Node({'B':['C','D']})
	c = Node({'C':['D']})
	d = Node({'D':[]})
	e = Node({'F':[]})
	node_list.append(a)
	node_list.append(b)
	node_list.append(c)
	node_list.append(d)
	node_list.append(e)
	g = Graph(node_list)
	assert [str(obj.name) for path in g.find_all_paths(a,a) for obj in path] == ['A']
	assert [str(obj.name) for path in g.find_all_paths(a,b) for obj in path] == ['A','B']
	assert [str(obj.name) for path in g.find_all_paths(a,c) for obj in path] == ['A','B','C','A','C']
 

def test_find_shortest_path(): 
	"""
	you should test with graphs that have 0, 1, 3 paths
	"""
	node_list = []
	a = Node({'A':['B','C']})
	b = Node({'B':['C','D']})
	c = Node({'C':['D']})
	d = Node({'D':[]})
	e = Node({'F':[]})
	node_list.append(a)
	node_list.append(b)
	node_list.append(c)
	node_list.append(d)
	node_list.append(e)
	g = Graph(node_list)
	assert g.find_shortest_path(a,e) == None
	assert g.print_path(g.find_shortest_path(a,b)) == 'A, B'
	assert g.print_path(g.find_shortest_path(a,d)) == 'A, B, C, D'
	assert g.print_path(g.find_shortest_path(a,a)) == 'A'

def test_has_route():
	"""
	you should test with graphs that have 0, 1, 3 paths
	"""
	node_list = []
	a = Node({'A':['B','C']})
	b = Node({'B':['C','D']})
	c = Node({'C':['D']})
	d = Node({'D':[]})
	e = Node({'F':[]})
	node_list.append(a)
	node_list.append(b)
	node_list.append(c)
	node_list.append(d)
	node_list.append(e)
	g = Graph(node_list)
	assert g.has_route(a,e) == False
	assert g.has_route(a,b) == True
	assert g.has_route(a,d) == True
	assert g.has_route(a,a) == True

