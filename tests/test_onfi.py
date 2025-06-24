import sys
import os
import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, Timer
from commands import txn, cmds
from bus import Bus
from memory import sigdict
from driver import NFCOpcodeDriver  



sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src/cocotbext/onfi')))

# Clock generator for the testbench
async def generate_clock(dut):
    """Generate clock pulses."""
    cocotb.start_soon(Clock(dut.iSystemClock, 1, units="ns").start())


@cocotb.test()
async def test_bus_signal_expansion(top):
    bus = Bus(top, name="inst_NFC_Physical_Top", signals=sigdict)
    
    
    assert hasattr(bus, "RE_0_n"), "Signal RE_0_n not found"
    assert hasattr(bus, "RE_1_n"), "Signal RE_1_n not found"

  
    ##assert getattr(bus, "IO0_0") == getattr(bus, "IO0_0") 

    ##found = False
    for sig_name in dir(bus):
        if sig_name.casefold() == "re_0_n".casefold():
            found = True
            break
    assert found, "Signal re_0_n (case-insensitive) not found"  



@cocotb.test()
async def test_send_opcodes(dut):
    
    cocotb.start_soon(generate_clock(dut))

    # Instantiating the Bus class with the DUT 
    bus = Bus(NandFlashController_Top=dut, name="nand_controller")

    # Instantiating the NFCOpcodeDriver with the DUT, Bus object, and clock signal
    opcode_driver = NFCOpcodeDriver(dut, bus, dut.iSystemClock)

   
    opcodes = [
        0b100010,  # Set Column Address
        0b100100,  # Set Row Address
        0b000001,  # Reset (Async)
        0b000010,  # Set Feature (Async)
        0b000101   # Get Feature (Sync)
    ]

    
    for opcode in opcodes:
        
        await opcode_driver.send_opcode(opcode)

       
        await Timer(1000, units='ns')  












   


@cocotb.test()
async def test_reset(dut):
    """Test reset command."""
    await generate_clock(dut)
    await txn('reset',dut)
    await Timer(10, units='ns')

@cocotb.test()
async def test_read_device_id(dut):
    """Test read device ID command."""
    await generate_clock(dut)
    addr = [0x00]  # Example address
    rv = await txn('read_device_id',dut,addr=addr)
    dut._log.info(f"Read Device ID: {rv}")

@cocotb.test()
async def test_block_erase(dut):
    """Test block erase command."""
    await generate_clock(dut)
    addr = [0x00, 0x00, 0x01]  # Example address
    await txn('block_erase',dut,addr=addr)
    await Timer(10, units='ns')

@cocotb.test()
async def test_standard_read(dut):
    """Test standard read command."""
    await generate_clock(dut)
    addr = [0x00, 0x00, 0x00, 0x00, 0x00]  # Example address
    rv = await txn('standard_read',dut, addr=addr)
    dut._log.info(f"Standard Read: {rv}")

@cocotb.test()
async def test_read_cache_sequential(dut):
    """Test the Read Cache Sequential Command."""
    await generate_clock(dut)
    await txn('read_cache_sequential', dut)
    await Timer(10, units='ns')

@cocotb.test()
async def test_read_cache_random(dut):
    """Test the Read Cache Random Command."""
    await generate_clock(dut)
    addr = [0x01, 0x02, 0x03, 0x04, 0x05]  # Example address
    await txn('read_cache_random', dut, addr=addr)
    await Timer(10, units='ns')

@cocotb.test()
async def test_copyback_read(dut):
    """Test the Copyback Read Command."""
    await generate_clock(dut)
    addr = [0x01, 0x02, 0x03, 0x04, 0x05]  # Example address
    await txn('copyback_read', dut, addr=addr)
    await Timer(10, units='ns')

@cocotb.test()
async def test_copyback_program(dut):
    """Test the Copyback Program Command."""
    await generate_clock(dut)
    addr = [0x01, 0x02, 0x03, 0x04, 0x05]  # Example address
    await txn('copyback_program', dut, addr=addr)
    await Timer(10, units='ns')

@cocotb.test()
async def test_copyback_read_with_data_output(dut):
    """Test the Copyback Read with Data Output Command."""
    await generate_clock(dut)
    addr = [0x01, 0x02, 0x03, 0x04, 0x05]  # Example address
    await txn('copyback_read_with_data_output', dut, addr=addr)
    await Timer(10, units='ns')

