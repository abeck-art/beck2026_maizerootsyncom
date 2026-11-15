# -*- coding: utf-8 -*-
"""
Created on Tue May 12 11:46:32 2026

@author: abeck
"""

# Compiled code to build models and run simulations for 7-member maize SynCom
# Accompanies manuscript "Genome-scale community metabolic modeling of maize
# root-associated microbiota shows that root exudates stimulate diverse 
# metabolic interactions"

import cobra
conda activate carveme



##### 1. Constructing individual metabolic models with CarveMe 


# C. pusillum (cpu) individual model, minimal medium, no Biolog data
carve --refseq GCF_002025645.1 -g MzSyn -i MzSyn --mediadb medialibrary.tsv -u grampos -o cpu_Syn.xml
# C. pusillum (cpu) individual model, minimal medium, Biolog data
carve --refseq GCF_002025645.1 -g MzSyn -i MzSyn --mediadb medialibrary.tsv -u grampos --soft Soft_cpu.tsv -o cpu_Syn_soft.xml
# C. pusillum (cpu) individual model, root exudate medium, no Biolog data
carve --refseq GCF_002025645.1 -g MzExud -i MzExud --mediadb medialibrary.tsv -u grampos -o cpu_Exud.xml
# C. pusillum (cpu) individual model, root exduate medium, Biolog data
carve --refseq GCF_002025645.1 -g MzExud -i MzExud --mediadb medialibrary.tsv -u grampos --soft Soft_cpu.tsv -o cpu_Exud_soft.xml

# E. ludwigii (elu) individual model, minimal medium, no Biolog data
carve --refseq GCF_002025685.1 -g MzSyn -i MzSyn --mediadb medialibrary.tsv -u gramneg -o elu_Syn.xml
# E. ludwigii (elu) individual model, minimal medium, Biolog data
carve --refseq GCF_002025685.1 -g MzSyn -i MzSyn --mediadb medialibrary.tsv -u gramneg --soft Soft_elu.tsv -o elu_Syn_soft.xml
# E. ludwigii (elu) individual model, root exudate medium, no Biolog data
carve --refseq GCF_002025685.1 -g MzExud -i MzExud --mediadb medialibrary.tsv -u gramneg -o elu_Exud.xml
# E. ludwigii (elu) individual model, root exudate medium, Biolog data
carve --refseq GCF_002025685.1 -g MzExud -i MzExud --mediadb medialibrary.tsv -u gramneg --soft Soft_elu.tsv -o elu_Exud_soft.xml

# H. robiniae (hro) individual model, minimal medium, no Biolog data
carve --refseq GCF_002025725.1 -g MzSyn -i MzSyn --mediadb medialibrary.tsv -u gramneg -o hro_Syn.xml
# H. robiniae (hro) individual model, minimal medium, Biolog data
carve --refseq GCF_002025725.1 -g MzSyn -i MzSyn --mediadb medialibrary.tsv -u gramneg --soft Soft_hro.tsv -o hro_Syn_soft.xml
# H. robiniae (hro) individual model, root exudate medium, no Biolog data
carve --refseq GCF_002025725.1 -g MzExud -i MzExud --mediadb medialibrary.tsv -u gramneg -o hro_Exud.xml
# H. robiniae (hro) individual model, root exudate medium, Biolog data
carve --refseq GCF_002025725.1 -g MzExud -i MzExud --mediadb medialibrary.tsv -u gramneg --soft Soft_hro.tsv -o hro_Exud_soft.xml

# P. putida (ppu) individual model, minimal medium, no Biolog data
carve --refseq GCF_002025705.1 -g MzSyn -i MzSyn --mediadb medialibrary.tsv -u gramneg -o ppu_Syn.xml
# P. putida (ppu) individual model, minimal medium, Biolog data
carve --refseq GCF_002025705.1 -g MzSyn -i MzSyn --mediadb medialibrary.tsv -u gramneg --soft Soft_ppu.tsv -o ppu_Syn_soft.xml
# P. putida (ppu) individual model, root exudate medium, no Biolog data
carve --refseq GCF_002025705.1 -g MzExud -i MzExud --mediadb medialibrary.tsv -u gramneg -o ppu_Exud.xml
# P. putida (ppu) individual model, root exudate medium, Biolog data
carve --refseq GCF_002025705.1 -g MzExud -i MzExud --mediadb medialibrary.tsv -u gramneg --soft Soft_ppu.tsv -o ppu_Exud_soft.xml

# S. maltophilia (sma) individual model, minimal medium, no Biolog data
carve --refseq GCF_002025605.1 -g MzSyn -i MzSyn --mediadb medialibrary.tsv -u gramneg -o sma_Syn.xml
# S. maltophilia (sma) individual model, minimal medium, Biolog data
carve --refseq GCF_002025605.1 -g MzSyn -i MzSyn --mediadb medialibrary.tsv -u gramneg --soft Soft_sma.tsv -o sma_Syn_soft.xml
# S. maltophilia (sma) individual model, root exudate medium, no Biolog data
carve --refseq GCF_002025605.1 -g MzExud -i MzExud --mediadb medialibrary.tsv -u gramneg -o sma_Exud.xml
# S. maltophilia (sma) individual model, root exudate medium, Biolog data
carve --refseq GCF_002025605.1 -g MzExud -i MzExud --mediadb medialibrary.tsv -u gramneg --soft Soft_sma.tsv -o sma_Exud_soft.xml

# B. pituitosa (opi) individual model, minimal medium, no Biolog data
carve --refseq GCF_002025625.1 -g MzSyn -i MzSyn --mediadb medialibrary.tsv -u gramneg -o opi_Syn.xml
# B. pituitosa (opi) individual model, minimal medium, Biolog data
carve --refseq GCF_002025625.1 -g MzSyn -i MzSyn --mediadb medialibrary.tsv -u gramneg --soft Soft_opi.tsv -o opi_Syn_soft.xml
# B. pituitosa (opi) individual model, root exudate medium, no Biolog data
carve --refseq GCF_002025625.1 -g MzExud -i MzExud --mediadb medialibrary.tsv -u gramneg -o opi_Exud.xml
# B. pituitosa (opi) individual model, root exudate medium, Biolog data
carve --refseq GCF_002025625.1 -g MzExud -i MzExud --mediadb medialibrary.tsv -u gramneg --soft Soft_opi.tsv -o opi_Exud_soft.xml 

# C. indologenes (cin) individual model, minimal medium, no Biolog data
carve --refseq GCF_002025665.1 -g MzSyn -i MzSyn --mediadb medialibrary.tsv -u gramneg -o cin_Syn.xml
# C. indologenes (cin) individual model, minimal medium, Biolog data
carve --refseq GCF_002025665.1 -g MzSyn -i MzSyn --mediadb medialibrary.tsv -u gramneg --soft Soft_cin.tsv -o cin_Syn_soft.xml
# C. indologenes (cin) individual model, root exudate medium, no Biolog data
carve --refseq GCF_002025665.1 -g MzExud -i MzExud --mediadb medialibrary.tsv -u gramneg -o cin_Exud.xml
# C. indologenes (cin) individual model, root exduate medium, Biolog data
carve --refseq GCF_002025665.1 -g MzExud -i MzExud --mediadb medialibrary.tsv -u gramneg --soft Soft_cin.tsv -o cin_Exud_soft.xml



##### 2. Perform FBA simulations to compare individual species models with and without Biolog data (Figure 2)

# C. pusillum (cpu)
model_Syn_cpu = cobra.io.read_sbml_model("cpu_Syn.xml")
model_SynSoft_cpu = cobra.io.read_sbml_model("cpu_Syn_soft.xml")
model_Exud_cpu = cobra.io.read_sbml_model("cpu_Exud.xml")
model_ExudSoft_cpu = cobra.io.read_sbml_model("cpu_Exud_soft.xml")
solS_cpu = model_Syn_cpu.optimize() # minimal medium without Biolog
solSS_cpu = model_SynSoft_cpu.optimize() # minimal medium with Biolog
solE_cpu = model_Exud_cpu.optimize() # exudate medium without Biolog
solES_cpu = model_ExudSoft_cpu.optimize() # exudate medium with Biolog

# E. ludwigii (elu)
model_Syn_elu = cobra.io.read_sbml_model("elu_Syn.xml")
model_SynSoft_elu = cobra.io.read_sbml_model("elu_Syn_soft.xml")
model_Exud_elu = cobra.io.read_sbml_model("elu_Exud.xml")
model_ExudSoft_elu = cobra.io.read_sbml_model("elu_Exud_soft.xml")
solS_elu = model_Syn_elu.optimize() # minimal medium without Biolog
solSS_elu = model_SynSoft_elu.optimize() # minimal medium with Biolog
solE_elu = model_Exud_elu.optimize() # exudate medium without Biolog
solES_elu = model_ExudSoft_elu.optimize() # exudate medium with Biolog

# H. robiniae (hro)
model_Syn_hro = cobra.io.read_sbml_model("hro_Syn.xml")
model_SynSoft_hro = cobra.io.read_sbml_model("hro_Syn_soft.xml")
model_Exud_hro = cobra.io.read_sbml_model("hro_Exud.xml")
model_ExudSoft_hro = cobra.io.read_sbml_model("hro_Exud_soft.xml")
solS_hro = model_Syn_hro.optimize() # minimal medium without Biolog
solSS_hro = model_SynSoft_hro.optimize() # minimal medium with Biolog
solE_hro = model_Exud_hro.optimize() # exudate medium without Biolog
solES_hro = model_ExudSoft_hro.optimize() # exudate medium with Biolog

# P. putida (ppu)
model_Syn_ppu = cobra.io.read_sbml_model("ppu_Syn.xml")
model_SynSoft_ppu = cobra.io.read_sbml_model("ppu_Syn_soft.xml")
model_Exud_ppu = cobra.io.read_sbml_model("ppu_Exud.xml")
model_ExudSoft_ppu = cobra.io.read_sbml_model("ppu_Exud_soft.xml")
solS_ppu = model_Syn_ppu.optimize() # minimal medium without Biolog
solSS_ppu = model_SynSoft_ppu.optimize() # minimal medium with Biolog
solE_ppu = model_Exud_ppu.optimize() # exudate medium without Biolog
solES_ppu = model_ExudSoft_ppu.optimize() # exudate medium with Biolog

# S. maltophilia (sma)
model_Syn_sma = cobra.io.read_sbml_model("sma_Syn.xml")
model_SynSoft_sma = cobra.io.read_sbml_model("sma_Syn_soft.xml")
model_Exud_sma = cobra.io.read_sbml_model("sma_Exud.xml")
model_ExudSoft_sma = cobra.io.read_sbml_model("sma_Exud_soft.xml")
solS_sma = model_Syn_sma.optimize() # minimal medium without Biolog
solSS_sma = model_SynSoft_sma.optimize() # minimal medium with Biolog
solE_sma = model_Exud_sma.optimize() # exudate medium without Biolog
solES_sma = model_ExudSoft_sma.optimize() # exudate medium with Biolog

### B. pituitosa (opi)
model_Syn_opi = cobra.io.read_sbml_model("opi_Syn.xml")
model_SynSoft_opi = cobra.io.read_sbml_model("opi_Syn_soft.xml")
model_Exud_opi = cobra.io.read_sbml_model("opi_Exud.xml")
model_ExudSoft_opi = cobra.io.read_sbml_model("opi_Exud_soft.xml")
solS_opi = model_Syn_opi.optimize() # minimal medium without Biolog
solSS_opi = model_SynSoft_opi.optimize() # minimal medium with Biolog
solE_opi = model_Exud_opi.optimize() # exudate medium without Biolog
solES_opi = model_ExudSoft_opi.optimize() # exudate medium with Biolog

# C. indologenes (cin)
model_Syn_cin = cobra.io.read_sbml_model("cin_Syn.xml")
model_SynSoft_cin = cobra.io.read_sbml_model("cin_Syn_soft.xml")
model_Exud_cin = cobra.io.read_sbml_model("cin_Exud.xml")
model_ExudSoft_cin = cobra.io.read_sbml_model("cin_Exud_soft.xml")
solS_cin = model_Syn_cin.optimize() # minimal medium without Biolog
solSS_cin = model_SynSoft_cin.optimize() # minimal medium with Biolog
solE_cin = model_Exud_cin.optimize() # exudate medium without Biolog
solES_cin = model_ExudSoft_cin.optimize() # exudate medium with Biolog



