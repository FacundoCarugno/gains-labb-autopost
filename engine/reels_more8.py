"""Dias 54-60: tanda 8. Datos verificados contra resumenes/notas de prensa el 25/11/2026."""
from reels_more import L, hook, cta, caption
from reels_more2 import tips3
from reels_more3 import stat, out

# ------------------------------------------------------------------ DIA 54
def reel_fitness(handle):
    S = [
        hook(54, "fifty-four", "cincuenta y cuatro", "TEACHING YOU: FITNESS AND LIFESPAN", "Enseñándote: forma física y vida", ["DOES FITNESS", "PREDICT LIFESPAN?"],
             "fitness and long-term survival", "la forma física y la supervivencia",
             ("How much does fitness change your risk of dying?", ["How much does fitness change", "your risk of dying?"]),
             ("¿Cuánto cambia tu riesgo de morir tu forma física?", ["¿Cuánto cambia tu riesgo de morir", "tu forma física?"]), icon="heart"),
        stat("TREADMILL TEST · 122,007 PEOPLE", "-80%", 150, 0.8, "heart", ["lower risk of death,", "elite vs low fitness"],
             [L("A study followed one hundred twenty-two thousand people who took a treadmill fitness test.", "Un estudio siguió a 122.007 personas que hicieron una prueba de esfuerzo en cinta.",
                ["122,007 people who took a", "treadmill fitness test."], ["122.007 personas que hicieron una", "prueba de esfuerzo en cinta."]),
              L("Those with elite fitness had about eighty percent lower risk of death than those with low fitness.", "Quienes tenían una forma física de élite tuvieron cerca de un 80 por ciento menos de riesgo de muerte que quienes tenían forma física baja.",
                ["Elite fitness: about 80% lower", "risk of death than low fitness."], ["Forma de élite: cerca de 80 % menos", "riesgo de muerte que forma baja."]),
              L("More fitness meant lower risk at every step, and the authors found no upper limit.", "Más forma física significó menos riesgo en cada escalón, y los autores no hallaron un límite superior.",
                ["More fitness, lower risk at every", "step. No upper limit found."], ["Más forma física, menos riesgo en cada", "escalón. Sin límite superior."])],
             count=(80, "-{:.0f}%")),
        tips3("READ THE FINE PRINT", ["heart", "target", "flask"],
              [("Low fitness: risk like smoking or diabetes", "Forma baja: riesgo como fumar o diabetes"),
               ("Elite = top 2.5% for age and sex", "Élite = el 2,5 % superior por edad y sexo"),
               ("Retrospective: association, not proof", "Retrospectivo: asociación, no prueba")],
              [L("Low fitness carried a risk comparable to, or greater than, smoking or diabetes.", "La forma física baja tuvo un riesgo comparable o mayor que fumar o la diabetes.",
                 ["Low fitness: a risk like, or", "above, smoking or diabetes."], ["Forma baja: un riesgo como, o mayor", "que, fumar o la diabetes."]),
               L("Elite meant the top two and a half percent for your age and sex.", "Élite significaba el dos y medio por ciento superior para tu edad y sexo.",
                 ["Elite means the top 2.5%", "for your age and sex."], ["Élite significa el 2,5 % superior", "para tu edad y sexo."]),
               L("It was retrospective and observational: an association, not proof.", "Fue retrospectivo y observacional: una asociación, no una prueba.",
                 ["Retrospective and observational:", "an association, not proof."], ["Retrospectivo y observacional:", "una asociación, no una prueba."])]),
        cta(54, "fifty-five", "cincuenta y cinco", "DAY 55 TOMORROW: EXERCISE AND COLDS", "Mañana, día 55: ejercicio y resfríos"),
    ]
    cap = caption(54, "fitness and lifespan", "forma física y vida",
                  "How much does fitness change your risk of dying? A study of 122,007 patients who had treadmill exercise testing at Cleveland Clinic (1991–2014) found that higher cardiorespiratory fitness was associated with lower long-term mortality at every level: elite performers (top 2.5% for age and sex) had about 80% lower risk of death than those with low fitness, and the authors found no upper limit to the benefit. Low fitness carried a risk comparable to or greater than traditional risk factors such as smoking and diabetes. The study was retrospective and observational, so it shows an association, not proof. Check with your doctor before starting a new exercise program.",
                  "¿Cuánto cambia tu riesgo de morir tu forma física? Un estudio de 122.007 pacientes que hicieron una prueba de esfuerzo en cinta en Cleveland Clinic (1991–2014) halló que una mayor aptitud cardiorrespiratoria se asoció con menor mortalidad a largo plazo en todos los niveles: los de élite (el 2,5 % superior por edad y sexo) tuvieron cerca de un 80 % menos de riesgo de muerte que quienes tenían forma física baja, y los autores no hallaron un límite superior al beneficio. La forma física baja tuvo un riesgo comparable o mayor que factores tradicionales como fumar y la diabetes. El estudio fue retrospectivo y observacional, así que muestra una asociación, no una prueba. Consulta con tu médico antes de empezar un programa nuevo.",
                  handle, "Mandsager et al., JAMA Netw Open, 2018")
    return out(54, "fitness-lifespan", S, cap, "#cardiofitness #longevity #health #cardio #fitness", "Mandsager et al., JAMA Netw Open, 2018")

