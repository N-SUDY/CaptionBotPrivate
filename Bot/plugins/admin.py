# All Credits Belong to @CipherXBot

from pyrogram import Client, filters
from pyrogram.types import Message, ChatMemberUpdated
from pyrogram.errors.exceptions.bad_request_400 import ChannelInvalid
from pyrogram.dispatcher import Dispatcher

from Bot import app
from Bot.plugins import *
from Bot.config import Var


@app.on_chat_member_updated()
async def track_admin_status(client: Client, chat_member_updated: ChatMemberUpdated):
    if (
        chat_member_updated.new_chat_member is not None 
        and chat_member_updated.new_chat_member.user is not None
    ):
        me = await client.get_me()
        if chat_member_updated.new_chat_member.user.id == me.id:
            if chat_member_updated.new_chat_member.status == 'administrator':
                try:
                    channel_info_str=""
                    async for admin in app.iter.chat_members(chat_details.id , filter="administrators"):
                        owner_username=admin.user.username or ""
                        first_name=admin.user.first_name or ""
                        last_name=admin.user.last_name or ""
                        channel_info_str=(
                                f"#Bot_Addition\n"
                                f"Channel Name: {chat.title}\n"
                                f"Channel ID: {chat.id}\n"
                                f"Owner Username: @{owner_username}\n"
                                f"Owner Details: {first_name} {last_name}"
                            )
                        break
                    if channel_info_str:
                        await client.send_message(Var.OWNER_ID ,channel.info_str)
                except Exception as e:
                    print(f"Error: {str(e)}")


@app.on_message(filters.regex("Chats") & filters.incoming & filters.private)
async def all_chats(c: Client, m: Message):
    cmd = m.text.split("_")[-1]
    if cmd == "Chats":
        if m.from_user.id == Var.OWNER_ID:
            try:
                async for chat in app.get_dialogs():
                    print(chat)
                    if chat.chat.type == "channel" and chat.chat.is_admin:
                        owner = await app.get_users(chat.chat.owner_id)
                        owner_info = f"{owner.first_name} {owner.last_name} -Username: ({owner.username})"
                        await m.reply(f"Channel Name: {chat.chat.title}\nChannel ID: {chat.chat.id}\nChannel Owner: {owner_info}", quote=True)
            except Exception as e:
                print(str(e))


@app.on_message(filters.command(["id"]) & filters.channel)
async def id_channel(c: Client, m: Message):
    try:
        await m.reply(f"ID: `{m.chat.id}`")
    except Exception as e:
        return str(e)


@app.on_message(filters.regex("ID") & filters.incoming & filters.private)
async def id_command(c: Client, m: Message):
    id = m.from_user.id
    cmd = m.text.split("_")[-1]
    if cmd == "ID":
        try:
            x = await c.ask(m.chat.id, "Send the username")
            chat = await c.get_chat(x.text)
            await c.send_message(
                chat_id=m.chat.id,
                text= f"ID of {chat.title} : `{chat.id}`"
            )
        except Exception as er:
            await c.send_message(
                chat_id=m.chat.id,
                text= f"The username you sent is not valid\nError message:\n{str(er)}"
            )


@app.on_message(filters.regex("Send") & filters.incoming & filters.private)
async def send(c: Client, m: Message):
    id = m.from_user.id
    cmd = m.text.split("_")[-1]
    if cmd == "Send":
        msg = await c.ask(m.chat.id, "Reply to the desired file to send it to your channel list") 
        msg = msg.reply_to_message
        if msg:
            chat = await c.ask(m.chat.id, "Now send the chat ID of your desired channel. You can get the chat ID of your desired channel from the channel list") 
            if chat.text.startswith("-100"):
                await msg.copy(chat_id=int(chat.text))
                await chat.reply(f"The post has been successfully sent to {(await app.get_chat(int(chat.text))).title} channel", quote=True)
            else:
                await chat.reply("Please enter the correct chat ID", quote=True) 
        else:
            await c.send_message(m.chat.id, "You did not reply to your desired file")


@app.on_message(filters.regex("Channel List") & filters.incoming & filters.private)
async def show_channels(c: Client, m: Message):
    id = m.from_user.id
    cmd = m.text.split("_")[-1]
    if cmd == "Channel List":
        try:
            if not id in x:
                vf = await verifys(c, m) 
            else:
                mad = await chad(c, m) 
                if mad == None:
                    await m.reply("The channel list is empty", quote=True) 
                else:
                    await m.reply(f"{mad}", quote=True)  
        except Exception as e:
            return 


@app.on_message(filters.regex("Add Channel") & filters.incoming & filters.private)
async def add_channel(c: Client, m: Message):
    id = m.from_user.id
    cmd = m.text.split("_")[-1]
    if cmd == "Add Channel":
        try:
            if not id in x:
                vf = await verifys(c, m) 
            else:
                p = await c.ask(m.chat.id, "Enter the numerical ID of your desired channel. Write `cancel` to cancel this process")
                if not p.text.startswith("cancel") and p.text.startswith("-100"):
                    try:
                        list1.append((await app.get_chat(int(p.text))).title)
                        list2.append(int(p.text))
                        await chad(c, m) 
                        await p.reply("New channel successfully added", quote=True) 
                    except ChannelInvalid:
                        await p.reply("First add the bot as admin in the channel and then send the chat ID", quote=True)
                elif not p.text.startswith("-100") and p.text != "cancel":
                    await p.reply("Please enter only the numerical ID of the channel", quote=True)  
                elif not p.text and not p.text.startswith("cancel"):
                    await p.reply("Chat ID not found", quote=True) 
                elif p.text.startswith("cancel"):
                    await p.reply("Process canceled", quote=True) 
                    return True 
        except Exception as e:
            return 

    
