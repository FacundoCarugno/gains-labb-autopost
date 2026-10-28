"""Dias 26-32: tanda 4. Datos verificados contra resumenes/abstracts el 28/10/2026."""
from reels_more import L, hook, cta, caption
from reels_more2 import tips3
from reels_more3 import stat, out

# ------------------------------------------------------------------ DIA 26
def reel_protein(handle):
    S = [
        hook(26, "twenty-six", "veintiséis", "TEACHING YOU: PROTEIN", "Enseñándote: proteína", ["HOW MUCH PROTEIN", "DO YOU NEED?"],
             "protein", "la proteína",
             ("Is more protein always better for muscle?", ["Is more protein always", "better for muscle?"]),
             ("¿Más proteína siempre es mejor para el músculo?", ["¿Más proteína siempre es", "mejor para el músculo?"]), icon="flame"),
        stat("PROTEIN + LIFTING · META-ANALYSIS", "1.6", 190, 0.55, "flame", ["g of protein per kg per day:", "gains stopped rising beyond it"],
             [L("A meta-analysis pooled forty-nine studies and one thousand eight hundred sixty-three people doing resistance training.",
                "Un metaanálisis reunió 49 estudios y 1.863 personas que hacían entrenamiento de fuerza.",
                ["49 studies, 1,863 people", "doing resistance training."], ["49 estudios, 1.863 personas", "haciendo entrenamiento de fuerza."]),
              L("Protein supplements added muscle and strength. Beyond about one point six grams per kilo per day, there were no further muscle-mass gains.",
                "Los suplementos de proteína sumaron músculo y fuerza. Por encima de unos 1,6 gramos por kilo al día no hubo más ganancia de masa muscular.",
                ["Protein added muscle and strength.", "Above ~1.6 g/kg/day: no further gains."], ["La proteína sumó músculo y fuerza.", "Sobre ~1,6 g/kg/día: sin más ganancia."]),
              L("For a seventy-kilo person, that is about one hundred thirteen grams a day.",
                "Para una persona de 70 kilos, son unos 113 gramos al día.",
                ["For a 70 kg person,", "that is ~113 g a day."], ["Para una persona de 70 kg,", "son ~113 g al día."])],
             count=(1.6, "{:.1f}")),
        tips3("THE NUMBERS", ["flame", "dumbbell", "flask"],
              [("Fat-free mass: +0.30 kg on average", "Masa libre de grasa: +0,30 kg en promedio"),
               ("Strength: +2.49 kg in 1-rep max", "Fuerza: +2,49 kg en 1RM"),
               ("Benefit fell with age, rose with experience", "El beneficio bajó con la edad y subió con la experiencia")],
              [L("On average, supplements added zero point three kilos of fat-free mass.", "En promedio, los suplementos sumaron 0,3 kilos de masa libre de grasa.",
                 ["On average: +0.30 kg", "of fat-free mass."], ["En promedio: +0,30 kg", "de masa libre de grasa."]),
               L("And two point five kilos to the one-rep max.", "Y 2,5 kilos al máximo de una repetición.", ["And +2.49 kg to the", "one-rep max."], ["Y +2,49 kg al", "máximo de una repetición."]),
               L("The benefit shrank with age and grew with training experience.", "El beneficio se redujo con la edad y creció con la experiencia de entrenamiento.",
                 ["It shrank with age and grew", "with training experience."], ["Se redujo con la edad y creció", "con la experiencia."])]),
        cta(26, "twenty-seven", "veintisiete", "DAY 27 TOMORROW: PROTEIN TIMING", "Mañana, día 27: momento de la proteína"),
    ]
    cap = caption(26, "protein", "proteína",
                  "Is more protein always better for muscle? A meta-analysis of 49 studies (1,863 participants) found that protein supplementation during prolonged resistance training increased 1-rep-max strength by 2.49 kg and fat-free mass by 0.30 kg on average. Total intakes above about 1.62 g/kg/day produced no further gains in fat-free mass. The benefit of supplementation decreased with age and increased with training experience. For a 70 kg person, 1.62 g/kg is roughly 113 g a day. If you have a kidney or other health condition, ask your doctor before changing your protein intake.",
                  "¿Más proteína siempre es mejor para el músculo? Un metaanálisis de 49 estudios (1.863 participantes) halló que la suplementación con proteína durante un entrenamiento de fuerza prolongado aumentó la fuerza de 1 repetición máxima en 2,49 kg y la masa libre de grasa en 0,30 kg en promedio. Con ingestas totales por encima de ~1,62 g/kg/día no hubo más ganancia de masa libre de grasa. El beneficio de la suplementación disminuyó con la edad y aumentó con la experiencia de entrenamiento. Para 70 kg, 1,62 g/kg son unos 113 g al día. Si tienes una condición renal u otra, consulta a tu médico antes de cambiar tu ingesta de proteína.",
                  handle, "Morton et al., Br J Sports Med, 2018")
    return out(26, "protein", S, cap, "#protein #musclegrowth #nutrition #strengthtraining #fitness", "Morton et al., Br J Sports Med, 2018")

