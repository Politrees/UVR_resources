"""
The lists are mainly compiled for this project: https://github.com/Bebra777228/PolUVR
If your project supports the integration of these model lists, feel free to use them.
"""

FORMATS = [
    # Lossless formats (maximum quality)
    "wav",        # Uncompressed audio standard (maximum file size)
    "flac",       # Best lossless (compression without loss + metadata)
    "aiff",       # Apple's version of WAV with tags

    # Modern lossy (optimal quality with compression)
    "opus",       # Best codec (outperforms AAC/MP3 at low bitrates)
    "m4a",        # AAC in MP4 container (standard for Apple/YouTube)
    "aac",        # Direct implementation of AAC

    # Classic lossy (universal support)
    "ogg",        # Vorbis (better quality than MP3 at the same bitrate)
    "mp3"         # Outdated but ubiquitous
]

STEMS = [
    # People
    "vocals", "male", "female", "aspiration", "crowd",
    # Instrumental
    "instrumental", "drums", "kick", "snare", "toms", "hh", "ride", "crash", "bass", "drum-bass", "guitar", "piano", "woodwinds",
    # Effects
    "echo", "reverb", "noise", "dry",
    # Other
    "other"
]


# ===== DEMUCS Models ===== #
DEMUCS_v1_MODELS = {
    'demucs': 'demucs.th',
    'demucs_extra': 'demucs_extra.th',
    'light': 'light.th',
    'light_extra': 'light_extra.th',
    'tasnet': 'tasnet.th',
    'tasnet_extra': 'tasnet_extra.th',
}
DEMUCS_v2_MODELS = {
    'demucs': 'demucs-e07c671f.th',
    'demucs48_hq': 'demucs48_hq-28a1282c.th',
    'demucs_extra': 'demucs_extra-3646af93.th',
    'demucs_unittest': 'demucs_unittest-09ebc15f.th',
    'tasnet': 'tasnet-beb46fac.th',
    'tasnet_extra': 'tasnet_extra-df3777b2.th',
}
DEMUCS_v3_MODELS = {
    'mdx': 'mdx.yaml',
    'mdx_q': 'mdx_q.yaml',
    'mdx_extra': 'mdx_extra.yaml',
    'mdx_extra_q': 'mdx_extra_q.yaml',
    'repro_mdx_a': 'repro_mdx_a.yaml',
    'repro_mdx_a_hybrid_only': 'repro_mdx_a_hybrid_only.yaml',
    'repro_mdx_a_time_only': 'repro_mdx_a_time_only.yaml',
    'UVR Model': 'UVR_Demucs_Model_1.yaml',
}
DEMUCS_v4_MODELS = {
    'htdemucs': 'htdemucs.yaml',
    'htdemucs_6s': 'htdemucs_6s.yaml',
    'htdemucs_ft': 'htdemucs_ft.yaml',
    'hdemucs_mmi': 'hdemucs_mmi.yaml',
}

