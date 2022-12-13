class xregister:
	def __init__(self, queue_length, init_value = 0):
		#self.cycle = 0
		#self.queue = [None] * queue_length
		
		self.cycle = 1
		self.xval = init_value
		
		self.signal_strengths = []

		self.image = ""
		self.append_image()

	def parse_instruction(self, instruction):
		if instruction is None or instruction == "noop":
			self.advance_cycle()
		elif instruction.startswith("addx "):
			self.advance_cycle(1)
			self.xval += int(instruction[5:])
			self.advance_cycle(1)

			
			#self.print_state()

			
			#self.advance_cycle()
		
		#self.print_state()
		
	def advance_cycle(self, amount = 1):
		for i in range(amount):
			self.append_image()
			self.cycle += 1

			if (self.cycle - 20) % 40 == 0:
				print(f"Signal strength during Cycle {self.cycle}: {my_reg.get_signal_strength()}")

	def append_image(self):
		self.image += "#" if self.cycle % 40 in range(self.xval - 1, self.xval + 1 + 1) else "."

	def get_xval(self):
		return self.xval

	def print_state(self):
		print(f"Start of Cycle {self.cycle}: {self.xval}")

	def get_cycle(self):
		return self.cycle
	
	def get_signal_strength(self):
		signal_strength = self.xval * self.cycle
		self.signal_strengths.append(signal_strength)
		return signal_strength

	def get_SS_sum(self):
		return sum(self.signal_strengths)
	
	def draw_image(self, image_width = 40):
		lines = [self.image[i:i+image_width] for i in range(0, len(self.image), image_width)]
		print(*lines, sep = "\n")

instructions = [line.rstrip() for line in open("input.txt", "r")]

my_reg = xregister(queue_length=2, init_value=1)

for instruction in instructions:
	my_reg.parse_instruction(instruction)

print(f"Sum of signal strengths is: {my_reg.get_SS_sum()}")
my_reg.draw_image()
	#my_reg.print_state()
