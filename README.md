# Calculator made with Tkinter
Basic calculator made for practice with python and to learn a bit of TKinter

![preview picture](preview.PNG)

For now it contains just basic functions like:
- addition
- subtraction
- multiplying
- division
- percentage calculation

I might add more in the future

Even tho it is just calculator, it still had some coding and logic to do, because of buttons functionality.

### Main features:
- Input checking (for example: only one 0 at front of the fraction, or only one dot per number, and more)
- Replacing last sign if we hit sign again
- If there is sign as last input and '.' will be clicked, it will add 0 before dot
- Correct order of operations
- For percentage: replace last number with calculated number: if last operation is adding, or subtracting, it will calculate whole input and insert right number instead percentage; if last operation is multiplying or dividing it will divide last number by 100
- Copying to clipboard


### Installation:
- Activate venv
- pip install -r requirements.txt
- python3 start.py