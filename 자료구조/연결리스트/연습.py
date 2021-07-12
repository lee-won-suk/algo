# 노드 구현
class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next

# 노드 mgmt
class NodeMgmt:

 #생성자
 def __init__(self,data):
     self.head=Node(data)

 #1 add
 def add(self,data):
 #-1 head가 없을 경우
    if self.head=="":
        self.head=Node(data)
 #-2 나머지 경우
    else:
        node=self.head
        while node.next:
            node=node.next
        node.next=Node(data) # 이부분 실수. node가 아니라 node.next에 연결해줬어야 한다.

 #2 desc
 def desc(self):
        node=self.head
        while node:
            print(node.data)
            node=node.next

 #3 delete
 def delete(self,data):
 #-1 head가 없을 경우
    if self.head=="":
        return
 #-2 head가 찾던 원소일 경우
    elif self.head.data==data:
        temp=self.head
        self.head=self.head.next
        del temp
 #-3 나머지 경우
    else:
        node=self.head
        while node.next:
            if node.next.data==data:
                temp=node.next
                node.next=node.next.next
                del temp
            else:
                node=node.next # 실수 :찾던 노드가 아니면 넘어가야 한다.

 #4 search_node
 def search_node(self,data):
    node=self.head
    #-1 현재원소가 찾던 원소일 경우
    while node:
        if node.data==data:
            return node
 #아닐경우
        else:
            node=node.next