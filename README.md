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
| 9348ca67-073d-3555-88bf-4ca0104ee9ad | -5.0725 | -44.2182 | 2024-11-05 00:00:00 | GOES-16 | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 39.8 |
| 73722ee8-a3a3-3121-ba3a-6274554e0dd8 | -4.408 | -43.1018 | 2024-11-05 00:00:00 | GOES-16 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 106.8 |
| 3f8c1df3-ff93-3cd0-acdf-b025a2527c64 | -4.3806 | -47.2388 | 2024-11-05 00:00:00 | GOES-16 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 60.1 |
| 0adcfe4d-f8b9-30fa-ac35-580489dba7ee | -5.6944 | -45.8323 | 2024-11-05 00:00:00 | GOES-16 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 140.0 |
| 530101e4-c201-3786-9c13-bfb222d1d88a | -3.1061 | -50.2686 | 2024-11-05 00:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 68.8 |
| 65892f97-05ee-3de8-b87a-53f008eb2058 | -5.0724 | -44.2412 | 2024-11-05 00:00:00 | GOES-16 | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 53.9 |
| 35d83261-b424-335c-9554-ed3b1fd72df1 | -3.5631 | -47.3847 | 2024-11-05 00:00:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 218.3 |
| c3f80c85-e8fd-3e80-ae23-f925bb4de65a | -4.4266 | -43.1241 | 2024-11-05 00:00:00 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 67.2 |
| 84d6206f-934e-396f-8d73-0e77358c6b96 | -5.6943 | -45.8547 | 2024-11-05 00:00:00 | GOES-16 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 53.7 |
| 1138880d-6c66-3e30-bdbe-ce5a0b15fc08 | -1.514 | -53.4918 | 2024-11-05 00:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 52.2 |
| a9f1bb52-f4a9-3ce3-9e13-1cb9d5e9fbdd | -3.4749 | -50.3826 | 2024-11-05 00:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 56.9 |
| 99fe9d92-8277-39ab-9920-3eb3ecaf21b0 | -10.7691 | -45.2539 | 2024-11-05 00:00:00 | GOES-16 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 54.8 |
| b7a28eee-d6e7-3491-9fc5-b6ad3d538857 | -3.563 | -47.4066 | 2024-11-05 00:00:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 102.4 |
| 3b36541e-f7fe-35b5-b583-ffd59d87739b | -4.2464 | -44.9287 | 2024-11-05 00:00:00 | GOES-16 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Amazônia | 65.5 |
| c8e74a26-7f63-3464-a833-7d997bec403a | -3.4612 | -45.5299 | 2024-11-05 00:00:00 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 65.5 |
| ee324cca-bbfb-32a7-b889-c6a5dfd132ec | -4.362 | -47.2397 | 2024-11-05 00:00:00 | GOES-16 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 46.6 |
| 7e59122a-fb4e-35b9-86d5-aa3798be99a5 | -11.8639 | -43.8644 | 2024-11-05 00:00:00 | GOES-16 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 119.7 |
| 216d5c69-9647-312d-bc49-a52d9aef9f88 | -3.1787 | -50.5807 | 2024-11-05 00:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 62.4 |
| 3d8c4b83-0039-3baf-ae8d-38c2295a02db | -3.1062 | -50.2476 | 2024-11-05 00:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 75.9 |
| 7acb061e-f0d3-3d04-962c-c92dbd1fcb77 | -4.4268 | -43.1007 | 2024-11-05 00:00:00 | GOES-16 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 78.6 |
| ee059abb-b993-3b1c-9075-72a2b9047dea | -4.243 | -48.5259 | 2024-11-05 00:00:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 61.6 |
| a83a06d2-aa60-3efd-a9af-d0ecdb32037a | -11.8634 | -43.888 | 2024-11-05 00:00:00 | GOES-16 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 70.4 |
| 3b4094ce-909d-3b94-8c86-fff0c6567c1e | -4.4079 | -43.1252 | 2024-11-05 00:00:00 | GOES-16 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 89.4 |
| e5537bd8-06e1-337e-a83d-a59eb22e0edb | -3.4798 | -45.5291 | 2024-11-05 00:00:00 | GOES-16 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 93.7 |
| 892925c0-2a69-3f4e-9a8f-d3553373dacb | -8.9336 | -65.0471 | 2024-11-05 00:00:00 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 9dc1caba-f2ba-3fee-8de1-11e59d245b9c | -3.967 | -48.15 | 2024-11-05 00:00:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 101.6 |
| 9f7958d3-f0d9-35ea-943c-c1ff317f698f | -4.2429 | -48.5474 | 2024-11-05 00:00:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 72.5 |
| 7412b2cb-ee61-3dcc-b0d9-cfa003ff035c | -3.0906 | -54.5073 | 2024-11-05 00:00:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 62.5 |
| 6900e3dc-a3e7-369a-82e0-bffaef239484 | -2.8065 | -51.4855 | 2024-11-05 00:00:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 75.5 |
| e636c09a-b51b-3248-bf93-0fb63bcc19fe | -3.5444 | -47.4073 | 2024-11-05 00:00:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 65.1 |
| b38c2e0c-c636-3900-b483-9d31dceeb676 | -13.3597 | -54.0072 | 2024-11-05 00:00:00 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 281933ae-ba99-304d-8505-595e459ced1e | -1.514 | -53.512 | 2024-11-05 00:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 59.3 |
| f1b47188-6166-3dba-8c15-2efb50d417be | -3.9669 | -48.1716 | 2024-11-05 00:00:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 26fd5701-152c-3c5e-9ea8-fea1aa0f309e | -2.8064 | -51.5061 | 2024-11-05 00:00:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 42.5 |
| 754c4bc7-972d-3992-ac92-15d07467e64a | -3.5632 | -47.3629 | 2024-11-05 00:00:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 66777105-f061-365a-b462-a3cc95ac85df | -3.1786 | -50.6016 | 2024-11-05 00:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 53.8 |
| 70d4d53f-59fa-38cf-b0df-f0bc9ab5548b | -3.0137 | -45.8384 | 2024-11-05 00:00:00 | GOES-16 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 38.2 |
| 260eb248-f7b0-37c3-99ca-691b8d55e099 | -3.0876 | -50.2691 | 2024-11-05 00:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 53.0 |
| a634fb7d-0667-3174-96c0-8101e670d694 | -5.6946 | -45.8098 | 2024-11-05 00:00:00 | GOES-16 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 46.4 |
| cbe8d12d-801d-348e-8c7e-07753a60e27b | -3.5446 | -47.3855 | 2024-11-05 00:00:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 118.3 |
| c1e18a9e-8274-3e7c-bb70-9e32b51d0306 | -13.36 | -53.9865 | 2024-11-05 00:00:00 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 73.0 |
| b8961e55-401c-32b7-9b86-09d3f42586cd | -12.4015 | -63.2884 | 2024-11-05 00:00:00 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 58.2 |
| f13ef7b5-9a42-3169-9557-ba3a85c4d822 | -5.4861 | -48.6121 | 2024-11-05 00:00:00 | GOES-16 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 95135176-3419-3dc4-8495-0f2c9c93e2bb | -4.843 | -44.9402 | 2024-11-05 00:00:00 | GOES-16 | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 57.1 |
| d84785f4-b534-3397-93c3-800ff95d85f0 | -4.8862 | -46.706 | 2024-11-05 00:00:00 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 27a03a72-9d8e-343c-8d56-889d7c17fbe1 | -3.4799 | -45.5067 | 2024-11-05 00:00:00 | GOES-16 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 41.5 |
| a6b4348d-a955-3cf7-8aeb-1a7c0367deae | -3.9669 | -48.1716 | 2024-11-05 00:10:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 8dd08a66-9b5c-32ff-9a3c-d2646edbe0df | -13.3597 | -54.0072 | 2024-11-05 00:10:00 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 57.3 |
| d44d6302-a440-3a0d-b940-13c8a9911c3d | -5.6943 | -45.8547 | 2024-11-05 00:10:00 | GOES-16 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 50.9 |
| 59cc3578-37f1-3810-9ea6-03cc03cfde6e | -3.4612 | -45.5299 | 2024-11-05 00:10:00 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 66.5 |
| 47cef28b-9ca5-3e83-8f9c-e57371582c8d | -6.1043 | -43.9362 | 2024-11-05 00:10:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 86.2 |
| 5d8d7e1f-698a-3fb1-a61e-e149287df8fe | -2.8065 | -51.4855 | 2024-11-05 00:10:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 83.7 |
| 5c4387b7-d9d1-3fd6-a0a2-e3d625c0d204 | -4.408 | -43.1018 | 2024-11-05 00:10:00 | GOES-16 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 75.5 |
| 37d6b704-148a-3569-945b-8780cb167a28 | -11.8639 | -43.8644 | 2024-11-05 00:10:00 | GOES-16 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 70.1 |
| f5a244a9-d3be-3333-97dd-1d54e93fc437 | -3.4798 | -45.5291 | 2024-11-05 00:10:00 | GOES-16 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 75.4 |
| 22dce3df-0c9a-397b-b9b4-e8bdb641d63a | -3.1062 | -50.2476 | 2024-11-05 00:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 68.9 |
| 22485e4a-c38b-3353-a4b6-29ff39330e95 | -8.915 | -65.0477 | 2024-11-05 00:10:00 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 55.4 |
| 31256a2c-fc2c-3c0d-a08e-ecfb94d9d24b | -4.843 | -44.9402 | 2024-11-05 00:10:00 | GOES-16 | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 73.1 |
| 43806f14-980a-306e-ad31-6e39c452f380 | -4.4079 | -43.1252 | 2024-11-05 00:10:00 | GOES-16 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 61.9 |
| 6eb1a25a-d2ae-3455-b6e1-e86733ed3af5 | -6.1226 | -43.9809 | 2024-11-05 00:10:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 49.5 |
| 7ab506ab-d04b-3a64-8349-5596eeb17b68 | -8.9336 | -65.0471 | 2024-11-05 00:10:00 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 72.3 |
| 46f6b15c-991c-3c14-9c4f-2bf8f878d8c9 | -5.6944 | -45.8323 | 2024-11-05 00:10:00 | GOES-16 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 144.0 |
| 19dc0d80-cc83-395e-9ee0-4423eb9d850a | -1.514 | -53.512 | 2024-11-05 00:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 57.0 |
| e27d0e49-b223-3c4e-8fd3-5072a7beb69a | -4.2429 | -48.5474 | 2024-11-05 00:10:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 8d07d061-bde6-38ea-b9e6-5f74c9e03153 | -3.967 | -48.15 | 2024-11-05 00:10:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 97.7 |
| 5d83c732-5789-3195-b8ae-89fdb9189424 | -4.243 | -48.5259 | 2024-11-05 00:10:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 46.7 |
| cc9096e6-7df9-377a-8948-4b968cabe133 | -12.4015 | -63.2884 | 2024-11-05 00:10:00 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 49a35fe4-cbe9-3db1-8c80-336b2c7edcb2 | -3.5446 | -47.3855 | 2024-11-05 00:10:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 137.7 |
| 118b8f2d-a350-3c99-bf19-68a75d4b277d | -3.563 | -47.4066 | 2024-11-05 00:10:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 100.6 |
| 32ef1a3e-6d2a-3f47-8352-20c31522d537 | -5.0724 | -44.2412 | 2024-11-05 00:10:00 | GOES-16 | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 49.7 |
| b8d5c62f-de6e-34f1-aa3a-28a62eae628f | -5.0725 | -44.2182 | 2024-11-05 00:10:00 | GOES-16 | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 45.2 |
| cbfaa28b-4cbc-30ed-a0b9-eda14a54e9cc | -4.3806 | -47.2388 | 2024-11-05 00:10:00 | GOES-16 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 06083bfb-60ab-396f-8b36-a1df40882dae | -2.8064 | -51.5061 | 2024-11-05 00:10:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 46.9 |
| 982766de-5823-3608-b7b8-e3573f0ca00e | -6.1229 | -43.9578 | 2024-11-05 00:10:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 105.5 |
| 281da656-45fc-3e3e-9e88-e0cc17d39334 | -8.9337 | -65.0283 | 2024-11-05 00:10:00 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 50.0 |
| 0142c245-63d0-3396-9dff-32f379832cc0 | -3.4799 | -45.5067 | 2024-11-05 00:10:00 | GOES-16 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 36.8 |
| f0220d22-58f4-352b-98b1-0e919d2d8b4c | -5.6758 | -45.8335 | 2024-11-05 00:10:00 | GOES-16 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 48.0 |
| 7e258c0d-da2a-3471-b23f-39d99c9c19c4 | -3.1061 | -50.2686 | 2024-11-05 00:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 64.2 |
| fe9cbaf6-817a-3469-bed4-3e3aa8053b99 | -3.1787 | -50.5807 | 2024-11-05 00:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 59.1 |
| e9ae5f2e-5dcd-3e1c-ba0b-046d79e9b49b | -3.5444 | -47.4073 | 2024-11-05 00:10:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 71.9 |
| e3ffe4c5-09ee-357b-825c-4ad01af48d99 | -4.8862 | -46.706 | 2024-11-05 00:10:00 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 70.3 |
| 3b7d9ed3-dcd5-32f1-99c9-6773333868de | -13.36 | -53.9865 | 2024-11-05 00:10:00 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 517bcf8f-f86c-3afb-8cfa-ee982caf3a48 | -6.1039 | -43.9824 | 2024-11-05 00:10:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 84.2 |
| b182dff8-8981-3025-8672-d4a9de17f454 | -6.0853 | -43.9608 | 2024-11-05 00:10:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 63.8 |
| e43c7edf-39bc-3a7d-a454-d4a6b4d1a970 | -1.514 | -53.4918 | 2024-11-05 00:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 50.8 |
| 3596cb3e-310e-3a22-bcc8-f355fea3ef32 | -4.2243 | -48.5482 | 2024-11-05 00:10:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 9de44e2e-37a4-3788-a48f-44b6a3ea26d5 | -3.5631 | -47.3847 | 2024-11-05 00:10:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 216.5 |
| 9849dee4-40c9-3e2e-bd9d-e0ac81f7d1c2 | -3.0722 | -54.5077 | 2024-11-05 00:10:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 58.6 |
| f5da74aa-7b59-3577-8be9-489927be819e | -6.1041 | -43.9593 | 2024-11-05 00:10:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 330.1 |
| f2f92ff9-5ad3-3860-a3c1-bc5829b94c21 | -4.2244 | -48.5267 | 2024-11-05 00:10:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 44.3 |
| cd499bee-5fc3-3906-99cd-a72b42b3b526 | -2.6507 | -48.5629 | 2024-11-05 00:10:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 54.0 |
| b55ac1ee-95e4-38e1-afa9-ad4541f098cb | -3.0906 | -54.5073 | 2024-11-05 00:10:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 66.7 |
| 23c2d268-d565-3b34-8ca3-1c0941923331 | -3.5632 | -47.3629 | 2024-11-05 00:10:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 43501318-6de1-39df-8fed-1cefba64377f | -4.362 | -47.2397 | 2024-11-05 00:10:00 | GOES-16 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 42.3 |
| b662c671-b31a-3785-a1cd-c7fb54c3f167 | -3.4612 | -45.5299 | 2024-11-05 00:20:00 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 7f30b09a-e427-346c-957b-7caf092f1e5a | -3.5444 | -47.4073 | 2024-11-05 00:20:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 26536701-4c9b-3e2e-a18e-16add248fc01 | -2.8249 | -51.485 | 2024-11-05 00:20:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 42.1 |
| 1e0eca3c-aa3b-360c-a103-1aaa183687c5 | -3.5446 | -47.3855 | 2024-11-05 00:20:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 136.8 |
| 11c577a9-1e50-3a2c-b355-08e3df80575d | -4.8862 | -46.706 | 2024-11-05 00:20:00 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 52.5 |
| 19cf82a7-dd52-3ff1-a873-e1936fd67e01 | -2.8438 | -51.3603 | 2024-11-05 00:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 41.8 |


[Clique aqui para ver as próximas entradas](README2.md)
