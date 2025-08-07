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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3a326d14-1098-328b-bd13-7507780afefa | -8.9213 | -60.7489 | 2025-08-07 09:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 46.9 |
| a153bab3-a9a1-3519-a03b-03e68fcc6d03 | -10.6441 | -44.7413 | 2025-08-07 10:50:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 116.5 |
| 6eab9df3-10e9-3db8-90e3-b3e3b40cef1a | -10.6441 | -44.7413 | 2025-08-07 11:00:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 173.4 |
| b270a2b4-7bb3-3aa2-886f-148c115a2cb5 | -10.6441 | -44.7413 | 2025-08-07 11:10:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 199.1 |
| 332357f3-baaf-39dc-a122-51e7a8300a14 | -10.6438 | -44.7645 | 2025-08-07 11:10:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 124.4 |
| 0b148a96-dd29-3c39-b62c-154af6b0d5e8 | -10.6441 | -44.7413 | 2025-08-07 11:20:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 117.5 |
| 794baf7a-cc26-353f-b3be-97617c5e8867 | -10.6441 | -44.7413 | 2025-08-07 11:30:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 115.6 |
| 6a1ea0db-af5a-3250-9c3e-b5a0e0d5a514 | -10.6441 | -44.7413 | 2025-08-07 11:40:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 102.6 |
| 421bada6-e84b-3628-a75f-0874d6134e21 | -6.2789 | -45.2716 | 2025-08-07 11:40:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 86.8 |
| 0d87477c-2446-3d56-904f-d0b38cb3a37d | -6.2789 | -45.2716 | 2025-08-07 11:50:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 104.3 |
| bcd801d2-aa00-3ae7-98f4-96b6f5a53ca6 | -10.6441 | -44.7413 | 2025-08-07 11:50:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 101.4 |
| fcf42300-11de-3dac-8f35-0cb401cc6e1f | -6.2792 | -45.249 | 2025-08-07 11:50:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 86.3 |
| a625592f-295d-3fee-b644-379d3ffc9cab | -6.27393 | -45.27086 | 2025-08-07 11:51:00 | TERRA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 75.9 |
| 42d81db7-9c28-369c-aeed-561382109d9c | -5.67759 | -41.40016 | 2025-08-07 11:51:00 | TERRA_M-M | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 82.0 |
| 7a36813c-3103-3f20-81c5-8f57f10e83e1 | -6.42013 | -44.03107 | 2025-08-07 11:51:00 | TERRA_M-M | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 156755b8-9db5-3cb1-91a4-136b16b33808 | -4.17657 | -42.02811 | 2025-08-07 11:51:00 | TERRA_M-M | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 7.8 |
| 30ce40f7-2cfe-3299-a1c8-8b62b030d552 | -6.27098 | -45.24672 | 2025-08-07 11:51:00 | TERRA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 43.5 |
| ba371923-94ed-3035-a2ab-6d2795251882 | -6.07914 | -44.68656 | 2025-08-07 11:51:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 69.6 |
| 0bfbf9f5-c309-3a28-b2e9-b2f6f3ddea88 | -4.39129 | -41.91452 | 2025-08-07 11:51:00 | TERRA_M-M | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 10.7 |
| 14b7e8e6-a640-3c3b-80b6-c35ce2d0b3b0 | -4.18856 | -38.36649 | 2025-08-07 11:51:00 | TERRA_M-M | CASCAVEL | CEARÁ | Brasil | 2303501 | 23 | 33 | nan | nan | nan | Caatinga | 7.6 |
| ba8881fa-59c1-32aa-b218-a618bad156bc | -6.0906 | -44.68814 | 2025-08-07 11:51:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 1607e38b-00ae-3665-a090-41fd506e45a3 | -6.07658 | -44.69302 | 2025-08-07 11:51:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 26.7 |
| 70df53b3-6b62-3037-ad3d-4e9d6096ad29 | -6.09044 | -44.67927 | 2025-08-07 11:51:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 3f5fb632-f03a-3b6c-b8b9-fa196f7922b5 | -6.26842 | -45.2637 | 2025-08-07 11:51:00 | TERRA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 192.8 |
| 0479bf08-68a7-3c0c-ab60-bdffbbe235c6 | -7.14576 | -38.51989 | 2025-08-07 11:51:00 | TERRA_M-M | SÃO JOSÉ DE PIRANHAS | PARAÍBA | Brasil | 2514503 | 25 | 33 | nan | nan | nan | Caatinga | 12.7 |
| 9bfaee46-1c55-3d71-b3d8-5ed176c8823e | -5.1895 | -37.94271 | 2025-08-07 11:51:00 | TERRA_M-M | LIMOEIRO DO NORTE | CEARÁ | Brasil | 2307601 | 23 | 33 | nan | nan | nan | Caatinga | 4.9 |
| e0fb3c29-9050-3dc2-bba7-9b6b293ff033 | -5.48292 | -39.30798 | 2025-08-07 11:51:00 | TERRA_M-M | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 74e15fc8-24cf-3563-bcb7-8c0972a19619 | -6.08805 | -44.69455 | 2025-08-07 11:51:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 44.5 |
| 99a6c9ba-1e1c-30c6-a077-9c0add47f606 | -6.26475 | -45.25168 | 2025-08-07 11:51:00 | TERRA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 53.0 |
| bdb1b42b-42f5-3190-8e24-e3395a4ed461 | -6.27665 | -45.25364 | 2025-08-07 11:51:00 | TERRA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 63.5 |
| 3a64c2c0-0286-380b-a946-30667de94690 | -4.18984 | -38.35753 | 2025-08-07 11:51:00 | TERRA_M-M | CASCAVEL | CEARÁ | Brasil | 2303501 | 23 | 33 | nan | nan | nan | Caatinga | 22.8 |
| 4a1dddc1-57bd-3a83-9027-f905559c6da0 | -4.39286 | -41.90401 | 2025-08-07 11:51:00 | TERRA_M-M | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 10.0 |
| dbd2d2d3-46f6-3dea-9811-c0c09b1e6955 | -6.26201 | -45.26886 | 2025-08-07 11:51:00 | TERRA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 36.3 |
| 047935c5-1967-3469-996e-772f10b4c28d | -4.68676 | -38.0411 | 2025-08-07 11:51:00 | TERRA_M-M | PALHANO | CEARÁ | Brasil | 2310001 | 23 | 33 | nan | nan | nan | Caatinga | 15.3 |
| b576335c-2079-30ba-ae8d-8557045d275a | -3.31003 | -39.28131 | 2025-08-07 11:51:00 | TERRA_M-M | TRAIRI | CEARÁ | Brasil | 2313500 | 23 | 33 | nan | nan | nan | Caatinga | 8.0 |
| 9273b186-7ad4-3d9f-a55c-99561c1e8f65 | -6.55249 | -42.81849 | 2025-08-07 11:51:00 | TERRA_M-M | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 11.4 |
| 5c6a03ec-d8a1-38da-b178-5c82fad6f407 | -6.55209 | -42.81175 | 2025-08-07 11:51:00 | TERRA_M-M | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 9.5 |
| fbbbdd85-c129-30b2-819a-a7fcda602904 | -4.19873 | -38.35876 | 2025-08-07 11:51:00 | TERRA_M-M | CASCAVEL | CEARÁ | Brasil | 2303501 | 23 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 8e42ca30-3d42-3b08-b766-3cf9b9f527e3 | -8.52079 | -43.2951 | 2025-08-07 11:53:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 91.3 |
| 43000371-031e-3622-b3b2-18d8b5e251d2 | -8.77353 | -40.55837 | 2025-08-07 11:53:00 | TERRA_M-M | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 11.4 |
| 98487d2f-10fe-3c3c-bba4-81203c4aa1ab | -10.64553 | -44.74402 | 2025-08-07 11:53:00 | TERRA_M-M | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 93.2 |
| bbd6f36d-5a3a-31a4-9c84-0350841e3ba7 | -10.63492 | -44.74239 | 2025-08-07 11:53:00 | TERRA_M-M | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 52.9 |
| f3b12938-57b1-395c-9940-8f8b44c2bbfe | -12.71492 | -46.37913 | 2025-08-07 11:53:00 | TERRA_M-M | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 1eb3678f-c571-3aa4-92dc-d6df412722ae | -6.52388 | -45.59555 | 2025-08-07 11:53:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 60.1 |
| 1e4cdc5a-f171-3553-bff0-8d9daf25ae45 | -12.48449 | -41.0588 | 2025-08-07 11:53:00 | TERRA_M-M | ANDARAÍ | BAHIA | Brasil | 2901304 | 29 | 33 | nan | nan | nan | Caatinga | 10.5 |
| 59837aee-20e8-3408-8008-622440988b2d | -10.63701 | -44.72913 | 2025-08-07 11:53:00 | TERRA_M-M | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 3869ed16-8f6a-33f5-b0ed-6f2a3c72c659 | -7.2756 | -44.32127 | 2025-08-07 11:53:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 21.9 |
| 90034601-ba38-3cf8-a1fe-a4f32a8b3172 | -12.01598 | -47.51432 | 2025-08-07 11:53:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 99f8e255-5d86-3a87-adcc-eb28efbf4b07 | -8.52253 | -43.28388 | 2025-08-07 11:53:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 13.2 |
| 5319a36e-1cd2-3a2a-854e-f1bea4c91823 | -6.79373 | -43.78739 | 2025-08-07 11:53:00 | TERRA_M-M | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 26.6 |
| 9cd3065e-9c07-3945-8a16-c7dbe0092304 | -12.27258 | -44.57511 | 2025-08-07 11:53:00 | TERRA_M-M | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 13.3 |
| ce86c288-500c-3d98-9e3b-94132fc0f11b | -11.80457 | -43.81956 | 2025-08-07 11:53:00 | TERRA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 20e80cb0-b82b-3c1a-a663-d9d63b8c1508 | -8.4793 | -45.69581 | 2025-08-07 11:53:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 14.4 |
| ccdb0450-d8a1-39c9-af30-ef730a2a7f1a | -13.00385 | -44.87683 | 2025-08-07 11:53:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 22ec93f4-a2db-353c-ab76-a69b6fcbcc3d | -11.14484 | -40.04284 | 2025-08-07 11:53:00 | TERRA_M-M | CALDEIRÃO GRANDE | BAHIA | Brasil | 2905503 | 29 | 33 | nan | nan | nan | Caatinga | 13.0 |
| f5d4d269-67f2-34e8-9305-81a5e64f16f6 | -11.14356 | -40.05187 | 2025-08-07 11:53:00 | TERRA_M-M | CALDEIRÃO GRANDE | BAHIA | Brasil | 2905503 | 29 | 33 | nan | nan | nan | Caatinga | 6.4 |
| f7373885-ac53-39c1-bf33-e9ae66023f85 | -8.51905 | -43.3064 | 2025-08-07 11:53:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 79.0 |
| ab2f9339-5337-34b8-924b-d941da3f4262 | -10.63283 | -44.75569 | 2025-08-07 11:53:00 | TERRA_M-M | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 23.5 |
| c3096fcd-45b4-382d-9211-0cf2306f4e9c | -10.63073 | -44.76898 | 2025-08-07 11:53:00 | TERRA_M-M | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 23.5 |
| 275d2747-dbb4-3f5c-a595-fed0584fdac9 | -7.73725 | -45.49533 | 2025-08-07 11:53:00 | TERRA_M-M | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 9785baee-a014-3bee-b930-2d97c4104b3b | -7.3736 | -45.31104 | 2025-08-07 11:53:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 13.3 |
| bb399900-11df-392c-8833-1a0a3f9fb451 | -8.97646 | -40.61808 | 2025-08-07 11:53:00 | TERRA_M-M | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 7.5 |
| 7e690fde-5232-35af-a3ce-c9453ee0a102 | -7.09843 | -40.6523 | 2025-08-07 11:53:00 | TERRA_M-M | FRONTEIRAS | PIAUÍ | Brasil | 2204303 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 8ed370e4-9add-323c-80c2-83fc9297f3ff | -8.82789 | -44.56643 | 2025-08-07 11:53:00 | TERRA_M-M | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 22.6 |
| 5c125122-f649-3062-b30d-93e9eea1fbc0 | -12.55025 | -47.1564 | 2025-08-07 11:53:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 28b66235-a5eb-3a17-9fd9-5260d4bd229f | -8.83385 | -45.55551 | 2025-08-07 11:53:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 11.9 |
| f3df7267-f05d-36bf-83f4-4c258daa3507 | -12.74492 | -44.8285 | 2025-08-07 11:53:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 0707bd63-5698-30b6-b727-b24691aa25c4 | -8.52366 | -39.72985 | 2025-08-07 11:53:00 | TERRA_M-M | SANTA MARIA DA BOA VISTA | PERNAMBUCO | Brasil | 2612604 | 26 | 33 | nan | nan | nan | Caatinga | 8.2 |
| c44c655c-7502-38ff-8203-388161727bba | -12.70065 | -46.39375 | 2025-08-07 11:53:00 | TERRA_M-M | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 5291e9d3-a11f-3b07-a5cf-1f8c2c694b02 | -10.64345 | -44.75732 | 2025-08-07 11:53:00 | TERRA_M-M | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 56.4 |
| f8904638-a0f4-30dc-a8f4-2101e15e920d | -13.64429 | -42.71189 | 2025-08-07 11:55:00 | TERRA_M-M | IGAPORÃ | BAHIA | Brasil | 2913408 | 29 | 33 | nan | nan | nan | Caatinga | 99.2 |
| c2958605-7390-3583-adad-2f301a39c7b3 | -16.47316 | -45.01478 | 2025-08-07 11:55:00 | TERRA_M-M | UBAÍ | MINAS GERAIS | Brasil | 3170008 | 31 | 33 | nan | nan | nan | Cerrado | 29.8 |
| d11bac12-7ea4-3fcc-afbd-5a158b5860d1 | -14.24516 | -43.75163 | 2025-08-07 11:55:00 | TERRA_M-M | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 9.4 |
| a8114b08-1732-3a19-984f-44528ff7230f | -14.56258 | -45.59164 | 2025-08-07 11:55:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 8a4f2114-7bca-3b17-8b6e-7af39120c067 | -16.11616 | -41.26797 | 2025-08-07 11:55:00 | TERRA_M-M | PEDRA AZUL | MINAS GERAIS | Brasil | 3148707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| 372f7f01-75e7-30f4-8d8f-01195c8105f4 | -16.11487 | -41.27715 | 2025-08-07 11:55:00 | TERRA_M-M | PEDRA AZUL | MINAS GERAIS | Brasil | 3148707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| 976a8582-7b1d-3455-b39e-dac960e55d98 | -14.55203 | -45.58986 | 2025-08-07 11:55:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 12.7 |
| f29d99dc-dd48-3eaf-88a8-66e353ebb9c0 | -15.44152 | -47.59874 | 2025-08-07 11:55:00 | TERRA_M-M | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 13.0 |
| d529ae73-ce85-33c7-8351-a6b0fd112068 | -16.339 | -43.51658 | 2025-08-07 11:55:00 | TERRA_M-M | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 5cbfc98d-263a-3b0f-97e3-171ae652e47a | -13.64287 | -42.72142 | 2025-08-07 11:55:00 | TERRA_M-M | IGAPORÃ | BAHIA | Brasil | 2913408 | 29 | 33 | nan | nan | nan | Caatinga | 38.5 |
| e8569609-6007-32a8-a7e3-ac53470b2814 | -14.56043 | -45.60491 | 2025-08-07 11:55:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 22.8 |
| 2d100739-c651-3e75-a9a4-9be7dfd63e1e | -16.27461 | -43.82642 | 2025-08-07 11:55:00 | TERRA_M-M | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 6.5 |
| e0c55045-ed8b-3aea-b22d-7ecb95cde9a0 | -16.27308 | -43.83654 | 2025-08-07 11:55:00 | TERRA_M-M | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 0f9aee22-f608-337a-8165-81dc3dffe689 | -21.44013 | -45.11816 | 2025-08-07 11:57:00 | TERRA_M-M | CARMO DA CACHOEIRA | MINAS GERAIS | Brasil | 3113909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 14.7 |
| 48e84502-faf6-3a8f-982b-7c74b74641a2 | -21.36607 | -44.22683 | 2025-08-07 11:57:00 | TERRA_M-M | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 18.3 |
| ecd0bc6e-495a-36c5-88be-4f733325e854 | -19.17475 | -48.38414 | 2025-08-07 11:57:00 | TERRA_M-M | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 469885e6-4c19-3da5-b5b0-e615bec5aa6c | -20.67387 | -42.27513 | 2025-08-07 11:57:00 | TERRA_M-M | FERVEDOURO | MINAS GERAIS | Brasil | 3125952 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| e5dd891c-c6e8-3cd4-86fc-635e4a2b3cec | -19.1716 | -48.40194 | 2025-08-07 11:57:00 | TERRA_M-M | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 9.8 |
| f1b1027c-dba4-362c-baf7-f2824ac07b3b | -6.2604 | -45.2504 | 2025-08-07 12:00:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 101.6 |
| b6f41325-4e2f-308c-9665-43833a02bfd0 | -10.6441 | -44.7413 | 2025-08-07 12:00:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 110.4 |
| c184fac8-9b1e-3689-aead-3ac8d2fde389 | -6.5192 | -45.5915 | 2025-08-07 12:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 89.8 |
| d01677f4-97f8-3812-bf9b-7c36438ba94d | -6.2789 | -45.2716 | 2025-08-07 12:00:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 122.7 |
| ebb4154f-48c8-312f-b6a2-1439e287f272 | -6.2602 | -45.2731 | 2025-08-07 12:00:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 109.9 |
| ef341dad-0833-313d-86ac-51d2d9e0d753 | -6.2792 | -45.249 | 2025-08-07 12:00:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 110.9 |
| 8d4fac9d-b6ab-3536-95a7-e7644f070f1f | -6.2602 | -45.2731 | 2025-08-07 12:10:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 134.7 |
| 167ad6b8-b6d6-3026-8f3e-25430a6e6187 | -6.2604 | -45.2504 | 2025-08-07 12:10:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 169.2 |
| fad75526-2088-3111-b7d8-5be30368e256 | -12.6314 | -48.1091 | 2025-08-07 12:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 79.2 |
| 7521e8af-5608-32da-8b11-212b9d17f193 | -10.6441 | -44.7413 | 2025-08-07 12:10:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 152.3 |
| 7abd8a9e-a172-3c83-9bdf-ef1777ba86be | -5.678 | -41.3987 | 2025-08-07 12:10:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 96.7 |
| 943f029d-2867-3c9b-811e-fa71ea015d80 | -6.2792 | -45.249 | 2025-08-07 12:10:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 118.8 |


[Clique aqui para ver as próximas entradas](README29.md)
