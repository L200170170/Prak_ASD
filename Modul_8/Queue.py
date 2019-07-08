class queue:
    def __init__(self):
        self.qlist=[]

    def Empty(self):
        return len(self)==0

    def __len__(self):
        return len(self.qlist)

    def enqueue(self,data):
        self.qlist.append(data)

    def dequeue(self):
        assert not self.Empty(),'gak ada isinya'
        return self.qlist.pop(0)

#nomer 4.1
    def depan(self):
        return self.qlist[0]
#nomer 4.2
    def belakang(self):
        return self.qlist[-1]


class pri:
    def __init__(self):
        self.qlist=[]

    def Empty(self):
        return len(self)==0

    def __len__(self):
        return len(self.qlist)

    def enqueue(self,data,priority):
        entry = prioq(data,priority)
        self.qlist.append(entry)

#nomer 4.1
    def depan(self):
        x=self.qlist[0].priority
        m=0
        for i in range (len (self.qlist)):
            if x < self.qlist[i].priority:
                    x=self.qlist[i].priority
                    m=i
        return self.qlist[m]

#nomer 4.2
    def belakang(self):
        x=self.qlist[0].priority
        m=0
        for i in range (len (self.qlist)):
            if x > self.qlist[i].priority:
                    x=self.qlist[i].priority
                    m=i
        return self.qlist[m]

#nomer 5
    def dequeue(self):
        assert not self.Empty(),'gak ada isinya'
        x=self.qlist[0].priority
        m=0
        for i in range (len (self.qlist)):
            if x > self.qlist[i].priority:
                    x=self.qlist[i].priority
                    m=i
        return self.qlist.pop(m)

class prioq(object):
    def __init__(self,data,priority):
        self.data = data
        self.priority = priority

i=queue()
i.enqueue("k")
i.enqueue("l")
i.enqueue("m")
i.enqueue("n")
i.enqueue("o")

i.dequeue()

q=pri()
q.enqueue("k",3)
q.enqueue("l",5)
q.enqueue("m",1)
q.enqueue("n",2)
q.enqueue("o",4)

q.dequeue().data
