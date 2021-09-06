# aws codeguru
## reviewer: connect to your github.com account and scan for PR(incremental)/branch(full) for recommendations.

- create github repo, checkin code
- in reviewer console, connect to github, grant oauth permissions, select the repo
- create PR on the repo
- check incremental recommendations, or on the PR on github.
- you can also create full scan on branches.

## profiler: run code and figure out most costly code. take lambda as example:

- create lambda, and corresponding iam role
- create profiler
- setup profiler: 
  - set lambda role
  - update lambda config, add environments AWS_CODEGURU_PROFILER_GROUP_ARN and AWS_CODEGURU_PROFILER_GROUP_NAME
  - update lambda code adding package codeguru_profiler_agent
  
```
  from codeguru_profiler_agent import with_lambda_profiler
  @with_lambda_profiler()
  def handler_name(event, context):
```

- call lambda > 5mins and wait for >15mins.
