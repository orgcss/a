# oracle cloud日记 
## 开通
普通登录cloud.oracle.com, 选中国，常用region选usEast.验证email,cellphone,mastercard, done. 
## 使用
找半天找到create instance入口，建了个arm的2core12G arm ubuntu
## 登录
22登录public ip. 装xfce4,xrdp,echo xfce4-session>~/.xsession;passwd ubuntu, done
## xrdp
xrdp连不上！。 找半天，才发现它的ubuntu image的iptables默认一堆设置，-F后成功。
之前有建及改security group(这个菜单也很不好找),不知道那个有没有起作用。
对了，google搜索方案时第一个方案指向oracle的收费support. 看来oracle的免费使用，是想要在support上收费，这也太猴急了点。。
## 体验
xrdp远程桌面，慢就一个字。不知道是网络，还是机器。。估计就是机器很慢。所谓arm 2core12G, 性能不行。打开openai.com,卡在主页动画。
## chatGPT
关掉openai.com,直接chat.openai.com,直接you do not have access. 看来openai这孙子只对MS的机器开放。。

# 总结：xrdp连接oracle arm机器慢不稳定；oracle arm机器慢；oracle配置项隐晦，很多导向它的收费support；chatGPT只对MS上的win机器开放；
