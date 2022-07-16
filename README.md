
# Python Port Scanner

Python port scanner which can scan and grab banner provided you give the IP address of the host that is needed to be scanned.

1)one single port  -> 22

2)mutiple ports    ->  22,25,80

3)range of ports   ->  22-80


## Deployment

To deploy this script run (make sure to run the tool in an isolated environment using -I)

```bash
  python3 -I pyscan.py -host <IP-Address> -port <Port Number>
```
## For single port
```bash
  python3 -I pyscan.py -host <IP-Address> -port 22
```
## For mutiple ports
```bash
  python3 -I pyscan.py -host <IP-Address> -port 22,80,25,21
```
## For range of ports
```bash
  python3 -I pyscan.py -host <IP-Address> -port 22-80
```



## Screenshots

![image](https://user-images.githubusercontent.com/106553324/179363839-97e446c6-a10a-48ab-8818-3571448f379b.png)


![image](https://user-images.githubusercontent.com/106553324/179363853-7a6a4aff-268d-4104-83c4-afc2a28d7024.png)


![image](https://user-images.githubusercontent.com/106553324/179363868-a3efb463-ada4-4b01-97a2-4549e487688b.png)

