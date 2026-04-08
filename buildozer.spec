[app]
title = AI Video Colorizer
package.name = colorizer
package.domain = org.wasim
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,prototxt,caffemodel,npy,txt
version = 0.1

# যে যে লাইব্রেরি প্রয়োজন (এখানে requests যোগ করা হয়েছে ডাউনলোডের জন্য)
requirements = python3,kivy,opencv-python,numpy,requests,urllib3

orientation = portrait
fullscreen = 0
android.archs = arm64-v8a, armeabi-v7a

# পারমিশন (ইন্টারনেট পারমিশন অবশ্যই লাগবে ফাইল ডাউনলোডের জন্য)
android.permissions = INTERNET, READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE, MANAGE_EXTERNAL_STORAGE

# অ্যান্ড্রয়েড এপিআই লেভেল
android.api = 33
android.minapi = 21

[buildozer]
log_level = 2
warn_on_root = 1
