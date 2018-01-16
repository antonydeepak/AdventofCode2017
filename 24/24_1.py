from sys import stdin

def strength(component):
    return component[0]+component[1]

def connect(source, connected, ports, components):
    best = 0
    for component in ports[source]:
        index = components[component]
        if not (connected & (1<<index)):
            connected |= (1<<index)
            open_port = component[0] if (component[0] != source) else component[1]
            best = max(best, strength(component) + connect(open_port, connected, ports, components))
            connected ^= (1<<index)
    return best

def build_ports(components):
    ports = {}
    for component in components:
        x,y = component
        if x not in ports:
            ports[x] = []
        if y not in ports:
            ports[y] = []
        ports[x].append(component)
        if x!=y:
            ports[y].append(component)
    return ports

if __name__ == '__main__':
    components = {}
    i = 1
    for line in stdin:
        component = tuple(map(int, map(lambda x: x.strip(), line.split('/'))))
        components[component] = i
        i += 1

    ports = build_ports(components)

    print(connect(0, 0, ports, components))