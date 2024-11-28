class TodoList:
    def __init__(self, todos):
        self.todos = todos
    
    def __str__(self):
        return f"Todo: {self.todos}"
    
    def __add__(self, todo):
        return TodoList(self.todos + [todo])
    

todo_list = TodoList(["CallHarry", "Clean Sink"])
todo_list = todo_list + "Read Book"
print(todo_list)