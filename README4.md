# Monitoramento de Queimadas na Amazônia

Este projeto tem como objetivo monitorar as queimadas na Amazônia e apresentar informações diárias atualizadas sobre os focos de incêndio detectados. Abaixo, você pode visualizar as queimadas mais recentes, com detalhes sobre localização, satélite que realizou a detecção, e outros fatores relevantes.

## Estrutura dos Dados

Cada entrada na tabela representa um foco de incêndio com as seguintes informações:

- **ID:** Identificador único do foco de incêndio.
- **Latitude/Longitude:** Coordenadas geográficas do foco detectado. Para visualizar o local exato, insira estas coordenadas no Google Maps ou outro aplicativo de mapas.
- **Data/Hora GMT:** Data e hora da detecção em formato GMT (Greenwich Mean Time).
- **Satélite:** Satélite responsável pela detecção do foco de incêndio.
- **Município, Estado e País:** Localização administrativa do foco detectado.
- **Dias sem Chuva:** Número de dias consecutivos sem precipitação na região, o que pode indicar um aumento no risco de incêndio.
- **Precipitação:** Quantidade de chuva (em milímetros) registrada no local.
- **Risco de Fogo:** Índice que indica a probabilidade de ocorrência de incêndio, baseado em fatores como condições climáticas e quantidade de combustível disponível.
- **Bioma:** Bioma onde o foco foi identificado, como Amazônia, Cerrado, ou Mata Atlântica.
- **FRP (Fire Radiative Power):** Potência radiativa do fogo, que mede a intensidade do incêndio. Focos com FRP mais alto indicam incêndios mais intensos.

## Visualização Gráfica

Se você deseja visualizar de forma gráfica onde as queimadas estão ocorrendo, copie as coordenadas de latitude e longitude mais recentes e cole no Google Maps. Isso permite uma compreensão espacial mais clara da distribuição dos focos de incêndio. Alternativamente, você também pode usar a descrição de localização (Município, Estado e País) para identificar a região afetada.

## Informação Adicional