# ------------------------------------------------------------------ DIA 55
def reel_colds(handle):
    S = [
        hook(55, "fifty-five", "cincuenta y cinco", "TEACHING YOU: EXERCISE AND COLDS", "Enseñándote: ejercicio y resfríos", ["CAN EXERCISE", "FEND OFF COLDS?"],
             "exercise and colds", "el ejercicio y los resfríos",
             ("Do people who exercise get fewer colds?", ["Do people who exercise", "get fewer colds?"]),
             ("¿Quienes entrenan se resfrían menos?", ["¿Quienes entrenan", "se resfrían menos?"]), icon="flask"),
        stat("COLD SYMPTOM DAYS · ABOUT 1,000 ADULTS", "43-46%", 120, 0.45, "flask", ["fewer days with cold symptoms", "in the most active and fit"],
             [L("A study followed about one thousand adults through twelve weeks of autumn and winter.", "Un estudio siguió a cerca de mil adultos durante doce semanas de otoño e invierno.",
                ["About 1,000 adults through", "12 weeks of autumn and winter."], ["Cerca de 1.000 adultos durante", "12 semanas de otoño e invierno."]),
              L("Adults who exercised five or more days a week, and felt fit, had forty-three to forty-six percent fewer days with cold symptoms.",
                "Los adultos que entrenaban cinco o más días por semana, y se sentían en forma, tuvieron entre un 43 y un 46 por ciento menos de días con síntomas de resfrío.",
                ["Exercise 5+ days a week and feeling fit:", "43–46% fewer days with cold symptoms."], ["Entrenar 5+ días por semana y sentirse en forma:", "43–46 % menos días con síntomas."]),
              L("Their symptoms were also milder, thirty-one to forty-one percent less severe.", "Sus síntomas también fueron más leves, entre un 31 y un 41 por ciento menos graves.",
                ["Symptoms were also milder:", "31–41% less severe."], ["Los síntomas también fueron más leves:", "31–41 % menos graves."])]),
        tips3("READ THE FINE PRINT", ["flask", "calendar", "check"],
              [("Exercise and fitness were self-reported", "Ejercicio y forma física autorreportados"),
               ("One autumn and winter only", "Solo un otoño e invierno"),
               ("A link, not a cure", "Una asociación, no una cura")],
              [L("People reported their own exercise and scored their own fitness.", "Las personas reportaron su propio ejercicio y calificaron su propia forma física.",
                 ["People reported their own exercise", "and rated their own fitness."], ["Las personas reportaron su ejercicio", "y calificaron su forma física."]),
               L("Data came from a single autumn and winter season.", "Los datos vinieron de una sola temporada de otoño e invierno.",
                 ["Data came from a single", "autumn and winter."], ["Los datos vinieron de un solo", "otoño e invierno."]),
               L("This is a link, not proof that exercise protects you from colds. See a doctor if you feel ill.", "Es una asociación, no prueba de que el ejercicio prevenga resfríos. Consulta a un médico si te sientes mal.",
                 ["A link, not proof that exercise", "prevents colds. Feeling ill? See a doctor."], ["Una asociación, no prueba de que el", "ejercicio prevenga resfríos. ¿Mal? Ve al médico."])]),
        cta(55, "fifty-six", "cincuenta y seis", "DAY 56 TOMORROW: ACTIVITY AND CANCER", "Mañana, día 56: actividad y cáncer"),
    ]
    cap = caption(55, "exercise and colds", "ejercicio y resfríos",
                  "Do people who exercise get fewer colds? A study of about 1,000 adults (aged 18–85) followed for 12 weeks in autumn and winter found that those who exercised aerobically on 5 or more days a week, and those who rated themselves as fit, had about 43–46% fewer days with upper respiratory infection symptoms than those who exercised one day a week or less. Symptom severity was also lower, by about 31–41%. Exercise and fitness were self-reported and data came from a single season: an association, not proof. If you feel ill, see a doctor.",
                  "¿Quienes entrenan se resfrían menos? Un estudio de unos 1.000 adultos (de 18 a 85 años) seguidos durante 12 semanas de otoño e invierno halló que quienes hacían ejercicio aeróbico 5 o más días por semana, y quienes se calificaban como en forma, tuvieron cerca de un 43–46 % menos de días con síntomas de infección respiratoria superior que quienes entrenaban un día por semana o menos. La gravedad de los síntomas también fue menor, cerca de un 31–41 %. El ejercicio y la forma física fueron autorreportados y los datos vienen de una sola temporada: una asociación, no una prueba. Si te sientes mal, consulta a un médico.",
                  handle, "Nieman et al., Br J Sports Med, 2011")
    return out(55, "colds", S, cap, "#immunity #coldseason #exercise #health #fitness", "Nieman et al., Br J Sports Med, 2011")

