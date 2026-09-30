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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a8818ca7-cc15-3ee9-adf4-a29b237b72d8 | -2.9924 | -51.045 | 2026-09-30 00:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 153.5 |
| 349488f1-226a-3e61-b760-3a56c19556d9 | -7.8295 | -45.8381 | 2026-09-30 00:10:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 133.5 |
| 9b13b1c4-0dc6-35f7-8249-bff769f3ca4e | -11.4499 | -43.4329 | 2026-09-30 00:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 126.6 |
| 6b6837b3-4882-3bf9-a015-7fc348e03361 | -3.2129 | -46.9383 | 2026-09-30 00:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 85.6 |
| a985b8fa-2803-3c3e-bced-ab9f3890ddef | -9.1256 | -67.8507 | 2026-09-30 00:10:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 65.1 |
| cec6281c-8958-3536-84fb-399e2c4b33fe | -6.2308 | -42.5226 | 2026-09-30 00:10:00 | GOES-19 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 29.8 |
| e7027847-3f93-3aeb-a9cd-44a67effe3fe | -7.8109 | -45.8173 | 2026-09-30 00:10:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 131.1 |
| b4b953ce-caa7-3f73-84b7-62e38e5af8f5 | -11.8814 | -64.9323 | 2026-09-30 00:10:00 | GOES-19 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 2d1fb859-9932-35da-b9b9-e01e81dc7244 | -9.1626 | -60.7948 | 2026-09-30 00:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 32.5 |
| d01f3fe3-1986-31f4-aa83-261fdc683555 | -11.7182 | -43.4386 | 2026-09-30 00:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 166.9 |
| 1c9f172f-0582-3a3a-be25-7f3b2b179746 | -20.5349 | -49.6016 | 2026-09-30 00:10:00 | GOES-19 | TANABI | SÃO PAULO | Brasil | 3553401 | 35 | 33 | nan | nan | nan | Cerrado | 96.0 |
| 1d1c7551-52af-3d40-9e3a-9a8564897dc9 | -7.8107 | -45.8399 | 2026-09-30 00:10:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 66.5 |
| 071f55aa-a1f6-3094-90fd-43adc48117e6 | -7.8483 | -45.8363 | 2026-09-30 00:10:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 146.7 |
| 83f4df9d-2328-3a9d-b075-9ef2597940bb | -2.9082 | -54.0907 | 2026-09-30 00:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 109.4 |
| 51d52d52-1e54-3b23-bff0-b37812c01fb6 | -6.22 | -42.5 | 2026-09-30 00:15:00 | MSG-03 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 88babf00-02a4-3984-b323-a4689d675afe | -18.27 | -53.09 | 2026-09-30 00:15:00 | MSG-03 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| d49c0fe5-7497-344e-9227-1d8948330a80 | -3.23 | -46.93 | 2026-09-30 00:15:00 | MSG-03 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5c3f84d7-5d26-3c3f-aa5a-684652fe52d7 | -6.22 | -42.54 | 2026-09-30 00:15:00 | MSG-03 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 2918c9a1-a79c-3617-a403-113acefd6a8f | -11.71 | -43.46 | 2026-09-30 00:15:00 | MSG-03 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| fb0776e6-bb6a-346b-aa32-214f130136d4 | -7.84 | -45.84 | 2026-09-30 00:15:00 | MSG-03 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3a2688c1-0c77-3331-9c1b-6a34469614f7 | -3.2315 | -46.9156 | 2026-09-30 00:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 74.9 |
| dd8002ae-bb6a-36db-af84-85f7f35bc832 | -9.1072 | -67.8326 | 2026-09-30 00:20:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 8d345627-7f0c-3cbc-be91-a97a1875a447 | -2.9739 | -51.0455 | 2026-09-30 00:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 115.8 |
| 725017e3-5121-36c9-82de-13c3fe007a5b | -2.9924 | -51.045 | 2026-09-30 00:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 91.3 |
| 5a5dc2cc-212f-37ae-a692-1492ba6ea75e | -2.974 | -51.0247 | 2026-09-30 00:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 87.4 |
| 9c432db1-c382-3f4f-b397-142db4403e8e | -11.64 | -43.5218 | 2026-09-30 00:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 143.9 |
| 2caae29f-e932-3867-87fb-e26af3063aea | -12.3085 | -47.9539 | 2026-09-30 00:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 193.9 |
| 5f39538a-4222-3eb6-9075-0dd2745116f6 | -12.2706 | -50.2735 | 2026-09-30 00:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 75.7 |
| 96a210d7-5727-30c5-b81c-f4b71085771a | -11.699 | -43.4416 | 2026-09-30 00:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 194.0 |
| bffb144f-1f28-371c-90bd-a90d13c0d6bd | -2.9925 | -51.0242 | 2026-09-30 00:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 63.3 |
| d69b0edc-8cb9-3d40-ba8a-435080b750f0 | -4.4507 | -47.9112 | 2026-09-30 00:20:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 70.2 |
| 8d9672ef-0e5b-3425-91de-a5121dc303e1 | -7.8109 | -45.8173 | 2026-09-30 00:20:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 134.4 |
| f49c4fae-f146-3607-89c4-cce4603a86d6 | -7.8483 | -45.8363 | 2026-09-30 00:20:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 155.8 |
| 2a459a1b-d37f-382a-a097-1465e43606c4 | -9.1256 | -67.8507 | 2026-09-30 00:20:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 64.4 |
| fec29b05-33df-3e91-816b-bb5898fb5987 | -7.7133 | -72.478 | 2026-09-30 00:20:00 | GOES-19 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 64.4 |
| 8ad5cef7-da82-3e46-a800-abe7d0e7f1e6 | -3.2313 | -46.9596 | 2026-09-30 00:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 69.9 |
| 0bd98171-69fe-3bf7-a6d7-da9d97f89844 | -11.4307 | -43.4358 | 2026-09-30 00:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 76.7 |
| 311ce7f4-fed4-3b87-b717-3b12e4a88417 | -6.2308 | -42.5226 | 2026-09-30 00:20:00 | GOES-19 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 51.2 |
| f853b392-6232-3e06-bd98-af50b5d81134 | -3.3801 | -50.95 | 2026-09-30 00:20:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 69.6 |
| 71f1a42b-45a5-3890-98ff-263862d7d403 | -11.8814 | -64.9323 | 2026-09-30 00:20:00 | GOES-19 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 66.4 |
| 8d05f050-80c7-3c79-984e-78a3ae9a4b81 | -7.7317 | -72.4779 | 2026-09-30 00:20:00 | GOES-19 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 86.4 |
| 4a9758f9-42af-3ea0-b2a3-5772b47329c9 | -9.1626 | -60.7948 | 2026-09-30 00:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 31.9 |
| 922f4118-285b-35ad-8b0c-541943b3aec7 | -12.2515 | -50.2758 | 2026-09-30 00:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 112.1 |
| 5145c29a-8991-3589-b5ed-90a01ef4cf7d | -6.895 | -43.7066 | 2026-09-30 00:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 101.4 |
| df39e3df-f8f2-331d-8be0-5cd6efe297b8 | -6.9138 | -43.7049 | 2026-09-30 00:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 71.9 |
| 8418bcd9-6593-3ee8-a0e3-c07e70149589 | -7.8486 | -45.8138 | 2026-09-30 00:20:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 210.4 |
| f724c3fd-051e-3c67-8a49-670d87380772 | -5.7561 | -45.1747 | 2026-09-30 00:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 87.7 |
| 63cfe7e8-64f5-33d0-a74e-4ab54aeca484 | -7.8297 | -45.8156 | 2026-09-30 00:20:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 276.0 |
| 381f9e58-d032-34a5-aecb-8178c832acd4 | -6.2123 | -42.5006 | 2026-09-30 00:20:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 195.8 |
| a4928d74-8968-3385-bfb8-ecbc7cbd6e12 | -11.7182 | -43.4386 | 2026-09-30 00:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 186.0 |
| 1a3b94b7-21c4-3247-9d89-abf0171c6fb9 | -2.9082 | -54.0907 | 2026-09-30 00:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 103.0 |
| 32ecd941-6b4c-388e-9939-b402545956f5 | -7.8295 | -45.8381 | 2026-09-30 00:20:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 145.2 |
| b1025de6-7b8d-3acf-bc6e-70ea06903a22 | -9.1257 | -67.8322 | 2026-09-30 00:20:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 82.4 |
| e63f3192-eca3-3dac-9e02-0600b434af91 | -11.6395 | -43.5455 | 2026-09-30 00:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 60.9 |
| b2e3e1a4-3345-3b11-8abc-0196c5f3b907 | -11.8812 | -64.9513 | 2026-09-30 00:20:00 | GOES-19 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 76.0 |
| 8116ff2e-e5e7-3650-927a-f4ff019a43a6 | -11.917 | -50.9787 | 2026-09-30 00:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 86.0 |
| 02466f00-2f95-3569-b9d9-4f017987bc98 | -3.2129 | -46.9383 | 2026-09-30 00:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 113.6 |
| f624a91a-0a29-36f2-b053-99c023deecb4 | -7.8107 | -45.8399 | 2026-09-30 00:20:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 71.3 |
| ea1e97d4-86f7-34df-acd4-10070bbf4d46 | -3.2314 | -46.9376 | 2026-09-30 00:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 276.0 |
| 0c1e3381-8073-31fc-b900-903a93c21a79 | -11.6986 | -43.4654 | 2026-09-30 00:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 97.1 |
| ee482427-be18-3856-ae04-982fa9d7e625 | -9.8775 | -36.0262 | 2026-09-30 00:20:00 | GOES-19 | ROTEIRO | ALAGOAS | Brasil | 2707800 | 27 | 33 | nan | nan | nan | Mata Atlântica | 66.6 |
| 3372c7de-4105-30b3-9ee9-4597bcdf794f | 3.2924 | -60.6101 | 2026-09-30 00:20:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 72.6 |
| 108fe547-4ef2-3886-b0f1-e3091333b3c6 | -11.7178 | -43.4623 | 2026-09-30 00:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 97.4 |
| 850aebcc-c682-3384-8ce3-4c57ede00a63 | -11.898 | -50.9809 | 2026-09-30 00:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 59.1 |
| 47968c9b-65d0-3edb-86e2-1b8d0ec09178 | -8.2865 | -50.2731 | 2026-09-30 00:20:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 76.6 |
| 24a9ba5d-587b-33bc-950b-42aa8c36e483 | -6.212 | -42.5243 | 2026-09-30 00:20:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 258.4 |
| 0a94eb28-53e3-3919-88c0-8c9989d4af5d | -10.0779 | -63.0804 | 2026-09-30 00:20:00 | GOES-19 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 82.7 |
| 9c8bde9c-eed9-36dc-93e9-4fac6c958529 | -12.2518 | -50.2543 | 2026-09-30 00:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 31e13e15-d618-32e3-ae62-80558cde5e49 | -11.9167 | -51.0 | 2026-09-30 00:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 65.9 |
| c312a322-a5fc-31bb-8762-eb39f8f1c1c9 | -4.4506 | -47.9329 | 2026-09-30 00:20:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 6bf702f8-d7aa-3502-9fe2-d53d1a5ea442 | 3.2742 | -60.6105 | 2026-09-30 00:20:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 76.4 |
| bf2d96de-1408-30eb-9ef2-3bee87d8fa70 | -11.4499 | -43.4329 | 2026-09-30 00:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 89.3 |
| 6f1a08c7-790e-3974-8094-f4ea468d2f31 | -11.6207 | -43.5248 | 2026-09-30 00:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 56.2 |
| 3e936606-5a73-3a29-a211-c50363b9581d | -3.2129 | -46.9383 | 2026-09-30 00:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 74.4 |
| 719edd81-31d7-35ef-8fe8-eaf7eca7f018 | -7.8483 | -45.8363 | 2026-09-30 00:30:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 154.3 |
| 3471da50-875e-33cc-8072-0b201d580627 | -7.5248 | -44.5485 | 2026-09-30 00:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 91.6 |
| c879d731-b6d8-35ad-b778-ec2e62864357 | -7.8486 | -45.8138 | 2026-09-30 00:30:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 223.0 |
| 8bca9dba-f7b0-3035-98a9-058718ee5c2b | -7.8109 | -45.8173 | 2026-09-30 00:30:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 127.2 |
| 674a15a9-e522-3347-af9e-6e754e6acb0e | -3.3801 | -50.95 | 2026-09-30 00:30:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 0492b8dd-6353-3c3f-aa01-0b78ebb92985 | -5.7561 | -45.1747 | 2026-09-30 00:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 88.5 |
| da896ec1-cdbc-3cfb-825e-321a96b77fe2 | -3.2315 | -46.9156 | 2026-09-30 00:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 71.6 |
| 2c6be5ce-fda6-3e6e-a893-75f035150f14 | -10.0779 | -63.0804 | 2026-09-30 00:30:00 | GOES-19 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 80.4 |
| 68e33598-e19e-3088-b459-76ccce447535 | -2.974 | -51.0247 | 2026-09-30 00:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 97.5 |
| e3b3382b-735f-31fb-ba73-3f13f1154b93 | -12.3277 | -47.9513 | 2026-09-30 00:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 89.7 |
| f18c2c72-c390-315c-a3fe-87253c40cccb | -2.9739 | -51.0455 | 2026-09-30 00:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 126.3 |
| 703940b2-3043-3eee-9da5-fb1b33656a82 | -7.8297 | -45.8156 | 2026-09-30 00:30:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 283.3 |
| 84124ce0-9bde-395d-90d4-74df98c44834 | -3.2314 | -46.9376 | 2026-09-30 00:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 350.5 |
| bddd5073-c894-3df2-be5c-77c27eef6f58 | -11.8814 | -64.9323 | 2026-09-30 00:30:00 | GOES-19 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 2329d517-0d16-380f-83e9-67a60118f339 | -11.4499 | -43.4329 | 2026-09-30 00:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 78.4 |
| 7505d3c9-f806-3c75-b5f2-73de69b49926 | -4.4507 | -47.9112 | 2026-09-30 00:30:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 84.9 |
| e95c7484-6422-3b06-b35d-94ede794b6af | -11.7178 | -43.4623 | 2026-09-30 00:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 85.6 |
| e38cd41d-b6bc-3de5-afcd-0badb2e88373 | -4.4506 | -47.9329 | 2026-09-30 00:30:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 73.1 |
| d6c44d3f-ec7d-3fd5-a550-89088ca16722 | -6.2123 | -42.5006 | 2026-09-30 00:30:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 101.8 |
| a6cbd8fe-6667-39f8-9510-746584407539 | -5.7374 | -45.176 | 2026-09-30 00:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 54.9 |
| 86abe27c-9d98-38dd-a7cf-a7adfb2dfb26 | -9.1257 | -67.8322 | 2026-09-30 00:30:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 76.5 |
| 320e3537-c208-3f6c-aa60-6d50b034e7b1 | -7.8107 | -45.8399 | 2026-09-30 00:30:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 63.4 |
| 5251bd23-0bee-3fa8-a239-c23a47d213ee | -6.895 | -43.7066 | 2026-09-30 00:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 115.7 |
| 1796a3e7-8f50-33fd-8060-fb746b001aa4 | -11.699 | -43.4416 | 2026-09-30 00:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 85.7 |
| a01a693c-a28d-34ff-86f3-ff77480b7372 | -2.9082 | -54.0907 | 2026-09-30 00:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 103.1 |
| 600da05f-b05e-3059-b13b-3f1b535f525c | -6.212 | -42.5243 | 2026-09-30 00:30:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 119.2 |


[Clique aqui para ver as próximas entradas](README3.md)