##### 3. Set substrate uptake constraints for each species model incorporating Biolog data (both minimal and exudate medium), to be used in media comparison simulations (Figure 3)

# Run parallel sets of commands for each species, clearing the "model" variable in between each species/medium
# Could be run in a loop, but each model was ran and checked separately due to absence of some uptake reactions, which would cause an error:
# Check if model reaction exists in model - if so, set the boundary; if not, skip (commented reactions)

# C. pusillum (cpu), minimal medium
model = cobra.io.read_sbml_model("cpu_Syn_soft.xml")
solBefore = model.optimize() # optimization solution before
# Adjust boundaries for major carbon source uptake
model.reactions.get_by_id("EX_glc__D_e").lower_bound #glucose check
model.reactions.get_by_id("EX_glc__D_e").lower_bound = -5
model.reactions.get_by_id("EX_mal__L_e").lower_bound #malate check
#model.reactions.get_by_id("EX_mal__L_e").lower_bound = -5
# Adjust boundaries for amino acid uptake
model.reactions.get_by_id("EX_arg__L_e").lower_bound #arginine check
model.reactions.get_by_id("EX_arg__L_e").lower_bound = -(0.25/9)
model.reactions.get_by_id("EX_asn__L_e").lower_bound #asparagine check
model.reactions.get_by_id("EX_asn__L_e").lower_bound = -(0.25/9)
model.reactions.get_by_id("EX_cys__L_e").lower_bound #cysteine check
#model.reactions.get_by_id("EX_cys__L_e").lower_bound = -(0.25/9)
model.reactions.get_by_id("EX_gln__L_e").lower_bound #glutamine check
model.reactions.get_by_id("EX_gln__L_e").lower_bound = -(0.25/9)
model.reactions.get_by_id("EX_ile__L_e").lower_bound #isoleucine check
model.reactions.get_by_id("EX_ile__L_e").lower_bound = -(0.25/9)
model.reactions.get_by_id("EX_leu__L_e").lower_bound #leucine check
model.reactions.get_by_id("EX_leu__L_e").lower_bound = -(0.25/9)
model.reactions.get_by_id("EX_lys__L_e").lower_bound #lysine check
model.reactions.get_by_id("EX_lys__L_e").lower_bound = -(0.25/9)
model.reactions.get_by_id("EX_pro__L_e").lower_bound #proline check
model.reactions.get_by_id("EX_pro__L_e").lower_bound = -(0.25/9)
model.reactions.get_by_id("EX_ser__L_e").lower_bound #serine check
model.reactions.get_by_id("EX_ser__L_e").lower_bound = -(0.25/9)
# Adjust boundaries for vitamin uptake
model.reactions.get_by_id("EX_btn_e").lower_bound #biotin check
model.reactions.get_by_id("EX_btn_e").lower_bound = -0.001
model.reactions.get_by_id("EX_cbl1_e").lower_bound #cobalamin check
#model.reactions.get_by_id("EX_cbl1_e").lower_bound = -0.001
model.reactions.get_by_id("EX_nac_e").lower_bound #niacin check
#model.reactions.get_by_id("EX_nac_e").lower_bound = -0.001
model.reactions.get_by_id("EX_pnto__R_e").lower_bound #pantothenate check
#model.reactions.get_by_id("EX_pnto__R_e").lower_bound = -0.001
model.reactions.get_by_id("EX_pydxn_e").lower_bound #pyridoxine check
#model.reactions.get_by_id("EX_pydxn_e").lower_bound = -0.001
model.reactions.get_by_id("EX_ribflv_e").lower_bound #riboflavin check
#model.reactions.get_by_id("EX_ribflv_e").lower_bound = -0.001
solAfter=model.optimize()
# Save model with constraints set
cobra.io.write_sbml_model(model, "cpu_Syn_soft_Bnds.xml")

# C. pusillum (cpu), root exudate medium
model = cobra.io.read_sbml_model("cpu_Exud_soft.xml")
solBefore = model.optimize() # optimization solution before
# Adjust boundaries for major carbon source uptake
model.reactions.get_by_id("EX_glyc_e").lower_bound #glycerol check
model.reactions.get_by_id("EX_glyc_e").lower_bound = -(10/24)
model.reactions.get_by_id("EX_rbt_e").lower_bound #ribitol check
model.reactions.get_by_id("EX_rbt_e").lower_bound = -(10/24)
model.reactions.get_by_id("EX_fru_e").lower_bound #fructose check
model.reactions.get_by_id("EX_fru_e").lower_bound = -(10/24)
model.reactions.get_by_id("EX_malt_e").lower_bound #maltose check
model.reactions.get_by_id("EX_malt_e").lower_bound = -(10/24)
model.reactions.get_by_id("EX_inost_e").lower_bound #inositol check
model.reactions.get_by_id("EX_inost_e").lower_bound = -(10/24)
model.reactions.get_by_id("EX_erthrs_e").lower_bound #erythrose check
#model.reactions.get_by_id("EX_erthrs_e").lower_bound = -(10/24)
model.reactions.get_by_id("EX_glc__D_e").lower_bound #glucose check
model.reactions.get_by_id("EX_glc__D_e").lower_bound = -(10/24)
model.reactions.get_by_id("EX_sucr_e").lower_bound #sucrose check
model.reactions.get_by_id("EX_sucr_e").lower_bound = -(10/24)
model.reactions.get_by_id("EX_arab__L_e").lower_bound #arabinose check
model.reactions.get_by_id("EX_arab__L_e").lower_bound = -(10/24)
model.reactions.get_by_id("EX_melib_e").lower_bound #melibiose check
model.reactions.get_by_id("EX_melib_e").lower_bound = -(10/24)
model.reactions.get_by_id("EX_lcts_e").lower_bound #lactose check
model.reactions.get_by_id("EX_lcts_e").lower_bound = -(10/24)
model.reactions.get_by_id("EX_isomal_e").lower_bound #isomaltose check
#model.reactions.get_by_id("EX_isomal_e").lower_bound = -(10/24)
model.reactions.get_by_id("EX_gal_e").lower_bound #galactose check
model.reactions.get_by_id("EX_gal_e").lower_bound = -(10/24)
model.reactions.get_by_id("EX_xyl__D_e").lower_bound #xylose check
model.reactions.get_by_id("EX_xyl__D_e").lower_bound = -(10/24)
model.reactions.get_by_id("EX_mal__L_e").lower_bound #malate check
#model.reactions.get_by_id("EX_mal__L_e").lower_bound = -(10/24)
model.reactions.get_by_id("EX_succ_e").lower_bound #succinate check
#model.reactions.get_by_id("EX_succ_e").lower_bound = -(10/24)
model.reactions.get_by_id("EX_cit_e").lower_bound #citrate check
model.reactions.get_by_id("EX_cit_e").lower_bound = -(10/24)
model.reactions.get_by_id("EX_oaa_e").lower_bound #oxaloacetate check
#model.reactions.get_by_id("EX_oaa_e").lower_bound = -(10/24)
model.reactions.get_by_id("EX_fum_e").lower_bound #fumarate check
#model.reactions.get_by_id("EX_fum_e").lower_bound = -(10/24)
model.reactions.get_by_id("EX_bz_e").lower_bound #benzoate check
#model.reactions.get_by_id("EX_bz_e").lower_bound = -(10/24)
model.reactions.get_by_id("EX_acon_C_e").lower_bound #cis-aconitate check
#model.reactions.get_by_id("EX_acon_C_e").lower_bound = -(10/24)
model.reactions.get_by_id("EX_tartr__L_e").lower_bound #tartaric acid check
#model.reactions.get_by_id("EX_tartr__L_e").lower_bound = -(10/24)
model.reactions.get_by_id("EX_lac__L_e").lower_bound #lactate check
model.reactions.get_by_id("EX_lac__L_e").lower_bound = -(10/24)
model.reactions.get_by_id("EX_malon_e").lower_bound #malonate check
#model.reactions.get_by_id("EX_malon_e").lower_bound = -(10/24)
# Adjust boundaries for amino acid and nucleoside uptake
model.reactions.get_by_id("EX_lys__L_e").lower_bound #lysine check
model.reactions.get_by_id("EX_lys__L_e").lower_bound = -(0.25/18)
model.reactions.get_by_id("EX_arg__L_e").lower_bound #arginine check
model.reactions.get_by_id("EX_arg__L_e").lower_bound = -(0.25/18)
model.reactions.get_by_id("EX_gln__L_e").lower_bound #glutamine check
model.reactions.get_by_id("EX_gln__L_e").lower_bound = -(0.25/18)
model.reactions.get_by_id("EX_ser__L_e").lower_bound #serine check
model.reactions.get_by_id("EX_ser__L_e").lower_bound = -(0.25/18)
model.reactions.get_by_id("EX_leu__L_e").lower_bound #leucine check
model.reactions.get_by_id("EX_leu__L_e").lower_bound = -(0.25/18)
model.reactions.get_by_id("EX_asn__L_e").lower_bound #asparagine check
model.reactions.get_by_id("EX_asn__L_e").lower_bound = -(0.25/18)
model.reactions.get_by_id("EX_ile__L_e").lower_bound #isoleucine check
model.reactions.get_by_id("EX_ile__L_e").lower_bound = -(0.25/18)
model.reactions.get_by_id("EX_asp__L_e").lower_bound #aspartate check
model.reactions.get_by_id("EX_asp__L_e").lower_bound = -(0.25/18)
model.reactions.get_by_id("EX_ala__L_e").lower_bound #alanine check
model.reactions.get_by_id("EX_ala__L_e").lower_bound = -(0.25/18)
model.reactions.get_by_id("EX_gly_e").lower_bound #glycine check
model.reactions.get_by_id("EX_gly_e").lower_bound = -(0.25/18)
model.reactions.get_by_id("EX_val__L_e").lower_bound #valine check
model.reactions.get_by_id("EX_val__L_e").lower_bound = -(0.25/18)
model.reactions.get_by_id("EX_glu__L_e").lower_bound #glutamate check
model.reactions.get_by_id("EX_glu__L_e").lower_bound = -(0.25/18)
model.reactions.get_by_id("EX_thr__L_e").lower_bound #threonine check
model.reactions.get_by_id("EX_thr__L_e").lower_bound = -(0.25/18)
model.reactions.get_by_id("EX_tyr__L_e").lower_bound #tyrosine check
model.reactions.get_by_id("EX_tyr__L_e").lower_bound = -(0.25/18)
model.reactions.get_by_id("EX_his__L_e").lower_bound #histidine check
model.reactions.get_by_id("EX_his__L_e").lower_bound = -(0.25/18)
model.reactions.get_by_id("EX_4abut_e").lower_bound #aminobutanoate check
#model.reactions.get_by_id("EX_4abut_e").lower_bound = -(0.25/18)
model.reactions.get_by_id("EX_cytd_e").lower_bound #cytidine check
model.reactions.get_by_id("EX_cytd_e").lower_bound = -(0.25/18)
model.reactions.get_by_id("EX_thymd_e").lower_bound #thymidine check
#model.reactions.get_by_id("EX_thymd_e").lower_bound = -(0.25/18)
solAfter=model.optimize()
# Save model with constraints set
cobra.io.write_sbml_model(model, "cpu_Exud_soft_Bnds.xml")

