import schemdraw
import schemdraw.elements as elm
from schemdraw import flow
from schemdraw import dsp


def teste1(d):
    # ============== Steps ============== #
    d += (step1 := flow.Box().label("1").fill(""))
    d += flow.Arrow().down().label("E1B2")
    d += (step2 := flow.Box().label("2").fill(""))

    # ============== Activities ============== #
    d += flow.Line().right(d.unit / 2).at(step1.E)
    d += (
        act1 := flow.Box(w=8, h=3)
        .anchor("W")
        .label("Avança E1Y1\ninicia temporizador1")
        .fill("")
    )

    d += flow.Line().right(d.unit / 2).at(step2.E)
    d += (
        act2 := flow.Box(w=8, h=3)
        .anchor("W")
        .label("Recua E1Y1\nreinicia temporizador1")
        .fill("")
    )

    # ============== Fail test ============== #
    d += flow.Line().left(d.unit * 4).at(step1.W)
    d += flow.Arrow().down(d.unit / 2).label("temp1")
    d += (fail_step1 := flow.Box().label("4").fill(""))
    d += flow.Line().right(d.unit / 2).at(fail_step1.E)
    d += (
        fail_act1 := flow.Box(w=8, h=3)
        .anchor("W")
        .label("Falha do sensor E1B2\n ou falha do avanço do\ncilindro")
        .fill("")
    )

    d += flow.Line().left(d.unit * 4).at(step2.W)
    d += flow.Arrow().down(d.unit / 2).label("temp1")
    d += (fail_step2 := flow.Box().label("5").fill(""))
    d += flow.Line().right(d.unit / 2).at(fail_step2.E)
    d += (
        fail_act2 := flow.Box(w=8, h=3)
        .anchor("W")
        .label("Falha do sensor E1B1\n ou falha do recuo do\ncilindro")
        .fill("")
    )

    # ============== End ============== #
    d += flow.Line().down(d.unit).at(step2.S).label("E1B1")
    d += flow.Arrow().down(d.unit * 2).label("")
    d += (
        test1 := elm.EncircleBox(
            [act1, act2, fail_step1, fail_step2, fail_act1, fail_act2], padx=0.8
        )
        .linestyle("--")
        .linewidth(2)
        .color("red")
        .label("Teste 1 (avanço/recuo do cilindro alimentação)", loc="left", rotate=90)
    )


def teste2(d):
    # ============== Steps ============== #
    d += (step1 := flow.Box().label("6").fill(""))
    d += flow.Arrow().down().label("E1S1")
    d = teste3(d)
    d += (step2 := flow.Box().label("7").fill(""))

    # ============== Activities ============== #
    d += flow.Line().right(d.unit / 2).at(step1.E)
    d += (
        act1 := flow.Box(w=8, h=3)
        .anchor("W")
        .label("Presença de peça\nno sensor E1S1\nreinicia temporizador1")
        .fill("")
    )

    d += flow.Line().right(d.unit / 2).at(step2.E)
    d += (
        act2 := flow.Box(w=8, h=3)
        .anchor("W")
        .label("Ausência de peça\nno sensor E1S1\nreinicia temporizador1")
        .fill("")
    )

    # ============== Fail test ============== #
    d += flow.Line().left(d.unit * 9).at(step1.W)
    d += flow.Arrow().down(d.unit / 2).label("temp1")
    d += (fail_step1 := flow.Box().label("18").fill(""))
    d += flow.Line().right(d.unit / 2).at(fail_step1.E)
    d += (
        fail_act1 := flow.Box(w=8, h=3)
        .anchor("W")
        .label("Falha do sensor E1S1")
        .fill("")
    )

    d += flow.Line().left(d.unit * 9).at(step2.W)
    d += flow.Arrow().down(d.unit / 2).label("temp1")
    d += (fail_step2 := flow.Box().label("19").fill(""))
    d += flow.Line().right(d.unit / 2).at(fail_step2.E)
    d += (
        fail_act2 := flow.Box(w=8, h=3)
        .anchor("W")
        .label("Falha do sensor E1S1")
        .fill("")
    )

    # ============== End ============== #
    d += flow.Line().down(d.unit).at(step2.S).label("!E1S1")
    d += flow.Line().down(d.unit).label("")
    d += (
        test1 := elm.EncircleBox(
            [act1, act2, fail_step1, fail_step2, fail_act1, fail_act2], padx=0.8
        )
        .linestyle("--")
        .linewidth(2)
        .color("blue")
        .label(
            "Teste 2 (testa o sensor de presença de peça na alimentação)",
            loc="left",
            rotate=90,
        )
    )


