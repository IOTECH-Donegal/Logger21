
from nmea.Utilities import calculate_crc

# HDT - Heading - True
# Actual vessel heading in degrees true produced by any device or system producing true heading.
# Example: $GPHDT,274.07,T*03\r\n
# 1 - headt = Heading of vehicle (true)
# 2 - mi = Mode Indicator
# 3 - cs = Checksum


def hdt(headt):
    # Construct a partial sentence, no $ and no CRC
    nmea_partial_sentence = "GPHDT," + headt + ",T"
    print(nmea_partial_sentence)
    # Calculate the CRC
    crc = calculate_crc(nmea_partial_sentence)

    # Construct the full sentence
    nmea_full_sentence = "$" + nmea_partial_sentence + "*" + crc

    return nmea_full_sentence

