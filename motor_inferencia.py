# motor_inferencia.py
# Sistema Experto de Nivelación BushiCode
# Librería: experta (pip install experta)
import collections
from preguntas import preguntas_quiz
import collections.abc
collections.Mapping = collections.abc.Mapping

from experta import *


# ─────────────────────────────────────────────
#  HECHOS (Facts)
# ─────────────────────────────────────────────

class RespuestaUsuario(Fact):
    """Almacena Q1..Q34 como True/False"""
    pass

class Bloque(Fact):
    """Resultado de la Fase 1"""
    valor = Field(str)

class Rango(Fact):
    """Resultado final"""
    valor = Field(str)


# ─────────────────────────────────────────────
#  EVALUADOR DE RESPUESTAS
#  (Convierte las respuestas del form en True/False)
# ─────────────────────────────────────────────

def evaluar_respuestas(respuestas_frontend: list) -> dict:
    """
    Entrada del JS: [ [1], [1,3], [2], ... ] (Lista de listas)
    Salida: {"Q1": True, "Q2": True, "Q3": False, ...}
    """
    evaluacion = {}
    
    for indice, pregunta in enumerate(preguntas_quiz):
        id_pregunta = f"Q{pregunta['id']}"
        
        # Evitar errores si el usuario mandó menos respuestas de las esperadas
        if indice < len(respuestas_frontend):
            resp_usuario = set(respuestas_frontend[indice])
        else:
            resp_usuario = set()
            
        resp_correcta = set(pregunta["respuesta_correcta"])
        
        # Si los sets son idénticos, la respuesta es True
        evaluacion[id_pregunta] = (resp_usuario == resp_correcta)
        
    return evaluacion


# ─────────────────────────────────────────────
#  MOTOR DE INFERENCIA
# ─────────────────────────────────────────────

