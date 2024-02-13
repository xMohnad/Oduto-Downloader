# Oduto Downloader
يقوم [السكربت](https://github.com/xMohnad/Oduto-Downloader/blob/main/Script/main.py) بتنزيل الفصول من مدونة [Oduto](https://nb19u.blogspot.com) وأي مدونة بنفس القالب.

# تشغيل السكربت على الجوال(أي سكربت):
أولًا تنزيل [Termux](https://github.com/termux/termux-app#github) وتثبيته

بعد تثبيته تحتاج لتحديث الحزم وتنزيل اللغة والمكتبات المستخدمة في السكربت وهي:

### قم بتثبت (بالترتيب):

`pkg upgrade`


`pkg install python`

`pip install beautifulsoup4 requests tqdm`


## تشغيل سكربت بايثون في Termux


بعد تنزيلهم قم بنسخ ملف بايثون الى خارج الملفات واكتب: `cd /sdcard` للذهاب إليه (تأكد من إعطائة إذن الوصول إلى الملفات، يمكنك عمل ذلك من الإعدادات إذا لم يطلب ذلك)



يمكنك الآن تفقد ملفاتك عبر `ls` اذا لم تجد الملف تأكد من نسخه إلى المكان المطلوب

إذا وجدته يمكنك تشغيله عبر `python اسم_الملف.py`(استبدل "اسم_الملف" بالذي لديك)  وقم بإضافة رابط الفصل وسيقوم بتنزيله.
# طريقة أخرى
بعد تثبيت ما ذُكِر يمكنك إنشاء ملف بكتابة `nano oduto.py` ولصق [السكربت](https://github.com/xMohnad/Oduto-Downloader/blob/main/Script/main.py) فيه وتشغيله بكتابة `python oduto.py`

# لأي سؤال:

[Twitter / X](https://x.com/xMohnad13)