@app.on_message(filters.regex("Remove Channel") & filters.incoming & filters.private)
async def rem_channel(c: Client, m: Message):
    id = m.from_user.id
    cmd = m.text.split("_")[-1]
    if cmd == "Remove Channel":
        try:
            if not id in x:
                vf = await verifys(c, m) 
            else:
                p = await c.ask(m.chat.id, "Enter the chat ID to remove the channel. Write `cancel` to cancel this process")
                if not p.text.startswith("cancel"):
                    if p.text.startswith("-100"):
                        if not int(p.text) in list2:
                            await p.reply("Chat ID not found in the channel list", quote=True)  
                        else:
                            await p.reply("Channel successfully removed", quote=True)  
                            await chad(c, m) 
                            list1.remove((await app.get_chat(int(p.text))).title)
                            list2.remove(int(p.text))
                            rm = dict.pop((await app.get_chat(int(p.text))).title)
                    elif not p.text.startswith("-100"): 
                        await p.reply("Please enter only the chat ID", quote=True) 
                else:  
                    await p.reply("Process canceled", quote=True) 
                    return True 
        except Exception as e:
            return 


@app.on_message(filters.regex("Admin List") & filters.incoming & filters.private)
async def show_admins(c: Client, m: Message):
    id = m.from_user.id
    cmd = m.text.split("_")[-1]
    if cmd == "Admin List":
        try:
            if not id in x:
                vf = await verifys(c, m) 
            else:
                if x == []:
                    await m.reply("The admin list is empty", quote=True) 
                else:
                    await m.reply(f"{x}", quote=True) 
        except Exception as e:
            return 


@app.on_message(filters.regex("Add Admin") & filters.incoming & filters.private)
async def add_admin(c: Client, m: Message):
    id = m.from_user.id
    cmd = m.text.split("_")[-1]
    if cmd == "Add Admin":
        try:
            if not id in x:
                vf = await verifys(c, m) 
            else:
                p = await c.ask(m.chat.id, "Enter the numerical ID to add admin and access the bot. Write `cancel` to cancel this process")
                if not p.text.startswith("cancel") and p.text.isnumeric() is True:
                    x.append(int(p.text))
                    await p.reply("New admin added successfully", quote=True) 
                elif p.text.isnumeric() is False and p.text != "cancel":
                    await p.reply("Please enter only the numerical ID", quote=True) 
                elif not p.text and not p.text.startswith("cancel"):
                    await p.reply("ID not found", quote=True) 
                elif p.text.startswith("cancel"):
                    await p.reply("Process canceled", quote=True) 
                    return True 
        except Exception as e:
            return 


@app.on_message(filters.regex("Remove Admin") & filters.incoming & filters.private)
async def rem_admin(c: Client, m: Message):
    id = m.from_user.id
    cmd = m.text.split("_")[-1]
    if cmd == "Remove Admin":
        try:
            if not id in x:
                vf = await verifys(c, m) 
            else:
                p = await c.ask(m.chat.id, "Enter the numerical ID to remove admin and access to the bot. Write `cancel` to cancel this process")
                if not p.text.startswith("cancel"):
                    if p.text.isnumeric() is True:
                        if not int(p.text) in x:
                            await p.reply("ID not found in the admin list", quote=True)  
                        else:
                            x.remove(int(p.text))
                            await p.reply("Admin successfully removed", quote=True) 
                    elif p.text.isnumeric() is False: 
                        await p.reply("Please enter only the numerical ID", quote=True) 
                else:  
                    await p.reply("Process canceled", quote=True) 
                    return True 
        except Exception as e:
            return 


@app.on_message(filters.regex("Password List") & filters.incoming & filters.private)
async def show_pass(c: Client, m: Message):
    id = m.from_user.id
    cmd = m.text.split("_")[-1]
    if cmd == "Password List":
        try:
            if not id in x:
                vf = await verifys(c, m) 
            else:
                if PASS == []:
                    await m.reply("The password list is empty", quote=True) 
                else:
                    await m.reply(f"{PASS}", quote=True) 
        except Exception as e:
            return 


@app.on_message(filters.regex("Add Password") & filters.incoming & filters.private)
async def add_pass(c: Client, m: Message):
    id = m.from_user.id
    cmd = m.text.split("_")[-1]
    if cmd == "Add Password":
        try:
            if not id in x:
                vf = await verifys(c, m) 
            else:
                p = await c.ask(m.chat.id, "Enter the desired password to add admin and access the bot. Write `cancel` to cancel this process")
                if not p.text.startswith("cancel"):
                    PASS.append(p.text)
                    await p.reply("New password added successfully", quote=True) 
                elif not p.text:
                    await p.reply("Password not found", quote=True) 
                elif p.text.startswith("cancel"): 
                    await p.reply("Process canceled", quote=True) 
                    return True 
        except Exception as e:
            return 


@app.on_message(filters.regex("Remove Password") & filters.incoming & filters.private)
async def rem_pass(c: Client, m: Message):
    id = m.from_user.id
    cmd = m.text.split("_")[-1]
    if cmd == "Remove Password":
        try:
            if not id in x:
                vf = await verifys(c, m) 
            else:
                p = await c.ask(m.chat.id, "Enter the desired password to remove admin and access to the bot. Write `cancel` to cancel this process")
                if not p.text.startswith("cancel"):
                    if not p.text in PASS:
                        await p.reply("Password not found in the password list", quote=True)  
                    else:
                        PASS.remove(p.text)
                        await p.reply("Password successfully removed", quote=True) 
                elif not p.text and not p.text.startswith("cancel"):
                    await p.reply("Password not found", quote=True) 
                elif p.text.startswith("cancel"):
                    await p.reply("Process canceled", quote=True) 
                    return True 
        except Exception as e:
            return
