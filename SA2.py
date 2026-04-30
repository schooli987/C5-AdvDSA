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


# Go back
def go_back():
    global current

    if current is None or current.prev is None:
        print("No previous page\n")
        return

    current = current.prev
    print("Back to:", current.url, "\nOpening in browser...\n")
    webbrowser.open(current.url)


# Go forward
def go_forward():
    global current

    if current is None or current.next is None:
        print("No forward page\n")
        return

    current = current.next
    print("Forward to:", current.url, "\nOpening in browser...\n")
    webbrowser.open(current.url)


# Menu (visit + navigation)
while True:
    print("1. Visit Page")
    print("2. Back")
    print("3. Forward")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == '1':
        url = input("Enter URL (https://...): ")
        visit(url)

    elif choice == '2':
        go_back()

    elif choice == '3':
        go_forward()

    elif choice == '5':
        print("Exiting...")
        break

    else:
        print("Invalid choice\n")