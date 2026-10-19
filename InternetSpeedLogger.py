import speedtest
import csv
import os
from datetime import datetime

FILE_NAME = "speed_history.csv"


def run_speed_test():
    print("\nConnecting to speed test server...")

    try:
        st = speedtest.Speedtest()
        st.get_best_server()

        print("Testing download speed...")
        download = st.download() / 1_000_000

        print("Testing upload speed...")
        upload = st.upload() / 1_000_000

        ping = st.results.ping

        date_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        print("\n========================================")
        print("          INTERNET SPEED REPORT")
        print("========================================")
        print(f"Date & Time    : {date_time}")
        print(f"Download Speed : {download:.2f} Mbps")
        print(f"Upload Speed   : {upload:.2f} Mbps")
        print(f"Ping           : {ping:.2f} ms")
        print("========================================")

        file_exists = os.path.exists(FILE_NAME)

        with open(FILE_NAME, "a", newline="") as file:
            writer = csv.writer(file)

            if not file_exists or os.path.getsize(FILE_NAME) == 0:
                writer.writerow([
                    "Date & Time",
                    "Download (Mbps)",
                    "Upload (Mbps)",
                    "Ping (ms)"
                ])

            writer.writerow([
                date_time,
                round(download, 2),
                round(upload, 2),
                round(ping, 2)
            ])

        print("Result saved to speed_history.csv")

    except Exception as error:
        print("\nSpeed test failed.")
        print("Check your internet connection.")
        print("Error:", error)


def view_history():
    if not os.path.exists(FILE_NAME):
        print("\nNo speed test history found.")
        return

    print("\n============== SPEED HISTORY ==============")

    with open(FILE_NAME, "r", newline="") as file:
        reader = csv.reader(file)

        for row in reader:
            print(" | ".join(row))

    print("===========================================")


while True:
    print("\n========================================")
    print("       INTERNET SPEED TEST LOGGER")
    print("========================================")
    print("1. Test Internet Speed")
    print("2. View Speed History")
    print("3. Exit")
    print("========================================")

    choice = input("Choose option: ").strip()

    if choice == "1":
        run_speed_test()

    elif choice == "2":
        view_history()

    elif choice == "3":
        print("Thank