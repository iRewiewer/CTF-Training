#============================================================================#
#============================ARCANE CALCULATOR===============================#
#============================================================================#

# https://play.picoctf.org/practice/challenge/121

import hashlib
from cryptography.fernet import Fernet
import base64

# GLOBALS --v
arcane_loop_trial = True
jump_into_full = False
full_version_code = ""

def enter_license():
    user_key = input("\nEnter your license key: ")
    user_key = user_key.strip()
    
    if check_key(user_key):
        decrypt_full_version(user_key)
    else:
        print("\nKey is NOT VALID. Check your data entry.\n\n")

def check_key(user_key):

    username_trial =b"GOUGH"

    flag_part = "picoCTF{1n_7h3_|<3y_of_f911a486}"

    print(hashlib.sha256(username_trial).hexdigest()[4])
    print(hashlib.sha256(username_trial).hexdigest()[5])
    print(hashlib.sha256(username_trial).hexdigest()[3])
    print(hashlib.sha256(username_trial).hexdigest()[6])
    print(hashlib.sha256(username_trial).hexdigest()[2])
    print(hashlib.sha256(username_trial).hexdigest()[7])
    print(hashlib.sha256(username_trial).hexdigest()[1])
    print(hashlib.sha256(username_trial).hexdigest()[8])

    # 4 5 3 6 2 7 1 8
    # Check dynamic part --v
    if user_key[i] != hashlib.sha256(username_trial).hexdigest()[4]: return False
    else: i += 1

    if user_key[i] != hashlib.sha256(username_trial).hexdigest()[5]: return False
    else: i += 1

    if user_key[i] != hashlib.sha256(username_trial).hexdigest()[3]: return False
    else: i += 1

    if user_key[i] != hashlib.sha256(username_trial).hexdigest()[6]: return False
    else: i += 1

    if user_key[i] != hashlib.sha256(username_trial).hexdigest()[2]: return False
    else: i += 1

    if user_key[i] != hashlib.sha256(username_trial).hexdigest()[7]: return False
    else: i += 1

    if user_key[i] != hashlib.sha256(username_trial).hexdigest()[1]: return False
    else: i += 1

    if user_key[i] != hashlib.sha256(username_trial).hexdigest()[8]: return False

    return True


def decrypt_full_version(key_str):

    key_base64 = base64.b64encode(key_str.encode())
    f = Fernet(key_base64)

    try:
        with open("keygenme.py", "w") as fout:
          global full_version
          global full_version_code
          full_version_code = f.decrypt(full_version)
          fout.write(full_version_code.decode())
          global arcane_loop_trial
          arcane_loop_trial = False
          global jump_into_full
          jump_into_full = True
          print("\nFull version written to 'keygenme.py'.\n\n"+ \
                 "Exiting trial version...")
    except FileExistsError:
    	sys.stderr.write("Full version of keygenme NOT written to disk, "+ \
	                  "ERROR: 'keygenme.py' file already exists.\n\n"+ \
			  "ADVICE: If this existing file is not valid, "+ \
			  "you may try deleting it and entering the "+ \
			  "license key again. Good luck")

def ui_flow():
    while True:
        enter_license()


