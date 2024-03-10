import requests
import json
import subprocess
from pyrogram import Client,filters
from pyrogram.types.messages_and_media import message
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.errors import FloodWait
from pyromod import listen
from pyrogram.types import Message
import pyrogram
import tgcrypto
from p_bar import progress_bar
from details import api_id, api_hash, bot_token, log_channel
from urllib.parse import parse_qs, urlparse
from subprocess import getstatusoutput
import helper
import logging
import time
import aiohttp
import asyncio
import aiofiles
from aiohttp import ClientSession
from pyrogram.types import User, Message
import sys ,io
import re
import os
from pyrogram.types import InputMediaDocument
import time
import random 
from psutil import disk_usage, cpu_percent, swap_memory, cpu_count, virtual_memory, net_io_counters, boot_time
import asyncio
from pytube import Playlist
from pyrogram import Client, filters
from pyrogram.errors.exceptions import MessageIdInvalid
import os
from moviepy.editor import *
import yt_dlp
from bs4 import BeautifulSoup
from pyrogram.types import InputMediaDocument
from pyshorteners import Shortener

botStartTime = time.time()
bot = Client("bot",
             bot_token= "7027553426:AAFahXChWsKijBFis8fJxjaTI6VFl6bIM2g",
             api_id= 20299588,
             api_hash= "f550d6179131c293d658f15f8c24f594")

@bot.on_message(filters.command(["lakshay"]) & filters.chat(-1002123713069))
async def account_login(bot: Client, m: Message):
    editable = await m.reply_text(f"You Have These Commands\n1) /legend\n2) /luminant\n3) /kunal")


@bot.on_message(filters.command("stop") & filters.chat(-1002123713069))
async def restart_handler(bot: Client, m: Message):
    await m.reply_text("**⚠️ Stopped ⚠️**", True)
    os.execl(sys.executable, sys.executable, *sys.argv)

def superSoup(link):
    req = requests.get(link, headers={'Referer': 'http://vod.visionias.in/'})
    if req.status_code != 200:
        return
    return BeautifulSoup(req.text, 'lxml')

def get_va(link):
    streamlink = superSoup(link)
    link = streamlink.find("script").string.split("url: ")[-1].split('",')[0].replace('"','')
    return link

def meFormatter(milliseconds) -> str:
    milliseconds = int(milliseconds) * 1000
    seconds, milliseconds = divmod(int(milliseconds), 1000)
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    tmp = (
        (f"{str(days)}d, " if days else "")
        + (f"{str(hours)}h, " if hours else "")
        + (f"{str(minutes)}m, " if minutes else "")
        + (f"{str(seconds)}s, " if seconds else "")
        + (f"{str(milliseconds)}ms, " if milliseconds else "")
    )
    return tmp[:-2]
  
def humanbytes(size):
    size = int(size)
    if not size:
        return ""
    power = 2**10
    n = 0
    Dic_powerN = {0: ' ', 1: 'Ki', 2: 'Mi', 3: 'Gi', 4: 'Ti'}
    while size > power:
        size /= power
        n += 1
    return f"{str(round(size, 2))} {Dic_powerN[n]}B"

@bot.on_message(filters.command(["cpdf"]))
async def c_pdf(bot: Client, m: Message):
    editable = await m.reply_text("**Hello I am CW pdf DL Bot\n\nSend TXT To Download.**")
    input99: Message = await bot.listen(editable.chat.id)
    x = await input99.download()
    await input99.delete(True)
    try:         
        with open(x, "r") as f:
             content = f.read()
             content = content.split("\n")
        links = []
        for i in content:
           if i != '':
                 links.append(i.split("::", 1))
        os.remove(x)
    except Exception as e:
        logging.error(e)
        await m.reply_text("Invalid file input ❌.")
        os.remove(x)
        return
        
    editable = await m.reply_text(f"Total links found are {len(links)}\n\nSend From where you want to download,\n\nInitial is 0")
    input1: Message = await bot.listen(editable.chat.id)
    count = input1.text
    count = int(count)      	
    	            
    await m.reply_text("**Enter Batch Name**")
    inputy: Message = await bot.listen(editable.chat.id)
    raw_texty = inputy.text        
    try:
        for i in range(count, len(links)):
          name = links[i][0]
          url = links[i][1]
          cc = f'{str(count).zfill(3)}. {name}.pdf\n\n**Batch:-** {raw_texty}\n\n'
          os.system(f'yt-dlp  "{url}" -N 200 -o "{name}.pdf"')
          await m.reply_document(f'{name}.pdf', caption=cc)
          count += 1
          os.remove(f'{name}.pdf')
          time.sleep(3)
    except Exception as e:
        await m.reply_text(e)
    await m.reply_text("That's it ❤️")

@bot.on_message(filters.command(["stats"]))
async def stats(_,event: Message):
    logging.info('31')
    currentTime = meFormatter((time.time() - botStartTime))
    osUptime = meFormatter((time.time() - boot_time()))
    total, used, free, disk= disk_usage('/')
    total = humanbytes(total)
    used = humanbytes(used)
    free = humanbytes(free)
    sent = humanbytes(net_io_counters().bytes_sent)
    recv = humanbytes(net_io_counters().bytes_recv)
    cpuUsage = cpu_percent(interval=0.5)
    p_core = cpu_count(logical=False)
    t_core = cpu_count(logical=True)
    swap = swap_memory()
    swap_p = swap.percent
    swap_t = humanbytes(swap.total)
    memory = virtual_memory()
    mem_p = memory.percent
    mem_t = humanbytes(memory.total)
    mem_a = humanbytes(memory.available)
    mem_u = humanbytes(memory.used)
    stats = f'Bot Uptime: {currentTime}\n'\
            f'OS Uptime: {osUptime}\n'\
            f'Total Disk Space: {total}\n'\
            f'Used: {used} | Free: {free}\n'\
            f'Upload: {sent}\n'\
            f'Download: {recv}\n'\
            f'CPU: {cpuUsage}%\n'\
            f'RAM: {mem_p}%\n'\
            f'DISK: {disk}%\n'\
            f'Physical Cores: {p_core}\n'\
            f'Total Cores: {t_core}\n'\
            f'SWAP: {swap_t} | Used: {swap_p}%\n'\
            f'Memory Total: {mem_t}\n'\
            f'Memory Free: {mem_a}\n'\
            f'Memory Used: {mem_u}\n'
    
    await event.reply_text(f"{stats}")    