def teste3(d):
    # ============== Steps ============== #
    d += (step1 := flow.Box().label("8").fill(""))
    d += flow.Arrow().down().label("E1S3")
    d += (step2 := flow.Box().label("9").fill(""))
    d += flow.Arrow().down().label("E1S2")
    d += (step3 := flow.Box().label("10").fill(""))
    d += flow.Arrow().down().label("E1S4")
    d += (step4 := flow.Box().label("11").fill(""))

    # ============== Activities ============== #
    d += flow.Line().right(d.unit / 2).at(step1.E)
    d += (
        act1 := flow.Box(w=8, h=3)
        .anchor("W")
        .label("Oscilador lado de \nalimentação (E1Y5) e \ninicia temporizador1")
        .fill("")
    )

    d += flow.Line().right(d.unit / 2).at(step2.E)
    d += (
        act2 := flow.Box(w=8, h=3)
        .anchor("W")
        .label("Fixa peça na ventosa \n(E1Y2) reinicia \ntemporizador1")
        .fill("")
    )

    d += flow.Line().right(d.unit / 2).at(step3.E)
    d += (
        act3 := flow.Box(w=8, h=3)
        .anchor("W")
        .label("Oscilador lado do \nelevador (E1Y3) \nreinicia temporizador1")
        .fill("")
    )

    d += flow.Line().right(d.unit / 2).at(step4.E)
    d += (
        act4 := flow.Box(w=8, h=3)
        .anchor("W")
        .label("Desfixa peça da \nventosa (E1Y3) \nreinicia temporizador1")
        .fill("")
    )

    # ============== Fail test ============== #
    d += flow.Line().left(d.unit * 4).at(step1.W)
    d += flow.Arrow().down(d.unit / 2).label("temp1")
    d += (fail_step1 := flow.Box().label("13").fill(""))
    d += flow.Line().right(d.unit / 2).at(fail_step1.E)
    d += (
        fail_act1 := flow.Box(w=8, h=3)
        .anchor("W")
        .label("Falha do sensor E1S3 \nou falha do avanço do \noscilador")
        .fill("")
    )

    d += flow.Line().left(d.unit * 4).at(step2.W)
    d += flow.Arrow().down(d.unit / 2).label("temp1")
    d += (fail_step2 := flow.Box().label("14").fill(""))
    d += flow.Line().right(d.unit / 2).at(fail_step2.E)
    d += (
        fail_act2 := flow.Box(w=8, h=3)
        .anchor("W")
        .label("falha do sensor E1S2 \nou falha da fixação da \nventosa")
        .fill("")
    )

    d += flow.Line().left(d.unit * 4).at(step3.W)
    d += flow.Arrow().down(d.unit / 2).label("temp1")
    d += (fail_step3 := flow.Box().label("15").fill(""))
    d += flow.Line().right(d.unit / 2).at(fail_step3.E)
    d += (
        fail_act3 := flow.Box(w=8, h=3)
        .anchor("W")
        .label("falha do sensor E1S4 ou\nfalha do retorno do\n oscilador")
        .fill("")
    )

    d += flow.Line().left(d.unit * 4).at(step4.W)
    d += flow.Arrow().down(d.unit / 2).label("temp1")
    d += (fail_step4 := flow.Box().label("16").fill(""))
    d += flow.Line().right(d.unit / 2).at(fail_step4.E)
    d += (
        fail_act4 := flow.Box(w=8, h=3)
        .anchor("W")
        .label("falha do sensor E1S2 ou\nfalha para desfixar\n peça da ventosa")
        .fill("")
    )

    # ============== End ============== #
    d += flow.Line().down(d.unit).at(step4.S).label("!E1S2")
    d += flow.Arrow().down(d.unit).label("")
    d += (
        test1 := elm.EncircleBox(
            [
                act1,
                act2,
                act3,
                act4,
                fail_step1,
                fail_step2,
                fail_step3,
                fail_step4,
                fail_act1,
                fail_act2,
                fail_act3,
                fail_act4,
            ],
            padx=0.8,
        )
        .linestyle("--")
        .linewidth(2)
        .color("green")
        .label("Teste 3 (testa o cilindro oscilador)", loc="left", rotate=90)
    )

    return d


