import iptc
import json
table = iptc.Table(iptc.Table.FILTER)
print str(table)
data=iptc.Chain(table,"INPUT")

print data
