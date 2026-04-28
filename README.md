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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2a2943fd-ae67-314b-b507-1d8fddb9a576 | -10.1604 | -46.5331 | 2026-04-28 00:10:00 | GOES-19 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 73.2 |
| 4aa8d782-6de8-391c-a04a-cfd7a158cd1f | -17.57314 | -47.82038 | 2026-04-28 00:13:00 | TERRA_M-M | CAMPO ALEGRE DE GOIÁS | GOIÁS | Brasil | 5204805 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 06f2b89c-d53a-33cf-ad12-b5d3c9ced058 | -13.40871 | -45.34067 | 2026-04-28 00:13:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 1bf091da-364f-3532-acf1-d64feb603bb3 | -13.40701 | -45.32943 | 2026-04-28 00:13:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 20.2 |
| 30f19752-d8d9-3ba9-bd75-943b45775978 | -17.09316 | -51.04935 | 2026-04-28 00:13:00 | TERRA_M-M | MONTIVIDIU | GOIÁS | Brasil | 5213756 | 52 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 29a5b312-fd49-3295-beab-5846c88e4f07 | -13.39726 | -45.33102 | 2026-04-28 00:13:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 5f72f9c0-36ed-3336-959d-975a81e999bc | -10.1538 | -46.54058 | 2026-04-28 00:16:00 | TERRA_M-M | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 46.8 |
| 670208d5-8cca-3160-8bb8-8228c8c5f05e | -10.40038 | -46.50114 | 2026-04-28 00:16:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 0b00211f-2717-39fb-bff1-a3f3160e708f | -10.15227 | -46.53017 | 2026-04-28 00:16:00 | TERRA_M-M | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 56.6 |
| 0e5ff596-1e3a-3687-ae9d-459fb4aaea03 | -10.15533 | -46.55095 | 2026-04-28 00:16:00 | TERRA_M-M | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| f106988c-a894-33dc-9056-1ee8e97996b2 | -8.15213 | -46.66326 | 2026-04-28 00:18:00 | TERRA_M-M | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| bdfdf8b6-af05-3800-b0e5-a543eccee07a | -8.16181 | -46.66188 | 2026-04-28 00:18:00 | TERRA_M-M | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 1d32817b-80f6-3496-a44f-8015880e65c9 | -8.15056 | -46.65247 | 2026-04-28 00:18:00 | TERRA_M-M | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 9cb773cc-6008-3d85-8bc2-a09ebd6fe604 | -10.1467 | -46.536301 | 2026-04-28 00:19:00 | METOP-C | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 99eba69a-faf6-33e6-a345-e9c9ca8bb89c | -6.2612 | -42.578201 | 2026-04-28 00:19:00 | METOP-C | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 311f3e1b-f2ba-3f49-b7d5-d0abcbbb3ec4 | -10.1448 | -46.527802 | 2026-04-28 00:19:00 | METOP-C | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4bdd078b-cba0-3dee-818c-4452364d4bcb | -10.3953 | -46.500198 | 2026-04-28 00:19:00 | METOP-C | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 28fd0972-5e59-39ad-b6fb-be58ef3ee739 | -8.1508 | -46.656799 | 2026-04-28 00:19:00 | METOP-C | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 04420017-f791-39a2-94c9-4cdc1de19508 | -6.2514 | -42.580502 | 2026-04-28 00:19:00 | METOP-C | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| b981fdb5-1f04-354c-8ae5-47ac651ba784 | -6.2498 | -42.573299 | 2026-04-28 00:19:00 | METOP-C | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| a64ec19f-3dbb-35fa-a608-1d2efe3af960 | -10.3971 | -46.508701 | 2026-04-28 00:19:00 | METOP-C | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 827b01ef-9943-3e6c-aff2-e97d1b8f82ce | -10.97505 | -38.12891 | 2026-04-28 03:15:00 | NOAA-20 | TOBIAS BARRETO | SERGIPE | Brasil | 2807402 | 28 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 84674c85-5f47-3a64-91a6-86567af43873 | -10.96955 | -38.1278 | 2026-04-28 03:15:00 | NOAA-20 | TOBIAS BARRETO | SERGIPE | Brasil | 2807402 | 28 | 33 | nan | nan | nan | Caatinga | 2.6 |
| ec0d852e-88ab-34a9-9080-b81fecf23262 | -18.70177 | -40.10749 | 2026-04-28 03:17:00 | NOAA-20 | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 755ad033-822d-3354-bb7a-524eeb78269e | -18.70257 | -40.10378 | 2026-04-28 03:17:00 | NOAA-20 | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 32f0477c-adf2-3610-922c-ffa7e2c48e4f | -17.22157 | -41.60581 | 2026-04-28 03:17:00 | NOAA-20 | CARAÍ | MINAS GERAIS | Brasil | 3113008 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| d5934109-f6d3-3e8d-a8eb-2922bf6fb332 | -17.22753 | -41.60774 | 2026-04-28 03:17:00 | NOAA-20 | CARAÍ | MINAS GERAIS | Brasil | 3113008 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 6726090e-1881-3e87-ad2e-33f33b2b9ed3 | -19.5897 | -40.05861 | 2026-04-28 03:17:00 | NOAA-20 | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| cd77de5f-d993-3a04-8cd0-7b59c5d63257 | -19.59498 | -40.05988 | 2026-04-28 03:17:00 | NOAA-20 | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 8c65f335-26b6-3f51-92ad-79edca4b0b45 | -17.72825 | -43.70378 | 2026-04-28 03:17:00 | NOAA-20 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 569afb1c-001f-3bb2-9eeb-463b80d43493 | -6.5631 | -51.1126 | 2026-04-28 03:50:00 | GOES-19 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 43.3 |
| 20f2eedf-2244-3c41-9896-6bbf744181d9 | -2.25798 | -47.8619 | 2026-04-28 04:02:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 595635ea-898d-36fa-a646-b48a2f0f8aa1 | -10.974 | -38.12929 | 2026-04-28 04:02:00 | NOAA-21 | TOBIAS BARRETO | SERGIPE | Brasil | 2807402 | 28 | 33 | nan | nan | nan | Caatinga | 9.4 |
| 9170a07d-e81b-3ef5-8bf0-0e22878ef0a0 | -8.48442 | -41.54309 | 2026-04-28 04:02:00 | NOAA-21 | LAGOA DO BARRO DO PIAUÍ | PIAUÍ | Brasil | 2205565 | 22 | 33 | nan | nan | nan | Caatinga | 20.7 |
| 04fc77c4-d905-3bc3-b0b1-5a62b2d956ac | -2.26377 | -47.85952 | 2026-04-28 04:02:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 12b84717-1530-37d8-99ee-35c8dc13a664 | -6.25808 | -42.58122 | 2026-04-28 04:02:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 3b453cc1-bf1c-3f68-8ee6-64618be6c2d5 | -8.15222 | -46.65735 | 2026-04-28 04:02:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 08a2b530-51cf-3f41-82f3-c81a719ca381 | -8.88152 | -37.94736 | 2026-04-28 04:02:00 | NOAA-21 | INAJÁ | PERNAMBUCO | Brasil | 2607000 | 26 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 1fbd2899-5220-3699-b4bb-a11541507959 | -8.94453 | -45.66905 | 2026-04-28 04:02:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b440f495-0a80-3b5f-9127-d7ebd9f46a78 | -6.24744 | -42.57961 | 2026-04-28 04:02:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 8.3 |
| f3ef7e5f-1193-32a8-ac5f-654c1d502955 | -10.40437 | -39.17738 | 2026-04-28 04:02:00 | NOAA-21 | MONTE SANTO | BAHIA | Brasil | 2921500 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 495c46a6-55fe-35ed-a4af-c3eb01f351db | -5.71572 | -45.16429 | 2026-04-28 04:02:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ba73fc6b-2993-31ba-ba72-f65f26e7d994 | -2.26301 | -47.86024 | 2026-04-28 04:02:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 512a8b4b-6523-333a-9aa2-e792469930a3 | -8.15664 | -46.65805 | 2026-04-28 04:02:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 14b970b1-833d-3a73-8885-ee86bac25f95 | -8.48834 | -41.54005 | 2026-04-28 04:02:00 | NOAA-21 | LAGOA DO BARRO DO PIAUÍ | PIAUÍ | Brasil | 2205565 | 22 | 33 | nan | nan | nan | Caatinga | 13.5 |
| e5c16770-d1c8-3394-a3c0-f84084577d53 | -6.25389 | -42.58472 | 2026-04-28 04:02:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 62a82d99-a9af-3281-97d7-6b4fd6a49197 | -10.97754 | -38.12982 | 2026-04-28 04:02:00 | NOAA-21 | TOBIAS BARRETO | SERGIPE | Brasil | 2807402 | 28 | 33 | nan | nan | nan | Caatinga | 1.7 |
| f861ddc5-5a86-3122-bf5e-5362a64ea841 | -3.46236 | -52.05151 | 2026-04-28 04:02:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 2d27809b-5638-3fc7-9bb3-5e1f9cd594eb | -9.17569 | -37.81423 | 2026-04-28 04:02:00 | NOAA-21 | MATA GRANDE | ALAGOAS | Brasil | 2705002 | 27 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 3bb74052-ddb0-37ed-8542-4344dfba1a83 | -6.25453 | -42.5807 | 2026-04-28 04:02:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| d7f59f98-6af9-3f0f-ad4e-f416b7149e6b | -7.62194 | -45.94881 | 2026-04-28 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 00a1142c-dbea-3164-841f-c5ba4a9d0758 | -10.40774 | -39.17792 | 2026-04-28 04:02:00 | NOAA-21 | MONTE SANTO | BAHIA | Brasil | 2921500 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 47964a52-23e6-310d-acb4-892de32e7f0d | -6.25163 | -42.57614 | 2026-04-28 04:02:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 8909ff54-8ce0-3557-adce-e0f09c3a23ac | -2.25849 | -47.8587 | 2026-04-28 04:02:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 02e7e2a0-8d2d-35e7-95a7-c3d829a1b671 | -8.15298 | -46.65295 | 2026-04-28 04:02:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 23c129b1-582d-328d-9f1c-21df9c0dd6b7 | -7.61239 | -46.45638 | 2026-04-28 04:02:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6f6fc515-0dde-3da5-b6ce-0c0c5de23013 | -5.69662 | -45.17673 | 2026-04-28 04:02:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7c3ff2db-5f75-3106-9eb8-ef1e0bd09537 | -6.25098 | -42.58016 | 2026-04-28 04:02:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 8.3 |
| b582157e-8066-3b03-9e96-98b5cd4ad816 | -8.48499 | -41.53952 | 2026-04-28 04:02:00 | NOAA-21 | LAGOA DO BARRO DO PIAUÍ | PIAUÍ | Brasil | 2205565 | 22 | 33 | nan | nan | nan | Caatinga | 12.9 |
| 18596682-c63e-3b67-b388-e5457e6e08e2 | -5.71987 | -45.16501 | 2026-04-28 04:02:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 381a0152-d849-3138-8cd8-7bd9d3ee6193 | -6.24808 | -42.57559 | 2026-04-28 04:02:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 0f85f13c-ed8d-3b52-abb5-ef13234edca4 | -2.26326 | -47.86272 | 2026-04-28 04:02:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 16d51fa6-3fc1-38bc-9fea-a7492c97be8b | -8.1603 | -46.66315 | 2026-04-28 04:02:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 20e06e79-b55d-30b4-96c3-130e0eba87bb | -13.39841 | -45.33052 | 2026-04-28 04:04:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9aef5783-0700-3126-895b-377a66b1b505 | -14.51725 | -42.49798 | 2026-04-28 04:04:00 | NOAA-21 | LICÍNIO DE ALMEIDA | BAHIA | Brasil | 2919405 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 4f5125e9-8c27-32b8-bd0d-76b3e36ae643 | -15.79197 | -41.28071 | 2026-04-28 04:04:00 | NOAA-21 | PEDRA AZUL | MINAS GERAIS | Brasil | 3148707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| d5e25aad-f576-3223-b1e4-8dafaf245e45 | -14.79438 | -42.80791 | 2026-04-28 04:04:00 | NOAA-21 | URANDI | BAHIA | Brasil | 2932606 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| bd9fa066-5ca8-339b-9f7f-78f5d74e461e | -17.22669 | -41.60598 | 2026-04-28 04:04:00 | NOAA-21 | CARAÍ | MINAS GERAIS | Brasil | 3113008 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| 69082cf9-382a-3b2d-935c-6693a95f79bd | -17.67277 | -46.73925 | 2026-04-28 04:04:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fee8ab41-d4eb-34a3-8f66-ce21d053fdbb | -13.40961 | -45.33255 | 2026-04-28 04:04:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3fd4841d-0e62-3205-be9d-56253b8bc294 | -16.52769 | -43.51774 | 2026-04-28 04:04:00 | NOAA-21 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 036d0843-f948-312a-9baa-59904deee19b | -17.88009 | -42.65643 | 2026-04-28 04:04:00 | NOAA-21 | ARICANDUVA | MINAS GERAIS | Brasil | 3104452 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| b7202737-87d4-38d9-bd3f-128e8646676b | -17.7344 | -43.69937 | 2026-04-28 04:04:00 | NOAA-21 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 38d421e5-0dfe-3fe5-a4fb-29ea610580af | -16.28737 | -39.24565 | 2026-04-28 04:04:00 | NOAA-21 | SANTA CRUZ CABRÁLIA | BAHIA | Brasil | 2927705 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| a23d218d-c02b-3020-a9a0-6703c54237c1 | -13.40215 | -45.33119 | 2026-04-28 04:04:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 842c16fd-07a5-3883-829f-709e2ca6350f | -15.95954 | -47.76549 | 2026-04-28 04:04:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 8aad01c3-cd15-3ea0-a974-f9e29c5710b0 | -18.15957 | -42.6521 | 2026-04-28 04:04:00 | NOAA-21 | SÃO JOSÉ DO JACURI | MINAS GERAIS | Brasil | 3163508 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 03a7fe1a-d695-3477-b25e-a9acafaf6a0f | -15.95809 | -47.76481 | 2026-04-28 04:04:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 00fd6cd4-3235-30d3-8552-ac4a4587224b | -18.70432 | -40.10378 | 2026-04-28 04:04:00 | NOAA-21 | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 282adb38-bf91-3170-a5b4-fd50b83b4888 | -15.58259 | -40.93562 | 2026-04-28 04:04:00 | NOAA-21 | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.2 |
| d255bfee-44b6-3e3e-8fab-f311f56fefb1 | -13.40666 | -45.32729 | 2026-04-28 04:04:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 00bf211e-efa5-3641-9b33-a13a05dbdcfa | -11.44884 | -39.28679 | 2026-04-28 04:04:00 | NOAA-21 | CONCEIÇÃO DO COITÉ | BAHIA | Brasil | 2908408 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 08a5e668-61a7-3f20-928b-e4b4ed62ff72 | -15.01916 | -43.62977 | 2026-04-28 04:04:00 | NOAA-21 | MATIAS CARDOSO | MINAS GERAIS | Brasil | 3140852 | 31 | 33 | nan | nan | nan | Caatinga | 0.9 |
| bd78fc19-4a4a-3b1a-930b-e5ef7d443a4b | -17.62246 | -39.71329 | 2026-04-28 04:04:00 | NOAA-21 | CARAVELAS | BAHIA | Brasil | 2906907 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 43523834-7140-3e08-b508-eed70bb2351e | -16.47389 | -41.21939 | 2026-04-28 04:04:00 | NOAA-21 | JEQUITINHONHA | MINAS GERAIS | Brasil | 3135803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 3661fa1d-89e2-36fe-b21c-da9d96ea7d70 | -15.13371 | -41.07491 | 2026-04-28 04:04:00 | NOAA-21 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 156d05a1-9fe4-32c3-8122-cc486cef207e | -17.23002 | -41.60651 | 2026-04-28 04:04:00 | NOAA-21 | CARAÍ | MINAS GERAIS | Brasil | 3113008 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| b8c9eafa-9144-3e27-a364-c66c23226839 | -13.3992 | -45.32594 | 2026-04-28 04:04:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 63d6997c-84d2-3321-8658-7407dfa9de3b | -14.52058 | -42.49852 | 2026-04-28 04:04:00 | NOAA-21 | LICÍNIO DE ALMEIDA | BAHIA | Brasil | 2919405 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 516201bd-a3b3-3953-8fcc-f50e1f19b2db | -13.40588 | -45.33187 | 2026-04-28 04:04:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c53d7b5d-c209-38ed-87f8-66b795821c29 | -17.73213 | -42.64573 | 2026-04-28 04:04:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 3911a678-6d8d-3a29-80f2-504a53b25cfb | -15.42209 | -43.05275 | 2026-04-28 04:04:00 | NOAA-21 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 1.4 |
| bc9a8ecb-5f36-3302-b27f-cac5a68d1816 | -13.41039 | -45.32798 | 2026-04-28 04:04:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 51888517-dff9-3b74-8491-907722e1d551 | -19.06367 | -46.22786 | 2026-04-28 04:06:00 | NOAA-21 | RIO PARANAÍBA | MINAS GERAIS | Brasil | 3155504 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 05749179-66d7-3e10-9c49-2668b2b4f474 | -20.8118 | -44.30092 | 2026-04-28 04:06:00 | NOAA-21 | RESENDE COSTA | MINAS GERAIS | Brasil | 3154200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 0a6f89f8-2a5e-3fde-b4d9-5515d225e3bd | -19.06293 | -46.22948 | 2026-04-28 04:06:00 | NOAA-21 | RIO PARANAÍBA | MINAS GERAIS | Brasil | 3155504 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 9169cb66-9d44-37d3-bb95-3d02659eb276 | -21.70651 | -48.43082 | 2026-04-28 04:06:00 | NOAA-21 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 58e3e79c-0506-3299-a34c-bd4851353ac1 | -19.86421 | -43.87151 | 2026-04-28 04:06:00 | NOAA-21 | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 1b441241-97c8-325a-8b27-75e9b7b70dae | -21.13722 | -48.55532 | 2026-04-28 04:06:00 | NOAA-21 | TAIAÇU | SÃO PAULO | Brasil | 3553104 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 52f0fce5-bc71-3757-88d7-4e5b912b9cdc | -20.80935 | -44.30106 | 2026-04-28 04:06:00 | NOAA-21 | RESENDE COSTA | MINAS GERAIS | Brasil | 3154200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |


[Clique aqui para ver as próximas entradas](README2.md)
