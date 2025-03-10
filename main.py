
# (str) Title of your application
title = My Application

# (str) Package name
package.name = lovelyapk

# (str) Package domain (needed for android/ios packaging)
package.domain = com.lovely.app

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas.gif

# (list) List of inclusions using pattern matching
#source.include_patterns = assets/*,images/*.png

# (list) Source files to exclude (let empty to not exclude anything)
#source.exclude_exts = spec

# (list) List of directory to exclude (let empty to not exclude anythi>
# source.exclude_dirs = tests, bin, venv

# (list) List of exclusions using pattern matching
# Do not prefix with './'
# source.exclude_patterns = license,images/*/*.jpg

# (str) Application versioning (method 1)
version = 0.1

# (str) Application versioning (method 2)
# version.regex = __version__ = ['"](.*)['"]
# version.filename = %(source.dir)s/main.py

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3,kivy,string,random

# (str) Custom source folders for requirements
# Sets custom source for any requirements with recipes
# requirements.source.kivy = ../../kivy

# (str) Presplash of the application
presplash.filename = %(source.dir)s/data/.gif

# (str) Icon of the application
icon.filename = %(source.dir)s/

# (list) Supported orientations
# Valid options are: landscape, portrait, portrait-reverse or landscap>
# orientation = portrait

# (list) List of service to declare
#services = NAME:ENTRYPOINT_TO_PY,NAME2:ENTRYPOINT2_TO_PY

#
# OSX Specific
#

#
# author = © Copyright Info

# change the major version of python used by the app
# osx.python_version = 3

# Kivy version to use# osx.kivy_version = 1.9.1

#
# Android specific
#

# (bool) Indicate if the application should be fullscreen or not
# fullscreen = 0

# (string) Presplash background color (for android toolchain)
# Supported formats are: #RRGGBB #AARRGGBB or one of the following nam>
# red, blue, green, black, white, gray, cyan, magenta, yellow, lightgr>
# darkgray, grey, lightgrey, darkgrey, aqua, fuchsia, lime, maroon, na>
# olive, purple, silver, teal.
#android.presplash_color = #FFFFFF

# (string) Presplash animation using Lottie format.
# see https://lottiefiles.com/ for examples and https://airbnb.design/>
# for general documentation.
# Lottie files can be created using various tools, like Adobe After Ef>
#android.presplash_lottie = "path/to/lottie/file.json"

# (str) Adaptive icon of the application (used if Android API level is>
#icon.adaptive_foreground.filename = %(source.dir)s/data/icon_fg.png
#icon.adaptive_background.filename = %(source.dir)s/data/icon_bg.png

# (list) Permissions
# (See https://python-for-android.readthedocs.io/en/latest/buildoption>
#android.permissions = android.permission.INTERNET, (name=android.perm>

# (list) features (adds uses-feature -tags to manifest)
#android.features = android.hardware.usb.host

# (int) Target Android API, should be as high as possible.
#android.api = 31

# (int) Minimum API your APK / AAB will support.
#android.minapi = 21

# (int) Android SDK version to use
#android.sdk = 20

# (str) Android NDK version to use
#android.ndk = 23b

# (int) Android NDK API to use. This is the minimum API your app will >
#android.ndk_api = 21

# (bool) Use --private data storage (True) or --dir public storage (Fa>
#android.private_storage = True

# (str) Android NDK directory (if empty, it will be automatically down>
#android.ndk_path =

# (str) Android SDK directory (if empty, it will be automatically down>
#android.sdk_path =

# (str) ANT directory (if empty, it will be automatically downloaded.)
#android.ant_path =

# (bool) If True, then skip trying to update the Android sdk
# This can be useful to avoid excess Internet downloads or save time# when an update is due and you just want to test/build your package
# android.skip_update = False

# (bool) If True, then automatically accept SDK license
# agreements. This is intended for automation only. If set to False,
# the default, you will be shown the license when first running
# buildozer.
# android.accept_sdk_license = False

# (str) Android entry point, default is ok for Kivy-based app
#android.entrypoint = org.kivy.android.PythonActivity

# (str) Full name including package path of the Java class that implem>
# use that parameter together with android.entrypoint to set custom Ja>
#android.activity_class_name = org.kivy.android.PythonActivity

# (str) Extra xml to write directly inside the <manifest> element of A>
# use that parameter to provide a filename from where to load your cus>
#android.extra_manifest_xml = ./src/android/extra_manifest.xml

# (str) Extra xml to write directly inside the <manifest><application>>
# use that parameter to provide a filename from where to load your cus>
#android.extra_manifest_application_arguments = ./src/android/extra_ma>

# (str) Full name including package path of the Java class that implem>
# use that parameter to set custom Java class which extends PythonServ>
#android.service_class_name = org.kivy.android.PythonService

