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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2a5f5290-82cd-3aec-9871-517e1382b034 | -4.09391 | -44.85817 | 2024-12-02 04:01:00 | NOAA-21 | LAGO VERDE | MARANHÃO | Brasil | 2105906 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 40ad56d0-3f18-3473-abcd-8bddbb3c986e | -3.85355 | -46.53358 | 2024-12-02 04:01:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 7e03cfca-e54a-3d9f-8731-823c6b869e52 | -1.8362 | -46.23381 | 2024-12-02 04:01:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ce5f04c9-7a92-3929-8ad9-77d3ad2fa080 | -4.63552 | -45.4586 | 2024-12-02 04:01:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 16.9 |
| c1f70ab6-8312-328b-922a-2dffa77c6301 | -5.91149 | -46.25034 | 2024-12-02 04:01:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| b3d34279-3992-3df4-8a37-2e596b0ac773 | -7.43282 | -43.71399 | 2024-12-02 04:01:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 46da770e-6796-3475-bf54-cbfcbd000996 | -4.94448 | -40.72974 | 2024-12-02 04:01:00 | NOAA-21 | IPAPORANGA | CEARÁ | Brasil | 2305654 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 95c47493-1e65-3b42-83fb-d63a322ada41 | -8.89535 | -35.51143 | 2024-12-02 04:01:00 | NOAA-21 | CAMPESTRE | ALAGOAS | Brasil | 2701357 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| fbbec968-90c3-3b85-b7d6-9b949744bc60 | -4.90564 | -41.33742 | 2024-12-02 04:01:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| d1264aa3-9432-357b-bebf-0f9819d25c4f | -3.26832 | -50.20763 | 2024-12-02 04:01:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 958f33ed-0b9f-3e7c-aac2-d9b7144670b6 | -2.28234 | -45.74323 | 2024-12-02 04:01:00 | NOAA-21 | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 04e0c070-d82b-3cd0-855d-40e19d154478 | -3.95275 | -47.05377 | 2024-12-02 04:01:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b57462ce-bb32-31cf-9d96-9d8857df2726 | -3.30486 | -46.4052 | 2024-12-02 04:01:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 8.7 |
| cad423de-9d8a-3e69-9690-43596e7db545 | -4.07337 | -49.06612 | 2024-12-02 04:01:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 4290aa70-85fa-3e71-8948-d5cfa5c615f8 | -2.59126 | -46.01458 | 2024-12-02 04:01:00 | NOAA-21 | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9e523ea7-0baf-34b2-b610-3fd130a7d054 | -2.48317 | -46.57088 | 2024-12-02 04:01:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 676e34e6-99b7-3a12-8cbc-2d3283a1f771 | -4.92581 | -48.42768 | 2024-12-02 04:01:00 | NOAA-21 | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bafb40fc-4e36-3575-9b49-ec6bcb0d7bf0 | -3.25547 | -50.5783 | 2024-12-02 04:01:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7d1c4405-0935-360c-af8e-53b379508594 | -2.99716 | -51.33152 | 2024-12-02 04:01:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2881c6f8-9147-3600-9337-fe5e8341ff8c | -5.32083 | -44.04665 | 2024-12-02 04:01:00 | NOAA-21 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 252d7e03-8f6f-30f4-bd63-7b6e4375329e | -0.31581 | -51.77518 | 2024-12-02 04:01:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a517fb89-81bd-3797-bab3-b74db12f7161 | -3.28419 | -50.55507 | 2024-12-02 04:01:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 16b95d84-bd69-3165-ad3d-193a827dd9d8 | -1.72596 | -52.64124 | 2024-12-02 04:01:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0c8b22ea-657b-3f88-93b6-be910261b8ca | -4.07086 | -47.08853 | 2024-12-02 04:01:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 9c109471-94c8-3f36-bd0d-2fd30f81d4fe | -3.53784 | -51.50063 | 2024-12-02 04:01:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d6a90420-73b6-3225-be92-eab63a18df31 | -3.28547 | -50.43472 | 2024-12-02 04:01:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8808085b-ca25-3ce0-add5-af144854cbf2 | -3.26979 | -46.44762 | 2024-12-02 04:01:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 94729f4b-0a47-313c-bf81-6935d4d77321 | -4.90847 | -41.3414 | 2024-12-02 04:01:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 8.6 |
| 8fc50e8e-5277-390d-83ae-67d62f686525 | -7.38549 | -34.95844 | 2024-12-02 04:01:00 | NOAA-21 | PEDRAS DE FOGO | PARAÍBA | Brasil | 2511202 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| f6cc5b2e-64b4-3c8a-8d2b-b3fa673abc79 | -6.81419 | -46.77348 | 2024-12-02 04:01:00 | NOAA-21 | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5220b24f-e7a3-362f-b348-d8b286f77f93 | -4.87033 | -41.35399 | 2024-12-02 04:01:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 7bb327cd-1b8f-3e98-9ada-1d8c55d7f52f | -2.99054 | -52.50894 | 2024-12-02 04:01:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| df2f17c9-b299-3218-9ed1-4b6aefed6f78 | -3.87482 | -46.57565 | 2024-12-02 04:01:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 381528d1-51da-3c40-9799-34ec9de35449 | -3.27351 | -50.21297 | 2024-12-02 04:01:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 45f66080-6580-36ee-88ff-5ad940c6eebe | -1.53671 | -45.84261 | 2024-12-02 04:01:00 | NOAA-21 | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 03370bda-77f0-3a3d-87bf-ea8d8cb69385 | -2.15706 | -49.75672 | 2024-12-02 04:01:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d9a49227-55cf-3fd0-ba3d-1032d009a5b0 | -6.24636 | -47.29252 | 2024-12-02 04:01:00 | NOAA-21 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 750154ed-2c24-39bf-8c2f-93a629ab39de | -5.58274 | -45.15321 | 2024-12-02 04:01:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 25560a93-055f-3356-8e3c-feb2b339723b | -2.70521 | -47.73885 | 2024-12-02 04:01:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7b2ee45c-c1a6-3a4d-bef9-9c512339e5b8 | -3.69675 | -47.11765 | 2024-12-02 04:01:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| eb9a5361-179c-3456-b058-408fbb716808 | -3.04778 | -49.37457 | 2024-12-02 04:01:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2118f578-2f86-384b-98f4-787254b40db2 | -6.37311 | -47.35264 | 2024-12-02 04:01:00 | NOAA-21 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0ed62786-58e7-309a-8da7-1bea56797fc4 | -1.9618 | -46.451 | 2024-12-02 04:01:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 006eb0a8-4613-3929-a30d-4a53ead079f9 | -3.29072 | -50.44023 | 2024-12-02 04:01:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 832ce012-d7dc-3c13-acea-488fc01eb673 | -2.50045 | -49.01471 | 2024-12-02 04:01:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4313155f-9748-3afd-943a-cfc728c96254 | -3.99523 | -47.27463 | 2024-12-02 04:01:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d542f9cb-6abb-3454-baed-78e07e022d84 | -3.14108 | -45.98948 | 2024-12-02 04:01:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 76422ebe-50a9-3f66-b46b-05bfc6939c5b | -2.6838 | -46.60827 | 2024-12-02 04:01:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 946ed2c3-76b9-3659-b262-706c0608f5d8 | -3.09273 | -53.23708 | 2024-12-02 04:01:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 921d297e-b619-3adb-b0c0-0c52a562943e | -4.53902 | -45.70169 | 2024-12-02 04:01:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cd9e3cf8-ea42-3ee8-b2d9-745c07c952ea | -3.31116 | -40.82063 | 2024-12-02 04:01:00 | NOAA-21 | URUOCA | CEARÁ | Brasil | 2313906 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 15630c0f-1ea2-30f7-9b0c-60833da4f79c | -2.69066 | -48.86011 | 2024-12-02 04:01:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1c62cfc8-07ee-331b-8b7d-cf29340f78a0 | -4.91632 | -41.33548 | 2024-12-02 04:01:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 8.8 |
| e1a90502-01a6-3c92-8415-de8c3f92f734 | -4.53048 | -45.70021 | 2024-12-02 04:01:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 787fec02-3198-3279-a941-35db35abca86 | -2.55933 | -45.56332 | 2024-12-02 04:01:00 | NOAA-21 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7e20b4f5-f460-304c-9ca9-ef76471973ec | -4.53475 | -45.70095 | 2024-12-02 04:01:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 69aaaa5d-994f-36c3-a6e8-24cb7825bf35 | -3.7007 | -47.12352 | 2024-12-02 04:01:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8685947a-4d2e-31dd-8ea6-8673ee201b37 | -4.05088 | -46.82026 | 2024-12-02 04:01:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0339ab44-c4e8-3b70-b098-aa9f836b31cb | -3.27424 | -50.20862 | 2024-12-02 04:01:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 459a404e-2723-3546-93e2-66c302f8996d | -4.7242 | -43.25222 | 2024-12-02 04:01:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1f3283ac-d78a-3408-ab18-beb08ef71412 | -6.08156 | -48.0491 | 2024-12-02 04:01:00 | NOAA-21 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 15.8 |
| ce00a6f2-b6e9-3b35-bf93-6658f5f99c04 | -3.28472 | -50.43924 | 2024-12-02 04:01:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 576a913c-2e69-3a27-8e75-122fd255a0a2 | -3.95275 | -46.50454 | 2024-12-02 04:01:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 193a47b5-4ba5-3b39-b819-34b517454fca | -3.28747 | -50.43742 | 2024-12-02 04:01:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| eb219582-f32a-3183-bc06-623cf1121747 | -3.77845 | -52.03365 | 2024-12-02 04:01:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 1d70aefc-d9c9-3ce0-9cf3-bac67d2e8b3e | -4.76599 | -46.42789 | 2024-12-02 04:01:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2bdb9077-84b1-34dd-824c-45561bcb6a66 | -4.05125 | -46.99321 | 2024-12-02 04:01:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 0ad03dd6-097c-370b-8730-5b1d0514ff1c | -4.19029 | -50.68404 | 2024-12-02 04:01:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 1513e007-ca8f-3dd4-912a-178f0dc4dafa | -3.27437 | -46.44843 | 2024-12-02 04:01:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 27114443-ebed-3594-bfb9-3560457d6917 | -8.82818 | -44.7844 | 2024-12-02 04:04:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f9828e47-52b2-3a23-9b5b-fc2d2b7d6306 | -8.13259 | -44.47947 | 2024-12-02 04:04:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 94f72734-7ff1-35d2-a561-eeca63e22079 | -8.87846 | -40.78171 | 2024-12-02 04:04:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 048b3dc5-becc-3bd2-a3f3-ea84e65c1cc7 | -11.13507 | -37.21857 | 2024-12-02 04:04:00 | NOAA-21 | ITAPORANGA D'AJUDA | SERGIPE | Brasil | 2803203 | 28 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 29369714-1616-3f73-9e32-72f1a7bc6402 | -11.62256 | -43.25237 | 2024-12-02 04:04:00 | NOAA-21 | MORPARÁ | BAHIA | Brasil | 2921609 | 29 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 2d12ebc7-1b25-3d57-82a0-f73defd68463 | -8.51183 | -42.87449 | 2024-12-02 04:04:00 | NOAA-21 | BREJO DO PIAUÍ | PIAUÍ | Brasil | 2201988 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 5c83313b-bcc7-3ca6-b224-fefd3a2e75aa | -8.83275 | -44.78035 | 2024-12-02 04:04:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 27e34e28-3714-3995-862c-86993fa80119 | -9.97859 | -36.33796 | 2024-12-02 04:04:00 | NOAA-21 | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| 1e71dce6-67bf-3091-a26e-8313947aa650 | -10.66391 | -44.49545 | 2024-12-02 04:04:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 9dc2095a-440a-32af-9467-127040157174 | -10.65372 | -44.48933 | 2024-12-02 04:04:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| a142b37b-3db1-3ad8-bbd7-db110cba5165 | -11.16105 | -44.73442 | 2024-12-02 04:04:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dd18afda-438a-3b98-832c-2d2ea7ab4f7b | -10.65594 | -44.49849 | 2024-12-02 04:04:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8a659ec3-70e3-3934-8412-d0f4060a8664 | -8.51121 | -42.87835 | 2024-12-02 04:04:00 | NOAA-21 | BREJO DO PIAUÍ | PIAUÍ | Brasil | 2201988 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 3b068d84-3e39-34d6-9001-ef8352e4e8de | -9.33869 | -36.02073 | 2024-12-02 04:04:00 | NOAA-21 | CAPELA | ALAGOAS | Brasil | 2701704 | 27 | 33 | nan | nan | nan | Mata Atlântica | 18.6 |
| 98764bd4-71dd-38d1-aa2a-dde1650f0195 | -11.27734 | -41.72976 | 2024-12-02 04:04:00 | NOAA-21 | JOÃO DOURADO | BAHIA | Brasil | 2918357 | 29 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 5a22dcd0-6660-3d09-ab57-d71be0593856 | -11.16471 | -44.73504 | 2024-12-02 04:04:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7b821221-a525-3950-960e-059819e929a2 | -9.18349 | -35.73574 | 2024-12-02 04:04:00 | NOAA-21 | FLEXEIRAS | ALAGOAS | Brasil | 2702801 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| c7fee50e-2723-361e-9f72-007607aa812a | -10.70129 | -44.97131 | 2024-12-02 04:04:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| c85fbaa1-3196-372e-8256-bdef0b6fed32 | -10.05542 | -36.55481 | 2024-12-02 04:04:00 | NOAA-21 | IGREJA NOVA | ALAGOAS | Brasil | 2703205 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 5fcc0ac6-2985-3e5f-9155-8b2440c44407 | -8.87792 | -40.78518 | 2024-12-02 04:04:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 4c96eae8-39b3-354c-93ce-608ef8dea223 | -9.19222 | -45.3486 | 2024-12-02 04:04:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 444e67e8-c74a-355c-955e-d568e453b6f5 | -8.83775 | -44.32543 | 2024-12-02 04:04:00 | NOAA-21 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2bc0010a-e8a7-3219-9d96-9f96eefd2395 | -10.65302 | -44.4936 | 2024-12-02 04:04:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 54a5802b-723a-3970-8830-ae57fd502c4f | -11.06025 | -45.38193 | 2024-12-02 04:04:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3554b020-4102-3268-96e1-44b848c21c07 | -10.65231 | -44.49787 | 2024-12-02 04:04:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6cb5edab-4f75-3336-89bc-e14beaa92e27 | -13.26531 | -43.93055 | 2024-12-02 04:04:00 | NOAA-21 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e8481565-1ad2-32ca-9322-b7edcf37c9d1 | -9.33472 | -36.02014 | 2024-12-02 04:04:00 | NOAA-21 | CAPELA | ALAGOAS | Brasil | 2701704 | 27 | 33 | nan | nan | nan | Mata Atlântica | 18.6 |
| e64b0415-8d08-3c09-b9cc-77ae35126656 | -10.65665 | -44.49421 | 2024-12-02 04:04:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1adb9ab5-d87e-37d4-b2fa-af1f4e64e15c | -9.19916 | -43.20415 | 2024-12-02 04:04:00 | NOAA-21 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| fed614e7-dc5e-3cdd-8e30-7a337a9b0fb1 | -15.61252 | -39.33482 | 2024-12-02 04:04:00 | NOAA-21 | MASCOTE | BAHIA | Brasil | 2920908 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 159c785d-424b-3929-b130-06d9ca6e3110 | -9.34014 | -36.01048 | 2024-12-02 04:04:00 | NOAA-21 | CAPELA | ALAGOAS | Brasil | 2701704 | 27 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |


[Clique aqui para ver as próximas entradas](README27.md)
