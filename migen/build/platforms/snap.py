import os
from migen.build.generic_platform import *
from migen.build.xilinx import XilinxPlatform, VivadoProgrammer

_io = [
    ("sys_clk", 0,
        Subsignal("p", Pins("E10")),
        Subsignal("n", Pins("D10")),
        IOStandard("LVDS_25")
    ),

    ("eth_clk", 0,
        Subsignal("125_p", Pins("H6")),
        Subsignal("125_n", Pins("H5")),
        Subsignal("p", Pins("K6")),
        Subsignal("n", Pins("K5"))
    ),

    ("spi", 0,
        Subsignal("miso", Pins("K20"), IOStandard("LVCMOS33")),
        Subsignal("mosi", Pins("J20"), IOStandard("LVCMOS33")),
        Subsignal("sclk", Pins("E17"), IOStandard("LVCMOS33")),
        Subsignal("cs_n", Pins("G19"), IOStandard("LVCMOS33")),
        Subsignal("flash_data", Pins("B24 A25 B22 A22"), IOStandard("LVCMOS25")),
        Subsignal("flash_csn", Pins("C23"), IOStandard("LVCMOS25"))
    ),

    ("gpio", 0, Pins("B21"), IOStandard("LVCMOS25")),
    ("gpio", 1, Pins("C21"), IOStandard("LVCMOS25")),
    ("gpio", 2, Pins("B20"), IOStandard("LVCMOS25")),
    ("gpio", 3, Pins("A20"), IOStandard("LVCMOS25")),
    ("gpio", 4, Pins("H24"), IOStandard("LVCMOS25")),
    ("gpio", 5, Pins("H23"), IOStandard("LVCMOS25")),
    ("gpio", 6, Pins("B26"), IOStandard("LVCMOS25")),
    ("gpio", 7, Pins("R25"), IOStandard("LVCMOS25")),
    ("gpio", 8, Pins("L17"), IOStandard("LVCMOS25")),
    ("gpio", 9, Pins("K18"), IOStandard("LVCMOS25")),
    ("usb", 0,
        Subsignal("tx", Pins("J8"), IOStandard("LVCMOS25")),
        Subsignal("cts", Pins("F10"), IOStandard("LVCMOS25")),
        Subsignal("rts", Pins("J13"), IOStandard("LVCMOS25")),
        Subsignal("rx", Pins("H13"), IOStandard("LVCMOS25"))
    ),

    ("mgt_tx", 0,
        Subsignal("p", Pins("P2 K2")),
        Subsignal("n", Pins("P1 K1"))
    ),
    ("mgt_rx", 0,
        Subsignal("p", Pins("R4 L4")),
        Subsignal("n", Pins("R3 L3"))
    ),

    ("led", 0, Pins("C13 C14 D13 D14 E12 E13"), IOStandard("LVCMOS25")),

    ("sync_in", 0,
        Subsignal("p", Pins("AD25"), IOStandard("LVDS_25")),
        Subsignal("n", Pins("AE25"), IOStandard("LVDS_25"))
    ),
    ("sync_out", 0, Pins("H9"), IOStandard("LVCMOS25")),

    ("sfp_disable", 0, Pins("U21 N16"), IOStandard(LVCMOS25)),

    ("zdok0", 0, Pins("AA23 AB24",
        "Y25 Y26 U24 U25 U19 U20 T24 T25 M21 M22 M24 L24 L22 K22 J24 J25",
        "G25 G26 Y22 AA22 Y23 AA24 V23 V24 R22 R23 R21 P21 P23 N23 K25 K26",
        "K23 J23 H21 G21 G22 F23 AE23 AF23 AC23 AC24 W23 W24 T22 T23 R18",
        "P18 N18 M19 N19 M20 J21 H22 G24 F24 D23 D24 AE22 AF22 AB26 AC26",
        "V21 W21 U17 T17 R16 R17 P19 P20 P16 N17 J26 H26 E25 D25 F22 E23"),
        IOStandard("LVCMOS25")),

    ("zdok0_p", 0, Pins(
        "AA23 Y25 U24 U19 T24 M21 M24 L22 J24 G25 Y22 Y23",
        "V23 R22 R21 P23 K25 K23 H21 G22 AE23 AC23 W23 T22 R18 N18",
        "N19 J21 G24 D23 AE22 AB26 V21 U17 R16 P19 P16 J26 E25 F22"), 
        IOStandard("LVDS_25")
    ),

    ("zdok0_n", 0, Pins(
        "AB24 Y26 U25 U20 T25 M22 L24 K22 J25 G26 AA22 AA24 V24",
        "R23 P21 N23 K26 J23 G21 F23 AF23 AC24 W24 T23 P18 M19 M20", 
        "H22 F24 D24 AF22 AC26 W21 T17 R17 P20 N17 H26 D25 E23"), 
        IOStandard("LVDS_25")
    ),

    ("adc", 0,
        Subsignal("csn", Pins("AF3 AF10 V14"), IOStandard("LVCMOS18")),
        Subsignal("rst_n", Pins("AE5 AF13 V19"), IOStandard("LVCMOS18")),
        Subsignal("pd", Pins("AE3 AE8 W15"), IOStandard("LVCMOS18")),
        Subsignal("sdata", Pins("AF2 AF9 W14"), IOStandard("LVCMOS18")),
        Subsignal("slk", Pins("M17 L18 K16"), IOStandard("LVCMOS33")),
        Subsignal("lclkp", Pins("AA3"), IOStandard("LVDS")),
        Subsignal("lclkn", Pins("AA2"), IOStandard("LVDS")),
        Subsignal("0_out", Pins(
            "V2 V1 U2 U1 W6 W5 U7 V6",
            "V3 W3 Y3 Y2 AD6 AD5 AD4 AD3"), 
            IOStandard("LVDS")),
        Subsignal("1_out", Pins(
            "V8 V7 W10 W9 Y8 Y7 Y11 Y10 AB12",
            "AC12 AA13 AA12 AA8 AA7 AC8 AD8"), 
            IOStandard("LVDS")),
        Subsignal("2_out", Pins(
            "AF14 AF15 AD15 AE15 AE18 AF18 AF19 AF20", 
            "AA14 AA15 AC14 AD14 AB19 AB20 AA19 AA20"),
            IOStandard("LVDS"))
    ),

    ("clk_sel", 0,
        Subsignal("a", Pins("A18")),
        Subsignal("b", Pins("A19")),
        IOStandard("LVCMOS33")
    ),

    ("lmx2581", 0,
        Subsignal("clk", Pins("H16")),
        Subsignal("data", Pins("J15")),
        Subsignal("muxout", Pins("J19")),
        Subsignal("le", Pins("J16")),
        Subsignal("ce", Pins("G15")),
        Subsignal("be", Pins("F15")),
        IOStandard("LVCMOS33")
    ),

    ("xadc", 0,
        Subsignal("p", Pins("N12")),
        Subsignal("n", Pins("P11"))
    ),
]