def teste4(d):
    # ============== Steps ============== #
    d += (step1 := flow.Box().label("aux1").fill(""))

    # ============== Activities ============== #
    d += flow.Line().right(d.unit / 2).at(step1.E)
    d += (
        act1 := flow.Box(w=8, h=3)
        .anchor("W")
        .label("Move oscilador\npara alimentação\n (E1Y5)")
        .fill("")
    )

    # ============== End ============== #
    d += flow.Line().down(d.unit).at(step1.S).label("E1S3")
    d += (dot := dsp.Dot())

    return dot


def teste5(d, dot):
    d += flow.Line().left(d.unit * 6).at(dot.center).label("")
    d += flow.Arrow().down(d.unit).label("Botão peça laranja")
    # ============== Steps ============== #
    d += (step1 := flow.Box().label("20").fill(""))
    d += flow.Arrow().down().label("E2B5")
    d += (step2 := flow.Box().label("21").fill(""))
    d += flow.Arrow().down().label("E1B6")
    d += (step3 := flow.Box().label("22").fill(""))
    d += flow.Arrow().down().label("E1B4")
    d += (step4 := flow.Box().label("23").fill(""))

    # ============== Activities ============== #
    d += flow.Line().right(d.unit / 2).at(step1.E)
    d += (
        act1 := flow.Box(w=8, h=3)
        .anchor("W")
        .label("Peça laranja \n (E2B5) ?")
        .fill("")
    )

    d += flow.Line().right(d.unit / 2).at(step2.E)
    d += (
        act2 := flow.Box(w=8, h=3)
        .anchor("W")
        .label("Presença de peça \n(E1B7) e reinicia \ntemporizador1")
        .fill("")
    )

    d += flow.Line().right(d.unit / 2).at(step3.E)
    d += (
        act3 := flow.Box(w=8, h=3)
        .anchor("W")
        .label("Avança cilindro (E2Y3) \n e reinicia temporizador1")
        .fill("")
    )

    d += flow.Line().right(d.unit / 2).at(step4.E)
    d += (
        act4 := flow.Box(w=8, h=3)
        .anchor("W")
        .label("Recua cilindro (E2Y3) \n e reinicia temporizador1")
        .fill("")
    )

    # ============== Fail test ============== #
    d += flow.Line().left(d.unit * 4).at(step1.W)
    d += flow.Arrow().down(d.unit / 2).label("temp1")
    d += (fail_step1 := flow.Box().label("25").fill(""))
    d += flow.Line().right(d.unit / 2).at(fail_step1.E)
    d += (
        fail_act1 := flow.Box(w=8, h=3)
        .anchor("W")
        .label("Falha do sensor\nótico E2B5")
        .fill("")
    )

    d += flow.Line().left(d.unit * 4).at(step2.W)
    d += flow.Arrow().down(d.unit / 2).label("temp1")
    d += (fail_step2 := flow.Box().label("26").fill(""))
    d += flow.Line().right(d.unit / 2).at(fail_step2.E)
    d += (
        fail_act2 := flow.Box(w=8, h=3)
        .anchor("W")
        .label("Falha do sensor\nde presença \nE2B6")
        .fill("")
    )

    d += flow.Line().left(d.unit * 4).at(step3.W)
    d += flow.Arrow().down(d.unit / 2).label("temp1")
    d += (fail_step3 := flow.Box().label("27").fill(""))
    d += flow.Line().right(d.unit / 2).at(fail_step3.E)
    d += (
        fail_act3 := flow.Box(w=8, h=3)
        .anchor("W")
        .label("Falha do sensor E2B4\nou falha do avanço\ndo cilindro")
        .fill("")
    )

    d += flow.Line().left(d.unit * 4).at(step4.W)
    d += flow.Arrow().down(d.unit / 2).label("temp1")
    d += (fail_step4 := flow.Box().label("28").fill(""))
    d += flow.Line().right(d.unit / 2).at(fail_step4.E)
    d += (
        fail_act4 := flow.Box(w=8, h=3)
        .anchor("W")
        .label("Falha do sensor E2B3\nou falha do recuo\ndo cilindro")
        .fill("")
    )

    # ============== End ============== #
    d += flow.Line().down(d.unit).at(step4.S).label("!E1S2")
    d += flow.Line().down(d.unit * 2.672).label("")
    d += flow.Line().right(d.unit * 6).label("")
    d += (
        test1 := elm.EncircleBox(
            [
                act1,
                act2,
                act3,
                act4,
                fail_step1,
                fail_step2,
                fail_step3,
                fail_step4,
                fail_act1,
                fail_act2,
                fail_act3,
                fail_act4,
            ],
            padx=0.8,
        )
        .linestyle("--")
        .linewidth(2)
        .color("indigo")
        .label(
            "Teste 4 (testa o cilindro de descarte e os sensores ótico e capacitivo)",
            loc="left",
            rotate=90,
        )
    )