### E. ludwigii (elu), minimal medium
model = cobra.io.read_sbml_model("elu_Syn_soft.xml")
solBefore = model.optimize() # optimization solution before
# Adjust boundaries for major carbon source uptake
model.reactions.get_by_id("EX_glc__D_e").lower_bound #glucose check
model.reactions.get_by_id("EX_glc__D_e").lower_bound = -5
model.reactions.get_by_id("EX_mal__L_e").lower_bound #malate check
model.reactions.get_by_id("EX_mal__L_e").lower_bound = -5
# Adjust boundaries for amino acid uptake
model.reactions.get_by_id("EX_arg__L_e").lower_bound #arginine check
model.reactions.get_by_id("EX_arg__L_e").lower_bound = -(0.25/9)
model.reactions.get_by_id("EX_asn__L_e").lower_bound #asparagine check
model.reactions.get_by_id("EX_asn__L_e").lower_bound = -(0.25/9)
model.reactions.get_by_id("EX_cys__L_e").lower_bound #cysteine check
#model.reactions.get_by_id("EX_cys__L_e").lower_bound = -(0.25/9)
model.reactions.get_by_id("EX_gln__L_e").lower_bound #glutamine check
model.reactions.get_by_id("EX_gln__L_e").lower_bound = -(0.25/9)
model.reactions.get_by_id("EX_ile__L_e").lower_bound #isoleucine check
model.reactions.get_by_id("EX_ile__L_e").lower_bound = -(0.25/9)
model.reactions.get_by_id("EX_leu__L_e").lower_bound #leucine check
model.reactions.get_by_id("EX_leu__L_e").lower_bound = -(0.25/9)
model.reactions.get_by_id("EX_lys__L_e").lower_bound #lysine check
model.reactions.get_by_id("EX_lys__L_e").lower_bound = -(0.25/9)
model.reactions.get_by_id("EX_pro__L_e").lower_bound #proline check
model.reactions.get_by_id("EX_pro__L_e").lower_bound = -(0.25/9)
model.reactions.get_by_id("EX_ser__L_e").lower_bound #serine check
model.reactions.get_by_id("EX_ser__L_e").lower_bound = -(0.25/9)
# Adjust boundaries for vitamin uptake
model.reactions.get_by_id("EX_btn_e").lower_bound #biotin check
model.reactions.get_by_id("EX_btn_e").lower_bound = -0.001
model.reactions.get_by_id("EX_cbl1_e").lower_bound #cobalamin check
#model.reactions.get_by_id("EX_cbl1_e").lower_bound = -0.001
model.reactions.get_by_id("EX_nac_e").lower_bound #niacin check
model.reactions.get_by_id("EX_nac_e").lower_bound = -0.001
model.reactions.get_by_id("EX_pnto__R_e").lower_bound #pantothenate check
model.reactions.get_by_id("EX_pnto__R_e").lower_bound = -0.001
model.reactions.get_by_id("EX_pydxn_e").lower_bound #pyridoxine check
model.reactions.get_by_id("EX_pydxn_e").lower_bound = -0.001
model.reactions.get_by_id("EX_ribflv_e").lower_bound #riboflavin check
#model.reactions.get_by_id("EX_ribflv_e").lower_bound = -0.001
solAfter=model.optimize()
# Save model with constraints set
cobra.io.write_sbml_model(model, "elu_Syn_soft_Bnds.xml")

### E. ludwigii (elu), root exudate medium
model = cobra.io.read_sbml_model("elu_Exud_soft.xml")
solBefore = model.optimize() # optimization solution before
# Adjust boundaries for major carbon source uptake
model.reactions.get_by_id("EX_glyc_e").lower_bound #glycerol check
model.reactions.get_by_id("EX_glyc_e").lower_bound = -(10/24)
model.reactions.get_by_id("EX_rbt_e").lower_bound #ribitol check
#model.reactions.get_by_id("EX_rbt_e").lower_bound = -(10/24)
model.reactions.get_by_id("EX_fru_e").lower_bound #fructose check
model.reactions.get_by_id("EX_fru_e").lower_bound = -(10/24)
model.reactions.get_by_id("EX_malt_e").lower_bound #maltose check
model.reactions.get_by_id("EX_malt_e").lower_bound = -(10/24)
model.reactions.get_by_id("EX_inost_e").lower_bound #inositol check
model.reactions.get_by_id("EX_inost_e").lower_bound = -(10/24)
model.reactions.get_by_id("EX_erthrs_e").lower_bound #erythrose check
#model.reactions.get_by_id("EX_erthrs_e").lower_bound = -(10/24)
model.reactions.get_by_id("EX_glc__D_e").lower_bound #glucose check
model.reactions.get_by_id("EX_glc__D_e").lower_bound = -(10/24)
model.reactions.get_by_id("EX_sucr_e").lower_bound #sucrose check
model.reactions.get_by_id("EX_sucr_e").lower_bound = -(10/24)
model.reactions.get_by_id("EX_arab__L_e").lower_bound #arabinose check
model.reactions.get_by_id("EX_arab__L_e").lower_bound = -(10/24)
model.reactions.get_by_id("EX_melib_e").lower_bound #melibiose check
model.reactions.get_by_id("EX_melib_e").lower_bound = -(10/24)
model.reactions.get_by_id("EX_lcts_e").lower_bound #lactose check
model.reactions.get_by_id("EX_lcts_e").lower_bound = -(10/24)
model.reactions.get_by_id("EX_isomal_e").lower_bound #isomaltose check
#model.reactions.get_by_id("EX_isomal_e").lower_bound = -(10/24)
model.reactions.get_by_id("EX_gal_e").lower_bound #galactose check
model.reactions.get_by_id("EX_gal_e").lower_bound = -(10/24)
model.reactions.get_by_id("EX_xyl__D_e").lower_bound #xylose check
model.reactions.get_by_id("EX_xyl__D_e").lower_bound = -(10/24)
model.reactions.get_by_id("EX_mal__L_e").lower_bound #malate check
model.reactions.get_by_id("EX_mal__L_e").lower_bound = -(10/24)
model.reactions.get_by_id("EX_succ_e").lower_bound #succinate check
model.reactions.get_by_id("EX_succ_e").lower_bound = -(10/24)
model.reactions.get_by_id("EX_cit_e").lower_bound #citrate check
model.reactions.get_by_id("EX_cit_e").lower_bound = -(10/24)
model.reactions.get_by_id("EX_oaa_e").lower_bound #oxaloacetate check
model.reactions.get_by_id("EX_oaa_e").lower_bound = -(10/24)
model.reactions.get_by_id("EX_fum_e").lower_bound #fumarate check
model.reactions.get_by_id("EX_fum_e").lower_bound = -(10/24)
model.reactions.get_by_id("EX_bz_e").lower_bound #benzoate check
model.reactions.get_by_id("EX_bz_e").lower_bound = -(10/24)
model.reactions.get_by_id("EX_acon_C_e").lower_bound #cis-aconitate check
#model.reactions.get_by_id("EX_acon_C_e").lower_bound = -(10/24)
model.reactions.get_by_id("EX_tartr__L_e").lower_bound #tartaric acid check
#model.reactions.get_by_id("EX_tartr__L_e").lower_bound = -(10/24)
model.reactions.get_by_id("EX_lac__L_e").lower_bound #lactate check
model.reactions.get_by_id("EX_lac__L_e").lower_bound = -(10/24)
model.reactions.get_by_id("EX_malon_e").lower_bound #malonate check
#model.reactions.get_by_id("EX_malon_e").lower_bound = -(10/24)
# Adjust boundaries for amino acid and nucleoside uptake
model.reactions.get_by_id("EX_lys__L_e").lower_bound #lysine check
model.reactions.get_by_id("EX_lys__L_e").lower_bound = -(0.25/18)
model.reactions.get_by_id("EX_arg__L_e").lower_bound #arginine check
model.reactions.get_by_id("EX_arg__L_e").lower_bound = -(0.25/18)
model.reactions.get_by_id("EX_gln__L_e").lower_bound #glutamine check
model.reactions.get_by_id("EX_gln__L_e").lower_bound = -(0.25/18)
model.reactions.get_by_id("EX_ser__L_e").lower_bound #serine check
model.reactions.get_by_id("EX_ser__L_e").lower_bound = -(0.25/18)
model.reactions.get_by_id("EX_leu__L_e").lower_bound #leucine check
model.reactions.get_by_id("EX_leu__L_e").lower_bound = -(0.25/18)
model.reactions.get_by_id("EX_asn__L_e").lower_bound #asparagine check
model.reactions.get_by_id("EX_asn__L_e").lower_bound = -(0.25/18)
model.reactions.get_by_id("EX_ile__L_e").lower_bound #isoleucine check
model.reactions.get_by_id("EX_ile__L_e").lower_bound = -(0.25/18)
model.reactions.get_by_id("EX_asp__L_e").lower_bound #aspartate check
model.reactions.get_by_id("EX_asp__L_e").lower_bound = -(0.25/18)
model.reactions.get_by_id("EX_ala__L_e").lower_bound #alanine check
model.reactions.get_by_id("EX_ala__L_e").lower_bound = -(0.25/18)
model.reactions.get_by_id("EX_gly_e").lower_bound #glycine check
model.reactions.get_by_id("EX_gly_e").lower_bound = -(0.25/18)
model.reactions.get_by_id("EX_val__L_e").lower_bound #valine check
model.reactions.get_by_id("EX_val__L_e").lower_bound = -(0.25/18)
model.reactions.get_by_id("EX_glu__L_e").lower_bound #glutamate check
model.reactions.get_by_id("EX_glu__L_e").lower_bound = -(0.25/18)
model.reactions.get_by_id("EX_thr__L_e").lower_bound #threonine check
model.reactions.get_by_id("EX_thr__L_e").lower_bound = -(0.25/18)
model.reactions.get_by_id("EX_tyr__L_e").lower_bound #tyrosine check
model.reactions.get_by_id("EX_tyr__L_e").lower_bound = -(0.25/18)
model.reactions.get_by_id("EX_his__L_e").lower_bound #histidine check
model.reactions.get_by_id("EX_his__L_e").lower_bound = -(0.25/18)
model.reactions.get_by_id("EX_4abut_e").lower_bound #aminobutanoate check
model.reactions.get_by_id("EX_4abut_e").lower_bound = -(0.25/18)
model.reactions.get_by_id("EX_cytd_e").lower_bound #cytidine check
model.reactions.get_by_id("EX_cytd_e").lower_bound = -(0.25/18)
model.reactions.get_by_id("EX_thymd_e").lower_bound #thymidine check
model.reactions.get_by_id("EX_thymd_e").lower_bound = -(0.25/18)
solAfter=model.optimize()
# Save model with constraints set
cobra.io.write_sbml_model(model, "elu_Exud_soft_Bnds.xml")

# H. robiniae (hro) minimal medium
model = cobra.io.read_sbml_model("hro_Syn_soft.xml")
solBefore = model.optimize() # optimization solution before
# Adjust boundaries for major carbon source uptake
model.reactions.get_by_id("EX_glc__D_e").lower_bound #glucose check
model.reactions.get_by_id("EX_glc__D_e").lower_bound = -5
model.reactions.get_by_id("EX_mal__L_e").lower_bound #malate check
model.reactions.get_by_id("EX_mal__L_e").lower_bound = -5
# Adjust boundaries for amino acid uptake
model.reactions.get_by_id("EX_arg__L_e").lower_bound #arginine check
model.reactions.get_by_id("EX_arg__L_e").lower_bound = -(0.25/9)
model.reactions.get_by_id("EX_asn__L_e").lower_bound #asparagine check
model.reactions.get_by_id("EX_asn__L_e").lower_bound = -(0.25/9)
model.reactions.get_by_id("EX_cys__L_e").lower_bound #cysteine check
#model.reactions.get_by_id("EX_cys__L_e").lower_bound = -(0.25/9)
model.reactions.get_by_id("EX_gln__L_e").lower_bound #glutamine check
model.reactions.get_by_id("EX_gln__L_e").lower_bound = -(0.25/9)
model.reactions.get_by_id("EX_ile__L_e").lower_bound #isoleucine check
model.reactions.get_by_id("EX_ile__L_e").lower_bound = -(0.25/9)
model.reactions.get_by_id("EX_leu__L_e").lower_bound #leucine check
model.reactions.get_by_id("EX_leu__L_e").lower_bound = -(0.25/9)
model.reactions.get_by_id("EX_lys__L_e").lower_bound #lysine check
model.reactions.get_by_id("EX_lys__L_e").lower_bound = -(0.25/9)
model.reactions.get_by_id("EX_pro__L_e").lower_bound #proline check
model.reactions.get_by_id("EX_pro__L_e").lower_bound = -(0.25/9)
model.reactions.get_by_id("EX_ser__L_e").lower_bound #serine check
model.reactions.get_by_id("EX_ser__L_e").lower_bound = -(0.25/9)
# Adjust boundaries for vitamin uptake
model.reactions.get_by_id("EX_btn_e").lower_bound #biotin check
#model.reactions.get_by_id("EX_btn_e").lower_bound = -0.001
model.reactions.get_by_id("EX_cbl1_e").lower_bound #cobalamin check
#model.reactions.get_by_id("EX_cbl1_e").lower_bound = -0.001
model.reactions.get_by_id("EX_nac_e").lower_bound #niacin check
model.reactions.get_by_id("EX_nac_e").lower_bound = -0.001
model.reactions.get_by_id("EX_pnto__R_e").lower_bound #pantothenate check
#model.reactions.get_by_id("EX_pnto__R_e").lower_bound = -0.001
model.reactions.get_by_id("EX_pydxn_e").lower_bound #pyridoxine check
#model.reactions.get_by_id("EX_pydxn_e").lower_bound = -0.001
model.reactions.get_by_id("EX_ribflv_e").lower_bound #riboflavin check
#model.reactions.get_by_id("EX_ribflv_e").lower_bound = -0.001
solAfter=model.optimize()
# Save model with constraints set
cobra.io.write_sbml_model(model, "hro_Syn_soft_Bnds.xml")

