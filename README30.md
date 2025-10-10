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

## Dados Diários - Página 30

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8d3227fb-2646-337d-9c28-40ca4e92c37d | -15.32871 | -43.18933 | 2025-10-10 04:02:00 | NOAA-20 | CATUTI | MINAS GERAIS | Brasil | 3115474 | 31 | 33 | nan | nan | nan | Caatinga | 2.8 |
| a6de945e-88e9-3301-9536-eb7bf2bd6277 | -15.08823 | -46.62205 | 2025-10-10 04:02:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e3b63239-e507-3193-9a23-64cbc1e2648a | -13.32019 | -47.73864 | 2025-10-10 04:02:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0eb0b39f-7e5a-3bfc-9320-e74b53ca819a | -12.62944 | -45.06691 | 2025-10-10 04:02:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 7fe2c386-38b0-30aa-bc63-502182701ce6 | -12.63477 | -45.05835 | 2025-10-10 04:02:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 28.4 |
| 9fdf911f-475d-3b74-b0f2-c89c7201e8c4 | -14.94079 | -46.76757 | 2025-10-10 04:02:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 2507d162-7137-3e89-b4d3-6883677b3761 | -15.55386 | -44.32851 | 2025-10-10 04:02:00 | NOAA-20 | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Caatinga | 2.3 |
| bf27fc02-bb4e-3d02-b12f-4212c1aefacd | -15.9144 | -43.29297 | 2025-10-10 04:02:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9663ed23-0bda-3c1d-a74a-88e84da27465 | -11.77867 | -45.15452 | 2025-10-10 04:02:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 27c07e4f-93e1-3add-aafc-ff0a88d5d85c | -11.96861 | -45.20141 | 2025-10-10 04:02:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2340f40f-0790-3439-ac54-ee6a8d9153dd | -12.40348 | -46.70547 | 2025-10-10 04:02:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a9624a52-ebd2-3f93-a651-b4f029487176 | -13.26278 | -48.02897 | 2025-10-10 04:02:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7eb02552-730f-3e57-903c-0d66c8489c48 | -16.32547 | -47.05327 | 2025-10-10 04:02:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d84ebd88-6ec6-35c8-af68-7096f7bc1242 | -14.43032 | -48.00727 | 2025-10-10 04:02:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 054d89d0-531e-327f-b084-ccdb0131f656 | -14.26962 | -45.89449 | 2025-10-10 04:02:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 66ad3b45-6135-34f6-b200-5bcdaf80d7a6 | -12.22734 | -43.79074 | 2025-10-10 04:02:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 37074d05-1707-3223-a44a-28fbdcf8ddd3 | -14.88253 | -48.23405 | 2025-10-10 04:02:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 22.6 |
| d23478aa-2278-30b5-acf7-427fafc93a5a | -10.8909 | -43.82197 | 2025-10-10 04:02:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 80e72c2b-5713-3381-9979-08ac62197d61 | -15.91501 | -43.28923 | 2025-10-10 04:02:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 05c88af6-ca18-3399-acc5-b26c18cc38e8 | -17.39132 | -46.87054 | 2025-10-10 04:02:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 76eb6496-5252-3130-8396-fbbadb271f38 | -15.30701 | -43.72151 | 2025-10-10 04:02:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 9ae9eaf5-c972-3a8f-89d7-ca4e2cc0d672 | -14.92934 | -46.78525 | 2025-10-10 04:02:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a6ceae99-1bfe-3c42-b4fb-c5c7c22c5848 | -13.30218 | -47.1297 | 2025-10-10 04:02:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 4130316c-6bd1-362c-b374-db021052d864 | -13.43395 | -47.58234 | 2025-10-10 04:02:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3bfc7e45-9bae-384a-9de1-72ce7e79a3c1 | -16.27542 | -47.16916 | 2025-10-10 04:02:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 02d7fe30-892a-3059-823f-e4f55489fb00 | -14.03526 | -42.17784 | 2025-10-10 04:02:00 | NOAA-20 | LAGOA REAL | BAHIA | Brasil | 2918753 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 8b718a49-4bca-3dab-9336-c780c524e6ae | -14.88515 | -48.24421 | 2025-10-10 04:02:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 7e95fc6f-552d-3506-a2d7-5d75d67dc0a3 | -17.64569 | -44.43438 | 2025-10-10 04:02:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| afea9594-8b57-3f65-beb7-7e88da7d3171 | -14.85976 | -48.47582 | 2025-10-10 04:02:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e5864826-aa48-3f4c-aeac-09ad2375cd25 | -14.37443 | -46.0075 | 2025-10-10 04:02:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 67c3a520-5609-3000-835a-53009fd35c3d | -14.72518 | -47.44352 | 2025-10-10 04:02:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ab4ca47f-78ab-3d51-885d-e174401fdb38 | -12.0255 | -43.63144 | 2025-10-10 04:02:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e675521e-e05a-3985-bd10-98643128e726 | -12.40415 | -46.70165 | 2025-10-10 04:02:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2858650c-5636-32d8-b50c-20072c7a30c7 | -11.31707 | -47.5208 | 2025-10-10 04:02:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| cc6cae76-f071-31f2-acdd-9fc982b1e3a4 | -15.09562 | -46.58101 | 2025-10-10 04:02:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cd3a0afd-b6d3-3051-b0a2-9508222c0045 | -14.44447 | -47.97921 | 2025-10-10 04:02:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 45ae7f07-ef4c-35ae-84ff-f261c2894bae | -11.77472 | -45.0417 | 2025-10-10 04:02:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b6a81a26-f213-334e-93d0-30addf6f98fd | -17.94505 | -45.02361 | 2025-10-10 04:02:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 9dd38cb0-946b-303b-a291-206b0805255a | -16.18324 | -43.66547 | 2025-10-10 04:02:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a4367bf8-b02d-378e-87b1-4e0d8e961221 | -11.63617 | -47.53309 | 2025-10-10 04:02:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| efed98ad-43b3-3dba-b7ea-e2021ca1403a | -16.12837 | -48.43769 | 2025-10-10 04:02:00 | NOAA-20 | ALEXÂNIA | GOIÁS | Brasil | 5200308 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 56297c2f-ffca-372c-b5bc-52a04ed15866 | -14.39065 | -46.00528 | 2025-10-10 04:02:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 40ea9806-df08-3600-9e2b-f62d56eebe93 | -13.84433 | -45.83716 | 2025-10-10 04:02:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a1bdd406-6aa5-3792-96cf-89160b3b6d88 | -15.57452 | -44.42634 | 2025-10-10 04:02:00 | NOAA-20 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 736de5a5-507a-3e5e-ad09-adf6df38aaab | -17.99739 | -44.97033 | 2025-10-10 04:02:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c056fb3e-8614-3a02-af5d-7a62ac28f41b | -12.63717 | -45.04455 | 2025-10-10 04:02:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 30467cdb-b39a-3fe8-8038-000c8a816155 | -12.62731 | -45.05706 | 2025-10-10 04:02:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 63f287c7-247f-3150-9016-f8a37d8d5984 | -14.38979 | -46.01026 | 2025-10-10 04:02:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b3ba92d9-fa7e-354f-bd9c-d9c8b7539f1a | -13.24739 | -46.47464 | 2025-10-10 04:02:00 | NOAA-20 | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e3b702a3-ae48-3e55-9f65-134f8d14474c | -15.46172 | -48.53304 | 2025-10-10 04:02:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 787cd7df-6839-3b7e-8601-2c0e3d9814cb | -16.08782 | -44.09212 | 2025-10-10 04:02:00 | NOAA-20 | PATIS | MINAS GERAIS | Brasil | 3147956 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e4c78470-9c1a-3c13-87ea-51dc621fe21f | -13.28289 | -48.01067 | 2025-10-10 04:02:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 11176296-bc30-3b6c-bc51-23c599939b03 | -17.21209 | -47.65767 | 2025-10-10 04:02:00 | NOAA-20 | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 6c86c032-6eb3-3dca-88a3-a80bbc25f85c | -10.62467 | -45.2399 | 2025-10-10 04:02:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0b2b0058-7433-382f-9140-e4bbc44444d0 | -11.44888 | -44.9477 | 2025-10-10 04:02:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 10d51c0c-a0d4-3597-93a7-960ac08e3c8f | -15.38054 | -47.29409 | 2025-10-10 04:02:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 459d982b-7110-3ec3-a788-9ca3f5ba5aeb | -13.06932 | -43.09479 | 2025-10-10 04:02:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 6bc8a053-3170-37b7-9179-a7da1d23aa97 | -13.02478 | -47.89083 | 2025-10-10 04:02:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| e54e4679-51cd-3fd1-93c4-8b8d7dfad6d8 | -14.73059 | -48.3643 | 2025-10-10 04:02:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 9ac93f0e-b53d-3bfa-9127-4f5f6b939d38 | -17.4797 | -46.963 | 2025-10-10 04:02:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4593827a-c230-3cc5-9fb6-3799b6c3361b | -14.92598 | -46.78107 | 2025-10-10 04:02:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a75b2691-320f-3d00-826f-18514618dcf6 | -12.92581 | -45.05505 | 2025-10-10 04:02:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 42532d4c-ecfe-3a4d-b3fb-0411561bd8a7 | -13.06106 | -43.8387 | 2025-10-10 04:02:00 | NOAA-20 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 97037738-2951-35a4-9780-32290354f012 | -16.67898 | -47.59404 | 2025-10-10 04:02:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7e1be7fe-a91d-3292-a37a-d41598779ae8 | -13.26898 | -48.02008 | 2025-10-10 04:02:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a412361e-2be2-3f3c-8a25-f2ea9f45ce1b | -13.31884 | -48.47299 | 2025-10-10 04:02:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 98fdbb23-56e3-3659-bf65-906dc2e7e0a7 | -13.29308 | -48.48524 | 2025-10-10 04:02:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7a45a7b0-e69e-326f-bff2-7d5a004f80a2 | -14.88757 | -48.23142 | 2025-10-10 04:02:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 22.6 |
| ed063e4a-3c54-3e34-baae-6900f7b12e57 | -13.88035 | -44.25101 | 2025-10-10 04:02:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7ba2bff9-74ec-3809-b7ec-85b1423e62ea | -11.77019 | -45.04541 | 2025-10-10 04:02:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6f8b6356-5f30-3240-be62-8fea00c1416e | -13.27336 | -48.02123 | 2025-10-10 04:02:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| f8c965b9-a246-30d4-8810-79bb78059de4 | -11.21819 | -40.46869 | 2025-10-10 04:02:00 | NOAA-20 | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| d9868200-cbb7-3ca7-ae99-99f0194e50c6 | -17.381 | -46.68439 | 2025-10-10 04:02:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6361bc5a-1b13-3dfd-b9c8-00f96ef92932 | -18.04541 | -44.98356 | 2025-10-10 04:02:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3f98265b-88e1-3ab3-89e4-53a553a875ea | -16.12711 | -48.43865 | 2025-10-10 04:02:00 | NOAA-20 | ALEXÂNIA | GOIÁS | Brasil | 5200308 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 10dab2e5-9ec0-3690-a809-b75a7a7a0d47 | -15.24155 | -46.37542 | 2025-10-10 04:02:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fe53318e-b182-30d6-a48e-c22b53460152 | -17.64916 | -47.25203 | 2025-10-10 04:02:00 | NOAA-20 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 175e43ac-fe89-3720-9875-c6243c6681d3 | -10.64475 | -44.41752 | 2025-10-10 04:02:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 71b806e0-745a-3bbd-b093-5f1b46b33262 | -13.24674 | -46.47826 | 2025-10-10 04:02:00 | NOAA-20 | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b1d5236d-e5a1-322f-9ada-2f205ea633be | -13.01345 | -41.42615 | 2025-10-10 04:02:00 | NOAA-20 | MUCUGÊ | BAHIA | Brasil | 2921906 | 29 | 33 | nan | nan | nan | Caatinga | 16.4 |
| 2000b976-90ad-34d1-84c5-2e908d444dc8 | -14.42675 | -48.00221 | 2025-10-10 04:02:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ba501f3a-1f73-3394-bc35-4a4ce4829a99 | -15.09382 | -46.59104 | 2025-10-10 04:02:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0e6eb136-4d1e-3102-84b2-46df2e02791f | -13.34927 | -47.75183 | 2025-10-10 04:02:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 13d618b1-ad20-3f72-908f-9b13210d603a | -17.93364 | -45.02242 | 2025-10-10 04:02:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 42595f40-7a8d-30c4-aff9-881ee5aec64a | -13.05065 | -46.80604 | 2025-10-10 04:02:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 01406f9e-cb1a-3be1-b799-4f38a4769bb0 | -13.31509 | -47.74186 | 2025-10-10 04:02:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| d086f7ec-9885-39b2-8476-c52e9bf77cd9 | -12.85431 | -43.81644 | 2025-10-10 04:02:00 | NOAA-20 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 29e7591c-57ac-332d-bc0c-09f4e45da0cd | -15.52621 | -39.90491 | 2025-10-10 04:02:00 | NOAA-20 | POTIRAGUÁ | BAHIA | Brasil | 2925402 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 81fc809b-ae7e-3157-bde8-2acffda1b678 | -13.23494 | -47.61284 | 2025-10-10 04:02:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 00df68e6-4690-3098-a2ac-6bb105441e2d | -15.32142 | -43.86507 | 2025-10-10 04:02:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 69cda782-8a2a-3411-a200-c3598d83754f | -11.96913 | -45.22104 | 2025-10-10 04:02:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b052f074-0c28-35dd-9419-2af88b09af00 | -15.46087 | -48.53765 | 2025-10-10 04:02:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6b0184cb-541d-3b4b-9215-003d98807991 | -15.51684 | -47.96749 | 2025-10-10 04:02:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5d9f68a6-abcc-3c4d-b918-f40f8d094491 | -15.35711 | -47.44362 | 2025-10-10 04:02:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| faf30c1c-e55f-3b8b-ae3b-268b05757475 | -12.61533 | -45.05962 | 2025-10-10 04:02:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 24909644-5a78-3778-960a-6ef1abebc1e0 | -14.27127 | -45.88505 | 2025-10-10 04:02:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 295441bf-3096-307f-bc44-97e38b1dc8d2 | -14.94482 | -46.76806 | 2025-10-10 04:02:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 708c008d-768a-3a1d-8e95-0a28c48506c0 | -11.68423 | -47.52001 | 2025-10-10 04:02:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| ebdaa49a-c0fa-349d-b2f0-917ed43f9932 | -13.38436 | -42.71302 | 2025-10-10 04:02:00 | NOAA-20 | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 20d4a040-c5a4-37fc-8d86-c01b4f74eba4 | -14.92999 | -46.78168 | 2025-10-10 04:02:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |


[Clique aqui para ver as próximas entradas](README31.md)
