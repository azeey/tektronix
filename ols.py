# Converts channel data from scope to a format recongnizable by the OLS logic
# sniffer client. The scope data is assumed to be acquired by some means (eg.
# pyVisa or pySerial)
#
import numpy as np
def to_ols(chdata, threshold, rate=25000000):
    """Given an array of data from each channel, this function returns a string
    that can be saved to a file and opened by the OLS software(http://www.lxtreme.nl/ols)
    The data is first converted to logic states based on the given threshold.


    :chdata: Data from each channel. Must be an array with each column respresenting data from corresponding channel.
    :threshold: Threshold for deciding between a high and a low.
    :rate: Sample rate
    :returns: Formatted string

    """
    # Boolean results become ones and zeros
    chbinary = np.int8(chdata > threshold)

    numsamples, numch = chdata.shape

    # Form byte values by shifting and adding each channel
    chbytes = np.zeros(numsamples)
    for i in xrange(numch):
        chbytes += (chbinary[:,i] << i)

    chstr = ["%x@%d" % (val,i) for i, val in enumerate(chbytes)]

    output = ";Channels: %d\n" % numch
    output += ";Rate: %d\n" % rate
    output += "\n".join(chstr)

    return output







    
    
