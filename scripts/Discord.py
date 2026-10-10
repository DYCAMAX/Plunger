from pypresence import Presence
import time

# Discord Presence iD
client_id = "1551906899203465386"

try:
    RPC = Presence(client_id)
    RPC.connect()

    # Discord Rich Presence Status
    RPC.update(
        state="Create a mod on Rabbids Games",
        details="",
        large_image="image_key", 
        large_text="Hover Text",
        start=time.time()
    )

    while True:
        time.sleep(15)  

except Exception as e:
    print(f"Error: {e}")   