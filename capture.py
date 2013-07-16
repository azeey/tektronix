# coding: utf-8
# Meant to be used in ipython

from wanglib.util import Serial
from wanglib.instruments.tektronix import TDS3000
import numpy as np
from tds3000socket import TDS3000Socket
import ols

class Capture(object):
    """Class to capture samples from Tektronix TDS 3054B"""

    def __init__(self, port='/dev/ttyS0', baud=38400):
        """@todo: to be defined1

        :port: Serial port
        :baud: Baud rate (max 38400)

        """
        self.port = port
        self.baud = baud
        self.bus = Serial(port, baudrate=baud, rtscts=True, term_chars='\n')
        self.init()

    def init(self):
        """@todo: Docstring for init

        :arg1: @todo
        :returns: @todo

        """
        self.bus.write('HDR OFF')
        self.bus.write('DATA:STOP 10000')
        self.bus.write('WFMPRE:NR_P 10000')
        self.scope = TDS3000(self.bus)

    def capture(self,channels=None):
        """Capture samples from the Tektronix TDS 3054B

        :channels: An array of the channels to retrieve
        :returns: Captured data array with each channel as column

        """

        if channels is None:
            channels = range(1,5)

        #allch = np.array([self.scope.get_wfm('CH%d' % i)[1] for i in channels]).T
        allch = [self.scope.get_wfm('CH%d' % i)[1] for i in channels]


        return np.array(allch).T

    def capsave(self, file_path, vthresh=1.5):
        """Capture, convert to OLS format and save to file

        Assumes a voltage threshold of 1.5

        :file_path: output file path
        :returns: None

        """
        allch = self.capture()
        out = ols.to_ols(allch, vthresh)
        open(file_path, 'w').write(out)




class CaptureSock(Capture):
    """Docstring for CaptureSock """

    def __init__(self, ipaddr):
        """@todo: to be defined1 """
        self.bus = TDS3000Socket(ipaddr)
        self.init()
        
