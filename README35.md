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

## Dados Diários - Página 35

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2842b6d7-8040-349d-b1eb-a5242d1e31e2 | -9.4244 | -67.2313 | 2024-10-03 01:26:00 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 38.3 |
| 8ef6734a-33ea-33a5-a82c-41520aa48c09 | -9.4368 | -64.5419 | 2024-10-03 01:26:00 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 80.1 |
| d5c85b28-3593-3933-849e-44b3ba619fea | -9.468 | -62.3857 | 2024-10-03 01:26:00 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 46e6e5db-d650-3e8a-8832-cb14cbd52f6f | -9.4865 | -62.4039 | 2024-10-03 01:26:00 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 66.6 |
| c6b224f7-f6b6-35d4-b2a1-0b31e743b410 | -9.4866 | -62.3849 | 2024-10-03 01:26:00 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 93.5 |
| c084e521-ebf8-3df9-86a9-d3dd22a0a262 | -9.4939 | -68.508 | 2024-10-03 01:26:01 | GOES-16 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 50.4 |
| bb3f006a-ed89-39a7-bb76-f8f7b56b42cb | -9.494 | -68.4895 | 2024-10-03 01:26:01 | GOES-16 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 67.2 |
| 7b33f96b-269b-355b-bf9b-84cac6e102a2 | -9.7173 | -64.2302 | 2024-10-03 01:26:02 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 51.2 |
| c05edd3e-d636-3880-a803-f5f8d1361f07 | -9.9129 | -60.0807 | 2024-10-03 01:26:03 | GOES-16 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 71c467e8-2ec2-3b7b-9a6d-0eb156cc8ae3 | -10.1802 | -57.2848 | 2024-10-03 01:26:04 | GOES-16 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 0aacfdaa-07b5-3917-85fe-d1cd2e764d6c | -10.3319 | -67.9868 | 2024-10-03 01:26:05 | GOES-16 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 49.0 |
| 57c80f03-ce52-3902-b310-a3654e92f6a9 | -10.3319 | -67.9682 | 2024-10-03 01:26:05 | GOES-16 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 4832bcb0-042e-3135-8544-2497b5c9f1d6 | -10.8942 | -63.8971 | 2024-10-03 01:26:08 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 53.9 |
| dff7e56a-f39a-3dd5-9b6f-04f0523daed4 | -11.6742 | -65.0172 | 2024-10-03 01:26:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 104df495-a9f1-3e1e-806d-d1b560d00fc2 | -12.4038 | -63.0009 | 2024-10-03 01:26:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 90.2 |
| 97ba7cca-3fca-34d7-a61b-c8c45f8b8191 | -12.404 | -62.9817 | 2024-10-03 01:26:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 85.8 |
| 2ae98fe8-dfb6-3477-8428-3008d7d88912 | -12.5332 | -53.1003 | 2024-10-03 01:26:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 73.8 |
| a88ab715-e598-3782-b70b-76853f1953d9 | -12.6484 | -63.1214 | 2024-10-03 01:26:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 76.1 |
| c6a7e7a8-7afa-3b51-8da5-86e4789bc725 | -12.6486 | -63.1022 | 2024-10-03 01:26:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 58.6 |
| dde2724e-33f1-321d-ab69-af5d02078139 | -12.8049 | -62.497 | 2024-10-03 01:26:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 72.7 |
| 81b8e743-2ce0-3962-9181-7ee797b1f821 | -12.8802 | -62.5503 | 2024-10-03 01:26:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 109.2 |
| 4afe9f06-d948-365e-8aeb-0c168d8d63f0 | -12.8803 | -62.531 | 2024-10-03 01:26:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 67.1 |
| ca4bbc51-c4b7-37fe-afc9-40545440fe83 | -12.8808 | -62.4731 | 2024-10-03 01:26:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 89.6 |
| 3cb6aea5-8d77-3f91-8bbb-e8384f3418ef | -12.881 | -62.4538 | 2024-10-03 01:26:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 93.7 |
| 9a0d2280-ba6f-34a0-bd6c-d81e1eb60ebb | -12.8991 | -62.5491 | 2024-10-03 01:26:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 98.7 |
| 6feaa5a4-9c87-31ab-909d-27c64b2be0c3 | -12.8993 | -62.5298 | 2024-10-03 01:26:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 69.1 |
| a45c5557-8306-3fcc-97c7-55918aaf7e54 | -12.8996 | -62.4913 | 2024-10-03 01:26:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 118.1 |
| cadbdb3e-8610-3e1a-878c-acadf25c0219 | -12.8998 | -62.472 | 2024-10-03 01:26:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 145.7 |
| a70e00c5-be43-398c-9644-f76236f57513 | -12.8999 | -62.4527 | 2024-10-03 01:26:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 88.1 |
| 8c1424f8-e7c8-3a17-84e1-90f0a810c6ef | -12.9167 | -62.7022 | 2024-10-03 01:26:20 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 75.7 |
| 18ff19b5-ba51-3be5-a4b1-03c5a2e63051 | -12.9187 | -62.4708 | 2024-10-03 01:26:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 68.6 |
| d9264a4d-0ea2-3c18-8c45-c4f00dad2f1e | -12.9741 | -62.6409 | 2024-10-03 01:26:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 72.7 |
| 9994f751-878c-3d1c-bb95-9110e0744d76 | -13.5184 | -51.211 | 2024-10-03 01:26:22 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 70.7 |
| dd9bc261-c6e3-33d6-a365-df75cd8f2026 | -13.5195 | -51.1467 | 2024-10-03 01:26:22 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 91.6 |
| 7eae8cd2-9e71-341d-80eb-1ab738a0c2f2 | -13.5198 | -51.1252 | 2024-10-03 01:26:22 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 79.3 |
| 617a53dc-5343-317b-b274-b0ce7e01aee7 | -13.5558 | -51.2704 | 2024-10-03 01:26:22 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 140.6 |
| 521a0a1f-c3de-340c-b6d2-441d6136be5f | -13.5562 | -51.2489 | 2024-10-03 01:26:22 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 228.6 |
| cbbc1850-0788-3091-89a2-1506dede1d76 | -13.5754 | -51.2464 | 2024-10-03 01:26:22 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 98.6 |
| 02e1f6ac-a8b6-3964-a2dc-c49e4d0aa958 | -14.5225 | -45.218 | 2024-10-03 01:26:27 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 53.7 |
| ebc67b36-350e-3d72-b173-7a156b9514d5 | -16.7455 | -57.4674 | 2024-10-03 01:26:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 71.9 |
| e0231f56-ad4a-3954-87ae-93792a34d47b | -16.7647 | -57.4856 | 2024-10-03 01:26:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 70.4 |
| 03dd5e31-0a20-364f-ad7f-63ecaae0c31d | -16.765 | -57.4652 | 2024-10-03 01:26:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 158.3 |
| 07200c8a-5976-3c11-9ed4-dd2eb7b50541 | -16.7654 | -57.4447 | 2024-10-03 01:26:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 85.1 |
| fb8579d9-4ec3-3c73-a32e-75795b17f67f | -19.0344 | -43.1944 | 2024-10-03 01:26:51 | GOES-16 | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 80.5 |
| dbac1a05-9d29-3001-8bcd-64ee1cf046f5 | -19.2962 | -42.5779 | 2024-10-03 01:26:52 | GOES-16 | MESQUITA | MINAS GERAIS | Brasil | 3141702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 76.8 |
| 59c205af-e2d5-33e7-b28d-ab7f55937735 | -19.5104 | -42.8691 | 2024-10-03 01:26:53 | GOES-16 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 64.0 |
| d9936abb-f0d3-3124-a25e-7d7363df6e46 | -21.3868 | -47.6734 | 2024-10-03 01:27:04 | GOES-16 | SÃO SIMÃO | SÃO PAULO | Brasil | 3550902 | 35 | 33 | nan | nan | nan | Cerrado | 144.9 |
| 9f959027-d6ba-33f3-b537-758d09565b12 | -21.3875 | -47.6497 | 2024-10-03 01:27:04 | GOES-16 | SÃO SIMÃO | SÃO PAULO | Brasil | 3550902 | 35 | 33 | nan | nan | nan | Cerrado | 86.0 |
| f4b38d49-0ebb-33ef-b84d-e4368528373d | -21.346 | -55.6626 | 2024-10-03 01:27:04 | GOES-16 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 97.2 |
| 2619e688-0030-36c9-80e5-346f522b2278 | -22.3094 | -44.0633 | 2024-10-03 01:27:08 | GOES-16 | VALENÇA | RIO DE JANEIRO | Brasil | 3306107 | 33 | 33 | nan | nan | nan | Mata Atlântica | 99.9 |
| 99c304b2-0a91-350b-9499-3f3799fe9814 | -22.3711 | -47.9225 | 2024-10-03 01:27:09 | GOES-16 | ITIRAPINA | SÃO PAULO | Brasil | 3523602 | 35 | 33 | nan | nan | nan | Cerrado | 72.0 |
| 660767e3-1af9-39be-8f11-d68b6c6827ce | -22.4452 | -46.8817 | 2024-10-03 01:27:09 | GOES-16 | MOGI MIRIM | SÃO PAULO | Brasil | 3530805 | 35 | 33 | nan | nan | nan | Cerrado | 102.2 |
| ac8c76aa-4d8b-3c17-ad37-5e72d669a606 | -22.446 | -46.8576 | 2024-10-03 01:27:09 | GOES-16 | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Cerrado | 133.4 |
| cd384e56-330a-3f99-ae88-912170308ac6 | -2.9616 | -54.6503 | 2024-10-03 01:35:23 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 69.8 |
| 68899e26-ce9b-39f5-b05e-9369f6e1b688 | -3.3854 | -42.2866 | 2024-10-03 01:35:25 | GOES-16 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 45.4 |
| b0631995-9100-31c7-b3e0-e81106cfdc27 | -3.3855 | -42.263 | 2024-10-03 01:35:25 | GOES-16 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 35.2 |
| ed4426bb-c4f5-3c30-a623-e96361cdc87c | -3.404 | -42.2858 | 2024-10-03 01:35:25 | GOES-16 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 169.5 |
| abfa164a-08c3-3fb4-ae24-a24037ee28b7 | -3.4042 | -42.2621 | 2024-10-03 01:35:25 | GOES-16 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 120.6 |
| 170c0087-5c57-3b34-9df4-9a4cf909424c | -3.4227 | -42.2849 | 2024-10-03 01:35:25 | GOES-16 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 33.6 |
| 7e23d61c-c7b4-3b30-8e41-ef8cb82ab7d3 | -3.4229 | -42.2612 | 2024-10-03 01:35:25 | GOES-16 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 37.4 |
| 9a16e951-c5cd-3b56-88bb-e42fdd97ec84 | -4.0949 | -48.4894 | 2024-10-03 01:35:29 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 72.8 |
| 72b2f29a-82bd-3477-a0c1-37a8f29039b6 | -4.095 | -48.4679 | 2024-10-03 01:35:29 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 86.3 |
| c23bd4e3-c27d-34c4-a4af-838f8406f79a | -4.1134 | -48.4886 | 2024-10-03 01:35:29 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 51.1 |
| 9a4cbfaa-fdcf-3ae7-99f3-f72aff266166 | -4.5373 | -43.3273 | 2024-10-03 01:35:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 55.8 |
| d7a07179-dbcc-3deb-bbb5-6e1a16117b1d | -4.5375 | -43.304 | 2024-10-03 01:35:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 104.8 |
| 3fca7fad-03ff-3339-b4de-a86b6394404b | -4.5562 | -43.3028 | 2024-10-03 01:35:32 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 61.2 |
| 006a4ee8-b409-30f1-9dc9-b7fe288f1107 | -4.9264 | -43.79 | 2024-10-03 01:35:34 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 94.8 |
| efee05d8-1222-3ba2-93a1-f43407bac839 | -4.9265 | -43.7669 | 2024-10-03 01:35:34 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 94.0 |
| d2ad2282-90e1-3be8-9145-f43b1dd68bb9 | -4.9451 | -43.7888 | 2024-10-03 01:35:34 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 68.8 |
| d802fe3b-e7fc-3cb0-a40c-9dfff046745a | -4.9452 | -43.7657 | 2024-10-03 01:35:34 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 66.5 |
| 60c5220d-f366-354a-9f3b-044df8060481 | -5.2441 | -43.8151 | 2024-10-03 01:35:35 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 81.2 |
| 5ad523c5-9e8e-3f27-936e-2462979b2fa0 | -5.2443 | -43.792 | 2024-10-03 01:35:35 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 77.8 |
| d64734f1-5f3a-3c1e-ac22-15d5f374602e | -5.8547 | -44.5988 | 2024-10-03 01:35:39 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 54.4 |
| 2dbe5036-f011-3ccb-b07f-32a02399c12f | -6.8777 | -59.0504 | 2024-10-03 01:35:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 10f0fb28-6c98-33f9-8c7e-bae19fa21330 | -6.8778 | -59.031 | 2024-10-03 01:35:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 49.2 |
| f367220d-639a-3c2f-95f7-de2d250b8ad7 | -8.8503 | -45.5313 | 2024-10-03 01:35:56 | GOES-16 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 27.9 |
| a67da20c-52cb-38ee-8dd2-0566ed6ee5a5 | -8.8506 | -45.5086 | 2024-10-03 01:35:56 | GOES-16 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 88.7 |
| 8c9f2752-3c35-36df-a81a-697a62ab16c5 | -8.8695 | -45.5066 | 2024-10-03 01:35:56 | GOES-16 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 35.5 |
| d8cdf361-c164-3acd-ae6d-220eb2fc021d | -8.8926 | -62.3348 | 2024-10-03 01:35:57 | GOES-16 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 55.9 |
| 97474dc1-3891-37cb-a0f5-0e03537244da | -8.9791 | -67.4099 | 2024-10-03 01:35:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 50.5 |
| c64657cf-d740-34ba-9c64-c834a90d460e | -9.0149 | -67.7423 | 2024-10-03 01:35:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 73.9 |
| 395b72ab-ce29-30ff-98d1-13216bd0255f | -9.0515 | -67.871 | 2024-10-03 01:35:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 76175132-04e2-3277-b2df-5cd9591c9a94 | -9.1566 | -61.6758 | 2024-10-03 01:35:58 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 84.4 |
| 73bf9603-283b-3d22-83ab-1f3c9eb412a8 | -9.4574 | -40.3641 | 2024-10-03 01:35:59 | GOES-16 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 112.7 |
| 85aecfeb-229a-38b1-a098-ad552c41f03b | -9.1752 | -61.6749 | 2024-10-03 01:35:59 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 66.4 |
| 5eaa9766-5d52-3d6f-a444-bf243de0c9b6 | -9.3839 | -61.0526 | 2024-10-03 01:36:00 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 79.3 |
| a1270224-0274-3bc4-a10b-0cb99ed48075 | -9.4368 | -64.5419 | 2024-10-03 01:36:00 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 49.5 |
| 38175002-987b-3d14-acbb-f23068e41620 | -9.4939 | -68.508 | 2024-10-03 01:36:01 | GOES-16 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 41.6 |
| d3923585-e28e-3936-9a44-7622f6aca5d7 | -9.494 | -68.4895 | 2024-10-03 01:36:01 | GOES-16 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 57.8 |
| ebd22ace-884b-34c6-add6-8c539e4bf1af | -9.7173 | -64.2302 | 2024-10-03 01:36:02 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 45.0 |
| 8c1908e9-1748-361a-b857-d3bca4a085bf | -9.9129 | -60.0807 | 2024-10-03 01:36:03 | GOES-16 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 50.3 |
| 5e844951-c3f2-3639-8e21-24c75c591da8 | -10.1615 | -57.2861 | 2024-10-03 01:36:04 | GOES-16 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 55.5 |
| fe6eab84-59af-30b1-9cf1-5bbdc6508720 | -10.1617 | -57.2663 | 2024-10-03 01:36:04 | GOES-16 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 55.4 |
| 407e22a1-5061-3b31-b48a-29ab6d7ec6d2 | -10.1804 | -57.265 | 2024-10-03 01:36:04 | GOES-16 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 53.8 |
| b11c3f10-6293-3d70-a86a-7e234f9af0ea | -10.1802 | -57.2848 | 2024-10-03 01:36:04 | GOES-16 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 55.4 |
| 2fee547c-fb5f-3968-b79d-aab1b5c46534 | -10.8942 | -63.8971 | 2024-10-03 01:36:08 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 50d1fe77-5715-3952-b2bb-72b9f85df7cb | -11.6742 | -65.0172 | 2024-10-03 01:36:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 2230a30d-d116-3a5d-9a23-3d620a230889 | -12.4038 | -63.0009 | 2024-10-03 01:36:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 88.5 |
| 9b66b824-f3da-3ab7-a9bf-4a01df7f21f2 | -12.404 | -62.9817 | 2024-10-03 01:36:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 77.5 |
| 2f55bbc2-f1f6-3b21-abab-f68d2c7e1028 | -12.5329 | -53.1212 | 2024-10-03 01:36:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 89.8 |


[Clique aqui para ver as próximas entradas](README36.md)
