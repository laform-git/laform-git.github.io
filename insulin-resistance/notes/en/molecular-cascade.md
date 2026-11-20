# Insulin Signaling — Molecular Cascade
*The molecular chain reaction from insulin binding its receptor through Akt activation to GLUT4 glucose uptake, and exactly where insulin resistance jams the cascade.*

**In plain words:** when insulin reaches a cell, it does not open the sugar door directly. It starts a chain reaction inside the cell, like a row of dominoes, and the last domino opens the door. This note follows that chain one piece at a time and shows the two places where fat stored in the wrong place jams it. That jam is what "insulin resistance" means at the smallest scale. The names of the proteins are long, but each one gets a plain job description in the table below.

**Words in this note:**
- **GLUT4**: the sugar door in muscle and fat cells that insulin opens
- **IRS-1**: insulin receptor substrate 1, the first relay in insulin's signal inside the cell
- **PI3K**: an enzyme that passes insulin's signal along inside the cell
- **PIP3**: a signaling molecule made by PI3K
- **DAG**: diacylglycerol, a fat fragment that can jam insulin's signal
- **SREBP-1c**: a switch that turns on fat-making in the liver
- **AMPK**: the cell's fuel-gauge switch, turned on when energy is low
- **HDL**: high-density lipoprotein, the "good" cholesterol carrier
- **LDL**: low-density lipoprotein, the "bad" cholesterol carrier
- **HbA1c**: a blood test showing average blood sugar over about three months
- **TG**: triglycerides, the main fat in the blood

## Why This Matters

Insulin resistance is not a broken lock. It is a jammed chain of dominoes inside the cell. Knowing exactly where the chain jams explains why berberine (a plant supplement), exercise and fasting work at the molecular level, meaning at the level of the molecules inside the cell.

---

## The Players — Quick Reference

