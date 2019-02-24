from mldata import parse_c45

class DecisionTree(Object):

	def DecisionTree(self):
		self.continuous_splits = {}
		self.features = []

	def set_presorted_splits(self, attrs_list, feat_index):
		self.continuous_splits[feat_index] = []
		for i in range(len(attrs_list) - 1):
			self.continuous_splits[feat_index].append((attrs_list[i+1] - attrs_list[i])/2.0)

	def build(self, dataset):
		self.features = dataset.schema
		for index, feature in enumerate(self.features):
			if feature.type == 'CONTINUOUS':
				attrs_list = sorted([ex[feat_index] for ex in dataset])
				self.set_presorted_splits(attrs_list, index)

	@staticmethod
	def _check_purity(self, dataset, index):
		prior = None
		for example in dataset:
			if prior is not None or example[index] != prior:
				return False
			prior = example[index]

		return True

	@staticmethod
	def _get_majority_class(self, dataset, class_index):
		class_counts = {}

		for example in dataset:
			if example[class_index] not in class_counts
				class_counts[example[class_index]] = 1
			else:
				class_counts[example[class_index]] += 1

		max_count = 0
		max_val = None
		for key, value in class_counts.items():
			if value > max_count:
				max_count = value
				max_val = key

		return max_val

	def _id3(self, dataset, class_index, remaining_feature_indecies):
		if self._check_purity(dataset, class_index):
			return Node.pure_node(dataset[0][class_index])
		elif not remaining_features:
			return Node.pure_node(self._get_majority_class(dataset, class_index))
		# Else continue to finding the best split



	@staticmethod
	def parse(filepath):
		return exset = parse_c45(filepath)