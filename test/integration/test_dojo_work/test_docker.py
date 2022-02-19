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
