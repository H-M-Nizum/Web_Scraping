import pandas as pd
from bs4 import BeautifulSoup
import requests

url = "https://www.airbnb.com/s/dhaka/homes?flexible_trip_lengths%5B%5D=one_week&monthly_start_date=2024-10-01&monthly_length=3&monthly_end_date=2025-01-01&date_picker_type=calendar&refinement_paths%5B%5D=%2Fhomes&source=structured_search_input_header&search_type=filter_change"
r = requests.get(url)
print(r)

soup = BeautifulSoup(r.text, "lxml")
a = soup.find('a', class_="l1ovpqvx atm_1he2i46_1k8pnbi_10saat9 atm_yxpdqi_1pv6nv4_10saat9 atm_1a0hdzc_w1h1e8_10saat9 atm_2bu6ew_929bqk_10saat9 atm_12oyo1u_73u7pn_10saat9 atm_fiaz40_1etamxe_10saat9 c1hw1t9g atm_1s_glywfm atm_5j_1ssbidh atm_3f_idpfg4 atm_9j_tlke0l atm_tl_1gw4zv3 atm_9s_116y0ak atm_h_1h6ojuz atm_fc_1h6ojuz atm_66_nqa18y atm_6h_t94yts atm_l8_idpfg4 atm_gi_idpfg4 atm_2a_1u8qnfj atm_2d_1kn93ch atm_4b_muzi1o atm_7l_jt7fhx atm_70_1dw9ftv atm_uc_10d7vwn atm_kd_glywfm atm_vy_fyhuej atm_e2_fyhuej atm_kd_glywfm_1w3cfyq atm_3f_glywfm_e4a3ld atm_l8_idpfg4_e4a3ld atm_gi_idpfg4_e4a3ld atm_3f_glywfm_1r4qscq atm_kd_glywfm_6y7yyg atm_kd_glywfm_pfnrn2_1oszvuo atm_l8_idpfg4_1icshfk_1oszvuo atm_gi_idpfg4_1icshfk_1oszvuo atm_3f_glywfm_b5gff8_1oszvuo atm_kd_glywfm_2by9w9_1oszvuo atm_k4_1piyxwk_1o5j5ji atm_9j_13gfvf7_1o5j5ji atm_uc_glywfm__1rrf6b5 atm_3f_glywfm_jo46a5 atm_l8_idpfg4_jo46a5 atm_gi_idpfg4_jo46a5 atm_3f_glywfm_1icshfk atm_kd_glywfm_19774hq atm_uc_aaiy6o_1w3cfyq atm_4b_1qnzqti_1w3cfyq atm_26_1qwqy05_1w3cfyq atm_7l_jt7fhx_1w3cfyq atm_70_5ilard_1w3cfyq atm_tr_m1zi52_1w3cfyq atm_uc_glywfm_1w3cfyq_1rrf6b5 atm_uc_aaiy6o_pfnrn2_1oszvuo atm_4b_1qnzqti_pfnrn2_1oszvuo atm_26_1qwqy05_pfnrn2_1oszvuo atm_7l_jt7fhx_pfnrn2_1oszvuo atm_70_5ilard_pfnrn2_1oszvuo atm_tr_m1zi52_pfnrn2_1oszvuo atm_uc_glywfm_pfnrn2_1o31aam atm_4b_muzi1o_1nos8r_uv4tnr atm_2d_1qwqy05_1nos8r_uv4tnr atm_7l_177r58q_1nos8r_uv4tnr atm_70_12rfm42_1nos8r_uv4tnr atm_tr_m1zi52_1nos8r_uv4tnr atm_4b_1k0ymf0_4fughm_uv4tnr atm_2d_1qwqy05_4fughm_uv4tnr atm_7l_9vytuy_4fughm_uv4tnr atm_70_glywfm_4fughm_uv4tnr atm_tr_1h7a3po_4fughm_uv4tnr atm_4b_muzi1o_csw3t1 atm_2d_1qwqy05_csw3t1 atm_7l_177r58q_csw3t1 atm_70_glywfm_csw3t1 atm_tr_1h7a3po_csw3t1 atm_4b_1k0ymf0_1o5j5ji atm_2d_1qwqy05_1o5j5ji atm_7l_9vytuy_1o5j5ji atm_70_glywfm_1o5j5ji atm_tr_1h7a3po_1o5j5ji dir dir-ltr")

print(a)