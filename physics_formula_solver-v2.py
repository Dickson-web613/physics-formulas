def physics_calculator_v2():
    while True:
        print("\n" + "=" * 38)
        print("    PHYSICS FORMULA SOLVER (SET 2)")
        print("=" * 38)
        print("1. Density (ρ = m / V)")
        print("2. Acceleration (a = (v - u) / t)")
        print("3. Kinetic Energy (KE = 0.5 × m × v²)")
        print("4. Potential Energy (PE = m × g × h)")
        print("5. Ohm's Law - Voltage (V = I × R)")
        
        choice = input("\nSelect a formula (1-5): ").strip()
        
        if choice == '1':
            print("\n--- Calculating Density (ρ = m / V) ---")
            m = float(input("Enter mass (m in kg): "))
            vol = float(input("Enter volume (V in m³): "))
            if vol == 0:
                print("Error: Volume cannot be zero.")
            else:
                density = m / vol
                print(f"Result: Density = {density:.2f} kg/m³")
                
        elif choice == '2':
            print("\n--- Calculating Acceleration (a = (v - u) / t) ---")
            u = float(input("Enter initial velocity (u in m/s): "))
            v = float(input("Enter final velocity (v in m/s): "))
            t = float(input("Enter time taken (t in seconds): "))
            if t == 0:
                print("Error: Time cannot be zero.")
            else:
                acc = (v - u) / t
                print(f"Result: Acceleration = {acc:.2f} m/s²")
                
        elif choice == '3':
            print("\n--- Calculating Kinetic Energy (KE = 0.5 × m × v²) ---")
            m = float(input("Enter mass (m in kg): "))
            v = float(input("Enter velocity (v in m/s): "))
            ke = 0.5 * m * (v ** 2)
            print(f"Result: Kinetic Energy = {ke:.2f} Joules")
            
        elif choice == '4':
            print("\n--- Calculating Potential Energy (PE = m × g × h) ---")
            m = float(input("Enter mass (m in kg): "))
            h = float(input("Enter height (h in meters): "))
            g = 9.81
            pe = m * g * h
            print(f"Result: Potential Energy = {pe:.2f} Joules (using g = 9.81 m/s²)")
            
        elif choice == '5':
            print("\n--- Calculating Voltage (V = I × R) ---")
            current = float(input("Enter current (I in Amperes): "))
            resistance = float(input("Enter resistance (R in Ohms): "))
            voltage = current * resistance
            print(f"Result: Voltage = {voltage:.2f} Volts")
            
        else:
            print("Invalid choice! Please select a number between 1 and 5.")
            
        # Prompt to continue or exit
        cont = input("\nDo you want to continue? (y/n): ").strip().lower()
        if cont not in ['y', 'yes']:
            print("\nExiting program. Goodbye!")
            break

# Run the calculator
if __name__ == "__main__":
    physics_calculator_v2()
