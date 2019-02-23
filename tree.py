from mldata import parse_c45

class DecisionTree(Object):

	def DecisionTree(self):
		pass

	def create_presorted_splits(dataset, feat_index):
		attr_class_pairs = sorted([ex[feat_index] for ex in dataset])
		for ex in 

	def build(self, dataset):
		self.continuous_splits = {}
		for index, feature in enumerate(dataset.schema):
			if feature.type == 'CONTINUOUS':



	@staticmethod
	def parse(filepath):
		return exset = parse_c45(filepath)