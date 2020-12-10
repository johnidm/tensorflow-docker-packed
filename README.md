# Machine Learning Docker Packed - TensorFlow

### Makefile commands

- `make install-dependences`:
- `make jupyter-notebook`:
- `make docker-run`:
- `make test-run`:

### Testing endpoints

##### Home

```
curl -i -X GET \
 'http://0.0.0.0:8000/'
```

##### Classifier
```
curl -i -X POST \
   -H "Content-Type:application/json" \
   -d \
'{
  "text": "Na data de 13/05/13, as partes celebraram Contrato de Financiamento com Garantia de Alienação Fiduciária (doc. Anexo contrato), sob o nº 30364- 550366207, aditado em 15/02/16, para pagamento no valor total de R$ 30.000,00, em 26 parcelas mensais e consecutivas de R$ 1.207,71. Tendo como objeto o bem com as seguintes características: Marca: GM Modelo: MONTANA 14 Ano: 2012 Cor: PRATA Placa: FDA9179 RENAVAM: 00464512247 CHASSI: BGCA8oXoDB1i00527"
}
  ' \
 'http://0.0.0.0:8000/do'
```

[API documentation](http://127.0.0.1:8000/docs)