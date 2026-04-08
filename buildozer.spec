[app]
title = AI Video Colorizer
package.name = colorizer
package.domain = org.wasim
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,prototxt,npy,txt
version = 0.1

# রিকোয়ারমেন্টস (ভার্সন নির্দিষ্ট করে দেওয়া হলো স্ট্যাবিলিটির জন্য)
requirements = python3,kivy==2.3.0,opencv-python,numpy,requests,urllib3,certifi

orientation = portrait
fullscreen = 0
android.archs = arm64-v8a, armeabi-v7a

# পারমিশন
android.permissions = INTERNET, READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE, MANAGE_EXTERNAL_STORAGE

# বিল্ড সেটিংস (খুবই গুরুত্বপূর্ণ)
android.api = 33
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license = True
android.skip_update = False

# বড় লাইব্রেরির জন্য মেমোরি এবং টাইমআউট সেটিংস
android.entrypoint = main.py
p4a.branch = master

# গ্রাফিক্স এবং রিসোর্স
source.include_patterns = *.prototxt,*.npy

[buildozer]
log_level = 2
warn_on_root = 1
