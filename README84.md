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

## Dados Diários - Página 84

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e53e624c-ebdf-376e-9dd2-1cd8eadc1365 | -10.7784 | -54.0368 | 2026-08-26 14:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 82.7 |
| fc2f809c-c0d4-3262-987f-f29bf8c8f35a | -14.5401 | -52.2714 | 2026-08-26 14:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 94.1 |
| aef3e194-9cd0-32d1-876b-e78c07d7854c | -11.8165 | -47.6647 | 2026-08-26 14:20:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 109.8 |
| 230436bb-a406-3aac-9902-47797446fed0 | -6.3322 | -54.7473 | 2026-08-26 14:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 73.3 |
| dd15a0fd-bef7-3ea4-865f-fa90b45cc09d | -8.5363 | -55.3027 | 2026-08-26 14:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 89.7 |
| 65167d83-5142-390f-bdb1-1af970361e0e | -6.2298 | -53.4805 | 2026-08-26 14:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 137.9 |
| 0f0f96f2-cfca-3abf-bd49-99a10b23338a | -7.1309 | -42.7945 | 2026-08-26 14:20:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 321.1 |
| 5a26728d-c445-3f86-b32e-c9520bc2d552 | -7.5104 | -61.3832 | 2026-08-26 14:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 55.5 |
| dbe21bda-46fe-3c09-801f-5ab594bc63e9 | -13.3402 | -48.2079 | 2026-08-26 14:20:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 84.6 |
| c6b02aec-f56e-3344-b2c4-f47d1990f631 | -7.6649 | -47.1242 | 2026-08-26 14:20:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 125.1 |
| 78f4945f-9222-30af-95d6-dc46f4af8033 | -6.6409 | -58.5181 | 2026-08-26 14:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 4d9f51e6-3db1-3c51-89e6-0b72b5ab56d1 | -6.6226 | -58.4995 | 2026-08-26 14:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 66.4 |
| 69049bf8-622f-3337-9615-6d6f2c751d9f | -11.004 | -51.1423 | 2026-08-26 14:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 148.4 |
| b98fdf41-4da3-3d06-909d-a994ef68cfc3 | -13.7555 | -51.9691 | 2026-08-26 14:20:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 128.4 |
| 812ce914-ad06-3787-9b86-8aaa4bdaad3d | -9.6024 | -55.1078 | 2026-08-26 14:20:00 | GOES-19 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 186.8 |
| d83f364f-d2bb-3a68-a43e-d6b325e359c5 | -4.8004 | -43.1476 | 2026-08-26 14:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 111.6 |
| 6ef4f403-d3ee-308e-b3c0-20abb66810c3 | -11.1939 | -53.9993 | 2026-08-26 14:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 78.5 |
| 4c051fd5-8869-3560-aca4-04cdef73c480 | -12.1422 | -43.3707 | 2026-08-26 14:20:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 155.0 |
| 9617f9f8-51ef-35cf-b4e7-5e7a34e3fc0d | -6.1743 | -53.4834 | 2026-08-26 14:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 65.8 |
| e14b008c-ff80-3cbd-8b2e-5977b3299ccc | -3.3081 | -42.7614 | 2026-08-26 14:20:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 79.5 |
| 782707ec-8100-3bdb-9143-f02a193a0063 | -8.6344 | -54.7528 | 2026-08-26 14:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 102.1 |
| 85427e8d-cf72-3791-8595-3559e0982a9b | -6.6917 | -45.1932 | 2026-08-26 14:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 102.9 |
| 07912543-92be-33a4-b9ed-a258df70df89 | -9.6776 | -55.082 | 2026-08-26 14:20:00 | GOES-19 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 117.3 |
| 68827f0a-5815-3f48-977d-1f3c234f918a | -13.7552 | -51.9903 | 2026-08-26 14:20:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 117.1 |
| ed806207-2bc5-32bd-9046-12511e138de2 | -6.0353 | -58.0376 | 2026-08-26 14:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 74.3 |
| 51862690-42d1-3514-a2b8-b2c1568bdd6f | -9.1899 | -49.9818 | 2026-08-26 14:20:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 104.3 |
| 861cd8b4-205a-316e-a01d-ca3056caf541 | -8.1482 | -47.5218 | 2026-08-26 14:20:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 127.3 |
| 9cac564d-5a62-3aa6-aaa0-d3571b7b942c | -10.76 | -53.9974 | 2026-08-26 14:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 71.5 |
| 8477c028-3098-3908-8008-72265952ebdd | -3.2178 | -61.2551 | 2026-08-26 14:20:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 50.8 |
| 23ad6422-f9fd-3ddb-95fd-089684053cb2 | -7.0242 | -59.2374 | 2026-08-26 14:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 77.0 |
| aa243589-e4c5-35da-9ee2-1d6c929d674e | -8.5973 | -54.7352 | 2026-08-26 14:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 81.4 |
| c4824845-6685-31f1-819e-657ca30bdd9a | -8.9418 | -45.748 | 2026-08-26 14:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 99.1 |
| 83a82f48-4c27-3a2b-ae3a-3bbcd183e94a | -11.1165 | -49.8707 | 2026-08-26 14:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 80.7 |
| 129012ca-6d5c-31ce-a6f7-001264578ba0 | -8.5361 | -55.3228 | 2026-08-26 14:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 63.9 |
| f0c30aaa-df72-31cb-864c-64395f83e502 | -3.2178 | -61.2362 | 2026-08-26 14:20:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 129.4 |
| a775ca37-e1a0-381b-a465-07d305b9521d | -7.1312 | -42.7708 | 2026-08-26 14:20:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 122.9 |
| 072d7e4e-df18-3092-9dcc-f3bd74c85ce4 | -7.6461 | -47.1258 | 2026-08-26 14:20:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 375.0 |
| 3fde6b0e-688a-3777-be71-d04f8a66f561 | -10.7598 | -54.0179 | 2026-08-26 14:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 154.1 |
| 67b1eb5d-c3f2-3b1c-9f2e-3bf40418a0c7 | -8.1671 | -54.9447 | 2026-08-26 14:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 3a462e4e-0532-3cce-9f98-c564dfb801f1 | -8.5975 | -54.715 | 2026-08-26 14:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 64ef8c9e-8582-3ff6-8744-09a9435a2fde | -12.6452 | -48.4168 | 2026-08-26 14:20:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 76.3 |
| a026a6b0-1da4-31e8-9949-7c7997090742 | -9.7246 | -49.3512 | 2026-08-26 14:20:00 | GOES-19 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 115.7 |
| add57960-28e1-3056-b4e4-b41a04b830d3 | -11.0037 | -51.1635 | 2026-08-26 14:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 157.5 |
| ec83cd58-d8d7-345a-a6c3-3a928b9774dc | -12.1701 | -50.6075 | 2026-08-26 14:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 97.7 |
| d467a812-3573-3e77-aaa9-d8e85eb6a4fa | -12.6836 | -48.4116 | 2026-08-26 14:20:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 96.6 |
| da27785f-7488-359d-a8ec-a2e542368d3c | -14.5828 | -52.0318 | 2026-08-26 14:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 99.7 |
| 0d16b521-ee76-32b9-b783-8eef602b4f78 | -9.1711 | -49.9835 | 2026-08-26 14:30:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 87.8 |
| 16667df8-b539-3218-a986-e8c878f5e5e2 | -8.8187 | -49.6093 | 2026-08-26 14:30:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 186.7 |
| 2782c9fa-92bc-361a-ab00-975d4050dbf8 | -13.3788 | -48.2022 | 2026-08-26 14:30:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 85a2b001-86be-3f64-b900-f4e571fb9cc9 | -10.7784 | -54.0368 | 2026-08-26 14:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 3bc0ea25-17b5-3412-9c60-858dd6fb334e | -11.1561 | -54.0028 | 2026-08-26 14:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 45.4 |
| a40fe5ec-cd05-39f9-a31b-46cecc649868 | -13.264 | -51.5205 | 2026-08-26 14:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 111.5 |
| dc81c5c8-4429-3133-88dd-27ea6ac17719 | -3.2178 | -61.2362 | 2026-08-26 14:30:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 101.3 |
| 4935678e-a2ee-34c0-9bb4-78ec6769a484 | -10.7598 | -54.0179 | 2026-08-26 14:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 137.0 |
| 6d9d2b7a-b087-333a-8eb7-ae0862f22952 | -10.7596 | -54.0384 | 2026-08-26 14:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 176.1 |
| 212a821d-8944-3d13-a933-baaf912e4386 | -11.7733 | -54.5396 | 2026-08-26 14:30:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 163.0 |
| 3241a4b8-684c-38ca-ac3b-930966bd647c | -12.1704 | -50.5861 | 2026-08-26 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 14ebd125-e573-3ad0-b654-e228f0bb378d | -11.7544 | -54.5414 | 2026-08-26 14:30:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 405.4 |
| ce524e85-4427-3586-9f95-aa69eb8a3b1c | -11.8161 | -47.6869 | 2026-08-26 14:30:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 474a6c7c-f40f-38ea-8456-58ee110bee51 | -10.76 | -53.9974 | 2026-08-26 14:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 71.6 |
| 5c9aae9b-2e69-3495-b7a3-aee26617e3ac | -10.4689 | -46.2028 | 2026-08-26 14:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 124.6 |
| 4a8d863b-9784-3d48-81f4-fb83e9a1130f | -3.79 | -59.284 | 2026-08-26 14:30:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 48.1 |
| eb298ef9-4b61-3f7d-bdb6-bad8489026ea | -15.7878 | -56.452 | 2026-08-26 14:30:00 | GOES-19 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 49.5 |
| d44751ad-5bd3-30b6-a964-a11200aeda11 | -8.9418 | -45.748 | 2026-08-26 14:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 66.5 |
| 4a471a97-27f7-3e2e-a0a7-d6d7c4f417c4 | -11.7546 | -54.5209 | 2026-08-26 14:30:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 647.9 |
| 3e9d67f3-4e11-3658-a9e0-43c3e501465e | -11.7973 | -47.6672 | 2026-08-26 14:30:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3a68d3ad-b69c-3632-b904-30ce6df485a2 | -9.1899 | -49.9818 | 2026-08-26 14:30:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 74.1 |
| 3b36913b-ccd6-3166-9c41-325ee7da36dd | -10.9405 | -50.255 | 2026-08-26 14:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 47.6 |
| 9f9b4083-22f4-3ef8-a00f-8cc7ed43f87d | -9.7246 | -49.3512 | 2026-08-26 14:30:00 | GOES-19 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 119.6 |
| bf901b06-e5b4-35c9-bbf4-1a5aa6659e69 | -11.8356 | -47.6621 | 2026-08-26 14:30:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c8a61603-5b40-32fe-8f36-027ed9ccb4cc | -9.659 | -55.0632 | 2026-08-26 14:30:00 | GOES-19 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 32.4 |
| d80c639e-fe50-3889-9d5f-da8f7cefa09b | -9.6022 | -55.128 | 2026-08-26 14:30:00 | GOES-19 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 71.1 |
| 4d110258-c876-32da-b086-241c6e7d34c4 | -12.1422 | -43.3707 | 2026-08-26 14:30:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 3c98d46f-3f11-35f1-902a-f29733d6932a | -11.8165 | -47.6647 | 2026-08-26 14:30:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 449f0e50-507b-3969-9360-8702617ccb7d | -13.2835 | -51.4968 | 2026-08-26 14:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 152.9 |
| 8156a38d-7581-31e7-9f03-e2e8cee492ea | -13.7552 | -51.9903 | 2026-08-26 14:30:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 71.8 |
| 7f884ee2-81a5-3312-9f3a-243506e32d6f | -10.7603 | -53.9769 | 2026-08-26 14:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 44.8 |
| d360c1ed-2e88-34e2-9505-de393f5cd852 | -11.7357 | -54.5227 | 2026-08-26 14:30:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 174.0 |
| 691a3457-13ab-3582-aa87-ba6ff79574a2 | -13.6817 | -51.7872 | 2026-08-26 14:30:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 98.3 |
| cada13f1-72bb-3037-9e2f-978b4a0cafee | -11.004 | -51.1423 | 2026-08-26 14:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 152.0 |
| 28dcaa32-6ada-34d0-9b5b-ff0fbb64c34a | -9.6776 | -55.082 | 2026-08-26 14:30:00 | GOES-19 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 103.7 |
| 23328934-6131-3f43-8715-8c81b1f5328a | -10.5596 | -50.4449 | 2026-08-26 14:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 181.8 |
| 691d1cd8-f281-3f80-b915-647716282d98 | -9.6024 | -55.1078 | 2026-08-26 14:30:00 | GOES-19 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 302.2 |
| d7eb5021-23b0-3d62-a7eb-dc68491203b4 | -10.7793 | -50.975 | 2026-08-26 14:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 46.7 |
| 836cc604-d110-30b4-bf92-0291fdb75ae4 | -11.7977 | -47.6449 | 2026-08-26 14:30:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d99a886e-a70a-3167-8c49-f44568345c32 | -11.7354 | -54.5431 | 2026-08-26 14:30:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 108.5 |
| 53de55c5-c481-339e-a270-63657efa719f | -3.1449 | -61.1808 | 2026-08-26 14:30:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 51.2 |
| 2ae8808f-f72a-3731-86a1-4bbcee6f73a2 | -9.6588 | -55.0834 | 2026-08-26 14:30:00 | GOES-19 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 86.4 |
| 1f6842ba-466e-3822-9279-f116ed8c8324 | -10.9216 | -50.2571 | 2026-08-26 14:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 87.4 |
| a69d2f94-6732-33be-a0c0-15014ad66042 | -9.1896 | -50.0032 | 2026-08-26 14:30:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 117.5 |
| 37b5e2fd-df62-3c80-a9f5-6a7f2bf36c48 | -9.7249 | -49.3296 | 2026-08-26 14:30:00 | GOES-19 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 86.6 |
| ba4e4237-9d92-33ff-90cd-ef13a71589a5 | -15.5543 | -47.106 | 2026-08-26 14:30:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 132.0 |
| 63adfe79-e734-3f6e-b02d-89c3e84b8888 | -12.6832 | -48.4337 | 2026-08-26 14:30:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 70.1 |
| 35fb9d5c-8d9f-3d25-b97a-fb4e7b8c0cb1 | -12.6836 | -48.4116 | 2026-08-26 14:30:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 104.5 |
| 33cab10c-f62c-3165-8d9c-ef400dbe8238 | -3.2178 | -61.2551 | 2026-08-26 14:30:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 54.6 |
| b03dc450-8336-35dc-a17f-e494da35a1c4 | -11.1939 | -53.9993 | 2026-08-26 14:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 90.9 |
| 1854e441-f0ec-3dbc-9484-206c3df574c3 | -12.1417 | -43.3945 | 2026-08-26 14:30:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 39592376-51d6-383b-a372-5383fc304a98 | -11.0037 | -51.1635 | 2026-08-26 14:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 220.5 |
| d0bc3059-b40d-380a-9dc1-f13297da606f | -9.1896 | -50.0032 | 2026-08-26 14:40:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 146.8 |
| f40285da-7b8b-31dc-9d3b-57b34e14e83b | -8.6415 | -50.3495 | 2026-08-26 14:40:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 134.6 |


[Clique aqui para ver as próximas entradas](README85.md)
