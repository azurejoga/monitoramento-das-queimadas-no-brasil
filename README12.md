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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 120df2c8-fadb-33a2-bf37-2d658796e75a | -3.32908 | -45.60987 | 2025-12-04 04:21:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2fc8c1d1-b798-3c85-9f07-85c6f3b9ba6a | -3.65957 | -43.60215 | 2025-12-04 04:21:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c4529016-e367-36d7-b4a6-34cf007e016a | -5.34402 | -42.11726 | 2025-12-04 04:21:00 | NOAA-21 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 121d0326-7814-307a-ab01-de00d842d975 | -4.56923 | -43.80847 | 2025-12-04 04:21:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 95132def-75aa-3d24-a2d4-3bf64df631b0 | -4.78101 | -46.12773 | 2025-12-04 04:21:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c0a7f0e0-0678-3228-9bf5-eec99ffb5335 | -4.47597 | -44.25282 | 2025-12-04 04:21:00 | NOAA-21 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 45e8de97-20e2-374d-95e4-bbcd6f72dd0a | -5.44605 | -46.90608 | 2025-12-04 04:21:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bd342340-dc99-3aa2-a13b-b6fd5f6c1f41 | -3.03562 | -44.26194 | 2025-12-04 04:21:00 | NOAA-21 | ROSÁRIO | MARANHÃO | Brasil | 2109601 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 646c7043-953e-3b21-9792-738217f90943 | -4.36478 | -46.33656 | 2025-12-04 04:21:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 92a9891d-03a4-38fd-a8c2-39dddcd51c0c | -5.99069 | -44.59495 | 2025-12-04 04:21:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1c06a655-96f1-3c32-a6c3-4ebb41a21e24 | -2.53745 | -49.45144 | 2025-12-04 04:21:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 7e8377ed-e0fc-3024-8d3f-12c24ad02cdd | -3.23008 | -46.85553 | 2025-12-04 04:21:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 65d21da0-361a-3316-b0b5-a7c71e8d70f8 | -5.09065 | -37.54701 | 2025-12-04 04:21:00 | NOAA-21 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 2.8 |
| cdc4c52a-5082-31a1-8480-13276049fb5b | -3.33127 | -45.01949 | 2025-12-04 04:21:00 | NOAA-21 | CAJARI | MARANHÃO | Brasil | 2102507 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d50944a8-a854-3e46-82b9-f16fc11b7cc9 | -1.96576 | -46.05426 | 2025-12-04 04:21:00 | NOAA-21 | MARACAÇUMÉ | MARANHÃO | Brasil | 2106326 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1d9d52d4-fe41-3d96-9c49-5edfa4c579f4 | -4.00789 | -46.54984 | 2025-12-04 04:21:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 968b3bef-2628-3c49-8505-c19ee5374642 | -5.79839 | -42.99175 | 2025-12-04 04:21:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 3dd4c372-bf88-3ed0-bc6c-b4b37b14e7ef | -4.74342 | -45.40758 | 2025-12-04 04:21:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7ab2cb8e-11ef-3ebb-ab00-e8e38c0abf40 | -4.31199 | -43.23389 | 2025-12-04 04:21:00 | NOAA-21 | AFONSO CUNHA | MARANHÃO | Brasil | 2100105 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3d880f96-ce42-3135-8507-9a2d5fa869e1 | -4.85766 | -40.75858 | 2025-12-04 04:21:00 | NOAA-21 | ARARENDÁ | CEARÁ | Brasil | 2301257 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| a1f00a05-198d-3a1b-97c7-188c53f8caf2 | -5.03005 | -43.97275 | 2025-12-04 04:21:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5583fa5f-d9d6-3f76-84da-a11a21355504 | -4.6966 | -44.49599 | 2025-12-04 04:21:00 | NOAA-21 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 55e50054-0121-3501-a54a-9546518b1985 | -5.08982 | -37.54865 | 2025-12-04 04:21:00 | NOAA-21 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 2.0 |
| cc647481-13b8-3f10-8cb9-23b05bc64772 | -3.25164 | -41.42413 | 2025-12-04 04:21:00 | NOAA-21 | LUÍS CORREIA | PIAUÍ | Brasil | 2205706 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 68bbb95f-6390-35ab-87b3-63062ed56f69 | -5.98684 | -44.59789 | 2025-12-04 04:21:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 9ed116a9-4815-3562-941b-62835845ab12 | -2.79163 | -45.42613 | 2025-12-04 04:21:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f9b8ed29-ed0f-39be-a224-cf6ae56bfb7a | -2.50971 | -48.47719 | 2025-12-04 04:21:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c44f91e4-a193-383f-8e8b-794e35b8e1c7 | -4.50381 | -45.7753 | 2025-12-04 04:21:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0c2a057c-5507-3aa1-819d-7a3660b4a524 | -7.21806 | -45.05129 | 2025-12-04 04:21:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7a4fe0fe-ab7a-3eb3-8108-db5a4d4b5ab8 | -4.73662 | -44.43519 | 2025-12-04 04:21:00 | NOAA-21 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 51e9b18e-4b33-38c7-8bd9-a78ab5a9c286 | -5.4152 | -45.76066 | 2025-12-04 04:21:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6a03788a-ab7f-38db-80b7-deeafc544ca4 | -1.98452 | -47.96708 | 2025-12-04 04:21:00 | NOAA-21 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5de02e04-9e21-3994-b789-170fde3bb5af | -4.39909 | -43.13187 | 2025-12-04 04:21:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 15.9 |
| ed793bee-2dae-3c14-8ed5-1ccf233c7cbc | -4.80984 | -45.67588 | 2025-12-04 04:21:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d9337c57-34de-3503-ae3a-60a68dd5054b | -6.28065 | -39.68548 | 2025-12-04 04:21:00 | NOAA-21 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 2904d094-4d52-3660-99df-05fd6ea251c5 | -2.54083 | -45.37273 | 2025-12-04 04:21:00 | NOAA-21 | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 9a58154f-9c90-3368-a4b5-ec6e985b3f4f | -5.24571 | -37.70341 | 2025-12-04 04:21:00 | NOAA-21 | GOVERNADOR DIX-SEPT ROSADO | RIO GRANDE DO NORTE | Brasil | 2404309 | 24 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 066791b0-dd77-3735-b1a8-151e15d5f635 | -2.12257 | -48.89135 | 2025-12-04 04:21:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7fcd0ed8-8f78-34bc-8977-3ce504934e4d | -4.2907 | -46.40201 | 2025-12-04 04:21:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0200106e-6836-30da-a932-4d1aaba34d92 | -4.3997 | -45.83249 | 2025-12-04 04:21:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5b18e038-e267-3eec-9373-0ccfd8b40643 | -5.46473 | -46.90104 | 2025-12-04 04:21:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cc1c995b-8d38-3e76-b58a-ccb5e441d0bb | -3.29603 | -50.20431 | 2025-12-04 04:21:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2d94e3ba-6609-368c-88f8-bad07a09f178 | -3.29944 | -50.18335 | 2025-12-04 04:21:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5da4a270-d031-30a0-aa35-cb99dad3108a | -4.74031 | -42.05589 | 2025-12-04 04:21:00 | NOAA-21 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| f9955c1f-df98-3fd4-9bce-4ef249b54256 | -2.7908 | -47.43632 | 2025-12-04 04:21:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3288304b-6f50-353b-8000-4f6200a1b8d7 | -3.82357 | -46.55338 | 2025-12-04 04:21:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 2fd91a73-8faf-3e9f-bc82-2e28b618f6c3 | -4.38388 | -47.65024 | 2025-12-04 04:21:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a84b267e-170b-3e14-8c78-f94a3d9800c0 | -2.84884 | -41.83257 | 2025-12-04 04:21:00 | NOAA-21 | ILHA GRANDE | PIAUÍ | Brasil | 2204659 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 93b3c303-3d24-3afa-819f-7ee065c34e12 | -4.30077 | -47.07778 | 2025-12-04 04:21:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 643ce409-48f3-35fe-8cc4-0af6b7329e14 | -6.90461 | -39.66225 | 2025-12-04 04:21:00 | NOAA-21 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| d2c6082e-cdc0-3c87-a05a-737c650ce25f | -3.38173 | -49.00684 | 2025-12-04 04:21:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8584b99f-e3a3-3046-81f4-128457856187 | -4.40577 | -43.1329 | 2025-12-04 04:21:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 49.7 |
| 06101eff-b2d6-3a2a-b328-5eb7aa1d5e8d | -1.42512 | -53.00894 | 2025-12-04 04:21:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5eb86f37-34d9-3c61-98f1-e14c1fffa6d7 | -2.31245 | -47.73775 | 2025-12-04 04:21:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8fc4fe1d-d4ad-3535-aaca-83edb718ba55 | -2.63713 | -48.03693 | 2025-12-04 04:21:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3cb091f0-2d90-3f64-bae3-d46925490896 | -4.51719 | -44.27348 | 2025-12-04 04:21:00 | NOAA-21 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fa5347c1-2541-3ec1-81f3-aafad2f5e09d | -2.95473 | -48.5876 | 2025-12-04 04:21:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5ecf1ed3-e1ba-38e5-8eff-dc0524e58a28 | -6.68246 | -39.50193 | 2025-12-04 04:21:00 | NOAA-21 | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 3.5 |
| fe6b7513-7ccd-3e9d-a2b2-ba8efc29d62a | -4.34245 | -45.79064 | 2025-12-04 04:21:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c45135a6-f494-37bc-9547-0b7d5c4c7cf8 | -4.93363 | -43.25803 | 2025-12-04 04:21:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 31d667e1-d9a6-38c9-bd75-26e0bd6b8889 | -5.00385 | -42.93735 | 2025-12-04 04:21:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| df14b3d9-d2e0-36ed-8f64-7f0ec8ef610a | -3.56659 | -47.18085 | 2025-12-04 04:21:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 662db4ee-23ac-398b-aa35-ae14b6d28256 | -4.39332 | -46.13485 | 2025-12-04 04:21:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1f5dbf0d-d7d0-30bd-94bd-06993cecaf53 | -4.03085 | -46.97566 | 2025-12-04 04:21:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 22461333-921e-350e-8c0c-ff5b9d905acb | -20.91617 | -56.36926 | 2025-12-04 04:23:00 | NOAA-21 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 2989a1e1-7c9e-3135-bf11-79276d0df81d | -19.63042 | -56.83569 | 2025-12-04 04:23:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| fdb91a5d-e9e4-3948-a4b8-138ead002a3d | -19.63425 | -56.76778 | 2025-12-04 04:23:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 33ffccbd-4b98-3d31-9f5a-fc5f67d0450b | -15.46119 | -39.23838 | 2025-12-04 04:23:00 | NOAA-21 | SANTA LUZIA | BAHIA | Brasil | 2928059 | 29 | 33 | nan | nan | nan | Mata Atlântica | 18.5 |
| c34f0b90-80a9-3a4d-ad31-c297fb82c581 | -10.51289 | -48.19516 | 2025-12-04 04:23:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d1426135-4ff2-3743-8682-827496f6be9f | -11.48807 | -40.60846 | 2025-12-04 04:23:00 | NOAA-21 | MIGUEL CALMON | BAHIA | Brasil | 2921203 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| ab5be1a3-30b0-39ff-be58-4ac4822e1817 | -19.63594 | -56.7672 | 2025-12-04 04:23:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 059dc2ae-cf7c-30cc-8b4c-774177dd79d6 | -19.27011 | -50.56277 | 2025-12-04 04:23:00 | NOAA-21 | LIMEIRA DO OESTE | MINAS GERAIS | Brasil | 3138625 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 95d92283-1c73-3785-80c2-9d5f06301c4f | -21.62258 | -56.1333 | 2025-12-04 04:23:00 | NOAA-21 | JARDIM | MATO GROSSO DO SUL | Brasil | 5005004 | 50 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 184f6b16-a78a-3270-b2df-126e46e7acf8 | -19.70193 | -49.20168 | 2025-12-04 04:23:00 | NOAA-21 | COMENDADOR GOMES | MINAS GERAIS | Brasil | 3116902 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 73e2f83d-99c5-315d-a50e-d9b1ca29c406 | -20.91673 | -56.37187 | 2025-12-04 04:23:00 | NOAA-21 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 6975cfd3-dafb-3c9c-917e-c0c14ca5f6ad | -19.63547 | -56.83685 | 2025-12-04 04:23:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 15108c0f-999f-3d8c-8261-afb584ed4230 | -14.15459 | -39.01209 | 2025-12-04 04:23:00 | NOAA-21 | MARAÚ | BAHIA | Brasil | 2920700 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| cb6f96a4-b549-3b1c-9b7d-cdaaa7a10fdc | -19.61988 | -56.84558 | 2025-12-04 04:23:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.1 |
| cbfe18fe-7a46-3fcb-b2ab-49f7b6f6b542 | -19.62908 | -56.84198 | 2025-12-04 04:23:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 32677d74-412f-39cc-ab08-def9c133ca75 | -19.61612 | -56.83809 | 2025-12-04 04:23:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 7a7be05c-5a08-32cb-8427-71e1f61cf25d | -21.62491 | -56.13575 | 2025-12-04 04:23:00 | NOAA-21 | JARDIM | MATO GROSSO DO SUL | Brasil | 5005004 | 50 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 06ee80ab-12a3-3e4a-a833-f0f1bbade160 | -20.91501 | -56.37476 | 2025-12-04 04:23:00 | NOAA-21 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 95a0238a-48e0-31c3-b86a-d61ce5759207 | -19.6348 | -56.84 | 2025-12-04 04:23:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 5f54ac0e-7672-3f6e-8e8c-080c7c472f1b | -19.62053 | -56.84242 | 2025-12-04 04:23:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.1 |
| 6664f556-d762-3d14-b3de-97bced37b308 | -19.63995 | -56.76582 | 2025-12-04 04:23:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| dc7ca179-a1bd-386e-a499-5818283756a1 | -19.62841 | -56.84513 | 2025-12-04 04:23:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 9.5 |
| 54a0ff9c-3440-3254-9e1e-5a1a891db677 | -22.90811 | -49.68953 | 2025-12-04 04:23:00 | NOAA-21 | SANTA CRUZ DO RIO PARDO | SÃO PAULO | Brasil | 3546405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| ef730463-fe24-37b2-817e-98990cacc30f | -21.6306 | -56.13167 | 2025-12-04 04:23:00 | NOAA-21 | JARDIM | MATO GROSSO DO SUL | Brasil | 5005004 | 50 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 002b9789-c098-33e9-bff4-91283a4d65d5 | -19.62268 | -56.84713 | 2025-12-04 04:23:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.3 |
| d1a72595-8d9c-32c8-bbb6-fb6be6b0f62c | -22.96375 | -49.95231 | 2025-12-04 04:23:00 | NOAA-21 | OURINHOS | SÃO PAULO | Brasil | 3534708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| b7358fe9-5555-3ae8-9367-7469dd339916 | -19.62117 | -56.83927 | 2025-12-04 04:23:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 04363b2d-ae6b-3bf3-95fd-078343a9e7a4 | -21.62724 | -56.13435 | 2025-12-04 04:23:00 | NOAA-21 | JARDIM | MATO GROSSO DO SUL | Brasil | 5005004 | 50 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 4b8f37c1-b60f-3ae8-b998-9af8e2079223 | -15.45647 | -39.2377 | 2025-12-04 04:23:00 | NOAA-21 | SANTA LUZIA | BAHIA | Brasil | 2928059 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 9a92dc8c-22d2-347f-af42-816170ba9f79 | -19.62975 | -56.83884 | 2025-12-04 04:23:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 2531daab-bf3b-3905-8fc4-1fa0eb1b8df8 | -19.6183 | -56.84281 | 2025-12-04 04:23:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 41fb9dcd-b4af-3a44-a9f8-1568b106de16 | -20.91561 | -56.37739 | 2025-12-04 04:23:00 | NOAA-21 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 10.4 |
| a171a2ec-d786-33f1-af6e-0aa7de062bc8 | -19.63491 | -56.76467 | 2025-12-04 04:23:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| b66777d7-de53-3d51-81b9-5b6663f05a95 | -21.62594 | -56.13062 | 2025-12-04 04:23:00 | NOAA-21 | JARDIM | MATO GROSSO DO SUL | Brasil | 5005004 | 50 | 33 | nan | nan | nan | Cerrado | 7.4 |
| ebd69513-cfee-32f3-be0b-36e9d0d70ade | -12.62643 | -47.43042 | 2025-12-04 04:23:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4aeddb01-53f4-39dc-a1bf-9816f7f92919 | -19.63414 | -56.84315 | 2025-12-04 04:23:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |


[Clique aqui para ver as próximas entradas](README13.md)
