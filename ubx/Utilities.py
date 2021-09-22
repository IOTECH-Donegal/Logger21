"""
Utilities for UBX sentences.
"""

from datetime import datetime
import os.path




def ubx_crc(payload_for_crc,ubx_crc_a, ubx_crc_b):
    # Convert CRC bytes to INT
    ubx_crc_a_int = int.from_bytes(ubx_crc_a, "little")
    ubx_crc_b_int = int.from_bytes(ubx_crc_b, "little")

    # Go get the two CRCs
    crc_a = 0
    crc_b = 0

    for byte in payload_for_crc:
        crc_a += byte
        crc_a &= 0xFF
        crc_b += crc_a
        crc_b &= 0xFF

    # Now catch the error if there is one
    if ubx_crc_a_int != crc_a:
        print(f'CRC_A Error, {ubx_crc_a_int} not equal to {crc_a}')
        return False
    if ubx_crc_b_int != crc_b:
        print(f'CRC_B Error, {ubx_crc_b_int} not equal to {crc_b}')
        return False

    return True


def itow(iTOW_in_ms):
    """
    Time/date as an integer week number (TOW)
    and a time of week expressed in seconds.
    """
    # Convert from ms to seconds
    itow_total_seconds = iTOW_in_ms / 1000
    # Calcuate number of seconds in
    day = 24 * 60 * 60
    hour = 60 * 60
    minute = 60
    # The day will be
    itow_day = int(itow_total_seconds / day)
    itow_hour = int((itow_total_seconds - (itow_day * day)) / hour)
    itow_minute = int((itow_total_seconds - (itow_day * day) - (itow_hour * hour)) / minute)
    itow_seconds = int((itow_total_seconds - (itow_day * day) - (itow_hour * hour)) - (itow_minute * minute))
    return itow_day, itow_hour, itow_minute, itow_seconds


