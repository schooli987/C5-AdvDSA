import webbrowser

# Node
class Node:
    def __init__(self, url):
        self.url = url
        self.prev = None
        self.next = None
current = None
# Visit page
def visit(url):
    global current

    new_node = Node(url)

    if current is None:
        current = new_node
    else:
        # delete forward history
        current.next = None

        new_node.prev = current
        current.next = new_node
        current = new_node

    print("Visited:", url, "\nOpening in browser...\n")
    webbrowser.open(url)

# Menu (only visit)
while True:
    print("1. Visit Page")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == '1':
        url = input("Enter URL (https://...): ")
        visit(url)

    elif choice == '5':
        print("Exiting...")
        break

    else:
        print("Invalid choice\n")


        