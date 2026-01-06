"""
This code is only made for educational and practice purposes. 
Author and Async Development are not responsible for misuse.

GhoSty OwO V4 Alpha Build
Stable Alpha Build Version: 011125.4.0.2

GitHub: https://github.com/WannaBeGhoSt
Discord: https://discord.gg/SyMJymrV8x
"""

import random as ghostyjija
import time
import re
import unicodedata
import asyncio as made_by_ghosty
from datetime import datetime, timedelta
from .utils import ghosty
from .modules import parse_zoo_message, fetch_zoo_data, format_value, parse_gems, SPEED_MODES
from .ghostycorehb import GhoStySolveNormalCap, GhoStySyncedCaptchaSolve

ghosty_start_time = datetime.now()
ghosty_commands_sent = 0
ghosty_gems_used = 0
last_gem_check = 0

running = True
pray_loop_running = True
has_started = False
sleep_mode = False
farming_start_time = None 
sleep_start_time = None

current_speed_mode = "durable"  
last_mode_change_time = datetime.now()

initial_cash = 0
initial_essence = 0
current_cash = 0
current_essence = 0
zoo_channel = None

GhoStyHbAlrActiveVar = False
GhoStyHuntbotTimestampJson = "ghostyhbtps.json"

GhoStyCoreAvailCheck = True

def ParseGhoStyTimeStrs(time_str):
    time_str = time_str.upper().strip()
    h = int(re.search(r'(\d+)H', time_str).group(1)) if 'H' in time_str else 0
    m = int(re.search(r'(\d+)M', time_str).group(1)) if 'M' in time_str else 0
    return timedelta(hours=h, minutes=m)

def LoadGhoStysHbData():
    try:
        import json as ghostop
        import os as brutality_ghosty
        if brutality_ghosty.path.exists(GhoStyHuntbotTimestampJson):
            with open(GhoStyHuntbotTimestampJson, "r") as f:
                return ghostop.load(f)
    except: pass
    return {}

def SaveHbDataGhoStys(data):
    import json as ghostop
    with open(GhoStyHuntbotTimestampJson, "w") as f:
        ghostop.dump(data, f, indent=4)

def GhoStyEmbedParser(msg_content):
    try:
        content = msg_content.lower().replace(",", "")
        match = re.search(r"current max autohunt:.*?for (\d+) cowoncy", content)
        if match:
            return int(match.group(1))
    except: pass
    return 20000 

async def GhoStyCapUrlSolver(url):
    try:
        if GhoStySolveNormalCap:
            try: return await GhoStySolveNormalCap(url)
            except: pass
        if GhoStySyncedCaptchaSolve:
            try: return GhoStySyncedCaptchaSolve(url)
            except: pass
    except: pass
    return None

