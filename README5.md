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
| 39c81cb0-97ee-3a90-98f6-469a1e0887be | -3.4899 | -43.6383 | 2025-11-05 01:40:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 156.4 |
| 9fc0d51b-118f-33a1-95ca-39ffa49affaf | -5.474 | -45.3976 | 2025-11-05 01:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 61.1 |
| d22b042a-a44e-3666-bb41-b182f3f59abf | -4.4446 | -43.2164 | 2025-11-05 01:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 119.2 |
| 1c6335d6-35bf-3740-b204-7fdda91343d1 | -4.4259 | -48.9465 | 2025-11-05 01:40:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 150.4 |
| 7c8de8f1-4502-3c38-a6ef-48198e90a28b | -1.2822 | -49.168 | 2025-11-05 01:40:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 48.5 |
| 256b634e-3eb2-305d-bf74-b83b32e73d44 | -1.2453 | -49.1472 | 2025-11-05 01:40:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 44.4 |
| 70d7c3b1-78bc-3ebb-b5f6-f35913327a48 | -3.4714 | -43.616 | 2025-11-05 01:40:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 47.6 |
| c9fae852-06b4-3d51-87e5-598ae2aec2d5 | -4.4073 | -48.9474 | 2025-11-05 01:40:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 118.6 |
| c6a2c42e-62e4-37db-ab10-bdab5a86c955 | -2.6509 | -48.4985 | 2025-11-05 01:50:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 34.6 |
| 2f844e4b-630d-31c3-8f09-2235bfec3982 | -11.8473 | -43.7256 | 2025-11-05 01:50:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 90.3 |
| d070e9f7-a872-32ee-9622-194a8af4bd51 | -1.2638 | -49.1469 | 2025-11-05 01:50:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 69.1 |
| 79ef580b-0fef-37cf-86c4-e96c73976815 | -1.2822 | -49.1467 | 2025-11-05 01:50:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 49.6 |
| 6fc2cb9e-626a-3732-8f75-c317d3c29bb1 | -4.4259 | -48.9465 | 2025-11-05 01:50:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 153.8 |
| 59e7793c-5ed9-3776-9ad8-73a3903f50dd | -4.4073 | -48.9474 | 2025-11-05 01:50:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 110.6 |
| 2bd92b1e-697f-3a47-9a8f-bc7522fb5ab8 | -4.4633 | -43.2152 | 2025-11-05 01:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 298.1 |
| 33f8191b-5bcb-3575-8bd9-e8cb43752bca | -1.3006 | -49.1677 | 2025-11-05 01:50:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 53.9 |
| ab802f52-b1d9-372d-ae77-d87fa4cf3d7a | -3.4712 | -43.6392 | 2025-11-05 01:50:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 60.0 |
| aa06b83a-05b4-3786-a7d1-484c4eaae46f | -4.4632 | -43.2386 | 2025-11-05 01:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 211.4 |
| 575bd650-ca0a-37e3-a822-81af9abf8b8f | -4.4819 | -43.2374 | 2025-11-05 01:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 147.1 |
| 3d76f6e3-4f4c-30f2-948a-794897310957 | -2.6508 | -48.52 | 2025-11-05 01:50:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 28.9 |
| 98e6c048-0809-3717-8a47-c43aa9b26598 | -3.4899 | -43.6383 | 2025-11-05 01:50:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 127.9 |
| 022a1853-cb5d-3e0f-97d1-bb93c763ae37 | -3.2799 | -44.5882 | 2025-11-05 01:50:00 | GOES-19 | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 72.9 |
| 7b5d8ca6-37d2-36e2-a6ec-b6ffd1dd26bf | -5.4551 | -45.4214 | 2025-11-05 01:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 71.4 |
| a4eec2a2-a6ea-37c6-b402-292e14435463 | -4.426 | -48.9251 | 2025-11-05 01:50:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 38.1 |
| bd94ff3d-22cd-3b5b-8b10-975f08528b49 | -3.2798 | -44.611 | 2025-11-05 01:50:00 | GOES-19 | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 397cf445-00c4-3d66-9532-8bdca8a65b68 | -3.2317 | -46.8716 | 2025-11-05 01:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 92.0 |
| abafc9a5-2fe1-3a82-8b0c-9e19c69ff3c2 | -4.482 | -43.2141 | 2025-11-05 01:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 130.4 |
| 928dda5c-caa5-3153-aa18-619fab5bed9b | -5.2268 | -48.4976 | 2025-11-05 01:50:00 | GOES-19 | ESPERANTINA | TOCANTINS | Brasil | 1707405 | 17 | 33 | nan | nan | nan | Amazônia | 55.6 |
| 8dd49002-5d94-38fa-827c-3cfd8e2a5f74 | -5.0399 | -43.6205 | 2025-11-05 01:50:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 84.9 |
| 46f69926-6728-380e-b637-0f85cc87b205 | -5.4553 | -45.3988 | 2025-11-05 01:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 183.9 |
| 92139680-08de-3f55-89af-cd6f73789d4b | -4.4446 | -43.2164 | 2025-11-05 01:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 92.3 |
| a5c7249b-e291-3dd6-b3f1-fd6f1cd13553 | -1.2822 | -49.168 | 2025-11-05 01:50:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 47.7 |
| 78f59226-324a-3884-9d90-a1c6c25b64f0 | -3.49 | -43.6152 | 2025-11-05 01:50:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 105.4 |
| 918a745c-4cd0-35b3-9871-8bb3cb36e114 | -5.2453 | -48.4966 | 2025-11-05 01:50:00 | GOES-19 | ESPERANTINA | TOCANTINS | Brasil | 1707405 | 17 | 33 | nan | nan | nan | Amazônia | 80.4 |
| 6e373084-5745-3a28-9a89-f56132dbe6a1 | -4.4633 | -43.2152 | 2025-11-05 02:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 295.1 |
| c32b7321-c1c3-3c90-8633-75a70c3239c1 | -2.7921 | -50.3196 | 2025-11-05 02:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 9522c106-f063-370a-8d8c-a3ae278a8312 | -1.2638 | -49.1469 | 2025-11-05 02:00:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 68.3 |
| b23d6616-a433-3b6a-84ef-3cc4dc12ca73 | -5.2453 | -48.4966 | 2025-11-05 02:00:00 | GOES-19 | ESPERANTINA | TOCANTINS | Brasil | 1707405 | 17 | 33 | nan | nan | nan | Amazônia | 77.3 |
| fc06c410-066e-30f2-a181-f21c1fe0331d | -3.49 | -43.6152 | 2025-11-05 02:00:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 94.0 |
| 4fb1b2b0-9aaa-3248-bff6-8c873a7b45e2 | -1.2822 | -49.168 | 2025-11-05 02:00:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 74.3 |
| fd071ce8-96b1-342d-a406-caf1072f51e8 | -5.0399 | -43.6205 | 2025-11-05 02:00:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 79.8 |
| 03b22c49-d06a-3d61-8abb-347f092c670e | -11.8473 | -43.7256 | 2025-11-05 02:00:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 67.8 |
| 9573fb16-5c82-35e0-99ea-30c11f2e1b91 | -4.4259 | -48.9465 | 2025-11-05 02:00:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 117.0 |
| 1cd35213-42d0-3e95-9ccc-2c58b88384e4 | -1.3006 | -49.1677 | 2025-11-05 02:00:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 277a7cff-97b1-3798-b526-f55436ed9531 | -4.4073 | -48.9474 | 2025-11-05 02:00:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 122.4 |
| 1049d76c-7cf9-3bb2-840a-a1322181a136 | -5.2268 | -48.4976 | 2025-11-05 02:00:00 | GOES-19 | ESPERANTINA | TOCANTINS | Brasil | 1707405 | 17 | 33 | nan | nan | nan | Amazônia | 58.4 |
| d3d4f714-9867-3731-adf4-5e5f23955ca5 | -4.4446 | -43.2164 | 2025-11-05 02:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 101.2 |
| 3214d53f-350f-3f09-ad5a-5ecf4db7107d | -3.2317 | -46.8716 | 2025-11-05 02:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 67.6 |
| ebd1d743-1fb7-3a30-b149-bd207951fccd | -1.2822 | -49.1467 | 2025-11-05 02:00:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 82.1 |
| 7f8a7187-97a3-3e8e-9b9f-09e1f5daf997 | -5.4553 | -45.3988 | 2025-11-05 02:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 131.3 |
| 04ade8b2-7762-37a0-bfa3-c57ae9ac6658 | -4.4819 | -43.2374 | 2025-11-05 02:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 133.6 |
| 72dd9616-a016-3530-a0e0-9f367cd7edcd | -3.4712 | -43.6392 | 2025-11-05 02:00:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 57.5 |
| 85716170-ac54-32a7-804d-4f979e69dc25 | -3.4899 | -43.6383 | 2025-11-05 02:00:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 110.1 |
| 1d7f28bc-4f14-3612-882c-6a48eea783c6 | -2.6508 | -48.52 | 2025-11-05 02:00:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 45.4 |
| 896b66a0-c7b5-35d2-b2c5-af0300c8a2ad | -4.4632 | -43.2386 | 2025-11-05 02:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 192.5 |
| 33a6fe79-11cb-36e2-b91b-7885433d7361 | -4.482 | -43.2141 | 2025-11-05 02:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 129.4 |
| b1523f74-01dd-3b44-9015-0d281fd4555e | -3.2317 | -46.8716 | 2025-11-05 02:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 011ffffe-d8fc-32b8-865f-0fd94c9c1fc4 | -5.2268 | -48.4976 | 2025-11-05 02:10:00 | GOES-19 | ESPERANTINA | TOCANTINS | Brasil | 1707405 | 17 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 8b4ac136-69ff-3858-9736-17654b3b1c87 | -4.4819 | -43.2374 | 2025-11-05 02:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 156.9 |
| 8587704b-c4c2-326e-859c-b0fbaa45d705 | -5.2453 | -48.4966 | 2025-11-05 02:10:00 | GOES-19 | ESPERANTINA | TOCANTINS | Brasil | 1707405 | 17 | 33 | nan | nan | nan | Amazônia | 76.6 |
| c89b4486-d010-3020-9b7a-15fe06434472 | -4.4259 | -48.9465 | 2025-11-05 02:10:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 132.2 |
| eee2783e-8fc3-35c6-b0e7-8895338b9abf | -4.4632 | -43.2386 | 2025-11-05 02:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 211.9 |
| f1f5fc7f-40be-315a-b48c-16e603db4ca1 | -4.482 | -43.2141 | 2025-11-05 02:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 105.2 |
| a3a1db82-a1e2-3d95-b4fb-69bbdbb55023 | -1.2822 | -49.1467 | 2025-11-05 02:10:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 89.0 |
| ec2145f0-8e48-32a8-b3a0-0df359d2a1e3 | -1.2822 | -49.168 | 2025-11-05 02:10:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 94.2 |
| f34a75b8-0fc7-3dbf-b103-384af36fd91f | -3.49 | -43.6152 | 2025-11-05 02:10:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 72.4 |
| 97909cd8-a643-3ab7-ada9-9ba8d073859f | -4.4633 | -43.2152 | 2025-11-05 02:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 284.0 |
| 9d83cee9-0b17-31f0-9ca3-b074d2f19e4c | -3.4899 | -43.6383 | 2025-11-05 02:10:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 112.9 |
| 0ce76ddb-c069-34f1-85c7-922d7dc48078 | -4.4446 | -43.2164 | 2025-11-05 02:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 96.1 |
| 5e8279fd-6274-3275-931e-11898ce671f4 | -1.3006 | -49.1677 | 2025-11-05 02:10:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 99.3 |
| b123ec8b-88fa-300d-b458-f9355d93cab7 | -2.6508 | -48.52 | 2025-11-05 02:10:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 31.2 |
| 458a1f8f-bbc2-3593-9e36-78903f02db83 | -4.426 | -48.9251 | 2025-11-05 02:10:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 47.8 |
| 247e06b6-7066-34f5-9e7c-5f60bfd6ffd6 | -1.3007 | -49.1464 | 2025-11-05 02:10:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 50.1 |
| f0afe3aa-ad4f-35a1-9dfa-92d44fef3877 | -5.0399 | -43.6205 | 2025-11-05 02:10:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 72.2 |
| 2e03436b-ae5c-3b0b-9ec5-4f15b99997e1 | -11.8473 | -43.7256 | 2025-11-05 02:10:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 78.5 |
| 649328cb-ffca-375f-9c44-5977b55fde16 | -5.4553 | -45.3988 | 2025-11-05 02:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 161.3 |
| ea708915-428c-3483-863a-098a9b6691e4 | -3.4712 | -43.6392 | 2025-11-05 02:10:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 52.1 |
| 9bbfe2db-4359-38ae-af9c-83d17787cab0 | -4.4073 | -48.9474 | 2025-11-05 02:10:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 96.9 |
| ed9000ed-0572-3bcb-97a3-ee0f9eebc136 | -1.2638 | -49.1469 | 2025-11-05 02:10:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 53.0 |
| d4e06791-58a3-362a-91ff-fac073855b52 | -3.8166 | -52.3608 | 2025-11-05 02:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 47.2 |
| 4a071f0b-7ee1-3e2c-8e91-6415f804c560 | -3.4712 | -43.6392 | 2025-11-05 02:20:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 49.4 |
| 19fd926d-fd30-342e-a00d-d96fa052b83c | -5.0399 | -43.6205 | 2025-11-05 02:20:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 77.3 |
| fd23cbf6-ca1e-3eda-b5ad-394626a16375 | -4.4819 | -43.2374 | 2025-11-05 02:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 118.9 |
| 710032d9-59eb-3b40-80e6-feca53238a24 | -1.3006 | -49.1677 | 2025-11-05 02:20:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 97.3 |
| ddb72d5d-4d77-3e2d-85c3-714ec7e364fc | -5.4553 | -45.3988 | 2025-11-05 02:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 131.1 |
| fb0a3e41-5936-32aa-ae8d-47a47bf301b3 | -4.4633 | -43.2152 | 2025-11-05 02:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 255.4 |
| 75a8547c-d142-388e-ac18-61c7b27363ac | -4.4259 | -48.9465 | 2025-11-05 02:20:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 104.0 |
| 0d22489d-a611-322c-8005-18045a72464d | -3.49 | -43.6152 | 2025-11-05 02:20:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 74.3 |
| 778ae811-51ad-35ad-a960-9864ab868d1c | -5.2453 | -48.4966 | 2025-11-05 02:20:00 | GOES-19 | ESPERANTINA | TOCANTINS | Brasil | 1707405 | 17 | 33 | nan | nan | nan | Amazônia | 111.3 |
| a6b45bd5-dc3a-3534-95d6-8fdd48de9b0e | -5.2268 | -48.4976 | 2025-11-05 02:20:00 | GOES-19 | ESPERANTINA | TOCANTINS | Brasil | 1707405 | 17 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 4941038e-8752-370a-9796-12a34b7eb7a9 | -4.4073 | -48.9474 | 2025-11-05 02:20:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 99.5 |
| 990e66bc-e570-3f38-a8ef-435beaacf812 | -2.7921 | -50.3196 | 2025-11-05 02:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 02baf46f-a264-3101-82d6-a48d2e17bab4 | -11.8473 | -43.7256 | 2025-11-05 02:20:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 58.3 |
| f415c498-bb37-331c-ac2d-544e749f1303 | -1.2822 | -49.168 | 2025-11-05 02:20:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 74.4 |
| 8b8c92db-ea39-3fff-bb7c-f493aecec640 | -3.2317 | -46.8716 | 2025-11-05 02:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 56.4 |
| f9cf30d7-d7a4-321a-a693-6f314d809023 | -4.4632 | -43.2386 | 2025-11-05 02:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 173.2 |
| 92565e4a-6a37-32c8-9eca-e51691f8e1d7 | -1.2822 | -49.1467 | 2025-11-05 02:20:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 80.8 |
| 865dc03c-e0ac-3e7e-9385-f55da69ee9c3 | -1.3007 | -49.1464 | 2025-11-05 02:20:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 54.1 |
| 0344c958-e0bc-3ad3-bd9b-7590522690c7 | -4.4446 | -43.2164 | 2025-11-05 02:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 92.2 |
| b451012f-5eae-3558-b8b8-ba94395d0731 | -2.6508 | -48.52 | 2025-11-05 02:20:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 41.5 |


[Clique aqui para ver as próximas entradas](README6.md)
