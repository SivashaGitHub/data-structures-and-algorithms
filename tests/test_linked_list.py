from data_structures_and_algorithms.Data_Structures.linked_list.linked_list import LinkedList,Node

def test_linked_list_creation():
    ll= LinkedList()
    assert ll.head == None

def test_node_apples():
    node = Node("a")

    assert node.value == "a"
    assert node.next ==None

def test_letters():
    string = LinkedList()
    string.head = Node("a")
    string.head.next= Node("b")    

    assert string.head.next.value =="b"

def test_insert_letters():
    string = LinkedList()
    string.insert("a")
    string.insert("b")
    string.insert("c")
    #string.insert("d")

    assert string.head.value == "c"
    assert string.head.next.value == "b"
    assert string.head.next.next.value =="a"
    
def test_includes():
    string = LinkedList()
    string.insert("a")
    string.insert("b")
    string.insert("c")
    #string.insert("d")

    assert string.includes("a") 
    assert string.includes ("d") == False


def test_string_list():
    string = LinkedList()
    string.insert("a")
    string.insert("b")
    string.insert("c")
    #actual = string.__str__()
    actual = string.toString()
    print (actual)
    assert actual == "{ c } -> { b } -> { a } -> NULL"





