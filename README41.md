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

## Dados Diários - Página 41

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 48c6824b-76db-39a6-955e-933d535b0aa2 | -18.10921 | -44.38211 | 2026-09-28 04:36:00 | NOAA-21 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 76ee75a6-d5fd-3b55-87ed-ae7ecd0a5292 | -15.13901 | -43.62238 | 2026-09-28 04:36:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 33699729-db3d-3a15-a33c-ce4037c1a85c | -14.80032 | -45.95691 | 2026-09-28 04:36:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c11d9908-02c4-3ece-bf44-1496031e28a3 | -15.17788 | -46.16387 | 2026-09-28 04:36:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 6.7 |
| fbea72c7-c55c-3e5b-8865-aa2fcfbe7b19 | -15.05862 | -47.23038 | 2026-09-28 04:36:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| fef45a40-3000-3672-b178-2c9bfa4cc4b6 | -15.22678 | -46.35811 | 2026-09-28 04:36:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b3b2c382-6f63-39ed-b1b3-54dfadc42b4e | -15.16791 | -46.15307 | 2026-09-28 04:36:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d2039530-e05f-302f-a0b4-0f161f521dc3 | -15.14338 | -43.62302 | 2026-09-28 04:36:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 1ba7ef1f-24b1-3e43-9ab3-2aca9f4ce834 | -13.72123 | -48.81749 | 2026-09-28 04:36:00 | NOAA-21 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 2ff394f0-db63-30ad-a3d4-90c2ebeead5e | -13.72177 | -48.81394 | 2026-09-28 04:36:00 | NOAA-21 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 5f274ad6-7e6e-3597-b50f-1dc25e9011c7 | -16.13388 | -49.50983 | 2026-09-28 04:36:00 | NOAA-21 | ITAUÇU | GOIÁS | Brasil | 5211404 | 52 | 33 | nan | nan | nan | Cerrado | 30.2 |
| f55b94fc-aa1e-324c-ac0c-a3ee9d12611c | -18.10432 | -44.38605 | 2026-09-28 04:36:00 | NOAA-21 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 07e2c1bb-9aa2-37e1-a36f-10bfb8963247 | -13.70738 | -48.81894 | 2026-09-28 04:36:00 | NOAA-21 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 58cd79f9-e6cf-39d7-b6e3-9f67fdb929e4 | -16.32234 | -46.55195 | 2026-09-28 04:36:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 491ea155-f8e7-3201-b7a0-ea24a64b0114 | -15.4731 | -46.14567 | 2026-09-28 04:36:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 840df2f3-7c48-3297-a3b2-f3f411a42895 | -15.58055 | -47.90355 | 2026-09-28 04:36:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5d09a00f-463f-3aad-8943-977bcf2d9f8f | -16.20412 | -42.87442 | 2026-09-28 04:36:00 | NOAA-21 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ee8f568a-a3ca-34f8-bc2f-635a8bcbda27 | -13.47002 | -48.59393 | 2026-09-28 04:36:00 | NOAA-21 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b051be5b-fafa-3844-8892-d0d7780c13ff | -13.34263 | -51.32617 | 2026-09-28 04:36:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6066a29c-be2a-391a-a9e5-5c2c7531d4af | -14.72522 | -45.57218 | 2026-09-28 04:36:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| d5750f6b-0b5e-3186-bfc0-e1d2aca30b3a | -15.68691 | -42.6786 | 2026-09-28 04:36:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 01f64e63-2be5-36a8-a679-a7be671f5e92 | -16.13776 | -49.50676 | 2026-09-28 04:36:00 | NOAA-21 | ITAUÇU | GOIÁS | Brasil | 5211404 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 2ea66a51-9a98-3efa-bfbd-e2cb3e8e19b2 | -18.18625 | -51.78103 | 2026-09-28 04:36:00 | NOAA-21 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6cbab1e5-e346-3d34-b0c4-3c5f3af64f6b | -15.17599 | -46.14979 | 2026-09-28 04:36:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 324b755b-5da4-3f32-a247-59c0014cb665 | -15.51191 | -45.40123 | 2026-09-28 04:36:00 | NOAA-21 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 77c3611a-9a78-32ce-b0f6-f6df2573a06f | -19.52382 | -46.0081 | 2026-09-28 04:36:00 | NOAA-21 | SANTA ROSA DA SERRA | MINAS GERAIS | Brasil | 3159704 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| fddf59eb-1e66-330d-b8c0-1cec093268a8 | -13.46947 | -48.59752 | 2026-09-28 04:36:00 | NOAA-21 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| bc022e67-74f2-386f-b621-9eb541cd995c | -15.08986 | -54.61527 | 2026-09-28 04:36:00 | NOAA-21 | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 03c93ad7-d99e-383a-b30c-04db1c37659b | -18.09998 | -44.38556 | 2026-09-28 04:36:00 | NOAA-21 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1d2c3c86-0f09-309f-b699-cd3af6ffae4c | -14.48702 | -48.33688 | 2026-09-28 04:36:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 38faeb7b-f5d8-3bc6-9d27-29a397f092c7 | -19.14818 | -43.83046 | 2026-09-28 04:36:00 | NOAA-21 | BALDIM | MINAS GERAIS | Brasil | 3105004 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 9cd40dd7-bb3f-3509-bc43-0cfe208b7f4c | -18.75941 | -44.40654 | 2026-09-28 04:36:00 | NOAA-21 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 86430e08-9409-39f7-a5a2-2e0f95791a4e | -18.10589 | -44.37297 | 2026-09-28 04:36:00 | NOAA-21 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| adfffb18-fe5d-3652-9705-04a4788b24c2 | -16.3641 | -52.41003 | 2026-09-28 04:36:00 | NOAA-21 | BALIZA | GOIÁS | Brasil | 5203104 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9ac8ed65-73e7-3e86-a90a-0abf69ee7fbd | -15.30819 | -46.9217 | 2026-09-28 04:36:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cbf14dfc-b9f0-39f8-945a-02ebfea671e1 | -12.90296 | -52.05472 | 2026-09-28 04:36:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f998b66b-ae31-3770-9815-a335b298a35b | -15.40726 | -47.91821 | 2026-09-28 04:36:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| ec54aee9-e00e-333b-ad6f-7677036880bd | -13.71736 | -48.82053 | 2026-09-28 04:36:00 | NOAA-21 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d1403cae-5c78-3166-af07-18ab0fa50785 | -15.57766 | -47.89917 | 2026-09-28 04:36:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 60b43450-4176-3b1b-a40c-554cab503266 | -13.69631 | -48.82448 | 2026-09-28 04:36:00 | NOAA-21 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b6912c49-1051-3205-87d1-a9d69b29af9f | -14.48215 | -53.63223 | 2026-09-28 04:36:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 224cc48c-ccc6-3f87-87f3-350c286097e5 | -14.51454 | -48.31472 | 2026-09-28 04:36:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fb0d3b1f-fa7b-3adc-8d1a-1e02fffb651e | -14.19177 | -44.36951 | 2026-09-28 04:36:00 | NOAA-21 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 3355ceb9-4d23-30b4-93d3-91ae65697137 | -15.15764 | -43.61619 | 2026-09-28 04:36:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 52cbb8df-11fc-3320-8bbf-310a9569dc22 | -14.49993 | -48.31993 | 2026-09-28 04:36:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8b4a2c9f-c0ae-3479-bf51-85e352ab5123 | -13.53291 | -52.91537 | 2026-09-28 04:36:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1b24fcbb-0c36-378a-aac5-b03c8598a87e | -15.17536 | -46.15441 | 2026-09-28 04:36:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 244fe794-1323-366b-a646-68792bf80dee | -18.11024 | -44.37347 | 2026-09-28 04:36:00 | NOAA-21 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| bf7709d7-04ee-3ad8-a6d4-22c9d92ebfa6 | -13.71349 | -48.82359 | 2026-09-28 04:36:00 | NOAA-21 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 986d5135-e907-3cad-a2d7-de73f66790c7 | -15.15159 | -43.62856 | 2026-09-28 04:36:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 6f2f50fb-df02-3eb5-8de8-52c6545b5ced | -15.15495 | -43.60244 | 2026-09-28 04:36:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 2.3 |
| bdf91b0d-0ac1-3a3f-8a9a-b07daafe30cd | -17.8329 | -44.40015 | 2026-09-28 04:36:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0cb95fe9-deaa-37e7-ba4b-47b7806c8851 | -19.15271 | -43.83132 | 2026-09-28 04:36:00 | NOAA-21 | BALDIM | MINAS GERAIS | Brasil | 3105004 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 0a56560c-68be-33a3-b826-ef4436ec3d6c | -13.69515 | -48.80968 | 2026-09-28 04:36:00 | NOAA-21 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| afc0ee5d-623d-3a2a-aa0a-4a65da66531e | -13.46613 | -48.59703 | 2026-09-28 04:36:00 | NOAA-21 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 4a4d50cd-9eca-3e7c-9650-45c833bb3eb1 | -13.46668 | -48.59344 | 2026-09-28 04:36:00 | NOAA-21 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3442bb8d-1cad-342e-822e-db0aaa48a2c2 | -14.59822 | -45.59624 | 2026-09-28 04:36:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 163ae563-3720-3fef-a119-70b91fed9714 | -15.40958 | -47.92641 | 2026-09-28 04:36:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |
| ef0cf0ed-7909-31e2-9ecf-b0fc8a4ee731 | -13.71681 | -48.82411 | 2026-09-28 04:36:00 | NOAA-21 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| db732801-6a3d-3f2f-8129-316fef422e5b | -15.15326 | -43.61559 | 2026-09-28 04:36:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 717b1e3d-4080-35df-a55f-0415db95422b | -16.13721 | -49.51038 | 2026-09-28 04:36:00 | NOAA-21 | ITAUÇU | GOIÁS | Brasil | 5211404 | 52 | 33 | nan | nan | nan | Cerrado | 30.2 |
| 63ebfc34-ac69-3e78-9381-becf1d4f38a8 | -14.08958 | -46.3179 | 2026-09-28 04:36:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9e82750b-1d5e-3b06-a88c-2889167940c5 | -17.83908 | -46.55451 | 2026-09-28 04:36:00 | NOAA-21 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 302e23c8-867d-331c-81db-5cf3762f4951 | -15.65465 | -52.67987 | 2026-09-28 04:36:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9038c167-fd3f-3f0b-a5ea-2e6739b09af4 | -13.45946 | -48.59599 | 2026-09-28 04:36:00 | NOAA-21 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 64f8b97a-ff61-3bd5-881f-47b43b449e1b | -17.8372 | -44.40089 | 2026-09-28 04:36:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cc8854b9-bb2a-3311-9afc-b5acd976f719 | -13.46 | -48.59238 | 2026-09-28 04:36:00 | NOAA-21 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a6c21176-8f90-39ff-89dd-f1a7ab5491a0 | -14.5151 | -48.31104 | 2026-09-28 04:36:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c9ba4412-6dc4-30da-bd29-372250183e91 | -17.68904 | -47.99068 | 2026-09-28 04:36:00 | NOAA-21 | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 32869826-9af0-3b3f-b01d-d1a9e1361f6b | -13.46838 | -48.60469 | 2026-09-28 04:36:00 | NOAA-21 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b6a84ddb-a2d1-3221-998f-1b2199bdddd7 | -19.07124 | -46.7184 | 2026-09-28 04:36:00 | NOAA-21 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 07486764-4c3b-3abf-a036-4c47672fc208 | -15.16161 | -43.58553 | 2026-09-28 04:36:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 9ce06015-2fc9-3511-bcc7-3ae24f5afa8c | -13.92494 | -47.85254 | 2026-09-28 04:36:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6a4d1b19-23a2-3f8e-92a1-bf1e3be15b35 | -13.68386 | -48.81908 | 2026-09-28 04:36:00 | NOAA-21 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 5434df86-1431-375d-b251-760f69ca6a9a | -15.16104 | -43.58991 | 2026-09-28 04:36:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 9633d340-86d1-3cd2-b3b8-0705c026b951 | -14.72587 | -45.56733 | 2026-09-28 04:36:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f2079c5f-b615-310f-bf2e-a3eb6c24d285 | -18.10485 | -44.38165 | 2026-09-28 04:36:00 | NOAA-21 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b6c4c32b-d03e-3606-b1f5-e5b249c2d11c | -18.55223 | -43.58408 | 2026-09-28 04:36:00 | NOAA-21 | PRESIDENTE KUBITSCHEK | MINAS GERAIS | Brasil | 3153301 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 730eee63-ba19-33f9-acee-cfd7ea35f854 | -14.48585 | -53.63279 | 2026-09-28 04:36:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2e08557f-f294-3228-b187-38f6771e9951 | -15.19432 | -48.43844 | 2026-09-28 04:36:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a5946768-03af-3fcd-bddb-9bb805371253 | -15.16483 | -46.14765 | 2026-09-28 04:36:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1159efc3-2a14-3521-ac04-da8542c01a5b | -15.5605 | -47.92032 | 2026-09-28 04:36:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8d814afa-1a31-3abc-a3b7-092fba443437 | -18.1005 | -44.38119 | 2026-09-28 04:36:00 | NOAA-21 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9d545fe2-d5a4-3f16-98fe-4b948b54563e | -18.11843 | -44.37878 | 2026-09-28 04:36:00 | NOAA-21 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9cf900c8-c471-34d8-bcaa-9a684ea05aa5 | -12.90447 | -52.0672 | 2026-09-28 04:36:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7d09e85f-509d-32b1-8e38-cb6fb58e6330 | -15.1915 | -48.43411 | 2026-09-28 04:36:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a8ba7b34-8db1-3d7c-bffd-132f24f2d91d | -14.79345 | -45.95108 | 2026-09-28 04:36:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 83ef6ce1-6776-32cf-877a-bee1a17dabc6 | -14.51848 | -48.31158 | 2026-09-28 04:36:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 64f6fd66-f617-3538-8fce-4afcff567d68 | -13.45613 | -48.59541 | 2026-09-28 04:36:00 | NOAA-21 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0219cc5f-4601-3417-ada3-c5b2393e138f | -16.3928 | -42.56398 | 2026-09-28 04:36:00 | NOAA-21 | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| cad5712a-f8ea-360d-be7a-c5aae262a4ee | -15.413 | -47.90299 | 2026-09-28 04:36:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 614dc39c-7de0-3e14-938a-6d366223ba37 | -18.12386 | -44.37031 | 2026-09-28 04:36:00 | NOAA-21 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f7c0c251-b947-3af6-bb86-1921d096d483 | -18.10868 | -44.38648 | 2026-09-28 04:36:00 | NOAA-21 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| bbd0ed1a-cad8-30ba-9502-aa1bf7f5b6a1 | -13.68774 | -48.81604 | 2026-09-28 04:36:00 | NOAA-21 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 74f4fa90-2811-317e-b5e6-db37853dbf5b | -15.17226 | -46.14912 | 2026-09-28 04:36:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 653c6a75-eb26-36c2-a12b-fb019be4af54 | -13.47281 | -48.59803 | 2026-09-28 04:36:00 | NOAA-21 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 53515e5f-30da-3dfe-8bbc-65310de4aad7 | -13.45667 | -48.59181 | 2026-09-28 04:36:00 | NOAA-21 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 68e69f14-6933-37f9-a95f-827b13533068 | -15.99736 | -47.73839 | 2026-09-28 04:36:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9e45f259-70a4-3472-9ad8-a32985ee8b23 | -13.6902 | -48.81984 | 2026-09-28 04:36:00 | NOAA-21 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2f79123e-00a5-30ff-aa82-0c9a2fd82fef | -15.34488 | -42.16898 | 2026-09-28 04:36:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.8 |


[Clique aqui para ver as próximas entradas](README42.md)
