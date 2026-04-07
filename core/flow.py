flows = {}

def update(pkt):
    key = (pkt[1].src, pkt[1].dst)
    flows[key] = flows.get(key, 0) + 1
    return {"flow": key, "count": flows[key]}
