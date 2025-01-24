import asyncio

from library.ascyn_example.message import MessageType


class PowerDevice:
    async def connect(self) -> None:
        print("Connecting to power device")
        await asyncio.sleep(0.5)
        print("Power device connected.")

    async def disconnect(self) -> None:
        print("Disconnecting power device")
        await asyncio.sleep(0.5)
        print("Power device disconnected.")

    async def send_message(self, message_type: MessageType, data: str = "") -> None:
        print(f"Power device handling message of type {message_type.name} with data [{data}].")
        await asyncio.sleep(0.5)
        print("Power device received message.")


class LowPowerDevice:
    async def connect(self) -> None:
        print("Connecting to Low Power Device")
        await asyncio.sleep(0.5)
        print("Low Power Device connected.")

    async def disconnect(self) -> None:
        print("Disconnecting Low Power Device")
        await asyncio.sleep(0.5)
        print("Low Power Device disconnected.")

    async def send_message(self, message_type: MessageType, data: str = "") -> None:
        print(f"Low Power Device handling message of type {message_type.name} with data [{data}].")
        await asyncio.sleep(0.5)
        print("Smart Speaker received message.")


class ComputerDevice:
    async def connect(self) -> None:
        print("Connecting to Computer Device")
        await asyncio.sleep(0.5)
        print("Computer Device connected.")

    async def disconnect(self) -> None:
        print("Disconnecting Computer Device")
        await asyncio.sleep(0.5)
        print("Computer Device disconnected.")

    async def send_message(self, message_type: MessageType, data: str = "") -> None:
        print(f"Computer Device handling message of type {message_type.name} with data [{data}].")
        await asyncio.sleep(0.5)
        print("Computer Device received message.")
