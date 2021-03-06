# 資料結構-二元樹/binary-search tree



## 一、樹的基本結構:
  
  **`節點(Node)`** <br/>
  **`父節點`** 圖例1 : `A、B、C、` <br/>
  **`子節點`** 圖例1 : `B、C、D、E、F、G`
  
  1. **`根節點(root)`**:第一個節點，而這個節點它上面並不會有父節點。圖例1:A節點 
    
  2. **`葉節點(leaf)`**:有父節點，但是沒有子節點。圖例1:D、E、F、G
  
  3. **`非終端節點`**:除了 **`葉節點(leaf)`**，其它的都是非終端節點。
  
  4. **`祖先節點`**: **`從根節點(root)`** 到所指定節點的路徑上所經過的節點，除了指定節點，路徑上的都是祖先節點。圖例1 : **`A → E`** **`祖先節點`** : **A**、**B**
  
  5. **`分支度(degree)`**:一個節點所擁有的子節點數，為該節點的分支度。因為是介紹**二元樹**，所以該樹的分支度會是為2。
  
  6. **`階層(level)`**:樹根level為 1 ，有子節點的話，該子節點的 **`階層(level) = 父節點的階層數 + 1`**，所以以圖例1的 **B節點** 就會是 **` 1 (A's level) + 1 = 2 (B's level)`**
  
  7. **`樹高(height)`** or **`樹深(depth)`**:為該樹的 **`最大階層數(Max level)`**。圖例1 : height = 3
  
  * 圖例1
  
               A  level:1 
             /   \
            B     C level:2
           / \   / \
          D   E F   G level:3
## 二、二元樹介紹:
   1. 走訪方式:**`中序走訪(LDR)、前序走訪(DLR)、後序走訪(LRD)`**
     

