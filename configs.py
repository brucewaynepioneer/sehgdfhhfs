import os
class Config:
    API_ID =  '26482070' #int(os.environ.get('API_ID', 0))
    API_HASH = '28f1d67e2693e057ae4611521c555136' #str(os.environ.get('API_HASH', None))
    BOT_TOKEN = '6557432874:AAGywcrSYYwKE9o_r3foRzfVM6khPLgPMxk' #str(os.environ.get('BOT_TOKEN', None))
    MONGO_URI = 'mongodb+srv://knight_rider:GODGURU12345@knight.jm59gu9.mongodb.net/?retryWrites=true&w=majority' #str(os.environ.get('MONGO_URI', None))
    UPDATES_CHANNEL = 'dev_gagan' #str(os.environ.get('UPDATES_CHANNEL', None)) #Start Without @
