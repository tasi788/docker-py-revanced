"""APK Sources used."""

APK_MIRROR_BASE_URL = "https://www.apkmirror.com"
APK_MIRROR_BASE_APK_URL = f"{APK_MIRROR_BASE_URL}/apk"
APK_MIRROR_PACKAGE_URL = f"{APK_MIRROR_BASE_URL}/?s=" + "{}"
APK_MIRROR_APK_CHECK = f"{APK_MIRROR_BASE_URL}/wp-json/apkm/v1/app_exists/"
UPTODOWN_BASE_URL = "https://{}.en.uptodown.com/android"
APK_PURE_BASE_URL = "https://apkpure.com"
APK_PURE_BASE_APK_URL = "https://d.apkpure.com/b/APK"
APK_PURE_URL = APK_PURE_BASE_APK_URL + "/{}?version=latest"
APK_PURE_ICON_URL = APK_PURE_BASE_URL + "/search?q={}"
APKS_SOS_BASE_URL = "https://apksos.com/download-app"
APK_SOS_URL = APKS_SOS_BASE_URL + "/{}"
GITHUB_BASE_URL = "https://github.com"
PLAY_STORE_BASE_URL = "https://play.google.com"
PLAY_STORE_APK_URL = f"{PLAY_STORE_BASE_URL}/store/apps/details?id=" + "{}"
APK_COMBO_BASE_URL = "https://apkcombo.com"
APK_COMBO_GENERIC_URL = APK_COMBO_BASE_URL + "/genericApp/{}"
not_found_icon = "https://img.icons8.com/bubbles/500/android-os.png"
revanced_api = "https://api.revanced.app/v2/patches/latest"
APK_MONK_BASE_URL = "https://www.apkmonk.com"
APK_MONK_APK_URL = APK_MONK_BASE_URL + "/app/{}/"
APK_MONK_ICON_URL = "https://cdn.apkmonk.com/logos/{}"
DRIVE_BASE_URL = "https://drive.google.com"
DRIVE_DOWNLOAD_BASE_URL = f"{DRIVE_BASE_URL}/uc?id="
DRIVE_DOWNLOAD_URL = DRIVE_DOWNLOAD_BASE_URL + "{}"
apk_sources = {
    "backdrops": f"{APK_MIRROR_BASE_APK_URL}/backdrops/backdrops-wallpapers/",
    "bacon": f"{APK_MIRROR_BASE_APK_URL}/onelouder-apps/baconreader-for-reddit/",
    "boost": f"{APK_MIRROR_BASE_APK_URL}/ruben-mayayo/boost-for-reddit/",
    "candyvpn": f"{APK_MIRROR_BASE_APK_URL}/liondev-io/candylink-vpn/",
    "duolingo": f"{APK_MIRROR_BASE_APK_URL}/duolingo/duolingo-duolingo/",
    "grecorder": f"{APK_MIRROR_BASE_APK_URL}/google-inc/google-recorder/",
    "icon_pack_studio": f"{APK_MIRROR_BASE_APK_URL}/smart-launcher-team/icon-pack-studio/",
    "infinity": f"{APK_MIRROR_BASE_APK_URL}/docile-alligator/infinity-for-reddit/",
    "inshorts": f"{APK_MIRROR_BASE_APK_URL}/inshorts-formerly-news-in-shorts/inshorts-news-in-60-words-2/",
    "instagram": f"{APK_MIRROR_BASE_APK_URL}/instagram/instagram-instagram/",
    "irplus": f"{APK_MIRROR_BASE_APK_URL}/binarymode/irplus-infrared-remote/",
    "lightroom": f"{APK_MIRROR_BASE_APK_URL}/adobe/lightroom/",
    "meme-generator-free": f"{APK_MIRROR_BASE_APK_URL}/zombodroid/meme-generator-free/",
    "messenger": f"{APK_MIRROR_BASE_APK_URL}/facebook-2/messenger/",
    "netguard": f"{APK_MIRROR_BASE_APK_URL}/marcel-bokhorst/netguard-no-root-firewall/",
    "nova_launcher": f"{APK_MIRROR_BASE_APK_URL}/teslacoil-software/nova-launcher/",
    "nyx-music-player": f"{APK_MIRROR_BASE_APK_URL}/awedea/nyx-music-player/",
    "pixiv": f"{APK_MIRROR_BASE_APK_URL}/pixiv-inc/pixiv/",
    "reddit": f"{APK_MIRROR_BASE_APK_URL}/redditinc/reddit/",
    "relay": f"{APK_MIRROR_BASE_APK_URL}/dbrady/relay-for-reddit-2/",
    "rif": f"{APK_MIRROR_BASE_APK_URL}/talklittle/reddit-is-fun/",
    "slide": f"{APK_MIRROR_BASE_APK_URL}/haptic-apps/slide-for-reddit/",
    "solidexplorer": f"{APK_MIRROR_BASE_APK_URL}/neatbytes/solid-explorer-beta/",
    "sonyheadphone": f"{APK_MIRROR_BASE_APK_URL}/sony-corporation/sony-headphones-connect/",
    "sync": f"{APK_MIRROR_BASE_APK_URL}/red-apps-ltd/sync-for-reddit/",
    "tasker": f"{APK_MIRROR_BASE_APK_URL}/joaomgcd/tasker-crafty-apps-eu/",
    "ticktick": f"{APK_MIRROR_BASE_APK_URL}/appest-inc/ticktick-to-do-list-with-reminder-day-planner/",
    "tiktok": f"{APK_MIRROR_BASE_APK_URL}/tiktok-pte-ltd/tik-tok-including-musical-ly/",
    "musically": f"{APK_MIRROR_BASE_APK_URL}/tiktok-pte-ltd/tik-tok-including-musical-ly/",
    "trakt": f"{APK_MIRROR_BASE_APK_URL}/trakt/trakt/",
    "twitch": f"{APK_MIRROR_BASE_APK_URL}/twitch-interactive-inc/twitch/",
    "twitter": f"{APK_MIRROR_BASE_APK_URL}/x-corp/twitter/",
    "vsco": f"{APK_MIRROR_BASE_APK_URL}/vsco/vsco-cam/",
    "warnwetter": f"{APK_MIRROR_BASE_APK_URL}/deutscher-wetterdienst/warnwetter/",
    "windy": f"{APK_MIRROR_BASE_APK_URL}/windy-weather-world-inc/windy-wind-weather-forecast/",
    "youtube": f"{APK_MIRROR_BASE_APK_URL}/google-inc/youtube/",
    "youtube_music": f"{APK_MIRROR_BASE_APK_URL}/google-inc/youtube-music/",
    "yuka": f"{APK_MIRROR_BASE_APK_URL}/yuka-apps/yuka-food-cosmetic-scan/",
    "strava": f"{APK_MIRROR_BASE_APK_URL}/strava-inc/strava-running-and-cycling-gps/",
    "vanced": f"{APK_MIRROR_BASE_APK_URL}/team-vanced/youtube-vanced/",
    "tumblr": f"{APK_MIRROR_BASE_APK_URL}/tumblr-inc/tumblr/",
    "my-expenses": UPTODOWN_BASE_URL.format("my-expenses"),
    "spotify": UPTODOWN_BASE_URL.format("spotify"),
    "androidtwelvewidgets": APK_PURE_URL,
    "reddit-news": APK_PURE_URL,
    "expensemanager": APK_SOS_URL,
    "finanz-online": APK_SOS_URL,
    "hex-editor": APK_PURE_URL,
    "photomath": APK_MONK_APK_URL,
    "joey": APK_MONK_APK_URL,
    "spotify-lite": APK_MONK_APK_URL,
    "digitales": APK_MONK_APK_URL,
    "scbeasy": APK_MONK_APK_URL,
}