# ------------------------------------------------------------------ DIA 56
def reel_cancer(handle):
    S = [
        hook(56, "fifty-six", "cincuenta y seis", "TEACHING YOU: ACTIVITY AND CANCER", "Enseñándote: actividad y cáncer", ["CAN BEING ACTIVE", "LOWER CANCER RISK?"],
             "physical activity and cancer", "la actividad física y el cáncer",
             ("Is being more active linked to lower cancer risk?", ["Is being more active linked", "to lower cancer risk?"]),
             ("¿Estar más activo se asocia con menos riesgo de cáncer?", ["¿Estar más activo se asocia", "con menos riesgo de cáncer?"]), icon="target"),
        stat("LEISURE ACTIVITY · 1.44 MILLION ADULTS", "13", 190, 0.5, "target", ["of 26 cancer types", "lower with more activity"],
             [L("A pooled analysis followed one point four four million adults for a median of eleven years.", "Un análisis conjunto siguió a 1,44 millones de adultos durante una mediana de 11 años.",
                ["1.44 million adults,", "median follow-up 11 years."], ["1,44 millones de adultos,", "seguimiento mediano de 11 años."]),
              L("More leisure-time activity was linked to lower risk of thirteen of twenty-six cancer types.", "Más actividad en el tiempo libre se asoció con menor riesgo de 13 de 26 tipos de cáncer.",
                ["More leisure activity: lower risk", "of 13 of 26 cancer types."], ["Más actividad en el tiempo libre: menor", "riesgo de 13 de 26 tipos de cáncer."]),
              L("Seven of them were at least twenty percent lower in the most active than in the least active.", "Siete de ellos fueron al menos un 20 por ciento menores en los más activos que en los menos activos.",
                ["7 of them at least 20% lower:", "most active vs least active."], ["7 de ellos al menos 20 % menos:", "más activos vs menos activos."])],
             count=(13, "{:.0f}")),
        tips3("READ THE FINE PRINT", ["target", "flask", "check"],
              [("Biggest drops: liver, kidney, esophagus", "Mayores bajas: hígado, riñón, esófago"),
               ("Little change after adjusting for BMI", "Poco cambio al ajustar por IMC"),
               ("Self-reported: association, not proof", "Autorreportado: asociación, no prueba")],
              [L("The biggest drops were in liver, kidney, and some stomach and esophagus cancers.", "Las mayores bajas fueron en cáncer de hígado, riñón y algunos de estómago y esófago.",
                 ["Biggest drops: liver, kidney, and", "some stomach and esophagus cancers."], ["Mayores bajas: hígado, riñón y", "algunos de estómago y esófago."]),
               L("Most links changed little after adjusting for body weight.", "La mayoría de las asociaciones cambió poco al ajustar por peso corporal.",
                 ["Most links changed little after", "adjusting for body weight."], ["La mayoría cambió poco al", "ajustar por peso corporal."]),
               L("Activity was self-reported, so this is an association, not proof.", "La actividad fue autorreportada, así que es una asociación, no una prueba.",
                 ["Self-reported activity: an", "association, not proof."], ["Actividad autorreportada: una", "asociación, no una prueba."])]),
        cta(56, "fifty-seven", "cincuenta y siete", "DAY 57 TOMORROW: ALCOHOL AND MUSCLE", "Mañana, día 57: alcohol y músculo"),
    ]
    cap = caption(56, "activity and cancer", "actividad y cáncer",
                  "Is being more active linked to lower cancer risk? A pooled analysis of 12 US and European cohorts (about 1.44 million adults aged 19–98, median follow-up 11 years, about 187,000 cancers) found that more leisure-time physical activity was associated with lower risk of 13 of 26 cancer types. Seven types were at least 20% lower in the most active (90th percentile) versus the least active (10th percentile). The largest reductions were for esophageal adenocarcinoma, liver, gastric cardia, kidney and myeloid leukemia. Most associations changed little after adjusting for BMI. Activity was self-reported: an association, not proof.",
                  "¿Estar más activo se asocia con menos riesgo de cáncer? Un análisis conjunto de 12 cohortes de EE. UU. y Europa (cerca de 1,44 millones de adultos de 19 a 98 años, seguimiento mediano de 11 años, unos 187.000 cánceres) halló que más actividad física en el tiempo libre se asoció con menor riesgo de 13 de 26 tipos de cáncer. Siete tipos fueron al menos un 20 % menores en los más activos (percentil 90) frente a los menos activos (percentil 10). Las mayores reducciones fueron en adenocarcinoma de esófago, hígado, cardias gástrico, riñón y leucemia mieloide. La mayoría de las asociaciones cambió poco al ajustar por IMC. La actividad fue autorreportada: una asociación, no una prueba.",
                  handle, "Moore et al., JAMA Intern Med, 2016")
    return out(56, "cancer", S, cap, "#cancerprevention #health #activelife #prevention #fitness", "Moore et al., JAMA Intern Med, 2016")

