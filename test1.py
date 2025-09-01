for dist in range(0,50,10):
    print("dist = ", dist)
    num_leds = min(int((60 - dist) // 10) + 1, 5) 
    print("led = ",num_leds)