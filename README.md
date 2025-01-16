![CoverImage](https://raw.githubusercontent.com/RobinKlepzig/HomeStorageManager/refs/heads/main/misc/cover-image.png)
# HomeStorageManager
The Home Storage Manager helps you organize and keep track of your stuff at home. It makes it easy to know where everything is. Perfect for staying tidy and finding things quickly!

> [!WARNING]  
> The web app has not yet been tested for hosting on the Internet and extended and debug error messages are also displayed

> [!CAUTION]
> After registration, it is recommended that the user logs out and logs in again

## Basic installation
```
docker run -d --name homestoragemanger --restart=unless-stopped -p 8000:8000 -e HOSTNAMEANDPORT=127.0.0.1:8000 robinklepzig/homestoragemanager:latest
```
### Parameter
HOSTNAMEANDPORT: under the hostname and port where the docker container is running

> [!IMPORTANT]  
> Using the app with reserve proxies is not yet supported

## Extended installation
```
docker run -d --name homestoragemanger --restart=unless-stopped -p 8000:8000 -e HOSTNAMEANDPORT=127.0.0.1:8000 -v $(pwd)/media:/hsm/media -v $(pwd)/db:/hsm/db robinklepzig/homestoragemanager:latest
```

### Parameter
HOSTNAMEANDPORT: under the hostname and port where the docker container is running

> [!IMPORTANT]  
> Using the app with reserve proxies is not yet supported

/hsm/media: here the images are stored locally

/hsm/db: here the db are stored locally

> [!CAUTION]
> So far no initial installation works without contents in the local folders, so it is necessary to manually copy the contents from the HomeStorageManager/*-initial folders beforehand

