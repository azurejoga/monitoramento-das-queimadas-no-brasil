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

## Dados Diários - Página 52

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| eaad7d7b-8f7b-3f0d-9604-49138d735252 | -6.16186 | -43.37789 | 2025-09-10 04:40:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0443650f-2606-3b29-a05d-995ee76d8e2d | -5.82752 | -44.09843 | 2025-09-10 04:40:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3740750d-bc14-3353-bf03-5af058405a8f | -2.3293 | -49.08273 | 2025-09-10 04:40:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 876e63c6-b30e-34cb-9193-ff8fd5f52550 | -3.31968 | -54.90882 | 2025-09-10 04:40:00 | NPP-375D | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c358c9ff-8e72-3dcd-b7cc-506929282efd | -5.41133 | -43.46197 | 2025-09-10 04:40:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 41d38f0b-be01-37ba-8a9b-04c124e3bd94 | -5.70437 | -45.45542 | 2025-09-10 04:40:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1a9d3daf-add9-35dc-934a-e1424f7102f5 | -6.05053 | -43.12578 | 2025-09-10 04:40:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 3.8 |
| a278d6fd-7230-315f-a854-6d1c4581bad9 | -5.63168 | -43.1128 | 2025-09-10 04:40:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 1.2 |
| ac19479c-9eff-3c5f-b92c-6b59fdc2c033 | -6.3169 | -43.4159 | 2025-09-10 04:40:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a7cfc79c-37e7-37e7-8c32-4553f69870a6 | -5.84482 | -44.8213 | 2025-09-10 04:40:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b444d878-c03c-3c9f-ae9f-94782cd10736 | -5.64521 | -42.62029 | 2025-09-10 04:40:00 | NPP-375D | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| ad7fe123-0fe8-310a-a06d-5179530e7bad | -5.66057 | -43.90204 | 2025-09-10 04:40:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a89ea818-5877-3084-9f25-ecc7aaaacd9b | -4.42092 | -47.95896 | 2025-09-10 04:40:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dec6817c-0e94-3f27-8060-2da926223e82 | -5.74931 | -47.46798 | 2025-09-10 04:40:00 | NPP-375D | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f69c928c-5ea7-3d2e-a325-5c4772581d6b | -6.27484 | -44.48056 | 2025-09-10 04:40:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4bf17b3c-50bb-34c4-90ad-3aa78a015fb3 | -4.1992 | -55.13148 | 2025-09-10 04:40:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 812e78d9-7771-3f84-8863-b4762b8e156a | -6.20486 | -43.50462 | 2025-09-10 04:40:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bf02bdfd-180f-3918-993b-a0aa1bdfbc4c | -5.98535 | -43.70913 | 2025-09-10 04:40:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5c36b74b-69ac-3f22-950d-6d191d939473 | -5.41946 | -45.88154 | 2025-09-10 04:40:00 | NPP-375D | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 559371c5-8764-3418-90d1-0eea7f775c76 | -5.42153 | -43.45159 | 2025-09-10 04:40:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| d2c0ab84-779b-3a9c-bb0f-dca3e1f8629d | -5.99321 | -46.19574 | 2025-09-10 04:40:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 04e9d411-913a-3d8b-b2d4-52d487ddba11 | -4.47068 | -48.11491 | 2025-09-10 04:40:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7f469046-9a0e-3e55-8504-c64b1cb56d38 | -5.64549 | -43.91859 | 2025-09-10 04:40:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 99593917-af13-3848-8e1b-aa3f56465c72 | -6.17058 | -41.05195 | 2025-09-10 04:40:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 957c8d0f-d58d-33fb-9c6d-2d589c9dc4d6 | -5.77385 | -45.53283 | 2025-09-10 04:40:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| db549026-a0c8-309f-8b37-8d7d99a1e3bd | -5.20341 | -45.4341 | 2025-09-10 04:40:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3923bea2-f6bd-3d08-91e0-f82dd1138521 | -5.1183 | -44.66217 | 2025-09-10 04:40:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 80f89285-3a62-33d5-bf8f-0c72de2304fa | -6.17107 | -43.37509 | 2025-09-10 04:40:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 55474f70-e5fc-396b-bc20-54cc7e0fde60 | -5.48443 | -42.66055 | 2025-09-10 04:40:00 | NPP-375D | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 73c9e1de-4880-3b81-8144-e73653780eb4 | -5.58493 | -42.91191 | 2025-09-10 04:40:00 | NPP-375D | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 2960fff8-eb3a-3d64-8467-545d0a770e88 | -6.19973 | -43.29923 | 2025-09-10 04:40:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 17dcbba3-aaa1-3422-a4ab-21647550099d | -6.56175 | -43.14972 | 2025-09-10 04:40:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6773901e-f258-3cb2-b4d6-79d4b8e00130 | -6.48352 | -41.75712 | 2025-09-10 04:40:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 65ca84ee-d8cf-3e27-8698-6bf812292678 | -5.76397 | -45.52217 | 2025-09-10 04:40:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 04905897-0508-30e5-b19e-f11564fb36e8 | -6.17497 | -41.04737 | 2025-09-10 04:40:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| d20de5dd-aca5-3f52-920b-6ca734f5ecc8 | -5.53752 | -42.65709 | 2025-09-10 04:40:00 | NPP-375D | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 8.9 |
| 2e23696c-af5d-3b9d-8d73-f8fa90f56892 | -4.49058 | -42.92628 | 2025-09-10 04:40:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 06b63ffb-61ef-3d9e-a204-89b070d11b14 | -5.64139 | -42.61483 | 2025-09-10 04:40:00 | NPP-375D | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| a3d66848-8cc7-36af-b40e-8614e08b701d | -4.40391 | -42.11657 | 2025-09-10 04:40:00 | NPP-375D | BOA HORA | PIAUÍ | Brasil | 2201770 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 22694eda-52ef-337f-8139-4a8e1e8ace48 | -5.50292 | -42.67446 | 2025-09-10 04:40:00 | NPP-375D | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 659b4f32-a265-3b23-8425-2bccb1d0718d | -5.91165 | -45.79846 | 2025-09-10 04:40:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 332051c7-e53d-31aa-b74b-85f5f5b04f6d | -5.72629 | -45.41269 | 2025-09-10 04:40:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3f91cb1f-7f67-3787-96e9-8c3d5b606225 | -5.22486 | -43.70283 | 2025-09-10 04:40:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| f635002e-f948-3520-8558-c58f24c5f5bd | -6.48207 | -42.41386 | 2025-09-10 04:40:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 88e69b1a-698e-30d2-8696-a51f6462e5b3 | -5.96404 | -45.80192 | 2025-09-10 04:40:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ad726a5a-2439-3051-9891-ed3c2cf6f3da | -5.96881 | -44.25814 | 2025-09-10 04:40:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 70742646-ff47-38ef-a8d0-e7c82728da85 | -4.86785 | -42.77031 | 2025-09-10 04:40:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 76df6b8d-0568-3c0a-b6e7-0d5afe25932f | -6.56237 | -43.14548 | 2025-09-10 04:40:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 628ac0a3-3e35-3571-9fa3-84373aa80f64 | -5.42677 | -45.88262 | 2025-09-10 04:40:00 | NPP-375D | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9e51fa89-63c9-3a69-9443-a936284a509e | -5.6647 | -43.90271 | 2025-09-10 04:40:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1e323ebb-e8de-3247-85e1-321cd3ba9f2e | -6.25132 | -43.39918 | 2025-09-10 04:40:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 561e9b2c-0334-3cfd-a788-fe774d43f3bd | -5.87663 | -43.98224 | 2025-09-10 04:40:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 499e7077-6fc6-34eb-b22b-a23b2223a273 | -4.94302 | -45.29633 | 2025-09-10 04:40:00 | NPP-375D | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7a14e113-5201-3988-a28c-88c0d908c0e7 | -6.28887 | -44.21866 | 2025-09-10 04:40:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6db4feea-f5b2-35b7-977d-1b1b7cf7e91d | -5.74987 | -47.46429 | 2025-09-10 04:40:00 | NPP-375D | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a3fbe55b-61ff-3726-acf3-8a01577a9c5c | -6.39843 | -43.50084 | 2025-09-10 04:40:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ed753fb3-7e4f-399d-91a2-483c89f0e6ba | -5.68749 | -43.34238 | 2025-09-10 04:40:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| decf9064-b015-3887-83fb-231d396e7c1d | -5.41672 | -43.45484 | 2025-09-10 04:40:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 10635efc-d917-36c3-b0f2-4149fd5f91c2 | -6.25932 | -43.40465 | 2025-09-10 04:40:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 908683d9-9498-3bd4-a124-c64f648785e5 | -5.6746 | -43.89282 | 2025-09-10 04:40:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6b636cd4-e49b-342d-bd2c-580c353a2d25 | -5.81155 | -45.66841 | 2025-09-10 04:40:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8c6731a4-bc27-3d95-b8e0-394236dcf743 | -5.57426 | -42.92339 | 2025-09-10 04:40:00 | NPP-375D | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 295423ef-8cd9-3219-ba63-2b91ec7b3d7f | -6.0562 | -43.11775 | 2025-09-10 04:40:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 1aca3710-c13d-36ab-9391-9cb62db701b6 | -6.35392 | -44.06349 | 2025-09-10 04:40:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 65274081-5375-3cda-a24b-61670ebb1401 | -5.42131 | -43.4235 | 2025-09-10 04:40:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8abc3ca9-4de3-3c60-8d14-5e847d6a2d78 | -3.54271 | -49.93879 | 2025-09-10 04:40:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| db8c1344-be4b-3989-993c-8cddd632b8eb | -4.09141 | -41.57563 | 2025-09-10 04:40:00 | NPP-375D | BRASILEIRA | PIAUÍ | Brasil | 2201960 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| bdd0e7df-32b9-326c-8202-29db061acaf7 | -5.81017 | -45.66958 | 2025-09-10 04:40:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8070ada8-bba7-3a9b-80f8-2a9219d2fb94 | -5.93976 | -45.68635 | 2025-09-10 04:40:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0e3a419f-8c6c-365b-9b54-402ec7aee20f | -6.17538 | -41.04445 | 2025-09-10 04:40:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| ec353b65-6440-3ad5-aa45-56f749e5862b | -6.17478 | -43.37995 | 2025-09-10 04:40:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a827fae5-a3ae-3a58-9508-a1f907af5599 | -5.53004 | -46.49665 | 2025-09-10 04:40:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 640c9ddb-910a-3eed-8098-7d439abe0209 | -5.67406 | -43.89649 | 2025-09-10 04:40:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 50e79bba-244b-38ab-9761-55cb5ef25815 | -5.93922 | -45.81607 | 2025-09-10 04:40:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6c10d58d-ddb4-39d1-a5f8-c344a4642ef5 | -6.25965 | -43.41579 | 2025-09-10 04:40:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 23.1 |
| 2baa580b-1ac3-30b2-849d-5ef4857e4f5e | -5.62732 | -43.11218 | 2025-09-10 04:40:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 1.2 |
| a686d7b5-f8aa-3536-89ae-f2a3a30395ff | -6.0518 | -43.1172 | 2025-09-10 04:40:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 329e5c63-a6d7-3625-bf67-b7f716a399f3 | -3.67899 | -49.01814 | 2025-09-10 04:40:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e8230eb5-8d9a-3141-8336-cbdbb8819e72 | -3.63826 | -49.21046 | 2025-09-10 04:40:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 838db4cb-6c62-3671-8d2f-b8622a418144 | -6.255 | -43.40406 | 2025-09-10 04:40:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 7417f2f4-95a1-32ae-97c3-b98912bb60fc | -6.25277 | -43.40228 | 2025-09-10 04:40:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 293ce9fb-ad41-3026-9583-044ceeefa282 | -6.05808 | -43.13525 | 2025-09-10 04:40:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 94dd0ef8-a617-3652-84e7-9b52fe335616 | -2.51303 | -51.90511 | 2025-09-10 04:40:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f0ac65ad-292f-3df4-b6e5-1d7ac0fb6506 | -4.72572 | -44.45854 | 2025-09-10 04:40:00 | NPP-375D | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8a6f12af-0c4f-3d18-99ac-3f6d3333b1da | -5.96271 | -45.81064 | 2025-09-10 04:40:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e3cf74e8-ed22-3e9d-8af9-fe84d3122f4c | -5.78449 | -44.84991 | 2025-09-10 04:40:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c9368215-4576-3caf-b388-29047e9d1f32 | -5.76092 | -42.75359 | 2025-09-10 04:40:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| da4927d5-8d89-39fc-b715-ec8d7b64db05 | -6.25158 | -43.41063 | 2025-09-10 04:40:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b8b5e5e3-b1c9-3b3e-97e4-d1cc5b4da395 | -5.45964 | -43.429 | 2025-09-10 04:40:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6678e8da-2005-34d6-8eed-f2c71d87e82b | -6.24944 | -43.41169 | 2025-09-10 04:40:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 452dc311-4275-36cc-8826-962cb1c9ebf3 | -5.88702 | -46.08758 | 2025-09-10 04:40:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f3224ee0-9b84-3ee8-9881-a51124471d7e | -5.5823 | -45.03385 | 2025-09-10 04:40:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 15.2 |
| c50861f3-95a9-3d0e-a905-b5c4d3fcd5bf | -6.17143 | -41.04617 | 2025-09-10 04:40:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 516d819d-19f5-36e1-aad9-9513a759c65d | -3.96431 | -43.24245 | 2025-09-10 04:40:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 665f2d41-dd91-3741-9172-800ed7ddf930 | -5.72124 | -43.89224 | 2025-09-10 04:40:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| af0774bf-fd04-347e-b85d-f0b48e7f7cb2 | -6.09874 | -44.77743 | 2025-09-10 04:40:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fb6a44d2-155f-3411-b509-7645e210a1e7 | -5.66363 | -43.90999 | 2025-09-10 04:40:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 48934bb8-73c0-3503-8baf-b132a1ae2ee4 | -5.36888 | -45.9686 | 2025-09-10 04:40:00 | NPP-375D | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0ef093f7-f694-3052-a366-b149904960ac | -3.04541 | -48.96109 | 2025-09-10 04:40:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 588b3556-cff3-3608-bac3-acf32883247d | -5.64455 | -42.62483 | 2025-09-10 04:40:00 | NPP-375D | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |


[Clique aqui para ver as próximas entradas](README53.md)
