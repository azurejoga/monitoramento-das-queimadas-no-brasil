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

## Dados Diários - Página 150

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| afcbc0b7-3759-3979-938d-f16a6252b1fb | -10.47394 | -68.13623 | 2026-10-05 17:37:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9e676247-c9ef-3fdd-a8a2-0249568f2d1e | -0.73851 | -57.95581 | 2026-10-05 17:37:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| d539251d-6bc5-33f3-8197-49dd622258cb | -9.36045 | -67.31125 | 2026-10-05 17:37:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 16.4 |
| 175f3a68-2965-3e09-a753-7c856ec86ebb | -3.66475 | -69.43844 | 2026-10-05 17:37:00 | NOAA-20 | SÃO PAULO DE OLIVENÇA | AMAZONAS | Brasil | 1303908 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 42a324ab-6d23-30c2-9ee1-dcedeb185439 | -7.23346 | -55.19263 | 2026-10-05 17:37:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| e72e2c08-f1ed-3d36-8ab4-c1ed24ab1f6d | 1.73001 | -55.62503 | 2026-10-05 17:37:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 18626147-13ba-37eb-956f-323da24c9db4 | -8.56788 | -66.70443 | 2026-10-05 17:37:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 7.9 |
| f58cb45a-5eff-36c0-a7c2-7863a39565de | 1.58686 | -50.98061 | 2026-10-05 17:37:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 3e67fbc2-cea5-3263-b001-2ffd342fb504 | 2.29176 | -55.89729 | 2026-10-05 17:37:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 03488aa7-6eb6-3571-b4b4-81b82cf623a0 | -1.56333 | -55.17606 | 2026-10-05 17:37:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| a9a1049c-ab3d-3c92-9202-0eaa6adfb468 | 1.74734 | -55.60067 | 2026-10-05 17:37:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 3b3f41a6-5453-35d5-991d-e2a8b03e4e83 | -7.22919 | -55.18108 | 2026-10-05 17:37:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 41.9 |
| 8fd22ae8-5c67-3ab5-9bfa-391522678ff2 | -2.60555 | -57.56847 | 2026-10-05 17:37:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 21.5 |
| ea6093e6-d6ff-3db0-8eb6-86ba5487f92b | 1.60884 | -55.77103 | 2026-10-05 17:37:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| aea9c98e-b152-32db-90aa-cc3ff154f7ef | -6.45755 | -54.99975 | 2026-10-05 17:37:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| c7be9345-004f-32e6-a0a2-6bc82c09c849 | -9.15542 | -68.2378 | 2026-10-05 17:37:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 9.6 |
| fb1109a5-8e3f-3e22-9119-5b455533cc1e | -8.8367 | -69.47949 | 2026-10-05 17:37:00 | NOAA-20 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 34.6 |
| 3c711f7b-b339-36d7-9eb0-2f12e4d581bd | -1.13465 | -52.01956 | 2026-10-05 17:37:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 7eacdd43-5494-3208-b12c-49154339d3e3 | -9.20779 | -71.86182 | 2026-10-05 17:37:00 | NOAA-20 | JORDÃO | ACRE | Brasil | 1200328 | 12 | 33 | nan | nan | nan | Amazônia | 14.7 |
| c697aa1e-3b69-3a3a-8f7b-85da0e349c47 | -9.37579 | -68.9261 | 2026-10-05 17:37:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 72b84074-4a7f-3588-847c-975c50f3b5a2 | -8.95468 | -68.78249 | 2026-10-05 17:37:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 24.8 |
| 3c84e501-a3d6-3838-9d6d-685546cfc31e | -9.21563 | -67.38931 | 2026-10-05 17:37:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 97997918-a5c6-3782-ba0f-6610ac5326af | -9.26194 | -67.62463 | 2026-10-05 17:37:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 78d72e40-f7a7-32f4-9d05-6476c1401f95 | -9.505 | -68.49418 | 2026-10-05 17:37:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 1165203b-f847-3fb2-a08d-5af93c0958b7 | -9.40402 | -65.89455 | 2026-10-05 17:37:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 8f3d35cb-2ab9-3ad7-ae09-5b337f46b4e0 | -10.83815 | -69.64944 | 2026-10-05 17:37:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 8bc095e1-5df8-3048-929c-b7501fddd39a | 4.21446 | -60.71424 | 2026-10-05 17:37:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 413dc11c-c701-3196-838f-8f49a3afa9cb | -9.91971 | -65.0183 | 2026-10-05 17:37:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 6.7 |
| d97be816-8c12-30e3-878b-1ce34f3759a1 | -9.57138 | -68.59576 | 2026-10-05 17:37:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 6.2 |
| d0d76157-19e8-31e9-b0ff-0b3db34cb677 | -9.11521 | -64.18038 | 2026-10-05 17:37:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 9.2 |
| a383329e-780a-3097-8a75-2601eb9ae575 | -1.35562 | -55.97959 | 2026-10-05 17:37:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 31.2 |
| 885c8fde-12e1-38d9-ab72-e049dbec6fbd | -8.32164 | -67.5883 | 2026-10-05 17:37:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 79c53a9d-9137-3a31-9755-9fbb69b3583d | -9.1256 | -68.21055 | 2026-10-05 17:37:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| f97d5e20-cf5b-31c9-b92d-46445fccf7d3 | 4.21105 | -60.71374 | 2026-10-05 17:37:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 13.0 |
| b9c2b1d7-37bd-39ae-b08a-6add37b6b63c | -0.73824 | -57.97805 | 2026-10-05 17:37:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| f506de3d-9337-33db-9e6b-e460d955b349 | -8.85979 | -66.79478 | 2026-10-05 17:37:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 68.8 |
| 3c468b6c-e0e7-3822-b726-14416c40dccc | -7.87029 | -54.71194 | 2026-10-05 17:37:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| a8ad86fa-00da-339e-8b52-92328fdce95a | -10.10536 | -68.26338 | 2026-10-05 17:37:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 36282c96-fbf3-3873-ab68-9f935c8262db | -8.88116 | -69.12712 | 2026-10-05 17:37:00 | NOAA-20 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 632c2723-f961-315e-95a5-7e1c7efefed4 | 3.58393 | -61.34046 | 2026-10-05 17:37:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 3982a3b3-8a89-3410-9e1d-8f40dba6e580 | -3.26944 | -68.33341 | 2026-10-05 17:37:00 | NOAA-20 | AMATURÁ | AMAZONAS | Brasil | 1300060 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 4b0739e1-d40c-3f6c-b4a5-f195620451ec | -9.11484 | -67.71169 | 2026-10-05 17:37:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 476e9a71-88df-3888-b3a7-cdb48c77330f | -6.72822 | -55.07219 | 2026-10-05 17:37:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 6d95b728-ba3e-39d4-9c17-979eb9b637f1 | -9.154 | -65.40921 | 2026-10-05 17:37:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 937379b2-cf23-3c1b-ba90-3230a81124ba | -2.05151 | -56.86552 | 2026-10-05 17:37:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 65a619e8-aebe-3af6-bddf-ff8983519adb | -10.49074 | -69.17136 | 2026-10-05 17:37:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 7.1 |
| a912decd-3485-39ff-aa15-0eb3b181726d | -10.78079 | -69.5194 | 2026-10-05 17:37:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 68.9 |
| 5c096429-394a-305d-8bbf-8d59e93ea599 | 1.85011 | -50.694 | 2026-10-05 17:37:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 9415fc5a-31c6-32e1-bbb2-38b36a5e5ba1 | -1.45276 | -53.59573 | 2026-10-05 17:37:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 1d6d55cc-311b-3221-be60-069bf11501ca | 1.88352 | -55.74076 | 2026-10-05 17:37:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 1596a5e4-9f3e-3049-8e9d-cd5bab0c9076 | -8.774 | -66.57022 | 2026-10-05 17:37:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 087db10c-baa4-3278-ba41-b2a5801beb94 | -9.15138 | -66.08089 | 2026-10-05 17:37:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.5 |
| d8ca3bd6-5089-3536-b7f5-751ae1d06978 | -8.69723 | -64.16864 | 2026-10-05 17:37:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 8.3 |
| ffab4f0a-a43d-346a-8e23-a92a1b6c6e36 | -10.73979 | -69.61516 | 2026-10-05 17:37:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 6.0 |
| e1cba992-fb0f-378d-abed-18dbde6d0522 | 3.06496 | -60.60309 | 2026-10-05 17:37:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 8ba1a005-8a50-3150-9baa-6e0b433ff44d | -1.35678 | -55.98702 | 2026-10-05 17:37:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 9e558f3c-5fd6-3599-8340-d3d5f91ea99a | -9.55421 | -68.46155 | 2026-10-05 17:37:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 25.9 |
| e809b3bf-1218-306f-b0b7-867868f915cf | -1.34089 | -55.96657 | 2026-10-05 17:37:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 4049b25d-6dea-3489-9239-8696c2b51b57 | 1.79118 | -50.62137 | 2026-10-05 17:37:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 4.8 |
| ef3739f5-f8ae-36ba-90de-90d62815c698 | 1.73578 | -55.61695 | 2026-10-05 17:37:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 15dd048f-1c1e-373d-b018-f7ee32de1871 | 1.84217 | -55.80449 | 2026-10-05 17:37:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 16db8b44-9bd8-3a5b-b518-07e0be6e3a2d | -8.93614 | -67.34451 | 2026-10-05 17:37:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 105.1 |
| 958b5005-1c69-3a2b-8327-fc8ef25cd1ab | -9.34822 | -68.92586 | 2026-10-05 17:37:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 46.7 |
| fd092b9a-aec8-37fd-98e7-0ad09376006e | -8.56633 | -67.13211 | 2026-10-05 17:37:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 61f09bb1-5da4-33ca-9d7e-ee6f1f595d2f | -1.75603 | -55.27889 | 2026-10-05 17:37:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| f5d99000-13e7-32b8-9d9a-5e0163324979 | -9.40901 | -65.89828 | 2026-10-05 17:37:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 7.4 |
| a6fa1323-d9f7-37a1-abb2-f750264699d5 | -9.13885 | -67.93031 | 2026-10-05 17:37:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 71a70381-fc61-3ca3-bba1-ef0df757ae89 | -8.85897 | -62.83187 | 2026-10-05 17:37:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 23.3 |
| 10630e04-72c9-3c02-91e8-64a681f6bbb0 | -2.77857 | -57.67121 | 2026-10-05 17:37:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 17.1 |
| 3ac6aee7-17d8-3944-b64a-daf1446daf48 | -9.15318 | -68.26022 | 2026-10-05 17:37:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ce9c999d-45ee-3068-a05e-8c8ab6fa4048 | 3.54118 | -51.50366 | 2026-10-05 17:37:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 7.3 |
| a66b9b74-9543-33d2-828e-993a55921586 | -2.75625 | -57.64845 | 2026-10-05 17:37:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 18.3 |
| 46d3f41a-ae7d-314f-9649-fe728a95b2a5 | -1.81729 | -57.10596 | 2026-10-05 17:37:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 833ce967-f84d-319b-90c8-db03c181a624 | -8.58331 | -67.14297 | 2026-10-05 17:37:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| d2cf4f78-d85e-3ef5-86b5-b078903d0369 | -8.56889 | -66.99626 | 2026-10-05 17:37:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 9.9 |
| a6c76a3b-f919-3712-92d2-e057fceaff5e | -1.7445 | -55.23439 | 2026-10-05 17:37:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| d6817ae3-035e-38f8-9d61-7090c1b6cdf5 | -7.32795 | -55.75539 | 2026-10-05 17:37:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 5129a338-c7b1-31a0-a572-5d56e253aae7 | -9.33962 | -68.79456 | 2026-10-05 17:37:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 38.8 |
| 8835329f-5b29-38b3-9d40-df000ddc91d8 | -9.11406 | -67.70605 | 2026-10-05 17:37:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 28.5 |
| e7f32769-a043-3ce4-baeb-3728ae575ed7 | -9.28611 | -68.25848 | 2026-10-05 17:37:00 | NOAA-20 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 6a2ba07d-563f-3ca0-9957-6a3cb22987d6 | -8.67127 | -70.04127 | 2026-10-05 17:37:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 209d8aff-3da9-31e0-ae42-98478986f2d4 | -3.17164 | -60.06071 | 2026-10-05 17:37:00 | NOAA-20 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| d833d165-e3d3-303f-b89b-d440cf864f27 | -8.66586 | -67.11097 | 2026-10-05 17:37:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 8.2 |
| c93e5b3c-14ae-3b96-9ee4-352447f7ec24 | -8.66302 | -66.93121 | 2026-10-05 17:37:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 13.3 |
| cb2c90e7-ddb3-36d1-bf4c-9f989888cab2 | -7.11581 | -55.72607 | 2026-10-05 17:37:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| a99c49fc-e86a-3c9e-9ad2-ffd7636ceae3 | -9.41376 | -68.8615 | 2026-10-05 17:37:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 9de0637e-39b3-39da-a848-add22473eec7 | -8.59619 | -67.13083 | 2026-10-05 17:37:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 9.2 |
| eb39d159-2101-373f-afc2-40033bdfc89a | -9.02708 | -65.70173 | 2026-10-05 17:37:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 19f52a76-4ee3-30e8-b3aa-b8e59a3bc123 | 3.0751 | -60.58217 | 2026-10-05 17:37:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 8.6 |
| af966f0c-35ca-319c-a0bd-f9dd1de73d2c | -10.24026 | -68.23232 | 2026-10-05 17:37:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 76f79235-b5d8-3009-8ac1-5d160c782e5e | 0.31369 | -60.43737 | 2026-10-05 17:37:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 7.5 |
| db3698a3-348a-3fa7-a4a9-13d26b460aa9 | -6.52549 | -55.28337 | 2026-10-05 17:37:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| fcd94993-9792-30f1-8dd2-5b0938d12e10 | -6.71612 | -55.07418 | 2026-10-05 17:37:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 574c060a-b9d7-3d2a-afbe-9ac62d2a92db | -2.76059 | -57.65216 | 2026-10-05 17:37:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 2eb4e357-6592-3a67-91ae-5ae1fe3e42f8 | -6.52606 | -55.28683 | 2026-10-05 17:37:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| f5bd964f-381c-3faa-bcee-ca089cb03794 | -10.44127 | -67.83694 | 2026-10-05 17:37:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 9f542db4-a894-3ee3-afe3-62db826663dc | -8.61564 | -70.01961 | 2026-10-05 17:37:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 706c7fd7-2047-3962-a194-b81aa6808b50 | 0.30965 | -50.99095 | 2026-10-05 17:37:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 432cb008-7687-3dc2-bbcb-313855bdc79a | 1.9774 | -60.61437 | 2026-10-05 17:37:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 9c1e0f20-8730-34c5-b605-3665dc4aa940 | -8.95355 | -69.11815 | 2026-10-05 17:37:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 5.0 |


[Clique aqui para ver as próximas entradas](README151.md)
