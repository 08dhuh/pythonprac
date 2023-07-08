class TreeNode:
    def __init__(self, story_piece):
        self.story_piece = story_piece
        self.choices = []

    def add_child(self, child):
        self.children.append(child)

    def remove_child(self, child):
        new_children = [ch for ch in self.children if ch.value != child.value]
        self.children = new_children
    
    def traverse(self):
        print(self.story_piece)
        if self.children:
            for child in self.children:
                child.traverse()

print('Once upon a time...')

story_root = TreeNode("""
You are in a forest clearing. There is a path to the left.
A bear emerges from the trees and roars!
Do you: 
1 ) Roar back!
2 ) Run to the left...
                      """
                      )
story_root.traverse()

# root = TreeNode("CEO")
# first_child = TreeNode("Vice-President")
# second_child = TreeNode("Head of Marketing")

# root.add_child(first_child)
# root.add_child(second_child)
# root.traverse()
