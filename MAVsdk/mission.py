import asyncio
from mavsdk import System
from mavsdk.mission import (MissionItem, MissionPlan)

async def run():
    drone = System(sysid=1)
    await drone.connect(system_address="udp://:14541")
    sysid = drone._sysid
    compid = drone._compid
    print("sysid: {sysid}")
    print("compid: {compid}")

    await drone.action.arm()

    mission_items = []
    #mission_items.append(MissionItem(47.398039859999997, 8.5455725400000002, 2.5, 5, 
    #                                 True, float('nan'), float('nan'), MissionItem.CameraAction.NONE, float('nan'), float('nan'),float('nan'),float('nan'),float('nan')))
    mission_items.append(MissionItem(38.1608227, -122.4535923, 15, 5, 
     True, float('nan'), float('nan'), MissionItem.CameraAction.NONE, float('nan'), float('nan'),float('nan'),float('nan'),float('nan')))
    
    mission_items.append(MissionItem(38.1603321, -122.4531431, 15, 5, 
     True, float('nan'), float('nan'), MissionItem.CameraAction.NONE, float('nan'), float('nan'),float('nan'),float('nan'),float('nan')))
    
    mission_items.append(MissionItem(38.1586948, -122.4524834, 15, 5, 
     True, float('nan'), float('nan'), MissionItem.CameraAction.NONE, float('nan'), float('nan'),float('nan'),float('nan'),float('nan')))
    
    mission_items.append(MissionItem(38.1588013, -122.4518987, 15, 5, 
     True, float('nan'), float('nan'), MissionItem.CameraAction.NONE, float('nan'), float('nan'),float('nan'),float('nan'),float('nan')))
    
    mission_items.append(MissionItem(38.1614728, -122.4528851, 15, 5, 
     True, float('nan'), float('nan'), MissionItem.CameraAction.NONE, float('nan'), float('nan'),float('nan'),float('nan'),float('nan')))
    # ... aggiungi altri waypoint come necessario


    mission_plan = MissionPlan(mission_items)
    print(drone)
    await drone.mission.upload_mission(mission_plan)
    await drone.mission.start_mission()

asyncio.get_event_loop().run_until_complete(run())
