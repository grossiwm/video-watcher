from sys import platform
import os

my_env = os.environ.copy()

def is_windows():
    return platform == 'win32'

def is_linux():
    return platform == 'linux' or platform == 'linux2'

def grep(name):
    if is_linux():
        return ['grep', name]
    elif is_windows():
        return ['findstr', name]

def jps_path():
    if is_linux():
        return ['sudo', '-E', 'jps']
    elif is_windows():
        return my_env['JAVA_HOME'] + "\\bin\jps.exe"

def kill(pid):
    if is_linux():
        return ['sudo', '-E', 'kill', str(pid)]
    elif is_windows():
        ['taskkill', '/PID', str(pid), '/F']

def sniffer_execution():
    if is_linux():
        return ['sudo', '-E', 'java', '-jar', 'jar/sniffer.jar', '192.168.25.21']
    elif is_windows():
        return ['java', '-jar', 'jar/sniffer.jar', '192.168.25.13']

def sniffer_execution_env(current_env):
    if is_linux():
        return {
            **current_env,
            'SystemRoot': '/'
        }
    elif is_windows():
        return current_env