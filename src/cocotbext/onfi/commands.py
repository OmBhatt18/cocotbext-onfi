'''import cocotb
from cocotb.triggers import Timer
import sys
import os
from cocotb.clock import Clock
from cocotb.triggers import FallingEdge, RisingEdge, Timer
from bus import Bus
from memory import sigdict
import re
cmds = {
    'reset': {
        'cmd1': 0xFF,
        'addr_len': None,
        'cmd2': None,
        'data': None,
        'await_data': False,
        'primary_delay': {'tWB': '100ns'},
        'secondary_delay': {'tRST': '500us'}  # Confirmed from Figure 5-5 .
    },
    'sync_reset': {
        'cmd1': 0xFC,
        'addr_len': None,
        'cmd2': None,
        'data': None,
        'await_data': False,
        'primary_delay': {'tWB': '100ns'},
        'secondary_delay': {'tRST': '500us'}  # Confirmed from Figure 5-6 .
    },
    'reset_lun': {
        'cmd1': 0xFA,
        'addr_len': 3,
        'cmd2': None,
        'data': None,
        'await_data': False,
        'primary_delay': {'tWB': '100ns'},
        'secondary_delay': {'tLUN_RST': '100us'}  # Confirmed from Figure 5-7 .
    },
    'read_device_id': {
        'cmd1': 0x90,
        'addr_len': 1,
        'cmd2': None,
        'data': None,
        'await_data': True,
        'primary_delay': {'tWB': '100ns'},
        'secondary_delay': {'tWHR': '80ns'}  # Confirmed from Figure 5-8 .
    },
    'read_param_page': {
        'cmd1': 0xEC,
        'addr_len': 1,
        'cmd2': None,
        'data': None,
        'await_data': True,
        'primary_delay': {'tR': '200us'},
        'secondary_delay': {'tRR': '20ns'}  # Confirmed from Read Parameter Page timing details .
    },
    'read_unique_id': {
        'cmd1': 0xED,
        'addr_len': 1,
        'cmd2': None,
        'data': None,
        'await_data': True,
        'primary_delay': {'tR': '200us'},
        'secondary_delay': {'tRR': '20ns'}  # Confirmed from Read Unique ID timing details .
    },
    'block_erase': {
        'cmd1': 0x60,
        'addr_len': 3,
        'cmd2': 0xD0,
        'data': None,
        'await_data': False,
        'primary_delay': {'tWB': '100ns'},
        'secondary_delay': {'tBERS': '3ms'}  # Confirmed from Block Erase timing details .
    },
    'read_status': {
        'cmd1': 0x70,
        'addr_len': None,
        'cmd2': None,
        'data': None,
        'await_data': True,
        'primary_delay': {'tWHR': '80ns'},
        'secondary_delay': {}  # Confirmed from Read Status timing details .
    },
    'read_status_enhanced': {
        'cmd1': 0x78,
        'addr_len': 3,
        'cmd2': None,
        'data': None,
        'await_data': True,
        'primary_delay': {'tWHR': '80ns'},
        'secondary_delay': {}  # Confirmed from Read Status Enhanced timing details .
    },
    'standard_read': {
        'cmd1': 0x00,
        'addr_len': 5,
        'cmd2': 0x30,
        'data': None,
        'await_data': True,
        'primary_delay': {'tWB': '100ns'},
        'secondary_delay': {'tR': '200us', 'tRR': '20ns'}  # Confirmed from Read timing details .
    },
    'read_cache_sequential': {
        'cmd1': 0x31,
        'addr_len': None,
        'cmd2': None,
        'data': None,
        'await_data': True,
        'primary_delay': {'tRCBSY': '250us'},
        'secondary_delay': {'tWB': '100ns', 'tRR': '20ns'}  
    },
    'read_cache_random': {
        'cmd1': 0x00,
        'addr_len': 5,
        'cmd2': 0x31,
        'data': None,
        'await_data': True,
        'primary_delay': {'tRCBSY': '250us'},
        'secondary_delay': {'tWB': '100ns', 'tRR': '20ns'}  
    },
    'block_erase': {
        'cmd1': 0x60,
        'addr_len': 3,
        'cmd2': 0xD0,
        'data': None,
        'await_data': False,
        'primary_delay': {'tWB': '100ns'},
        'secondary_delay': {'tBERS': '3ms'}  # Confirmed from Block Erase timing details&#8203;:contentReference[oaicite:3]{index=3}.
    },
    'read_status': {
        'cmd1': 0x70,
        'addr_len': None,
        'cmd2': None,
        'data': None,
        'await_data': True,
        'primary_delay': {'tWHR': '80ns'},
        'secondary_delay': {}  # Confirmed from Read Status timing details]
    },
    'read_status_enhanced': {
        'cmd1': 0x78,
        'addr_len': 3,
        'cmd2': None,
        'data': None,
        'await_data': True,
        'primary_delay': {'tWHR': '80ns'},
        'secondary_delay': {}  # Confirmed from Read Status Enhanced timing 
    },
    'read_device_id': {
        'cmd1': 0x90,
        'addr_len': 1,
        'cmd2': None,
        'data': None,
        'await_data': True,
        'primary_delay': {'tWB': '100ns'},
        'secondary_delay': {'tWHR': '80ns'}  # Confirmed from Read ID timing details&#8203;:contentReference[oaicite:6]{index=6}.
    },
    'read_param_page': {
        'cmd1': 0xEC,
        'addr_len': 1,
        'cmd2': None,
        'data': None,
        'await_data': True,
        'primary_delay': {'tR': '200us'},
        'secondary_delay': {'tRR': '20ns'}  # Confirmed from Read Parameter Page timing details&#8203;:contentReference[oaicite:7]{index=7}.
    },
    'read_unique_id': {
        'cmd1': 0xED,
        'addr_len': 1,
        'cmd2': None,
        'data': None,
        'await_data': True,
        'primary_delay': {'tR': '200us'},
        'secondary_delay': {'tRR': '20ns'}  # Confirmed from Read Unique ID timing details&#8203;:contentReference[oaicite:8]{index=8}.
    },
    'reset_lun': {
        'cmd1': 0xFA,
        'addr_len': 3,
        'cmd2': None,
        'data': None,
        'await_data': False,
        'primary_delay': {},
        'secondary_delay': {'tLUN_RST': '100us'}  # Confirmed from Reset LUN timing details&#8203;:contentReference[oaicite:9]{index=9}.
    },
    'copyback_read': {
        'cmd1': 0x00,
        'addr_len': 5,
        'cmd2': 0x35,
        'data': None,
        'await_data': False,
        'primary_delay': {'tR': '200us', 'tWB': '100ns'},
        'secondary_delay': {'tCCS': '500ns'}  # Confirmed from Copyback timing details&#8203;:contentReference[oaicite:0]{index=0}.
    },
    'copyback_read_with_data_output': {
        'cmd1': 0x05,
        'addr_len': 5,
        'cmd2': 0xE0,
        'data': None,
        'await_data': True,
        'primary_delay': {'tCCS': '500ns'},
        'secondary_delay': {'tRR': '20ns', 'tWB': '100ns'}  # Confirmed from Figure 5-30&#8203;:contentReference[oaicite:1]{index=1}.
    },
    'copyback_program': {
        'cmd1': 0x85,
        'addr_len': 5,
        'cmd2': 0x10,
        'data': None,
        'await_data': False,
        'primary_delay': {'tADL': '100ns'},
        'secondary_delay': {'tPROG': '700us', 'tCCS': '500ns'}  # Based on timing details in Figure 5-31&#8203;:contentReference[oaicite:2]{index=2}.
    },
    'zq_calibration_long': {
        'cmd1': 0xF9,
        'addr_len': 1,
        'cmd2': None,
        'data': None,
        'await_data': False,
        'primary_delay': {'tZQCL': '1ms'},
        'secondary_delay': {'tWB': '100ns'}  # Confirmed from ZQ Calibration Long details .
    },
    'zq_calibration_short': {
        'cmd1': 0xFB,
        'addr_len': 1,
        'cmd2': None,
        'data': None,
        'await_data': False,
        'primary_delay': {'tZQCS': '250us'},
        'secondary_delay': {'tWB': '100ns'}  # Confirmed from ZQ Calibration Short details .
    },
    'get_feature': {
        'cmd1': 0xEE,
        'addr_len': 1,
        'cmd2': None,
        'data': None,
        'await_data': True,
        'primary_delay': {'tFEAT': '1us'},
        'secondary_delay': {'tRR': '20ns'}  # Confirmed from the Get Feature command timing .
    },
    'set_feature': {
        'cmd1': 0xEF,
        'addr_len': 1,
        'cmd2': None,
        'data': [0x00, 0x00, 0x00, 0x00],
        'await_data': False,
        'primary_delay': {'tADL': '100ns'},
        'secondary_delay': {'tWB': '100ns'}  # Based on Set Feature command timing details .
    },
    'read_page': {
        'cmd1': 0x00,
        'addr_len': 5,
        'cmd2': 0x30,
        'data': None,
        'await_data': True,
        'primary_delay': {'tWB': '100ns'},
        'secondary_delay': {'tR': '200us'}  # Confirmed from Read Page timing .
    },
    'multi_plane_page_read': {
        'cmd1': 0x00,
        'addr_len': 5,
        'cmd2': 0x32,
        'data': None,
        'await_data': True,
        'primary_delay': {'tPLRBSY': '200us'},
        'secondary_delay': {'tWB': '100ns'}  # Based on Multi-plane Page Read timing details .
    },
    'multi_plane_program': {
        'cmd1': 0x80,
        'addr_len': 5,
        'cmd2': 0x11,
        'data': None,
        'await_data': False,
        'primary_delay': {'tPLPBSY': '700us'},
        'secondary_delay': {'tWB': '100ns'}  # Based on Multi-plane Program timing details .
    }
}
async def txn(name, dut, bus=None, byte=None, addr=None, data=None):
    txn_template = cmds[name]
    txdata = []
    signal_keywords = ["CLE", "ALE", "WE", "RE", "CE", "bus"]  # Added 'bus' as a keyword

    # Initialize the Bus with the DUT
    bus = Bus(dut)

    # Get available signals in the Bus
    bus_signal_names = dir(bus)
    print("Available signals in Bus:", bus_signal_names)

    # Collect relevant signals that need to be driven
    relevant_signals = {}
    for sig_name in bus_signal_names:
        actual_name = bus.get_actual_signal_name(sig_name)
        if any(keyword in actual_name for keyword in signal_keywords):
            relevant_signals[actual_name] = getattr(bus, sig_name)

    # Drive relevant signals
    for sig_name, sig_obj in relevant_signals.items():
        keyword = next((kw for kw in signal_keywords if kw in sig_name), None)
        signal_value = txn_template.get(keyword, None)
        if signal_value is not None:
            sig_obj.value = signal_value
            print(f"Driving {sig_name} to {signal_value}")
        else:
            print(f"Warning: No value found for {sig_name} in the txn template. Skipping.")

    # Helper function to send a command
    async def _send_command(bus, cmd):
        if hasattr(bus, 'CLE'):
            bus.CLE.value = 1  # Command Latch Enable
        if hasattr(bus, 'ALE'):
            bus.ALE.value = 0  # Address Latch Disable
        bus.IObus.value = cmd
        print(f"Sending command: {cmd}")
        await Timer(10, units='ns')
        if hasattr(bus, 'CLE'):
            bus.CLE.value = 0

    
    async def _send_address(bus, addr, addr_len):
        if hasattr(bus, 'ALE'):
            bus.ALE.value = 1  # Address Latch Enable
        for byte in addr[:addr_len]:
            bus.IObus.value = byte
            print(f"Sending address byte: {byte}")
            await Timer(10, units='ns')
        if hasattr(bus, 'ALE'):
            bus.ALE.value = 0

    
    async def _send_data(bus, data):
        for byte in data:
            bus.IObus.value = byte
            print(f"Sending data byte: {byte}")
            await Timer(10, units='ns')

    
    async def _read_data(bus):
        read_data = []
        for _ in range(8):  # Example loop for 8 bytes; adjust as needed
            await Timer(10, units='ns')
            read_data.append(bus.IObus.value)
            print(f"Read data byte: {bus.IObus.value}")
        return read_data

    
    async def _get_bytes(length):
        read_data = []
        for _ in range(length):
            await Timer(10, units='ns')
            read_data.append(dut.IObus.value.integer)
        print(f"Received data: {read_data}")
        return read_data

    
    if txn_template.get('cmd1') is not None:
        await _send_command(bus, txn_template['cmd1'])

    
    if 'primary_delay' in txn_template:
        for delay_name, delay_time in txn_template['primary_delay'].items():
            await Timer(int(delay_time.rstrip('nsus')), units=delay_time[-2:])

    
    if txn_template.get('addr_len') is not None:
        if addr is None:
            addr = [0x00] * txn_template['addr_len']
        txdata.extend(addr[:txn_template['addr_len']])
        await _send_address(bus, addr, txn_template['addr_len'])

    
    if data is None and txn_template.get('data') is not None:
        data = txn_template['data']
    if data is not None:
        txdata.extend(data)
        await _send_data(bus, data)

    
    if txn_template.get('cmd2') is not None:
        await _send_command(bus, txn_template['cmd2'])

    
    if 'secondary_delay' in txn_template:
        for delay_name, delay_time in txn_template['secondary_delay'].items():
            await Timer(int(delay_time.rstrip('nsus')), units=delay_time[-2:])

    
    if txn_template.get('await_data'):
        rv = await _read_data(bus)
        return rv

    
    for i in range(8):
        signal_name_0 = f"IO{i}_0"
        signal_name_1 = f"IO{i}_1"
        if hasattr(bus, signal_name_0):
            getattr(bus, signal_name_0).value = (byte >> i) & 0x1
        else:
            print(f"Warning: Signal {signal_name_0} not found in Bus. Skipping.")
        if hasattr(bus, signal_name_1):
            getattr(bus, signal_name_1).value = (byte >> (i + 8)) & 0x1
        else:
            print(f"Warning: Signal {signal_name_1} not found in Bus. Skipping.")

    
    dut.IO_bus.value = byte
    print(f"Set IO bus value to {byte}")

    # Completion Signal Check
    if txn_template.get('await_data'):
        rv = await _get_bytes(len(txdata))
        return rv
    else:
        return None

async def _drive_to_io_ports(dut, bus, byte):
    for i in range(8):
        signal_name_0 = f"IO{i}_0"
        signal_name_1 = f"IO{i}_1"

        if hasattr(bus, signal_name_0):
            setattr(getattr(bus, signal_name_0), 'value', (byte >> i) & 0x1)
        else:
            print(f"Warning: Signal {signal_name_0} not found in Bus. Skipping.")

        if hasattr(bus, signal_name_1):
            setattr(getattr(bus, signal_name_1), 'value', (byte >> (i + 8)) & 0x1)
        else:
            print(f"Warning: Signal {signal_name_1} not found in Bus. Skipping.")
        dut.IO_bus.value = byte

async def _get_bytes(num_bytes):
    rv = [0xFF] * num_bytes  
    return rv
def parse_delay(delay_time):
    
    Parse a delay string into its numeric value and unit.
    Supports delays in the format <number><unit> where unit is one or more letters (e.g., 'ns', 'us', 'ms', 's', etc.).
    """
    match = re.fullmatch(r'(\d+)([a-zA-Z]+)', delay_time)
    if not match:
        raise ValueError(f"Invalid delay format: {delay_time}")
    num_str, unit = match.groups()
    return int(num_str), unit

async def txn(name, dut, bus=None, byte=None, addr=None, data=None):
    txn_template = cmds[name]
    txdata = []
    signal_keywords = ["CLE", "ALE", "WE", "RE", "CE", "bus"]  # Added 'bus' as a keyword

    # Initialize the Bus with the DUT
    bus = Bus(dut)

    # Get available signals in the Bus
    bus_signal_names = dir(bus)
    print("Available signals in Bus:", bus_signal_names)

    # Collect relevant signals that need to be driven
    relevant_signals = {}
    for sig_name in bus_signal_names:
        actual_name = bus.get_actual_signal_name(sig_name)
        if any(keyword in actual_name for keyword in signal_keywords):
            relevant_signals[actual_name] = getattr(bus, sig_name)

    # Drive relevant signals
    for sig_name, sig_obj in relevant_signals.items():
        keyword = next((kw for kw in signal_keywords if kw in sig_name), None)
        signal_value = txn_template.get(keyword, None)
        if signal_value is not None:
            sig_obj.value = signal_value
            print(f"Driving {sig_name} to {signal_value}")
        else:
            print(f"Warning: No value found for {sig_name} in the txn template. Skipping.")

    # Helper function to send a command
    async def _send_command(bus, cmd):
        if hasattr(bus, 'CLE'):
            bus.CLE.value = 1  # Command Latch Enable
        if hasattr(bus, 'ALE'):
            bus.ALE.value = 0  # Address Latch Disable
        bus.IObus.value = cmd
        print(f"Sending command: {cmd}")
        await Timer(10, units='ns')
        if hasattr(bus, 'CLE'):
            bus.CLE.value = 0

    async def _send_address(bus, addr, addr_len):
        if hasattr(bus, 'ALE'):
            bus.ALE.value = 1  # Address Latch Enable
        for byte in addr[:addr_len]:
            bus.IObus.value = byte
            print(f"Sending address byte: {byte}")
            await Timer(10, units='ns')
        if hasattr(bus, 'ALE'):
            bus.ALE.value = 0

    async def _send_data(bus, data):
        for byte in data:
            bus.IObus.value = byte
            print(f"Sending data byte: {byte}")
            await Timer(10, units='ns')

    async def _read_data(bus):
        read_data = []
        for _ in range(8):  # Example loop for 8 bytes; adjust as needed
            await Timer(10, units='ns')
            read_data.append(bus.IObus.value)
            print(f"Read data byte: {bus.IObus.value}")
        return read_data

    async def _get_bytes(length):
        read_data = []
        for _ in range(length):
            await Timer(10, units='ns')
            read_data.append(dut.IObus.value.integer)
        print(f"Received data: {read_data}")
        return read_data

    if txn_template.get('cmd1') is not None:
        await _send_command(bus, txn_template['cmd1'])

    if 'primary_delay' in txn_template:
        for delay_name, delay_time in txn_template['primary_delay'].items():
            numeric_value, unit = parse_delay(delay_time)
            await Timer(numeric_value, units=unit)

    if txn_template.get('addr_len') is not None:
        if addr is None:
            addr = [0x00] * txn_template['addr_len']
        txdata.extend(addr[:txn_template['addr_len']])
        await _send_address(bus, addr, txn_template['addr_len'])

    if data is None and txn_template.get('data') is not None:
        data = txn_template['data']
    if data is not None:
        txdata.extend(data)
        await _send_data(bus, data)

    if txn_template.get('cmd2') is not None:
        await _send_command(bus, txn_template['cmd2'])

    if 'secondary_delay' in txn_template:
        for delay_name, delay_time in txn_template['secondary_delay'].items():
            numeric_value, unit = parse_delay(delay_time)
            await Timer(numeric_value, units=unit)

    if txn_template.get('await_data'):
        rv = await _read_data(bus)
        return rv

    for i in range(8):
        signal_name_0 = f"IO{i}_0"
        signal_name_1 = f"IO{i}_1"
        if hasattr(bus, signal_name_0):
            getattr(bus, signal_name_0).value = (byte >> i) & 0x1
        else:
            print(f"Warning: Signal {signal_name_0} not found in Bus. Skipping.")
        if hasattr(bus, signal_name_1):
            getattr(bus, signal_name_1).value = (byte >> (i + 8)) & 0x1
        else:
            print(f"Warning: Signal {signal_name_1} not found in Bus. Skipping.")

    dut.IO_bus.value = byte
    print(f"Set IO bus value to {byte}")

    # Completion Signal Check
    if txn_template.get('await_data'):
        rv = await _get_bytes(len(txdata))
        return rv
    else:
        return None '''

