"""Dias 40-46: tanda 6. Datos verificados contra resumenes/abstracts/notas de prensa el 10/11/2026."""
from reels_more import L, hook, cta, caption
from reels_more2 import tips3
from reels_more3 import stat, out

# ------------------------------------------------------------------ DIA 40
def reel_strength_mort(handle):
    S = [
        hook(40, "forty", "cuarenta", "TEACHING YOU: LIFTING AND LONGEVITY", "Enseñándote: pesas y longevidad", ["DOES LIFTING WEIGHTS", "LINK TO LIVING LONGER?"],
             "strength training and mortality", "el entrenamiento de fuerza y la mortalidad",
             ("Is lifting weights linked to a longer life?", ["Is lifting weights", "linked to a longer life?"]),
             ("¿Levantar pesas se asocia con vivir más?", ["¿Levantar pesas se asocia", "con vivir más?"]), icon="dumbbell"),
        stat("MUSCLE-STRENGTHENING · 16 STUDIES", "10-20%", 130, 0.2, "dumbbell", ["lower risk of death,", "an association"],
             [L("A review pooled sixteen studies that followed people for up to twenty-five years.", "Una revisión reunió 16 estudios que siguieron a personas hasta 25 años.",
                ["16 studies following people", "for up to 25 years."], ["16 estudios que siguieron a personas", "hasta 25 años."]),
              L("Muscle-strengthening activity was linked to a ten to twenty percent lower risk of death from any cause, heart disease and cancer.",
                "La actividad de fuerza se asoció con un diez a veinte por ciento menos de riesgo de muerte por cualquier causa, enfermedad cardíaca y cáncer.",
                ["Linked to 10–20% lower risk of death:", "any cause, heart disease, cancer."], ["Asociada a 10–20 % menos riesgo de muerte:", "cualquier causa, corazón, cáncer."]),
              L("The sweet spot looked like half an hour to an hour a week.", "El punto ideal pareció ser de treinta a sesenta minutos por semana.",
                ["The sweet spot looked like", "30–60 minutes a week."], ["El punto ideal parecía ser", "30–60 minutos por semana."])]),
        tips3("READ THE FINE PRINT", ["dumbbell", "heart", "flask"],
              [("With cardio: 40% lower all-cause risk", "Con aeróbico: 40 % menos riesgo total"),
               ("Training was self-reported", "El entrenamiento fue autorreportado"),
               ("Observational: association, not proof", "Observacional: asociación, no prueba")],
              [L("Combined with aerobic activity, the all-cause risk was forty percent lower.", "Combinado con actividad aeróbica, el riesgo total fue un cuarenta por ciento menor.",
                 ["Combined with aerobic activity,", "all-cause risk was 40% lower."], ["Combinado con aeróbico, el", "riesgo total fue 40 % menor."]),
               L("Training was self-reported, and few studies were pooled for each outcome.", "El entrenamiento fue autorreportado y se reunieron pocos estudios por resultado.",
                 ["Self-reported training, and few", "studies for each outcome."], ["Entrenamiento autorreportado y pocos", "estudios por cada resultado."]),
               L("All were observational studies. That is an association, not proof.", "Todos fueron estudios observacionales. Es una asociación, no una prueba.",
                 ["All observational studies:", "an association, not proof."], ["Todos observacionales:", "una asociación, no una prueba."])]),
        cta(40, "forty-one", "cuarenta y uno", "DAY 41 TOMORROW: PREVENTING FALLS", "Mañana, día 41: prevenir caídas"),
    ]
    cap = caption(40, "lifting and longevity", "pesas y longevidad",
                  "Is lifting weights linked to a longer life? A systematic review and meta-analysis of 16 prospective cohort studies (follow-up up to 25 years) found that muscle-strengthening activity was associated with a 10–20% lower risk of all-cause, cardiovascular and total cancer mortality, with the largest benefit around 30–60 minutes per week and no conclusive extra benefit beyond about an hour. Combined with aerobic activity, risk was about 40% lower for all-cause mortality. Training was self-reported, few studies were pooled per outcome, and all were observational: an association, not proof.",
                  "¿Levantar pesas se asocia con vivir más? Una revisión sistemática y metaanálisis de 16 estudios de cohortes prospectivos (seguimiento de hasta 25 años) halló que la actividad de fortalecimiento muscular se asoció con un 10–20 % menos de riesgo de mortalidad por cualquier causa, cardiovascular y por cáncer, con el mayor beneficio alrededor de 30–60 minutos por semana y sin beneficio extra concluyente más allá de una hora. Combinada con actividad aeróbica, el riesgo fue cerca de un 40 % menor para la mortalidad total. El entrenamiento fue autorreportado, se reunieron pocos estudios por resultado y todos fueron observacionales: una asociación, no una prueba.",
                  handle, "Momma et al., Br J Sports Med, 2022")
    return out(40, "strength-mortality", S, cap, "#strengthtraining #longevity #weightlifting #health #fitness", "Momma et al., Br J Sports Med, 2022")