| Term | Plain English |
|---|---|
| Insulin Receptor (IR) | The lock on the cell surface |
| Phosphorylation | Sticking a phosphate tag onto a protein — turns it on or off |
| IRS-1 / IRS-2 | First relays inside the cell — the first domino (IRS-1 dominates in muscle, IRS-2 in liver) |
| PI3K | Enzyme that lights the assemble-here flare |
| PIP2 / PIP3 | Membrane signals — PIP3 is the active flare |
| PDK1 + mTORC2 | Two enzymes that together fully activate Akt |
| Akt | Grand central station — activates all downstream effects (everything that happens after it in the chain) |
| GLUT4 | The actual glucose door in muscle and fat cells |
| AS160 | Brake keeping GLUT4 closed — Akt releases it |
| GSK3 | Blocks glycogen storage (glycogen is the body's short-term sugar store) — Akt switches it off |
| FOXO1 | Gene switch telling liver to make sugar — Akt ejects it |
| mTORC1 / SREBP | Build fat and protein — Akt fires them up |
| DAG | Fat byproduct that jams IRS-1 |
| Ceramide | Fat byproduct that disables Akt |
| PKCθ/ε | Enzymes activated by DAG — PKCθ puts a wrong tag on IRS-1 (muscle); PKCε blocks the receptor's own kinase (liver) |
| PP2A | Enzyme activated by ceramide — strips Akt's activation tags |

*An enzyme is a protein that does a job, such as switching another protein on or off. A kinase is an enzyme that switches proteins on or off by adding a phosphate tag.*

---

## The Cascade — Step by Step

### Step 1 — Insulin binds the receptor

- Insulin binds the two α-subunits (alpha parts) of the receptor on the outside of the cell
- This changes the receptor's shape and brings its two inner β-subunits (beta parts) together
- *In plain words:* the key goes into the lock.

### Step 2 — Autophosphorylation (lock activates itself)

- The β-subunits tag each other with phosphate groups on tyrosine residues (tyrosine is one of the building blocks of proteins)
- This is the literal molecular moment of the key turning the lock
- ✅ Rock solid: textbook receptor tyrosine kinase mechanism (a receptor that switches itself on by tagging tyrosines)

### Step 3 — IRS-1 docking (first domino)

- Active receptor phosphorylates IRS-1 (and IRS-2, the main relay in liver)
- Tyrosine-phosphate tags act as Velcro docking stations for the next proteins
- Most critical relay point — if jammed here, the whole chain fails
- *In plain words:* the lock passes the message to the first runner inside the cell.
- 🟢 In muscle of people with obesity or type 2 diabetes, insulin's activation of IRS-1–PI3K is sharply reduced, and this tracks glucose disposal, meaning how much sugar the body clears from the blood (Cusi 2000)

### Step 4 — PI3K lights the flare

- PI3K docks onto IRS-1, converts PIP2 into PIP3
- PIP3 = the assemble-here signal on the inner cell wall
- PTEN erases PIP3 — the natural off-switch
- *In plain words:* a flare goes up on the inside of the cell wall, calling the next workers to gather there.

### Step 5 — Akt fully activated

- PIP3 recruits PDK1 and Akt to the membrane
- PDK1 tags Akt at Thr308; mTORC2 tags Akt at Ser473 (Thr308 and Ser473 are two exact spots on the Akt protein)
- Both tags required = Akt fully ON
- *In plain words:* the central switch needs two keys turned at once, like a bank vault. When both are turned, it switches on.
- ✅ Rock solid: dual phosphorylation is textbook (mTORC2 as the Ser473 kinase: Sarbassov 2005)

### Step 6 — Akt fires 4 payoffs simultaneously

**Payoff 1 — Glucose doors open**
- Akt switches off brake AS160
- GLUT4 vesicles (tiny bubbles inside the cell that carry the sugar doors) fuse to the cell surface — glucose flows in
- ✅ Rock solid

**Payoff 2 — Glycogen storage**
- Akt blocks GSK3 → glycogen synthesis ramps up
- ✅ Rock solid

**Payoff 3 — Liver shuts off glucose production**
- Akt ejects FOXO1 from the nucleus (the cell's control center, where the genes are) → the genes PEPCK and G6Pase, which make sugar, go silent
- ✅ Rock solid
- In the whole body, much of insulin's fast suppression of liver glucose output is indirect — by curbing fat breakdown (lipolysis) in fat tissue and by curbing glucagon (the hormone that tells the liver to release sugar) — not only this direct liver signal 🟢 (Petersen & Shulman 2018)

**Payoff 4 — Fat and protein synthesis**
- Akt fires mTORC1 and SREBP-1c → storage and building mode
- ✅ Rock solid: Akt → mTORC1 → SREBP-1c drives fat synthesis in normal physiology
- This branch stays partially active even in insulin resistance — IR blocks glucose uptake AND keeps promoting fat storage simultaneously
- 🟢 The phenomenon ("selective hepatic insulin resistance", hepatic meaning of the liver: high blood sugar plus high triglycerides, the main fat in the blood) is well documented (Brown & Goldstein 2008). 🟡 Its cause is contested: one view is a still-sensitive SREBP-1c branch; another is that excess substrate (glucose diverted from insulin-resistant muscle, plus fatty acids) drives liver fat production largely independent of insulin signaling (Petersen 2007; Petersen & Shulman 2018)

### Step 7 — The growth branch (MAPK, parallel)

- IRS-1 also feeds: Grb2 → Ras → Raf → MEK → ERK
- Handles cell growth, not glucose — stays active even when metabolic branch fails
- *In plain words:* insulin's signal also splits off into a second track that tells cells to grow. That track keeps working even when the sugar track is jammed.
- 🟢 In muscle from people with type 2 diabetes, insulin's activation of the MAPK branch was normal while the PI3K branch was nearly absent (Cusi 2000)

---

## Where Insulin Resistance Breaks the Chain

### Saboteur 1 — DAG jams Step 3 (IRS-1)

- Ectopic fat (fat inside muscle or liver cells) produces DAG — specifically, DAG builds up when fat enters these cells faster than it can be burned or safely stored. Stored fat droplets themselves are fairly inert: endurance athletes carry high muscle fat yet are very insulin sensitive (Goodpaster 2001)
- DAG activates PKCθ (muscle; shown in humans: Szendroedi 2014) or PKCε (liver)
- In muscle, PKCθ slaps an inhibitory (blocking) phosphate tag on a serine of IRS-1 (Ser1101, an exact spot on the protein) — the wrong tag (Li 2004)
- In liver, PKCε instead tags the insulin receptor itself (Thr1160), blocking its kinase activity (Petersen 2016)
- The signal relays only weakly — the first domino barely tips
- *In plain words:* fat that leaks into muscle and liver cells makes a by-product (DAG). DAG switches on an enzyme that puts the wrong tag on the first runner, so the runner barely moves.
- 🟢 Strong evidence for DAG → PKC → insulin resistance in human muscle and liver
- 🟡 The serine-tag step is less settled: IRS proteins have more than 50 serine/threonine sites with both positive and negative effects, and their exact role in living tissue is debated (Copps & White 2012)

### Saboteur 2 — Ceramide disables Step 5 (Akt)

- Ectopic fat also produces ceramide
- Ceramide activates PP2A, which strips activating phosphates OFF Akt (and PKCζ, which keeps Akt away from the membrane, the cell wall)
- Even if Steps 1–4 worked, the signal dies here
- *In plain words:* a second fat by-product (ceramide) pulls the two keys back out of the central switch, so it turns off again.
- 🟢 Strong evidence in cell and animal studies (Chavez & Summers 2012)
- 🟡 In humans the data are less consistent than for DAG (Petersen & Shulman 2018)

### The Cruel Irony

- Both saboteurs come from fat in the wrong place (other contributors — inflammation, ER stress (strain on the cell's protein-making factory), and high insulin itself — are also proposed 🟡 Petersen & Shulman 2018)
- Fat-storage branch (Payoff 4) keeps running while glucose handling is jammed
- IR simultaneously blocks glucose uptake AND continues promoting fat storage

---

## One-Breath Summary

Insulin binds → receptor self-activates → IRS-1 tagged → PI3K lights PIP3 flare → Akt double-tagged ON → GLUT4 opens + glycogen stored + liver shut off + fat built. Resistance = DAG jams the signal at Step 3 (IRS-1 in muscle, the receptor's kinase in liver), ceramide kills Akt at Step 5. Both caused by fat in the wrong place.

*Same thing in everyday words:* insulin turns the key → a chain of messengers carries the message inward → the central switch turns on → sugar doors open, sugar is stored, the liver stops making sugar, and fat gets built. In insulin resistance, fat in the wrong place jams the chain in two spots, so the sugar message gets lost.

---

## Why Berberine, Exercise & Fasting All Work

- All three activate AMPK (the cell's fuel gauge, which switches on when energy runs low) — a parallel bypass that circumvents the jammed cascade 🟡 (fully true only for exercise; see below)
- AMPK drives GLUT4 to the surface independently of IRS-1 and Akt
- **Exercise:** muscle contraction moves GLUT4 to the surface through signals separate from insulin, and this still works in insulin-resistant muscle ✅. AMPK is one of these signals, but not the only one — no single pathway fully explains it (Sylow 2017) 🟢
- **Berberine:** activates AMPK and moves GLUT4 independently of PI3K in cell and animal studies (Lee 2006) 🟢; in humans it likely acts through several routes, and the AMPK bypass as the main explanation is 🟡
- **Fasting / calorie deficit:** works mainly by emptying liver fat and glycogen and lowering insulin, not through a direct AMPK–GLUT4 bypass; that framing is 🔴 interpretation
- This is why they restore insulin sensitivity even when the top of the cascade is broken 🟡 — exercise and weight loss also repair the cascade itself by draining ectopic fat (see Practical Takeaway)

---

## Key Correction

> Insulin usually binds the receptor (lock) fine. The jam is inside — at IRS-1 in muscle or the receptor's own kinase in liver (Step 3, DAG), or at Akt (Step 5, ceramide). The key fits. The message gets lost.

---

## Practical Takeaway

Draining ectopic fat (fat stored where it does not belong) from muscle and liver — through exercise, caloric deficit, or reducing refined carbohydrate load — is the most direct way to unjam both saboteur points and restore insulin sensitivity. 🟢 In people with type 2 diabetes, losing about 8 kg cut liver fat by about 80% and normalized liver insulin resistance and fasting glucose (Petersen 2005); in the DiRECT trial, an intensive weight-loss program put 46% of people with recent type 2 diabetes into remission (blood sugar back below the diabetes line without diabetes drugs) at 12 months (Lean 2018). Calorie deficit is the proven driver; cutting refined carbohydrate helps mainly by lowering calories and liver fat production 🟡.

---

## Open Threads

- AMPK deep dive — how berberine, exercise, and fasting hit the same bypass
- Full GLUT4 trafficking mechanism
- mTORC1 vs mTORC2 — different roles in the same cascade

---

## Addendum (2026-07-31): Selective Insulin Resistance — Why Insulin Resistance Makes MORE Fat, Not Less

**The paradox**

If part of insulin's job is to build fat, shouldn't insulin resistance mean *less* fat gets made? It would, if the resistance were uniform across the whole cascade. It is not.

**The mechanism: resistance is pathway-specific, not all-or-nothing**

Back to Step 6 above: Akt fires 4 effects from a single signal. In insulin resistance, the saboteurs (DAG at IRS-1, ceramide at Akt) do not switch off all 4 effects equally.

- **Effect 1 (GLUT4/glucose uptake)**: becomes resistant early and severely. It is the pathway most sensitive to the DAG/ceramide jam. 🟢 (Cusi 2000; Petersen 2007)
- **Effect 4 (mTORC1/SREBP-1c → fat and protein synthesis)**: in the liver, fat-making stays active and even increases. The literature calls this **"selective hepatic insulin resistance"** 🟢 (Brown & Goldstein 2008): the liver goes deaf to insulin's glucose-control message but keeps making fat. 🟡 Whether this is because the SREBP-1c branch stays "fully responsive" to insulin is debated; part of the extra fat may come from excess substrate (glucose and fatty acids) rather than from the insulin signal (Petersen 2007; Petersen & Shulman 2018).

**Why this makes things worse, step by step**

1. Effect 1 is jammed → blood glucose stays high after meals.
2. The pancreas responds the only way it can: it secretes **more insulin** to try to force the resistant glucose pathway open (compensatory hyperinsulinemia).
3. That extra insulin cannot fix the jammed glucose pathway (Steps 3/5 are still blocked), but it **does reach the fat-building pathway, which is still responding** 🟡 (Effect 4, SREBP-1c → ACC/FAS, two fat-making enzymes → de novo lipogenesis, the liver making new fat from sugar; see the Lipid Triad note).
4. Net result: high blood sugar **and** higher triglyceride/fat production at the same time; not in spite of the resistance, but *because of* the compensatory response to it.

**The analogy**

Two doors, the same key. The lock on the glucose door wears out (resistant), so the body cuts more copies of the key (more insulin) to force it. The lock on the fat door never wore out. Now it gets far more keys than normal and opens harder and more often than before the resistance began.

---

**The point to remember: in insulin resistance the key still fits the lock. The message gets lost inside the cell, jammed by fat stored in the wrong place. Draining that fat through exercise and weight loss is the most direct way to clear the jam.**

---
**References:**
1. Petersen MC, Shulman GI. Mechanisms of insulin action and insulin resistance. *Physiol Rev* 2018;98(4):2133-2223. [PubMed](https://pubmed.ncbi.nlm.nih.gov/30067154/)
2. Sarbassov DD, Guertin DA, Ali SM, et al. Phosphorylation and regulation of Akt/PKB by the rictor-mTOR complex. *Science* 2005;307(5712):1098-1101. [PubMed](https://pubmed.ncbi.nlm.nih.gov/15718470/)
3. Cusi K, Maezono K, Osman A, et al. Insulin resistance differentially affects the PI 3-kinase- and MAP kinase-mediated signaling in human muscle. *J Clin Invest* 2000;105(3):311-320. [PubMed](https://pubmed.ncbi.nlm.nih.gov/10675357/)
4. Brown MS, Goldstein JL. Selective versus total insulin resistance: a pathogenic paradox. *Cell Metab* 2008;7(2):95-96. [PubMed](https://pubmed.ncbi.nlm.nih.gov/18249166/)
5. Petersen KF, Dufour S, Savage DB, et al. The role of skeletal muscle insulin resistance in the pathogenesis of the metabolic syndrome. *Proc Natl Acad Sci U S A* 2007;104(31):12587-12594. [PubMed](https://pubmed.ncbi.nlm.nih.gov/17640906/)
6. Goodpaster BH, He J, Watkins S, Kelley DE. Skeletal muscle lipid content and insulin resistance: evidence for a paradox in endurance-trained athletes. *J Clin Endocrinol Metab* 2001;86(12):5755-5761. [PubMed](https://pubmed.ncbi.nlm.nih.gov/11739435/)
7. Szendroedi J, Yoshimura T, Phielix E, et al. Role of diacylglycerol activation of PKCθ in lipid-induced muscle insulin resistance in humans. *Proc Natl Acad Sci U S A* 2014;111(26):9597-9602. [PubMed](https://pubmed.ncbi.nlm.nih.gov/24979806/)
8. Li Y, Soos TJ, Li X, et al. Protein kinase C Theta inhibits insulin signaling by phosphorylating IRS1 at Ser(1101). *J Biol Chem* 2004;279(44):45304-45307. [PubMed](https://pubmed.ncbi.nlm.nih.gov/15364919/)
9. Petersen MC, Madiraju AK, Gassaway BM, et al. Insulin receptor Thr1160 phosphorylation mediates lipid-induced hepatic insulin resistance. *J Clin Invest* 2016;126(11):4361-4371. [PubMed](https://pubmed.ncbi.nlm.nih.gov/27760050/)
10. Copps KD, White MF. Regulation of insulin sensitivity by serine/threonine phosphorylation of insulin receptor substrate proteins IRS1 and IRS2. *Diabetologia* 2012;55(10):2565-2582. [PubMed](https://pubmed.ncbi.nlm.nih.gov/22869320/)
11. Chavez JA, Summers SA. A ceramide-centric view of insulin resistance. *Cell Metab* 2012;15(5):585-594. [PubMed](https://pubmed.ncbi.nlm.nih.gov/22560211/)
12. Sylow L, Kleinert M, Richter EA, Jensen TE. Exercise-stimulated glucose uptake - regulation and implications for glycaemic control. *Nat Rev Endocrinol* 2017;13(3):133-148. [PubMed](https://pubmed.ncbi.nlm.nih.gov/27739515/)
13. Lee YS, Kim WS, Kim KH, et al. Berberine, a natural plant product, activates AMP-activated protein kinase with beneficial metabolic effects in diabetic and insulin-resistant states. *Diabetes* 2006;55(8):2256-2264. [PubMed](https://pubmed.ncbi.nlm.nih.gov/16873688/)
14. Petersen KF, Dufour S, Befroy D, et al. Reversal of nonalcoholic hepatic steatosis, hepatic insulin resistance, and hyperglycemia by moderate weight reduction in patients with type 2 diabetes. *Diabetes* 2005;54(3):603-608. [PubMed](https://pubmed.ncbi.nlm.nih.gov/15734833/)
15. Lean MEJ, Leslie WS, Barnes AC, et al. Primary care-led weight management for remission of type 2 diabetes (DiRECT): an open-label, cluster-randomised trial. *Lancet* 2018;391(10120):541-551. [PubMed](https://pubmed.ncbi.nlm.nih.gov/29221645/)
