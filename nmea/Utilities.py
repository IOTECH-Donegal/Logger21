import socket


def udp_sender(MCAST_GRP, MCAST_PORT, message):

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 32)
    sock.sendto(message, (MCAST_GRP, MCAST_PORT))


def validate_crc(nmea_full_sentence):
    """
    Compare a calculated CRC to the received value
    """

    try:
        # The last two characters are HH where HH is the CRC
        checksum = nmea_full_sentence[-3:]
        # XOR all values between $ and *
        calculated_checksum = calculate_crc(nmea_full_sentence[1:-4])
        # Compare the calculated checksum with the numerical value of the extracted string
        if calculated_checksum == hex(int(checksum, 16)):
            return True
        else:
            return False
    except:
        print('Error trying to validate CRC in ' + nmea_full_sentence)


def calculate_crc(nmea_partial_sentence):
    """
    Calculate the CRC of a NMEA sentence, CRC is a simple XOR of all values between $ and *
    """

    # Reset to zero
    calculated_checksum = 0
    # Go through each character and XOR, create an integer
    for character in nmea_partial_sentence:
        calculated_checksum ^= ord(character)
    # Convert to hex, 2 digits
    calculated_checksum_2_digits = format(calculated_checksum, '02X')
    return calculated_checksum_2_digits
