# jupyter-notebook
on ubuntu20.04 server: sudo apt-get install jupyter-notebook

jupyter notebook --ip 0.0.0.0 --port 8888 & #to start the server so you can access from your desktop browser.

alternatively, you can do jupyter notebook --generate-config to generate config file and edit it for listen ip and port.

# R support on jupyter notebook
on ubuntu20.04:
```
sudo apt-get install r-base
sudo apt-get install jupyter # to install jupyter otherwise bellow will fail
R
install.packages('IRkernel')
IRkernel::installspec() # need jupyter, or check path by install.packages("devtools"), system.file('kernelspec', package = 'IRkernel')
```
restart jupyter then you have R on jupyter notebook.

try bellow commands:
```
a<-c(1,5,8,2,3)
sort(a)
table(a)
as.data.frame(a)
library()
```
