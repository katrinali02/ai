from expand import expand

#create node class
class Node:
	def __init__(self, state, parent=None):
		self.state = state
		self.parent = parent

#solution function
def solution(node):
	path = []
	#update parent node
	while node:
		path.insert(0, node.state)
		node = node.parent
	
	#get path
	return path


#a* function
def a_star_search(dis_map, time_map, start, end):
	
	#initalize list of nodes stored as tuples: (f, g, h, node_object)
	open_list = [(dis_map.get(start, {}).get(end, 0), 0, dis_map.get(start, {}).get(end, 0), Node(start))] 

	#track nodes already searched
	closed_list = set()

	#iterate thorugh nodes in open list, sort, pop one w lowest f/h value
	while open_list:
		open_list.sort(key=lambda x: (x[0], x[2])) 
		_, g, _, current_node = open_list.pop(0) 

		#check if arrived at target node
		if current_node.state == end:
			return solution(current_node)
		
		#add searched nodes to closed_list
		closed_list.add(current_node.state)

		#expand to get neighboring nodes
		for neighbor_state in expand(current_node.state, time_map):
			
			#create node object for neighbor, keep parent node reference
			if neighbor_state not in closed_list:
				neighbor_node = Node(neighbor_state, current_node)
                
                #calculate new g, h, and f values given neighboring nodes
				cost = time_map[current_node.state][neighbor_state]
				new_g = g + cost
				h = dis_map.get(neighbor_state, {}).get(end, 0)
				f = new_g + h
                
				#ensure open_list always contains lowest-costing path
				existing_node = next((item for item in open_list if item[3].state == neighbor_state), None)
				#check if neighbor is already in open_list w a higher (remove) or lower (add) cost
				if existing_node:
					if existing_node[1] <= new_g:
						continue
					else:
						open_list.remove(existing_node)
				open_list.append((f, new_g, h, neighbor_node))
    
	return None


#dfs function
def depth_first_search(time_map, start, end):

	#initialize starting point, stack, searched set
	start_node = Node(start)
	stack = [start_node]
	searched = set()

	while stack:
		
		#pop last node added to stack so code can explore other neighboring nodes
		node = stack.pop()

		#check if arrived at target node
		if node.state == end:
			return solution(node)
		
		#otherwise we expand and get neighbors of current node
		neighbors = expand(node.state, time_map)

		#check and add neighboring nodes to stack to be searched
		for neighbor in neighbors:
			if neighbor not in searched and not any(existing_node.state == neighbor for existing_node in stack): 
				stack.append(Node(neighbor,node))

	return None 


#bfs function
def breadth_first_search(time_map, start, end):
	
	#create queue of nodes in fringe
	fringe = [Node(start)] 

	#keep track of nodes searched already
	searched = set()

	while fringe: #while there are nodes in fringe list (exits if no nodes)
		
		#pop first node from queue
		node = fringe.pop(0)

		#check if arrived at target node
		if node.state == end:
			return solution(node)

		#mark node as searched
		searched.add(node.state)

		#check and add nodes to fringe to be searched
		for neighbor in expand(node.state, time_map):
			if neighbor not in searched and not any(n.state == neighbor for n in fringe): 
				fringe.append(Node(neighbor, node))
                
	return None