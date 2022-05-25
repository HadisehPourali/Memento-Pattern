from EditorState import EditorState


class Editor:

    def createState(self):
        return EditorState(self.content)

    def restore(self, state):
        self.content = state.getContent()

    def setContent(self, content):
        self.content = content

    def getContent(self):
        return self.content




