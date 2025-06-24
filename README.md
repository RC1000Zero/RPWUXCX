# Wii U Rich Presence Plugin - Database
Image database for the [Wii U Rich Presence plugin](https://github.com/FlamingNineteen/RichPresenceWUPS).
<!-- ## Contribute
To add games that are not yet listed, you can use [WiiUDownloader](https://github.com/Xpl0itU/WiiUDownloader) to get the data, and create a pull request to add the game.

In WiiUDownloader, you can download decrypted game contents. Select the game(s) you want to add, then toggle "Decrypt contents" before downloading. **Be aware of the game's region.**

Once the contents are decrypted, open the `meta` folder. `iconTex.tga` is the game's icon. Use a file converter to convert this file to a jpg file, and use an image upscaler to upscale the image to 512x512 if necessary.

Additionally, there should be a `meta.xml` file. In that file, find the `longname` tags. These are the names the plugin uses to match images.

Fork this repository, and add your image to the `icon` folder. Keep the file name short, like an acronym of the game's title. Then in `titles.json`, add keys to the image for every `shortname` tag in `meta.xml`. Do not include duplicates. Here is an example for LEGO® Marvel Superheroes: `"LEGO® Marvel":"legoms.jpg"`

Finally, create a pull request, and delete the decrypted contents of your game(s).

The Python script in this repository `add.py` can be used to automate adding the images and keys to the repository. Run the script and fill out the information in a terminal. -->