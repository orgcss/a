# nn bp算法死磕

nn的backpropagation算法，是nn入门必修。以前写过，还成功过，今天重写，无论如何不收敛了！。 真气死我也。一早折腾到晚上11点，打算死磕到底！。
两层神经元，一层hidden一层output，基本框架：
```
  class nn:
    def __init__(s,eta): s.act=lambda x:1/(1+np.exp(-x))
    def fit(s,data,target):
    # for j in range(len(data)): dat,tgt=data[j:j+1], target[j:j+1] 不需要：走batch
      for i in range(100): # 或target-out2小于特定值？
        out1,out2=s.predict(data)
        s.w2+=s.eta*out1.T@((target-out2)*(1-out2)*out2)
        s.w1+=s.eta*data.T@((target-out2)@s.w2.T*(1-out1)*out1) # 或用(target-out2)*out2*(1-out2)作为误差来传递
    def predict(s,data):
      out1=s.act(data@s.w1)
      out2=s.act(out1@s.w2)
      return out1,out2
```
关键有几处：
## w1,w2用转置(n0,n1), (n1,n2)理解起来顺得多
## 梯度下降，方向不要走反了，学习速率eta选合适
## 批量，否则新加一个，跳跃一下，跳来跳去；training数据随机一下，否则突然跳跃，前功尽弃。
## 输入数据注意有坑！。 ndarray[:,:x]/10结果出其不意。
## 输入归一化，因为activation=1/(1+np.exp(-x))在(0,1)范围。
## 还不太理解为什么偏移量b可以忽略。
## 打印误差值以debug
