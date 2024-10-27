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

## Dados Diários - Página 55

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8668c60e-838c-36ea-8b08-842e38464fd1 | -22.20429 | -54.7663 | 2024-10-27 04:29:00 | NOAA-20 | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| e17a8c39-94cb-3427-996f-e8546ee77278 | -23.3066 | -54.94636 | 2024-10-27 04:29:00 | NOAA-20 | AMAMBAI | MATO GROSSO DO SUL | Brasil | 5000609 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 4147e650-6570-3372-b3d8-b415797d124d | -22.18713 | -55.655 | 2024-10-27 04:29:00 | NOAA-20 | PONTA PORÃ | MATO GROSSO DO SUL | Brasil | 5006606 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4ad6a8e0-b61d-3d79-add0-ea004e75bdb2 | -22.18365 | -55.65458 | 2024-10-27 04:29:00 | NOAA-20 | PONTA PORÃ | MATO GROSSO DO SUL | Brasil | 5006606 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 765cb96e-1ee7-33c9-a66c-1b8ea29e8332 | -23.23563 | -55.45214 | 2024-10-27 04:29:00 | NOAA-20 | CORONEL SAPUCAIA | MATO GROSSO DO SUL | Brasil | 5003157 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 91fa6951-1379-386c-a332-bce60b683c27 | -29.05219 | -50.27078 | 2024-10-27 04:32:00 | NOAA-20 | JAQUIRANA | RIO GRANDE DO SUL | Brasil | 4311122 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 47bd6241-bb2a-30f9-82fc-59caf039b7ec | -30.15033 | -52.02448 | 2024-10-27 04:32:00 | NOAA-20 | MINAS DO LEÃO | RIO GRANDE DO SUL | Brasil | 4312252 | 43 | 33 | nan | nan | nan | Pampa | 0.4 |
| 3e155858-a50e-3be3-b043-f37979648121 | -29.81313 | -51.17548 | 2024-10-27 04:32:00 | NOAA-20 | SAPUCAIA DO SUL | RIO GRANDE DO SUL | Brasil | 4320008 | 43 | 33 | nan | nan | nan | Pampa | 1.5 |
| 1985ce3b-fa03-357e-92c6-12f8a35e5b21 | -30.53194 | -53.41412 | 2024-10-27 04:32:00 | NOAA-20 | CAÇAPAVA DO SUL | RIO GRANDE DO SUL | Brasil | 4302808 | 43 | 33 | nan | nan | nan | Pampa | 0.7 |
| 2a03fa27-ca89-301e-91ab-426041c18963 | -0.9815 | -53.7192 | 2024-10-27 04:35:11 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 50.0 |
| 051d872b-616c-3d36-99a6-fd761844cc2e | -0.9815 | -53.699 | 2024-10-27 04:35:11 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 113.0 |
| b0e4b3ef-e947-35b0-88cc-2743037fcc0c | -0.9815 | -53.6789 | 2024-10-27 04:35:11 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 40.5 |
| fed98ad8-93d2-3061-b5c2-d260e8b0365f | -0.9998 | -53.719 | 2024-10-27 04:35:11 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 36.6 |
| 83eaa884-5adc-3c6b-985e-f3ce3fc632ec | -0.9998 | -53.6989 | 2024-10-27 04:35:11 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 76.2 |
| c1011288-ad0a-361e-b346-4411a11072f1 | -2.5495 | -51.1812 | 2024-10-27 04:35:20 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 135.2 |
| 351544fb-2aa0-37a7-86b1-45e183377f9d | -2.531 | -51.2024 | 2024-10-27 04:35:20 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 61.3 |
| fe7058e8-8bf7-3f62-ad58-0dea1b4a3b2a | -2.5311 | -51.1816 | 2024-10-27 04:35:20 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 225.9 |
| 9e82307f-1ab0-34e6-a798-74a45c051981 | -2.5312 | -51.1609 | 2024-10-27 04:35:20 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 111.3 |
| 46e91300-fb73-32ea-931f-49566b99f13c | -2.5495 | -51.2019 | 2024-10-27 04:35:20 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 41.8 |
| 86b370d8-8c3e-3543-a7e3-2100612a04f6 | -2.5496 | -51.1604 | 2024-10-27 04:35:20 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 77.4 |
| d3241f33-629f-3902-94d5-7db59642d42b | -2.8329 | -49.2626 | 2024-10-27 04:35:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 90.4 |
| 5d29203a-8186-3656-abf2-91f7902ce865 | -2.833 | -49.2413 | 2024-10-27 04:35:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 111.1 |
| 3fd064da-e6da-34f7-b503-2081df6a6805 | -2.8514 | -49.262 | 2024-10-27 04:35:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 73.4 |
| f655dae3-3d37-37d0-8d31-8de0f65bbb73 | -2.8515 | -49.2408 | 2024-10-27 04:35:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 86.1 |
| bdc48255-0b55-3fe7-9314-30085e2bbd00 | -2.9161 | -51.751 | 2024-10-27 04:35:22 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 43.6 |
| a0270e8b-a889-30ba-9c58-79a241bc034d | -2.9345 | -51.7505 | 2024-10-27 04:35:22 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 54.2 |
| 5d61ce32-f809-3938-819c-32f3c0d786df | -6.0515 | -39.8243 | 2024-10-27 04:35:39 | GOES-16 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 307.9 |
| 5ceb799a-aa5e-39f7-931c-d4253e82fe96 | -6.0518 | -39.7994 | 2024-10-27 04:35:39 | GOES-16 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 102.0 |
| e1de324f-f301-3555-bba6-0a69c9494d36 | -6.0326 | -39.826 | 2024-10-27 04:35:39 | GOES-16 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 188.0 |
| 8be899fb-9378-37be-9a19-89a02122ea23 | -6.0329 | -39.8012 | 2024-10-27 04:35:39 | GOES-16 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 67.8 |
| f4c53aaf-4da6-3217-8bd1-e3e23a43ce88 | -0.9815 | -53.6789 | 2024-10-27 04:45:11 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 36.4 |
| e25e77a1-2a37-3ae7-9466-d2faa1a16074 | -0.9815 | -53.699 | 2024-10-27 04:45:11 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 99.8 |
| e413bdde-0a88-3a04-ae53-73981a179069 | -0.9815 | -53.7192 | 2024-10-27 04:45:11 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 44.7 |
| c31af324-5213-3b1c-82cb-c29d57237b0d | -0.9998 | -53.6989 | 2024-10-27 04:45:12 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 80.7 |
| f21e51c7-5034-3bcd-b75a-6897a087f685 | -0.9998 | -53.719 | 2024-10-27 04:45:12 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 39.0 |
| 988a33dc-e269-39f4-9cae-e64f9e25ab29 | -2.7034 | -49.3088 | 2024-10-27 04:45:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 36.7 |
| 53089e43-33d9-3261-8c8b-331372659572 | -2.6321 | -54.2975 | 2024-10-27 04:45:21 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 42.0 |
| b5982af1-9b41-3b8d-b320-ceb94479f218 | -2.8515 | -49.2408 | 2024-10-27 04:45:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 90.7 |
| da711f06-46b9-351b-8b29-9fc7117ba235 | -2.8514 | -49.262 | 2024-10-27 04:45:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 85.6 |
| 78a1730e-d9d0-3c81-a612-76e2f4027ecb | -2.833 | -49.2413 | 2024-10-27 04:45:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 118.9 |
| 46d66289-8683-3d79-9201-82e0f81beb92 | -2.8329 | -49.2626 | 2024-10-27 04:45:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 93.7 |
| 1a7fc9b0-8f4d-3386-8050-030bd30e8052 | -2.9345 | -51.7505 | 2024-10-27 04:45:23 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 4629aff2-e483-3554-8fab-7c4716282d7e | -6.0518 | -39.7994 | 2024-10-27 04:45:40 | GOES-16 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 76.2 |
| 53dceed1-9c06-3d26-b9c1-f31b99fe2bc4 | -6.0515 | -39.8243 | 2024-10-27 04:45:40 | GOES-16 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 127.8 |
| 7f77ae61-a5c9-3aa9-a358-0b2426567633 | -6.0329 | -39.8012 | 2024-10-27 04:45:40 | GOES-16 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 97.9 |
| 5e26c007-7a7d-3048-862e-1de088622c21 | -6.0326 | -39.826 | 2024-10-27 04:45:40 | GOES-16 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 179.8 |
| c3b035c3-73e2-371f-adc8-4e7122e77e81 | -0.9815 | -53.7192 | 2024-10-27 04:55:11 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 38.1 |
| af54c242-3ac8-3707-a451-5cfdfba1e5ab | -0.9815 | -53.699 | 2024-10-27 04:55:11 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 106.0 |
| 92f61264-4c0a-3f9d-ad67-f7dc59d2e104 | -0.9815 | -53.6789 | 2024-10-27 04:55:11 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 41.1 |
| 43394e9c-5657-3847-814e-83d5bb6c0d71 | -0.9998 | -53.6989 | 2024-10-27 04:55:11 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 70.5 |
| 0896a80d-2e36-3ef6-ab12-1dc4e53a168b | -2.5127 | -51.1821 | 2024-10-27 04:55:20 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 40.0 |
| 6ecd0ecf-25a6-33c5-b535-bb3c91545b7e | -2.5311 | -51.1816 | 2024-10-27 04:55:20 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 153.8 |
| 9bd793f6-e5a7-3a6b-ad9d-81cd576a2568 | -2.5312 | -51.1609 | 2024-10-27 04:55:20 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 79.9 |
| b0390dd6-5a7e-3fbe-bfbc-762e9a06fcfe | -2.5495 | -51.1812 | 2024-10-27 04:55:20 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 140.4 |
| bb116422-3cc2-37f3-9de6-c24a3ebbb372 | -2.5496 | -51.1604 | 2024-10-27 04:55:20 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 21bace60-bd8e-33e6-92e0-8de1a046fbea | -2.531 | -51.2024 | 2024-10-27 04:55:20 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 38.6 |
| 209cf380-01f5-3e37-b202-7f3157fac8b5 | -2.8329 | -49.2626 | 2024-10-27 04:55:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 97.5 |
| bcf7e9f4-b934-396c-a0c7-258e9b52cda2 | -2.9161 | -51.751 | 2024-10-27 04:55:22 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 48.6 |
| e79692e7-d493-358a-a393-02847e367d59 | -2.8515 | -49.2408 | 2024-10-27 04:55:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 83.4 |
| a54107df-8995-32e6-ba55-7bdcabe023aa | -2.8514 | -49.262 | 2024-10-27 04:55:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 66.5 |
| 060cd4aa-3fe9-31af-b962-8e5e0990c08a | -2.9345 | -51.7505 | 2024-10-27 04:55:22 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 46.9 |
| 2fba4eb1-1f51-3465-b7ff-aa8cb21f9aee | -2.833 | -49.2413 | 2024-10-27 04:55:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 161.4 |
| fd62fbb1-65d7-3687-9335-1ff27be518d5 | -4.15453 | -43.69987 | 2024-10-27 05:04:00 | AQUA_M-M | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 12.2 |
| c6392b69-cb3b-30af-b22e-fe55dd5bec61 | -3.59589 | -43.66862 | 2024-10-27 05:04:00 | AQUA_M-M | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 13.2 |
| cf265f21-18d2-32e0-848b-a77a08f08852 | -3.59442 | -43.67832 | 2024-10-27 05:04:00 | AQUA_M-M | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 8adedd3a-2060-3268-9b7c-e13a0f70e1a3 | -3.1239 | -45.27422 | 2024-10-27 05:04:00 | AQUA_M-M | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 6.4 |
| d0a5ec6d-6184-3ae7-8b6f-4562f4b25953 | -3.11593 | -45.26723 | 2024-10-27 05:04:00 | AQUA_M-M | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 32.6 |
| 77f28dce-1ea9-3479-9bc3-364967e0167a | -3.11114 | -45.22947 | 2024-10-27 05:04:00 | AQUA_M-M | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 7.7 |
| f4a19551-2eeb-3a79-8763-fd309a3f8490 | -3.06346 | -44.32362 | 2024-10-27 05:04:00 | AQUA_M-M | BACABEIRA | MARANHÃO | Brasil | 2101251 | 21 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 3a02b9d6-6942-3549-992c-554ef603a7bc | -3.06185 | -44.33427 | 2024-10-27 05:04:00 | AQUA_M-M | BACABEIRA | MARANHÃO | Brasil | 2101251 | 21 | 33 | nan | nan | nan | Amazônia | 14.7 |
| f03b01bb-ea72-37c4-9820-0e3f7c27275e | -0.9815 | -53.699 | 2024-10-27 05:05:11 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 86.8 |
| dcdbed3e-518d-3823-b43b-adb12f7c686b | -0.9815 | -53.6789 | 2024-10-27 05:05:11 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 31.4 |
| 776022d5-d3c4-3428-b167-952f9fa58398 | -0.9998 | -53.6989 | 2024-10-27 05:05:11 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 6ec74697-3412-3952-826d-9ca043c94fef | -0.9815 | -53.7192 | 2024-10-27 05:05:11 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 40.1 |
| bfadcff4-c14e-32af-8cc3-513f6040ea4d | -2.531 | -51.2024 | 2024-10-27 05:05:20 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 55.0 |
| eb0fe275-35be-350b-8d81-50677eae04f3 | -2.5311 | -51.1816 | 2024-10-27 05:05:20 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 168.8 |
| 196ee562-6e10-3b6d-a460-d1b94b6a8e9c | -2.5312 | -51.1609 | 2024-10-27 05:05:20 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 81.7 |
| 11e7f6bc-d944-37ff-bbeb-5b27644428ec | -2.5495 | -51.1812 | 2024-10-27 05:05:20 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 93.5 |
| e5c3b73e-2151-3386-8ca2-c3462829f3d9 | -2.5496 | -51.1604 | 2024-10-27 05:05:20 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 51.9 |
| f4c3376c-7f55-37d9-a598-9fcc5cb0fd0b | -2.7034 | -49.3088 | 2024-10-27 05:05:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 34.3 |
| 04df6740-cd09-3d03-add9-8c39ee044cde | -2.8329 | -49.2626 | 2024-10-27 05:05:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 93.1 |
| 63b065b0-22d0-344a-814b-87db29bbbf30 | -2.833 | -49.2413 | 2024-10-27 05:05:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 101.6 |
| 29dff31a-117a-3840-b813-330a52bb6589 | -2.8514 | -49.262 | 2024-10-27 05:05:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 80.5 |
| 195818b7-2736-3c99-ae11-770c70ba20b4 | -2.8515 | -49.2408 | 2024-10-27 05:05:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 78.2 |
| 17d67371-a7c9-37aa-bd1d-9f8f2545b6af | -2.9161 | -51.751 | 2024-10-27 05:05:22 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 39.6 |
| a886fb8f-f1db-3fc1-aa1d-d42a3eb9f75c | -2.9345 | -51.7505 | 2024-10-27 05:05:22 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 49.5 |
| 92b14691-4df3-3f35-96be-45c21eee820f | -3.1278 | -45.2736 | 2024-10-27 05:05:23 | GOES-16 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 62.9 |
| a7cedef7-c069-32a3-ac5e-073b42096c16 | -9.43941 | -44.45757 | 2024-10-27 05:06:00 | AQUA_M-M | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| d533e60f-0194-351d-a62b-5dc8aed3ccf5 | -8.34972 | -42.25859 | 2024-10-27 05:06:00 | AQUA_M-M | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 13.8 |
| e8b87146-dbf7-32bb-962f-af1a0bc5a660 | -7.55741 | -38.74741 | 2024-10-27 05:06:00 | AQUA_M-M | MAURITI | CEARÁ | Brasil | 2308104 | 23 | 33 | nan | nan | nan | Caatinga | 8.3 |
| 07d6eab6-6772-30b6-91e7-598621a39c0c | -7.2478 | -41.22692 | 2024-10-27 05:06:00 | AQUA_M-M | FRANCISCO SANTOS | PIAUÍ | Brasil | 2204204 | 22 | 33 | nan | nan | nan | Caatinga | 13.6 |
| c92d1dce-ea61-3370-b7ad-76e33669b065 | -6.67699 | -40.90179 | 2024-10-27 05:06:00 | AQUA_M-M | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 11.0 |
| 2e2aa439-f195-38ce-972e-95ade500b893 | -6.54976 | -40.50863 | 2024-10-27 05:06:00 | AQUA_M-M | AIUABA | CEARÁ | Brasil | 2300408 | 23 | 33 | nan | nan | nan | Caatinga | 16.8 |
| a83204a3-8748-3290-91e5-d493a2fbdbe5 | -6.04395 | -39.81736 | 2024-10-27 05:06:00 | AQUA_M-M | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 7b2f98f1-d3a8-38cf-a2d7-cbc6a0285588 | -6.03439 | -39.81604 | 2024-10-27 05:06:00 | AQUA_M-M | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 8.1 |
| 11ab0e0c-448d-3332-b9a7-dce91dcb3730 | -5.87632 | -42.93062 | 2024-10-27 05:06:00 | AQUA_M-M | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 11.6 |
| ad762f71-83f6-3652-9d1f-001202188b64 | -5.87498 | -42.93956 | 2024-10-27 05:06:00 | AQUA_M-M | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| ab9de126-027c-3049-a935-cffbf10b2e20 | -5.41282 | -43.37341 | 2024-10-27 05:06:00 | AQUA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| c8395a62-2f85-35e6-aa99-a7c3350fa7a0 | -4.93894 | -42.90388 | 2024-10-27 05:06:00 | AQUA_M-M | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| aecc9a64-853f-39e3-bf3f-c0d425b19018 | -10.5947 | -44.27277 | 2024-10-27 05:06:00 | AQUA_M-M | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 17.4 |


[Clique aqui para ver as próximas entradas](README56.md)
