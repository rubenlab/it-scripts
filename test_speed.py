import os
import time

def test_disk_speed(file_path, file_size, block_size, wait_time):
    write_speeds = []
    read_speeds = []

    for i in range(10):
        print(f"Running test {i+1} ...")

        # Test write speed
        start_time = time.time()
        with open(file_path, 'wb') as f:
            for _ in range(file_size // block_size):
                f.write(os.urandom(block_size))
            f.flush()
            os.fsync(f.fileno())
        write_time = time.time() - start_time

        # Calculate write speed
        write_speed = file_size / write_time / (1024 * 1024)  # MB/s
        write_speeds.append(write_speed)
        print(f"Write speed: {write_speed:.2f} MB/s")

        # Wait for 1 second to make sure everything is written
        time.sleep(wait_time)

        # Test read speed
        start_time = time.time()
        with open(file_path, 'rb') as f:
            while f.read(block_size):
                pass
        read_time = time.time() - start_time

        # Calculate read speed
        read_speed = file_size / read_time / (1024 * 1024)  # MB/s
        read_speeds.append(read_speed)
        print(f"Read speed: {read_speed:.2f} MB/s")

        # Remove the test file
        os.remove(file_path)

    average_write_speed = sum(write_speeds) / len(write_speeds)
    average_read_speed = sum(read_speeds) / len(read_speeds)

    print(f"Average write speed: {average_write_speed:.2f} MB/s")
    print(f"Average read speed: {average_read_speed:.2f} MB/s")

if __name__ == "__main__":
    file_path = "/mnt/storage/TemScripting/test_file"  # Adjust the path as needed
    # file_path = "/mnt/pool1/home/falcon4/share/TemScripting/test_file"
    file_size = 256 * 1024 * 1024  # 128MB
    block_size = 256 * 1024  # 256 KB
    wait_time = 5  # 1 second

    test_disk_speed(file_path, file_size, block_size, wait_time)