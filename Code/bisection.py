"""
วิธีการแบ่งครึ่ง (Bisection Method)
สำหรับหาค่ารากของสมการ f(x) = 0
"""

import math


def f(x):
    """
    ฟังก์ชันที่ต้องการหาราก
    ตัวอย่าง: f(x) = x³ - 4x - 9
    """
    return x**3 - 4*x - 9


def bisection(a, b, tol=1e-6, max_iter=100):
    """
    วิธีการแบ่งครึ่งสำหรับหารากของสมการ
    
    พารามิเตอร์:
    a, b: ช่วงเริ่มต้น [a, b] ที่มีรากอยู่ระหว่าง (f(a)*f(b) < 0)
    tol: ค่าความคลาดเคลื่อนที่ยอมรับได้ (default: 1e-6)
    max_iter: จำนวนรอบสูงสุด (default: 100)
    
    คืนค่า: ค่ารากโดยประมาณ
    """
    # ตรวจสอบเงื่อนไขการมีรากในช่วง
    fa = f(a)
    fb = f(b)
    
    if fa * fb > 0:
        raise ValueError("ต้องมี f(a)*f(b) < 0 เพื่อให้แน่ใจว่ามีรากในช่วง [a,b]")
    
    print("วิธีการแบ่งครึ่ง")
    print("รอบ\t      a\t\t      b\t\t      c\t\t    f(c)")
    print("-" * 70)
    
    # วนรอบเพื่อหาราก
    for i in range(1, max_iter + 1):
        # หาจุดกึ่งกลาง
        c = (a + b) / 2
        fc = f(c)
        
        # แสดงผลลัพธ์แต่ละรอบ
        print(f"{i:3d}\t{a:.10f}\t{b:.10f}\t{c:.10f}\t{fc:.6e}")
        
        # ตรวจสอบว่าเจอรากแล้วหรือไม่
        if abs(fc) < tol or abs(b - a) < tol:
            print("-" * 70)
            return c
        
        # ปรับช่วงตามค่าของ f(c)
        if fa * fc < 0:
            b = c
            fb = fc
        else:
            a = c
            fa = fc
    
    print("-" * 70)
    return c


def main():
    """
    ฟังก์ชันหลักสำหรับทดสอบวิธีการแบ่งครึ่ง
    """
    try:
        # กำหนดช่วงเริ่มต้นที่มีรากอยู่ระหว่าง
        a = 2.0
        b = 3.0
        tolerance = 1e-6
        
        print(f"หารากของสมการ f(x) = x³ - 4x - 9 ในช่วง [{a}, {b}]")
        print(f"ค่าความคลาดเคลื่อนที่ยอมรับ: {tolerance}")
        print()
        
        # เรียกใช้วิธีการแบ่งครึ่ง
        root = bisection(a, b, tol=tolerance)
        
        print(f"\nรากของสมการคือ x ≈ {root:.10f}")
        print(f"ตรวจสอบ: f({root:.10f}) = {f(root):.6e}")
        
    except ValueError as e:
        print(f"เกิดข้อผิดพลาด: {e}")
    except Exception as e:
        print(f"เกิดข้อผิดพลาดที่ไม่คาดคิด: {e}")


if __name__ == "__main__":
    main()