### H. robiniae (hro) root exudate medium
model = cobra.io.read_sbml_model("hro_Exud_soft.xml")
solBefore = model.optimize() # optimization solution before
# Adjust boundaries for major carbon source uptake
model.reactions.get_by_id("EX_glyc_e").lower_bound #glycerol check
model.reactions.get_by_id("EX_glyc_e").lower_bound = -(10/24)
model.reactions.get_by_id("EX_rbt_e").lower_bound #ribitol check
#model.reactions.get_by_id("EX_rbt_e").lower_bound = -(10/24)
model.reactions.get_by_id("EX_fru_e").lower_bound #fructose check
#model.reactions.get_by_id("EX_fru_e").lower_bound = -(10/24)
model.reactions.get_by_id("EX_malt_e").lower_bound #maltose check
#model.reactions.get_by_id("EX_malt_e").lower_bound = -(10/24)
model.reactions.get_by_id("EX_inost_e").lower_bound #inositol check
model.reactions.get_by_id("EX_inost_e").lower_bound = -(10/24)
model.reactions.get_by_id("EX_erthrs_e").lower_bound #erythrose check
#model.reactions.get_by_id("EX_erthrs_e").lower_bound = -(10/24)
model.reactions.get_by_id("EX_glc__D_e").lower_bound #glucose check
model.reactions.get_by_id("EX_glc__D_e").lower_bound = -(10/24)
model.reactions.get_by_id("EX_sucr_e").lower_bound #sucrose check
#model.reactions.get_by_id("EX_sucr_e").lower_bound = -(10/24)
model.reactions.get_by_id("EX_arab__L_e").lower_bound #arabinose check
model.reactions.get_by_id("EX_arab__L_e").lower_bound = -(10/24)
model.reactions.get_by_id("EX_melib_e").lower_bound #melibiose check
#model.reactions.get_by_id("EX_melib_e").lower_bound = -(10/24)
model.reactions.get_by_id("EX_lcts_e").lower_bound #lactose check
model.reactions.get_by_id("EX_lcts_e").lower_bound = -(10/24)
model.reactions.get_by_id("EX_isomal_e").lower_bound #isomaltose check
#model.reactions.get_by_id("EX_isomal_e").lower_bound = -(10/24)
model.reactions.get_by_id("EX_gal_e").lower_bound #galactose check
model.reactions.get_by_id("EX_gal_e").lower_bound = -(10/24)
model.reactions.get_by_id("EX_xyl__D_e").lower_bound #xylose check
model.reactions.get_by_id("EX_xyl__D_e").lower_bound = -(10/24)
model.reactions.get_by_id("EX_mal__L_e").lower_bound #malate check
model.reactions.get_by_id("EX_mal__L_e").lower_bound = -(10/24)
model.reactions.get_by_id("EX_succ_e").lower_bound #succinate check
model.reactions.get_by_id("EX_succ_e").lower_bound = -(10/24)
model.reactions.get_by_id("EX_cit_e").lower_bound #citrate check
model.reactions.get_by_id("EX_cit_e").lower_bound = -(10/24)
model.reactions.get_by_id("EX_oaa_e").lower_bound #oxaloacetate check
model.reactions.get_by_id("EX_oaa_e").lower_bound = -(10/24)
model.reactions.get_by_id("EX_fum_e").lower_bound #fumarate check
model.reactions.get_by_id("EX_fum_e").lower_bound = -(10/24)
model.reactions.get_by_id("EX_bz_e").lower_bound #benzoate check
model.reactions.get_by_id("EX_bz_e").lower_bound = -(10/24)
model.reactions.get_by_id("EX_acon_C_e").lower_bound #cis-aconitate check
#model.reactions.get_by_id("EX_acon_C_e").lower_bound = -(10/24)
model.reactions.get_by_id("EX_tartr__L_e").lower_bound #tartaric acid check
#model.reactions.get_by_id("EX_tartr__L_e").lower_bound = -(10/24)
model.reactions.get_by_id("EX_lac__L_e").lower_bound #lactate check
model.reactions.get_by_id("EX_lac__L_e").lower_bound = -(10/24)
model.reactions.get_by_id("EX_malon_e").lower_bound #malonate check
#model.reactions.get_by_id("EX_malon_e").lower_bound = -(10/24)
# Adjust boundaries for amino acid and nucleoside uptake
model.reactions.get_by_id("EX_lys__L_e").lower_bound #lysine check
model.reactions.get_by_id("EX_lys__L_e").lower_bound = -(0.25/18)
model.reactions.get_by_id("EX_arg__L_e").lower_bound #arginine check
model.reactions.get_by_id("EX_arg__L_e").lower_bound = -(0.25/18)
model.reactions.get_by_id("EX_gln__L_e").lower_bound #glutamine check
model.reactions.get_by_id("EX_gln__L_e").lower_bound = -(0.25/18)
model.reactions.get_by_id("EX_ser__L_e").lower_bound #serine check
model.reactions.get_by_id("EX_ser__L_e").lower_bound = -(0.25/18)
model.reactions.get_by_id("EX_leu__L_e").lower_bound #leucine check
model.reactions.get_by_id("EX_leu__L_e").lower_bound = -(0.25/18)
model.reactions.get_by_id("EX_asn__L_e").lower_bound #asparagine check
model.reactions.get_by_id("EX_asn__L_e").lower_bound = -(0.25/18)
model.reactions.get_by_id("EX_ile__L_e").lower_bound #isoleucine check
model.reactions.get_by_id("EX_ile__L_e").lower_bound = -(0.25/18)
model.reactions.get_by_id("EX_asp__L_e").lower_bound #aspartate check
model.reactions.get_by_id("EX_asp__L_e").lower_bound = -(0.25/18)
model.reactions.get_by_id("EX_ala__L_e").lower_bound #alanine check
model.reactions.get_by_id("EX_ala__L_e").lower_bound = -(0.25/18)
model.reactions.get_by_id("EX_gly_e").lower_bound #glycine check
model.reactions.get_by_id("EX_gly_e").lower_bound = -(0.25/18)
model.reactions.get_by_id("EX_val__L_e").lower_bound #valine check
model.reactions.get_by_id("EX_val__L_e").lower_bound = -(0.25/18)
model.reactions.get_by_id("EX_glu__L_e").lower_bound #glutamate check
model.reactions.get_by_id("EX_glu__L_e").lower_bound = -(0.25/18)
model.reactions.get_by_id("EX_thr__L_e").lower_bound #threonine check
model.reactions.get_by_id("EX_thr__L_e").lower_bound = -(0.25/18)
model.reactions.get_by_id("EX_tyr__L_e").lower_bound #tyrosine check
model.reactions.get_by_id("EX_tyr__L_e").lower_bound = -(0.25/18)
model.reactions.get_by_id("EX_his__L_e").lower_bound #histidine check
model.reactions.get_by_id("EX_his__L_e").lower_bound = -(0.25/18)
model.reactions.get_by_id("EX_4abut_e").lower_bound #aminobutanoate check
#model.reactions.get_by_id("EX_4abut_e").lower_bound = -(0.25/18)
model.reactions.get_by_id("EX_cytd_e").lower_bound #cytidine check
#model.reactions.get_by_id("EX_cytd_e").lower_bound = -(0.25/18)
model.reactions.get_by_id("EX_thymd_e").lower_bound #thymidine check
#model.reactions.get_by_id("EX_thymd_e").lower_bound = -(0.25/18)
solAfter=model.optimize()
# Save model with constraints set
cobra.io.write_sbml_model(model, "hro_Exud_soft_Bnds.xml")

### P. putida (ppu) minimal medium
model = cobra.io.read_sbml_model("ppu_Syn_soft.xml")
solBefore = model.optimize() # optimization solution before
# Adjust boundaries for major carbon source uptake
model.reactions.get_by_id("EX_glc__D_e").lower_bound #glucose check
model.reactions.get_by_id("EX_glc__D_e").lower_bound = -5
model.reactions.get_by_id("EX_mal__L_e").lower_bound #malate check
model.reactions.get_by_id("EX_mal__L_e").lower_bound = -5
# Adjust boundaries for amino acid uptake
model.reactions.get_by_id("EX_arg__L_e").lower_bound #arginine check
model.reactions.get_by_id("EX_arg__L_e").lower_bound = -(0.25/9)
model.reactions.get_by_id("EX_asn__L_e").lower_bound #asparagine check
model.reactions.get_by_id("EX_asn__L_e").lower_bound = -(0.25/9)
model.reactions.get_by_id("EX_cys__L_e").lower_bound #cysteine check
#model.reactions.get_by_id("EX_cys__L_e").lower_bound = -(0.25/9)
model.reactions.get_by_id("EX_gln__L_e").lower_bound #glutamine check
model.reactions.get_by_id("EX_gln__L_e").lower_bound = -(0.25/9)
model.reactions.get_by_id("EX_ile__L_e").lower_bound #isoleucine check
model.reactions.get_by_id("EX_ile__L_e").lower_bound = -(0.25/9)
model.reactions.get_by_id("EX_leu__L_e").lower_bound #leucine check
model.reactions.get_by_id("EX_leu__L_e").lower_bound = -(0.25/9)
model.reactions.get_by_id("EX_lys__L_e").lower_bound #lysine check
model.reactions.get_by_id("EX_lys__L_e").lower_bound = -(0.25/9)
model.reactions.get_by_id("EX_pro__L_e").lower_bound #proline check
model.reactions.get_by_id("EX_pro__L_e").lower_bound = -(0.25/9)
model.reactions.get_by_id("EX_ser__L_e").lower_bound #serine check
model.reactions.get_by_id("EX_ser__L_e").lower_bound = -(0.25/9)
# Adjust boundaries for vitamin uptake
model.reactions.get_by_id("EX_btn_e").lower_bound #biotin check
#model.reactions.get_by_id("EX_btn_e").lower_bound = -0.001
model.reactions.get_by_id("EX_cbl1_e").lower_bound #cobalamin check
#model.reactions.get_by_id("EX_cbl1_e").lower_bound = -0.001
model.reactions.get_by_id("EX_nac_e").lower_bound #niacin check
model.reactions.get_by_id("EX_nac_e").lower_bound = -0.001
model.reactions.get_by_id("EX_pnto__R_e").lower_bound #pantothenate check
model.reactions.get_by_id("EX_pnto__R_e").lower_bound = -0.001
model.reactions.get_by_id("EX_pydxn_e").lower_bound #pyridoxine check
model.reactions.get_by_id("EX_pydxn_e").lower_bound = -0.001
model.reactions.get_by_id("EX_ribflv_e").lower_bound #riboflavin check
#model.reactions.get_by_id("EX_ribflv_e").lower_bound = -0.001
solAfter=model.optimize()
# Save model with constraints set
cobra.io.write_sbml_model(model, "ppu_Syn_soft_Bnds.xml")

