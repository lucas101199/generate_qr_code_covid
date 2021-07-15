import sys
import zlib
import pprint
# Modules tiers (Pillow, Pyzbar, base45, cbor2)
import base45
import cbor2


b45data = "6BFOXN%TSMAHN-H6SKJPT.-7G2TZ971V8ELBXEJW.TFJTXG41UQR$TTSJNSO4.OK1JZZPQA36S4HZ6SH9X5Q9AIMZ5BTMUW5-5QNF6O MOL1 MM5HM.PH0/H2:61:UYYAVY9U3QZIESH9UKPSH9WC5PF6846A$Q%76UW6A/9KP5AUJIZI.EJJ14B2MZ8DC8CWVD 8D*NI+PB/VSQOL9DLKWCZ3E7KDW0KZ J$XI4OIMEDTJCJKDLEDL9CZTAMEIW CI4U/DC.ZJ5OI9YI:8D-FD%PDMOL4WC$ZJ*DJWP42W5+XO9KQL+Q9D6E:73X712S5D6HL6:ERCA7T5M9+5:ZJ::A-4JUM97H98$QP3R8BHPCM%YL-/N+BF-CFX/Q5NT$MC%OCHX7VRTG5S5YNDQSW7WNZ93*SIK5$QGMK28BV*1M1BQXCCN7UDS3V/4:CKYE7.8J5Y8F5MO8OXTD830X93Q0"
zlibdata = base45.b45decode(b45data)
cbordata = zlib.decompress(zlibdata)
decoded = cbor2.loads(cbordata)
print(decoded)
print("Header\n----------------")
print(cbor2.loads(decoded.value[0]))
print("\nPayload\n----------------")
print(cbor2.loads(decoded.value[2]))
print("\nSignature ?\n----------------")
print(decoded.value[3])