# ------------------------------------------------------------------ DIA 57
def reel_alcohol(handle):
    S = [
        hook(57, "fifty-seven", "cincuenta y siete", "TEACHING YOU: ALCOHOL AND MUSCLE", "Enseñándote: alcohol y músculo", ["DOES ALCOHOL", "HURT MUSCLE RECOVERY?"],
             "alcohol after training", "el alcohol después de entrenar",
             ("What does alcohol do to muscle recovery?", ["What does alcohol do", "to muscle recovery?"]),
             ("¿Qué le hace el alcohol a la recuperación muscular?", ["¿Qué le hace el alcohol a la", "recuperación muscular?"]), icon="flame"),
        stat("ALCOHOL AFTER TRAINING · 8 MEN", "-24%", 150, 0.24, "flame", ["muscle protein building", "with alcohol plus protein"],
             [L("Eight active men did a hard workout, then drank alcohol, about twelve standard drinks, over three hours.", "Ocho hombres activos hicieron un entrenamiento duro y luego bebieron alcohol, unos 12 tragos estándar, durante tres horas.",
                ["8 active men: hard workout, then", "about 12 standard drinks."], ["8 hombres activos: entrenamiento duro,", "luego unos 12 tragos estándar."]),
              L("Muscle protein building was about twenty-four percent lower with alcohol plus protein than with protein alone.", "La construcción de proteína muscular fue cerca de un 24 por ciento menor con alcohol más proteína que con proteína sola.",
                ["Muscle protein building ~24% lower", "with alcohol plus protein."], ["Construcción de proteína muscular ~24 %", "menor con alcohol más proteína."]),
              L("And about thirty-seven percent lower with alcohol plus carbohydrate.", "Y cerca de un 37 por ciento menor con alcohol más carbohidrato.",
                ["And ~37% lower with", "alcohol plus carbohydrate."], ["Y ~37 % menor con", "alcohol más carbohidrato."])],
             count=(24, "-{:.0f}%")),
        tips3("READ THE FINE PRINT", ["flame", "flask", "check"],
              [("An extreme dose: about 12 drinks", "Una dosis extrema: unos 12 tragos"),
               ("Protein softened the hit", "La proteína suavizó el golpe"),
               ("Only 8 men, one muscle sample", "Solo 8 hombres, una muestra muscular")],
              [L("The dose was extreme, about twelve standard drinks. Smaller amounts were not tested.", "La dosis fue extrema, unos 12 tragos estándar. No se probaron cantidades menores.",
                 ["An extreme dose: ~12 drinks.", "Smaller amounts were not tested."], ["Una dosis extrema: ~12 tragos.", "No se probaron cantidades menores."]),
               L("Protein helped: it was eighteen percent higher than carbohydrate, but alcohol still lowered it.", "La proteína ayudó: fue un 18 por ciento mayor que el carbohidrato, pero el alcohol igual la redujo.",
                 ["Protein helped: 18% higher than", "carbs, but alcohol still lowered it."], ["La proteína ayudó: 18 % mayor que los", "carbohidratos, pero el alcohol igual la bajó."]),
               L("It was only eight men, with a single muscle sample, so it is one clue.", "Fueron solo ocho hombres, con una sola muestra muscular, así que es una pista.",
                 ["Only 8 men and a single", "muscle sample: one clue."], ["Solo 8 hombres y una sola", "muestra muscular: una pista."])]),
        cta(57, "fifty-eight", "cincuenta y ocho", "DAY 58 TOMORROW: DEEP SQUATS", "Mañana, día 58: sentadillas profundas"),
    ]
    cap = caption(57, "alcohol and muscle recovery", "alcohol y recuperación muscular",
                  "What does alcohol do to muscle recovery? In a small crossover study, 8 physically active men did a hard session of concurrent training (leg extensions, cycling and sprint intervals) and then drank alcohol (1.5 g per kg of body mass, about 12 standard drinks, over 3 hours). Muscle protein synthesis was about 24% lower with alcohol plus protein than with protein alone, and about 37% lower with alcohol plus carbohydrate. Protein softened the hit, but alcohol still lowered it. The dose was extreme, there was no exercise-only trial, and only 8 men took part: one clue, not the final word.",
                  "¿Qué le hace el alcohol a la recuperación muscular? En un pequeño estudio cruzado, 8 hombres físicamente activos hicieron una sesión dura de entrenamiento concurrente (extensiones de pierna, ciclismo e intervalos de sprint) y luego bebieron alcohol (1,5 g por kg de masa corporal, unos 12 tragos estándar, durante 3 horas). La síntesis de proteína muscular fue cerca de un 24 % menor con alcohol más proteína que con proteína sola, y cerca de un 37 % menor con alcohol más carbohidrato. La proteína suavizó el golpe, pero el alcohol igual la redujo. La dosis fue extrema, no hubo una prueba solo con ejercicio y participaron solo 8 hombres: una pista, no la última palabra.",
                  handle, "Parr et al., PLoS One, 2014")
    return out(57, "alcohol", S, cap, "#recovery #musclebuilding #alcohol #protein #fitness", "Parr et al., PLoS One, 2014")

