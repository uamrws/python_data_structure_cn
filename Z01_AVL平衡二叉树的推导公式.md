## AVL平衡二叉树的推导公式

![右旋转示例图](/Users/uamrws/Desktop/右旋转示例图.jpg)

<h3><center>右旋转示例图(Figure 1)</center></h3>

基于FIgure1 我们看到了树的右旋转操作:

实际发生节点平衡因子变动的只有E节点和C节点，其他节点的平衡因子实际未产生变化,可做如下推导

```
设节点A为根节点，其左节点为B
现对该树进行右旋

原根节点A的平衡因子表达式记为：
f(OA) = h(B) - h(OAR) 
⇒ f(OA) = 1+max(h(OBL),h(OBR)) - h(OAR) 
⇒ h(OAR) = 1+max(h(OBL),h(OBR)) - f(OA) 

原左节点B的平衡因子表达式记为：
f(OB) = h(OBL) - h(OBR) 
⇒ h(OBL) = f(OB) +h(OBR) 

右旋后根节点的平衡因子表达式记为：
f(NA) =h(OBR) - h(OAR) 
⇒ f(NA) = h(OBR) -1-max(h(OBL),h(OBR))+ f(OA)
⇒ f(NA) = f(OA) -1+min(h(OBR)-h(OBL), 0) 
⇒ f(NA) =f(OA) -1-max(f(OB), 0)
右旋后节点B的平衡因子表达式记为：
f(NB) = h(OBL) - h(NA) 
⇒ f(NB) = h(OBL) - 1-max(h(OBR), h(OAR)) 
⇒ f(NB) = f(OB) -1+h(OBR)-max(h(OBR), h(OAR))
⇒ f(NB) = f(OB) - 1+ min(0, f(NA))
```

以同样方式可以推导左旋公式如下

```
设节点A为根节点，其右节点为B
现对该树进行左旋

原根节点A的平衡因子表达式记为：
f(OA) = h(OAL) - h(B) 
⇒ f(OA) = h(OAL)- 1 - max(h(OBL), h(OBR))
⇒ h(OAL) =  f(OA) + 1 + max(h(OBL), h(OBR))

原右节点B的平衡因子表达式记为：
f(OB) = h(OBL) - h(OBR) 
⇒ h(OBR) = h(OBL) - f(OB) 

左旋后根节点的平衡因子表达式记为：
f(NA) =h(OAL) - h(OBL) 
⇒ f(NA) = f(OA) + 1 + max(h(OBL), h(OBR))- h(OBL)
⇒ f(NA) = f(OA) + 1 + max(0, h(OBR)- h(OBL)) 
⇒ f(NA) =f(OA) + 1 - min(0, f(OB))  
左旋后节点B的平衡因子表达式记为：
f(NB) = h(NA) - h(OBR) 
⇒ f(NB) = 1+max(h(OAL), h(OBL)) - h(OBR)
⇒ f(NB) = 1+max(h(OAL), h(OBL)) - h(OBL) + f(OB)
⇒ f(NB) = f(OB) + 1 + max(f(NA), 0) 
```



























