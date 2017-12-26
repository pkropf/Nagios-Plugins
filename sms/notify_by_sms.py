#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Nagios plugin to send sms notifications via GSM modem 

Copyright (c) 2017 Peter Kropf. All rights reserved.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.


This provides a simple sms notification by writing an smsd format message to
the /var/spool/sms/outgoing directory. This assumes that the smstools package
is installed and running. It has been tested using a USB HUAWEI Mobile modem 
with a Ting sim card.

Example:

    ./notify_by_sms phone_number whatever else is to be sent
"""


import sys
import os
from datetime import datetime
from syslog import syslog


SMS_OUTGOING='/var/spool/sms/outgoing'

file_name = os.path.join(SMS_OUTGOING, '%s.msg' % datetime.now().strftime('%Y%m%d %H%M%S %f'))
log_msg = 'sending sms via "%s" ' % file_name
log_msg += ' '.join(sys.argv[1:])
syslog(log_msg)

f = open(file_name, 'w')
f.write('To: %s\n' % sys.argv[1])
f.write('\n')
for m in sys.argv[2:]:
    f.write('%s\n' % m)
f.close()
