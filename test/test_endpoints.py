def test_home(client):
    response = client.get("/")
    assert response.status_code == 200

    expected = {
        "status": "Running RESTful Machine Learning",
        "versions": {"flask": "1.1.2", "numpy": "1.18.5", "tensorflow": "2.3.1"},
    }
    assert expected == response.json

def test_classification(client):
    text = """Na data de 13/05/13, as partes celebraram Contrato de Financiamento
        com Garantia de Alienação Fiduciária (doc. Anexo contrato), sob o nº
        30364- 550366207, aditado em 15/02/16, para pagamento no
        valor total de R$ 30.000,00, em 26 parcelas mensais e consecutivas de
        R$ 1.207,71. Tendo como objeto o bem com as seguintes características:
        Marca: GM Modelo: MONTANA 14 Ano: 2012 Cor: PRATA Placa: FDA9179
        RENAVAM: 00464512247 CHASSI: BGCA8oXoDB1i00527
        """

    response = client.post(
        "/do",
        json={
            "text": text
        },
    )

    assert response.status_code == 201

    excepted = {
        "targets": {
            "0": "0.05",
            "1": "0.0",
            "2": "0.0",
            "3": "0.0",
            "4": "0.95",
            "5": "0.0",
            "6": "0.0",
        },       
        "text": text,
    }
    assert excepted == response.json
