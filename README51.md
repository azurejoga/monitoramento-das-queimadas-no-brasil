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

## Dados Diários - Página 51

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f3929c21-3c45-3c4d-a06c-bf864a63f056 | -15.23654 | -48.74717 | 2025-10-01 04:21:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| bf16dc7c-bd9b-3ace-abb7-9bc02758f405 | -12.95325 | -48.43372 | 2025-10-01 04:21:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 575e4a22-79d8-3b6f-b0bd-00afa9e1cdfd | -15.23929 | -48.75168 | 2025-10-01 04:21:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| d9729981-9164-3e9a-aebb-b6bc9ffbd43a | -15.9431 | -46.23732 | 2025-10-01 04:21:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 886f3033-07e8-3ba1-8f0f-8f2b5e329a69 | -13.56112 | -48.06688 | 2025-10-01 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 05ebdd64-b334-39f4-90a1-7bfdb95c02a7 | -11.20044 | -47.19963 | 2025-10-01 04:21:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 26855c94-9a53-3708-8bef-a4bd0f4ffa19 | -10.64185 | -48.53221 | 2025-10-01 04:21:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| c164e7ec-5ef4-3dcb-871d-3488ed70eef8 | -15.55367 | -48.18665 | 2025-10-01 04:21:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 3.8 |
| cc134838-719e-3429-9a83-dc013ada49f8 | -13.67434 | -48.06237 | 2025-10-01 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 76e8a518-a93c-3485-aefa-93c870828e70 | -11.46306 | -44.96934 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| a52f0ae8-2217-353e-96ba-5d7107fdd64a | -14.91171 | -51.675 | 2025-10-01 04:21:00 | NOAA-21 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 23.7 |
| 4a317795-74bc-33cc-9148-bfcb70df158f | -10.91516 | -44.32487 | 2025-10-01 04:21:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e5918f56-54e7-368b-a8db-a91b5e8eb4e6 | -11.94737 | -47.06841 | 2025-10-01 04:21:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9e28fa76-8dd9-353c-a560-24a49d5b724f | -13.07152 | -47.08636 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2a827806-9ec1-3978-84c3-a4fc3477b9f7 | -14.70884 | -48.27467 | 2025-10-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9c47511e-a6ad-3ed1-8e07-621965995aac | -13.76208 | -47.93654 | 2025-10-01 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ed2662c1-71bb-30c2-b14c-6fca4a704ff2 | -12.83499 | -47.01046 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cf985234-5530-332c-a238-63f3e98699dc | -12.1767 | -51.41357 | 2025-10-01 04:21:00 | NOAA-21 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| eb108750-bacb-3109-b0a5-8493ecfb1b41 | -13.07987 | -47.07674 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ad6c248d-a4ed-33e5-9d8c-c78d5ba682a0 | -13.53383 | -44.84383 | 2025-10-01 04:21:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b957f58a-e462-3aba-8d10-2afeac7dd918 | -11.47229 | -45.10897 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4c268ccd-0007-3204-acf1-9ec9738cf9e8 | -16.37621 | -47.06517 | 2025-10-01 04:21:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 5.9 |
| d9325674-1fb4-3c9b-ae08-723778db7a62 | -13.22573 | -47.33562 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7208a20a-3dbb-3cb1-805f-28c79e02f6c4 | -13.36574 | -47.28908 | 2025-10-01 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2b3b13f4-1cba-36f9-892f-51a653c7d7e7 | -14.02559 | -46.32258 | 2025-10-01 04:21:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9e999264-4d2e-3bd6-bb2d-b4a514f5c569 | -12.87279 | -46.94372 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 627837d3-b1cd-3d79-94cd-03e5a847deb9 | -14.52818 | -53.12375 | 2025-10-01 04:21:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| e242dfce-6b92-314b-a8cd-39dd70ceffda | -14.50346 | -48.41681 | 2025-10-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 25e003c9-b331-3d54-8aad-62063341d974 | -15.48467 | -45.90101 | 2025-10-01 04:21:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4782afd5-5ab7-30a7-8c4e-55cdb342e208 | -14.85418 | -48.3372 | 2025-10-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 15407ad5-0827-3a99-bb9f-bd0df1e36cd6 | -11.76847 | -46.84546 | 2025-10-01 04:21:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e53468cf-b873-3cc1-bbda-db4dea521b55 | -11.81866 | -44.97801 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 3043b6c8-64ab-31bb-ac7c-ae36af01bc94 | -10.06929 | -50.25975 | 2025-10-01 04:21:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 712065c0-5043-39a8-8bf3-32fb5dc1d869 | -13.76965 | -47.97507 | 2025-10-01 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 115ce5e4-b455-3536-9550-118e553dc58b | -15.33775 | -56.63344 | 2025-10-01 04:21:00 | NOAA-21 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 34eac0b2-5c0f-3d45-8644-50e058ab3d60 | -10.91028 | -46.56987 | 2025-10-01 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| b1c48701-fc0d-3106-9b1e-710bd71be11c | -11.46615 | -45.08261 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| cdf91b01-9588-3052-9f44-e3c29f9f9743 | -16.19385 | -49.99039 | 2025-10-01 04:21:00 | NOAA-21 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 9604ae9d-e603-3d57-b7b6-7e975ceaeb86 | -12.85043 | -47.02037 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| dcc7ddb1-67b4-31f9-a465-e7bf904ff727 | -14.14992 | -49.20272 | 2025-10-01 04:21:00 | NOAA-21 | NOVA IGUAÇU DE GOIÁS | GOIÁS | Brasil | 5214879 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d31e5cb4-c847-319e-a1ad-9aaf3224e801 | -11.84479 | -45.00766 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8acf3f10-1209-35fa-9747-c8a0c7641971 | -10.3448 | -48.21792 | 2025-10-01 04:21:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ac959d13-fa30-3e3e-8b12-b3045ac1a132 | -14.05628 | -45.03018 | 2025-10-01 04:21:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 779aa87d-340a-3a8d-8099-21080114abe5 | -16.02311 | -50.90966 | 2025-10-01 04:21:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a22313e1-f759-3066-b61b-75964429d524 | -13.76597 | -51.21544 | 2025-10-01 04:21:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 09329c8f-8663-3a23-9cd8-489ee65a8102 | -16.01644 | -50.90387 | 2025-10-01 04:21:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| a246564b-397d-3559-ae81-54bc4639c96c | -12.24138 | -47.81928 | 2025-10-01 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| c52f779c-f28a-37f7-a1c6-819f5cfa8f4a | -13.78559 | -48.00491 | 2025-10-01 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f87b6fea-939c-3794-90f1-a356dabb2dc4 | -12.79556 | -46.91652 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9f2793a5-0d71-3266-a19d-6b698993e127 | -11.81315 | -44.99176 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c148d1b5-3085-3ed5-bf09-d2f3cd670cfd | -11.6753 | -44.2833 | 2025-10-01 04:21:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f540f4c0-2c9c-331a-bcce-f28bfb93e7d9 | -13.70467 | -48.62977 | 2025-10-01 04:21:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 4e3b5ffa-d018-339d-b9fc-a2f768bbf002 | -13.76809 | -51.22641 | 2025-10-01 04:21:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6ac85410-ca43-363b-ad11-2c5e4a2b9b5b | -14.99942 | -46.94834 | 2025-10-01 04:21:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0091428f-8c2b-378a-9b10-18d01d2a3020 | -14.89444 | -48.36681 | 2025-10-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 83bb1ba1-9c0c-3ad2-a641-46a1194dc004 | -14.7171 | -48.13873 | 2025-10-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8a352fe1-5892-3283-ae4a-799ee3739e9a | -14.95092 | -49.94559 | 2025-10-01 04:21:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| eabd94a3-2f51-3c4a-8fdd-8d90de0f32a3 | -13.76328 | -47.92915 | 2025-10-01 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0302e1be-608f-3a0a-adb6-bc652218a012 | -11.47284 | -45.10543 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7ba5980d-4d49-3199-9939-4071a069c18c | -10.82373 | -47.97616 | 2025-10-01 04:21:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 18f73242-854a-3e60-9dc4-32273c65f0a4 | -12.38393 | -44.7007 | 2025-10-01 04:21:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 52c32978-97e5-377e-b223-95ab6af074ad | -11.66515 | -44.28172 | 2025-10-01 04:21:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 406f388a-e92f-33f1-b078-9f1517493d55 | -15.47631 | -45.86628 | 2025-10-01 04:21:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 119b576f-3eb5-3eb1-acdf-bb109bf6c4fe | -10.75545 | -45.36919 | 2025-10-01 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0a5fd9a4-4952-3fc4-a9e2-3bb239809d5d | -13.26173 | -48.43819 | 2025-10-01 04:21:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8608cf68-062c-367b-a3ca-4795dbccaab9 | -15.23508 | -48.73486 | 2025-10-01 04:21:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 620d1d4a-76e5-32da-a1fa-943272509800 | -10.65021 | -48.52544 | 2025-10-01 04:21:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2b2f0d62-c83c-30e1-bc2e-329b734252fa | -11.84584 | -44.9786 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 57879f0f-7787-3816-b578-dbf600ef4bd8 | -14.90378 | -47.20985 | 2025-10-01 04:21:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e2e8dd0e-bb8b-35cc-8f48-87fbcf981ae4 | -11.94955 | -47.07611 | 2025-10-01 04:21:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 295a6a1f-39d7-3c42-a0fd-16eb796cb14e | -13.76628 | -47.97457 | 2025-10-01 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 8adece4a-d379-33d4-b008-3f5c8979b9e3 | -12.21668 | -47.80014 | 2025-10-01 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 62d6721d-4844-3943-a714-33a9d38a6a81 | -14.19114 | -46.11055 | 2025-10-01 04:21:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| c0145ff0-3af8-38db-ac62-ea2d261ca22c | -10.08743 | -50.20102 | 2025-10-01 04:21:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ca3c97f3-ebf4-3688-b4ad-a65e060c2bcd | -13.77428 | -48.01059 | 2025-10-01 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| a42bb3ca-2c02-38dc-a7fb-51b18751b003 | -14.6876 | -46.96201 | 2025-10-01 04:21:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ae71d76b-34c6-328b-a1be-9c0205c425d4 | -15.34042 | -47.8432 | 2025-10-01 04:21:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f385111a-efca-3ec8-8f14-25cd3f9f969f | -14.35366 | -47.13584 | 2025-10-01 04:21:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5a58d204-5df2-3e3f-9396-2446fd7f0f44 | -11.83191 | -44.9582 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d5e89002-885a-3d4d-b130-4c12d6aec4f5 | -12.22065 | -47.79713 | 2025-10-01 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7516e907-8f25-3415-91bc-3e9947b0379c | -11.63589 | -47.91137 | 2025-10-01 04:21:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6ddbdc57-cda0-3c60-be9c-2abbe5df37b5 | -13.21849 | -47.33816 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 4bd84283-6b44-3c79-a038-41e65e702e5c | -11.45973 | -44.9688 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 27e8e4c2-d022-3527-8921-2cbd11867a06 | -14.79922 | -48.32455 | 2025-10-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 63d32fae-23ac-320d-81f4-aff76bf8bbd8 | -16.41146 | -47.05642 | 2025-10-01 04:21:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bdd0683e-f673-3cc2-ac20-89c60e1b1ea3 | -15.30311 | -46.39729 | 2025-10-01 04:21:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8a33503f-dc0e-3ea2-8d99-51c9e25bbdbf | -15.40832 | -47.053 | 2025-10-01 04:21:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ef070d9f-df9f-31c9-8273-a59c46ac6005 | -11.66858 | -47.49031 | 2025-10-01 04:21:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a59bc1cb-7c3a-34bc-bec1-6af9e15c2568 | -15.41493 | -47.05408 | 2025-10-01 04:21:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b2fa0a20-6228-3724-9ebe-4d15dc024298 | -14.04227 | -47.99113 | 2025-10-01 04:21:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 04bd4021-7621-3697-ab85-09d9185958b4 | -12.83878 | -47.02942 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ab1e1f86-b7c2-30ac-b9a7-e09b0bf57d10 | -13.296 | -47.5772 | 2025-10-01 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a4027026-cd34-3925-aa72-daf237253d1b | -11.84498 | -48.05081 | 2025-10-01 04:21:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1c08cf29-6fd4-34ae-8740-66537890c244 | -11.39258 | -44.89653 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dd778f2b-3a8a-38e8-8959-eccb1d3adf8c | -15.33229 | -46.2741 | 2025-10-01 04:21:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 362a4785-9efb-31e1-9b93-8b26b3ac30f1 | -16.02889 | -50.88604 | 2025-10-01 04:21:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 99b51c4f-8fb2-3dc2-a29b-042d811af67a | -10.93807 | -46.50201 | 2025-10-01 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e2d62c65-8cd7-31df-b890-34da36dfb4e7 | -13.69926 | -48.64095 | 2025-10-01 04:21:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 919f0551-b0e7-3049-a099-b0321828778a | -15.47521 | -45.87354 | 2025-10-01 04:21:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ce7dee6c-94c3-3154-b143-e9c53c466888 | -14.2027 | -46.10153 | 2025-10-01 04:21:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README52.md)
