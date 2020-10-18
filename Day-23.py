def levelOrder(self,root):
    if root is None:
        return 0
    thislevel = [root]
    results = []
    while thislevel:
        nextlevel = []
        for n in thislevel:
            results.append(n.data)
            if n.left:
                nextlevel.append(n.left)
            if n.right:
                nextlevel.append(n.right)
        thislevel=nextlevel
    final = ' '.join(str(e) for e in results)    
    print (final)