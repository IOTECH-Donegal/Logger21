from nmea.Utilities import calculate_crc

# THS - True heading and status
# $GPTHS,77.52,E*32\r\n
# 1 - headt = Heading of vehicle (true)
# 2 - mi = Mode Indicator
# 3 - cs = Checksum


def ths(headt, mode_indicator):
    # Construct a partial sentence, no $ and no CRC
    nmea_partial_sentence = "GPTHS," + headt + "," + mode_indicator
    # Calculate the CRC
    crc = calculate_crc(nmea_partial_sentence)

    # Construct the full sentence
    nmea_full_sentence = "$" + nmea_partial_sentence + "*" + crc

    return nmea_full_sentence