# ------------------------------------------------------------------ DIA 58
def reel_squat(handle):
    S = [
        hook(58, "fifty-eight", "cincuenta y ocho", "TEACHING YOU: DEEP SQUATS", "Enseñándote: sentadillas profundas", ["ARE DEEP SQUATS", "BAD FOR YOUR KNEES?"],
             "deep squats and your knees", "las sentadillas profundas y tus rodillas",
             ("Are deep squats really bad for your knees?", ["Are deep squats really", "bad for your knees?"]),
             ("¿Las sentadillas profundas realmente dañan las rodillas?", ["¿Las sentadillas profundas", "realmente dañan las rodillas?"]), icon="dumbbell"),
        stat("KNEE PRESSURE · SPORTS MEDICINE REVIEW", "90°", 190, 0.5, "dumbbell", ["knee bend where kneecap", "pressure peaks"],
             [L("A review in Sports Medicine looked at the evidence on deep squats, the knee and the spine.", "Una revisión en Sports Medicine analizó la evidencia sobre las sentadillas profundas, la rodilla y la columna.",
                ["A Sports Medicine review on", "deep squats, knee and spine."], ["Una revisión de Sports Medicine sobre", "sentadillas profundas, rodilla y columna."]),
              L("Pressure behind the kneecap peaks at about a ninety degree bend.", "La presión detrás de la rótula alcanza su pico cerca de los noventa grados de flexión.",
                ["Pressure behind the kneecap", "peaks around 90° of bend."], ["La presión detrás de la rótula", "llega al pico cerca de 90°."]),
              L("Going deeper spreads the load over a larger area, so deeper does not mean more stress.", "Bajar más reparte la carga en un área mayor, así que más profundo no significa más estrés.",
                ["Going deeper spreads the load,", "so deeper is not more stress."], ["Bajar más reparte la carga,", "más profundo no es más estrés."])]),
        tips3("THE CAUTIONS", ["dumbbell", "check", "target"],
              [("Learn technique with supervision", "Aprende la técnica con supervisión"),
               ("Add load gradually", "Aumenta la carga de a poco"),
               ("Half squats, max loads: may wear joints", "Medias con cargas máximas: pueden desgastar")],
              [L("The authors say deep squats are safe when technique is learned under expert supervision.", "Los autores dicen que las sentadillas profundas son seguras si la técnica se aprende con supervisión experta.",
                 ["Safe when technique is learned", "under expert supervision."], ["Seguras si la técnica se aprende", "con supervisión experta."]),
               L("And when the load is increased gradually.", "Y cuando la carga aumenta gradualmente.",
                 ["And when the load", "increases gradually."], ["Y cuando la carga", "aumenta gradualmente."]),
               L("They warn that half squats with near-maximal loads may promote long-term wear.", "Advierten que las medias sentadillas con cargas casi máximas pueden favorecer el desgaste a largo plazo.",
                 ["Half squats with near-max loads", "may promote long-term wear."], ["Medias sentadillas con cargas casi máximas", "pueden favorecer desgaste a largo plazo."])]),
        cta(58, "fifty-nine", "cincuenta y nueve", "DAY 59 TOMORROW: CAFFEINE AND SLEEP", "Mañana, día 59: cafeína y sueño"),
    ]
    cap = caption(58, "deep squats and your knees", "sentadillas profundas y tus rodillas",
                  "Are deep squats really bad for your knees? A review in Sports Medicine analyzed how squat depth and load affect the knee joint and the spine. The authors conclude that deep squats are not inherently harmful, and that concerns are largely unfounded when technique and loading are sound: pressure behind the kneecap peaks around 90° of knee bend, and going deeper spreads the load over a larger area. They say deep squats are safe when technique is learned under expert supervision and load is increased progressively, and warn that half or quarter squats with near-maximal loads may promote long-term wear. It is a review of biomechanics, not a trial of injuries. If you have knee pain or past injury, ask a professional.",
                  "¿Las sentadillas profundas realmente dañan las rodillas? Una revisión en Sports Medicine analizó cómo la profundidad y la carga de la sentadilla afectan la articulación de la rodilla y la columna. Los autores concluyen que las sentadillas profundas no son inherentemente dañinas y que las preocupaciones son en gran parte infundadas cuando la técnica y la carga son adecuadas: la presión detrás de la rótula llega al pico cerca de 90° de flexión, y bajar más reparte la carga en un área mayor. Dicen que son seguras si la técnica se aprende con supervisión experta y la carga aumenta progresivamente, y advierten que las medias o cuartos de sentadilla con cargas casi máximas pueden favorecer el desgaste a largo plazo. Es una revisión de biomecánica, no un ensayo de lesiones. Si tienes dolor de rodilla o una lesión previa, consulta a un profesional.",
                  handle, "Hartmann et al., Sports Med, 2013")
    return out(58, "deep-squat", S, cap, "#squat #kneehealth #legday #technique #fitness", "Hartmann et al., Sports Med, 2013")

