import subprocess

volPer = '80'

subprocess.Popen(['amixer', 'set', 'PCM', '--', volPer + '%'])
subprocess.Popen(['aplay', '/home/pi/sounds/berzerk/b-alert.wav'])

