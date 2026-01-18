"""
วิธีการคอร์ด (Secant Method)
สำหรับหาค่ารากของสมการ f(x) = 0
"""

import math


def f(x):
    """
    ฟังก์ชันที่ต้องการหาราก
    ตัวอย่าง: f(x) = cos(x) - x
    """
    return math.cos(x) - x


def secant(x0, x1, tol=1e-6, max_iter=100):
    """
    วิธีการคอร์ดสำหรับหารากของสมการ
    
    พารามิเตอร์:
    x0, x1: ค่าเริ่มต้นสองจุดแรก
    tol: ค่าความคลาดเคลื่อนที่ยอมรับได้ (default: 1e-6)
    max_iter: จำนวนรอบสูงสุด (default: 100)
    
    คืนค่า: ค่ารากโดยประมาณ
    
    หมายเหตุ:
    - ไม่ต้องการการครอบราก (bracketing) เหมือนวิธีการแบ่งครึ่ง
    - ใช้จุดสองจุดก่อนหน้าเพื่อประมาณอนุพันธ์ (ไม่ต้องการ f'(x))
    - มักจะเร็วกว่าวิธีการแบ่งครึ่งแต่ช้ากว่าวิธีนิวตัน-ราฟสัน
    """
    print("วิธีการคอร์ด (Secant Method)")
    print("รอบ\t      x0\t\t      x1\t\t      x2\t\t    ความคลาดเคลื่อน")
    print("-" * 85)
    
    # วนรอบเพื่อหาราก
    for i in range(1, max_iter + 1):
        f0 = f(x0)
        f1 = f(x1)
        
        # ตรวจสอบว่าตัวหารเป็นศูนย์หรือไม่
        if (f1 - f0) == 0:
            raise ZeroDivisionError("วิธีคอร์ดล้มเหลว: f(x1) - f(x0) = 0")
        
        # คำนวณค่าใหม่โดยใช้สูตรคอร์ด
        x2 = x1 - f1 * (x1 - x0) / (f1 - f0)
        err = abs(x2 - x1)
        
        # แสดงผลลัพธ์แต่ละรอบ
        print(f"{i:3d}\t{x0:.10f}\t{x1:.10f}\t{x2:.10f}\t{err:.6e}")
        
        # ตรวจสอบว่าเจอรากแล้วหรือไม่
        if err < tol:
            print("-" * 85)
            return x2
        
        # อัพเดทค่าสำหรับรอบถัดไป
        x0, x1 = x1, x2
    
    print("-" * 85)
    return x1


def main():
    """
    ฟังก์ชันหลักสำหรับทดสอบวิธีการคอร์ด
    """
    try:
        # กำหนดค่าเริ่มต้นสองจุด
        x0 = 0.5
        x1 = 1.0
        tolerance = 1e-6
        
        print(f"หารากของสมการ f(x) = cos(x) - x")
        print(f"ค่าเริ่มต้น x0 = {x0}, x1 = {x1}")
        print(f"ค่าความคลาดเคลื่อนที่ยอมรับ: {tolerance}")
        print()
        
        # เรียกใช้วิธีการคอร์ด
        root = secant(x0, x1, tol=tolerance)
        
        print(f"\nรากของสมการคือ x ≈ {root:.10f}")
        print(f"ตรวจสอบ: f({root:.10f}) = {f(root):.6e}")
        
    except ValueError as e:
        print(f"เกิดข้อผิดพลาด: {e}")
    except ZeroDivisionError as e:
        print(f"เกิดข้อผิดพลาด: {e}")
    except Exception as e:
        print(f"เกิดข้อผิดพลาดที่ไม่คาดคิด: {e}")


if __name__ == "__main__":
    main()