class MotorBushiCode(KnowledgeEngine):

    # ══════════════════════════════════════════
    #  FASE 1 — ASIGNACIÓN DE BLOQUE (R1 - R6)
    # ══════════════════════════════════════════

    # R1
    @Rule(
        AS.r << RespuestaUsuario(),
        TEST(lambda r: not r["Q1"] or not r["Q2"])
    )
    def r1_bloque_nulo(self, r):
        self.declare(Bloque(valor="Nulo"))

    # R2
    @Rule(
        AS.r << RespuestaUsuario(),
        TEST(lambda r: r["Q1"] and not r["Q10"]),
        NOT(Bloque())
    )
    def r2_bloque_basico(self, r):
        self.declare(Bloque(valor="Basico"))

    # R3
    @Rule(
        AS.r << RespuestaUsuario(),
        TEST(lambda r: r["Q10"] and not r["Q16"]),
        NOT(Bloque())
    )
    def r3_bloque_funcional(self, r):
        self.declare(Bloque(valor="Funcional"))

    # R4
    @Rule(
        AS.r << RespuestaUsuario(),
        TEST(lambda r: r["Q16"] and not r["Q25"]),
        NOT(Bloque())
    )
    def r4_bloque_poo(self, r):
        self.declare(Bloque(valor="POO_Avanzado"))

    # R5
    @Rule(
        AS.r << RespuestaUsuario(),
        TEST(lambda r: r["Q25"] and not r["Q30"]),
        NOT(Bloque())
    )
    def r5_bloque_senior(self, r):
        self.declare(Bloque(valor="Python_Senior"))

    # R6
    @Rule(
        AS.r << RespuestaUsuario(),
        TEST(lambda r: r["Q30"]),
        NOT(Bloque())
    )
    def r6_bloque_arquitecto(self, r):
        self.declare(Bloque(valor="Arquitecto"))


    # ══════════════════════════════════════════
    #  FASE 2 — BLOQUE NULO Y BÁSICO (R7 - R13)
    # ══════════════════════════════════════════

    # R7
    @Rule(Bloque(valor="Nulo"), NOT(Rango()))
    def r7(self):
        self.declare(Rango(valor="BRONCE-3"))

    # R8
    @Rule(
        Bloque(valor="Basico"),
        AS.r << RespuestaUsuario(),
        TEST(lambda r: not r["Q3"]),
        NOT(Rango())
    )
    def r8(self, r):
        self.declare(Rango(valor="BRONCE-3"))

    # R9
    @Rule(
        Bloque(valor="Basico"),
        AS.r << RespuestaUsuario(),
        TEST(lambda r: r["Q3"] and not r["Q4"] and not r["Q5"]),
        NOT(Rango())
    )
    def r9(self, r):
        self.declare(Rango(valor="BRONCE-2"))

    # R10
    @Rule(
        Bloque(valor="Basico"),
        AS.r << RespuestaUsuario(),
        TEST(lambda r: (r["Q4"] or r["Q5"]) and not r["Q6"]),
        NOT(Rango())
    )
    def r10(self, r):
        self.declare(Rango(valor="BRONCE-1"))

    # R11
    @Rule(
        Bloque(valor="Basico"),
        AS.r << RespuestaUsuario(),
        TEST(lambda r: r["Q6"] and not r["Q8"]),
        NOT(Rango())
    )
    def r11(self, r):
        self.declare(Rango(valor="BRONCE-1"))

    # R12
    @Rule(
        Bloque(valor="Basico"),
        AS.r << RespuestaUsuario(),
        TEST(lambda r: r["Q6"] and r["Q8"] and not r["Q9"]),
        NOT(Rango())
    )
    def r12(self, r):
        self.declare(Rango(valor="PLATA-3"))

    # R13
    @Rule(
        Bloque(valor="Basico"),
        AS.r << RespuestaUsuario(),
        TEST(lambda r: r["Q9"]),
        NOT(Rango())
    )
    def r13(self, r):
        self.declare(Rango(valor="PLATA-3"))


    # ══════════════════════════════════════════
    #  FASE 3 — BLOQUE FUNCIONAL (R14 - R20)
    # ══════════════════════════════════════════

    # R14
    @Rule(
        Bloque(valor="Funcional"),
        AS.r << RespuestaUsuario(),
        TEST(lambda r: not r["Q11"]),
        NOT(Rango())
    )
    def r14(self, r):
        self.declare(Rango(valor="PLATA-2"))

    # R15
    @Rule(
        Bloque(valor="Funcional"),
        AS.r << RespuestaUsuario(),
        TEST(lambda r: r["Q11"] and not r["Q13"]),
        NOT(Rango())
    )
    def r15(self, r):
        self.declare(Rango(valor="PLATA-1"))

    # R16
    @Rule(
        Bloque(valor="Funcional"),
        AS.r << RespuestaUsuario(),
        TEST(lambda r: r["Q13"] and not r["Q15"]),
        NOT(Rango())
    )
    def r16(self, r):
        self.declare(Rango(valor="PLATA-1"))

    # R17
    @Rule(
        Bloque(valor="Funcional"),
        AS.r << RespuestaUsuario(),
        TEST(lambda r: r["Q15"] and not r["Q12"]),
        NOT(Rango())
    )
    def r17(self, r):
        self.declare(Rango(valor="ORO-3"))

    # R18
    @Rule(
        Bloque(valor="Funcional"),
        AS.r << RespuestaUsuario(),
        TEST(lambda r: r["Q15"] and r["Q12"] and not r["Q14"]),
        NOT(Rango())
    )
    def r18(self, r):
        self.declare(Rango(valor="ORO-3"))

    # R19
    @Rule(
        Bloque(valor="Funcional"),
        AS.r << RespuestaUsuario(),
        TEST(lambda r: r["Q14"] and not r["Q15"]),
        NOT(Rango())
    )
    def r19(self, r):
        self.declare(Rango(valor="ORO-2"))

    # R20
    @Rule(
        Bloque(valor="Funcional"),
        AS.r << RespuestaUsuario(),
        TEST(lambda r: r["Q15"] and r["Q14"]),
        NOT(Rango())
    )
    def r20(self, r):
        self.declare(Rango(valor="ORO-2"))


    # ══════════════════════════════════════════
    #  FASE 4 — BLOQUE POO AVANZADO (R21 - R29)
    # ══════════════════════════════════════════

    # R21
    @Rule(
        Bloque(valor="POO_Avanzado"),
        AS.r << RespuestaUsuario(),
        TEST(lambda r: not r["Q17"]),
        NOT(Rango())
    )
    def r21(self, r):
        self.declare(Rango(valor="ORO-1"))

    # R22
    @Rule(
        Bloque(valor="POO_Avanzado"),
        AS.r << RespuestaUsuario(),
        TEST(lambda r: r["Q17"] and not r["Q18"]),
        NOT(Rango())
    )
    def r22(self, r):
        self.declare(Rango(valor="ORO-1"))

    # R23
    @Rule(
        Bloque(valor="POO_Avanzado"),
        AS.r << RespuestaUsuario(),
        TEST(lambda r: r["Q18"] and not r["Q19"]),
        NOT(Rango())
    )
    def r23(self, r):
        self.declare(Rango(valor="PLATINO-3"))

    # R24
    @Rule(
        Bloque(valor="POO_Avanzado"),
        AS.r << RespuestaUsuario(),
        TEST(lambda r: r["Q19"] and not r["Q20"]),
        NOT(Rango())
    )
    def r24(self, r):
        self.declare(Rango(valor="PLATINO-3"))

    # R25
    @Rule(
        Bloque(valor="POO_Avanzado"),
        AS.r << RespuestaUsuario(),
        TEST(lambda r: r["Q20"] and not r["Q21"]),
        NOT(Rango())
    )
    def r25(self, r):
        self.declare(Rango(valor="PLATINO-2"))

    # R26
    @Rule(
        Bloque(valor="POO_Avanzado"),
        AS.r << RespuestaUsuario(),
        TEST(lambda r: r["Q21"] and not r["Q22"]),
        NOT(Rango())
    )
    def r26(self, r):
        self.declare(Rango(valor="PLATINO-2"))

    # R27
    @Rule(
        Bloque(valor="POO_Avanzado"),
        AS.r << RespuestaUsuario(),
        TEST(lambda r: r["Q22"] and not r["Q23"]),
        NOT(Rango())
    )
    def r27(self, r):
        self.declare(Rango(valor="PLATINO-2"))

    # R28
    @Rule(
        Bloque(valor="POO_Avanzado"),
        AS.r << RespuestaUsuario(),
        TEST(lambda r: r["Q22"] and not r["Q24"]),
        NOT(Rango())
    )
    def r28(self, r):
        self.declare(Rango(valor="PLATINO-2"))

    # R29
    @Rule(
        Bloque(valor="POO_Avanzado"),
        AS.r << RespuestaUsuario(),
        TEST(lambda r: r["Q23"] and r["Q24"]),
        NOT(Rango())
    )
    def r29(self, r):
        self.declare(Rango(valor="PLATINO-1"))


    # ══════════════════════════════════════════
    #  FASE 5 — BLOQUE PYTHON SENIOR (R30 - R34)
    # ══════════════════════════════════════════

    # R30
    @Rule(
        Bloque(valor="Python_Senior"),
        AS.r << RespuestaUsuario(),
        TEST(lambda r: not r["Q26"]),
        NOT(Rango())
    )
    def r30(self, r):
        self.declare(Rango(valor="PLATINO-1"))

    # R31
    @Rule(
        Bloque(valor="Python_Senior"),
        AS.r << RespuestaUsuario(),
        TEST(lambda r: r["Q26"] and not r["Q27"]),
        NOT(Rango())
    )
    def r31(self, r):
        self.declare(Rango(valor="DIAMANTE-3"))

    # R32
    @Rule(
        Bloque(valor="Python_Senior"),
        AS.r << RespuestaUsuario(),
        TEST(lambda r: r["Q27"] and not r["Q28"]),
        NOT(Rango())
    )
    def r32(self, r):
        self.declare(Rango(valor="DIAMANTE-3"))

    # R33
    @Rule(
        Bloque(valor="Python_Senior"),
        AS.r << RespuestaUsuario(),
        TEST(lambda r: r["Q28"] and not r["Q29"]),
        NOT(Rango())
    )
    def r33(self, r):
        self.declare(Rango(valor="DIAMANTE-2"))

    # R34
    @Rule(
        Bloque(valor="Python_Senior"),
        AS.r << RespuestaUsuario(),
        TEST(lambda r: r["Q29"]),
        NOT(Rango())
    )
    def r34(self, r):
        self.declare(Rango(valor="DIAMANTE-1"))


    # ══════════════════════════════════════════
    #  FASE 6 — BLOQUE ARQUITECTO (R35 - R39)
    # ══════════════════════════════════════════

    # R35
    @Rule(
        Bloque(valor="Arquitecto"),
        AS.r << RespuestaUsuario(),
        TEST(lambda r: not r["Q31"]),
        NOT(Rango())
    )
    def r35(self, r):
        self.declare(Rango(valor="MAESTRO-3"))

    # R36
    @Rule(
        Bloque(valor="Arquitecto"),
        AS.r << RespuestaUsuario(),
        TEST(lambda r: r["Q31"] and not r["Q32"]),
        NOT(Rango())
    )
    def r36(self, r):
        self.declare(Rango(valor="MAESTRO-3"))

    # R37
    @Rule(
        Bloque(valor="Arquitecto"),
        AS.r << RespuestaUsuario(),
        TEST(lambda r: r["Q32"] and not r["Q33"]),
        NOT(Rango())
    )
    def r37(self, r):
        self.declare(Rango(valor="MAESTRO-2"))

    # R38
    @Rule(
        Bloque(valor="Arquitecto"),
        AS.r << RespuestaUsuario(),
        TEST(lambda r: r["Q33"] and not r["Q34"]),
        NOT(Rango())
    )
    def r38(self, r):
        self.declare(Rango(valor="MAESTRO-1"))

    # R39
    @Rule(
        Bloque(valor="Arquitecto"),
        AS.r << RespuestaUsuario(),
        TEST(lambda r: r["Q34"]),
        NOT(Rango())
    )
    def r39(self, r):
        self.declare(Rango(valor="CODE-PREDATOR"))


    # ══════════════════════════════════════════
    #  FASE 7 — REGLAS ANTI-TRAMPA (R40 - R45)
    #  salience=100 → se disparan ANTES que el resto
    # ══════════════════════════════════════════

    # R40: Adivinó C-Extensions pero no sabe declarar variables
