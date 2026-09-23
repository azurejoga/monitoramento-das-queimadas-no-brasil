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

## Dados Diários - Página 87

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6f017c69-f179-3546-bb1b-072eb8377844 | -6.04206 | -53.2721 | 2026-09-23 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 362b8b50-2f23-3766-811e-c1e1427c0141 | -10.25557 | -50.20562 | 2026-09-23 05:04:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a89ad97d-cff9-37fc-89dd-c201758357b9 | -9.15758 | -61.37073 | 2026-09-23 05:04:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 30576283-4601-3933-afb5-f9d4120c513a | -8.33277 | -50.82838 | 2026-09-23 05:04:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d806b73f-4bb0-3538-bd27-1b2b9ac061bd | -7.39464 | -55.21385 | 2026-09-23 05:04:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3a55a178-c0f3-375b-8c8f-cfa5c150b2d7 | -6.60582 | -43.74048 | 2026-09-23 05:04:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| c42d9d1c-e6d5-3a94-9a03-a83e9d470551 | -3.42765 | -61.32616 | 2026-09-23 05:04:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8c2b0f12-340f-3a3d-8a1a-f83698364090 | -6.94114 | -52.60081 | 2026-09-23 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d41bcc8d-1793-3199-8227-27af213cc679 | -11.10973 | -51.05441 | 2026-09-23 05:04:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 153c04b7-4ec3-3374-beac-700459c2a5fe | -6.61409 | -59.95311 | 2026-09-23 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9d138c9c-2579-32a8-8b9f-e8b970458faf | -5.99951 | -44.26132 | 2026-09-23 05:04:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 208f4100-4fe3-32b7-8e79-ff6981f8186d | -7.17233 | -48.62714 | 2026-09-23 05:04:00 | NPP-375D | MURICILÂNDIA | TOCANTINS | Brasil | 1713957 | 17 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 37cfe8ab-43ae-395d-8e1e-792bceb03767 | -8.28607 | -54.77728 | 2026-09-23 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b8f0a0c7-56a6-395e-990b-07113b77bd04 | -11.65573 | -43.47406 | 2026-09-23 05:04:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 65926b03-bdd1-3487-9534-b85ffbb71a09 | -5.57018 | -52.02416 | 2026-09-23 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cdf33481-dd7a-37f0-9647-5dee93db08b5 | -6.64779 | -50.93409 | 2026-09-23 05:04:00 | NPP-375D | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3f2450a4-8e57-3449-8a5a-34ee6779d2ac | -8.08471 | -44.34615 | 2026-09-23 05:04:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6ee3b6f0-61fd-371e-bb3b-7f53d76db3e5 | -6.10087 | -44.15036 | 2026-09-23 05:04:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 45849b73-b9b6-30c7-997a-85fcbe195449 | -6.35488 | -58.28851 | 2026-09-23 05:04:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c086b3cb-3bed-3484-a7aa-aa1f5b0eccd3 | -10.45556 | -50.36166 | 2026-09-23 05:04:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9ea8ca6a-3a7f-3387-bb47-bb53cc20d66b | -5.76996 | -43.76891 | 2026-09-23 05:04:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6ef7eb96-bd36-3383-ae01-5a334085ca23 | -6.4423 | -48.4643 | 2026-09-23 05:04:00 | NPP-375D | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ad0ce4dd-eeee-319a-86b6-4e4bdd3c05f9 | -6.73725 | -59.42125 | 2026-09-23 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cddac869-a081-39cc-abf9-7be191538370 | -6.46202 | -49.8718 | 2026-09-23 05:04:00 | NPP-375D | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 48784ca5-2f37-3165-8ff8-e0ff102b476a | -3.92226 | -60.55466 | 2026-09-23 05:04:00 | NPP-375D | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3ddb9e35-172c-39ac-a5e0-689a8c828a1e | -9.04587 | -65.42027 | 2026-09-23 05:04:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bbef630d-def9-3b2a-bf17-c5724eaf5573 | -3.68812 | -60.57786 | 2026-09-23 05:04:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 57b5d644-0f83-3210-994e-a5acc1352bcb | -9.15732 | -61.37149 | 2026-09-23 05:04:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a625cceb-8b67-34ef-b8b7-63d7bcbcab2c | -6.27715 | -59.91919 | 2026-09-23 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a11f790b-305e-3d17-aa70-4caf31dc39f6 | -10.28633 | -50.52231 | 2026-09-23 05:04:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 85a98671-f36e-31be-8e92-7ef4b3ce99fa | -6.63712 | -59.93154 | 2026-09-23 05:04:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 16.9 |
| 5021d7f1-c324-3719-be8e-d033e9ee24f8 | -6.45686 | -54.98764 | 2026-09-23 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f397f47b-3f48-31c8-a183-c54efc872828 | -6.34925 | -57.77469 | 2026-09-23 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6c7c9a7b-1515-35ca-a92f-0aaad0955d82 | -6.30038 | -57.74048 | 2026-09-23 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9278356e-42fb-3417-944d-2b8d833dda1a | -7.55504 | -48.67729 | 2026-09-23 05:04:00 | NPP-375D | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 18520e90-3cc4-3b59-987a-d6f69772f5a8 | -4.09343 | -62.09806 | 2026-09-23 05:04:00 | NPP-375D | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f442a3d0-90f5-34a7-abb6-970f9e580c7d | -4.44412 | -55.07115 | 2026-09-23 05:04:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 537669ac-59eb-3b4f-b870-ca03d76b31fc | -10.70524 | -48.72048 | 2026-09-23 05:04:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ab8fea80-6bdc-37df-9af1-d208d98e8f75 | -3.78586 | -55.87949 | 2026-09-23 05:04:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 74a387af-729a-3328-ad66-1cf8df88daa6 | -4.04681 | -56.3152 | 2026-09-23 05:04:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 713637e2-20a1-3d39-9786-2fb3ee169633 | -6.68277 | -55.06228 | 2026-09-23 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8ef08e9f-dcce-3f03-b96d-611d93fb9272 | -5.79151 | -51.88434 | 2026-09-23 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a6c98031-1304-3190-8aef-0d6f619a3377 | -10.71136 | -48.70596 | 2026-09-23 05:04:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 42c5762f-f2c5-3050-a859-d384101c5794 | -7.55675 | -48.69201 | 2026-09-23 05:04:00 | NPP-375D | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | 1.5 |
| baa1ec36-e959-3260-8254-f730412d87fc | -5.85115 | -52.02603 | 2026-09-23 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9ed1a696-dd76-3fb1-ab0f-c58cd1006ebe | -9.04566 | -65.42118 | 2026-09-23 05:04:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 3e190e0b-c1d9-33ef-9f52-65fce944ba5d | -3.67407 | -55.51827 | 2026-09-23 05:04:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9f6cfcc6-64ab-393a-8122-d32abcae3303 | -7.58617 | -57.66383 | 2026-09-23 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 26fb6d59-28aa-3e7c-a875-29efad3ed69b | -4.08777 | -62.09704 | 2026-09-23 05:04:00 | NPP-375D | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5acda539-ad37-301d-a69e-f4255044aaf1 | -6.81427 | -59.43456 | 2026-09-23 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e0e57da1-a591-34bd-a8db-3546a41db235 | -6.62081 | -59.91992 | 2026-09-23 05:04:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 33bca205-e2f7-3ebe-a4b4-5c195c5956ae | -5.82238 | -52.07851 | 2026-09-23 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 43c2d30c-555c-3a37-8777-4ed631949e36 | -6.62142 | -57.98512 | 2026-09-23 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 10a6f3aa-69e1-3491-892c-1fd1cfe857e3 | -6.13688 | -43.85427 | 2026-09-23 05:04:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 52a7166a-4f34-3674-871b-6854f7eee6ac | -5.48129 | -51.23342 | 2026-09-23 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a9d1f81f-76ca-3e5d-b1f3-3511421d5ff6 | -8.62209 | -54.62323 | 2026-09-23 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 86475ded-82fe-3cf3-85bd-9b72edb5ea56 | -9.10448 | -61.43712 | 2026-09-23 05:04:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 724b3cfc-848b-3235-9876-8a71fc46c14e | -3.77763 | -60.74631 | 2026-09-23 05:04:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d2d07f55-8287-3bf0-b585-611cb7e537a4 | -6.89576 | -46.54184 | 2026-09-23 05:04:00 | NPP-375D | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e66222dc-88a2-3393-91ec-450cb0d4a394 | -6.67294 | -42.57067 | 2026-09-23 05:04:00 | NPP-375D | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | 8.9 |
| 06a19351-e0d8-393c-8d99-e9cd1f96c1fe | -5.12897 | -46.05332 | 2026-09-23 05:04:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 958caabf-c59a-3e21-bf94-afdee48fce49 | -7.88414 | -61.17727 | 2026-09-23 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 49a82746-2ec4-357b-a1a9-1c796e1fecba | -6.61111 | -43.74121 | 2026-09-23 05:04:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 28.1 |
| 43b0ab8a-7061-3583-85be-4ac8996287dc | -3.68654 | -60.55558 | 2026-09-23 05:04:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6a2913eb-5c39-341d-b13d-23ea80dcbc6f | -4.12722 | -54.24767 | 2026-09-23 05:04:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5fc1cc63-5282-3b00-9661-aea177061360 | -6.84138 | -55.3084 | 2026-09-23 05:04:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ed63c11c-9f1c-3fdc-80d8-8e7dbc738d45 | -10.26216 | -50.2354 | 2026-09-23 05:04:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| d9e92207-f469-32c5-ba9d-1b86aa9a63f5 | -5.92472 | -59.91969 | 2026-09-23 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 15.4 |
| edbf8a3e-53d0-3c66-9889-59d473f0c962 | -8.45598 | -51.48591 | 2026-09-23 05:04:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0c489dcc-c621-3aa5-9740-31fb9b1c253f | -6.61202 | -43.73468 | 2026-09-23 05:04:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 57.3 |
| 80052067-1364-3eb7-b736-4fcf07d0386e | -11.89131 | -45.77626 | 2026-09-23 05:04:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 30.1 |
| 45875bb0-a5ff-385a-8286-a75d2efaa134 | -6.61372 | -59.95976 | 2026-09-23 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 53189c52-a7cd-3bda-98dd-9201edc5997e | -4.15637 | -60.78881 | 2026-09-23 05:04:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8ec3473e-24c6-39d8-895c-d76237f310a1 | -8.12011 | -44.43504 | 2026-09-23 05:04:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| edaebe54-5fed-3bbe-aaa1-8b034ef06f49 | -6.72293 | -44.15728 | 2026-09-23 05:04:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 11.9 |
| d8e361ec-30ae-33dd-8de4-3d59e1dc5c27 | -8.76714 | -45.83995 | 2026-09-23 05:04:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 96fdd5d1-287b-3b5d-800a-de1d19c28af7 | -4.41908 | -55.49903 | 2026-09-23 05:04:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b9a0f554-fd2c-3cf5-a339-bbc25021558f | -6.39718 | -60.02008 | 2026-09-23 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1aed8e86-4b7e-3688-beae-0c5e38c07ee7 | -3.86162 | -58.82727 | 2026-09-23 05:04:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 920cffba-8bec-3033-974a-864a4cee75dd | -10.90471 | -51.52433 | 2026-09-23 05:04:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d773447c-21c2-3dcf-854d-b69026b7e753 | -6.75301 | -59.05225 | 2026-09-23 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b8bda15a-5714-3dc2-b83e-e0250e9398bf | -4.8387 | -55.76445 | 2026-09-23 05:04:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 49028d97-8ead-3ab6-8ffe-3206027c1e82 | -11.89279 | -45.76489 | 2026-09-23 05:04:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 10.5 |
| dc860511-dc76-38f7-900d-e2f1e2833dcb | -7.31656 | -42.2646 | 2026-09-23 05:04:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 9ee8e218-db5f-3e6a-a6d6-b72c87163a8f | -6.62216 | -59.93414 | 2026-09-23 05:04:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| e44ff7b8-93ad-3965-8a1b-b13cdeb1b05f | -5.86323 | -46.10971 | 2026-09-23 05:04:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 79986238-f049-3a7b-8e7d-d427cf6c7479 | -6.38066 | -42.78998 | 2026-09-23 05:04:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| fd20d434-b1dd-3f46-86ce-0f130948e2ab | -5.82818 | -50.22054 | 2026-09-23 05:04:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9e179c2c-ec05-31da-be52-c546cdee48e1 | -6.61237 | -59.96322 | 2026-09-23 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 34a8c039-1bac-3a69-97c0-476c92a5c501 | -5.60626 | -45.9483 | 2026-09-23 05:04:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b68065ed-65a9-31ec-b11d-3cb3647ecef1 | -5.84439 | -47.87186 | 2026-09-23 05:04:00 | NPP-375D | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 75619a44-57b2-3769-a1eb-1234f6fd262f | -6.84 | -55.53345 | 2026-09-23 05:04:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cfaa41c9-ce1f-347f-8e37-ff08dfba4575 | -7.09686 | -52.74713 | 2026-09-23 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c88f4b84-ebcd-3cbf-bd10-d8eacfcc15fa | -11.88562 | -45.78124 | 2026-09-23 05:04:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 2852b897-76ae-3109-ba94-45332a273039 | -6.61753 | -59.99001 | 2026-09-23 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0b4a9711-3811-3442-b65d-c27e86a1402f | -9.96953 | -50.25263 | 2026-09-23 05:04:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cb99a8df-d246-3875-ae36-2d7219cb78e9 | -11.82448 | -49.53627 | 2026-09-23 05:04:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 0f63e56d-c29c-3c48-9d84-1d757a1b275c | -4.27652 | -55.43456 | 2026-09-23 05:04:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7e66f10b-81dc-3601-889d-4e304eee8483 | -10.90588 | -51.51666 | 2026-09-23 05:04:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bf628c80-2aaa-34a0-832e-9c67c389a72a | -5.83226 | -50.21726 | 2026-09-23 05:04:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README88.md)
