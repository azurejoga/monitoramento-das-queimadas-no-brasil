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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2619a44e-2a58-3e46-9e68-f0d1b1487e47 | -12.3328 | -52.4743 | 2025-04-05 00:00:00 | GOES-16 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 90.2 |
| e971dc6f-a0ae-319a-9fd2-a158435520b6 | -9.7432 | -37.0672 | 2025-04-05 00:00:00 | GOES-16 | BATALHA | ALAGOAS | Brasil | 2700706 | 27 | 33 | nan | nan | nan | Caatinga | 83.8 |
| f71f43b4-0a4c-3ceb-a2f2-b4a798ee0951 | -8.1078 | -43.1175 | 2025-04-05 00:00:00 | GOES-16 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 80.8 |
| 34b6253c-d39c-3848-b611-02da4aec7f44 | -8.1078 | -43.1175 | 2025-04-05 00:10:00 | GOES-16 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 88.2 |
| a223fb9d-0d25-333a-bb1b-aa7701ff9c73 | -12.3328 | -52.4743 | 2025-04-05 00:10:00 | GOES-16 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 92.8 |
| cdf7bb1f-214a-34c7-8379-7564259290a5 | -20.5862 | -56.0392 | 2025-04-05 00:10:00 | GOES-16 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 79.4 |
| 97887431-8073-31f9-9ee6-4b6609e2cb5d | -12.3328 | -52.4743 | 2025-04-05 00:20:00 | GOES-16 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 103.4 |
| fc77a5c9-8550-3b3d-86ad-c1d9f81af03b | -20.5862 | -56.0392 | 2025-04-05 00:20:00 | GOES-16 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 62.9 |
| b84ab09f-bbd2-353b-b6cf-2c3acaff1bf9 | -8.1078 | -43.1175 | 2025-04-05 00:20:00 | GOES-16 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 102.5 |
| f031028d-705a-34e5-b12b-4afbb1a7fe5c | -8.1078 | -43.1175 | 2025-04-05 00:30:00 | GOES-16 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 68.6 |
| 2bca348b-0a7c-3798-b29f-0874d9b83c9b | -12.3328 | -52.4743 | 2025-04-05 00:30:00 | GOES-16 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 93.4 |
| 01dd6bc2-2bac-333a-be74-db6f554ddd34 | -12.3328 | -52.4743 | 2025-04-05 00:40:00 | GOES-16 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 88.3 |
| b1cecf7c-7a53-3b36-adaf-c52c5f9e4cf4 | -12.3328 | -52.4743 | 2025-04-05 00:50:00 | GOES-16 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 93.8 |
| 02f157ba-942a-3ec0-8d88-cdd4973ae757 | -10.5797 | -45.128799 | 2025-04-05 00:50:00 | METOP-C | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 50099a2a-08c2-35a9-80d1-3160d7821b4b | -12.3309 | -52.466999 | 2025-04-05 00:50:00 | METOP-C | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5c4cf8a0-157b-32ec-b523-5e998407a8fc | -12.3228 | -52.4771 | 2025-04-05 00:50:00 | METOP-C | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e4452255-a9ee-3336-b6ad-717ead7bc7d4 | -12.3292 | -52.459 | 2025-04-05 00:50:00 | METOP-C | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| db9513dc-61c2-350b-8dd3-241b4184dfe7 | -12.3344 | -52.483002 | 2025-04-05 00:50:00 | METOP-C | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9b6f11da-e01f-31f3-88c0-37479e612804 | -13.0439 | -45.011902 | 2025-04-05 00:50:00 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d1efbc49-2ca6-3cad-9f07-c47ea4f73f97 | -21.455999 | -48.7075 | 2025-04-05 00:50:00 | METOP-C | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 920780c3-35e3-3494-9920-db612dc29694 | -8.1125 | -43.123299 | 2025-04-05 00:50:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| a3f878e4-ac89-3df6-a7ac-3881e9224271 | -10.5822 | -45.139301 | 2025-04-05 00:50:00 | METOP-C | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 1fae9599-dd18-3c2b-a87c-807d07753f29 | -12.3326 | -52.474998 | 2025-04-05 00:50:00 | METOP-C | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| cf754af8-59c6-34ee-8f38-2dedff9da74c | -21.6301 | -48.752899 | 2025-04-05 00:50:00 | METOP-C | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| e38caa9c-5d47-3263-9d90-7ed61f9e7c2a | -12.3328 | -52.4743 | 2025-04-05 01:00:00 | GOES-16 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 95.5 |
| 3a64034b-df8c-3a24-aced-3ef97b5848dc | -12.3328 | -52.4743 | 2025-04-05 01:10:00 | GOES-16 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 68.4 |
| 37fd1ec4-9dda-34ec-bade-0a286f4f7863 | -8.1078 | -43.1175 | 2025-04-05 01:20:00 | GOES-16 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 52.7 |
| 073eb5d7-93d8-3e5b-944b-eb70c467745e | -12.3328 | -52.4743 | 2025-04-05 01:20:00 | GOES-16 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 77.5 |
| b3b57e10-9d09-3bfd-9413-42b2bff3be5b | -20.8512 | -47.7554 | 2025-04-05 01:20:00 | GOES-16 | BATATAIS | SÃO PAULO | Brasil | 3505906 | 35 | 33 | nan | nan | nan | Cerrado | 62.9 |
| a4b1b8ee-d6b9-3a0a-a69e-f4e51cd1e0bf | -20.83554 | -47.75792 | 2025-04-05 01:22:00 | TERRA_M-M | SALES OLIVEIRA | SÃO PAULO | Brasil | 3544905 | 35 | 33 | nan | nan | nan | Cerrado | 52.4 |
| 32abe8a7-9de6-3527-9a9f-9b3e3eef5841 | -23.14696 | -54.8964 | 2025-04-05 01:22:00 | TERRA_M-M | AMAMBAI | MATO GROSSO DO SUL | Brasil | 5000609 | 50 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 7d2aabaf-bb5e-3968-a81a-f25ec0ba84ab | -20.82982 | -47.76516 | 2025-04-05 01:22:00 | TERRA_M-M | SALES OLIVEIRA | SÃO PAULO | Brasil | 3544905 | 35 | 33 | nan | nan | nan | Cerrado | 73.9 |
| 88d7beef-1989-3b7d-8321-05bd8d175662 | -20.84009 | -47.78176 | 2025-04-05 01:22:00 | TERRA_M-M | SALES OLIVEIRA | SÃO PAULO | Brasil | 3544905 | 35 | 33 | nan | nan | nan | Cerrado | 33.5 |
| 85d18696-3d6f-3ff5-b2f9-189024668b72 | -20.58161 | -56.04153 | 2025-04-05 01:22:00 | TERRA_M-M | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 8af4880f-a1cc-3221-ad88-1f560f240b95 | -12.32486 | -52.46162 | 2025-04-05 01:24:00 | TERRA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 10.5 |
| daf2ba15-2c74-34db-96ba-5da876df1cf0 | -12.3267 | -52.4669 | 2025-04-05 01:24:00 | TERRA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 33.4 |
| a9b2709a-acf6-3df1-97df-121b325f6947 | -13.21082 | -53.25106 | 2025-04-05 01:24:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 8.4 |
| fb9ac323-d92e-32ba-a136-272384677e5a | -12.32735 | -52.47696 | 2025-04-05 01:24:00 | TERRA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 54.8 |
| 30359f68-146a-376b-b910-ce1b7f5df28b | -12.32908 | -52.48227 | 2025-04-05 01:24:00 | TERRA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 35.7 |
| a2121976-96fa-34d1-a711-041c6d0f6d20 | -8.1078 | -43.1175 | 2025-04-05 01:30:00 | GOES-16 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 57.5 |
| 316d935b-4bec-3d7d-81e0-fdd6f0a9ec66 | -12.3328 | -52.4743 | 2025-04-05 01:30:00 | GOES-16 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 69dd38c0-1de5-3a22-a234-05d0b38052ce | -8.1078 | -43.1175 | 2025-04-05 01:40:00 | GOES-16 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 58.9 |
| df08fec1-737c-34ee-ba18-8ec4dc479931 | -12.3328 | -52.4743 | 2025-04-05 01:40:00 | GOES-16 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 70.5 |
| 872d4f1c-0c6b-38a3-9d32-289def8f7b0f | -8.1078 | -43.1175 | 2025-04-05 01:50:00 | GOES-16 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 72.1 |
| febcbf2d-34f7-3180-906d-36129c30223a | -20.8306 | -47.7603 | 2025-04-05 02:00:00 | GOES-16 | SALES OLIVEIRA | SÃO PAULO | Brasil | 3544905 | 35 | 33 | nan | nan | nan | Cerrado | 67.8 |
| d247efa2-bc5e-3897-b069-3a0a73d768f4 | -20.8512 | -47.7554 | 2025-04-05 02:00:00 | GOES-16 | BATATAIS | SÃO PAULO | Brasil | 3505906 | 35 | 33 | nan | nan | nan | Cerrado | 79.6 |
| 03918b89-69ba-3989-9ca6-fc75379f7017 | -8.1078 | -43.1175 | 2025-04-05 02:00:00 | GOES-16 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 56.7 |
| 628bbe9d-7ef1-3538-bd73-10e8352178c1 | -20.8306 | -47.7603 | 2025-04-05 02:10:00 | GOES-16 | SALES OLIVEIRA | SÃO PAULO | Brasil | 3544905 | 35 | 33 | nan | nan | nan | Cerrado | 131.0 |
| fbe19f59-8a4e-3820-b47f-56563f2f2262 | -20.8512 | -47.7554 | 2025-04-05 02:10:00 | GOES-16 | BATATAIS | SÃO PAULO | Brasil | 3505906 | 35 | 33 | nan | nan | nan | Cerrado | 85.0 |
| def8bcaf-72fb-3e94-b5e6-48ffb7204447 | -8.1078 | -43.1175 | 2025-04-05 02:20:00 | GOES-16 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 63.6 |
| 0412550e-0ac5-3f6b-b7d0-4bf4cc117022 | -20.8512 | -47.7554 | 2025-04-05 02:20:00 | GOES-16 | BATATAIS | SÃO PAULO | Brasil | 3505906 | 35 | 33 | nan | nan | nan | Cerrado | 101.5 |
| 10706bab-9f2a-37b5-a660-ea4f0050f79a | -20.8306 | -47.7603 | 2025-04-05 02:20:00 | GOES-16 | SALES OLIVEIRA | SÃO PAULO | Brasil | 3544905 | 35 | 33 | nan | nan | nan | Cerrado | 108.2 |
| ddec2d35-bf3b-3ed9-abe0-7079cffebef0 | -12.3328 | -52.4743 | 2025-04-05 02:30:00 | GOES-16 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 13dce6c3-07e1-3898-9098-b632c3142139 | -20.8512 | -47.7554 | 2025-04-05 02:30:00 | GOES-16 | BATATAIS | SÃO PAULO | Brasil | 3505906 | 35 | 33 | nan | nan | nan | Cerrado | 81.0 |
| e6caad39-3bee-3d31-971a-0d7c6b2637ad | -20.8306 | -47.7603 | 2025-04-05 02:30:00 | GOES-16 | SALES OLIVEIRA | SÃO PAULO | Brasil | 3544905 | 35 | 33 | nan | nan | nan | Cerrado | 143.9 |
| ba32c9bb-1ab3-3558-a060-09f830e3822a | -10.5806 | -45.1413 | 2025-04-05 02:40:00 | GOES-16 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 66.9 |
| 4ab49763-0b80-34f6-aad6-163b2b9e109c | -20.8512 | -47.7554 | 2025-04-05 02:40:00 | GOES-16 | BATATAIS | SÃO PAULO | Brasil | 3505906 | 35 | 33 | nan | nan | nan | Cerrado | 89.7 |
| bf20c293-0379-31ad-8b74-198cb4d5adb1 | -12.3328 | -52.4743 | 2025-04-05 02:40:00 | GOES-16 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 55.4 |
| 41532656-abb9-3fac-9029-8c5b76269443 | -20.8306 | -47.7603 | 2025-04-05 02:40:00 | GOES-16 | SALES OLIVEIRA | SÃO PAULO | Brasil | 3544905 | 35 | 33 | nan | nan | nan | Cerrado | 112.3 |
| b4a79ac3-826e-353d-a44d-b62be53afd7f | -10.5806 | -45.1413 | 2025-04-05 02:50:00 | GOES-16 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 60.8 |
| 68961403-6e2c-30f1-a969-044dd6c5a553 | -12.3328 | -52.4743 | 2025-04-05 02:50:00 | GOES-16 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 52.1 |
| 97b7a9e0-6897-3a4c-9b67-28ad000e6593 | -20.8512 | -47.7554 | 2025-04-05 02:50:00 | GOES-16 | BATATAIS | SÃO PAULO | Brasil | 3505906 | 35 | 33 | nan | nan | nan | Cerrado | 91.2 |
| 213022c3-1274-3f72-b8d6-91d38395b83b | -20.8306 | -47.7603 | 2025-04-05 02:50:00 | GOES-16 | SALES OLIVEIRA | SÃO PAULO | Brasil | 3544905 | 35 | 33 | nan | nan | nan | Cerrado | 148.7 |
| 882068c4-9dfc-3054-8b36-aef2f868c376 | -8.1078 | -43.1175 | 2025-04-05 02:50:00 | GOES-16 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 62.7 |
| 48cff74c-03e0-366d-b071-e3a83e0eb345 | -10.5809 | -45.1183 | 2025-04-05 03:00:00 | GOES-16 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 54.2 |
| d3645651-d699-3b1b-9b63-2c08dc630a2c | -20.8306 | -47.7603 | 2025-04-05 03:00:00 | GOES-16 | SALES OLIVEIRA | SÃO PAULO | Brasil | 3544905 | 35 | 33 | nan | nan | nan | Cerrado | 133.5 |
| b7b4aafd-94ee-36ea-a5fa-8af5b3a00f51 | -20.8512 | -47.7554 | 2025-04-05 03:00:00 | GOES-16 | BATATAIS | SÃO PAULO | Brasil | 3505906 | 35 | 33 | nan | nan | nan | Cerrado | 97.4 |
| 5f36d910-736e-3c73-ab16-b8183b84b37d | -10.5806 | -45.1413 | 2025-04-05 03:00:00 | GOES-16 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 73.4 |
| 0cb03d97-6d20-3c6c-ac6f-c24d34477aac | -20.8512 | -47.7554 | 2025-04-05 03:10:00 | GOES-16 | BATATAIS | SÃO PAULO | Brasil | 3505906 | 35 | 33 | nan | nan | nan | Cerrado | 70.5 |
| e3694bc8-d398-3a03-b277-30c6ab228444 | -20.8306 | -47.7603 | 2025-04-05 03:10:00 | GOES-16 | SALES OLIVEIRA | SÃO PAULO | Brasil | 3544905 | 35 | 33 | nan | nan | nan | Cerrado | 111.5 |
| 2ebe507e-8bcb-36b2-8497-b9d2e081e697 | -8.1078 | -43.1175 | 2025-04-05 03:10:00 | GOES-16 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 67.5 |
| 317dd3e2-946b-3655-b0a3-3a72c61fc90b | -10.5806 | -45.1413 | 2025-04-05 03:10:00 | GOES-16 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 61.8 |
| cba5734d-48ab-3333-9cad-2da8445ddf2d | -20.8512 | -47.7554 | 2025-04-05 03:20:00 | GOES-16 | BATATAIS | SÃO PAULO | Brasil | 3505906 | 35 | 33 | nan | nan | nan | Cerrado | 77.3 |
| a6cd35fa-0b10-3494-823c-2ac5c0859220 | -20.8306 | -47.7603 | 2025-04-05 03:20:00 | GOES-16 | SALES OLIVEIRA | SÃO PAULO | Brasil | 3544905 | 35 | 33 | nan | nan | nan | Cerrado | 98.0 |
| fc3e1308-1105-3fa8-abee-e02f54b273b3 | -20.8512 | -47.7554 | 2025-04-05 03:30:00 | GOES-16 | BATATAIS | SÃO PAULO | Brasil | 3505906 | 35 | 33 | nan | nan | nan | Cerrado | 70.6 |
| 59fd9a1a-e755-376e-aff9-8983b46940b6 | -19.6367 | -48.309 | 2025-04-05 03:30:00 | GOES-16 | VERÍSSIMO | MINAS GERAIS | Brasil | 3171105 | 31 | 33 | nan | nan | nan | Cerrado | 65.9 |
| d6510ac1-c2c9-3b6f-928d-f983c096b648 | -19.6564 | -48.3277 | 2025-04-05 03:30:00 | GOES-16 | VERÍSSIMO | MINAS GERAIS | Brasil | 3171105 | 31 | 33 | nan | nan | nan | Cerrado | 91.5 |
| e7c7664f-e345-3a6f-809d-25eb0e500e4a | -20.8306 | -47.7603 | 2025-04-05 03:30:00 | GOES-16 | SALES OLIVEIRA | SÃO PAULO | Brasil | 3544905 | 35 | 33 | nan | nan | nan | Cerrado | 73.8 |
| 20d9fa19-df2d-38b5-a09f-1622a8be5711 | -19.6361 | -48.3321 | 2025-04-05 03:30:00 | GOES-16 | VERÍSSIMO | MINAS GERAIS | Brasil | 3171105 | 31 | 33 | nan | nan | nan | Cerrado | 109.1 |
| f2e7bdda-38e6-3b9f-8b33-889f74e63071 | -10.5806 | -45.1413 | 2025-04-05 03:30:00 | GOES-16 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 57.6 |
| 4416e275-f744-34c9-aced-c19d26582e85 | -5.03029 | -38.68983 | 2025-04-05 03:34:00 | NOAA-21 | QUIXADÁ | CEARÁ | Brasil | 2311306 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| c40e0b87-c738-3f0a-8846-5f88e5ddbc6d | -5.02969 | -38.69355 | 2025-04-05 03:34:00 | NOAA-21 | QUIXADÁ | CEARÁ | Brasil | 2311306 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 566712aa-b842-3d0f-aa90-f7e5d5640123 | -5.02842 | -38.69028 | 2025-04-05 03:34:00 | NOAA-21 | QUIXADÁ | CEARÁ | Brasil | 2311306 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 8574a2cf-4e7a-30b4-b20b-0c047a5d24a9 | -7.22684 | -35.78983 | 2025-04-05 03:36:00 | NOAA-21 | MASSARANDUBA | PARAÍBA | Brasil | 2509206 | 25 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 496a7ddd-f2a3-37bc-99ce-45574c0a87f8 | -9.33096 | -37.00926 | 2025-04-05 03:36:00 | NOAA-21 | IATI | PERNAMBUCO | Brasil | 2606507 | 26 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 5eedbb62-b798-3a03-9dac-079ba4f9b94f | -8.10903 | -43.12476 | 2025-04-05 03:36:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 9.9 |
| 131c2ba4-53cd-3607-9f9d-8e359b537e28 | -8.10372 | -43.12391 | 2025-04-05 03:36:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 9.9 |
| 45230272-9888-3d2b-a44d-770d73d85656 | -7.58552 | -37.06864 | 2025-04-05 03:36:00 | NOAA-21 | AMPARO | PARAÍBA | Brasil | 2500734 | 25 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 4e5b7830-8313-3e25-9ffe-f38906816acc | -8.11434 | -43.12566 | 2025-04-05 03:36:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| bad0a6a2-c57a-39c9-8a6e-f6c896f5e6b2 | -6.85646 | -35.05477 | 2025-04-05 03:36:00 | NOAA-21 | RIO TINTO | PARAÍBA | Brasil | 2512903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 19.9 |
| c2c969ea-319f-3911-9371-565198dd5e60 | -9.74586 | -37.06794 | 2025-04-05 03:36:00 | NOAA-21 | BATALHA | ALAGOAS | Brasil | 2700706 | 27 | 33 | nan | nan | nan | Caatinga | 3.4 |
| a9c0f685-6058-3725-913c-585faa711987 | -8.45834 | -36.0584 | 2025-04-05 03:36:00 | NOAA-21 | ALTINHO | PERNAMBUCO | Brasil | 2600807 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 042ac29a-da01-3322-89e1-c201c4da8921 | -10.36867 | -36.34373 | 2025-04-05 03:36:00 | NOAA-21 | PIAÇABUÇU | ALAGOAS | Brasil | 2706802 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 68d90225-423c-3274-8cd1-e3a647ae2176 | -9.97921 | -37.91184 | 2025-04-05 03:36:00 | NOAA-21 | PEDRO ALEXANDRE | BAHIA | Brasil | 2924207 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 3463ac0f-3066-3692-9b36-daa18364488f | -4.61247 | -43.15613 | 2025-04-05 03:36:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 472b8f64-06b9-3258-a044-a64f77517b3c | -4.61077 | -43.15297 | 2025-04-05 03:36:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 52f1c797-7a70-3cba-9d29-bcc384777988 | -9.74233 | -37.06736 | 2025-04-05 03:36:00 | NOAA-21 | BATALHA | ALAGOAS | Brasil | 2700706 | 27 | 33 | nan | nan | nan | Caatinga | 1.0 |
| feeb69d5-e3e7-31ed-9564-c0ecfdde7987 | -10.69635 | -37.04956 | 2025-04-05 03:36:00 | NOAA-21 | ROSÁRIO DO CATETE | SERGIPE | Brasil | 2806107 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| dea0d68b-9b3a-368b-ae82-f9d0877183d2 | -8.10844 | -43.12806 | 2025-04-05 03:36:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 9.9 |
| b46669ac-2e78-39f4-ba36-df4e62aa6beb | -6.85982 | -35.0553 | 2025-04-05 03:36:00 | NOAA-21 | RIO TINTO | PARAÍBA | Brasil | 2512903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 19.9 |


[Clique aqui para ver as próximas entradas](README2.md)
