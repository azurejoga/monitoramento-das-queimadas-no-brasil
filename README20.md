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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ef1aae24-648c-388b-9a89-f38a29d69067 | -22.78503 | -45.07763 | 2025-08-21 03:53:00 | NOAA-21 | LORENA | SÃO PAULO | Brasil | 3527207 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 9e228ab6-a37e-3367-aeb4-bd524321b423 | -22.70811 | -42.64678 | 2025-08-21 03:53:00 | NOAA-21 | RIO BONITO | RIO DE JANEIRO | Brasil | 3304300 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| b7efb512-1423-3fef-810e-d56836353373 | -22.78968 | -45.0735 | 2025-08-21 03:53:00 | NOAA-21 | LORENA | SÃO PAULO | Brasil | 3527207 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 6272998b-9e3d-32f4-a412-e85697256e32 | -23.23246 | -47.5287 | 2025-08-21 03:53:00 | NOAA-21 | PORTO FELIZ | SÃO PAULO | Brasil | 3540606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 56a27559-3492-35ec-8a81-2cd56739302c | -23.31159 | -46.89983 | 2025-08-21 03:53:00 | NOAA-21 | CAJAMAR | SÃO PAULO | Brasil | 3509205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 04e4fa6b-351d-3ee6-882d-e07f8f89e78c | -29.88606 | -50.58492 | 2025-08-21 03:55:00 | NOAA-21 | SANTO ANTÔNIO DA PATRULHA | RIO GRANDE DO SUL | Brasil | 4317608 | 43 | 33 | nan | nan | nan | Pampa | 1.4 |
| 8dd90379-909a-378d-8401-894d2f1169a4 | -28.63159 | -49.27196 | 2025-08-21 03:55:00 | NOAA-21 | MORRO DA FUMAÇA | SANTA CATARINA | Brasil | 4211207 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| cfabd1ad-6b52-3fb2-a846-fe5d74d4880f | -7.0354 | -44.6167 | 2025-08-21 04:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 221.6 |
| 79c57378-e0c0-34ad-bc55-9da76e2cd59c | -8.8736 | -62.4115 | 2025-08-21 04:00:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 64.4 |
| a1b70cfb-270f-3b55-a3cd-091c1c01c07d | -7.0164 | -44.6413 | 2025-08-21 04:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 140.5 |
| 0e49bde1-bf24-3e90-8b33-01c4d0509313 | -8.8737 | -62.3925 | 2025-08-21 04:00:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 79.2 |
| 0c383cb3-0ed2-32f4-921d-155b602c5c2f | -7.0352 | -44.6396 | 2025-08-21 04:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 83.4 |
| 04ed1324-5a87-3a97-a057-805f3f4023ff | -7.0166 | -44.6184 | 2025-08-21 04:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 404.3 |
| 16915cf2-a73a-38d3-ab5a-0691876d9201 | -7.0169 | -44.5954 | 2025-08-21 04:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 60.1 |
| e0ae5127-c425-3c81-8822-0f4f9ffa11b0 | -7.0354 | -44.6167 | 2025-08-21 04:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 261.3 |
| 6a288f22-c94a-350a-a631-1bd03873ec7d | -7.0169 | -44.5954 | 2025-08-21 04:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 60.6 |
| f443dc7f-82e1-3659-a968-442aa1ef3c97 | -13.0317 | -45.1724 | 2025-08-21 04:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 261.5 |
| 961f8dcd-00ea-3f2f-985f-60529330d8ac | -7.0166 | -44.6184 | 2025-08-21 04:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 370.5 |
| a08e3302-1c92-369f-8032-666d131a6a8b | -13.0128 | -45.1523 | 2025-08-21 04:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 133.5 |
| 78ad22be-3846-3de7-96fd-5a66e1d987e5 | -13.0123 | -45.1756 | 2025-08-21 04:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 221.9 |
| 80090785-c987-3574-92ac-5fab8f0964b5 | -8.8737 | -62.3925 | 2025-08-21 04:10:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 114.9 |
| 0401664f-57ee-33b8-810d-5b455cba3734 | -13.051 | -45.1693 | 2025-08-21 04:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 91.0 |
| c7761434-1e40-3eb2-b28d-fae16fe27fcd | -8.8736 | -62.4115 | 2025-08-21 04:10:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 96.9 |
| 572e8a2e-2266-3336-95b4-b7f1c2e8be85 | -8.8552 | -62.3933 | 2025-08-21 04:10:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 42.9 |
| b1981f75-f230-3596-a7b7-37ac8fd6b9d5 | -13.0312 | -45.1957 | 2025-08-21 04:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 89.8 |
| 325b3136-fe03-35c2-b40b-1f0994f20aaa | -7.0352 | -44.6396 | 2025-08-21 04:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 92.7 |
| 444ec195-d874-3336-a59b-a3df5ce6065c | -8.8735 | -62.4305 | 2025-08-21 04:10:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 43.6 |
| 986e3af3-5e11-3140-989a-53f7faefb037 | -7.0164 | -44.6413 | 2025-08-21 04:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 122.9 |
| f6ca1169-0425-3e45-be11-b9badc840e8e | -13.0321 | -45.1492 | 2025-08-21 04:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 176.6 |
| 37a36e1a-17bb-3c04-9b7e-19ca541b234c | -4.99547 | -44.87757 | 2025-08-21 04:14:00 | NPP-375D | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f83db159-a034-3ca2-aa22-f8bde84095f7 | -2.82321 | -47.72382 | 2025-08-21 04:14:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6269c8c8-ef4e-389a-a3de-c0cc410fe91e | -5.99572 | -39.30876 | 2025-08-21 04:14:00 | NPP-375D | DEPUTADO IRAPUAN PINHEIRO | CEARÁ | Brasil | 2304269 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| f41e5c0e-98a7-334a-a8b7-52ea742b9646 | -2.73001 | -47.44219 | 2025-08-21 04:14:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b0269d6d-99c8-310a-a57d-a94837568e3b | -2.44574 | -47.32591 | 2025-08-21 04:14:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 414d714d-7e1f-32a6-a55e-72aba23eee5b | -2.54372 | -47.71558 | 2025-08-21 04:14:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e88a0108-b1ac-357f-9758-e4dc54358cb1 | -3.83778 | -47.41632 | 2025-08-21 04:14:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fbf9adb8-85ed-36af-b86a-c5f5d00b806e | -3.87909 | -50.97671 | 2025-08-21 04:14:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 393aadb7-af19-3a8c-9200-1f84b894bd65 | -4.16914 | -48.57648 | 2025-08-21 04:14:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9a70ea57-f86f-3008-b159-854c973b1aee | -4.86487 | -42.53924 | 2025-08-21 04:14:00 | NPP-375D | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| d5df6d2c-9e39-37bc-acbf-0721e52c4610 | -5.37935 | -42.34697 | 2025-08-21 04:14:00 | NPP-375D | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| ab1929b3-c5cc-3879-964b-2caed26202f5 | -4.87097 | -42.54374 | 2025-08-21 04:14:00 | NPP-375D | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 696b1bfa-c26a-392c-8159-d866028517e8 | -3.94492 | -41.83092 | 2025-08-21 04:14:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| c225bd1f-c668-39b6-8d17-09dfeb093ff0 | -3.99015 | -42.50756 | 2025-08-21 04:14:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 5424d8ee-8a8b-34e8-8e35-bb1cf60042d0 | -5.10601 | -43.15601 | 2025-08-21 04:14:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f49b82a5-b058-37d5-a270-0f84818b46f8 | -3.81714 | -41.56506 | 2025-08-21 04:14:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 2dcfebf9-46cd-3625-9767-a9c503eb42f9 | -4.29087 | -48.2768 | 2025-08-21 04:14:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 403a4185-8feb-3058-a153-439634da6167 | -3.87389 | -40.45643 | 2025-08-21 04:14:00 | NPP-375D | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 0187ac28-0c84-39ae-a9f8-f799352a6666 | -5.38267 | -42.34749 | 2025-08-21 04:14:00 | NPP-375D | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 8829019c-c94f-39fb-96c3-ebcd1295e4c6 | -3.81878 | -41.55457 | 2025-08-21 04:14:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| b25fe59d-a195-3524-85bd-6d1e2e7de69d | -4.86433 | -42.54269 | 2025-08-21 04:14:00 | NPP-375D | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| acbdc05a-22c8-3f67-8495-c2273b7cfff4 | -5.10824 | -43.16347 | 2025-08-21 04:14:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bb8eb449-097f-31cd-a970-6f3bcf96d790 | -2.55339 | -47.70926 | 2025-08-21 04:14:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 2c908b93-a1e4-35ab-8b64-fec6065b0fb1 | -3.98182 | -43.24326 | 2025-08-21 04:14:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f8262ae3-7ce5-3457-93ef-b3318429bff3 | -4.31406 | -48.08361 | 2025-08-21 04:14:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| a4a9722b-e9d6-3b7a-8187-0dc367a75508 | -2.25577 | -47.84941 | 2025-08-21 04:14:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d82ea489-9f71-3bc4-bdf5-80ea88e59f59 | -2.38806 | -47.66471 | 2025-08-21 04:14:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7674b952-6102-3d54-9783-8166c16eaa73 | -5.41323 | -42.36652 | 2025-08-21 04:14:00 | NPP-375D | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 50a00218-c94d-3900-8f51-703da7c1b628 | -2.38886 | -47.6601 | 2025-08-21 04:14:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 11122987-f197-39e8-9a17-611772d29009 | -3.81933 | -41.55107 | 2025-08-21 04:14:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 6cecc053-8fcf-3042-8252-0db96efd2919 | -3.52702 | -41.09148 | 2025-08-21 04:14:00 | NPP-375D | VIÇOSA DO CEARÁ | CEARÁ | Brasil | 2314102 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 9e1f8e38-0ef7-3ec0-8028-272c0f31df71 | -2.38866 | -47.66086 | 2025-08-21 04:14:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6d8dac0d-1cf0-3d7e-b2ba-a09c2a94fb44 | -4.78066 | -44.91899 | 2025-08-21 04:14:00 | NPP-375D | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ce3e7e36-8b04-3681-a4c5-577c0daa4863 | -5.24349 | -42.71232 | 2025-08-21 04:14:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 94f6c47d-1fc3-345e-b85a-c3a9a06e8827 | -2.25813 | -47.84911 | 2025-08-21 04:14:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| cf221c68-a56a-3b1a-904d-5992e21d9eaf | -2.53888 | -47.71869 | 2025-08-21 04:14:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e54cceee-23a5-3716-bfe9-a0d266dc20bb | -2.44424 | -47.32528 | 2025-08-21 04:14:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9cb7754b-7637-3681-8688-7f368c7f0655 | -2.62308 | -46.84571 | 2025-08-21 04:14:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 85928c72-0885-3e6a-b8fb-3ae6e47d22a7 | -3.98351 | -42.50652 | 2025-08-21 04:14:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 0852bd51-9e9a-3641-b8cd-064645aaafe2 | -4.71326 | -47.21851 | 2025-08-21 04:14:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 6.3 |
| dfb97233-a4ff-3f49-985b-d448234bcdb2 | -3.83123 | -47.73545 | 2025-08-21 04:14:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3ddcc1d6-9426-3018-985e-165de947cabe | -4.13032 | -48.01906 | 2025-08-21 04:14:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8b702dc8-d0d6-3a1f-87e7-382e5917b0db | -3.98573 | -42.51395 | 2025-08-21 04:14:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| ed316177-d863-3c4b-a920-9815f6f7f761 | -2.44836 | -47.32593 | 2025-08-21 04:14:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 335f63c0-e413-36b1-82ff-19aa3c69a9b5 | -4.01616 | -49.50336 | 2025-08-21 04:14:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4f6b440d-5ad2-3f1e-8de6-62cd4e6e93bc | -5.40991 | -42.366 | 2025-08-21 04:14:00 | NPP-375D | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 8ad6a71d-2c27-35a2-84a4-4399ae0284b2 | -4.86765 | -42.54322 | 2025-08-21 04:14:00 | NPP-375D | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 3d31a617-cbf1-31a6-9481-d4df0ef871d5 | -2.69743 | -48.20803 | 2025-08-21 04:14:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4232ec2a-40d2-3bb2-ae4e-39702c4b84a6 | -4.02081 | -49.50413 | 2025-08-21 04:14:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0485d78a-c718-3626-b4fe-29f61f4d93ec | -3.48273 | -47.67945 | 2025-08-21 04:14:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c730ec9b-a133-3998-9179-96da52cc01d1 | -3.24272 | -39.52503 | 2025-08-21 04:14:00 | NPP-375D | ITAPIPOCA | CEARÁ | Brasil | 2306405 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 585f22c6-b5fd-3512-ba98-c07913472861 | -4.91403 | -45.32029 | 2025-08-21 04:14:00 | NPP-375D | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 21487dc5-80ff-3a7a-afbd-02c662419bc2 | -4.86799 | -41.57685 | 2025-08-21 04:14:00 | NPP-375D | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 579bf21e-86f2-3008-bc75-b3c88a76e0d3 | -5.12923 | -43.09557 | 2025-08-21 04:14:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b4f80d5f-d943-32bf-a79c-bb67dd119b3a | -3.04033 | -49.44553 | 2025-08-21 04:14:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 14b8a901-a764-3ff2-ada2-73d721fe31eb | -2.90595 | -48.25165 | 2025-08-21 04:14:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5c561da1-db62-3602-97bd-1adc47d80a0a | -3.65287 | -48.32752 | 2025-08-21 04:14:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4a8d42c4-32be-34f5-9f2c-e5a2733d1937 | -5.25824 | -44.47655 | 2025-08-21 04:14:00 | NPP-375D | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8cfa03e3-740e-3ffe-b41e-4d8c67be25e9 | -5.40604 | -42.36894 | 2025-08-21 04:14:00 | NPP-375D | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 96fdf72a-8860-3521-8aec-98fadd0fcb4f | -4.01774 | -49.50639 | 2025-08-21 04:14:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 680de71a-b4e1-36d7-9f6f-dc341e476c07 | -5.10546 | -43.15948 | 2025-08-21 04:14:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e59edcdb-0473-34ac-ab08-a481641f0062 | -4.64699 | -41.40872 | 2025-08-21 04:14:00 | NPP-375D | MILTON BRANDÃO | PIAUÍ | Brasil | 2206357 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 508b51a3-c2b8-3ff4-bcd4-140af7aeaee1 | -5.39048 | -41.23298 | 2025-08-21 04:14:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| cf836ea8-9331-34db-9990-b89ac4d1f92b | -4.72582 | -38.39772 | 2025-08-21 04:14:00 | NPP-375D | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 14f9ed3d-f153-3c15-ada5-f80caf100d44 | -4.77692 | -45.32015 | 2025-08-21 04:14:00 | NPP-375D | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7aedbd38-7271-385b-a222-be22048eda40 | -2.38401 | -47.66323 | 2025-08-21 04:14:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2900d34d-98f8-3bee-b1b4-d4139a30deb8 | -3.03806 | -49.42979 | 2025-08-21 04:14:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 900d552d-b7bb-31bf-bd52-f30ed5399933 | -5.24301 | -37.69653 | 2025-08-21 04:14:00 | NPP-375D | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 0.5 |
| b8971fd6-9a9b-3d28-971b-8dc5f8dd0322 | -5.40936 | -42.36946 | 2025-08-21 04:14:00 | NPP-375D | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 44209f04-2989-3127-920e-e12d2b3f91fb | -3.99347 | -42.50808 | 2025-08-21 04:14:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| de272aeb-5e6a-3cca-b954-c708f9fb888b | -3.73768 | -48.93128 | 2025-08-21 04:14:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README21.md)
