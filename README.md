# HomeStorageManager
The Home Storage Manager helps you organize and keep track of your stuff at home. It makes it easy to know where everything is. Perfect for staying tidy and finding things quickly!

## Installation

docker run -d --name homestoragemanger --restart=unless-stopped -p 8000:8000 -e HOSTNAMEANDPORT=127.0.0.1:8000 -v $(pwd)/media:/hsm/media -v $(pwd)/db:/hsm/db robinklepzig/homestoragemanager:latest
