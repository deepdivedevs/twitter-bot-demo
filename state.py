import json

class State:
    def __init__(self):
        self.posted_links = set()
        self.filename = "state.json"

    def load(self):
        try:
            with open(self.filename, 'r') as f:
                links = json.load(f)
                self.posted_links = set(links)
        except FileNotFoundError:
            self.posted_links = set()

    def save(self):
        with open(self.filename, 'w') as f:
            json.dump(list(self.posted_links), f)

    def is_posted(self, link):
        return link in self.posted_links
    
    def add_link(self, link):
        self.posted_links.add(link)