def teste6(d, dot):
    d += flow.Line().right(d.unit * 6).at(dot.center).label("")
    d += flow.Arrow().down(d.unit).label("Botão peça metálica")
    # ============== Steps ============== #
    d += (step1 := flow.Box().label("29").fill(""))
    d += flow.Arrow().down().label("E2B7")
    d += (step2 := flow.Box().label("30").fill(""))
    d += flow.Arrow().down().label("E2B2")
    d += (step3 := flow.Box().label("31").fill(""))
    d += flow.Arrow().down().label("E2B4")
    d += (step4 := flow.Box().label("32").fill(""))
    d += flow.Arrow().down().label("E2B3")
    d += (step5 := flow.Box().label("33").fill(""))

    # ============== Activities ============== #
    d += flow.Line().right(d.unit / 2).at(step1.E)
    d += (
        act1 := flow.Box(w=8, h=3).anchor("W").label("Peça metálica\n(E2B6) ?").fill("")
    )

    d += flow.Line().right(d.unit / 2).at(step2.E)
    d += (
        act2 := flow.Box(w=8, h=3)
        .anchor("W")
        .label("Avança elevador (E2Y2)\ne reinicia temporizador1")
        .fill("")
    )

    d += flow.Line().right(d.unit / 2).at(step3.E)
    d += (
        act3 := flow.Box(w=8, h=3)
        .anchor("W")
        .label("Avança cilindro (E2Y3)\ne reinicia temporizador1")
        .fill("")
    )

    d += flow.Line().right(d.unit / 2).at(step4.E)
    d += (
        act4 := flow.Box(w=8, h=3)
        .anchor("W")
        .label("Recua cilindro (E2Y3)\ne reinicia temporizador1")
        .fill("")
    )

    d += flow.Line().right(d.unit / 2).at(step5.E)
    d += (
        act5 := flow.Box(w=8, h=3)
        .anchor("W")
        .label("Recua elevador (E2Y2)\ne reinicia temporizador1")
        .fill("")
    )

    # ============== Fail test ============== #
    d += flow.Line().left(d.unit * 4).at(step1.W)
    d += flow.Arrow().down(d.unit / 2).label("temp1")
    d += (fail_step1 := flow.Box().label("35").fill(""))
    d += flow.Line().right(d.unit / 2).at(fail_step1.E)
    d += (
        fail_act1 := flow.Box(w=8, h=3)
        .anchor("W")
        .label("Falha do sensor\nmetálico E2B7")
        .fill("")
    )

    d += flow.Line().left(d.unit * 4).at(step2.W)
    d += flow.Arrow().down(d.unit / 2).label("temp1")
    d += (fail_step2 := flow.Box().label("36").fill(""))
    d += flow.Line().right(d.unit / 2).at(fail_step2.E)
    d += (
        fail_act2 := flow.Box(w=8, h=3)
        .anchor("W")
        .label("Falha do sensor E2B2 \nou falha do avanço do \nelevador")
        .fill("")
    )

    d += flow.Line().left(d.unit * 4).at(step3.W)
    d += flow.Arrow().down(d.unit / 2).label("temp1")
    d += (fail_step3 := flow.Box().label("37").fill(""))
    d += flow.Line().right(d.unit / 2).at(fail_step3.E)
    d += (
        fail_act3 := flow.Box(w=8, h=3)
        .anchor("W")
        .label("Falha do sensor E2B4 \nou falha do avanço do \ncilindro de descarte")
        .fill("")
    )

    d += flow.Line().left(d.unit * 4).at(step4.W)
    d += flow.Arrow().down(d.unit / 2).label("temp1")
    d += (fail_step4 := flow.Box().label("38").fill(""))
    d += flow.Line().right(d.unit / 2).at(fail_step4.E)
    d += (
        fail_act4 := flow.Box(w=8, h=3)
        .anchor("W")
        .label("Falha do sensor E2B3 \nou falha do recuo do \ncilindro de descarte")
        .fill("")
    )

    d += flow.Line().left(d.unit * 4).at(step5.W)
    d += flow.Arrow().down(d.unit / 2).label("temp1")
    d += (fail_step5 := flow.Box().label("39").fill(""))
    d += flow.Line().right(d.unit / 2).at(fail_step5.E)
    d += (
        fail_act5 := flow.Box(w=8, h=3)
        .anchor("W")
        .label("Falha do sensor E2B1 \nou falha do recup do \nelevador")
        .fill("")
    )

    # ============== End ============== #
    d += flow.Line().down(d.unit).at(step5.S).label("E2B1")
    d += flow.Line().down(d.unit).label("")
    d += flow.Line().left(d.unit * 6).label("")
    d += (
        test1 := elm.EncircleBox(
            [
                act1,
                act2,
                act3,
                act4,
                act5,
                fail_step1,
                fail_step2,
                fail_step3,
                fail_step4,
                fail_step5,
                fail_act1,
                fail_act2,
                fail_act3,
                fail_act4,
                fail_act5,
            ],
            padx=0.8,
        )
        .linestyle("--")
        .linewidth(2)
        .color("violet")
        .label(
            "Teste 5 (testa o cilindro elevador e sensor metálico)",
            loc="left",
            rotate=90,
        )
    )


def teste7(d):
    d += flow.Arrow().down(d.unit).label("")
    # ============== Steps ============== #
    d += (step1 := flow.Box().label("aux2").fill(""))

    # ============== Activities ============== #
    d += flow.Line().right(d.unit / 2).at(step1.E)
    d += (
        act1 := flow.Box(w=8, h=3)
        .anchor("W")
        .label("Move oscilador\npara elevador\n (E1Y4)")
        .fill("")
    )

    # ============== End ============== #
    d += flow.Line().down(d.unit).at(step1.S).label("")


with schemdraw.Drawing() as d:
    d.config(fontsize=6, inches_per_unit=1)

    d += (b := flow.Start().label("Start"))
    d += flow.Arrow().down().label("Botão de depuração")

    teste1(d)
    teste2(d)
    dot = teste4(d)
    teste5(d, dot)
    teste6(d, dot)
    d += (dot := dsp.Dot())
    teste7(d)

    d += flow.Line().left(d.unit * 12).label("")
    d += flow.Line().up(d.unit * 33.25).label("E1S4")
    d += flow.Arrow().right(d.unit * 11.45).label("")

    d.save("./grafcet2.svg")
    # d.draw()
