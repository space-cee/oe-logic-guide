# GATE
All standard gate logic blocks


# AND Gate

![AND Block](../../images/AND.png)

**Category:** OE Logic > Gates > AND Gate

**Description:** Returns true if both inputs are true.

**Input types:**  
- boolean  

**Output types:**  
- boolean

**Simulation:**  

| Input 1 | Input 2 | Output |
|---------|---------|--------|
| 0       | 0       | 0      |
| 0       | 1       | 0      |
| 1       | 0       | 0      |
| 1       | 1       | 1      |


# NAND Gate

![NAND Block](../../images/NAND.png)

**Category:** OE Logic > Gates > NAND Gate

**Description:** Returns true while any input is false.

**Input types:**  
- boolean  

**Output types:**  
- boolean

**Simulation:**  

| Input 1 | Input 2 | Output |
|---------|---------|--------|
| 0       | 0       | 1      |
| 0       | 1       | 1      |
| 1       | 0       | 1      |
| 1       | 1       | 0      |

Logically equivalent to an AND gate with a NOT after it.


# OR Gate

![OR Block](../../images/OR.png)

**Category:** OE Logic > Gates > OR Gate

**Description:** Returns true any input is the same.

**Input types:**  
- boolean  

**Output types:**  
- boolean

**Simulation:**  

| Input 1 | Input 2 | Output |
|---------|---------|--------|
| 0       | 0       | 0      |
| 0       | 1       | 1      |
| 1       | 0       | 1      |
| 1       | 1       | 1      |


# NOR Gate

![NOR Block](../../images/NOR.png)

**Category:** OE Logic > Gates > NOR Gate

**Description:** Returns true when none of the inputs are true.

**Input types:**  
- boolean  

**Output types:**  
- boolean

**Simulation:**  

| Input 1 | Input 2 | Output |
|---------|---------|--------|
| 0       | 0       | 1      |
| 0       | 1       | 0      |
| 1       | 0       | 0      |
| 1       | 1       | 0      |

Logically equivalent to an OR gate with a NOT after it.


# XOR Gate

![XOR Block](../../images/XOR.png)

**Category:** OE Logic > Gates > XOR Gate

**Description:** Returns true only if one input is true
**Input types:**  
- boolean  

**Output types:**  
- boolean

**Simulation:**  

| Input 1 | Input 2 | Output |
|---------|---------|--------|
| 0       | 0       | 0      |
| 0       | 1       | 1      |
| 1       | 0       | 1      |
| 1       | 1       | 0      |


# XNOR Gate

![XNOR Block](../../images/XNOR.png)

**Category:** OE Logic > Gates > XNOR Gate

**Description:** Returns true if both inputs are the same.

**Input types:**  
- boolean  

**Output types:**  
- boolean

**Simulation:**  

| Input 1 | Input 2 | Output |
|---------|---------|--------|
| 0       | 0       | 1      |
| 0       | 1       | 0      |
| 1       | 0       | 0      |
| 1       | 1       | 1      |

Logically equivalent to a XOR gate with a NOT after it.



# MUX (Multiplexer)

![Multiplexer Block](../../images/Multiplexer.gif)

**Category:** OE Logic > Gates > Multiplexer

**Description:** Outputs values depending on 'State' input.

**Input types:**  
- Universal 

**State types:**
- bool
- number
- byte

**Output types:**  
- Universal

**Simulation:**  

**Number/Byte State:**

|  State  | Output |
|---------|--------|
|   ≤ 0   | False input |
|   ≥ 1   | True input |



**Bool State:**

|  State  | Output |
|---------|--------|
|   False | False input |
|   True  | True input |
