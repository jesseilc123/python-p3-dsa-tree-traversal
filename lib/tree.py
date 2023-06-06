class Tree:
  def __init__(self, root = None):
    self.root = root

  def get_element_by_id(self, id):
    result = None
    nodes_to_visit = [self.root]

    while len(nodes_to_visit) > 0:
      node = nodes_to_visit.pop(0)
      if node["id"] != id:
        # depth-first traversal
        # nodes_to_visit = node["children"] + nodes_to_visit
        # breadth-first traversal
        nodes_to_visit = nodes_to_visit + node["children"]
      else:
        result = node 
        break
    
    return result
  

