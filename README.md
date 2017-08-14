# vario-js
[![Build Status](https://travis-ci.org/graymalkin/vario.svg?branch=master)](https://travis-ci.org/graymalkin/vario)


Video overlays for Glider Pilots

This project is to create a web tool for building video overlays with flight telemetry for glider and powered pilots.

## Development

Dev needs to be done in a virtual env.

```
virtualenv .venv
. ./.venv/bin/activate
python3 setup.py build
```


## Notes

 - We'll need to read in `.igc` files ([details here](http://carrier.csi.cam.ac.uk/forsterlewis/soaring/igc_file_format/))
 - Some method to output videos
 - Some method of positioning instruments
 - Maybe a specification language so that we can automate positioning
 - Desired "instruments":
    - ASI
    - Thermalling trace
    - Vario(?)
    - Altimeter
    - Wind direction
    - Compass
 - Desired text readouts
    - Speed (Airspeed/groundspeed)
    - Average climb
    - Altitude ([QNH/QFE](https://en.wikipedia.org/wiki/Q_code#Aeronautical_Code_signals_.28QAA.E2.80.93QNZ.3B_ICAO.29))
    - Wind speed
    - Wind bearing
    - Flight bearing
    
