yum install docker
sudo usermod -a -G docker ec2-user
systemctl enable docker
sudo curl -L https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m) -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose

yum install git -y

search shuffler github and follow install doc.