##all woorking except 4 below
'''import cocotb
from cocotb.triggers import Timer
import sys
import os
from cocotb.clock import Clock
from cocotb.triggers import FallingEdge, RisingEdge, Timer
from bus import Bus
from memory import sigdict
import re

# Original commands plus new definitions for the missing ones
cmds = {
    'reset': {
        'cmd1': 0xFF,
        'addr_len': None,
        'cmd2': None,
        'data': None,
        'await_data': False,
        'primary_delay': {'tWB': '100ns'},
        'secondary_delay': {'tRST': '500us'}  # Confirmed from Figure 5-5.
    },
    'sync_reset': {
        'cmd1': 0xFC,
        'addr_len': None,
        'cmd2': None,
        'data': None,
        'await_data': False,
        'primary_delay': {'tWB': '100ns'},
        'secondary_delay': {'tRST': '500us'}  # Confirmed from Figure 5-6.
    },
    'reset_lun': {
        'cmd1': 0xFA,
        'addr_len': 3,
        'cmd2': None,
        'data': None,
        'await_data': False,
        'primary_delay': {'tWB': '100ns'},
        'secondary_delay': {'tLUN_RST': '100us'}  # Confirmed from Figure 5-7.
    },
    'read_device_id': {
        'cmd1': 0x90,
        'addr_len': 1,
        'cmd2': None,
        'data': None,
        'await_data': True,
        'primary_delay': {'tWB': '100ns'},
        'secondary_delay': {'tWHR': '80ns'}  # Confirmed from Figure 5-8.
    },
    'read_param_page': {
        'cmd1': 0xEC,
        'addr_len': 1,
        'cmd2': None,
        'data': None,
        'await_data': True,
        'primary_delay': {'tR': '200us'},
        'secondary_delay': {'tRR': '20ns'}  # Confirmed from Read Parameter Page timing details.
    },
    'read_unique_id': {
        'cmd1': 0xED,
        'addr_len': 1,
        'cmd2': None,
        'data': None,
        'await_data': True,
        'primary_delay': {'tR': '200us'},
        'secondary_delay': {'tRR': '20ns'}  # Confirmed from Read Unique ID timing details.
    },
    'block_erase': {
        'cmd1': 0x60,
        'addr_len': 3,
        'cmd2': 0xD0,
        'data': None,
        'await_data': False,
        'primary_delay': {'tWB': '100ns'},
        'secondary_delay': {'tBERS': '3ms'}  # Confirmed from Block Erase timing details.
    },
    'read_status': {
        'cmd1': 0x70,
        'addr_len': None,
        'cmd2': None,
        'data': None,
        'await_data': True,
        'primary_delay': {'tWHR': '80ns'},
        'secondary_delay': {}  # Confirmed from Read Status timing details.
    },
    'read_status_enhanced': {
        'cmd1': 0x78,
        'addr_len': 3,
        'cmd2': None,
        'data': None,
        'await_data': True,
        'primary_delay': {'tWHR': '80ns'},
        'secondary_delay': {}  # Confirmed from Read Status Enhanced timing details.
    },
    'standard_read': {
        'cmd1': 0x00,
        'addr_len': 5,
        'cmd2': 0x30,
        'data': None,
        'await_data': True,
        'primary_delay': {'tWB': '100ns'},
        'secondary_delay': {'tR': '200us', 'tRR': '20ns'}  # Confirmed from Read timing details.
    },
    'read_cache_sequential': {
        'cmd1': 0x31,
        'addr_len': None,
        'cmd2': None,
        'data': None,
        'await_data': True,
        'primary_delay': {'tRCBSY': '250us'},
        'secondary_delay': {'tWB': '100ns', 'tRR': '20ns'}  
    },
    'read_cache_random': {
        'cmd1': 0x00,
        'addr_len': 5,
        'cmd2': 0x31,
        'data': None,
        'await_data': True,
        'primary_delay': {'tRCBSY': '250us'},
        'secondary_delay': {'tWB': '100ns', 'tRR': '20ns'}  
    },
    # Duplicate keys removed if any; below we add new ones if needed.
    'copyback_read': {
        'cmd1': 0x00,
        'addr_len': 5,
        'cmd2': 0x35,
        'data': None,
        'await_data': False,
        'primary_delay': {'tR': '200us', 'tWB': '100ns'},
        'secondary_delay': {'tCCS': '500ns'}  # Confirmed from Copyback timing details.
    },
    'copyback_read_with_data_output': {
        'cmd1': 0x05,
        'addr_len': 5,
        'cmd2': 0xE0,
        'data': None,
        'await_data': True,
        'primary_delay': {'tCCS': '500ns'},
        'secondary_delay': {'tRR': '20ns', 'tWB': '100ns'}  # Confirmed from Figure 5-30.
    },
    'copyback_program': {
        'cmd1': 0x85,
        'addr_len': 5,
        'cmd2': 0x10,
        'data': None,
        'await_data': False,
        'primary_delay': {'tADL': '100ns'},
        'secondary_delay': {'tPROG': '700us', 'tCCS': '500ns'}  # Based on timing details in Figure 5-31.
    },
    # New command added to support the "with data modification" variant
    'copyback_program_with_data_mod': {
        'cmd1': 0x85,   # You may change this opcode if it differs from the basic copyback program
        'addr_len': 5,
        'cmd2': 0x10,   # Confirmation opcode (if needed)
        'data': None,   # Or optionally provide default data
        'await_data': False,
        'primary_delay': {'tADL': '100ns'},
        'secondary_delay': {'tPROG': '700us', 'tCCS': '500ns'}  # Adjust delays if required
    },
    'zq_calibration_long': {
        'cmd1': 0xF9,
        'addr_len': 1,
        'cmd2': None,
        'data': None,
        'await_data': False,
        'primary_delay': {'tZQCL': '1ms'},
        'secondary_delay': {'tWB': '100ns'}  # Confirmed from ZQ Calibration Long details.
    },
    'zq_calibration_short': {
        'cmd1': 0xFB,
        'addr_len': 1,
        'cmd2': None,
        'data': None,
        'await_data': False,
        'primary_delay': {'tZQCS': '250us'},
        'secondary_delay': {'tWB': '100ns'}  # Confirmed from ZQ Calibration Short details.
    },
    'get_feature': {
        'cmd1': 0xEE,
        'addr_len': 1,
        'cmd2': None,
        'data': None,
        'await_data': True,
        'primary_delay': {'tFEAT': '1us'},
        'secondary_delay': {'tRR': '20ns'}  # Confirmed from the Get Feature command timing.
    },
    'set_feature': {
        'cmd1': 0xEF,
        'addr_len': 1,
        'cmd2': None,
        'data': [0x00, 0x00, 0x00, 0x00],
        'await_data': False,
        'primary_delay': {'tADL': '100ns'},
        'secondary_delay': {'tWB': '100ns'}  # Based on Set Feature command timing details.
    },
    'read_page': {
        'cmd1': 0x00,
        'addr_len': 5,
        'cmd2': 0x30,
        'data': None,
        'await_data': True,
        'primary_delay': {'tWB': '100ns'},
        'secondary_delay': {'tR': '200us'}  # Confirmed from Read Page timing.
    },
    # New commands for multi-plane operations:
    'multi_plane_page_program': {
        'cmd1': 0x80,    # Example opcode for multi-plane page program
        'addr_len': 5,
        'cmd2': 0x11,    # Second-phase opcode if required
        'data': None,
        'await_data': False,
        'primary_delay': {'tPLPBSY': '700us'},
        'secondary_delay': {'tWB': '100ns'}
    },
    'multi_plane_block_erase': {
        'cmd1': 0x60,    # Erase command for multi-plane
        'addr_len': 3,
        'cmd2': 0xD0,    # Confirm command
        'data': None,
        'await_data': False,
        'primary_delay': {'tWB': '100ns'},
        'secondary_delay': {'tBERS': '3ms'}
    },
    'multi_plane_page_read': {
        'cmd1': 0x00,
        'addr_len': 5,
        'cmd2': 0x32,
        'data': None,
        'await_data': True,
        'primary_delay': {'tPLRBSY': '200us'},
        'secondary_delay': {'tWB': '100ns'}  # Based on Multi-plane Page Read timing details.
    },
    'multi_plane_program': {
        'cmd1': 0x80,
        'addr_len': 5,
        'cmd2': 0x11,
        'data': None,
        'await_data': False,
        'primary_delay': {'tPLPBSY': '700us'},
        'secondary_delay': {'tWB': '100ns'}  # Based on Multi-plane Program timing details.
    }
}

def parse_delay(delay_time):
    """
    Parse a delay string into its numeric value and unit.
    Supports delays in the format <number><unit> where unit is one or more letters (e.g., 'ns', 'us', 'ms', 's', etc.).
    """
    match = re.fullmatch(r'(\d+)([a-zA-Z]+)', delay_time)
    if not match:
        raise ValueError(f"Invalid delay format: {delay_time}")
    num_str, unit = match.groups()
    return int(num_str), unit

async def txn(name, dut, bus=None, byte=None, addr=None, data=None):
    txn_template = cmds[name]
    txdata = []
    signal_keywords = ["CLE", "ALE", "WE", "RE", "CE", "bus"]  # Added 'bus' as a keyword

    # Initialize the Bus with the DUT
    bus = Bus(dut)

    # Get available signals in the Bus
    bus_signal_names = dir(bus)
    print("Available signals in Bus:", bus_signal_names)

    # Collect relevant signals that need to be driven
    relevant_signals = {}
    for sig_name in bus_signal_names:
        actual_name = bus.get_actual_signal_name(sig_name)
        if any(keyword in actual_name for keyword in signal_keywords):
            relevant_signals[actual_name] = getattr(bus, sig_name)

    # Drive relevant signals
    for sig_name, sig_obj in relevant_signals.items():
        keyword = next((kw for kw in signal_keywords if kw in sig_name), None)
        signal_value = txn_template.get(keyword, None)
        if signal_value is not None:
            sig_obj.value = signal_value
            print(f"Driving {sig_name} to {signal_value}")
        else:
            print(f"Warning: No value found for {sig_name} in the txn template. Skipping.")

    # Helper function to send a command
    async def _send_command(bus, cmd):
        if hasattr(bus, 'CLE'):
            bus.CLE.value = 1  # Command Latch Enable
        if hasattr(bus, 'ALE'):
            bus.ALE.value = 0  # Address Latch Disable
        bus.IObus.value = cmd
        print(f"Sending command: {cmd}")
        await Timer(10, units='ns')
        if hasattr(bus, 'CLE'):
            bus.CLE.value = 0

    async def _send_address(bus, addr, addr_len):
        if hasattr(bus, 'ALE'):
            bus.ALE.value = 1  # Address Latch Enable
        for byte in addr[:addr_len]:
            bus.IObus.value = byte
            print(f"Sending address byte: {byte}")
            await Timer(10, units='ns')
        if hasattr(bus, 'ALE'):
            bus.ALE.value = 0

    async def _send_data(bus, data):
        for byte in data:
            bus.IObus.value = byte
            print(f"Sending data byte: {byte}")
            await Timer(10, units='ns')

    async def _read_data(bus):
        read_data = []
        for _ in range(8):  # Example loop for 8 bytes; adjust as needed
            await Timer(10, units='ns')
            read_data.append(bus.IObus.value)
            print(f"Read data byte: {bus.IObus.value}")
        return read_data

    async def _get_bytes(length):
        read_data = []
        for _ in range(length):
            await Timer(10, units='ns')
            read_data.append(dut.IObus.value.integer)
        print(f"Received data: {read_data}")
        return read_data

    if txn_template.get('cmd1') is not None:
        await _send_command(bus, txn_template['cmd1'])

    if 'primary_delay' in txn_template:
        for delay_name, delay_time in txn_template['primary_delay'].items():
            numeric_value, unit = parse_delay(delay_time)
            await Timer(numeric_value, units=unit)

    if txn_template.get('addr_len') is not None:
        if addr is None:
            addr = [0x00] * txn_template['addr_len']
        txdata.extend(addr[:txn_template['addr_len']])
        await _send_address(bus, addr, txn_template['addr_len'])

    if data is None and txn_template.get('data') is not None:
        data = txn_template['data']
    if data is not None:
        txdata.extend(data)
        await _send_data(bus, data)

    if txn_template.get('cmd2') is not None:
        await _send_command(bus, txn_template['cmd2'])

    if 'secondary_delay' in txn_template:
        for delay_name, delay_time in txn_template['secondary_delay'].items():
            numeric_value, unit = parse_delay(delay_time)
            await Timer(numeric_value, units=unit)

    if txn_template.get('await_data'):
        rv = await _read_data(bus)
        return rv

    # Only drive IO ports if a byte value is provided.
    if byte is not None:
        for i in range(8):
            signal_name_0 = f"IO{i}_0"
            signal_name_1 = f"IO{i}_1"
            if hasattr(bus, signal_name_0):
                getattr(bus, signal_name_0).value = (byte >> i) & 0x1
            else:
                print(f"Warning: Signal {signal_name_0} not found in Bus. Skipping.")
            if hasattr(bus, signal_name_1):
                getattr(bus, signal_name_1).value = (byte >> (i + 8)) & 0x1
            else:
                print(f"Warning: Signal {signal_name_1} not found in Bus. Skipping.")
        if hasattr(dut, "IO_bus"):
            dut.IO_bus.value = byte
            print(f"Set IO bus value to {byte}")
        else:
            print("Warning: DUT does not contain IO_bus signal. Skipping IO bus update.")

    # Completion Signal Check
    if txn_template.get('await_data'):
        rv = await _get_bytes(len(txdata))
        return rv
    else:
        return None '''
