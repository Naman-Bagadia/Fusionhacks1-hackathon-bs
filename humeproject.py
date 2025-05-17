import os
import asyncio
from hume.legacy import HumeVoiceClient, MicrophoneInterface

async def main() -> None:
    try:
        HUME_API_KEY = "qLv805FNRT6HzK2tHwdg89RwW1UpsXHOxgVw8jyoujZvOihU"
        client = HumeVoiceClient(HUME_API_KEY)

        async with client.connect(config_id="681f31b0-3735-4297-8664-7510563f09d2") as socket:
            mic_interface = MicrophoneInterface()
            await mic_interface.start(socket, allow_user_interrupt=True)
    except Exception as e:
        print("⚠️ Error occurred:", e)

if __name__ == "__main__":
    asyncio.run(main())
