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

## Third-Party Libs

* eeprom.py
  * https://github.com/brainelectronics/micropython-eeprom/blob/main/eeprom/eeprom.py
* sdcard.py
  * https://raw.githubusercontent.com/micropython/micropython-lib/master/micropython/drivers/storage/sdcard/sdcard.py
* Pico_ePaper-5.65.py
  * https://github.com/waveshareteam/Pico_ePaper_Code/blob/main/python/Pico-ePaper-5.65f.py

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
  * Explains how to create .bmp images in GIMP

## References

* RP2040
  * https://www.elektronik-kompendium.de/sites/raspberry-pi/2611061.htm

* EEPROM
  * https://www.instructables.com/How-to-Add-an-EEPROM-to-Raspberry-Pi-Pico/
  * https://ww1.microchip.com/downloads/en/devicedoc/doc0336.pdf

* Micropython
  * https://github.com/micropython/micropython-lib