import cocotb
from cocotb.triggers import Timer
import sys
import os
from cocotb.clock import Clock
from cocotb.triggers import FallingEdge, RisingEdge, Timer
from bus import Bus
from memory import sigdict
import re

# Original commands plus new definitions for the missing ones
cmds = {
    'reset': {
        'cmd1': 0xFF,
        'addr_len': None,
        'cmd2': None,
        'data': None,
        'await_data': False,
        'primary_delay': {'tWB': '100ns'},
        'secondary_delay': {'tRST': '500us'}  # Confirmed from Figure 5-5.
    },
    'sync_reset': {
        'cmd1': 0xFC,
        'addr_len': None,
        'cmd2': None,
        'data': None,
        'await_data': False,
        'primary_delay': {'tWB': '100ns'},
        'secondary_delay': {'tRST': '500us'}  # Confirmed from Figure 5-6.
    },
    'reset_lun': {
        'cmd1': 0xFA,
        'addr_len': 3,
        'cmd2': None,
        'data': None,
        'await_data': False,
        'primary_delay': {'tWB': '100ns'},
        'secondary_delay': {'tLUN_RST': '100us'}  # Confirmed from Figure 5-7.
    },
    'read_device_id': {
        'cmd1': 0x90,
        'addr_len': 1,
        'cmd2': None,
        'data': None,
        'await_data': True,
        'primary_delay': {'tWB': '100ns'},
        'secondary_delay': {'tWHR': '80ns'}  # Confirmed from Figure 5-8.
    },
    'read_param_page': {
        'cmd1': 0xEC,
        'addr_len': 1,
        'cmd2': None,
        'data': None,
        'await_data': True,
        'primary_delay': {'tR': '200us'},
        'secondary_delay': {'tRR': '20ns'}  # Confirmed from Read Parameter Page timing details.
    },
    'read_unique_id': {
        'cmd1': 0xED,
        'addr_len': 1,
        'cmd2': None,
        'data': None,
        'await_data': True,
        'primary_delay': {'tR': '200us'},
        'secondary_delay': {'tRR': '20ns'}  # Confirmed from Read Unique ID timing details.
    },
    'block_erase': {
        'cmd1': 0x60,
        'addr_len': 3,
        'cmd2': 0xD0,
        'data': None,
        'await_data': False,
        'primary_delay': {'tWB': '100ns'},
        'secondary_delay': {'tBERS': '3ms'}  # Confirmed from Block Erase timing details.
    },
    'read_status': {
        'cmd1': 0x70,
        'addr_len': None,
        'cmd2': None,
        'data': None,
        'await_data': True,
        'primary_delay': {'tWHR': '80ns'},
        'secondary_delay': {}  # Confirmed from Read Status timing details.
    },
    'read_status_enhanced': {
        'cmd1': 0x78,
        'addr_len': 3,
        'cmd2': None,
        'data': None,
        'await_data': True,
        'primary_delay': {'tWHR': '80ns'},
        'secondary_delay': {}  # Confirmed from Read Status Enhanced timing details.
    },
    'standard_read': {
        'cmd1': 0x00,
        'addr_len': 5,
        'cmd2': 0x30,
        'data': None,
        'await_data': True,
        'primary_delay': {'tWB': '100ns'},
        'secondary_delay': {'tR': '200us', 'tRR': '20ns'}  # Confirmed from Read timing details.
    },
    'read_cache_sequential': {
        'cmd1': 0x31,
        'addr_len': None,
        'cmd2': None,
        'data': None,
        'await_data': True,
        'primary_delay': {'tRCBSY': '250us'},
        'secondary_delay': {'tWB': '100ns', 'tRR': '20ns'}
    },
    'read_cache_random': {
        'cmd1': 0x00,
        'addr_len': 5,
        'cmd2': 0x31,
        'data': None,
        'await_data': True,
        'primary_delay': {'tRCBSY': '250us'},
        'secondary_delay': {'tWB': '100ns', 'tRR': '20ns'}
    },
    'copyback_read': {
        'cmd1': 0x00,
        'addr_len': 5,
        'cmd2': 0x35,
        'data': None,
        'await_data': False,
        'primary_delay': {'tR': '200us', 'tWB': '100ns'},
        'secondary_delay': {'tCCS': '500ns'}  # Confirmed from Copyback timing details.
    },
    'copyback_read_with_data_output': {
        'cmd1': 0x05,
        'addr_len': 5,
        'cmd2': 0xE0,
        'data': None,
        'await_data': True,
        'primary_delay': {'tCCS': '500ns'},
        'secondary_delay': {'tRR': '20ns', 'tWB': '100ns'}  # Confirmed from Figure 5-30.
    },
    'copyback_program': {
        'cmd1': 0x85,
        'addr_len': 5,
        'cmd2': 0x10,
        'data': None,
        'await_data': False,
        'primary_delay': {'tADL': '100ns'},
        'secondary_delay': {'tPROG': '700us', 'tCCS': '500ns'}  # Based on timing details in Figure 5-31.
    },
    # New command: copyback_program_with_data_mod (placeholder values)
    'copyback_program_with_data_mod': {
        'cmd1': 0x85,   # Adjust opcode if different from copyback_program
        'addr_len': 5,
        'cmd2': 0x10,
        'data': None,
        'await_data': False,
        'primary_delay': {'tADL': '100ns'},
        'secondary_delay': {'tPROG': '700us', 'tCCS': '500ns'}
    },
    'zq_calibration_long': {
        'cmd1': 0xF9,
        'addr_len': 1,
        'cmd2': None,
        'data': None,
        'await_data': False,
        'primary_delay': {'tZQCL': '1ms'},
        'secondary_delay': {'tWB': '100ns'}  # Confirmed from ZQ Calibration Long details.
    },
    'zq_calibration_short': {
        'cmd1': 0xFB,
        'addr_len': 1,
        'cmd2': None,
        'data': None,
        'await_data': False,
        'primary_delay': {'tZQCS': '250us'},
        'secondary_delay': {'tWB': '100ns'}  # Confirmed from ZQ Calibration Short details.
    },
    'get_feature': {
        'cmd1': 0xEE,
        'addr_len': 1,
        'cmd2': None,
        'data': None,
        'await_data': True,
        'primary_delay': {'tFEAT': '1us'},
        'secondary_delay': {'tRR': '20ns'}  # Confirmed from the Get Feature command timing.
    },
    'set_feature': {
        'cmd1': 0xEF,
        'addr_len': 1,
        'cmd2': None,
        'data': [0x00, 0x00, 0x00, 0x00],
        'await_data': False,
        'primary_delay': {'tADL': '100ns'},
        'secondary_delay': {'tWB': '100ns'}  # Based on Set Feature command timing details.
    },
    'read_page': {
        'cmd1': 0x00,
        'addr_len': 5,
        'cmd2': 0x30,
        'data': None,
        'await_data': True,
        'primary_delay': {'tWB': '100ns'},
        'secondary_delay': {'tR': '200us'}  # Confirmed from Read Page timing.
    },
    # New commands for multi-plane operations:
    'multi_plane_page_program': {
        'cmd1': 0x80,    # Example opcode for multi-plane page program
        'addr_len': 5,
        'cmd2': 0x11,    # Second-phase opcode if required
        'data': None,
        'await_data': False,
        'primary_delay': {'tPLPBSY': '700us'},
        'secondary_delay': {'tWB': '100ns'}
    },
    'multi_plane_block_erase': {
        'cmd1': 0x60,    # Erase command for multi-plane
        'addr_len': 3,
        'cmd2': 0xD0,    # Confirmation command
        'data': None,
        'await_data': False,
        'primary_delay': {'tWB': '100ns'},
        'secondary_delay': {'tBERS': '3ms'}
    },
    'multi_plane_page_read': {
        'cmd1': 0x00,
        'addr_len': 5,
        'cmd2': 0x32,
        'data': None,
        'await_data': True,
        'primary_delay': {'tPLRBSY': '200us'},
        'secondary_delay': {'tWB': '100ns'}  # Based on Multi-plane Page Read timing details.
    },
    'multi_plane_program': {
        'cmd1': 0x80,
        'addr_len': 5,
        'cmd2': 0x11,
        'data': None,
        'await_data': False,
        'primary_delay': {'tPLPBSY': '700us'},
        'secondary_delay': {'tWB': '100ns'}  # Based on Multi-plane Program timing details.
    },
    # New commands for missing tests:
    'random_data_input': {
        'cmd1': 0xA1,  # Example opcode; adjust as needed
        'addr_len': 3,  # Example address length
        'cmd2': None,
        'data': None,
        'await_data': False,
        'primary_delay': {'tRDI': '150ns'},  # Example delay parameter
        'secondary_delay': {'tRDI': '75ns'}    # Example delay parameter
    },
    'random_data_output': {
        'cmd1': 0xA2,  # Example opcode; adjust as needed
        'addr_len': 3,  # Example address length
        'cmd2': None,
        'data': None,
        'await_data': True,
        'primary_delay': {'tRDO': '150ns'},  # Example delay parameter
        'secondary_delay': {'tRDO': '75ns'}    # Example delay parameter
    },
    'program_page': {
        'cmd1': 0x80,  # Example opcode; adjust as needed
        'addr_len': 5,
        'cmd2': 0x10,
        'data': None,
        'await_data': False,
        'primary_delay': {'tPP': '200us'},  # Example delay parameter
        'secondary_delay': {'tWR': '100ns'}   # Example delay parameter
    },
    'program_page_cache': {
        'cmd1': 0x82,  # Example opcode; adjust as needed
        'addr_len': 5,
        'cmd2': 0x30,
        'data': None,
        'await_data': False,
        'primary_delay': {'tPPC': '200us'},  # Example delay parameter
        'secondary_delay': {'tWR': '100ns'}   # Example delay parameter
    },
    'read_page_cache_sequential': {
        'cmd1': 0x84,  # Example opcode; adjust as needed
        'addr_len': 5,
        'cmd2': 0x30,
        'data': None,
        'await_data': True,
        'primary_delay': {'tRPCS': '250us'},  # Example delay parameter
        'secondary_delay': {'tR': '100ns'}      # Example delay parameter
    }
}

