# Node
class ImageNode:
    def __init__(self, image):
        self.image = image
        self.prev = None
        self.next = None


current = None


# Add image (like visit)
def add_image(image):
    global current

    new_node = ImageNode(image)

    if current is None:
        current = new_node
    else:
        # delete forward images
        current.next = None

        new_node.prev = current
        current.next = new_node
        current = new_node

    print("Viewing:", image, "\n")


# View previous image
def view_previous():
    global current

    if current is None or current.prev is None:
        print("No previous image\n")
        return

    current = current.prev
    print("Viewing:", current.image, "\n")


# View next image
def view_next():
    global current

    if current is None or current.next is None:
        print("No next image\n")
        return

    current = current.next
    print("Viewing:", current.image, "\n")


# Show all images
def show_gallery():
    if current is None:
        print("Gallery is empty\n")
        return

    temp = current

    # go to first image
    while temp.prev:
        temp = temp.prev

    print("Gallery:")
    while temp:
        print(temp.image, end=" -> ")
        temp = temp.next
    print("END\n")


# Menu
while True:
    print("1. Add Image")
    print("2. View Previous")
    print("3. View Next")
    print("4. Show Gallery")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == '1':
        image = input("Enter image name: ")
        add_image(image)

    elif choice == '2':
        view_previous()

    elif choice == '3':
        view_next()

    elif choice == '4':
        show_gallery()

    elif choice == '5':
        print("Exiting...")
        break

    else:
        print("Invalid choice\n")