# R40: Adivinó concurrencia pero falla en lo básico
    @Rule(
        AND(
            AS.r << RespuestaUsuario(),
            TEST(lambda r: r["Q34"] and not r["Q1"])
        ),
        salience=100
    )
    def r40(self, r):
        self.declare(Rango(valor="BRONCE-3"))

    # R41: Adivinó asincronismo pero no sabe qué es un return
    @Rule(
        AND(
            AS.r << RespuestaUsuario(),
            TEST(lambda r: r["Q30"] and not r["Q10"])
        ),
        salience=100
    )
    def r41(self, r):
        self.declare(Rango(valor="BRONCE-2"))

    # R42: Adivinó decoradores pero no sabe usar if/else
    @Rule(
        AND(
            AS.r << RespuestaUsuario(),
            TEST(lambda r: r["Q25"] and not r["Q3"])
        ),
        salience=100
    )
    def r42(self, r):
        self.declare(Rango(valor="BRONCE-3"))

    # R43: Adivinó clases pero no sabe usar una lista
    @Rule(
        AND(
            AS.r << RespuestaUsuario(),
            TEST(lambda r: r["Q16"] and not r["Q6"])
        ),
        salience=100
    )
    def r43(self, r):
        self.declare(Rango(valor="BRONCE-1"))

    # R44: Adivinó testing pero falla en funciones básicas
    @Rule(
        AND(
            AS.r << RespuestaUsuario(),
            TEST(lambda r: r["Q29"] and not r["Q10"])
        ),
        salience=100
    )
    def r44(self, r):
        self.declare(Rango(valor="BRONCE-2"))

    # R45: Adivinó entornos virtuales pero falla en operadores
    @Rule(
        AND(
            AS.r << RespuestaUsuario(),
            TEST(lambda r: r["Q24"] and not r["Q2"])
        ),
        salience=100
    )
    def r45(self, r):
        self.declare(Rango(valor="BRONCE-3"))


# ─────────────────────────────────────────────
#  FUNCIÓN PRINCIPAL — inferir_nivel()
#  Entrada: respuestas crudas del formulario
#  Salida:  dict con bloque y rango final
# ─────────────────────────────────────────────

def inferir_nivel(respuestas_usuario: dict) -> dict:
    """
    Uso desde Flask:
        from motor_inferencia import inferir_nivel
        resultado = inferir_nivel(respuestas_del_form)
        nivel_final = resultado["rango"]   # ← guardar en DB
    """
    Q = evaluar_respuestas(respuestas_usuario)

    motor = MotorBushiCode()
    motor.reset()
    motor.declare(RespuestaUsuario(**Q))
    motor.run()

    bloque_final = "Nulo"
    rango_final  = "BRONCE-3"

    for fact in motor.facts.values():
        if isinstance(fact, Bloque):
            bloque_final = fact["valor"]
        if isinstance(fact, Rango):
            rango_final = fact["valor"]

    return {
        "bloque": bloque_final,
        "rango":  rango_final,
        "detalle_preguntas": Q
    }

