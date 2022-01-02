class Task:
    def __init__(self, name, due_date):
        self.name = name
        self.due_date = due_date
        self.comments = []
        self.completed = False

    def change_name(self, new_name:str):
        if self.name != new_name:
            previous_name = self.name
            self.name = new_name
            return new_name
        else:
            return "Name cannot be the same."

    def change_due_date(self, new_date: str):
        if self.due_date == new_date:
            return "Date cannot be the same."
        self.due_date = new_date
        return self.due_date

    def add_comment(self, comment: str):
        self.comments.append(comment)

    def edit_comment(self,comment_number: int, new_comment: str):
        if comment_number in range(len(self.comments)):
            self.comments[comment_number] = new_comment
            return ", ".join(self.comments)
        else:
            return "Cannot find comment."

    def details(self):
        return f"Name: {self.name} - Due Date: {self.due_date}"




class Section:
    def __init__(self, name):
        self.name = name
        self.tasks = []
