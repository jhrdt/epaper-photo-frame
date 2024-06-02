import machine
import time
import uos
from machine import I2C, Pin

# Third-Party
import sdcard
from eeprom import EEPROM
from epaper import EPD_5in65

# Local
import bitmap


# Fns
#
def display_bytes(epd, bytes_gen):
    epd.send_command(0x61)   # Set Resolution setting
    epd.send_data(0x02)
    epd.send_data(0x58)
    epd.send_data(0x01)
    epd.send_data(0xC0)
    epd.send_command(0x10)

    for b in bytes_gen:
        epd.digital_write(epd.dc_pin, 1)
        epd.digital_write(epd.cs_pin, 0)
        epd.spi.write(b)
        epd.digital_write(epd.cs_pin, 1)

    epd.send_command(0x04)   # 0x04
    epd.BusyHigh()
    epd.send_command(0x12)   # 0x12
    epd.BusyHigh()
    epd.send_command(0x02)   # 0x02
    epd.BusyLow()
    epd.delay_ms(200)

def clean_display(epd):
    epd.EPD_5IN65F_Clear(epd.White)
    #epd.EPD_5IN65F_Clear(epd.Clean)

def poweroff(i):
    pin = Pin(i, Pin.OUT)
    pin.high()
    pin.low()

def is_switch_on(i):
    pin = Pin(i, mode=Pin.IN, pull=Pin.PULL_UP)
    return bool(1 - pin.value())


# Constants
#
IMAGE_DIR = "/imgs"
DONE_PIN = 16
SWITCH_PIN = 20


# Debug
#
#led = Pin(25, Pin.OUT)
#led.toggle()

time.sleep(2)

if not is_switch_on(SWITCH_PIN):
    poweroff(DONE_PIN)


# EEPROM
#
I2C_ADDR = 0x50     # DEC 80, HEX 0x50
EEPROM_SIZE = 16    # AT24C16 on 0x50
i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=400_000)
eeprom = EEPROM(addr=I2C_ADDR, at24x=EEPROM_SIZE, i2c=i2c)

rom_data = eeprom.read(1, 3)
try:
    image_i = int(rom_data)
except ValueError:
    image_i = 0


# SD Card Reader
#
spi = machine.SPI(
    0,
    baudrate=1_000_000,
    polarity=0,
    phase=0,
    bits=8,
    firstbit=machine.SPI.MSB,
    sck=machine.Pin(2),
    mosi=machine.Pin(3),  # TX
    miso=machine.Pin(4)  # RX
)
cs = machine.Pin(5, machine.Pin.OUT)
sd = sdcard.SDCard(spi, cs)

vfs = uos.VfsFat(sd)
uos.mount(vfs, IMAGE_DIR)

images = [item for item in sorted(uos.listdir(IMAGE_DIR)) if item.endswith(".bmp")]

if image_i >= len(images):
    image_i = 0
    bmp_image = images[image_i]
    eeprom.write(1, f"{image_i:03d}")
else:
    bmp_image = images[image_i]
    image_i += 1
    eeprom.write(1, f"{image_i:03d}")


# ePaper Display
#
epd = EPD_5in65()
clean_display(epd)
with open(f"{IMAGE_DIR}/{bmp_image}", "rb") as img:
    bytestream = bitmap.as_bytes(img)
    display_bytes(epd, bytestream)


# Shutdown
#
poweroff(DONE_PIN)
