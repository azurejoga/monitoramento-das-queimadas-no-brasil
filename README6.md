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
| 81b94a61-bab4-3e11-979c-fa6307a8c6c7 | -10.19864 | -59.43691 | 2024-12-31 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 31.3 |
| c5ddf1fb-bd56-3308-b4df-85479d4a3397 | -10.70228 | -59.23689 | 2024-12-31 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3ca141a5-7ee0-32c2-aab3-b76513b70aa9 | -9.4646 | -59.20049 | 2024-12-31 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4f3f41b0-bcdc-35cf-8b8d-d28a07d36f3b | -10.70839 | -59.2312 | 2024-12-31 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9dd48c53-ea90-3c32-8826-53cdc23e5516 | -15.37856 | -59.88416 | 2024-12-31 05:01:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 71d601f3-417b-3276-a536-7c24214f9951 | -17.74135 | -56.32375 | 2024-12-31 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 7a651703-9b33-3800-ab5b-07886bf0894d | -19.83431 | -57.47486 | 2024-12-31 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| a2344ded-6889-3a28-8b65-8261122fbfaf | -15.36326 | -59.8859 | 2024-12-31 05:01:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 93d4c910-06c3-3a51-b924-3f509d40216b | -20.5017 | -55.8052 | 2024-12-31 05:01:00 | NOAA-21 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 80a083f1-0ce6-3768-8329-f1cc8b3881e0 | -17.7419 | -56.32012 | 2024-12-31 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 7ea054bf-809c-33b4-898c-1877a82f8449 | -18.30806 | -55.34416 | 2024-12-31 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| d6b68a08-2ef8-375c-9534-33087def335d | -19.12323 | -54.4378 | 2024-12-31 05:01:00 | NOAA-21 | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 03a0a46e-7592-3d0a-893e-1454708147ff | -19.84036 | -57.47966 | 2024-12-31 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 298bae0e-6bec-3035-b1aa-3ebe54e2f6a7 | -15.16303 | -56.4641 | 2024-12-31 05:01:00 | NOAA-21 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| b55c080b-2e07-3bbc-a734-805a6874e4ba | -19.12676 | -54.43838 | 2024-12-31 05:01:00 | NOAA-21 | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ff313622-9732-3a48-b4cf-9ee400c045a5 | -20.50223 | -55.80431 | 2024-12-31 05:01:00 | NOAA-21 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8d0c6f89-e5e3-39b3-8185-d1ae6b9dc230 | -15.36615 | -59.89095 | 2024-12-31 05:01:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 791c23a9-37cb-399f-84c9-1afb661594e2 | -20.29702 | -54.7948 | 2024-12-31 05:01:00 | NOAA-21 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5f38ee73-6bb6-3b3b-a222-79ae1cf8acd1 | -19.34058 | -54.168 | 2024-12-31 05:01:00 | NOAA-21 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5ffddf25-31f1-38c7-8c33-67a1d450eedc | -20.47776 | -53.67603 | 2024-12-31 05:01:00 | NOAA-21 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0aee2722-9043-392f-9768-e9657401ecbf | -15.36979 | -59.8916 | 2024-12-31 05:01:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 60c10287-6348-3ede-9c14-a41e9b94b895 | -15.37781 | -59.88853 | 2024-12-31 05:01:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9b58a137-0f56-37c3-89ce-857d4727bf54 | -17.74799 | -56.32486 | 2024-12-31 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 7fd38dee-daee-3e76-853e-5e9e81646be4 | -15.16522 | -56.47176 | 2024-12-31 05:01:00 | NOAA-21 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 09354c4c-51b1-3025-948e-1cc6ae0ddf9f | -15.37566 | -59.87912 | 2024-12-31 05:01:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2618fbc6-98f1-3458-b0cd-3ed94df3e24d | -18.98513 | -56.38912 | 2024-12-31 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 1f64c7f3-78ef-3ecf-8554-83307297e5cc | -20.00151 | -54.73945 | 2024-12-31 05:01:00 | NOAA-21 | ROCHEDO | MATO GROSSO DO SUL | Brasil | 5007505 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 870e31a1-bac4-3e31-bf05-07537c2cdaba | -19.831 | -57.47429 | 2024-12-31 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| f1e60f89-c41c-3370-b921-0dc89dd856e8 | -15.16578 | -56.4682 | 2024-12-31 05:01:00 | NOAA-21 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f3d44c57-c99a-3bf4-8eec-4e449e9f15e7 | -19.83705 | -57.47909 | 2024-12-31 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.9 |
| c0faabbe-95cb-3450-a934-1b437801635e | -20.00135 | -54.74204 | 2024-12-31 05:01:00 | NOAA-21 | ROCHEDO | MATO GROSSO DO SUL | Brasil | 5007505 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6d81ee3b-7af2-3568-8c6b-469b4e4d4b31 | -15.15917 | -56.46711 | 2024-12-31 05:01:00 | NOAA-21 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2f0cceb3-421d-3c29-b69c-4cb11d54f3bc | -21.19271 | -54.44994 | 2024-12-31 05:01:00 | NOAA-21 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 59652044-2a02-3475-b032-c3de43e748cf | -19.83762 | -57.47543 | 2024-12-31 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 2173ab36-42e7-3380-9381-5fd30b740a50 | -15.15972 | -56.46355 | 2024-12-31 05:01:00 | NOAA-21 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| cba4fbff-5835-3580-b7db-049fc645ace3 | -19.84093 | -57.47601 | 2024-12-31 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 51df28e7-5a3c-3d0d-997c-a6e287e00c51 | -18.78797 | -52.71824 | 2024-12-31 05:01:00 | NOAA-21 | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f86adab8-4622-3ca2-af2a-075a51dcfd7a | -17.74854 | -56.32122 | 2024-12-31 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 904a4d8b-6011-3514-8c98-562a151ab8b1 | -18.31145 | -55.34471 | 2024-12-31 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 491f9d72-3ece-35d4-ba5c-7fbacbeb5911 | -16.166 | -58.32159 | 2024-12-31 05:01:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.5 |
| 84c51e94-5156-3b22-acbb-959e21b2fdb1 | -15.89447 | -57.95986 | 2024-12-31 05:01:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.4 |
| 6db7c661-c999-3a07-9a66-46c53f53a277 | -15.3793 | -59.87977 | 2024-12-31 05:01:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 42ef6aa6-9cbf-358b-a594-cafe7fba00c9 | -15.16247 | -56.46765 | 2024-12-31 05:01:00 | NOAA-21 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d9dd1ab1-8d31-388f-88b7-f8e9102d5f42 | -17.74467 | -56.32431 | 2024-12-31 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 5568dd5c-8e65-3e04-a9f1-305a7d98b594 | -20.50167 | -55.80822 | 2024-12-31 05:01:00 | NOAA-21 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 052b248b-9b1a-3076-9377-a8dfe4df61f2 | -15.4715 | -59.89091 | 2024-12-31 05:01:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 14a1825e-d1dd-3427-85a7-ae3f53408c62 | -19.97003 | -55.34475 | 2024-12-31 05:01:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 848589d6-3d22-302d-8458-57ec87de1274 | -15.37492 | -59.88349 | 2024-12-31 05:01:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7f2fb903-dd45-3199-b143-e91a697cb649 | -15.37343 | -59.89226 | 2024-12-31 05:01:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 93b00fcc-ca0b-30ad-bda6-3e693267570f | -17.74522 | -56.32067 | 2024-12-31 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 3935ea4e-b6f1-3b0d-9ad3-fa585925b68e | -22.11673 | -51.46636 | 2024-12-31 05:03:00 | NOAA-21 | PRESIDENTE PRUDENTE | SÃO PAULO | Brasil | 3541406 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 8e335d8a-55cc-315c-9f64-c87d26ddfc88 | -23.04857 | -49.89516 | 2024-12-31 05:03:00 | NOAA-21 | OURINHOS | SÃO PAULO | Brasil | 3534708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 76b7427d-3a5b-3e4a-b807-01dac8f93c4c | -22.12109 | -51.46695 | 2024-12-31 05:03:00 | NOAA-21 | PRESIDENTE PRUDENTE | SÃO PAULO | Brasil | 3541406 | 35 | 33 | nan | nan | nan | Mata Atlântica | 27.7 |
| 5c8d8d35-a9b3-365d-90ce-cdf9aef334cc | -22.1216 | -51.46255 | 2024-12-31 05:03:00 | NOAA-21 | PRESIDENTE PRUDENTE | SÃO PAULO | Brasil | 3541406 | 35 | 33 | nan | nan | nan | Mata Atlântica | 27.7 |
| 4b26dee3-c005-3a4f-a61d-2249cc0827f2 | -22.07047 | -55.49216 | 2024-12-31 05:03:00 | NOAA-21 | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2a70a98b-2fd9-35e1-93ed-9800486c2302 | -22.54647 | -48.37777 | 2024-12-31 05:03:00 | NOAA-21 | MINEIROS DO TIETÊ | SÃO PAULO | Brasil | 3529807 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b33acc44-c65b-333b-8682-39b01f246001 | -30.50508 | -54.00736 | 2024-12-31 05:05:00 | NOAA-21 | SANTA MARGARIDA DO SUL | RIO GRANDE DO SUL | Brasil | 4316972 | 43 | 33 | nan | nan | nan | Pampa | 1.5 |
| c709d78e-4245-3054-92d9-ef8e44c4b6ee | -30.50554 | -54.00308 | 2024-12-31 05:05:00 | NOAA-21 | SANTA MARGARIDA DO SUL | RIO GRANDE DO SUL | Brasil | 4316972 | 43 | 33 | nan | nan | nan | Pampa | 1.5 |
| 268173d8-3c18-32b3-9f99-a4d0f9312913 | 4.32679 | -60.45307 | 2024-12-31 05:20:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9075c9d9-7ad7-3435-8cf2-6dcc2e1d4b3c | 3.47421 | -60.46458 | 2024-12-31 05:20:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1a8df191-f117-352f-bfcb-29fd9328b200 | 3.18421 | -60.37132 | 2024-12-31 05:20:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 88cd2774-0334-388c-beb2-c17d8aa527eb | 3.62623 | -60.40754 | 2024-12-31 05:20:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9a57626c-cc8e-3b1b-87f0-7b42f43c7d32 | 3.18706 | -60.3671 | 2024-12-31 05:20:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 83b2691f-59e2-381f-b69c-64fc1f4a621c | 3.47306 | -60.4571 | 2024-12-31 05:20:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c2a1eb78-f319-34c2-993c-338ce619eb70 | 4.15699 | -60.7097 | 2024-12-31 05:20:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a0faf186-ad47-3191-a418-0f66dbc7547a | 3.47363 | -60.46083 | 2024-12-31 05:20:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 23cbf819-fe6e-3d26-85de-ec828ae3e344 | 3.5693 | -60.22289 | 2024-12-31 05:20:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3e4a5639-4317-3bd4-8f37-33176bfbe9a9 | -10.19988 | -59.43948 | 2024-12-31 05:22:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 30704387-b110-3af6-9e2b-50a33a91745f | -1.6522 | -45.85857 | 2024-12-31 05:22:00 | NPP-375D | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cc7acaa8-28c9-3047-8210-b34b2475eb21 | -2.28843 | -53.67474 | 2024-12-31 05:22:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f7680c5f-d6f7-3be3-826e-0df5a5d68ade | -10.70553 | -59.23541 | 2024-12-31 05:22:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 88cc3a96-f076-3a37-9677-ecf5215c639f | -1.64504 | -45.85739 | 2024-12-31 05:22:00 | NPP-375D | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e9d0207b-5bb1-3ff9-bd04-73821c8e9b6c | -9.4742 | -66.0397 | 2024-12-31 05:22:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d6f538cd-6963-3836-8c33-beadef42d28a | -10.70181 | -59.23606 | 2024-12-31 05:22:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f4d3f19b-63cb-371f-bb34-a4566729e259 | 3.20065 | -60.54388 | 2024-12-31 05:22:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 48d8ddc9-58a5-335c-9df8-b0b3386421dc | -10.70943 | -59.23318 | 2024-12-31 05:22:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 76ffae4e-472c-3f15-abd5-57165c6e2f5b | -1.25166 | -46.60338 | 2024-12-31 05:22:00 | NPP-375D | AUGUSTO CORRÊA | PARÁ | Brasil | 1500909 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5242baf2-1f87-3e53-b7c9-3a36d29a696a | -10.19699 | -59.43517 | 2024-12-31 05:22:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7efe3aae-3b47-32b1-847b-0643e54fa57f | -10.70961 | -59.23202 | 2024-12-31 05:22:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 944224b9-18e5-3517-80aa-f6c5d8ce4800 | -1.64863 | -45.86263 | 2024-12-31 05:22:00 | NPP-375D | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ee01824d-6ac6-3257-8a2a-ec1b72eaed98 | 3.20006 | -60.54013 | 2024-12-31 05:22:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 92bf3d53-2b2d-3954-8a79-2a9dbb0f681d | -1.65115 | -45.86558 | 2024-12-31 05:22:00 | NPP-375D | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 18700332-8333-3879-90d0-2111932f5d15 | -1.65578 | -45.86383 | 2024-12-31 05:22:00 | NPP-375D | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 99cabc8e-1869-3528-9c75-434bef70edf5 | -10.19641 | -59.43897 | 2024-12-31 05:22:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a018548f-7d89-3759-8232-4ad8fce1e4b0 | -10.20045 | -59.43567 | 2024-12-31 05:22:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dc2dd069-1ab7-3759-9eab-3612834a9066 | -10.70611 | -59.23146 | 2024-12-31 05:22:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a1fa3012-3ee2-3b98-9ffd-c4b4c6a06180 | -10.70592 | -59.23262 | 2024-12-31 05:22:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4d5ce8b1-2aeb-34ed-9693-5c08d46f45dd | -15.37631 | -59.88585 | 2024-12-31 05:25:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 41699ad5-a386-38cc-96ea-2c1f947521a8 | -15.3769 | -59.88169 | 2024-12-31 05:25:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 84e295b2-544d-3ebe-a3cb-b7175f129ae4 | -12.24946 | -63.46362 | 2024-12-31 05:25:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| eef142fc-e07b-3d91-b540-54b888230cfa | -15.38047 | -59.88224 | 2024-12-31 05:25:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c43046ee-8d29-3862-a190-84a969210aaa | -15.1652 | -56.46495 | 2024-12-31 05:25:00 | NPP-375D | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 42d1fd17-be6a-3bdb-b16e-6e4820febfa9 | -15.36143 | -59.8878 | 2024-12-31 05:25:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6e0563ee-35d7-3875-b998-b3812c4fd669 | -15.16085 | -56.46431 | 2024-12-31 05:25:00 | NPP-375D | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8af0ddfb-ea35-3485-8722-f1e3a2096f5a | -12.24608 | -63.46304 | 2024-12-31 05:25:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a69ed04f-7d9a-3c9f-98ae-37ffe393fbee | -17.74464 | -56.31898 | 2024-12-31 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| e09daa25-4893-3b92-95c4-09becc1b65f6 | -15.365 | -59.88836 | 2024-12-31 05:25:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 11a4ac16-221f-30bf-b966-28c690864b8a | -15.37571 | -59.89 | 2024-12-31 05:25:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 364cb1a9-e122-3a6b-a6ee-8a2698c7d7e5 | -15.47271 | -59.89064 | 2024-12-31 05:25:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| cb41cfbc-1d9d-39b3-9509-ae8467ff1c23 | -15.37214 | -59.88945 | 2024-12-31 05:25:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |


[Clique aqui para ver as próximas entradas](README7.md)
