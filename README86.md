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

## Dados Diários - Página 86

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| efc20eb1-2411-38e2-af4f-298cf7a4e827 | -9.8619 | -64.9958 | 2026-10-06 15:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 47.5 |
| 702c6ead-ff21-351f-a510-aec2aee79254 | -11.4503 | -43.4091 | 2026-10-06 15:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 211.8 |
| 272e7e90-9176-3b3c-a9db-b35fd38db4d6 | -9.1076 | -67.703 | 2026-10-06 15:10:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 43.5 |
| 7b0c7425-aa9f-3d35-a806-f68464859d95 | -0.3952 | -52.0562 | 2026-10-06 15:10:00 | GOES-19 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 73.6 |
| 943bfea1-4023-3238-8e98-0dbe02f65f3b | -11.6758 | -43.658 | 2026-10-06 15:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 373.8 |
| d6ce2511-0f6c-35b7-86d6-8f446eda00e6 | -10.9762 | -45.4094 | 2026-10-06 15:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 133.3 |
| 703e236b-4f54-329f-a972-62bb05057c02 | 1.7855 | -55.5461 | 2026-10-06 15:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 83.0 |
| 009124ac-faaf-3aa3-a14e-aab90081554d | -9.9175 | -65.0313 | 2026-10-06 15:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 2688b113-c80f-3433-baef-f690e3df840d | 1.7303 | -55.6456 | 2026-10-06 15:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 67.3 |
| e039db3a-c6a3-323d-b24c-920c48933cb7 | -3.2398 | -53.8813 | 2026-10-06 15:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 146.4 |
| 2f1a350f-f216-3ba5-8570-1c43ab454880 | 1.5649 | -55.9829 | 2026-10-06 15:10:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 69.9 |
| e2f76e43-7625-34ba-a643-585cb5609492 | -6.457 | -55.441 | 2026-10-06 15:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 73.2 |
| 574642e4-a997-36c5-be50-a9d534329394 | 1.8767 | -55.7424 | 2026-10-06 15:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 75.2 |
| 6bb44c67-e841-331c-b56c-7aae930212da | -11.6566 | -43.661 | 2026-10-06 15:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 127.0 |
| 62104f30-ef9b-3489-bf4f-d1c1f0d9f9a7 | -11.6378 | -43.6403 | 2026-10-06 15:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 146.0 |
| 54a99914-bacb-39ec-9d21-4a1e9a9df013 | -11.657 | -43.6373 | 2026-10-06 15:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 249.5 |
| 77d79f23-95be-3857-8a08-ba7c60625fe4 | -4.54701 | -37.82333 | 2026-10-06 15:16:00 | NPP-375 | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 6.7 |
| c93f9795-436c-3929-976d-8173d3bea593 | -7.24627 | -37.13853 | 2026-10-06 15:16:00 | NPP-375 | DESTERRO | PARAÍBA | Brasil | 2505402 | 25 | 33 | nan | nan | nan | Caatinga | 12.4 |
| 4f16d154-fe4a-383f-85f1-d9f5941d14c3 | -4.54515 | -37.82475 | 2026-10-06 15:16:00 | NPP-375 | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 8.9 |
| c0913453-4363-3833-bdc4-60bd2cb8e0f5 | -9.0584 | -66.1073 | 2026-10-06 15:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 47.2 |
| da58577f-913d-33be-a106-1d8e83194689 | -9.8619 | -64.9958 | 2026-10-06 15:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 54.2 |
| c79f0cb7-7c59-3253-bf20-4c1ff7090772 | -8.6101 | -67.1783 | 2026-10-06 15:20:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 54.6 |
| ee5fd589-6574-36d4-83ec-4ffac7aed476 | 1.4922 | -55.688 | 2026-10-06 15:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 48.1 |
| 44b77656-db5d-3b6e-95ac-4aafdb713aaa | 3.0732 | -60.5949 | 2026-10-06 15:20:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 65.9 |
| f8e8928d-2088-335b-8c63-de341bcc5ccb | -9.0098 | -69.3852 | 2026-10-06 15:20:00 | GOES-19 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 111.7 |
| 996f0853-11b2-30f1-9870-b83814ada030 | 1.8767 | -55.7424 | 2026-10-06 15:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 76.6 |
| 23fc9377-6926-3cc6-bbff-19454fde14e9 | -2.7879 | -57.6649 | 2026-10-06 15:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 108.2 |
| 80167879-e60a-3fc0-856b-cea48c55cce1 | -9.1334 | -65.9 | 2026-10-06 15:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 47.0 |
| fdb92677-655b-338d-984b-b0a702c8df33 | -11.4503 | -43.4091 | 2026-10-06 15:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 187.3 |
| 3f7cf675-f1f6-3c41-9f55-6ec1f0576157 | -7.7127 | -73.0429 | 2026-10-06 15:20:00 | GOES-19 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 46.9 |
| d20a7cc0-53c1-3b43-9736-912bd8478871 | -2.7713 | -57.0229 | 2026-10-06 15:20:00 | GOES-19 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 55.4 |
| e9fa3ff3-da45-3062-b51c-fa0698e9a701 | -9.1613 | -68.2568 | 2026-10-06 15:20:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 75.8 |
| b8a6d5ca-a2ad-3811-9da0-d27dfa264449 | -8.6034 | -69.3374 | 2026-10-06 15:20:00 | GOES-19 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 57.8 |
| db862cb5-b01f-323f-b37a-1a3ba9b742c8 | -11.0485 | -45.6511 | 2026-10-06 15:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 114.6 |
| a10011b5-0d51-3588-b550-00c6c0c704e4 | -0.3952 | -52.0562 | 2026-10-06 15:20:00 | GOES-19 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 69.8 |
| 2c0bd9ab-e2fa-3c94-a783-3c54e6fc75ed | 1.8584 | -55.7624 | 2026-10-06 15:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 77.0 |
| cbfdad2d-cabd-3403-a909-1836cb0e3af8 | -9.1511 | -66.0859 | 2026-10-06 15:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 232f6384-d7ba-3230-a297-0310635ba2b2 | -9.077 | -66.0881 | 2026-10-06 15:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 44.5 |
| ee74c664-21cd-3eb2-ab8a-c1809ad42478 | -4.365 | -43.9165 | 2026-10-06 15:20:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 116.4 |
| 2f3cbbb5-103f-3ee3-8e58-5e78907f7872 | -9.1222 | -64.3843 | 2026-10-06 15:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 730a2763-b8a0-3ffa-877b-55ac08faae9c | -9.0097 | -69.4036 | 2026-10-06 15:20:00 | GOES-19 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 83.0 |
| 59ae0be3-c4fd-3261-91b7-d1f28fb01a7f | -8.5916 | -67.1973 | 2026-10-06 15:20:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 50.5 |
| a0f37af8-e095-31c2-8b11-37c7757c2035 | -9.1407 | -64.4024 | 2026-10-06 15:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 7008f859-0ed8-346f-aca3-4c1c11177500 | 3.128 | -60.594 | 2026-10-06 15:20:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 150.4 |
| bf0bc721-160c-363a-b734-c5561d416495 | -9.5174 | -67.1544 | 2026-10-06 15:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 47.0 |
| 6d4e8a82-b318-3268-ac76-fd9b657593d5 | -9.1408 | -64.3836 | 2026-10-06 15:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 63.8 |
| d29737f1-e790-3107-9f47-3655fd49be6c | -8.9257 | -66.8549 | 2026-10-06 15:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 43.7 |
| c8c5af51-d9a5-3253-ab3e-d41572e0b4f3 | 1.9864 | -55.8789 | 2026-10-06 15:20:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 93.1 |
| 5b3b23e6-bc83-36e1-92a8-593b93de6ba5 | -9.9175 | -65.0313 | 2026-10-06 15:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 62.3 |
| d803e626-007e-3810-8e17-9095eaeabe67 | 0.3221 | -51.0038 | 2026-10-06 15:20:00 | GOES-19 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 85.0 |
| 816aca0b-f3b6-3a30-98e2-1fb8f807598b | -2.7879 | -57.6843 | 2026-10-06 15:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 119.3 |
| 5eaea77a-db24-3120-815e-88ad36c372f4 | -9.0347 | -67.39 | 2026-10-06 15:20:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 84.1 |
| 71fc96e8-051a-3909-904a-f2f562aaab79 | -11.4503 | -43.4091 | 2026-10-06 15:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 181.1 |
| 614398b9-7433-3689-994a-62a5fede945b | 1.8767 | -55.7424 | 2026-10-06 15:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 78.2 |
| 1bc231e0-7f53-35f5-bbfb-92db31b7656f | 1.8951 | -55.7224 | 2026-10-06 15:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 73.9 |
| 5992eff9-135f-3005-b4b7-301930a9f13f | -11.657 | -43.6373 | 2026-10-06 15:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 164.7 |
| 5c4bf7e6-cb8e-3e2b-aeff-5352e130e330 | -10.9571 | -45.412 | 2026-10-06 15:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 113.2 |
| 07dc1f5c-6623-30bf-b462-bb4ef4f66586 | -9.0584 | -66.1073 | 2026-10-06 15:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 51.0 |
| db8a9cb5-0ffd-3b1c-a8bf-4b23830d8e15 | -3.7117 | -55.4667 | 2026-10-06 15:30:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 51.3 |
| 0af5d67b-c7b4-3b59-a009-5bb9e0cf05c5 | 1.5649 | -55.9829 | 2026-10-06 15:30:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 71.8 |
| ddbf195d-4290-33ea-b35e-3db360575462 | 1.4922 | -55.688 | 2026-10-06 15:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 84f87847-6da9-303b-b0f4-bc5119f872c1 | -6.65 | -43.7749 | 2026-10-06 15:30:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 59.1 |
| 3259c703-9a8a-381c-9209-852a2dd0ce1b | -9.0097 | -69.4036 | 2026-10-06 15:30:00 | GOES-19 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 92.6 |
| e564c794-e4d8-3717-b57c-89055130dd39 | -9.8447 | -44.7988 | 2026-10-06 15:30:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 156.0 |
| 93e1cfc6-7c4e-3d49-92b1-93994c3bf8d9 | -8.5916 | -67.1973 | 2026-10-06 15:30:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 47.1 |
| 0cbf5af5-9221-3df5-b4be-15178a0c402f | -9.8619 | -64.9958 | 2026-10-06 15:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 66.1 |
| 5efdfa74-7b6c-3569-8877-869903383e58 | -9.8244 | -65.0535 | 2026-10-06 15:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 57.7 |
| c8d95d78-92a5-3506-80e2-cb649724ff8f | -9.1613 | -68.2568 | 2026-10-06 15:30:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 74.8 |
| 389a0e2f-fabd-3c84-9c9b-afe7351c1a3d | -9.0098 | -69.3852 | 2026-10-06 15:30:00 | GOES-19 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 133.8 |
| 74e19473-28f2-3aec-9ae9-15228ac22903 | -9.8444 | -44.8218 | 2026-10-06 15:30:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 269.2 |
| 2d571090-547b-34fe-b422-b4aee786ec17 | -0.3768 | -52.0563 | 2026-10-06 15:30:00 | GOES-19 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 76.2 |
| ed5db320-781f-3a6a-b4fb-fda4582f54c0 | -8.9257 | -66.8549 | 2026-10-06 15:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 51.2 |
| 3e8dd70d-2151-31fe-bf08-f6027defe219 | -9.1511 | -66.0859 | 2026-10-06 15:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 58.7 |
| e293b7ba-b94d-3d03-bcb3-63f079068e13 | -9.8634 | -44.8195 | 2026-10-06 15:30:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 221.0 |
| c59e9a4f-73d9-3a67-b1b1-3eaac7d32ab2 | -8.6034 | -69.3374 | 2026-10-06 15:30:00 | GOES-19 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 46.8 |
| a111a453-8001-3e3c-9227-b032a1c43eed | 0.3221 | -51.0038 | 2026-10-06 15:30:00 | GOES-19 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 80.2 |
| 6afbf079-8309-3265-ada6-b918053f2c51 | -9.1055 | -68.3135 | 2026-10-06 15:30:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 50.2 |
| 77b3eed9-4ae9-3d74-8529-d97a1aba821e | -9.5594 | -66.0359 | 2026-10-06 15:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 47.7 |
| 53710165-f5f8-3fa1-b402-918086216b15 | -2.7713 | -57.0229 | 2026-10-06 15:30:00 | GOES-19 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 93701a6f-d085-32e4-bcea-86683e297cba | -9.1408 | -64.3836 | 2026-10-06 15:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 65.3 |
| df996aa9-c588-3175-9634-6cb285eb8015 | -7.8356 | -45.3175 | 2026-10-06 15:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 142.0 |
| 19a1fa56-d420-344d-994a-c433a019fca4 | -19.05532 | -40.0285 | 2026-10-06 15:31:00 | NOAA-20 | SOORETAMA | ESPÍRITO SANTO | Brasil | 3205010 | 32 | 33 | nan | nan | nan | Mata Atlântica | 10.7 |
| 6496a07f-5e07-3ae0-98bd-0d916aae5d70 | -17.07317 | -41.88071 | 2026-10-06 15:31:00 | NOAA-20 | ARAÇUAÍ | MINAS GERAIS | Brasil | 3103405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.4 |
| 83b7d759-ad09-31de-a697-6a521c9ae7c2 | -18.8587 | -41.0455 | 2026-10-06 15:31:00 | NOAA-20 | MANTENÓPOLIS | ESPÍRITO SANTO | Brasil | 3203304 | 32 | 33 | nan | nan | nan | Mata Atlântica | 7.9 |
| 6e3ed286-9035-32ec-8c50-9b6eb34d0fd5 | -19.27512 | -41.27209 | 2026-10-06 15:31:00 | NOAA-20 | RESPLENDOR | MINAS GERAIS | Brasil | 3154309 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| 30155941-8196-3cb8-9132-c630cc0c076c | -19.05363 | -40.02729 | 2026-10-06 15:31:00 | NOAA-20 | SOORETAMA | ESPÍRITO SANTO | Brasil | 3205010 | 32 | 33 | nan | nan | nan | Mata Atlântica | 8.1 |
| 8104342c-0ad5-3b55-b06f-8f632ad0fd79 | -17.07594 | -41.88028 | 2026-10-06 15:31:00 | NOAA-20 | ARAÇUAÍ | MINAS GERAIS | Brasil | 3103405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.6 |
| e0068132-9932-3921-b5e4-0b7f0a892646 | -18.85919 | -41.05144 | 2026-10-06 15:31:00 | NOAA-20 | MANTENÓPOLIS | ESPÍRITO SANTO | Brasil | 3203304 | 32 | 33 | nan | nan | nan | Mata Atlântica | 7.9 |
| 7d2f854b-6cd1-3a18-8c39-39b9d9cd18d5 | -16.83472 | -41.86919 | 2026-10-06 15:31:00 | NOAA-20 | ARAÇUAÍ | MINAS GERAIS | Brasil | 3103405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.4 |
| 11f3dee0-3304-3d16-9e81-a939071a9992 | -17.02571 | -41.03271 | 2026-10-06 15:31:00 | NOAA-20 | ÁGUAS FORMOSAS | MINAS GERAIS | Brasil | 3100906 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| a70dc336-209b-3605-83da-f3757b731677 | -18.95197 | -40.99784 | 2026-10-06 15:31:00 | NOAA-20 | ALTO RIO NOVO | ESPÍRITO SANTO | Brasil | 3200359 | 32 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| 3eb7c1a8-0a08-3d70-b21d-29bd6e35e682 | -12.60412 | -38.54126 | 2026-10-06 15:33:00 | NOAA-20 | SÃO SEBASTIÃO DO PASSÉ | BAHIA | Brasil | 2929503 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| 544434bd-266d-3df8-a74e-5ae15533c91b | -9.12925 | -40.26936 | 2026-10-06 15:33:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 55b75078-1cbb-3e3e-9b8c-5a426e6c1120 | -14.6171 | -41.41807 | 2026-10-06 15:33:00 | NOAA-20 | CARAÍBAS | BAHIA | Brasil | 2906899 | 29 | 33 | nan | nan | nan | Caatinga | 14.3 |
| 5051ad32-aff6-38da-8636-a0a55ae47034 | -10.58277 | -39.46104 | 2026-10-06 15:33:00 | NOAA-20 | MONTE SANTO | BAHIA | Brasil | 2921500 | 29 | 33 | nan | nan | nan | Caatinga | 12.2 |
| 1723e312-1ab5-3508-8411-27a520fa7a55 | -14.73158 | -41.58216 | 2026-10-06 15:33:00 | NOAA-20 | MAETINGA | BAHIA | Brasil | 2919959 | 29 | 33 | nan | nan | nan | Caatinga | 6.0 |
| bae434e1-970e-33df-9e05-3c1045966352 | -12.96364 | -41.061 | 2026-10-06 15:33:00 | NOAA-20 | ITAETÉ | BAHIA | Brasil | 2915007 | 29 | 33 | nan | nan | nan | Caatinga | 15.3 |
| c33b5fec-2db8-35f6-84da-c0e976e5194d | -14.98472 | -42.33656 | 2026-10-06 15:33:00 | NOAA-20 | MORTUGABA | BAHIA | Brasil | 2921807 | 29 | 33 | nan | nan | nan | Caatinga | 10.2 |
| 5f6516b2-6a25-3d95-8707-e7163728ef1b | -16.72187 | -42.04871 | 2026-10-06 15:33:00 | NOAA-20 | ARAÇUAÍ | MINAS GERAIS | Brasil | 3103405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| c0cfa14c-e148-31fe-b328-d50c9d6b0054 | -15.61206 | -41.6773 | 2026-10-06 15:33:00 | NOAA-20 | ÁGUAS VERMELHAS | MINAS GERAIS | Brasil | 3101003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.5 |


[Clique aqui para ver as próximas entradas](README87.md)