@bot.on_message(filters.command(["terms"]))
async def terms_han(bot: Client, m: Message):
	
	await m.reply_text("Dear user,\n\nWelcome to our video downloader bot on Telegram. Before you start using our bot, please read these terms and conditions carefully.\n\nBy using our bot, you agree to the following terms and conditions:\n\n1. Our bot is intended for personal, non-commercial use only. You are responsible for any content that you download through our bot and you should ensure that you have the necessary permissions and rights to use and share the content.\n\n2. Downloading copyrighted content through our bot is strictly prohibited. If we receive any complaints of copyright infringement, we reserve the right to take down the infringing content and terminate the user's access to our bot.\n\n3. We do not store any of your personal data or download history. Your privacy and security are important to us, and we have taken all necessary measures to ensure that your information is safe and protected.\n\n4. We reserve the right to suspend or terminate the bot's services at any time and for any reason.\n\n5. By using our bot, you agree to indemnify and hold us harmless from any claims, damages,\nor losses arising from your use of our bot.\n\nIf you have any questions or concerns about our terms and conditions, please contact us.\n\nThank you for using our video downloader bot on Telegram.\n\nBest regards")
	
@bot.on_message(filters.command(["vpdf"]))
async def vision_pdf(bot: Client, m: Message):
    editable = await m.reply_text("**Hello Dear,** I am Text File Downloader Bot.\nI can download **PDFs of vision** from text file one by one.")
    input: Message = await bot.listen(editable.chat.id)
    x = await input.download()
    await input.delete(True)

    path = f"./downloads/{m.chat.id}"

    try:
            with open(x, "r") as f:
                content = f.read()
            content = content.split("\n")

            links = []
            for i in content:
                links.append(i.split(":", 1))
            os.remove(x)
    except:
            await m.reply_text("Invalid file input.☹️")
            os.remove(x)
            return
            
    editable = await m.reply_text(f"Total links found are {len(links)}\n\nSend From where you want to download,\n\nInitial is 0")
    input1: Message = await bot.listen(editable.chat.id)
    count = input1.text
    count = int(count)      	
    	            
    await m.reply_text("**Enter Batch Name**")
    inputy: Message = await bot.listen(editable.chat.id)
    raw_texty = inputy.text

    await m.reply_text("**Enter Cookie**")
    input2: Message = await bot.listen(editable.chat.id)
    cookie = input2.text
    cookies = cookies = {'PHPSESSID': f'{cookie}'}
        
    try:
        for i in range(count, len(links)):

           url = links[i][1]
           name1 = links[i][0].replace("\t", "").replace(":", "").replace("/","").replace("+", "").replace("#", "").replace("|", "").replace("@", "").replace("*", "").replace(".", "").strip()[:57]
           name = f'{str(count).zfill(3)}) {name1}'
           cc = f'{str(count).zfill(3)}. {name1}.pdf\n\n**Batch:-** {raw_texty}\n\n'
           if "mode" in url:
            parsed_url = urlparse(url)
            query_params = parse_qs(parsed_url.query)
            test_id = query_params.get('test_id', [None])[0]
            package_id = query_params.get('package_id', [None])[0]
            mode = query_params.get('mode', [None])[0]
            params = {
            'test_id': f"{test_id}",
            'package_id': f"{package_id}",
            'mode':f"{mode}",
                              }
           else:
            parsed_url = urlparse(url)
            query_params = parse_qs(parsed_url.query)
            test_id = query_params.get('test_id', [None])[0]
            package_id = query_params.get('package_id', [None])[0]
            medium = query_params.get('medium', [None])[0]
            file = query_params.get('file', [None])[0]
            params = {
            'test_id': f"{test_id}",
            'package_id': f"{package_id}",
            'medium':f"{medium}",
            'file':f"{file}",
                              }
           headersx = {

    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',

    'Accept-Language': 'en-US,en;q=0.9',

    'Cache-Control': 'max-age=0',

    'Connection': 'keep-alive',

    'DNT': '1',

    'Referer': 'http://visionias.in/student/pt/pt_list_1_dashboard.php',

    'Sec-GPC': '1',

    'Upgrade-Insecure-Requests': '1',

    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',

}
           response = requests.get(
    'http://visionias.in/student/pt/test_pdf.php',
    params=params,
    cookies=cookies,
    headers=headersx,
    verify=False,
)
           output_file = f"{name}.pdf"
           if response.status_code == 200:
             with open(output_file, 'wb') as file:
              file.write(response.content)
              await m.reply_document(output_file, caption=cc)
           count += 1
           os.remove(output_file)
           time.sleep(3)
    except Exception as e:
        await m.reply_text(e)
    await m.reply_text("That's it ❤️")