# ------------------------------------------------------------------ DIA 27
def reel_timing(handle):
    S = [
        hook(27, "twenty-seven", "veintisiete", "TEACHING YOU: PROTEIN TIMING", "Enseñándote: momento de la proteína", ["IS THERE AN", "ANABOLIC WINDOW?"],
             "protein timing", "el momento de la proteína",
             ("Must you drink protein right after training?", ["Must you drink protein", "right after training?"]),
             ("¿Hay que tomar proteína justo después de entrenar?", ["¿Hay que tomar proteína", "justo después de entrenar?"]), icon="clock"),
        {"type": "vs", "tail": 0.7, "head": "SQUAT 1-REP MAX GAIN · 10 WEEKS", "sub": "21 trained men · protein before vs after",
         "rows": [{"title": "Protein before", "sub": "pre-workout", "es": "Antes de entrenar", "val": 3.7, "fmt": "+{:.1f}%"},
                  {"title": "Protein after", "sub": "post-workout", "es": "Después de entrenar", "val": 4.9, "fmt": "+{:.1f}%"}],
         "lines": [L("In a ten-week trial, twenty-one trained men took the same protein either right before or right after lifting.",
                     "En un ensayo de diez semanas, 21 hombres entrenados tomaron la misma proteína justo antes o justo después de entrenar.",
                     ["21 trained men, 10 weeks: same", "protein before or after lifting."], ["21 hombres entrenados, 10 semanas: la misma", "proteína antes o después de entrenar."]),
                   L("Squat strength rose three point seven percent with protein before, and four point nine percent after.",
                     "La fuerza en sentadilla subió un 3,7 por ciento con proteína antes y un 4,9 por ciento después.",
                     ["Squat strength: +3.7% before,", "+4.9% after."], ["Fuerza en sentadilla: +3,7 % antes,", "+4,9 % después."]),
                   L("That difference was not statistically significant.", "Esa diferencia no fue estadísticamente significativa.",
                     ["That difference was not", "statistically significant."], ["Esa diferencia no fue", "estadísticamente significativa."])]},
        tips3("WHAT IT MEANS", ["clock", "flask", "target"],
              [("Pre and post: similar effects", "Antes y después: efectos similares"),
               ("No sign of a narrow window", "Sin señal de una ventana estrecha"),
               ("One small trial, in an energy deficit", "Un ensayo pequeño, con déficit de energía")],
              [L("Protein before or after training had similar effects on all measures.", "La proteína antes o después de entrenar tuvo efectos similares en todas las medidas.",
                 ["Before or after: similar effects", "on all measures."], ["Antes o después: efectos similares", "en todas las medidas."]),
               L("The authors saw no sign of a narrow anabolic window.", "Los autores no vieron señal de una ventana anabólica estrecha.",
                 ["The authors saw no sign of a", "narrow anabolic window."], ["Los autores no vieron señal de", "una ventana anabólica estrecha."]),
               L("But it was one small trial, and the men ended up in an energy deficit.", "Pero fue un ensayo pequeño, y los hombres terminaron en déficit de energía.",
                 ["But it was one small trial, and", "the men ended in an energy deficit."], ["Pero fue un ensayo pequeño, y los", "hombres quedaron en déficit de energía."])]),
        cta(27, "twenty-eight", "veintiocho", "DAY 28 TOMORROW: HIIT VS STEADY CARDIO", "Mañana, día 28: HIIT vs cardio constante"),
    ]
    cap = caption(27, "protein timing", "momento de la proteína",
                  "Must you drink protein right after training? In a 10-week trial, 21 resistance-trained men (3 sessions a week) took protein either right before or right after training. Squat 1RM rose 3.7% (before) vs 4.9% (after) and bench press 2.4% vs 3.3%, with no significant difference between groups; muscle thickness also showed no consistent difference. The authors saw no support for a narrow post-exercise anabolic window. Caveat: one small trial, and participants unintentionally ended up in an energy deficit, so results may not apply to everyone.",
                  "¿Hay que tomar proteína justo después de entrenar? En un ensayo de 10 semanas, 21 hombres entrenados en fuerza (3 sesiones por semana) tomaron proteína justo antes o justo después de entrenar. La sentadilla 1RM subió 3,7 % (antes) vs 4,9 % (después) y el press de banca 2,4 % vs 3,3 %, sin diferencia significativa entre grupos; el grosor muscular tampoco mostró una diferencia consistente. Los autores no vieron apoyo para una ventana anabólica posterior al ejercicio estrecha. Salvedad: un ensayo pequeño, y los participantes quedaron sin querer en déficit de energía, así que puede no aplicar a todos.",
                  handle, "Schoenfeld et al., PeerJ, 2017")
    return out(27, "protein-timing", S, cap, "#proteintiming #anabolicwindow #nutrition #musclegrowth #gym", "Schoenfeld et al., PeerJ, 2017")