# ------------------------------------------------------------------ DIA 41
def reel_falls(handle):
    S = [
        hook(41, "forty-one", "cuarenta y uno", "TEACHING YOU: PREVENTING FALLS", "Enseñándote: prevenir caídas", ["CAN EXERCISE", "PREVENT FALLS?"],
             "exercise and falls", "el ejercicio y las caídas",
             ("Can exercise help older adults avoid falls?", ["Can exercise help", "older adults avoid falls?"]),
             ("¿El ejercicio ayuda a los mayores a evitar caídas?", ["¿El ejercicio ayuda a los", "mayores a evitar caídas?"]), icon="walk"),
        stat("COCHRANE REVIEW · 108 TRIALS", "-23%", 150, 0.23, "walk", ["fewer falls with exercise,", "adults living at home"],
             [L("A large review pooled one hundred eight trials with over twenty-three thousand people, average age seventy-six.",
                "Una revisión Cochrane reunió 108 ensayos con más de veintitrés mil personas, de 76 años en promedio.",
                ["108 trials, 23,407 people,", "average age 76."], ["108 ensayos, 23.407 personas,", "edad promedio 76."]),
              L("Exercise lowered the number of falls by about twenty-three percent.", "El ejercicio redujo el número de caídas cerca de un veintitrés por ciento.",
                ["Exercise cut the number of", "falls by about 23%."], ["El ejercicio redujo el número de", "caídas cerca de un 23 %."]),
              L("And the number of people who fell, by about fifteen percent.", "Y el número de personas que se cayeron, cerca de un quince por ciento.",
                ["And the number of people", "who fell, by about 15%."], ["Y el número de personas que", "se cayeron, cerca de un 15 %."])],
             count=(23, "-{:.0f}%")),
        tips3("WHAT THE EVIDENCE SAYS", ["walk", "target", "flask"],
              [("Balance and functional: high certainty", "Equilibrio y funcional: alta certeza"),
               ("Mixed programs: less certain", "Programas mixtos: menos certeza"),
               ("Tai Chi: promising, uncertain", "Tai Chi: prometedor, incierto")],
              [L("Balance and functional exercises had high-certainty evidence for reducing falls.", "Los ejercicios de equilibrio y funcionales tuvieron evidencia de alta certeza para reducir caídas.",
                 ["Balance and functional exercises:", "high-certainty evidence."], ["Ejercicios de equilibrio y funcionales:", "evidencia de alta certeza."]),
               L("Plans mixing balance, functional and resistance work were less certain.", "Los programas que mezclan equilibrio, funcional y fuerza fueron menos seguros.",
                 ["Mixed balance, functional and", "resistance programs: less certain."], ["Mezcla de equilibrio, funcional y", "fuerza: menos certeza."]),
               L("Tai Chi may help, but the evidence is uncertain. Ask a professional to design a program.", "El Tai Chi puede ayudar, pero la evidencia es incierta. Pide a un profesional que diseñe un programa.",
                 ["Tai Chi may help: uncertain.", "Ask a professional for a program."], ["Tai Chi puede ayudar: incierto.", "Pide un programa a un profesional."])]),
        cta(41, "forty-two", "cuarenta y dos", "DAY 42 TOMORROW: LIFTING INJURIES", "Mañana, día 42: lesiones al levantar"),
    ]
    cap = caption(41, "exercise and falls", "ejercicio y caídas",
                  "Can exercise help older adults avoid falls? A Cochrane review of 108 randomized trials (23,407 participants, average age 76, living in the community) found that exercise reduced the rate of falls by about 23% and the number of people who fell by about 15%. Balance and functional exercises had high-certainty evidence; multi-category programs were less certain; Tai Chi may help but the evidence is uncertain. Side effects were poorly reported and usually not serious. Evidence for fewer fractures is less certain. If you are older or at risk of falling, ask a professional to design your program.",
                  "¿El ejercicio ayuda a los mayores a evitar caídas? Una revisión Cochrane de 108 ensayos aleatorizados (23.407 participantes, edad promedio 76 años, viviendo en la comunidad) halló que el ejercicio redujo la tasa de caídas cerca de un 23 % y el número de personas que se cayeron cerca de un 15 %. Los ejercicios de equilibrio y funcionales tuvieron evidencia de alta certeza; los programas multicategoría, menos certeza; el Tai Chi puede ayudar, pero la evidencia es incierta. Los efectos adversos se reportaron poco y no solían ser graves. La evidencia sobre menos fracturas es menos segura. Si eres mayor o tienes riesgo de caídas, pide a un profesional que diseñe tu programa.",
                  handle, "Sherrington et al., Cochrane Database Syst Rev, 2019")
    return out(41, "falls", S, cap, "#balance #falls #healthyaging #mobility #fitness", "Sherrington et al., Cochrane, 2019")

