'''
Extracted from ZED-F9P - Interface Description, section 3
'''

UBX_CLASS = {
    b"\x01": "NAV",  # Navigation solution messages
    b"\x02": "RXM",  # Status from the receiver manager
    b"\x27": "SEC",  # Security features of the receiver
}