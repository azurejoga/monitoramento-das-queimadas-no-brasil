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
| cc68a1e2-4f5f-3d00-9583-99612ee7204c | -17.15717 | -44.43688 | 2025-09-08 04:53:00 | NOAA-21 | JEQUITAÍ | MINAS GERAIS | Brasil | 3135605 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 51c57c03-d741-3254-85d2-23a1af311a8b | -15.35139 | -49.12697 | 2025-09-08 04:53:00 | NOAA-21 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 845fbd62-bced-33c0-a081-5adfb4c00085 | -17.29478 | -50.38852 | 2025-09-08 04:53:00 | NOAA-21 | ACREÚNA | GOIÁS | Brasil | 5200134 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 05ece81d-b48e-328c-b05b-12e9c43bc528 | -15.25419 | -53.82254 | 2025-09-08 04:53:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 25cc7b8b-d606-34ae-85db-4295dc8deef3 | -14.79592 | -48.10935 | 2025-09-08 04:53:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 38c0781e-6f09-3d8f-aa1d-9bda4591a7a7 | -12.93714 | -54.7926 | 2025-09-08 04:53:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c30da127-c866-3301-be7b-5ba07dd10102 | -17.57632 | -44.54123 | 2025-09-08 04:53:00 | NOAA-21 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 84106390-b652-344f-87fa-bf33ad6478ee | -12.47514 | -53.8577 | 2025-09-08 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7aa96903-a494-3e49-8fcc-bd52ca8b2c45 | -17.71159 | -44.48262 | 2025-09-08 04:53:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ac1ef41f-40e2-3c01-9c4f-9f6f5e7bd118 | -9.12406 | -65.95988 | 2025-09-08 04:53:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a4e333f6-8b12-3e70-b1f9-1f6bf2810cc1 | -13.30271 | -51.73856 | 2025-09-08 04:53:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7f5e3a82-ca56-39e0-b300-e77ac89a43c9 | -11.44878 | -49.24799 | 2025-09-08 04:53:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 422c3d7f-c455-39a3-9b0f-dc6eb25164f0 | -17.26119 | -46.70172 | 2025-09-08 04:53:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 43f3a410-3e5c-38fe-aff9-9eb852194fc4 | -16.34704 | -52.93707 | 2025-09-08 04:53:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 26236287-2464-3937-9c5b-bbcc2d70e40a | -12.83175 | -52.90236 | 2025-09-08 04:53:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f78ebc53-a506-3ff6-b4ca-4f84a50c50e3 | -13.70751 | -46.87875 | 2025-09-08 04:53:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 571a241f-da7c-34c3-b0dd-251a71355536 | -11.01308 | -52.05655 | 2025-09-08 04:53:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f246f210-8869-3dbe-9c6f-bc9e63edc88b | -15.25554 | -52.38315 | 2025-09-08 04:53:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ffa3940c-1204-301b-a2e8-310fdbacb504 | -12.46189 | -44.6505 | 2025-09-08 04:53:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 998c6377-5fae-3053-8dbc-2f1939af8b2b | -11.03287 | -52.04047 | 2025-09-08 04:53:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7d43854d-8f49-31a1-b4e1-2dc8750bc43b | -11.59761 | -52.19801 | 2025-09-08 04:53:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 308143b0-e1f3-3a40-a069-723fdf7218dd | -16.35846 | -43.63896 | 2025-09-08 04:53:00 | NOAA-21 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b18d9812-86e5-35d6-a9de-576abc80e26f | -12.5225 | -53.85811 | 2025-09-08 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 144340bc-27e2-340e-815a-3548ee2bfc8d | -14.51953 | -48.76453 | 2025-09-08 04:53:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a3953ec2-8ab2-33b0-93a4-f4844cb11888 | -11.89376 | -50.96645 | 2025-09-08 04:53:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5e06f5fb-ce28-36c9-bb70-bdf97c6af5e1 | -11.90328 | -64.98911 | 2025-09-08 04:53:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b4a38aa4-8b82-33ad-b76f-571089a0fa77 | -15.53262 | -49.26084 | 2025-09-08 04:53:00 | NOAA-21 | JARAGUÁ | GOIÁS | Brasil | 5211800 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4f946c6c-e86d-37d9-9dee-7fbbaaa3248d | -12.63307 | -56.98731 | 2025-09-08 04:53:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e8adad7b-fb2d-3abd-a0a3-f5abd43359c8 | -12.93164 | -54.78444 | 2025-09-08 04:53:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| cdc1ebb5-83c1-396b-9cf3-6c3d60e28d95 | -11.40944 | -50.39225 | 2025-09-08 04:53:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 23.7 |
| 6a6d7546-32a3-33d3-9c3c-05cf2cbe4df3 | -12.49649 | -48.0934 | 2025-09-08 04:53:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 01a0d923-a612-3c8f-a8c1-429c04bc4ec5 | -17.62208 | -44.8327 | 2025-09-08 04:53:00 | NOAA-21 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 15b9d5ae-d54d-3ec4-a92a-da190a73faab | -14.93159 | -55.88031 | 2025-09-08 04:53:00 | NOAA-21 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7350fe1e-b5c7-3470-a5de-3c456e923173 | -14.71895 | -55.91173 | 2025-09-08 04:53:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 38696d64-a940-34b7-bae9-238bcefa6551 | -11.86548 | -51.05943 | 2025-09-08 04:53:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 9.9 |
| afc85530-9760-3a52-9267-d0a789a98680 | -13.02646 | -48.0935 | 2025-09-08 04:53:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1407b8fe-07b9-3857-b071-e69ced22ebcb | -12.46932 | -48.03476 | 2025-09-08 04:53:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cfd3c37c-6f21-36a1-8477-53e09d7a5fa6 | -15.82603 | -52.26531 | 2025-09-08 04:53:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 59b090ea-2ffc-311f-a731-94c7f79bdd00 | -16.28174 | -45.68513 | 2025-09-08 04:53:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 5.3 |
| f6c9240f-7fec-3fa4-a33c-68387d972a7a | -14.81061 | -48.24223 | 2025-09-08 04:53:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 7b245b36-721f-30b0-920e-ae46ca579d01 | -15.68499 | -53.55384 | 2025-09-08 04:53:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 674ef890-a4eb-3840-aa05-58fa1729bf97 | -16.94054 | -45.8497 | 2025-09-08 04:53:00 | NOAA-21 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5d69593d-c93c-3144-a6dd-c847760acdbc | -14.50872 | -48.81484 | 2025-09-08 04:53:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 89411953-9298-331f-b153-05ddfc0a600e | -15.52848 | -49.26021 | 2025-09-08 04:53:00 | NOAA-21 | JARAGUÁ | GOIÁS | Brasil | 5211800 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dd44d124-0770-348b-aa6c-d01398819019 | -12.87636 | -47.9804 | 2025-09-08 04:53:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e9af9f24-fdc4-3789-bdd0-fde9a9c84c5a | -12.94162 | -54.7643 | 2025-09-08 04:53:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 861e9165-4ec6-3554-b379-3ef394a5737f | -11.89707 | -46.65086 | 2025-09-08 04:53:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4617b960-13ff-3cfd-ba58-849ba473ca05 | -16.89858 | -45.79011 | 2025-09-08 04:53:00 | NOAA-21 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fcf2588b-c13f-308c-bb1c-bc5ea1bae184 | -11.44809 | -49.25296 | 2025-09-08 04:53:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 50b261ca-f41c-363d-b864-5b0761cda6b0 | -11.21276 | -55.01952 | 2025-09-08 04:53:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 60700242-16ff-37c7-90df-f19b3190592d | -11.21449 | -55.00876 | 2025-09-08 04:53:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c48f21e2-6b8c-31d6-bbb5-a757616c8d7e | -11.19778 | -55.00606 | 2025-09-08 04:53:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 15.8 |
| b421e9ca-eb89-3314-95af-f427a6c82287 | -14.42977 | -48.45507 | 2025-09-08 04:53:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 48fdb5bc-8051-3599-b9e0-14414e3f3dac | -12.20082 | -53.91409 | 2025-09-08 04:53:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 037ea504-be4f-3129-9845-b01c382fd510 | -10.05313 | -59.36209 | 2025-09-08 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 102ea7a7-4960-3d82-b512-b750adc3aaf5 | -14.2183 | -53.34997 | 2025-09-08 04:53:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 36162137-0c26-3c9c-8e01-e59f59c6db14 | -11.05129 | -54.17314 | 2025-09-08 04:53:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cd5dbdc9-6c05-3c5e-84d5-95582bf878f0 | -15.00188 | -48.00991 | 2025-09-08 04:53:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c09a8e44-43f5-350c-8dcb-206f54fc5454 | -12.87709 | -62.10516 | 2025-09-08 04:53:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 378fb094-1e6b-3ec9-95a8-db06cbfd61b2 | -11.11685 | -52.01869 | 2025-09-08 04:53:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bf9f5d3d-5bf4-3e0a-b653-7b3eaa506913 | -8.88904 | -64.22263 | 2025-09-08 04:53:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 838fc434-267e-3bb7-b11e-7a99b2f0cf6a | -12.82908 | -52.94294 | 2025-09-08 04:53:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 27f97273-b290-3bad-b198-1c848184de73 | -12.82271 | -56.52563 | 2025-09-08 04:53:00 | NOAA-21 | TAPURAH | MATO GROSSO | Brasil | 5108006 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3c62cea0-afca-3ba0-8577-b33378053cea | -14.45708 | -56.80804 | 2025-09-08 04:53:00 | NOAA-21 | ARENÁPOLIS | MATO GROSSO | Brasil | 5101308 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 09ded67e-c063-3b4e-ad2f-299db5960d55 | -11.38702 | -50.33964 | 2025-09-08 04:53:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ea6cd883-a654-30f2-8588-098efa0586b4 | -15.66484 | -53.8695 | 2025-09-08 04:53:00 | NOAA-21 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0d6bbd1a-c678-35de-9ac4-d549f62bd1d5 | -11.10204 | -52.00114 | 2025-09-08 04:53:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 11cf0320-3e56-30b8-9244-cd38c8f11f34 | -11.83043 | -46.77495 | 2025-09-08 04:53:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| aa2bc6df-d54c-38d6-bb08-b19813b6f057 | -15.70505 | -46.55814 | 2025-09-08 04:53:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c6ebac85-a15a-3429-9ac7-d721feb593d5 | -11.62208 | -47.1469 | 2025-09-08 04:53:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 7fcc54f4-b4e8-3332-97d1-fbf891f61224 | -11.38431 | -50.41077 | 2025-09-08 04:53:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 073f69d2-8ff5-3eef-9897-7c332c68ffdd | -13.82782 | -46.24364 | 2025-09-08 04:53:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| cdd58e5e-5d7c-3dda-a160-29271750baf1 | -15.25437 | -52.3911 | 2025-09-08 04:53:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d6668e81-8666-3260-8577-ebeb0513880f | -15.01929 | -48.00383 | 2025-09-08 04:53:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| cc4a160f-344d-3a02-a04f-2661ae76f233 | -15.17503 | -55.99279 | 2025-09-08 04:53:00 | NOAA-21 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 6.8 |
| fd6236cf-f230-3049-b43c-0f07b6b62148 | -12.47787 | -53.84011 | 2025-09-08 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2d29ea44-7dac-316a-8c48-7ee78317208f | -15.7682 | -53.56334 | 2025-09-08 04:53:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 55e22183-c136-3d56-81ca-35ccd641fbae | -14.42925 | -48.45917 | 2025-09-08 04:53:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b3a8b6f9-492f-399d-a4d5-45909d9e6d3f | -18.1466 | -43.40041 | 2025-09-08 04:53:00 | NOAA-21 | COUTO DE MAGALHÃES DE MINAS | MINAS GERAIS | Brasil | 3120102 | 31 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 795d8325-0b31-3d92-911c-36d84e25a739 | -11.79625 | -62.74224 | 2025-09-08 04:53:00 | NOAA-21 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a9d83c81-d4c4-36f9-a72c-ee3f9b451690 | -14.29789 | -44.87172 | 2025-09-08 04:53:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6c0cf050-2cb9-38b6-a41d-40605d8167bf | -15.24105 | -52.38503 | 2025-09-08 04:53:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e311ad9a-8288-39fc-82e2-5516867a04df | -15.73593 | -53.58093 | 2025-09-08 04:53:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| db4b3650-f85c-3b95-920b-dd1c2d698baa | -16.98038 | -45.83053 | 2025-09-08 04:53:00 | NOAA-21 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7b1aa01d-f760-358d-9154-27a43b2ecb57 | -15.53363 | -48.37002 | 2025-09-08 04:53:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 75ce1000-bbd9-3263-bbd6-787e1a69b75d | -13.03577 | -47.13224 | 2025-09-08 04:53:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 29d81eaf-bc77-3f76-8fa9-dd82e7b302e2 | -15.96829 | -48.10738 | 2025-09-08 04:53:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 5.2 |
| bcb8c5b5-a499-3680-b1e2-9ed83de7af15 | -11.90178 | -64.9874 | 2025-09-08 04:53:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ebd60b66-2695-3bc7-bb16-8ff80cb220be | -15.75923 | -53.55426 | 2025-09-08 04:53:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 004ed871-f322-3099-b4c9-571caebf204d | -12.17067 | -43.94948 | 2025-09-08 04:53:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0dc6ee5c-7128-3e4b-9498-a3ab1bc56ab6 | -11.66126 | -46.88427 | 2025-09-08 04:53:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 7583bcf2-5166-35b9-b891-29349f2ac996 | -17.64568 | -44.78852 | 2025-09-08 04:53:00 | NOAA-21 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 4fc02071-2a50-3c0b-a5a6-06d7803c3216 | -12.95374 | -54.77355 | 2025-09-08 04:53:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 49d3cd77-21e3-388d-a990-f058bc4583f1 | -11.83245 | -47.55716 | 2025-09-08 04:53:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 67ca10df-ec52-34a1-8d74-eb9a3b4fb222 | -15.08182 | -50.10461 | 2025-09-08 04:53:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d9dfced7-4769-31ca-8abb-d7f32a2551e0 | -12.19752 | -53.91355 | 2025-09-08 04:53:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 062b5566-af7d-3081-92c0-9cdf35b0757e | -12.94157 | -54.78606 | 2025-09-08 04:53:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| acc6e4ca-5b0c-31c6-94f5-31442981c10f | -15.18894 | -47.97919 | 2025-09-08 04:53:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| f5a04045-7d32-376a-a1cb-8395b0577531 | -12.19367 | -53.91653 | 2025-09-08 04:53:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c118c683-0015-3e06-9006-5b0dab48587c | -14.93769 | -55.88503 | 2025-09-08 04:53:00 | NOAA-21 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |


[Clique aqui para ver as próximas entradas](README73.md)