### P. putida (ppU) root exudate medium
model = cobra.io.read_sbml_model("ppu_Exud_soft.xml")
solBefore = model.optimize() # optimization solution before
# Adjust boundaries for major carbon source uptake
model.reactions.get_by_id("EX_glyc_e").lower_bound #glycerol check
model.reactions.get_by_id("EX_glyc_e").lower_bound = -(10/24)
model.reactions.get_by_id("EX_rbt_e").lower_bound #ribitol check
#model.reactions.get_by_id("EX_rbt_e").lower_bound = -(10/24)
model.reactions.get_by_id("EX_fru_e").lower_bound #fructose check
model.reactions.get_by_id("EX_fru_e").lower_bound = -(10/24)
model.reactions.get_by_id("EX_malt_e").lower_bound #maltose check
model.reactions.get_by_id("EX_malt_e").lower_bound = -(10/24)
model.reactions.get_by_id("EX_inost_e").lower_bound #inositol check
model.reactions.get_by_id("EX_inost_e").lower_bound = -(10/24)
model.reactions.get_by_id("EX_erthrs_e").lower_bound #erythrose check
#model.reactions.get_by_id("EX_erthrs_e").lower_bound = -(10/24)
model.reactions.get_by_id("EX_glc__D_e").lower_bound #glucose check
model.reactions.get_by_id("EX_glc__D_e").lower_bound = -(10/24)
model.reactions.get_by_id("EX_sucr_e").lower_bound #sucrose check
model.reactions.get_by_id("EX_sucr_e").lower_bound = -(10/24)
model.reactions.get_by_id("EX_arab__L_e").lower_bound #arabinose check
model.reactions.get_by_id("EX_arab__L_e").lower_bound = -(10/24)
model.reactions.get_by_id("EX_melib_e").lower_bound #melibiose check
#model.reactions.get_by_id("EX_melib_e").lower_bound = -(10/24)
model.reactions.get_by_id("EX_lcts_e").lower_bound #lactose check
#model.reactions.get_by_id("EX_lcts_e").lower_bound = -(10/24)
model.reactions.get_by_id("EX_isomal_e").lower_bound #isomaltose check
#model.reactions.get_by_id("EX_isomal_e").lower_bound = -(10/24)
model.reactions.get_by_id("EX_gal_e").lower_bound #galactose check
model.reactions.get_by_id("EX_gal_e").lower_bound = -(10/24)
model.reactions.get_by_id("EX_xyl__D_e").lower_bound #xylose check
model.reactions.get_by_id("EX_xyl__D_e").lower_bound = -(10/24)
model.reactions.get_by_id("EX_mal__L_e").lower_bound #malate check
model.reactions.get_by_id("EX_mal__L_e").lower_bound = -(10/24)
model.reactions.get_by_id("EX_succ_e").lower_bound #succinate check
model.reactions.get_by_id("EX_succ_e").lower_bound = -(10/24)
model.reactions.get_by_id("EX_cit_e").lower_bound #citrate check
model.reactions.get_by_id("EX_cit_e").lower_bound = -(10/24)
model.reactions.get_by_id("EX_oaa_e").lower_bound #oxaloacetate check
model.reactions.get_by_id("EX_oaa_e").lower_bound = -(10/24)
model.reactions.get_by_id("EX_fum_e").lower_bound #fumarate check
model.reactions.get_by_id("EX_fum_e").lower_bound = -(10/24)
model.reactions.get_by_id("EX_bz_e").lower_bound #benzoate check
model.reactions.get_by_id("EX_bz_e").lower_bound = -(10/24)
model.reactions.get_by_id("EX_acon_C_e").lower_bound #cis-aconitate check
#model.reactions.get_by_id("EX_acon_C_e").lower_bound = -(10/24)
model.reactions.get_by_id("EX_tartr__L_e").lower_bound #tartaric acid check
#model.reactions.get_by_id("EX_tartr__L_e").lower_bound = -(10/24)
model.reactions.get_by_id("EX_lac__L_e").lower_bound #lactate check
model.reactions.get_by_id("EX_lac__L_e").lower_bound = -(10/24)
model.reactions.get_by_id("EX_malon_e").lower_bound #malonate check
#model.reactions.get_by_id("EX_malon_e").lower_bound = -(10/24)
# Adjust boundaries for amino acid and nucleoside uptake
model.reactions.get_by_id("EX_lys__L_e").lower_bound #lysine check
model.reactions.get_by_id("EX_lys__L_e").lower_bound = -(0.25/18)
model.reactions.get_by_id("EX_arg__L_e").lower_bound #arginine check
model.reactions.get_by_id("EX_arg__L_e").lower_bound = -(0.25/18)
model.reactions.get_by_id("EX_gln__L_e").lower_bound #glutamine check
model.reactions.get_by_id("EX_gln__L_e").lower_bound = -(0.25/18)
model.reactions.get_by_id("EX_ser__L_e").lower_bound #serine check
model.reactions.get_by_id("EX_ser__L_e").lower_bound = -(0.25/18)
model.reactions.get_by_id("EX_leu__L_e").lower_bound #leucine check
model.reactions.get_by_id("EX_leu__L_e").lower_bound = -(0.25/18)
model.reactions.get_by_id("EX_asn__L_e").lower_bound #asparagine check
model.reactions.get_by_id("EX_asn__L_e").lower_bound = -(0.25/18)
model.reactions.get_by_id("EX_ile__L_e").lower_bound #isoleucine check
model.reactions.get_by_id("EX_ile__L_e").lower_bound = -(0.25/18)
model.reactions.get_by_id("EX_asp__L_e").lower_bound #aspartate check
model.reactions.get_by_id("EX_asp__L_e").lower_bound = -(0.25/18)
model.reactions.get_by_id("EX_ala__L_e").lower_bound #alanine check
model.reactions.get_by_id("EX_ala__L_e").lower_bound = -(0.25/18)
model.reactions.get_by_id("EX_gly_e").lower_bound #glycine check
model.reactions.get_by_id("EX_gly_e").lower_bound = -(0.25/18)
model.reactions.get_by_id("EX_val__L_e").lower_bound #valine check
model.reactions.get_by_id("EX_val__L_e").lower_bound = -(0.25/18)
model.reactions.get_by_id("EX_glu__L_e").lower_bound #glutamate check
model.reactions.get_by_id("EX_glu__L_e").lower_bound = -(0.25/18)
model.reactions.get_by_id("EX_thr__L_e").lower_bound #threonine check
model.reactions.get_by_id("EX_thr__L_e").lower_bound = -(0.25/18)
model.reactions.get_by_id("EX_tyr__L_e").lower_bound #tyrosine check
model.reactions.get_by_id("EX_tyr__L_e").lower_bound = -(0.25/18)
model.reactions.get_by_id("EX_his__L_e").lower_bound #histidine check
model.reactions.get_by_id("EX_his__L_e").lower_bound = -(0.25/18)
model.reactions.get_by_id("EX_4abut_e").lower_bound #aminobutanoate check
#model.reactions.get_by_id("EX_4abut_e").lower_bound = -(0.25/18)
model.reactions.get_by_id("EX_cytd_e").lower_bound #cytidine check
#model.reactions.get_by_id("EX_cytd_e").lower_bound = -(0.25/18)
model.reactions.get_by_id("EX_thymd_e").lower_bound #thymidine check
#model.reactions.get_by_id("EX_thymd_e").lower_bound = -(0.25/18)
solAfter=model.optimize()
# Save model with constraints set
cobra.io.write_sbml_model(model, "ppu_Exud_soft_Bnds.xml")

### S. maltophilia (sma) minimal medium
model = cobra.io.read_sbml_model("sma_Syn_soft.xml")
solBefore = model.optimize() # optimization solution before
# Adjust boundaries for major carbon source uptake
model.reactions.get_by_id("EX_glc__D_e").lower_bound #glucose check
model.reactions.get_by_id("EX_glc__D_e").lower_bound = -5
model.reactions.get_by_id("EX_mal__L_e").lower_bound #malate check
model.reactions.get_by_id("EX_mal__L_e").lower_bound = -5
# Adjust boundaries for amino acid uptake
model.reactions.get_by_id("EX_arg__L_e").lower_bound #arginine check
model.reactions.get_by_id("EX_arg__L_e").lower_bound = -(0.25/9)
model.reactions.get_by_id("EX_asn__L_e").lower_bound #asparagine check
model.reactions.get_by_id("EX_asn__L_e").lower_bound = -(0.25/9)
model.reactions.get_by_id("EX_cys__L_e").lower_bound #cysteine check
#model.reactions.get_by_id("EX_cys__L_e").lower_bound = -(0.25/9)
model.reactions.get_by_id("EX_gln__L_e").lower_bound #glutamine check
model.reactions.get_by_id("EX_gln__L_e").lower_bound = -(0.25/9)
model.reactions.get_by_id("EX_ile__L_e").lower_bound #isoleucine check
model.reactions.get_by_id("EX_ile__L_e").lower_bound = -(0.25/9)
model.reactions.get_by_id("EX_leu__L_e").lower_bound #leucine check
model.reactions.get_by_id("EX_leu__L_e").lower_bound = -(0.25/9)
model.reactions.get_by_id("EX_lys__L_e").lower_bound #lysine check
model.reactions.get_by_id("EX_lys__L_e").lower_bound = -(0.25/9)
model.reactions.get_by_id("EX_pro__L_e").lower_bound #proline check
model.reactions.get_by_id("EX_pro__L_e").lower_bound = -(0.25/9)
model.reactions.get_by_id("EX_ser__L_e").lower_bound #serine check
model.reactions.get_by_id("EX_ser__L_e").lower_bound = -(0.25/9)
# Adjust boundaries for vitamin uptake
model.reactions.get_by_id("EX_btn_e").lower_bound #biotin check
#model.reactions.get_by_id("EX_btn_e").lower_bound = -0.001
model.reactions.get_by_id("EX_cbl1_e").lower_bound #cobalamin check
#model.reactions.get_by_id("EX_cbl1_e").lower_bound = -0.001
model.reactions.get_by_id("EX_nac_e").lower_bound #niacin check
#model.reactions.get_by_id("EX_nac_e").lower_bound = -0.001
model.reactions.get_by_id("EX_pnto__R_e").lower_bound #pantothenate check
#model.reactions.get_by_id("EX_pnto__R_e").lower_bound = -0.001
model.reactions.get_by_id("EX_pydxn_e").lower_bound #pyridoxine check
model.reactions.get_by_id("EX_pydxn_e").lower_bound = -0.001
model.reactions.get_by_id("EX_ribflv_e").lower_bound #riboflavin check
#model.reactions.get_by_id("EX_ribflv_e").lower_bound = -0.001
solAfter=model.optimize()
# Save model with constraints set
cobra.io.write_sbml_model(model, "sma_Syn_soft_Bnds.xml")

