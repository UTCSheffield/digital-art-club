````columns
id: C5YRsNA5wgfTv7GAob1Cp
===
## Drums
These short names correspond to different parts of a standard drum kit:

`bd` = Bass drum
`sd` = Snare drum
`hh` = Hi-hat (closed)
`oh` = Hi-hat (open)

- You play the sound by pressing the play button (or `Ctrl`+`Enter`)
- You can stop the sound by hitting `Ctrl` and `.`
- The sounds have to load, so you might not hear them at first!

What happens if we put more sounds in the pattern?

```javascript
sound("bd hh sd oh hh bd oh sd")
```

## Mininotation

The green writing inside the speech marks has its own set of rules. We call this the 'mininotation' and it's the core of how Strudel generates patterns.

We can speed things up with `*` 
```javascript
sound("hh")
sound("hh*4")
sound("hh*32")
```

Or slow them down with `/` - the snare only sounds every other cycle:

```javascript
sound("bd sd/2") 
```

We can choose different sounds from a set using `:`. The computer starts counting at `0`, so `casio:0` is the same as `casio`.

```javascript
sound("casio casio casio casio")
sound("casio casio:1 casio casio:5")
```
===
An alternative way to do this is with `n`:

```javascript
n("0 1 0 5").sound("casio")
```

We can add a rest using `~` or `-`:

```javascript
n("0 1 ~ 5").sound("casio")
```

We can create more variation with sub-sequences.
We do this by breaking our steps down into mini patterns using `[]`:

```javascript
sound("bd sd bd hh")
sound("bd sd [bd cp] [hh oh]")
```

You can also use `*` or `/` to speed up or slow down sub-sequences:

```javascript
sound("bd sd [bd cp]/2 [hh oh]*2")
```

You can nest sequences within sequences for dense patterns:

```javascript
sound("bd bd [hh hh] [hh [hh hh]]")
```

You can also use `<>` to play events once per cycle:

```javascript
sound("bd bd <hh cp> sd")
```

Let's add some easy randomness using `?`.
Putting `?` after a sound means there is a 50% probability that the sound will play.

```javascript
sound("hh*8?")
```

---