@cocotb.test()
async def test_copyback_program_with_data_mod(dut):
    """Test the Copyback Program with Data Modification Command."""
    await generate_clock(dut)
    addr = [0x01, 0x02, 0x03, 0x04, 0x05]  # Example address
    await txn('copyback_program_with_data_mod', dut, addr=addr)
    await Timer(10, units='ns')

@cocotb.test()
async def test_zq_calibration_long(dut):
    """Test the ZQ Calibration Long Command."""
    await generate_clock(dut)
    addr = [0x01]  # Example address
    await txn('zq_calibration_long', dut, addr=addr)
    await Timer(10, units='ns')

@cocotb.test()
async def test_zq_calibration_short(dut):
    """Test the ZQ Calibration Short Command."""
    await generate_clock(dut)
    addr = [0x01]  # Example address
    await txn('zq_calibration_short', dut, addr=addr)
    await Timer(10, units='ns')

@cocotb.test()
async def test_get_feature(dut):
    """Test the Get Feature Command."""
    await generate_clock(dut)
    addr = [0x01]  # Example address
    await txn('get_feature', dut, addr=addr)
    await Timer(10, units='ns')

@cocotb.test()
async def test_set_feature(dut):
    """Test the Set Feature Command."""
    await generate_clock(dut)
    addr = [0x01]  # Example address
    data = [0x00, 0x00, 0x00, 0x00]  # Example data
    await txn('set_feature', dut, addr=addr, data=data)
    await Timer(10, units='ns')

@cocotb.test()
async def test_read_page(dut):
    """Test the Read Page Command."""
    await generate_clock(dut)
    addr = [0x01, 0x02, 0x03, 0x04, 0x05]  # Example address
    await txn('read_page', dut, addr=addr)
    await Timer(10, units='ns')

@cocotb.test()
async def test_random_data_input(dut):
    """Test the Random Data Input Command."""
    await generate_clock(dut)
    addr = [0x01, 0x02]  # Example address
    await txn('random_data_input', dut, addr=addr)
    await Timer(10, units='ns')

@cocotb.test()
async def test_random_data_output(dut):
    """Test the Random Data Output Command."""
    await generate_clock(dut)
    addr = [0x01, 0x02]  # Example address
    await txn('random_data_output', dut, addr=addr)
    await Timer(10, units='ns')

@cocotb.test()
async def test_program_page(dut):
    """Test the Program Page Command."""
    await generate_clock(dut)
    addr = [0x01, 0x02, 0x03, 0x04, 0x05]  # Example address
    await txn('program_page', dut, addr=addr)
    await Timer(10, units='ns')

@cocotb.test()
async def test_program_page_cache(dut):
    """Test the Program Page Cache Command."""
    await generate_clock(dut)
    addr = [0x01, 0x02, 0x03, 0x04, 0x05]  # Example address
    await txn('program_page_cache', dut, addr=addr)
    await Timer(10, units='ns')

@cocotb.test()
async def test_read_page_cache_sequential(dut):
    """Test the Read Page Cache Sequential Command."""
    await generate_clock(dut)
    await txn('read_page_cache_sequential', dut)
    await Timer(10, units='ns')

@cocotb.test()
async def test_multi_plane_page_read(dut):
    """Test the Multi Plane Page Read Command."""
    await generate_clock(dut)
    addr = [0x01, 0x02, 0x03, 0x04, 0x05]  # Example address
    await txn('multi_plane_page_read', dut, addr=addr)  # Corrected command name
    await Timer(10, units='ns')

@cocotb.test()
async def test_multi_plane_page_program(dut):
    """Test the Multi Plane Page Program Command."""
    await generate_clock(dut)
    addr = [0x01, 0x02, 0x03, 0x04, 0x05]  # Example address
    await txn('multi_plane_page_program', dut, addr=addr)  # Corrected command name
    await Timer(10, units='ns')

@cocotb.test()
async def test_multi_plane_block_erase(dut):
    """Test the Multi Plane Block Erase Command."""
    await generate_clock(dut)
    addr = [0x01, 0x02, 0x03]  # Example address
    await txn('multi_plane_block_erase', dut, addr=addr)  # Corrected command name
    await Timer(10, units='ns')





