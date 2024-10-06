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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ee0bf232-2281-3831-811a-ac8370c360ab | -18.6586 | -57.2759 | 2024-10-06 00:26:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 96.9 |
| 3aa06794-dd6f-3871-8a75-edc263e1a1a6 | -25.0089 | -54.0785 | 2024-10-06 00:27:23 | GOES-16 | DIAMANTE D'OESTE | PARANÁ | Brasil | 4107157 | 41 | 33 | nan | nan | nan | Mata Atlântica | 52.6 |
| 4e7549aa-9ca2-3804-92af-9abf59b82762 | -25.0303 | -54.074 | 2024-10-06 00:27:23 | GOES-16 | RAMILÂNDIA | PARANÁ | Brasil | 4121257 | 41 | 33 | nan | nan | nan | Mata Atlântica | 88.4 |
| 62899ff4-bec6-3ac6-9bfe-d2defcced23b | -1.7668 | -47.1984 | 2024-10-06 00:35:16 | GOES-16 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 65.0 |
| d0cbcc49-c57b-34bd-bcab-c9fb78e50c13 | -2.6857 | -49.0965 | 2024-10-06 00:35:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 33.2 |
| 4126d85f-06e3-3b6f-9bf0-fa4f93fd7919 | -2.6858 | -49.0752 | 2024-10-06 00:35:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 234.8 |
| e9bdfa7f-2a4f-311b-b72d-5dc314b5f582 | -2.6859 | -49.0539 | 2024-10-06 00:35:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 161.8 |
| 012992be-74b0-32a7-9b36-182b4b573198 | -2.7043 | -49.0747 | 2024-10-06 00:35:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 135.1 |
| 6ede652a-0c2e-3610-8ea7-f0f0fe0de7a5 | -2.7043 | -49.0533 | 2024-10-06 00:35:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 98.2 |
| 0e2c7073-c182-3811-aa74-a392173d73d8 | -2.8169 | -48.601 | 2024-10-06 00:35:22 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 89.2 |
| 17d40667-d464-3d10-bbf8-9beb19b33f0b | -3.1298 | -48.9764 | 2024-10-06 00:35:24 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 35.2 |
| 10393216-583e-3950-af74-05beeda5bf56 | -3.1299 | -48.955 | 2024-10-06 00:35:24 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 51.4 |
| 8a152920-5623-3534-b04b-b53c89b332e8 | -3.1432 | -50.2254 | 2024-10-06 00:35:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 56.9 |
| 9fe1cee4-dfb7-3c4b-a8ae-0c6a461e2cf3 | -3.7255 | -41.6748 | 2024-10-06 00:35:27 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 52.1 |
| 8fadd220-bb17-3e1a-98fe-cac6cc039a5a | -3.8007 | -41.6229 | 2024-10-06 00:35:27 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 48.9 |
| 93177256-05de-3d2a-b73d-c2f98d3e40bc | -3.8008 | -41.5989 | 2024-10-06 00:35:27 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 240.4 |
| 03ac077a-ea1a-3db1-a00a-323b90b1af47 | -3.801 | -41.575 | 2024-10-06 00:35:27 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 110.3 |
| 8402e808-83ff-32a0-adc3-dad3435f6936 | -3.7935 | -49.4636 | 2024-10-06 00:35:28 | GOES-16 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 40.2 |
| c9b3d80c-b143-3112-bc1a-c4a52482722d | -5.5716 | -44.8927 | 2024-10-06 00:35:37 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 118.5 |
| 6d6a4c5b-69d1-38e3-8596-72d1e40b8425 | -5.5718 | -44.87 | 2024-10-06 00:35:37 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 197.7 |
| c0c29f67-934c-32ce-9d16-0a7a2190a4e4 | -5.5905 | -44.8687 | 2024-10-06 00:35:38 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 81.2 |
| 01616d26-5687-306c-8d7c-592417da3605 | -5.8214 | -44.1426 | 2024-10-06 00:35:39 | GOES-16 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 163.5 |
| 4a8ecaf6-0305-39be-9760-ca4aed6b4356 | -5.8216 | -44.1196 | 2024-10-06 00:35:39 | GOES-16 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 123.3 |
| 8c38e8e5-3b80-39d0-828a-ccb19a518f6a | -6.9514 | -59.0666 | 2024-10-06 00:35:46 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 117.4 |
| d27efcc3-337d-3f8d-8bef-9c06afd6012f | -6.9699 | -59.0658 | 2024-10-06 00:35:46 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 68.4 |
| 8dbf936f-e2fc-3271-86da-85e9844c2c4b | -7.1532 | -59.2898 | 2024-10-06 00:35:47 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 74.5 |
| 96dbfaf4-b16d-35bc-a7ec-795a7778ea8a | -7.4995 | -34.8464 | 2024-10-06 00:35:48 | GOES-16 | PITIMBU | PARAÍBA | Brasil | 2511905 | 25 | 33 | nan | nan | nan | Mata Atlântica | 104.4 |
| fba0c46a-04a7-310b-ad46-9a11abc50679 | -7.4741 | -72.6801 | 2024-10-06 00:35:49 | GOES-16 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 44.5 |
| e9d7e203-e048-3683-b476-68ee6a2ebf14 | -7.8698 | -54.9029 | 2024-10-06 00:35:51 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 203c1708-40c7-370e-b9ff-cbcfa09b4472 | -7.87 | -54.8828 | 2024-10-06 00:35:51 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 78.2 |
| 95525be7-cebb-3a4f-8f1f-6dde8bcf58b1 | -7.9639 | -54.7764 | 2024-10-06 00:35:51 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 0a0aa25c-95c1-36bf-ae62-8eb1a3040c3b | -7.964 | -54.7562 | 2024-10-06 00:35:51 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 67.6 |
| f343098b-e54e-332e-afc6-b9f059a5ded1 | -7.9825 | -54.7752 | 2024-10-06 00:35:52 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 57.1 |
| c5bd758b-c15f-35a3-931e-9710c276b5bc | -7.9826 | -54.7551 | 2024-10-06 00:35:52 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 10e85c1d-5a36-3209-8e50-a3cca6f51a53 | -8.1081 | -55.3098 | 2024-10-06 00:35:52 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 4f143874-980f-3b27-8db4-15e7748e0056 | -8.2139 | -61.2022 | 2024-10-06 00:35:53 | GOES-16 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 65.5 |
| 2d19368b-8039-33a7-9479-583648d0ccbc | -8.2324 | -61.2014 | 2024-10-06 00:35:53 | GOES-16 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 54.7 |
| 269fcaf0-4781-3a0e-8ab5-6377a197f003 | -9.1759 | -61.5794 | 2024-10-06 00:35:59 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 74.5 |
| e3905772-0208-386a-9f8e-85bd48d73f4f | -9.176 | -61.5603 | 2024-10-06 00:35:59 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 70.2 |
| f2d2c2d3-5460-3d3a-9b77-8c735bb587c0 | -9.3278 | -46.5385 | 2024-10-06 00:35:59 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 72.4 |
| 273331b2-393a-3168-9cff-c21e1b54ae6f | -9.3464 | -46.5589 | 2024-10-06 00:35:59 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 83.2 |
| 61bc3d0f-ebf7-3fe9-bdff-735ee7f80085 | -9.3467 | -46.5365 | 2024-10-06 00:35:59 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 105.3 |
| 043cd45c-dd99-302d-be6c-29e9408b8df7 | -9.365 | -51.0687 | 2024-10-06 00:35:59 | GOES-16 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 59.7 |
| b3e79a0c-de74-3139-b375-e90807796575 | -9.3637 | -64.3378 | 2024-10-06 00:36:00 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 52.1 |
| 90c27813-ae5c-3159-8b66-f6f4f99e894b | -9.3638 | -64.319 | 2024-10-06 00:36:00 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 74.9 |
| c7d260d1-7083-3100-9971-93d0aa2bdc8b | -9.6691 | -47.8328 | 2024-10-06 00:36:01 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 126.0 |
| 4e4b75fd-5031-3612-b8d1-939aa1001625 | -9.6694 | -47.8108 | 2024-10-06 00:36:01 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 71.1 |
| 31798831-42c4-310d-bdd7-600a337d1d9c | -9.6877 | -47.8528 | 2024-10-06 00:36:01 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 73.9 |
| 0cfa6413-59c5-3e25-a828-c836b5f64aa5 | -9.688 | -47.8308 | 2024-10-06 00:36:01 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 258.0 |
| 7f4f2438-eaed-3d5b-a5c3-bd00512f50f6 | -9.6883 | -47.8088 | 2024-10-06 00:36:01 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 129.8 |
| 421bf151-f1c9-34ff-86d2-cdff8b81afa8 | -9.7069 | -47.8288 | 2024-10-06 00:36:01 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 72.4 |
| 86104ecf-1705-3859-9206-ef7bc90fe161 | -9.8552 | -60.2966 | 2024-10-06 00:36:02 | GOES-16 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 53.0 |
| e3abe006-3443-3245-b90b-39b18a335918 | -10.6962 | -53.0354 | 2024-10-06 00:36:07 | GOES-16 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 58.9 |
| f6474299-2569-33d3-8aff-23582fbcff7e | -11.0966 | -54.2336 | 2024-10-06 00:36:09 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 75.5 |
| 701769d2-7802-39cd-a8d5-ea8f6a9817ee | -11.1155 | -54.2319 | 2024-10-06 00:36:09 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 55.9 |
| 69d1fa00-b3ac-38d5-b89d-6d645d48538c | -12.0211 | -63.7478 | 2024-10-06 00:36:15 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 106.4 |
| 2106d3b9-4850-372f-8277-6230b5524482 | -12.5093 | -45.3017 | 2024-10-06 00:36:16 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 72.8 |
| db34fa66-3b81-32ec-a4dc-fa451ee77a4d | -12.6089 | -53.1338 | 2024-10-06 00:36:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 129.2 |
| 539ac7cc-203d-3bcc-accd-f3e5eaef8b9d | -12.6092 | -53.1129 | 2024-10-06 00:36:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 107.0 |
| 990e5766-3912-33db-ba57-88de531376ba | -12.628 | -53.1317 | 2024-10-06 00:36:18 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 148.3 |
| e74a6054-3bd2-3f62-93e3-5e40ce9e718e | -12.6283 | -53.1108 | 2024-10-06 00:36:18 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 198.8 |
| 0a15c746-b147-33fd-b7cf-ae6c0e7d39c4 | -12.6474 | -53.1088 | 2024-10-06 00:36:18 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 134.5 |
| fb9a4908-4562-3785-806d-9c2a0ff19f97 | -12.6532 | -54.0415 | 2024-10-06 00:36:18 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 104.4 |
| beae9917-6c3b-3aea-8181-6adfa3b35341 | -12.6535 | -54.0208 | 2024-10-06 00:36:18 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 83.1 |
| 84746ac1-81c1-3f39-b6ed-851e690c03fc | -12.7627 | -50.5567 | 2024-10-06 00:36:18 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 105.7 |
| ccb47cbc-8d71-3ac2-bc60-1e41b0f02020 | -12.763 | -50.5352 | 2024-10-06 00:36:18 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 241.5 |
| e661f41d-ee48-3340-ae58-2db8ff7ede64 | -12.7634 | -50.5136 | 2024-10-06 00:36:18 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 94.3 |
| b0ebca42-be41-3669-824e-cd72229501c3 | -13.6724 | -51.1911 | 2024-10-06 00:36:23 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 104.2 |
| f9bf0639-a912-3f19-a798-00533d3cdc1c | -16.3959 | -57.3641 | 2024-10-06 00:36:38 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 59.6 |
| 2532a1b6-5b06-35f3-aa77-167c479aabb6 | -16.4362 | -57.278 | 2024-10-06 00:36:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 53.5 |
| c22c05b9-bacb-360c-8089-70517d3b450b | -16.5745 | -57.16 | 2024-10-06 00:36:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 59.3 |
| b8c4233c-7c34-3f05-8bbc-dbe2e13f4b92 | -16.614 | -55.9214 | 2024-10-06 00:36:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 195.8 |
| 3bf45cb5-bc9e-374b-b146-a8c7f33e8557 | -16.6143 | -55.9007 | 2024-10-06 00:36:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 140.9 |
| e3132d93-0146-3bbb-bc3f-eb85c49b5efc | -16.6398 | -55.5452 | 2024-10-06 00:36:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 149.6 |
| c5f92258-509f-37b2-ae8c-ed61e60d9e73 | -16.6402 | -55.5243 | 2024-10-06 00:36:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 110.0 |
| d16f8e29-8942-3944-af5a-990ed56b5ace | -16.6594 | -55.5427 | 2024-10-06 00:36:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 100.3 |
| 7d97256e-9471-3125-bc45-388bed43e08a | -16.6871 | -57.4536 | 2024-10-06 00:36:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 68.4 |
| 3807e451-7578-37bb-a1c1-aebd99933e71 | -16.7647 | -57.4856 | 2024-10-06 00:36:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 99.0 |
| 9f07f953-7a9c-3682-9209-a95a9d4a23f9 | -16.8238 | -57.4584 | 2024-10-06 00:36:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 93.0 |
| c0bbb636-4e46-3b2a-9095-2dec02edd393 | -16.8668 | -54.8694 | 2024-10-06 00:36:41 | GOES-16 | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 115.6 |
| 0400d3a5-bc2b-363f-8886-dce24803b4de | -16.8672 | -54.8485 | 2024-10-06 00:36:41 | GOES-16 | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 165.6 |
| 029b4702-6504-3a59-ade4-a888bb4b9efc | -16.9283 | -55.8405 | 2024-10-06 00:36:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 114.1 |
| e3ccf320-a099-3a18-80f5-8f4dfac4b756 | -16.9287 | -55.8197 | 2024-10-06 00:36:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 115.2 |
| 6e143d24-0311-36e1-b5d1-df29adccfce8 | -16.9545 | -56.6226 | 2024-10-06 00:36:41 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 115.8 |
| 02150284-5bb9-38ca-8e18-b10b99a1ab9b | -17.3837 | -42.6483 | 2024-10-06 00:36:42 | GOES-16 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 71.5 |
| 10b58031-7c1c-338d-b18e-2c4a85002c4b | -17.0007 | -55.0607 | 2024-10-06 00:36:42 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 101.9 |
| fca30fc0-41cd-3f20-92c5-58deddc8c75e | -17.0203 | -55.0581 | 2024-10-06 00:36:42 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 110.6 |
| b1f1b98d-e08f-3a07-b3e5-b1992e885a17 | -17.0207 | -55.0371 | 2024-10-06 00:36:42 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 93.5 |
| 6474035e-d5d4-3f96-ae9d-0ce7a7f78bc8 | -17.1375 | -57.4221 | 2024-10-06 00:36:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 93.5 |
| 7fc6559a-d931-3e11-bd70-4638428ae946 | -17.812 | -53.7859 | 2024-10-06 00:36:46 | GOES-16 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 283.9 |
| a2f64828-fa20-332d-b65b-1d1e71289f0c | -17.8125 | -53.7645 | 2024-10-06 00:36:46 | GOES-16 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 261.5 |
| 8df614fe-7490-313c-94f6-48481105efbb | -17.8319 | -53.7829 | 2024-10-06 00:36:46 | GOES-16 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 158.9 |
| 35dc5060-241b-3483-b445-8d96b3c92a32 | -17.8323 | -53.7616 | 2024-10-06 00:36:46 | GOES-16 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 153.3 |
| ed3de73c-5021-3545-ad79-c248a3db4bcd | -18.6387 | -57.2785 | 2024-10-06 00:36:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 86.1 |
| 81b474b1-0410-3cbd-88da-d2ca663a2f59 | -18.6586 | -57.2759 | 2024-10-06 00:36:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 100.3 |
| 4810b0c6-d0f3-3b02-a31b-0aabd0d7f3e3 | -18.659 | -57.2552 | 2024-10-06 00:36:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 77.8 |
| c66288fe-6803-3fd5-9233-a0732298ff4e | -25.0089 | -54.0785 | 2024-10-06 00:37:23 | GOES-16 | DIAMANTE D'OESTE | PARANÁ | Brasil | 4107157 | 41 | 33 | nan | nan | nan | Mata Atlântica | 81.8 |
| 701792ec-8122-3118-8918-876d6beb5a93 | -25.0303 | -54.074 | 2024-10-06 00:37:23 | GOES-16 | RAMILÂNDIA | PARANÁ | Brasil | 4121257 | 41 | 33 | nan | nan | nan | Mata Atlântica | 70.6 |
| 73488f81-6606-317b-b196-da0cf1e116f8 | -25.025801 | -54.050098 | 2024-10-06 00:44:25 | METOP-B | DIAMANTE D'OESTE | PARANÁ | Brasil | 4107157 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 4cecc0b9-f633-35c6-9b58-a6715e9bfea1 | -25.028099 | -54.063301 | 2024-10-06 00:44:25 | METOP-B | DIAMANTE D'OESTE | PARANÁ | Brasil | 4107157 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |


[Clique aqui para ver as próximas entradas](README5.md)
