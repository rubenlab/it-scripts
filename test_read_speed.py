import os
import time
from statistics import mean

def test_read_speed(directory, block_size=4096):
    read_speeds = []

    file_paths = [os.path.join(directory, file_name) for file_name in os.listdir(directory) if os.path.isfile(os.path.join(directory, file_name))]
    for file_path in file_paths:
        # Test read speed
        start_time = time.time()
        with open(file_path, 'rb') as f:
            while f.read(block_size):
                pass
        read_time = time.time() - start_time
        file_size = os.path.getsize(file_path)

        # Calculate read speed
        read_speed = file_size / read_time / (1024 * 1024)  # MB/s
        read_speeds.append(read_speed)
        print(f"Read speed for {file_path}: {read_speed:.2f} MB/s")

    average_speed = mean(read_speeds)
    print(f"Average read speed: {average_speed:.2f} MB/s")

if __name__ == "__main__":
    # Replace this with the actual directory you want to test
    directory_path = "/mnt/storage/TemScripting/EF-Falcon/Arsen/10_3_22/images/"
    block_size = 256 * 1024  # 256 KB
    test_read_speed(directory_path, block_size)