# Encrypted blob of full version
def writeGame(key_str):
    f = Fernet(base64.b64encode(key_str.encode()))
    with open("keygenme.py", "w") as fout:
        full_version = b"""
gAAAAABgT_nv39GmDRYkPhrc2hba8UHCHnSTHqdFxXNdemW0svN2hYYw-6n56ErD3NrQYQlNL0sfdsGTmvWKxh5gVRGeCv5kNq-l6PpL0Fzzjo1x_E2Jjbw_xWKIwbvd7BRXFQZKnhs2ehcSEacqES4gsVMOExHUetxFtmYiHLMB0_kqueeT8zf_vcXAPzbiYA0hvD_QSAXzPiKwM2IsGpGzIS5O4_ODq6-knKszeQFstWKFNH_-jNAylCTWSQpPrWqJxCWhSINPhOZ9-PkBsy8lpqmksa6ZBCMvej4W9YFldupRHNoHUHzt8xScEvcsTzIgNmvzOsCBSf5GJGHbLw4yVjsNWmbKRKiE_6BrRMHZW01hcYbfNa1TdJ1MLUX64e_tpDDjMfKvlXZ1qMx4GDwR2lFza9_fm98zoaV-ccgQ1qiSf3wDU1KuKxd9e9TbUAn2TTJfVH9d6IU8emK3QWcn8XRFcMRzVMvlBuNnCVrZmHCYZUzRmwneo15FS-giH63hPzfvjuRfzwp1sFa3wqo5YTJHWejsU0suORvViiDuIpDozmlXTLKLhKj51NkI6QqqDXhMcWkHwKy9V1LN2Furmz_rPbahbNAxnTAWpjF0VELQAvyNHdVy0yxBIbbOJq1oMvHiDJo2adecADc8hMRb4RZJoLqokXxtKLulywhagQjX9METL9bw1YTP9orWXAMwKhTdDbEUdnHViEq8MHo5DcnVvH0yPlnc9Zn2s3_UOfswnhz5vKm0ZbDc5aX0sFTNiMJVjjCrMhQ6HYp5yf_ybd9Tcx_u6xLtwUZBERZWt931n4hQN8n4C_XmDsMehuoSuFmi2NpAuDhX2rcEQK86Ito0KYp-8n2RmbOjzcjo5V5aqHXujmEfX8GYIUWEUKXVcFouF5rZtxtNz3Wsm_j4tqL4Tom27YE5eK7LQSi5B-AsmSF5JGTam2mWeykOGyE-3pHZmNxxkRfdRjxM0uFV13yjQSLFgNIkZ--8n0uAoTb62c7ZFxoFItMNrWasd5zMvp9Nqq70se2KOUieV6VbPJdSL0Sf1uGDmbRFdMmopDm-AuS-7-MLBGiOPmwXtse_9yXjUggeuo3UU4bxyQxCgwh17Ul1ZgxGeopcU7s7Sjm3rqxwlaJWTPRzeF5AXxtZHgyyZjwQ3EB9xYeoMCFh6gsF06bcwnK1Esgar7IYR3JBUfBH6KnWiTyhx_dLkUdomAPMPY0cRoreYsXmFKkEWhYg-TCdifL0nRT8BTEhVyUwFTvqn4PJknTn8NXelYu8co3n8_PoxsOnTrbdNXBJP9vD8Qp2oMi0ZsyCIeekwuX7MCcK4oFVpLGwOrhJdQhJWVqxQdt0ULS-ROB08eOglsXifnVrDl0hi2B0EYcWxxGs-CzsXJPSBvqKWti9XdU5oIhuUH2d7jnAx0pM9tTKqNiL5sfL2mhakMI8XGcljZw2KI0ldgaOW_UvAgh8N3FgKUR4qh_iJ0raoQaaJJFbFneKRoDNT3QsywP_qj6avStEbMGnhN3iBOoc7S3VrN8853X5fow2yDUJaexAKjpYGphE7K4e1g3fHWYjvgnJ-AoXfqALOwDLzaLRjVHSsgF1TQl39XgiAgEzJL-7w_zBn_Hxl5BfYtqe4vxf4PVMZGvof0jXMpM4W-AQ8IW-41LbNgNbPnRuTLubiJCV7MWYu8J7wO0ADSqgv0aXK60IOl0NphAzflWRvjytyT1CljFa0wcsBZvTyyks_ZOoa2__iAj3VlQjcrQynzrxoT5NASs_k51IYPr913nkfOT29oekedYMcxaHzlICLXmjlVHctJfATgYue7xc1BotMDO0Uj5q-wfcg03dq1cZmJ_qhe3AqWrZt3RraYVcvTT2B9Nu2KHBTyjQvCsQMXyFjlqasFZ4jSuNcqybxS3ocP4z-5oGV43zsVjr6YAZyjQiUoLJN6i6h39G5YfH4SStpbTcj7WXWj9WNqxcrF_swHNeIkOPByEa34TIXyJvEOGefZOw7h-F-hxCGuho7LOwabIopS6IykeSLMw1Ra4COmYN-VamVHVUGo50AVEXcmcnHL9NmXP_812Y_sSFdNPo-jglCzjv3KS5jajY1tReYKC9ehz5phUgReaVkiawSc5Tm5BZ42dfJuYZeTwnknsgTWiyGt3Ov6PddqD_40Ye6oHMLO0VjjT_Ul8GWh8hhmxcWxbN8H6dYwLJD0_-YbXvFpRQSi8IQ7BKjY0ZrZm1_tYO87Gg5YcUJznce53ltjXtGCgNIqywt3FDyJ709hOATCIHWf_u-Jfmc7QcIuSss7Rjh68ZgQoQu0Ybjt0Y5bEGEymuyYbgvdUwW8xTksnpl9Jju4x8hMORUQtkyxD0SBG1j7OEsDCK4axMjWxBj4D0liLOSwUuCWr5COJ0Bf_SlydQmufol1HzVIwxTSUG2m7gXEO6cv6gvBIzK0DdcUMjEzXNnqa8davVM0tFvXfuQcgjz8C7tj4-fu4UvikQyAvO5PdSIhClyl06fAyuUmmJgKvyyuoX3plOaMqq5rJbCzXl8OV1anQzSscXIR2Ur_ePhX5IoZNe2XifzLkgVk-lc-Z0gj5Q4WRuo2IYxOcJG-woHvml0oHDY-hQU-gNflauD38YQcfpwdXV0WgcQseWgKNlXfEuldWVktYXn8JNvqVUTOXrNJBEGB9RDyQqp9IubjhQqOJh31eunKYq6oTx4PgjSii0QOKaLKkonBsYtAbb3cUwSoCvek719cI2tp33XWYq2UqQ8J74PtRNzG061_RR_TxHKyWBll-6ii9dgFPki104UzjFkFXkYPzButkzcvcXIDAWD2RNBK6-bshYKS2xr5XxJXgr3QBTWdjrm-p6EwlbFd4DGDR7ran7b38NRkrFD0ignYiKc68xlAPGg9E084LBVXCVlRas8YvYReJH_sl6ZR7faNme2F-qYFzbcvD3jmp5fX0nzvyJuTGWa51qh7siaVBxHETZ_rzoqTh-tr91b_aHPFdcQMfe1Pd-GBQiy9e5N41GQ4MCpvzs87kV5spprXd_DOKnkjeC5bJDFUoIdMk5r-UO2boRH0tHONCbUOzw7HOgFcJUA13yjtvGGbfPPMHvhFMtMDMRw8gacd-5WHaLeh05yBy4UjT_9flAGAqYMWbvrhkAbwEYPJ0abxp1weANOcYZ-gMHm7kn9kF_eTpzKXxWsViR0AekfepQICVZI1eJzLjV2w6qWq7yDA2ALUxFW10GuEqhP9DI_OVVg6AILHPgokj0pcVA9zUizVTWaGnB1Te8_Zlw5Ik-MwNFPJHYLAug14JI4iYeY0zVsgvkpPJmg_dJD4U7Lr4PBwANvyz5NmGZiITqslCAwUDRMK10u3o2ZmSMn-MuBje_9NRYvh8SRvtbWCB46Yj1YMSJvaqci0MaJK8FdPeDPJ84uSK3eWzq75X96k9nVPnHPnlLkcls3480mlq_81V9MTWlLcvgqhEU4FxE7lGjSF9orw7HCK_9lx2rXwuFAaovFweQw2bu7Nr7pH1X82y0XQCI7aeP687QHdONEoIkWikG5Oub8kEGTBq1D4yeRLocq8dPSoRUAPOb6g-QVAOlu3fiJBGIikubJUWSdQ97pbLgxhnpCrRYS3uFZVo-4f5lnwBNEHrR7DuVc13M-rkUXO-oeqrz6Txmr-xAjYtWrg7IsMr-UPihTJC0Gsmm1FAlXtVOmuKYjwOV7DG4aPzE1MjDAHMWidls3ECcueaLdUV-oY6Hw3WwOK_Nnj10sPmWSFSuMPeOBwPEL2M-1tCkbOvilqccCAelhS87qU_fDUKzD68TV1tJIoXEKW4sdwAVGxguEv1BAm4G7LhrH08McB5n3ja5I_3IqkeYdyHaxAXJ-O2thg==
"""
        full_version_code = ""
        full_version_code = f.decrypt(full_version)
        fout.write(full_version_code.decode())

# Enter main loop
ui_flow()

#exec(full_version_code)