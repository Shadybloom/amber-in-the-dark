#!/bin/bash
# Скрипт озвучивает текст из буфера обмена иксов.
# Требуется синтезатор речи:
# https://github.com/Olga-Yakovleva/RHVoice/
# И xclip для копирования текста из буфера обмена.
# Удобно привязать к горячей клавише, например, для awesome-wm (в ~/.config/awesome/rc.lua):
#    awful.key({ modkey,           }, "v", function () awful.util.spawn_with_shell("rhvoice-xclip.sh") end),
# Достаточно выделить кусок текста (где угодно) и нажать win+v -- и синтезатор прочитает.

if [ "$(pidof RHVoice-client)" ]
then
    killall RHVoice-client & killall aplay
    # Брр, как-то это сурово.
    kill -9 `ps aux | grep 'rhvoice-xclip.sh' | awk '{print $2}'`
else
    IFS=$'\n'
    RHVoice-service
    for entry in $(xclip -o)
    do
        echo "$entry" | RHVoice-client -s Anna | aplay -f S16_LE -c1 -r24000 -q
        sleep 0.1s
    done
fi
