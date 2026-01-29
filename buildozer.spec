name: Build APK

on:
  push:
    branches: [ "main" ]

jobs:
  build:
    runs-on: ubuntu-latest

    steps:

    # ----------------------------------------------------
    # 1) Récupérer le code du dépôt
    # ----------------------------------------------------
    - name: Checkout repository
      uses: actions/checkout@v4

    # ----------------------------------------------------
    # 2) Installer Python
    # ----------------------------------------------------
    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: "3.10"

    # ----------------------------------------------------
    # 3) Installer les dépendances Linux + Buildozer
    # ----------------------------------------------------
    - name: Install dependencies
      run: |
        sudo apt update
        sudo apt install -y \
          python3-pip python3-setuptools git python3-dev \
          build-essential libffi-dev libssl-dev \
          liblzma-dev zlib1g-dev libncurses5-dev \
          libstdc++6 unzip wget

        pip install --upgrade pip
        pip install buildozer cython

    # ----------------------------------------------------
    # 4) Installer le SDK Android + outils
    # ----------------------------------------------------
    - name: Install Android SDK
      run: |
        mkdir -p $HOME/android-sdk/cmdline-tools
        cd $HOME/android-sdk/cmdline-tools

        wget https://dl.google.com/android/repository/commandlinetools-linux-11076708_latest.zip -O tools.zip
        unzip tools.zip
        rm tools.zip
        mv cmdline-tools latest

        export ANDROID_HOME=$HOME/android-sdk
        export ANDROID_SDK_ROOT=$HOME/android-sdk
        export PATH=$PATH:$ANDROID_HOME/cmdline-tools/latest/bin

        yes | sdkmanager --licenses || true
        sdkmanager "platform-tools" "platforms;android-34" "build-tools;34.0.0"

    # ----------------------------------------------------
    # 5) Construire l’APK
    # ----------------------------------------------------
    - name: Build APK
      run: |
        export ANDROID_HOME=$HOME/android-sdk
        export ANDROID_SDK_ROOT=$HOME/android-sdk
        export PATH=$PATH:$ANDROID_HOME/platform-tools:$ANDROID_HOME/build-tools/34.0.0:$ANDROID_HOME/cmdline-tools/latest/bin

        buildozer android debug

    # ----------------------------------------------------
    # 6) Upload APK généré
    # ----------------------------------------------------
    - name: Upload APK
      uses: actions/upload-artifact@v4
      with:
        name: APK-final
        path: bin/*.apk