# ------------------------------------------------------------------ DIA 28
def reel_hiit(handle):
    S = [
        hook(28, "twenty-eight", "veintiocho", "TEACHING YOU: HIIT VS STEADY CARDIO", "Enseñándote: HIIT vs cardio constante", ["HIIT OR STEADY CARDIO", "FOR LOSING FAT?"],
             "intervals versus steady cardio", "intervalos contra cardio constante",
             ("Is interval training better for losing fat?", ["Is interval training", "better for losing fat?"]),
             ("¿El entrenamiento por intervalos es mejor para perder grasa?", ["¿Los intervalos son mejores", "para perder grasa?"]), icon="bolt"),
        {"type": "vs", "tail": 0.7, "head": "TIME NEEDED (STEADY CARDIO = 100%)", "sub": "13 trials · overweight adults 18–45",
         "rows": [{"title": "HIIT", "sub": "intervals", "es": "Intervalos", "val": 60, "fmt": "{:.0f}%", "win": True},
                  {"title": "Steady cardio", "sub": "moderate intensity", "es": "Cardio constante", "val": 100, "fmt": "{:.0f}%"}],
         "lines": [L("A meta-analysis of thirteen trials compared interval training with steady moderate cardio in overweight and obese adults.",
                     "Un metaanálisis de 13 ensayos comparó el entrenamiento por intervalos con cardio moderado constante en adultos con sobrepeso y obesidad.",
                     ["13 trials: intervals vs steady", "moderate cardio, overweight adults."], ["13 ensayos: intervalos vs cardio", "moderado constante, con sobrepeso."]),
                   L("Both reduced body fat, and the two did not differ significantly.", "Ambos redujeron la grasa corporal, y no difirieron de forma significativa.",
                     ["Both reduced body fat,", "with no significant difference."], ["Ambos redujeron la grasa,", "sin diferencia significativa."]),
                   L("But intervals took about forty percent less training time.", "Pero los intervalos requirieron cerca de un cuarenta por ciento menos de tiempo de entrenamiento.",
                     ["But intervals took about 40%", "less training time."], ["Pero los intervalos requirieron ~40 %", "menos tiempo de entrenamiento."])]},
        tips3("TAKEAWAYS", ["bolt", "clock", "check"],
              [("Similar fat loss either way", "Pérdida de grasa similar en ambos"),
               ("Intervals: time-efficient", "Intervalos: más eficientes en tiempo"),
               ("Best one is the one you keep doing", "La mejor es la que sigues haciendo")],
              [L("In these trials, fat loss was similar either way.", "En estos ensayos, la pérdida de grasa fue similar en ambos casos.",
                 ["In these trials, fat loss", "was similar either way."], ["En estos ensayos, la pérdida de grasa", "fue similar en ambos casos."]),
               L("Intervals may be a time-efficient option.", "Los intervalos pueden ser una opción eficiente en tiempo.",
                 ["Intervals may be a", "time-efficient option."], ["Los intervalos pueden ser una", "opción eficiente en tiempo."]),
               L("So pick the one you will actually keep doing. Hard intervals are not for everyone, so check with your doctor.", "Así que elige la que de verdad vas a mantener. Los intervalos intensos no son para todos: consulta a tu médico.",
                 ["Pick the one you will keep doing.", "Hard intervals: check with your doctor."], ["Elige la que vas a mantener.", "Intervalos intensos: consulta a tu médico."])]),
        cta(28, "twenty-nine", "veintinueve", "DAY 29 TOMORROW: RANGE OF MOTION", "Mañana, día 29: rango de movimiento"),
    ]
    cap = caption(28, "intervals vs steady cardio", "intervalos vs cardio constante",
                  "Is interval training better for losing fat? A systematic review and meta-analysis of 13 trials (overweight and obese adults aged 18–45, about 3 sessions a week for 10 weeks on average) found that both HIIT and moderate-intensity continuous training significantly reduced whole-body fat mass, with no significant difference between them. HIIT required about 40% less training time. The authors conclude both are similarly effective across body composition measures, and HIIT may be a time-efficient part of weight management. Hard intervals are not for everyone: if you have a health condition, ask your doctor first.",
                  "¿El entrenamiento por intervalos es mejor para perder grasa? Una revisión sistemática y metaanálisis de 13 ensayos (adultos con sobrepeso y obesidad de 18–45 años, unas 3 sesiones por semana durante 10 semanas en promedio) halló que tanto el HIIT como el entrenamiento continuo de intensidad moderada redujeron de forma significativa la masa grasa total, sin diferencia significativa entre ellos. El HIIT requirió cerca de un 40 % menos de tiempo de entrenamiento. Los autores concluyen que ambos son igual de efectivos en las medidas de composición corporal, y que el HIIT puede ser una parte eficiente en tiempo del control de peso. Los intervalos intensos no son para todos: si tienes una condición de salud, consulta antes a tu médico.",
                  handle, "Wewege et al., Obes Rev, 2017")
    return out(28, "hiit", S, cap, "#hiit #cardio #fatloss #weightloss #fitness", "Wewege et al., Obes Rev, 2017")

