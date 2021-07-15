import sys
from binascii import unhexlify

from base45 import b45decode
from zlib import decompress

from cose.keys import SymmetricKey
from cose.messages import CoseMessage, Enc0Message
import cbor2
import json

base45string = "6BFOXN%TSMAHN-H6SKJPT.-7G2TZ971V8ELBXEJW.TFJTXG41UQR$TTSJNSO4.OK1JZZPQA36S4HZ6SH9X5Q9AIMZ5BTMUW5-5QNF6O MOL1 MM5HM.PH0/H2:61:UYYAVY9U3QZIESH9UKPSH9WC5PF6846A$Q%76UW6A/9KP5AUJIZI.EJJ14B2MZ8DC8CWVD 8D*NI+PB/VSQOL9DLKWCZ3E7KDW0KZ J$XI4OIMEDTJCJKDLEDL9CZTAMEIW CI4U/DC.ZJ5OI9YI:8D-FD%PDMOL4WC$ZJ*DJWP42W5+XO9KQL+Q9D6E:73X712S5D6HL6:ERCA7T5M9+5:ZJ::A-4JUM97H98$QP3R8BHPCM%YL-/N+BF-CFX/Q5NT$MC%OCHX7VRTG5S5YNDQSW7WNZ93*SIK5$QGMK28BV*1M1BQXCCN7UDS3V/4:CKYE7.8J5Y8F5MO8OXTD830X93Q0"
compressedBinaryData = b45decode(base45string)

