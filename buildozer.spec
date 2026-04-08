[app]
title = AI Colorizer Lite
package.name = colorizerlite
package.domain = org.wasim
source.dir = .
source.include_exts = py,png,jpg,kv,txt
version = 0.1

# OpenCV বাদ দিয়ে শুধু Pillow রাখা হয়েছে
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
