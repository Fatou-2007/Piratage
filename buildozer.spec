[app]

title = piratage
package.name = piratage
package.domain = org.test

source.dir = .
source.include_exts = py,kv,png,jpg,ttf,txt,ogg,wav,mp3

version = 0.1

requirements = python3,kivy

orientation = portrait
fullscreen = 0


[buildozer]

log_level = 2
warn_on_root = 1

android.sdk = 33
android.ndk = 23b
android.ndk_api = 21
android.api = 33

android.archs = arm64-v8a, armeabi-v7a

android.build_tools_version = 33.0.2
