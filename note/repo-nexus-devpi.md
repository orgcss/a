# nexus & devpi repo configuration
因为网络原因，没有一个本地maven或pypi缓存的话，重复install/build可能会很慢。让我们来架设简单的本地repo服务器。

## nexus
nexus为maven而生，新版本还支持pypi。

nexus安装很简单：下载、解压、启动。注意配置cache folder, proxy(在advanced里), repos. 

访问：http://localhost:8081/nexus/， 用户admin/admin123

注：
- 直接启动：./nexus start
- 注册systemd：sudo vim /etc/systemd/system/nexus.service
```
[Unit]
Description=apache nexus
After=network.target

[Service]
ExecStart=/media/data/app/nexus-2.15.1-02/bin/nexus start
ExecStop=/media/data/app/nexus-2.15.1-02/bin/nexus stop
User=css
#ExecReload=/media/data/app/nexus-2.15.1-02/bin/nexus restart
Restart=on-abort
Type=forking
TimeoutSec=600

[Install]
WantedBy=multi-user.target
```

## devpi
如果你的nexus是老版本不支持pypi, 那可以安装devpi。
```bash
python3.6 -m venv env36devpi
source env36devpi/bin/activate
pip install devpi-server devpi-web devpi-client
devpi-init --serverdir $repo_folder
devpi-gen-config --serverdir $repo_folder
sudo cp gen-config/devpi.service /etc/systemd/system/devpi.service
sudo systemctl start devpi.service
```
### 然后就可以访问http://localhost:3141/，也可以安装：
pip install xxx -i http://localhost:3141/root/pypi

- 会发现packages都缓存在serverdir下了并且在不断增长。
- 设国内源到~/.pip/pip.conf会让devpi快不少:
```
[global]
index-url = https://pypi.tuna.tsinghua.edu.cn/simple
[install]
trusted-host=mirrors.aliyun.com
```

## 附：wakeonlan在ubuntu18.04笔记本上似乎隔天失效
vim /etc/network/interfaces加以下内容不知道会不会解决：
```
auto eth0
iface eth0 inet static
  address 192.168.0.55
  netmask 255.255.255.0
  gateway 192.168.0.1
  up ethtool -s eth0 wol g
```
