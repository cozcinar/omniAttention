# # # sequences

def sequence(classSeq):
    seq = []

    if classSeq == '8K_MPEG':

        Stitched_left_Dancing360_8K = {'name': 'Stitched_left_Dancing360_8K', 'latex': 'left_Dancing360', 'folder': 'sequences/360VR/ETRI/Stitched/StitchedDancing/8K/', \
        'seqFolder': 'Stitched_left_Dancing360_8K', 'yuvName': 'Stitched_left_Dancing360_8K_30p_8192x4096','frate': 30,\
        'width': 8192,'height': 4096,'V3': 600,'VS': 0,'cFormat': 'YUV420_8b', 'playID': 3, 'sal_playID': 14, 'bDepth': 8,\
        'spaSampling': {
            'sp1': {'width':8192, 'height':4096, 'start': 0, 'stop': 49500}, \
            'sp2': {'width':4096, 'height':2048, 'start': 0, 'stop': 49500}, \
            'sp3': {'width':3072, 'height':1536, 'start': 0, 'stop': 49500}, \
            'sp4': {'width':2048, 'height':1024, 'start': 0, 'stop': 49500}, \
            'sp5': {'width':1024, 'height':512} }}# 30 600 'frate': 30

        Stitched_left_Driving360_8K = {'name': 'Stitched_left_Driving360_8K', 'latex': 'left_Driving360', 'folder': 'sequences/360VR/ETRI/Stitched/StitchedDriving/8K/', \
        'seqFolder': 'Stitched_left_Driving360_8K', 'yuvName': 'Stitched_left_Driving360_8K_30p_8192x4096','frate': 30, \
        'width': 8192,'height': 4096,'V3': 600,'VS': 0,'cFormat': 'YUV420_8b', 'playID': 15, 'sal_playID': 15, 'bDepth': 8,\
        'spaSampling': {
            'sp1': {'width':8192, 'height':4096, 'start': 0, 'stop': 49500}, \
            'sp2': {'width':4096, 'height':2048, 'start': 0, 'stop': 49500}, \
            'sp3': {'width':3072, 'height':1536, 'start': 0, 'stop': 49500}, \
            'sp4': {'width':2048, 'height':1024, 'start': 0, 'stop': 49500}, \
            'sp5': {'width':1024, 'height':512} }}

        Trolley_8K = {'name': 'Trolley', 'folder': 'sequences/360VR/InterDigital/', \
        'seqFolder': 'Trolley', 'yuvName': 'Trolley_30p_8192x4096_8bit','frate': 30, \
        'width': 8192,'height': 4096,'V3': 600,'VS': 0,'cFormat': 'YUV420_8b', 'playID': 17, 'sal_playID': 17, 'bDepth': 8,\
        'spaSampling': {
            'sp1': {'width':8192, 'height':4096, 'start': 0, 'stop': 49500}, \
            'sp2': {'width':4096, 'height':2048, 'start': 0, 'stop': 49500}, \
            'sp3': {'width':3072, 'height':1536, 'start': 0, 'stop': 49500}, \
            'sp4': {'width':2048, 'height':1024, 'start': 0, 'stop': 49500}, \
            'sp5': {'width':1024, 'height':512} }}

        Harbor_8K = {'name': 'Harbor', 'latex': 'Harbor', 'folder': 'sequences/360VR/InterDigital/', \
        'seqFolder': 'Harbor', 'yuvName': 'Harbor_30p_8192x4096_8bit','frate': 30, \
        'width': 8192,'height': 4096,'V3': 600,'VS': 0,'cFormat': 'YUV420_8b', 'playID': 999, 'sal_playID': 8, 'bDepth': 8,\
        'spaSampling': { \
            'sp1': {'width':8192, 'height':4096, 'start': 0, 'stop': 49500}, \
            'sp2': {'width':4096, 'height':2048, 'start': 0, 'stop': 49500}, \
            'sp3': {'width':3072, 'height':1536, 'start': 0, 'stop': 49500}, \
            'sp4': {'width':2048, 'height':1024, 'start': 0, 'stop': 49500}, \
            'sp5': {'width':1024, 'height':512} }}
        
        Gaslamp_8K = {'name': 'Gaslamp', 'latex': 'Gaslamp360', 'folder': 'sequences/360VR/InterDigital/', 'seqFolder': 'Gaslamp', \
        'yuvName': 'Gaslamp_30p_8192x4096_8bit','frate': 30, 'width': 8192,'height': 4096,'V3': 600,'VS': 0,\
        'cFormat': 'YUV420_8b', 'playID': 999, 'sal_playID': 6, 'bDepth': 8, 'spaSampling': { \
        'sp1': {'width':8192, 'height':4096, 'start': 0, 'stop': 49500}, \
        'sp2': {'width':4096, 'height':2048, 'start': 0, 'stop': 49500}, \
        'sp3': {'width':3072, 'height':1536, 'start': 0, 'stop': 49500}, \
        'sp4': {'width':2048, 'height':1024, 'start': 0, 'stop': 49500}, \
        'sp5': {'width':1024, 'height':512, 'rto':0.125} }}
        
        Basketball_8K = {'name': 'Basketball', 'latex': 'basketball', 'folder': 'sequences/360VR/GoPro/Equirectancular/8K/', 'seqFolder': 'Basketball', \
        'yuvName': 'Basketball_30p_8192x4096_8bit','frate': 30, 'width': 8192,'height': 4096,'V3': 600,'VS': 0,\
        'cFormat': 'YUV420_8b', 'playID': 999, 'sal_playID': 1, 'bDepth': 8, 'spaSampling': { \
        'sp1': {'width':8192, 'height':4096, 'start': 0, 'stop': 49500}, \
        'sp2': {'width':4096, 'height':2048, 'start': 0, 'stop': 49500}, \
        'sp3': {'width':3072, 'height':1536, 'start': 0, 'stop': 49500}, \
        'sp4': {'width':2048, 'height':1024, 'start': 0, 'stop': 49500}, \
        'sp5': {'width':1024, 'height':512} }}



        ChairLiftN8 = {'name': 'ChairLiftN8', 'folder': 'sequences/360VR/InterDigital/', 'seqFolder': 'ChairLiftN8', \
        'yuvName': 'ChairliftRide_30p_8192x4096_8bit','frate': 30, 'width': 8192,'height': 4096,'V3': 600,'VS': 0,\
        'cFormat': 'YUV420_8b', 'playID': 3, 'sal_playID': 3, 'bDepth': 8, 'spaSampling': { \
        'sp1': {'width':8192, 'height':4096, 'start': 0, 'stop': 49500}, \
        'sp2': {'width':4096, 'height':2048, 'start': 0, 'stop': 49500}, \
        'sp3': {'width':3072, 'height':1536, 'start': 0, 'stop': 49500}, \
        'sp4': {'width':2048, 'height':1024, 'start': 0, 'stop': 49500}, \
        'sp5': {'width':1024, 'height':512} }}

        ChairLift_8K_10 = {'name': 'ChairLift', 'folder': 'sequences/360VR/InterDigital/', 'seqFolder': 'ChairLift', \
        'yuvName': 'ChairliftRide_30p_8192x4096_10bit','frate': 30, 'width': 8192,'height': 4096,'V3': 600,'VS': 0,\
        'cFormat': 'YUV420_10b', 'playID': 3, 'bDepth': 8, 'spaSampling': { \
        'sp1': {'width':8192, 'height':4096, 'start': 0, 'stop': 49500}, \
        'sp2': {'width':4096, 'height':2048, 'start': 0, 'stop': 49500}, \
        'sp3': {'width':3072, 'height':1536, 'start': 0, 'stop': 49500}, \
        'sp4': {'width':2048, 'height':1024, 'start': 0, 'stop': 49500}, \
        'sp5': {'width':1024, 'height':512} }}

        KiteFlite_8K = {'name': 'KiteFlite', 'folder': 'sequences/360VR/InterDigital/', 'seqFolder': 'KiteFlite', \
        'yuvName': 'KiteFlite_30p_8192x4096_8bit', 'frate': 30, 'width': 8192,'height': 4096,'V3': 600,'VS': 0,\
        'cFormat': 'YUV420_8b', 'playID': 999, 'sal_playID': 10, 'bDepth': 8, 'spaSampling': { \
        'sp1': {'width':8192, 'height':4096, 'start': 0, 'stop': 49500}, \
        'sp2': {'width':4096, 'height':2048, 'start': 0, 'stop': 49500}, \
        'sp3': {'width':3072, 'height':1536, 'start': 0, 'stop': 49500}, \
        'sp4': {'width':2048, 'height':1024, 'start': 0, 'stop': 49500}, \
        'sp5': {'width':1024, 'height':512} }}

        SkateboardInLot_8K = {'name': 'SkateboardInLot', 'folder': 'sequences/360VR/GoPro/Equirectancular/8K/', 'seqFolder': 'SkateboardInLot', \
        'yuvName': 'SkateboardInLot_30p_8192x4096_8bit','frate': 30, 'width': 8192,'height': 4096,'V3': 600,'VS': 0,\
        'cFormat': 'YUV420_8b', 'playID': 13, 'sal_playID': 13, 'bDepth': 8, 'spaSampling': { \
        'sp1': {'width':8192, 'height':4096, 'start': 0, 'stop': 49500}, \
        'sp2': {'width':4096, 'height':2048, 'start': 0, 'stop': 49500}, \
        'sp3': {'width':3072, 'height':1536, 'start': 0, 'stop': 49500}, \
        'sp4': {'width':2048, 'height':1024, 'start': 0, 'stop': 49500}, \
        'sp5': {'width':1024, 'height':512} }}

        SkateboardTrick_le = {'name': 'SkateboardTrick_le', 'folder': 'sequences/360VR/GoPro/Equirectancular/8K/', 'seqFolder': 'SkateboardTrick_le', \
                              'yuvName': 'SkateboardTrick_le_8192x4096_60fps_8bit_420_erp','frate': 60, \
                              'width': 8192,'height': 4096,'V3': 600,'VS': 0, 'cFormat': 'YUV420_8b', 'playID': 999, 'sal_playID': 999, 'bDepth': 8, \
                              'spaSampling': {'sp1': {'width':8192, 'height':4096, 'start': 0, 'stop': 49500}, \
                                              'sp2': {'width':4096, 'height':2048, 'start': 0, 'stop': 49500}, \
                                              'sp3': {'width':3072, 'height':1536, 'start': 0, 'stop': 49500}, \
                                              'sp4': {'width':2048, 'height':1024, 'start': 0, 'stop': 49500}, \
                                              'sp5': {'width':1024, 'height':512, 'start': 0, 'stop': 49500} }}

        Train_8K = {'name': 'Train', 'latex': 'train_le', 'folder': 'sequences/360VR/GoPro/Equirectancular/8K/', 'seqFolder': 'Train', \
        'yuvName': 'Train_re_60p_8192x4096_8bit','frate': 60, 'width': 8192,'height': 4096,'V3': 600,'VS': 0,\
        'cFormat': 'YUV420_8b', 'playID': 2, 'sal_playID': 16, 'bDepth': 8, 'spaSampling': { \
        'sp1': {'width':8192, 'height':4096, 'start': 0, 'stop': 49500}, \
        'sp2': {'width':4096, 'height':2048, 'start': 0, 'stop': 49500}, \
        'sp3': {'width':3072, 'height':1536, 'start': 0, 'stop': 49500}, \
        'sp4': {'width':2048, 'height':1024, 'start': 0, 'stop': 49500}, \
        'sp5': {'width':1024, 'height':512} }}         

        JamSession_8K = {'name': 'JamSession', 'folder': 'sequences/360VR/GoPro/Equirectancular/8K/', 'seqFolder': 'JamSession', \
        'yuvName': 'JamSession_le_30p_8192x4096_8bit','frate': 30, 'width': 8192,'height': 4096,'V3': 600,'VS': 0,\
        'cFormat': 'YUV420_8b', 'playID': 999, 'sal_playID': 9, 'bDepth': 8, 'spaSampling': { \
        'sp1': {'width':8192, 'height':4096, 'start': 0, 'stop': 49500}, \
        'sp2': {'width':4096, 'height':2048, 'start': 0, 'stop': 49500}, \
        'sp3': {'width':3072, 'height':1536, 'start': 0, 'stop': 49500}, \
        'sp4': {'width':2048, 'height':1024, 'start': 0, 'stop': 49500}, \
        'sp5': {'width':1024, 'height':512} }}

        # sequence list
        #seq = [Gaslamp_8K]
        seq =  [Stitched_left_Dancing360_8K,Basketball_8K, Train_8K, Stitched_left_Driving360_8K,Gaslamp_8K]
        #seq = [Stitched_left_Dancing360_8K, Basketball_8K, Train_8K, Stitched_left_Driving360_8K,Gaslamp_8K,Harbor_8K]
        #seq = [ Harbor_8K ]
        #seq = [Stitched_left_Dancing360_8K, Basketball_8K, Train_8K, Stitched_left_Driving360_8K, Gaslamp_8K]

        # sequence list for saliency
