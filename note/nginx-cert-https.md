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
- certs for domain cannot be used for sub.domain, unless *.domain specifically

## enable https
- Uncomment last section for https server in nginx.conf
- ssl_ciphers 'ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-CHACHA20-POLY1305:ECDHE-RSA-CHACHA20-POLY1305:DHE-RSA-AES128-GCM-SHA256:DHE-RSA-AES256-GCM-SHA384';

## directory index for download
```
    location /somedirectory/ {
        autoindex on;
        autoindex_exact_size off;
        autoindex_format html;
        autoindex_localtime on;
    }
```

## file upload
```
    location ~ "/upload/([0-9a-zA-Z-.]*)$" {
        dav_methods  PUT DELETE MKCOL COPY MOVE;
        client_body_temp_path /tmp/incoming;
        alias     /upload/$1;
        create_full_put_path   on;
        dav_access             group:rw  all:r;

        client_body_in_file_only on;
        client_body_buffer_size 128k;
        client_max_body_size 100M;
        proxy_pass_request_headers on;
        proxy_set_body $request_body_file;
        proxy_pass http://127.0.0.1/upload;
        proxy_redirect off;
    }
```
- curl -T file.zip http://server/upload/tt.zip
- setenforce 0; /etc/selinux/config

## reverse proxy
```
    location ~ \.php {
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_pass http://127.0.0.1:8000;
    }
```
