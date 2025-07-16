def config_check():

    import os

    # Specify the directory name and create the config directory if missing
    directory_name = "config"

    try:
        os.mkdir(directory_name)
        print("\nDirectory '{directory_name}' created successfully.")
    except:
        print("\nConfig folder already exists")

# Now checking wifi_config.txt
    try:
      f = open('config/wifi_config.txt', 'r') #makes an exception if not exist
      dummy_read = f.read()
      print('\nThe config/wifi_config.txt exists')
      f.close()
    except: #if it does not exist, then create it
      f = open('config/wifi_config.txt', 'w') #writing a new file
      f.write("Your Wi-Fi SSID" + "\n")
      f.write("Your Wi-Fi Password")
      f.close()
      print('\nCreated a new wifi_config.txt file\n')

# Now checking weather_config.txt
    try:
      f = open('config/weather_config.txt', 'r') #makes an exception if not exist
      dummy_read = f.read()
      print('\nThe config/weather_config.txt exists\n')
      f.close()
    except: #if it does not exist, then create it
      f = open('config/weather_config.txt', 'w') #writing a new file
      f.write("Scoresby" + ",")
      f.write("AU")
      f.close()
      print('\nCreated a new weather_config.txt file\n')

config_check() # Check relevant config folders/files exist, if not create them

