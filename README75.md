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

## Dados Diários - Página 75

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 18bf8a06-c882-3abe-80cf-1bd6d7b78191 | -12.61352 | -55.20668 | 2024-10-12 04:59:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0492cb00-23c8-360e-a008-1fb1a74497ad | -12.61297 | -55.2102 | 2024-10-12 04:59:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 54207a0c-cb56-314a-94c1-a81964100a25 | -12.61242 | -55.21372 | 2024-10-12 04:59:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0cb34e12-fa57-3386-a612-a60a959eb806 | -12.61188 | -55.21725 | 2024-10-12 04:59:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1731fb30-a9bb-3602-a4a2-cc318dd51ac0 | -12.60912 | -55.21319 | 2024-10-12 04:59:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5d21e1d7-69cf-3a69-8455-675c0ad9d0b0 | -12.49947 | -54.51111 | 2024-10-12 04:59:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f13a4577-a73d-3640-8920-8e81b8a04a7e | -12.49892 | -54.5147 | 2024-10-12 04:59:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b1a450fe-81aa-3511-b058-9766fd5afdbb | -12.49558 | -54.51417 | 2024-10-12 04:59:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1bf45c9b-baf0-33a8-8896-d07a12827dd2 | -12.45106 | -54.56269 | 2024-10-12 04:59:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 32.2 |
| a8bb081e-22e4-3986-8901-a6bf13d0b1e6 | -12.45051 | -54.56628 | 2024-10-12 04:59:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 29.3 |
| f7e55721-78af-3973-b85f-a04039a49cdd | -12.44996 | -54.56987 | 2024-10-12 04:59:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 29.3 |
| 7984e3d5-1e55-3979-b01e-9b560235eda7 | -12.44941 | -54.57345 | 2024-10-12 04:59:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 16.2 |
| 54d52402-7631-3f7d-a546-459677388f98 | -12.44828 | -54.55858 | 2024-10-12 04:59:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 32.2 |
| d6f4f7c7-4145-3025-bd42-00d48aa0ed37 | -12.44773 | -54.56217 | 2024-10-12 04:59:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 32.2 |
| cc78f294-7824-3310-b0b7-79dc6503d1e9 | -12.44718 | -54.56576 | 2024-10-12 04:59:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 29.3 |
| b30fcaf9-b969-3e07-a46a-473c3b5275c2 | -12.44663 | -54.56935 | 2024-10-12 04:59:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 29.3 |
| e9d17aea-7dfa-3fb9-9292-b312621e3dc2 | -12.44607 | -54.57293 | 2024-10-12 04:59:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 16.2 |
| 8ce31344-b3b6-385b-8a7c-afceb8d366de | -12.44552 | -54.57651 | 2024-10-12 04:59:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 16.2 |
| 3908543e-f8c8-371f-b285-2b057c5ddb74 | -12.44495 | -54.55806 | 2024-10-12 04:59:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| a91ad9a6-2f47-3e26-93fc-24cc598e5b85 | -12.4444 | -54.56165 | 2024-10-12 04:59:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 29fec97d-bcbc-3eb5-990b-7f3b2dd5b9bc | -12.44424 | -54.4513 | 2024-10-12 04:59:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f14daad7-8e17-33f8-bb3f-ac60264222b7 | -12.44384 | -54.56524 | 2024-10-12 04:59:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 741ac2f1-6674-3905-8adf-d1e191235dce | -12.44329 | -54.56882 | 2024-10-12 04:59:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| decd8e2f-a838-3611-b793-f7c5c39200d8 | -12.44274 | -54.57241 | 2024-10-12 04:59:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 858bfdfe-5928-3f3e-9f13-f186a8887f8e | -12.44219 | -54.57599 | 2024-10-12 04:59:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 4c9584fc-ef38-3409-a27b-656f25ab8f36 | -12.44162 | -54.55753 | 2024-10-12 04:59:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| f2b62a7d-0fc7-3169-84c3-c6190fc0002f | -12.44106 | -54.56112 | 2024-10-12 04:59:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 57b313f8-ac89-3923-9c98-8f07df0f5684 | -12.44051 | -54.5647 | 2024-10-12 04:59:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 4c1bc981-fd35-3ca7-a6db-dcf9ac8c16c5 | -12.43996 | -54.5683 | 2024-10-12 04:59:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 47c1640d-f7b6-340f-9f60-c8a8132435d8 | -12.43941 | -54.57188 | 2024-10-12 04:59:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 0c28456d-7ef8-3923-86f4-2d382848a801 | -12.43886 | -54.57547 | 2024-10-12 04:59:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 7.7 |
| f94964b0-1c9e-3b2b-8e91-b45294193a34 | -12.43831 | -54.57905 | 2024-10-12 04:59:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5d80d1a2-2593-3bde-8c40-779e4edebc49 | -12.43773 | -54.56059 | 2024-10-12 04:59:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1559f3ba-27bc-37e4-aa48-8addaecda6e7 | -12.43718 | -54.56417 | 2024-10-12 04:59:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7d3eb577-1f86-346b-867b-b01c986417b7 | -12.43663 | -54.56777 | 2024-10-12 04:59:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8a29ac18-cabc-3d6a-8a3a-57bfb91ed65d | -12.43608 | -54.57136 | 2024-10-12 04:59:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 41ec09d6-0ef1-38d7-84aa-2576eb4a3d03 | -12.43553 | -54.57494 | 2024-10-12 04:59:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1419c494-0169-313b-8ae0-422d8dd7ab2e | -12.4344 | -54.56006 | 2024-10-12 04:59:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9df20350-7a0a-3962-b34b-d16d8ae0b5bb | -12.43387 | -54.58568 | 2024-10-12 04:59:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8e22e897-b4fc-3395-b9a5-8bb6706aa658 | -12.43385 | -54.56365 | 2024-10-12 04:59:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 26067e07-038f-30f2-81d9-ec8e1e4ba98f | -12.43333 | -54.58925 | 2024-10-12 04:59:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4349061e-7349-3d03-89ed-be635b84912f | -12.43219 | -54.57441 | 2024-10-12 04:59:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f0c11daf-75c7-3ebb-a4fb-d7e4544f66b0 | -12.43164 | -54.578 | 2024-10-12 04:59:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d9542d71-f9ce-388f-bb55-45554f4a7237 | -12.42721 | -54.58463 | 2024-10-12 04:59:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 45a10671-f000-322f-9840-f29f28d5ed94 | -12.42666 | -54.5882 | 2024-10-12 04:59:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 289b7f8d-f788-3f37-b9a6-5b4316b312ee | -12.40668 | -54.585 | 2024-10-12 04:59:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0cc5dbc4-9351-39b6-9bb9-a014353a64a5 | -12.4039 | -54.58088 | 2024-10-12 04:59:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c02d7fa3-065c-3b3d-9585-f5364d65199f | -12.40335 | -54.58447 | 2024-10-12 04:59:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 13df565b-ef28-3ad4-b7cb-adc91aff1959 | -12.39305 | -54.45051 | 2024-10-12 04:59:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 439769d1-c10e-3063-ab1d-55974e1eeea9 | -12.39251 | -54.45411 | 2024-10-12 04:59:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a6d6fd90-716f-3804-b302-c64cf7f654f9 | -12.38917 | -54.45358 | 2024-10-12 04:59:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3b0d6f47-77cd-365a-bf82-3170366a718e | -12.38862 | -54.45718 | 2024-10-12 04:59:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 95ce3c02-7f4d-3b19-8a98-16651967a9ca | -12.38807 | -54.46077 | 2024-10-12 04:59:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e2d6fe9f-f7bd-3016-a00f-a4202238025c | -12.38474 | -54.46024 | 2024-10-12 04:59:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7350c5c1-38a1-3357-9205-aaaf29cf7bfc | -12.38419 | -54.46383 | 2024-10-12 04:59:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f111cc5e-3173-3cf1-86a0-868904f44189 | -13.99013 | -54.58182 | 2024-10-12 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2b60de5e-a09d-3c7f-8099-ae83de878e67 | -8.4416 | -55.46639 | 2024-10-12 04:59:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2347f88f-406f-3e4b-b6d2-365694c5db1e | -8.44103 | -55.4699 | 2024-10-12 04:59:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ac24fed8-c026-3029-baf1-7549ed891786 | -8.43884 | -55.46235 | 2024-10-12 04:59:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c5408f92-42de-320d-b188-73e903b7691b | -8.43828 | -55.46585 | 2024-10-12 04:59:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6110e6d3-1571-39ea-b5df-962f48a6caf6 | -8.43772 | -55.46937 | 2024-10-12 04:59:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8849233d-c881-33b5-a2fe-1ffc5d633e06 | -8.43716 | -55.47287 | 2024-10-12 04:59:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cc520b76-5c9b-3760-98dd-07fff545699e | -8.43608 | -55.4583 | 2024-10-12 04:59:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0550a082-bdd0-3b6e-9924-18c12fe26083 | -8.43552 | -55.46181 | 2024-10-12 04:59:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0df0fc95-ef34-32d5-b56b-40e843930437 | -8.43496 | -55.46532 | 2024-10-12 04:59:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a7070592-bd04-3f48-8b07-949ae12abaf2 | -8.4344 | -55.46883 | 2024-10-12 04:59:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d38cb1c5-4844-3bec-af67-ed5fcb2233be | -8.43384 | -55.47234 | 2024-10-12 04:59:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c28d7fdc-a52e-30dc-81ba-dcb4a7e9806c | -8.43328 | -55.47585 | 2024-10-12 04:59:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 31269fcf-5e14-3a50-a348-022c496d5428 | -8.43276 | -55.45776 | 2024-10-12 04:59:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| abef21b3-fe44-3880-b1f1-3967b2877a5b | -8.4322 | -55.46128 | 2024-10-12 04:59:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2074afd1-84d4-3d61-9b5b-341f69e72df9 | -8.43164 | -55.46479 | 2024-10-12 04:59:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b2dba649-d875-3adf-898f-d41e9494c98a | -8.43108 | -55.4683 | 2024-10-12 04:59:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cfeee00c-c570-3edb-998a-08e750fd3daf | -8.43052 | -55.47181 | 2024-10-12 04:59:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ee534c25-037b-3c1b-bfa0-fd0453120d90 | -8.42996 | -55.47531 | 2024-10-12 04:59:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c5ef8c7d-dc38-3dcb-8b65-ba3d794098a1 | -8.42944 | -55.45723 | 2024-10-12 04:59:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d39c805a-ae89-354f-99c0-9a2263c2788f | -8.42888 | -55.46075 | 2024-10-12 04:59:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 49d52705-df0c-3a3e-8313-f364adcd9066 | -8.42832 | -55.46426 | 2024-10-12 04:59:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1134add0-78be-3629-827c-4df43fe981cf | -8.42776 | -55.46777 | 2024-10-12 04:59:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d9cfcab1-1717-3b6e-be0e-6e610f1e0728 | -8.42721 | -55.47127 | 2024-10-12 04:59:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 597b305f-a2fa-379e-85da-fc931de396ab | -8.42665 | -55.47478 | 2024-10-12 04:59:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4bc0ed33-bf12-3267-b19e-1fca34065191 | -8.42613 | -55.4567 | 2024-10-12 04:59:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 592f4efd-1982-333d-b42e-2b88d99cd26f | -8.42557 | -55.46021 | 2024-10-12 04:59:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 26b2de0b-16c9-3ae5-ae48-cc80b79dc9cb | -8.42501 | -55.46372 | 2024-10-12 04:59:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 512da70f-09ce-339e-b9ab-6ca44f448393 | -8.42445 | -55.46723 | 2024-10-12 04:59:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| e3f66723-b35a-38e9-b346-47ff202e1a22 | -8.42389 | -55.47074 | 2024-10-12 04:59:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 2d015ea7-e29c-3c84-a3bb-9ebf6da81afc | -8.42225 | -55.45968 | 2024-10-12 04:59:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7d1b9240-3685-34fa-af95-87e511a40a51 | -8.42169 | -55.46319 | 2024-10-12 04:59:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| a1c8b1e7-6d39-334a-b1aa-da18f5380baf | -8.42113 | -55.4667 | 2024-10-12 04:59:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 12f3590c-110c-3a11-80cd-26f2ab2b4e97 | -8.42057 | -55.47021 | 2024-10-12 04:59:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| f03b6ab8-2947-33ef-9f02-87437bebdeea | -9.96389 | -55.33329 | 2024-10-12 04:59:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 60b633ae-c5f3-3cd7-9546-763638342759 | -9.96114 | -55.32928 | 2024-10-12 04:59:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 686fcb1f-7635-32ca-8617-de0710fa43b7 | -9.96059 | -55.33277 | 2024-10-12 04:59:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 433ab21d-fdd2-345e-aeae-1207d6b7cd1b | -9.95729 | -55.33224 | 2024-10-12 04:59:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 414c2614-155b-3816-ba40-094c6cc9a6ea | -9.58327 | -55.7996 | 2024-10-12 04:59:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8dd217c3-173c-3fd5-82b1-c14965d49049 | -9.57995 | -55.79906 | 2024-10-12 04:59:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d5af0ec2-3aff-3d24-8b62-451fd5a1b2db | -9.57938 | -55.80259 | 2024-10-12 04:59:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e3d4cf62-720a-31ac-af0f-6570fcd7e9b3 | -9.57662 | -55.79853 | 2024-10-12 04:59:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 56fe30e1-6aa4-39e4-8034-5c0f07dcd9f2 | -9.57606 | -55.80206 | 2024-10-12 04:59:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 9dc65904-76a5-3f93-a5a9-84cd6c5fe88c | -9.57549 | -55.80559 | 2024-10-12 04:59:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 54c9e929-dcad-3e50-bb52-e6c606cb8bdf | -9.5733 | -55.79799 | 2024-10-12 04:59:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README76.md)