### S. maltophilia (sma), root exudate medium
model = cobra.io.read_sbml_model("sma_Exud_soft.xml")
solBefore = model.optimize() # optimization solution before
# Adjust boundaries for major carbon source uptake
model.reactions.get_by_id("EX_glyc_e").lower_bound #glycerol check
model.reactions.get_by_id("EX_glyc_e").lower_bound = -(10/24)
model.reactions.get_by_id("EX_rbt_e").lower_bound #ribitol check
#model.reactions.get_by_id("EX_rbt_e").lower_bound = -(10/24)
model.reactions.get_by_id("EX_fru_e").lower_bound #fructose check
model.reactions.get_by_id("EX_fru_e").lower_bound = -(10/24)
model.reactions.get_by_id("EX_malt_e").lower_bound #maltose check
model.reactions.get_by_id("EX_malt_e").lower_bound = -(10/24)
model.reactions.get_by_id("EX_inost_e").lower_bound #inositol check
#model.reactions.get_by_id("EX_inost_e").lower_bound = -(10/24)
model.reactions.get_by_id("EX_erthrs_e").lower_bound #erythrose check
#model.reactions.get_by_id("EX_erthrs_e").lower_bound = -(10/24)
model.reactions.get_by_id("EX_glc__D_e").lower_bound #glucose check
model.reactions.get_by_id("EX_glc__D_e").lower_bound = -(10/24)
model.reactions.get_by_id("EX_sucr_e").lower_bound #sucrose check
model.reactions.get_by_id("EX_sucr_e").lower_bound = -(10/24)
model.reactions.get_by_id("EX_arab__L_e").lower_bound #arabinose check
model.reactions.get_by_id("EX_arab__L_e").lower_bound = -(10/24)
model.reactions.get_by_id("EX_melib_e").lower_bound #melibiose check
model.reactions.get_by_id("EX_melib_e").lower_bound = -(10/24)
model.reactions.get_by_id("EX_lcts_e").lower_bound #lactose check
model.reactions.get_by_id("EX_lcts_e").lower_bound = -(10/24)
model.reactions.get_by_id("EX_isomal_e").lower_bound #isomaltose check
#model.reactions.get_by_id("EX_isomal_e").lower_bound = -(10/24)
model.reactions.get_by_id("EX_gal_e").lower_bound #galactose check
model.reactions.get_by_id("EX_gal_e").lower_bound = -(10/24)
model.reactions.get_by_id("EX_xyl__D_e").lower_bound #xylose check
#model.reactions.get_by_id("EX_xyl__D_e").lower_bound = -(10/24)
model.reactions.get_by_id("EX_mal__L_e").lower_bound #malate check
model.reactions.get_by_id("EX_mal__L_e").lower_bound = -(10/24)
model.reactions.get_by_id("EX_succ_e").lower_bound #succinate check
model.reactions.get_by_id("EX_succ_e").lower_bound = -(10/24)
model.reactions.get_by_id("EX_cit_e").lower_bound #citrate check
model.reactions.get_by_id("EX_cit_e").lower_bound = -(10/24)
model.reactions.get_by_id("EX_oaa_e").lower_bound #oxaloacetate check
#model.reactions.get_by_id("EX_oaa_e").lower_bound = -(10/24)
model.reactions.get_by_id("EX_fum_e").lower_bound #fumarate check
model.reactions.get_by_id("EX_fum_e").lower_bound = -(10/24)
model.reactions.get_by_id("EX_bz_e").lower_bound #benzoate check
model.reactions.get_by_id("EX_bz_e").lower_bound = -(10/24)
model.reactions.get_by_id("EX_acon_C_e").lower_bound #cis-aconitate check
#model.reactions.get_by_id("EX_acon_C_e").lower_bound = -(10/24)
model.reactions.get_by_id("EX_tartr__L_e").lower_bound #tartaric acid check
#model.reactions.get_by_id("EX_tartr__L_e").lower_bound = -(10/24)
model.reactions.get_by_id("EX_lac__L_e").lower_bound #lactate check
model.reactions.get_by_id("EX_lac__L_e").lower_bound = -(10/24)
model.reactions.get_by_id("EX_malon_e").lower_bound #malonate check
#model.reactions.get_by_id("EX_malon_e").lower_bound = -(10/24)
# Adjust boundaries for amino acid and nucleoside uptake
model.reactions.get_by_id("EX_lys__L_e").lower_bound #lysine check
model.reactions.get_by_id("EX_lys__L_e").lower_bound = -(0.25/18)
model.reactions.get_by_id("EX_arg__L_e").lower_bound #arginine check
model.reactions.get_by_id("EX_arg__L_e").lower_bound = -(0.25/18)
model.reactions.get_by_id("EX_gln__L_e").lower_bound #glutamine check
model.reactions.get_by_id("EX_gln__L_e").lower_bound = -(0.25/18)
model.reactions.get_by_id("EX_ser__L_e").lower_bound #serine check
model.reactions.get_by_id("EX_ser__L_e").lower_bound = -(0.25/18)
model.reactions.get_by_id("EX_leu__L_e").lower_bound #leucine check
model.reactions.get_by_id("EX_leu__L_e").lower_bound = -(0.25/18)
model.reactions.get_by_id("EX_asn__L_e").lower_bound #asparagine check
model.reactions.get_by_id("EX_asn__L_e").lower_bound = -(0.25/18)
model.reactions.get_by_id("EX_ile__L_e").lower_bound #isoleucine check
model.reactions.get_by_id("EX_ile__L_e").lower_bound = -(0.25/18)
model.reactions.get_by_id("EX_asp__L_e").lower_bound #aspartate check
model.reactions.get_by_id("EX_asp__L_e").lower_bound = -(0.25/18)
model.reactions.get_by_id("EX_ala__L_e").lower_bound #alanine check
model.reactions.get_by_id("EX_ala__L_e").lower_bound = -(0.25/18)
model.reactions.get_by_id("EX_gly_e").lower_bound #glycine check
model.reactions.get_by_id("EX_gly_e").lower_bound = -(0.25/18)
model.reactions.get_by_id("EX_val__L_e").lower_bound #valine check
model.reactions.get_by_id("EX_val__L_e").lower_bound = -(0.25/18)
model.reactions.get_by_id("EX_glu__L_e").lower_bound #glutamate check
model.reactions.get_by_id("EX_glu__L_e").lower_bound = -(0.25/18)
model.reactions.get_by_id("EX_thr__L_e").lower_bound #threonine check
model.reactions.get_by_id("EX_thr__L_e").lower_bound = -(0.25/18)
model.reactions.get_by_id("EX_tyr__L_e").lower_bound #tyrosine check
model.reactions.get_by_id("EX_tyr__L_e").lower_bound = -(0.25/18)
model.reactions.get_by_id("EX_his__L_e").lower_bound #histidine check
#model.reactions.get_by_id("EX_his__L_e").lower_bound = -(0.25/18)
model.reactions.get_by_id("EX_4abut_e").lower_bound #aminobutanoate check
model.reactions.get_by_id("EX_4abut_e").lower_bound = -(0.25/18)
model.reactions.get_by_id("EX_cytd_e").lower_bound #cytidine check
model.reactions.get_by_id("EX_cytd_e").lower_bound = -(0.25/18)
model.reactions.get_by_id("EX_thymd_e").lower_bound #thymidine check
model.reactions.get_by_id("EX_thymd_e").lower_bound = -(0.25/18)
solAfter=model.optimize()
# Save model with constraints set
cobra.io.write_sbml_model(model, "sma_Exud_soft_Bnds.xml")

### For B. pituitosa (opi) minimal medium
model = cobra.io.read_sbml_model("opi_Syn_soft.xml")
solBefore = model.optimize() # optimization solution before
# Adjust boundaries for major carbon source uptake
model.reactions.get_by_id("EX_glc__D_e").lower_bound #glucose check
model.reactions.get_by_id("EX_glc__D_e").lower_bound = -5
model.reactions.get_by_id("EX_mal__L_e").lower_bound #malate check
model.reactions.get_by_id("EX_mal__L_e").lower_bound = -5
# Adjust boundaries for amino acid uptake
model.reactions.get_by_id("EX_arg__L_e").lower_bound #arginine check
model.reactions.get_by_id("EX_arg__L_e").lower_bound = -(0.25/9)
model.reactions.get_by_id("EX_asn__L_e").lower_bound #asparagine check
model.reactions.get_by_id("EX_asn__L_e").lower_bound = -(0.25/9)
model.reactions.get_by_id("EX_cys__L_e").lower_bound #cysteine check
#model.reactions.get_by_id("EX_cys__L_e").lower_bound = -(0.25/9)
model.reactions.get_by_id("EX_gln__L_e").lower_bound #glutamine check
model.reactions.get_by_id("EX_gln__L_e").lower_bound = -(0.25/9)
model.reactions.get_by_id("EX_ile__L_e").lower_bound #isoleucine check
model.reactions.get_by_id("EX_ile__L_e").lower_bound = -(0.25/9)
model.reactions.get_by_id("EX_leu__L_e").lower_bound #leucine check
model.reactions.get_by_id("EX_leu__L_e").lower_bound = -(0.25/9)
model.reactions.get_by_id("EX_lys__L_e").lower_bound #lysine check
model.reactions.get_by_id("EX_lys__L_e").lower_bound = -(0.25/9)
model.reactions.get_by_id("EX_pro__L_e").lower_bound #proline check
model.reactions.get_by_id("EX_pro__L_e").lower_bound = -(0.25/9)
model.reactions.get_by_id("EX_ser__L_e").lower_bound #serine check
model.reactions.get_by_id("EX_ser__L_e").lower_bound = -(0.25/9)
# Adjust boundaries for vitamin uptake
model.reactions.get_by_id("EX_btn_e").lower_bound #biotin check
model.reactions.get_by_id("EX_btn_e").lower_bound = -0.001
model.reactions.get_by_id("EX_cbl1_e").lower_bound #cobalamin check
#model.reactions.get_by_id("EX_cbl1_e").lower_bound = -0.001
model.reactions.get_by_id("EX_nac_e").lower_bound #niacin check
#model.reactions.get_by_id("EX_nac_e").lower_bound = -0.001
model.reactions.get_by_id("EX_pnto__R_e").lower_bound #pantothenate check
#model.reactions.get_by_id("EX_pnto__R_e").lower_bound = -0.001
model.reactions.get_by_id("EX_pydxn_e").lower_bound #pyridoxine check
#model.reactions.get_by_id("EX_pydxn_e").lower_bound = -0.001
model.reactions.get_by_id("EX_ribflv_e").lower_bound #riboflavin check
model.reactions.get_by_id("EX_ribflv_e").lower_bound = -0.001
solAfter=model.optimize()
# Save model with constraints set
cobra.io.write_sbml_model(model, "opi_Syn_soft_Bnds.xml")

### B. pituitosa (opi), root exudate medium
model = cobra.io.read_sbml_model("opi_Exud_soft.xml")
solBefore = model.optimize() # optimization solution before
# Adjust boundaries for major carbon source uptake
model.reactions.get_by_id("EX_glyc_e").lower_bound #glycerol check
model.reactions.get_by_id("EX_glyc_e").lower_bound = -(10/24)
model.reactions.get_by_id("EX_rbt_e").lower_bound #ribitol check
#model.reactions.get_by_id("EX_rbt_e").lower_bound = -(10/24)
model.reactions.get_by_id("EX_fru_e").lower_bound #fructose check
model.reactions.get_by_id("EX_fru_e").lower_bound = -(10/24)
model.reactions.get_by_id("EX_malt_e").lower_bound #maltose check
model.reactions.get_by_id("EX_malt_e").lower_bound = -(10/24)
model.reactions.get_by_id("EX_inost_e").lower_bound #inositol check
model.reactions.get_by_id("EX_inost_e").lower_bound = -(10/24)
model.reactions.get_by_id("EX_erthrs_e").lower_bound #erythrose check
#model.reactions.get_by_id("EX_erthrs_e").lower_bound = -(10/24)
model.reactions.get_by_id("EX_glc__D_e").lower_bound #glucose check
model.reactions.get_by_id("EX_glc__D_e").lower_bound = -(10/24)
model.reactions.get_by_id("EX_sucr_e").lower_bound #sucrose check
#model.reactions.get_by_id("EX_sucr_e").lower_bound = -(10/24)
model.reactions.get_by_id("EX_arab__L_e").lower_bound #arabinose check
model.reactions.get_by_id("EX_arab__L_e").lower_bound = -(10/24)
model.reactions.get_by_id("EX_melib_e").lower_bound #melibiose check
model.reactions.get_by_id("EX_melib_e").lower_bound = -(10/24)
model.reactions.get_by_id("EX_lcts_e").lower_bound #lactose check
model.reactions.get_by_id("EX_lcts_e").lower_bound = -(10/24)
model.reactions.get_by_id("EX_isomal_e").lower_bound #isomaltose check
#model.reactions.get_by_id("EX_isomal_e").lower_bound = -(10/24)
model.reactions.get_by_id("EX_gal_e").lower_bound #galactose check
model.reactions.get_by_id("EX_gal_e").lower_bound = -(10/24)
model.reactions.get_by_id("EX_xyl__D_e").lower_bound #xylose check
model.reactions.get_by_id("EX_xyl__D_e").lower_bound = -(10/24)
model.reactions.get_by_id("EX_mal__L_e").lower_bound #malate check
model.reactions.get_by_id("EX_mal__L_e").lower_bound = -(10/24)
model.reactions.get_by_id("EX_succ_e").lower_bound #succinate check
model.reactions.get_by_id("EX_succ_e").lower_bound = -(10/24)
model.reactions.get_by_id("EX_cit_e").lower_bound #citrate check
model.reactions.get_by_id("EX_cit_e").lower_bound = -(10/24)
model.reactions.get_by_id("EX_oaa_e").lower_bound #oxaloacetate check
model.reactions.get_by_id("EX_oaa_e").lower_bound = -(10/24)
model.reactions.get_by_id("EX_fum_e").lower_bound #fumarate check
model.reactions.get_by_id("EX_fum_e").lower_bound = -(10/24)
model.reactions.get_by_id("EX_bz_e").lower_bound #benzoate check
model.reactions.get_by_id("EX_bz_e").lower_bound = -(10/24)
model.reactions.get_by_id("EX_acon_C_e").lower_bound #cis-aconitate check
#model.reactions.get_by_id("EX_acon_C_e").lower_bound = -(10/24)
model.reactions.get_by_id("EX_tartr__L_e").lower_bound #tartaric acid check
#model.reactions.get_by_id("EX_tartr__L_e").lower_bound = -(10/24)
model.reactions.get_by_id("EX_lac__L_e").lower_bound #lactate check
#model.reactions.get_by_id("EX_lac__L_e").lower_bound = -(10/24)
model.reactions.get_by_id("EX_malon_e").lower_bound #malonate check
#model.reactions.get_by_id("EX_malon_e").lower_bound = -(10/24)
# Adjust boundaries for amino acid and nucleoside uptake
model.reactions.get_by_id("EX_lys__L_e").lower_bound #lysine check
model.reactions.get_by_id("EX_lys__L_e").lower_bound = -(0.25/18)
model.reactions.get_by_id("EX_arg__L_e").lower_bound #arginine check
model.reactions.get_by_id("EX_arg__L_e").lower_bound = -(0.25/18)
model.reactions.get_by_id("EX_gln__L_e").lower_bound #glutamine check
model.reactions.get_by_id("EX_gln__L_e").lower_bound = -(0.25/18)
model.reactions.get_by_id("EX_ser__L_e").lower_bound #serine check
model.reactions.get_by_id("EX_ser__L_e").lower_bound = -(0.25/18)
model.reactions.get_by_id("EX_leu__L_e").lower_bound #leucine check
model.reactions.get_by_id("EX_leu__L_e").lower_bound = -(0.25/18)
model.reactions.get_by_id("EX_asn__L_e").lower_bound #asparagine check
model.reactions.get_by_id("EX_asn__L_e").lower_bound = -(0.25/18)
model.reactions.get_by_id("EX_ile__L_e").lower_bound #isoleucine check
model.reactions.get_by_id("EX_ile__L_e").lower_bound = -(0.25/18)
model.reactions.get_by_id("EX_asp__L_e").lower_bound #aspartate check
model.reactions.get_by_id("EX_asp__L_e").lower_bound = -(0.25/18)
model.reactions.get_by_id("EX_ala__L_e").lower_bound #alanine check
model.reactions.get_by_id("EX_ala__L_e").lower_bound = -(0.25/18)
model.reactions.get_by_id("EX_gly_e").lower_bound #glycine check
model.reactions.get_by_id("EX_gly_e").lower_bound = -(0.25/18)
model.reactions.get_by_id("EX_val__L_e").lower_bound #valine check
model.reactions.get_by_id("EX_val__L_e").lower_bound = -(0.25/18)
model.reactions.get_by_id("EX_glu__L_e").lower_bound #glutamate check
model.reactions.get_by_id("EX_glu__L_e").lower_bound = -(0.25/18)
model.reactions.get_by_id("EX_thr__L_e").lower_bound #threonine check
model.reactions.get_by_id("EX_thr__L_e").lower_bound = -(0.25/18)
model.reactions.get_by_id("EX_tyr__L_e").lower_bound #tyrosine check
model.reactions.get_by_id("EX_tyr__L_e").lower_bound = -(0.25/18)
model.reactions.get_by_id("EX_his__L_e").lower_bound #histidine check
model.reactions.get_by_id("EX_his__L_e").lower_bound = -(0.25/18)
model.reactions.get_by_id("EX_4abut_e").lower_bound #aminobutanoate check
#model.reactions.get_by_id("EX_4abut_e").lower_bound = -(0.25/18)
model.reactions.get_by_id("EX_cytd_e").lower_bound #cytidine check
#model.reactions.get_by_id("EX_cytd_e").lower_bound = -(0.25/18)
model.reactions.get_by_id("EX_thymd_e").lower_bound #thymidine check
#model.reactions.get_by_id("EX_thymd_e").lower_bound = -(0.25/18)
solAfter=model.optimize()
# Save model with constraints set
cobra.io.write_sbml_model(model, "opi_Exud_soft_Bnds.xml")

