import socket
import re
import math

def solve_quadratic(a, b, c):
    """Solve the quadratic equation ax^2 + bx + c = 0."""
    discriminant = b**2 - 4*a*c
    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        return f"x1: {root1:.3f} ; x2: {root2:.3f}"
    elif discriminant == 0:
        root = -b / (2*a)
        return f"x: {root:.3f}"
    else:
        return "Not possible"


def parse_equation(equation):
    """Parse the equation string to extract coefficients A, B, C, and D."""
    # Remove spaces and normalize formatting
    equation = equation.replace(" ", "")

    # Match coefficients A, B, C, and D
    match = re.match(r"([+-]?\d+\.?\d*)x²([+-]?\d+\.?\d*)x¹([+-]?\d+)=([+-]?\d+)", equation)
    if match:
        a = float(match.group(1))  # Coefficient of x²
        b = float(match.group(2))  # Coefficient of x¹
        c = float(match.group(3))  # Constant term on the left-hand side
        d = float(match.group(4))  # Constant term on the right-hand side
        return a, b, c - d  # Adjust c to account for the right-hand side constant
    else:
        raise ValueError("Invalid equation format")

def main():
    host = "challenge01.root-me.org"
    port = 52018

    # Create a TCP socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.settimeout(20)  # Extend timeout for slower responses
        print(f"Connecting to {host}:{port}...")
        client_socket.connect((host, port))
        print("Connected successfully!")

        while True:
            try:
                # Receive the equation prompt
                prompt = client_socket.recv(4096).decode('utf-8').strip()
                print(prompt)

                if "Solve this equation please:" in prompt:
                    # Extract the equation from the prompt
                    equation = prompt.split("Solve this equation please:")[1].strip()
                    print(f"Equation: {equation}")

                    # Parse the equation and solve it
                    try:
                        a, b, c = parse_equation(equation)
                        solution = solve_quadratic(a, b, c)
                        print(f"Solution: {solution}")

                        # Send the solution back to the server
                        client_socket.sendall((solution + "\n").encode('utf-8'))
                    except Exception as e:
                        print(f"Error parsing or solving the equation: {e}")
                        break
                else:
                    # Print any final message or response
                    print(prompt)
                    client_socket.close()
                    break
            except socket.timeout:
                print("Connection timed out. Retrying...")
                break
            except Exception as e:
                print(f"An error occurred: {e}")
                break

if __name__ == "__main__":
    main()

