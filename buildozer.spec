[app]
title = AI Colorizer
package.name = colorizerwasim
package.domain = org.wasim
source.dir = .
source.include_exts = py,png,jpg,kv,txt
version = 0.1

# প্রয়োজনীয় লাইব্রেরি (OpenCV ছাড়া, তাই খুব দ্রুত হবে)
requirements = python3,kivy==2.3.0,Pillow,numpy,requests

orientation = portrait
android.archs = arm64-v8a, armeabi-v7a
android.permissions = INTERNET, READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE
android.api = 33
android.minapi = 21
android.accept_sdk_license = True

[buildozer]
log_level = 2
warn_on_root = 1
