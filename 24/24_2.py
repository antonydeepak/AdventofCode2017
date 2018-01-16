from sys import stdin

def strength(component):
    return component[0]+component[1]

def connect(source, connected, ports, components):
    best_length = 0
    best_strength = 0

    for component in ports[source]:
        index = components[component]
        if not (connected & (1<<index)):
            # print(f'{source}=>{component}', end='')
            connected |= (1<<index)
            open_port = component[0] if (component[0] != source) else component[1]

            l,s = connect(open_port, connected, ports, components)
            if (l+1)>=best_length:
                if (l+1)==best_length:
                    best_strength = max(best_strength, strength(component)+s)
                else:
                    best_strength = strength(component)+s

                best_length = l+1

            connected ^= (1<<index)

    return best_length,best_strength

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