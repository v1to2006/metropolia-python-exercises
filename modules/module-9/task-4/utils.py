class Utils:
	@staticmethod
	def clamp(current, min, max) -> int:
		if current > max:
			return max
		elif current < min:
			return min
		else:
			return current