basic.show_icon(IconNames.HEART)
radio.set_group(1)
pins.set_pull(DigitalPin.P13, PinPullMode.PULL_NONE)
pins.set_pull(DigitalPin.P14, PinPullMode.PULL_NONE)
pins.set_pull(DigitalPin.P15, PinPullMode.PULL_NONE)
pins.set_pull(DigitalPin.P16, PinPullMode.PULL_NONE)

def on_forever():
    if pins.digital_read_pin(DigitalPin.P15) == 0:
        radio.send_string("Open")
        basic.show_icon(IconNames.HAPPY)
    elif pins.digital_read_pin(DigitalPin.P13) == 0:
        radio.send_string("Close")
        basic.show_icon(IconNames.NO)
    elif pins.digital_read_pin(DigitalPin.P16) == 0:
        radio.send_string("LEDL")
        basic.show_leds("""
            . . # . .
                        . # # . .
                        # # # . .
                        . # # . .
                        . . # . .
        """)
    elif pins.digital_read_pin(DigitalPin.P14) == 0:
        radio.send_string("LEDR")
        basic.show_leds("""
            . . # . .
                        . . # # .
                        . . # # #
                        . . # # .
                        . . # . .
        """)
    else:
        if pins.analog_read_pin(AnalogPin.P2) > 550 and (pins.analog_read_pin(AnalogPin.P1) > 400 and pins.analog_read_pin(AnalogPin.P1) < 600):
            radio.send_string("F")
            basic.show_leds("""
                . . # . .
                                . # # # .
                                # . # . #
                                . . # . .
                                . . # . .
            """)
        elif pins.analog_read_pin(AnalogPin.P2) < 450 and (pins.analog_read_pin(AnalogPin.P1) > 400 and pins.analog_read_pin(AnalogPin.P1) < 600):
            radio.send_string("B")
            basic.show_leds("""
                . . # . .
                                . . # . .
                                # . # . #
                                . # # # .
                                . . # . .
            """)
        elif pins.analog_read_pin(AnalogPin.P1) < 450 and (pins.analog_read_pin(AnalogPin.P2) > 400 and pins.analog_read_pin(AnalogPin.P2) < 600):
            radio.send_string("L")
            basic.show_leds("""
                . . # . .
                                . # . . .
                                # # # # #
                                . # . . .
                                . . # . .
            """)
        elif pins.analog_read_pin(AnalogPin.P1) > 550 and (pins.analog_read_pin(AnalogPin.P2) > 400 and pins.analog_read_pin(AnalogPin.P2) < 600):
            radio.send_string("R")
            basic.show_leds("""
                . . # . .
                                . . . # .
                                # # # # #
                                . . . # .
                                . . # . .
            """)
        else:
            radio.send_string("S")
            basic.show_leds("""
                . . . . .
                                . # # # .
                                . # # # .
                                . # # # .
                                . . . . .
            """)
basic.forever(on_forever)
