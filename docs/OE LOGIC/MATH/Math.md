# MATH
All standard math logic blocks


# ABS (Absolute)

![ABS Block](../../images/ABS.png)

**Category:** OE Logic > Math > Absolute

**Description:** Removes the minus sign from your number.

**Input types:**  
- number  
- vector (both inputs must be the same type)

**Output types:**  
- number  
- vector (same type as inputs)

**Examples:**  
- `-5 -> 5`  
- `(-2,5,-7) -> (2,5,7)`


# ADD (Addition)

![ADD Block](../../images/ADD.png)

**Category:** OE Logic > Math > Addition

**Description:** Adds values together.  

**Input types:**  
- number  
- vector (both inputs must be the same type)  

**Output types:**  
- number  
- vector (same type as inputs)  

**Examples:**  
- `3 + 4 = 7`  
- `(10, 20, 13) + (5, 3, 7) = (15, 23, 20)`  
- `-5 + 3 = 2`


# CEIL (Ceiling)

![CEIL Block](../../images/CEIL.png)

**Category:** OE Logic > Math > Ceiling

**Description:** Rounds input numbers up.  

**Input types:**  
- number  
- vector (both inputs must be the same type)  

**Output types:**  
- number  
- vector (same type as inputs)  

**Examples:**  
- `-5.43 → -5`  
- `3.5 → 4`  
- `(10.4, -20.6, 13.5) → (11, -20, 14)`


# DIV (Division)

![DIV Block](../../images/DIV.png)

**Category:** OE Logic > Math > Division

**Description:** Divides the first value by the second.  

**Input types:**  
- number  
- vector (both inputs must be the same type)  

**Output types:**  
- number  
- vector (same type as inputs)  

**Examples:**  
- `-5/3 = 1.667`  
- `10/2 = 5`  
- `8/0 = UNDEFINED`  
- `(10, 20, 13) + (5, -3, 7) = (2, -6.667, 1.857)`

**Tip:** Dividing by 0 will result in undefined, setting the block on fire.


# FLOOR

![FLOOR Block](../../images/FLOOR.png)

**Category:** OE Logic > Math Floor

**Description:** Rounds input numbers down.  

**Input types:**  
- number  
- vector (both inputs must be the same type)  

**Output types:**  
- number  
- vector (same type as inputs)  

**Examples:**  
- `-5.43 → -6`  
- `3.5 → 3`  
- `(10.4, -20.6, 13.5) → (10, -21, 13)`


# MUL (Multiplication)

![MUL Block](../../images/MUL.png)

**Category:** OE Logic > Math > Multiplication

**Description:** Multiplies both values together.  

**Input types:**  
- number  
- vector (both inputs must be the same type)  

**Output types:**  
- number  
- vector (same type as inputs)  

**Examples:**  
- `5 * 5 = 25`  
- `9 * -12 = -108`  
- `-8 * 0 = 0`  
- `(10, 20, -13) * (5, -3, -7) = (50, -60, 91)`



# SUB (Subtraction)

![SUB Block](../../images/SUB.png)

**Category:** OE Logic > Math > Subtraction

**Description:** Subtracs the second value from the first.  

**Input types:**  
- number  
- vector (both inputs must be the same type)  

**Output types:**  
- number  
- vector (same type as inputs)  

**Examples:**  
- `3 - 4 = -1`  
- `(10, 20, 13) - (5, 3, 7) = (5, 17, 6)`  
- `-5 - 3 = -8`
