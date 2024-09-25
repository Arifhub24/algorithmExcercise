import heapq

class Edge:
	def __init__(self, weight, start_vertex, target_vertex):
		self.weight = weight
		self.start_vertex = start_vertex
		self.target_vertex = target_vertex


class Node:
	def __init__(self, name):
		self.name = name
		self.visited = False
		self.neighbors = []
		self.predecessor = None
		self.min_distance = float('inf')

	def __lt__(self, other_node):
		return self.min_distance < other_node.min_distance

	def add_edge(self, weight, target_vertex):
		edge = Edge(weight, self, target_vertex)
		self.neighbors.append(edge)

		


class Dijstra:
	def __init__(self):
		self.heap = []

	def calculate(self, start_vertex):
		start_vertex.min_distance = 0
		heapq.heappush(self.heap, start_vertex)
		while self.heap:
			current_vertex = heapq.heappop(self.heap)
			if current_vertex.visited:
				continue
			for edge in current_vertex.neighbors:
				start = edge.start_vertex
				target = edge.target_vertex
				new_distance = start.min_distance + edge.weight
				if new_distance < target.min_distance:
					target.min_distance = new_distance
					heapq.heappush(self.heap, target)
					target.predecessor = current_vertex
			current_vertex.visited = True


	def get_shortest_path(self, start_point):
		print(f"the shortest path is {start_point.min_distance}")
		start = start_point
		path = ""
		while start is not None:
			path = start.name + ' ' + path 
			start = start.predecessor
		print(path)

	def show_shortest_path(self, target_vertex):
		return target_vertex.name, target_vertex.min_distance









____________________________ instance __________________________________

if __name__ == '__main__':
	nodeA = Node("A")
	nodeB = Node("B")
	nodeC = Node("C")
	nodeD = Node("D")
	nodeE = Node("E")
	nodeF = Node("F")
	nodeG = Node("G")
	nodeH = Node("H")

	nodeA.add_edge(6, nodeB)
	nodeA.add_edge(9, nodeD)
	nodeA.add_edge(10, nodeC)

	nodeB.add_edge(16, nodeE)
	nodeB.add_edge(13, nodeF)
	nodeB.add_edge(5, nodeD)

	nodeC.add_edge(6, nodeD)
	nodeC.add_edge(5, nodeH)
	nodeC.add_edge(21, nodeG)

	nodeD.add_edge(8, nodeF)
	nodeD.add_edge(7, nodeH)

	nodeE.add_edge(10, nodeG)

	nodeF.add_edge(4, nodeE)
	nodeF.add_edge(12, nodeG)

	nodeH.add_edge(2, nodeF)
	nodeH.add_edge(14, nodeG)
