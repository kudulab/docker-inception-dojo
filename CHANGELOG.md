### 0.5.0 (2024-Feb-03)

* docker-compose 2.23.3 on alpine and 2.24.5-1 on ubuntu
* pytest 7.4.3 on alpine and 7.4.0-2 on ubuntu
* bump base docker image for alpine: docker:25.0.2-dind-alpine3.19
* bump base docker image for ubuntu: ubuntu:23.10

### 0.4.0 (2022-Aug-02)

* pytest 7.1.2
* bump base docker image for alpine: docker:20.10.17-dind-alpine3.16
* bump base docker image for ubuntu: ubuntu:20.04
* s6 overlay 3.1.1.2

### 0.3.0 (2022-Feb-28)

* Make Docker daemon log to a file, and not to the console. Logging to the console makes the output cluttered, as logs from Docker daemon are incoming together with any other logs or output

### 0.2.1 (2022-Feb-19)

* Bump pytest to 6.1.1
* Upgrade pip

### 0.2.0 (2022-Feb-18)

Use new alpine image `docker:20.10.12-dind-alpine3.15`

### 0.1.3 (2020-Dec-20)

Use Dojo scripts from version 0.10.3, remove duplicated creation of `/run/user/{dojo_uid}`

### 0.1.2 (2019-Dec-31)

Use Dojo scripts from version 0.6.3, because we need the directory
 `/run/user/{dojo_uid}` to exist.

### 0.1.1 (2019-Apr-27)

fix virtualenv in ubuntu

### 0.1.0 (2019-Apr-27)

Initial release - alpine and ubuntu18 with docker in docker.
