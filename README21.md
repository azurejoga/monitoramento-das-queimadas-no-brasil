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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 020e2736-f5a4-3069-87ba-7ec309e786f6 | -7.45757 | -46.21161 | 2025-09-18 04:14:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5ec94e3b-37ee-3e09-86c4-28c829d44acd | -9.38165 | -45.3808 | 2025-09-18 04:14:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b21b7a00-737d-3974-abf3-df601940663b | -11.1154 | -45.35766 | 2025-09-18 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 11dcda13-7e3e-3074-9b8c-f7711bee7750 | -7.38058 | -47.03963 | 2025-09-18 04:14:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 13.4 |
| de3bf325-7384-3ebe-bc07-cda0f6988812 | -12.90476 | -44.66793 | 2025-09-18 04:14:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 8.6 |
| b6e81055-95e9-32a9-8305-edab581f5b17 | -7.55893 | -44.76382 | 2025-09-18 04:14:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f9ed8b90-5647-316b-9f24-18853a676f41 | -13.76435 | -42.55367 | 2025-09-18 04:14:00 | NOAA-20 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 33048c17-d703-3fe3-9e38-ec8feeda21c5 | -11.32905 | -43.47779 | 2025-09-18 04:14:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 04436eae-6bd6-3fde-86d2-b7f2af3137a8 | -8.69374 | -46.36192 | 2025-09-18 04:14:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 557923be-7d24-3eb0-a584-fd02f4ff51ab | -11.46993 | -43.55461 | 2025-09-18 04:14:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 797c0eaf-6725-3179-ae1f-c7c6e7d9ee13 | -13.16171 | -40.68129 | 2025-09-18 04:14:00 | NOAA-20 | MARCIONÍLIO SOUZA | BAHIA | Brasil | 2920809 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 21005682-7264-31c0-82e8-047a42fed642 | -12.36855 | -43.20454 | 2025-09-18 04:14:00 | NOAA-20 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 28c2b200-11e3-3d9c-968c-dd7ded36c849 | -11.99876 | -46.72337 | 2025-09-18 04:14:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 80167ae9-1aff-3a12-b1d5-6adae5ecbe71 | -6.72028 | -47.20427 | 2025-09-18 04:14:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b91bc667-15aa-3b83-88d8-cbbd71d4bc69 | -11.44998 | -43.55143 | 2025-09-18 04:14:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 012f9af6-3dd7-3929-9140-6f4ced803b95 | -12.23983 | -46.77554 | 2025-09-18 04:14:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| bf3a1823-d718-32fb-a038-32c0ca8e01bf | -11.59666 | -49.81291 | 2025-09-18 04:14:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f3763555-1a37-39a3-809d-255b31b15db4 | -9.15925 | -46.96386 | 2025-09-18 04:14:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 18.6 |
| 0917d13f-3f46-38e0-b20c-6d0a4bd14ce1 | -12.10352 | -44.83647 | 2025-09-18 04:14:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cf6b08c4-8476-3881-b8c6-e1cebc3e32b8 | -11.93694 | -38.33454 | 2025-09-18 04:14:00 | NOAA-20 | INHAMBUPE | BAHIA | Brasil | 2913705 | 29 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 3cd0a0a3-07b3-3f5f-9732-a2d3217fb509 | -9.08015 | -44.94142 | 2025-09-18 04:14:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5e2b1cd8-e004-3f6e-8385-eab1abd92537 | -8.65614 | -46.43446 | 2025-09-18 04:14:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a65b1337-409f-354c-894b-c1a187295977 | -8.13774 | -43.62862 | 2025-09-18 04:14:00 | NOAA-20 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a0a79b97-d16d-3cc5-8b2b-58d0105515f2 | -7.84778 | -45.59926 | 2025-09-18 04:14:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 583a9ea7-0185-31e8-94b7-6db7bb0c201a | -12.08665 | -45.80812 | 2025-09-18 04:14:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c9730d1c-80e2-3e38-aefa-828b447f1e24 | -8.1351 | -44.84154 | 2025-09-18 04:14:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 30.9 |
| 7062b8d0-3619-3754-a73f-d8e23495e44a | -7.5478 | -44.7471 | 2025-09-18 04:14:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e47a54fe-da0f-3722-a140-51492e93fe65 | -12.41124 | -44.71714 | 2025-09-18 04:14:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 521ef22c-2272-3210-8101-56bdd974f47a | -8.95393 | -45.52824 | 2025-09-18 04:14:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3ea5f583-20c2-3eb1-b815-20ec26d678f8 | -7.28799 | -43.93171 | 2025-09-18 04:14:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 35c96f08-ea0f-34bc-9dc6-df6765d85c4c | -9.17667 | -46.97113 | 2025-09-18 04:14:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| db421fe8-c47f-324e-a785-16ca36e2bea2 | -10.62691 | -44.23226 | 2025-09-18 04:14:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.3 |
| d5579f3a-d97d-3114-8d65-efb5c25b22c3 | -7.21901 | -44.3865 | 2025-09-18 04:14:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9394b1d9-8cd4-3203-8563-9a5de22faf4b | -11.71029 | -50.76931 | 2025-09-18 04:14:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b23a8288-2e63-38a4-ad3a-b334c017c69a | -13.94174 | -47.99141 | 2025-09-18 04:14:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3dbdbe95-c43f-302d-80ef-b744751cfd97 | -11.46661 | -43.55407 | 2025-09-18 04:14:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 46213cb4-3170-366b-bc93-87a6e7790d89 | -15.09804 | -42.24519 | 2025-09-18 04:14:00 | NOAA-20 | CONDEÚBA | BAHIA | Brasil | 2908705 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 3be01d1c-0f8e-39c3-90b7-19d0008a50cd | -9.14279 | -44.90756 | 2025-09-18 04:14:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fff46d81-93d0-389e-ba88-b08b7d9748f8 | -7.52381 | -45.28522 | 2025-09-18 04:14:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6e923eb6-2386-32c5-b2ce-a1c2f7435e2b | -11.38082 | -50.83485 | 2025-09-18 04:14:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 18.9 |
| 8b8ca13a-8d6c-35e4-984b-bc0c8a88b0d8 | -14.59438 | -45.17173 | 2025-09-18 04:14:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a876abc6-fafd-3681-8fed-5c8aef1c4382 | -11.26882 | -47.44323 | 2025-09-18 04:14:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 71526cf0-24ca-3e2a-977e-daa3da82e591 | -7.66467 | -45.12891 | 2025-09-18 04:14:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fddd7578-7a95-3529-894b-c0c5d6ca6f75 | -8.62914 | -45.30547 | 2025-09-18 04:14:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6f484a87-c384-3af7-a3d5-d5189bae45cb | -9.03859 | -44.96413 | 2025-09-18 04:14:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ad973ac5-92fc-3a31-8985-cf7c6708ed65 | -7.40709 | -50.0095 | 2025-09-18 04:14:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 49a1d682-5df9-39d8-a383-8e481ddc8f8e | -8.8976 | -46.13459 | 2025-09-18 04:14:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 91d6a3ba-1f5f-3986-af0d-21ebe0d5564f | -8.88461 | -46.14812 | 2025-09-18 04:14:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b8e95f97-f93b-383e-a0cd-3ac4661fc4fb | -12.69973 | -44.97433 | 2025-09-18 04:14:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2e767926-f080-37be-ae04-ee827ea6c44f | -10.64222 | -42.3145 | 2025-09-18 04:14:00 | NOAA-20 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 5b8a862e-e204-3793-9945-b1860193373c | -11.23622 | -47.43786 | 2025-09-18 04:14:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fc8c47ff-9570-3446-8fad-b3034c2f5f1d | -8.06879 | -45.44844 | 2025-09-18 04:14:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b2806b73-3f94-327e-8677-8b33ba78fb5e | -9.83205 | -48.41308 | 2025-09-18 04:14:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bb5540c2-dc18-3a49-aa04-675e9e0a45f2 | -11.49932 | -43.6064 | 2025-09-18 04:14:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8dfd63da-3118-3152-a8fb-4eb17c9c9c4f | -13.04461 | -47.96701 | 2025-09-18 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| e22ab324-3480-3611-b4b6-fe8380c2c0ad | -7.19554 | -48.60286 | 2025-09-18 04:14:00 | NOAA-20 | MURICILÂNDIA | TOCANTINS | Brasil | 1713957 | 17 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 111bc22f-26dc-37cc-9f96-bb67c6153312 | -9.82868 | -48.43312 | 2025-09-18 04:14:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| a703840b-22bf-3056-9a74-c07b83a93512 | -12.40004 | -51.4272 | 2025-09-18 04:14:00 | NOAA-20 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 64c00bbe-e57f-33da-b2b0-fb72c80d3cdb | -11.18201 | -45.35013 | 2025-09-18 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6cba20e0-eb7d-30b9-bc8e-f1f8434a5542 | -9.15053 | -46.94925 | 2025-09-18 04:14:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 255beaf6-f266-37ba-b72d-0956f23821e8 | -7.29918 | -46.56048 | 2025-09-18 04:14:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 880ee25c-fb95-381b-b65b-219bcc8decce | -14.31245 | -45.15026 | 2025-09-18 04:14:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 8.1 |
| ec0af1a8-8586-30bb-b50e-66c034d18bf9 | -12.90365 | -44.67498 | 2025-09-18 04:14:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 755bb1e5-e497-3e57-9b46-ee26581e5f74 | -13.07484 | -42.13657 | 2025-09-18 04:14:00 | NOAA-20 | RIO DO PIRES | BAHIA | Brasil | 2926905 | 29 | 33 | nan | nan | nan | Caatinga | 34.1 |
| ac83dad5-4ceb-3f74-a2a1-a0128718037b | -13.82286 | -43.23554 | 2025-09-18 04:14:00 | NOAA-20 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 0.2 |
| 7c024e5f-6216-3997-8139-db7cbb2db9d3 | -13.62264 | -42.47756 | 2025-09-18 04:14:00 | NOAA-20 | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 338fb240-fc2c-3f04-a553-5c29d4bc442a | -10.92696 | -47.84087 | 2025-09-18 04:14:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9fc6c8df-4785-3ae7-93a1-3a0b34324010 | -11.16701 | -45.33652 | 2025-09-18 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5f145bb7-075d-3130-bf17-891de2e41c6a | -7.45181 | -42.63333 | 2025-09-18 04:14:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 25457493-2d08-312c-88a9-596c77ad8e4e | -11.16132 | -45.35041 | 2025-09-18 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8214601c-4874-3970-a6c8-3ca0d2b3a122 | -7.51438 | -45.322 | 2025-09-18 04:14:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d608694a-b73e-3f42-bbcd-fc49b217b3cc | -10.64506 | -42.31874 | 2025-09-18 04:14:00 | NOAA-20 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 2.7 |
| c2b1fc70-55f5-33c2-b122-c36f11d9f49c | -9.54313 | -50.83998 | 2025-09-18 04:14:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 074063a7-c073-3459-84ff-39d8ddac142c | -7.17729 | -44.34693 | 2025-09-18 04:14:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 775929c9-7307-3790-93af-ce686ac87948 | -14.30448 | -47.11184 | 2025-09-18 04:14:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9c7b64e6-117b-3a34-bc91-a552d48a1a87 | -12.23636 | -46.77494 | 2025-09-18 04:14:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 7adf1812-b842-3057-904e-dea54517abea | -8.88174 | -46.1437 | 2025-09-18 04:14:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 90a3f111-f489-3d8a-8d25-a460d2d6c75c | -11.59598 | -49.81671 | 2025-09-18 04:14:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a2b65933-e5b1-38df-ac6d-68485ccd5b07 | -9.15415 | -46.94983 | 2025-09-18 04:14:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| f7a9a2d0-18d3-320b-9161-0d247c34ff80 | -10.87526 | -47.7752 | 2025-09-18 04:14:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| cd6e8aff-b429-3052-97b2-5d1f263cd62f | -9.37884 | -45.37667 | 2025-09-18 04:14:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 946edd5d-2c28-3bde-87ac-3042b7900bbf | -11.38164 | -50.83041 | 2025-09-18 04:14:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 39.9 |
| c5d0a2df-a935-3c15-a956-71fb081557d6 | -13.03672 | -47.94733 | 2025-09-18 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7474279e-e75f-3c77-8452-8a2ad51a5cbd | -10.95293 | -49.57338 | 2025-09-18 04:14:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 452ca8cc-fbc3-399f-9042-e87637541c6b | -11.93322 | -38.32988 | 2025-09-18 04:14:00 | NOAA-20 | INHAMBUPE | BAHIA | Brasil | 2913705 | 29 | 33 | nan | nan | nan | Mata Atlântica | 26.0 |
| c90aacad-ab29-3c4f-8a63-e49d74cd9c05 | -10.74698 | -46.55085 | 2025-09-18 04:14:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 59a6553b-0119-3e08-92a6-911695ab2590 | -7.94019 | -43.88894 | 2025-09-18 04:14:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6dc300e2-7923-399d-a64a-dbd099a38aac | -13.96351 | -44.23723 | 2025-09-18 04:14:00 | NOAA-20 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9c7464ae-8e66-3c3f-a008-99f3e77b5300 | -11.49489 | -43.61294 | 2025-09-18 04:14:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6dddfed0-5f3f-38e9-a4c4-2fea66eec6fa | -11.71809 | -50.77334 | 2025-09-18 04:14:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4be75a53-30ca-3b9e-9cef-47589a0ecd42 | -7.8347 | -43.84785 | 2025-09-18 04:14:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f80e3f02-3cab-3014-b435-54317b271ecc | -11.16803 | -45.35151 | 2025-09-18 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 81855ca0-d78f-3df8-a304-d8c8d58e7ea3 | -9.11467 | -48.11055 | 2025-09-18 04:14:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 12b8e968-d2b5-3a03-8bb8-b5d77cde6e98 | -8.9265 | -44.50043 | 2025-09-18 04:14:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a4363acd-e6c8-33b1-a19d-18b5145e5c98 | -7.3282 | -43.99872 | 2025-09-18 04:14:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ffb2b74f-3357-36f2-9630-f549f4b12594 | -13.4001 | -46.8041 | 2025-09-18 04:14:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3c8342eb-76b1-3666-a371-bd4d9d15aec6 | -7.50286 | -44.32991 | 2025-09-18 04:14:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 374991dc-13bd-3a74-8dda-98a5d3304d4f | -10.60961 | -46.46464 | 2025-09-18 04:14:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5ffc6951-f341-385d-b877-2b40a4fb78f9 | -7.8484 | -45.59542 | 2025-09-18 04:14:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cf7813a4-21f5-3823-a986-787aa34ee622 | -7.94184 | -43.87851 | 2025-09-18 04:14:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README22.md)
