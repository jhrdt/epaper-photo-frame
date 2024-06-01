# Readme

Photo frame using the 7 color 5.65 inch e-paper display from Waveshare

## BOM

* Pico-ePaper-5.65 (7-Color)
* RP2040
* Micro SD Breakout Board 3,3V 6Pin
* AT24C16 EEPROM Memory Module 
* TPL5110 Low Power Timer Breakout ([Adafruit](https://learn.adafruit.com/adafruit-tpl5110-power-timer-breakout?view=all))
* Panasonic NCR18650B (3,6V - 3,7V 3400mAh Li-Ion)
* DIP switch (1-Lane)
* (Soft) Tactile Button
* Rocker Switch

## Wire

| Component |  | RP2040 | | RP2040 |  | Component |
| --- | --- | --- | --- | --- | --- | --- |
| EEPROM | SDA | GP0 | | VBUS | | |
| EEPROM | SCL | GP1 | | VSYS | | |
| | | GND | | GND | | |
| SD | CLK | GP2 | | 3V3_EN | | |
| SD | MOSI | GP3 | | 3V3 (OUT) | | |
| SD | MISO | GP4 | | | | |
| SD | CS | GP5 | | GP28 | | |
| | | GND | | GND | | |
| | | GP6 | | GP27 | | |
| | | GP7 | | GP26 | | |
| EPD | DC | GP8 | | RUN | | |
| EPD | CS | GP9 | | GP22 | | |
| | | GND | | GND | | |
| EPD | CLK | GP10 | | GP21 | | |
| EPD | DIN | GP11 | | GP20 | | DIP Switch |
| EPD | RST | GP12 | | GP19 | | |
| EPD | BUSY | GP13 | | GP18 | | |
| | | GND | | GND | | DIP Switch | |
| | | GP14 | | GP17 | | |
| | | GP15 | | GP16 | | |

## Third-Party Libs

* eeprom.py
  * https://github.com/brainelectronics/micropython-eeprom/blob/main/eeprom/eeprom.py
* sdcard.py
  * https://raw.githubusercontent.com/micropython/micropython-lib/master/micropython/drivers/storage/sdcard/sdcard.py
* Pico_ePaper-5.65.py
  * https://github.com/waveshareteam/Pico_ePaper_Code/blob/main/python/Pico-ePaper-5.65f.py
* picozero.py
  * https://github.com/RaspberryPiFoundation/picozero/blob/main/picozero/picozero.py

## Appendix

Raspberry Pi Pico
* https://www.raspberrypi.com/documentation/microcontrollers/raspberry-pi-pico.html
* https://micropython.org/download/RPI_PICO/

Waveshare (ePaper 5.65)
* https://www.waveshare.com/wiki/Pico-ePaper-5.65
* https://github.com/waveshareteam/Pico_ePaper_Code
* https://www.waveshare.com/product/displays/e-paper/epaper-1/5.65inch-e-paper-module-f.htm

Projects
* https://github.com/robertmoro/7ColorEPaperPhotoFrame


## References

* RP2040
  * https://www.elektronik-kompendium.de/sites/raspberry-pi/2611061.htm

* EEPROM
  * https://www.instructables.com/How-to-Add-an-EEPROM-to-Raspberry-Pi-Pico/
  * https://ww1.microchip.com/downloads/en/devicedoc/doc0336.pdf

* Micropython
  * https://github.com/micropython/micropython-lib