async def CheckGhoStyHbMsgFetch(ctx, cowoncy_amount=None):
    global GhoStyHbAlrActiveVar
    try:
        await made_by_ghosty.sleep(1)
        messages = await ctx.channel.history(limit=5).flatten()

        for msg in messages:
            if msg.author.id != 408785106942164992:
                continue

            msg_content = str(msg.content)
            if not msg_content and msg.embeds:
                embed = msg.embeds[0]
                msg_content = (embed.description or "") + "".join(f"{f.name}\n{f.value}" for f in embed.fields)
            msg_content_lower = msg_content.lower()

            if "beep. boop. i am huntbot" in msg_content_lower:
                optimal_cowoncy = GhoStyEmbedParser(msg_content)
                print(f"HuntBot: Found optimal cowoncy: {optimal_cowoncy}")
                
                data = LoadGhoStysHbData()
                data["optimal_cowoncy"] = optimal_cowoncy
                data["channel_id"] = ctx.channel.id
                SaveHbDataGhoStys(data)
                
                await made_by_ghosty.sleep(2)
                await ctx.send(f"owo hb {optimal_cowoncy}")
                await made_by_ghosty.sleep(4)
                return await CheckGhoStyHbMsgFetch(ctx, optimal_cowoncy)

            if "i will be back in" in msg_content_lower:
                match = re.search(r"i will be back in (\d+h\s*\d*m?|\d+m)", msg_content_lower)
                if match:
                    time_str = match.group(1).strip()
                    delta = ParseGhoStyTimeStrs(time_str)
                    next_time = datetime.now() + delta
                    
                    data = LoadGhoStysHbData()
                    data.update({
                        "next_huntbot_time": next_time.isoformat(),
                        "is_hunting": True,
                        "last_updated": datetime.now().isoformat(),
                        "channel_id": ctx.channel.id
                    })
                    SaveHbDataGhoStys(data)
                    
                    GhoStyHbAlrActiveVar = True
                    print(f"⏰ Next huntbot in {delta} (at {next_time.strftime('%H:%M:%S')})")
                    await ctx.send(f" ⏰ HuntBot will trigger in {delta}")
                    return True

            if "here is your password!" in msg_content_lower and msg.attachments:
                url = msg.attachments[0].url
                print(f"🔍 Solving captcha from {url}")
                result = await GhoStyCapUrlSolver(url)

                if result:
                    use_cowoncy = cowoncy_amount or LoadGhoStysHbData().get("optimal_cowoncy", 20000)
                    await made_by_ghosty.sleep(2)
                    await ctx.send(f"owo autohunt {use_cowoncy} {result}")
                    print(f"✅ Auto-solved HuntBot: `{result}` (Used {use_cowoncy})")
                    
                    await made_by_ghosty.sleep(4)
                    return await CheckGhoStyHbMsgFetch(ctx, use_cowoncy)
                else:
                    await ctx.send(" ❌ GhoSty Core Module failed to solve HuntBot. Please join the support server to get help.")
                    return False

            if ("you spent" in msg_content_lower and "cowoncy" in msg_content_lower and 
                "i will be back in" in msg_content_lower):
                match = re.search(r"i will be back in (\d+h\s*\d*m?|\d+m)", msg_content_lower)
                if match:
                    time_str = match.group(1).strip()
                    delta = ParseGhoStyTimeStrs(time_str)
                    next_time = datetime.now() + delta
                    
                    data = LoadGhoStysHbData()
                    data.update({
                        "next_huntbot_time": next_time.isoformat(),
                        "is_hunting": True,
                        "last_updated": datetime.now().isoformat(),
                        "channel_id": ctx.channel.id,
                        "hunt_stage": "waiting_for_return" 
                    })
                    SaveHbDataGhoStys(data)
                    
                    GhoStyHbAlrActiveVar = True
                    print(f"🎯 Hunt started Will return in {delta} (at {next_time.strftime('%H:%M:%S')})")
                    await ctx.send(f"🎯 Hunt active Bot will return in {delta}")
                    return True

            if "i am back with" in msg_content_lower and "animals" in msg_content_lower:
                print(f"🎉 Hunt completed! Bot is back with animals")
                await ctx.send("🎉 Hunt completed! Restarting HuntBot in 15 seconds")
                await made_by_ghosty.sleep(15)
                
                await ctx.send("owo hb")
                print(f"📤 Sent: owo hb (after hunt return)")
                await made_by_ghosty.sleep(4)
                return await CheckGhoStyHbMsgFetch(ctx)

        return False
    except Exception as e:
        print(f"⚠️ Error in CheckGhoStyHbMsgFetch: {e}")
        return False

@ghosty.command(aliases=["h"])
async def help(ctx):
    ghosty_help = """
    # 🤑 GhoSty OwO Farm V4.0.2 🤑 
Prefix: `.`

**__Main__**
 🌟 Start: *Starts The AutoBot*
 🛑 Stop: *Stops The AutoBot*
 🔍 Status: *Shows Bot Status*
 ⚡ Speed: *Change speed mode (efficient/fast/durable)*

**__Features__**
 ⚠ Ban Bypass
 🚨 Auto Detects OwO Warnings
 ⏱ Auto Cut After 1 Warning
 💎 Auto Use Gems 
 🦁 Zoo Value Tracking & Profit Calculator
 🏹 Fast And Secure
 🛏️ Smart Dynamic Auto Sleep
 🎯 Auto HuntBot Integration with Auto Solver

**__Made with 💖 and 🧠 by GhoSty | [Async Development]__** 
"""
    await ctx.send(ghosty_help)  

