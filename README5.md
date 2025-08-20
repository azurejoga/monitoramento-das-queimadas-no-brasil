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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9c2e0ef7-c354-3ddb-9adc-948c7da24c76 | -12.955 | -46.1504 | 2025-08-20 00:50:00 | GOES-19 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 53.3 |
| 78e52d64-496b-3059-a8ff-a893bb10fef9 | -13.1367 | -54.9171 | 2025-08-20 00:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 48.9 |
| 07c65695-a041-3ecf-85ad-8dbbe162cb96 | -8.034 | -47.6639 | 2025-08-20 01:00:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 82.6 |
| fbfaba6f-156e-38e3-8c83-b611d83e56ec | -15.0002 | -54.8135 | 2025-08-20 01:00:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 46.7 |
| 2499e447-50a2-3b35-8db5-f9ffce368c36 | -11.7508 | -48.1825 | 2025-08-20 01:00:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 71.9 |
| bd2a6a3f-1bce-3610-834d-48eea516ed99 | -20.339 | -51.7062 | 2025-08-20 01:00:00 | GOES-19 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 136.2 |
| 2bc812e5-5d81-38e7-a261-5c98341c7a75 | -13.1555 | -54.9357 | 2025-08-20 01:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 114.1 |
| 85a76dd7-db4f-3723-b7c5-9998eb7ef094 | -7.6481 | -45.2673 | 2025-08-20 01:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 112.5 |
| e959a02a-fa1b-35fd-ab15-9c7e7c6d92ac | -13.1367 | -54.9171 | 2025-08-20 01:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 62.0 |
| c310df7a-bfc7-3695-b6d6-3ce1f8bbaf2b | -13.3346 | -54.4233 | 2025-08-20 01:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 41.3 |
| 4e16cbb3-c799-3daf-9bd6-1e7e4e5f3338 | -13.1364 | -54.9376 | 2025-08-20 01:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 82.1 |
| c82ed5b3-db11-3648-a2d3-2a4ee455da83 | -4.4331 | -47.76 | 2025-08-20 01:00:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 51.0 |
| 0e2f14d5-25b2-3d8b-987b-7cae36a0cb64 | -13.1558 | -54.9151 | 2025-08-20 01:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 89.6 |
| 62cf3daa-486a-3157-bba7-cff50c720b51 | -20.3385 | -51.7284 | 2025-08-20 01:00:00 | GOES-19 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 74.1 |
| e91283a7-1ee9-381b-b06c-142c2a9cc77b | -7.6293 | -45.2691 | 2025-08-20 01:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 85.5 |
| 3b9c7d46-43da-39a3-be07-0e3ae3729786 | -4.912 | -43.2337 | 2025-08-20 01:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 94.7 |
| 1551efe0-4b86-39b9-ad56-95edd644a3aa | -8.8736 | -62.4115 | 2025-08-20 01:00:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 52.9 |
| f79b1868-a14d-36c5-96c6-d30f6651fa37 | -12.9778 | -56.8614 | 2025-08-20 01:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 55.6 |
| f6032284-57b6-3110-ad60-bbc6a346b027 | -13.3318 | -54.419201 | 2025-08-20 01:06:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 63efae30-a038-3f9d-8549-5ec5dfc63f88 | -20.327999 | -51.697498 | 2025-08-20 01:06:00 | METOP-B | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 0e346696-ba69-39ab-88aa-71339f354f75 | -12.9783 | -56.875999 | 2025-08-20 01:06:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 38269d99-271d-3687-83bb-f2533db61e87 | -7.0267 | -59.669899 | 2025-08-20 01:06:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6574f550-21be-3399-82cc-88778b09f467 | -9.8975 | -60.276901 | 2025-08-20 01:06:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 75e6c127-bd93-3eda-a93b-1a92b8b930b6 | -10.9174 | -57.5051 | 2025-08-20 01:06:00 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 59500ae9-7c74-348d-a602-c25c18020899 | -9.5231 | -60.535099 | 2025-08-20 01:06:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2d3f62d3-6c1c-3d37-8cea-33701fa65bee | -14.9934 | -54.822102 | 2025-08-20 01:06:00 | METOP-B | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e63c7b10-7ae6-3126-bbf2-042ad4a8cfdd | -9.2281 | -60.325001 | 2025-08-20 01:06:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 994b613e-2435-364a-8c78-4d09642aae63 | -10.9195 | -57.514099 | 2025-08-20 01:06:00 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 97b58f68-c6e1-381d-bc1b-ea19be5130cb | -16.779499 | -49.665001 | 2025-08-20 01:06:00 | METOP-B | CAMPESTRE DE GOIÁS | GOIÁS | Brasil | 5204607 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| f40f8324-a41a-36d7-8d78-4f259f4d83d1 | -7.9648 | -55.296299 | 2025-08-20 01:06:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a47fe6f9-b3c0-36eb-8ac4-3b8459c1141f | -11.6796 | -60.180901 | 2025-08-20 01:06:00 | METOP-B | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 3f957c8a-ed10-3255-b9c0-dfe8e0061dc1 | -6.1503 | -57.7141 | 2025-08-20 01:06:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f5477083-0a69-393c-9d70-059ee45e5712 | -8.8907 | -62.401402 | 2025-08-20 01:06:00 | METOP-B | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 0aea67f2-086a-39f3-9f02-3fcd1033a41c | -9.2166 | -59.6875 | 2025-08-20 01:06:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ca977370-305e-3d45-ad0a-1c9797d79660 | -13.1602 | -54.937302 | 2025-08-20 01:06:00 | METOP-B | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c8ab3f87-5099-3948-ba0d-b490b3d5eef7 | -13.3286 | -54.406399 | 2025-08-20 01:06:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 72d93828-d508-35bc-9566-afd7d9d67b0a | -5.4514 | -60.1273 | 2025-08-20 01:06:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| aa5d680c-dfbf-3d6f-9069-19ad004a1909 | -7.0249 | -59.662102 | 2025-08-20 01:06:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0268ef16-c1d8-3ede-b859-10ab6de6e264 | -10.2462 | -64.474297 | 2025-08-20 01:06:00 | METOP-B | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 20985dd9-da9e-3ed1-8729-dfc3d41a5d11 | -8.4414 | -63.864399 | 2025-08-20 01:06:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 79be4dd6-403f-36f8-8f48-2b3e7f8964f5 | -20.5285 | -57.398499 | 2025-08-20 01:06:00 | METOP-B | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 246acfba-5272-30ab-88fe-8971b421a590 | -11.612 | -65.074402 | 2025-08-20 01:06:00 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 1e6250e7-8f3e-355b-b3da-f75d8d82ca0f | -8.8778 | -62.389702 | 2025-08-20 01:06:00 | METOP-B | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| ee0955f4-9d04-37d8-a80b-cc08e47852a0 | -6.1406 | -57.7164 | 2025-08-20 01:06:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1a2170ee-59a0-3091-8074-392cb836966a | -9.2068 | -60.822601 | 2025-08-20 01:06:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 35f740aa-f1ae-387f-99ee-62bc66053b12 | -13.1505 | -54.9398 | 2025-08-20 01:06:00 | METOP-B | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f7f52082-2e09-3880-a203-2b684cb39091 | -11.5619 | -50.462502 | 2025-08-20 01:06:00 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 60a6b617-85be-3460-9f4b-0f8af714dbe0 | -8.8793 | -62.396599 | 2025-08-20 01:06:00 | METOP-B | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| f2e9825b-c8b9-3202-bf14-4c090991b16a | -10.4548 | -64.395103 | 2025-08-20 01:06:00 | METOP-B | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 0d187484-1a36-3202-912d-ed6360a96295 | -9.5215 | -60.528 | 2025-08-20 01:06:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 628879ea-dbe5-39d3-bb84-e66e5e200ebe | -10.256 | -64.472198 | 2025-08-20 01:06:00 | METOP-B | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| faf388db-ccce-37d9-9cad-1286cd83ac49 | -13.3448 | -54.3885 | 2025-08-20 01:06:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 68772c32-7e6b-3d89-b8a1-27b8fd5d0aae | -20.3454 | -51.7243 | 2025-08-20 01:06:00 | METOP-B | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 305b0ed9-57dc-3c85-aaea-4417dc0a9a8a | -12.9717 | -56.848301 | 2025-08-20 01:06:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5e8da951-7707-37f3-8a7b-a74cc58dde17 | -13.348 | -54.401402 | 2025-08-20 01:06:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 55937e0e-3333-368f-a17a-f86d23ceab4b | -10.445 | -64.397202 | 2025-08-20 01:06:00 | METOP-B | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 6d481dc6-2eac-3992-b917-ba684fe79c8f | -8.4398 | -63.856899 | 2025-08-20 01:06:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 65975f9a-65cd-3799-8f46-3754171b7879 | -10.9152 | -57.495998 | 2025-08-20 01:06:00 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1955bf20-c7dd-3282-903e-dbfec6fc1c47 | -11.6698 | -60.183102 | 2025-08-20 01:06:00 | METOP-B | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 35a72f1e-6aba-3f06-a503-af544f8a73a0 | -12.9881 | -56.8736 | 2025-08-20 01:06:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a529cc72-d421-34d5-a35e-9cb4df2d63a0 | -13.0347 | -56.852299 | 2025-08-20 01:06:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8628da8e-2c3c-3c5e-b5e2-8f4205c0c690 | -13.1371 | -57.153301 | 2025-08-20 01:06:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 664cd498-b8bd-3bfb-81a6-d4e62e924f9e | -12.9837 | -56.855202 | 2025-08-20 01:06:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0f507d61-3d05-355c-8b5b-0995aafddd22 | -13.335 | -54.431999 | 2025-08-20 01:06:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3c9b2173-b633-3a36-99fc-492bd5066165 | -13.1543 | -54.913399 | 2025-08-20 01:06:00 | METOP-B | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 75613e74-74ce-3522-889e-00cad9134094 | -20.3319 | -51.712299 | 2025-08-20 01:06:00 | METOP-B | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| d8ed7912-234e-35d4-9c62-538b3f6f65f6 | -8.8824 | -62.4105 | 2025-08-20 01:06:00 | METOP-B | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 851407a2-57d1-389a-a66e-cc4ee00f4e29 | -9.2314 | -60.339401 | 2025-08-20 01:06:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3eb3001c-4ee6-3135-8b2d-d73f1e81c5a6 | -12.9859 | -56.864399 | 2025-08-20 01:06:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 398f60d1-9dba-3eef-a1ca-8621698d19e0 | -16.7859 | -49.688 | 2025-08-20 01:06:00 | METOP-B | CAMPESTRE DE GOIÁS | GOIÁS | Brasil | 5204607 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 5760c9e2-3567-35cf-bde7-34e2c245e15b | -20.4468 | -53.704399 | 2025-08-20 01:06:00 | METOP-B | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 6ba63789-932a-3928-b91c-2439a0748721 | -9.2183 | -59.695 | 2025-08-20 01:06:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f5a7b5ab-6166-3d42-bb9b-1cc27edf4c75 | -8.9683 | -60.497398 | 2025-08-20 01:06:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 59b534f2-53c4-349c-a71b-a801a6ea96f4 | -20.341499 | -51.709499 | 2025-08-20 01:06:00 | METOP-B | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| fb35382f-0ec0-3807-81a4-dd361429805b | -12.9804 | -56.8853 | 2025-08-20 01:06:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3196291b-3f03-3954-92c9-7b4526832594 | -13.3383 | -54.4039 | 2025-08-20 01:06:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e75b2162-0805-38e2-a031-aed01a41528e | -15.8692 | -50.6618 | 2025-08-20 01:06:00 | METOP-B | ITAPIRAPUÃ | GOIÁS | Brasil | 5211008 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 68b8ccf6-4c24-3c56-9ff2-092d0ed57b95 | -20.533001 | -57.373001 | 2025-08-20 01:06:00 | METOP-B | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 836c2382-44e2-3b28-8d43-205a37a8424c | -15.0004 | -54.808102 | 2025-08-20 01:06:00 | METOP-B | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 6cd3a497-ced5-3b3b-9222-23fb4fedc265 | -6.1382 | -57.706402 | 2025-08-20 01:06:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8d9ea682-e342-390a-9c56-44b95441f886 | -12.9739 | -56.857601 | 2025-08-20 01:06:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 057c6a44-3606-3444-a4be-fa43ee1565f4 | -6.1526 | -57.724201 | 2025-08-20 01:06:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 902a585b-b7d7-39a6-a2a4-6493a8e79396 | -10.4565 | -64.403297 | 2025-08-20 01:06:00 | METOP-B | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 0110dc4f-8cd6-3379-8705-65a2c5538459 | -14.9906 | -54.810699 | 2025-08-20 01:06:00 | METOP-B | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 482b5793-f703-33b9-b517-38d645dd8b7d | -8.8891 | -62.394402 | 2025-08-20 01:06:00 | METOP-B | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 0d6fa28b-143c-31db-84fd-9ce77bc3215a | -10.4467 | -64.405403 | 2025-08-20 01:06:00 | METOP-B | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 1d89b450-515d-3ad4-8c85-1804f8657ed8 | -6.9383 | -62.878601 | 2025-08-20 01:06:00 | METOP-B | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ca2afd6e-adfc-31be-b87a-74dafa3a5a4d | -20.337601 | -51.694698 | 2025-08-20 01:06:00 | METOP-B | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 2501022c-adf3-3d75-ba07-321b43b80c22 | -11.6682 | -60.175999 | 2025-08-20 01:06:00 | METOP-B | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 867edd1a-b2bc-3c00-ba50-ab7b628ecd0a | -8.6284 | -62.147301 | 2025-08-20 01:06:00 | METOP-B | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3f0be902-6da3-31ec-b97f-40e467a6da4c | -13.1475 | -54.927898 | 2025-08-20 01:06:00 | METOP-B | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| bdb8b0bc-fbb0-35ba-836e-2186951e50b8 | -13.1572 | -54.9254 | 2025-08-20 01:06:00 | METOP-B | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8584d59f-79a5-3ffa-bd22-d7b050cf4cda | -9.8991 | -60.2841 | 2025-08-20 01:06:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 51e8a7db-a007-3afa-ac37-0af1abc2d4cf | -20.4496 | -53.715599 | 2025-08-20 01:06:00 | METOP-B | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| fd88a648-68c6-3014-ac5a-724eed59f2a0 | -15.0032 | -54.8195 | 2025-08-20 01:06:00 | METOP-B | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 825310d7-409f-380e-9bfb-de84073696e5 | -6.9368 | -62.8717 | 2025-08-20 01:06:00 | METOP-B | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a120ca13-c8eb-30d4-8847-7fba9b47f100 | -13.0325 | -56.843102 | 2025-08-20 01:06:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6fedac92-c841-3be0-a5bf-04010d0c6f1a | -12.9761 | -56.866798 | 2025-08-20 01:06:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6102f3e6-3895-3570-a9fb-57f0db9906d6 | -6.1479 | -57.704102 | 2025-08-20 01:06:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bbe28ecf-e2e0-3912-8d5f-57da333ef7ae | -9.2298 | -60.332199 | 2025-08-20 01:06:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README6.md)
