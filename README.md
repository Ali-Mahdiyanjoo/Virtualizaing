<h1 align="center">Welcome to GMS <img src="https://raw.githubusercontent.com/MartinHeinz/MartinHeinz/master/wave.gif" width="30px"> </h1>
<p align="center">

[![GitHub license](https://img.shields.io/github/license/Naereen/StrapDown.js.svg)](https://github.com/Naereen/StrapDown.js/blob/master/LICENSE)
![](https://img.shields.io/badge/OS-Linux-informational?style=flat&logo=linux&logoColor=white&color=40c640)
![](https://img.shields.io/badge/Code-Python-informational?style=flat&logo=python&logoColor=white&collor)
![](https://img.shields.io/badge/Shell-Bash-informational?style=flat&logo=gnu-bash&logoColor=white&color=40c640)
    
## Description 
All of us need to monitor our hardware to achieve more from our machine especially GPU for model training, monitoring large scale machines that have GPU is not an easy thing to do, so because of that, I made this GMS(GPU Monitoring Service) to help you to do in the right way.
* Note: this service just run on Linux machine and Nvidia GPU for now, and for and better user experience use firefox :))

## Installation <img src="https://media.giphy.com/media/WUlplcMpOCEmTGBtBW/giphy.gif" width="30"> 
</em></p>

1. Clone project
```
git clone https://github.com/Ali-Mahdiyanjoo/Virtualizaing
```

2. Install requirements in the virtual environment
- for the instruction on installing a virtual environment check [this](https://stackoverflow.com/questions/23842713/using-python-3-in-virtualenv).
```
pip3 install -r requirements.txt
```

3. Install MongoDB if it's not been installed before on your system.
```
sudo apt install mongodb
sudo systemctl start mongodb.service
```

4. Create DB in MongoDB name "GPU_MONITORING"
```
use DATABASE_NAME
```

5. Create 2 collection in "GPU_MONITORING" DB names: "DATAS" (for data with history line) & "DATAS_SINGLE" (for data updating instantly).

```
db.creatCollection("name")
```

6. Copy the following files for GPU info gathering in the machine you want.

* just before transforming change ip in nvidia-smi-collector.sh to ip of the machine you are running this code

```
sudo cp nvidia-smi-collector-json nvidia-smi-collector.sh /usr/sbin
sudo cp nvidia-smi-collector.service /etc/systemd/system
```

7. Enable and start nvidia-smi-collector.service
```
sudo systemctl enable nvidia-smi-collector.service
sudo systemctl start nvidia-smi-collector.service
```
8. In the last run All_seervice.py
  
  ```
  python3 All_service.py
  ```

##  <img src="https://media.giphy.com/media/LnQjpWaON8nhr21vNW/giphy.gif" width="60"> Contributing

Contributions, issues and feature requests are welcome.<br />
Feel free to check [issues page](https://github.com/adib-vali/DataPanel_Project/issues) if you want to contribute.<br />
[Check the contributing guide](./CONTRIBUTING.md).<br />

## 👩‍💻 Authors 👨‍💻

👤 **Ali mahdiyanjoo**

- Github: [@Ali-Mahdiyanjoo](https://github.com/Ali-Mahdiyanjoo)
- Linkedin: [@Ali-Mahdiyanjoo](https://www.linkedin.com/in/ali-mahdiyanjoo-1452101b6)

## 📝 License
Datapanel analyzer is primarily distributed under the terms the [MIT](https://github.com/kefranabg/readme-md-generator/blob/master/LICENSE)
 license.
