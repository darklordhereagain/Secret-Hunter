# 🔐 Secret-Hunter

Secret-Hunter is a **multi-functional educational toolkit** for analyzing logs, filtering credentials, and testing login endpoints.  
It features filtering, service checkers (cPanel, SMTP, WordPress), and an exclusive data classifier.  

> ⚠️ **Disclaimer:** This project is for **educational and research purposes only**. Misuse is strictly prohibited.  

---

## 🧰 Requirements  

- ✅ Python **3.10+**  
- ✅ `git` installed  
- ✅ Internet connection  
- ✅ Works on **Windows / Linux / Termux (Android)**  

---

## ⚙️ Installation Guide  

### 📱 Termux (Android)  
```bash
pkg update && pkg upgrade -y
pkg install python git -y
pkg install libandroid-support -y
rm -rf Secret-Hunter
git clone --depth=1 https://github.com/darklordhereagain/Secret-Hunter
cd Secret-Hunter
pip install -r requirements.txt
termux-setup-storage
python Secret_Hunter.py
```

### 💻 Linux / Windows  
```bash
git clone https://github.com/darklordhereagain/Secret-Hunter.git
cd Secret-Hunter
python -m venv venv
source venv/bin/activate    # Linux/Mac
venv\Scripts\activate       # Windows
pip install -r requirements.txt
python Secret_Hunter.py
```

## 🚀 Features  

- 📂 **Log Filter** → Extracts credentials from raw log files  
- 🌐 **cPanel/WHM/Webmail Checker** → Test login endpoints  
- 📧 **SMTP Checker** → Verify email servers and send test mail  
- 🔑 **WordPress Checker** → Validate login details  
- 🗂️ **Exclusive Filter** → Sorts Social, Mail, Bank, Crypto, Cookies & Card data  
- 📊 **Auto Reports** → Saves output with banners and timestamps  
- 🖥️ **System Info** → Collect OS, processes, metadata  
