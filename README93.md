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

## Dados Diários - Página 93

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| de9026cc-6e7e-30ad-8d71-153ce7359cf9 | -9.51825 | -54.73528 | 2026-10-07 05:06:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f58dc832-e7c1-33fd-be97-a854e3831b87 | -12.39049 | -49.81978 | 2026-10-07 05:06:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| afd51a06-9dfa-3a82-8128-2844d6e47c7a | -9.23133 | -67.87356 | 2026-10-07 05:06:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 33003d4b-bcd0-3db4-92fe-d5c8da33cdd9 | -11.72879 | -43.6623 | 2026-10-07 05:06:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 8.1 |
| f2f9d9c6-33eb-3ff4-9dca-723cdb62b1e4 | -11.79725 | -46.703 | 2026-10-07 05:06:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 7354a148-339d-34ea-82f6-87d806870a6a | -10.22095 | -44.6481 | 2026-10-07 05:06:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 35781208-566e-3dab-a437-31ecf269a49a | -9.13998 | -65.29072 | 2026-10-07 05:06:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 34b5b4e3-16d2-365b-9d4f-28a9ca056fa3 | -9.95736 | -67.1955 | 2026-10-07 05:06:00 | NOAA-21 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1049452a-aa35-3861-ba7a-187c0577c794 | -11.57794 | -48.44073 | 2026-10-07 05:06:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4d360492-3d24-3e39-940d-301690939adb | -11.67015 | -43.62418 | 2026-10-07 05:06:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 9353d2de-b2f7-3513-ac37-f2ff954cd67f | -11.2317 | -44.87265 | 2026-10-07 05:06:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 0401a7c7-3f6e-3372-98f7-56c9f6fe2f76 | -8.71414 | -69.46252 | 2026-10-07 05:06:00 | NOAA-21 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 0d93599f-3b8b-33c7-8925-3015b9718938 | -9.10613 | -65.36113 | 2026-10-07 05:06:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| da979cae-8865-3209-902c-a0e1688a9d11 | -8.91334 | -49.98379 | 2026-10-07 05:06:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 0f7897dd-52ae-3c75-81e6-b623f9e18d76 | -11.22722 | -45.26416 | 2026-10-07 05:06:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 67a47db8-e8ff-3c1d-a8ae-8d63c40c7d25 | -8.97246 | -65.44283 | 2026-10-07 05:06:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b1fbd658-c0eb-3c21-8a96-bbd78a2dae48 | -10.84769 | -50.65648 | 2026-10-07 05:06:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0e90d6d7-2928-31a5-bfa1-63fcb3db80ce | -8.28408 | -50.27368 | 2026-10-07 05:06:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| f0d0ca83-1927-33c8-bbe8-cda5e665e14f | -9.46115 | -67.08641 | 2026-10-07 05:06:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 85bd8d6c-6475-3dbc-a72f-383a21c972a3 | -8.74321 | -47.87598 | 2026-10-07 05:06:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7c49cdd3-a44c-3a8a-af8d-ec8c2607eb09 | -12.17312 | -44.72164 | 2026-10-07 05:06:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b9f4e837-3a34-3c5a-9fb4-a8cc8fd8153c | -8.91395 | -49.97931 | 2026-10-07 05:06:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 973ad626-81c6-3b36-a038-a1ed892259cf | -10.99044 | -45.42533 | 2026-10-07 05:06:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.7 |
| b6002b75-f698-38ed-ac3a-9753271937e4 | -9.11342 | -67.86137 | 2026-10-07 05:06:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 49e8f1c4-d9d1-341d-9ba5-3a36d38b44da | -9.15225 | -65.94593 | 2026-10-07 05:06:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 33b924b9-7106-3a02-a69e-6be527595a08 | -10.97492 | -45.40973 | 2026-10-07 05:06:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f29d8838-aa0b-3098-a137-3d021f1a5646 | -9.05694 | -65.48492 | 2026-10-07 05:06:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 09051497-8214-31a3-892c-94f777da7e10 | -9.13776 | -65.30309 | 2026-10-07 05:06:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a4e0ae8d-76e2-31ea-bdc5-e8f7d559b761 | -12.19248 | -44.71655 | 2026-10-07 05:06:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0f29eaf0-d308-368c-afeb-b2c631a791c4 | -9.23323 | -67.87228 | 2026-10-07 05:06:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 35be88a0-07bf-336c-8849-8f3d460e5a08 | -9.11339 | -67.82815 | 2026-10-07 05:06:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e99ad3d2-8598-3914-acae-fc6ccf7fcf00 | -9.11431 | -67.83294 | 2026-10-07 05:06:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a903c85a-a4d6-3b46-8ee7-be71e798c9f1 | -9.25975 | -45.64977 | 2026-10-07 05:06:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 732443df-e43a-32f9-b1d9-86dc186efff5 | -11.79675 | -46.70723 | 2026-10-07 05:06:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 44017cc5-e2a4-3ec3-914a-17f1045cd83d | -11.84698 | -62.67163 | 2026-10-07 05:06:00 | NOAA-21 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 27fd1d2e-04f6-36dc-a9e9-fe0b66c58968 | -9.115 | -67.86158 | 2026-10-07 05:06:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 30927355-3c3a-37b7-b1d7-aa60bd56d1ad | -10.85589 | -50.66203 | 2026-10-07 05:06:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c9c7343a-0b03-3f43-8595-48a42f9012b0 | -8.90949 | -49.97866 | 2026-10-07 05:06:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 48812a62-6da9-37de-a15f-37139c62d585 | -8.15295 | -64.07564 | 2026-10-07 05:06:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8c30e2c5-f54b-3d1f-b063-e9ac8d756b18 | -11.32742 | -46.67346 | 2026-10-07 05:06:00 | NOAA-21 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 4d6e26bb-2ecc-3b9b-a104-bfe8272e72b3 | -9.79794 | -48.92015 | 2026-10-07 05:06:00 | NOAA-21 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d65c8bd8-bb10-3a77-bc42-5b3c994269c7 | -9.59259 | -65.24162 | 2026-10-07 05:06:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 843801d5-b2f9-3ed4-b8a9-944376194c84 | -7.75065 | -54.94719 | 2026-10-07 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5d7da926-e048-3702-9d46-12a8b14ced99 | -9.09184 | -67.67902 | 2026-10-07 05:06:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 67a7a598-dbaf-3064-9757-5b91cea7474e | -9.29658 | -63.74083 | 2026-10-07 05:06:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 656728fe-0781-36ff-a2d3-0e453e31a563 | -9.13831 | -65.30001 | 2026-10-07 05:06:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 3da477a3-6c2e-3fe9-9b5f-a2122e2bbfbf | -9.25734 | -45.64854 | 2026-10-07 05:06:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| ee074191-a69e-3d3e-8b21-ce13acdcb453 | -12.47941 | -51.29022 | 2026-10-07 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8af18507-d07d-3246-93d5-833e28e0037b | -11.6778 | -43.61898 | 2026-10-07 05:06:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.5 |
| dba36c1e-e098-3a0b-b512-6485220e6e18 | -9.09611 | -67.68909 | 2026-10-07 05:06:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b57df30f-c528-3175-91d1-9f709de3b067 | -11.73723 | -43.64959 | 2026-10-07 05:06:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| d5f5e4bf-2816-3208-a772-1e528051058a | -11.73576 | -43.66317 | 2026-10-07 05:06:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| d1e50d7e-c441-3362-80da-e5af779c65c0 | -9.11239 | -65.35586 | 2026-10-07 05:06:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2de5552b-60ef-35e6-9c80-34fdff93808f | -11.40816 | -55.08089 | 2026-10-07 05:06:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7365a8eb-c110-314c-ab18-b6b9e6159d43 | -8.91198 | -68.79211 | 2026-10-07 05:06:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9a555093-6fb9-3b3a-aaba-de1f0ec84394 | -8.74793 | -47.87996 | 2026-10-07 05:06:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 39a6fe62-5db9-3d99-b7ac-eb4bccc30484 | -10.99147 | -45.4165 | 2026-10-07 05:06:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 7c495c31-6d0a-3baa-a989-ccfd76f95eba | -9.29574 | -63.74561 | 2026-10-07 05:06:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f9784a89-4080-3889-afc8-7cbbf649239c | -11.33372 | -46.6699 | 2026-10-07 05:06:00 | NOAA-21 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 198c22a4-db91-3903-bdd2-25ed007a5a63 | -9.26029 | -45.64536 | 2026-10-07 05:06:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 7e743667-c4d6-3c41-baa7-2b73a285cfe9 | -9.16165 | -47.57797 | 2026-10-07 05:06:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c8bec5d7-ab8f-36d1-9ba7-f7df4de3a472 | -8.50192 | -50.13412 | 2026-10-07 05:06:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e7f19f06-1268-381e-9052-67f73a8b769c | -9.60884 | -67.48048 | 2026-10-07 05:06:00 | NOAA-21 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 622d6617-393d-34db-8400-262d4846e2de | -9.608 | -67.48476 | 2026-10-07 05:06:00 | NOAA-21 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 7d7908b3-89cd-383c-a494-9c3d8d0ed474 | -13.50503 | -44.36328 | 2026-10-07 05:06:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 3ee678ea-f232-3b5c-b842-d622df81179b | -9.47108 | -67.07486 | 2026-10-07 05:06:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 93e8d04d-cb05-31c1-935c-ad44dbbd5248 | -11.23813 | -44.87368 | 2026-10-07 05:06:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 13.5 |
| af2ecd54-cdda-3aa2-b221-8fcfe1cce47a | -9.22874 | -67.88747 | 2026-10-07 05:06:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1d60b163-f6f4-3486-8ad6-19585a46b842 | -8.53581 | -55.37062 | 2026-10-07 05:06:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1ae4c7d7-3f35-3933-8e73-44ac527f6985 | -8.90564 | -49.97353 | 2026-10-07 05:06:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 963bc3f5-8a98-3bf1-9d49-51d569f84722 | -8.59936 | -67.0464 | 2026-10-07 05:06:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 3e065b9a-5362-3b3a-ba3e-3127d309a846 | -12.1931 | -44.71065 | 2026-10-07 05:06:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3a530bac-0016-371f-90ba-84886fa98599 | -8.53807 | -55.37825 | 2026-10-07 05:06:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 10dc74df-68e2-3b88-8fcd-4c530351a7f3 | -9.30544 | -49.3996 | 2026-10-07 05:06:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f44070d2-f9bd-3180-803a-9acc5407b31e | -8.91131 | -49.96526 | 2026-10-07 05:06:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a924fee6-6ad0-3607-b8c9-d6147a84f09e | -8.5986 | -67.05051 | 2026-10-07 05:06:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3607dbb3-1689-37b2-a422-aa26a89f57ac | -9.23476 | -67.88866 | 2026-10-07 05:06:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d371a29c-d192-303b-b7db-cc4e16df658a | -9.14453 | -65.29475 | 2026-10-07 05:06:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d06a662e-89d6-3e50-a13b-4a26b7f03448 | -9.3311 | -63.67832 | 2026-10-07 05:06:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| fe769819-03c1-3365-a10d-d66b63845b16 | -9.27337 | -50.66596 | 2026-10-07 05:06:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 372860ad-f482-3f48-b4d0-b8d56a12752a | -13.50317 | -44.36605 | 2026-10-07 05:06:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 71cb9856-beba-366e-9c0c-25320a49100e | -9.11589 | -67.85698 | 2026-10-07 05:06:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e6ef7c5b-839f-390c-ae74-eb2b6f88c9ad | -10.49143 | -50.43272 | 2026-10-07 05:06:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 72ef5578-58a6-32ce-9808-28b8ce45c336 | -10.1277 | -46.84681 | 2026-10-07 05:06:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a45eeed8-8525-3a20-9f82-36f557a72080 | -9.13942 | -65.29383 | 2026-10-07 05:06:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f09b5be4-6ede-331d-9f55-9c250d30f9ec | -12.48073 | -51.29166 | 2026-10-07 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3bff55f5-f6fd-3869-814a-a4fd0d95eb1b | -13.63861 | -44.42089 | 2026-10-07 05:06:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 75767393-acb4-38d3-862c-4e26fdc7e521 | -12.47644 | -51.29105 | 2026-10-07 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 05691d33-1a28-3e10-906b-fc4987ddc2ae | -10.99654 | -45.42719 | 2026-10-07 05:06:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 15dc368e-06c7-33d3-a1f2-d6c633c3dd67 | -13.638 | -44.4269 | 2026-10-07 05:06:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4cd517d3-1b2d-3c13-b3f7-8ef90c466aae | -9.2839 | -67.90107 | 2026-10-07 05:06:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 764ee28e-4dad-3688-8baf-3afc3ea51a16 | -9.15507 | -65.94895 | 2026-10-07 05:06:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 9.7 |
| a5e4e3ee-f874-3242-b225-3fea65b4c9ca | -9.15164 | -65.94936 | 2026-10-07 05:06:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8bdd1a46-1836-30a2-88fb-7ac6681e8917 | -8.63403 | -67.0529 | 2026-10-07 05:06:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 2aaa9e3d-d0a0-360e-873b-e012a3a8f797 | -11.22675 | -44.86614 | 2026-10-07 05:06:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| beaa7692-d4ab-3228-9f31-a534b2e03e17 | -10.9867 | -45.41685 | 2026-10-07 05:06:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| fc29587d-9dca-358d-a823-bb9388081156 | -9.80209 | -48.92632 | 2026-10-07 05:06:00 | NOAA-21 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c38a8c1f-96ec-35c4-b72c-ebe26909d491 | -9.15697 | -65.95033 | 2026-10-07 05:06:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 57030359-4c3e-3723-abc2-7fd10db508c6 | -12.6682 | -47.49522 | 2026-10-07 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 179e89d9-1717-3d21-a285-57cea69254a7 | -11.79146 | -46.70214 | 2026-10-07 05:06:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |


[Clique aqui para ver as próximas entradas](README94.md)
