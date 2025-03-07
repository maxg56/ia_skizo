all:
	source conf_seve/venv/bin/activate
	python3 conf_seve/app/main.py
compile:
	arduino-cli compile --fqbn arduino:mbed_nano:nano33ble ser

upload:
	arduino-cli upload -p /dev/ttyACM0 --fqbn arduino:mbed_nano:nano33ble ser
