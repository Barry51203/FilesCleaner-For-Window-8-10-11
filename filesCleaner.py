import os
import shutil
import tempfile
from datetime import datetime
from tkinter import messagebox
import tkinter as tk

# ฟังก์ชันสำหรับการลบไฟล์ใน Temp
def clear_temp():
    # กำหนดที่อยู่ไฟล์ log
    log_file = os.path.join(tempfile.gettempdir(), 'FilesCleaner.log')
    with open(log_file, 'w') as log:
        # เขียนข้อความบันทึกลงใน log
        log.write(f"Cleaning Process Started: {datetime.now()}\n")
        
        # ลบไฟล์ใน C:\Windows\temp
        try:
            windows_temp = r'C:\Windows\temp'
            if os.path.exists(windows_temp):
                shutil.rmtree(windows_temp)  # ลบโฟลเดอร์ทั้งหมด
                os.makedirs(windows_temp)  # สร้างโฟลเดอร์ใหม่
                log.write(f"{windows_temp} cleaned.\n")
            else:
                log.write(f"{windows_temp} does not exist.\n")
        except Exception as e:
            log.write(f"Error cleaning {windows_temp}: {str(e)}\n")
        
        # ลบไฟล์ใน C:\Windows\Prefetch
        try:
            windows_prefetch = r'C:\Windows\Prefetch'
            if os.path.exists(windows_prefetch):
                for file in os.listdir(windows_prefetch):
                    os.remove(os.path.join(windows_prefetch, file))
                log.write(f"{windows_prefetch} cleaned.\n")
            else:
                log.write(f"{windows_prefetch} does not exist.\n")
        except Exception as e:
            log.write(f"Error cleaning {windows_prefetch}: {str(e)}\n")

        # ลบไฟล์ใน Temp ของผู้ใช้
        try:
            user_temp = tempfile.gettempdir()
            if os.path.exists(user_temp):
                shutil.rmtree(user_temp)  # ลบโฟลเดอร์ทั้งหมด
                os.makedirs(user_temp)  # สร้างโฟลเดอร์ใหม่
                log.write(f"{user_temp} cleaned.\n")
            else:
                log.write(f"{user_temp} does not exist.\n")
        except Exception as e:
            log.write(f"Error cleaning {user_temp}: {str(e)}\n")

        log.write(f"Cleaning Process Completed: {datetime.now()}\n")

    # แสดงผลการทำงาน
    messagebox.showinfo("Files Cleaner", "Files Cleaner completed successfully.\nLogs can be found at: " + log_file)

# ฟังก์ชันสำหรับการแสดง UI
def main():
    # สร้างหน้าต่าง GUI
    root = tk.Tk()
    root.withdraw()  # ซ่อนหน้าต่างหลัก

    # แสดงข้อความเตือนและรอการกดปุ่ม
    response = messagebox.askyesno("Start Cleaning", "Do you want to start cleaning the temporary files?")
    if response:
        clear_temp()  # เรียกใช้ฟังก์ชันทำความสะอาด
    else:
        messagebox.showinfo("Cancelled", "Cleaning process was cancelled.")

# เรียกใช้โปรแกรม
if __name__ == "__main__":
    main()