# ------------------------------------------------------------------ DIA 59
def reel_caffeine_sleep(handle):
    S = [
        hook(59, "fifty-nine", "cincuenta y nueve", "TEACHING YOU: CAFFEINE AND SLEEP", "Enseñándote: cafeína y sueño", ["WHEN SHOULD YOU", "STOP CAFFEINE?"],
             "caffeine and sleep", "la cafeína y el sueño",
             ("Does an afternoon coffee wreck your sleep?", ["Does an afternoon coffee", "wreck your sleep?"]),
             ("¿Un café a la tarde arruina tu sueño?", ["¿Un café a la tarde", "arruina tu sueño?"]), icon="moon"),
        stat("CAFFEINE BEFORE BED · 12 SLEEPERS", "-1h", 190, 0.5, "moon", ["of sleep lost with caffeine", "6 hours before bed"],
             [L("Twelve healthy sleepers took a big dose of caffeine, about two to three cups of coffee.", "Doce personas con sueño sano tomaron 400 miligramos de cafeína, unas dos a tres tazas de café.",
                ["12 healthy sleepers took 400 mg", "of caffeine: 2–3 cups of coffee."], ["12 personas con sueño sano tomaron 400 mg", "de cafeína: 2–3 tazas de café."]),
              L("They took it at zero, three or six hours before bedtime.", "La tomaron a cero, tres o seis horas antes de acostarse.",
                ["Taken 0, 3 or 6 hours", "before bedtime."], ["Tomada 0, 3 o 6 horas", "antes de acostarse."]),
              L("Even six hours before bed, measured sleep dropped by more than an hour.", "Incluso seis horas antes de acostarse, el sueño medido bajó más de una hora.",
                ["Even 6 hours before bed,", "sleep dropped by over an hour."], ["Incluso 6 horas antes,", "el sueño bajó más de una hora."])]),
        tips3("READ THE FINE PRINT", ["moon", "flask", "check"],
              [("Zero and 3 hours also hurt sleep", "A 0 y 3 horas también dañó el sueño"),
               ("Sleep diaries missed the effect", "Los diarios de sueño no lo notaron"),
               ("Only 12 people, one dose", "Solo 12 personas, una dosis")],
              [L("Caffeine at zero and three hours before bed also disrupted sleep.", "La cafeína a cero y tres horas antes de acostarse también alteró el sueño.",
                 ["Caffeine 0 and 3 hours before", "bed also disrupted sleep."], ["Cafeína a 0 y 3 horas antes", "también alteró el sueño."]),
               L("A home monitor caught it, but the sleep diary did not. People did not notice.", "Un monitor en casa lo detectó, pero los diarios de sueño no. Las personas no lo notaron.",
                 ["A home monitor caught it;", "sleep diaries did not."], ["Un monitor en casa lo detectó;", "los diarios de sueño no."]),
               L("It was only twelve people and one dose, so smaller amounts were not tested.", "Fueron solo doce personas y una dosis, así que no se probaron cantidades menores.",
                 ["Only 12 people, one dose:", "smaller amounts not tested."], ["Solo 12 personas, una dosis:", "cantidades menores sin probar."])]),
        cta(59, "sixty", "sesenta", "DAY 60 TOMORROW: RUNNING AND KNEES", "Mañana, día 60: correr y rodillas"),
    ]
    cap = caption(59, "caffeine and sleep", "cafeína y sueño",
                  "Does an afternoon coffee wreck your sleep? In a small placebo-controlled study, 12 healthy normal sleepers took 400 mg of caffeine (about 2–3 cups of coffee) 0, 3 or 6 hours before bedtime. Even at 6 hours, objectively measured total sleep time dropped by more than one hour, and caffeine at 3 and 0 hours also disrupted sleep. A home monitor recorded the loss, but participants' sleep diaries did not reflect it: people did not notice. Only 12 people and a single dose were tested, so smaller amounts were not studied. The authors suggest avoiding substantial caffeine for at least 6 hours before bed.",
                  "¿Un café a la tarde arruina tu sueño? En un pequeño estudio controlado con placebo, 12 personas con sueño sano tomaron 400 mg de cafeína (unas 2–3 tazas de café) 0, 3 o 6 horas antes de acostarse. Incluso a las 6 horas, el tiempo total de sueño medido objetivamente bajó más de una hora, y la cafeína a las 3 y 0 horas también alteró el sueño. Un monitor en casa registró la pérdida, pero los diarios de sueño de los participantes no la reflejaron: no lo notaron. Solo se probaron 12 personas y una dosis, así que no se estudiaron cantidades menores. Los autores sugieren evitar cantidades importantes de cafeína al menos 6 horas antes de dormir.",
                  handle, "Drake et al., J Clin Sleep Med, 2013")
    return out(59, "caffeine-sleep", S, cap, "#sleep #caffeine #coffee #recovery #fitness", "Drake et al., J Clin Sleep Med, 2013")

