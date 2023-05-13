class Node:

    def __init__(self, data):
        self.value = data
        self.next = None

class Parent:

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def print_single_linked_list(self):
        # Validamos si la lista está vacía
        if not self.head:
            return print('La lista no tiene nodos')
        else:
            current_node = self.head
            while current_node:
                print(current_node.value)
                current_node = current_node.next

    def add_node_at_end(self, data):
        new_node = Node(data)
        # 1. Valido si la lista tiene al menos un nodo
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        # 2. Validar cuando al menos existe un nodo
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def add_node_at_start(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1

    def delete_at_end(self):
        if not self.head:
            return print('Lista vacìa, nada que eliminar')     
        elif self.length == 1:
            self.head = None
            self.tail = None
            self.length -=1
        else:
            current_node = self.head
            new_tail = current_node
            while current_node.next != None:
                new_tail = current_node
                #Pasamos a visitar el sgte nodo de la lista:
                current_node = current_node.next
            print('Nodo a eliminar es ', self.tail.value)
            self.tail = new_tail
            self.tail.next = None
            self.length -= 1
    
    def delete_at_start(self):
        if not self.head:
            return print('Lista vacía, nada que eliminar')     
        elif self.length == 1:
            self.head = None
            self.tail = None
            self.length -=1
        else:
            current_node = self.head
            print('Nodo a eliminar es ', current_node.value)
            self.head = current_node.next
            current_node = None
            self.length -=1

    def get_value_node_by_index(self, index):
        #Validar que el indice suministrado si se encuentre en la lista
        if index < 1 and index > self.length:
            return print('Indice fuera del rango')
        elif index == 1:
            return self.head
        elif index == self.length:
            return self.tail
        else:
            current_node = self.head
            contador_nodos_visitados = 1
            while index != contador_nodos_visitados:
                current_node = current_node.next
                contador_nodos_visitados += 1
            return current_node
    
    def remove_node_by_index(self, index):
        if index == 1:
            self.delete_at_start()
        elif index == self.length:
            self.delete_at_end()
        else:
            remove_node = self.get_value_node_by_index(index)
            #Validar si si se encuentra el nodo a eliminar
            if remove_node != None:
                previous_node = self.get_value_node_by_index(index-1)
                previous_node.next = remove_node.next
                remove_node = None
                self.length -= 1
    
    def remove_node_by_value(self, data):
        i = 1
        current_node = self.head
        while i <= self.length :
            if current_node.value == data:
                self.remove_node_by_index(i)
                i = self.length + 1
            else:
                current_node = current_node.next
                i += 1
        #Implementar
    
    def reverse_single_linked_list(self):
        previous = None
        current = self.head
        next = None
        
        while (current is not None):
            next = current.next
            current.next = previous
            previous = current
            current = next
        
        self.head = previous  
        # |1|2|3|4| -> |4|3|2|1|
    
    def get_value_middle_node(self):
        current_node = self.head
        mitad = self.length/2
        i = 1.0
        if (self.length%2 != 0):
            mitad = (self.length/2)+0.5
        while (i < mitad):
            current_node = current_node.next
            i+=1
        print(current_node.value)
        # Obtener valor del nodo de la mitad de la lista
    
    def add_odd_values_at_end(self, data):
        if(data%2 == 0):
            new_node = Node(data)
            if self.head == None:
                self.head = new_node
                self.tail = new_node
            else:
                self.tail.next = new_node
                self.tail = new_node
            self.length += 1
        # Añadir al final únicamente valores pares

    def add_not_odd_values_at_start(self, data):
        if(data%2 != 0):
            new_node = Node(data)
            if self.head == None:
                self.head = new_node
                self.tail = new_node
            else:
                new_node.next = self.head
                self.head = new_node
            self.length += 1
        # Añadir a la inicio únicamente valores impares
    
    def get_sum_all_values(self):
        current_node = self.head
        i = 0
        valor = 0
        while i < self.length:
            valor += current_node.value
            current_node = current_node.next
            i += 1
        return(valor)
        # Obtener el valor de la suma de todos los nodos de la lista