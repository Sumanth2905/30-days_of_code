def insert(self,head,data):
        if head is None:  	#no node is present
            head = Node(data)
            self.tail = head
        else: 			#there are some nodes present
            node = Node(data)
            self.tail.next = node
            self.tail = node
        return head
