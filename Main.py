from Editor import Editor
from History import History

editor = Editor()
history = History()

editor.setContent("a")
history.push(editor.createState())

editor.setContent("b")
history.push(editor.createState())

editor.setContent("c")
editor.restore(history.pop())  #return b
editor.restore(history.pop())  #return a

print(editor.getContent())

