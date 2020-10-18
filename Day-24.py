def removeDuplicates(self,head):
    c = head
    while True:
        try:
            if c.data == c.next.data:
               c.next =  c.next.next
            else:  c  =  c.next
        except AttributeError: 
            return head