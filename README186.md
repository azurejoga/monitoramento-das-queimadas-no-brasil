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

## Dados Diários - Página 186

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 37236801-9958-3bbe-a28a-59e144573ca5 | -6.9336 | -58.9514 | 2026-08-28 21:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 97.7 |
| a1d04dba-c920-3375-9d2a-34678c4e5049 | -4.1934 | -54.5755 | 2026-08-28 21:10:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 80.7 |
| 56b04487-ec9e-3052-9013-64920a13b389 | -6.8572 | -59.3986 | 2026-08-28 21:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 146.8 |
| e30082b6-f8cd-3451-9947-cfd55b159933 | -14.4859 | -58.4874 | 2026-08-28 21:10:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 202.7 |
| 8302f1a3-85e0-31bd-b92e-3571ba4acf22 | -9.0198 | -57.5574 | 2026-08-28 21:10:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 96.2 |
| f612c1f1-6681-321a-9c17-b84d021c6eb2 | -7.5516 | -69.9963 | 2026-08-28 21:10:00 | GOES-19 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 110.5 |
| 7ec35bce-e3ff-3ecb-b76a-7d72971560f2 | -14.9389 | -56.3011 | 2026-08-28 21:10:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 76.9 |
| 5d2da3f5-7f00-346c-9fff-b86dcd929cbb | -5.871 | -57.7715 | 2026-08-28 21:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 105.7 |
| 54fdc9f2-92f7-32f2-ac28-65fc3e3a797e | -7.5477 | -61.3247 | 2026-08-28 21:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 99.9 |
| 050fe6d6-a02f-39bc-8c95-32a7042b225f | -9.0012 | -57.5585 | 2026-08-28 21:10:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 83.7 |
| c66f136d-f16a-318b-bc66-730cbb858483 | -8.6012 | -70.2192 | 2026-08-28 21:10:00 | GOES-19 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 84.8 |
| c74d4a74-d3f4-323f-a915-45c0ef5e9b2e | -6.1656 | -57.7988 | 2026-08-28 21:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 86.4 |
| 6fefcd1a-1c81-36b7-bfc2-73a8743cf834 | -5.8711 | -57.752 | 2026-08-28 21:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 69.3 |
| 6b6292d8-4b29-318c-97ae-761f9b253735 | -9.9708 | -53.9419 | 2026-08-28 21:10:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 99.3 |
| 553eec78-af67-3dc2-97ff-b62eae2be6aa | -6.1657 | -57.7793 | 2026-08-28 21:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 106.9 |
| e184ce57-ffd3-3fa8-b723-ea0d01b39e47 | -6.9521 | -58.9506 | 2026-08-28 21:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 73.4 |
| 9a5e4054-fce7-37f7-b624-2cf8149f70f3 | -11.1916 | -51.2708 | 2026-08-28 21:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 139.1 |
| 043a4c80-18b7-39dc-b781-72c73def5183 | -5.8894 | -57.7708 | 2026-08-28 21:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 263.2 |
| b0e05107-a058-3ea7-840c-c5716c0c1c61 | -5.8895 | -57.7513 | 2026-08-28 21:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 355.5 |
| f7c15f32-495a-327a-b507-45e2bafce783 | -8.5969 | -54.7755 | 2026-08-28 21:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 126.7 |
| a70c3a15-d0f6-315a-b136-3feb6dd4898e | -11.7167 | -54.5244 | 2026-08-28 21:10:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 130.6 |
| 9a3eebf9-bbfe-32c0-a5d8-eef5da65fc21 | -7.5662 | -61.3049 | 2026-08-28 21:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 212.8 |
| 32f5dfc6-61dd-37a6-a71d-c2f80c924dd5 | 0.1549 | -60.393 | 2026-08-28 21:10:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 82.2 |
| d2f23b14-6264-3b6d-aaa1-13d4ab58ae2b | 0.1367 | -60.393 | 2026-08-28 21:10:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 79.1 |
| afdf25e6-199c-3d09-b4b1-a3ac6ae1ad26 | -11.7165 | -54.5449 | 2026-08-28 21:10:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 109.3 |
| c97f60b8-6263-3572-94c3-a1aece269676 | -14.4856 | -58.5074 | 2026-08-28 21:10:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 122.7 |
| 8bc6190c-6796-3df6-83dd-c30197b02f50 | -5.9079 | -57.7506 | 2026-08-28 21:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 72.9 |
| 68bf8976-df34-3e25-9632-ee1ca28ec98d | -7.529 | -61.3635 | 2026-08-28 21:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 81.3 |
| 0ec0e40b-5dd1-3d2d-a997-432d7bb135bd | -9.8739 | -60.2955 | 2026-08-28 21:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 158.0 |
| 3f5c9380-ca9e-34d9-9401-e55960891521 | -9.1425 | -61.0069 | 2026-08-28 21:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 103.2 |
| e4426f87-c86a-309e-b724-b2c09b236931 | -9.4329 | -51.6926 | 2026-08-28 21:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 72.9 |
| 72d8dab7-b586-308a-905b-17c2597980b0 | -9.971 | -53.9214 | 2026-08-28 21:10:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 93.5 |
| b5d07081-9315-3a90-9673-9b828a097e6b | -6.7699 | -55.6644 | 2026-08-28 21:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 428.9 |
| 84d918d9-9b8a-3b03-acae-56f56933febb | -14.5051 | -58.4856 | 2026-08-28 21:10:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 103.9 |
| b3a7201c-430d-3ef6-b3a8-e020c0d74512 | -8.5971 | -54.7553 | 2026-08-28 21:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 109.5 |
| 196fbc8e-fcaf-3c52-a845-1d58b243f4ea | -6.1472 | -57.7995 | 2026-08-28 21:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 0cdfbb7c-7386-3c6f-a4cf-2ad99a44c4c1 | -6.7247 | -60.0189 | 2026-08-28 21:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 123.6 |
| 46e12bd6-068b-3208-b8c5-f46368dbe25b | -6.0004 | -57.6884 | 2026-08-28 21:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 74.1 |
| c095b255-138a-3523-b473-1594f88c03d9 | -14.2027 | -52.8432 | 2026-08-28 21:10:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 82.7 |
| 1e0c17ef-3cd1-3628-a5af-cb023d57da78 | -14.9386 | -56.3216 | 2026-08-28 21:10:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 103.5 |
| c902f4c4-b244-3320-a2a8-4f7327af7324 | -6.7513 | -55.6853 | 2026-08-28 21:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 105.5 |
| a5b8b081-c7f0-3762-99a3-2f97b2ab7c33 | -6.7515 | -55.6455 | 2026-08-28 21:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 105.8 |
| 1bcead62-a031-38ab-9104-6e0c6c65529d | -3.6216 | -60.547 | 2026-08-28 21:10:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 46e874cb-a06a-3cec-a0d3-6e0248e8c3db | -4.0574 | -56.2865 | 2026-08-28 21:10:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 127.5 |
| ea4fb397-3ed3-3969-8098-b4716b6034e9 | -6.7514 | -55.6654 | 2026-08-28 21:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 259.8 |
| d47f6370-33d4-37ec-a51c-86121808f874 | -6.7248 | -59.9998 | 2026-08-28 21:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 83.8 |
| d7ebccc4-6480-36d2-af34-db7de2f61d6f | -10.7407 | -54.0401 | 2026-08-28 21:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 98.3 |
| c2bc6252-d50e-3e04-b22e-e98f2f8b0f25 | -12.77 | -44.29 | 2026-08-28 21:15:00 | MSG-03 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 337d1198-1ee1-33e5-b641-d99cf19a231f | -12.74 | -44.28 | 2026-08-28 21:15:00 | MSG-03 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c50098cb-6f5a-3c13-a23a-3ee242a6fcc0 | -5.9 | -42.68 | 2026-08-28 21:15:00 | MSG-03 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| e49870c3-aa5c-3d61-9d6d-892e89b939ee | -5.87 | -42.67 | 2026-08-28 21:15:00 | MSG-03 | LAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2205540 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| ae79dc64-beda-36f5-ba86-c68bf00b519a | -5.87 | -42.72 | 2026-08-28 21:15:00 | MSG-03 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 3aa995e1-6194-3bdb-a28e-db7903367712 | -17.59 | -51.63 | 2026-08-28 21:15:00 | MSG-03 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 56db8d45-aa1b-326f-a924-34a210cdc197 | -5.0373 | -51.9422 | 2026-08-28 21:20:00 | GOES-19 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 126.3 |
| 62947278-9c37-3a3b-9cb6-743c06918938 | -14.4856 | -58.5074 | 2026-08-28 21:20:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 89.3 |
| a7fc6f2d-d231-353a-b904-672bcf10fcd7 | -8.5971 | -54.7553 | 2026-08-28 21:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 88.7 |
| 1fc025ab-8c8f-3f19-9226-c6d58c453c9c | -10.7407 | -54.0401 | 2026-08-28 21:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 79.8 |
| 4b43d98b-555a-3e3a-af13-923245e15e7e | -14.4859 | -58.4874 | 2026-08-28 21:20:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 107.0 |
| bc46b2e4-311a-3bfb-82c8-68d0c611a4ba | -5.9078 | -57.77 | 2026-08-28 21:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 1c7cfc80-956b-39ae-bffd-b0147cc49537 | -6.7247 | -60.0189 | 2026-08-28 21:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 104.6 |
| c572cafe-d654-3abc-bbb2-28b948108f5c | -14.5051 | -58.4856 | 2026-08-28 21:20:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 108.7 |
| 50f7fc3e-1545-36ae-836c-29c5bd1922d0 | 0.1549 | -60.393 | 2026-08-28 21:20:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 83.2 |
| a1635fe0-7fff-373c-964f-a8ea08010e4e | -5.8711 | -57.752 | 2026-08-28 21:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 89.3 |
| 6e2621ad-2a38-3ef1-8946-d034e162b3f6 | -11.7165 | -54.5449 | 2026-08-28 21:20:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 108.5 |
| 8de48fd8-179f-3caf-9a12-2bac281b0d73 | -7.5477 | -61.3247 | 2026-08-28 21:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 77.8 |
| 4e37b9a7-a504-3bc9-9ccc-23c4f5361b7e | -6.1656 | -57.7988 | 2026-08-28 21:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 92.9 |
| 2c59df7f-04e4-3871-a907-487ddcfba190 | -5.9819 | -57.6892 | 2026-08-28 21:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 17fb4c7c-9499-3051-9c19-4621c8faaa7f | -14.9389 | -56.3011 | 2026-08-28 21:20:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 109.4 |
| ea25497b-dd50-3db8-869d-773b1d6967b1 | -7.4953 | -55.2862 | 2026-08-28 21:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 75.1 |
| 9c62fcdd-c4a7-315b-b88f-622a988cd656 | -14.2027 | -52.8432 | 2026-08-28 21:20:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 96.2 |
| 5b270159-4128-3ef4-8a3a-9a59cb324fa0 | -5.8894 | -57.7708 | 2026-08-28 21:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 294.4 |
| 5d77fb83-31c1-37bc-8fc3-f9e3009e6469 | -8.5969 | -54.7755 | 2026-08-28 21:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 110.7 |
| 1dd75e55-bb29-3f4d-94f5-5602f24ed2bb | -9.9708 | -53.9419 | 2026-08-28 21:20:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 88.6 |
| 575bb42f-798f-389c-bc19-c3f48b99324b | -7.5516 | -69.9963 | 2026-08-28 21:20:00 | GOES-19 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 104.7 |
| 7bc49502-1348-3ca9-987c-9819704cdad6 | -8.5968 | -54.7957 | 2026-08-28 21:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 73.4 |
| de9cb8e9-ec8e-3131-8a32-abc3eaf3885b | -6.9521 | -58.9506 | 2026-08-28 21:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 74.7 |
| 874c1241-74b5-3ac9-a44e-94b7e6720865 | -5.8895 | -57.7513 | 2026-08-28 21:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 309.1 |
| eea49c32-e3d3-3837-a870-fecfe76a7fab | -14.9015 | -52.6055 | 2026-08-28 21:20:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 94.0 |
| 0da37598-960b-3b09-a253-aac2da159a1a | -7.5661 | -61.3239 | 2026-08-28 21:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 111.2 |
| 43636b29-88e3-39fa-aa63-cbeb123759fa | -4.0574 | -56.2865 | 2026-08-28 21:20:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 84.9 |
| 268fd7a0-e967-3594-af0c-b1eb5cd6018e | -11.1916 | -51.2708 | 2026-08-28 21:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 79.3 |
| 17cfb37a-e624-34ec-95b4-c7a054399640 | -6.9336 | -58.9514 | 2026-08-28 21:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 80.5 |
| 02d9e079-c933-3d38-8b62-f49e816ba74b | -14.9011 | -52.6267 | 2026-08-28 21:20:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 105.3 |
| ea3cdf64-6436-338e-b8bc-c40575b47ff9 | -5.7799 | -57.58 | 2026-08-28 21:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 66.5 |
| 5f388462-549a-354e-829e-092658f16ae4 | -6.8572 | -59.3986 | 2026-08-28 21:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 116.3 |
| 620b05a3-3820-3047-979d-f286ae1ba688 | -14.9386 | -56.3216 | 2026-08-28 21:20:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 149.0 |
| eecf271c-d8e4-3f76-ad86-b49f032709d9 | -6.0004 | -57.6884 | 2026-08-28 21:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 91.0 |
| 7f043523-a092-36e4-ae12-5455a423425e | -6.1657 | -57.7793 | 2026-08-28 21:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 105.0 |
| c64a6795-e865-39f1-a638-ec93c39d6245 | 0.1367 | -60.412 | 2026-08-28 21:20:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 96.4 |
| 0b24a5fa-d250-331a-bbd0-bebfbd40e5e6 | -6.8757 | -59.3978 | 2026-08-28 21:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 124.3 |
| ff52cc76-043d-3497-8d25-7f2b1e072ed4 | -11.7167 | -54.5244 | 2026-08-28 21:20:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 116.7 |
| 8151dd20-c783-3cf4-b79f-8fe60ffc5245 | 0.1367 | -60.393 | 2026-08-28 21:20:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 116.7 |
| 649bc56d-3b29-3113-aecb-8fe8eab54770 | -6.7652 | -63.054 | 2026-08-28 21:20:00 | GOES-19 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 92.1 |
| 25de47e0-0053-37df-938f-e8931c31e918 | -7.5662 | -61.3049 | 2026-08-28 21:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 200.9 |
| 5d5c345b-3916-32dd-8add-479262a91373 | -9.8739 | -60.2955 | 2026-08-28 21:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 137.5 |
| 8984c688-2d8b-394a-a567-c17b34a21c41 | -14.9193 | -56.3237 | 2026-08-28 21:20:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 89.7 |
| 98d9a147-4fa6-3b1e-a58a-3b3e6174bc3e | -8.6012 | -70.2192 | 2026-08-28 21:20:00 | GOES-19 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 91.8 |
| a958b5c2-b880-3e9e-a36c-257324b55434 | -4.1934 | -54.5755 | 2026-08-28 21:20:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 86.5 |
| 4e8f5eea-38d5-34a2-9a70-992a9ce6ea85 | -8.5366 | -55.2625 | 2026-08-28 21:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 103.7 |
| fc9d62b5-a96d-3b99-8f41-394a0bf781c3 | -9.971 | -53.9214 | 2026-08-28 21:20:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 76.3 |


[Clique aqui para ver as próximas entradas](README187.md)
