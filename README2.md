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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 71638234-d1a4-3286-ade8-e25b5cd0dcca | -3.72746 | -42.17658 | 2025-11-21 00:13:00 | TERRA_M-M | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 123390af-a213-377a-95ba-74632ffb24fb | -3.34318 | -45.00852 | 2025-11-21 00:13:00 | TERRA_M-M | CAJARI | MARANHÃO | Brasil | 2102507 | 21 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 91014f63-bb93-3c46-a7bf-5104decac8a5 | -3.17914 | -44.29904 | 2025-11-21 00:13:00 | TERRA_M-M | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 376c6ee0-11ad-3a91-ab11-5cf3f55c88d5 | -2.97896 | -44.57791 | 2025-11-21 00:13:00 | TERRA_M-M | CAJAPIÓ | MARANHÃO | Brasil | 2102408 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| b2280ae7-e64a-367e-9cf6-efdfda872a5b | -3.30869 | -45.56332 | 2025-11-21 00:13:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 12.7 |
| c5c6e6bd-d0bf-3dfd-aa4f-a40fd2632ef6 | -2.90481 | -45.37293 | 2025-11-21 00:13:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 32bc2112-bac8-3cbd-9290-132d7fbe95fe | -3.44303 | -44.93265 | 2025-11-21 00:13:00 | TERRA_M-M | CAJARI | MARANHÃO | Brasil | 2102507 | 21 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 13fd6380-e0ff-32c3-a2e2-e03a98d20b30 | -3.13321 | -41.87882 | 2025-11-21 00:13:00 | TERRA_M-M | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| f2431e2f-dfeb-3686-8a51-84eb529add51 | -5.74074 | -39.39584 | 2025-11-21 00:13:00 | TERRA_M-M | SENADOR POMPEU | CEARÁ | Brasil | 2312700 | 23 | 33 | nan | nan | nan | Caatinga | 9.9 |
| a467be30-cf86-329a-b6d7-764b6c1c76bd | -3.30991 | -45.57217 | 2025-11-21 00:13:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 12.1 |
| a603f719-637a-3bda-bc86-16c87787c771 | -5.4296 | -40.66528 | 2025-11-21 00:13:00 | TERRA_M-M | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 19.8 |
| d06e9e92-3631-348a-bbad-4b255c536a39 | -2.77641 | -45.24172 | 2025-11-21 00:13:00 | TERRA_M-M | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| e09eed70-0b67-3c71-970b-eb56e999c992 | -3.21538 | -45.4771 | 2025-11-21 00:13:00 | TERRA_M-M | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 73.4 |
| e574f445-b1ac-3f99-b1f1-dba97f79ecc7 | -4.37217 | -45.5203 | 2025-11-21 00:13:00 | TERRA_M-M | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 0ec795c1-6e1c-3f98-aa67-dbddd4490c2d | -5.7531 | -45.10983 | 2025-11-21 00:13:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 4b5b06ae-49b8-3dd5-8fcb-5e6d83efe03e | -2.84608 | -45.6138 | 2025-11-21 00:13:00 | TERRA_M-M | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| ee342e93-05fd-33b1-986f-ad555499b8ce | -6.00595 | -39.51355 | 2025-11-21 00:13:00 | TERRA_M-M | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 13.3 |
| be675cd7-4719-353d-b16e-700fd9d61f5b | -3.30486 | -43.53849 | 2025-11-21 00:13:00 | TERRA_M-M | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 3cc54f73-48d5-38b2-b167-8acd50fe5673 | -3.03884 | -45.07615 | 2025-11-21 00:13:00 | TERRA_M-M | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 0d3cafb6-346f-3e96-9b91-297cec8e2149 | -3.99649 | -42.48927 | 2025-11-21 00:13:00 | TERRA_M-M | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 8.0 |
| 31246c23-831a-33f3-81b5-d661ff79596e | -5.20975 | -42.17193 | 2025-11-21 00:13:00 | TERRA_M-M | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 10.2 |
| 75187b0b-a335-3dfc-b53b-be379b03b65a | -3.85643 | -43.36341 | 2025-11-21 00:13:00 | TERRA_M-M | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| ba28e2f5-3a0b-3e27-aa7d-95504462d485 | -3.47301 | -45.2771 | 2025-11-21 00:13:00 | TERRA_M-M | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 1537999b-fd98-331a-8d31-bde2b88cbb53 | -3.04779 | -45.07488 | 2025-11-21 00:13:00 | TERRA_M-M | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 51.2 |
| 68c25ee2-5087-3b40-90cc-37b34eb78948 | -2.59738 | -47.00495 | 2025-11-21 00:15:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 308bb5a4-972d-3c4a-a83b-23bee8622825 | -0.25965 | -48.55922 | 2025-11-21 00:15:00 | TERRA_M-M | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| ae260701-8ef9-3b85-af00-89a5aefedeac | -2.29903 | -45.65512 | 2025-11-21 00:15:00 | TERRA_M-M | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 4.4 |
| abe86b9a-3e71-3d82-820e-c9b632785077 | -1.4329 | -46.78593 | 2025-11-21 00:15:00 | TERRA_M-M | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 33.5 |
| 1502e5ba-8ca9-32bb-a4ae-efe3032e34ba | -2.34295 | -45.63396 | 2025-11-21 00:15:00 | TERRA_M-M | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 7b18c5d4-5c7f-39ae-b5e7-9af3afcf9d9b | -1.79401 | -46.3911 | 2025-11-21 00:15:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| ed496b8b-c828-3a0d-9ee8-05a73712b4cf | -2.63974 | -46.91703 | 2025-11-21 00:15:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 65.7 |
| 213aa9a5-75ba-3097-a169-37373965d1e8 | -2.51171 | -45.99095 | 2025-11-21 00:15:00 | TERRA_M-M | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| c65b0a27-507b-3d4f-9e85-51f8e9265a7c | -2.59616 | -46.99601 | 2025-11-21 00:15:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 21ff047b-253b-30bd-925c-a4e6e3e99a79 | -2.40441 | -46.27205 | 2025-11-21 00:15:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 5287f8ac-3a44-399b-9e78-21b006707b1d | -1.90589 | -45.60802 | 2025-11-21 00:15:00 | TERRA_M-M | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| fff48d9a-9858-3d70-ad2a-942192b53734 | -2.2978 | -45.64625 | 2025-11-21 00:15:00 | TERRA_M-M | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 5aa042ce-d04f-31b8-ac15-2d444ac41d7c | -2.08855 | -45.32662 | 2025-11-21 00:15:00 | TERRA_M-M | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 17.5 |
| cdfc701f-bd88-36bb-adc1-ac112fac262a | -2.64097 | -46.92593 | 2025-11-21 00:15:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 30.7 |
| 084eb4f5-1f44-31a4-8a8c-6b06500a1101 | -2.215 | -46.10486 | 2025-11-21 00:15:00 | TERRA_M-M | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| de441e95-1cdc-3e37-a73f-d1f130ded1af | -1.92578 | -47.08368 | 2025-11-21 00:15:00 | TERRA_M-M | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 752c79a0-0dda-3d15-9e5e-e2b8c507c855 | -1.92454 | -47.07476 | 2025-11-21 00:15:00 | TERRA_M-M | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 86fcdab9-d38f-30df-b6ce-115e706ba5c2 | -2.08981 | -45.33562 | 2025-11-21 00:15:00 | TERRA_M-M | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 834add37-0872-36a4-ad05-6f9ff27b6277 | -1.00721 | -47.30018 | 2025-11-21 00:15:00 | TERRA_M-M | NOVA TIMBOTEUA | PARÁ | Brasil | 1505007 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 97818fdb-c20c-3178-a17a-e8bb5471cfd8 | -0.26098 | -48.5689 | 2025-11-21 00:15:00 | TERRA_M-M | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 9bdf79b7-a7ee-3669-ae76-4d1393787201 | -1.93467 | -47.08244 | 2025-11-21 00:15:00 | TERRA_M-M | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 15.9 |
| 7bc907fd-6a6d-311b-b55c-6066a77503d5 | 3.889 | -59.6395 | 2025-11-21 00:49:00 | METOP-B | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| cc270e63-75ed-38e9-a322-3faaa06ddeba | -21.038401 | -48.5658 | 2025-11-21 00:49:00 | METOP-B | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 374fe9f8-9863-329a-bc4b-1047913dfdfd | -21.035 | -48.552898 | 2025-11-21 00:49:00 | METOP-B | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 1dd402c8-282c-35aa-aed0-795b1315fa34 | -22.915899 | -48.6651 | 2025-11-21 00:49:00 | METOP-B | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 1a564fa5-2dae-3c6e-a157-6880c7bf318b | -22.9189 | -48.676998 | 2025-11-21 00:49:00 | METOP-B | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 54e42645-a528-3ab7-9f28-a4a450ebe009 | 3.8905 | -59.6325 | 2025-11-21 00:49:00 | METOP-B | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| cba7f5a1-6ff9-3e46-bc43-2fdeaaa7694d | -22.922001 | -48.688999 | 2025-11-21 00:49:00 | METOP-B | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 3d5f3aef-0a54-3bdf-862c-5b49d23cbd0d | -21.289499 | -49.672798 | 2025-11-21 00:49:00 | METOP-B | ADOLFO | SÃO PAULO | Brasil | 3500204 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 04620e58-88b4-3b91-b9a1-38ac57cc98e4 | -10.3257 | -63.689899 | 2025-11-21 01:32:00 | METOP-C | CAMPO NOVO DE RONDÔNIA | RONDÔNIA | Brasil | 1100700 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 8a31c32c-a562-301c-a533-ccd1f0e3237a | -10.3275 | -63.698101 | 2025-11-21 01:32:00 | METOP-C | CAMPO NOVO DE RONDÔNIA | RONDÔNIA | Brasil | 1100700 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 9b3f0432-2945-3cd3-8de5-48723baf696b | -22.926399 | -48.692799 | 2025-11-21 01:32:00 | METOP-C | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| b22e8147-9d2b-34a9-869b-e004febbda9d | -22.9212 | -48.6744 | 2025-11-21 01:32:00 | METOP-C | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 5e12cdfc-4a9a-3a9f-b64c-fa3ad3590768 | -11.95917 | -62.84651 | 2025-11-21 01:49:00 | TERRA_M-M | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 13.9 |
| efb6556b-ba49-370c-81ee-f9697f52ebf9 | -9.63332 | -67.48653 | 2025-11-21 01:51:00 | TERRA_M-M | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 726f4528-a884-3689-b8fd-32145d080d1f | -3.14237 | -40.17939 | 2025-11-21 03:21:00 | NOAA-21 | MARCO | CEARÁ | Brasil | 2307809 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| d445d475-df19-3a47-9a05-1f5fda809f63 | -5.4284 | -40.66811 | 2025-11-21 03:21:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| a94a9da7-3aef-36aa-9cae-d7764c4e7846 | -4.14875 | -43.67284 | 2025-11-21 03:21:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0100d5ac-6eb7-3e89-922e-b6ab89637259 | -5.73202 | -39.39821 | 2025-11-21 03:21:00 | NOAA-21 | SENADOR POMPEU | CEARÁ | Brasil | 2312700 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 01a5a32a-f69c-343f-bf24-441bc5afd836 | -4.13907 | -43.68572 | 2025-11-21 03:21:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 006fbead-49c7-3338-a9e8-0836cca79f64 | -4.1594 | -43.67439 | 2025-11-21 03:21:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 76b45b28-d439-36c0-a451-c8dc9c4c7f33 | -2.84285 | -40.10991 | 2025-11-21 03:21:00 | NOAA-21 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| b8af80bc-175b-35c6-80fd-3e230d79a751 | -4.14747 | -43.6799 | 2025-11-21 03:21:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 3b053bbb-5c71-3aa8-99b0-1ae8e7e1928e | -4.14859 | -43.69438 | 2025-11-21 03:21:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 675f0c46-4054-39d1-bef9-3110af7ba54e | -4.14734 | -43.70158 | 2025-11-21 03:21:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| ce9406e8-5542-3c34-87ea-8b05d84a65d5 | -4.14395 | -43.67896 | 2025-11-21 03:21:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 21dc7f44-3fae-3768-8841-7854dc3aca7e | -4.1523 | -43.67313 | 2025-11-21 03:21:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| f040da45-6158-30ed-9c7f-492c74ccc4f5 | -4.16528 | -43.68276 | 2025-11-21 03:21:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 17.9 |
| 6b4c5290-00e7-3801-a37d-1e30db17f979 | -4.17136 | -43.66941 | 2025-11-21 03:21:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 17a196a4-29bb-34fa-b3f2-b2432446360e | -3.1469 | -40.183 | 2025-11-21 03:21:00 | NOAA-21 | MARCO | CEARÁ | Brasil | 2307809 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| e6eab6a7-5564-3f0d-9a42-7eb84462f3de | -2.89283 | -41.68522 | 2025-11-21 03:21:00 | NOAA-21 | PARNAÍBA | PIAUÍ | Brasil | 2207702 | 22 | 33 | nan | nan | nan | Cerrado | 10.5 |
| be3d8e46-9270-3794-93ea-89772e2c6ab8 | -5.42767 | -40.67221 | 2025-11-21 03:21:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 28aa6f3c-d442-3864-8d63-e9c7ddd52c0c | -3.87583 | -38.4044 | 2025-11-21 03:21:00 | NOAA-21 | AQUIRAZ | CEARÁ | Brasil | 2301000 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 9b27812a-8685-314e-b4f8-7c944781f406 | -5.17064 | -35.85742 | 2025-11-21 03:21:00 | NOAA-21 | PEDRA GRANDE | RIO GRANDE DO NORTE | Brasil | 2409506 | 24 | 33 | nan | nan | nan | Caatinga | 1.7 |
| eede5f6a-662e-3e39-9f84-796db5de85ae | -4.15105 | -43.68027 | 2025-11-21 03:21:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| adce9e2b-7625-3b7d-9a47-b32c6dede1e9 | -5.73318 | -39.39147 | 2025-11-21 03:21:00 | NOAA-21 | SENADOR POMPEU | CEARÁ | Brasil | 2312700 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| ddc1b0ca-8112-3719-9590-38be8e541645 | -3.14753 | -40.18455 | 2025-11-21 03:21:00 | NOAA-21 | MARCO | CEARÁ | Brasil | 2307809 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 4a949f2d-ef12-3fb1-a463-8911e53cb6ee | -7.38546 | -35.26984 | 2025-11-21 03:21:00 | NOAA-21 | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 02667488-8cdb-3f41-a634-d916ba0bc280 | -5.42731 | -40.67569 | 2025-11-21 03:21:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 8512356c-65ea-393d-8078-5f854c374b75 | -2.962 | -41.55608 | 2025-11-21 03:21:00 | NOAA-21 | LUÍS CORREIA | PIAUÍ | Brasil | 2205706 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| bfd848e1-e1ca-3f56-8449-51dbf8c0226e | -5.42802 | -40.67156 | 2025-11-21 03:21:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| ed6dc4f9-c4bb-3888-b6f3-4c4a1034f8f2 | -2.89328 | -41.6868 | 2025-11-21 03:21:00 | NOAA-21 | PARNAÍBA | PIAUÍ | Brasil | 2207702 | 22 | 33 | nan | nan | nan | Cerrado | 10.5 |
| addfe513-715e-347b-93b6-98b4dde06a42 | -3.87814 | -38.40417 | 2025-11-21 03:21:00 | NOAA-21 | AQUIRAZ | CEARÁ | Brasil | 2301000 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| c62ebaec-904b-3050-a182-bc8ef2fc9715 | -4.15586 | -43.67405 | 2025-11-21 03:21:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| a022daf2-bed3-32e6-bcdd-56dfae361a12 | -4.15816 | -43.68154 | 2025-11-21 03:21:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 83ecc051-ba84-334f-a188-4f6daaadd90d | -4.15456 | -43.68123 | 2025-11-21 03:21:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 037a5688-89d5-3aad-adfe-0587000edc17 | -5.73259 | -39.39491 | 2025-11-21 03:21:00 | NOAA-21 | SENADOR POMPEU | CEARÁ | Brasil | 2312700 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| bd4e8306-f57f-3abf-aa06-d6537fdaf53b | -3.14824 | -40.18028 | 2025-11-21 03:21:00 | NOAA-21 | MARCO | CEARÁ | Brasil | 2307809 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| af934203-e9dd-3329-88dd-ff984a35d043 | -3.99931 | -41.05391 | 2025-11-21 03:21:00 | NOAA-21 | SÃO BENEDITO | CEARÁ | Brasil | 2312304 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 0ce29f6a-e28a-3a2f-8927-941a04b44ce5 | -5.42693 | -40.67634 | 2025-11-21 03:21:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| f92d1d24-3130-3f36-864c-f4d2bda5d314 | -2.84369 | -40.11112 | 2025-11-21 03:21:00 | NOAA-21 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 7a5c86a7-25d9-3c39-9a90-92808f0928e6 | -4.16169 | -43.68236 | 2025-11-21 03:21:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 93718ced-7ec8-3f51-9f04-a615f1b683d7 | -6.00293 | -39.51225 | 2025-11-21 03:21:00 | NOAA-21 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 85a7cabf-14c1-3b68-ae21-f12b0946f1e6 | -4.16774 | -43.66856 | 2025-11-21 03:21:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 19.2 |
| 4572899e-091e-3cbe-9d4b-0dcf4c4072ff | -3.14103 | -40.18212 | 2025-11-21 03:21:00 | NOAA-21 | MARCO | CEARÁ | Brasil | 2307809 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| a008e2c4-2ef6-30a2-9956-68d787086837 | -4.14163 | -43.67166 | 2025-11-21 03:21:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |


[Clique aqui para ver as próximas entradas](README3.md)
