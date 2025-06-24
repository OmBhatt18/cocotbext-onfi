#export PATH := $(PATH):/home/om/intelFPGA/18.1/modelsim_ase/bin/
#SIM ?= modelsim
#TOPLEVEL_LANG ?= verilog


#export PYTHONPATH := /home/om/tests/cocotbext-onfi/src/cocotbext/onfi
#TOPLEVEL?=top



#VERILOG_SOURCES += ../hdl/dummy_dut.v
#VERILOG_SOURCES += ../hdl/nand_controller.v
#VERILOG_SOURCES += ../hdl/top.v




#MODULE = test_onfi

#onfi:
#	$(MAKE) sim MODULE=$(MODULE)

#include $(shell cocotb-config --makefiles)/Makefile.sim
#Working Makefile

export PATH := $(PATH):/home/om/intelFPGA/18.1/modelsim_ase/bin/
SIM ?= modelsim
TOPLEVEL_LANG ?= verilog

TESTS= test_bus_signal_expansion test_send_opcodes test_reset test_read_device_id test_block_erase test_standard_read test_read_cache_sequential test_read_cache_random test_copyback_read test_copyback_program test_copyback_read_with_data_output test_copyback_program_with_data_mod test_zq_calibration_long test_zq_calibration_short test_get_feature test_set_feature test_read_page test_random_data_input test_random_data_output test_program_page test_program_page_cache test_read_page_cache_sequential test_multi_plane_page_read test_multi_plane_page_program test_multi_plane_block_erase
export PYTHONPATH := /home/om/tests/cocotbext-onfi/src/cocotbext/onfi
TOPLEVEL?=NandFlashController_Top
VERILOG_SOURCES += /opt/Xilinx/Vivado/2017.2/ids_lite/ISE/verilog/xeclib/unisims/IDELAYCTRL.v
VERILOG_SOURCES += /opt/Xilinx/Vivado/2017.2/ids_lite/ISE/verilog/xeclib/unisims/IDELAYE2.v
VERILOG_SOURCES += /opt/Xilinx/Vivado/2017.2/ids_lite/ISE/verilog/xeclib/unisims/IBUFG.v
VERILOG_SOURCES += /opt/Xilinx/Vivado/2017.2/ids_lite/ISE/verilog/xeclib/unisims/FIFO36E1.v
VERILOG_SOURCES += /opt/Xilinx/Vivado/2017.2/ids_lite/ISE/verilog/xeclib/unisims/ODDR.v
VERILOG_SOURCES += /opt/Xilinx/Vivado/2017.2/ids_lite/ISE/verilog/xeclib/unisims/IOBUF.v
VERILOG_SOURCES += /opt/Xilinx/Vivado/2017.2/ids_lite/ISE/verilog/xeclib/unisims/OBUF.v
VERILOG_SOURCES += /opt/Xilinx/Vivado/2017.2/ids_lite/ISE/verilog/xeclib/unisims/FD.v
VERILOG_SOURCES += /opt/Xilinx/Vivado/2017.2/ids_lite/ISE/verilog/xeclib/unisims/FD_1.v
VERILOG_SOURCES += /opt/Xilinx/Vivado/2017.2/ids_lite/ISE/verilog/xeclib/unisims/IDDR.v
VERILOG_SOURCES += /opt/Xilinx/Vivado/2017.2/ids_lite/ISE/verilog/xeclib/unisims/IBUF.v

