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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bc229167-806c-33a9-9157-12784ca8ed2e | -18.0458 | -51.1336 | 2025-09-28 02:30:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 57.5 |
| c6a4d375-d587-37b3-a318-cd1e64b30a4a | -9.6512 | -62.8336 | 2025-09-28 02:30:00 | GOES-19 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 116.1 |
| 82099ae5-1035-315d-91cb-69ca0d1bfb7e | -9.6324 | -62.8534 | 2025-09-28 02:30:00 | GOES-19 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 61da555e-c1bc-389a-b32d-754b1d964e51 | -2.5957 | -48.4141 | 2025-09-28 02:30:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 41.7 |
| bef680be-12b8-3b65-b929-806019b4b855 | -9.6697 | -62.8518 | 2025-09-28 02:30:00 | GOES-19 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 9d4f27da-f6bf-310c-ba6b-c2c750507e34 | -16.9864 | -53.6947 | 2025-09-28 02:30:00 | GOES-19 | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 73.7 |
| 4e2badc3-e59a-3bc5-8779-481e0c92b7be | -16.947 | -53.7003 | 2025-09-28 02:30:00 | GOES-19 | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 52.8 |
| 78365329-401d-33b2-aba6-d12d7342b378 | -18.0254 | -51.1591 | 2025-09-28 02:30:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 67.1 |
| 6220f7e0-c644-3685-93c5-05591bb03452 | -7.7975 | -47.0019 | 2025-09-28 02:30:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 77.6 |
| 41bf0c0e-64d6-3432-bf2a-78e743cdd4a5 | -9.6511 | -62.8526 | 2025-09-28 02:30:00 | GOES-19 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 154.7 |
| 04dfe5c2-9147-3945-954a-f23de22a472d | -18.1977 | -53.3208 | 2025-09-28 02:40:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 45e97130-d72e-3df3-89f9-63f9d0ec8e4c | -11.4413 | -44.9998 | 2025-09-28 02:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 57.2 |
| 03fc494d-6041-32be-a030-d2f00606c582 | -16.9864 | -53.6947 | 2025-09-28 02:40:00 | GOES-19 | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 54.0 |
| 98f4f9a9-6c76-30b8-9870-cffeb0e75687 | -5.7396 | -42.8461 | 2025-09-28 02:40:00 | GOES-19 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 55.2 |
| d02a9810-4bd4-30e9-9d09-dc34ec5eab64 | -15.0585 | -42.3178 | 2025-09-28 02:40:00 | GOES-19 | MORTUGABA | BAHIA | Brasil | 2921807 | 29 | 33 | nan | nan | nan | Caatinga | 57.2 |
| 5dff6ea2-0237-3930-8b38-421d1966292d | -9.6697 | -62.8518 | 2025-09-28 02:40:00 | GOES-19 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 49.4 |
| 3cfa9841-5181-355c-9256-d6ba993cac9a | -9.6326 | -62.8344 | 2025-09-28 02:40:00 | GOES-19 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 5e4731cf-6ce6-357d-b47a-49faf2190a72 | -7.7975 | -47.0019 | 2025-09-28 02:40:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 66.3 |
| 67d78777-f5c2-3377-91b2-a6444de85aa1 | -12.9918 | -49.4448 | 2025-09-28 02:40:00 | GOES-19 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 61.1 |
| 984b5c56-cebf-32c1-b2cd-6b540d7b0645 | -11.9846 | -47.8865 | 2025-09-28 02:40:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 67.7 |
| ddffd9c1-7fc4-3297-9d60-8cda373917d7 | -9.6511 | -62.8526 | 2025-09-28 02:40:00 | GOES-19 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 143.0 |
| 6ca632da-8944-392c-a4d0-e2bacb059700 | -9.6324 | -62.8534 | 2025-09-28 02:40:00 | GOES-19 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 71.1 |
| 519664e2-44b7-36bd-94db-635ba4a8b893 | -5.8187 | -44.4413 | 2025-09-28 02:40:00 | GOES-19 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 68.0 |
| 0fd5cd6a-70a5-3d67-a143-63150e164268 | -15.0579 | -42.3424 | 2025-09-28 02:40:00 | GOES-19 | MORTUGABA | BAHIA | Brasil | 2921807 | 29 | 33 | nan | nan | nan | Caatinga | 57.3 |
| 865afbfd-05d4-3a72-aacd-c4fca7f4b274 | -7.8823 | -44.5594 | 2025-09-28 02:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 84.8 |
| 40c84567-2ee5-3325-a305-2477f1501148 | -16.9667 | -53.6975 | 2025-09-28 02:40:00 | GOES-19 | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 127.2 |
| 5fe244c4-fbe0-3ad2-a1f4-69dbabfa653d | -2.5957 | -48.4141 | 2025-09-28 02:40:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 42.0 |
| 57bed54a-7f91-3f52-8a6a-92feaceafd4f | -7.3847 | -47.0378 | 2025-09-28 02:40:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 64.9 |
| 243846ea-ee0c-3184-bf5d-fabd683a3cc8 | -7.8634 | -44.5612 | 2025-09-28 02:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 93.6 |
| a0f8c612-fa44-3c83-823c-658ede851caa | -9.6512 | -62.8336 | 2025-09-28 02:40:00 | GOES-19 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 127.8 |
| f450c2a9-ba78-3175-a7ac-75a229a9082c | -8.1611 | -46.4122 | 2025-09-28 02:50:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 39.7 |
| d8fbc019-0ed5-32c0-b651-8ceb37ddc523 | -9.6511 | -62.8526 | 2025-09-28 02:50:00 | GOES-19 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 170.1 |
| c65529c4-50e9-3369-950d-efeeb1ff96ac | -8.1799 | -46.4104 | 2025-09-28 02:50:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 40.9 |
| 20d57048-1451-3b77-97e3-e74a2b8dd5f1 | -9.6512 | -62.8336 | 2025-09-28 02:50:00 | GOES-19 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 159.5 |
| 17fcd5db-e93e-3451-80b1-8ba7443978ce | -5.7585 | -42.8211 | 2025-09-28 02:50:00 | GOES-19 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 39.3 |
| aa2a9952-4bfb-32bb-8ce0-03326c8395b8 | -2.5772 | -48.4146 | 2025-09-28 02:50:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 41.4 |
| 8461508f-99a6-3711-aca7-c90e6ddb1c68 | -5.6461 | -44.933 | 2025-09-28 02:50:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 62.6 |
| ef9d4423-d3d2-3973-88a0-86535fa9054a | -16.9667 | -53.6975 | 2025-09-28 02:50:00 | GOES-19 | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 124.4 |
| 9f33aa25-487e-3605-aa9b-58f2904e2d30 | -7.7975 | -47.0019 | 2025-09-28 02:50:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 62.3 |
| 9c88469b-afdf-394c-9f53-8b626018392a | -7.8634 | -44.5612 | 2025-09-28 02:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 105.4 |
| 86ea14cc-3b62-3622-af54-9dbaa926dec9 | -5.7396 | -42.8461 | 2025-09-28 02:50:00 | GOES-19 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 39.5 |
| 569fc402-af38-3a32-aea9-3f789f18e534 | -7.8823 | -44.5594 | 2025-09-28 02:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 88.4 |
| 3b5c7344-db39-3fee-b370-8146f1f4c8ed | -7.3847 | -47.0378 | 2025-09-28 02:50:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 43.0 |
| a787e49a-3704-3923-a0fb-5386dab8d1f2 | -5.7583 | -42.8447 | 2025-09-28 02:50:00 | GOES-19 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 67.0 |
| c58f15b6-023d-3eb7-8cac-75b02b8e5348 | -9.6512 | -62.8336 | 2025-09-28 03:00:00 | GOES-19 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 124.1 |
| 96b77c95-6aa2-3bd3-b877-bf84a73c37c8 | -11.5858 | -45.4851 | 2025-09-28 03:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 95.5 |
| eb5d4a41-e8d5-3dc9-87ae-b7d1b1ebf874 | -7.7972 | -47.0241 | 2025-09-28 03:00:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 57.1 |
| 26103b0d-464d-3c30-9d00-dc8093ddbdf0 | -7.7975 | -47.0019 | 2025-09-28 03:00:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 80.6 |
| 28cc5902-fcd2-30d5-953d-afca4a2923c1 | -16.9667 | -53.6975 | 2025-09-28 03:00:00 | GOES-19 | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 80.1 |
| 0af1704c-1968-35b4-bd2b-bcd30d92d75d | -2.5772 | -48.4146 | 2025-09-28 03:00:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 49.3 |
| 4b4753e1-3847-3c68-ba70-b52048fe3c0b | -9.6511 | -62.8526 | 2025-09-28 03:00:00 | GOES-19 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 172.0 |
| 1b3b5372-f1e7-3cca-b622-a37f76db7b1a | -7.3847 | -47.0378 | 2025-09-28 03:00:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 54.7 |
| 1cb3c742-a902-379a-90d7-f4fc7c902761 | -18.1977 | -53.3208 | 2025-09-28 03:00:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 74.8 |
| a28e8c50-690b-31bf-b61b-94ee4d6cdd7e | -11.9846 | -47.8865 | 2025-09-28 03:00:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 66.9 |
| 156a0866-7fea-315c-9db6-816fa8285c2a | -7.8163 | -47.0003 | 2025-09-28 03:00:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 55.8 |
| f23e9202-58f5-3008-adc4-9127754436dd | -9.6697 | -62.8518 | 2025-09-28 03:00:00 | GOES-19 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 48.5 |
| e8e86970-3951-373a-9db6-64fd3ad16766 | -9.6512 | -62.8336 | 2025-09-28 03:10:00 | GOES-19 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 117.9 |
| 849cbbd4-acfb-3d8b-af11-91bf3cb16e67 | -16.9667 | -53.6975 | 2025-09-28 03:10:00 | GOES-19 | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 83.5 |
| b2fe6f95-8edd-389f-b494-5ee180d39afb | -9.6326 | -62.8344 | 2025-09-28 03:10:00 | GOES-19 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 55.6 |
| 96538b6c-4b57-3cf7-94a5-c559f684648b | -12.9918 | -49.4448 | 2025-09-28 03:10:00 | GOES-19 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 55.9 |
| 6030e201-2952-3d9e-af00-cf17cd3fc7d4 | -7.8163 | -47.0003 | 2025-09-28 03:10:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 45.4 |
| d92c994e-8004-30ba-ba8d-fb35ea71e5e2 | -5.8149 | -42.8167 | 2025-09-28 03:10:00 | GOES-19 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 117.3 |
| 87f627ff-caa3-3ece-b729-8399f3618cd6 | -9.6511 | -62.8526 | 2025-09-28 03:10:00 | GOES-19 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 117.7 |
| 08930187-c3d9-3525-b7da-019240033c45 | -9.6324 | -62.8534 | 2025-09-28 03:10:00 | GOES-19 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 66dfe16d-368a-3379-a7d7-4ee45f69ece3 | -5.8151 | -42.7931 | 2025-09-28 03:10:00 | GOES-19 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 71.6 |
| 458a31f6-d80c-35fe-8a3c-46ad7a623141 | -7.7975 | -47.0019 | 2025-09-28 03:10:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 57.0 |
| 7ed7645d-df19-3cd7-8c93-982e32a1349e | -13.6118 | -48.101 | 2025-09-28 03:10:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 66.4 |
| 7aad1ce1-e995-3dae-8184-32fbfb6d2b10 | -5.3059 | -43.1365 | 2025-09-28 03:20:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 81.8 |
| 07502af9-21fe-345b-9be7-390af6262103 | -8.1799 | -46.4104 | 2025-09-28 03:20:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 49.4 |
| a5f3962a-6c9a-3f68-a952-5ee00ddf4d20 | -2.5957 | -48.4141 | 2025-09-28 03:20:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 34.4 |
| 9ad493ef-5f3b-3d70-bbf8-f382ae0bde2e | -12.6917 | -46.8708 | 2025-09-28 03:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 63.2 |
| 9f3918fd-4afd-3698-929b-8d1a6998b7b9 | -9.6512 | -62.8336 | 2025-09-28 03:20:00 | GOES-19 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 97.9 |
| 84681d3c-43d4-38c7-b85c-4c56453dfb6d | -9.6324 | -62.8534 | 2025-09-28 03:20:00 | GOES-19 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 65.6 |
| 555ee86b-3e2e-39bd-ab2a-17a9f597e329 | -16.9667 | -53.6975 | 2025-09-28 03:20:00 | GOES-19 | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 67.1 |
| 43b1a097-5131-35b5-9801-b339c59720fd | -8.1611 | -46.4122 | 2025-09-28 03:20:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 63.8 |
| b411b192-1bde-3e7f-8016-7fe647d7b123 | -11.9846 | -47.8865 | 2025-09-28 03:20:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 68.5 |
| e7b698cf-318b-30ec-a6db-89acf4c4f04c | -5.2871 | -43.1379 | 2025-09-28 03:20:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 87.0 |
| 053e8194-ed77-3ed8-b767-daa126b48488 | -5.7396 | -42.8461 | 2025-09-28 03:20:00 | GOES-19 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 53.1 |
| 1822a6f6-446f-3f84-8523-c0b44ca00e01 | -5.3057 | -43.1599 | 2025-09-28 03:20:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 113.6 |
| 70dd95fe-7747-32e6-811b-4a0307804d48 | -5.8187 | -44.4413 | 2025-09-28 03:20:00 | GOES-19 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 72.3 |
| 299eca6a-5798-3e48-884b-c2f92ab7d9b1 | -5.8149 | -42.8167 | 2025-09-28 03:20:00 | GOES-19 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 117.6 |
| 10caabab-8ce2-3300-b07a-336441bb4cd0 | -12.9918 | -49.4448 | 2025-09-28 03:20:00 | GOES-19 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 53.2 |
| 0e633ee8-2521-317e-93bb-2fa81b50dacc | -9.6511 | -62.8526 | 2025-09-28 03:20:00 | GOES-19 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 126.0 |
| 0ba92515-921c-3755-af6a-2810408514cc | -11.0083 | -57.0658 | 2025-09-28 03:20:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 47.1 |
| 99c8f868-6ad5-3692-90d3-8602b8e5bb11 | -8.2856 | -45.4545 | 2025-09-28 03:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 63.7 |
| c7058d46-0527-383d-8a25-beeb90005659 | -8.1614 | -46.3899 | 2025-09-28 03:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 42.4 |
| 3b4256c6-4d0d-35f3-81a9-96f5d0c5c472 | -9.6326 | -62.8344 | 2025-09-28 03:20:00 | GOES-19 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 8ce7b096-5e80-3de5-a3eb-64075baf9429 | -5.2869 | -43.1613 | 2025-09-28 03:20:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 124.0 |
| 8046e784-d696-3166-8a21-d799c0dcdffc | -11.5858 | -45.4851 | 2025-09-28 03:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 68.8 |
| 4affbfad-f283-3a8b-be10-aaf0e687b4ec | -2.5772 | -48.4146 | 2025-09-28 03:20:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 34.4 |
| 2ae965d5-e967-3152-9986-426dc5d409f6 | -8.1611 | -46.4122 | 2025-09-28 03:30:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 111.6 |
| 38d2dc8b-5fcf-33f9-80b8-996376a59158 | -9.6324 | -62.8534 | 2025-09-28 03:30:00 | GOES-19 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 50.0 |
| 71696b8e-f095-337f-a888-e7a00aa35eee | -8.1614 | -46.3899 | 2025-09-28 03:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 58.7 |
| 613e5410-cf8d-35b2-84da-bc346b49cf20 | -5.8149 | -42.8167 | 2025-09-28 03:30:00 | GOES-19 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 85.9 |
| 61139f5e-19e4-378f-a886-9877c4dd33a3 | -9.6512 | -62.8336 | 2025-09-28 03:30:00 | GOES-19 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 93.5 |
| 41ef0a6b-4f37-3bae-8628-4668593a3543 | -12.9918 | -49.4448 | 2025-09-28 03:30:00 | GOES-19 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 78.5 |
| 2880c497-f40c-3285-86be-4c836eddb963 | -9.6511 | -62.8526 | 2025-09-28 03:30:00 | GOES-19 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 118.0 |
| e00d6324-b03a-344f-a5c4-5d82a5ecd061 | -16.9667 | -53.6975 | 2025-09-28 03:30:00 | GOES-19 | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 68.6 |
| f86f35ab-c294-3ec8-9411-089f164cae08 | -8.1802 | -46.3881 | 2025-09-28 03:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 45.4 |
| 4866242c-24a1-3fa9-8856-c8f58110a070 | -8.1799 | -46.4104 | 2025-09-28 03:30:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 83.2 |


[Clique aqui para ver as próximas entradas](README11.md)