# ------------------------------------------------------------------ DIA 42
def reel_injuries(handle):
    S = [
        hook(42, "forty-two", "cuarenta y dos", "TEACHING YOU: LIFTING INJURIES", "Enseñándote: lesiones al levantar", ["IS LIFTING", "DANGEROUS?"],
             "injury risk in lifting sports", "las lesiones al levantar pesas",
             ("How often do lifters actually get injured?", ["How often do lifters", "actually get injured?"]),
             ("¿Con qué frecuencia se lesionan los que levantan?", ["¿Con qué frecuencia se lesionan", "los que levantan?"]), icon="check"),
        stat("INJURIES PER 1,000 HOURS", "2-4", 190, 0.3, "check", ["in most weight-training", "sports (approximate)"],
             [L("A review of injury studies in lifting sports found about two to four injury cases per thousand hours in most of them.",
                "Una revisión de estudios de lesiones en deportes de pesas halló cerca de dos a cuatro lesiones por mil horas en la mayoría.",
                ["Most lifting sports: about 2–4", "injuries per 1,000 hours."], ["La mayoría: cerca de 2–4", "lesiones por 1.000 horas."]),
              L("The authors call that low compared with common team sports.", "Los autores lo consideran bajo comparado con deportes de equipo comunes.",
                ["The authors call that low vs", "common team sports."], ["Los autores lo ven bajo frente a", "deportes de equipo comunes."]),
              L("But most studies looked back in time, so treat the numbers as approximate.", "Pero la mayoría de los estudios miraron hacia atrás, así que toma los números como aproximados.",
                ["Most studies looked back in time:", "numbers are approximate."], ["La mayoría miró hacia atrás:", "números aproximados."])]),
        tips3("WHERE AND HOW OFTEN", ["check", "target", "dumbbell"],
              [("Bodybuilding: lowest, 0.24–1", "Fisicoculturismo: el más bajo, 0,24–1"),
               ("Strongman: highest, 4.5–6.1", "Strongman: el más alto, 4,5–6,1"),
               ("Shoulder, low back, knee: common", "Hombro, espalda baja, rodilla: comunes")],
              [L("Bodybuilding had the lowest rate, from point two four to one per thousand hours.", "El fisicoculturismo tuvo la tasa más baja, de 0,24 a 1 por mil horas.",
                 ["Bodybuilding: lowest rate,", "0.24–1 per 1,000 hours."], ["Fisicoculturismo: la tasa más baja,", "0,24–1 por 1.000 horas."]),
               L("Strongman had a higher rate, from four point five to six point one.", "Strongman tuvo una tasa mayor, de 4,5 a 6,1.",
                 ["Strongman: higher rate,", "4.5–6.1 per 1,000 hours."], ["Strongman: tasa mayor,", "4,5–6,1 por 1.000 horas."]),
               L("The shoulder, lower back and knee were among the most commonly injured areas.", "El hombro, la espalda baja y la rodilla estuvieron entre las zonas más lesionadas.",
                 ["Shoulder, lower back and knee were", "among the most injured areas."], ["Hombro, espalda baja y rodilla: entre", "las zonas más lesionadas."])]),
        cta(42, "forty-three", "cuarenta y tres", "DAY 43 TOMORROW: EXERCISE AND SLEEP", "Mañana, día 43: ejercicio y sueño"),
    ]
    cap = caption(42, "lifting injuries", "lesiones al levantar",
                  "Is lifting dangerous? A systematic review of injury studies across the weight-training sports found most had roughly 2–4 injuries per 1,000 hours of training or competition, which the authors describe as relatively low compared with common team sports. Bodybuilding had the lowest rate (about 0.24–1 per 1,000 h) and strongman among the highest (about 4.5–6.1). The shoulder, lower back, knee, elbow and wrist/hand were generally the most commonly injured areas; strains, tendinitis and sprains were the most common types. Most studies were retrospective, so the numbers are approximate.",
                  "¿Levantar pesas es peligroso? Una revisión sistemática de estudios de lesiones en los deportes de pesas halló que la mayoría tenía cerca de 2–4 lesiones por 1.000 horas de entrenamiento o competencia, lo que los autores describen como relativamente bajo frente a los deportes de equipo comunes. El fisicoculturismo tuvo la tasa más baja (cerca de 0,24–1 por 1.000 h) y el strongman, de las más altas (cerca de 4,5–6,1). El hombro, la espalda baja, la rodilla, el codo y la muñeca/mano fueron en general las zonas más lesionadas; los esguinces, tendinitis y distensiones fueron los tipos más comunes. La mayoría de los estudios fue retrospectiva, así que los números son aproximados.",
                  handle, "Keogh & Winwood, Sports Med, 2017")
    return out(42, "injuries", S, cap, "#weightlifting #injuryprevention #gym #strengthtraining #fitness", "Keogh & Winwood, Sports Med, 2017")