# ------------------------------------------------------------------ DIA 60
def reel_running_knees(handle):
    S = [
        hook(60, "sixty", "sesenta", "TEACHING YOU: RUNNING AND KNEES", "Enseñándote: correr y rodillas", ["DOES RUNNING", "WRECK YOUR KNEES?"],
             "running and joint health", "correr y la salud de las articulaciones",
             ("Does running really wreck your knees and hips?", ["Does running really wreck", "your knees and hips?"]),
             ("¿Correr realmente arruina rodillas y caderas?", ["¿Correr realmente arruina", "rodillas y caderas?"]), icon="walk"),
        stat("HIP AND KNEE OSTEOARTHRITIS", "3.5%", 150, 0.035, "walk", ["of recreational runners,", "vs 10.2% of sedentary people"],
             [L("A meta-analysis pooled seventeen studies with over one hundred fourteen thousand people.", "Un metaanálisis reunió 17 estudios con más de 114.000 personas.",
                ["17 studies pooled, over", "114,000 people."], ["17 estudios reunidos, más de", "114.000 personas."]),
              L("Hip or knee osteoarthritis showed up in three point five percent of recreational runners, versus ten point two percent of sedentary people.",
                "La artrosis de cadera o rodilla apareció en el 3,5 por ciento de los corredores recreativos, frente al 10,2 por ciento de las personas sedentarias.",
                ["Osteoarthritis: 3.5% of recreational", "runners vs 10.2% of sedentary."], ["Artrosis: 3,5 % de corredores", "recreativos vs 10,2 % de sedentarios."]),
              L("But it was thirteen point three percent in competitive runners.", "Pero fue del 13,3 por ciento en corredores de competencia.",
                ["But 13.3% in", "competitive runners."], ["Pero 13,3 % en", "corredores de competencia."])]),
        tips3("READ THE FINE PRINT", ["walk", "flask", "check"],
              [("How much running is safe: unknown", "Cuánto correr es seguro: se desconoce"),
               ("Weight, job and past injury: not assessed", "Peso, trabajo y lesiones previas: no evaluados"),
               ("A link, not proof running protects", "Una asociación, no prueba de que proteja")],
              [L("The scientists could not say how much running is safe for hips and knees.", "Los investigadores no pudieron decir cuánto correr es seguro para caderas y rodillas.",
                 ["They could not say how much", "running is safe for joints."], ["No pudieron decir cuánto correr", "es seguro para las articulaciones."]),
               L("They did not assess body weight, job load or past injury.", "No evaluaron el peso corporal, la carga laboral ni las lesiones previas.",
                 ["Body weight, job load and past", "injury were not assessed."], ["Peso corporal, carga laboral y", "lesiones previas no se evaluaron."]),
               L("It is a link, not proof that running protects your joints.", "Es una asociación, no prueba de que correr proteja tus articulaciones.",
                 ["A link, not proof that running", "protects your joints."], ["Una asociación, no prueba de que", "correr proteja tus articulaciones."])]),
        {"type": "cta", "tail": 1.0, "next_en": "MORE LESSONS COMING", "next_es": "Vienen más lecciones",
         "lines": [L("Save this, and send it to a friend who loves running.", "Guárdalo y envíaselo a un amigo que ame correr.",
                     ["Save this, and send it to a", "friend who loves running."], ["Guárdalo y envíaselo a un", "amigo que ame correr."]),
                   L("Follow for one new lesson every day.", "Sígueme para una lección nueva cada día.",
                     ["Follow for one new lesson", "every day."], ["Sígueme para una lección", "nueva cada día."])]},
    ]
    cap = (f"Day 60 teaching you: running and knees 💪\n"
           f"Does running really wreck your knees and hips? A systematic review and meta-analysis (17 studies, 114,829 people) found hip or knee osteoarthritis in about 3.5% of recreational runners, 10.2% of sedentary non-runners and 13.3% of competitive runners. The researchers could not determine how much running is safe for the joints and did not assess body weight, occupational load or past injury. This is an association, not proof that running protects your joints. If you have joint pain, ask a professional.\n\n"
           f"Día 60 enseñándote: correr y rodillas 💪\n"
           f"¿Correr realmente arruina rodillas y caderas? Una revisión sistemática y metaanálisis (17 estudios, 114.829 personas) halló artrosis de cadera o rodilla en cerca del 3,5 % de los corredores recreativos, el 10,2 % de las personas sedentarias y el 13,3 % de los corredores de competencia. Los investigadores no pudieron determinar cuánto correr es seguro para las articulaciones y no evaluaron el peso corporal, la carga laboral ni las lesiones previas. Es una asociación, no una prueba de que correr proteja tus articulaciones. Si tienes dolor articular, consulta a un profesional.\n\n"
           f"Save this 📌 and follow {handle}. / Guárdalo y sigue a {handle}.\n"
           f"Source / Fuente: Alentorn-Geli et al., J Orthop Sports Phys Ther, 2017.\n"
           f"Educational content, not medical advice. / Contenido educativo, no es consejo médico.")
    return out(60, "running-knees", S, cap, "#running #kneehealth #jointhealth #cardio #fitness", "Alentorn-Geli et al., JOSPT, 2017")

REELS_MORE8 = {54: reel_fitness, 55: reel_colds, 56: reel_cancer, 57: reel_alcohol, 58: reel_squat, 59: reel_caffeine_sleep, 60: reel_running_knees}
