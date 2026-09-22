[app]

title = FILOT Pump Assistant
package.name = filot
package.domain = org.filot

source.dir = .
source.include_exts = py,png,jpg,jpeg,kv,atlas,json

version = 0.1

requirements = python3,kivy

orientation = portrait

fullscreen = 0


[buildozer]

log_level = 2

warn_on_root = 1


[android]

android.api = 35
android.minapi = 21

android.archs = arm64-v8a

android.allow_backup = False

android.accept_sdk_license = True[app]

title = FILOT Test

package.name = filottest

package.domain = com.kianelectronic

source.dir = .

source.include_exts = py,png,jpg,jpeg,kv,atlas

version = 1.0.0

requirements = python3,kivy

orientation = portrait

fullscreen = 0


[buildozer]

log_level = 2

warn_on_root = 1


[android]

android.api = 35

android.minapi = 23

android.accept_sdk_license = True
