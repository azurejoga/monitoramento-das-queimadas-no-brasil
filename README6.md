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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b378fdb8-d59b-38c5-b4f9-191bf201ac7e | -22.57046 | -44.7492 | 2025-09-16 03:15:00 | NOAA-20 | QUELUZ | SÃO PAULO | Brasil | 3541901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| fa64a009-0162-3348-bd74-24782a9122c8 | -19.29904 | -41.90215 | 2025-09-16 03:15:00 | NOAA-20 | TARUMIRIM | MINAS GERAIS | Brasil | 3168408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 7a53ef3d-9aa2-3c0d-af31-9b304b5e34d9 | -17.8612 | -44.4487 | 2025-09-16 03:15:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c07cb846-716d-31cb-8bea-95d6d6a3234d | -22.71322 | -43.23788 | 2025-09-16 03:15:00 | NOAA-20 | DUQUE DE CAXIAS | RIO DE JANEIRO | Brasil | 3301702 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 9b963eba-3691-307a-add2-0a1cb39f7529 | -21.19911 | -44.3792 | 2025-09-16 03:15:00 | NOAA-20 | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 23.7 |
| 8fbfa00a-681d-3fb6-8f0d-092cb81d8d35 | -22.71209 | -43.24266 | 2025-09-16 03:15:00 | NOAA-20 | DUQUE DE CAXIAS | RIO DE JANEIRO | Brasil | 3301702 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| f6669f99-161c-31fd-87f6-13ee730f947b | -16.0192 | -59.2427 | 2025-09-16 03:20:00 | GOES-19 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 78.0 |
| f86b3930-e618-344d-a844-9091946d4e53 | -15.6268 | -47.3661 | 2025-09-16 03:20:00 | GOES-19 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 50.2 |
| 2192a6cb-6be6-3c77-b7a6-7339322f59c3 | -10.7115 | -46.488 | 2025-09-16 03:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 137.9 |
| 69dc5dc6-73a6-370f-b236-30e892067246 | -10.7306 | -46.4856 | 2025-09-16 03:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 111.6 |
| 0d1fb8ff-d1c1-3b7a-bb17-bc2de443724c | -21.2014 | -44.3584 | 2025-09-16 03:20:00 | GOES-19 | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 68.0 |
| b23bc46d-161f-3ad0-a7f1-8f2e99442ce1 | -10.7833 | -50.6772 | 2025-09-16 03:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 76.3 |
| 42354c3c-3794-33a6-8abe-639b680c46de | -10.7392 | -44.7515 | 2025-09-16 03:20:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 72.5 |
| 09dd1ada-e478-3cad-8c23-bba7aea6b3c2 | -10.7205 | -44.731 | 2025-09-16 03:20:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 71.4 |
| b769f650-4bb7-3065-bafa-39b234fe2853 | -10.8025 | -50.6539 | 2025-09-16 03:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 88.8 |
| 65010235-69e9-3891-84d5-9fecca90f4ea | -10.7112 | -46.5106 | 2025-09-16 03:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 117.7 |
| 074443af-e9ba-3212-87f9-859c6a101dff | -10.7201 | -44.7541 | 2025-09-16 03:20:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 164.7 |
| 909c5760-669b-33e1-9769-87a65732e2a4 | -10.8022 | -50.6752 | 2025-09-16 03:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 121.8 |
| 76778313-5e42-3f82-b15d-993a924ee1e3 | -11.1299 | -45.3426 | 2025-09-16 03:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 67.6 |
| 06e2d527-35dc-3a04-a10f-847f9b43079e | -10.7836 | -50.6559 | 2025-09-16 03:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 97.8 |
| 5cbab364-b7f6-3067-b6ad-f044c3e490fa | -10.7302 | -46.5082 | 2025-09-16 03:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 94.7 |
| 23b71916-70a2-38f3-9ee0-8c677b8ac30a | -10.7115 | -46.488 | 2025-09-16 03:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 108.5 |
| 27eb6499-cbc7-3f6d-9fe9-d5da3cf15228 | -10.7306 | -46.4856 | 2025-09-16 03:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 89.5 |
| c70a9107-a8d4-3a64-b3d2-9f2c2013ad24 | -10.7833 | -50.6772 | 2025-09-16 03:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 64.6 |
| 93a14e0b-0228-3713-b938-fb9334580ff2 | -10.7836 | -50.6559 | 2025-09-16 03:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 103.6 |
| 3d252a09-5a3f-342a-aac6-32d3f0234f5d | -10.7201 | -44.7541 | 2025-09-16 03:30:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 123.6 |
| a9b94b63-f566-3384-8887-28d4f5973b44 | -10.8025 | -50.6539 | 2025-09-16 03:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 102.3 |
| 9044332e-3fb4-3353-a5c4-3771b8c5fee5 | -10.7112 | -46.5106 | 2025-09-16 03:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 122.9 |
| 113cd742-749c-318b-828d-2c41e913ba09 | -10.7205 | -44.731 | 2025-09-16 03:30:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 66.8 |
| 7400176b-8265-3817-a0ab-c22240727a53 | -10.8022 | -50.6752 | 2025-09-16 03:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 88.5 |
| 61f11482-3891-33df-a392-a4d8c81a8186 | -21.2014 | -44.3584 | 2025-09-16 03:30:00 | GOES-19 | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 79.6 |
| 95342848-42d3-3eb6-9bdd-ddaea9bba29e | -10.7302 | -46.5082 | 2025-09-16 03:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 97.3 |
| 6962837e-0ea3-3a0f-a7e4-876168bdd4dc | -10.7201 | -44.7541 | 2025-09-16 03:40:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 92.4 |
| 37cd9696-162d-325a-9164-285cf9202f1a | -10.7306 | -46.4856 | 2025-09-16 03:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 93.8 |
| 44f7a4fa-ecfe-36e4-b321-0b4540714da9 | -12.749 | -47.9595 | 2025-09-16 03:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 72.7 |
| c9394eb2-4acb-38f9-a382-88dd0be8cce8 | -11.1299 | -45.3426 | 2025-09-16 03:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 66.1 |
| 6180fca3-2166-3e4a-8235-d186568edec5 | -10.8022 | -50.6752 | 2025-09-16 03:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 56.7 |
| 975aaa19-2790-3c40-bd56-11277ac5b6b4 | -10.7112 | -46.5106 | 2025-09-16 03:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 121.3 |
| 3d15e6a7-e494-3419-b692-79284c1ae302 | -10.7115 | -46.488 | 2025-09-16 03:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 110.0 |
| a3f30bbf-094f-3fdb-99b1-ddfa9bccae96 | -10.7833 | -50.6772 | 2025-09-16 03:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 50.3 |
| b9506795-218e-3667-9495-3c8bcafbbd97 | -12.7678 | -47.9791 | 2025-09-16 03:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 91.4 |
| 3314b352-5fbc-36a2-90ee-eab3690c0c03 | -9.1053 | -44.8412 | 2025-09-16 03:40:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 130.6 |
| e9da2509-76d2-3a6b-b455-1d4a43300799 | -9.105 | -44.8641 | 2025-09-16 03:40:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 103.9 |
| 1fc0fd33-1c62-3719-a6f2-f398410a3ba5 | -10.7302 | -46.5082 | 2025-09-16 03:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 102.9 |
| 97488e79-29ec-3f13-a5cf-dba2a4be6c8c | -12.7682 | -47.9568 | 2025-09-16 03:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 97.3 |
| 12ff4d7a-bcf8-38ef-8a1f-fa5c4bd6d4c3 | -18.5676 | -49.2579 | 2025-09-16 04:00:00 | GOES-19 | CENTRALINA | MINAS GERAIS | Brasil | 3115805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 65.8 |
| 696579b9-9550-381c-b826-e150738e2931 | -2.45166 | -49.3635 | 2025-09-16 04:00:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3a3e0028-1134-30f7-9115-ef79d219ef09 | -4.59815 | -43.31809 | 2025-09-16 04:00:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d57c29ad-9729-31ad-8b00-9dcd20a4ec26 | -3.83163 | -44.10067 | 2025-09-16 04:00:00 | NOAA-21 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d1eee974-3697-3f92-8ecb-d1a25ac3f239 | -3.80775 | -41.5633 | 2025-09-16 04:00:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 39167320-6478-3de7-b4cc-9f59bf1e1cd4 | -3.80657 | -41.57079 | 2025-09-16 04:00:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| e8889427-ea88-33b5-a4d8-f917d0233ace | -3.81698 | -41.54943 | 2025-09-16 04:00:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 56fbc188-3a10-3a5c-924b-9ac7ce70dbc6 | -3.83002 | -44.1107 | 2025-09-16 04:00:00 | NOAA-21 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2bfea268-1cb7-3c0c-8c49-a0a2496e1d93 | -3.8269 | -44.10506 | 2025-09-16 04:00:00 | NOAA-21 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 838de7cd-d778-305b-b93b-0e5725eac39a | -4.84858 | -43.3731 | 2025-09-16 04:00:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5876ac4c-3e40-3bfd-bb7d-27059b1f8a25 | -3.83635 | -44.09626 | 2025-09-16 04:00:00 | NOAA-21 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| f3edade1-f0fe-3456-ba37-2cf7d625336a | -4.60115 | -43.32307 | 2025-09-16 04:00:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| de115c5c-1bb4-339d-bbe1-d165da1513f3 | -3.81178 | -41.5601 | 2025-09-16 04:00:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 3b2c6280-68ec-38cb-8e4d-e7d4abe5e160 | -3.8261 | -44.11006 | 2025-09-16 04:00:00 | NOAA-21 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a4157229-2036-33de-9696-05065d457ebd | -3.73664 | -49.04266 | 2025-09-16 04:00:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| a451625c-50fe-3883-a905-0e228632c38c | -3.30953 | -42.16766 | 2025-09-16 04:00:00 | NOAA-21 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 3e76ed3f-f40e-3662-9fb2-66402b317fbb | -3.08352 | -48.81565 | 2025-09-16 04:00:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 541e5e32-6e2d-3762-96ef-7561ae90d7f4 | -3.40277 | -46.90499 | 2025-09-16 04:00:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| e4c78ede-9494-3b9d-8e14-ba3bd45fc1c8 | -3.83867 | -44.10691 | 2025-09-16 04:00:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8728ee79-3904-30b4-9fa4-5eede02c7443 | -5.21321 | -37.85381 | 2025-09-16 04:00:00 | NOAA-21 | LIMOEIRO DO NORTE | CEARÁ | Brasil | 2307601 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 641cce18-4f0c-3258-b6f3-3878b567e52f | -3.89876 | -40.92071 | 2025-09-16 04:00:00 | NOAA-21 | IBIAPINA | CEARÁ | Brasil | 2305308 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 90175466-53a2-3924-92fb-290de1868eb2 | -3.40274 | -46.9074 | 2025-09-16 04:00:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 918959f8-772d-3c67-86c9-f3db3f10cacd | -2.13551 | -48.01115 | 2025-09-16 04:00:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3e799de1-9d36-3182-8a6b-60cb2eb71f82 | -3.81403 | -41.56812 | 2025-09-16 04:00:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 1a666c8f-ba02-375a-a377-2b7dd2e3e85a | -3.81059 | -41.56758 | 2025-09-16 04:00:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 19030c0a-fcb1-36e8-b19f-0ff39ad86bc3 | -3.81687 | -41.5724 | 2025-09-16 04:00:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 0b4c2863-0a96-31b0-916e-5657f997e121 | -3.07867 | -48.81119 | 2025-09-16 04:00:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6902ce25-0761-37fa-93e0-deeb1585bd5d | -3.81354 | -41.54889 | 2025-09-16 04:00:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 16b41e50-d3be-3e9a-852f-46ff1f801952 | -4.78909 | -42.73819 | 2025-09-16 04:00:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 0b5b11de-b353-352d-a002-a5ea4a900cb6 | -4.06124 | -46.9357 | 2025-09-16 04:00:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 715ba52a-ccc8-35ed-a57c-a6387b258cde | -4.00852 | -43.2337 | 2025-09-16 04:00:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 346313ad-769d-3f11-a767-d3b945740fb5 | -3.82218 | -44.10942 | 2025-09-16 04:00:00 | NOAA-21 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 5472a873-e125-321f-a1dd-15875e25aec9 | -3.24486 | -39.5164 | 2025-09-16 04:00:00 | NOAA-21 | ITAPIPOCA | CEARÁ | Brasil | 2306405 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 85116abd-eb6d-3ccd-bb8c-fe6b1c5543d8 | -4.1637 | -46.79196 | 2025-09-16 04:00:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 767259fb-bdbf-394b-b285-842b773f8265 | -4.85328 | -41.61522 | 2025-09-16 04:00:00 | NOAA-21 | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| dd7e9bb2-4cc9-3275-811b-49ec08ef0df0 | -3.74152 | -49.04709 | 2025-09-16 04:00:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 405e8885-42ce-3339-8a54-b6de1ea04ec0 | -3.82298 | -44.10444 | 2025-09-16 04:00:00 | NOAA-21 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| fc4a270f-baea-3346-98db-36dde010dee1 | -3.42202 | -43.16702 | 2025-09-16 04:00:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dfb2378f-a8e2-3d83-8988-33a1a29dbd1b | -3.23911 | -43.22285 | 2025-09-16 04:00:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f7bd1599-b3fc-3d4f-ab72-8b49c385337d | -3.89291 | -42.51614 | 2025-09-16 04:00:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 5f8d2cde-7829-3b3e-acbf-3dfa86f70f92 | -4.81244 | -37.81265 | 2025-09-16 04:00:00 | NOAA-21 | JAGUARUANA | CEARÁ | Brasil | 2307007 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| a3259365-46bf-34e3-a9e3-cbed930129d3 | -5.09292 | -41.16129 | 2025-09-16 04:00:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 3d245455-6896-3a7f-bae7-548ec0a8a7b5 | -4.84743 | -43.37196 | 2025-09-16 04:00:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 148c7d47-7f17-3669-a053-36f7ab3cf2a6 | -4.78976 | -42.73407 | 2025-09-16 04:00:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 5487dc1b-5116-3ab6-ae72-1ddeb1ca5b4d | -3.94439 | -41.82884 | 2025-09-16 04:00:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 206e6649-2eb6-3360-8918-7094c744a38e | -3.81295 | -41.55263 | 2025-09-16 04:00:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 66428723-55f1-346d-9f84-adc9fdad3549 | -3.44164 | -39.21334 | 2025-09-16 04:00:00 | NOAA-21 | PARAIPABA | CEARÁ | Brasil | 2310258 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 1bf350f6-44b2-3258-a504-30f73212878e | -3.80716 | -41.56705 | 2025-09-16 04:00:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 31fcd7b6-8ca5-3635-9281-267df49757c6 | -4.91248 | -38.00415 | 2025-09-16 04:00:00 | NOAA-21 | RUSSAS | CEARÁ | Brasil | 2311801 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| fec77516-51e8-3152-9f6a-a871b9ce7dd6 | -3.83947 | -44.1019 | 2025-09-16 04:00:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 8d6f906b-d4f7-34c4-91f8-42e06dc97351 | -3.42114 | -43.14867 | 2025-09-16 04:00:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 7ab935c5-25be-3f37-b4a1-14463a02d7d2 | -3.99669 | -43.23634 | 2025-09-16 04:00:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 625a07c6-6528-39e0-9da0-3ec6ae5f2ac6 | -3.81569 | -41.57992 | 2025-09-16 04:00:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 30ad626a-da00-3c26-a1a1-8df7263ab5ff | -2.16174 | -46.4011 | 2025-09-16 04:00:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9a4ebdd2-98ce-3b34-b06d-4e4a9b1b3fd7 | -3.83083 | -44.10567 | 2025-09-16 04:00:00 | NOAA-21 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |


[Clique aqui para ver as próximas entradas](README7.md)
