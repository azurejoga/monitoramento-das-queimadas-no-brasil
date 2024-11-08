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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2e8c3cfd-688f-3d3b-96c6-18ea135f0cc0 | -1.1283 | -53.72924 | 2024-11-08 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0a47cf45-a3d2-3abd-a787-1404331d12ca | -3.62017 | -50.19662 | 2024-11-08 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 32b24235-00e4-3514-ae74-8b11610e189e | -4.87041 | -42.95503 | 2024-11-08 04:53:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 26.2 |
| b1385165-baa5-357c-b866-3e2d2c971ac3 | -3.96948 | -48.17711 | 2024-11-08 04:53:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 26.9 |
| b6d53221-2b43-3b1f-ace0-1d43a1759491 | -5.17359 | -44.22642 | 2024-11-08 04:53:00 | NOAA-21 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0ed28df7-e3a5-3763-a061-6fe8a70fbeb9 | -2.68921 | -51.81858 | 2024-11-08 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5d9f2a41-7d9c-3bb7-b8ef-d059ac9370bd | -4.78448 | -45.64724 | 2024-11-08 04:53:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5f7d0976-3913-3b12-9b51-eb397f335fdd | -3.07036 | -54.77907 | 2024-11-08 04:53:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 75edaffa-9b7b-3e34-bafc-497221009e8a | -1.14641 | -52.00256 | 2024-11-08 04:53:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 53da7154-d160-38f1-a574-bbf025720079 | -3.80904 | -43.6003 | 2024-11-08 04:53:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 80f88521-64b0-3b36-96e3-875ff19f96d7 | -3.97396 | -48.17304 | 2024-11-08 04:53:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| cc901574-e084-38f9-92d8-00dd49fc0ef6 | -2.62237 | -51.91707 | 2024-11-08 04:53:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ade15c87-8a3e-3256-b46a-2e98334b5d2f | -4.77033 | -45.74233 | 2024-11-08 04:53:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c87db49f-c0e1-3c37-a022-a78948e5af18 | -3.06547 | -52.50083 | 2024-11-08 04:53:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4258a6a5-5deb-30f1-b7d7-3cd20a26ca00 | -1.67272 | -53.81657 | 2024-11-08 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6fad7738-50d2-3bce-8af4-15a4d8dbf496 | -2.89895 | -54.60346 | 2024-11-08 04:53:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ec7fb235-e863-3baf-a85a-437b59f3cd45 | -2.83724 | -53.97894 | 2024-11-08 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ca9daf8a-c102-3e26-a1ac-0b0cd1070f49 | -3.07422 | -50.56758 | 2024-11-08 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 0f5198f3-d029-368a-9819-72abd9406115 | -2.88593 | -48.28546 | 2024-11-08 04:53:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c30d325c-7bd7-3724-a6cc-16222e75f484 | -2.22062 | -53.72494 | 2024-11-08 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 73e7bbe4-de1c-32e6-9750-ca2cf1ad5132 | -1.75232 | -54.1957 | 2024-11-08 04:53:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e6c97f42-4695-307c-b298-64266cbd10b5 | -3.05256 | -51.33976 | 2024-11-08 04:53:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c4df42a3-37ea-3995-bc7c-9d3cc74d11aa | -2.21109 | -46.36336 | 2024-11-08 04:53:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bc55889e-43bb-3e52-b2b7-aae64c4ac564 | -0.60577 | -49.55938 | 2024-11-08 04:53:00 | NOAA-21 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cc4dde49-0590-3579-adfa-1863414e8f25 | -2.62567 | -51.91758 | 2024-11-08 04:53:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1d490edc-582a-37a7-bf46-0530ce1a7f34 | -3.06616 | -53.90718 | 2024-11-08 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 512c76cc-efd5-39fa-b5aa-344370d85b52 | -2.82586 | -52.94343 | 2024-11-08 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| caf3f4f4-5523-320e-a69e-a4734337977f | -5.17318 | -44.2293 | 2024-11-08 04:53:00 | NOAA-21 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1bb6fa96-a129-3908-ab6c-a3ab2933cd88 | -2.03215 | -52.34179 | 2024-11-08 04:53:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| d2635f57-76f0-382b-9272-24c37bab552f | -1.38217 | -47.50328 | 2024-11-08 04:53:00 | NOAA-21 | SANTA MARIA DO PARÁ | PARÁ | Brasil | 1506609 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cad3819e-714f-3519-bb17-3fd460a934b9 | -4.71367 | -49.60658 | 2024-11-08 04:53:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 02fb9acd-c28d-3adc-99d1-9fe9adebaa5f | -3.03284 | -53.27224 | 2024-11-08 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5608b749-4dab-37be-b724-563f403c5243 | -4.46428 | -50.25043 | 2024-11-08 04:53:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 76505dcb-e3f6-303a-b612-ef8f16bd5fe5 | -3.95648 | -48.16091 | 2024-11-08 04:53:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 057739f1-8d6f-3b1a-8c97-326cde8f625e | -3.37465 | -50.22028 | 2024-11-08 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c811a016-b8d4-3bdd-b643-86ba567190f3 | -3.95718 | -48.15634 | 2024-11-08 04:53:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 2a3b1239-4241-34d5-8a15-b965354c5029 | -0.38295 | -51.44347 | 2024-11-08 04:53:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1793446a-b6e3-310d-91c9-2bc3b36d6eeb | -4.24725 | -48.53971 | 2024-11-08 04:53:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e30209e3-d510-3638-bba5-3b7f950bd3b8 | -3.37409 | -50.22396 | 2024-11-08 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 52e7256e-3b8f-30e2-b031-85433091a745 | -3.95957 | -48.16604 | 2024-11-08 04:53:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 18.5 |
| cf9c443e-11aa-35b1-8a5c-e0eef775d393 | -1.56616 | -52.25508 | 2024-11-08 04:53:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a990f42f-7e3b-396b-93bc-8ed759c48bcc | -2.97966 | -50.29852 | 2024-11-08 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b7da9e84-60ad-39e7-87da-eb8ae5e1e891 | -4.91748 | -44.04494 | 2024-11-08 04:53:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cf977739-c449-36cd-b566-fd679effd147 | -1.52555 | -51.11951 | 2024-11-08 04:53:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e691cffd-3e7b-38db-a660-10a03a45acd6 | 1.00448 | -60.5844 | 2024-11-08 04:53:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ee2d2b4d-aba8-348c-9493-9993d511e00b | -0.9686 | -52.44244 | 2024-11-08 04:53:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 43b6deee-8088-3a7d-b416-8c97d5718cc2 | -2.16111 | -53.65511 | 2024-11-08 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| ea370f58-d644-369a-a790-8b30da2d6e94 | -3.96139 | -48.12861 | 2024-11-08 04:53:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0247498c-a871-3853-a191-45e8238ef64b | -4.9179 | -44.04192 | 2024-11-08 04:53:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 47a85ed2-505b-3c50-a846-6094d739d89c | 0.74189 | -59.77307 | 2024-11-08 04:53:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cf339622-c115-3a43-a5ff-2c8aa00c6700 | -3.25081 | -50.02049 | 2024-11-08 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b4c464bc-351e-3856-b184-f3bfb95cb94d | -2.5666 | -47.34094 | 2024-11-08 04:53:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f5891f17-fd31-3ff0-90ac-478c69c740b9 | -3.55658 | -47.38184 | 2024-11-08 04:53:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 71.5 |
| 2782eebc-ee78-3473-a42e-cf93c4f5522e | -4.56002 | -46.3377 | 2024-11-08 04:53:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0cdf1f37-01d9-3459-a893-0de9cb860334 | -3.38894 | -54.17481 | 2024-11-08 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 42b68389-170e-30de-bb52-0040f53bff62 | -4.24259 | -46.52345 | 2024-11-08 04:53:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 47839f64-0e55-3aa8-ae93-373e4c1922ee | -3.11748 | -53.12224 | 2024-11-08 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 002ae6ee-15b7-39f7-9ab2-a08fafb7823b | -4.68081 | -46.45182 | 2024-11-08 04:53:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2801765c-0962-3838-ad63-e2e49fa02e43 | -3.37693 | -50.22817 | 2024-11-08 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 87f09014-1796-3570-b817-f854cc1834ae | -2.21662 | -53.72811 | 2024-11-08 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5bc02191-c9fa-3605-839d-cfa48aa71d91 | -3.37745 | -52.35595 | 2024-11-08 04:53:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 170e7a64-e98b-3358-a7da-400138f34f3a | -2.82142 | -52.94992 | 2024-11-08 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 77634969-266a-3046-b4c0-b60b410fafff | -4.91848 | -44.04391 | 2024-11-08 04:53:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7c7d11c9-5099-3702-97ac-9ba0838beb03 | -2.07882 | -52.04234 | 2024-11-08 04:53:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| feba22e9-3957-3577-8358-883d3305bf0d | -3.06674 | -53.90349 | 2024-11-08 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5e7761a6-9055-3d8b-9b6d-62b7f8e49c54 | -2.05286 | -53.29591 | 2024-11-08 04:53:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e1373bac-da3f-3232-ad31-f962386b395b | -2.69577 | -51.68962 | 2024-11-08 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 073a415f-ffc7-3b28-bc4e-10e975e21e87 | -2.36152 | -46.80808 | 2024-11-08 04:53:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3abea069-600e-3565-8703-c0e0c2c0a6f7 | -2.61727 | -51.75477 | 2024-11-08 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 90deb7ed-f849-39d8-b715-0f3ec60815cb | -2.92184 | -51.04249 | 2024-11-08 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6dad4d25-2eb5-363c-be56-8391e62b998a | -2.606 | -51.30228 | 2024-11-08 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| e03e80f0-46a2-34cf-80ac-bea44d2a40b6 | -4.14242 | -44.41849 | 2024-11-08 04:53:00 | NOAA-21 | ALTO ALEGRE DO MARANHÃO | MARANHÃO | Brasil | 2100436 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8368ccf1-1fb7-3f00-9851-81f9de74d012 | -1.06173 | -53.66163 | 2024-11-08 04:53:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9253b4cc-8e2f-3c65-96e3-ff674935d5be | -1.50532 | -51.53118 | 2024-11-08 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8df2f855-e022-3c22-b6ef-58e8ee0dc948 | -1.53603 | -52.01056 | 2024-11-08 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 44e89a4c-1dbc-3904-9f99-5edb34713eca | -2.21449 | -53.6749 | 2024-11-08 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cbefbdb8-c2ab-3614-9f8c-786f15f37ec7 | -3.08035 | -53.27595 | 2024-11-08 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 026a3481-5285-3022-86c8-9f376329cb19 | -1.3775 | -52.26424 | 2024-11-08 04:53:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 953c31a9-1174-3f38-a879-c087cbda5849 | -3.0143 | -53.43385 | 2024-11-08 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7abc916e-8595-3de8-972d-2a80d39d18ec | -2.25821 | -53.73075 | 2024-11-08 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0cf14d4d-061c-3192-a71b-de46322c93a2 | -4.3059 | -48.61909 | 2024-11-08 04:53:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d1701159-d1f3-3e9b-b260-d69a0eae9e98 | -3.0457 | -53.27785 | 2024-11-08 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| f810982f-5bab-31d3-bfec-1bec3a9d23f6 | -0.90098 | -51.76348 | 2024-11-08 04:53:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 50db6d05-10a3-3fc7-a1a7-34a14dff4460 | -3.71935 | -49.00314 | 2024-11-08 04:53:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4c990cb5-8ce4-3ea6-930f-33c06fac93f3 | -3.18045 | -53.84996 | 2024-11-08 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cf9ee28c-d86b-3935-9ed4-7fc6eff8ede8 | -2.19731 | -48.37641 | 2024-11-08 04:53:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e3a1cf9b-9da9-382d-900f-c1a1a0de193f | -2.86991 | -50.32661 | 2024-11-08 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8e7ad4e5-ad34-3a3f-86e8-f0d9180b5f54 | -2.61262 | -51.30329 | 2024-11-08 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 79125a19-3f40-3310-9c0b-f65d98a3c792 | -2.9213 | -51.04598 | 2024-11-08 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 382414d2-1f91-300d-8df8-8e6652db22cd | -3.59013 | -43.02903 | 2024-11-08 04:53:00 | NOAA-21 | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7fbfd808-e756-341a-b020-d79b6a7ef33a | -2.80241 | -52.94344 | 2024-11-08 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 24.7 |
| 80defbda-9398-3ec5-a756-52192e9494a0 | -4.6827 | -46.44559 | 2024-11-08 04:53:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| b21ad95d-3f29-3c9d-ae51-81af07293aa3 | -2.9032 | -51.46883 | 2024-11-08 04:53:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1991e93d-a51a-33d0-92a4-c8a19882e17f | -3.458 | -52.01325 | 2024-11-08 04:53:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dc6c6fa0-b39b-3ede-8a2a-bd894d9f5060 | -1.46191 | -52.57311 | 2024-11-08 04:53:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 21b1bca1-057f-3488-9b98-371e202c9419 | -3.19663 | -53.39645 | 2024-11-08 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5bfbe48a-e6ff-3ce2-acf5-4b4c7d7f6c16 | -3.01161 | -53.23266 | 2024-11-08 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 856f0e32-2bd7-3f11-9a84-3dd9db7d515c | -1.50601 | -52.07286 | 2024-11-08 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 4b791546-43e9-34a7-abdc-c796aaaf5b32 | -3.03899 | -53.27682 | 2024-11-08 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 566a6492-3087-3206-91a3-49a9d9097521 | -3.03675 | -51.52811 | 2024-11-08 04:53:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |


[Clique aqui para ver as próximas entradas](README27.md)
