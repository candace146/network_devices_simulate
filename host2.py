import signal
import threading
import json
import time
# Network devices
from network_devices.host_core import Host

# Crear instancia del host
host2 = Host(
    host_name="Host2",
    mac_address="00:11:22:33:44:56",
    ip_address="",
    logical_port_connected_to="2",
    switch_ip="127.0.0.1",
    switch_port=49000
)
# Conectar el host al switch
host2.connect_to_switch()

# Función para escuchar paquetes desde el switch
def listen_for_packets():
    while True:
        host2.receive_packet()

# Inicia un hilo para escuchar paquetes
listener_thread = threading.Thread(target=listen_for_packets, daemon=True)
listener_thread.start()


packet = {
    "type": "normal",
    "packet_id": 1,
    "src_mac": host2.host_mac_address,
    "dst_mac": "00:11:22:33:44:55",  
    "src_ip": host2.ip_address,
    "dst_ip": "172.16.16.2",
    "sw_port": host2.host_logical_port_connected_to,
    "message": "Hello, network!",
    "host_name": host2.host_name
}


time.sleep(5)
host2.send_packet(packet)

# Enviar un paquete al switch




# Manejo de señales para cerrar el proceso correctamente
def signal_handler(sig, frame):
    print("\n Exiting Host...")
    host2.disconnect_from_switch()  # Asegúrate de cerrar el socket
    exit(0)

signal.signal(signal.SIGINT, signal_handler)




# Mantener el host corriendo indefinidamente
while True:
    pass  # El proceso seguirá corriendo hasta que reciba Ctrl+C


