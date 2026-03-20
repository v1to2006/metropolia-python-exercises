class Utils:
	@staticmethod
	def clamp(current, min_number, max_number) -> int:
		if current > max_number:
			return max_number
		elif current < min_number:
			return min_number
		else:
			return current