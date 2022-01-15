import time
import psutil
import json


def get_size(bytes, suffix="B"):
    # unit conversion
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor


def get_stats():
    # Line break
    print("=" * 40, "network Info", "=" * 40)

    # CPU frequencies
    CPU_Frequency = psutil.cpu_freq()
    finalCPU_data = CPU_Frequency.current

    new_value = psutil.net_io_counters().bytes_sent + \
        psutil.net_io_counters().bytes_recv

    bandwith_sent = get_size(psutil.net_io_counters().bytes_sent)

    bandwith_received = get_size(psutil.net_io_counters().bytes_recv)

    data = json.dumps({'cpu_meter': finalCPU_data, 'average_bandwith': new_value,
                       'bandwith_received': bandwith_received, 'bandwith_sent': bandwith_sent})
    print(data)
    return data


if __name__ == "__main__":
    get_stats()
    # while True:
    #     time.sleep(2)  # sleep for 2 seconds
    #     get_stats()
