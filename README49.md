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

## Dados Diários - Página 49

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f7af24ae-1b5a-37d6-879e-f6c85708edc2 | -2.67396 | -54.79172 | 2025-08-28 04:57:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 68696c94-f1b7-39f5-9296-3a81a3072be6 | -6.43274 | -44.57548 | 2025-08-28 04:57:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 9ab2c669-3a58-313e-afe8-d9c4fff90b29 | -3.98047 | -51.06064 | 2025-08-28 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 64711ee3-4bae-3d60-ad13-7eeb0e8ac6c0 | -8.08698 | -44.99041 | 2025-08-28 04:57:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 34f5decc-a80e-3fdb-88e7-314b864871c0 | -5.77506 | -44.9297 | 2025-08-28 04:57:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| be58fb53-c8f6-35e2-b5c3-8708adabe695 | -6.16466 | -44.40063 | 2025-08-28 04:57:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 64764589-0f9a-3d9e-86a2-33295bfbd4c2 | -8.23841 | -45.07816 | 2025-08-28 04:57:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 7.4 |
| a6d3b86a-21b6-31a9-ba1f-74646fbf7434 | -8.2939 | -45.12735 | 2025-08-28 04:57:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| aeeb4bd8-02ab-3890-ae66-5523476174e6 | -8.56339 | -51.3203 | 2025-08-28 04:57:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1484a43e-b35b-3c73-a67a-8f0b89cca626 | -4.48469 | -55.55928 | 2025-08-28 04:57:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9c1c0077-babf-3f7b-ac3b-7018c716e311 | -3.75523 | -54.8165 | 2025-08-28 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e76a9919-fe25-3953-a05a-7da4b6762d83 | -7.55383 | -63.8373 | 2025-08-28 04:57:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7638708d-49ff-3d92-adb3-fee7be751472 | -5.88403 | -50.15295 | 2025-08-28 04:57:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a4c263c8-a84b-3bda-b044-c32bed16c842 | -6.87257 | -43.59309 | 2025-08-28 04:57:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4b455784-1d36-3fbe-8d5c-2aad5d2ef758 | -8.23886 | -45.07463 | 2025-08-28 04:57:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 00443cdd-96d0-303a-92c2-85987af95183 | -6.92764 | -52.81552 | 2025-08-28 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f5d680b2-ab26-309e-b7e7-ca0a2b45a05a | -7.27766 | -60.29602 | 2025-08-28 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 744375db-37a6-3d0d-ade9-2a89ab9b502a | -6.59981 | -45.96782 | 2025-08-28 04:57:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 77366201-39da-3bac-949e-942355bd6cca | -4.08118 | -48.0423 | 2025-08-28 04:57:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 09add238-9476-34ba-9bc8-b637ebf89495 | -6.87024 | -43.61082 | 2025-08-28 04:57:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c94f441c-0562-337b-8e46-ca579f028846 | -6.4388 | -44.57272 | 2025-08-28 04:57:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| c5855d7d-f61c-3fcf-8bb5-2afa5ebd56d1 | -8.83075 | -52.02237 | 2025-08-28 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c85079b1-2b3b-357e-8d57-7742ff902f99 | -8.27721 | -45.16908 | 2025-08-28 04:57:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 855ee2a3-3558-3d31-8dd2-94c8e292984f | -6.00084 | -57.84727 | 2025-08-28 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 13274bc2-8f5d-3e03-a8c8-ef8d458d9740 | -3.76524 | -54.81803 | 2025-08-28 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d6ae89b1-c7bc-3f2b-bc75-87ef59b7c4d2 | -8.44275 | -41.44948 | 2025-08-28 04:57:00 | NOAA-21 | QUEIMADA NOVA | PIAUÍ | Brasil | 2208650 | 22 | 33 | nan | nan | nan | Caatinga | 14.1 |
| 937a62dc-9b0c-3147-bde0-4cba2de7d8c7 | -8.24523 | -45.07151 | 2025-08-28 04:57:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0281ebf8-6cf6-3e40-a71a-c67eab0eb239 | -7.25979 | -57.65792 | 2025-08-28 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bbe72d22-64cf-33ab-af11-95902935ba7c | -6.20178 | -51.45446 | 2025-08-28 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fa1fe822-dd81-36fe-ae00-8f5e9b2cee7a | -8.09569 | -45.01007 | 2025-08-28 04:57:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| aa736742-9678-386e-907b-baf10861355b | -8.70845 | -50.38043 | 2025-08-28 04:57:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 525733c9-39b2-34fb-8c1d-a858ae73ec5d | -6.28292 | -44.48323 | 2025-08-28 04:57:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| efeab6f7-5d2f-3f33-a02a-94948a360013 | -7.68079 | -45.00038 | 2025-08-28 04:57:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 49c7c712-a423-3c37-81a6-686d324cc8ec | -6.86739 | -43.63245 | 2025-08-28 04:57:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 6b78cc1e-3240-3b4e-a691-40f6aa71297f | -4.79732 | -47.26744 | 2025-08-28 04:57:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 19.4 |
| 0624d5ee-54c0-3872-a8d5-2d378bb91245 | -3.79059 | -45.03934 | 2025-08-28 04:57:00 | NOAA-21 | PIO XII | MARANHÃO | Brasil | 2108702 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 810f7546-ceaa-3526-bfbe-259e1bb1f6b9 | -5.54645 | -45.374 | 2025-08-28 04:57:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0cdb78cd-abb6-30bd-89cf-8fb458671af4 | -6.90532 | -62.93789 | 2025-08-28 04:57:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3981f161-4bb2-3605-9410-287e0a39b969 | -9.66073 | -48.3114 | 2025-08-28 04:57:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 712ed32d-c7d3-3ae3-8860-4ffa9b5c956f | -8.29661 | -45.14933 | 2025-08-28 04:57:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| aa7e3525-19ed-3e53-bae7-4a9d4e581c5b | -8.29111 | -45.14853 | 2025-08-28 04:57:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 75327c30-252c-3bf0-8305-cf90b4fd808e | -7.73437 | -50.28691 | 2025-08-28 04:57:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| fa091d43-fac9-33f5-82a5-d670d187b715 | -9.05216 | -54.94569 | 2025-08-28 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0092fd1d-e226-349c-885b-d71115ca019c | -6.87853 | -43.59414 | 2025-08-28 04:57:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4bbf5359-6c91-37c0-9643-8b313c8e2925 | -2.67675 | -54.79577 | 2025-08-28 04:57:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 03ca0d0a-cf88-3399-9c5d-bd0fba5a26ea | -6.12739 | -44.42202 | 2025-08-28 04:57:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bf1e32c9-2a41-32e3-a4f4-236a7072e98e | -4.48912 | -47.67878 | 2025-08-28 04:57:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| dd77dcb3-2d12-3b2e-b7b0-1f26070e9957 | -9.05655 | -54.93927 | 2025-08-28 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 8d70a6d5-7998-312a-87ea-f243222cee63 | -2.74694 | -48.5643 | 2025-08-28 04:57:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3a6db9e3-6465-33fc-a842-6629a8735269 | -8.85624 | -47.15786 | 2025-08-28 04:57:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9b1d724c-9460-36dc-9fc5-9aaac1377012 | -7.56327 | -63.84585 | 2025-08-28 04:57:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 15884b36-fc8b-35c1-8059-d000df9de472 | -6.90583 | -62.93491 | 2025-08-28 04:57:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 90735bce-742a-30ef-9a19-97fb4d7bf13e | -8.27073 | -45.17585 | 2025-08-28 04:57:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 05b8c0a8-4961-33d2-bf17-443dfdb5b9d2 | -8.28626 | -45.18544 | 2025-08-28 04:57:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 65.7 |
| 05fb6def-3af8-3a4f-bb9b-e77adca81834 | -7.73505 | -50.29397 | 2025-08-28 04:57:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| fe373d6f-3545-38d6-b6be-b7b6be752e29 | -5.84521 | -45.30691 | 2025-08-28 04:57:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2b96a5bb-0e4d-3904-9b16-974687c3e46b | -7.90139 | -61.52385 | 2025-08-28 04:57:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0a4bb305-1827-3974-8700-aea335112977 | -7.35192 | -57.63477 | 2025-08-28 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f4d76e50-63d0-3652-9402-67a3581246cf | -7.2591 | -57.66207 | 2025-08-28 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7c22bbbe-059f-3f55-89e0-139c66383900 | -4.51344 | -43.64483 | 2025-08-28 04:57:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b6568d16-303d-35e2-9c45-761024bd926f | -6.49172 | -47.48486 | 2025-08-28 04:57:00 | NOAA-21 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e40fb199-82ab-3ee7-a0ea-a83d03707852 | -8.44294 | -43.69016 | 2025-08-28 04:57:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 808803ef-55ef-3518-b171-25ab14c3050e | -6.25085 | -60.01984 | 2025-08-28 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 28a96361-7cec-38a0-aab5-7fde40f74926 | -6.16383 | -44.06771 | 2025-08-28 04:57:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| db76cd5f-5978-3740-9f4b-16e986eff417 | -5.64808 | -45.25776 | 2025-08-28 04:57:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9b7ac309-9caa-3f58-8d76-1e79add17f97 | -7.06491 | -44.36587 | 2025-08-28 04:57:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 91d905bc-29f8-3b62-8aea-718ed22b4c31 | -9.45202 | -51.94877 | 2025-08-28 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 0613724f-c3bf-3267-a542-3a50664ff69a | -6.15669 | -55.80416 | 2025-08-28 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b66478d4-b9a5-3df0-a6da-6dd206bf158e | -8.28819 | -45.17074 | 2025-08-28 04:57:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 38.4 |
| d5c437ec-f686-3b8a-9117-f2619e8a41d3 | -7.16054 | -45.15279 | 2025-08-28 04:57:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 93d5a497-ffc9-34fe-9837-0c7c5318f16c | -6.87391 | -43.62906 | 2025-08-28 04:57:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 7269cb35-c63a-3425-858d-397689a92c45 | -8.2717 | -45.1684 | 2025-08-28 04:57:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 6d07da30-ce55-3796-8098-d8f081259f71 | -8.27623 | -45.17655 | 2025-08-28 04:57:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 9.2 |
| c197c87f-37e1-3599-94e5-20ae0be68fb9 | -6.07836 | -43.99617 | 2025-08-28 04:57:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6e7f55e7-a35d-3957-b2ac-76922ddd63c6 | -7.18969 | -44.06185 | 2025-08-28 04:57:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a17c28fd-7d37-348f-b884-06f6c0f06e66 | -2.74641 | -48.56781 | 2025-08-28 04:57:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 140e19ab-3021-3ac7-867f-78e038029044 | -3.48543 | -51.1903 | 2025-08-28 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 06120bb3-1eac-3eb5-9b2f-1e84d03be241 | -3.59511 | -49.45746 | 2025-08-28 04:57:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 716e9f92-29b0-3e94-9d9d-2edfbef9e865 | -7.59739 | -63.34413 | 2025-08-28 04:57:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| fcd5747a-5e64-35a3-b93d-68cb123cf6d0 | -6.8552 | -55.11453 | 2025-08-28 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5bad6835-34c5-3915-8e5d-c732e9ff0f43 | -6.92023 | -62.93541 | 2025-08-28 04:57:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eb667b5e-8666-31b4-8092-7921028b0458 | -6.19138 | -44.16535 | 2025-08-28 04:57:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9ac5230e-520f-3fef-88e2-d4fef8a46092 | -3.49552 | -51.17888 | 2025-08-28 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 77b96089-3c06-3bc0-8036-7803879e4b2c | -8.0911 | -45.00206 | 2025-08-28 04:57:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b319ce53-7ddc-3c29-8ec8-20d655f4988d | -8.90626 | -47.33174 | 2025-08-28 04:57:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c27286ee-8495-3829-93ad-cbf1e1502b43 | -7.5998 | -63.34247 | 2025-08-28 04:57:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bb3b5061-0525-3fd3-a994-b96483f284ff | -7.8957 | -44.77665 | 2025-08-28 04:57:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7c469477-709a-3001-ac05-a861ed5f9b93 | -6.90452 | -62.93575 | 2025-08-28 04:57:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9ea4e2f4-ccb0-3072-ae13-3da85bb2e0f6 | -9.67459 | -47.06887 | 2025-08-28 04:57:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| aa8a562b-f5c2-3dd3-8ed1-bb30fb823930 | -7.28254 | -60.29279 | 2025-08-28 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 40c982d2-c111-3084-85ed-6150cb773d98 | -5.84566 | -45.30376 | 2025-08-28 04:57:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 48cb82fa-b602-3a2d-961d-9c4adad4029f | -3.84894 | -56.97606 | 2025-08-28 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| eb79683f-21ff-3996-a5b7-8645b5d073e8 | -8.29469 | -45.16395 | 2025-08-28 04:57:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 64a07217-8627-39fa-9ccf-685b36d1f0df | -3.72766 | -48.35629 | 2025-08-28 04:57:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1f58c9d0-3ecd-3ecb-a592-3fc0dc427118 | -5.54689 | -45.3708 | 2025-08-28 04:57:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0f1f00e5-8cec-370e-95d5-ea2f5f5f810d | -8.29616 | -45.15279 | 2025-08-28 04:57:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 9.7 |
| c2b80794-706d-35a4-b60f-59d29a655e73 | -8.27218 | -45.16471 | 2025-08-28 04:57:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a63d9356-44b1-3bed-a615-2f0acb8a5755 | -5.31898 | -55.87745 | 2025-08-28 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6af01f08-c7a4-3f9a-91d7-2f18ae305b9f | -4.86265 | -50.89951 | 2025-08-28 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f288481f-f1da-377b-a63b-9b0f7a32e3ec | -10.37117 | -45.16562 | 2025-08-28 04:57:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |


[Clique aqui para ver as próximas entradas](README50.md)
