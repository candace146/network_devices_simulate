import json
import threading
import signal
import socket
import sys

## Import Network Devices
from network_devices.switch_core import Switch

# Signal handler
def signal_handler(sig, frame):
    switch.stop()
    print("\n Exiting...") # Llama al método para detener el switch
    sys.exit(0)

# Main script
if __name__ == "__main__":
    try:
        # Initialize switch instance
        switch = Switch("sw1", 4)
        
        # Start switch operations
        switch.start_switch_socket()
        switch.start()  # Comienza el hilo para aceptar conexiones
        
        # Setup signal handler
        signal.signal(signal.SIGINT, signal_handler)
        
        # Keep the main thread alive
        while True:
            pass  # El programa sigue corriendo hasta que se reciba Ctrl+C
    except Exception as e:
        switch.stop()
        print(f" An error occurred: {e}")
