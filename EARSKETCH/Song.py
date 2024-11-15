# description: 
from earsketch import *

setTempo(80)

fitMedia(AK_UNDOG_PIANO_1, 1, 1, 5)
fitMedia(AK_UNDOG_PIANO_2, 2, 1, 5)
fitMedia(AK_UNDOG_PAD_1, 3, 1, 5)
fitMedia(AK_UNDOG_PAD_2, 4, 1, 5)
fitMedia(AK_UNDOG_808_3, 5, 1, 5)
fitMedia(CIARA_SET_DRUMBEAT_2, 6, 1, 5)
fitMedia(AK_UNDOG_PERC_TAMBOURINE_1, 7, 1, 5)
fitMedia(AK_UNDOG_PERC_SHAKER_1, 8, 1, 5)
fitMedia(AK_UNDOG_PERC_WOODBLOCKS, 9, 1, 5)

setEffect(1, REVERB, REVERB_TIME, 2000)
setEffect(1, REVERB, REVERB_DAMPFREQ, 18000)
setEffect(1, REVERB, MIX, 0.5)
