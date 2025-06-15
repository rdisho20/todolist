class Todo:
    COMPLETED = "X"
    NOT_COMPLETED = " "

    def __init__(self, title):
        self._title = title
        self.done = False

    def __str__(self):
        marker = Todo.COMPLETED if self.done else Todo.NOT_COMPLETED
        return f"[{marker}] {self.title}"
    
    def __eq__(self, other):
        if not isinstance(other, Todo):
            return NotImplemented

        return self.title == other.title and self.done == other.done

    @property
    def title(self):
        return self._title
    
    @property
    def done(self):
        return self._done
    
    @done.setter
    def done(self, done):
        self._done = done


class TodoList:
    def __init__(self, title):
        self._title = title
        self._todos = []
    
    @property
    def title(self):
        return self._title
    
    def add(self, todo):
        if not isinstance(todo, Todo):
            raise TypeError
        
        self._todos.append(todo)
    
    def __str__(self):
        output_lines = [f"---- Today's Todos ----"]
        output_lines += [str(todo) for todo in self._todos]
        return '\n'.join(output_lines)
    
    def __len__(self):
        return len(self._todos)
    
    def first(self):
        return self._todos[0]

    def last(self):
        return self._todos[-1]
    
    def to_list(self):
        return self._todos.copy()
    
    def todo_at(self, index):
        return self._todos[index]
    
    def mark_done_at(self, index):
        self._todos[index].done = True

    def mark_undone_at(self, index):
        self._todos[index].done = False

    def mark_all_done(self):
        def mark_done(todo):
            todo.done = True

        self.each(mark_done)

    def mark_all_undone(self):
        def mark_undone(todo):
            todo.done = False

        self.each(mark_undone)
    
    def all_done(self):
        # all() returns True if list is empty
        return all(todo.done for todo in self._todos)
    
    def remove_at(self, index):
        self._todos.pop(index)
    
    def each(self, callback):
        for todo in self._todos:
            callback(todo)
    
    def select(self, callback):
        result = TodoList(self.title)

        def choose(todo):
            if callback(todo):
                result.add(todo)
        
        self.each(choose)
        return result
    
    def find_by_title(self, title):
        found = self.select(lambda todo: title == todo.title)
        return found.todo_at(0)
    
    def done_todos(self):
        return self.select(lambda todo: todo.done)

    def undone_todos(self):
        return self.select(lambda todo: not todo.done)
    
    def mark_done(self, title):
        done = self.find_by_title(title)
        done.mark_done_at(0)


empty_todo_list = TodoList('Nothing Doing')

def setup():
    todo1 = Todo('Buy milk')
    todo2 = Todo('Clean room')
    todo3 = Todo('Go to gym')

    todo2.done = True

    todo_list = TodoList("Today's Todos")
    todo_list.add(todo1)
    todo_list.add(todo2)
    todo_list.add(todo3)

    return todo_list

def step_8():
    print('--------------------------------- Step 8')
    todo_list = setup()

    print(todo_list)
    # ---- Today's Todos -----
    # [ ] Buy milk
    # [X] Clean room
    # [ ] Go to gym

    todo_list.mark_all_done()
    print(todo_list)
    # ---- Today's Todos -----
    # [X] Buy milk
    # [X] Clean room
    # [X] Go to gym

    todo_list.mark_all_undone()
    print(todo_list)
    # ---- Today's Todos -----
    # [ ] Buy milk
    # [ ] Clean room
    # [ ] Go to gym

step_8()