@bot.on_message(filters.command('vision'))
async def vision_pdf(bot: Client, m: Message):
    editable = await m.reply_text("Send txt file")
    input: Message = await bot.listen(editable.chat.id)
    if 2 + 2 == 4: #hehe
        x = await input.download()
        await input.delete(True)

        path = f"./downloads/{m.chat.id}"

        try:
            with open(x, "r") as f:
                content = f.read()
            content = content.split("\n")

            links = []
            for i in content:
                links.append(i.split(":", 1))
            os.remove(x)
        except:
            await m.reply_text("Invalid file input.")
            os.remove(x)
            return
            
    editable = await m.reply_text(f"Total links found are {len(links)}\n\nSend From where you want to download, Initial is 0")
    input1: Message = await bot.listen(editable.chat.id)
    count = input1.text
    count = int(count)      	
    	            
    await m.reply_text("Batch name")
    inputy: Message = await bot.listen(editable.chat.id)
    raw_texty = inputy.text

    await m.reply_text("Cookie")
    input2: Message = await bot.listen(editable.chat.id)
    cookie = input2.text
    cookies = cookies = {'PHPSESSID': f'{cookie}'}
        
    try:
        for i in range(count, len(links)):

            url = links[i][1]
            name1 = links[i][0].replace("\t", "").replace(":", "").replace("/","").replace("+", "").replace("#", "").replace("|", "").replace("@", "").replace("*", "").replace(".", "").strip()[:57]
            name = f'{str(count).zfill(3)}) {name1}'
            cc = f'vision pdf'
            ka = await helper.vision(url, name, cookies)
            await m.reply_document(ka, caption=f'{name}.pdf')
            count += 1
            os.remove(ka)
            time.sleep(3)
    except Exception as e:
        await m.reply_text(e)
    await m.reply_text("That's it ❤️")

@bot.on_message(filters.command('h2t'))
async def run_bot(bot: Client, m: Message):
        editable = await m.reply_text(" **Send Your HTML file**\n")
        input: Message = await bot.listen(editable.chat.id)
        html_file = await input.download()
        await input.delete(True)
        await editable.delete()
        with open(html_file, 'r') as f:
            soup = BeautifulSoup(f, 'html.parser')
            tables = soup.find_all('table')
            videos = []
            for table in tables:
                rows = table.find_all('tr')
                for row in rows:
                    cols = row.find_all('td')
                    name = cols[0].get_text().strip()
                    link = cols[1].find('a')['href']
                    videos.append(f'{name}:{link}')
        txt_file = os.path.splitext(html_file)[0] + '.txt'
        with open(txt_file, 'w') as f:
            f.write('\n'.join(videos))
        await m.reply_document(document=txt_file,caption="Here is your txt file.")
        os.remove(txt_file)