uncompressedBinaryData = decompress(compressedBinaryData)
# print(uncompressedBinaryData)
cose = CoseMessage.decode(uncompressedBinaryData)
print(cose)
cborRep = cose.payload
print(cborRep)
cbor2Object = cbor2.loads(cborRep)
cbor2Object[-260][1]['nam']['fn'] = "FERNANDEZ"
cbor2Object[-260][1]['nam']['fnt'] = "FERNANDEZ"
cbor2Object[-260][1]['nam']['gn'] = "LUCAS"
cbor2Object[-260][1]['nam']['gnt'] = "LUCAS"
cbor2Object[-260][1]['dob'] = "1999-11-10"
print(json.dumps(cbor2Object))
cbor_encode = cbor2.dumps(cbor2Object)
cborrep1 = cbor_encode
#print(cborrep1)
# msg = Enc0Message(
#     phdr={'ALG': 'Es256'},
#     uhdr={'KID': b'|b\xee\xbe\x0e\xa7\xe7\t'},
#     payload='\xa4\x01dCNAM\x04\x1ad\x88\xe6\xe0\x06\x1a`\xed\xa3L9\x01\x03\xa1\x01\xa4av\x81\xaabcix\x1durn:uvci:01:FR:8T8VXSXW15NU#5bcobFRbdn\x02bdtj2021-07-13bisdCNAMbmamORG-100031184bmplEU/1/20/1507bsd\x02btgi840539006bvpgJ07BX03cdobj1999-11-10cnam\xa4bfniFERNANDEZbgneLUCAScfntiFERNANDEZcgnteLUCAScvere1.3.0'.encode('utf-8')
# )
# msg.key = SymmetricKey(unhexlify(b'iVBORw0KGgoAAAANSUhEUgAAAMIAAADCAQAAAAAzmiCcAAAFnElEQVR4nNVYwYpdyQ3VsxpCgwb5AwyzyTagoRrMgEw98MowP5FVtt4GZjMwMFt/wPxEwJCVQU0ZQkBGDf6AIWDItho9aAL1UBZZZubWNqnlvQhJp46ODnUq+PVz/+w3fgD8b/853XxzenU9PX+8uT/fnT/d3F/uH785nQ9ioHoWDogRprkWzOhFWd2OYqQx8lzNCMHUTYdE4lHMDQD84UfEv9HrdcLzOj98gZ8v58N+oKRZ766ARY0mkpPQcR6oniS5qrcZusZMRtPjfk51Qvmvr9eH/sNRniolJuq4ZqycusYcveqwNjehFQbNRmNA9kbdxnE/QCuCtNXwjBxQodn5uJ87oOsDPN3CeHxrX3/5DuB+nf9KB7yGomAmE+nMsFobC8N7HtfWsPWpGDSrR2Bb3XmuTT8sDI3SVzNZnqqObR7jFsgIEj5np0DtbottU5tEN0Qgn0XdvbnDsHGchyaQRMRstMYKQrJEOIo51d3f8fHr3xN8NLo+3b68fdK//PKoeIh1Cgu5oTZu2aY1tDU2tXlXBxghy2vyii4RqhsMBql7WZUaFznP6uzHeZTRceCQZd0VXNHD+TgGgY2dkRqpaXApobfj2tCbIs2EmCLONHDC2MyCYRFneK0Ys6yUA2XDN3Vymtmkc+81ctJcTMf9FGhrzsUtxUZRZGlssKaQNgQTJ2d0pwWRSzZaBU0bN6BCRsOM5gmHsw3FHSKzd1lSveVsmdb7cT/QKOeYjXIoZ7NJTu2Q18+g0eXKt0BPJJ8F7PzdRb4QH+v1BA1AAWpmSyASUaFv+ok1gSxYQIOVsAf0TcwY2KmDTZem5izeAeIYg8ZMnZrMSOnTuEU6r83MIWIVSV8zehsCIzA2u3F6XyW6oHcc3ctIjTcclcY8YKKUzt5WuA+Xw/uBWjo6l9lQiOjsVg1to6MdOwwr1m5tzgTOmgobXrMP6X0FUBsec64cudtZ4jMSDUQTYIwVXWGjb8gzp9XEZOCoEcNxbDh6+/58/Qw3v/wLBC/nO7oT+Pb7dux3gtGYvBF5xznEUDpt7sct06aLD7LmvYQxeNMPuE1cGdzNq2SN5RCHs/0M5PL2hT3A9T28fnn/FcGfX+N4++F45gZP7JTLGq+Qyga15qa2kLaoaZZTm5TqUZmH+nYDV//8u/UJ4PFP9vLz5fzursHPj090WJsmdE52QjQjyrkKY6O9k4eWWXBvIQ6lOFg3u4QBImYCwEgWyAVScMjrGxB4fPXPF9Dh+v2nJ0y61qdX/dMG66ZTOjV0mYXCEzja4W58Bm/o6YXDha5vH/hk48MLv1zpepwHAItMQEUpDef0EbDRgyzOAWNMzarVvTfkudE3gek0A3XWxIUkQ4ZvfFV0yMm8ipSkWls+GsTGJ06SrtxxNBzdfAIM2Pk3zQgKU5mAGTxy1cINd4B7CTIvTaE1NAHGprbRucJtgOhgEAPI0TYeyScCTejMGgOIwhhxs7NWsLlg8hQJkJgzdW52SVgx+UjgrojVQ9hyo9cY1hxBVKJxRPGa6Bvv4lCmExZJDeMYKqPaxlPM0lxKJUh9JvGoarGbU1k1ccloCplozap2vheqhSoyh+OUXjGp9Q0P2kwo0lF9aVVGM4O+wzpGwHDTmdDMmyClbTwFYRGwp/SmXYdNjbY2MdahWS1aiuZuRaCKsvHk2ci1k0RyM8acQ3SDAXOQgiwWG6ssbbVBm72tE9KwAGNANzDVYDjUt1MB3FzzDeBHmLcfUd68u6Cer+PwDeV0c13P3/10IT8/Cbx6AKLTBY81sacARnUk48S5CNvqG38tzYJqAFvzLkiQA6FtNLGpt8QBKxzZSDUb+S5PjJosXLLQ25SlMjb7h99/hd/+aH/8xyt+/gH8DJeP+R90fjsP4MKJPixDh9UUwbW29/Or5//0jevfCCdIdD4xlaMAAAAASUVORK5CYII='))
# msg.encode()
# print(msg)