class FreqStack:

    def __init__(self):
        self.freq = {}       # val -> frequency
        self.group = {}      # frequency -> stack of values
        self.max_freq = 0

    def push(self, val: int) -> None:
        # Increase frequency
        self.freq[val] = self.freq.get(val, 0) + 1
        f = self.freq[val]

        # Put val into the stack corresponding to this frequency
        if f not in self.group:
            self.group[f] = []

        self.group[f].append(val)

        # Update highest frequency
        self.max_freq = max(self.max_freq, f)

    def pop(self) -> int:
        # Get most recently pushed value among max-frequency values
        val = self.group[self.max_freq].pop()

        # Decrease its frequency
        self.freq[val] -= 1

        # If no values remain at this frequency,
        # decrease max_freq
        if not self.group[self.max_freq]:
            self.max_freq -= 1

        return val