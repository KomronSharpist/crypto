import asyncio
import json
import logging
import re
from datetime import datetime, date, timedelta, time,  timezone
from aiogram import Dispatcher
from aiogram.enums import ChatMemberStatus
from aiogram.filters.command import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram import Bot, types
import time

logging.basicConfig(level=logging.INFO)
# bot = Bot(token="5804242862:AAGRkQXyTMnVpEwojt13Cjr4v-zm6MRwa6g") # test
bot = Bot(token="6738630567:AAFQp5cPNqyxCQA3FhAgmSnB1PBGbJFus8I")
dp = Dispatcher()
crypto_list = {'ICX': 'HALOL', 'UTK': 'HALOL', 'KEY': 'HALOL', 'APE': 'HALOL', 'ATOM': 'HALOL', 'CELR': 'HALOL', 'DENT': 'HALOL', 'RSR': 'HALOL', 'RIF': 'HALOL', 'WAVES': 'HALOL', 'ONE': 'HALOL', 'PERL': 'HALOL', 'PHA': 'HALOL', 'RAD': 'HALOL', 'CFX': 'HALOL', 'SOL': 'HALOL', 'LIT': 'HALOL', 'XTZ': 'HALOL', 'ETH': 'HALOL', 'POND': 'HALOL', 'FTM': 'HALOL', 'BTC': 'HALOL', 'CELO': 'HALOL', 'LRC': 'HALOL', 'ROSE': 'HALOL', 'TRB': 'HALOL', 'FLUX': 'HALOL', 'REQ': 'HALOL', 'ETC': 'HALOL', 'DOGE': 'HALOL', 'IOST': 'HALOL', 'ENS': 'HALOL', 'AVAX': 'HALOL', 'MINA': 'HALOL', 'MATIC': 'HALOL', 'OP': 'HALOL', 'SKL': 'HALOL', 'FET': 'HALOL', 'ADA': 'HALOL', 'HOT': 'HALOL', 'ACH': 'HALOL', 'BAT': 'HALOL', 'MOVR': 'HALOL', 'CTK': 'HALOL', 'VET': 'HALOL', 'STX': 'HALOL', 'KSM': 'HALOL', 'ICP': 'HALOL', 'THETA': 'HALOL', 'DOT': 'HALOL', 'BLZ': 'HALOL', 'IRIS': 'HALOL', 'AR': 'HALOL', 'PHB': 'HALOL', 'DGB': 'HALOL', 'APT': 'HALOL', 'XEM': 'HALOL', 'ZEC': 'HALOL', 'ANT': 'HALOL', 'GLMR': 'HALOL', 'MANA': 'HALOL', 'MASK': 'HALOL', 'TOMO': 'HALOL', 'LTO': 'HALOL', 'AGIX': 'HALOL', 'DATA': 'HALOL', 'JASMY': 'HALOL', 'KLAY': 'HALOL', 'BCH': 'HALOL', 'FIL': 'HALOL', 'LINK': 'HALOL', 'FIO': 'HALOL', 'LPT': 'HALOL', 'RVN': 'HALOL', 'CTXC': 'HALOL', 'IOTA': 'HALOL', 'STORJ': 'HALOL', 'GTC': 'HALOL', 'AVA': 'HALOL', 'MDT': 'HALOL', 'NEAR': 'HALOL', 'VIDT': 'HALOL', 'CHR': 'HALOL', 'FLOW': 'HALOL', 'SYS': 'HALOL', 'COS': 'HALOL', 'DASH': 'HALOL', 'NULS': 'HALOL', 'TRX': 'HALOL', 'TWT': 'HALOL', 'LTC': 'HALOL', 'QTUM': 'HALOL', 'CTSI': 'HALOL', 'GRT': 'HALOL', 'SCRT': 'HALOL', 'DUSK': 'HALOL', 'EOS': 'HALOL', 'DCR': 'HALOL', 'OXT': 'HALOL', 'NKN': 'HALOL', 'GMT': 'HALOL', 'WTC': 'HALOL', 'ARPA': 'HALOL', 'HBAR': 'HALOL', 'PUNDIX': 'HALOL', 'TFUEL': 'HALOL', 'SXP': 'HALOL', 'XMR': 'HALOL', 'ALGO': 'HALOL', 'BICO': 'HALOL', 'CKB': 'HALOL', 'SFP': 'HALOL', 'TVK': 'HALOL', 'PAXG': 'HALOL', 'OMG': 'HALOL', 'ARDR': 'HALOL', 'POWR': 'HALOL', 'ATA': 'HALOL', 'DREP': 'HALOL', 'XLM': 'HALOL', 'XEC': 'HALOL', 'GAS': 'HALOL', 'FIRO': 'HALOL', 'LOOM': 'HALOL', 'QKC': 'HALOL', 'RARE': 'HALOL', 'CHZ': 'HALOL', 'ONG': 'HALOL', 'PROM': 'HALOL', 'XRP': 'HALOL', 'GLM': 'HALOL', 'RLC': 'HALOL', 'VTHO': 'HALOL', 'DOCK': 'HALOL', 'HIVE': 'HALOL', 'AMP': 'HALOL', 'BAND': 'HALOL', 'ZIL': 'HALOL', 'STMX': 'HALOL', 'MTL': 'HALOL', 'KMD': 'HALOL', 'ABBC': 'HALOL', 'ADX': 'HALOL', 'AERGO': 'HALOL', 'AIOZ': 'HALOL', 'AKT': 'HALOL', 'ALEPH': 'HALOL', 'ALT': 'HALOL', 'AOG': 'HALOL', 'APL': 'HALOL', 'ARRR': 'HALOL', 'AURORA': 'HALOL', 'BFC': 'HALOL', 'BLUR': 'HALOL', 'BUSD': 'HALOL', 'CARD': 'HALOL', 'CERE': 'HALOL', 'CQT': 'HALOL', 'CRPT': 'HALOL', 'CSPR': 'HALOL', 'DAG': 'HALOL', 'DERO': 'HALOL', 'DFA': 'HALOL', 'DIVI': 'HALOL', 'DPR': 'HALOL', 'DVPN': 'HALOL', 'EDG': 'HALOL', 'EGLD': 'HALOL', 'EWT': 'HALOL', 'GOM2': 'HALOL', 'GRIN': 'HALOL', 'GST': 'HALOL', 'HAI': 'HALOL', 'HAPI': 'HALOL', 'HNT': 'HALOL', 'HTR': 'HALOL', 'HYDRA': 'HALOL', 'IOTX': 'HALOL', 'KAI': 'HALOL', 'KDA': 'HALOL', 'KLV': 'HALOL', 'KOK': 'HALOL', 'KRL': 'HALOL', 'LITH': 'HALOL', 'LOCUS': 'HALOL', 'LYXE': 'HALOL', 'MAP': 'HALOL', 'METIS': 'HALOL', 'MITX': 'HALOL', 'MLK': 'HALOL', 'MNW': 'HALOL', 'MOOV': 'HALOL', 'MXC': 'HALOL', 'NIM': 'HALOL', 'NOIA': 'HALOL', 'NWC': 'HALOL', 'ORAI': 'HALOL', 'ORBS': 'HALOL', 'ORC': 'HALOL', 'PLU': 'HALOL', 'PRE': 'HALOL', 'PRQ': 'HALOL', 'PUSH': 'HALOL', 'QNT': 'HALOL', 'REAP': 'HALOL', 'REV.3L': 'HALOL', 'RLY': 'HALOL', 'RMRK': 'HALOL', 'RNDR': 'HALOL', 'SHR': 'HALOL', 'SOLVE': 'HALOL', 'SOUL': 'HALOL', 'STC': 'HALOL', 'STRAX': 'HALOL', 'SUTER': 'HALOL', 'SWASH': 'HALOL', 'SYLO': 'HALOL', 'TEL': 'HALOL', 'TIME': 'HALOL', 'TLOS': 'HALOL', 'TONE': 'HALOL', 'TON': 'HALOL', 'TRAC': 'HALOL', 'TRIAS': 'HALOL', 'USDC': 'HALOL', 'USDP': 'HALOL', 'VID': 'HALOL', 'VLX': 'HALOL', 'VRA': 'HALOL', 'VSYS': 'HALOL', 'WHALE': 'HALOL', 'WOM': 'HALOL', 'XCH': 'HALOL', 'XCN': 'HALOL', 'XDC': 'HALOL', 'XNO': 'HALOL', 'XPR': 'HALOL', 'XYM': 'HALOL', 'XYO': 'HALOL', 'ZEN': 'HALOL', 'AQT': 'HALOL', 'ARA': 'HALOL', 'ARK': 'HALOL', 'ARV': 'HALOL', 'BEAM': 'HALOL', 'BLY': 'HALOL', 'BORA': 'HALOL', 'BSV': 'HALOL', 'BTM': 'HALOL', 'CRT': 'HALOL', 'DKA': 'HALOL', 'DMD': 'HALOL', 'DORA': 'HALOL', 'ELF': 'HALOL', 'EL': 'HALOL', 'HC': 'HALOL', 'HERO': 'HALOL', 'HEZ': 'HALOL', 'HIBS': 'HALOL', 'ICHI': 'HALOL', 'IQ': 'HALOL', 'KIN': 'HALOL', 'LN': 'HALOL', 'MAPS': 'HALOL', 'MATH': 'HALOL', 'META': 'HALOL', 'MLT': 'HALOL', 'MSB': 'HALOL', 'MTA': 'HALOL', 'MVL': 'HALOL', 'NAS': 'HALOL', 'NAV': 'HALOL', 'NEBL': 'HALOL', 'NEST': 'HALOL', 'PAC': 'HALOL', 'PNK': 'HALOL', 'RAE': 'HALOL', 'RARI': 'HALOL', 'RAZOR': 'HALOL', 'SAFE': 'HALOL', 'SBR': 'HALOL', 'SC': 'HALOL', 'SDN': 'HALOL', 'SERO': 'HALOL', 'SNT': 'HALOL', 'STARS': 'HALOL', 'STEEM': 'HALOL', 'TMTG': 'HALOL', 'TORN': 'HALOL', 'TPT': 'HALOL', 'TUSD': 'HALOL', 'UPI': 'HALOL', '': 'HALOL', 'WNT': 'HALOL', 'XAUT': 'HALOL', 'XEP': 'HALOL', 'XPX': 'HALOL', 'XVG': 'HALOL', 'ZIG': 'HALOL', 'APM': 'HALOL', 'BCD': 'HALOL', 'CVC': 'HALOL', 'INT': 'HALOL', 'LSK': 'HALOL', 'MITH': 'HALOL'}
chanel_add_session = {}
chanel_control_session = {}
crypto_check_session = {}
admin_control_session = {}
data_control_session = {}
admin_add_session = {}
admin_sessions = {}
data_delete_session = {}
data_get_session = {}
data_add_session = {}
user_session = {}
owner_sessions = {}
crypto_control_session = {}
crypto_add_session = {}
crypto_delete_session = {}
user_reload_messages = {}
send_message_session = {}
send_message_premium_session = {}
inline_keyboard_session = {}
inline_keyboard_premium_session = {}
add_inline_keyboard_session = {}
add_inline_keyboard_premium_session = {}
logging.basicConfig(level=logging.INFO)
admin_userIds = {1052097431: "𝙺𝚘𝚖𝚛𝚘𝚗", 1885498684: "AZIZBEK"}
today = datetime.now().date()
ownerId = [1885498684, 1052097431]
reklam = ""
reklamBuilder = InlineKeyboardBuilder()
video_file_id = 0
chat_id = 0
channel_usernames = []
sended_users = []
unsended_users = []
last_response_time = {}
accessed_users = []