# ------------------------------------------------------------------ DIA 43
def reel_sleep(handle):
    S = [
        hook(43, "forty-three", "cuarenta y tres", "TEACHING YOU: EXERCISE AND SLEEP", "Enseñándote: ejercicio y sueño", ["DOES EXERCISE", "HELP YOU SLEEP?"],
             "exercise and sleep", "el ejercicio y el sueño",
             ("Does working out help you sleep better?", ["Does working out", "help you sleep better?"]),
             ("¿Entrenar te ayuda a dormir mejor?", ["¿Entrenar te ayuda", "a dormir mejor?"]), icon="moon"),
        stat("EXERCISE AND SLEEP · META-ANALYSIS", "66", 190, 0.5, "moon", ["studies reviewed,", "published through 2013"],
             [L("A meta-analysis pooled sixty-six studies on exercise and sleep.", "Un metaanálisis reunió 66 estudios sobre ejercicio y sueño.",
                ["66 studies on exercise", "and sleep."], ["66 estudios sobre ejercicio", "y sueño."]),
              L("A single workout had a small benefit for total sleep time and sleep efficiency.", "Un solo entrenamiento tuvo beneficios pequeños en el tiempo total de sueño y la eficiencia del sueño.",
                ["One workout: small benefits for", "total sleep time and efficiency."], ["Un entrenamiento: beneficios pequeños en", "tiempo total y eficiencia del sueño."]),
              L("And a moderate benefit on time awake during the night.", "Y un beneficio moderado en el tiempo despierto durante la noche.",
                ["And a moderate benefit on", "time awake at night."], ["Y un beneficio moderado en el", "tiempo despierto de noche."])],
             count=(66, "{:.0f}")),
        tips3("REGULAR EXERCISE", ["moon", "calendar", "flask"],
              [("Sleep quality: moderate benefit", "Calidad del sueño: beneficio moderado"),
               ("Intensity was not a key factor", "La intensidad no fue un factor clave"),
               ("Not a cure: insomnia? Ask a doctor", "No es una cura: ¿insomnio? Consulta al médico")],
              [L("Regular exercise had a moderate benefit on sleep quality.", "El ejercicio regular tuvo un beneficio moderado en la calidad del sueño.",
                 ["Regular exercise: a moderate", "benefit on sleep quality."], ["Ejercicio regular: beneficio moderado", "en la calidad del sueño."]),
               L("Intensity was not a significant moderator, but sex, age, timing and adherence were.", "La intensidad no fue un moderador significativo, pero sí el sexo, la edad, el horario y la constancia.",
                 ["Intensity did not matter much; sex,", "age, timing and adherence did."], ["La intensidad no importó mucho; sí", "sexo, edad, horario y constancia."]),
               L("The effect was small to moderate. If you have insomnia, ask your doctor.", "Los efectos fueron de pequeños a moderados. Si tienes insomnio, consulta a tu médico.",
                 ["Small to moderate effects. With", "insomnia, ask your doctor."], ["Efectos de pequeños a moderados. Con", "insomnio, consulta a tu médico."])]),
        cta(43, "forty-four", "cuarenta y cuatro", "DAY 44 TOMORROW: WEEKEND WARRIORS", "Mañana, día 44: guerreros de fin de semana"),
    ]
    cap = caption(43, "exercise and sleep", "ejercicio y sueño",
                  "Does working out help you sleep better? A meta-analytic review of 66 studies (published through May 2013) found that a single workout had small beneficial effects on total sleep time, sleep onset latency, sleep efficiency and slow-wave sleep, and a moderate beneficial effect on wake time after sleep onset. Regular exercise had small benefits for total sleep time and sleep efficiency, small-to-medium for sleep onset latency, and a moderate benefit for sleep quality. Effects were moderated by sex, age, baseline activity, exercise type, time of day, duration and adherence; intensity was not a significant moderator. If you have insomnia, ask your doctor.",
                  "¿Entrenar te ayuda a dormir mejor? Una revisión metaanalítica de 66 estudios (publicados hasta mayo de 2013) halló que un solo entrenamiento tuvo efectos beneficiosos pequeños en el tiempo total de sueño, la latencia de inicio, la eficiencia y el sueño de ondas lentas, y un efecto beneficioso moderado en el tiempo despierto tras iniciar el sueño. El ejercicio regular tuvo beneficios pequeños en el tiempo total de sueño y la eficiencia, de pequeños a medianos en la latencia de inicio y moderado en la calidad del sueño. Los efectos variaron según sexo, edad, actividad basal, tipo de ejercicio, hora del día, duración y constancia; la intensidad no fue un moderador significativo. Si tienes insomnio, consulta a tu médico.",
                  handle, "Kredlow et al., J Behav Med, 2015")
    return out(43, "sleep-exercise", S, cap, "#sleep #sleepbetter #exercise #recovery #fitness", "Kredlow et al., J Behav Med, 2015")

