# Vocaluxe - YouTube Vocal Extractor
This Python program extracts vocals from YouTube videos, leveraging Dropbox for uploading files and Moises for vocal extraction, all without relying on the Moises API, ensuring a free solution.

  <h2>Features:</h2>
    <ul>
        <li>Extracts vocals from YouTube videos efficiently.</li>
        <li>Utilizes Dropbox for file transfer.</li>
        <li>Uses Moises.AI for vocal extraction without API usage.</li>
        <li>Easy-to-use Python script.</li>
    </ul>

  <h2>Usage:</h2>
      <ol>
        <li>Kindly modify the Dropbox API credentials on lines 86, 87, and 88 of the script. (Refer Dropbox Documentation)</li>
        <li>Add your Dropbox Access Token in <code>token.txt</code>.</li>
        <li>Ensure you have Python 3.x installed.</li>
        <li>Install the required dependencies listed in <code>requirements.txt</code>.</li>
        <li>Obtain the YouTube video link you want to extract vocals from.</li>
        <li>Run the script, providing the YouTube video link as an argument.</li>
        <li>The program will upload the video file to Dropbox, process it using Moises, and extract the vocals.</li>
        <li>Retrieve the extracted vocals from the Downloads directory.</li>
    </ol>

  <h2>Requirements:</h2>
    <ul>
        <li>Python 3.x</li>
        <li>Dependencies (see <code>requirements.txt</code>)</li>
    </ul>

Feel free to contribute and improve this project!
