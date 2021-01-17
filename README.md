# MicroPython
Playing around with MicroPython and ESP32. Tool _ampy_ is used for
uploading code to the board. Configuration is in file _.ampy_ in the root dir.

## Boards
I have usewd these boards.
* Lolin32 Lite. On board LED on pin 22 (Active low).

## Uploading code
To upload code to your board, you can copy-paste it in to the the REPL
environment, or upload it as _main.py_ with the _ampy_ tool.

### Upload with ampy

* Run the code on the board: *ampy run your-code.py*

Once you are done, you can upload the code to the board, so it will run
when the board is powered on or reset.
To be run on startup, your file needs to be uploaded as _main.py_.
You can make a symlink called _main.py_ to the file you want to upload,
or create a copy as _main.py_ before uploading.

* Make a symlink: *ln -s your-code.py main.py*
* Upload the code to the board: *ampy put main.py*

### Copy-paste
To copy-paste, from the _REPL_, enter paste mode with _CTRL-E_, paste your
code, and exit the pase mode with _CTRL-D_.


## Development
How to get up and running (On Ubuntu 20.*). This is based on https://docs.micropython.org/en/latest/esp32/tutorial/intro.html

* Make virtual python environment: _python3 -m venv .venv_
* Activate environment: _source .venv/bin/activate_
* Install esptool: _pip3 install -r requirements-dev.txt_
* Download firmware: http://micropython.org/download/esp32/
* Make yourself a member of group _dialout_ to be able to access the serial connection to your board: _sudo addgroup MY-USER dialout_
* To make your primary group _dialout_in the current session: _newgrp dialout_
* Erase current content of SPI flash on your board: _esptool.py --port /dev/ttyUSB0 erase flash_
* Install firmware: _esptool.py --port /dev/ttyUSB0 --chip esp32 write_flash --compress 0x1000 esp32-idf3-20200902-v1.13.bin_
* Connect to REPL (Interactive Python environment): _cu -l /dev/ttyUSB0 -s 115200_
* In REPL, type _type()_ to get som tips on setting up your EPS32.
* Disconnect from board (From _cu_): _~._


## 

* Get info on board: _espefuse.py -p /dev/ttyUSB0 summary_
* List files on board: _ampy --port /dev/ttyUSB0 ls_
* Upload a file to your board: _ampy --port /dev/ttyUSB0 put main.py_
