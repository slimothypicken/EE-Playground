#import pyvisa as vs
import logging
import serial

#logginsetup
logging.basicConfig(
	level=logging.INFO,
	format="%(asctime)s [%(levelname)s] %(message)s"
)

log = logging.getLogger(__name__)
rotate = logging.handlers.RotatingFileHandler("app.log", maxBytes=3000000, backupCount = 1)
rotate.setFormatter(logging.Formatter("%(asctime)s [%(levelname)s] %(message)s"))
log.addHandler(rotate)


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
	processed = handle(data)
	device.write(processed)
	log.info(f"Sent: {processed!r}")