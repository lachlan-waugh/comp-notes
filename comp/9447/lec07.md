# Monolithic vs Microservice architecture
## Monolith
	Frontend - Backend - Database
	Single point of failure
	Maintainability: have to take down everything when you need to fix/update something, long build times 

## Microservices
	splitting it up into a large amount of smaller programs, each handling a small functionality.
	Scalability, Availability benefits
`
# Containers vs VMs
## Virtual machines
	Much more heavy weight
	Need to update all of them separately, there's no real image

## Containers
	Cutting out the middle man - no need for a hypervisor
	You can spin up a container in ~5 mins, vms may need 30

# Container orchestration
You provide container images, environment variables
e.g. kubernetes & ecs
Much greater scalability
Ability to isolate the containers on different machines (nodes), each node runs it's own container
Each node can run multiple containers
ECR (elastic container registry) is AWS's is a docker image repository

# Serverless
You don't focus on the infrastructure, only on the code
You can run containers as lambda functions


