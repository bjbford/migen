from migen.build.generic_platform import *
from migen.build.xilinx import XilinxPlatform, VivadoProgrammer

# All IO pins/ports on zcu111 device.
# Above each section is listed the format for how to Ctrl-F to that 
# specfic pin set in the ZCU111.xdc file. Swappable parts are surrounded
# by ().
_io = [
	# GPIO_LED_(#)_LS
	("user_led", 0, Pins("AR13"), IOStandard("LVCMOS18")),
    ("user_led", 1, Pins("AP13"), IOStandard("LVCMOS18")),
    ("user_led", 2, Pins("AR16"), IOStandard("LVCMOS18")),
    ("user_led", 3, Pins("AP16"), IOStandard("LVCMOS18")),
    ("user_led", 4, Pins("AP15"), IOStandard("LVCMOS18")),
    ("user_led", 5, Pins("AN16"), IOStandard("LVCMOS18")),
    ("user_led", 6, Pins("AN17"), IOStandard("LVCMOS18")),
    ("user_led", 7, Pins("AV15"), IOStandard("LVCMOS18")),

    # CPU_RESET
    ("cpu_reset", 0, Pins("AF15"), IOStandard("LVCMOS18")),

    # GPIO_SW_(direction)
    ("user_sw_c", 0, Pins("AW5"), IOStandard("LVCMOS18")),
    ("user_sw_n", 0, Pins("AW3"), IOStandard("LVCMOS18")),
    ("user_sw_s", 0, Pins("E8"), IOStandard("LVCMOS18")),
    ("user_sw_w", 0, Pins("AW6"), IOStandard("LVCMOS18")),
    ("user_sw_e", 0, Pins("AWE"), IOStandard("LVCMOS18")),

    # GPIO_DIP_SW(#)
    ("user_dip_sw", 0, Pins("AF16"), IOStandard("LVCMOS12")),
    ("user_dip_sw", 1, Pins("AF17"), IOStandard("LVCMOS12")),
    ("user_dip_sw", 2, Pins("AH15"), IOStandard("LVCMOS12")),
    ("user_dip_sw", 3, Pins("AH16"), IOStandard("LVCMOS12")),
    ("user_dip_sw", 4, Pins("AN17"), IOStandard("LVCMOS12")),
    ("user_dip_sw", 5, Pins("AG17"), IOStandard("LVCMOS12")),
    ("user_dip_sw", 6, Pins("AJ15"), IOStandard("LVCMOS12")),
    ("user_dip_sw", 7, Pins("AJ16"), IOStandard("LVCMOS12")),

    # USER_SMA_MGT_CLOCK_C_(N/P)
    ("user_sma_clock", 0,
        Subsignal("p", Pins("T32"), IOStandard("LVDS")), # Swap LVDS w/ MGTREFCLK ?
        Subsignal("n", Pins("T31"), IOStandard("LVDS"))
    ),

    #("user_sma_gpio", 0,
    #    Subsignal("p", Pins("H27"), IOStandard("LVDS")),
    #    Subsignal("n", Pins("G27"), IOStandard("LVDS"))
    #),
    #("user_sma_gpio_p", 0, Pins("H27"), IOStandard("LVCMOS18")),
    #("user_sma_gpio_n", 0, Pins("G27"), IOStandard("LVCMOS18")),

    # CLK_100_(N/P)
    ("clk100", 0,
        Subsignal("p", Pins("AM15"), IOStandard("LVDS")),
        Subsignal("n", Pins("AN15"), IOStandard("LVDS"))
    ),

    # CLK_125_(N/P)
    ("clk125", 0,
        Subsignal("p", Pins("AL17"), IOStandard("LVDS")),
        Subsignal("n", Pins("AM17"), IOStandard("LVDS"))
    ),

    #("clk300", 0,
    #    Subsignal("p", Pins("AK17"), IOStandard("DIFF_SSTL12")),
    #    Subsignal("n", Pins("AK16"), IOStandard("DIFF_SSTL12"))
    #),

    # PL_I2C0_(SCL/SDC)_LS
    ("i2c", 0,
        Subsignal("scl", Pins("AT16")),
        Subsignal("sda", Pins("AW16")),
        IOStandard("LVCMOS18")
    ),

    # PL_I2C1_(SCL/SDA)_LS
    ("i2c", 1,
        Subsignal("scl", Pins("AV16")),
        Subsignal("sda", Pins("AV13")),
        IOStandard("LVCMOS18")
    ),

    # UART2_(CTS/RTS)_B
    # UART2_(RXD/TXD)_FPGA_(RXD/TXD)
    # DOUBLE CHECK RX/TX DIRECTION
    ("serial", 0,
        Subsignal("cts", Pins("AT14")),
        Subsignal("rts", Pins("AU14")),
        Subsignal("tx", Pins("AU15")),
        Subsignal("rx", Pins("AT15")),
        IOStandard("LVCMOS18")
	),


    #("spiflash", 0,  # clock needs to be accessed through primitive
    #    Subsignal("cs_n", Pins("AA26")),
    #    Subsignal("dq", Pins("AC7 AB7 AA7 Y7")),
    #    IOStandard("LVCMOS18")
    #),

    #("spiflash", 1,  # clock needs to be accessed through primitive
    #    Subsignal("cs_n", Pins("T26")),
    #    Subsignal("dq", Pins("M20 L20 R21 R22")),
    #    IOStandard("LVCMOS18")
    #),

    #("hdmi", 0,
    #    Subsignal("d", Pins(
    #        "AK11 AP11 AP13 AN13 AN11 AM11 AN12 AM12",
    #        "AL12 AK12 AL13 AK13 AD11 AH12 AG12 AJ11",
    #        "AG10 AK8")),
    #    Subsignal("de", Pins("AE11")),
    #    Subsignal("clk", Pins("AF13")),
    #    Subsignal("vsync", Pins("AH13")),
    #    Subsignal("hsync", Pins("AE13")),
    #    Subsignal("spdif", Pins("AE12")),
    #    Subsignal("spdif_out", Pins("AF12")),
    #    IOStandard("LVCMOS18")
    #),


    #("ddram", 0,
    #    Subsignal("a", Pins(
    #        "AE17 AH17 AE18 AJ15 AG16 AL17 AK18 AG17",
    #        "AF18 AH19 AF15 AD19 AJ14 AG19"),
    #        IOStandard("SSTL12_DCI")),
    #    Subsignal("ba", Pins("AF17 AL15"), IOStandard("SSTL12_DCI")),
    #    Subsignal("bg", Pins("AG15"), IOStandard("SSTL12_DCI")),
    #    Subsignal("ras_n", Pins("AF14"), IOStandard("SSTL12_DCI")), # A16
    #    Subsignal("cas_n", Pins("AG14 "), IOStandard("SSTL12_DCI")), # A15
    #    Subsignal("we_n", Pins("AD16"), IOStandard("SSTL12_DCI")), # A14
    #    Subsignal("cs_n", Pins("AL19"), IOStandard("SSTL12_DCI")),
    #    Subsignal("act_n", Pins("AH14"), IOStandard("SSTL12_DCI")),
    #    Subsignal("ten", Pins("AH16"), IOStandard("SSTL12_DCI")),
    #    Subsignal("alert_n", Pins("AJ16"), IOStandard("SSTL12_DCI")),
    #    Subsignal("par", Pins("AD18"), IOStandard("SSTL12_DCI")),
    #    Subsignal("dm", Pins("AD21 AE25 AJ21 AM21 AH26 AN26 AJ29 AL32"),
    #        IOStandard("POD12_DCI")),
    #    Subsignal("dq", Pins(
    #        "AE23 AG20 AF22 AF20 AE22 AD20 AG22 AE20",
    #        "AJ24 AG24 AJ23 AF23 AH23 AF24 AH22 AG25",
    #
    #        "AL22 AL25 AM20 AK23 AK22 AL20 AL24 AL23",
    #        "AM24 AN23 AN24 AP23 AP25 AN22 AP24 AM22",
    #
    #        "AH28 AK26 AK28 AM27 AJ28 AH27 AK27 AM26",
    #        "AL30 AP29 AM30 AN28 AL29 AP28 AM29 AN27",
    #
    #        "AH31 AH32 AJ34 AK31 AJ31 AJ30 AH34 AK32",
    #        "AN33 AP33 AM34 AP31 AM32 AN31 AL34 AN32",
    #       ),
    #        IOStandard("POD12_DCI")),
    #    Subsignal("dqs_p", Pins("AG21 AH24 AJ20 AP20 AL27 AN29 AH33 AN34"),
    #        IOStandard("DIFF_POD12")),
    #    Subsignal("dqs_n", Pins("AH21 AJ25 AK20 AP21 AL28 AP30 AJ33 AP34"),
    #        IOStandard("DIFF_POD12")),
    #    Subsignal("clk_p", Pins("AE16"), IOStandard("DIFF_SSTL2_DCI")),
    #    Subsignal("clk_n", Pins("AE15"), IOStandard("DIFF_SSTL2_DCI")),
    #    Subsignal("cke", Pins("AD15"), IOStandard("SSTL12_DCI")),
    #    Subsignal("odt", Pins("AJ18"), IOStandard("SSTL12_DCI")),
    #    Subsignal("reset_n", Pins("AL18"), IOStandard("LVCMOS12")),
    #    Misc("SLEW=FAST"),
    #),

    #("pcie_x1", 0,
    #    Subsignal("rst_n", Pins("K22"), IOStandard("LVCMOS18")),
    #    Subsignal("clk_p", Pins("AB6")),
    #    Subsignal("clk_n", Pins("AB5")),
    #    Subsignal("rx_p", Pins("AB2")),
    #    Subsignal("rx_n", Pins("AB1")),
    #    Subsignal("tx_p", Pins("AC3")),
    #    Subsignal("tx_n", Pins("AC4"))
    #),

    #("pcie_x2", 0,
    #    Subsignal("rst_n", Pins("K22"), IOStandard("LVCMOS18")),
    #    Subsignal("clk_p", Pins("AB6")),
    #    Subsignal("clk_n", Pins("AB5")),
    #    Subsignal("rx_p", Pins("AB2 AD2")),
    #    Subsignal("rx_n", Pins("AB1 AD1")),
    #    Subsignal("tx_p", Pins("AC3 AE4")),
    #    Subsignal("tx_n", Pins("AC4 AE3"))
    #),

    #"pcie_x4", 0,
    #    Subsignal("rst_n", Pins("K22"), IOStandard("LVCMOS18")),
    #    Subsignal("clk_p", Pins("AB6")),
    #    Subsignal("clk_n", Pins("AB5")),
    #    Subsignal("rx_p", Pins("AB2 AD2 AF2 AH2")),
    #    Subsignal("rx_n", Pins("AB1 AD1 AF1 AH1")),
    #    Subsignal("tx_p", Pins("AC3 AE4 AG4 AH6")),
    #    Subsignal("tx_n", Pins("AC4 AE3 AG3 AH5"))
    #),

    #"pcie_x8", 0,
    #    Subsignal("rst_n", Pins("K22"), IOStandard("LVCMOS18")),
    #    Subsignal("clk_p", Pins("AB6")),
    #    Subsignal("clk_n", Pins("AB5")),
    #    Subsignal("rx_p", Pins("AB2 AD2 AF2 AH2 AJ4 AK2 AM2 AP2")),
    #    Subsignal("rx_n", Pins("AB1 AD1 AF1 AH1 AJ3 AK1 AM1 AP1")),
    #    Subsignal("tx_p", Pins("AC3 AE4 AG4 AH6 AK6 AL4 AM6 AN4")),
    #    Subsignal("tx_n", Pins("AC4 AE3 AG3 AH5 AK5 AL3 AM5 AN3"))
    #),

    #("sgmii_clock", 0,
    #    Subsignal("p", Pins("P26"), IOStandard("LVDS_25")),
    #    Subsignal("n", Pins("N26"), IOStandard("LVDS_25"))
    #),

    #("user_sma_mgt_refclk", 0,
    #    Subsignal("p", Pins("V6")),
    #    Subsignal("n", Pins("V5"))
    #),
    #("user_sma_mgt_tx", 0,
    #    Subsignal("p", Pins("R4")),
    #    Subsignal("n", Pins("R3"))
    #),
    #("user_sma_mgt_rx", 0,
    #    Subsignal("p", Pins("P2")),
    #    Subsignal("n", Pins("P1"))
    #),

    # SFP0_RX_(N/P)
    ("sfp_rx", 0,
        Subsignal("p", Pins("AA38")),
        Subsignal("n", Pins("AA39"))
    ),
    ("sfp_rx", 1,
        Subsignal("p", Pins("W38")),
        Subsignal("n", Pins("W39"))
    ),
    ("sfp_rx", 2,
        Subsignal("p", Pins("U38")),
        Subsignal("n", Pins("U39"))
    ),
    ("sfp_rx", 3,
        Subsignal("p", Pins("R38")),
        Subsignal("n", Pins("R39"))
    ),

    # SFP0_TX_(N/P)
    ("sfp_tx", 0,
        Subsignal("p", Pins("Y35")),
        Subsignal("n", Pins("Y36"))
    ),
    ("sfp_tx", 1,
        Subsignal("p", Pins("V35")),
        Subsignal("n", Pins("V36"))
    ),
    ("sfp_tx", 2,
        Subsignal("p", Pins("T35")),
        Subsignal("n", Pins("T36"))
    ),
    ("sfp_tx", 3,
        Subsignal("p", Pins("R33")),
        Subsignal("n", Pins("R34"))
    ),

    # SFP0_TX_DISABLE_B
    ("sfp_tx_disable_n", 0, Pins("G12"), IOStandard("LVCMOS18")),
    ("sfp_tx_disable_n", 1, Pins("G10"), IOStandard("LVCMOS18")),
    ("sfp_tx_disable_n", 2, Pins("K12"), IOStandard("LVCMOS18")),
    ("sfp_tx_disable_n", 3, Pins("J7"), IOStandard("LVCMOS18")),
    
    # SFP_REC_CLOCK_C_(N/P)
    ("sfp_rec_clock_c", 0,
    	Subsignal("p", Pins("AW14")),
    	Subsignal("n", Pins("AW13")),
    	IOStandard("LVDS")
	),

	# SFP_SI5382_IN1_C_(N/P)
    ("sfp_si5382_in1_c", 0,
    	Subsignal("p", Pins("AA33")),
    	Subsignal("n", Pins("AA34"))
	),

	# SFP_SI5382_OUT_C_(N/P)
    ("sfp_si5382_out_c", 0,
    	Subsignal("p", Pins("Y31")),
    	Subsignal("n", Pins("Y32"))
	),

	# SFP_SI5382_CLK_IN_SEL
    ("sfp_si5382_in1_c", 0, Pins("E39"), IOStandard("LVCMOS18")),

]

