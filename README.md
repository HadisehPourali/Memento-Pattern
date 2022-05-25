# Memento Pattern

we use this pattern for implement undo mechanism

we have three class:

### Editor class:

createState(): store the current state of Editor inside the state object(EditorState) and
returns it

restore(state): takes a state object and brings Editor back to that state

### EditorState class:

storing the state of Editor at the given time

### History class:

states: list

this class has state management responsibility

storing a list of Editor state(previous states) for undo mechanism

push(state): add a new state in history

pop(): remove and return last state


