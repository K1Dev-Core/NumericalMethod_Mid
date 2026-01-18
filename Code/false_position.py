"""
วิธีการจุดเท็จ (False Position Method / Regula Falsi)
สำหรับหาค่ารากของสมการ f(x) = 0
"""

import math


def f(x):
    """
    ฟังก์ชันที่ต้องการหาราก
    ตัวอย่าง: f(x) = e^(-x) - x
    """
    return math.exp(-x) - x


def false_position(a, b, tol=1e-6, max_iter=100):
    """
    วิธีการจุดเท็จสำหรับหารากของสมการ
    
    พารามิเตอร์:
    a, b: ช่วงเริ่มต้น [a, b] ที่มีรากอยู่ระหว่าง (f(a)*f(b) < 0)
    tol: ค่าความคลาดเคลื่อนที่ยอมรับได้ (default: 1e-6)
    max_iter: จำนวนรอบสูงสุด (default: 100)
    
    คืนค่า: ค่ารากโดยประมาณ
    
    หมายเหตุ:
    - ใช้การสร้างเส้นตรงระหว่างจุด (a,f(a)) และ (b,f(b)) เพื่อประมาณราก
    - มักจะเร็วกว่าวิธีการแบ่งครึ่ง
    """
    # ตรวจสอบเงื่อนไขการมีรากในช่วง
    fa = f(a)
    fb = f(b)
    
    if fa * fb > 0:
        raise ValueError("ต้องมี f(a)*f(b) < 0 เพื่อให้แน่ใจว่ามีรากในช่วง [a,b]")
    
    print("วิธีการจุดเท็จ (False Position)")
    print("รอบ\t      a\t\t      b\t\t      xr\t\t   f(xr)")
    print("-" * 75)
    
    xr = None
    # วนรอบเพื่อหาราก
    for i in range(1, max_iter + 1):
        # หาจุดประมาณรากโดยใช้การสร้างเส้นตรง
        xr = (a * fb - b * fa) / (fb - fa)
        fxr = f(xr)
        
        # แสดงผลลัพธ์แต่ละรอบ
        print(f"{i:3d}\t{a:.10f}\t{b:.10f}\t{xr:.10f}\t{fxr:.6e}")
        
        # ตรวจสอบว่าเจอรากแล้วหรือไม่
        if abs(fxr) < tol:
            print("-" * 75)
            return xr
        
        # ปรับช่วงตามค่าของ f(xr)
        if fa * fxr < 0:
            b = xr
            fb = fxr
        else:
            a = xr
            fa = fxr
    
    print("-" * 75)
    return xr


def main():
    """
    ฟังก์ชันหลักสำหรับทดสอบวิธีการจุดเท็จ
    """
    try:
        # กำหนดช่วงเริ่มต้นที่มีรากอยู่ระหว่าง
        a = 0.0
        b = 1.0
        tolerance = 1e-6
        
        print(f"หารากของสมการ f(x) = e^(-x) - x ในช่วง [{a}, {b}]")
        print(f"ค่าความคลาดเคลื่อนที่ยอมรับ: {tolerance}")
        print()
        
        # เรียกใช้วิธีการจุดเท็จ
        root = false_position(a, b, tol=tolerance)
        
        print(f"\nรากของสมการคือ x ≈ {root:.10f}")
        print(f"ตรวจสอบ: f({root:.10f}) = {f(root):.6e}")
        
    except ValueError as e:
        print(f"เกิดข้อผิดพลาด: {e}")
    except Exception as e:
        print(f"เกิดข้อผิดพลาดที่ไม่คาดคิด: {e}")


if __name__ == "__main__":
    main()