# ------------------------------------------------------------------ DIA 44
def reel_weekend(handle):
    S = [
        hook(44, "forty-four", "cuarenta y cuatro", "TEACHING YOU: WEEKEND WARRIORS", "Enseñándote: guerreros de fin de semana", ["ONLY TRAIN", "ON WEEKENDS?"],
             "weekend training", "los guerreros de fin de semana",
             ("Does training only on the weekend still count?", ["Does training only on", "the weekend still count?"]),
             ("¿Entrenar solo el fin de semana sirve igual?", ["¿Entrenar solo el fin de", "semana sirve igual?"]), icon="calendar"),
        stat("WEEKEND WARRIORS VS INACTIVE", "-30%", 150, 0.3, "calendar", ["lower risk of death,", "63,591 adults"],
             [L("A study followed sixty-three thousand five hundred ninety-one adults in England and Scotland.", "Un estudio siguió a 63.591 adultos en Inglaterra y Escocia.",
                ["63,591 adults in", "England and Scotland."], ["63.591 adultos en", "Inglaterra y Escocia."]),
              L("People who got the recommended activity in one or two sessions a week had about thirty percent lower risk of death than inactive people.",
                "Quienes lograron la actividad recomendada en una o dos sesiones por semana tuvieron cerca de un treinta por ciento menos de riesgo de muerte que los inactivos.",
                ["Recommended activity in 1–2 sessions:", "about 30% lower risk of death."], ["Actividad recomendada en 1–2 sesiones:", "cerca de 30 % menos riesgo de muerte."]),
              L("Heart disease deaths were about forty percent lower, and cancer deaths about eighteen.", "Las muertes por enfermedad cardíaca fueron cerca de un cuarenta por ciento menores, y las de cáncer, cerca de un dieciocho.",
                ["Heart disease deaths: about 40%", "lower. Cancer: about 18% lower."], ["Muertes cardíacas: cerca de 40 %", "menos. Cáncer: cerca de 18 % menos."])],
             count=(30, "-{:.0f}%")),
        tips3("READ THE FINE PRINT", ["calendar", "flask", "check"],
              [("Activity was self-reported", "La actividad fue autorreportada"),
               ("Over 90% white: may not generalize", "Más del 90 % blancos: puede no generalizarse"),
               ("Association, not proof", "Asociación, no prueba")],
              [L("Physical activity was self-reported.", "La actividad física fue autorreportada.", ["Physical activity was", "self-reported."], ["La actividad física fue", "autorreportada."]),
               L("Over ninety percent of the people were white, so the findings may not apply to everyone.", "Más del noventa por ciento de los participantes eran blancos, así que los resultados pueden no aplicarse a todos.",
                 ["Over 90% were white, so it may", "not apply to everyone."], ["Más del 90 % eran blancos: puede", "no aplicarse a todos."]),
               L("It cannot show cause and effect. Ease in gradually if you are not used to exercise.", "No puede demostrar causa y efecto. Empieza de a poco si no estás acostumbrado al ejercicio.",
                 ["It cannot show cause and effect.", "Ease in gradually."], ["No demuestra causa y efecto.", "Empieza de a poco."])]),
        cta(44, "forty-five", "cuarenta y cinco", "DAY 45 TOMORROW: WEIGHTS AND ANXIETY", "Mañana, día 45: pesas y ansiedad"),
    ]
    cap = caption(44, "weekend warriors", "guerreros de fin de semana",
                  "Does training only on weekends still count? A study of 63,591 adults in England and Scotland (surveys from 1994 to 2012) found that “weekend warriors”, who got the recommended amount of activity in one or two sessions a week, had about 30% lower risk of death from any cause, about 40% lower from cardiovascular disease and about 18% lower from cancer than inactive adults. Activity was self-reported, over 90% of participants were white, and the study cannot show cause and effect: an association, not proof. If you are not used to exercise, build up gradually.",
                  "¿Entrenar solo el fin de semana sirve igual? Un estudio de 63.591 adultos en Inglaterra y Escocia (encuestas de 1994 a 2012) halló que los “guerreros de fin de semana”, que lograron la actividad recomendada en una o dos sesiones por semana, tuvieron cerca de un 30 % menos de riesgo de muerte por cualquier causa, cerca de un 40 % menos por enfermedad cardiovascular y cerca de un 18 % menos por cáncer que los adultos inactivos. La actividad fue autorreportada, más del 90 % de los participantes eran blancos y el estudio no puede demostrar causa y efecto: una asociación, no una prueba. Si no estás acostumbrado al ejercicio, avanza de a poco.",
                  handle, "O'Donovan et al., JAMA Intern Med, 2017")
    return out(44, "weekend-warrior", S, cap, "#weekendwarrior #exercise #health #consistency #fitness", "O'Donovan et al., JAMA Intern Med, 2017")

