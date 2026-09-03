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

## Dados Diários - Página 72

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 639a4558-ba8b-339c-b80a-18bc877920c2 | -7.5662 | -61.3049 | 2026-09-03 17:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 48.1 |
| 6e43d83e-5db7-312d-a56d-6a785157d94d | -3.4185 | -61.3273 | 2026-09-03 17:00:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 01416ccf-f6c7-3fd5-a1f7-06b6a6824cde | -3.0904 | -61.0871 | 2026-09-03 17:10:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 46a645a2-53e4-3834-856b-6aeb7b4635f6 | -11.2966 | -50.5367 | 2026-09-03 17:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 88.3 |
| 846e67d0-4ad8-3989-865b-b3848d946dba | -3.1266 | -61.2188 | 2026-09-03 17:10:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 4c5f2f5c-9599-3ac6-afac-9c2dd9331a3e | -11.3156 | -50.5346 | 2026-09-03 17:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 83.4 |
| 559bae75-f154-323b-ada3-8cba84ace393 | -3.7828 | -61.7545 | 2026-09-03 17:10:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 64.4 |
| 74ae7ea7-774f-39ee-81d7-739dc7ca54a3 | -3.1449 | -61.1808 | 2026-09-03 17:10:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 85.6 |
| 7fcb3f63-338e-3f08-88c4-75dcf1e0c34a | -3.1267 | -61.1811 | 2026-09-03 17:10:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 71.1 |
| b4a6285b-7856-3521-a1c1-d34a953ca88b | -7.2005 | -60.6897 | 2026-09-03 17:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 38.3 |
| f9f82804-c9dd-3cb1-b575-aa8d02fdffcf | -10.4142 | -50.0112 | 2026-09-03 17:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 78.0 |
| a3bd5766-e198-3305-b7ab-f78dcacfd576 | -5.5649 | -60.193 | 2026-09-03 17:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 48.7 |
| a64c01c0-d0ab-3cdb-bc1e-247a9b42655c | -7.7707 | -61.087 | 2026-09-03 17:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 43.2 |
| 18b035d1-c15a-379f-b158-f0dcbc06cb79 | -6.5486 | -58.5413 | 2026-09-03 17:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 7648ef01-ec3b-38db-97e8-f849813776ed | -3.7533 | -59.3231 | 2026-09-03 17:10:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 75.8 |
| 786e37b9-904e-37ea-bf75-5ff98f33e025 | -3.4003 | -61.3087 | 2026-09-03 17:10:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 86.1 |
| f6588037-80dd-3bf0-b7de-a0bbd4932c30 | -3.4185 | -61.3273 | 2026-09-03 17:10:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 66.3 |
| c951065e-00ce-32b9-b7a5-0abb95c673a2 | -6.6766 | -58.7299 | 2026-09-03 17:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 228694c4-049c-3702-9242-63601540b6cd | -6.6226 | -58.4995 | 2026-09-03 17:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 45.4 |
| fc784f60-fa2f-3690-8d63-6a6ccba5f9bf | -19.1144 | -57.3823 | 2026-09-03 17:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 122.4 |
| e20c6940-054d-34e3-8c92-02458b280651 | -9.4814 | -60.4324 | 2026-09-03 17:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 53.2 |
| 59047a5f-4bb6-3296-b158-4fbd47418c25 | -3.4002 | -61.3276 | 2026-09-03 17:10:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 110.3 |
| 9408c923-2928-3450-87d3-364e812d87ec | -7.2933 | -60.5905 | 2026-09-03 17:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 43.6 |
| 0290b5c8-cd7b-31fd-9ba0-92995c4c330c | -3.0347 | -61.4657 | 2026-09-03 17:10:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 3e5335b7-2163-3a59-9c7e-e433d576ba5f | -3.7645 | -61.7548 | 2026-09-03 17:10:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 59.7 |
| aa4fca39-e7f0-3f7f-b418-969ebb86d736 | -5.1 | -37.84 | 2026-09-03 17:15:00 | MSG-03 | QUIXERÉ | CEARÁ | Brasil | 2311504 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| a858306c-363b-33b2-b328-1eb7e1a44967 | -5.07 | -37.84 | 2026-09-03 17:15:00 | MSG-03 | QUIXERÉ | CEARÁ | Brasil | 2311504 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| ec4d138b-d8cc-36b6-9f98-7d6737b2505e | -10.87 | -45.34 | 2026-09-03 17:15:00 | MSG-03 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 4ea81e4d-01e4-34be-998a-71da7b28005e | -3.3871 | -59.3883 | 2026-09-03 17:20:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 76.0 |
| fa00f567-1672-369d-ba4b-a647044d1551 | -3.7717 | -59.2844 | 2026-09-03 17:20:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 0c76e424-d7bb-3c74-899a-6c095c521087 | -6.7463 | -59.4416 | 2026-09-03 17:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 200.6 |
| 40001beb-44a6-3fd6-99a5-557af726f765 | -8.3718 | -62.697 | 2026-09-03 17:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 47.5 |
| 6a6e0f47-c1dd-3e0d-a8b6-193cdbfcdd8b | -11.6202 | -50.4789 | 2026-09-03 17:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 86.5 |
| 46e77bd8-7fd4-3ee0-b0e9-e5317e0b5b78 | -3.4002 | -61.3276 | 2026-09-03 17:20:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 102.1 |
| 8228ba8e-e56b-3e3a-b51b-451632ef14f6 | -11.4898 | -50.301 | 2026-09-03 17:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 91.9 |
| a13deec3-9014-31bd-b819-091f5eafaa0d | -9.4814 | -60.4324 | 2026-09-03 17:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 48.4 |
| 86ec0eea-622c-3004-b119-f05036a64f37 | -3.1449 | -61.1808 | 2026-09-03 17:20:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 68.8 |
| f6641f4b-327a-3250-a513-6ad994def1f9 | -3.2361 | -61.217 | 2026-09-03 17:20:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 69.9 |
| 3548db2d-e60a-34b3-a04b-642290aea599 | -6.6013 | -59.0037 | 2026-09-03 17:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 54.9 |
| e0bf4a7b-7fab-38c7-b374-caa1b78234de | -3.0904 | -61.0871 | 2026-09-03 17:20:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 55.6 |
| f260484e-fc1b-33e3-b85a-d82cde2fe5ef | -7.2006 | -60.6706 | 2026-09-03 17:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 7e4edba4-dfd5-3a12-ac44-eff34b59cb25 | -7.5668 | -61.2096 | 2026-09-03 17:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 72.5 |
| 70ab807c-fa48-3027-92b5-b35c1e4354bc | -3.1815 | -61.1424 | 2026-09-03 17:20:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 112.7 |
| 640477f4-60ed-352c-ae46-27da2f6c1be0 | -3.9707 | -60.0258 | 2026-09-03 17:20:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 2a7e73d8-5c8a-3c45-b77b-ecfb9f5c9f11 | -7.1822 | -60.6713 | 2026-09-03 17:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 35.2 |
| d77663cf-9ae5-37b9-b593-c06559a771bd | -7.2932 | -60.6096 | 2026-09-03 17:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 55.9 |
| 251e4958-67a9-3b6a-a1ab-3515eb99579c | -9.12 | -61.6011 | 2026-09-03 17:20:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 49.1 |
| 96411125-5850-30d6-81fb-0a0db769fd3f | -11.2966 | -50.5367 | 2026-09-03 17:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 94.2 |
| 3a4b5759-accd-34e3-abad-73f86f36d9b0 | -3.1267 | -61.1811 | 2026-09-03 17:20:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 73.3 |
| 18479365-495a-3a2f-82cc-57f4993139b8 | -6.6226 | -58.4995 | 2026-09-03 17:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 47.7 |
| 0c1c6201-dcb6-30a2-b80c-d48a0674639f | -3.7828 | -61.7545 | 2026-09-03 17:20:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 65.6 |
| b2777add-9160-33e9-8d69-6a3e5fa6bcbb | -19.1147 | -57.3615 | 2026-09-03 17:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 108.8 |
| c9eaaefd-be3a-3652-8534-f710cccca53f | -3.4003 | -61.3087 | 2026-09-03 17:20:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 82.7 |
| 65b9d222-33d3-395c-8e4d-1dc04e8c1567 | -11.3156 | -50.5346 | 2026-09-03 17:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 79.2 |
| 7a084746-ccd4-3567-bf40-8820c0fd482c | -3.7645 | -61.7548 | 2026-09-03 17:20:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 2709dae9-cbe0-326a-ae30-5e28b86b5af9 | -7.2746 | -60.6294 | 2026-09-03 17:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 38.5 |
| 8c1b3fd9-cebc-3f38-9286-b087f2bc2438 | -8.5542 | -63.1814 | 2026-09-03 17:20:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 85.5 |
| ebb9626b-1d0a-3612-8351-4dc10a5c6530 | -10.9592 | -50.2744 | 2026-09-03 17:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 102.3 |
| 81970eae-1822-32b4-91d2-0b2474e5901e | -6.6766 | -58.7299 | 2026-09-03 17:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 66.5 |
| 2780b841-85a1-3897-b439-70d8c656a7ee | -8.3717 | -62.716 | 2026-09-03 17:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 46.4 |
| 09ebebac-240a-3b55-8e12-651bf5350173 | -7.2927 | -60.7052 | 2026-09-03 17:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 44.3 |
| 13c64678-1949-3d8c-b032-36a6e37d379b | -12.0705 | -64.7721 | 2026-09-03 17:20:00 | GOES-19 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 38.6 |
| 0f7e1e07-997c-3781-bfc7-8fd42ae55224 | -3.1083 | -61.2191 | 2026-09-03 17:20:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 64.2 |
| 534ef2a9-3aaa-3341-9a95-7499647e5b6b | -19.1144 | -57.3823 | 2026-09-03 17:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 110.7 |
| 9075bd6f-947b-3f28-8f88-d6c2fb14fc4c | -11.2295 | -51.2667 | 2026-09-03 17:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 78.2 |
| a74c6467-e93a-3da1-b94d-bc7aadf8087d | -19.1144 | -57.3823 | 2026-09-03 17:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 107.4 |
| e2f22281-3c01-3b54-a90d-4d18d6b817ec | -7.3117 | -60.6089 | 2026-09-03 17:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 79.1 |
| c60b49f5-1b9e-3cf2-8ae5-a2dda042a0b1 | -11.6573 | -50.5389 | 2026-09-03 17:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 106.2 |
| 79c0e448-cc94-39d6-90c6-775de2775133 | -7.2006 | -60.6706 | 2026-09-03 17:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 69.0 |
| 1971fea1-2141-38a0-8d12-a80045f3ec4c | -19.1347 | -57.3589 | 2026-09-03 17:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 92.6 |
| 43073f33-f4d8-3f61-a82b-6930a4c57c55 | -11.6389 | -50.4982 | 2026-09-03 17:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 91.6 |
| a7ea1baa-8c2b-3ed2-8c43-ad130c4f61bc | -11.172 | -51.3151 | 2026-09-03 17:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 87.4 |
| c85e738e-fd46-340e-b101-e6aae3476c53 | -10.9592 | -50.2744 | 2026-09-03 17:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 107.3 |
| e927291c-18f5-3fef-b9cf-988703045c6c | -6.6765 | -58.7492 | 2026-09-03 17:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 64.4 |
| b2394323-37c3-30b1-8a93-2b181bbdea43 | -6.6766 | -58.7299 | 2026-09-03 17:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 64.9 |
| d06c4b6b-697d-316f-b153-6759612adc17 | -6.9872 | -59.2582 | 2026-09-03 17:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 59.8 |
| e2c3bdca-f3f1-3a28-9857-c187fb0498bf | -6.6226 | -58.4995 | 2026-09-03 17:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 44.8 |
| e8d651d8-9d8d-3e07-ac6b-13d16dc61221 | -11.2106 | -51.2688 | 2026-09-03 17:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 93.4 |
| e35f54cc-50ad-3118-b0c1-c00b2d9dd5cc | -6.8062 | -58.6469 | 2026-09-03 17:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 81.3 |
| 2e82e294-f04f-39a9-bc08-09fc90aa64d9 | -11.4895 | -50.3225 | 2026-09-03 17:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 94.9 |
| 20f03db4-388b-30e2-a605-07b7a5f07d69 | -6.7123 | -58.9412 | 2026-09-03 17:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 74.4 |
| d5ec8f43-23b9-3012-b8a0-c41948f71e8e | -11.6577 | -50.5175 | 2026-09-03 17:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 97.2 |
| 45346a42-393c-39e9-94f2-1bd6d0b17fc3 | -19.1147 | -57.3615 | 2026-09-03 17:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 102.9 |
| ba85eac9-4170-3ab2-9d5f-d883e0be902c | -11.4898 | -50.301 | 2026-09-03 17:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 99.3 |
| 17c3dbbe-992d-3094-9f0f-5d26fb41d56e | -11.5086 | -50.3204 | 2026-09-03 17:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 110.8 |
| affb35d5-271b-34eb-9cea-a50f5889ab6c | -9.1386 | -61.6002 | 2026-09-03 17:40:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 189.8 |
| 1cf864b7-ad50-3e7e-b1ca-5a702a6bf002 | -11.172 | -51.3151 | 2026-09-03 17:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 87.9 |
| f3a9b40f-75be-366d-ba31-b4fe1b08509c | -20.8174 | -57.6709 | 2026-09-03 17:40:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 90.0 |
| 24918b48-2216-3ef0-be3c-16d776d79c8b | -8.5728 | -63.1807 | 2026-09-03 17:40:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 71.1 |
| 7cf647d2-ffb0-3ef3-aed9-2111161652e6 | -10.8396 | -50.7139 | 2026-09-03 17:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 87.7 |
| 946c39d6-37f0-37fa-9504-3c1870e922a9 | -10.8582 | -50.7332 | 2026-09-03 17:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 81.1 |
| 959691d8-1774-375d-8e9f-edae74f2e853 | -3.1449 | -61.1997 | 2026-09-03 17:40:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 67.0 |
| a17c6002-6161-36ea-8aa5-c870ca5f1eeb | -6.6938 | -58.942 | 2026-09-03 17:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 49.1 |
| 68844a27-c2da-3ac9-acb7-f4e09b589829 | -1.4944 | -54.2563 | 2026-09-03 17:40:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 99.8 |
| 06fe1bc0-0d0e-3997-928e-bb96f9ecab02 | -1.5128 | -54.2561 | 2026-09-03 17:40:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 84.1 |
| df31e79f-e5d3-3f2c-9936-4d938a03c81c | -3.218 | -61.1607 | 2026-09-03 17:40:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 127.5 |
| be817769-f7cf-3005-abfc-93d170209bec | -6.6036 | -58.5972 | 2026-09-03 17:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 46.3 |
| 743e83e8-fefe-38f7-991d-93ae8e605577 | -3.4002 | -61.3276 | 2026-09-03 17:40:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 99.1 |
| c0fd289f-0b11-3640-9ef2-8574a4eaf007 | -7.2746 | -60.6294 | 2026-09-03 17:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 48.8 |
| 900552e1-d957-30ca-b228-f90eab484805 | -6.695 | -58.7291 | 2026-09-03 17:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 64.5 |


[Clique aqui para ver as próximas entradas](README73.md)
