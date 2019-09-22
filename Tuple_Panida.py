{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "1.กำหนดให้ brand_shirt = (\"CPS\", \"CCDOUBLEO\", \"AIIZ\",\"ELLE\", \"LACOSTE\", \"NIKE\")\n",
    "\n",
    "1.1 ให้เขียนคำสั่งโปรแกรมแสดงตำแหน่งของแบรนด์ AIIZ,CPSและ NIKE\n",
    "1.2 ให้เขียนคำสั่งโปรแกรมแสดงจำนวนข้อมูลทั้งหมดในทูเพิล\n",
    "1.3 ให้เขียนคำสั่งโปรแกรมตรวจสอบแบรนด์เสื้อ ELLE, KITO, ADDA อยู่ใน shirt หรือไม่"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "ตำแหน่งของแบรนด์ AIIZ คือ 2\n",
      "ตำแหน่งของแบรนด์ LACOSTE คือ 4\n",
      "ตำแหน่งของแบรนด์ NIKE คือ 5\n",
      "จำนวนข้อมูลทั้งหมดในทูเพิล คือ 6 รายการ\n",
      "มีแบรนด์ ELLE อยู่ใน brand_shirt หรือไม่ = True\n",
      "มีแบรนด์ KITO อยู่ใน brand_shirt หรือไม่ = False\n",
      "มีแบรนด์ ADDA อยู่ใน brand_shirt หรือไม่ = False\n"
     ]
    }
   ],
   "source": [
    "brand_shirt = (\"CPS\", \"CCDOUBLEO\", \"AIIZ\", \"ELLE\", \"LACOSTE\", \"NIKE\" )\n",
    "print(\"ตำแหน่งของแบรนด์ AIIZ คือ\",brand_shirt.index(\"AIIZ\"))\n",
    "print(\"ตำแหน่งของแบรนด์ LACOSTE คือ\",brand_shirt.index(\"LACOSTE\"))\n",
    "print(\"ตำแหน่งของแบรนด์ NIKE คือ\",brand_shirt.index(\"NIKE\"))\n",
    "print(\"จำนวนข้อมูลทั้งหมดในทูเพิล คือ\",len(brand_shirt),\"รายการ\")\n",
    "print(\"มีแบรนด์ ELLE อยู่ใน brand_shirt หรือไม่ =\",\"ELLE\" in brand_shirt)\n",
    "print(\"มีแบรนด์ KITO อยู่ใน brand_shirt หรือไม่ =\",\"KITO\" in brand_shirt)\n",
    "print(\"มีแบรนด์ ADDA อยู่ใน brand_shirt หรือไม่ =\",\"ADDA\" in brand_shirt)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
