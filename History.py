class History:
    states = []

    def push(self, state):
        self.__class__.states.append(state)

    def pop(self):
        lastIndex = len(self.__class__.states) - 1
        lastState = self.__class__.states[lastIndex]
        self.__class__.states.remove(lastState)

        return lastState
