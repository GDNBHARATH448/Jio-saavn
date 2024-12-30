from pyrogram import Client, filters
import json

# Replace with your own API ID, API Hash, and Bot Token
api_id = 'YOUR_API_ID'
api_hash = 'YOUR_API_HASH'
bot_token = 'YOUR_BOT_TOKEN'

app = Client("admin_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

# Load admin data from a JSON file
def load_admins():
    try:
        with open("admins.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Save admin data to a JSON file
def save_admins(admins):
    with open("admins.json", "w") as file:
        json.dump(admins, file)

# Initialize admin list
admins = load_admins()

# Check if a user is an admin
def is_admin(user_id):
    return user_id in admins

# Add a new admin (only by existing admins)
@app.on_message(filters.command("addadmin") & filters.user(admins))
async def add_admin(client, message):
    if len(message.command) == 2:
        try:
            new_admin_id = int(message.command[1])
            if new_admin_id not in admins:
                admins.append(new_admin_id)
                save_admins(admins)
                await message.reply_text(f"User {new_admin_id} added as admin.")
            else:
                await message.reply_text("User is already an admin.")
        except ValueError:
            await message.reply_text("Invalid user ID.")
    else:
        await message.reply_text("Usage: /addadmin <user_id>")

# Remove an admin (only by existing admins)
@app.on_message(filters.command("removeadmin") & filters.user(admins))
async def remove_admin(client, message):
    if len(message.command) == 2:
        try:
            remove_admin_id = int(message.command[1])
            if remove_admin_id in admins:
                admins.remove(remove_admin_id)
                save_admins(admins)
                await message.reply_text(f"User {remove_admin_id} removed from admins.")
            else:
                await message.reply_text("User is not an admin.")
        except ValueError:
            await message.reply_text("Invalid user ID.")
    else:
        await message.reply_text("Usage: /removeadmin <user_id>")

# List all admins
@app.on_message(filters.command("listadmins") & filters.user(admins))
async def list_admins(client, message):
    if admins:
        admin_list = "\n".join([str(admin) for admin in admins])
        await message.reply_text(f"Admins:\n{admin_list}")
    else:
        await message.reply_text("No admins found.")

app.run()