class Platform(XilinxPlatform):
    default_clk_name = "clk100"
    default_clk_period = 10
    usermemaddr = 0x800000  >> 8 

    def __init__(self):
        XilinxPlatform.__init__(self, "xc7k160tffg676-2", _io, toolchain="vivado")
        if toolchain == "vivado":
            self.toolchain.bitstream_commands = ['set_property BITSTREAM.CONFIG.CONFIGRATE 33 [current_design]',
                                            'set_property BITSTREAM.CONFIG.SPI_BUSWIDTH 4 [current_design]',
                                            'set_property BITSTREAM.CONFIG.SPI_32BIT_ADDR Yes [current_design]',
                                            'set_property BITSTREAM.CONFIG.TIMER_CFG 2000000 [current_design]'] # about 10 seconds
            self.toolchain.additional_commands += ['write_cfgmem  -format mcs -size 32 -interface SPIx4 -loadbit "up 0x0 ./myproj.runs/impl_1/top.bit " -checksum -file "./myproj.runs/impl_1/top.mcs" -force']
            self.toolchain.additional_commands += ['write_cfgmem  -format mcs -size 32 -interface SPIx4 -loadbit "up 0x%.7x ./myproj.runs/impl_1/top.bit " -checksum -file "./myproj.runs/impl_1/top_0x%x.mcs" -force' % (usermemaddr, usermemaddr)]
            self.toolchain.additional_commands += ['write_cfgmem  -format bin -size 32 -interface SPIx4 -loadbit "up 0x0 ./myproj.runs/impl_1/top.bit " -checksum -file "./myproj.runs/impl_1/top.bin" -force']
        
        snap_infra_path = os.environ['MLIB_DEVEL_PATH'] + '/jasper_library/hdl_sources/infrastructure/snap_infrastructure.v'
        XilinxPlatform.add_source(self, snap_infra_path, language="verilog")

    def create_programmer(self):
        return VivadoProgrammer()

    def do_finalize(self, fragment):
        XilinxPlatform.do_finalize(self, fragment)
        try:
            self.add_period_constraint(self.lookup_request("sys_clk").p, 5.0)
        except ConstraintError:
            pass
        self.add_platform_command('set_property CONFIG_VOLTAGE 2.5 [current_design]')
        self.add_platform_command('set_property CFGBVS VCCO [current_design]')