VERILOG_SOURCES += ../hdl/NandFlashcontroller/lib/axis/rtl/arbiter.v
VERILOG_SOURCES += ../hdl/NandFlashcontroller/lib/axis/rtl/axis_adapter.v
VERILOG_SOURCES += ../hdl/NandFlashcontroller/lib/axis/rtl/axis_arb_mux.v
VERILOG_SOURCES += ../hdl/NandFlashcontroller/lib/axis/rtl/axis_async_fifo.v
VERILOG_SOURCES += ../hdl/NandFlashcontroller/lib/axis/rtl/axis_async_fifo_adapter.v
VERILOG_SOURCES += ../hdl/NandFlashcontroller/lib/axis/rtl/axis_broadcast.v
VERILOG_SOURCES += ../hdl/NandFlashcontroller/lib/axis/rtl/axis_cobs_decode.v
VERILOG_SOURCES += ../hdl/NandFlashcontroller/lib/axis/rtl/axis_cobs_encode.v
VERILOG_SOURCES += ../hdl/NandFlashcontroller/lib/axis/rtl/axis_crosspoint.v
VERILOG_SOURCES += ../hdl/NandFlashcontroller/lib/axis/rtl/axis_demux.v
VERILOG_SOURCES += ../hdl/NandFlashcontroller/lib/axis/rtl/axis_fifo.v
VERILOG_SOURCES += ../hdl/NandFlashcontroller/lib/axis/rtl/axis_fifo_adapter.v
VERILOG_SOURCES += ../hdl/NandFlashcontroller/lib/axis/rtl/axis_frame_join.v
VERILOG_SOURCES += ../hdl/NandFlashcontroller/lib/axis/rtl/axis_frame_length_adjust.v
VERILOG_SOURCES += ../hdl/NandFlashcontroller/lib/axis/rtl/axis_frame_length_adjust_fifo.v
VERILOG_SOURCES += ../hdl/NandFlashcontroller/lib/axis/rtl/axis_frame_len.v
VERILOG_SOURCES += ../hdl/NandFlashcontroller/lib/axis/rtl/axis_ll_bridge.v
VERILOG_SOURCES += ../hdl/NandFlashcontroller/lib/axis/rtl/axis_mux.v
VERILOG_SOURCES += ../hdl/NandFlashcontroller/lib/axis/rtl/axis_pipeline_register.v
VERILOG_SOURCES += ../hdl/NandFlashcontroller/lib/axis/rtl/axis_ram_switch.v
VERILOG_SOURCES += ../hdl/NandFlashcontroller/lib/axis/rtl/axis_rate_limit.v
VERILOG_SOURCES += ../hdl/NandFlashcontroller/lib/axis/rtl/axis_register.v
VERILOG_SOURCES += ../hdl/NandFlashcontroller/lib/axis/rtl/axis_srl_fifo.v
VERILOG_SOURCES += ../hdl/NandFlashcontroller/lib/axis/rtl/axis_srl_register.v
VERILOG_SOURCES += ../hdl/NandFlashcontroller/lib/axis/rtl/axis_stat_counter.v
VERILOG_SOURCES += ../hdl/NandFlashcontroller/lib/axis/rtl/axis_switch.v
VERILOG_SOURCES += ../hdl/NandFlashcontroller/lib/axis/rtl/axis_tap.v
VERILOG_SOURCES += ../hdl/NandFlashcontroller/lib/axis/rtl/ll_axis_bridge.v
VERILOG_SOURCES += ../hdl/NandFlashcontroller/lib/axis/rtl/priority_encoder.v
VERILOG_SOURCES += ../hdl/NandFlashcontroller/lib/axis/rtl/sync_reset.v


