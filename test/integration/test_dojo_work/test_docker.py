import os
import subprocess

def decode_utf8(bytes):
    return bytes.decode('utf-8')

def run_command(exe, args):
    result = subprocess.run([exe] + args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    result.stdout = decode_utf8(result.stdout)
    result.stderr = decode_utf8(result.stderr)
    return result

def test_current_directory_is_dojo_work():
    result = run_command('pwd', [])
    assert '/dojo/work' in result.stdout
    assert result.returncode == 0

def test_docker_ps():
    result = run_command('docker', ['ps'])
    assert 'CONTAINER ID' in result.stdout
    assert result.returncode == 0

def test_docker_run():
    result = run_command('docker', ['run', 'hello-world'])
    assert 'Hello from Docker!' in result.stdout
    assert result.returncode == 0

def test_docker_compose_cli():
    result = run_command('docker-compose', ['--version'])
    assert result.returncode == 0

def test_virtualenv_create():
    result = run_command('python3', ['-m', 'venv', 'my_venv'])
    assert result.returncode == 0

def test_docker_logs_are_not_printed_to_console():
    result = run_command('docker', ['run', 'hello-world'])
    assert 'Hello from Docker!' in result.stdout
    assert 'ERRO' not in result.stdout
    assert 'ERRO' not in result.stderr
    assert 'INFO' not in result.stdout
    assert 'INFO' not in result.stderr
    assert result.returncode == 0

    # log file exists and is not empty
    result = run_command('tail', ['/var/log/docker/current'])
    assert 'info' in result.stdout

# https://github.com/kudulab/dojo/issues/38
def test_docker_compose_run_and_output_from_container_is_visible1():
    result = run_command('docker-compose', ['-f', './dc.yaml', '-p',  'testdojorunid', 'run', '--rm', 'default', 'sh', '-c', 'printenv', 'HOME'])
    print('stdout')
    print(result.stdout)
    print('stderr')
    print(result.stderr)
    assert '/root' in result.stdout
    assert result.returncode == 0

# https://github.com/kudulab/dojo/issues/38
def test_docker_compose_run_and_output_from_container_is_visible2():
    result = run_command('docker-compose', '-f ./dc.yaml -p testdojorunid run --rm default sh -c "whoami"'.split(' '))
    print('stdout')
    print(result.stdout)
    print('stderr')
    print(result.stderr)
    assert 'root' in result.stdout
    assert result.returncode == 0
