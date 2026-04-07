from scapy.all import sniff, IP

def run(callback):
    def handle(pkt):
        if IP in pkt:
            callback(pkt)
    sniff(prn=handle, store=False)
