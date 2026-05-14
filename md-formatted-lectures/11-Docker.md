- DevOps, CI/CD pipeline

- Docker and containerization

  - Concepts

  - Practice




[▪](https://www.youtube.com/watch?v=scEDHsr3APg) [DevOps CI/CD Explained in 100 Seconds (youtube.com) (2m)](https://www.youtube.com/watch?v=scEDHsr3APg)




- Planning: Git(Hub), Jira

- Codebase: Git(Hub), Jira

- Building: Gradle, Maven, Make

- Testing: Pytest, Selenium


- Integration: Jenkins


- Deploy: Docker, Chef

- Operate: Docker, Chef

- Monitor: Nagios, Grafana, Power BI




- Like a mini-VM

- Isolated from the global environment

- A bit like pip modules: You can download

other images (“VMs”) and use them




[▪](https://www.youtube.com/watch?v=Gjnup-PuquQ) [Docker in 100 Seconds (youtube.com) (2m)](https://www.youtube.com/watch?v=Gjnup-PuquQ)




- Uses less space

- Faster boot-up time

- Generally better performance

- Easy to scale up

- Easily portable




- Pros of isolation

  - Works more independently

  - Lower internal complexity

  - More likely to work on other’s machine


- Cons of isolation

  - More effort to set up

  - More external complexity


**Docker**


- Docker client, server and registry

- Docker images

- Docker containers

- Docker file: Setup/config file

- Volumes



**OpenStack**


- OpenStack environment

- OS images

- Running instances/VMs

- Configuration field/file

- Volumes




- `docker container create [options] image [command] [arg...]`

- `docker pull <image>:<tag>:` Pulls an image from DTR

- `docker push <image>:<tag>:` Push an image to DTR

- `docker images:` Lists local images

- `docker ps:` Lists running containers

- `docker rm <id>:` Remove a stopped container

- `docker start <id>:` Start a stopped container


- `docker help`




FROM node:19


WORKDIR _/app_


COPY _package*.json ./_


RUN _npm install_


COPY _. ._


ENV PORT= _8080_


EXPOSE _8080_


RUN _echo_ "The ARG variable value is $PORT"


CMD _[_ "npm" _,_ "start" _]_




