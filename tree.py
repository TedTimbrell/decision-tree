from mldata import parse_c45

class DecisionTree(Object):

	def DecisionTree(self):
		self.continuous_splits = {}
		self.features = []

	def set_presorted_splits(dataset, feat_index):
		attrs_list = sorted([ex[feat_index] for ex in dataset])
		self.continuous_splits[feat_index] = []
		for i in range(len(attrs_list) - 1):
			self.continuous_splits[feat_index].append((attrs_list[i+1] - attrs_list[i])/2.0)

	def build(self, dataset):
		self.features = dataset.schema
		for index, feature in enumerate(self.features):
			if feature.type == 'CONTINUOUS':
				self.set_presorted_splits(dataset, index)

	@staticmethod
	def _check_purity(dataset, index):
		prior = None
		for example in dataset:
			if prior is not None or example[index] != prior:
				return False
			prior = example[index]
		return True

	def id3(dataset, class_index, remaining_features):
		pass

	@staticmethod
	def parse(filepath):
		return exset = parse_c45(filepath)