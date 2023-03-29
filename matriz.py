from listas_enlazadas import LinkedList

class Matrix:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.head = None

    def add_row(self, values):
        if len(values) != self.columns:
            raise ValueError("The length of values should be equal to the number of columns")
        new_row = LinkedList()
        for value in values:
            new_row.add_node(value)
        if self.head is None:
            self.head = new_row
        else:
            current_row = self.head
            while current_row.next_node is not None:
                current_row = current_row.next_node
            current_row.next_node = new_row

    def get_value(self, row, column):
        if row < 0 or row >= self.rows or column < 0 or column >= self.columns:
            raise ValueError("Invalid row or column index")
        current_row = self.head
        for i in range(row):
            current_row = current_row.next_node
        current_cell = current_row.head
        for j in range(column):
            current_cell = current_cell.next_node
        return current_cell.value
    
matrix = Matrix(3, 3)
matrix.add_row([1, 2, 3])
matrix.add_row([4, 5, 6])
matrix.add_row([7, 8, 9])

value = matrix.get_value(1, 1)
print(value)