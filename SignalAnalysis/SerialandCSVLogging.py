#import pyvisa as vs
import logging
import serial
import csv
from time import time

#logginsetup
logging.basicConfig(
	level=logging.INFO,
	format="%(asctime)s [%(levelname)s] %(message)s"
)

log = logging.getLogger(__name__)
rotate = logging.handlers.RotatingFileHandler("app.log", maxBytes=3000000, backupCount = 1)
rotate.setFormatter(logging.Formatter("%(asctime)s [%(levelname)s] %(message)s"))
log.addHandler(rotate)

#CSV setup
csv_file = open("sensor_data.csv", "w", newline="") 
csv_writer = csv.writer(csv_file) 
csv_writer.writerow(["timestamp", "value"])


log.info("Starting serial loop...")

#Open a virtual serial port
device = serial.Serial('/dev/pts/5', baudrate=115200, timeout=.1)


def handle(data: bytes) -> bytes:
	return data.upper()

while True:
	data = device.read(64)
	if not data:
		continue #nothing received loop again
	
	log.info(f"Received: {data!r}")
	try:
	  value = int(data.decode().strip()) 
	  csv_writer.writerow([time(), value])
	  csv_file.flush()
	except ValueError:
	  log.warning(f"Non-numeric data received: {data!r}")
	processed = handle(data)
	device.write(processed)
	log.info(f"Sent: {processed!r}")