VERILOG_SOURCES += ../hdl/NandFlashcontroller/lib/verilog-axi/rtl/arbiter.v
VERILOG_SOURCES += ../hdl/NandFlashcontroller/lib/verilog-axi/rtl/axi_adapter_rd.v
VERILOG_SOURCES += ../hdl/NandFlashcontroller/lib/verilog-axi/rtl/axi_adapter.v
VERILOG_SOURCES += ../hdl/NandFlashcontroller/lib/verilog-axi/rtl/axi_adapter_wr.v
VERILOG_SOURCES += ../hdl/NandFlashcontroller/lib/verilog-axi/rtl/axi_axil_adapter_rd.v
VERILOG_SOURCES += ../hdl/NandFlashcontroller/lib/verilog-axi/rtl/axi_axil_adapter.v
VERILOG_SOURCES += ../hdl/NandFlashcontroller/lib/verilog-axi/rtl/axi_axil_adapter_wr.v
VERILOG_SOURCES += ../hdl/NandFlashcontroller/lib/verilog-axi/rtl/axi_cdma_desc_mux.v
VERILOG_SOURCES += ../hdl/NandFlashcontroller/lib/verilog-axi/rtl/axi_cdma.v
VERILOG_SOURCES += ../hdl/NandFlashcontroller/lib/verilog-axi/rtl/axi_crossbar_addr.v
VERILOG_SOURCES += ../hdl/NandFlashcontroller/lib/verilog-axi/rtl/axi_crossbar_rd.v
VERILOG_SOURCES += ../hdl/NandFlashcontroller/lib/verilog-axi/rtl/axi_crossbar.v
VERILOG_SOURCES += ../hdl/NandFlashcontroller/lib/verilog-axi/rtl/axi_crossbar_wr.v
VERILOG_SOURCES += ../hdl/NandFlashcontroller/lib/verilog-axi/rtl/axi_dma_desc_mux.v
VERILOG_SOURCES += ../hdl/NandFlashcontroller/lib/verilog-axi/rtl/axi_dma_rd.v
VERILOG_SOURCES += ../hdl/NandFlashcontroller/lib/verilog-axi/rtl/axi_dma.v
VERILOG_SOURCES += ../hdl/NandFlashcontroller/lib/verilog-axi/rtl/axi_dma_wr.v
VERILOG_SOURCES += ../hdl/NandFlashcontroller/lib/verilog-axi/rtl/axi_dp_ram.v
VERILOG_SOURCES += ../hdl/NandFlashcontroller/lib/verilog-axi/rtl/axi_fifo_rd.v
VERILOG_SOURCES += ../hdl/NandFlashcontroller/lib/verilog-axi/rtl/axi_fifo.v
VERILOG_SOURCES += ../hdl/NandFlashcontroller/lib/verilog-axi/rtl/axi_fifo_wr.v
VERILOG_SOURCES += ../hdl/NandFlashcontroller/lib/verilog-axi/rtl/axi_interconnect.v
VERILOG_SOURCES += ../hdl/NandFlashcontroller/lib/verilog-axi/rtl/axi_ram_rd_if.v
VERILOG_SOURCES += ../hdl/NandFlashcontroller/lib/verilog-axi/rtl/axi_ram.v
VERILOG_SOURCES += ../hdl/NandFlashcontroller/lib/verilog-axi/rtl/axi_ram_wr_if.v
VERILOG_SOURCES += ../hdl/NandFlashcontroller/lib/verilog-axi/rtl/axi_ram_wr_rd_if.v
VERILOG_SOURCES += ../hdl/NandFlashcontroller/lib/verilog-axi/rtl/axi_register_rd.v
VERILOG_SOURCES += ../hdl/NandFlashcontroller/lib/verilog-axi/rtl/axi_register.v
VERILOG_SOURCES += ../hdl/NandFlashcontroller/lib/verilog-axi/rtl/axi_register_wr.v
VERILOG_SOURCES += ../hdl/NandFlashcontroller/lib/verilog-axi/rtl/axil_adapter_rd.v
VERILOG_SOURCES += ../hdl/NandFlashcontroller/lib/verilog-axi/rtl/axil_adapter.v
VERILOG_SOURCES += ../hdl/NandFlashcontroller/lib/verilog-axi/rtl/axil_adapter_wr.v
VERILOG_SOURCES += ../hdl/NandFlashcontroller/lib/verilog-axi/rtl/axil_cdc_rd.v
VERILOG_SOURCES += ../hdl/NandFlashcontroller/lib/verilog-axi/rtl/axil_cdc.v
VERILOG_SOURCES += ../hdl/NandFlashcontroller/lib/verilog-axi/rtl/axil_cdc_wr.v
VERILOG_SOURCES += ../hdl/NandFlashcontroller/lib/verilog-axi/rtl/axil_dp_ram.v
VERILOG_SOURCES += ../hdl/NandFlashcontroller/lib/verilog-axi/rtl/axil_interconnect.v
VERILOG_SOURCES += ../hdl/NandFlashcontroller/lib/verilog-axi/rtl/axil_ram.v
VERILOG_SOURCES += ../hdl/NandFlashcontroller/lib/verilog-axi/rtl/axil_register_rd.v
VERILOG_SOURCES += ../hdl/NandFlashcontroller/lib/verilog-axi/rtl/axil_register.v
VERILOG_SOURCES += ../hdl/NandFlashcontroller/lib/verilog-axi/rtl/axil_register_wr.v
VERILOG_SOURCES += ../hdl/NandFlashcontroller/lib/verilog-axi/rtl/priority_encoder.v







