import asyncio
from mavsdk import System
from mavsdk.offboard import (OffboardError, Attitude,PositionNedYaw,AttitudeRate,VelocityNedYaw)

async def run():
    # Inizializza il sistema del drone
    drone = System(sysid=1)
    await drone.connect(system_address="udp://:14541")
    sysid = drone._sysid
    compid = drone._compid
    print("sysid: {sysid}")
    print("compid: {compid}")
    print("Starting offboard mode...")
    try:
        # Avvia la modalità offboard
                # Imposta un setpoint di orientamento per eseguire un flip (ad esempio, rollio a 180 gradi)
        await drone.offboard.set_attitude(Attitude(0, 0, 0, 0))  # 3.14159 radianti è equivalente a 180 gradi

        await drone.offboard.start()
    except OffboardError as error:
        print(f"Starting offboard mode failed with error code: {error._result.result}")
        return

    try:

        await drone.offboard.set_attitude_rate(AttitudeRate(0, 430, 0, 1))  # Roll: 0 deg/s, Pitch: 60 deg/s, Yaw: 0 deg/s, Thrust: 0.5

        # Attendere un po' di tempo per il flip
        await asyncio.sleep(0.38)  # Attendiamo 3 secondi per il flip

        await drone.offboard.set_attitude_rate(AttitudeRate(0, 0, 0, 0))
        # Rimuovi il setpoint di orientamento per tornare in posizione di stabilità
        await drone.offboard.set_attitude(Attitude(0,0,0,0))  # Roll: 0 deg/s, Pitch: 0 deg/s, Yaw: 0 deg/s, Thrust: 0

        # Dopo aver eseguito il flip, puoi fermare la modalità offboard:
        await drone.offboard.stop()

        await drone.action.land()

    except OffboardError as error:
        print(f"Offboard operation failed with error code: {error._result.result}")

asyncio.get_event_loop().run_until_complete(run())
