# 遞迴走訪
root = None # 根節點
class TreeNode(): # 樹節點
    def __init__(self,data):
        self.value = data
        self.left_node = None
        self.right_node = None
        return

class binary_tree():
    def __init__(self):
        return
    def insertnode(data):
        global root
        if (root == None):
            root = TreeNode(data)
        else:
            current_node = root
            while(True):
                tempParent = current_node
                if (data <= current_node.value):
                    current_node = current_node.left_node
                    if(current_node == None):
                        tempParent.left_node = TreeNode(data)
                        return
                else:
                    current_node = current_node.right_node
                    if(current_node == None):
                        tempParent.right_node = TreeNode(data)
                        return
    def TreeTraversal_inorder(node): # 遞迴中序法 LDR
        if(node != None):
            binary_tree.TreeTraversal_inorder(node.left_node)
            print(node.value,end=" ")
            binary_tree.TreeTraversal_inorder(node.right_node)
    def TreeTraversal_preoder(node): # 遞迴前序法 DLR
        if(node != None):
            print(node.value,end=" ")
            binary_tree.TreeTraversal_preoder(node.left_node)
            binary_tree.TreeTraversal_preoder(node.right_node)
    def TreeTraversal_postorder(node): # 遞迴後序法 LRD
        if(node != None):
            binary_tree.TreeTraversal_postorder(node.left_node)
            binary_tree.TreeTraversal_postorder(node.right_node)
            print(node.value,end=" ")
            
        
        
def main():
    my_tree = binary_tree
    print("原始資料:")
    all_data = [ -45,-48,-40,8,-3,-26,-29,-17,-7,46,17,29,27,32] # 輸入資料
    for num in all_data:
        print(num,end=" ")
        my_tree.insertnode(num)
    print()
    print("遞迴中序法:")
    my_tree.TreeTraversal_inorder(root)
    print()

    print("遞迴前序法:")
    my_tree.TreeTraversal_preoder(root)
    print()
    
    print("遞迴後序法:")
    my_tree.TreeTraversal_postorder(root)
    print()

if __name__ == '__main__':    
    main()
