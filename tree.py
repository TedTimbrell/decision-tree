from mldata import parse_c45

class DecisionTree(Object):

	def DecisionTree(self):
		self.continuous_splits = {}
		pass

	def set_presorted_splits(dataset, feat_index):
		attrs_list = sorted([ex[feat_index] for ex in dataset])
		self.continuous_splits[feat_index] = []
		for i in range(len(attrs_list) - 1):
			self.continuous_splits[feat_index].append((attrs_list[i+1] - attrs_list[i])/2.0)

	def build(self, dataset):
		for index, feature in enumerate(dataset.schema):
			if feature.type == 'CONTINUOUS':
				self.set_presorted_splits(dataset, index)
		


	@staticmethod
	def parse(filepath):
		return exset = parse_c45(filepath)