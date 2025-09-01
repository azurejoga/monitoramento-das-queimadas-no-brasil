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

## Dados Diários - Página 80

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 884f4f50-913a-3324-a307-308c59584e01 | -8.84919 | -70.84338 | 2025-09-01 05:23:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| eee90ea9-f343-32d0-93a5-e4e4ac2da7f9 | -9.46011 | -62.34048 | 2025-09-01 05:23:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 304e187b-7d08-32cd-b635-10e37ec48123 | -9.45069 | -62.33533 | 2025-09-01 05:23:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 132bc6a7-b5a6-3f88-b4ec-1d7832b6a704 | -8.24257 | -72.81893 | 2025-09-01 05:23:00 | NOAA-21 | PORTO WALTER | ACRE | Brasil | 1200393 | 12 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a1c868c3-d635-37de-9b2f-68a5cddfe01a | -8.73543 | -62.40572 | 2025-09-01 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7d5122e2-dc6d-38e2-bf72-3b2f8ff111cc | -8.6229 | -62.59353 | 2025-09-01 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fd73c6b6-b6d6-34de-8787-5339214a25c8 | -7.58912 | -61.62877 | 2025-09-01 05:23:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 45ef632a-515f-367c-b2a3-168cc2a15562 | -8.76422 | -61.42517 | 2025-09-01 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| e4230c56-1c98-34c4-84b3-36c1e83a48aa | -8.722 | -62.42553 | 2025-09-01 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 22309e6c-7482-3065-80b6-0722b473c715 | -7.58967 | -61.62528 | 2025-09-01 05:23:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6448a4e9-0621-3a49-b7f6-5f3827a01d59 | -9.34787 | -65.42731 | 2025-09-01 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2d1281cc-bf89-3a1b-bb46-8be8bfd1a847 | -9.8325 | -65.05501 | 2025-09-01 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 55af1cb0-3053-3f7c-ad9e-70015b854519 | -9.06444 | -65.42392 | 2025-09-01 05:23:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8227d7e3-cac0-331b-ba24-5f31d4398348 | -9.27733 | -67.64588 | 2025-09-01 05:23:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8b4454dc-aef4-35e5-bae9-ce92790dc11d | -10.04503 | -48.09872 | 2025-09-01 05:23:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 6142dee1-88c6-3f55-8dcf-fa0657ff6ef2 | -7.58635 | -61.62475 | 2025-09-01 05:23:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| beabe6a3-1ca6-39b5-af8c-e225387cc4a1 | -9.06979 | -65.4152 | 2025-09-01 05:23:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 17184fa4-b0b6-33c6-9629-31d5441153b6 | -7.10679 | -63.04005 | 2025-09-01 05:23:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b0eba819-b74c-33be-a577-ca0831703740 | -9.13734 | -65.54492 | 2025-09-01 05:23:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 425e4bf0-8206-30ab-b657-eb381f73da13 | -9.86757 | -65.02317 | 2025-09-01 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bf87c59a-1007-3dc5-aa02-37ad0ed5f4b7 | -9.44503 | -60.56848 | 2025-09-01 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1e2a8728-7b4f-3749-84c6-99f17d8268fd | -9.83689 | -65.05125 | 2025-09-01 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 77935144-71a1-3a36-b959-45f0d532dfe4 | -7.69532 | -61.10487 | 2025-09-01 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3d52234d-f772-37d5-a9ad-dda605d9e7f0 | -8.73991 | -62.39914 | 2025-09-01 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bc3366bb-6e01-3215-a480-d1e641166515 | -9.13394 | -65.84727 | 2025-09-01 05:23:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 854cc92a-f8f1-3829-9c89-9b4807034dc1 | -9.12971 | -65.54363 | 2025-09-01 05:23:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 3680c944-d204-318f-aed2-2a550cb3c2a2 | -8.82732 | -47.83024 | 2025-09-01 05:23:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 6c7efa2a-a81d-3139-9c33-942c612ff7a6 | -7.69842 | -61.4754 | 2025-09-01 05:23:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0743f0ca-9018-3151-b0b4-ec6a2448bd61 | -8.65824 | -62.8261 | 2025-09-01 05:23:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 36012679-a924-3291-93dc-7385df967ab8 | -8.73435 | -62.39095 | 2025-09-01 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e6708594-89c2-371a-987a-83568eb050bc | -8.66509 | -62.92082 | 2025-09-01 05:23:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5daadf06-67ad-3c4a-9549-7368b3d1de92 | -8.8494 | -47.51688 | 2025-09-01 05:23:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 82641627-f0c1-3911-978e-3e3c9813d56e | -10.27857 | -54.25501 | 2025-09-01 05:23:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 004013d0-8e0c-310f-89f7-c719ddaf1cb8 | -10.369 | -52.28356 | 2025-09-01 05:23:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6ce85338-c441-3d1e-bc51-ca41b1fd6941 | -4.16052 | -46.78727 | 2025-09-01 05:23:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 66d928e9-ba63-3878-8bf4-a20ed930d855 | -8.76091 | -61.42466 | 2025-09-01 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 2c6beead-277d-3172-b2a9-38358e3a7720 | -9.4818 | -65.60153 | 2025-09-01 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 69a3c6b2-0c4d-3086-b07d-4c83951951ac | -10.24395 | -51.11084 | 2025-09-01 05:23:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f347db90-c03f-3718-bdb7-c4c9823af09b | -7.45275 | -63.1571 | 2025-09-01 05:23:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b2813a1d-7dc3-31a1-a46a-fcd81c017c64 | -7.70505 | -61.47645 | 2025-09-01 05:23:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2e4f604f-48a3-377f-9e1e-f42a5298a480 | -8.34764 | -62.92662 | 2025-09-01 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 945c8b9c-5b43-36f9-9e25-9eb46d643873 | -7.44868 | -63.16034 | 2025-09-01 05:23:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 24ee2be5-d0bb-3011-828f-7c6fba4b87b9 | -9.11851 | -61.20432 | 2025-09-01 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 07fd2758-44f5-3096-b2dc-7cecba7a5009 | -7.06521 | -63.05673 | 2025-09-01 05:23:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7a87977b-baed-3692-95bd-6a6ba81b37b4 | -8.96418 | -65.97035 | 2025-09-01 05:23:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dc304b4e-9532-392c-b701-fea462d9464c | -4.1248 | -47.65528 | 2025-09-01 05:23:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 06faeadb-75af-3753-97f4-569159e1e67a | -8.51027 | -67.12446 | 2025-09-01 05:23:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 05103d33-919b-341c-b922-d064325878b5 | -9.43887 | -60.54222 | 2025-09-01 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 33f832bf-097b-3e0c-bdd1-86fb5e0b4e67 | -2.41658 | -49.34435 | 2025-09-01 05:23:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f766124a-9113-3580-9a32-c8ee125e8902 | -8.59413 | -62.56691 | 2025-09-01 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 54d88de5-7e27-3189-bad2-e476240cb3fa | -8.28502 | -61.40159 | 2025-09-01 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1c6ff98e-584d-367e-8d52-ebd0bad4310b | -11.07606 | -52.07074 | 2025-09-01 05:23:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9fc82aa4-b922-3c0f-8050-dfcbaef8542e | -6.97366 | -71.74693 | 2025-09-01 05:23:00 | NOAA-21 | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4e303b67-72d3-34da-b6d5-a1ff0538d712 | -3.68403 | -49.19259 | 2025-09-01 05:23:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9df71ea9-a9fa-3d3d-8ea9-c3a92a8bfd0f | -9.14115 | -65.54558 | 2025-09-01 05:23:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 00f90772-5ce0-3b28-82a3-3117ae597112 | -9.13353 | -65.54428 | 2025-09-01 05:23:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 4c70b4ce-1a70-363c-96e2-3ee01d95a167 | -8.50959 | -67.1285 | 2025-09-01 05:23:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dc7c7145-319e-351b-8f2e-721766f72b69 | -7.11239 | -62.98279 | 2025-09-01 05:23:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 93c8e72a-0d99-3b89-9fc1-2976b6d4082f | -10.24293 | -51.11885 | 2025-09-01 05:23:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Cerrado | 10.5 |
| e3426b7b-3426-38d6-ad1c-6085fb20df3d | -5.5687 | -47.41182 | 2025-09-01 05:23:00 | NOAA-21 | DAVINÓPOLIS | MARANHÃO | Brasil | 2103752 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 8f73b3f0-3560-3c0b-aaee-aa57608fa464 | -9.05529 | -65.43197 | 2025-09-01 05:23:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e15148df-17de-3d63-b231-fd223e24a3b5 | -8.64529 | -67.24596 | 2025-09-01 05:23:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 10.7 |
| a433b38a-48f6-38eb-bc00-8b087b1c5a6e | -9.80929 | -61.2038 | 2025-09-01 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 044d3ec0-9768-3c81-ad73-ce209f75147a | -8.63693 | -62.59208 | 2025-09-01 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2d7a0b63-71a4-363f-8d83-244c5dde8104 | -8.73487 | -62.40928 | 2025-09-01 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3320ec95-6339-3d40-a31d-b25e4c3656d2 | -9.43784 | -60.57096 | 2025-09-01 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 133ea0d1-6865-3f60-8d92-b61e4285d628 | -9.64539 | -47.79898 | 2025-09-01 05:23:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 75b3b79d-3a3d-34cd-8f68-cd74b405bad7 | -9.12891 | -65.54836 | 2025-09-01 05:23:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 48be7b8c-e72a-3635-9dc5-ccb721f83375 | -8.2259 | -62.94135 | 2025-09-01 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c46ca044-e64b-33b8-a3c1-6f60107f349a | -8.55906 | -63.00988 | 2025-09-01 05:23:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a2c0db4d-af4c-3036-a48a-5dd3edb92a27 | -7.09569 | -63.13194 | 2025-09-01 05:23:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1e8b4579-3f63-37ca-b42b-6438232fddfa | -8.72313 | -62.41839 | 2025-09-01 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 601eb02a-1606-36f1-9884-37fc4e88b340 | -7.9571 | -63.49228 | 2025-09-01 05:23:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3f6366d3-43bf-3bf7-9c56-7c3994e5d7a9 | -9.44008 | -60.57852 | 2025-09-01 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2f89aa37-9d4b-391c-8d81-825c881bec43 | -9.45289 | -62.34294 | 2025-09-01 05:23:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 14089e66-6f47-353b-a997-923f84eeaa38 | -9.1119 | -61.20327 | 2025-09-01 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ee38160b-c6d7-35f0-82a0-bb547a767b81 | -8.31081 | -55.10003 | 2025-09-01 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 95ec6c0b-8c6b-3a14-b634-3838e8baba61 | -7.59851 | -61.63383 | 2025-09-01 05:23:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| aa86da18-f4c9-3240-bf4f-2f2db0036e12 | -9.4671 | -60.3144 | 2025-09-01 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 671dd2fc-e0d4-34ed-9a1e-80d1d82b1988 | -9.13052 | -65.53889 | 2025-09-01 05:23:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 66fcc727-2351-3454-9d58-6a9ecc0e8ebe | -9.14253 | -65.84364 | 2025-09-01 05:23:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7ffc9ded-a221-3595-8858-5b3147096457 | -9.17088 | -67.71199 | 2025-09-01 05:23:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 113ac5f1-4859-38a0-9bd5-02212759de52 | -7.27972 | -60.65281 | 2025-09-01 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 29e02e28-28de-31d3-97d5-cfde3171f558 | -8.55506 | -63.01303 | 2025-09-01 05:23:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8080f8ee-5a63-3d3d-9d4d-6259a4657c47 | -8.55786 | -63.01728 | 2025-09-01 05:23:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3ba9295c-a22a-33f6-a406-107bebe29c90 | -8.71252 | -62.42036 | 2025-09-01 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 755295b8-a1f1-387a-a5e4-f68d3ec2bc71 | -8.42708 | -62.29031 | 2025-09-01 05:23:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 98bf5963-8909-3457-9dfe-6bbf28b705a3 | -9.84332 | -65.05499 | 2025-09-01 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 11c22aae-b711-3e1a-bdd8-9d11ec8ea8fa | -8.68746 | -62.40535 | 2025-09-01 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d82334a0-d79b-3255-819d-29c0b9587a84 | -8.95194 | -65.94756 | 2025-09-01 05:23:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 024f2159-a30b-3658-b170-3092b9757b0a | -8.62012 | -62.58938 | 2025-09-01 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 40ae8092-3eda-3634-8d25-b3e2fa6719bd | -9.127 | -65.84106 | 2025-09-01 05:23:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ff58e0d0-14a1-3c2e-b554-d62abd872025 | -9.45114 | -60.57303 | 2025-09-01 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 37c57201-213a-32f8-890c-6b2eb09990fb | -10.0527 | -48.09356 | 2025-09-01 05:23:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| c79f7fcc-25fd-3596-b71e-8e3e8ff311dd | -9.83617 | -65.05563 | 2025-09-01 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 0b71666b-6474-3022-992c-764bd9498bf6 | -8.35058 | -70.26158 | 2025-09-01 05:23:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9bc5d11d-f279-3963-814c-c0ce84892e5c | -9.45786 | -62.35463 | 2025-09-01 05:23:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8db2a156-efea-32f9-b3dd-12a2a2aebb66 | -10.24934 | -51.11689 | 2025-09-01 05:23:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a637db78-b87a-351d-a1b4-f32b32e8b535 | -7.09447 | -63.1396 | 2025-09-01 05:23:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 318b44df-1307-39db-8c5a-43fc2f7fcc18 | -8.646 | -67.24189 | 2025-09-01 05:23:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |


[Clique aqui para ver as próximas entradas](README81.md)
