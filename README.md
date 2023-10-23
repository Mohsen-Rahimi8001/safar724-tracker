# safar724-tracker

### Changing source and destination
you can send a get request to the getcities endpoint to get city codes.

### Linux
if you have a linux distro, you can use this command:

```watch -n [delay] python tracker.py -d <date> -s[optional]```

## Endpoints
### get cities

```https://safar724.com/route/getcities```

### search for bus

```https://safar724.com/bus/getservices?origin=<origin_code>&destination=<dest_code>&date=<date>```
