from minheap import MinHeap


def shortest(v):
    """calculates shortest distance by adding weights of all predecessors verts in path"""
    dist = 0
    while v.pred:
        dist +=  v.pred.get_weight(v)
        v = v.pred
    print dist



def dijkstra(graph, s, e):
    """Simple dijkstra algo to work out shortest path to an end node"""
   
    pq = MinHeap()
    # Set the distance for the start node to zero then build heap
    s.set_distance(0)
    pq.build_heap([(v.get_distance(),v) for v in graph])

    while not pq.is_empty():
        cv = pq.del_min()
        current_v = cv[1]
        current_v.set_as_visited()
        if current_v.get_key() == e.get_key():
        	break
        else:
	        for v in current_v.adj:
	            new_dist = current_v.get_distance() + current_v.get_weight(v)
	            if new_dist < v.get_distance():
	                v.set_distance(new_dist)
	                v.set_pred(current_v)
	                pq.decrease_val(v, new_dist)
    

	# if queue empties before end is found it means there are no paths from source to end
    if pq.is_empty() == True:
    	print 'No path to exists'
    else:
    	shortest(e)