# ===== VR-ARCH Models ===== #
VR_ARCH_MODELS = {
    'MGM_HIGHEND_v4': 'MGM_HIGHEND_v4.pth',
    'MGM_LOWEND_A_v4': 'MGM_LOWEND_A_v4.pth',
    'MGM_LOWEND_B_v4': 'MGM_LOWEND_B_v4.pth',
    'MGM_MAIN_v4': 'MGM_MAIN_v4.pth',
    '1_HP-UVR': '1_HP-UVR.pth',
    '2_HP-UVR': '2_HP-UVR.pth',
    '3_HP-Vocal-UVR': '3_HP-Vocal-UVR.pth',
    '4_HP-Vocal-UVR': '4_HP-Vocal-UVR.pth',
    '5_HP-Karaoke-UVR': '5_HP-Karaoke-UVR.pth',
    '6_HP-Karaoke-UVR': '6_HP-Karaoke-UVR.pth',
    '7_HP2-UVR': '7_HP2-UVR.pth',
    '8_HP2-UVR': '8_HP2-UVR.pth',
    '9_HP2-UVR': '9_HP2-UVR.pth',
    '10_SP-UVR-2B-32000-1': '10_SP-UVR-2B-32000-1.pth',
    '11_SP-UVR-2B-32000-2': '11_SP-UVR-2B-32000-2.pth',
    '12_SP-UVR-3B-44100': '12_SP-UVR-3B-44100.pth',
    '13_SP-UVR-4B-44100-1': '13_SP-UVR-4B-44100-1.pth',
    '14_SP-UVR-4B-44100-2': '14_SP-UVR-4B-44100-2.pth',
    '15_SP-UVR-MID-44100-1': '15_SP-UVR-MID-44100-1.pth',
    '16_SP-UVR-MID-44100-2': '16_SP-UVR-MID-44100-2.pth',
    '17_HP-Wind_Inst-UVR': '17_HP-Wind_Inst-UVR.pth',
    'UVR-BVE-4B_SN-44100-1': 'UVR-BVE-4B_SN-44100-1.pth',
    'UVR-DeEcho-Normal by FoxJoy': 'UVR-De-Echo-Normal.pth',
    'UVR-DeEcho-Aggressive by FoxJoy': 'UVR-De-Echo-Aggressive.pth',
    'UVR-DeEcho-DeReverb by FoxJoy': 'UVR-DeEcho-DeReverb.pth',
    'UVR-DeNoise-Lite by FoxJoy': 'UVR-DeNoise-Lite.pth',
    'UVR-DeNoise by FoxJoy': 'UVR-DeNoise.pth',
    'UVR-DeReverb by aufr33 & jarredou': 'UVR-De-Reverb-aufr33-jarredou.pth',
}

# ===== MDXN-NET Models ===== #
MDXNET_MODELS = {
    'UVR-MDX-NET 1': 'UVR_MDXNET_1_9703.onnx',
    'UVR-MDX-NET 2': 'UVR_MDXNET_2_9682.onnx',
    'UVR-MDX-NET 3': 'UVR_MDXNET_3_9662.onnx',
    'UVR_MDXNET_9482': 'UVR_MDXNET_9482.onnx',
    'UVR-MDX-NET Inst 1': 'UVR-MDX-NET-Inst_1.onnx',
    'UVR-MDX-NET Inst 2': 'UVR-MDX-NET-Inst_2.onnx',
    'UVR-MDX-NET Inst 3': 'UVR-MDX-NET-Inst_3.onnx',
    'UVR-MDX-NET Inst HQ 1': 'UVR-MDX-NET-Inst_HQ_1.onnx',
    'UVR-MDX-NET Inst HQ 2': 'UVR-MDX-NET-Inst_HQ_2.onnx',
    'UVR-MDX-NET Inst HQ 3': 'UVR-MDX-NET-Inst_HQ_3.onnx',
    'UVR-MDX-NET Inst HQ 4': 'UVR-MDX-NET-Inst_HQ_4.onnx',
    'UVR-MDX-NET Inst HQ 5': 'UVR-MDX-NET-Inst_HQ_5.onnx',
    'UVR-MDX-NET Inst Main': 'UVR-MDX-NET-Inst_Main.onnx',
    'UVR-MDX-NET Karaoke': 'UVR_MDXNET_KARA.onnx',
    'UVR-MDX-NET Karaoke 2': 'UVR_MDXNET_KARA_2.onnx',
    'UVR-MDX-NET Crowd HQ 1 By Aufr33': 'UVR-MDX-NET_Crowd_HQ_1.onnx',
    'UVR-MDX-NET Main': 'UVR_MDXNET_Main.onnx',
    'UVR-MDX-NET Voc FT': 'UVR-MDX-NET-Voc_FT.onnx',
    'Kim Inst': 'Kim_Inst.onnx',
    'Kim Vocal 1': 'Kim_Vocal_1.onnx',
    'Kim Vocal 2': 'Kim_Vocal_2.onnx',
    'kuielab_a_bass': 'kuielab_a_bass.onnx',
    'kuielab_a_drums': 'kuielab_a_drums.onnx',
    'kuielab_a_other': 'kuielab_a_other.onnx',
    'kuielab_a_vocals': 'kuielab_a_vocals.onnx',
    'kuielab_b_bass': 'kuielab_b_bass.onnx',
    'kuielab_b_drums': 'kuielab_b_drums.onnx',
    'kuielab_b_other': 'kuielab_b_other.onnx',
    'kuielab_b_vocals': 'kuielab_b_vocals.onnx',
    'Reverb HQ By FoxJoy': 'Reverb_HQ_By_FoxJoy.onnx',
    'VIP | UVR-MDX-NET_Inst_82_beta': 'UVR-MDX-NET_Inst_82_beta.onnx',
    'VIP | UVR-MDX-NET_Inst_90_beta': 'UVR-MDX-NET_Inst_90_beta.onnx',
    'VIP | UVR-MDX-NET_Inst_187_beta': 'UVR-MDX-NET_Inst_187_beta.onnx',
    'VIP | UVR-MDX-NET-Inst_full_292': 'UVR-MDX-NET-Inst_full_292.onnx',
    'VIP | UVR-MDX-NET_Main_340': 'UVR-MDX-NET_Main_340.onnx',
    'VIP | UVR-MDX-NET_Main_390': 'UVR-MDX-NET_Main_390.onnx',
    'VIP | UVR-MDX-NET_Main_406': 'UVR-MDX-NET_Main_406.onnx',
    'VIP | UVR-MDX-NET_Main_427': 'UVR-MDX-NET_Main_427.onnx',
    'VIP | UVR-MDX-NET_Main_438': 'UVR-MDX-NET_Main_438.onnx',
}

