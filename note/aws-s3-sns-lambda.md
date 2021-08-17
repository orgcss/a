# aws: s3-->sns-->lambda

## lambda: 
  - function
  - policy: allow sns
## sns:
  - topic
  - policy: allow s3
  - subscription
## s3:
  - notification: custom lambda to add;
