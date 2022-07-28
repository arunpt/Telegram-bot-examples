from pyrogram import Client, filters
from pyrogram.raw import types
from pyrogram.raw import functions
from pyrogram.utils import get_channel_id

app = Client(
    "hmmm",
    api_id=12345,
    api_hash="abcedfghijklm23hb3bd",
    bot_token="5302586671:AAEaE31UqS9mCDOSCdqJYUhVa4LF_Uh9iss"
)


@app.on_message(filters.command("start"))
async def hello(_, message):
    await message.reply_text("hey")


@app.on_raw_update()
async def join_req(client, update, _, __):
    if isinstance(update, types.UpdateBotChatInviteRequester):
        channel = await client.resolve_peer(
            get_channel_id(update.peer.channel_id)
        )
        user = await client.resolve_peer(update.user_id)
        await client.send(
            functions.messages.HideChatJoinRequest(
                peer=channel,
                user_id=user,
                approved=True
            )
        )


app.run()