As queimadas na Amazônia não apenas afetam a biodiversidade local, mas também têm implicações globais, contribuindo para o aquecimento global e a emissão de gases de efeito estufa. O monitoramento contínuo é essencial para entender e mitigar os impactos desses incêndios, além de auxiliar na gestão de políticas ambientais e ações de preservação.

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d4317bf7-3890-3006-899f-83dcfb6f3ba7 | -9.6303 | -48.545502 | 2025-07-29 00:22:00 | METOP-B | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d0120aff-6c1e-3485-ba71-4a1a4b2c0b17 | -3.2741 | -49.144699 | 2025-07-29 00:22:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a64f9073-cc4e-3608-bf00-353acf24bf0c | -2.985 | -48.5979 | 2025-07-29 00:22:00 | METOP-B | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0d70a6ed-9a06-33fb-86a4-d4b7e101ae63 | -14.0002 | -44.614601 | 2025-07-29 00:22:00 | METOP-B | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 8399bc0c-1bc7-3201-b863-ccd7e5837868 | -14.4929 | -46.536098 | 2025-07-29 00:22:00 | METOP-B | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 962c589d-cc8f-375b-8207-bab208be2eef | -11.3482 | -51.233501 | 2025-07-29 00:22:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 01c0ee71-6cae-36d8-bafd-d5f47a7d5caa | -9.9955 | -48.111801 | 2025-07-29 00:22:00 | METOP-B | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2aeb19c3-10e4-3759-9d6a-6141188fa505 | -8.8884 | -47.332199 | 2025-07-29 00:22:00 | METOP-B | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 28b67f9b-fab7-3380-a531-bb71a701047a | -10.5255 | -50.243698 | 2025-07-29 00:22:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a6b45010-bf81-345e-ac34-e6141aa159c6 | -7.8042 | -44.9505 | 2025-07-29 00:22:00 | METOP-B | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 6c9ce9fa-8fc9-3596-8b14-917a7920f964 | -8.5027 | -43.312099 | 2025-07-29 00:22:00 | METOP-B | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| ddc652c9-ac09-38fe-a2b8-fa74ab35f9f9 | -5.3541 | -45.259602 | 2025-07-29 00:22:00 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4c081309-baa4-3355-8c2d-7c9f4bc5d1fa | -13.0978 | -52.130501 | 2025-07-29 00:22:00 | METOP-B | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b54f5a28-777d-38c6-bdde-82ed361e7607 | -9.3967 | -45.4907 | 2025-07-29 00:22:00 | METOP-B | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 23504907-d219-335d-8461-5600139785e1 | -5.6439 | -44.351601 | 2025-07-29 00:22:00 | METOP-B | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 789109c1-c2a1-3731-aab7-611d26817ab0 | -6.3946 | -53.339699 | 2025-07-29 00:22:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 38c3ab89-003b-364b-b226-17165e8e619c | -3.3555 | -47.157001 | 2025-07-29 00:22:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e9cc92c6-0dfa-39b0-8431-e4bfbb8a972e | -2.9039 | -48.287498 | 2025-07-29 00:22:00 | METOP-B | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 18d28bcd-aace-3921-aa21-3efed0c3d248 | -2.8941 | -48.2897 | 2025-07-29 00:22:00 | METOP-B | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3170dded-59a8-3bf0-b994-3933101cd78a | -6.4044 | -53.337601 | 2025-07-29 00:22:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b76ebd19-60c3-33ad-96c3-f5435e1cba88 | -7.8499 | -46.7229 | 2025-07-29 00:22:00 | METOP-B | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 71f41687-d9d9-3611-94d6-8e166b465952 | -2.8923 | -48.281601 | 2025-07-29 00:22:00 | METOP-B | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bf19babd-f37d-33f5-8193-a8e46caf37f9 | -15.1271 | -45.312698 | 2025-07-29 00:22:00 | METOP-B | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 33eb11b9-efc7-3f95-9ed0-cc9d2dea7168 | -7.8143 | -50.2253 | 2025-07-29 00:22:00 | METOP-B | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d279c540-8075-330a-8dfd-5e9ab4e0e21b | -9.0825 | -50.837299 | 2025-07-29 00:22:00 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 039785c8-85be-3a4c-890c-e71b5b8e48f3 | -3.7382 | -49.056301 | 2025-07-29 00:22:00 | METOP-B | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5d7b3668-e613-38ba-b05c-84d0314a1c73 | -11.27 | -44.646301 | 2025-07-29 00:22:00 | METOP-B | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 0cb79a84-d0d4-3d47-bccd-b8376efd2ba8 | -14.5009 | -46.526001 | 2025-07-29 00:22:00 | METOP-B | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 79b1501c-9379-3e26-8cac-2f1757ec9110 | -7.9175 | -44.0877 | 2025-07-29 00:22:00 | METOP-B | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| db01f5c9-dfa9-3355-a23f-7a660232fc58 | -2.8325 | -52.3484 | 2025-07-29 00:22:00 | METOP-B | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 51710005-9d1b-3f6f-962f-1c31cf76fd1a | -5.8463 | -44.207901 | 2025-07-29 00:22:00 | METOP-B | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 637faf73-e2f7-39b6-a0af-04acaf83779e | -16.667101 | -47.714298 | 2025-07-29 00:22:00 | METOP-B | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 869ef65e-e2a5-312a-9869-9e66cc2cf1a1 | -14.3759 | -50.321999 | 2025-07-29 00:22:00 | METOP-B | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| cda117b5-1497-35ec-898f-7cf9074c506c | -5.3443 | -45.261902 | 2025-07-29 00:22:00 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 44092b1c-da93-3dd1-8949-4e031d176d73 | -14.127 | -45.277901 | 2025-07-29 00:22:00 | METOP-B | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ef5707bd-dde3-3f01-a4cf-a71141b885b6 | -5.3469 | -45.273201 | 2025-07-29 00:22:00 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b5098077-29dd-3ded-ac08-c95663cc401b | -18.446501 | -54.643501 | 2025-07-29 00:22:00 | METOP-B | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| c8e52052-fc76-3290-abdb-c5a64f644b35 | -12.9905 | -44.8867 | 2025-07-29 00:22:00 | METOP-B | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 9c54f611-1822-30bd-aa81-eac1016976c1 | -14.0024 | -44.6241 | 2025-07-29 00:22:00 | METOP-B | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 01274709-e448-3f55-8a9e-2a189c41bca4 | -14.3196 | -48.645302 | 2025-07-29 00:22:00 | METOP-B | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 11e1ffe6-587e-3753-84e7-bdc114d7bbfb | -6.3963 | -53.347599 | 2025-07-29 00:22:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| beeb8564-ec04-3bdf-8fb9-4136ad451fd2 | -7.9272 | -44.0853 | 2025-07-29 00:22:00 | METOP-B | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 90ce6ddb-237a-3253-8c7a-895da738d680 | -14.3744 | -50.314602 | 2025-07-29 00:22:00 | METOP-B | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| ec93258e-9876-3934-a3ce-e697077f57b4 | -11.4346 | -45.119099 | 2025-07-29 00:22:00 | METOP-B | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d2847f49-4896-3480-8c7d-8c6f1853fb05 | -8.1356 | -49.500099 | 2025-07-29 00:22:00 | METOP-B | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5d3c761b-b2b5-3d8f-9ac2-19be2fb02102 | -15.8124 | -41.883999 | 2025-07-29 00:22:00 | METOP-B | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| dc42adad-fb9b-3f88-9e50-0ba19e4e9716 | -7.7313 | -51.100101 | 2025-07-29 00:22:00 | METOP-B | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0481755b-53e1-33b3-baf4-14bcea643ce5 | -11.741 | -48.171299 | 2025-07-29 00:22:00 | METOP-B | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 402c71cb-11aa-348d-8353-bf6a11b1055f | -6.8431 | -46.3839 | 2025-07-29 00:22:00 | METOP-B | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8d4c1b4a-4cfd-351c-970d-1409e9f125f1 | -14.318 | -48.638302 | 2025-07-29 00:22:00 | METOP-B | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| e7444c1b-3cc2-3564-8282-4bf31b85ed46 | -8.1371 | -49.507 | 2025-07-29 00:22:00 | METOP-B | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1228041f-2b27-3b72-97b8-2117a40f8b31 | -9.0841 | -50.844299 | 2025-07-29 00:22:00 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 130b93b7-54a2-3c0e-8d94-1bd73321c5b0 | -18.453699 | -54.627701 | 2025-07-29 00:22:00 | METOP-B | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 42e12e9b-80e2-39dd-a821-4a208763edbf | -8.9499 | -46.751999 | 2025-07-29 00:22:00 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5359916e-7b3b-3f41-b1a0-6ac899dfe72b | -6.3911 | -53.3237 | 2025-07-29 00:22:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 122e0ec2-1aee-39b6-ae8d-5b7fda7f85bd | -9.7265 | -48.288799 | 2025-07-29 00:22:00 | METOP-B | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 545a2d9f-fcb4-347b-aef2-beb6073ba224 | -5.8494 | -44.221001 | 2025-07-29 00:22:00 | METOP-B | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2ea896fb-0781-3512-9f91-e80d92f07a96 | -6.4275 | -53.349201 | 2025-07-29 00:22:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 95f9cd0f-e9b0-36a7-8fe8-d2dd884a6562 | -7.2441 | -43.0467 | 2025-07-29 00:22:00 | METOP-B | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 8341c4d1-ad6d-3888-8dd4-54db0ae75277 | -6.9041 | -52.852001 | 2025-07-29 00:22:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c130be06-6a0b-3a47-9b11-e5f7f47c8882 | -6.383 | -53.333801 | 2025-07-29 00:22:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dba36fc0-b19b-3156-b62f-8853b29dad66 | -15.4896 | -50.057201 | 2025-07-29 00:22:00 | METOP-B | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| d258ac15-91d0-3739-bad5-6f29ebd60aaa | -6.409 | -53.3116 | 2025-07-29 00:22:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a9afd5c9-4a2a-35f4-b609-b8f7a612ae26 | -7.8576 | -46.711899 | 2025-07-29 00:22:00 | METOP-B | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 30e22271-700b-3f23-a883-ac1c10a81652 | -7.8519 | -46.731499 | 2025-07-29 00:22:00 | METOP-B | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3da90559-1335-31d1-9d72-4d9776bc93b8 | -16.612101 | -49.447601 | 2025-07-29 00:22:00 | METOP-B | TRINDADE | GOIÁS | Brasil | 5221403 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| cd8abc74-119a-3f10-91b9-66cf28eb5ad4 | -4.127 | -49.271 | 2025-07-29 00:22:00 | METOP-B | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 285f5331-67ee-3eed-a5f0-766e53c774a6 | -2.8843 | -48.291901 | 2025-07-29 00:22:00 | METOP-B | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 973998a2-2c96-3948-a59c-d55c218639e6 | -6.3928 | -53.331699 | 2025-07-29 00:22:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5dd41ce6-0451-3c5f-bdc9-f5ee18e79ef7 | -3.7463 | -49.0466 | 2025-07-29 00:22:00 | METOP-B | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c1f6c237-35e7-3ffd-9760-8deb3a7f5870 | -18.448999 | -54.657501 | 2025-07-29 00:22:00 | METOP-B | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 2958ac86-20f8-3131-bfa4-48e126c5152f | -6.9058 | -52.859699 | 2025-07-29 00:22:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d1a011bb-8ee9-37a6-8f72-619e2b60369e | -9.3944 | -45.480999 | 2025-07-29 00:22:00 | METOP-B | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| a1b3f31d-71d0-3abf-96a1-2ed4cc4ce4d1 | -10.527 | -50.250702 | 2025-07-29 00:22:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 082e1a04-f778-383c-9d4b-df7f8af79479 | -5.3567 | -45.270901 | 2025-07-29 00:22:00 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2146c19b-8e39-3cbb-b902-bbd1131d9271 | -2.8921 | -48.2977 | 2025-07-29 00:30:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 98.2 |
| 693defaa-5d03-3cdf-9476-c8ae34e36fb6 | -7.8568 | -46.7304 | 2025-07-29 00:30:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 104.7 |
| b967701c-52a4-3871-b9de-e08f15dbe1e6 | -18.4486 | -54.6674 | 2025-07-29 00:30:00 | GOES-19 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 166.0 |
| 952c185b-0476-36c3-8694-590c93fcf7bb | -11.4201 | -45.1181 | 2025-07-29 00:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 57.8 |
| a4efc8a1-b6ab-3400-b6e2-ba93d5c81185 | -18.449 | -54.6462 | 2025-07-29 00:30:00 | GOES-19 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 64.4 |
| 57c8a331-c9e8-359a-9571-c0df0211c54d | -7.2597 | -43.0645 | 2025-07-29 00:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 110.9 |
| e5f16567-ba93-3b55-ac55-d643bdabcc10 | -11.7317 | -48.1849 | 2025-07-29 00:30:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 89.3 |
| 278db730-056b-3b9c-a0c0-3954a50476bf | -7.2408 | -43.0664 | 2025-07-29 00:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 176.1 |
| 018fd431-75b7-37e7-ba73-8cb603f3a908 | -7.4541 | -49.4018 | 2025-07-29 00:30:00 | GOES-19 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 80.1 |
| e31a3f46-e4b5-30a2-a7c7-4ebdb8b7ea10 | -7.9256 | -44.0937 | 2025-07-29 00:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 81.3 |
| 3da50014-9ed0-3c5e-8784-144ef314ed4f | -7.9445 | -44.0918 | 2025-07-29 00:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 65.1 |
| 48c63dae-d7ea-305d-8657-c707d98e5c14 | -18.4287 | -54.6704 | 2025-07-29 00:30:00 | GOES-19 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 69.4 |
| 32c6da97-9fd5-33dd-961a-fa72447118ef | -5.363 | -45.2695 | 2025-07-29 00:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 80.6 |
| 110d1ddd-773b-3435-9190-1e142ebe2cf3 | -11.4393 | -45.1154 | 2025-07-29 00:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 94.0 |
| a7f956f4-588b-3a88-afcc-67dc022abaa4 | -7.2411 | -43.0428 | 2025-07-29 00:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 66.5 |
| 108ec13b-065e-31e9-ae5f-8d7b32b17205 | -7.4728 | -49.4004 | 2025-07-29 00:30:00 | GOES-19 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 30931eec-f1dd-380b-913f-127888578fa7 | -18.4685 | -54.6645 | 2025-07-29 00:30:00 | GOES-19 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 57.0 |
| 043634b9-6b7d-3880-9ac7-65f5b5fac4ba | -11.4389 | -45.1385 | 2025-07-29 00:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 50.6 |
| 97a0724d-581c-318b-86ff-23636cd43440 | -11.7508 | -48.1825 | 2025-07-29 00:30:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 99.8 |
| c5241166-365e-344e-b37d-1ad0820f36f1 | -18.4287 | -54.6704 | 2025-07-29 00:40:00 | GOES-19 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 66.1 |
| c1f20c8c-8d18-35a0-9989-c4a7cac0dcf5 | -7.2597 | -43.0645 | 2025-07-29 00:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 98.9 |
| ea575c05-e6a1-3fbd-a846-195c812eb303 | -11.7508 | -48.1825 | 2025-07-29 00:40:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 103.5 |
| b856dbf4-10ff-3c95-b8fa-381a8f14046d | -11.4201 | -45.1181 | 2025-07-29 00:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 63.5 |
| b4dbb458-32de-3377-a1e2-4b50ede257dd | -7.9256 | -44.0937 | 2025-07-29 00:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 80.7 |
| bededda3-b0fa-309e-840d-61b0a5d046a0 | -7.4541 | -49.4018 | 2025-07-29 00:40:00 | GOES-19 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 76.0 |


[Clique aqui para ver as próximas entradas](README5.md)
