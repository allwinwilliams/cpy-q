class Cpyq():

    def __init__(self):
        self.Q=[]
        self.nq=["","","","","","","","",""]

    def copy_nq(self,n,s):
        self.nq[n-1]=s

    def paste_nq(self,n):
        return self.nq[n-1]

    def clear(self):
        self.Q.clear()

    def add_front(self, s):
        self.Q.insert(0,s)

    def add_back(self, s):
        self.Q.append(s)

    def add_n(self, s, n):
        if n<=len(self.Q):
            self.Q.insert(n-1,s)

    def del_front(self):
        if len(self.Q)==1:
            return self.Q[0]
        return self.Q.pop(0)

    def del_back(self):
        if len(self.Q)==1:
            return self.Q[0]
        return self.Q.pop()

    def del_n(self, n):
        if n<=len(self.Q):
            return self.Q.pop(n-1)
        return None

    def get_front(self):
        return self.Q[0]

    def get_back(self):
        return self.Q[len(self.Q)-1]

    def get_n(self, n):
        if n<=len(self.Q):
            return self.Q[n-1]
        return None

    def show(self):
            print("Q",self.Q)