def parse_delay(delay_time):
    """
    Parse a delay string into its numeric value and unit.
    Supports delays in the format <number><unit> where unit is one or more letters (e.g., 'ns', 'us', 'ms', 's', etc.).
    """
    match = re.fullmatch(r'(\d+)([a-zA-Z]+)', delay_time)
    if not match:
        raise ValueError(f"Invalid delay format: {delay_time}")
    num_str, unit = match.groups()
    return int(num_str), unit

async def txn(name, dut, bus=None, byte=None, addr=None, data=None):
    txn_template = cmds[name]
    txdata = []
    signal_keywords = ["CLE", "ALE", "WE", "RE", "CE", "bus"]  # Added 'bus' as a keyword

    # Initialize the Bus with the DUT
    bus = Bus(dut)

    # Get available signals in the Bus
    bus_signal_names = dir(bus)
    print("Available signals in Bus:", bus_signal_names)

    # Collect relevant signals that need to be driven
    relevant_signals = {}
    for sig_name in bus_signal_names:
        actual_name = bus.get_actual_signal_name(sig_name)
        if any(keyword in actual_name for keyword in signal_keywords):
            relevant_signals[actual_name] = getattr(bus, sig_name)

    # Drive relevant signals
    for sig_name, sig_obj in relevant_signals.items():
        keyword = next((kw for kw in signal_keywords if kw in sig_name), None)
        signal_value = txn_template.get(keyword, None)
        if signal_value is not None:
            sig_obj.value = signal_value
            print(f"Driving {sig_name} to {signal_value}")
        else:
            print(f"Warning: No value found for {sig_name} in the txn template. Skipping.")

    # Helper function to send a command
    async def _send_command(bus, cmd):
        if hasattr(bus, 'CLE'):
            bus.CLE.value = 1  # Command Latch Enable
        if hasattr(bus, 'ALE'):
            bus.ALE.value = 0  # Address Latch Disable
        bus.IObus.value = cmd
        print(f"Sending command: {cmd}")
        await Timer(10, units='ns')
        if hasattr(bus, 'CLE'):
            bus.CLE.value = 0

    async def _send_address(bus, addr, addr_len):
        if hasattr(bus, 'ALE'):
            bus.ALE.value = 1  # Address Latch Enable
        for byte in addr[:addr_len]:
            bus.IObus.value = byte
            print(f"Sending address byte: {byte}")
            await Timer(10, units='ns')
        if hasattr(bus, 'ALE'):
            bus.ALE.value = 0

    async def _send_data(bus, data):
        for byte in data:
            bus.IObus.value = byte
            print(f"Sending data byte: {byte}")
            await Timer(10, units='ns')

    async def _read_data(bus):
        read_data = []
        for _ in range(8):  # Example loop for 8 bytes; adjust as needed
            await Timer(10, units='ns')
            read_data.append(bus.IObus.value)
            print(f"Read data byte: {bus.IObus.value}")
        return read_data

    async def _get_bytes(length):
        read_data = []
        for _ in range(length):
            await Timer(10, units='ns')
            read_data.append(dut.IObus.value.integer)
        print(f"Received data: {read_data}")
        return read_data

    if txn_template.get('cmd1') is not None:
        await _send_command(bus, txn_template['cmd1'])

    if 'primary_delay' in txn_template:
        for delay_name, delay_time in txn_template['primary_delay'].items():
            numeric_value, unit = parse_delay(delay_time)
            await Timer(numeric_value, units=unit)

    if txn_template.get('addr_len') is not None:
        if addr is None:
            addr = [0x00] * txn_template['addr_len']
        txdata.extend(addr[:txn_template['addr_len']])
        await _send_address(bus, addr, txn_template['addr_len'])

    if data is None and txn_template.get('data') is not None:
        data = txn_template['data']
    if data is not None:
        txdata.extend(data)
        await _send_data(bus, data)

    if txn_template.get('cmd2') is not None:
        await _send_command(bus, txn_template['cmd2'])

    if 'secondary_delay' in txn_template:
        for delay_name, delay_time in txn_template['secondary_delay'].items():
            numeric_value, unit = parse_delay(delay_time)
            await Timer(numeric_value, units=unit)

    if txn_template.get('await_data'):
        rv = await _read_data(bus)
        return rv

    # Only drive IO ports if a byte value is provided.
    if byte is not None:
        for i in range(8):
            signal_name_0 = f"IO{i}_0"
            signal_name_1 = f"IO{i}_1"
            if hasattr(bus, signal_name_0):
                getattr(bus, signal_name_0).value = (byte >> i) & 0x1
            else:
                print(f"Warning: Signal {signal_name_0} not found in Bus. Skipping.")
            if hasattr(bus, signal_name_1):
                getattr(bus, signal_name_1).value = (byte >> (i + 8)) & 0x1
            else:
                print(f"Warning: Signal {signal_name_1} not found in Bus. Skipping.")
        if hasattr(dut, "IO_bus"):
            dut.IO_bus.value = byte
            print(f"Set IO bus value to {byte}")
        else:
            print("Warning: DUT does not contain IO_bus signal. Skipping IO bus update.")

    # Completion Signal Check
    if txn_template.get('await_data'):
        rv = await _get_bytes(len(txdata))
        return rv
    else:
        return None