# ===== MDX23C Models ===== #
MDX23C_MODELS = {
    'MDX23C DeReverb by aufr33 & jarredou': 'MDX23C-De-Reverb-aufr33-jarredou.ckpt',
    'MDX23C DrumSep by aufr33 & jarredou': 'MDX23C-DrumSep-aufr33-jarredou.ckpt',
    'MDX23C InstVoc HQ': 'MDX23C-8KFFT-InstVoc_HQ.ckpt',
    # 'MDX23C Phantom Centre extraction by wesleyr36': 'model_mdx23c_ep_271_l1_freq_72.2383.ckpt', | doesn't work, config editing required | config_mdx23c_similarity.yaml
    'VIP | MDX23C_D1581': 'MDX23C_D1581.ckpt',
    'VIP | MDX23C InstVoc HQ 2': 'MDX23C-8KFFT-InstVoc_HQ_2.ckpt',
}

# ===== Roformer Models ===== #
ROFORMER_MODELS = {
    # BandSplit Roformer
    # 'BandSplit Roformer | 4-stems FT by SYH99999': 'BandSplit_Roformer_4stems_FT_by_SYH99999.pth', | doesn't work, config editing required | config_BandSplit_Roformer_4stems_FT_by_SYH99999.yaml
    'BandSplit Roformer | SDR 1053 by Viperx': 'model_bs_roformer_ep_937_sdr_10.5309.ckpt',
    'BandSplit Roformer | SDR 1296 by Viperx': 'model_bs_roformer_ep_368_sdr_12.9628.ckpt',
    'BandSplit Roformer | SDR 1297 by Viperx': 'model_bs_roformer_ep_317_sdr_12.9755.ckpt',
    'BandSplit Roformer | Chorus Male-Female by Sucial': 'model_chorus_bs_roformer_ep_267_sdr_24.1275.ckpt',
    'BandSplit Roformer | Male-Female by aufr33': 'bs_roformer_male_female_by_aufr33_sdr_7.2889.ckpt',
    'BandSplit Roformer | Dereverb by anvuew': 'deverb_bs_roformer_8_384dim_10depth.ckpt',
    # 'BandSplit Roformer | Inst-EXP-Value-Residual by Unwa': 'BS_Inst_EXP_VRL.ckpt', | doesn't work, architecture editing required
    'BandSplit Roformer | Revive by Unwa': 'bs_roformer_revive_by_unwa.ckpt',
    'BandSplit Roformer | Vocals by Gabox': 'bs_roformer_voc_gabox.ckpt',

    # MelBand Roformer
    # 'MelBand Roformer | 4-stems FT Large v1 by SYH99999': 'MelBand_Roformer_4stems_FT_Large_v1_by_SYH99999.ckpt', | doesn't work, config editing required | config_MelBand_Roformer_4stems_FT_Large_by_SYH99999.yaml
    # 'MelBand Roformer | 4-stems FT Large v2 by SYH99999': 'MelBand_Roformer_4stems_FT_Large_v2_by_SYH99999.ckpt', | doesn't work, config editing required | config_MelBand_Roformer_4stems_FT_Large_by_SYH99999.yaml
    # 'MelBand Roformer | 4-stems Large v1 by Aname': 'MelBand_Roformer_4stems_Large_v1_by_Aname.ckpt', | doesn't work, config editing required | config_MelBand_Roformer_4stems_Large_v1_by_Aname.yaml
    # 'MelBand Roformer | 4-stems XL v1 by Aname': 'MelBand_Roformer_4stems_XL_v1_by_Aname.ckpt', | doesn't work, config editing required | config_MelBand_Roformer_4stems_XL_v1_by_Aname.yaml
    'MelBand Roformer | SDR 1143 by Viperx': 'model_mel_band_roformer_ep_3005_sdr_11.4360.ckpt',
    # 'MelBand Roformer | Small by Aname': 'melband_roformer_small_by_aname.ckpt', | doesn't work, config editing required | config_melband_roformer_small_by_aname.yaml
    'MelBand Roformer | Aspiration by Sucial': 'aspiration_mel_band_roformer_sdr_18.9845.ckpt',
    'MelBand Roformer | Aspiration Less Aggressive by Sucial': 'aspiration_mel_band_roformer_less_aggr_sdr_18.1201.ckpt',
    'MelBand Roformer | Bleed Suppressor v1 by Unwa & 97chris': 'mel_band_roformer_bleed_suppressor_v1.ckpt',
    'MelBand Roformer | Crowd by Aufr33 & Viperx': 'mel_band_roformer_crowd_aufr33_viperx_sdr_8.7144.ckpt',
    'MelBand Roformer | DeReverb by anvuew': 'dereverb_mel_band_roformer_anvuew_sdr_19.1729.ckpt',
    'MelBand Roformer | DeReverb Mono by anvuew': 'dereverb_mel_band_roformer_mono_anvuew_sdr_20.4029.ckpt',
    'MelBand Roformer | DeReverb Less Aggressive by anvuew': 'dereverb_mel_band_roformer_less_aggressive_anvuew_sdr_18.8050.ckpt',
    'MelBand Roformer | DeReverb Big by Sucial': 'dereverb_big_mbr_ep_362.ckpt',
    'MelBand Roformer | DeReverb Super Big by Sucial': 'dereverb_super_big_mbr_ep_346.ckpt',
    'MelBand Roformer | DeReverb-Echo by Sucial': 'dereverb-echo_mel_band_roformer_sdr_10.0169.ckpt',
    'MelBand Roformer | DeReverb-Echo v2 by Sucial': 'dereverb-echo_mel_band_roformer_sdr_13.4843_v2.ckpt',
    'MelBand Roformer | DeReverb-Echo Fused by Sucial': 'dereverb_echo_mbr_fused.ckpt',
    'MelBand Roformer | Denoise by Aufr33': 'denoise_mel_band_roformer_aufr33_sdr_27.9959.ckpt',
    'MelBand Roformer | Denoise Aggr by Aufr33': 'denoise_mel_band_roformer_aufr33_aggr_sdr_27.9768.ckpt',
    'MelBand Roformer | Instrumental by becruily': 'mel_band_roformer_instrumental_becruily.ckpt',
    'MelBand Roformer | Instrumental by Gabox': 'mel_band_roformer_instrumental_gabox.ckpt',
    'MelBand Roformer | Instrumental v1 by Gabox': 'mel_band_roformer_inst_v1_gabox.ckpt',
    'MelBand Roformer | Instrumental v2 by Gabox': 'mel_band_roformer_inst_v2_gabox.ckpt',
    'MelBand Roformer | Instrumental v3 by Gabox': 'mel_band_roformer_inst_v3_gabox.ckpt',
    'MelBand Roformer | Instrumental Bleedless v1 by Gabox': 'mel_band_roformer_inst_bleedless_v1_gabox.ckpt',
    'MelBand Roformer | Instrumental Bleedless v2 by Gabox': 'mel_band_roformer_inst_bleedless_v2_gabox.ckpt',
    'MelBand Roformer | Instrumental DeNoise-DeBleed by Gabox': 'mel_band_roformer_inst_denoise_debleed_gabox.ckpt',
    'MelBand Roformer | Instrumental Fullness v1 by Gabox': 'mel_band_roformer_inst_fullness_v1_gabox.ckpt',
    'MelBand Roformer | Instrumental Fullness v2 by Gabox': 'mel_band_roformer_inst_fullness_v2_gabox.ckpt',
    'MelBand Roformer | Instrumental Fullness v3 by Gabox': 'mel_band_roformer_inst_fullness_v3_gabox.ckpt',
    'MelBand Roformer | Instrumental Fullness v4 Noise by Gabox': 'mel_band_roformer_inst_fullness_v4_noise_gabox.ckpt',
    'MelBand Roformer | Instrumental Fullness v5 by Gabox': 'mel_band_roformer_inst_fullness_v5_gabox.ckpt',
    'MelBand Roformer | Instrumental Fullness v5 Noise by Gabox': 'mel_band_roformer_inst_fullness_v5_noise_gabox.ckpt',
    'MelBand Roformer | Instrumental Fullness v6 by Gabox': 'mel_band_roformer_inst_fullness_v6_gabox.ckpt',
    'MelBand Roformer | Instrumental Fullness v6 Noise by Gabox': 'mel_band_roformer_inst_fullness_v6_noise_gabox.ckpt',
    'MelBand Roformer | Instrumental Fullness v7 by Gabox': 'mel_band_roformer_inst_fullness_v7_gabox.ckpt',
    'MelBand Roformer | Instrumental Fullness v7 Noise by Gabox': 'mel_band_roformer_inst_fullness_v7_noise_gabox.ckpt',
    'MelBand Roformer | Instrumental Fullness v8 by Gabox': 'mel_band_roformer_inst_fullness_v8_gabox.ckpt',
    'MelBand Roformer | Instrumental Fullness vX by Gabox': 'mel_band_roformer_inst_fullness_vX_gabox.ckpt',
    'MelBand Roformer | instrumental Metal preview by Mesk': 'melband_roformer_inst_metal_prev_by_mesk.ckpt',
    'MelBand Roformer | Karaoke by Aufr33 & Viperx': 'mel_band_roformer_karaoke_aufr33_viperx_sdr_10.1956.ckpt',
    'MelBand Roformer | Karaoke by becruily': 'melband_roformer_karaoke_becruily.ckpt',
    'MelBand Roformer | Karaoke by Gabox': 'mel_band_roformer_karaoke_gabox.ckpt',
    'MelBand Roformer | Vocals by becruily': 'mel_band_roformer_vocals_becruily.ckpt',
    'MelBand Roformer | Vocals by Kimberley Jensen': 'vocals_mel_band_roformer.ckpt',
    'MelBand Roformer | Vocals by Gabox': 'mel_band_roformer_voc_gabox.ckpt',
    'MelBand Roformer | Vocals Bleedless by Aname': 'melband_roformer_vocals_bleedness_by_aname.ckpt',
    'MelBand Roformer | Vocals Fullness by Aname': 'mel_band_roformer_vocals_fullness_aname.ckpt',
    'MelBand Roformer | Vocals Fullness v1 by Gabox': 'mel_band_roformer_voc_fullness_v1_gabox.ckpt',
    'MelBand Roformer | Vocals Fullness v2 by Gabox': 'mel_band_roformer_voc_fullness_v2_gabox.ckpt',
    'MelBand Roformer | Vocals Fullness v3 by Gabox': 'mel_band_roformer_voc_fullness_v3_gabox.ckpt',
    'MelBand Roformer | Vocals Fullness v4 by Gabox': 'mel_band_roformer_voc_fullness_v4_gabox.ckpt',
    'MelBand Roformer | Vocals Fullness v5 by Gabox': 'mel_band_roformer_voc_fullness_v5_gabox.ckpt',

    # MelBand Roformer Pre-Trained by Kim
    'MelBand Roformer Kim | Inst v1 by Unwa': 'melband_roformer_inst_v1.ckpt',
    'MelBand Roformer Kim | Inst v1e by Unwa': 'melband_roformer_inst_v1e.ckpt',
    'MelBand Roformer Kim | Inst v1e Plus by Unwa': 'melband_roformer_inst_v1e_plus.ckpt',
    'MelBand Roformer Kim | Inst v2 by Unwa': 'melband_roformer_inst_v2.ckpt',
    'MelBand Roformer Kim | InstVoc Duality v1 by Unwa': 'melband_roformer_instvoc_duality_v1.ckpt',
    'MelBand Roformer Kim | InstVoc Duality v2 by Unwa': 'melband_roformer_instvoc_duality_v2.ckpt',
    'MelBand Roformer Kim | FT by Unwa': 'mel_band_roformer_kim_ft_unwa.ckpt',
    'MelBand Roformer Kim | FT v2 by Unwa': 'mel_band_roformer_kim_ft2_unwa.ckpt',
    'MelBand Roformer Kim | FT v2 Bleedless by Unwa': 'mel_band_roformer_kim_ft2_bleedless_unwa.ckpt',
    'MelBand Roformer Kim | Big Beta v4 FT by Unwa': 'melband_roformer_big_beta4.ckpt',
    'MelBand Roformer Kim | Big Beta v5e FT by Unwa': 'melband_roformer_big_beta5e.ckpt',
    'MelBand Roformer Kim | Big Beta v6 FT by Unwa': 'melband_roformer_big_beta6.ckpt',
    'MelBand Roformer Kim | Big Beta v6x FT by Unwa': 'melband_roformer_big_beta6x.ckpt',
    'MelBand Roformer Kim | SYHFT by SYH99999': 'MelBandRoformerSYHFT.ckpt',
    'MelBand Roformer Kim | SYHFT v2 by SYH99999': 'MelBandRoformerSYHFTV2.ckpt',
    'MelBand Roformer Kim | SYHFT v2.5 by SYH99999': 'MelBandRoformerSYHFTV2.5.ckpt',
    'MelBand Roformer Kim | SYHFT v3 by SYH99999': 'MelBandRoformerSYHFTV3Epsilon.ckpt',
    'MelBand Roformer Kim | Big SYHFT v1 by SYH99999': 'MelBandRoformerBigSYHFTV1.ckpt',
    'MelBand Roformer Kim | Vocals v1 by Aname': 'melband_roformer_kim_vocals_v1_by_aname.ckpt',
    'MelBand Roformer Kim | Vocals v2 by Aname': 'melband_roformer_kim_vocals_v2_by_aname.ckpt',
    'MelBand Roformer Kim | Vocals v3 by Aname': 'melband_roformer_kim_vocals_v3_by_aname.ckpt',
    'MelBand Roformer Kim | Vocals Fullness v1 by Aname': 'melband_roformer_kim_vocals_fullness_v1_by_aname.ckpt',
    'MelBand Roformer Kim | Vocals Fullness v2 by Aname': 'melband_roformer_kim_vocals_fullness_v2_by_aname.ckpt',
}

# ===== SCnet Models ===== #
SCNET_MODELS = {
    '4-stems SCNet Large': 'model_scnet_sdr_9.3244.ckpt',
    '4-stems SCNet Large by starrytong': 'SCNet-large_starrytong_fixed.ckpt',
    '4-stems SCNet MUSDB18 by starrytong': 'scnet_checkpoint_musdb18.ckpt',
    '4-stems SCNet XL': 'model_scnet_ep_54_sdr_9.8051.ckpt',
}

# ===== Bandit Models ===== #
BANDIT_MODELS = {
    'Cinematic Bandit Plus by kwatcharasupat': 'model_bandit_plus_dnr_sdr_11.47.ckpt',
    'Cinematic Bandit v2 Multilang by kwatcharasupat': 'checkpoint-multi_fixed.ckpt',
}
