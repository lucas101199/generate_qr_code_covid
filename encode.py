import sys
from base45 import b45decode
from zlib import decompress
from cose.messages import CoseMessage
import cbor2
import json

base45string = "6BFOXN%TSMAHN-H6SKJPT.-7G2TZ971V8ELBXEJW.TFJTXG41UQR$TTSJNSO4.OK1JZZPQA36S4HZ6SH9X5Q9AIMZ5BTMUW5-5QNF6O MOL1 MM5HM.PH0/H2:61:UYYAVY9U3QZIESH9UKPSH9WC5PF6846A$Q%76UW6A/9KP5AUJIZI.EJJ14B2MZ8DC8CWVD 8D*NI+PB/VSQOL9DLKWCZ3E7KDW0KZ J$XI4OIMEDTJCJKDLEDL9CZTAMEIW CI4U/DC.ZJ5OI9YI:8D-FD%PDMOL4WC$ZJ*DJWP42W5+XO9KQL+Q9D6E:73X712S5D6HL6:ERCA7T5M9+5:ZJ::A-4JUM97H98$QP3R8BHPCM%YL-/N+BF-CFX/Q5NT$MC%OCHX7VRTG5S5YNDQSW7WNZ93*SIK5$QGMK28BV*1M1BQXCCN7UDS3V/4:CKYE7.8J5Y8F5MO8OXTD830X93Q0"
compressedBinaryData = b45decode(base45string)

uncompressedBinaryData = decompress(compressedBinaryData)
# print(uncompressedBinaryData)
cose = CoseMessage.decode(uncompressedBinaryData)
cborRep = cose.payload
#print(cborRep)
cbor2Object = cbor2.loads(cborRep)
cbor2Object[-260][1]['nam']['fn'] = "FERNANDEZ"
cbor2Object[-260][1]['nam']['fnt'] = "FERNANDEZ"
cbor2Object[-260][1]['nam']['gn'] = "LUCAS"
cbor2Object[-260][1]['nam']['gnt'] = "LUCAS"
cbor2Object[-260][1]['dob'] = "1999-11-10"
print(json.dumps(cbor2Object, indent=4))