### C. indologenes (cin), minimal medium
model = cobra.io.read_sbml_model("cin_Syn_soft.xml")
solBefore = model.optimize() # optimization solution before
# Adjust boundaries for major carbon source uptake
model.reactions.get_by_id("EX_glc__D_e").lower_bound #glucose check
model.reactions.get_by_id("EX_glc__D_e").lower_bound = -5
model.reactions.get_by_id("EX_mal__L_e").lower_bound #malate check
model.reactions.get_by_id("EX_mal__L_e").lower_bound = -5
# Adjust boundaries for amino acid uptake
model.reactions.get_by_id("EX_arg__L_e").lower_bound #arginine check
model.reactions.get_by_id("EX_arg__L_e").lower_bound = -(0.25/9)
model.reactions.get_by_id("EX_asn__L_e").lower_bound #asparagine check
model.reactions.get_by_id("EX_asn__L_e").lower_bound = -(0.25/9)
model.reactions.get_by_id("EX_cys__L_e").lower_bound #cysteine check
#model.reactions.get_by_id("EX_cys__L_e").lower_bound = -(0.25/9)
model.reactions.get_by_id("EX_gln__L_e").lower_bound #glutamine check
model.reactions.get_by_id("EX_gln__L_e").lower_bound = -(0.25/9)
model.reactions.get_by_id("EX_ile__L_e").lower_bound #isoleucine check
model.reactions.get_by_id("EX_ile__L_e").lower_bound = -(0.25/9)
model.reactions.get_by_id("EX_leu__L_e").lower_bound #leucine check
model.reactions.get_by_id("EX_leu__L_e").lower_bound = -(0.25/9)
model.reactions.get_by_id("EX_lys__L_e").lower_bound #lysine check
model.reactions.get_by_id("EX_lys__L_e").lower_bound = -(0.25/9)
model.reactions.get_by_id("EX_pro__L_e").lower_bound #proline check
model.reactions.get_by_id("EX_pro__L_e").lower_bound = -(0.25/9)
model.reactions.get_by_id("EX_ser__L_e").lower_bound #serine check
model.reactions.get_by_id("EX_ser__L_e").lower_bound = -(0.25/9)
# Adjust boundaries for vitamin uptake
model.reactions.get_by_id("EX_btn_e").lower_bound #biotin check
#model.reactions.get_by_id("EX_btn_e").lower_bound = -0.001
model.reactions.get_by_id("EX_cbl1_e").lower_bound #cobalamin check
#model.reactions.get_by_id("EX_cbl1_e").lower_bound = -0.001
model.reactions.get_by_id("EX_nac_e").lower_bound #niacin check
#model.reactions.get_by_id("EX_nac_e").lower_bound = -0.001
model.reactions.get_by_id("EX_pnto__R_e").lower_bound #pantothenate check
#model.reactions.get_by_id("EX_pnto__R_e").lower_bound = -0.001
model.reactions.get_by_id("EX_pydxn_e").lower_bound #pyridoxine check
#model.reactions.get_by_id("EX_pydxn_e").lower_bound = -0.001
model.reactions.get_by_id("EX_ribflv_e").lower_bound #riboflavin check
#model.reactions.get_by_id("EX_ribflv_e").lower_bound = -0.001
solAfter=model.optimize()
# Save model with constraints set
cobra.io.write_sbml_model(model, "cin_Syn_soft_Bnds.xml")

### C. indologenes (cin), root exudate medium
model = cobra.io.read_sbml_model("cin_Exud_soft.xml")
solBefore = model.optimize() # optimization solution before
# Adjust boundaries for major carbon source uptake
model.reactions.get_by_id("EX_glyc_e").lower_bound #glycerol check
model.reactions.get_by_id("EX_glyc_e").lower_bound = -(10/24)
model.reactions.get_by_id("EX_rbt_e").lower_bound #ribitol check
#model.reactions.get_by_id("EX_rbt_e").lower_bound = -(10/24)
model.reactions.get_by_id("EX_fru_e").lower_bound #fructose check
#model.reactions.get_by_id("EX_fru_e").lower_bound = -(10/24)
model.reactions.get_by_id("EX_malt_e").lower_bound #maltose check
#model.reactions.get_by_id("EX_malt_e").lower_bound = -(10/24)
model.reactions.get_by_id("EX_inost_e").lower_bound #inositol check
model.reactions.get_by_id("EX_inost_e").lower_bound = -(10/24)
model.reactions.get_by_id("EX_erthrs_e").lower_bound #erythrose check
#model.reactions.get_by_id("EX_erthrs_e").lower_bound = -(10/24)
model.reactions.get_by_id("EX_glc__D_e").lower_bound #glucose check
model.reactions.get_by_id("EX_glc__D_e").lower_bound = -(10/24)
model.reactions.get_by_id("EX_sucr_e").lower_bound #sucrose check
#model.reactions.get_by_id("EX_sucr_e").lower_bound = -(10/24)
model.reactions.get_by_id("EX_arab__L_e").lower_bound #arabinose check
#model.reactions.get_by_id("EX_arab__L_e").lower_bound = -(10/24)
model.reactions.get_by_id("EX_melib_e").lower_bound #melibiose check
#model.reactions.get_by_id("EX_melib_e").lower_bound = -(10/24)
model.reactions.get_by_id("EX_lcts_e").lower_bound #lactose check
model.reactions.get_by_id("EX_lcts_e").lower_bound = -(10/24)
model.reactions.get_by_id("EX_isomal_e").lower_bound #isomaltose check
#model.reactions.get_by_id("EX_isomal_e").lower_bound = -(10/24)
model.reactions.get_by_id("EX_gal_e").lower_bound #galactose check
model.reactions.get_by_id("EX_gal_e").lower_bound = -(10/24)
model.reactions.get_by_id("EX_xyl__D_e").lower_bound #xylose check
model.reactions.get_by_id("EX_xyl__D_e").lower_bound = -(10/24)
model.reactions.get_by_id("EX_mal__L_e").lower_bound #malate check
model.reactions.get_by_id("EX_mal__L_e").lower_bound = -(10/24)
model.reactions.get_by_id("EX_succ_e").lower_bound #succinate check
model.reactions.get_by_id("EX_succ_e").lower_bound = -(10/24)
model.reactions.get_by_id("EX_cit_e").lower_bound #citrate check
model.reactions.get_by_id("EX_cit_e").lower_bound = -(10/24)
model.reactions.get_by_id("EX_oaa_e").lower_bound #oxaloacetate check
#model.reactions.get_by_id("EX_oaa_e").lower_bound = -(10/24)
model.reactions.get_by_id("EX_fum_e").lower_bound #fumarate check
model.reactions.get_by_id("EX_fum_e").lower_bound = -(10/24)
model.reactions.get_by_id("EX_bz_e").lower_bound #benzoate check
model.reactions.get_by_id("EX_bz_e").lower_bound = -(10/24)
model.reactions.get_by_id("EX_acon_C_e").lower_bound #cis-aconitate check
#model.reactions.get_by_id("EX_acon_C_e").lower_bound = -(10/24)
model.reactions.get_by_id("EX_tartr__L_e").lower_bound #tartaric acid check
#model.reactions.get_by_id("EX_tartr__L_e").lower_bound = -(10/24)
model.reactions.get_by_id("EX_lac__L_e").lower_bound #lactate check
#model.reactions.get_by_id("EX_lac__L_e").lower_bound = -(10/24)
model.reactions.get_by_id("EX_malon_e").lower_bound #malonate check
#model.reactions.get_by_id("EX_malon_e").lower_bound = -(10/24)
# Adjust boundaries for amino acid and nucleoside uptake
model.reactions.get_by_id("EX_lys__L_e").lower_bound #lysine check
model.reactions.get_by_id("EX_lys__L_e").lower_bound = -(0.25/18)
model.reactions.get_by_id("EX_arg__L_e").lower_bound #arginine check
model.reactions.get_by_id("EX_arg__L_e").lower_bound = -(0.25/18)
model.reactions.get_by_id("EX_gln__L_e").lower_bound #glutamine check
model.reactions.get_by_id("EX_gln__L_e").lower_bound = -(0.25/18)
model.reactions.get_by_id("EX_ser__L_e").lower_bound #serine check
model.reactions.get_by_id("EX_ser__L_e").lower_bound = -(0.25/18)
model.reactions.get_by_id("EX_leu__L_e").lower_bound #leucine check
model.reactions.get_by_id("EX_leu__L_e").lower_bound = -(0.25/18)
model.reactions.get_by_id("EX_asn__L_e").lower_bound #asparagine check
model.reactions.get_by_id("EX_asn__L_e").lower_bound = -(0.25/18)
model.reactions.get_by_id("EX_ile__L_e").lower_bound #isoleucine check
model.reactions.get_by_id("EX_ile__L_e").lower_bound = -(0.25/18)
model.reactions.get_by_id("EX_asp__L_e").lower_bound #aspartate check
model.reactions.get_by_id("EX_asp__L_e").lower_bound = -(0.25/18)
model.reactions.get_by_id("EX_ala__L_e").lower_bound #alanine check
#model.reactions.get_by_id("EX_ala__L_e").lower_bound = -(0.25/18)
model.reactions.get_by_id("EX_gly_e").lower_bound #glycine check
model.reactions.get_by_id("EX_gly_e").lower_bound = -(0.25/18)
model.reactions.get_by_id("EX_val__L_e").lower_bound #valine check
model.reactions.get_by_id("EX_val__L_e").lower_bound = -(0.25/18)
model.reactions.get_by_id("EX_glu__L_e").lower_bound #glutamate check
model.reactions.get_by_id("EX_glu__L_e").lower_bound = -(0.25/18)
model.reactions.get_by_id("EX_thr__L_e").lower_bound #threonine check
model.reactions.get_by_id("EX_thr__L_e").lower_bound = -(0.25/18)
model.reactions.get_by_id("EX_tyr__L_e").lower_bound #tyrosine check
model.reactions.get_by_id("EX_tyr__L_e").lower_bound = -(0.25/18)
model.reactions.get_by_id("EX_his__L_e").lower_bound #histidine check
model.reactions.get_by_id("EX_his__L_e").lower_bound = -(0.25/18)
model.reactions.get_by_id("EX_4abut_e").lower_bound #aminobutanoate check
#model.reactions.get_by_id("EX_4abut_e").lower_bound = -(0.25/18)
model.reactions.get_by_id("EX_cytd_e").lower_bound #cytidine check
model.reactions.get_by_id("EX_cytd_e").lower_bound = -(0.25/18)
model.reactions.get_by_id("EX_thymd_e").lower_bound #thymidine check
model.reactions.get_by_id("EX_thymd_e").lower_bound = -(0.25/18)
solAfter=model.optimize()
# Save model with constraints set
cobra.io.write_sbml_model(model, "cin_Exud_soft_Bnds.xml")



