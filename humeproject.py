import os
import asyncio
from hume.legacy import HumeVoiceClient, MicrophoneInterface

async def main() -> None:
    try:
        HUME_API_KEY = "qLv805FNRT6HzK2tHwdg89RwW1UpsXHOxgVw8jyoujZvOihU"
        client = HumeVoiceClient(HUME_API_KEY)

        async with client.connect(config_id="f692be0b-5929-4bb7-8675-2d988bff4432") as socket:
            mic_interface = MicrophoneInterface()
            await mic_interface.start(socket, allow_user_interrupt=True)
    except Exception as e:
        print("⚠️ Error occurred:", e)

if __name__ == "__main__":
    asyncio.run(main())