Group Music Editor - [https://tinyurl.com/olpflok](https://tinyurl.com/olpflok)
Full Workshop - [https://tinyurl.com/OlpStrudel](https://tinyurl.com/OlpStrudel)

````


````columns
id: OXI9p_TA0cWmy8rKQC55F
===
## Drum Machines

```javascript
$: sound("bd hh sd oh hh bd oh sd").bank("RolandTR808")
$: sound("bd hh sd oh").bank("linn")
```

You can change the bank / drum machine to any of these
```
9000, ace, ajkpercusyn, akailinn, akaimpc60, akaixr10, alesishr16, alesissr16, bd, bossdr110, bossdr220, bossdr55, bossdr550, brk, casiorz1, casiosk1, casiovl1, cb, circuitsdrumtracks, circuitstom, compurhythm1000, compurhythm78, compurhythm8000, concertmatemg1, cp, cr, d110, d70, ddm110, ddr30, dmx, doepferms404, dpm48, dr110, dr220, dr55, dr550, drumulator, emudrumulator, emumodular, emusp12, hh, hr16, ht, jd990, korgddm110, korgkpr77, korgkr55, korgkrz, korgm1, korgminipops, korgpoly800, korgt3, kpr77, kr55, krz, linn, linn9000, linndrum, linnlm1, linnlm2, lm1, lm2, lm8953, lt, m1, mc202, mc303, mfb512, microrhythmer12, minipops, misc, moogconcertmatemg1, mpc1000, mpc60, mridangam, ms404, mt, mt32, oberheimdmx_, oberheimdmx, oh, percysyn, polaris, poly800, r8, r88, rd, rhodespolaris, rhythmace, rim, rm50, rolandcompurhythm1000, rolandcompurhythm78, rolandcompurhythm8000, rolandd110, rolandd70, rolandddr30, rolandjd990, rolandmc202, rolandmc303, rolandmt32, rolandr8, rolands50, rolandsh09, rolandsystem100, rolandtr505, rolandtr606, rolandtr626, rolandtr707, rolandtr727, rolandtr808, rolandtr909, rx21, rx5, ry30, rz1, s50, sakatadpm48, sd, sds400, sds5, sequentialcircuitsdrumtracks, sequentialcircuitstom, sergemodular, sh, sh09, simmonssds400, simmonssds5, sk1, soundmastersr88, sp12, spacedrum, sr16, system100, t3, tb, tg33, tr505, tr606, tr626, tr707, tr727, tr808, tr909, univoxmicrorhythmer12, viscospacedrum, vl1, xdrumlm8953, xr10, yamaharm50, yamaharx21, yamaharx5, yamahary30, yamahatg33
```

===
## Synths

Task : Try finding the some sounds ```sound("gm_synth_bass_2:0")``` and replacing the instruments with something from this list

```
brown, bytebeat, crackle, gm_accordion, gm_acoustic_bass, gm_acoustic_guitar_nylon, gm_acoustic_guitar_steel, gm_agogo, gm_alto_sax, gm_applause, gm_bagpipe, gm_bandoneon, gm_banjo, gm_baritone_sax, gm_bassoon, gm_bird_tweet, gm_blown_bottle, gm_brass_section, gm_breath_noise, gm_celesta, gm_cello, gm_choir_aahs, gm_church_organ, gm_clarinet, gm_clavinet, gm_contrabass, gm_distortion_guitar, gm_drawbar_organ, gm_dulcimer, gm_electric_bass_finger, gm_electric_bass_pick, gm_electric_guitar_clean, gm_electric_guitar_jazz, gm_electric_guitar_muted, gm_english_horn, gm_epiano1, gm_epiano2, gm_fiddle, gm_flute, gm_french_horn, gm_fretless_bass, gm_fx_atmosphere, gm_fx_brightness, gm_fx_crystal, gm_fx_echoes, gm_fx_goblins, gm_fx_rain, gm_fx_sci_fi, gm_fx_soundtrack, gm_glockenspiel, gm_guitar_fret_noise, gm_guitar_harmonics, gm_gunshot, gm_harmonica, gm_harpsichord, gm_helicopter, gm_kalimba, gm_koto, gm_lead_1_square, gm_lead_2_sawtooth, gm_lead_3_calliope, gm_lead_4_chiff, gm_lead_5_charang, gm_lead_6_voice, gm_lead_7_fifths, gm_lead_8_bass_lead, gm_marimba, gm_melodic_tom, gm_music_box, gm_muted_trumpet, gm_oboe, gm_ocarina, gm_orchestra_hit, gm_orchestral_harp, gm_overdriven_guitar, gm_pad_bowed, gm_pad_choir, gm_pad_halo, gm_pad_metallic, gm_pad_new_age, gm_pad_poly, gm_pad_sweep, gm_pad_warm, gm_pan_flute, gm_percussive_organ, gm_piano, gm_piccolo, gm_pizzicato_strings, gm_recorder, gm_reed_organ, gm_reverse_cymbal, gm_rock_organ, gm_seashore, gm_shakuhachi, gm_shamisen, gm_shanai, gm_sitar, gm_slap_bass_1, gm_slap_bass_2, gm_soprano_sax, gm_steel_drums, gm_string_ensemble_1, gm_string_ensemble_2, gm_synth_bass_1, gm_synth_bass_2, gm_synth_brass_1, gm_synth_brass_2, gm_synth_choir, gm_synth_drum, gm_synth_strings_1, gm_synth_strings_2, gm_taiko_drum, gm_telephone, gm_tenor_sax, gm_timpani, gm_tinkle_bell, gm_tremolo_strings, gm_trombone, gm_trumpet, gm_tuba, gm_tubular_bells, gm_vibraphone, gm_viola, gm_violin, gm_voice_oohs, gm_whistle, gm_woodblock, gm_xylophone, pink, pulse, saw, sawtooth, sbd, sin, sine, sqr, square, supersaw, tri, triangle, white, z_noise, z_sawtooth, z_sine, z_square, z_tan, z_triangle, zzfx"
```

````


