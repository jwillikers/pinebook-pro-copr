# pinebook-pro-copr

This repository contains unofficial rpms needed for running Fedora on Pinebook Pro.
The generated packages are available here: https://copr.fedorainfracloud.org/coprs/jwillikers/pinebook-pro/

The `ap6256-firmware` package only contains Bluetooth firmware for the wireless card.
It is meant to be used with the wireless firmware provided via this RPM: https://fedora.roving-it.com/brcm-pinebookpro-0.0-1.noarch.rpm

## Structure

SPEC location | Role | Status | Package build location
------------ | ------------- | ------------ | ------------
[ap6256-firmware/](ap6256-firmware/) | ap6256 Firmware | [![ap6256 Firmware build status](https://copr.fedorainfracloud.org/coprs/jwillikers/pinebook-pro/package/ap6256-firmware/status_image/last_build.png)](https://copr.fedorainfracloud.org/coprs/jwillikers/pinebook-pro/package/ap6256-firmware/) | [ap6256 Firmware Package](https://copr.fedorainfracloud.org/coprs/jwillikers/pinebook-pro/package/ap6256-firmware/) 

## Quick Enable

$ `dnf copr enable jwillikers/pinebook-pro`

## Credits

* https://github.com/e-minguez
* https://copr.fedorainfracloud.org/coprs/aptupdate/pinebook-pro/
