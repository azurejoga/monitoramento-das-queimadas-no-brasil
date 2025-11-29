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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c324fe9a-fdc2-3f75-958e-79706b10b0f0 | -8.1822 | -43.2034 | 2025-11-29 04:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 58.7 |
| 0186f9eb-be6c-3770-a692-2a97e4efbb4b | -2.7845 | -47.4125 | 2025-11-29 04:20:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 57.2 |
| 0988fc72-5304-30cc-be2f-1bb77415860f | -2.6526 | -48.0244 | 2025-11-29 04:20:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 50.9 |
| 89ea1238-37e4-3083-b299-3b437fbf864e | -20.1813 | -52.3754 | 2025-11-29 04:20:00 | GOES-19 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 77.6 |
| 4c826150-5861-3dfc-9ce5-a39c94d8c5ca | -2.6322 | -48.542 | 2025-11-29 04:20:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 1f4ce1fe-13c2-3c08-9841-465b82607ee9 | -2.7845 | -47.4343 | 2025-11-29 04:20:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 29dbb0b1-8163-3ce3-b27a-e5fa17b2575c | -8.1633 | -43.2055 | 2025-11-29 04:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 104.2 |
| 73eecb1e-24f3-35d7-a50e-3c9123655a98 | -8.0321 | -43.1257 | 2025-11-29 04:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 50.9 |
| 7d45672b-62b8-3b50-abbf-de7122ed9568 | -25.91224 | -52.52884 | 2025-11-29 04:21:00 | NOAA-21 | CHOPINZINHO | PARANÁ | Brasil | 4105409 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 0a146878-3497-3dfb-94a1-9548fd692a48 | -25.23461 | -50.76717 | 2025-11-29 04:21:00 | NOAA-21 | GUAMIRANGA | PARANÁ | Brasil | 4108957 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| b6be7834-883f-30f7-a193-298181ee57f1 | -25.1791 | -49.40024 | 2025-11-29 04:21:00 | NOAA-21 | ITAPERUÇU | PARANÁ | Brasil | 4111258 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| e1750f6e-c436-35cf-8174-ed979a249dc5 | -27.65456 | -50.67512 | 2025-11-29 04:21:00 | NOAA-21 | SÃO JOSÉ DO CERRITO | SANTA CATARINA | Brasil | 4216800 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| fbef5b39-5d02-3570-a5ca-0267094c734a | -25.1757 | -49.39957 | 2025-11-29 04:21:00 | NOAA-21 | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 95a3ed75-f9d2-3ec5-bba9-0b03d283b150 | -25.34682 | -51.15284 | 2025-11-29 04:21:00 | NOAA-21 | GUARAPUAVA | PARANÁ | Brasil | 4109401 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| eb76b08b-7224-3897-b65b-4bc3230c3b90 | -20.1807 | -52.3975 | 2025-11-29 04:30:00 | GOES-19 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 63.7 |
| 9ed93ad3-8888-3428-80ef-bc8f17a07fbd | -8.1633 | -43.2055 | 2025-11-29 04:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 85.6 |
| a2f79605-c07f-3d26-bbec-a95a0e9e923e | -8.1636 | -43.1819 | 2025-11-29 04:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 47.7 |
| 5c5b7784-9d9b-3d24-8b9c-98949d965758 | -2.6341 | -48.0249 | 2025-11-29 04:30:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 46.9 |
| de353f27-3649-379b-8072-c1983c1e3674 | -20.2016 | -52.3717 | 2025-11-29 04:30:00 | GOES-19 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 63.3 |
| 4e7fc1a2-2e9e-3981-8179-a67931d4a498 | -20.1813 | -52.3754 | 2025-11-29 04:30:00 | GOES-19 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 120.7 |
| 6e4127a0-4a1d-3e63-b8b2-4fedb929ef4f | -8.0321 | -43.1257 | 2025-11-29 04:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 47.6 |
| 6e6754b5-f296-3ad4-b0ca-584db5ef04e0 | -2.6322 | -48.542 | 2025-11-29 04:30:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 54.9 |
| 67001d48-b885-3128-b200-c324a451b1bf | -20.1807 | -52.3975 | 2025-11-29 04:40:00 | GOES-19 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 70.8 |
| 796138ae-7fe5-3eaf-9bfd-5d7a3a8c4b14 | -8.1822 | -43.2034 | 2025-11-29 04:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 49.8 |
| fbfe05bd-a2c0-3b5b-85ed-4402ef357ab6 | -20.2016 | -52.3717 | 2025-11-29 04:40:00 | GOES-19 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 112.6 |
| 289b43eb-4830-3d50-986a-775530048e49 | -20.1813 | -52.3754 | 2025-11-29 04:40:00 | GOES-19 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 168.1 |
| e1445b2d-59ca-322e-94cf-a079a48cc45a | -8.1633 | -43.2055 | 2025-11-29 04:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 101.6 |
| af970c7c-7a48-3350-beb6-752fd4e3bbcf | 1.66993 | -50.71552 | 2025-11-29 04:40:00 | NPP-375D | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4c766fb5-fb08-35f1-a1bf-0507dcbf1790 | 0.85464 | -50.18539 | 2025-11-29 04:40:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0e8c12a6-152e-359b-9abc-c4f93f566076 | 2.03051 | -55.79152 | 2025-11-29 04:40:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0a10b9f4-38d7-3acb-8c75-69e5c886190f | 1.67354 | -50.71496 | 2025-11-29 04:40:00 | NPP-375D | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4437b5dc-4dfb-398c-9c68-c6e7708de959 | -4.08494 | -50.75417 | 2025-11-29 04:42:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 69d39aaa-859b-3596-bbb1-549d802c3230 | -3.30591 | -50.20409 | 2025-11-29 04:42:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f628ff32-331e-3af6-bbde-09fedfd37931 | -4.16688 | -43.75443 | 2025-11-29 04:42:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b6bd5fa2-8e04-39ba-9b6f-bfc2427511c1 | -2.69907 | -51.79286 | 2025-11-29 04:42:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4e4f87df-cdd7-30df-8ab1-0365b28311c4 | -4.01363 | -49.11244 | 2025-11-29 04:42:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 59e97f29-3fa5-359e-b8f0-729272005553 | -4.10553 | -42.90892 | 2025-11-29 04:42:00 | NPP-375D | DUQUE BACELAR | MARANHÃO | Brasil | 2103901 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 01ed29e2-d9af-302a-9b54-d9c775c85b5f | -3.84049 | -44.1253 | 2025-11-29 04:42:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| aa5901ba-e14a-3b13-a38e-4cc3d26cdd2d | -2.95652 | -49.17964 | 2025-11-29 04:42:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 77cec7f6-4ac2-3b1e-a6ac-2e132917359f | -3.00398 | -45.42015 | 2025-11-29 04:42:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 83a87ff6-da62-3b04-94c3-f7d8f5fa76e9 | -2.30162 | -47.73841 | 2025-11-29 04:42:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2e8b8e2c-14f8-307e-abad-d1e33ca8bba1 | -3.2413 | -50.58922 | 2025-11-29 04:42:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 67046d84-7be2-365d-8bd7-6b2555e2e4e4 | -2.42162 | -47.22946 | 2025-11-29 04:42:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 1c2e3299-0ddd-3ebd-ad39-5f5f7753c180 | -3.32603 | -53.32332 | 2025-11-29 04:42:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 45b73e04-8588-3bc3-aa35-bc239b6fa8cf | -4.93358 | -43.46902 | 2025-11-29 04:42:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4cdd316d-3740-3e60-be5a-0f3eee30afe7 | -6.60113 | -43.6885 | 2025-11-29 04:42:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f318e0d4-d0f7-35af-a458-6dea768c7bc1 | -1.48822 | -45.78988 | 2025-11-29 04:42:00 | NPP-375D | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 64ca3df6-c8b4-3770-a8f6-4c5bcb854d00 | -5.07278 | -40.82131 | 2025-11-29 04:42:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| a7bd03fb-46b0-395e-bc47-024ad5d14b31 | -3.35818 | -50.49042 | 2025-11-29 04:42:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ace7c234-fd2e-3747-8cb7-abe4bf700c11 | -1.49561 | -47.80535 | 2025-11-29 04:42:00 | NPP-375D | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 10d62884-d792-349f-a6e5-c90cefd84f1a | -4.85215 | -38.74008 | 2025-11-29 04:42:00 | NPP-375D | IBARETAMA | CEARÁ | Brasil | 2305266 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 5954e22c-e432-392a-8098-f810aff53de0 | -1.35296 | -53.09419 | 2025-11-29 04:42:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 03418f2d-d76a-3ce6-b9cd-b0a0f44f3bb1 | -5.00362 | -38.53859 | 2025-11-29 04:42:00 | NPP-375D | IBICUITINGA | CEARÁ | Brasil | 2305332 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 85c4e5ec-25fe-30bd-874c-77a0515b724d | -2.65096 | -48.0315 | 2025-11-29 04:42:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c988b4bc-300f-3015-8a08-697386262039 | -1.35549 | -53.09305 | 2025-11-29 04:42:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d7a6d4bc-c5f3-3b98-9427-a56f165524bb | -2.65151 | -48.02803 | 2025-11-29 04:42:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 76ea31bc-926d-3131-9aef-b0dd3f565ec3 | -2.89963 | -50.23319 | 2025-11-29 04:42:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fb0c0a3d-21f5-319f-8c1d-026005356c25 | -3.20497 | -46.82006 | 2025-11-29 04:42:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3e419ac5-16b1-3093-9787-d1fb13fa21d8 | -2.64376 | -48.03393 | 2025-11-29 04:42:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 488b21cf-b6de-3d34-937b-8dc60dc72025 | -4.47375 | -50.09203 | 2025-11-29 04:42:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bf886886-f5e7-3d95-9e00-8ca05a1f6b1c | -2.46795 | -48.22652 | 2025-11-29 04:42:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| f94d09c0-2013-32d3-bdaa-6775972dcd6b | -2.7857 | -47.4168 | 2025-11-29 04:42:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 09a6ff7a-82e2-3f90-9f98-b97387b91142 | -4.43505 | -40.92657 | 2025-11-29 04:42:00 | NPP-375D | CROATÁ | CEARÁ | Brasil | 2304236 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| f4b60c70-35dc-3d85-bcdb-36ce02c31be9 | -2.63358 | -48.5489 | 2025-11-29 04:42:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 85dce2c2-3b01-36e0-bc38-c1609d610b5f | -6.70087 | -41.46347 | 2025-11-29 04:42:00 | NPP-375D | SÃO JOSÉ DO PIAUÍ | PIAUÍ | Brasil | 2210201 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 28d14641-e27e-3a6c-8831-0307ce9dfeaf | -0.97094 | -47.56705 | 2025-11-29 04:42:00 | NPP-375D | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2c4eec42-a1d1-3335-9fb8-97b138b7cc0a | -2.74568 | -49.86377 | 2025-11-29 04:42:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 50cfcc53-c869-32db-b817-3f9aca3a4903 | -3.17785 | -45.62096 | 2025-11-29 04:42:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a9304d64-caf3-3815-a347-f73f5ca7656b | -2.4324 | -48.60229 | 2025-11-29 04:42:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3ed3f894-c9a4-3005-80d4-3314bbd8d478 | -0.75112 | -47.75921 | 2025-11-29 04:42:00 | NPP-375D | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 893a73d8-84a6-3923-a089-ff07f25026d3 | -2.63135 | -48.5415 | 2025-11-29 04:42:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 8e503e2b-0ee8-30b4-965e-d8d439fe8f45 | -3.94846 | -44.76753 | 2025-11-29 04:42:00 | NPP-375D | LAGO VERDE | MARANHÃO | Brasil | 2105906 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3bd6ad80-5900-3c5a-b5fd-894cbb05e32a | -2.73442 | -45.26179 | 2025-11-29 04:42:00 | NPP-375D | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e72bc189-bca3-3528-b2b5-e3b687a3658a | -3.20781 | -46.82431 | 2025-11-29 04:42:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 65deaaa1-865c-31ee-958d-7b4378af9b7c | -1.08485 | -53.18128 | 2025-11-29 04:42:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e5d94477-e5bb-31e9-91d5-68605b9a1cde | -2.17666 | -48.42079 | 2025-11-29 04:42:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4c8e87e4-a6ed-3378-ad18-b19a954ff82a | -2.95984 | -49.18016 | 2025-11-29 04:42:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9b899655-9846-35a3-a6a9-0552d3921021 | -3.1726 | -51.2489 | 2025-11-29 04:42:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 252ae0b5-8757-37e4-a12f-408f7352b279 | -4.1012 | -42.90828 | 2025-11-29 04:42:00 | NPP-375D | DUQUE BACELAR | MARANHÃO | Brasil | 2103901 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1a4c434b-3c14-39b3-9675-c22abe28f864 | -4.62917 | -43.98793 | 2025-11-29 04:42:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| eb4687ce-c52a-32ff-ac0f-294b3723cfeb | -4.11616 | -44.90251 | 2025-11-29 04:42:00 | NPP-375D | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 64dae453-968c-3ef0-806e-ced064e25512 | -4.11544 | -44.90715 | 2025-11-29 04:42:00 | NPP-375D | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 08ec7af2-1f0c-3d5c-87db-d0608b4c1b7d | -4.00977 | -49.11537 | 2025-11-29 04:42:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 73f13d0c-fe3e-30fa-9ce6-79aa25aef7d6 | -3.1658 | -45.24166 | 2025-11-29 04:42:00 | NPP-375D | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 02ec545f-98a7-383b-a759-9631df66a8cb | -2.92583 | -53.07426 | 2025-11-29 04:42:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| df5a8b1d-ad24-33da-91ac-2745da63731d | -3.84572 | -44.12838 | 2025-11-29 04:42:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cf1c1419-54e1-33bb-a26f-51236bf408e0 | -2.96071 | -50.99246 | 2025-11-29 04:42:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 96265a7c-efc7-3db0-a95e-2b70445715d2 | -2.90485 | -49.80524 | 2025-11-29 04:42:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 26d9448d-e75c-3724-b1bd-aed15e0e888a | -2.65042 | -48.03497 | 2025-11-29 04:42:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f0dec8ad-e540-3b71-86e8-efba4d59849f | -2.22598 | -47.5117 | 2025-11-29 04:42:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 530a69b8-1523-306f-9c14-f0d9494309ce | -3.84447 | -44.12591 | 2025-11-29 04:42:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ee8587c3-4ac5-30c1-b496-7ca00abf7771 | -2.99969 | -45.42382 | 2025-11-29 04:42:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4d02db02-e6c8-393f-b37f-e7182ed7284e | -3.17851 | -45.61681 | 2025-11-29 04:42:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 081f0127-30ae-33bd-beef-3b51a739a748 | -2.64431 | -48.03046 | 2025-11-29 04:42:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a6c68c68-c9c0-3644-ae15-3d3847c80072 | -2.96359 | -50.99678 | 2025-11-29 04:42:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4a708253-0f2e-3b0b-9c8f-d8fb674ae629 | -2.06541 | -53.22561 | 2025-11-29 04:42:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ecd230e9-85ea-3c6a-a3ea-31fe40471feb | -2.74737 | -47.13228 | 2025-11-29 04:42:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ef219c37-37b8-37bb-b725-2daa71960876 | -2.70604 | -48.34837 | 2025-11-29 04:42:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bacf0507-a925-32e6-b185-93d42ed5c2e1 | -3.03016 | -51.43731 | 2025-11-29 04:42:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1e2a2648-00dc-3d46-8dc2-34c32b417d0e | -2.6864 | -47.36184 | 2025-11-29 04:42:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |


[Clique aqui para ver as próximas entradas](README20.md)