# ------------------------------------------------------------------ DIA 45
def reel_anxiety(handle):
    S = [
        hook(45, "forty-five", "cuarenta y cinco", "TEACHING YOU: WEIGHTS AND ANXIETY", "Enseñándote: pesas y ansiedad", ["CAN LIFTING", "EASE ANXIETY?"],
             "resistance training and anxiety", "el entrenamiento de fuerza y la ansiedad",
             ("Can lifting weights reduce anxiety symptoms?", ["Can lifting weights", "reduce anxiety symptoms?"]),
             ("¿Levantar pesas puede reducir los síntomas de ansiedad?", ["¿Levantar pesas puede reducir", "los síntomas de ansiedad?"]), icon="heart"),
        stat("RESISTANCE TRAINING · META-ANALYSIS", "16", 190, 0.4, "heart", ["trials, 922 participants,", "anxiety symptoms"],
             [L("A meta-analysis pooled sixteen studies with nine hundred twenty-two people.", "Un metaanálisis reunió 16 estudios con 922 participantes.",
                ["16 studies with", "922 participants."], ["16 estudios con", "922 participantes."]),
              L("Resistance training lowered anxiety symptoms, a small but significant effect.", "El entrenamiento de fuerza redujo los síntomas de ansiedad, un efecto pequeño pero significativo.",
                ["Weights reduced anxiety symptoms:", "a small but significant effect."], ["Las pesas redujeron la ansiedad:", "un efecto pequeño pero significativo."]),
              L("Training frequency and intensity did not significantly change the result.", "La frecuencia y la intensidad del entrenamiento no cambiaron significativamente el resultado.",
                ["Frequency and intensity did not", "significantly change it."], ["La frecuencia y la intensidad no", "lo cambiaron significativamente."])],
             count=(16, "{:.0f}")),
        tips3("WHO BENEFITED", ["heart", "dumbbell", "check"],
              [("Healthy people: effect 0.50", "Personas sanas: efecto 0,50"),
               ("People with illness: effect 0.19", "Personas con enfermedad: efecto 0,19"),
               ("Not a replacement for treatment", "No reemplaza un tratamiento")],
              [L("Healthy people showed a bigger effect, about point five.", "Las personas sanas mostraron un efecto mayor, cerca de 0,5.",
                 ["Healthy people showed a", "bigger effect: about 0.50."], ["Personas sanas: un efecto", "mayor, cerca de 0,50."]),
               L("People with a physical or mental illness showed a smaller one, about point one nine.", "Las personas con una enfermedad física o mental mostraron uno menor, cerca de 0,19.",
                 ["People with an illness: smaller,", "about 0.19."], ["Personas con enfermedad: menor,", "cerca de 0,19."]),
               L("It is not a replacement for treatment. If anxiety affects your life, talk to a professional.", "No reemplaza un tratamiento. Si la ansiedad afecta tu vida, habla con un profesional.",
                 ["Not a replacement for treatment.", "Anxious? Talk to a professional."], ["No reemplaza un tratamiento.", "¿Ansiedad? Habla con un profesional."])]),
        cta(45, "forty-six", "cuarenta y seis", "DAY 46 TOMORROW: WALKING PACE", "Mañana, día 46: ritmo al caminar"),
    ]
    cap = caption(45, "weights and anxiety", "pesas y ansiedad",
                  "Can lifting weights reduce anxiety symptoms? A meta-analysis of 16 articles (31 effects, 922 participants) found that resistance exercise training significantly reduced anxiety symptoms (Hedges' g = 0.31, 95% CI 0.17–0.44). The effect was larger in healthy participants (0.50) than in those with a physical or mental illness (0.19), and training frequency and intensity were not significant moderators. Resistance training is not a replacement for treatment: if anxiety affects your daily life, talk to a health professional.",
                  "¿Levantar pesas puede reducir los síntomas de ansiedad? Un metaanálisis de 16 artículos (31 efectos, 922 participantes) halló que el entrenamiento de fuerza redujo significativamente los síntomas de ansiedad (g de Hedges = 0,31; IC 95 % 0,17–0,44). El efecto fue mayor en participantes sanos (0,50) que en quienes tenían una enfermedad física o mental (0,19), y la frecuencia y la intensidad no fueron moderadores significativos. El entrenamiento de fuerza no reemplaza un tratamiento: si la ansiedad afecta tu vida diaria, habla con un profesional de la salud.",
                  handle, "Gordon et al., Sports Med, 2017")
    return out(45, "anxiety", S, cap, "#mentalhealth #anxiety #strengthtraining #wellbeing #fitness", "Gordon et al., Sports Med, 2017")