@ghosty.command()
async def speed(ctx, mode: str = None):
    global current_speed_mode, last_mode_change_time
    
    if mode is None:
        current_config = SPEED_MODES[current_speed_mode]
        await ctx.send(f"Current speed mode: **{current_config['name']}**\n\nAvailable modes: `efficient`, `fast (Not Recommended, Don't Use)`, `durable (Recommended)`")
        return
    
    mode = mode.lower()
    
    if mode not in SPEED_MODES:
        await ctx.send("❌ Invalid speed mode. Available modes: `efficient`, `fast (Not Recommended, Don't Use)`, `durable (Recommended)`")
        return
    
    current_speed_mode = mode
    last_mode_change_time = datetime.now()
    current_config = SPEED_MODES[current_speed_mode]
    
    await ctx.send(f"✅ Speed mode changed to: **{current_config['name']}**")

async def do_gem_check(ctx):
    global ghosty_gems_used 
    if sleep_mode:
        return
    
    await ctx.send("owo inventory")
    
    current_config = SPEED_MODES[current_speed_mode]
    await made_by_ghosty.sleep(3)  
    
    try:
        latest_messages = await ctx.channel.history(limit=2).flatten()
        
        for message in latest_messages:
            if message.author.id == 408785106942164992:  
                if "inventory" in message.content.lower():
                    gem_numbers = await parse_gems(message.content)
                    if gem_numbers: 
                        use_command = "owo use " + " ".join(gem_numbers)
                        await ctx.send("owo lb all")
                        await ctx.send(use_command)
                        ghosty_gems_used += len(gem_numbers)
                        await made_by_ghosty.sleep(3)
                    else:
                        print("No gems found")
                    break
    except Exception as e:
        print(f"Error in gem check: {e}")
        import traceback
        print(traceback.format_exc())

async def check_warning(ctx):
    global running
    if sleep_mode:
        return False

    try:
        messages = await ctx.channel.history(limit=10).flatten()

        for msg in messages:

            msg_content = str(msg.content)
            if not msg_content:
                continue
            msg_content_clean = unicodedata.normalize("NFKC", msg_content)
            msg_content_clean = re.sub(r'[\u200B-\u200D\uFEFF]', '', msg_content_clean)
            msg_content_lower = msg_content_clean.lower()

            if "captcha" in msg_content_lower and "verify" in msg_content_lower:
                warning_pattern = r'[\(\[\{]?\s*(\d+)\s*[\/／]\s*5\s*[\)\]\}]?'
                match = re.search(warning_pattern, msg_content_lower)

                if match:
                    warning_count = int(match.group(1))
                    print(f"⚠️ CAPTCHA WARNING DETECTED: ({warning_count}/5)")

                    if warning_count == 1:
                        running = False
                        await ctx.send(
                            "⚠ WARNING DETECTED! 🛑 Stopping | **SOLVE YOUR CAPTCHA FIRST** | "
                            "Then Type `.start` again to restart grinding."
                        )
                        print("⚠ Stopped due to CAPTCHA (1/5)")
                        return True

        return False

    except Exception as e:
        print(f"Warning check error: {e}")
        return False


async def monitor_huntbot(ctx):
    global GhoStyHbAlrActiveVar
    
    while running:
        try:
            data = LoadGhoStysHbData()
            if "next_huntbot_time" in data and data.get("channel_id") == ctx.channel.id:
                next_time_str = data["next_huntbot_time"]
                next_time = datetime.fromisoformat(next_time_str)
                current_time = datetime.now()

                if current_time >= next_time and data.get("is_hunting"):
                    print(f"⏰ HuntBot timer reached! Triggering HuntBot...")
                    await ctx.send("⏰ HuntBot timer reached! Restarting...")
                    data["is_hunting"] = False
                    SaveHbDataGhoStys(data)
                    GhoStyHbAlrActiveVar = False
                    await made_by_ghosty.sleep(2)
                    await ctx.send("owo hb")
                    print(f"📤 Sent: owo hb (auto-triggered by timer)")
                    await made_by_ghosty.sleep(4)
                    await CheckGhoStyHbMsgFetch(ctx)

            await made_by_ghosty.sleep(30)
            
        except Exception as e:
            print(f"⚠️ Error in monitor_huntbot: {e}")
            await made_by_ghosty.sleep(60)


