# core/memory_scanner.py

from pymem import Pymem
from pymem.exception import ProcessNotFound
import re

def attach_to_process(process_name):
    try:
        pm = Pymem(process_name)
        return pm
    except ProcessNotFound:
        return None

def scan_for_value(pm, value, value_type='int'):
    matches = []

    if value_type == 'int':
        value = int(value)
        scan_func = pm.search_all_memory
        pattern = value.to_bytes(4, byteorder='little', signed=True)
    elif value_type == 'string':
        scan_func = pm.pattern_scan_all
        pattern = bytes(value, 'utf-8')
    else:
        return ["[!] Unsupported value type"]

    try:
        for region in pm.process.iter_region():
            try:
                buffer = pm.read_bytes(region.base_address, region.region_size)
                if pattern in buffer:
                    offset = buffer.find(pattern)
                    addr = region.base_address + offset
                    matches.append(f"[MEMORY] Found match at 0x{addr:08X}")
            except:
                continue
    except Exception as e:
        matches.append(f"[!] Memory scan failed: {e}")

    return matches if matches else ["[MEMORY] No matching values found."]