# ------------------------------------------------------------------ DIA 29
def reel_rom(handle):
    S = [
        hook(29, "twenty-nine", "veintinueve", "TEACHING YOU: RANGE OF MOTION", "Enseñándote: rango de movimiento", ["FULL OR PARTIAL", "REPS FOR GROWTH?"],
             "range of motion", "el rango de movimiento",
             ("Should you lift through the full range of motion?", ["Should you lift through", "the full range of motion?"]),
             ("¿Hay que levantar con el rango de movimiento completo?", ["¿Hay que levantar con el", "rango de movimiento completo?"]), icon="dumbbell"),
        stat("RANGE OF MOTION · SYSTEMATIC REVIEW", "6", 190, 0.4, "dumbbell", ["studies, 135 participants", "(4 lower body, 2 upper body)"],
             [L("A systematic review found six studies comparing full and partial range of motion, with one hundred thirty-five participants.",
                "Una revisión sistemática halló seis estudios que comparaban rango completo y parcial, con 135 participantes.",
                ["6 studies compared full vs partial", "range of motion, 135 participants."], ["6 estudios compararon rango completo", "vs parcial, 135 participantes."]),
              L("For the lower body, full range of motion produced more muscle growth.", "Para el tren inferior, el rango completo produjo más crecimiento muscular.",
                ["For the lower body, full range", "gave more muscle growth."], ["En el tren inferior, el rango completo", "dio más crecimiento muscular."])],
             count=(6, "{:.0f}")),
        tips3("THE FINE PRINT", ["dumbbell", "list", "flask"],
              [("Lower body: full range looks better", "Tren inferior: el rango completo rinde más"),
               ("Upper body: limited, conflicting", "Tren superior: evidencia limitada y contradictoria"),
               ("Trunk: no studies yet", "Tronco: aún sin estudios")],
              [L("For the lower body, full range of motion looks better for growth.", "Para el tren inferior, el rango completo parece mejor para crecer.",
                 ["Lower body: full range looks", "better for growth."], ["Tren inferior: el rango completo", "parece mejor para crecer."]),
               L("For the upper body, the evidence is limited and conflicting.", "Para el tren superior, la evidencia es limitada y contradictoria.",
                 ["Upper body: the evidence is", "limited and conflicting."], ["Tren superior: la evidencia es", "limitada y contradictoria."]),
               L("And for the trunk, nobody has studied it yet.", "Y para el tronco, nadie lo ha estudiado todavía.",
                 ["And for the trunk,", "no studies yet."], ["Y para el tronco,", "aún no hay estudios."])]),
        cta(29, "thirty", "treinta", "DAY 30 TOMORROW: STRETCHING", "Mañana, día 30: estiramientos"),
    ]
    cap = caption(29, "range of motion", "rango de movimiento",
                  "Should you lift through the full range of motion? A systematic review of 6 studies (135 participants: 4 on lower-limb training, 2 on upper-body training) found that full range of motion produced greater hypertrophy of the lower-body muscles than partial range of motion. For the upper body, the evidence was limited and conflicting, and no studies had examined trunk muscles. Small samples, mostly young men: treat it as a guide, not a law.",
                  "¿Hay que levantar con el rango de movimiento completo? Una revisión sistemática de 6 estudios (135 participantes: 4 de entrenamiento de miembros inferiores y 2 de tren superior) halló que el rango de movimiento completo produjo mayor hipertrofia de los músculos del tren inferior que el rango parcial. Para el tren superior, la evidencia fue limitada y contradictoria, y ningún estudio había examinado los músculos del tronco. Muestras pequeñas, sobre todo hombres jóvenes: tómalo como guía, no como ley.",
                  handle, "Schoenfeld & Grgic, SAGE Open Med, 2020")
    return out(29, "rom", S, cap, "#rangeofmotion #hypertrophy #squat #strengthtraining #gym", "Schoenfeld & Grgic, SAGE Open Med, 2020")

