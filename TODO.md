TODO
    สร้างระบบจัดการร้านค้าในรูปแบบ GUI เก็บไฟล์ข้อมูลเป็น local sql
    - Login ของ Owner และ Cashier
    - ระบบของ Owner และ Cashier
        - ระบบจัดการสิทธิ์เข้าระบบของ Owner
            - เพิ่มลด Owner และ Cashier
            - Log
                - Log การ Login
                    - เก็บ username และบันทึกเวลาเข้าระบบ และเวลาออกจากระบบ
                - Log การแก้ไขสิทธิ์
                    - เก็บ username คนที่แก้ไข้สิทธิ์
                    - แก้ไข้อะไร เวลาเท่าไร
                - Log การเพิ่มรายการสินค้า และระบบสต็อกสินค้า
                    - เก็บ username ที่ทำการเพิ่มสินค้า และเพิ่มสต็อก และระบุเวลา
                - Log การขายสินค้า
                    - เก็บ username รายการสินค้า และจำนวนที่ลูกค้าจ่าย
            - ระบบ Export Log เป็นไฟล์ Excel/PDF
        - ระบบจัดการสินค้า (Owner & Cashier)
            - ระบบเพิ่มรายการสินค้า
            - ระบบสต็อก
            ( สแกน Barcode เพื่อเพิ่มรายการสินค้า และจำนวนสินค้าในสต็อก แต่ถ้าสแกน Barcode และตรวจเจอรายการสินค้า จะเป็นการเพิ่มสต็อก )
    - ระบบขายสินค้า
        ( จะต้อง Login ก่อน )
        - สแกน Barcode สินค้า และดึงข้อมูลชื่อสินค้า และราคา
        - ระบบระบุจำนวนสินค้า ( ถ้าสแกน Barcode สินค้าเดิม 2 รอบระบบจะเพิ่มจำนวนให้เอง )
        - จำนวนราคาสินค้าทั้งหมดในรายการ
        - ระบบหักสินค้าในสต็อกหลังจากคิดเงินลูกค้า
        - ระบบเครื่องคิดเลข เพื่อคิดเงินทอนให้ลูกค้า