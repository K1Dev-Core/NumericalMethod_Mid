"""
วิธีการของเครเมอร์ (Cramer's Rule)
สำหรับแก้ระบบสมการเชิงเส้น Ax = b
"""

import numpy as np


def cramers_rule(A, b):
    """
    วิธีการของเครเมอร์สำหรับแก้ระบบสมการเชิงเส้น Ax = b
    
    พารามิเตอร์:
    A: เมทริกซ์สัมประสิทธิ์ (n x n)
    b: เวกเตอร์ค่าคงที่ (n x 1)
    
    คืนค่า: (x, detA) โดยที่
    - x: เวกเตอร์คำตอบ
    - detA: ดีเทอร์มินันต์ของเมทริกซ์ A
    
    หมายเหตุ:
    - เหมาะสำหรับระบบขนาดเล็ก (2x2, 3x3, 4x4)
    - ถ้า det(A) = 0 ระบบจะไม่มีคำตอบเฉพาะ
    """
    # แปลงเป็น numpy array
    A = np.array(A, dtype=float)
    b = np.array(b, dtype=float).reshape(-1)
    
    # ตรวจสอบขนาดของเมทริกซ์
    n, m = A.shape
    if n != m:
        raise ValueError("เมทริกซ์ A ต้องเป็นเมทริกซ์จัตุรัส (n x n)")
    if b.size != n:
        raise ValueError("เวกเตอร์ b ต้องมีขนาดเท่ากับจำนวนแถวของเมทริกซ์ A")
    
    # คำนวณดีเทอร์มินันต์ของเมทริกซ์ A
    detA = np.linalg.det(A)
    if abs(detA) < 1e-10:
        raise ValueError("det(A) = 0 -> ระบบไม่มีคำตอบเฉพาะ (ไม่สามารถใช้วิธีเครเมอร์ได้)")
    
    # สร้างเวกเตอร์คำตอบ
    x = np.zeros(n, dtype=float)
    
    # คำนวณค่า x_i สำหรับแต่ละตัวแปร
    for i in range(n):
        # สร้างเมทริกซ์ A_i โดยแทนที่คอลัมน์ที่ i ด้วยเวกเตอร์ b
        Ai = A.copy()
        Ai[:, i] = b
        
        # คำนวณ x_i = det(A_i) / det(A)
        x[i] = np.linalg.det(Ai) / detA
    
    return x, detA


def main():
    """
    ฟังก์ชันหลักสำหรับทดสอบวิธีการของเครเมอร์
    """
    try:
        # ตัวอย่างระบบสมการ 3x3:
        # 2x +  y -  z =  8
        # -3x - y + 2z = -11
        # -2x + y + 2z = -3
        A = [
            [ 2,  1, -1],
            [-3, -1,  2],
            [-2,  1,  2],
        ]
        b = [8, -11, -3]
        
        print("วิธีการของเครเมอร์สำหรับแก้ระบบสมการเชิงเส้น")
        print("ระบบสมการ:")
        print("2x +  y -  z =  8")
        print("-3x - y + 2z = -11")
        print("-2x + y + 2z = -3")
        print()
        
        # เรียกใช้วิธีการของเครเมอร์
        x, detA = cramers_rule(A, b)
        
        print(f"det(A) = {detA:.6f}")
        print(f"คำตอบ (x, y, z) = ({x[0]:.6f}, {x[1]:.6f}, {x[2]:.6f})")
        
        # ตรวจสอบคำตอบ
        print("\nตรวจสอบคำตอบ:")
        for i in range(len(A)):
            lhs = sum(A[i][j] * x[j] for j in range(len(x)))
            print(f"สมการที่ {i+1}: {lhs:.6f} = {b[i]:.6f} (ความคลาดเคลื่อน = {abs(lhs - b[i]):.2e})")
        
    except ValueError as e:
        print(f"เกิดข้อผิดพลาด: {e}")
    except Exception as e:
        print(f"เกิดข้อผิดพลาดที่ไม่คาดคิด: {e}")


if __name__ == "__main__":
    main()
