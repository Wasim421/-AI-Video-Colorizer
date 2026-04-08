[app]
title = AI Video Colorizer
package.name = colorizer
package.domain = org.wasim
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,prototxt,npy,txt
version = 0.1

# OpenCV এবং Numpy এর জন্য রিকোয়ারমেন্টস
requirements = python3,kivy==2.3.0,opencv-python,numpy,requests,urllib3

orientation = portrait
fullscreen = 0
android.archs = arm64-v8a, armeabi-v7a

# পারমিশন (ইন্টারনেট এবং স্টোরেজ)
android.permissions = INTERNET, READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE, MANAGE_EXTERNAL_STORAGE

# অ্যান্ড্রয়েড এসডিকে সেটিংস
android.api = 33
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license = True
android.skip_update = False

# ফাইল ইনক্লুশন (বড় মডেল ফাইলটি যেহেতু ডাউনলোড হবে, তাই এখানে caffemodel বাদ দেওয়া হয়েছে)
source.include_patterns = assets/*,*.prototxt,*.npy

[buildozer]
log_level = 2
warn_on_root = 1
