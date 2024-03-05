class Enfermedad:
    def __init__(self, nombre, preguntas):
        self.nombre = nombre
        self.preguntas = preguntas


class MaquinaDeInferencia:
    def __init__(self):
        self.enfermedades = [
            Enfermedad("Asma", ["¿Tiene dificultad para respirar?", "¿Ha tenido sibilancias en el pecho?"]),
            Enfermedad("VIH", ["¿Ha tenido relaciones sexuales sin protección?", "¿Ha compartido agujas?"]),
            Enfermedad("Diabetes", ["¿Tiene sed frecuente?", "¿Orina con frecuencia?"]),
            Enfermedad("Alzheimer", ["¿Tiene problemas de memoria a corto plazo?", "¿Se siente desorientado/a con frecuencia?"]),
            Enfermedad("Gripe", ["¿Tiene fiebre alta?", "¿Tiene dolor de cabeza y muscular?"]),
            Enfermedad("Lupus", ["¿Tiene dolor o hinchazón en las articulaciones?", "¿Se siente fatigado/a con frecuencia?"]),
            Enfermedad("Herpes", ["¿Ha experimentado llagas en la boca o en los genitales?", "¿Siente hormigueo o picazón en la piel?"]),
            Enfermedad("Ansiedad", ["¿Siente nerviosismo o preocupación excesiva?", "¿Tiene problemas para conciliar el sueño?"]),
            Enfermedad("COVID", ["¿Ha estado en contacto con personas infectadas por COVID-19?", "¿Ha experimentado fiebre o tos seca recientemente?"]),
            Enfermedad("Colitis", ["¿Experimenta dolor abdominal?", "¿Tiene diarrea con frecuencia?"])
        ]

    def hacer_pregunta(self, pregunta):
        respuesta = input(pregunta + " (Sí/No): ").lower()
        return respuesta == 'sí' or respuesta == 'si'

    def inferir_enfermedad(self):
        for enfermedad in self.enfermedades:
            sintomas_coinciden = True
            for pregunta in enfermedad.preguntas:
                if not self.hacer_pregunta(pregunta):
                    sintomas_coinciden = False
                    break
            if sintomas_coinciden:
                return enfermedad.nombre
        return "No se puede determinar la enfermedad."

    def ejecutar_maquina(self):
        print("Bienvenido a la máquina de inferencia de enfermedades.")
        print("Por favor, responde las siguientes preguntas con Sí o No.")
        enfermedad_detectada = self.inferir_enfermedad()
        print("La enfermedad detectada es:", enfermedad_detectada)


if __name__ == "__main__":
    maquina = MaquinaDeInferencia()
    maquina.ejecutar_maquina()