try:
    with open('all_users.json', 'r') as file:
        all_users = json.load(file)
except FileNotFoundError:
    all_users = []

try:
    with open('data.json', 'r') as file:
        data = json.load(file)
except FileNotFoundError:
    data = []

try:
    with open('inactive_users.json', 'r') as file:
        inactive_users = json.load(file)
except FileNotFoundError:
    inactive_users = []

try:
    with open('active_users.json', 'r') as file:
        active_users = json.load(file)
except FileNotFoundError:
    active_users = []


try:
    with open('today_active_users.json', 'r') as file:
        today_active_users = json.load(file)
except FileNotFoundError:
    today_active_users = []


try:
    with open('today_logined_users.json', 'r') as file:
        today_logined_users = json.load(file)
except FileNotFoundError:
    today_logined_users = []

try:
    with open('user_referals.json', 'r') as file:
        user_referals = json.load(file)
except FileNotFoundError:
    user_referals = {}


async def is_subscribed(user_id, channel_username):
    try:
        member = await bot.get_chat_member(channel_username, user_id)
        desired_statuses = {
            ChatMemberStatus.MEMBER,
            ChatMemberStatus.CREATOR,
            ChatMemberStatus.ADMINISTRATOR,
        }
        if member.status in desired_statuses:
            return True
    except Exception as e:
        return False
async def periodic_user_check():
    while True:
        now_utc = datetime.now(timezone.utc)
        utc_plus_5 = timedelta(hours=5)
        now = now_utc + utc_plus_5
        next_midnight = datetime.combine(now.date() + timedelta(days=1), datetime.min.time(), timezone.utc)
        time_until_midnight = (next_midnight - now).total_seconds()

        hours, remainder = divmod(time_until_midnight, 3600)
        minutes, seconds = divmod(remainder, 60)
        print(f"Keyingi yangilanishgacha: {int(hours):02d}:{int(minutes):02d}:{int(seconds):02d}")
        await asyncio.sleep(time_until_midnight)

        today_active_users.clear()
        today_logined_users.clear()
        with open('today_logined_users.json', 'w') as file:
            json.dump(today_logined_users, file)
        with open('today_active_users.json', 'w') as file:
            json.dump(today_active_users, file)
def get_duplicates():
    seen = set()
    duplicates = set()
    for item in today_active_users:
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)
    return list(duplicates)