# ------------------------------------------------------------------ DIA 30
def reel_stretch(handle):
    S = [
        hook(30, "thirty", "treinta", "TEACHING YOU: STRETCHING", "Enseñándote: estiramientos", ["SHOULD YOU STRETCH", "BEFORE LIFTING?"],
             "stretching", "los estiramientos",
             ("Does stretching before training hurt your performance?", ["Does stretching before training", "hurt your performance?"]),
             ("¿Estirar antes de entrenar baja tu rendimiento?", ["¿Estirar antes de entrenar", "baja tu rendimiento?"]), icon="walk"),
        stat("STATIC STRETCHING · SYSTEMATIC REVIEW", "-3.7%", 150, 0.37, "walk", ["average change in performance", "after static stretching"],
             [L("A systematic review looked at how stretching right before exercise changes performance.", "Una revisión sistemática analizó cómo cambia el rendimiento al estirar justo antes de entrenar.",
                ["How does stretching right before", "exercise change performance?"], ["¿Cómo cambia el rendimiento al estirar", "justo antes de entrenar?"]),
              L("Static stretching reduced performance by about three point seven percent on average.", "El estiramiento estático redujo el rendimiento un 3,7 por ciento en promedio.",
                ["Static stretching reduced", "performance ~3.7% on average."], ["El estiramiento estático redujo", "el rendimiento ~3,7 % en promedio."]),
              L("Holding it for sixty seconds or more per muscle was worse than shorter holds.", "Mantenerlo sesenta segundos o más por músculo fue peor que hacerlo menos tiempo.",
                ["Holds of 60+ seconds per muscle:", "-4.6%. Shorter: -1.1%."], ["Mantener 60+ segundos por músculo:", "-4,6 %. Menos: -1,1 %."])]),
        tips3("WHAT TO DO", ["walk", "heart", "clock"],
              [("Dynamic stretching: +1.3% performance", "Estiramiento dinámico: +1,3 % de rendimiento"),
               ("Range-of-motion gains fade in <30 min", "La ganancia de rango se pierde en <30 min"),
               ("Stretch in a warm-up, then move", "Estira dentro de la entrada en calor y muévete")],
              [L("Dynamic stretching slightly improved performance, by one point three percent.", "El estiramiento dinámico mejoró levemente el rendimiento, un 1,3 por ciento.",
                 ["Dynamic stretching slightly", "improved performance: +1.3%."], ["El estiramiento dinámico mejoró", "levemente el rendimiento: +1,3 %."]),
               L("Range of motion improved, but the gains typically lasted under thirty minutes.", "El rango de movimiento mejoró, pero las ganancias solían durar menos de treinta minutos.",
                 ["Range of motion improved, but", "typically for under 30 minutes."], ["El rango mejoró, pero típicamente", "por menos de 30 minutos."]),
               L("The authors suggest stretching within a warm-up, followed by dynamic activity.", "Los autores sugieren estirar dentro de una entrada en calor, seguida de actividad dinámica.",
                 ["Authors: stretch within a warm-up,", "followed by dynamic activity."], ["Autores: estirar dentro de una entrada", "en calor, seguida de actividad dinámica."])]),
        cta(30, "thirty-one", "treinta y uno", "DAY 31 TOMORROW: ONE-MINUTE BURSTS", "Mañana, día 31: ráfagas de un minuto"),
    ]
    cap = caption(30, "stretching", "estiramientos",
                  "Does stretching before training hurt your performance? A systematic review of the acute effects of stretching found that static stretching reduced subsequent performance by about 3.7% on average (-4.6% with holds of 60 s or more per muscle, -1.1% with shorter holds), while dynamic stretching improved it by about 1.3%. All stretching types improved range of motion, but the gains typically lasted under 30 minutes. Static and PNF stretching showed no clear effect on injury rates. The authors suggest stretching within a warm-up followed by dynamic activity. Effects were small to moderate.",
                  "¿Estirar antes de entrenar baja tu rendimiento? Una revisión sistemática de los efectos agudos del estiramiento halló que el estiramiento estático redujo el rendimiento posterior en un 3,7 % en promedio (-4,6 % con 60 s o más por músculo, -1,1 % con menos tiempo), mientras que el dinámico lo mejoró un 1,3 %. Todos los tipos mejoraron el rango de movimiento, pero las ganancias solían durar menos de 30 minutos. El estiramiento estático y el PNF no mostraron un efecto claro sobre las lesiones. Los autores sugieren estirar dentro de una entrada en calor seguida de actividad dinámica. Los efectos fueron de pequeños a moderados.",
                  handle, "Behm et al., Appl Physiol Nutr Metab, 2016")
    return out(30, "stretching", S, cap, "#stretching #mobility #warmup #flexibility #fitness", "Behm et al., Appl Physiol Nutr Metab, 2016")

