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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2be54590-e354-3e9d-ab7d-0753555e8e90 | -10.36063 | -57.22882 | 2025-06-19 05:12:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 08c15abb-0004-36e2-9dae-ef215b173dba | -12.80092 | -48.73176 | 2025-06-19 05:12:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 18df5e47-28f6-3a5e-820a-04dc73f98195 | -12.02804 | -57.09752 | 2025-06-19 05:12:00 | NOAA-21 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4f25aa6d-a3f0-3b07-a649-240bf14ea756 | -9.49141 | -56.08331 | 2025-06-19 05:12:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 2c449a81-0583-3cbd-a9ba-0ed6dda3c061 | -10.64519 | -49.45913 | 2025-06-19 05:12:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 18afa0c2-0c2d-31c8-aa8d-10d593c6b4e4 | -11.81861 | -54.49936 | 2025-06-19 05:12:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 44a6567c-b835-318a-b3a4-b282fcc6da66 | -9.50058 | -56.09245 | 2025-06-19 05:12:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 02e8c6d0-161a-3027-a91f-f38883f22734 | -11.53319 | -54.38003 | 2025-06-19 05:12:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 947c9bdd-4d9d-3e08-a3b6-7c75117a9b7a | -10.28256 | -60.5398 | 2025-06-19 05:12:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 346b83c7-8e4f-3a2a-9b3a-92837625d472 | -12.22426 | -55.52583 | 2025-06-19 05:12:00 | NOAA-21 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 28915201-0cd9-3a62-a1bd-7fd6aa4d2242 | -11.56821 | -47.43338 | 2025-06-19 05:12:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 25eb1501-5609-35fc-9e99-7d63519b1588 | -10.64036 | -49.45517 | 2025-06-19 05:12:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5bf12b7a-beff-36ae-a848-4e37ab7a6cb1 | -12.02466 | -57.09698 | 2025-06-19 05:12:00 | NOAA-21 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1e7db1ba-0d71-3850-b4fe-1effedda56eb | -11.94764 | -58.75477 | 2025-06-19 05:12:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 192e2e46-4235-3705-b984-d18b95a76ac7 | -13.29 | -57.07025 | 2025-06-19 05:12:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 5b3a879c-3921-30f1-8d2a-71988b10c27f | -9.79068 | -47.18848 | 2025-06-19 05:12:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7dbf8518-1a88-319e-91f1-98f1f1093b23 | -11.13754 | -53.93594 | 2025-06-19 05:12:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ca0acf8e-318c-3f8a-bc6d-2d63713eb7dc | -9.334 | -57.84557 | 2025-06-19 05:12:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f0d41e80-a746-3b5d-aea7-68ff735bcb4d | -11.96083 | -58.73535 | 2025-06-19 05:12:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bb48ccc1-3dd0-32cb-87e0-3b78b559465c | -13.64907 | -53.94131 | 2025-06-19 05:12:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 21f92d52-0907-3c84-b592-3ed65558ab14 | -11.95808 | -58.73132 | 2025-06-19 05:12:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 289abb54-df1b-37f5-a386-f3310696ad26 | -9.79725 | -47.18497 | 2025-06-19 05:12:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 90c7248a-dc1d-3448-8725-8ddc34c84daa | -11.80668 | -57.35286 | 2025-06-19 05:12:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 572a3335-496a-37d6-af8a-16251938f7b5 | -14.44014 | -48.89996 | 2025-06-19 05:12:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| b4d0d97f-107f-39b4-8972-bbef456edcb0 | -13.57848 | -59.20472 | 2025-06-19 05:12:00 | NOAA-21 | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 58d512c2-991e-3c8d-8719-8876eec72086 | -11.5249 | -56.99144 | 2025-06-19 05:12:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 645a8410-ee0d-3906-814e-d00183ae1d9d | -11.77055 | -54.3695 | 2025-06-19 05:12:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4613a3e5-71d7-3c99-aa17-99d0251d409c | -10.86065 | -53.76834 | 2025-06-19 05:12:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 866f8448-2b53-3411-9b71-29b1e9030fff | -9.79366 | -47.18287 | 2025-06-19 05:12:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 2c64e297-e60b-3610-b75c-5600ec48a05b | -9.38178 | -63.43297 | 2025-06-19 05:12:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 316c8e11-3b9f-3939-a8dd-d1019aa751fb | -12.02859 | -57.09383 | 2025-06-19 05:12:00 | NOAA-21 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 917158f7-c235-3b95-a8cf-4c85d35dc382 | -9.79668 | -47.18941 | 2025-06-19 05:12:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| a8d9d883-27c5-3a68-a46c-e0854757584a | -9.3979 | -65.51632 | 2025-06-19 05:12:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 446473f4-2fe9-372b-beed-490f095d2a5c | -9.32987 | -47.83105 | 2025-06-19 05:12:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1e2109f3-cbd7-3893-b41e-e5f80c62515a | -13.57793 | -59.20824 | 2025-06-19 05:12:00 | NOAA-21 | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 988a9d34-c95b-358c-bef8-e1c3e7d14739 | -10.09683 | -60.49404 | 2025-06-19 05:12:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 590c1768-fce5-3e1f-a2eb-7e757e8b3649 | -11.94379 | -58.75774 | 2025-06-19 05:12:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 2fa2d67b-ba28-3398-85a2-9811b0c6b176 | -10.27787 | -60.54683 | 2025-06-19 05:12:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 149d1aea-365b-3e2a-920c-6960c07753f3 | -11.95204 | -58.74829 | 2025-06-19 05:12:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 19.3 |
| 4ce6b34a-a586-3674-8d8e-e46468793839 | -11.82242 | -54.49993 | 2025-06-19 05:12:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cdf3f301-a893-36a7-b98d-1b8c28612cfc | -12.58479 | -56.98337 | 2025-06-19 05:12:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5bf4c731-db93-3588-9b1b-7957fd5d16e4 | -11.0804 | -55.05464 | 2025-06-19 05:12:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 28a8b742-8539-388f-8f95-ddf9986462a2 | -9.45959 | -57.84723 | 2025-06-19 05:12:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 11baa630-e03a-3082-9b0c-98a9fae68af5 | -12.23245 | -63.60436 | 2025-06-19 05:12:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0a75ce00-f8ad-3f67-b824-2e2f6e257e4e | -9.80022 | -47.17924 | 2025-06-19 05:12:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 07745b80-6a95-3564-93d4-023fe4747d05 | -10.15484 | -48.98551 | 2025-06-19 05:12:00 | NOAA-21 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| bf82979d-d3f1-3677-b081-9c98d664b8cd | -10.86182 | -53.76135 | 2025-06-19 05:12:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fc481cdb-4fc9-3408-977d-291fce459d9f | -11.9427 | -58.76475 | 2025-06-19 05:12:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 01a6e0ce-dc5d-3bc3-8b0c-efd323ac27d5 | -10.50627 | -53.58329 | 2025-06-19 05:12:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 11.6 |
| d2de53f1-2fce-3048-9f9d-dc357d712205 | -9.39419 | -63.26466 | 2025-06-19 05:12:00 | NOAA-21 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c0bbb561-1e7f-37da-a46a-9d22cd6fda85 | -11.57326 | -47.43254 | 2025-06-19 05:12:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6784ef51-47ae-3dea-811f-3b4223dfaf6c | -12.22351 | -55.52346 | 2025-06-19 05:12:00 | NOAA-21 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1ad0030b-d063-3d42-862e-fdb9e46f429d | -11.95478 | -58.73078 | 2025-06-19 05:12:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| b540f070-09ae-30f9-ae87-3823440f73d6 | -11.95094 | -58.7553 | 2025-06-19 05:12:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7707c700-4757-3f64-a9c7-6fbc96db69b0 | -13.5205 | -56.57225 | 2025-06-19 05:12:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 73d372ee-cf19-3512-8ac5-beba0214d709 | -9.41767 | -48.41989 | 2025-06-19 05:12:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b1031411-9cab-3fd3-abcf-5bfcc54c0f4e | -12.50933 | -58.35902 | 2025-06-19 05:12:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 449574d0-d504-3fe6-91cf-33d6f312c100 | -12.02914 | -57.09014 | 2025-06-19 05:12:00 | NOAA-21 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a57d9808-f93c-3df8-b109-3064024e1cd2 | -11.88624 | -54.67576 | 2025-06-19 05:12:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 82077a12-0007-31d9-b194-dc352c22ce43 | -11.10347 | -60.84966 | 2025-06-19 05:12:00 | NOAA-21 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 79d61bc5-ddc0-3ac5-9efc-0116b93a64d8 | -14.06921 | -53.39463 | 2025-06-19 05:12:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| fe172e9a-9928-3b73-a6f0-9d3fcb80fade | -11.96245 | -58.75003 | 2025-06-19 05:12:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 09f31061-476a-3351-8aa3-c449bc069d64 | -12.58138 | -56.98284 | 2025-06-19 05:12:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0fb9437a-3df2-3ea4-a074-7c864b52eaf5 | -11.96193 | -58.72834 | 2025-06-19 05:12:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 351fc256-d390-34b2-a358-f3125cfe5ee6 | -14.22399 | -45.5188 | 2025-06-19 05:12:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 2c6f81c4-2135-38a1-8680-21eb2f5a996a | -13.29285 | -57.07456 | 2025-06-19 05:12:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5634e06b-c067-3c74-a2ea-3f3038391617 | -10.65654 | -49.45406 | 2025-06-19 05:12:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 19768df8-0b9e-3ecd-ad7f-11bcea08ca26 | -16.30176 | -58.26386 | 2025-06-19 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 8099d09c-9be3-3ee5-9786-7ef162536b16 | -18.65558 | -55.74929 | 2025-06-19 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 236eb164-b7c1-36c1-b214-f7ecd63cd821 | -18.65878 | -55.75492 | 2025-06-19 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.4 |
| b86aa51a-144d-3be7-86b8-de202cb2b1b2 | -18.3043 | -54.26112 | 2025-06-19 05:14:00 | NOAA-21 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 6472fd6d-22ac-3524-b5c0-e70a7148d6d0 | -15.29207 | -48.66219 | 2025-06-19 05:14:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 59079e0c-a1c4-38db-b8f6-a621b5d8febc | -16.30231 | -58.26014 | 2025-06-19 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 12.6 |
| 5216befc-06ce-360b-aa23-2f943cb47ad3 | -17.9389 | -52.6987 | 2025-06-19 05:14:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 357b86ee-13bc-3c90-96d3-0f684fb1e1d7 | -13.72456 | -58.68165 | 2025-06-19 05:14:00 | NOAA-21 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c8b7183d-00bc-3b60-b899-1583c0e76d53 | -14.82917 | -59.81864 | 2025-06-19 05:14:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c8ebfa49-091e-3814-ad48-d8196dcfac57 | -18.66332 | -55.75042 | 2025-06-19 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 49ecd830-cd30-3bb5-be09-f5426762179f | -16.30961 | -58.2575 | 2025-06-19 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.8 |
| 6ccc5731-c3df-3652-bce8-604e689308ef | -16.64874 | -49.36603 | 2025-06-19 05:14:00 | NOAA-21 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| ebb8543c-bf17-3223-90d1-a2524a97c450 | -18.99701 | -52.08139 | 2025-06-19 05:14:00 | NOAA-21 | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 63bbb1fe-1974-3225-9540-818c8a5e3a25 | -17.57285 | -47.50112 | 2025-06-19 05:14:00 | NOAA-21 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 357e66b5-ede0-3d80-ad09-92bb0a7779dd | -14.46395 | -58.06394 | 2025-06-19 05:14:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8c23ec32-920b-358d-abd0-ea64c976461c | -16.65067 | -49.3657 | 2025-06-19 05:14:00 | NOAA-21 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 02a2c6ed-0615-3232-9152-15a48cc4db96 | -14.31043 | -59.89304 | 2025-06-19 05:14:00 | NOAA-21 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6a9f5370-5e64-3a79-bc68-fdf4ef1c2977 | -19.54583 | -49.66698 | 2025-06-19 05:14:00 | NOAA-21 | CAMPINA VERDE | MINAS GERAIS | Brasil | 3111101 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 4ff1dc25-a1c4-39ee-88c9-117e882738ad | -15.67261 | -59.6274 | 2025-06-19 05:14:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ae42dbcb-7a36-3643-a20b-794367d6d018 | -18.99146 | -52.08633 | 2025-06-19 05:14:00 | NOAA-21 | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 770e9ab9-fa6b-3714-aca2-09c39b230c81 | -17.75611 | -52.42908 | 2025-06-19 05:14:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0d8b11a5-b7e1-37a8-b271-6b1457e1689f | -19.12629 | -52.69915 | 2025-06-19 05:14:00 | NOAA-21 | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 118ee852-99d5-3ea0-87a6-90913bf508f7 | -16.31353 | -58.25432 | 2025-06-19 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| f95bbe52-71c3-38a9-a784-2b0fe33ec67d | -19.71448 | -54.62019 | 2025-06-19 05:14:00 | NOAA-21 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 38d5c95e-2b0d-38ee-b2b4-2cfcdd608ea5 | -19.54543 | -49.67115 | 2025-06-19 05:14:00 | NOAA-21 | CAMPINA VERDE | MINAS GERAIS | Brasil | 3111101 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| b8b264a7-5309-3349-850f-1634d2746258 | -19.17493 | -57.542 | 2025-06-19 05:14:00 | NOAA-21 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 6a11fa63-98b8-30bc-8b0d-049c03dbcc80 | -15.6693 | -59.62684 | 2025-06-19 05:14:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| efd2d9bd-cbee-39c1-b44a-67a05c64daae | -16.30624 | -58.25694 | 2025-06-19 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.8 |
| 4eff0342-d6b9-3c36-9e2c-a3c0de2bbd21 | -16.30513 | -58.2644 | 2025-06-19 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 63518706-3226-3123-ad61-c83ed5101687 | -20.37642 | -55.03944 | 2025-06-19 05:14:00 | NOAA-21 | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 78228d14-d1b2-329d-a054-d30b8259fa86 | -17.76025 | -52.43482 | 2025-06-19 05:14:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| be8d027a-a282-3642-a517-d4bf6e059e8f | -16.30287 | -58.2564 | 2025-06-19 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 12.6 |
| f47d362e-4124-3bd0-ab24-c789e1f206be | -14.311 | -59.88947 | 2025-06-19 05:14:00 | NOAA-21 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |


[Clique aqui para ver as próximas entradas](README23.md)
