import traceback
from pyrogram import *
from pyrogram.types import *
from .gen import generate_session, ask_ques, buttons_ques
from Amang import *


@app.on_callback_query(filters.regex(pattern=r"^(generate|pyrogram|jasa_repo|multi_funsgi|helpernya|telethon)$"))
async def _callbacks(bot: Client, callback_query: CallbackQuery):
    query = callback_query.data.lower()
    user = await bot.get_me()
    mention = user.mention
    await callback_query.message.delete()
    if query == "generate":
        await callback_query.answer()
        await callback_query.message.reply(ask_ques.format(callback_query.from_user.first_name), reply_markup=InlineKeyboardMarkup(buttons_ques))
    elif query == "jasa_repo":
        await callback_query.message.reply(
            text="""
𝙅𝘼𝙎𝘼 𝘿𝙀𝙋𝙇𝙊𝙔 𝘽𝙊𝙏 𝙏𝙀𝙇𝙀𝙂𝙍𝘼𝙈
🚀 𝙐𝙎𝙀𝙍𝘽𝙊𝙏 𝙂𝘾𝘼𝙎𝙏
├ ʀᴘ. 30.000  [ ʙᴜʟᴀɴᴀɴ ᴜsᴇʀʙᴏᴛ ]
└ sɪsᴛᴇᴍ ᴛᴇʀɪᴍᴀ ᴊᴀᴅɪ
🚀 𝘽𝙊𝙏 𝙈𝙐𝙎𝙄𝙆
├ ʀᴘ. 180.000 [ ᴠᴘs/1ʙᴜʟᴀɴ ]
├ ᴀᴡᴀʟᴀɴ ᴘᴀsᴀɴɢ
└ sɪsᴛᴇᴍ ᴛᴇʀɪᴍᴀ ᴊᴀᴅɪ
🚀 𝘽𝙊𝙏 𝙈𝙐𝙎𝙄𝙆 & 𝙈𝘼𝙉𝘼𝙂𝙀
├ ʀᴘ. 10.000  [ ᴄʟᴏɴᴇ ɢʜ ]
├ ʀᴘ. 300.000  [ ᴅᴇᴘʟᴏʏ + ʜᴇʀᴏᴋᴜ + ᴠᴘs ]
└ sɪsᴛᴇᴍ ᴛᴇʀɪᴍᴀ ᴊᴀᴅɪ
🚀 𝘽𝙊𝙏 𝙈𝘼𝙉𝘼𝙂𝙀
├ ʀᴘ. 80.000 [ ʜᴇʀᴏᴋᴜ ]
└ sɪsᴛᴇᴍ ᴛᴇʀɪᴍᴀ ᴊᴀᴅɪ
ᴄᴀᴛᴀᴛᴀɴ:
1. ᴀᴘᴀʙɪʟᴀ ʙᴏᴛ ʏᴀɴɢ ᴀɴᴅᴀ ɪɴɢɪɴᴋᴀɴ ᴛɪᴅᴀᴋ ᴀᴅᴀ ᴅɪᴀᴛᴀs, sɪʟᴀᴋᴀɴ ᴘᴍ AMANG
2. ᴄᴀᴛᴀᴛᴀɴ ʜᴇʀᴏᴋᴜ ʀᴀᴡᴀɴ sᴜsᴘᴇɴ ᴊᴀᴅɪ sᴀʏᴀ ᴅᴇᴘʟᴏʏ ᴅɪ ᴠᴘs.
3. sɪʟᴀʜᴋᴀɴ ʜᴜʙᴜɴɢɪ AMANG ᴜɴᴛᴜᴋ ᴍᴇʟɪʜᴀᴛ / ᴍᴇɴᴀɴʏᴀᴋᴀɴ ᴄᴏɴᴛᴏʜ ʙᴏᴛ.
𝗦𝗘𝗞𝗜𝗔𝗡 𝗧𝗘𝗥𝗜𝗠𝗔 𝗞𝗔𝗦𝗜𝗛 🙏.
""",
          reply_markup=InlineKeyboardMarkup(
              [
                [
                  InlineKeyboardButton(
                    text="Amang",
                    user_id=OWNER_ID),
                ],
                [
                  InlineKeyboardButton(
                    text="Kembali",
                    callback_data="ahh_ajg"),
                ],
              ]
            ),
        )
    elif query == "multi_funsgi":
        await callback_query.message.reply(
            text="""
Daftar Perintah Multi Fungsi Bot Amang 🤖

Jika menemukan Kendala atau Masalah, silahkan hubungi @amwangsupport atau @amwang
""",
          reply_markup=InlineKeyboardMarkup(
              [
                [
                  InlineKeyboardButton(
                    text="Fsub Premium",
                    url=f"https://t.me/FileSharingPremium_Bot"),
                  InlineKeyboardButton(
                    text="Ubot Premium",
                    url=f"https://t.me/PremiumGcast2bot"),
                ],
                [
                  InlineKeyboardButton(
                    text="Kembali",
                    callback_data="ahh_ajg"),
                ],
              ]
            ),
        )
    elif query == "helpernya":
        await callback_query.message.reply(
            text="""
Berikut Adalah Daftar Perintah Untuk Manage & Music
""",
          reply_markup=InlineKeyboardMarkup(
              [
                [
                  InlineKeyboardButton(
                    text="Manage",
                    callback_data="bot_commands"),
                  InlineKeyboardButton(
                    text="Music",
                    callback_data="settings_back_helper"),
                ],
                [
                  InlineKeyboardButton(
                    text="Kembali",
                    callback_data="ahh_ajg"),
                ],
              ]
            ),
        )
    elif query.startswith("pyrogram") or query.startswith("telethon"):
        try:
            if query == "pyrogram":
                await callback_query.answer()
                await generate_session(bot, callback_query.message)
            elif query == "telethon":
                await callback_query.answer()
                await generate_session(bot, callback_query.message, telethon=True)
        except Exception as e:
            print(traceback.format_exc())
            print(e)
            await callback_query.message.reply(ERROR_MESSAGE.format(str(e)))


ERROR_MESSAGE = "Buset Eror Jink! \n\n**Error** : {} " \
            "\n\nCoba Lu Ngadu Sono Ke @amwangsupport"
