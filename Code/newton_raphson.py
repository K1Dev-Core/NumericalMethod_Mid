"""
วิธีการของนิวตัน-ราฟสัน (Newton-Raphson Method)
สำหรับหาค่ารากของสมการ f(x) = 0
"""

import math


def f(x):
    """
    ฟังก์ชันที่ต้องการหาราก
    ตัวอย่าง: f(x) = x³ - 2x - 5
    """
    return x**3 - 2*x - 5


def df(x):
    """
    อนุพันธ์ของฟังก์ชัน f(x)
    ตัวอย่าง: f'(x) = 3x² - 2
    """
    return 3*x**2 - 2


def newton_raphson(x0, tol=1e-6, max_iter=100):
    """
    วิธีการของนิวตัน-ราฟสันสำหรับหารากของสมการ
    
    พารามิเตอร์:
    x0: ค่าเริ่มต้นเดาของราก
    tol: ค่าความคลาดเคลื่อนที่ยอมรับได้ (default: 1e-6)
    max_iter: จำนวนรอบสูงสุด (default: 100)
    
    คืนค่า: ค่ารากโดยประมาณ
    
    หมายเหตุ:
    - ต้องการอนุพันธ์ของฟังก์ชัน f'(x)
    - มักจะลู่เข้าเร็วมากถ้าค่าเริ่มต้นใกล้กับรากจริง
    - อาจลู่เข้าไม่ได้ถ้าค่าเริ่มต้นไกลจากรากหรือ f'(x) = 0
    """
    x = x0
    
    print("วิธีการของนิวตัน-ราฟสัน")
    print("รอบ\t      x\t\t    x_new\t\t    f(x)\t\t    ความคลาดเคลื่อน")
    print("-" * 85)
    
    # วนรอบเพื่อหาราก
    for i in range(1, max_iter + 1):
        fx = f(x)
        dfx = df(x)
        
        # ตรวจสอบว่าอนุพันธ์เป็นศูนย์หรือไม่
        if dfx == 0:
            raise ZeroDivisionError("วิธีนิวตัน-ราฟสันล้มเหลว: f'(x) = 0")
        
        # คำนวณค่าใหม่
        x_new = x - fx / dfx
        err = abs(x_new - x)
        
        # แสดงผลลัพธ์แต่ละรอบ
        print(f"{i:3d}\t{x:.10f}\t{x_new:.10f}\t{fx:.6e}\t{err:.6e}")
        
        # ตรวจสอบว่าเจอรากแล้วหรือไม่
        if err < tol:
            print("-" * 85)
            return x_new
        
        x = x_new
    
    print("-" * 85)
    return x


def main():
    """
    ฟังก์ชันหลักสำหรับทดสอบวิธีการของนิวตัน-ราฟสัน
    """
    try:
        # กำหนดค่าเริ่มต้น
        x0 = 2.0
        tolerance = 1e-6
        
        print(f"หารากของสมการ f(x) = x³ - 2x - 5")
        print(f"ค่าเริ่มต้น x0 = {x0}")
        print(f"ค่าความคลาดเคลื่อนที่ยอมรับ: {tolerance}")
        print()
        
        # เรียกใช้วิธีการของนิวตัน-ราฟสัน
        root = newton_raphson(x0, tol=tolerance)
        
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