##### 4. Perfom FBA simulations comparing minimal and exudate media on an equal substrate uptake basis (Figure 3)

# C. pusillum (cpu)
model_Syn_cpuB = cobra.io.read_sbml_model("cpu_Syn_soft_Bnds.xml")
model_Exud_cpuB = cobra.io.read_sbml_model("cpu_Exud_soft_Bnds.xml")
solS_cpuB = model_Syn.optimize()
solE_cpuB = model_Exud.optimize()

# E. ludwigii (elu)
model_Syn_eluB = cobra.io.read_sbml_model("elu_Syn_soft_Bnds.xml")
model_Exud_eluB = cobra.io.read_sbml_model("elu_Exud_soft_Bnds.xml")
solS_eluB = model_Syn.optimize()
solE_eluB = model_Exud.optimize()

# H. robiniae (hro)
model_Syn_hroB = cobra.io.read_sbml_model("hro_Syn_soft_Bnds.xml")
model_Exud_hroB = cobra.io.read_sbml_model("hro_Exud_soft_Bnds.xml")
solS_hroB = model_Syn.optimize()
solE_hroB = model_Exud.optimize()

# P. putida (ppu)
model_Syn_ppuB = cobra.io.read_sbml_model("ppu_Syn_soft_Bnds.xml")
model_Exud_ppuB = cobra.io.read_sbml_model("ppu_Exud_soft_Bnds.xml")
solS_ppuB = model_Syn.optimize()
solE_ppuB = model_Exud.optimize()

# S. maltophilia (sma)
model_Syn_smaB = cobra.io.read_sbml_model("sma_Syn_soft_Bnds.xml")
model_Exud_smaB = cobra.io.read_sbml_model("sma_Exud_soft_Bnds.xml")
solS_smaB = model_Syn.optimize()
solE_smaB = model_Exud.optimize()

# B. pituitosa (opi)
model_Syn_opiB = cobra.io.read_sbml_model("opi_Syn_soft_Bnds.xml")
model_Exud_opiB = cobra.io.read_sbml_model("opi_Exud_soft_Bnds.xml")
solS_opiB = model_Syn.optimize()
solE_opiB = model_Exud.optimize()

# C. indologenes (cin)
model_Syn_cinB = cobra.io.read_sbml_model("cin_Syn_soft_Bnds.xml")
model_Exud_cinB = cobra.io.read_sbml_model("cin_Exud_soft_Bnds.xml")
solS_cinB = model_Syn.optimize()
solE_cinB = model_Exud.optimize()



##### 5. Create community models

# Community models generated from individual bacterial models incorporating Biolog data after boundaries have been applied
# Community, minimal medium
merge_community opi_Syn_soft_Bnds.xml cin_Syn_soft_Bnds.xml cpu_Syn_soft_Bnds.xml elu_Syn_soft_Bnds.xml hro_Syn_soft_Bnds.xml ppu_Syn_soft_Bnds.xml sma_Syn_soft_Bnds.xml -i MzSyn --mediadb mylibrary_v2.tsv -o C7_Syn_soft_Bnds.xml
# Community, root exudate media
merge_community opi_Exud_soft_Bnds.xml cin_Exud_soft_Bnds.xml cpu_Exud_soft_Bnds.xml elu_Exud_soft_Bnds.xml hro_Exud_soft_Bnds.xml ppu_Exud_soft_Bnds.xml sma_Exud_soft_Bnds.xml -i MzExud --mediadb mylibrary_v2.tsv -o C7_Exud_soft_Bnds.xml



##### 6. Perform community FBA model simulations (Figures 4-6)

# Community, biomass optimization, minimal and exudate media
model7_Syn = cobra.io.read_sbml_model("C7_Syn_soft_init.xml") # minimal medium
model7_Exud = cobra.io.read_sbml_model("C7_Exud_soft_init.xml") # exudate medium

# Check and adjust boundaries for meoh feasibility - should not be able to produce methanol
model7_Syn.reactions.get_by_id("EX_meoh_e").lower_bound #meoh check
#model7_Syn.reactions.get_by_id("EX_meoh_e").lower_bound = 0
model7_Syn.reactions.get_by_id("EX_meoh_e").upper_bound #meoh check
model7_Syn.reactions.get_by_id("EX_meoh_e").upper_bound = 0
model7_Exud.reactions.get_by_id("EX_meoh_e").lower_bound #meoh check
#model7_Exud.reactions.get_by_id("EX_meoh_e").lower_bound = 0
model7_Exud.reactions.get_by_id("EX_meoh_e").upper_bound #meoh check
model7_Exud.reactions.get_by_id("EX_meoh_e").upper_bound = 0

# Run simulation
sol7S = model7_Syn.optimize() # minimal medium solution
sol7E = model7_Exud.optimize() # exudate medium solution



##### 6. Sensitivity testing for individual bacterial models in exudate medium

import cobra
import numpy as np
import pandas as pd

# Define the output data table
output_df = pd.DataFrame(columns=['substrate', 'exchg rxn','mu w/ 2X sub','mu w/ 0.5X sub'])

# Create a list of the primary substrates and corresponding exchange reactions to test and add to the data table
sublist = np.array(["Glycerol","Ribitol","Fructose","Maltose","Inositol","Erythrose","Glucose","Sucrose","Arabinose","Melibiose","Lactose","Isomaltose","Galactose","Xylose","Malate","Succinate","Citrate","Oxaloacetate","Fumarate","Benzoate","Aconitate","Tartrate","Lactate","Malonate"])
col_sublist = sublist.reshape(-1,1)

rxnlist = np.array(["EX_glyc_e","EX_rbt_e","EX_fru_e","EX_malt_e","EX_inost_e","EX_erthrs_e","EX_glc__D_e","EX_sucr_e","EX_arab__L_e","EX_melib_e","EX_lcts_e","EX_isomal_e","EX_gal_e","EX_xyl__D_e","EX_mal__L_e","EX_succ_e","EX_cit_e","EX_oaa_e","EX_fum_e","EX_bz_e","EX_acon_C_e","EX_tartr__L_e","EX_lac__L_e","EX_malon_e"])
col_rxnlist = rxnlist.reshape(-1,1)

output_df[['substrate']] = col_sublist
output_df[['exchg rxn']] = col_rxnlist

# Iterate the following over each substrate in the data table
for row in output_df.index:
    
    # Read in the bacterial metabolic model
    model_Exud = cobra.io.read_sbml_model("sma_Exud_soft_Bnds.xml")
    
    # Check if the model has the given exchange reaction
    try:
        check = model_Exud.reactions.get_by_id(output_df.loc[row,'exchg rxn']).lower_bound #oxaloacetate check
    except KeyError:
        # If the reaction is not present, assign values to NA
        print("this reaction does NOT exist")
        output_df.loc[row,'mu w/ 2X sub'] = "NA"
        output_df.loc[row,'mu w/ 0.5X sub'] = "NA"
    else:
        print("this reaction does exist")
        # Change the substrate boundary to 2X the original constraint
        model_Exud.reactions.get_by_id(output_df.loc[row,'exchg rxn']).lower_bound = -(10/24)*2
        # Optimize the model solution
        solL = model_Exud.optimize()
        # Assign the optimized objective value to the corresponding spot in the data table
        output_df.loc[row,'mu w/ 2X sub'] = solL.objective_value
        # Change the substrate boundary to 0.5X the original constraint
        model_Exud.reactions.get_by_id(output_df.loc[row,'exchg rxn']).lower_bound = -(10/24)*0.5
        # Optimize the model solution
        solS = model_Exud.optimize()
        # Assign the optimized objective value to the corresponding spot in the data table
        output_df.loc[row,'mu w/ 0.5X sub'] = solS.objective_value
        # Clear the model variable before reiterating the loop
        del model_Exud
    


##### 7. Assigning growth/nongrowth states to Biolog data for each bacterial species

import numpy as np
import pandas as pd

# Read in the data for the desired bacterial species
growth_data = pd.read_excel('CIN_rawreads.xlsx',sheet_name='replicateaverages',skiprows=2)

# Define the output data table
output_df = pd.DataFrame(columns=['substrate_label', 'max_growth_rate'])

# Iterate the following over each Biolog substrate in the input data file
for col in growth_data.columns:

    if col == 'Hour':
        print('Skipping first column')
        continue

    relative_slope = growth_data[['Hour',col]]

    # Average the values based on their neighbors (1 on each side)
    relative_slope['avg_val'] = np.zeros(len(relative_slope))
    for i in range(1,len(relative_slope)-1):
        relative_slope.loc[i,'avg_val'] = np.mean((relative_slope.loc[i-1,col],relative_slope.loc[i,col],relative_slope.loc[i+1,col]))

    # Normalization
    y_min = relative_slope['avg_val'].min()
    y_max = relative_slope['avg_val'].max()
    relative_slope['normalized'] = (relative_slope['avg_val'] - y_min) / (y_max - y_min)

    # Smoothing using a Savitzky-Golay filter
    from scipy.signal import savgol_filter
    relative_slope['y_smoothed'] = savgol_filter(relative_slope['normalized'], window_length=11, polyorder=2)

    # Calculating the derivative
    relative_slope['derivative'] = np.gradient(relative_slope['y_smoothed'], relative_slope['Hour'])

    # Initial thresholding
    flat_threshold = 0.05
    relative_slope['increase'] = False
    relative_slope.loc[relative_slope['derivative'] > flat_threshold, 'increase'] = True

    # Noise filter
    noise_threshold = 25
    if max(relative_slope[col]) < noise_threshold:
        relative_slope['increase'] = False

    # Too few data points filter
    size_threshold = 10
    print(relative_slope['increase'].sum())
    if relative_slope['increase'].sum() < size_threshold:
        relative_slope['increase'] = False
    increase_points = relative_slope[relative_slope['increase'] == True]

    if len(increase_points) > 2:
        # Neighbor filter (removes bottom 10% and top 10%)
        l = np.array(increase_points.index)
        lower_cut = l[l < np.quantile(l,0.2)]
        upper_cut = l[l > np.quantile(l,0.8)]
        # Trim the increase_points dataframe
        increase_points = increase_points.iloc[len(lower_cut)-1:len(increase_points)-len(upper_cut)]
        # Set the increase_points dataframe to be the final say on increase being T/F
        relative_slope['increase'] = False
        relative_slope.loc[increase_points.index, 'increase'] = True
        # Set the slope
        slope = (increase_points[col].iloc[-1] - increase_points[col].iloc[0]) / (increase_points['Hour'].iloc[-1] - increase_points['Hour'].iloc[0])
    else:
        relative_slope['increase'] = False
        slope = 0
    
    row_list = [col,slope]
    output_df.loc[len(output_df)] = row_list

