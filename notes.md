# notes

## motors

- a4988 driver
- stepper 1.7A 0.4Nm


### old

- small disc rotating motor: https://www.hackster.io/touchmysound/10-midi-controlled-vibration-motors-for-piano-performance-513430
- stepper for puppet dancer
- solenoid for toy piano

https://www.conrad.de/de/p/eurolite-md-1515-discokugel-motor-12-cm-1284295.html

https://www.conrad.de/de/p/joy-it-schrittmotor-nema-flat01-0-06-nm-0-8-a-0-8-a-wellen-durchmesser-4-mm-2355880.html

it might end up with two motors for dual rotation on the dancer, solenoids for hitting the keys and perhaps some light

[driver uln2803](https://www.adafruit.com/product/970)

[tutorial](https://learn.adafruit.com/midi-solenoid-drum-kit?view=all)
[uln more info](https://microcontrollerslab.com/introduction-uln2803-features/)

[motor 17HS2408 - 0.6a - datahseet](https://alexnld.com/product/hanpose-17hs2408-28mm-nema-17-stepper-motor-42-motor-42bygh-0-6a-12n-cm-4-lead-for-cnc-laser-3d-printer-motor/)

consider simple dc motors rather than steppers

the power supply for the stepper should be at least 9v

for the solenoids, let's just do with a raspberry pi zero W and eventually figure out ethernet over usb on the regular rpi0