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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8f267989-3480-3c28-9c14-8f470919159b | -12.1102 | -50.7857 | 2024-10-14 01:06:15 | GOES-16 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 93.4 |
| d24bae58-af67-3ee6-8921-870c72e43eab | -12.1106 | -50.7643 | 2024-10-14 01:06:15 | GOES-16 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 83.6 |
| feec4d18-208c-3bd1-aec7-0bc15ad261c7 | -12.4981 | -63.0148 | 2024-10-14 01:06:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 72.7 |
| d136686f-e75b-3955-891d-61e02e283749 | -12.4983 | -62.9956 | 2024-10-14 01:06:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 05606c9b-0f4c-3ce7-9e84-e449db1cd5bd | -12.517 | -63.0137 | 2024-10-14 01:06:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 911f09fb-d416-363b-a1e2-f083f50016a1 | -12.7687 | -62.3064 | 2024-10-14 01:06:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 73.3 |
| 93cd8c6e-d6fd-36fc-87d3-b10e2fc33e2f | -12.7688 | -62.2872 | 2024-10-14 01:06:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 125.7 |
| a86d8527-380e-31e6-a3b2-f95eda486406 | -12.8699 | -53.5423 | 2024-10-14 01:06:19 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 92.3 |
| e977f144-7bd1-3203-9c24-05b49711a238 | -12.8702 | -53.5215 | 2024-10-14 01:06:19 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 95.1 |
| 6fa85563-14af-3bbe-9bd8-5575756195c0 | -12.7878 | -62.286 | 2024-10-14 01:06:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 55.3 |
| d675c036-252d-3bc1-b9e8-cd499cbabb1b | -12.889 | -53.5402 | 2024-10-14 01:06:19 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 115.1 |
| f6069c92-ef76-31e1-9fab-ec8af40a86ee | -12.8893 | -53.5194 | 2024-10-14 01:06:19 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 99.7 |
| 8fc201cb-050c-364a-a7c0-e046d86a468e | -17.1267 | -56.8693 | 2024-10-14 01:06:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 53.2 |
| e50629cb-f339-326a-bb0e-efdcaa11a7f0 | -17.6471 | -56.3084 | 2024-10-14 01:06:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 80.9 |
| 05f21b9a-c3d6-3a79-ad61-79b2a1dbcbe6 | -17.6474 | -56.2876 | 2024-10-14 01:06:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 71.5 |
| a732a87c-7f61-3401-a689-5089572f6391 | -18.2375 | -56.418 | 2024-10-14 01:06:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 52.2 |
| aaba95eb-bfa5-3116-a685-3eea0267ba84 | -21.76 | -48.2851 | 2024-10-14 01:07:06 | GOES-16 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 110.8 |
| 1940b2af-5a47-3eb8-a247-b45dfffd217c | -22.28683 | -49.12369 | 2024-10-14 01:13:00 | TERRA_M-M | BAURU | SÃO PAULO | Brasil | 3506003 | 35 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 51161183-eb19-35eb-a91f-b5032daca52b | -22.28536 | -49.11372 | 2024-10-14 01:13:00 | TERRA_M-M | BAURU | SÃO PAULO | Brasil | 3506003 | 35 | 33 | nan | nan | nan | Cerrado | 21.9 |
| 49aeec99-9d81-3c0c-b156-c8a668347806 | -22.27632 | -49.11526 | 2024-10-14 01:13:00 | TERRA_M-M | BAURU | SÃO PAULO | Brasil | 3506003 | 35 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 05cfbfec-c1d8-3189-a588-5475abbb222f | -21.87692 | -48.9733 | 2024-10-14 01:13:00 | TERRA_M-M | IACANGA | SÃO PAULO | Brasil | 3519105 | 35 | 33 | nan | nan | nan | Mata Atlântica | 34.2 |
| b54395fb-6406-392e-90ea-726843255015 | -21.87542 | -48.96328 | 2024-10-14 01:13:00 | TERRA_M-M | IACANGA | SÃO PAULO | Brasil | 3519105 | 35 | 33 | nan | nan | nan | Mata Atlântica | 18.8 |
| 4f98d17c-a59b-3479-8139-17d074397a82 | -21.76522 | -48.30147 | 2024-10-14 01:13:00 | TERRA_M-M | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 75.8 |
| c9e6d605-3b3c-30d4-8e1c-51ec04588579 | -21.76356 | -48.29072 | 2024-10-14 01:13:00 | TERRA_M-M | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 123.9 |
| de9f1f26-c78e-3ffb-9545-6dbf8c0c473c | -21.75751 | -48.3138 | 2024-10-14 01:13:00 | TERRA_M-M | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 7.3 |
| bfb65779-2136-37c5-abc8-6b66c4edb11e | -21.75586 | -48.30318 | 2024-10-14 01:13:00 | TERRA_M-M | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 217.4 |
| f5d83e91-3701-35fe-a843-c27a0f5f7ebb | -21.75421 | -48.29252 | 2024-10-14 01:13:00 | TERRA_M-M | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 119.4 |
| 78c1c357-a662-3591-b4a8-0a1d2895bb0d | -21.55728 | -48.02652 | 2024-10-14 01:13:00 | TERRA_M-M | RINCÃO | SÃO PAULO | Brasil | 3543709 | 35 | 33 | nan | nan | nan | Cerrado | 8.7 |
| b11180f6-bc7f-3c16-a5ed-ff9a8498e9df | -21.55555 | -48.01541 | 2024-10-14 01:13:00 | TERRA_M-M | RINCÃO | SÃO PAULO | Brasil | 3543709 | 35 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 21bd59d4-daea-342d-9ca4-a3fe7ed3f1ef | -22.2944 | -49.11219 | 2024-10-14 01:13:00 | TERRA_M-M | BAURU | SÃO PAULO | Brasil | 3506003 | 35 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 4e058748-752a-3c09-a1a8-67a781eb9419 | -21.04702 | -48.62029 | 2024-10-14 01:15:00 | TERRA_M-M | PIRANGI | SÃO PAULO | Brasil | 3539004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.0 |
| e10144a3-ece1-3094-ba07-10304aeb8f80 | -20.31991 | -47.14805 | 2024-10-14 01:15:00 | TERRA_M-M | IBIRACI | MINAS GERAIS | Brasil | 3129707 | 31 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 3b1425ab-c3e4-3dd6-bf67-fca1cb537a76 | -20.31798 | -47.13609 | 2024-10-14 01:15:00 | TERRA_M-M | IBIRACI | MINAS GERAIS | Brasil | 3129707 | 31 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 2a33ee60-f06c-3c46-8779-0294567faaf0 | -18.59381 | -50.22567 | 2024-10-14 01:15:00 | TERRA_M-M | GOUVELÂNDIA | GOIÁS | Brasil | 5209150 | 52 | 33 | nan | nan | nan | Mata Atlântica | 14.8 |
| 1703c817-f7d2-32b4-9129-7151fb93bb17 | -18.24375 | -56.50166 | 2024-10-14 01:15:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 45.3 |
| 9d20a3d6-8f0f-399f-8608-24ef6ba735dc | -18.23239 | -56.5031 | 2024-10-14 01:15:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.9 |
| 96900dcf-3c7e-3437-90ad-7c56f51fdd17 | -18.02627 | -53.67881 | 2024-10-14 01:15:00 | TERRA_M-M | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 3d2daf50-c6e5-30c0-a495-ce54989bfad0 | -2.4344 | -46.9195 | 2024-10-14 01:15:20 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 78.8 |
| cebd0a01-db62-3de2-b086-29add56ecc4c | -2.4529 | -46.919 | 2024-10-14 01:15:20 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 24360a31-17a5-3863-acc0-50bdf2dd7cfe | -2.6117 | -49.1198 | 2024-10-14 01:15:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 37.4 |
| 652636ba-edd3-3761-a177-cf0720d44f1f | -2.6118 | -49.0985 | 2024-10-14 01:15:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 25.9 |
| ec731624-ac3a-3224-81b7-d44c631427d3 | -2.6052 | -57.5711 | 2024-10-14 01:15:21 | GOES-16 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 46.3 |
| a8f587e8-a594-3052-90c2-4b9ac548060e | -2.6302 | -49.1193 | 2024-10-14 01:15:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 28.7 |
| 77fcf4b3-42f0-3d80-884e-cf6fa6159541 | -3.0656 | -51.1883 | 2024-10-14 01:15:24 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 32.7 |
| 15b27962-fc32-3e16-9622-23237e22be6b | -3.289 | -42.8327 | 2024-10-14 01:15:25 | GOES-16 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 72.1 |
| 93211e37-531e-3c9e-b143-0fee8c16dbc9 | -3.3076 | -42.8553 | 2024-10-14 01:15:25 | GOES-16 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 162.1 |
| 97a1c994-e40b-37a1-83fa-23a70607b2b7 | -3.3077 | -42.8318 | 2024-10-14 01:15:25 | GOES-16 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 246.4 |
| 9a9fb762-0a7a-39d0-bdb6-e628ff6b2b14 | -4.1146 | -48.2731 | 2024-10-14 01:15:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 73.4 |
| 6fec1f47-e7b3-3ec4-b004-53f64cf39c88 | -4.3428 | -50.5172 | 2024-10-14 01:15:31 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 96.9 |
| 44fb8c90-ac67-3a23-af6b-ae95c36dc68e | -4.343 | -50.4962 | 2024-10-14 01:15:31 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 73.8 |
| 71646962-6cd1-3b40-9f15-c63cbd140b72 | -4.3613 | -50.5164 | 2024-10-14 01:15:31 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 61.1 |
| e1dd060d-5017-3e1b-823f-9b3becf39c44 | -4.3565 | -55.1291 | 2024-10-14 01:15:31 | GOES-16 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 45.9 |
| bdace6aa-5b72-3e69-97f6-1d4823036708 | -4.6197 | -44.8626 | 2024-10-14 01:15:32 | GOES-16 | IGARAPÉ GRANDE | MARANHÃO | Brasil | 2105203 | 21 | 33 | nan | nan | nan | Cerrado | 56.4 |
| afac365c-17c6-3f44-8aac-91773426e17b | -6.3749 | -59.9936 | 2024-10-14 01:15:43 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 50.3 |
| 32316120-acfa-35aa-bf97-f4d0e128bfd0 | -6.3933 | -59.9929 | 2024-10-14 01:15:43 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 51.1 |
| 05c00020-acb8-3e1f-b320-3219a4dcd883 | -7.9625 | -49.0607 | 2024-10-14 01:15:52 | GOES-16 | BERNARDO SAYÃO | TOCANTINS | Brasil | 1703206 | 17 | 33 | nan | nan | nan | Amazônia | 147.5 |
| a8e22601-bec7-3c66-aa0a-7d99f6ba15d9 | -7.9418 | -63.6365 | 2024-10-14 01:15:52 | GOES-16 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 57.6 |
| 60bc64c8-ad29-3dfd-8a0a-24ed63ee90d1 | -7.9419 | -63.6177 | 2024-10-14 01:15:52 | GOES-16 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 52.2 |
| 6c2a724c-228a-3285-b7a0-27ff2c93cab9 | -7.9603 | -63.6359 | 2024-10-14 01:15:52 | GOES-16 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 59.6 |
| a301526c-b07d-324d-814b-db24c512a6db | -7.9604 | -63.6171 | 2024-10-14 01:15:52 | GOES-16 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 54.1 |
| 48996cfa-166f-3409-85d3-9a43dbfbce24 | -8.4734 | -48.6276 | 2024-10-14 01:15:54 | GOES-16 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Amazônia | 78.3 |
| 6e321459-708b-3c7a-8208-4eedb632b028 | -9.1021 | -47.9355 | 2024-10-14 01:15:58 | GOES-16 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 84.6 |
| 97613c38-4080-35d4-a1b0-12b7d073a145 | -9.1042 | -61.1811 | 2024-10-14 01:15:59 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 70.5 |
| 8ec6acf5-d97a-33c4-9277-1be692d1558f | -9.1043 | -61.162 | 2024-10-14 01:15:59 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 87.3 |
| 9cdc8341-e748-3386-8b50-002a2eea1da9 | -9.6446 | -40.5847 | 2024-10-14 01:16:00 | GOES-16 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 64.5 |
| 32af44a2-43c7-3e87-ad17-58c8c130df00 | -9.4888 | -45.8228 | 2024-10-14 01:16:00 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 98.1 |
| d2d66410-2860-3a90-b830-8dd3f2ac6779 | -10.0622 | -44.2391 | 2024-10-14 01:16:03 | GOES-16 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 123.2 |
| ad664f17-e09a-3907-ad2c-fea22225d957 | -10.0626 | -44.2158 | 2024-10-14 01:16:03 | GOES-16 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 109.3 |
| 78e224d5-f117-319d-9d39-8806c94b932c | -10.0813 | -44.2366 | 2024-10-14 01:16:03 | GOES-16 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 174.4 |
| f6227d81-e9e2-315a-8811-9ff5cca9c256 | -10.0816 | -44.2133 | 2024-10-14 01:16:03 | GOES-16 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 132.3 |
| 14d3ea27-24d2-300d-ada0-058fc28939e6 | -9.9973 | -47.3329 | 2024-10-14 01:16:03 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 76.3 |
| 146f63cf-d7d0-3d21-92e0-10bdb01cea53 | -10.016 | -47.353 | 2024-10-14 01:16:03 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 87.8 |
| 3d421f3f-3554-3b96-9649-89db0bca9728 | -10.0163 | -47.3308 | 2024-10-14 01:16:03 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 173.2 |
| 6ef7bbb6-7bbf-336d-8430-b498b4f70c06 | -10.0166 | -47.3085 | 2024-10-14 01:16:03 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 98.9 |
| 2cdfc86f-257d-3c56-b3ad-d7a812bfbd7f | -10.0352 | -47.3286 | 2024-10-14 01:16:03 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 119.5 |
| 8928cd30-4fb1-3239-8b30-40926d679a91 | -10.4918 | -42.433 | 2024-10-14 01:16:05 | GOES-16 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 103.7 |
| 6b49557b-d381-3273-a081-806df8549551 | -10.5307 | -49.7843 | 2024-10-14 01:16:06 | GOES-16 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 114.1 |
| 138bd742-ca1d-3836-b058-5350d011aa83 | -11.17 | -39.9192 | 2024-10-14 01:16:09 | GOES-16 | QUEIMADAS | BAHIA | Brasil | 2925808 | 29 | 33 | nan | nan | nan | Caatinga | 76.6 |
| 33b18c38-1c16-3c24-926b-86b0f4bf082a | -11.1705 | -39.894 | 2024-10-14 01:16:09 | GOES-16 | QUEIMADAS | BAHIA | Brasil | 2925808 | 29 | 33 | nan | nan | nan | Caatinga | 113.1 |
| 18176fd5-5350-34df-bba4-00cf00e153d1 | -11.1893 | -39.9159 | 2024-10-14 01:16:09 | GOES-16 | QUEIMADAS | BAHIA | Brasil | 2925808 | 29 | 33 | nan | nan | nan | Caatinga | 71.2 |
| 3555be9d-4f13-3062-babf-884e271e14e0 | -11.1898 | -39.8906 | 2024-10-14 01:16:09 | GOES-16 | QUEIMADAS | BAHIA | Brasil | 2925808 | 29 | 33 | nan | nan | nan | Caatinga | 105.9 |
| adf76e3d-1fc9-33ad-8190-ec3c8d77e597 | -12.1306 | -50.6978 | 2024-10-14 01:16:15 | GOES-16 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 83.8 |
| e7b5f5a6-6ef3-31d4-b01f-23df616a4daa | -12.1497 | -50.6956 | 2024-10-14 01:16:15 | GOES-16 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 63.2 |
| b46e1251-2327-37a3-845f-818f0cefcc75 | -12.1688 | -50.6933 | 2024-10-14 01:16:15 | GOES-16 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 62.2 |
| 27310097-5ad3-318f-9b17-83b515b406d8 | -12.3807 | -53.1167 | 2024-10-14 01:16:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 60.6 |
| d3ca508d-2b50-35b7-bf31-cf86630d723e | -12.3997 | -53.1147 | 2024-10-14 01:16:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 92.7 |
| 18841862-98d4-3ce5-88f8-f169fd9907c0 | -12.4981 | -63.0148 | 2024-10-14 01:16:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 83.0 |
| 229daf11-fd9f-3c68-aeac-6f72bd0ee98f | -12.4983 | -62.9956 | 2024-10-14 01:16:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 62.5 |
| ff1151ea-efa4-32a4-8a95-19b47fc5ac00 | -12.517 | -63.0137 | 2024-10-14 01:16:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 3867c5e2-cea7-3ee3-87e4-ddb5fe6ddffc | -12.7688 | -62.2872 | 2024-10-14 01:16:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 92.0 |
| b9fc47c2-7636-3847-afae-7c91b9788e77 | -12.8699 | -53.5423 | 2024-10-14 01:16:19 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 74.3 |
| 5b69bd95-a99f-38e8-bac2-5ae589abeb58 | -12.8702 | -53.5215 | 2024-10-14 01:16:19 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 55.9 |
| 173d6f62-4e31-37cf-a6e4-f12a9c999c61 | -12.889 | -53.5402 | 2024-10-14 01:16:19 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 107.2 |
| 62e439a9-2e52-341e-8733-1ed4f11c6f71 | -12.8893 | -53.5194 | 2024-10-14 01:16:19 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 79.3 |
| 795450e9-5726-3df7-822e-c4866b2cedb5 | -17.0823 | -56.0076 | 2024-10-14 01:16:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 72.8 |
| 818103ed-da97-328d-9f18-6cb9d571e706 | -17.1267 | -56.8693 | 2024-10-14 01:16:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 50.5 |
| fbfbb1b0-df50-34cc-a139-2c48ea58b0bb | -17.6471 | -56.3084 | 2024-10-14 01:16:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 66.2 |
| 8d95a6a7-63f2-320a-b7b9-32fba717e6fd | -17.6474 | -56.2876 | 2024-10-14 01:16:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 64.2 |
| 90b0f434-2dc5-361f-ae24-a1c192a86162 | -17.6668 | -56.3059 | 2024-10-14 01:16:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 56.1 |
| 87981cc7-2c46-3362-868e-d2258c1945ee | -17.6876 | -56.2409 | 2024-10-14 01:16:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 57.0 |


[Clique aqui para ver as próximas entradas](README17.md)