@ghosty.command()
async def start(ctx):
    global running, last_gem_check, ghosty_commands_sent, has_started
    global initial_cash, initial_essence, zoo_channel, sleep_mode, sleep_start_time
    global last_mode_change_time, ghosty_start_time, farming_start_time
    
    if running and has_started:
        await ctx.send("⚠️ **GhoSty OwO Worker is already running!**\n\n🛑 Please use `.stop` first, then `.start` to restart/force fix the worker.\nJoin the support server for better guidance.")
        return
    
    running = True
    sleep_mode = False
    has_started = True
    zoo_channel = ctx.channel
    last_gem_check = time.time()
    last_command = None
    sleep_start_time = None
    farming_start_time = datetime.now()
    last_mode_change_time = datetime.now()
    
    current_config = SPEED_MODES[current_speed_mode]
    zoo_data = await fetch_zoo_data(ctx)
    
    if zoo_data:
        initial_cash = zoo_data['total_cash']
        initial_essence = zoo_data['total_essence']

    await made_by_ghosty.sleep(2)
    data = LoadGhoStysHbData()
    data["channel_id"] = ctx.channel.id
    SaveHbDataGhoStys(data)
    await ctx.send("owo hb")
    await made_by_ghosty.sleep(4)
    await CheckGhoStyHbMsgFetch(ctx)
    
    ghosty.loop.create_task(monitor_huntbot(ctx))
    
    await made_by_ghosty.sleep(2)

    while running:
        try:
            
            if has_started and running and not sleep_mode:
                current_time = datetime.now()
                
                active_mode = current_speed_mode
                max_run_time = (current_time - last_mode_change_time).total_seconds()
                
                current_config = SPEED_MODES[active_mode]
                elapsed_time = (current_time - farming_start_time).total_seconds()
                
                max_run_time = ghostyjija.uniform(
                    current_config['run_duration_min'],
                    current_config['run_duration_max']
                )
                
                if elapsed_time >= max_run_time:
                    sleep_mode = True
                    sleep_duration = ghostyjija.uniform(
                        current_config['sleep_duration_min'],
                        current_config['sleep_duration_max']
                    )
                    sleep_start_time = current_time
                    sleep_end_time = current_time + timedelta(seconds=sleep_duration)
                    
                    await ctx.send(f"😴 Entering sleep mode. Will resume at **{sleep_end_time.strftime('%d-%b-%Y %I:%M:%S %p')}**")
                    print(f"Sleep mode started. Will resume at {sleep_end_time.strftime('%d-%b-%Y %I:%M:%S %p')}")
                    
                    await made_by_ghosty.sleep(sleep_duration)
                    
                    sleep_mode = False
                    farming_start_time = datetime.now()
                    last_mode_change_time = datetime.now()
                    await ctx.send("⏰ Waking up from sleep. Resuming")
                    print("⏰ Waking up from sleep. Resuming")
                    continue

            if sleep_mode:
                await made_by_ghosty.sleep(10)
                continue

            current_time = time.time()
            current_config = SPEED_MODES[current_speed_mode]
            
            gem_check_interval = ghostyjija.randint(
                int(current_config['gem_check_interval_min']), 
                int(current_config['gem_check_interval_max'])
            )
            
            if current_time - last_gem_check >= gem_check_interval:
                warning_detected = await check_warning(ctx)
                if warning_detected or not running:
                    break
                await do_gem_check(ctx)
                last_gem_check = current_time
                continue

            def ghostysmarttypo(command):
                if ghostyjija.random() < 0.12:
                    idx = ghostyjija.randint(0, len(command)-1)
                    ghostytypochars = ghostyjija.choice('abcdefghijklmnopqrstuvwxyz')
                    return command[:idx] + ghostytypochars + command[idx+1:]
                return command

            commands = [
                ghostysmarttypo("owoh"), ghostysmarttypo("owo pray"), ghostysmarttypo("owo h"), ghostysmarttypo("owo b"), ghostysmarttypo("owob"),
                ghostysmarttypo("owoh"), ghostysmarttypo("owo h"),
                ghostysmarttypo(ghostyjija.choice(["owo cf 1", "owoz", "owo s 2", "owo owo", "owoq"])),
                ghostysmarttypo(ghostyjija.choice(["owo pup", "owo army", "owo piku", "owo run"])),
                ghostysmarttypo(ghostyjija.choice(["owo punch <@408785106942164992>", "owo roll"]))
            ]
            command = ghostyjija.choice(commands)

            while command == last_command:
                command = ghostyjija.choice(commands)
            last_command = command

            await ctx.send(command)
            ghosty_commands_sent += 1

            await made_by_ghosty.sleep(current_config['command_delay'])
            warning_detected = await check_warning(ctx)
            if warning_detected or not running:
                break

            await made_by_ghosty.sleep(ghostyjija.uniform(
                current_config['action_delay_min'], 
                current_config['action_delay_max']
            ))
            if ghostyjija.random() < 0.05:
                await made_by_ghosty.sleep(ghostyjija.uniform(
                    current_config['random_long_delay_min'], 
                    current_config['random_long_delay_max']
                ))

        except Exception as e:
            print(f"Error in main loop: {e}")


