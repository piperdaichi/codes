# coding: UTF-8
import RPi.GPIO as GPIO
import time
import requests

GPIO_INPUT = 14

GPIO.setmode(GPIO.BCM)
GPIO.setup(GPIO_INPUT, GPIO.IN)

def line_notify():
    payload = {'message':'家燃えてるぞ'}  
    headers = {'Authorization': 'Bearer ' + 'Er2E2rf2fna2ISpeaSppsfYasDJ9nqV5L1rjnoojk3f'} # 発行したトークン
    requests.post('https://notify-api.line.me/api/notify', data=payload, headers=headers)

try:
	while True:
		if GPIO.input(GPIO_INPUT) == GPIO.LOW:
			line_notify()
			print("smoke detected")
			time.sleep(5)
		else:
			print("runninng")
			time.sleep(1)
except KeyboardInterrupt:
	print("stopped")
	GPIO.cleanup()