_connectors = [
    ("FMCP_HSPC", {

    	# FMCP_HSPC_DP(#)_
        "DP0_C2M_P": "P35",
        "DP0_C2M_N": "P36",
        "DP0_M2C_P": "N38",
        "DP0_M2C_N": "N39",
        "DP1_C2M_P": "N33",
        "DP1_C2M_N": "N34",
        "DP1_M2C_P": "M36",
        "DP1_M2C_N": "M37",
        "DP2_C2M_P": "L33",
        "DP2_C2M_N": "L34",
        "DP2_M2C_P": "L38",
        "DP2_M2C_N": "L39",
        "DP3_C2M_P": "B6",
        "DP3_C2M_N": "B5",
        "DP3_M2C_P": "A4",
        "DP3_M2C_N": "A3",
        "DP4_C2M_P": "N4",
        "DP4_C2M_N": "N3",
        "DP4_M2C_P": "M2",
        "DP4_M2C_N": "M1",
        "DP5_C2M_P": "J4",
        "DP5_C2M_N": "J3",
        "DP5_M2C_P": "H2",
        "DP5_M2C_N": "H1",
        "DP6_C2M_P": "L4",
        "DP6_C2M_N": "L3",
        "DP6_M2C_P": "K2",
        "DP6_M2C_N": "K1",
        "DP7_C2M_P": "G4",
        "DP7_C2M_N": "G3",
        "DP7_M2C_P": "F2",
        "DP7_M2C_N": "F1",
        "DP8_C2M_P": "D31",
        "DP8_C2M_N": "D32",
        "DP8_M2C_P": "E38",
        "DP8_M2C_N": "E39",
        "DP9_C2M_P": "C33",
        "DP9_C2M_N": "C34",
        "DP9_M2C_P": "D36",
        "DP9_M2C_N": "D37",
        "DP10_C2M_P": "B31",
        "DP10_C2M_N": "B32",
        "DP10_M2C_P": "C38",
        "DP10_M2C_N": "C39",
        "DP11_C2M_P": "A33",
        "DP11_C2M_N": "A34",
        "DP11_M2C_P": "B36",
        "DP11_M2C_N": "B37",

        # FMCP_HSPC_GBTCLK0_M2C_(N/P)
        "GBTCLK0_M2C_C_N": "W34",
        "GBTCLK0_M2C_C_P": "W33",
        "GBTCLK1_M2C_C_N": "U34",
        "GBTCLK1_M2C_C_P": "U33",
        "GBTCLK2_M2C_C_N": "P32",
        "GBTCLK2_M2C_C_P": "P31",

        # FMCP_HSPC_CLK(#)_M2C_(M/P)
        "CLK0_M2C_P": "AN10",
        "CLK0_M2C_N": "AP10",
        "CLK1_M2C_P": "AP20",
        "CLK1_M2C_N": "AP19",

        # FMCP_HSPC_LA(##)_(N/P)
        "LA00_CC_P": "AP9",
        "LA00_CC_N": "AR9",
        "LA01_CC_P": "AP8",
        "LA01_CC_N": "AR8",
		"LA01_P": "AP8",
        "LA01_N": "AR8",
        "LA02_P": "AH13",
        "LA02_N": "AJ13",
        "LA03_P": "AJ12",
        "LA03_N": "AK12",
        "LA04_P": "AG12",
        "LA04_N": "AH12",
        "LA05_P": "AM8",
        "LA05_N": "AM7",
        "LA06_P": "AL8",
        "LA06_N": "AL7",
        "LA07_P": "AK13",
        "LA07_N": "AL12",
        "LA08_P": "AL9",
        "LA08_N": "AM9",
        "LA09_P": "AN8",
        "LA09_N": "AN7",
        "LA10_P": "AM12",
        "LA10_N": "AN12",
        "LA11_P": "AT10",
        "LA11_N": "AU10",
        "LA12_P": "AL10",
        "LA12_N": "AM10",
        "LA13_P": "AM13",
        "LA13_N": "AN13",
        "LA14_P": "AL14",
        "LA14_N": "AM14",
        "LA15_P": "AJ14",
        "LA15_N": "AK14",
        "LA16_P": "AR12",
        "LA16_N": "AR11",
        "LA17_P": "AN21",
        "LA17_N": "AP21",
        "LA18_P": "AM20",
        "LA18_N": "AN20",
		"LA19_P": "AU20",
        "LA19_N": "AU19",
		"LA20_P": "AR17",
        "LA20_N": "AT17",
        "LA21_P": "AL19",
        "LA21_N": "AM19",
        "LA22_P": "AR19",
        "LA22_N": "AT19",
        "LA23_P": "AM18",
        "LA23_N": "AN18",
        "LA24_P": "AL22",
        "LA24_N": "AM22",
        "LA25_P": "AL21",
        "LA25_N": "AL20",
        "LA26_P": "AR22",
        "LA26_N": "AT22",
        "LA27_P": "AR21",
        "LA27_N": "AT21",
        "LA28_P": "AJ18",
        "LA28_N": "AK18",
        "LA29_P": "AK22",
        "LA29_N": "AK21",
        "LA30_P": "AG20",
        "LA30_N": "AH20",
        "LA31_P": "AJ20",
        "LA31_N": "AJ19",
        "LA32_P": "AF20",
        "LA32_N": "AF19",
        "LA33_P": "AG18",
        "LA33_N": "AH18",
        }
    ),

    ("LPC", {

        "GBTCLK0_M2C_P": "AA24",
        "GBTCLK0_M2C_N": "AA25",
        "LA01_CC_P": "W25",
        "LA01_CC_N": "Y25",
        "LA05_P": "V27",
        "LA05_N": "V28",
        "LA09_P": "V26",
        "LA09_N": "W26",
        "LA13_P": "AA20",
        "LA13_N": "AB20",
        "LA17_CC_P": "AA32",
        "LA17_CC_N": "AB32",
        "LA23_P": "AD30",
        "LA23_N": "AD31",
        "LA26_P": "AF33",
        "LA26_N": "AG34",
        "CLK0_M2C_P": "AA24",
        "CLK0_M2C_N": "AA25",
        "LA02_P": "AA22",
        "LA02_N": "AB22",
        "LA04_P": "U26",
        "LA04_N": "U27",
        "LA07_P": "V22",
        "LA07_N": "V23",
        "LA11_P": "V21",
        "LA11_N": "W21",
        "LA15_P": "AB25",
        "LA15_N": "AB26",
        "LA19_P": "AA29",
        "LA19_N": "AB29",
        "LA21_P": "AC33",
        "LA21_N": "AD33",
        "LA24_P": "AE32",
        "LA24_N": "AF32",
        "LA28_P": "V31",
        "LA28_N": "W31",
        "LA30_P": "Y31",
        "LA30_N": "Y32",
        "LA32_P": "W30",
        "LA32_N": "Y30",
        "LA06_P": "V29",
        "LA06_N": "W29",
        "LA10_P": "T22",
        "LA10_N": "T23",
        "LA14_P": "U21",
        "LA14_N": "U22",
        "LA18_CC_P": "AB30",
        "LA18_CC_N": "AB31",
        "LA27_P": "AG31",
        "LA27_N": "AG32",
        "CLK1_M2C_P": "AC31",
        "CLK1_M2C_N": "AC32",
        "LA00_CC_P": "W23",
        "LA00_CC_N": "W24",
        "LA03_P": "W28",
        "LA03_N": "Y28",
        "LA08_P": "U24",
        "LA08_N": "U25",
        "LA12_P": "AC22",
        "LA12_N": "AC23",
        "LA16_P": "AB21",
        "LA16_N": "AC21",
        "LA20_P": "AA34",
        "LA20_N": "AB34",
        "LA22_P": "AC34",
        "LA22_N": "AD34",
        "LA25_P": "AE33",
        "LA25_N": "AF34",
        "LA29_P": "U34",
        "LA29_N": "V34",
        "LA31_P": "V33",
        "LA31_N": "W34",
        "LA33_P": "W33",
        "LA33_N": "Y33",
        }
    )
]


class Platform(XilinxPlatform):
    default_clk_name = "clk125"
    default_clk_period = 8.0

    def __init__(self):
        XilinxPlatform.__init__(self, "xcku040-ffva1156-2-e", _io, _connectors,
            toolchain="vivado")

    def create_programmer(self):
        return VivadoProgrammer()