# (str) Android app theme, default is ok for Kivy-based app
# android.apptheme = "@android:style/Theme.NoTitleBar"

# (list) Pattern to whitelist for the whole project
#android.whitelist =

# (str) Path to a custom whitelist file
#android.whitelist_src =

# (str) Path to a custom blacklist file
#android.blacklist_src =

# (list) List of Java .jar files to add to the libs so that pyjnius ca>
# their classes. Don't add jars that you do not need, since extra jars>
# down the build process. Allows wildcards matching, for example:
# OUYA-ODK/libs/*.jar
#android.add_jars = foo.jar,bar.jar,path/to/more/*.jar

# (list) List of Java files to add to the android project (can be java>
# directory containing the files)
#android.add_src =

# (list) Android AAR archives to add
#android.add_aars =

# (list) Put these files or directories in the apk assets directory.
# Either form may be used, and assets need not be in 'source.include_e>
# 1) android.add_assets = source_asset_relative_path
# 2) android.add_assets = source_asset_path:destination_asset_relative>
#android.add_assets =

# (list) Put these files or directories in the apk res directory.
# The option may be used in three ways, the value may contain one or z>
# Some examples:
# 1) A file to add to resources, legal resource names contain ['a-z','>
# android.add_resources = my_icons/all-inclusive.png:drawable/all_incl>
# 2) A directory, here  'legal_icons' must contain resources of one ki>
# android.add_resources = legal_icons:drawable
# 3) A directory, here 'legal_resources' must contain one or more dire>
# each of a resource kind:  drawable, xml, etc...# android.add_resources = legal_resources
#android.add_resources =

# (list) Gradle dependencies to add
#android.gradle_dependencies =

# (bool) Enable AndroidX support. Enable when 'android.gradle_dependen>
# contains an 'androidx' package, or any package from Kotlin source.
# android.enable_androidx requires android.api >= 28
#android.enable_androidx = True

# (list) add java compile options
# this can for example be necessary when importing certain java librar>
# see https://developer.android.com/studio/write/java8-support for fur>
# android.add_compile_options = "sourceCompatibility = 1.8", "targetCo>

# (list) Gradle repositories to add {can be necessary for some android>
# please enclose in double quotes
# e.g. android.gradle_repositories = "maven { url 'https://kotlin.bint>
#android.add_gradle_repositories =

# (list) packaging options to add
# see https://google.github.io/android-gradle-dsl/current/com.android.>
# can be necessary to solve conflicts in gradle_dependencies
# please enclose in double quotes
# e.g. android.add_packaging_options = "exclude 'META-INF/common.kotli>
#android.add_packaging_options =

# (list) Java classes to add as activities to the manifest.
#android.add_activities = com.example.ExampleActivity

# (str) OUYA Console category. Should be one of GAME or APP
# If you leave this blank, OUYA support will not be enabled
#android.ouya.category = GAME

# (str) Filename of OUYA Console icon. It must be a 732x412 png image.
#android.ouya.icon.filename = %(source.dir)s/data/ouya_icon.png

# (str) XML file to include as an intent filters in <activity> tag
#android.manifest.intent_filters =

# (list) Copy these files to src/main/res/xml/ (used for example with >
#android.res_xml = PATH_TO_FILE,

# (str) launchMode to set for the main activity
#android.manifest.launch_mode = standard

# (str) screenOrientation to set for the main activity.
# Valid values can be found at https://developer.android.com/guide/top>
#android.manifest.orientation = fullSensor

# (list) Android additional libraries to copy into libs/armeabi
#android.add_libs_armeabi = libs/android/*.so
#android.add_libs_armeabi_v7a = libs/android-v7/*.so
#android.add_libs_arm64_v8a = libs/android-v8/*.so
#android.add_libs_x86 = libs/android-x86/*.so
#android.add_libs_mips = libs/android-mips/*.so# (bool) Indicate whether the screen should stay on
# Don't forget to add the WAKE_LOCK permission if you set this to True
#android.wakelock = False

# (list) Android application meta-data to set (key=value format)
#android.meta_data =

# (list) Android library project to add (will be added in the
# project.properties automatically.)
#android.library_references =

# (list) Android shared libraries which will be added to AndroidManife>
#android.uses_library =

# (str) Android logcat filters to use
#android.logcat_filters = *:S python:D

# (bool) Android logcat only display log for activity's pid
#android.logcat_pid_only = False

# (str) Android additional adb arguments
#android.adb_args = -H host.docker.internal

# (bool) Copy library instead of making a libpymodules.so
#android.copy_libs = 1

# (list) The Android archs to build for, choices: armeabi-v7a, arm64-v>
# In past, was `android.arch` as we weren't supporting builds for mult>
# android.archs = arm64-v8a, armeabi-v7a

# (int) overrides automatic versionCode computation (used in build.gra>
# this is not the same as