# ------------------------------------------------------------------ DIA 31
def reel_vilpa(handle):
    S = [
        hook(31, "thirty-one", "treinta y uno", "TEACHING YOU: ONE-MINUTE BURSTS", "Enseñándote: ráfagas de un minuto", ["CAN 1-MINUTE BURSTS", "REALLY MATTER?"],
             "short bursts of activity", "las ráfagas cortas de actividad",
             ("No time to exercise? Could one-minute bursts count?", ["No time to exercise? Could", "1-minute bursts count?"]),
             ("¿Sin tiempo para entrenar? ¿Cuentan las ráfagas de un minuto?", ["¿Sin tiempo para entrenar? ¿Cuentan", "las ráfagas de un minuto?"]), icon="bolt"),
        stat("INTENSE DAILY-LIFE BURSTS", "3–4", 190, 0.5, "bolt", ["bursts a day of about", "one minute each"],
             [L("A study of wearable-device data looked at short bursts of intense activity in daily life, like climbing stairs fast.",
                "Un estudio con datos de dispositivos portátiles analizó ráfagas cortas de actividad intensa en la vida diaria, como subir escaleras rápido.",
                ["Wearable data: short bursts of", "intense daily activity, like fast stairs."], ["Datos de dispositivos: ráfagas cortas", "de actividad intensa, como escaleras."]),
              L("Three to four bursts a day, about one minute each, were associated with up to forty percent lower risk of death.",
                "Tres a cuatro ráfagas al día, de un minuto cada una, se asociaron con hasta un cuarenta por ciento menos de riesgo de muerte.",
                ["3–4 bursts a day, ~1 minute each:", "up to 40% lower risk of death."], ["3–4 ráfagas al día, ~1 minuto cada una:", "hasta 40 % menos riesgo de muerte."])]),
        tips3("READ THIS CAREFULLY", ["bolt", "flask", "heart"],
              [("Up to 49% lower cardiovascular death risk", "Hasta 49 % menos riesgo de muerte cardiovascular"),
               ("These are maximums, not typical results", "Son máximos, no resultados típicos"),
               ("Association, not proof of cause", "Asociación, no prueba de causa")],
              [L("The association with cardiovascular death was up to forty-nine percent lower.", "La asociación con la muerte cardiovascular fue de hasta un 49 por ciento menos.",
                 ["Cardiovascular death: up to", "49% lower risk."], ["Muerte cardiovascular: hasta", "49 % menos riesgo."]),
               L("Those are best-case figures, not typical results.", "Son cifras del mejor caso, no resultados típicos.",
                 ["Those are best-case figures,", "not typical results."], ["Son cifras del mejor caso,", "no resultados típicos."]),
               L("And this is observational: association, not proof of cause.", "Y es observacional: asociación, no prueba de causa.",
                 ["Observational: association,", "not proof of cause."], ["Observacional: asociación,", "no prueba de causa."])]),
        cta(31, "thirty-two", "treinta y dos", "DAY 32 TOMORROW: BACK PAIN", "Mañana, día 32: dolor de espalda"),
    ]
    cap = caption(31, "one-minute bursts", "ráfagas de un minuto",
                  "No time to exercise? A study using wearable-device data looked at vigorous intermittent lifestyle physical activity (VILPA): very short bursts of intense activity in daily life, like climbing stairs fast. Three to four bursts a day of about one minute each were associated with up to 40% lower risk of all-cause and cancer death and up to 49% lower risk of cardiovascular death. These are best-case (\"up to\") figures from an observational study: association, not proof of cause. If you have a health condition, ask your doctor before doing intense bursts.",
                  "¿Sin tiempo para entrenar? Un estudio con datos de dispositivos portátiles analizó la actividad física vigorosa intermitente del estilo de vida (VILPA): ráfagas muy cortas de actividad intensa en la vida diaria, como subir escaleras rápido. Tres a cuatro ráfagas al día de ~1 minuto cada una se asociaron con hasta un 40 % menos de riesgo de muerte por todas las causas y por cáncer y hasta un 49 % menos de muerte cardiovascular. Son cifras del mejor caso (\"hasta\") de un estudio observacional: asociación, no prueba de causa. Si tienes una condición de salud, consulta a tu médico antes de hacer ráfagas intensas.",
                  handle, "Stamatakis et al., Nat Med, 2022")
    return out(31, "vilpa", S, cap, "#exercisesnacks #stairs #health #longevity #fitness", "Stamatakis et al., Nat Med, 2022")