#        seq = [Basketball_8K, ChairLiftN8, Gaslamp_8K, Harbor_8K, JamSession_8K, KiteFlite_8K, SkateboardInLot_8K, #Stitched_left_Dancing360_8K, Stitched_left_Driving360_8K, Train_8K, Trolley_8K]

    elif classSeq == '4K_MPEG_v1':
        abyss_great_shark_vr    =   {'name': 'abyss_great_shark_vr', 'folder': 'sequences/360VR/GoPro/Equirectancular/', 
        'seqFolder': 'abyss_great_shark_vr', 'yuvName': 'abyss_great_shark_vr_30p_3840x1920','frate': 30, 'color': 1,
        'width': 3840,'height': 1920, 'V3': 1145,'VS': 0,'cFormat': 'YUV420_8b', 'spaSampling': { 'sp1': {'width':3840, 'height':1920}, 
        'sp2': {'width':1920, 'height':960}, 'sp3': {'width':1440, 'height':720}, 'sp4': {'width':960, 'height':480}}}

        bicyclist_vr    =   {'name': 'bicyclist_vr', 'folder': 'sequences/360VR/GoPro/Equirectancular/', 'seqFolder': 'bicyclist_vr', 'yuvName': 'bicyclist_vr_25p_3840x1920','frate': 25, 'color': 1,
        'width': 3840,'height': 1920, 'V3': 1500,'VS': 0,'cFormat': 'YUV420_8b', 'spaSampling': { 'sp1': {'width':3840, 'height':1920}, 
        'sp2': {'width':1920, 'height':960}, 'sp3': {'width':1440, 'height':720}, 'sp4': {'width':960, 'height':480}}}

        glacier_vr    =   {'name': 'glacier_vr', 'folder': 'sequences/360VR/GoPro/Equirectancular/', 
        'seqFolder': 'glacier_vr', 'yuvName': 'glacier_vr_24p_3840x1920','frate': 24, 'color': 1,
        'width': 3840,'height': 1920, 'V3': 1440,'VS': 0,'cFormat': 'YUV420_8b', 'spaSampling': { 'sp1': {'width':3840, 'height':1920}, 
        'sp2': {'width':1920, 'height':960}, 'sp3': {'width':1440, 'height':720}, 'sp4': {'width':960, 'height':480}}}

        paramotor_training_vr    =   {'name': 'paramotor_training_vr', 'folder': 'sequences/360VR/GoPro/Equirectancular/', 
        'seqFolder': 'paramotor_training_vr', 'yuvName': 'paramotor_training_vr_25p_3840x1920','frate': 25, 'color': 1,
        'width': 3840,'height': 1920, 'V3': 1279,'VS': 0,'cFormat': 'YUV420_8b', 'spaSampling': { 'sp1': {'width':3840, 'height':1920}, 
        'sp2': {'width':1920, 'height':960}, 'sp3': {'width':1440, 'height':720}, 'sp4': {'width':960, 'height':480}}}

        # FIXED: CHECK the frame rate of this sequence
        skateboarding_vr    =   {'name': 'skateboarding_vr', 'folder': 'sequences/360VR/GoPro/Equirectancular/', 
        'seqFolder': 'skateboarding_vr', 'yuvName': 'skateboarding_vr_60p_4096x2048','frate': 60, 'color': 1,
        'width': 4096,'height': 2048, 'V3': 1372,'VS': 0,'cFormat': 'YUV420_8b', 'spaSampling': { 'sp1': {'width':4096, 'height':2048}, 
        'sp2': {'width':2048, 'height':1024}, 'sp3': {'width':1536, 'height':768}, 'sp4': {'width':1024, 'height':512}}}

        timelapse_basejump_vr   =   {'name': 'timelapse_basejump_vr', 'folder': 'sequences/360VR/GoPro/Equirectancular/', 
        'seqFolder': 'timelapse_basejump_vr', 'yuvName': 'timelapse_basejump_vr_25p_3840x1920','frate': 25, 'color': 1,
        'width': 3840,'height': 1920, 'V3': 330,'VS': 0,'cFormat': 'YUV420_8b', 'spaSampling': { 'sp1': {'width':3840, 'height':1920}, 
        'sp2': {'width':1920, 'height':960}, 'sp3': {'width':1440, 'height':720}, 'sp4': {'width':960, 'height':480}}}

        timelapse_building_vr    =   {'name': 'timelapse_building_vr', 'folder': 'sequences/360VR/GoPro/Equirectancular/', 
        'seqFolder': 'timelapse_building_vr', 'yuvName': 'timelapse_building_vr_25p_3840x1920','frate': 25, 'color': 1,
        'width': 3840,'height': 1920, 'V3': 327,'VS': 0,'cFormat': 'YUV420_8b', 'spaSampling': { 'sp1': {'width':3840, 'height':1920}, 
        'sp2': {'width':1920, 'height':960}, 'sp3': {'width':1440, 'height':720}, 'sp4': {'width':960, 'height':480}}}

        ballooning_vr    =   {'name': 'ballooning_vr', 'folder': 'sequences/360VR/GoPro/Equirectancular/', 
        'seqFolder': 'ballooning_vr', 'yuvName': 'ballooning_vr_25p_3840x2160','frate': 25, 'color': 1,
        'width': 3840,'height': 2160, 'V3': 655,'VS': 0,'cFormat': 'YUV420_8b', 'spaSampling': { 'sp1': {'width':3840, 'height':2160}, 
        'sp2': {'width':1920, 'height':1080}, 'sp3': {'width':1440, 'height':810}, 'sp4': {'width':960, 'height':540}}}

        ski_downhill_vr    =   {'name': 'ski_downhill_vr', 'folder': 'sequences/360VR/GoPro/Equirectancular/', 
        'seqFolder': 'ski_downhill_vr', 'yuvName': 'ski_downhill_vr_30p_3840x2160','frate': 30, 'color': 1,
        'width': 3840,'height': 2160, 'V3': 1799, 'VS': 0,'cFormat': 'YUV420_8b', 'spaSampling': { \
        'sp1': {'width':3840, 'height':2160}, \
        'sp2': {'width':1920, 'height':1080}, \
        'sp3': {'width':1440, 'height':810}, \
        'sp4': {'width':960, 'height':540}}}

        seq = [ abyss_great_shark_vr, bicyclist_vr, glacier_vr, paramotor_training_vr, skateboarding_vr, timelapse_basejump_vr, timelapse_building_vr, 
        ballooning_vr, ski_downhill_vr ]

    elif classSeq == '4K_MPEG_v2':

        BearAttack_left    =   {'name': 'BearAttack_left', 'folder': 'sequences/360VR/nokia/', \
        'seqFolder': 'BearAttack', 'yuvName': 'BearAttack_equirect_left_30p_3840x1920','frate': 30, 'color': 1,\
        'width': 3840,'height': 1920, 'V3': 300,'VS': 0,'cFormat': 'YUV420_8b', 'playID': 5, 'sal_playID': 2, 'spaSampling': { \
        'sp1': {'width':3840, 'height':1920, 'start': 0, 'stop': 8000}, \
        'sp2': {'width':1720, 'height':960, 'start': 0, 'stop': 8000}, \
        'sp3': {'width':1290, 'height':624, 'start': 0, 'stop': 8000}, \
        'sp4': {'width':860, 'height':480, 'start': 0, 'stop': 8000}
            }}

        GT_Sheriff    =   {'name': 'GT_Sheriff', 'latex': 'GT_Sheriff', 'folder': 'sequences/360VR/nokia/', \
        'seqFolder': 'GT_Sheriff', 'yuvName': 'GT_Sheriff_equirect_left_30p_4320x2160','frate': 30, 'color': 1, \
        'width': 4320,'height': 2160, 'V3': 300,'VS': 0,'cFormat': 'YUV420_8b', 'playID': 10, 'sal_playID': 7, 'spaSampling': { \
        'sp1': {'width':4320, 'height':2160, 'start': 0, 'stop': 8000}, \
        'sp2': {'width':2160, 'height':1080, 'start': 0, 'stop': 8000}, \
        'sp3': {'width':1620, 'height':810, 'start': 0, 'stop': 8000}, \
        'sp4': {'width':1080, 'height':540, 'start': 0, 'stop': 8000}
            }}

        LRRH    =   {'name': 'LRRH', 'latex': 'LRRH', 'folder': 'sequences/360VR/nokia/', \
        'seqFolder': 'LRRH', 'yuvName': 'LRRH_equirect_left_30p_3840x1920','frate': 30, 'color': 1, \
        'width': 3840,'height': 1920, 'V3': 300,'VS': 0,'cFormat': 'YUV420_8b', 'playID': 11, 'sal_playID': 11, 'spaSampling': { \
        'sp1': {'width':3840, 'height':1920, 'start': 0, 'stop': 8000}, \
        'sp2': {'width':1920, 'height':960, 'start': 0, 'stop': 8000}, \
        'sp3': {'width':1440, 'height':720, 'start': 0, 'stop': 8000}, \
        'sp4': {'width':960, 'height':480}}}

        PoleVault_le    =   {'name': 'PoleVault_le', 'folder': 'sequences/360VR/CIVIT/', \
        'seqFolder': 'PoleVault_le', 'yuvName': 'PoleVault_le_30p_3840x1920_8bit','frate': 30, 'color': 1, \
        'width': 3840,'height': 1920, 'V3': 300,'VS': 0,'cFormat': 'YUV420_8b', 'playID': 12, 'sal_playID': 12, 'spaSampling': { \
        'sp1': {'width':3840, 'height':1920, 'start': 0, 'stop': 8000}, \
        'sp2': {'width':1920, 'height':960, 'start': 0, 'stop': 8000}, \
        'sp3': {'width':1440, 'height':720, 'start': 0, 'stop': 8000}, \
        'sp4': {'width':960, 'height':480}}}

        AerialCity    =   {'name': 'AerialCity', 'folder': 'sequences/360VR/LetinVR/', \
        'seqFolder': 'AerialCity', 'yuvName': 'AerialCity_30p_3840x1920_8bit','frate': 30, 'color': 1,\
        'width': 3840,'height': 1920, 'V3': 300,'VS': 0,'cFormat': 'YUV420_8b', 'playID': 0, 'sal_playID': 0, 'spaSampling': { \
        'sp1': {'width':3840, 'height':1920, 'start': 0, 'stop': 8000}, \
        'sp2': {'width':1920, 'height':960, 'start': 0, 'stop': 8000}, \
        'sp3': {'width':1440, 'height':720, 'start': 0, 'stop': 8000}, \
        'sp4': {'width':960, 'height':480}}}

        DrivingInCity    =   {'name': 'DrivingInCity', 'folder': 'sequences/360VR/LetinVR/', \
        'seqFolder': 'DrivingInCity', 'yuvName': 'DrivingInCity_30p_3840x1920_8bit','frate': 30, 'color': 1, \
        'width': 3840,'height': 1920, 'V3': 300,'VS': 0,'cFormat': 'YUV420_8b', 'playID': 7, 'sal_playID': 4, 'spaSampling': { \
        'sp1': {'width':3840, 'height':1920, 'start': 0, 'stop': 8000}, \
        'sp2': {'width':1920, 'height':960, 'start': 0, 'stop': 8000}, \
        'sp3': {'width':1440, 'height':720, 'start': 0, 'stop': 8000}, \
        'sp4': {'width':960, 'height':480}}}

        BPO_Berlioz    =   {'name': 'BPO_Berlioz', 'folder': 'sequences/360VR/HHI/', \
        'seqFolder': 'BPO_Berlioz', 'yuvName': 'BPO_Berlioz','frate': 30, 'color': 1, \
        'width': 3840,'height': 1920, 'V3': 300,'VS': 0,'cFormat': 'YUV420_8b', 'playID': 4, 'spaSampling': { \
        'sp1': {'width':3840, 'height':1920, 'start': 0, 'stop': 8000}, \
        'sp2': {'width':1920, 'height':960, 'start': 0, 'stop': 8000}, \
        'sp3': {'width':1440, 'height':720, 'start': 0, 'stop': 8000}, \
        'sp4': {'width':960, 'height':480}}}

        DrivingInCountry    =   {'name': 'DrivingInCountry', 'folder': 'sequences/360VR/LetinVR/', \
        'seqFolder': 'DrivingInCountry', 'yuvName': 'DrivingInCountry_30p_3840x1920_8bit','frate': 30, 'color': 1, \
        'width': 3840,'height': 1920, 'V3': 300,'VS': 0,'cFormat': 'YUV420_8b', 'playID': 8, 'sal_playID': 5, 'spaSampling': { \
        'sp1': {'width':3840, 'height':1920, 'start': 0, 'stop': 8000}, \
        'sp2': {'width':1920, 'height':960, 'start': 0, 'stop': 8000}, \
        'sp3': {'width':1440, 'height':720, 'start': 0, 'stop': 8000}, \
        'sp4': {'width':960, 'height':480}}}

        #seq = [LRRH, GT_Sheriff]
        #seq = []
        seq =  [LRRH]

        #seq = [AerialCity, BearAttack_left, DrivingInCity, DrivingInCountry, GT_Sheriff, LRRH, PoleVault_le]
    # return seq

    elif classSeq == '6K_MPEG':

        Landing2 = {'name': 'Landing2', 'folder': 'sequences/360VR/GoPro/Equirectancular/6K/', \
        'seqFolder': 'Landing2', 'yuvName': 'Landing2_6144x3072_30fps_8bit_420_erp','frate': 30, \
        'width': 6144,'height': 3072,'V3': 600,'VS': 0,'cFormat': 'YUV420_8b', 'playID': 999, \
        'spaSampling': { 'sp1': {'width':6144, 'height':3072}, 'sp2': {'width':3072, 'height':1536}, 'sp3': {'width':2304, 'height':1152}, \
        'sp4': {'width':1536, 'height':768}, 'sp5': {'width':768, 'height':384} }}

        BranCastle2 = {'name': 'BranCastle2', 'folder': 'sequences/360VR/GoPro/Equirectancular/6K/', \
        'seqFolder': 'BranCastle2', 'yuvName': 'BranCastle2_6144x3072_30fps_8bit_420_erp','frate': 30, \
        'width': 6144,'height': 3072,'V3': 600,'VS': 0,'cFormat': 'YUV420_8b', 'playID': 999, \
        'spaSampling': { 'sp1': {'width':6144, 'height':3072}, 'sp2': {'width':3072, 'height':1536}, 'sp3': {'width':2304, 'height':1152}, \
        'sp4': {'width':1536, 'height':768}, 'sp5': {'width':768, 'height':384} }}

        Broadway = {'name': 'Broadway', 'folder': 'sequences/360VR/InterDigital/6K/', \
        'seqFolder': 'Broadway', 'yuvName': 'Broadway_6144x3072_60fps_8bit_420_erp','frate': 60, \
        'width': 6144,'height': 3072,'V3': 600,'VS': 0,'cFormat': 'YUV420_8b', 'playID': 999, \
        'spaSampling': { 'sp1': {'width':6144, 'height':3072}, 'sp2': {'width':3072, 'height':1536}, 'sp3': {'width':2304, 'height':1152}, \
        'sp4': {'width':1536, 'height':768}, 'sp5': {'width':768, 'height':384} }}

        Balboa = {'name': 'Balboa', 'folder': 'sequences/360VR/InterDigital/6K/', \
        'seqFolder': 'Balboa', 'yuvName': 'Balboa_6144x3072_60fps_8bit_420_erp','frate': 60, \
        'width': 6144,'height': 3072,'V3': 600,'VS': 0,'cFormat': 'YUV420_8b', 'playID': 999, \
        'spaSampling': { 'sp1': {'width':6144, 'height':3072}, 'sp2': {'width':3072, 'height':1536}, 'sp3': {'width':2304, 'height':1152}, \
        'sp4': {'width':1536, 'height':768}, 'sp5': {'width':768, 'height':384} }}


        seq = [Landing2, BranCastle2, Broadway, Balboa]

    if classSeq == 'gwandel':

        rollerCoaster = {'name': 'rollerCoaster_30p_3840x2048_8bit', 'folder': 'sequences/360VR/gwandel/', \
        'seqFolder': 'rollerCoaster', 'yuvName': 'rollerCoaster_30p_3840x2048_8bit','frate': 30, \
        'width': 3840,'height': 2048,'V3': 4246,'VS': 0,'cFormat': 'YUV420_8b', 'playID': 999, \
        'spaSampling': { 'sp1': {'width':3840, 'height':2048}, 'sp2': {'width':1920, 'height':1024}, 'sp3': {'width':1440, 'height':768}, \
        'sp4': {'width':960, 'height':512} }}

        timeLapse = {'name': 'timeLapse_30p_3840x2048_8bit', 'folder': 'sequences/360VR/gwandel/', \
        'seqFolder': 'timeLapse', 'yuvName': 'timeLapse_30p_3840x2048_8bit','frate': 30, \
        'width': 3840,'height': 2048,'V3': 4246,'VS': 0,'cFormat': 'YUV420_8b', 'playID': 999, \
        'spaSampling': { 'sp1': {'width':3840, 'height':2048}, 'sp2': {'width':1920, 'height':1024}, 'sp3': {'width':1440, 'height':768}, \
        'sp4': {'width':960, 'height':512} }}

        seq = [rollerCoaster, timeLapse]

    return seq