VERILOG_SOURCES += ../hdl/NandFlashcontroller/rtl/NFC_Atom_Command_Async.v   # Base module
VERILOG_SOURCES += ../hdl/NandFlashcontroller/rtl/NFC_Atom_Command_Sync.v    # Base module

VERILOG_SOURCES += ../hdl/NandFlashcontroller/rtl/NFC_Atom_Datainput_Async.v
VERILOG_SOURCES += ../hdl/NandFlashcontroller/rtl/NFC_Atom_Datainput_Sync.v
VERILOG_SOURCES += ../hdl/NandFlashcontroller/rtl/NFC_Atom_Dataoutput_Async.v
VERILOG_SOURCES += ../hdl/NandFlashcontroller/rtl/NFC_Atom_Dataoutput_Sync.v

VERILOG_SOURCES += ../hdl/NandFlashcontroller/rtl/NFC_Command_Reset.v
VERILOG_SOURCES += ../hdl/NandFlashcontroller/rtl/NFC_Command_SetFeature.v
VERILOG_SOURCES += ../hdl/NandFlashcontroller/rtl/NFC_Command_GetFeature.v
VERILOG_SOURCES += ../hdl/NandFlashcontroller/rtl/NFC_Command_EraseBlock.v
VERILOG_SOURCES += ../hdl/NandFlashcontroller/rtl/NFC_Command_ProgramPage.v
VERILOG_SOURCES += ../hdl/NandFlashcontroller/rtl/NFC_Command_ReadPage.v
VERILOG_SOURCES += ../hdl/NandFlashcontroller/rtl/NFC_Command_ReadStatus.v
VERILOG_SOURCES += ../hdl/NandFlashcontroller/rtl/NFC_Command_Issue_Top.v
VERILOG_SOURCES += ../hdl/NandFlashcontroller/rtl/NFC_Command_Issue_to_Atom_Command_Generator_Mux.v
VERILOG_SOURCES += ../hdl/NandFlashcontroller/rtl/NFC_Command_Idle.v

VERILOG_SOURCES += ../hdl/NandFlashcontroller/rtl/NFC_Atom_Command_Generator_Top.v
VERILOG_SOURCES += ../hdl/NandFlashcontroller/rtl/NFC_Atom_Command_Generator_to_Physical_Mux.v

VERILOG_SOURCES += ../hdl/NandFlashcontroller/rtl/NFC_Physical_Input.v
VERILOG_SOURCES += ../hdl/NandFlashcontroller/rtl/NFC_Physical_Output.v
VERILOG_SOURCES += ../hdl/NandFlashcontroller/rtl/NFC_Physical_Top.v
VERILOG_SOURCES += ../hdl/NandFlashcontroller/rtl/NFC_Pinpad.v

VERILOG_SOURCES += ../hdl/NandFlashcontroller/rtl/NandFlashController_Top.v
VERILOG_SOURCES += ../hdl/NandFlashcontroller/rtl/NandFlashController_Top_AXI.v

VERILOG_SOURCES += ../hdl/NandFlashcontroller/rtl/NandFlashController_AXIL_Reg.v
VERILOG_SOURCES += ../hdl/NandFlashcontroller/rtl/NandFlashController_Interface_adapter.v

VERILOG_SOURCES += ../hdl/NandFlashcontroller/rtl/NFC_Atom_Idle.v

VERILOG_SOURCES += ../hdl/NandFlashcontroller/tb/tb_NandFlashController_Top_AXI.v
VERILOG_SOURCES += ../hdl/NandFlashcontroller/tb/tb_NandFlashController_Top.v
##VERILOG_SOURCES += ../hdl/NandFlashcontroller/tb/tb_NandFlashController_Top_wave.do
VERILOG_SOURCES += ../hdl/NandFlashcontroller/tb/tb_NFC_Atom_Command_Generator_Top.v
VERILOG_SOURCES += ../hdl/NandFlashcontroller/tb/tb_NFC_Command_Issue_Top.v
VERILOG_SOURCES += ../hdl/NandFlashcontroller/tb/tb_NFC_Physical_Top.v

VSIM_ARGS += +memlimit=4096M





MODULE = test_onfi

onfi: $(TESTS)

$(TESTS):
	$(MAKE) sim MODULE=$(MODULE) TESTCASE=$@
include $(shell cocotb-config --makefiles)/Makefile.sim