@ghosty.command()  
async def stop(ctx):
    global running, has_started, sleep_mode
    await ctx.send(
        "🛑 Stopping | Type .start again to re-start grinding"
    )  
    running = False
    has_started = False
    sleep_mode = False


@ghosty.command()
async def status(ctx):
    global ghosty_start_time, ghosty_commands_sent, ghosty_gems_used, last_gem_check, has_started
    global initial_cash, initial_essence, current_cash, current_essence, zoo_channel, current_speed_mode
    global sleep_mode, sleep_start_time
    
    current_config = SPEED_MODES[current_speed_mode]
    
    if sleep_mode:
        ghosty_state = f"😴 Sleeping ({current_config['name']})"
        if sleep_start_time:
            sleep_elapsed = datetime.now() - sleep_start_time
            hrs, rem = divmod(int(sleep_elapsed.total_seconds()), 3600)
            mins, secs = divmod(rem, 60)
            ghosty_state += f" | Slept: {hrs}h {mins}m {secs}s"
    elif has_started and running:
        ghosty_state = f"🟢 Running ({current_config['name']})"
    else:
        ghosty_state = f"⚫ Not Running ({current_config['name']})"
    
    ghosty_uptime = datetime.now() - ghosty_start_time
    hrs, rem = divmod(int(ghosty_uptime.total_seconds()), 3600)
    mins, secs = divmod(rem, 60)

    profit_text = ""
    if has_started and zoo_channel and not sleep_mode:
        await ctx.send("🔍 Fetching current zoo data for profit calculation...")
        
        await zoo_channel.send("owo zoo")
        await made_by_ghosty.sleep(3)
        
        try:
            messages = await zoo_channel.history(limit=10).flatten()
            zoo_messages = []
            
            for msg in messages:
                if msg.author.id == 408785106942164992:
                    if any(keyword in msg.content.lower() for keyword in ['zoo', 'animals', 'cowoncy']):
                        zoo_messages.append(msg.content)
            
            if zoo_messages:
                zoo_data = await parse_zoo_message(zoo_messages)
                current_cash = zoo_data['total_cash']
                current_essence = zoo_data['total_essence']
                
                cash_profit = current_cash - initial_cash
                essence_profit = current_essence - initial_essence
                
                profit_text = f"\n\n💰 **Profit Since Start:**\n> 💵 Cash: {format_value(cash_profit)} ({format_value(initial_cash)} → {format_value(current_cash)})\n> ✨ Essence: {format_value(essence_profit)} ({format_value(initial_essence)} → {format_value(current_essence)})"
        except Exception as e:
            print(f"Error fetching status zoo data: {e}\n\nJoin the support server for help.")
            profit_text = "\n\n⚠ Could not fetch current zoo data\nJoin the support server for help."

    gstatusghosty = f"""
🔍 **GhoSty OwO Status:** {ghosty_state}

> 🕒 **Running Since:** {ghosty_start_time.strftime('%d-%b-%Y %I:%M:%S %p')}
> 📈 **Uptime:** {hrs}h {mins}m {secs}s
> 📊 **Commands Sent:** {ghosty_commands_sent}
> 💎 **Gems Potentially Used:** {ghosty_gems_used}
> ⚡ **Speed Mode:** {current_config['name']}
> 🛏️ **Sleeping?:** {"Yes" if sleep_mode else "No"}
> 🎯 **HuntBot Active?:** {"Yes" if GhoStyHbAlrActiveVar else "No"}
> 🧠 **HuntBot Solver:** {"Available" if GhoStyCoreAvailCheck else "Not Available"}
> ♻️ **Last Gem Check:** {'<t:' + str(int(last_gem_check)) + ':R>' if last_gem_check else 'Never'}{profit_text}
"""
    await ctx.send(gstatusghosty)