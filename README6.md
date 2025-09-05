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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e16fa70f-e937-3e9d-8f82-54d5f11dee1a | -7.68282 | -50.26307 | 2025-09-05 00:33:00 | TERRA_M-M | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 20.8 |
| ef3b492e-504e-3586-bd4a-d9ac04d63946 | -2.78884 | -49.62796 | 2025-09-05 00:33:00 | TERRA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| c946d7d2-62e7-3201-9bce-15848a51584d | -4.20942 | -50.44017 | 2025-09-05 00:33:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| fd54fc07-ca23-3969-8a31-0c372e3b1158 | -8.09297 | -45.33314 | 2025-09-05 00:33:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 111.0 |
| c2dcbcca-2dfc-3057-a180-277e728af25e | -6.13676 | -44.58465 | 2025-09-05 00:33:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 1950e5ec-cc56-3cb0-aaa5-635510542964 | -5.5542 | -46.19873 | 2025-09-05 00:33:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 48.3 |
| 462e9397-1368-3a32-a3bb-d300bb25f282 | -6.90198 | -45.1867 | 2025-09-05 00:33:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 11.7 |
| a3b34141-7060-3580-a214-a271124c70bb | -3.2362 | -50.05654 | 2025-09-05 00:33:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 5bb07fe2-66b4-3c20-aa7c-f01465cea75d | -5.56356 | -46.19736 | 2025-09-05 00:33:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 28.8 |
| 6bf0d9c3-f226-32e4-8efe-f5f9f4a978a8 | -8.02383 | -45.42438 | 2025-09-05 00:33:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 21.0 |
| d82b1622-98e3-3e57-ace1-02249b6c3a92 | -7.05472 | -50.85627 | 2025-09-05 00:33:00 | TERRA_M-M | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 14.6 |
| c00d13f7-e4de-33bd-b0c5-92d151b71fac | -5.98912 | -49.23455 | 2025-09-05 00:33:00 | TERRA_M-M | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 7ca1c0e2-c52b-3201-bd00-b1bfcbce080e | -7.46294 | -48.96751 | 2025-09-05 00:33:00 | TERRA_M-M | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | 6.0 |
| bdd14bfe-24b6-3dd0-81d4-f7a95d87b3e3 | -6.27991 | -53.4362 | 2025-09-05 00:33:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 19.6 |
| 43322f9d-e188-3260-b95b-b51be7e03fd7 | -7.76063 | -48.78162 | 2025-09-05 00:33:00 | TERRA_M-M | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 61fb73e8-578f-362f-a7c4-2b4eded4ecfe | -9.70813 | -51.07396 | 2025-09-05 00:33:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 94.5 |
| 18de6c47-94a4-308a-b791-223ae3051002 | -8.44351 | -49.20135 | 2025-09-05 00:33:00 | TERRA_M-M | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| a09f51b9-79ec-3884-82bf-59040b0d4f1f | -8.01328 | -45.45268 | 2025-09-05 00:33:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 70c5ada5-4020-3539-83bf-a00c41e267fb | -8.00237 | -45.44409 | 2025-09-05 00:33:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 13.4 |
| c048d038-2ab0-3399-8056-1f97f05f4596 | -6.05425 | -46.00278 | 2025-09-05 00:33:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 21.7 |
| 5e6e91c6-9ae5-322a-9d51-bdb2e38ace96 | -6.69523 | -44.82484 | 2025-09-05 00:33:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 17.4 |
| f4ec11b0-90b3-342d-b592-cbf4e1c6cafc | -3.85226 | -48.97702 | 2025-09-05 00:33:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 92c107da-e73e-3550-a57a-8530b06bd456 | -6.96301 | -45.53843 | 2025-09-05 00:33:00 | TERRA_M-M | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 9e04b490-28af-382e-aa3f-3fe44cb8aeac | -8.93962 | -48.64681 | 2025-09-05 00:33:00 | TERRA_M-M | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 48.0 |
| de7723ae-c2a4-36a3-8679-7970ad450e9c | -7.30113 | -44.07349 | 2025-09-05 00:33:00 | TERRA_M-M | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 016e434b-7551-3af3-9d6a-5db5d0c2b919 | -6.27326 | -53.54156 | 2025-09-05 00:33:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 36cc1b82-5ee9-3623-8228-54f1f3a5c3c4 | -12.7522 | -56.9622 | 2025-09-05 00:36:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 041ab25b-570c-3f0d-bc73-fd97f3f41e9a | -11.4869 | -52.2374 | 2025-09-05 00:36:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7e0a4b8a-1cb1-395e-8784-873ab4729479 | -9.1897 | -55.231098 | 2025-09-05 00:36:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 48c5ac22-43ea-3b32-9df8-17d7c0e33d2e | -15.8509 | -55.970001 | 2025-09-05 00:36:00 | METOP-B | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 7f459f96-9b27-3ffb-a82a-d8d293feceed | -5.3411 | -60.134998 | 2025-09-05 00:36:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b61e6c9b-22f5-3ac4-887e-52f58301ab34 | -9.5516 | -51.088299 | 2025-09-05 00:36:00 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 27a0c158-864c-3664-8d15-6346eabcf373 | -12.3578 | -53.873901 | 2025-09-05 00:36:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6696aa89-0122-3eb4-8bc1-0c9d98466c3a | -8.6278 | -49.656601 | 2025-09-05 00:36:00 | METOP-B | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d2fc724e-504b-3091-91b0-661181f1b01c | -11.4991 | -54.554298 | 2025-09-05 00:36:00 | METOP-B | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c7e8a212-9011-3764-bed9-01d926d9b9e5 | -7.6508 | -52.147598 | 2025-09-05 00:36:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f35e2dd5-a8f6-374f-a3e1-59b657202efa | -17.387899 | -46.652901 | 2025-09-05 00:36:00 | METOP-B | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 04d47677-9889-3d60-a3d7-4fab2fd21328 | -5.5892 | -49.312199 | 2025-09-05 00:36:00 | METOP-B | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 02cbb3ca-127f-3e64-8550-79ff3d419de2 | -24.1691 | -50.750999 | 2025-09-05 00:36:00 | METOP-B | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 3015d6c1-7a1c-3ca3-82c9-a2c2ad905e79 | -20.382299 | -46.1423 | 2025-09-05 00:36:00 | METOP-B | PIUMHI | MINAS GERAIS | Brasil | 3151503 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 0c8f20e2-374b-31c4-8db2-d0653d98aa23 | -11.4967 | -52.2351 | 2025-09-05 00:36:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8c246091-8636-388b-ac2b-6c81fd6634ee | -9.1815 | -55.240299 | 2025-09-05 00:36:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cf89062b-a501-3114-ac86-5b770f2b081e | -5.4399 | -45.057598 | 2025-09-05 00:36:00 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4bc6c158-eccd-3f81-bba9-95dfde71a854 | -10.0008 | -55.177799 | 2025-09-05 00:36:00 | METOP-B | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| cee0b48a-da33-3db1-b607-5dd0a7279df2 | -15.447 | -52.9006 | 2025-09-05 00:36:00 | METOP-B | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a2e0f53e-afc7-38e0-a6dc-2478951e18f8 | -15.5872 | -53.639801 | 2025-09-05 00:36:00 | METOP-B | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a4691aa9-6db2-304f-a01b-e2b79e849b61 | -8.7188 | -52.037998 | 2025-09-05 00:36:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6f0d0b41-f526-3eb3-902d-2a964c96bf4f | -7.5383 | -50.284698 | 2025-09-05 00:36:00 | METOP-B | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ff1eb465-7a1d-3901-aa37-95ee2a979562 | -14.8935 | -49.6036 | 2025-09-05 00:36:00 | METOP-B | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 484be4f7-b476-3620-bb25-fc6670210ed2 | -12.9692 | -57.1213 | 2025-09-05 00:36:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| cc17f04d-0d4e-3113-9092-059b5327d0c6 | -6.4434 | -44.563 | 2025-09-05 00:36:00 | METOP-B | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 52541cf0-8a19-3aaa-a2cb-bcabecc10649 | -11.6899 | -51.4561 | 2025-09-05 00:36:00 | METOP-B | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 57ea7533-f024-333f-ba8e-e70d6120681b | -11.0574 | -55.026001 | 2025-09-05 00:36:00 | METOP-B | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d3a866db-1d4a-3eca-9e05-d65bc8eac1bb | -11.1778 | -55.249199 | 2025-09-05 00:36:00 | METOP-B | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0f2a3d1c-9080-3ee4-80b3-178d934255fc | -6.1364 | -53.462002 | 2025-09-05 00:36:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 162884b7-3279-31eb-a1bc-0397ef1659a8 | -11.4983 | -52.242298 | 2025-09-05 00:36:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 42751771-53a5-392b-a430-3dde584fa04b | -7.5471 | -50.322498 | 2025-09-05 00:36:00 | METOP-B | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c51bf5cb-a68b-3817-9e6f-eb8f5fc524fb | -12.7424 | -56.964298 | 2025-09-05 00:36:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a6be045b-e0e7-3078-9cbd-76b21e082e0d | -7.7444 | -45.340698 | 2025-09-05 00:36:00 | METOP-B | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| d9dabed3-50cb-397a-ba44-a534722094f6 | -5.4592 | -45.052898 | 2025-09-05 00:36:00 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| abdf7506-b4ab-3460-a921-96df9d02ec5c | -21.2227 | -46.984901 | 2025-09-05 00:36:00 | METOP-B | MONTE SANTO DE MINAS | MINAS GERAIS | Brasil | 3143203 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 2ee70ef4-8b31-32d1-8aaf-744e7132430a | -14.9992 | -52.364498 | 2025-09-05 00:36:00 | METOP-B | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 46ef5ecf-e3dc-336d-856a-f2b77b6841aa | -7.5734 | -50.346199 | 2025-09-05 00:36:00 | METOP-B | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 68745932-5f32-3c5a-869b-40ae271b2dfc | -15.613 | -53.664101 | 2025-09-05 00:36:00 | METOP-B | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 8e8706bd-904c-3e46-bd02-46f32d82cfb4 | -10.3513 | -50.4468 | 2025-09-05 00:36:00 | METOP-B | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d432b5e6-c218-33f7-8785-9839aaf38214 | -5.5821 | -49.326099 | 2025-09-05 00:36:00 | METOP-B | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e1bc070a-ab64-3a08-9c33-24c12e501ea1 | -7.8608 | -45.478199 | 2025-09-05 00:36:00 | METOP-B | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 7ce1f21e-fbb4-3245-a7e3-43da6277f42e | -7.5831 | -50.343899 | 2025-09-05 00:36:00 | METOP-B | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d164d4de-bbfc-3e8b-a4ca-9cbe3035345e | -9.0725 | -57.099201 | 2025-09-05 00:36:00 | METOP-B | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a5f65340-2e87-3681-923d-741cf93506e1 | -10.3291 | -53.639 | 2025-09-05 00:36:00 | METOP-B | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c1273b3f-a840-36ba-8191-5d3b46215c5a | -15.0216 | -52.418999 | 2025-09-05 00:36:00 | METOP-B | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 83bf6b87-4ea4-311b-917c-7f1776559fd2 | -6.7024 | -52.823399 | 2025-09-05 00:36:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4f5f20da-86fb-3fcc-a3c9-5fc725feee0f | -10.3353 | -53.666801 | 2025-09-05 00:36:00 | METOP-B | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 094272dd-10b1-3367-9afd-09f4a3a707d3 | -7.8704 | -45.434601 | 2025-09-05 00:36:00 | METOP-B | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 194c9571-8e94-34fb-aaaa-97a2618a2f87 | -14.1305 | -45.238998 | 2025-09-05 00:36:00 | METOP-B | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 564247fc-ce1c-383b-a399-e8d4e49ea6d7 | -14.9894 | -52.366798 | 2025-09-05 00:36:00 | METOP-B | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 79d57028-8900-3ab8-b9ed-370bf5663343 | -11.4738 | -52.225201 | 2025-09-05 00:36:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 054a36bd-d202-3edf-b455-1c9fa89ed5f1 | -5.3606 | -60.130901 | 2025-09-05 00:36:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c9f24022-e296-334b-a648-0c5abf5021f2 | -6.7007 | -52.816002 | 2025-09-05 00:36:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1d06b9f9-608d-3d83-8cf8-d0209babd346 | -6.6828 | -52.8279 | 2025-09-05 00:36:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 99a2f721-dd44-3164-9e4f-aec64860557d | -9.8378 | -51.656898 | 2025-09-05 00:36:00 | METOP-B | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 62a914e0-b4b7-3c65-b975-0baf50741537 | -10.3193 | -53.641201 | 2025-09-05 00:36:00 | METOP-B | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| da352a8e-31a8-31c1-88e6-8835948aa340 | -12.3465 | -53.869099 | 2025-09-05 00:36:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 75e04fa2-40ae-3aea-bcf5-73a781259fd5 | -6.1168 | -53.4664 | 2025-09-05 00:36:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6c3e7fd1-96d2-3a6b-9ec8-0f7504034c0d | -11.6263 | -50.691002 | 2025-09-05 00:36:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 3be9bfd6-0762-3832-a72b-f36f17d38db1 | -7.7394 | -45.320702 | 2025-09-05 00:36:00 | METOP-B | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| a41dabd7-3fe9-3e8d-80f4-fd42ba8f7a09 | -23.4643 | -52.905201 | 2025-09-05 00:36:00 | METOP-B | RONDON | PARANÁ | Brasil | 4122602 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 6410acd1-ee04-34c6-a7f3-9bbcd75b8757 | -8.9225 | -47.027699 | 2025-09-05 00:36:00 | METOP-B | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 590da2c6-dfc5-3332-8591-f47d7a925c26 | -7.5636 | -50.348499 | 2025-09-05 00:36:00 | METOP-B | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 643c9291-5750-37d2-8ab6-7f5b8ca7900d | -6.4397 | -44.589001 | 2025-09-05 00:36:00 | METOP-B | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 78dc7777-d521-3a04-bd11-bc790505ec7e | -9.0645 | -57.109402 | 2025-09-05 00:36:00 | METOP-B | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5adfc52f-0534-3e7b-b32b-6a97daf503a1 | -11.5374 | -52.1875 | 2025-09-05 00:36:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f61e6f8b-8cb9-323d-b8cf-cb38fad8f3b0 | -22.172899 | -48.633598 | 2025-09-05 00:36:00 | METOP-B | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 47fd1ee5-e5c3-3ed3-9187-55059271aa6a | -7.8607 | -45.437 | 2025-09-05 00:36:00 | METOP-B | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 7b5097ce-350a-377a-985a-c241516a53b5 | -15.5758 | -53.6348 | 2025-09-05 00:36:00 | METOP-B | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 67262440-f803-36c6-be0d-b8ce704635d8 | -10.0897 | -50.563702 | 2025-09-05 00:36:00 | METOP-B | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 84ea3a5f-10a5-3ca3-9958-754de8b62d01 | -14.1346 | -45.254902 | 2025-09-05 00:36:00 | METOP-B | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f5675db6-f28e-3b16-8875-5de496214608 | -20.314699 | -54.540699 | 2025-09-05 00:36:00 | METOP-B | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 7fc5c864-dfe4-3474-868a-9c215a0a46b6 | -5.3629 | -60.141499 | 2025-09-05 00:36:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9a9b0348-26a4-3945-8acf-06db26716721 | -16.1625 | -52.973801 | 2025-09-05 00:36:00 | METOP-B | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README7.md)
