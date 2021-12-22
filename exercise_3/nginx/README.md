# Prerequisites
Install Helm3

MacOS with brew

`brew install helm`


Other Install Methods
https://helm.sh/docs/intro/install/

# Installation, validation, and testing
1. Ensure you have a valid connection to a k8s cluster

2. Install a release of the chart `helm install quirky-walrus ./`

3. Test the chart correctly deploys an nginx service `helm test quirky-walrus`

# Clean Up
1. Delete the release `helm delete quirky-walrus` 

# Commonly Used Values

| Value | Default | Description |
| ----- | ------- | ---------------  |
| replicaCount | 3 | Int: The number of replicas to create the nginx deployment with | 
| env | { ENV: PROD } | Dict:  of values to pass to the deployment as environment variables |
| autoscaling.enabled | true | Bool: enable or disable a HPA for the deployment |
| autoscaling.minReplicas | 3 | Int: minimum number of replicas | 
| autoscaling.maxReplicas | 3 | Int: maximum number of replicas | 
| autoscaling.targetCPUUtilizationPercentage | 50 | Int: percent of CPU usage to target |
| autoscaling.targetMemoryUtilizationPercentage | 80 | Int: percent of Memory usage to target |

# Contributing 
- validate the helm charts `helm lint ./`
- check the manifest output `helm template ./`
- get updates for diff `helm upgrade --install quirky-walrus ./ --dry-run --debug`

# Notes for the interviewer 
This helm template was boot strapped with `helm chart create` and then developed to meet the requirements of the exercise.
You can also find an example set of kubectl manifests in ./example_manifests

