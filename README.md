# docker-inception-dojo

A [Dojo](https://github.com/kudulab/dojo) Docker image to execute Dojo tests.

Built both from alpine and ubuntu.

## Usage

1. Install [Dojo](https://github.com/kudulab/dojo/#installation)
2. Provide a Dojofile:
```
$ cat Dojofile
DOJO_DOCKER_IMAGE="kudulab/inception-dojo:ubuntu-0.4.0"
# or if you prefer the alpine version
# DOJO_DOCKER_IMAGE="kudulab/inception-dojo:alpine-0.4.0"
DOJO_DOCKER_OPTIONS="--privileged"
```
3. Run`dojo` in the same directory as Dojofile. It will:
  * docker pull a Docker image
  * start a Docker container
  * log you into the Docker container

4. Example commands to run inside the Dojo created container:
```
docker ps -a
docker-compose --version
```


## Contributing
Instructions how to update this project.

1. Create a new feature branch from the main branch
1. Work on your changes in that feature branch. If you want, describe you changes in [CHANGELOG.md](CHANGELOG.md).
1. Build your image locally to check that it succeeds: `./tasks build ubuntu` and `./tasks build alpine`
1. Test your image locally: `./tasks itest ubuntu` and `./tasks itest alpine`. You may need to install the test framework - you can run [these commands](https://github.com/kudulab/docker-dotnet-dojo/blob/3.2.0/image/Dockerfile.debian#L58) to do it.
1. You may also test your image by running it interactively with dojo. Please run `./tasks example ubuntu` or `./tasks example alpine`.
1. If you are happy with the results, create a PR from your feature branch to master branch

After this, someone will read your PR, merge it and ensure version bump (using `./tasks set_version`). CI pipeline will run to automatically build and test docker image, release the project and publish the docker image.

## License

Copyright 2019-2024 Ava Czechowska, Tom Setkowski

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
