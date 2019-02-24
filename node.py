class Node(Object):

	class Type():
		LEAF = 'leaf'
		INTERNAL = 'internal'

	@staticmethod
    def pure_node(class_label):
        """
        Create a pure node which returns the given class label"""
        return Node(node_type=Node.Type.LEAF, label=class_label)

	def Node(self, node_type, children=None):
		pass
