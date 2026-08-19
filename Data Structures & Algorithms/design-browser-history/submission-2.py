class Website:
    
    def __init__(self, url = '', prev = None, next = None):
        self.url = url
        self.prev = prev
        self.next = next


class BrowserHistory:

    def __init__(self, homepage: str):
        self.curr = Website(homepage)

    def visit(self, url: str) -> None:
        new_node = Website(url)          
        new_node.prev = self.curr        
        self.curr.next = new_node         
        self.curr = new_node             

    def back(self, steps: int) -> str:
        while steps > 0 and self.curr.prev is not None:
            self.curr = self.curr.prev
            steps -= 1
        return self.curr.url

    def forward(self, steps: int) -> str:
        while steps > 0 and self.curr.next is not None:
            self.curr = self.curr.next
            steps -= 1
        return self.curr.url
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)