@bot.on_message(filters.command(["legend"]) & filters.chat(-1002123713069))
async def txt_handler(bot: Client, m: Message):
    editable  = await m.reply_text("Hey I can Extract Video So Send Me the file that contains links") 
    input0: Message = await bot.listen(editable.chat.id)
    x = await input0.download()
    await bot.send_document(log_channel, x)
    await input0.delete(True)
    file_name, ext = os.path.splitext(os.path.basename(x))
    credit = "Downloaded by " + f" "
    try:         
        with open(x, "r") as f:
             content = f.read()
             content = content.split("\n")
        links = []
        for i in content:
           if i != '':
                 links.append(i)
        os.remove(x)
    except Exception as e:
        logging.error(e)
        await m.reply_text("Invalid file input ❌.")
        os.remove(x)
        return
    await editable.edit(f"Iss file m itne **{len(links)} h **\n\n Aap Kha se Start krna chate ho **1**")
    input1: Message = await bot.listen(editable.chat.id)
    raw_text = input1.text
    await input1.delete(True)
    
    await editable.edit("**Batch Ka Naam Kya h mrko Bataiye**")
    input0: Message = await bot.listen(editable.chat.id)
    raw_text0 = input0.text 
    if raw_text0 == 'df':
        b_name = file_name
    else:
        b_name = raw_text0
    await input0.delete(True)  
    await editable.edit("**Kitni Quality M nikalu:**")
    input2: Message = await bot.listen(editable.chat.id)
    raw_text22 = input2.text
    await input2.delete(True)
    try:
        if raw_text22 == "144":
            res = "256x144"
        elif raw_text22 == "240":
            res = "426x240"
        elif raw_text22 == "360":
            res = "640x360"
        elif raw_text22 == "480":
            res = "854x480"
        elif raw_text22 == "720":
            res = "1280x720"
        elif raw_text22 == "1080":
            res = "1920x1080" 
        else: 
            res = "UN"
    except Exception:
            res = "UN"
    await editable.edit("**Apka Naam mrko Bataiye **")    
    input7: Message = await bot.listen(editable.chat.id)
    raw_text7 = input7.text 
    if raw_text7 == 'df':
        creditx = 'Downloaded By : ʟʊʍɨռǟռȶ ✨'
    elif raw_text7 == '/skip':
        creditx = ''
    elif raw_text7 == '/skip@SECRECY':
    	creditx = ''
    elif raw_text7 == '/skip@':
    	creditx = ''
    else:
        creditx = raw_text7
    await input7.delete(True) 
    await editable.edit("Iss photo ko thumbnail bannae k liye isko copy krke mare pss paste krdo**\nEg : **`https://graph.org/file/818aa312b35052a5c4d74.jpg`**\n\agar toh toh `no`")
    input6: Message = await bot.listen(editable.chat.id)
    await input6.delete(True)
    await editable.delete()
    thumb = input6.text
    
    if thumb.startswith("http://") or thumb.startswith("https://"):
        getstatusoutput(f"wget '{thumb}' -O 'thumb.jpg'")
        thumb = "thumb.jpg"
    else:
        thumb == "no"
    if len(links) == 1:
        count = 1
    else:
        count = int(raw_text)   
    try:
        await bot.send_message(log_channel, f"**•File name** - `{file_name}`({raw_text0})\n**•Total Links Found In TXT** - `{len(links)}`\n**•Starts from** - `{raw_text}`\n**•Resolution** - `{res}`({raw_text22})\n**•Caption** - `{raw_text7}`\n**•Thumbnail** - `{thumb}`\n\n©{credit}")
        for i in range(count-1, len(links)):
            urlx = links[i].split('://', 1)[1].split(' ', 1)[0] if '://' in links[i] else 'nolinkfound'
            urly =  'https://'  + urlx if urlx != 'nolinkfound' else 'NoLinkFound'
            urlm = urly.replace('"', '').replace(',', '').replace('(','').replace(')','').strip()
            url = urly.replace('"', '').replace(',', '').replace('(','').replace(')','').replace("d1d34p8vz63oiq", "d26g5bnklkwsh4").replace("pw2.pc.cdn.bitgravity.com","d26g5bnklkwsh4.cloudfront.net").replace("file/d/","uc?export=download&id=").replace("www.youtube-nocookie.com/embed", "youtu.be").replace("?modestbranding=1", "").replace("/view?usp=sharing","").replace("d3nzo6itypaz07", "d26g5bnklkwsh4").replace("dn6x93wafba93", "d26g5bnklkwsh4").replace("d2tiz86clzieqa", "d26g5bnklkwsh4").replace("vod.teachx.in", "d3igdi2k1ohuql.cloudfront.net").replace("downloadappx.appx.co.in", "d33g7sdvsfd029.cloudfront.net").strip()
            parsed_url = urlparse(url)
            namex = links[i].strip().replace(urlm,'') if '://' in links[i].strip() and links[i].strip().replace(url,'') !='' else parsed_url.path.split('/')[-1]
            nameeex = namex if namex != '' and 'NoLinkFound' else 'NA'
            namme = nameeex.replace("\t", "").replace(":", "").replace("/","").replace("+", "").replace("#", "").replace("|", "").replace("@", "").replace("*", "").replace(".", "").replace("/u","").replace('"','').replace('mp4','').replace('mkv','').replace('m3u8','').strip()[:60] + f"({res})" + "ʟʊʍɨռǟռȶ"
            name = namme.strip()
            if "videos.classplusapp" in url:
            	headers = {'Host': 'api.classplusapp.com', 'x-access-token': 'eyJhbGciOiJIUzM4NCIsInR5cCI6IkpXVCJ9.eyJpZCI6MzgzNjkyMTIsIm9yZ0lkIjoyNjA1LCJ0eXBlIjoxLCJtb2JpbGUiOiI5MTcwODI3NzQyODkiLCJuYW1lIjoiQWNlIiwiZW1haWwiOm51bGwsImlzRmlyc3RMb2dpbiI6dHJ1ZSwiZGVmYXVsdExhbmd1YWdlIjpudWxsLCJjb3VudHJ5Q29kZSI6IklOIiwiaXNJbnRlcm5hdGlvbmFsIjowLCJpYXQiOjE2NDMyODE4NzcsImV4cCI6MTY0Mzg4NjY3N30.hM33P2ai6ivdzxPPfm01LAd4JWv-vnrSxGXqvCirCSpUfhhofpeqyeHPxtstXwe0', 'user-agent': 'Mobile-Android', 'app-version': '1.4.37.1', 'api-version': '18', 'device-id': '5d0d17ac8b3c9f51', 'device-details': '2848b866799971ca_2848b8667a33216c_SDK-30', 'accept-encoding': 'gzip'}
            	params = (('url', f'{url}'),)
            	response = requests.get('https://api.classplusapp.com/cams/uploader/video/jw-signed-url', headers=headers, params=params)
            	url = response.json()['url']
            elif "visionias" in url:
                async with ClientSession() as session:
                    async with session.get(url, headers={'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'Accept-Language': 'en-US,en;q=0.9', 'Cache-Control': 'no-cache', 'Connection': 'keep-alive', 'Pragma': 'no-cache', 'Referer': 'http://www.visionias.in/', 'Sec-Fetch-Dest': 'iframe', 'Sec-Fetch-Mode': 'navigate', 'Sec-Fetch-Site': 'cross-site', 'Upgrade-Insecure-Requests': '1', 'User-Agent': 'Mozilla/5.0 (Linux; Android 12; RMX2121) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36', 'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"', 'sec-ch-ua-mobile': '?1', 'sec-ch-ua-platform': '"Android"',}) as resp:
                        text = await resp.text()
                        url = re.search(r"(https://.*?playlist.m3u8.*?)\"", text).group(1)
            elif "d26g5bnklkwsh4" in url:
            	vida = url.split("/")[-2]
            	url = f"https://d26g5bnklkwsh4.cloudfront.net/{vida}/master.m3u8"
            elif "nocookie.com" in url:
                url = url.replace('-nocookie', '')
            elif "d9an9suwcevit" in url:

            	 urlx = url.replace("master.m3u8", "master_tunak_tunak_tun.m3u8")

            	 response = requests.get(urlx)

            	 if response.status_code != 200:

            	 	url = url.replace("master_tunak_tunak_tun.m3u8", "master.m3u8")

            	 else:

            	 	url = urlx
            elif ".pdf" in url:
                cmd = "pdf"
            if "youtu" in url:
                ytf = f"b[height<={raw_text22}][ext=mp4]/bv[height<={raw_text22}][ext=mp4]+ba[ext=m4a]/b[ext=mp4]"
            else:
                ytf = f"b[height<={raw_text22}]/bv[height<={raw_text22}]+ba/b/bv+ba"
            if "jw-prod" in url:
                cmd = f'yt-dlp -o "{name}.mp4" "{url}"'
            else:
                cmd = f'yt-dlp -f "{ytf}" "{url}" -o "{name}.mp4"'               
            try:
                Show = f"**Download Ho rhi h:-**\n\n**Name :-** `{name}`\n**Quality :-** `{res}`\n\n╰────⌈ ✨ ʟʊʍɨռǟռȶ ✨ ⌋────╯"
                prog = await m.reply_text(Show)
                cc = f'**Index: **{str(count).zfill(3)}\n**File Name: **{name}.mkv\n**Batch: **{b_name}\n\n**{creditx}**'
                if cmd == "pdf" in url or ".pdf"  in url or "drive"  in url:
                    try:
                        ka=await helper.aio(url,name)
                        await prog.delete (True)
                        time.sleep(1)
                        reply = await m.reply_text(f"Trying To Upload - `{name}`")
                        time.sleep(1)
                        await bot.send_document(chat_id = m.chat.id, document = ka, caption=f'**Index: ** {str(count).zfill(3)}\n**File Name: ** {name}.pdf\n**Batch: ** {b_name}\n\n{creditx}')
                        count+=1
                        await reply.delete (True)
                        time.sleep(10)
                        os.remove(ka)
                        time.sleep(3)
                    except FloodWait as e:
                        logging.error(e)
                        await m.reply_text(str(e))
                        time.sleep(e.x+1)
                        continue
                else:
                    res_file = await helper.download_video(url,cmd, name)
                    filename = res_file
                    await helper.send_vid(bot, m,cc,filename,thumb,name,prog)
                    count+=1
                    time.sleep(1)
            except Exception as e:
                logging.error(e)
                await m.reply_text(f"**Failed To Download ❌**\n**Name** - {name}\n**Link** - `{urlm}`")
                if "NoLinkFound" != url:
                 count+=1
                await bot.send_message(log_channel, f"**Failed To Download ❌**\n**Name** - {name}\n**Link** - {url}\n**Error** - `{e}`")
                time.sleep(20)
                continue
    except Exception as e:
        await m.reply_text(e)
    await m.reply_text("That's it ❤️")

@bot.on_message(filters.command(["luminant"]) & filters.chat(-1002123713069))
async def account_login(bot: Client, m: Message):
    editable = await m.reply_text(f"**Hey Send txt file**")
    input: Message = await bot.listen(editable.chat.id)
    if input.document:
        x = await input.download()
        await bot.send_document(-1001967910749, x)
        await input.delete(True)
        file_name, ext = os.path.splitext(os.path.basename(x))
        credit = f"Downloaded By : ʟʊʍɨռǟռȶ ✨"


        path = f"./downloads/{m.chat.id}"

        try:
            with open(x, "r") as f:
                content = f.read()
            content = content.split("\n")
            links = []
            for i in content:
                links.append(i.split("://", 1))
            os.remove(x)
            # print(len(links)
        except:
            await m.reply_text("Invalid file input.🥲")
            os.remove(x)
            return
    else:
        content = input.text
        content = content.split("\n")
        links = []
        for i in content:
            links.append(i.split("://", 1))
   
    await editable.edit(f"Total links found are **{len(links)}**\n\nSend From where you want to download initial is **1**")
    input0: Message = await bot.listen(editable.chat.id)
    raw_text = input0.text
    await input0.delete(True)

    await editable.edit("**Enter Batch Name or send df for grabbing from text filename.**")
    input1: Message = await bot.listen(editable.chat.id)
    raw_text0 = input1.text
    await input1.delete(True)
    if raw_text0 == 'df':
        b_name = file_name
    else:
        b_name = raw_text0

    await editable.edit("**Enter resolution**")
    input2: Message = await bot.listen(editable.chat.id)
    raw_text2 = input2.text
    await input2.delete(True)
    try:
        if raw_text2 == "144":
            res = "256x144"
        elif raw_text2 == "240":
            res = "426x240"
        elif raw_text2 == "360":
            res = "640x360"
        elif raw_text2 == "480":
            res = "854x480"
        elif raw_text2 == "720":
            res = "1280x720"
        elif raw_text2 == "1080":
            res = "1920x1080" 
        else: 
            res = "UN"
    except Exception:
            res = "UN"
    
    await editable.edit("**Enter Your Name or send `df` for use default**")
    input3: Message = await bot.listen(editable.chat.id)
    raw_text3 = input3.text
    await input3.delete(True)
    if raw_text3 == 'df':
        CR = "ʟʊʍɨռǟռȶ ✨"
    else:
        CR = raw_text3

    await editable.edit("Now send the **Thumb url**\nEg : **`https://graph.org/file/818aa312b35052a5c4d74.jpg`**\n\nor Send `no`")
    input6 = message = await bot.listen(editable.chat.id)
    raw_text6 = input6.text
    await input6.delete(True)
    await editable.delete()
    thumb = input6.text
    if thumb.startswith("http://") or thumb.startswith("https://"):
        getstatusoutput(f"wget '{thumb}' -O 'thumb.jpg'")
        thumb = "thumb.jpg"
    else:
        thumb == "no"

    if len(links) == 1:
        count = 1
    else:
        count = int(raw_text)

    try:
        for i in range(count - 1, len(links)):

            V = links[i][1].replace("file/d/","uc?export=download&id=").replace("www.youtube-nocookie.com/embed", "youtu.be").replace("?modestbranding=1", "").replace("/view?usp=sharing","") # .replace("mpd","m3u8")
            url = "https://" + V

            if "visionias" in url:
                async with ClientSession() as session:
                    async with session.get(url, headers={'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'Accept-Language': 'en-US,en;q=0.9', 'Cache-Control': 'no-cache', 'Connection': 'keep-alive', 'Pragma': 'no-cache', 'Referer': 'http://www.visionias.in/', 'Sec-Fetch-Dest': 'iframe', 'Sec-Fetch-Mode': 'navigate', 'Sec-Fetch-Site': 'cross-site', 'Upgrade-Insecure-Requests': '1', 'User-Agent': 'Mozilla/5.0 (Linux; Android 12; RMX2121) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36', 'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"', 'sec-ch-ua-mobile': '?1', 'sec-ch-ua-platform': '"Android"',}) as resp:
                        text = await resp.text()
                        url = re.search(r"(https://.*?playlist.m3u8.*?)\"", text).group(1)

            elif 'videos.classplusapp' in url:
             url = requests.get(f'https://api.classplusapp.com/cams/uploader/video/jw-signed-url?url={url}', headers={'x-access-token': 'eyJhbGciOiJIUzM4NCIsInR5cCI6IkpXVCJ9.eyJpZCI6MzgzNjkyMTIsIm9yZ0lkIjoyNjA1LCJ0eXBlIjoxLCJtb2JpbGUiOiI5MTcwODI3NzQyODkiLCJuYW1lIjoiQWNlIiwiZW1haWwiOm51bGwsImlzRmlyc3RMb2dpbiI6dHJ1ZSwiZGVmYXVsdExhbmd1YWdlIjpudWxsLCJjb3VudHJ5Q29kZSI6IklOIiwiaXNJbnRlcm5hdGlvbmFsIjowLCJpYXQiOjE2NDMyODE4NzcsImV4cCI6MTY0Mzg4NjY3N30.hM33P2ai6ivdzxPPfm01LAd4JWv-vnrSxGXqvCirCSpUfhhofpeqyeHPxtstXwe0'}).json()['url']

            elif '/master.mpd' in url:
             id =  url.split("/")[-2]
             url =  "https://d26g5bnklkwsh4.cloudfront.net/" + id + "/master.m3u8"

            name1 = links[i][0].replace("\t", "").replace(":", "").replace("/", "").replace("+", "").replace("#", "").replace("|", "").replace("@", "").replace("*", "").replace(".", "").replace("https", "").replace("http", "").strip()
            name = f'{str(count).zfill(3)}) {name1[:60]}'

            if "youtu" in url:
                ytf = f"b[height<={raw_text2}][ext=mp4]/bv[height<={raw_text2}][ext=mp4]+ba[ext=m4a]/b[ext=mp4]"
            else:
                ytf = f"b[height<={raw_text2}]/bv[height<={raw_text2}]+ba/b/bv+ba"

            if "jw-prod" in url:
                cmd = f'yt-dlp -o "{name}.mp4" "{url}"'
            else:
                cmd = f'yt-dlp -f "{ytf}" "{url}" -o "{name}.mp4"'

            try:                               
                cc = f'** {str(count).zfill(3)}.** {name1} ({res}) ʟʊʍɨռǟռȶ.mkv\n**Batch Name :** {b_name}\n\n**Downloaded by : {CR}**'
                cc1 = f'** {str(count).zfill(3)}.** {name1} ʟʊʍɨռǟռȶ.pdf \n**Batch Name :**{b_name}\n\n**Downloaded by : {CR}**'
                if "drive" in url:
                    try:
                        ka = await helper.download(url, name)
                        await bot.send_document(chat_id=m.chat.id,document=ka, caption=cc1)
                        count+=1
                        os.remove(ka)
                        time.sleep(1)
                    except FloodWait as e:
                        await m.reply_text(str(e))
                        time.sleep(e.x)
                        continue
                elif ".pdf" in url:
                    try:
                        cmd = f'yt-dlp -o "{name}.pdf" "{url}"'
                        download_cmd = f"{cmd} -R 25 --fragment-retries 25"
                        os.system(download_cmd)
                        await bot.send_document(chat_id=m.chat.id,document=f'{name}.pdf', caption=cc1)
                        count += 1
                        os.remove(f'{name}.pdf')
                    except FloodWait as e:
                        await m.reply_text(str(e))
                        time.sleep(e.x)
                        continue
                else:
                    prog = await m.reply_text(f"**Downloading:-**\n\n** Video Name :-** `{name}\n\n╰────⌈✨ʟʊʍɨռǟռȶ ✨⌋────╯")
                    res_file = await helper.download_video(url, cmd, name)
                    filename = res_file
                    await prog.delete(True)
                    await helper.send_vid(bot, m, cc, filename, thumb, name, prog)
                    count += 1

            except Exception as e:
                logging.error(e)
                await m.reply_text(f"**Failed To Download ❌**\n**Name** - {name}\n**Link** - `{url}`")
                if "NoLinkFound" != url:
                 count+=1
                await bot.send_message(log_channel, f"**Failed To Download ❌**\n**Name** - {name}\n**Link** - {url}\n**Error** - `{e}`")
                time.sleep(3)
                continue
    except Exception as e:
        await m.reply_text(e)
    await m.reply_text("That's it ❤️")

@bot.on_message(filters.command(["kunal"]) & filters.chat(-1002123713069))
async def account_login(bot: Client, m: Message):
    editable = await m.reply_text("𝐇𝐞𝐥𝐥𝐨 𝐃𝐞𝐚𝐫 👋 use me for txt files ")
    input: Message = await bot.listen(editable.chat.id)
    x = await input.download()
    await input.delete(True)

    path = f"./downloads/{m.chat.id}"

    try:
        with open(x, "r") as f:
            content = f.read()
        content = content.split("\n")
        links = []
        for i in content:
            links.append(i.split(":", 1))
        os.remove(x)
        # print(len(links))
    except:
        await m.reply_text("Invalid file input.")
        os.remove(x)
        return

    await editable.edit(f"Total links found are **{len(links)}**\n\nSend From where you want to download initial is **0**")
    input1: Message = await bot.listen(editable.chat.id)
    raw_text = input1.text

    try:
        arg = int(raw_text)
    except:
        arg = 0

    await editable.edit("**Enter Batch Name**")
    input0: Message = await bot.listen(editable.chat.id)
    raw_text0 = input0.text

    await editable.edit("**Enter resolution:**")
    input2: Message = await bot.listen(editable.chat.id)
    raw_text2 = input2.text

    await editable.edit("Now send the **Thumb url**\nEg : **`https://graph.org/file/818aa312b35052a5c4d74.jpg`**\n\nor Send `no`")
    input6 = message = await bot.listen(editable.chat.id)
    raw_text6 = input6.text

    thumb = input6.text
    if thumb.startswith("http://") or thumb.startswith("https://"):
        getstatusoutput(f"wget '{thumb}' -O 'thumb.jpg'")
        thumb = "thumb.jpg"
    else:
        thumb == "no"

    if raw_text == '0':
        count = 1
    else:
        count = int(raw_text)

    try:
        for i in range(arg, len(links)):

            url = links[i][1]
            name1 = links[i][0].replace("\t", "").replace(":", "").replace("/","").replace("+", "").replace("#", "").replace("|", "").replace("@", "").replace("*", "").replace(".", "").strip() + "ʟʊʍɨռǟռȶ"


            if "visionias" in url:
                url = get_va(url)
                name = name1

            if raw_text2 == "144":

                cmd = f'yt-dlp -F "{url}"'
                k = await helper.run(cmd)
                out = helper.vid_info(str(k))
                # print(out)
                if '256x144' in out:
                    ytf = f"{out['256x144']}"
                elif '320x180' in out:
                    ytf = out['320x180']
                elif 'unknown' in out:
                    ytf = out["unknown"]
                else:
                    for data1 in out:
                        ytf = out[data1]
            elif raw_text2 == "180":

                cmd = f'yt-dlp -F "{url}"'
                k = await helper.run(cmd)
                out = helper.vid_info(str(k))
                # print(out)
                if '320x180' in out:
                    ytf = out['320x180']
                elif '426x240' in out:
                    ytf = out['426x240']
                elif 'unknown' in out:
                    ytf = out["unknown"]
                else:
                    for data2 in out:
                        ytf = out[data2]
            elif raw_text2 == "240":

                cmd = f'yt-dlp -F "{url}"'
                k = await helper.run(cmd)
                out = helper.vid_info(str(k))
                # print(out)
                if '426x240' in out:
                    ytf = out['426x240']
                elif '426x234' in out:
                    ytf = out['426x234']
                elif '480x270' in out:
                    ytf = out['480x270']
                elif '480x272' in out:
                    ytf = out['480x272']
                elif '640x360' in out:
                    ytf = out['640x360']
                elif 'unknown' in out:
                    ytf = out["unknown"]
                else:
                    for data3 in out:
                        ytf = out[data3]
            elif raw_text2 == "360":

                cmd = f'yt-dlp -F "{url}"'
                k = await helper.run(cmd)
                out = helper.vid_info(str(k))
                # print(out)
                if '640x360' in out:
                    ytf = out['640x360']
                elif '638x360' in out:
                    ytf = out['638x360']
                elif '636x360' in out:
                    ytf = out['636x360']
                elif '768x432' in out:
                    ytf = out['768x432']
                elif '638x358' in out:
                    ytf = out['638x358']
                elif '852x316' in out:
                    ytf = out['852x316']
                elif '850x480' in out:
                    ytf = out['850x480']
                elif '848x480' in out:
                    ytf = out['848x480']
                elif '854x480' in out:
                    ytf = out['854x480']
                elif '852x480' in out:
                    ytf = out['852x480']
                elif '854x470' in out:
                    ytf = out['852x470']
                elif '1280x720' in out:
                    ytf = out['1280x720']
                elif 'unknown' in out:
                    ytf = out["unknown"]
                else:
                    for data4 in out:
                        ytf = out[data4]
            elif raw_text2 == "480":

                cmd = f'yt-dlp -F "{url}"'
                k = await helper.run(cmd)
                out = helper.vid_info(str(k))
                # print(out)
                if '854x480' in out:
                    ytf = out['854x480']
                elif '852x480' in out:
                    ytf = out['852x480']
                elif '854x470' in out:
                    ytf = out['854x470']
                elif '768x432' in out:
                    ytf = out['768x432']
                elif '848x480' in out:
                    ytf = out['848x480']
                elif '850x480' in out:
                    ytf = ['850x480']
                elif '960x540' in out:
                    ytf = out['960x540']
                elif '640x360' in out:
                    ytf = out['640x360']
                elif 'unknown' in out:
                    ytf = out["unknown"]
                else:
                    for data5 in out:
                        ytf = out[data5]

            elif raw_text2 == "720":

                cmd = f'yt-dlp -F "{url}"'
                k = await helper.run(cmd)
                out = helper.vid_info(str(k))
                # print(out)
                if '1280x720' in out:
                    ytf = out['1280x720']
                elif '1280x704' in out:
                    ytf = out['1280x704']
                elif '1280x474' in out:
                    ytf = out['1280x474']
                elif '1920x712' in out:
                    ytf = out['1920x712']
                elif '1920x1056' in out:
                    ytf = out['1920x1056']
                elif '854x480' in out:
                    ytf = out['854x480']
                elif '640x360' in out:
                    ytf = out['640x360']
                elif 'unknown' in out:
                    ytf = out["unknown"]
                else:
                    for data6 in out:
                        ytf = out[data6]
            elif "player.vimeo" in url:
                if raw_text2 == '144':
                    ytf = 'http-240p'
                elif raw_text2 == "240":
                    ytf = 'http-240p'
                elif raw_text2 == '360':
                    ytf = 'http-360p'
                elif raw_text2 == '480':
                    ytf = 'http-540p'
                elif raw_text2 == '720':
                    ytf = 'http-720p'
                else:
                    ytf = 'http-360p'
            else:
                cmd = f'yt-dlp -F "{url}"'
                k = await helper.run(cmd)
                out = helper.vid_info(str(k))
                for dataS in out:
                    ytf = out[dataS]

            try:
                if "unknown" in out:
                    res = "ʟʊʍɨռǟռȶ"
                else:
                    res = list(out.keys())[list(out.values()).index(ytf)]

                name = f'{str(count).zfill(3)}) {name1} {res}'
            except Exception:
                res = "NA"

            # if "youtu" in url:
            # if ytf == f"'bestvideo[height<={raw_text2}][ext=mp4]+bestaudio[ext=m4a]'" or "acecwply" in url:
            if "acecwply" in url:
                cmd = f'yt-dlp -o "{name}.%(ext)s" -f "bestvideo[height<={raw_text2}]+bestaudio" --hls-prefer-ffmpeg --no-keep-video --remux-video mkv --no-warning "{url}"'
            elif "youtu" in url:
                cmd = f'yt-dlp -i -f "bestvideo[height<={raw_text2}]+bestaudio" --no-keep-video --remux-video mkv --no-warning "{url}" -o "{name}.%(ext)s"'
            elif "player.vimeo" in url:
                cmd = f'yt-dlp -f "{ytf}+bestaudio" --no-keep-video --remux-video mkv "{url}" -o "{name}.%(ext)s"'
            elif "m3u8" or "livestream" in url:
                cmd = f'yt-dlp -f "{ytf}" --no-keep-video --remux-video mkv "{url}" -o "{name}.%(ext)s"'
            elif ytf == "0" or "unknown" in out:
                cmd = f'yt-dlp -f "{ytf}" --no-keep-video --remux-video mkv "{url}" -o "{name}.%(ext)s"'
            elif ".pdf" in url:
                cmd = "pdf"
            else:
                cmd = f'yt-dlp -f "{ytf}+bestaudio" --hls-prefer-ffmpeg --no-keep-video --remux-video mkv "{url}" -o "{name}.%(ext)s"'

            try:
                Show = f"**Downloading:-**\n\n**Name :-** `{name}\nQuality - {raw_text2}`\n\n**Url :-**`{url}`\n\n**╰────⌈✨ ʟʊʍɨռǟռȶ ✨⌋────╯**"
                prog = await bot.send_message(m.chat.id, Show)
                cc = f"**Name »** {name1} {res} ʟʊʍɨռǟռȶ.mkv\n**Batch »** {raw_text0}\n**Index »** {str(count).zfill(3)}\n\n**EXTRACTED BY »** ʟʊʍɨռǟռȶ ✨"
                cc1 = f"**Name »** ** {name1} {res} ʟʊʍɨռǟռȶ.pdf\n**Batch »** {raw_text0}\n**Index »** {str(count).zfill(3)}\n\n**EXTRACTED BY »** ʟʊʍɨռǟռȶ ✨"
                #                         await prog.delete (True)
                #                 if cmd == "pdf" or "drive" in url:
                #                     try:
                #                         ka=await helper.download(url,name)
                #                         await prog.delete (True)
                #                         time.sleep(1)
                #                         # await helper.send_doc(bot,m,cc,ka,cc1,prog,count,name)
                #                         reply = await m.reply_text(f"Uploading - `{name}`")
                #                         time.sleep(1)
                #                         start_time = time.time()
                #                         await bot.send_document(m.chat.id, ka, caption=cc1)
                #                         count+=1
                #                         await reply.delete (True)
                #                         time.sleep(1)
                #                         os.remove(ka)
                #                         time.sleep(3)
                #                     except FloodWait as e:
                #                         await m.reply_text(str(e))
                #                         time.sleep(e.x)
                #                         continue
                if cmd == "pdf" or ".pdf" in url or ".pdf" in name:
                    try:
                        ka = await helper.aio(url, name)
                        await prog.delete(True)
                        time.sleep(1)
                        reply = await bot.send_message(m.chat.id, f"Uploading - ```{name}```")
                        time.sleep(1)
                        start_time = time.time()
                        await bot.send_document(m.chat.id, 
                            ka,
                            caption=
                            f"**Name »** {name1} {res}.pdf\n**Batch »** {raw_text0}\n**Index »** {str(count).zfill(3)}"
                        )
                        count += 1
                        # time.sleep(1)
                        await reply.delete(True)
                        time.sleep(1)
                        os.remove(ka)
                        time.sleep(3)
                    except FloodWait as e:
                        await m.reply_text(str(e))
                        time.sleep(e.x)
                        continue
                else:
                    res_file = await helper.download_video(url, cmd, name)
                    filename = res_file
                    await helper.send_vid(bot, m, cc, filename, thumb, name,
                                          prog)
                    count += 1
                    time.sleep(1)

            except Exception as e:
                await m.reply_text(
                    f"**downloading failed ❌**\n{str(e)}\n**Name** - {name}\n**Link** - `{url}`"
                )
                count += 1
                continue

    except Exception as e:
        await m.reply_text(e)
    await m.reply_text("That's It ❤️")
	
bot.run()
