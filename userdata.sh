sudo yum update -y
sudo yum install -y docker conntrack 
sudo usermod -aG docker ec2-user
sudo systemctl start docker
curl -LO "https://storage.googleapis.com/kubernetes-release/release/$(curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt)/bin/linux/amd64/kubectl"
curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
sudo chmod +x kubectl minikube-linux-amd64
sudo install kubectl /usr/bin/kubectl
sudo install minikube-linux-amd64 /usr/bin/minikube

sudo chmod 777 tools/* && sudo cp tools/* /usr/bin/
chmod +x bashrc && echo ". $PWD/bashrc" | sudo tee -a /etc/bashrc

minikube start --driver=none