async def get_referred_user_id(payload):
    try:
        user_id = int(payload.split('=')[-1])
        return user_id
    except (ValueError, IndexError):
        return None

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    user_id = message.from_user.id
    channel_unsubscribed = []
    user_session[user_id] = True
    if user_id in crypto_control_session:
        del crypto_control_session[user_id]
    if user_id in crypto_add_session:
        del crypto_add_session[user_id]
    if user_id in crypto_delete_session:
        del crypto_delete_session[user_id]

    if user_id in admin_control_session:
        del admin_control_session[user_id]
    if user_id in data_control_session:
        del data_control_session[user_id]
    if user_id in admin_add_session:
        del admin_add_session[user_id]
    if user_id in admin_sessions:
        del admin_sessions[user_id]
    if user_id in owner_sessions:
        del owner_sessions[user_id]

    if user_id in chanel_control_session:
        del chanel_control_session[user_id]
    if user_id in chanel_add_session:
        del chanel_add_session[user_id]

    if user_id not in admin_userIds or user_id not in ownerId:
        for channel_username in channel_usernames:
            if await is_subscribed(user_id, channel_username):
                continue
            else:
                channel_unsubscribed.append(channel_username)
        builder = InlineKeyboardBuilder()
        for channel in channel_unsubscribed:
            builder.add(types.InlineKeyboardButton(text=f"{channel}", url=f"https://t.me/{channel[1:]}"))
            builder.adjust(1, 1)
        if channel_unsubscribed:
            builder.add(types.InlineKeyboardButton(text=f"Tekshirish ✅", callback_data="checkSubscription"))
            builder.adjust(1, 1)
            await message.answer(
                "• Botdan foydalanish uchun avval kanalga obuna bo’ling va <b>Tekshirish</b> tugmasini bosing! ",
                reply_markup=builder.as_markup(), parse_mode="HTML")
            return
    kb = [
        [
            types.KeyboardButton(text="Asosiy kanalimiz 💬"),
            types.KeyboardButton(text="Kursimiz haqida ❕")
        ],
        [
            types.KeyboardButton(text="Trading darsliklar 📹"),
            types.KeyboardButton(text="VIPKANAL  Haqida 💎")
        ],
        [
            types.KeyboardButton(text="Do'st taklif qilish ➕"),
            types.KeyboardButton(text="Taklif qilingan do'stlar 📈")
        ],
        [types.KeyboardButton(text="Bepul skalping signallar 📈")],
        [types.KeyboardButton(text="Trading ortidan baraka topish 💵")],
        [types.KeyboardButton(text="Coinlar hukmini aniqlash ☪️")],
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    text = message.text
    if text.startswith('/start '):
        payload = text[len('/start '):]
        referred_user_id = await get_referred_user_id(payload)
        if referred_user_id != user_id:
            if referred_user_id in user_referals:
                if user_id not in user_referals[referred_user_id]:
                    user_referals[referred_user_id].append(user_id)
                    user_info = await bot.get_chat(user_id)
                    username = user_info.username if user_info.username else user_info.first_name
                    await bot.send_message(referred_user_id, f"Siz {username}ni taklif qildingiz ✅")
            else:
                user_referals[referred_user_id] = [user_id]
                user_info = await bot.get_chat(user_id)
                username = user_info.username if user_info.username else user_info.first_name
                await bot.send_message(referred_user_id, f"Siz {username}ni taklif qildingiz ✅")
            with open('user_referals.json', 'w') as file:
                json.dump(user_referals, file)
        else:
            await message.answer("Notog'ri referal link.")
    await message.answer("<b>Salom! 👋</b>\n\nO'zingizga kerakli bo'limni tanlgan!\n\n<b>Buyruqlar:</b>\n/start - botni qayta ishga tushirish;", reply_markup=keyboard, parse_mode="HTML")

@dp.message(Command("myid"))
async def cmd_start(message: types.Message):
    keyboard = types.ReplyKeyboardRemove()
    await message.answer(f"Sizning ID raqamingiz: {message.from_user.id}", reply_markup=keyboard)

@dp.message(Command("admin"))
async def cmd_start_admin(message: types.Message):
    user_id = message.from_user.id
    if user_id in admin_userIds.keys():
        admin_sessions[user_id] = True
        if user_id in ownerId:
            owner_sessions[user_id] = True
            kb = [
                [
                    types.KeyboardButton(text="Xabar yuborish ✉️"),
                    types.KeyboardButton(text="Statistika 📊")
                ],
                [
                    types.KeyboardButton(text="Crypto qo'shish ➕"),
                    types.KeyboardButton(text="Kanal qo'shish ➕")
                ],
                [
                    types.KeyboardButton(text="Malumotlar boshqaruvi 📂"),
                    types.KeyboardButton(text="Malumot turlari 🔀")
                ],
                [types.KeyboardButton(text="Premium xabar yuborish ✉️")],
                [types.KeyboardButton(text="Admin boshqaruvi 👤")],
                [types.KeyboardButton(text="Orqaga qaytish 🔙")],
            ]
            keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
            await message.answer(f"Admin panelga xush kelibsiz. Menuni tanlang!", reply_markup=keyboard)
        elif user_id in admin_userIds.keys():
            kb = [
                [
                    types.KeyboardButton(text="Xabar yuborish ✉️"),
                    types.KeyboardButton(text="Statistika 📊")
                ],
                [types.KeyboardButton(text="Kanal qo'shish ➕")],
                [types.KeyboardButton(text="Orqaga qaytish 🔙")],
            ]
            keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
            await message.answer(f"Admin panelga xush kelibsiz. Menuni tanlang!", reply_markup=keyboard)

async def check_subcription(message: types.Message):
    user_id = message.from_user.id

    channel_unsubscribed = []
    for channel_username in channel_usernames:
        if await is_subscribed(user_id, channel_username):
            continue
        else:
            channel_unsubscribed.append(channel_username)
    builder = InlineKeyboardBuilder()
    for channel in channel_unsubscribed:
        builder.add(types.InlineKeyboardButton(text=f"{channel}", url=f"https://t.me/{channel[1:]}"))
        builder.adjust(1, 1)
    if channel_unsubscribed:
        builder.add(types.InlineKeyboardButton(text=f"Tekshirish ✅", callback_data="checkSubscription"))
        builder.adjust(1, 1)
        await message.answer(
            "• Botdan foydalanish uchun avval kanalga obuna bo’ling va <b>Tekshirish</b> tugmasini bosing!",
            reply_markup=builder.as_markup(), parse_mode="HTML")
        return
    elif len(channel_unsubscribed) == 0:
        if user_id not in today_logined_users and user_id not in all_users:
            today_logined_users.append(user_id)
            with open('today_logined_users.json', 'w') as file:
                json.dump(today_logined_users, file)
        today_active_users.append(user_id)
        with open('today_active_users.json', 'w') as file:
            json.dump(today_active_users, file)
        if user_id not in all_users:
            all_users.append(user_id)
            with open('all_users.json', 'w') as file:
                json.dump(all_users, file)
        if user_id not in active_users:
            active_users.append(user_id)
            with open('active_users.json', 'w') as file:
                json.dump(active_users, file)
        if user_id in all_users:
            if user_id in inactive_users:
                inactive_users.remove(user_id)
                with open('inactive_users.json', 'w') as file:
                    json.dump(inactive_users, file)
        return True
@dp.message()
async def handle_message(message: types.Message):
    global new_api_key, last_api_key_update, video_file_id, reklam, reklamBuilder
    user_id = message.from_user.id
    user_message = message.text

    if user_id in admin_sessions:
        if user_message == "Orqaga qaytish  🔙" or user_message == "Bekor qilish ❌" :
            reklam = ""
            reklamBuilder = InlineKeyboardBuilder()
            if user_id in send_message_session:
                del send_message_session[user_id]
            if user_id in send_message_premium_session:
                del send_message_premium_session[user_id]
            if user_id in add_inline_keyboard_session:
                del add_inline_keyboard_session[user_id]
            if user_id in inline_keyboard_session:
                del inline_keyboard_session[user_id]
            if user_id in add_inline_keyboard_premium_session:
                del add_inline_keyboard_premium_session[user_id]
            if user_id in inline_keyboard_premium_session:
                del inline_keyboard_premium_session[user_id]
            if user_id in crypto_control_session:
                del crypto_control_session[user_id]
            if user_id in crypto_add_session:
                del crypto_add_session[user_id]
            if user_id in crypto_delete_session:
                del crypto_delete_session[user_id]
            if user_id in admin_control_session:
                del admin_control_session[user_id]
            if user_id in data_control_session:
                del data_control_session[user_id]
            if user_id in admin_add_session:
                del admin_add_session[user_id]
            if user_id in chanel_control_session:
                del chanel_control_session[user_id]
            if user_id in chanel_add_session:
                del chanel_add_session[user_id]
            if user_id in crypto_add_session:
                del crypto_add_session[user_id]
            if user_id in crypto_delete_session:
                del crypto_delete_session[user_id]
            if user_id in ownerId:
                owner_sessions[user_id] = True
                kb = [
                    [
                        types.KeyboardButton(text="Xabar yuborish ✉️"),
                        types.KeyboardButton(text="Statistika 📊")
                    ],
                    [
                        types.KeyboardButton(text="Crypto qo'shish ➕"),
                        types.KeyboardButton(text="Kanal qo'shish ➕")
                    ],
                    [
                        types.KeyboardButton(text="Malumotlar boshqaruvi 📂"),
                        types.KeyboardButton(text="Malumot turlari 🔀")
                    ],
                    [types.KeyboardButton(text="Premium xabar yuborish ✉️")],
                    [types.KeyboardButton(text="Admin boshqaruvi 👤")],
                    [types.KeyboardButton(text="Orqaga qaytish 🔙")],
                ]
                keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
                await message.answer(f"Admin panelga xush kelibsiz. Menuni tanlang!", reply_markup=keyboard)
            elif user_id in admin_userIds.keys():
                kb = [
                    [
                        types.KeyboardButton(text="Statistika 📊")
                    ],
                    [types.KeyboardButton(text="Kanal qo'shish ➕")],
                    [types.KeyboardButton(text="Orqaga qaytish 🔙")],
                ]
                keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
                await message.answer(f"Admin panelga xush kelibsiz. Menuni tanlang!", reply_markup=keyboard)
        elif user_id in admin_control_session:
            await admin_control_session_service(message)
        elif user_id in data_add_session:
            await data_add_service(message)
        elif user_id in data_delete_session:
            await delete_data_by_code(message)
        elif user_id in data_get_session:
            await get_list_data(message)
        elif user_id in data_control_session:
            await data_control_session_service(message)
        elif user_id in inline_keyboard_session:
            if user_message == "Qo'shish ✅":
                add_inline_keyboard_session[user_id] = True
                kb = [
                    [
                        types.KeyboardButton(text="Bekor qilish ❌"),
                    ]
                ]
                keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
                await message.answer(
                    "Kanal nomi*Kanal sslikasi\nKanal nomi*Kanal sslikasi\n...\n\nIltimos shu ko`rinishda kiriting",
                    reply_markup=keyboard)
            elif user_message == "Tashlab o'tish ❌":
                if isinstance(reklam, types.Message) and reklam.video:
                    video = reklam.video
                    caption = reklam.caption

                    await bot.send_video(
                        chat_id=user_id,
                        video=video.file_id,
                        caption=caption,
                        disable_notification=True,
                        reply_markup=reklamBuilder.as_markup(),
                        parse_mode="HTML"
                    )
                elif isinstance(reklam, types.Message):
                    await bot.copy_message(
                        chat_id=user_id,
                        from_chat_id=reklam.chat.id,
                        message_id=reklam.message_id,
                        reply_markup=reklamBuilder.as_markup(),
                        parse_mode="HTML"
                    )
                kb = [
                    [
                        types.KeyboardButton(text="Yuborish ✅"),
                        types.KeyboardButton(text="Bekor qilish ❌"),
                    ]
                ]
                keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
                await message.answer(
                    "Xabaringiz to'g'rimi? Agarda to'g'ri bo'lsa \"Yuborish ✅\" tugmasini bosing aks holda \"Bekor qilish ❌\"ni bosing",
                    reply_markup=keyboard)
            elif user_message == "Yuborish ✅":
                if user_id in ownerId:
                    owner_sessions[user_id] = True
                    del inline_keyboard_session[user_id]
                    kb = [
                        [
                            types.KeyboardButton(text="Xabar yuborish ✉️"),
                            types.KeyboardButton(text="Statistika 📊")
                        ],
                        [
                            types.KeyboardButton(text="Crypto qo'shish ➕"),
                            types.KeyboardButton(text="Kanal qo'shish ➕")
                        ],
                        [
                            types.KeyboardButton(text="Malumotlar boshqaruvi 📂"),
                            types.KeyboardButton(text="Malumot turlari 🔀")
                        ],
                        [types.KeyboardButton(text="Premium xabar yuborish ✉️")],
                        [types.KeyboardButton(text="Admin boshqaruvi 👤")],
                        [types.KeyboardButton(text="Orqaga qaytish 🔙")],
                    ]
                    keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
                    await message.answer(f"Admin panelga xush kelibsiz. Menuni tanlang!", reply_markup=keyboard)
                elif user_id in admin_userIds.keys():
                    kb = [
                        [
                            types.KeyboardButton(text="Xabar yuborish ✉️"),
                            types.KeyboardButton(text="Statistika 📊")
                        ],
                        [types.KeyboardButton(text="Kanal qo'shish ➕")],
                        [types.KeyboardButton(text="Orqaga qaytish 🔙")],
                    ]
                    keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
                    await message.answer(f"Admin panelga xush kelibsiz. Menuni tanlang!", reply_markup=keyboard)
                del send_message_session[message.from_user.id]
                await send_message_controller(message)
            elif user_id in add_inline_keyboard_session:
                keyboards = user_message.split("\n")
                for keyboard in keyboards:
                    name = keyboard.split("*")[0]
                    url = keyboard.split("*")[1]
                    reklamBuilder.add(types.InlineKeyboardButton(text=f"{name}", url=f"{url}"))
                    reklamBuilder.adjust(1, 1)
                if isinstance(reklam, types.Message) and reklam.video:
                    video = reklam.video
                    caption = reklam.caption

                    await bot.send_video(
                        chat_id=user_id,
                        video=video.file_id,
                        caption=caption,
                        disable_notification=True,
                        reply_markup=reklamBuilder.as_markup(),
                        parse_mode="HTML"
                    )
                elif isinstance(reklam, types.Message):
                    await bot.copy_message(
                        chat_id=user_id,
                        from_chat_id=reklam.chat.id,
                        message_id=reklam.message_id,
                        reply_markup=reklamBuilder.as_markup(),
                        parse_mode="HTML"
                    )
                kb = [
                    [
                        types.KeyboardButton(text="Yuborish ✅"),
                        types.KeyboardButton(text="Bekor qilish ❌"),
                    ]
                ]
                keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
                await message.answer(
                    "Xabaringiz to'g'rimi? Agarda to'g'ri bo'lsa \"Yuborish ✅\" tugmasini bosing aks holda \"Bekor qilish ❌\"ni bosing",
                    reply_markup=keyboard)
        elif user_id in inline_keyboard_premium_session:
            if user_message == "Qo'shish ✅":
                add_inline_keyboard_premium_session[user_id] = True
                kb = [
                    [
                        types.KeyboardButton(text="Bekor qilish ❌"),
                    ]
                ]
                keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
                await message.answer(
                    "Kanal nomi*Kanal sslikasi\nKanal nomi*Kanal sslikasi\n...\n\nIltimos shu ko`rinishda kiriting",
                    reply_markup=keyboard)
            elif user_message == "Tashlab o'tish ❌":
                if isinstance(reklam, types.Message) and reklam.video:
                    video = reklam.video
                    caption = reklam.caption

                    await bot.send_video(
                        chat_id=user_id,
                        video=video.file_id,
                        caption=caption,
                        disable_notification=True,
                        reply_markup=reklamBuilder.as_markup(),
                        parse_mode="HTML"
                    )
                elif isinstance(reklam, types.Message):
                    await bot.copy_message(
                        chat_id=user_id,
                        from_chat_id=reklam.chat.id,
                        message_id=reklam.message_id,
                        reply_markup=reklamBuilder.as_markup(),
                        parse_mode="HTML"
                    )
                kb = [
                    [
                        types.KeyboardButton(text="Yuborish ✅"),
                        types.KeyboardButton(text="Bekor qilish ❌"),
                    ]
                ]
                keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
                await message.answer(
                    "Xabaringiz to'g'rimi? Agarda to'g'ri bo'lsa \"Yuborish ✅\" tugmasini bosing aks holda \"Bekor qilish ❌\"ni bosing",
                    reply_markup=keyboard)
            elif user_message == "Yuborish ✅":
                if user_id in ownerId:
                    owner_sessions[user_id] = True
                    del inline_keyboard_premium_session[user_id]
                    kb = [
                        [
                            types.KeyboardButton(text="Xabar yuborish ✉️"),
                            types.KeyboardButton(text="Statistika 📊")
                        ],
                        [
                            types.KeyboardButton(text="Crypto qo'shish ➕"),
                            types.KeyboardButton(text="Kanal qo'shish ➕")
                        ],
                        [
                            types.KeyboardButton(text="Malumotlar boshqaruvi 📂"),
                            types.KeyboardButton(text="Malumot turlari 🔀")
                        ],
                        [types.KeyboardButton(text="Premium xabar yuborish ✉️")],
                        [types.KeyboardButton(text="Admin boshqaruvi 👤")],
                        [types.KeyboardButton(text="Orqaga qaytish 🔙")],
                    ]
                    keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
                    await message.answer(f"Admin panelga xush kelibsiz. Menuni tanlang!", reply_markup=keyboard)
                elif user_id in admin_userIds.keys():
                    kb = [
                        [
                            types.KeyboardButton(text="Xabar yuborish ✉️"),
                            types.KeyboardButton(text="Statistika 📊")
                        ],
                        [types.KeyboardButton(text="Kanal qo'shish ➕")],
                        [types.KeyboardButton(text="Orqaga qaytish 🔙")],
                    ]
                    keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
                    await message.answer(f"Admin panelga xush kelibsiz. Menuni tanlang!", reply_markup=keyboard)
                del send_message_premium_session[message.from_user.id]
                await send_message_premium_controller(message)
            elif user_id in add_inline_keyboard_premium_session:
                keyboards = user_message.split("\n")
                for keyboard in keyboards:
                    name = keyboard.split("*")[0]
                    url = keyboard.split("*")[1]
                    reklamBuilder.add(types.InlineKeyboardButton(text=f"{name}", url=f"{url}"))
                    reklamBuilder.adjust(1, 1)
                if isinstance(reklam, types.Message) and reklam.video:
                    video = reklam.video
                    caption = reklam.caption

                    await bot.send_video(
                        chat_id=user_id,
                        video=video.file_id,
                        caption=caption,
                        disable_notification=True,
                        reply_markup=reklamBuilder.as_markup(),
                        parse_mode="HTML"
                    )
                elif isinstance(reklam, types.Message):
                    await bot.copy_message(
                        chat_id=user_id,
                        from_chat_id=reklam.chat.id,
                        message_id=reklam.message_id,
                        reply_markup=reklamBuilder.as_markup(),
                        parse_mode="HTML"
                    )
                kb = [
                    [
                        types.KeyboardButton(text="Yuborish ✅"),
                        types.KeyboardButton(text="Bekor qilish ❌"),
                    ]
                ]
                keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
                await message.answer(
                    "Xabaringiz to'g'rimi? Agarda to'g'ri bo'lsa \"Yuborish ✅\" tugmasini bosing aks holda \"Bekor qilish ❌\"ni bosing",
                    reply_markup=keyboard)
        elif user_id in send_message_session:
            await send_message_service(message)
        elif user_id in send_message_premium_session:
            await send_message_premiuim_service(message)
        elif user_id in crypto_control_session:
            await crypto_control_session_service(message)
        elif user_id in chanel_control_session:
            await chanel_control_session_service(message)
        else:
            await admin_sessions_service(message)
    elif await check_subcription(message):
        if user_message == "Menyuga qaytish 🔙":
            if user_id in crypto_check_session:
                del crypto_check_session[user_id]
            kb = [
                [
                    types.KeyboardButton(text="Asosiy kanalimiz 💬"),
                    types.KeyboardButton(text="Kursimiz haqida ❕")
                ],
                [
                    types.KeyboardButton(text="Trading darsliklar 📹"),
                    types.KeyboardButton(text="VIPKANAL  Haqida 💎")
                ],
                [
                    types.KeyboardButton(text="Do'st taklif qilish ➕"),
                    types.KeyboardButton(text="Taklif qilingan do'stlar 📈")
                ],
                [types.KeyboardButton(text="Bepul skalping signallar 📈")],
                [types.KeyboardButton(text="Trading ortidan baraka topish 💵")],
                [types.KeyboardButton(text="Coinlar hukmini aniqlash ☪️")],
            ]
            keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
            await message.answer(
                "<b>Salom! 👋</b>\n\nO'zingizga kerakli bo'limni tanlgan!\n\n<b>Buyruqlar:</b>\n/start - botni qayta ishga tushirish;",
                reply_markup=keyboard, parse_mode="HTML")
        if user_message == "Coinlar hukmini aniqlash ☪️":
            crypto_check_session[user_id] = True
            kb = [
                [types.KeyboardButton(text="Menyuga qaytish 🔙")],
            ]
            keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
            await message.answer("Tekshirilayotgan kriptovalyutaning nomini (tikerini) lotin tilida kichik harflarda yozing.\n\nMasalan: <b>btc</b>", reply_markup=keyboard, parse_mode="HTML")
        elif user_id in crypto_check_session:
            await crypto_check(message)
        if user_message == "Asosiy kanalimiz 💬":
            await asosiy_channels_service(message)
        if user_message == "Kursimiz haqida ❕":
            await kursimiz_haqida_service(message)
        if user_message == "Trading darsliklar 📹":
            await trading_darsliklar_service(message)
        if user_message == "VIPKANAL  Haqida 💎":
            await vip_haqida_service(message)
        if user_message == "Bepul skalping signallar 📈":
            if len(user_referals.get(user_id, [])) >= 10:
                if user_id not in accessed_users:
                    accessed_users[user_id] = True
                await trading_haqida_qisqa_vidyolar_service(message)
            else:
                referral_link = f'https://t.me/Afrosiyob_trading_bot?start={user_id}'
                await message.answer(f"Bu bo'limni ochish uchun siz 10 do'stingizni taklif qilishingiz kerak!\n\nSizning referal linkiz: \n{referral_link}\n\n Do'stlaringizni taklif qilish uchun ularga jonating.!")
        if user_message == "Trading ortidan baraka topish 💵":
            await savdo_trading_baraka_service(message)
        if user_message == "Do'st taklif qilish ➕":
            referral_link = f'https://t.me/Afrosiyob_trading_bot?start={user_id}'
            await message.answer(f"Sizning referal linkiz: \n{referral_link}\n\n Do'stlaringizni taklif qilish uchun ularga jonating.!")
        if user_message == "Taklif qilingan do'stlar 📈":
            await message.answer(f"Siz taklif qilgan do'stlar soni: {len(user_referals.get(user_id, []))}")


async def crypto_check(message: types.Message):
    user_message = message.text.lower()
    crypto_name = next((crypto for crypto in crypto_list if crypto.lower() == user_message), None)

    if crypto_name:
        await message.answer(f"{crypto_list[crypto_name]}")
    else:
        await message.answer("Bu kriptovalyuta boʻyicha hozircha ma'lumot yo'q!")
async def admin_control_session_service(message: types.Message):
    user_id = message.from_user.id
    user_message = message.text
    if user_message == "Adminlar royxati 📄":
        builder = InlineKeyboardBuilder()
        for item in list(admin_userIds.items()):
            builder.add(types.InlineKeyboardButton(text=f"{item[0]}", callback_data=f"nothing"))
            builder.add(types.InlineKeyboardButton(text=f"{item[1]}", callback_data=f"nothing"))
            builder.add(types.InlineKeyboardButton(text=f"🗑", callback_data=f"admin_delete_{item[0]}"))
            builder.adjust(3, 3)
        await message.answer(
            f"Adminlar royxati 📄",
            reply_markup=builder.as_markup())
    elif user_id in admin_add_session:
        del admin_add_session[user_id]
        userid = user_message.split(" ")
        admin_userIds[int(userid[0])] = userid[1]
        await message.answer("Admin qoshildi", )
    if user_message == "Admin qoshish ➕":
        admin_add_session[user_id] = True
        await message.answer("Admin qoshish ➕ uchun uning ID sini va Ismini yozing. Misol : 2479323 Ismi", )

async def data_add_service(message: types.Message):
    user_id = message.from_user.id
    user_message = message.text

    if message.photo:
        media_type = 'photo'
        media_file = message.photo[-1].file_id
    elif message.video:
        media_type = 'video'
        media_file = message.video.file_id
    elif user_message == "Orqaga qaytish 🔙":
        del data_add_session[user_id]
        await cmd_start_admin(message)


    caption = message.caption
    code_pattern = re.compile(r'#\d+_\w+')
    code_match = code_pattern.search(caption)
    if code_match:
        code = code_match.group()
        caption = caption.replace(code, '')
        code = code.replace('#', '').split("_")
    else:
        code = None

    json_filename = 'data.json'
    try:
        with open(json_filename, 'r') as json_file:
            existing_data = json.load(json_file)
    except FileNotFoundError:
        existing_data = []

    encoded_caption = caption.encode('unicode-escape').decode('utf-8')

    new_entry = {
        'media_type': media_type,
        'media_file': media_file,
        'caption': encoded_caption,
        'code': None,
        'type': None
    }

    if code and len(code) >= 2:
        new_entry['code'] = code[0]
        new_entry['type'] = code[1]
    else:
        await message.answer(f"Notog'ri format ❌", parse_mode="HTML")
        return

    if any(entry['code'] == new_entry['code'] for entry in existing_data):
        await message.answer(f"Code alaqachon bor ❌", parse_mode="HTML")
        return

    existing_data.append(new_entry)
    with open(json_filename, 'w') as json_file:
        json.dump(existing_data, json_file)

    await message.answer(f"Xabaringiz saqlandi ✅", parse_mode="HTML")
    del data_add_session[user_id]

async def get_list_data(message: types.Message):
    json_filename = 'data.json'
    try:
        with open(json_filename, 'r') as json_file:
            data = json.load(json_file)

        if not isinstance(data, list) or not data:
            await bot.send_message(message.from_user.id, "Hozircha hech qanday malumotlar yo'q❗️")
            del data_get_session[message.from_user.id]
            return

        filtered_data = [entry for entry in data if entry.get('type') == message.text]

        if not filtered_data:
            await bot.send_message(message.from_user.id, "Hozircha hech qanday malumotlar yo'q❗️")
            del data_get_session[message.from_user.id]
            return

        films_list = "\n".join([f"\n\ncode: {entry.get('code', 'No code')}\n"
                                f"type: {entry.get('type', 'No type')}\n"
                                f"caption: {entry.get('caption', 'No caption')}" for entry in filtered_data])

        del data_get_session[message.from_user.id]
        await send_message_chunks(message.chat.id, films_list)
    except FileNotFoundError:
        del data_get_session[message.from_user.id]
        await bot.send_message(message.from_user.id, "Hozircha hech qanday malumotlar yo'q❗️")

async def data_control_session_service(message: types.Message):
    user_id = message.from_user.id
    user_message = message.text
    if user_message == "Malumot o'chirish ❌":
        await message.answer("Malumot raqamini tashalang. #raqam")
        data_delete_session[user_id] = True
    if user_message == "Malumotlar royxati 📄":
        await message.answer("Malumot turini kiriting. ✏️")
        data_get_session[user_id] = True
    if user_message == "Malumot qoshish ➕":
        data_add_session[user_id] = True
        kb = []
        keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
        await message.answer("Malumotni tashlang 📂\n\nItimos ma'lumotni korsatilgan tartibda tashlang:\n\nFile: Rasim yokida Vidyo\nCaption: #code_type (code qaytarilmasligi kerak, typeni esa Malumot turlari degan joydan olishingiz mumkun)", reply_markup=keyboard)

async def delete_data_by_code(message: types.Message):
    json_filename = 'data.json'
    try:
        with open(json_filename, 'r') as json_file:
            data = json.load(json_file)

        if not isinstance(data, list) or not data:
            await bot.send_message(message.from_user.id, "Hozircha hech qanday malumot yo'q❗️")
            del data_delete_session[message.from_user.id]
            return

        code_to_delete = message.text
        updated_data = [entry for entry in data if 'code' in entry and entry['code'] != code_to_delete]

        if len(updated_data) < len(data):
            with open(json_filename, 'w') as json_file:
                json.dump(updated_data, json_file)

            await bot.send_message(message.from_user.id, "Malumot o'chirildi✅")
            del data_delete_session[message.from_user.id]
        else:
            await bot.send_message(message.from_user.id, "Bunaqa kod bilan malumot topilmadi❗️")
            del data_delete_session[message.from_user.id]

    except FileNotFoundError:
        await bot.send_message(message.from_user.id, "Hozircha hech qanday filmlar yo'q❗️")
        del data_delete_session[message.from_user.id]


async def get_list_by_code(message: types.Message, code):
    json_filename = 'data.json'
    try:
        with open(json_filename, 'r') as json_file:
            data = json.load(json_file)

        if not isinstance(data, list) or not data:
            await bot.send_message(message.from_user.id, "Hozircha hech qanday malumotlar yo'q❗️")
            return

        matching_entries = [entry for entry in data if 'type' in entry and entry.get('type') == code]
        if not matching_entries:
            await bot.send_message(message.from_user.id, "Hozircha hech qanday malumotlar yo'q❗️")
            return

        if matching_entries:
            for entry in matching_entries:
                file_id = entry.get('media_file')
                raw_caption = entry.get('caption').replace('\\n', '\n')

                caption = raw_caption.encode('utf-8').decode('unicode-escape')

                if entry['media_type'] == 'photo':
                    await bot.send_photo(chat_id=message.from_user.id, photo=file_id, caption=caption,
                                         parse_mode="HTML")
                elif entry['media_type'] == 'video':
                    await bot.send_video(chat_id=message.from_user.id, video=file_id, caption=caption,
                                         parse_mode="HTML")

            return
    except FileNotFoundError:
        await bot.send_message(message.from_user.id, "Hozircha hech qanday malumotlar yo'q❗️")

async def asosiy_channels_service(message: types.Message):
    await get_list_by_code(message,"1")
async def kursimiz_haqida_service(message: types.Message):
    await get_list_by_code(message,"2")
async def trading_darsliklar_service(message: types.Message):
    await get_list_by_code(message,"3")
async def vip_haqida_service(message: types.Message):
    await get_list_by_code(message,"4")
async def trading_haqida_qisqa_vidyolar_service(message: types.Message):
    await get_list_by_code(message,"5")
async def savdo_trading_baraka_service(message: types.Message):
    await get_list_by_code(message,"6")
async def admin_sessions_service(message: types.Message):
    user_id = message.from_user.id
    user_message = message.text
    if user_message == "Crypto qo'shish ➕" and user_id in ownerId:
        crypto_control_session[user_id] = True
        kb = [
            [
                types.KeyboardButton(text="Crypto qo'shish  ➕"),
                types.KeyboardButton(text="Crypto royxati 📄"),
            ],
            [types.KeyboardButton(text="Crypto ochirish ❌")],
            [types.KeyboardButton(text="Orqaga qaytish  🔙")]
        ]
        keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
        await message.answer(
            "Crypto qo'shish ➕",
            reply_markup=keyboard)
    if user_message == "Xabar yuborish ✉️":
        send_message_session[user_id] = True
        kb = [
            [types.KeyboardButton(text="Orqaga qaytish  🔙")]
        ]
        keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
        await message.answer(f"Marhamat xabaringizni yuborishingiz mumkin", reply_markup=keyboard)
    if user_message == "Premium xabar yuborish ✉️":
        send_message_premium_session[user_id] = True
        kb = [
            [types.KeyboardButton(text="Orqaga qaytish  🔙")]
        ]
        keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
        await message.answer(f"Marhamat xabaringizni yuborishingiz mumkin", reply_markup=keyboard)
    if user_message == "Admin boshqaruvi 👤" and user_id in ownerId:
        admin_control_session[user_id] = True
        kb = [
            [
                types.KeyboardButton(text="Admin qoshish ➕"),
                types.KeyboardButton(text="Adminlar royxati 📄"),
            ],
            [types.KeyboardButton(text="Orqaga qaytish  🔙")]
        ]
        keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
        await message.answer(
            "Admin boshqaruvi 👤",
            reply_markup=keyboard)
    if user_message == "Malumotlar boshqaruvi 📂":
        data_control_session[user_id] = True
        kb = [
            [
                types.KeyboardButton(text="Malumot qoshish ➕"),
                types.KeyboardButton(text="Malumotlar royxati 📄"),
            ],
            [types.KeyboardButton(text="Malumot o'chirish ❌")],
            [types.KeyboardButton(text="Orqaga qaytish  🔙")]
        ]
        keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
        await message.answer(
            "Malumotlar boshqaruvi 📂",
            reply_markup=keyboard)
    if user_message == "Malumot turlari 🔀":
        await message.answer(
            "1. Asosiy kanal.\n2. Kursimiz haqida\n3. Trading darsliklar.\n4. VIPKANAL  Haqida.\n5. Bepul skalping signallar\n6.  Trading ortidan baraka topish")
    if user_message == "Statistika 📊":
        await message.answer(f"📊 Jami a'zolar soni: {len(all_users)}\n"
                             f"📈 Aktiv a'zolar soni: {len(active_users)}\n"
                             f"📊 Bugungi ishlatganlar: {len(get_duplicates())}\n"
                             f"📉 Block qilganlar soni: {len(inactive_users)}\n"
                             f"📊 Bugungi a'zolar: {len(today_logined_users)}")
    if user_message == "Kanal qo'shish ➕":
        chanel_control_session[user_id] = True
        kb = [
            [
                types.KeyboardButton(text="Kanal qoshish ➕"),
                types.KeyboardButton(text="Kanallar royxati 📄"),
            ],
            [types.KeyboardButton(text="Orqaga qaytish  🔙")]
        ]
        keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
        await message.answer(
            "Kanal qo'shish ➕",
            reply_markup=keyboard)
    if user_message == "Orqaga qaytish 🔙":
        if user_id in owner_sessions:
            del owner_sessions[user_id]
        del admin_sessions[user_id]
        user_session[user_id] = True
        if user_id in crypto_check_session:
            del crypto_check_session[user_id]
        kb = [
            [
                types.KeyboardButton(text="Asosiy kanalimiz 💬"),
                types.KeyboardButton(text="Kursimiz haqida ❕")
            ],
            [
                types.KeyboardButton(text="Trading darsliklar 📹"),
                types.KeyboardButton(text="VIPKANAL  Haqida 💎")
            ],
            [
                types.KeyboardButton(text="Do'st taklif qilish ➕"),
                types.KeyboardButton(text="Taklif qilingan do'stlar 📈")
            ],
            [types.KeyboardButton(text="Bepul skalping signallar 📈")],
            [types.KeyboardButton(text="Trading ortidan baraka topish 💵")],
            [types.KeyboardButton(text="Coinlar hukmini aniqlash ☪️")],
        ]
        keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
        await message.answer(
            "<b>Salom! 👋</b>\n\nO'zingizga kerakli bo'limni tanlgan!\n\n<b>Buyruqlar:</b>\n/start - botni qayta ishga tushirish;",
            reply_markup=keyboard, parse_mode="HTML")

async def send_message_service(message: types.Message):
    global reklam
    reklam = message
    kb = [
        [
            types.KeyboardButton(text="Qo'shish ✅"),
            types.KeyboardButton(text="Tashlab o'tish ❌"),
        ]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    await message.answer("Xabaringiz saqlandi. Xabar tagiga keyboard reklama qo'shasizmi?", reply_markup=keyboard)
    inline_keyboard_session[message.from_user.id] = True

async def send_message_premiuim_service(message: types.Message):
    global reklam
    reklam = message
    kb = [
        [
            types.KeyboardButton(text="Qo'shish ✅"),
            types.KeyboardButton(text="Tashlab o'tish ❌"),
        ]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    await message.answer("Xabaringiz saqlandi. Xabar tagiga keyboard reklama qo'shasizmi?", reply_markup=keyboard)
    inline_keyboard_premium_session[message.from_user.id] = True

async def send_message_premium_service(message: types.Message):
    global reklam
    reklam = message
    kb = [
        [
            types.KeyboardButton(text="Qo'shish ✅"),
            types.KeyboardButton(text="Tashlab o'tish ❌"),
        ]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    await message.answer("Xabaringiz saqlandi. Xabar tagiga keyboard reklama qo'shasizmi?", reply_markup=keyboard)
    inline_keyboard_premium_session[message.from_user.id] = True

async def send_message_chunks(chat_id, text):
    max_message_length = 4096
    chunks = [text[i:i + max_message_length] for i in range(0, len(text), max_message_length)]
    for chunk in chunks:
        await bot.send_message(chat_id, chunk)

async def crypto_control_session_service(message: types.Message):
    user_id = message.from_user.id
    user_message = message.text
    if user_message == "Crypto royxati 📄":
        films_list = "\n".join(
            [f"\n\ncode: {key}\ncaption: {value}" for key, value in crypto_list.items()])
        chat_id = message.chat.id
        await send_message_chunks(chat_id, films_list)
    elif user_id in crypto_add_session:
        userid = user_message.replace("_", "").split(" ")
        if userid[0] in crypto_list.keys():
            await message.answer("Crypto mavjud", )
        else:
            crypto_list[userid[0]] = userid[1]
            await message.answer("Crypto qoshildi", )
    elif user_id in crypto_delete_session:
        try:
            code_to_delete = message.text

            if code_to_delete in crypto_list.keys():
                del crypto_list[code_to_delete]
                await bot.send_message(message.from_user.id, "Crypto o'chirildi✅")
            else:
                await bot.send_message(message.from_user.id, "Bunaqa kod bilan crypto topilmadi❗️")
        except FileNotFoundError:
            await bot.send_message(message.from_user.id, "Bunaqa kod bilan crypto topilmadi❗️")
    if user_message == "Crypto qo'shish  ➕":
        crypto_add_session[user_id] = True
        kb = [
            [types.KeyboardButton(text="Orqaga qaytish  🔙")],
        ]
        keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
        await message.answer("Qoshmoqchi bolgan Crypto ingizni jonating. Misol : CryptoNomi HalolYokiHarom", reply_markup=keyboard)
    if user_message == "Crypto ochirish ❌":
        crypto_delete_session[user_id] = True
        kb = [
            [types.KeyboardButton(text="Orqaga qaytish  🔙")],
        ]
        keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
        await message.answer("Ochirmoqchi bolgan Crypto ingizni jonating. Misol : tbc", reply_markup=keyboard)

async def chanel_control_session_service(message: types.Message):
    user_id = message.from_user.id
    user_message = message.text
    if user_message == "Kanallar royxati 📄":
        builder = InlineKeyboardBuilder()
        for item in channel_usernames:
            builder.add(types.InlineKeyboardButton(text=f"{item}", callback_data=f"nothing"))
            builder.add(types.InlineKeyboardButton(text=f"🗑", callback_data=f"channel_delete_{item}"))
            builder.adjust(2, 2)
        await message.answer(
            f"Siz qoshgan kanallar lar royxati",
            reply_markup=builder.as_markup())
    elif user_id in chanel_add_session:
        if user_message.startswith("@"):
            del chanel_add_session[user_id]
            channel_usernames.append(f"{user_message}")
            await message.answer("Kanal qoshildi", )
        else: await message.answer("Iltimos kanal nomini tog'ri kiriting!")
    if user_message == "Kanal qoshish ➕":
        chanel_add_session[user_id] = True
        await message.answer("Qoshmoqchi bolgan kanalingizni jonating. Misol : @kanal", )
async def send_video_message(user_id, video, caption, counter):
    try:
        await bot.send_video(
            chat_id=user_id,
            video=video.file_id,
            caption=caption,
            disable_notification=True,
            reply_markup=reklamBuilder.as_markup(),
            parse_mode="HTML"
        )
        print(f"{user_id} jonatildi, {len(all_users) - counter} qoldi ")
        sended_users.append(user_id)
        if user_id in inactive_users:
            active_users.append(user_id)
            inactive_users.remove(user_id)
            with open('inactive_users.json', 'w') as file:
                json.dump(inactive_users, file)
            with open('active_users.json', 'w') as file:
                json.dump(active_users, file)
    except Exception as e:
        print(f"{user_id} jonatilmadi, {len(all_users) - counter} qoldi ")
        unsended_users.append(user_id)
        if user_id in active_users:
            active_users.remove(user_id)
            inactive_users.append(user_id)
            with open('inactive_users.json', 'w') as file:
                json.dump(inactive_users, file)
            with open('active_users.json', 'w') as file:
                json.dump(active_users, file)
async def send_copy_message(user_id, counter, reklam):
    try:
        await bot.copy_message(
            chat_id=user_id,
            from_chat_id=reklam.chat.id,
            message_id=reklam.message_id,
            reply_markup=reklamBuilder.as_markup(),
            parse_mode="HTML"
        )
        print(f"{user_id} jonatildi, {len(all_users) - counter} qoldi ")
        sended_users.append(user_id)
        if user_id in inactive_users:
            active_users.append(user_id)
            inactive_users.remove(user_id)
            with open('inactive_users.json', 'w') as file:
                json.dump(inactive_users, file)
            with open('active_users.json', 'w') as file:
                json.dump(active_users, file)
    except Exception as e:
        print(f"{user_id} jonatilmadi, {len(all_users) - counter} qoldi ")
        unsended_users.append(user_id)
        if user_id in active_users:
            active_users.remove(user_id)
            inactive_users.append(user_id)
            with open('inactive_users.json', 'w') as file:
                json.dump(inactive_users, file)
            with open('active_users.json', 'w') as file:
                json.dump(active_users, file)

async def send_message_controller(message: types.Message):
    global reklam
    start_time = datetime.now()
    counter = 0
    if isinstance(reklam, types.Message):
        video = reklam.video
        caption = reklam.caption

        for user_id in all_users:
            counter += 1
            if reklam.video:
                await send_video_message(user_id, video, caption, counter)
            else:
                await send_copy_message(user_id, counter, reklam)

    end_time = datetime.now()
    execution_time = end_time - start_time
    total_seconds = execution_time.total_seconds()
    minutes, seconds = divmod(total_seconds, 60)
    time_string = f"{int(minutes)} daqiqa {int(seconds)} sekund vaqt oralig'ida yuborildi."

    await message.answer(
        f"Xabaringiz yuborildi ✅\n\nYuborilmaganlar soni: {len(unsended_users)}\nYuborilganlar soni: {len(sended_users)}\n{time_string}"
    )

async def send_message_premium_controller(message: types.Message):
    global reklam
    start_time = datetime.now()
    counter = 0
    if isinstance(reklam, types.Message):
        video = reklam.video
        caption = reklam.caption

        for user_id in accessed_users:
            counter += 1
            if reklam.video:
                await send_video_message(user_id, video, caption, counter)
            else:
                await send_copy_message(user_id, counter, reklam)

    end_time = datetime.now()
    execution_time = end_time - start_time
    total_seconds = execution_time.total_seconds()
    minutes, seconds = divmod(total_seconds, 60)
    time_string = f"{int(minutes)} daqiqa {int(seconds)} sekund vaqt oralig'ida yuborildi."

    await message.answer(
        f"Xabaringiz yuborildi ✅\n\nYuborilmaganlar soni: {len(unsended_users)}\nYuborilganlar soni: {len(sended_users)}\n{time_string}"
    )
@dp.callback_query(lambda callback: callback.data.startswith("admin_delete_"))
async def admin_controller(callback: types.CallbackQuery):
    if callback.data.startswith("admin_delete_"):
        user_id = callback.data.split("_")
        admin = admin_userIds[int(user_id[2])]

        if admin:
            del admin_userIds[int(user_id[2])]
            builder = InlineKeyboardBuilder()
            for item in list(admin_userIds.items()):
                builder.add(types.InlineKeyboardButton(text=f"{item[0]}", callback_data=f"nothing"))
                builder.add(types.InlineKeyboardButton(text=f"{item[1]}", callback_data=f"nothing"))
                builder.add(types.InlineKeyboardButton(text=f"🗑", callback_data=f"admin_delete_{item[0]}"))
                builder.adjust(3, 3)
            await callback.message.answer(f"Adminlar royxati 📄", reply_markup=builder.as_markup())
            await callback.answer(f"Deleting admin: {admin}", show_alert=True)
        else:
            await callback.answer("Admin not found.", show_alert=True)

@dp.callback_query(lambda callback: callback.data.startswith("crypto_delete_"))
async def crypto_controller(callback: types.CallbackQuery):
    if callback.data.startswith("crypto_delete_"):
        api_name = callback.data.split("_")[2]

        if api_name in crypto_list.keys():
            del crypto_list[api_name]
            builder = InlineKeyboardBuilder()
            for item in list(crypto_list.items()):
                builder.add(types.InlineKeyboardButton(text=f"{item[0]}", callback_data=f"nothing"))
                builder.add(types.InlineKeyboardButton(text=f"{item[1]}", callback_data=f"nothing"))
                builder.add(types.InlineKeyboardButton(text=f"🗑", callback_data=f"crypto_delete_{item[0]}"))
                builder.adjust(3, 3)
            await callback.message.answer(f"Cryptolar royxati", reply_markup=builder.as_markup())
            await callback.answer(f"Deleting api: {api_name}", show_alert=True)
        else:
            await callback.answer("Crypto not found.", show_alert=True)

@dp.callback_query(lambda callback: callback.data == 'bekorqilish')
async def cancel_callback(callback: types.CallbackQuery):
    await callback.message.delete()

@dp.callback_query(lambda callback: callback.data.startswith("channel_delete_"))
async def channel_controller(callback: types.CallbackQuery):
    if callback.data.startswith("channel_delete_"):
        channel_name = callback.data.split("@")[1]
        if f"@{channel_name}" in channel_usernames:
            channel_usernames.remove(f"@{channel_name}")
            builder = InlineKeyboardBuilder()
            for item in channel_usernames:
                builder.add(types.InlineKeyboardButton(text=f"{item}", callback_data=f"nothing"))
                builder.add(types.InlineKeyboardButton(text=f"🗑", callback_data=f"channel_delete_{item}"))
                builder.adjust(2, 2)
            await callback.message.answer(f"Kanallar royxati 📄", reply_markup=builder.as_markup())
            await callback.answer(f"Deleting channel: {channel_name}", show_alert=True)
        else:
            await callback.answer("Chanel not found.", show_alert=True)

@dp.callback_query(lambda callback: callback.data.startswith("checkSubscription"))
async def channel_controller(callback: types.CallbackQuery):
    if callback.data.startswith("checkSubscription"):
        user_id = callback.from_user.id
        channel_unsubscribed = []
        for channel_username in channel_usernames:
            if await is_subscribed(user_id, channel_username):
                continue
            else:
                channel_unsubscribed.append(channel_username)
        builder = InlineKeyboardBuilder()
        for channel in channel_unsubscribed:
            builder.add(types.InlineKeyboardButton(text=f"{channel}", url=f"https://t.me/{channel[1:]}"))
            builder.adjust(1, 1)
        if channel_unsubscribed:
            await callback.answer("• Botdan foydalanish uchun avval kanalga obuna bo’ling.")
            return
        else:
            if user_id not in today_logined_users and user_id not in all_users:
                today_logined_users.append(user_id)
                with open('today_logined_users.json', 'w') as file:
                    json.dump(today_logined_users, file)
            today_active_users.append(user_id)
            with open('today_active_users.json', 'w') as file:
                json.dump(today_active_users, file)
            if user_id not in all_users:
                all_users.append(user_id)
                with open('all_users.json', 'w') as file:
                    json.dump(all_users, file)
            if user_id not in active_users:
                active_users.append(user_id)
                with open('active_users.json', 'w') as file:
                    json.dump(active_users, file)
            if user_id in all_users and user_id in inactive_users:
                inactive_users.remove(user_id)
                with open('inactive_users.json', 'w') as file:
                    json.dump(inactive_users, file)
            await bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
            await callback.answer("")
            await callback.message.answer(
                "Tekshirilayotgan kriptovalyutaning nomini (tikerini) lotin tilida  kichik harflarda yozing.\n\nMasalan: <b>btc</b>",
                parse_mode="HTML")

async def set_default_commands():
    await bot.set_my_commands([
        types.BotCommand(command="start", description="Qayta ishga tushurish"),
    ])

async def main():
    await set_default_commands()
    await dp.start_polling(bot)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.create_task(main())
    loop.create_task(periodic_user_check())

    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass
    finally:
        tasks = asyncio.all_tasks(loop=loop)
        for task in tasks:
            task.cancel()

        loop.run_until_complete(asyncio.gather(*tasks, return_exceptions=True))
        loop.close()