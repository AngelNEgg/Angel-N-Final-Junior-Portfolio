# Song 1 
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

# Song 2
from earsketch import *

init()

setTempo(165)

setEffect(2, REVERB, REVERB_TIME, 2500)
setEffect(2, VOLUME, GAIN, -10, 1, 1)
fitMedia(IRCA_BOMBA_SEIS_CORRIDO_ELEC_GUITAR_SEG, 1, 1, 20)
fitMedia(IRCA_BOMBA_SEIS_CORRIDO_ELEC_GUITAR_PRI, 2, 1, 20)
fitMedia(IRCA_BOMBA_SEIS_CORRIDO_ELEC_GUITAR_SEG, 3, 1, 20)
fitMedia(IRCA_BOMBA_SEIS_CORRIDO_ELEC_PIANO, 4, 1, 20)
fitMedia(IRCA_BOMBA_SEIS_CORRIDO_BARRIL_HIGH, 5, 1, 20)
fitMedia(IRCA_BOMBA_SEIS_CORRIDO_BAJO, 6, 1, 20)
fitMedia(IRCA_BOMBA_SEIS_CORRIDO_CUA, 7, 1, 20)

# Song 3
#Angel Nazaire
#11/19/2024
# Sample
from earsketch import *

init()

setTempo(80)
bass1 = Y20_HARP_SYNTH_1
bass2 = Y20_SINE_1
drum =Y07_DRUM_SAMPLE
lead = Y20_ELECTRO_1
lead2 = Y20_ELECTRO_2
crash = Y07_CRASH
hat = Y08_OPEN_HI_HATS
vocal = 

fitMedia(bass1, 1, 1, 9)
fitMedia(bass2, 2, 1, 9)
setEffect(2, VOLUME, GAIN, 5)
fitMedia(lead, 3, 1, 9)
fitMedia(lead2, 4, 1, 9)

fitMedia(drum, 5, 1, 9)
fitMedia(hat, 6, 1, 9)
setEffect(6, VOLUME, GAIN, 1, 1, -10, 3)
setEffect(6, VOLUME, GAIN, 1, 5, -10, 7)

fitMedia(crash, 7, 1, 5)
fitMedia(crash, 7, 5, 9)

# Song 4
from earsketch import *

init()

setTempo(120)

fitMedia(YG_TECHNO_FILTERED_LOOP_1, 1, 1, 9)
fitMedia(YG_TECHNO_ELECTRIC_PIANO_1, 2, 5, 9)
fitMedia(YG_TECHNO_SYNTH_1, 3, 5, 9)
fitMedia(Y27_ELECTRO_1, 4, 5, 9)
fitMedia(YG_TECHNO_DRUMS_3, 5, 5, 9)
fitMedia(YG_TECHNO_SYNTH_2, 6, 5, 9)
fitMedia(YG_TECHNO_SYNTH_BASS_2, 7, 5, 9)