# ------------------------------------------------------------------ DIA 46
def reel_pace(handle):
    S = [
        hook(46, "forty-six", "cuarenta y seis", "TEACHING YOU: WALKING PACE", "Enseñándote: ritmo al caminar", ["DOES HOW FAST YOU WALK", "MATTER?"],
             "walking pace", "el ritmo al caminar",
             ("Does walking faster change your health risk?", ["Does walking faster", "change your health risk?"]),
             ("¿Caminar más rápido cambia tu riesgo de salud?", ["¿Caminar más rápido cambia", "tu riesgo de salud?"]), icon="walk"),
        {"type": "vs", "tail": 0.7, "head": "LOWER RISK OF DEATH VS SLOW WALKERS", "sub": "about 50,000 walkers · 11 cohorts",
         "rows": [{"title": "Average pace", "sub": "all-cause", "es": "Ritmo promedio", "val": 20, "fmt": "-{:.0f}%"},
                  {"title": "Brisk / fast", "sub": "all-cause", "es": "Rápido", "val": 24, "fmt": "-{:.0f}%", "win": True}],
         "lines": [L("A study pooled data from about fifty thousand walkers in eleven British groups.",
                     "Un estudio reunió datos de cerca de cincuenta mil caminantes en once cohortes británicas.",
                     ["About 50,000 walkers in", "11 British cohorts."], ["Cerca de 50.000 caminantes en", "11 cohortes británicas."]),
                   L("Compared with slow walkers, an average pace had twenty percent lower risk of death, and a brisk pace twenty-four percent.",
                     "Frente a los caminantes lentos, un ritmo promedio tuvo un veinte por ciento menos de riesgo de muerte, y un ritmo rápido, un veinticuatro por ciento.",
                     ["Vs slow walkers: average pace -20%", "risk of death, brisk pace -24%."], ["Vs lentos: ritmo promedio -20 %", "riesgo de muerte, rápido -24 %."]),
                   L("Pace was reported by the walkers themselves, so this is an association, not proof.",
                     "El ritmo fue autoevaluado, así que es una asociación, no una prueba.",
                     ["Pace was self-rated: an", "association, not proof."], ["Ritmo autoevaluado: una", "asociación, no una prueba."])]},
        tips3("READ THE FINE PRINT", ["walk", "flask", "check"],
              [("Over 60: heart risk -46% to -53%", "Mayores de 60: riesgo cardíaco -46 % a -53 %"),
               ("Fast is about 5–7 km/h, by fitness", "Rápido: unos 5–7 km/h, según tu forma"),
               ("No clear effect on cancer deaths", "Sin efecto claro en muertes por cáncer")],
              [L("Among walkers over sixty, heart disease death risk was forty-six to fifty-three percent lower.", "Entre caminantes mayores de sesenta, el riesgo de muerte cardíaca fue de un cuarenta y seis a un cincuenta y tres por ciento menor.",
                 ["Walkers over 60: heart disease", "death risk 46–53% lower."], ["Mayores de 60: riesgo de muerte", "cardíaca 46–53 % menor."]),
               L("Fast is roughly five to seven kilometer per hour, depending on your fitness.", "Rápido es aproximadamente de cinco a siete kilómetros por hora, según tu condición.",
                 ["Fast is roughly 5–7 km/h,", "depending on your fitness."], ["Rápido es de 5–7 km/h", "según tu condición."]),
               L("No significant effect of pace was found for cancer deaths.", "No se halló un efecto significativo del ritmo en las muertes por cáncer.",
                 ["No significant effect of pace", "on cancer deaths."], ["Sin efecto significativo del", "ritmo en muertes por cáncer."])]),
        {"type": "cta", "tail": 1.0, "next_en": "MORE LESSONS COMING", "next_es": "Vienen más lecciones",
         "lines": [L("Save this, and send it to a friend who loves walking.", "Guárdalo y envíaselo a un amigo que ame caminar.",
                     ["Save this, and send it to a", "friend who loves walking."], ["Guárdalo y envíaselo a un", "amigo que ame caminar."]),
                   L("Follow for one new lesson every day.", "Sígueme para una lección nueva cada día.",
                     ["Follow for one new lesson", "every day."], ["Sígueme para una lección", "nueva cada día."])]},
    ]
    cap = (f"Day 46 teaching you: walking pace 💪\n"
           f"Does walking faster change your health risk? A pooled analysis of about 50,000 walkers in 11 British cohorts found that, compared with slow walkers, an average pace was associated with about 20% lower risk of all-cause death and a brisk or fast pace with about 24% lower; for cardiovascular death the figures were about 24% and 21%. Among walkers aged 60+, cardiovascular death risk was about 46% (average) and 53% (fast) lower. Pace was self-rated, “fast” is roughly 5–7 km/h depending on fitness, no significant effect was found for cancer deaths, and these are associations, not proof.\n\n"
           f"Día 46 enseñándote: ritmo al caminar 💪\n"
           f"¿Caminar más rápido cambia tu riesgo de salud? Un análisis agrupado de unos 50.000 caminantes de 11 cohortes británicas halló que, frente a los caminantes lentos, un ritmo promedio se asoció con cerca de un 20 % menos de riesgo de muerte por cualquier causa y un ritmo rápido con cerca de un 24 % menos; para la muerte cardiovascular, las cifras fueron cerca de 24 % y 21 %. En mayores de 60, el riesgo de muerte cardiovascular fue cerca de 46 % (promedio) y 53 % (rápido) menor. El ritmo fue autoevaluado, “rápido” es de unos 5–7 km/h según tu condición, no hubo efecto significativo en muertes por cáncer y son asociaciones, no pruebas.\n\n"
           f"Save this 📌 and follow {handle}. / Guárdalo y sigue a {handle}.\n"
           f"Source / Fuente: Stamatakis et al., Mayo Clin Proc, 2018.\n"
           f"Educational content, not medical advice. / Contenido educativo, no es consejo médico.")
    return out(46, "walking-pace", S, cap, "#walking #health #longevity #cardio #fitness", "Stamatakis et al., Mayo Clin Proc, 2018")

REELS_MORE6 = {40: reel_strength_mort, 41: reel_falls, 42: reel_injuries, 43: reel_sleep, 44: reel_weekend, 45: reel_anxiety, 46: reel_pace}
