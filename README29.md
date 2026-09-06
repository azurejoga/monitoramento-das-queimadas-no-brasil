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

## Dados Diários - Página 29

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 73e9f338-5548-31b3-9d30-2919bba7d750 | -6.63794 | -59.44134 | 2026-09-06 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2a08df79-84a5-3b91-b2e9-711508b79018 | -6.50951 | -58.29019 | 2026-09-06 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 993da35b-e63c-3841-adc8-86c2242d1a73 | -6.87843 | -55.60579 | 2026-09-06 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3802ce87-7cea-3d96-9d35-6442e9149ecf | -4.36695 | -47.77892 | 2026-09-06 05:23:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 19.7 |
| 17e2f236-5233-319e-95ce-7ecd16d9b5d4 | -3.15336 | -59.14545 | 2026-09-06 05:23:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b162d267-b2a9-3a52-b15b-61f18681ca80 | -6.51841 | -58.29883 | 2026-09-06 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 05f702ce-214e-357d-99e1-08d7bd78c83e | -5.28842 | -60.12998 | 2026-09-06 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 54d437c1-edf7-3624-9657-ced2330e73de | -4.34992 | -56.2886 | 2026-09-06 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 91dc1181-eee2-3e3d-aec3-832023c47fb5 | -2.70701 | -59.68516 | 2026-09-06 05:23:00 | NPP-375D | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5e47185b-4736-3c9f-b230-e325a27e59f8 | -9.63624 | -47.68305 | 2026-09-06 05:23:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7043ebbd-6ce9-3bdb-9f6e-70b2b173f212 | -3.62451 | -54.60866 | 2026-09-06 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9b6795b3-83b6-3fbb-9477-6e9139a528b6 | -5.32991 | -56.02279 | 2026-09-06 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a014ea07-7762-342b-b958-b13938ae5b2d | -2.97801 | -60.93694 | 2026-09-06 05:23:00 | NPP-375D | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fcf344f0-7f2b-382d-8b07-08d380b5ddb9 | -5.1353 | -56.26797 | 2026-09-06 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 0625d213-643a-3734-bcaf-9cfe187f6d9e | -3.42696 | -58.31375 | 2026-09-06 05:23:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8376ed69-da28-3940-8c78-972336c0c35f | -6.43951 | -58.15666 | 2026-09-06 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ebe348b7-d6de-3601-8324-a4ce06429393 | -3.07718 | -61.08931 | 2026-09-06 05:23:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ce250927-ad59-3fd8-98b0-3e13048633e5 | -5.36289 | -56.02031 | 2026-09-06 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| d4c56b53-3b17-3240-b312-8fb4466f8b9a | -5.37188 | -56.029 | 2026-09-06 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 20.4 |
| 1f7793c4-875e-3d10-aa5a-13cd74edd53c | -6.13158 | -57.69273 | 2026-09-06 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ad0cdb06-b89a-3085-980c-e8f09bce9897 | -2.93902 | -57.89171 | 2026-09-06 05:23:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a643df5b-3e19-3be9-a29f-f395f6bbe5a3 | -2.58802 | -59.40419 | 2026-09-06 05:23:00 | NPP-375D | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 26afac83-7dda-3bc3-ad2b-086c045e5dbe | -2.8865 | -57.30359 | 2026-09-06 05:23:00 | NPP-375D | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fcfe5311-62ca-38f7-8f62-1cb3fdbb62b2 | -5.15097 | -55.96991 | 2026-09-06 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 81876599-65dc-3d56-b673-3c347198363f | -4.67875 | -55.63713 | 2026-09-06 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 06665e85-f522-3d4f-8014-cf25fbfa903f | -3.21951 | -53.16492 | 2026-09-06 05:23:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c49dd7b4-9040-394c-aaa5-16975e1595cb | -2.86622 | -50.45635 | 2026-09-06 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2612d4f3-0628-3603-be80-521b64e93ae3 | -5.6527 | -60.23505 | 2026-09-06 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 90f22f4b-57af-3daa-a819-7aa9eb192317 | -1.49685 | -54.82494 | 2026-09-06 05:23:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6f51be09-847c-3306-8d5e-0bfdfa9b1794 | -2.86059 | -50.46405 | 2026-09-06 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fb34b11f-202b-3d1f-9360-b6ae70ffeb53 | -6.895 | -62.96167 | 2026-09-06 05:23:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 9e476d66-321f-3893-a0d2-c146c495148a | -6.07007 | -57.80054 | 2026-09-06 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 141e3180-f836-32ba-9848-6ccc58e053d1 | -5.14199 | -55.9612 | 2026-09-06 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| d8670c35-5c87-3ce3-a238-491c83093d9a | -6.95416 | -59.74652 | 2026-09-06 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f4aa430d-2549-35ee-9cb3-80af7fa772f3 | -6.22766 | -55.6186 | 2026-09-06 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0b2ca2ee-3769-3db6-8330-8b3251e603af | -3.79298 | -55.87848 | 2026-09-06 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1b169218-6462-300f-b25f-d9dcc10aa796 | -4.35037 | -55.03351 | 2026-09-06 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f36eb555-ac57-3c24-b17b-761cd5ec09a1 | -5.14199 | -56.26902 | 2026-09-06 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 16.1 |
| ba83cee2-dc73-3051-b12b-5f75a887cf0d | -13.8053 | -51.67581 | 2026-09-06 05:23:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e63fe14f-5d55-30a7-937b-c93beba26b2e | -5.59842 | -60.24459 | 2026-09-06 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a11643ea-4562-3c71-aae7-62d69393f6a9 | -19.04469 | -56.69438 | 2026-09-06 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 9a0a9719-6971-3464-bd66-8dde36bdcec9 | -11.33281 | -45.071 | 2026-09-06 05:25:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9664a779-68b2-3da5-be85-0da56144c156 | -8.62404 | -66.52435 | 2026-09-06 05:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e55efd9c-97ed-3363-88f0-6a3aff66f3ba | -8.6297 | -66.52225 | 2026-09-06 05:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 81f7017e-d34f-346c-b783-3b2dc16fc86f | -8.62514 | -66.51828 | 2026-09-06 05:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 943faf75-b650-314b-935e-ce4bd05f6c51 | -10.63269 | -58.81835 | 2026-09-06 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 82ea9b55-4970-3d74-b547-296525ab6c50 | -19.04533 | -56.68979 | 2026-09-06 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 6451c9d8-3a9e-3051-b38b-e851c6a5c129 | -16.40396 | -49.20299 | 2026-09-06 05:25:00 | NPP-375D | NERÓPOLIS | GOIÁS | Brasil | 5214507 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e9881f32-3f01-3b7c-aa35-3a07f9b22fc3 | -11.32802 | -45.06456 | 2026-09-06 05:25:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 852ffd41-891e-399b-9351-b93114690018 | -11.50087 | -50.25488 | 2026-09-06 05:25:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 238d2501-9ef1-340b-b22b-1c7318020e24 | -10.65768 | -57.7154 | 2026-09-06 05:25:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 43f5ed69-bb18-3f7b-b021-d4c22765fbd0 | -11.50593 | -50.25557 | 2026-09-06 05:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| eca59304-e1fb-3720-bb09-88bf9d20f7e4 | -11.32733 | -45.07055 | 2026-09-06 05:25:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4c505061-b582-37ff-b553-e8933608a022 | -8.62349 | -66.52737 | 2026-09-06 05:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 524e50f6-ca2e-3b83-85ea-5490d8e60e12 | -8.63481 | -66.52321 | 2026-09-06 05:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9aad0bd8-59cf-3672-84a8-84104939f973 | -11.32592 | -45.069 | 2026-09-06 05:25:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7aa228fc-003d-3db0-b440-d135660dce6e | -11.33352 | -45.06451 | 2026-09-06 05:25:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a6a73e8e-f476-3e09-9665-301423ebf802 | -8.62915 | -66.5253 | 2026-09-06 05:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5d163342-54ec-3414-b1c9-4baf1158a4fb | -7.79479 | -70.05107 | 2026-09-06 05:25:00 | NPP-375D | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e19f55be-cf93-328f-a793-016f0247c3fe | -10.50457 | -54.57253 | 2026-09-06 05:25:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c2dfdc7d-aa0b-32eb-b09c-8d9963367665 | -8.62625 | -66.51216 | 2026-09-06 05:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d44dd6be-5ad1-3848-8add-0402bd336d69 | -11.28753 | -45.70169 | 2026-09-06 05:25:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fce61cbb-737f-3304-8c68-a6d75718afa6 | -7.79412 | -70.0507 | 2026-09-06 05:25:00 | NPP-375D | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a77dc868-5df2-30c0-afa6-db6bbe8bf8a3 | -8.62569 | -66.51521 | 2026-09-06 05:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0c2a0b85-db38-3cfc-ae47-2f7e9d8785df | -7.79308 | -70.05605 | 2026-09-06 05:25:00 | NPP-375D | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 33d92f36-cf09-3656-af3c-9b9da4c44888 | -8.62805 | -66.53139 | 2026-09-06 05:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e5a4bd09-99bd-3163-a96a-56067feaf97c | -7.79379 | -70.05643 | 2026-09-06 05:25:00 | NPP-375D | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 604fb959-6df2-3610-a85e-ca792dd02700 | -8.63025 | -66.5192 | 2026-09-06 05:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f9231220-3ea4-328b-8605-2035b34484cf | -8.6286 | -66.52834 | 2026-09-06 05:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 250713a2-eadc-39c0-b7d5-b7ce3b1c0e5f | -8.63081 | -66.51614 | 2026-09-06 05:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ac41bb67-5cbf-38d2-a14b-7ea43b464a9a | -5.3645 | -56.0447 | 2026-09-06 05:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 61.6 |
| 6dc74841-9365-3693-9d5e-e1b2da813637 | -5.3646 | -56.0249 | 2026-09-06 05:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 100.4 |
| c1a48b9d-3a55-3d2e-a516-4f5f84024918 | -5.1423 | -56.2703 | 2026-09-06 05:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 49.9 |
| b7f2dce4-28ac-35ab-9600-12c775172366 | 4.36179 | -59.74759 | 2026-09-06 05:38:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b9539f37-8e32-3739-9680-6afa307ce1f9 | 4.36238 | -59.75122 | 2026-09-06 05:38:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 23591405-9ac0-3be7-b36b-531c032424a4 | -5.3646 | -56.0249 | 2026-09-06 05:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 100.5 |
| e9004699-56cc-3ff1-b01b-ab21eb91a33e | -5.1423 | -56.2703 | 2026-09-06 05:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 57.4 |
| c2484200-0a38-3f23-990f-e48433604d39 | -5.3645 | -56.0447 | 2026-09-06 05:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 99b25a03-b9ea-3532-8fa9-c484beba2c90 | -3.07584 | -61.17889 | 2026-09-06 05:40:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9ae18e60-0e0d-3aae-acbb-74d29d6bf7f4 | -3.17626 | -61.14045 | 2026-09-06 05:40:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 05197e4a-a76b-36f7-97b6-479220ae441d | -3.13836 | -60.63935 | 2026-09-06 05:40:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 328b762c-75a6-35d4-bf8e-992b8aff0fba | 1.09162 | -59.65704 | 2026-09-06 05:40:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cf9a3f37-c402-39ed-9532-4d5e6a19daa8 | -3.86022 | -51.0369 | 2026-09-06 05:40:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0b424666-0415-37df-aee2-2e795adac046 | -3.13485 | -60.63882 | 2026-09-06 05:40:00 | NOAA-20 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| cd2e21c5-2f48-3a44-948f-400b781d8468 | -3.14597 | -60.63657 | 2026-09-06 05:40:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8ebd8ef3-aec6-30d6-9424-6f06451c23e8 | -3.03404 | -61.24458 | 2026-09-06 05:40:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 12f69f46-b69f-3cad-9893-7dc36eb544e2 | -1.3976 | -55.17343 | 2026-09-06 05:40:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7104ff84-f5bd-3134-a984-4f938fde6694 | -3.08043 | -61.53262 | 2026-09-06 05:40:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8b882852-16ed-3258-861f-5783b9260872 | -1.38716 | -55.17722 | 2026-09-06 05:40:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 112dcf52-9844-3988-af88-c7628ee82cf0 | -3.19662 | -61.2351 | 2026-09-06 05:40:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e4da9b5e-2546-313a-954c-b54f5c2f0f35 | -2.51537 | -57.90331 | 2026-09-06 05:40:00 | NOAA-20 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4716d69d-64e1-30d5-824e-8890a28b086e | -3.11082 | -60.6551 | 2026-09-06 05:40:00 | NOAA-20 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 667aec06-e1b5-3f57-b402-89ee142859fc | -2.87046 | -50.46502 | 2026-09-06 05:40:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c1dfef03-a1bd-3e52-8e71-bce6be1d6202 | -3.16246 | -50.82465 | 2026-09-06 05:40:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 437f2b40-ecb9-38e7-b114-f22ef88f0669 | -3.79645 | -55.87868 | 2026-09-06 05:40:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0a73c9c0-fe98-3754-9e92-89611c862d52 | -2.25202 | -53.76368 | 2026-09-06 05:40:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 17a28e46-09b2-35e7-9d8c-9944268f4302 | 0.30662 | -60.44703 | 2026-09-06 05:40:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 50432919-d39c-3ddf-8bd6-17bed8231545 | -3.14187 | -60.63992 | 2026-09-06 05:40:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 10570acb-7537-3df1-a5ee-3d4bc7b3d276 | -3.06946 | -61.2197 | 2026-09-06 05:40:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b4a4047d-96de-3844-9d29-f9ae60c98d0a | -3.23245 | -58.89351 | 2026-09-06 05:40:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README30.md)
