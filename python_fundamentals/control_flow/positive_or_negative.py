cat << 'EOF' > python_fundamentals/control_flow/positive_or_negative.py
#!/usr/bin/env python3
number = __import__('random').randint(-10, 10)
if number > 0:
    print(f"{number} is positive")
elif number == 0:
    print(f"{number} is zero")
else:
    print(f"{number} is negative")
EOF