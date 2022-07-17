# cert and https and nginx

## get cert from ZeroSSL for free
- register on zeroSSL
- certificates --> fill in domain, etc
- validate via cname: goto your domain, add a record pointing to validate zeroSSL url as instructed
- download cert and private key

## nginx https
- install nginx on ec2: sudo amazon-linux-extras install nginx1
- vim /etc/nginx/nginx.conf, uncomment ssl configurations, update certificate and certificate_key
- upload cert and private key
- restart nginx. if failed with no cipher match, add below:
  - ssl_protocols TLSv1.2 TLSv1.3;
  - ssl_ciphers ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-CHACHA20-POLY1305:ECDHE-RSA-CHACHA20-POLY1305:DHE-RSA-AES128-GCM-SHA256:DHE-RSA-AES256-GCM-SHA384;

## about cert chain
Two kinds of certs: 
- CA certs has X509v3 Basic Constraints: critical, CA:**TRUE**, 
  - pathlen:0 means no sub CAs (it can only sign to end-user instead of intemediate CA).
- end user certs has no "Basic Constraints" or has CA:**FALSE**
- root-self-signed certs has CA:**TRUE**
