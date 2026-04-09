[app]
title = AI Colorizer Lite
package.name = colorizerwasim
package.domain = org.wasim
source.dir = .
source.include_exts = py,png,jpg,kv,txt
version = 0.1

# ১. সঠিক রিকোয়ারমেন্টস (Pillow ছোট হাতের অক্ষরে)
requirements = python3,kivy==2.3.0,pillow,numpy,requests

orientation = portrait
fullscreen = 0
android.archs = arm64-v8a, armeabi-v7a

# ২. স্টোরেজ এবং ইন্টারনেট পারমিশন
android.permissions = INTERNET, READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE, MANAGE_EXTERNAL_STORAGE

# ৩. অ্যান্ড্রয়েড সেটিংস
android.api = 33
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license = True
android.skip_update = False

# ৪. লগক্যাট ফিল্টার (আপনার দেয়া সেটিংস)
android.logcat_filters = *:S python:D

# ৫. হোয়াইটলিস্ট (ইমেজ প্রসেসিং ফিক্স)
android.whitelist = lib-dynload/_imaging.so

[buildozer]
log_level = 2
warn_on_root = 1
