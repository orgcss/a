<pre>
numpy, scipy
matplotlib.pyplot
pandas, xlrd, xlsxwriter, openpyxl, csv;
sklearn:
  datasets; 
  classification; 
  nn; 
  svm;
theano(GIL问题，GPU计算，CUDA,OpenCL), keras; sympy(符号计算); tensorFlow; 
</pre>

## create jupyter notebook for machine learning
on aws ec2 ubuntu20.04:
```
  sudo apt install pip jupyter-notebook -y
  umask 002
  sudo python3 -m pip install numpy scipy pandas matplotlib 
  sudo python3 -m pip install -U scikit-learn
```
nohup jupyter notebook --ip 0.0.0.0 --port 8080 &

## open jupyter notebook:  http://ip:8080, new python, and try:
```
import sklearn as sk
print(sk.show_versions())
```