# ------------------------------------------------------------------ DIA 32
def reel_back(handle):
    S = [
        hook(32, "thirty-two", "treinta y dos", "TEACHING YOU: BACK PAIN", "Enseñándote: dolor de espalda", ["DOES EXERCISE HELP", "LOW BACK PAIN?"],
             "exercise for low back pain", "el ejercicio para el dolor lumbar",
             ("Does exercise help chronic low back pain?", ["Does exercise help", "chronic low back pain?"]),
             ("¿El ejercicio ayuda con el dolor lumbar crónico?", ["¿El ejercicio ayuda con", "el dolor lumbar crónico?"]), icon="heart"),
        stat("COCHRANE REVIEW · 249 TRIALS", "-15", 190, 0.15, "heart", ["points of pain (0–100 scale)", "vs no treatment"],
             [L("A Cochrane review included two hundred forty-nine trials and almost twenty-five thousand adults with chronic non-specific low back pain.",
                "Una revisión Cochrane incluyó 249 ensayos y casi 25.000 adultos con dolor lumbar crónico inespecífico.",
                ["Cochrane: 249 trials, ~24,500 adults", "with chronic low back pain."], ["Cochrane: 249 ensayos, ~24.500 adultos", "con dolor lumbar crónico."]),
              L("Compared with no treatment, exercise reduced pain by about fifteen points on a zero to one hundred scale.",
                "Comparado con no recibir tratamiento, el ejercicio redujo el dolor unos quince puntos en una escala de cero a cien.",
                ["Vs no treatment, exercise cut pain", "~15 points on a 0–100 scale."], ["Vs ningún tratamiento, el ejercicio bajó", "el dolor ~15 puntos en una escala 0–100."]),
              L("The certainty of that evidence was moderate.", "La certeza de esa evidencia fue moderada.",
                ["The certainty of that", "evidence was moderate."], ["La certeza de esa", "evidencia fue moderada."])]),
        tips3("THE LIMITS", ["heart", "flask", "target"],
              [("Pain vs other treatments: ~9 points", "Dolor vs otros tratamientos: ~9 puntos"),
               ("Function vs no treatment: ~7 points", "Función vs sin tratamiento: ~7 puntos"),
               ("Those effects are probably small", "Esos efectos son probablemente pequeños")],
              [L("Against other conservative care, the pain difference was about nine points.", "Frente a otros cuidados conservadores, la diferencia de dolor fue de unos nueve puntos.",
                 ["Vs other conservative care,", "the pain gap was ~9 points."], ["Frente a otros cuidados conservadores,", "la diferencia fue de ~9 puntos."]),
               L("For function, exercise beat no treatment by about seven points.", "En función, el ejercicio superó a no tratar por unos siete puntos.",
                 ["For function, exercise beat", "no treatment by ~7 points."], ["En función, el ejercicio superó", "a no tratar por ~7 puntos."]),
               L("Those effects are probably small. If your pain is severe or lasting, see a doctor.", "Esos efectos son probablemente pequeños. Si tu dolor es fuerte o persistente, consulta a un médico.",
                 ["Probably small effects. If pain is", "severe or lasting, see a doctor."], ["Efectos probablemente pequeños. Si el dolor", "es fuerte o persistente, ve a un médico."])]),
        {"type": "cta", "tail": 1.0, "next_en": "MORE LESSONS COMING", "next_es": "Vienen más lecciones",
         "lines": [L("Save this, and send it to a friend with a sore back.", "Guárdalo y envíaselo a un amigo con dolor de espalda.",
                     ["Save this, and send it to a", "friend with a sore back."], ["Guárdalo y envíaselo a un", "amigo con dolor de espalda."]),
                   L("Follow for one new lesson every day.", "Sígueme para una lección nueva cada día.",
                     ["Follow for one new lesson", "every day."], ["Sígueme para una lección", "nueva cada día."])]},
    ]
    cap = (f"Day 32 teaching you: exercise and low back pain 💪\n"
           f"Does exercise help chronic low back pain? A Cochrane review of 249 trials (24,486 adults with chronic non-specific low back pain) found that, compared with no treatment, exercise reduced pain by about 15 points on a 0–100 scale (35 trials, moderate-certainty evidence). Against other conservative care, the pain difference was about 9 points, and effects on function were about 7 points vs no treatment and 4 vs other care; the authors consider these probably small. If your pain is severe, new, or lasting, see a doctor.\n\n"
           f"Día 32 enseñándote: ejercicio y dolor lumbar 💪\n"
           f"¿El ejercicio ayuda con el dolor lumbar crónico? Una revisión Cochrane de 249 ensayos (24.486 adultos con dolor lumbar crónico inespecífico) halló que, comparado con no recibir tratamiento, el ejercicio redujo el dolor unos 15 puntos en una escala de 0–100 (35 ensayos, evidencia de certeza moderada). Frente a otros cuidados conservadores, la diferencia de dolor fue de ~9 puntos, y los efectos sobre la función fueron de ~7 puntos vs sin tratamiento y 4 vs otros cuidados; los autores los consideran probablemente pequeños. Si tu dolor es fuerte, nuevo o persistente, consulta a un médico.\n\n"
           f"Save this 📌 and follow {handle}. / Guárdalo y sigue a {handle}.\n"
           f"Source / Fuente: Hayden et al., Cochrane Database Syst Rev, 2021.\n"
           f"Educational content, not medical advice. / Contenido educativo, no es consejo médico.")
    return out(32, "back-pain", S, cap, "#lowbackpain #backpain #exercisetherapy #health #fitness", "Hayden et al., Cochrane, 2021")

REELS_MORE4 = {26: reel_protein, 27: reel_timing, 28: reel_hiit, 29: reel_rom, 30: reel_stretch, 31: reel_vilpa, 32: reel_back}
