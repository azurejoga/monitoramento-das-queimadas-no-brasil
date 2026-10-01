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

## Dados Diários - Página 114

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 84c41c41-de43-3ca4-9fbe-675a37dd0693 | -5.8412 | -53.4799 | 2026-10-01 18:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 79.9 |
| 02c9903e-710a-33f3-8275-f37f64437347 | -6.1949 | -53.177 | 2026-10-01 18:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 121.3 |
| 5e19b2e2-8331-387e-b4ec-15edf814b4be | -11.6216 | -43.4774 | 2026-10-01 18:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 138.2 |
| da2e8e3c-4911-3b25-ba86-6f75ea9bd86a | -11.3935 | -43.3705 | 2026-10-01 18:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 123.7 |
| 2535c908-69bc-3cb6-8aa5-5f457687a8d6 | -11.4123 | -43.3913 | 2026-10-01 18:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 119.0 |
| bc8e4ec9-71a2-32c2-a9bd-4b1beaffba63 | -3.0728 | -49.3615 | 2026-10-01 18:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 173.3 |
| 86be7cb7-da6c-30aa-8791-2feb82ee6285 | -6.3401 | -51.1263 | 2026-10-01 18:10:00 | GOES-19 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 156.3 |
| 12390b0b-523f-3e70-9cb3-160338009cfc | -3.8573 | -55.7992 | 2026-10-01 18:10:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 62.1 |
| 52a16e85-0c3d-38fb-86a8-8bcb26c1e83a | -6.1764 | -53.1779 | 2026-10-01 18:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 57.6 |
| 094b77e9-c88c-30d5-80f2-2782bcf3e9c5 | -5.9151 | -53.4965 | 2026-10-01 18:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 229.4 |
| fb7e551b-8451-3fed-af89-ca37860bada7 | -6.1784 | -52.8919 | 2026-10-01 18:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 44fdb4fe-bb4c-395e-94de-998b767975c9 | -2.974 | -51.0247 | 2026-10-01 18:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 52.4 |
| 80a78a5d-cdbc-3a4e-ba56-7b9b58662e18 | -11.2945 | -43.551 | 2026-10-01 18:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 131.6 |
| d3778193-b087-36d4-973e-5dbf91840eab | -3.9886 | -41.5165 | 2026-10-01 18:10:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 110.2 |
| 875b5546-e49d-3ea1-b1eb-5486c24614de | -3.839 | -55.7997 | 2026-10-01 18:10:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 9609b61d-920b-3545-affd-76deed9b9f97 | -14.4707 | -40.7074 | 2026-10-01 18:10:00 | GOES-19 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 271.1 |
| 5befb5e2-2cda-35f0-9ae3-e7d0a44c4b52 | -11.3931 | -43.3942 | 2026-10-01 18:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 110.3 |
| e65b06ab-9857-3ede-ad01-4a2ca5bdc6c9 | -3.8573 | -55.8189 | 2026-10-01 18:10:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 52.5 |
| bcbf4199-ffb8-3d65-a46b-c211d430cbda | -15.1456 | -43.5847 | 2026-10-01 18:10:00 | GOES-19 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 123.2 |
| d5d1e80e-7a16-3a46-baea-e5c839efd3f0 | -6.1402 | -53.0574 | 2026-10-01 18:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 91.1 |
| 0e519f13-7c0b-3d4d-ada6-e88f3ced5e54 | -9.83 | -44.86 | 2026-10-01 18:15:00 | MSG-03 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 696d1cc6-dc56-328e-a457-2018120ea04f | -11.71 | -43.6 | 2026-10-01 18:15:00 | MSG-03 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e8558439-de6a-3dd3-b266-cb9f71fdce80 | -13.0 | -41.87 | 2026-10-01 18:15:00 | MSG-03 | PIATÃ | BAHIA | Brasil | 2924306 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 4b0497cb-bed1-34c2-b04b-d6f974963519 | -6.26 | -53.12 | 2026-10-01 18:15:00 | MSG-03 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a9ddb74b-0cd6-3e67-8981-fc23d623ab7b | -11.3 | -43.59 | 2026-10-01 18:15:00 | MSG-03 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 128789c0-4410-33f2-9bad-7a4facc0e4a3 | -5.95 | -43.83 | 2026-10-01 18:15:00 | MSG-03 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 64c798ca-8ad5-3e41-bf6d-f40eb076120c | -9.83 | -44.82 | 2026-10-01 18:15:00 | MSG-03 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| bcebcae2-eced-3423-9bde-29e36b80e8df | -5.98 | -43.84 | 2026-10-01 18:15:00 | MSG-03 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2b0be34e-b9c5-38ba-af1a-b652d5602e9e | -11.51 | -43.5 | 2026-10-01 18:15:00 | MSG-03 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| bb9323dd-3a96-3926-a130-7c65df11a748 | -10.55 | -50.07 | 2026-10-01 18:15:00 | MSG-03 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 825fc633-50c4-3d88-8ec6-5fe80183c0ef | -15.5 | -46.11 | 2026-10-01 18:15:00 | MSG-03 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 9bf96bb1-13d0-3b8d-abad-752c07e4def0 | -5.76 | -45.14 | 2026-10-01 18:15:00 | MSG-03 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 970c8d74-8cf8-3ed1-9fa0-662013fdfb1d | -11.45 | -43.49 | 2026-10-01 18:15:00 | MSG-03 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| afce0086-78d0-323e-b08b-9b244da270b0 | -13.0 | -41.82 | 2026-10-01 18:15:00 | MSG-03 | PIATÃ | BAHIA | Brasil | 2924306 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| a8853cea-4575-3d90-b9f3-8d43c352900e | -14.37 | -44.81 | 2026-10-01 18:15:00 | MSG-03 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 59a1bc45-95e2-3645-bfe5-9fa8948afadc | -7.2 | -52.61 | 2026-10-01 18:15:00 | MSG-03 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 88d0fe1b-a6f3-3fb5-a3e0-de6601ccd10b | -10.58 | -50.08 | 2026-10-01 18:15:00 | MSG-03 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 804fd27f-53e8-31f8-9f4a-204488d42554 | -7.84 | -55.17 | 2026-10-01 18:15:00 | MSG-03 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c9992cc9-20cb-30b6-ba39-39a7636a99d1 | -7.84 | -55.1 | 2026-10-01 18:15:00 | MSG-03 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d494beb1-faf3-3d65-8053-9a1ba4559ef4 | -3.839 | -55.7997 | 2026-10-01 18:20:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 79.2 |
| 2bbe7c92-5ba8-38b3-b6d1-ca5c266be753 | -5.8412 | -53.4799 | 2026-10-01 18:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 78.0 |
| 5c63219a-8f4c-3f83-b2e8-5648e5a5cce9 | -5.8596 | -53.4993 | 2026-10-01 18:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 180.9 |
| 16a0c763-e0a9-3cad-b531-d8984b3d0330 | -10.6918 | -40.8455 | 2026-10-01 18:20:00 | GOES-19 | MIRANGABA | BAHIA | Brasil | 2921401 | 29 | 33 | nan | nan | nan | Caatinga | 152.2 |
| f4baa58b-5a91-34d4-a676-485df0d98e82 | -11.4123 | -43.3913 | 2026-10-01 18:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 106.6 |
| 672fd9ec-9e48-3525-a7e6-e081bdc7141b | -14.4707 | -40.7074 | 2026-10-01 18:20:00 | GOES-19 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 238.3 |
| 0f0a8d47-d442-32f3-85bb-8b8ebb9a8d58 | -13.3292 | -43.8335 | 2026-10-01 18:20:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 120.7 |
| 86e6b1c0-9fbc-344a-9a7e-0d93164b9101 | -6.1949 | -53.177 | 2026-10-01 18:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 129.9 |
| bbb16113-2543-3fe6-a5bc-72b01643794b | -11.3935 | -43.3705 | 2026-10-01 18:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 125.5 |
| b79a688d-45d4-35c1-911c-21f6783f4875 | -2.974 | -51.0247 | 2026-10-01 18:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 49.9 |
| d6b2f44c-c107-3a9a-9565-715448137a95 | -11.6011 | -43.5515 | 2026-10-01 18:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 135.2 |
| 53cc9d34-7ca1-3115-8cf3-83fa91ee311b | -3.0728 | -49.3615 | 2026-10-01 18:20:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 147.4 |
| f36a0008-d71e-31ea-9cb2-b658a811cb29 | -5.841 | -53.5205 | 2026-10-01 18:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 56.0 |
| c84242ce-f9aa-3cf9-9e6e-92a48bab9409 | -5.8597 | -53.479 | 2026-10-01 18:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 211.2 |
| 69ecb898-6ff7-3f27-9471-25e16a66c04a | -6.1402 | -53.0574 | 2026-10-01 18:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 98.2 |
| 92c5e2d7-d4d4-3433-b491-e4502d9ecec3 | -3.8573 | -55.8189 | 2026-10-01 18:20:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 07b91b03-c69a-3862-870a-ba6ab8058e67 | -6.3215 | -51.1274 | 2026-10-01 18:20:00 | GOES-19 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 53.6 |
| c9aba826-65cd-3e99-90a7-e607610735c8 | -6.3215 | -51.1274 | 2026-10-01 18:30:00 | GOES-19 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 84.5 |
| 000d715d-4788-3f68-bee3-67aa928d3d9e | -6.1764 | -53.1779 | 2026-10-01 18:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 56.7 |
| b6533402-d4c0-3ddb-b99f-8ff9c3c76a89 | -4.3947 | -54.8286 | 2026-10-01 18:30:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 23a41898-ac97-3b01-881c-5a66207b50a3 | -3.3068 | -50.8481 | 2026-10-01 18:30:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 66.4 |
| f1356c12-dff9-3714-a566-89b58d153878 | -3.8573 | -55.8189 | 2026-10-01 18:30:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 18b35bd9-fde3-345f-b5eb-81bf18605536 | -3.8573 | -55.7992 | 2026-10-01 18:30:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 76.8 |
| fb7394e5-4a89-3888-898f-adbba5b1ecf1 | -6.1784 | -52.8919 | 2026-10-01 18:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 18a3b7fa-b418-355c-8a28-d66f90bf9528 | -6.3401 | -51.1263 | 2026-10-01 18:30:00 | GOES-19 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 98.8 |
| 878dc39e-5a55-3ab5-975c-c9f2b5d253c8 | -11.3935 | -43.3705 | 2026-10-01 18:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 105.0 |
| 0c064498-dbc3-3afe-a674-4c39b5d6c178 | -5.9889 | -53.5335 | 2026-10-01 18:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 47.5 |
| ceb35317-bb18-364b-8f6a-c3a3f19f04f5 | -11.6203 | -43.5485 | 2026-10-01 18:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 168.6 |
| d8678907-e7d2-3e78-a70d-4802b2141c19 | -13.3292 | -43.8335 | 2026-10-01 18:30:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 106.7 |
| a0edf64c-7c30-33cc-ae56-d754a263e433 | -11.4311 | -43.4121 | 2026-10-01 18:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 125.0 |
| cd1b8ac4-2240-3406-9c26-eb6b6989dc9d | -5.8411 | -53.5002 | 2026-10-01 18:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 52.7 |
| 97e51f3a-121d-325c-9191-481a1b27aebf | -11.6011 | -43.5515 | 2026-10-01 18:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 129.0 |
| 3d206efc-513b-38dc-b122-b635ed3c9bfc | -6.1949 | -53.177 | 2026-10-01 18:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 119.9 |
| ceb82a44-fa81-3ae7-af13-79720a9d9c4e | -6.8863 | -52.5027 | 2026-10-01 18:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 72.3 |
| ef4d207e-0494-3544-a1d6-ad296462b371 | -14.4707 | -40.7074 | 2026-10-01 18:30:00 | GOES-19 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 201.7 |
| dc644a42-d5d0-3f44-9f70-c5d1cbc6f468 | -6.1402 | -53.0574 | 2026-10-01 18:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 88.7 |
| 37c8aa56-a164-3e9d-a467-d367be56e665 | -6.1401 | -53.0779 | 2026-10-01 18:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 55.6 |
| b1cae316-9664-38f3-9c2f-a26c7e3611da | -11.6207 | -43.5248 | 2026-10-01 18:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 184.6 |
| 47c48d99-8183-3718-8a57-0d9c8c9d681d | -6.3399 | -51.1471 | 2026-10-01 18:40:00 | GOES-19 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 7d65b2e3-fa9d-36a1-aa26-85a07a85ab4a | -5.8411 | -53.5002 | 2026-10-01 18:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 50.9 |
| f51fd8a9-364d-3776-a9fe-7a4cfaf35112 | -11.6011 | -43.5515 | 2026-10-01 18:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 157.5 |
| 30ea0689-65d4-3cc7-a9e3-f098dcc2ec24 | -11.6199 | -43.5722 | 2026-10-01 18:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 178.4 |
| f3a9bdc8-d891-37e3-99a7-aecfc10d3560 | -6.0829 | -53.3051 | 2026-10-01 18:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 49.5 |
| 74fa6c90-89d1-33ae-8556-45037b6bfc3f | -11.6395 | -43.5455 | 2026-10-01 18:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 146.9 |
| d56ef440-d7a7-3fc8-a6c2-0c44e9ff6064 | -11.3133 | -43.5718 | 2026-10-01 18:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 245.5 |
| 6d67f284-8bbc-3731-a3ec-99f9d72efc95 | -11.4503 | -43.4091 | 2026-10-01 18:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 174.2 |
| b2a7d6e8-afb8-32d6-96ca-0b9de048ee3d | -11.2941 | -43.5747 | 2026-10-01 18:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 90.5 |
| 9f7d5696-c054-3020-b9a8-a0ff977fe719 | -11.4691 | -43.4299 | 2026-10-01 18:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 139.2 |
| 0626cdba-dd77-33d8-abc7-43f14606901a | -11.4499 | -43.4329 | 2026-10-01 18:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 140.4 |
| d1616513-5124-3848-8686-45885f08f081 | -11.6015 | -43.5278 | 2026-10-01 18:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 178.7 |
| 5cfc186c-d160-39bc-bed1-ebf8c4a2d847 | -11.4311 | -43.4121 | 2026-10-01 18:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 108.4 |
| 7268b133-2d09-3d30-9414-3b0982138900 | -6.3805 | -46.4083 | 2026-10-01 18:40:00 | GOES-19 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 46.6 |
| 6f9a60cb-ca58-3ef5-b412-b37ee5df8623 | -6.7341 | -52.9632 | 2026-10-01 18:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 69.2 |
| 89a8e4a1-da50-3df0-be40-c766f760b1a3 | -6.1217 | -53.0584 | 2026-10-01 18:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 55.9 |
| 95653b84-248e-3990-9b66-911c9772dcd0 | -6.1388 | -53.2614 | 2026-10-01 18:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 55.7 |
| e73fa5b3-be2b-39e2-8dfe-247545b75656 | -11.3137 | -43.5481 | 2026-10-01 18:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 114.5 |
| 49dbe463-31b0-3121-9b66-d948bf56ff8c | 1.9608 | -50.8612 | 2026-10-01 18:40:00 | GOES-19 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 58.1 |
| fb3bb22b-dff0-3c25-ab91-5af1e63e277c | -13.3292 | -43.8335 | 2026-10-01 18:40:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 107.4 |
| 323ac986-af3e-3b11-b7b2-f26958acc6de | -11.4495 | -43.4566 | 2026-10-01 18:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 92.5 |
| 7c5fbb23-0bda-3d1a-9548-d90b22a1fe75 | -6.3401 | -51.1263 | 2026-10-01 18:40:00 | GOES-19 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 82.4 |
| 02d3add1-3373-32ee-a97e-a2a481874d79 | -14.4707 | -40.7074 | 2026-10-01 18:40:00 | GOES-19 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 184.2 |


[Clique aqui para ver as próximas entradas](README115.md)
