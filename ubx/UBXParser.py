
# Dictionaries of static data
import ubx.ClassID as ubc
import ubx.MessageID as ubm


class UBXParser():
    # Constructor
    def __init__(self):

        # Switch this on for verbose processing
        self.debug = 1

        # Properties used by calling program
        self.unique_id = ''
        self.longitude = 0
        self.latitude = 0
        self.altitude = 0
        self.horizontal_accuracy = 0
        self.vertical_accuracy = 0
        self.heading = 0

        # Status values, set when updated, reset from the calling program
        self.new_position = 0
        self.new_heading = 0

        self.sentence_class = ''
        self.message_type = ''

    def ubx_parser(self, byte3, byte4, ubx_payload):
        # Check if a valid UBX class
        if byte3 in ubc.UBX_CLASS:
            self.sentence_class = ubc.UBX_CLASS[byte3]
            if ubc.UBX_CLASS[byte3] == 'NAV':
                # Check if a valid message
                if byte4 in ubm.UBX_NAV:
                    self.message_type = ubm.UBX_NAV[byte4]
                    print(f'UBX: Received {self.message_type}')
            if ubc.UBX_CLASS[byte3] == 'RXM':
                # Check if a valid message
                if byte4 in ubm.UBX_RXM:
                    self.message_type = ubm.UBX_RXM[byte4]
                    print(f'UBX: Received {self.message_type}')
            if ubc.UBX_CLASS[byte3] == 'SEC':
                # Check if a valid message
                if byte4 in ubm.UBX_SEC:
                    self.message_type = ubm.UBX_SEC[byte4]
                    print(f'UBX: Received {self.message_type}')
        else:
            print(f'UBX: Unknown Class {byte3}')

