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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 302043a3-9807-39b3-a227-2440c28951af | -3.3269 | -50.4504 | 2024-10-05 00:15:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 43.4 |
| f573ca5c-8067-367a-a8e1-23f6e2f1d496 | -3.5994 | -47.5359 | 2024-10-05 00:15:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 935c0acf-6e51-3e0b-95a9-70fdb0c183d8 | -3.5995 | -47.5142 | 2024-10-05 00:15:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 102.5 |
| 35104c9a-3b98-32fd-9ba6-5529c09d7768 | -3.618 | -47.5352 | 2024-10-05 00:15:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 107.1 |
| 2fa15fb5-2b00-326a-b296-36bebb462337 | -3.6181 | -47.5134 | 2024-10-05 00:15:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 170.6 |
| adbec174-cf03-37a5-8ad2-3cb52a4b3d1d | -4.0148 | -43.2408 | 2024-10-05 00:15:29 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 60.5 |
| f7b3f9f1-86ca-3d2d-8485-65c652a11050 | -4.0608 | -47.9511 | 2024-10-05 00:15:29 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 74.6 |
| da1c4777-24fa-3c8c-aa47-a32134950bcc | -4.0793 | -47.9719 | 2024-10-05 00:15:29 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 73.3 |
| 903a5a09-1414-37f4-a301-91f233ffb2e7 | -4.0794 | -47.9502 | 2024-10-05 00:15:29 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 263.3 |
| 36734c0a-3f19-3cf9-af94-9082d8d6a2a3 | -4.0795 | -47.9285 | 2024-10-05 00:15:29 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 68.4 |
| 9b9222d7-399b-3abd-8345-cca1389aaa20 | -4.0979 | -47.9494 | 2024-10-05 00:15:29 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 89.1 |
| ba93cd0e-f458-3670-a34c-ed5c86122d88 | -4.7851 | -50.8117 | 2024-10-05 00:15:33 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 4b01af6b-9cab-3990-ab79-519ebf4e2540 | -4.8036 | -50.8108 | 2024-10-05 00:15:33 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 55.2 |
| d60b96b1-33ce-3327-b448-f19ca86e2607 | -5.3911 | -46.4322 | 2024-10-05 00:15:36 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 71.5 |
| d06a2235-088b-3f20-bd75-78d45fcac70a | -5.8214 | -44.1426 | 2024-10-05 00:15:39 | GOES-16 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 134.7 |
| b882dcf8-e326-3a89-93d8-d69aa4348958 | -5.8216 | -44.1196 | 2024-10-05 00:15:39 | GOES-16 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 179.9 |
| 997b63ad-e85c-339e-bcf6-45377a6dc31a | -5.8403 | -44.1181 | 2024-10-05 00:15:39 | GOES-16 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 55.1 |
| e8635102-7236-3806-857c-d98b06974233 | -6.9514 | -59.0666 | 2024-10-05 00:15:46 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 80.8 |
| 8a204b88-b43e-3fa5-88a4-da80b5984792 | -7.0233 | -59.3918 | 2024-10-05 00:15:46 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 72.8 |
| e9cb5d72-1192-3770-baf8-e838abbe2d38 | -7.1346 | -59.3099 | 2024-10-05 00:15:47 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 89.0 |
| be98b34d-2558-354e-87dd-4f0f0916f242 | -7.1347 | -59.2906 | 2024-10-05 00:15:47 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 79.2 |
| eb159ab8-6b8a-3d18-b767-c913e6dfe939 | -7.7362 | -49.2297 | 2024-10-05 00:15:50 | GOES-16 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 214.9 |
| 2200acf4-a7b3-3cc6-a850-e74daa457b85 | -7.7364 | -49.2082 | 2024-10-05 00:15:50 | GOES-16 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 292.9 |
| a5fe1292-982d-35bf-9999-8aed6e9ddc65 | -7.7549 | -49.2282 | 2024-10-05 00:15:50 | GOES-16 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 197.7 |
| 73e9fe9a-4936-398b-9b05-657d8bb6e0ae | -7.7551 | -49.2067 | 2024-10-05 00:15:50 | GOES-16 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 257.4 |
| ff93461f-c764-376e-8622-98696f69d523 | -7.7736 | -49.2267 | 2024-10-05 00:15:50 | GOES-16 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 45.0 |
| f498a8df-da5a-3dff-9b37-992a365cf522 | -7.7738 | -49.2052 | 2024-10-05 00:15:50 | GOES-16 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 49.8 |
| e234c8cd-8db6-3e63-8281-4c5d6918934c | -8.2323 | -61.2205 | 2024-10-05 00:15:53 | GOES-16 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 95.0 |
| cfdb7e42-d446-3084-b520-099553e77875 | -8.7769 | -49.9763 | 2024-10-05 00:15:56 | GOES-16 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 66.7 |
| a01d4115-4f77-3abe-a493-a9bdf9039168 | -8.7772 | -49.955 | 2024-10-05 00:15:56 | GOES-16 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 97.9 |
| 373e6c85-cd1f-3836-9d64-50a1e6ebab64 | -8.7774 | -49.9336 | 2024-10-05 00:15:56 | GOES-16 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 46.7 |
| b3ebc331-7ef5-3712-a451-4e61560fdfbb | -8.7957 | -49.9747 | 2024-10-05 00:15:56 | GOES-16 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 100.1 |
| ed24704d-27ea-33e3-8f8b-3555feb6f73e | -8.7959 | -49.9533 | 2024-10-05 00:15:56 | GOES-16 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 97.5 |
| b59dce49-bcc8-33d6-a620-958849ecd7a9 | -8.9853 | -49.8083 | 2024-10-05 00:15:57 | GOES-16 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 43.1 |
| 2d6a230e-15cb-3aad-9fd8-495f265b4399 | -9.7745 | -36.395 | 2024-10-05 00:16:00 | GOES-16 | LIMOEIRO DE ANADIA | ALAGOAS | Brasil | 2704203 | 27 | 33 | nan | nan | nan | Mata Atlântica | 138.9 |
| f3fa7b9e-857c-31bf-a70e-1aa3da7a8620 | -9.775 | -36.368 | 2024-10-05 00:16:00 | GOES-16 | CAMPO ALEGRE | ALAGOAS | Brasil | 2701407 | 27 | 33 | nan | nan | nan | Mata Atlântica | 217.5 |
| 9eae563c-4fda-334a-969b-3e4f320508a2 | -9.7943 | -36.3647 | 2024-10-05 00:16:00 | GOES-16 | CAMPO ALEGRE | ALAGOAS | Brasil | 2701407 | 27 | 33 | nan | nan | nan | Mata Atlântica | 79.3 |
| 0ef4718c-5215-3c29-8f71-2d7792e4c24f | -9.5686 | -64.2171 | 2024-10-05 00:16:01 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 37.3 |
| 82212165-cd90-3314-b947-0be6cd41925e | -10.4424 | -50.7336 | 2024-10-05 00:16:05 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 53.4 |
| cf4bf10f-178d-362a-85b8-c69e18c6923a | -10.4427 | -50.7123 | 2024-10-05 00:16:05 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 43.3 |
| a266fb33-fbef-35f4-a369-9162883c3b71 | -10.5757 | -64.0248 | 2024-10-05 00:16:07 | GOES-16 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 9e21f63e-034b-323b-8480-20221dad2801 | -10.5943 | -64.024 | 2024-10-05 00:16:07 | GOES-16 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 93.2 |
| c75cb01d-02af-3c86-90f5-81bf1116f0a8 | -11.0966 | -54.2336 | 2024-10-05 00:16:09 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 79.2 |
| 879118d0-4917-37b8-bca6-78c3d6e2e256 | -11.0969 | -54.2131 | 2024-10-05 00:16:09 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 55.6 |
| d1190f5e-8907-31df-a0e5-fe3c147925d7 | -11.1155 | -54.2319 | 2024-10-05 00:16:09 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 77.6 |
| 168df898-ed67-3c5f-910e-6e46eabaf472 | -11.1158 | -54.2114 | 2024-10-05 00:16:09 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 52.3 |
| bda1663c-fb70-3a99-9818-2c99cca2da4c | -11.6995 | -47.8131 | 2024-10-05 00:16:12 | GOES-16 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 44.7 |
| 8c898031-3534-3127-8633-56ec7981824d | -11.7187 | -47.8107 | 2024-10-05 00:16:12 | GOES-16 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 110.9 |
| 2338dcfa-18d3-35e4-bf3b-ab3b7d302ed5 | -11.719 | -47.7884 | 2024-10-05 00:16:12 | GOES-16 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 67.7 |
| f17fba5a-9052-3a10-970e-b6b0d69536b2 | -12.7623 | -50.5782 | 2024-10-05 00:16:18 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 147.3 |
| 85c365bf-8f59-3a0e-8878-91e221e8563d | -12.7627 | -50.5567 | 2024-10-05 00:16:18 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 138.6 |
| 544e9c2e-27ae-32b3-947b-ccf252930988 | -13.1543 | -51.1931 | 2024-10-05 00:16:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 139.7 |
| 9882a4c0-b490-377a-86e1-48c3c69decd3 | -15.5597 | -57.4553 | 2024-10-05 00:16:34 | GOES-16 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 141.6 |
| 6ef656ae-5db9-336f-aa12-d990dd49d61c | -15.5791 | -57.4532 | 2024-10-05 00:16:34 | GOES-16 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 124.1 |
| 58f43099-3294-399e-a2c3-07af0983314e | -15.7149 | -57.4388 | 2024-10-05 00:16:35 | GOES-16 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 90.8 |
| dcc058d1-8ce3-3d96-86d2-75fdc9be7fde | -15.7151 | -57.4184 | 2024-10-05 00:16:35 | GOES-16 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 114.5 |
| 48c01fcc-c1c9-3b5d-a3a6-1662d72dfb99 | -15.7343 | -57.4367 | 2024-10-05 00:16:35 | GOES-16 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 90.0 |
| 9d134137-7be6-3bf4-b74d-fdc8e1637a6a | -15.7346 | -57.4164 | 2024-10-05 00:16:35 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 119.6 |
| 0dbc934d-69c8-323b-ba94-250ae192aa93 | -16.5345 | -57.2259 | 2024-10-05 00:16:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 103.4 |
| 4686f814-116b-31f2-b3ec-93396e50f27d | -16.554 | -57.2237 | 2024-10-05 00:16:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 242.1 |
| c107aff2-7391-31bc-972d-821c49e2abb7 | -16.5544 | -57.2032 | 2024-10-05 00:16:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 124.9 |
| 7c25092f-9c6d-38a2-94e4-ba107f5f8459 | -16.5736 | -57.2215 | 2024-10-05 00:16:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 128.2 |
| dba8af56-6f68-3f87-abd1-e4a22fd46ad8 | -16.5742 | -57.1805 | 2024-10-05 00:16:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 149.5 |
| 20a311fb-2a6f-35a2-bf96-b635e0efe092 | -16.5745 | -57.16 | 2024-10-05 00:16:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 146.8 |
| 5b52e2c1-9a16-3e59-808f-9780e24b0038 | -16.5938 | -57.1783 | 2024-10-05 00:16:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 95.1 |
| ef3e1df4-1ec7-3ada-8165-31cc52cf51a2 | -16.6594 | -55.5427 | 2024-10-05 00:16:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 101.8 |
| fc85cae4-8dac-3b45-bcdd-d3798d15b30e | -16.6598 | -55.5219 | 2024-10-05 00:16:40 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 95.3 |
| 9c842aac-b6c3-3cf3-921a-e7bbb3220a07 | -16.6601 | -55.501 | 2024-10-05 00:16:40 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 82.4 |
| a91d3a4c-cb15-3b18-b59c-19a389dd5b23 | -16.679 | -55.5402 | 2024-10-05 00:16:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 115.3 |
| c93aaf0b-fab1-37b9-8db8-aee44adf807e | -16.6797 | -55.4985 | 2024-10-05 00:16:40 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 84.0 |
| fb97b4c6-eadc-3bbc-a590-235f70c39538 | -16.6801 | -55.4777 | 2024-10-05 00:16:40 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 90.2 |
| fd60d49d-2c5c-3014-8b30-f09c1cad3b09 | -16.6871 | -57.4536 | 2024-10-05 00:16:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 102.9 |
| 6772d769-73f9-3fce-833d-d9ca55f6a884 | -16.7647 | -57.4856 | 2024-10-05 00:16:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 162.7 |
| eab54db2-39c5-3b2f-b3c7-f486c4e3d889 | -16.7843 | -57.4834 | 2024-10-05 00:16:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 104.5 |
| 3145264d-7211-342f-afeb-e4ce389df002 | -17.0888 | -56.7915 | 2024-10-05 00:16:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 111.7 |
| ecb12c2d-d978-3b40-bba8-9f89d3a9e9cd | -17.0892 | -56.7709 | 2024-10-05 00:16:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 129.2 |
| 83f74fb5-d962-3df9-b162-8703837fe5bf | -17.1085 | -56.7892 | 2024-10-05 00:16:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 105.5 |
| 618fa4ea-5442-33e5-bedf-4c3688ea8209 | -17.1288 | -56.7455 | 2024-10-05 00:16:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 99.0 |
| 75617804-5908-3d9c-943a-acc2aad5e8b6 | -18.4867 | -52.8009 | 2024-10-05 00:16:49 | GOES-16 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 137.7 |
| 178843c7-d7ab-328b-85aa-162b4fc8d9c2 | -18.4872 | -52.7792 | 2024-10-05 00:16:49 | GOES-16 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 135.9 |
| 573ae686-a664-3b12-91b6-0de26a530782 | -18.8809 | -43.6032 | 2024-10-05 00:16:50 | GOES-16 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 95.7 |
| 8f1eac41-2be9-3ff4-9893-7492756aa6d1 | -18.8816 | -43.5785 | 2024-10-05 00:16:50 | GOES-16 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 97.8 |
| ba51c58c-5f9b-390d-a7ba-3fc4bd0543cd | -18.6586 | -57.2759 | 2024-10-05 00:16:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 53.0 |
| 7a5eb2de-83d9-3ce0-9d2a-5adc5c11d331 | -18.6782 | -57.2941 | 2024-10-05 00:16:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 104.6 |
| 4e421a88-4458-398a-84b6-a6eb574b10fd | -18.6785 | -57.2734 | 2024-10-05 00:16:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 111.8 |
| 8e67b5b4-bbc8-3e45-a97b-d62f2212b76d | -18.6981 | -57.2915 | 2024-10-05 00:16:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 84.1 |
| 2983acb0-a9f3-31cd-a6cb-9df2b8f0b40b | -19.5096 | -42.8942 | 2024-10-05 00:16:53 | GOES-16 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 74.0 |
| 12fc5b8e-3d8a-3bbb-ab7b-7d25c9da421a | -20.5904 | -51.3907 | 2024-10-05 00:17:00 | GOES-16 | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 100.2 |
| 0291aeb4-5afc-3024-9908-cc3970c4fd79 | -20.7901 | -47.7465 | 2024-10-05 00:17:01 | GOES-16 | NUPORANGA | SÃO PAULO | Brasil | 3533601 | 35 | 33 | nan | nan | nan | Cerrado | 106.6 |
| b7c3b055-ec2b-334e-b826-4d9ac2719ea9 | -20.9385 | -49.0098 | 2024-10-05 00:17:02 | GOES-16 | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 102.9 |
| bf82771d-57f9-382d-b150-fe5650b0597a | -21.769899 | -47.027 | 2024-10-05 00:19:37 | METOP-C | CASA BRANCA | SÃO PAULO | Brasil | 3510807 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| d637ebad-d212-35df-b57c-7b77fddbe29b | -21.788799 | -48.715199 | 2024-10-05 00:19:42 | METOP-C | IBITINGA | SÃO PAULO | Brasil | 3519600 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 874ce361-3cab-3510-8897-ee0b356ceb0d | -21.7924 | -48.737499 | 2024-10-05 00:19:42 | METOP-C | IBITINGA | SÃO PAULO | Brasil | 3519600 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 16809d15-f88e-3560-8e87-c5a1e5b29395 | -19.833799 | -42.368698 | 2024-10-05 00:19:55 | METOP-C | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| f96c22be-0c03-3dee-aea7-bd184c29c9bc | -20.915001 | -48.984699 | 2024-10-05 00:19:57 | METOP-C | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 614aa61b-bfb9-333b-b092-51acf7e7bbf4 | -20.918699 | -49.007301 | 2024-10-05 00:19:57 | METOP-C | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 9028fec2-8a37-33e9-9348-9781d9a5db75 | -19.500601 | -42.892601 | 2024-10-05 00:20:02 | METOP-C | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 3621697d-7d97-3445-ac7c-8ae7e90ece38 | -19.489 | -42.885799 | 2024-10-05 00:20:02 | METOP-C | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| f03b7f77-8723-3772-bfe5-fd2c8ac739ab | -19.490801 | -42.894798 | 2024-10-05 00:20:02 | METOP-C | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| ca59c3e6-f257-3fb7-871b-800e17710341 | -19.492701 | -42.9039 | 2024-10-05 00:20:02 | METOP-C | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |


[Clique aqui para ver as próximas entradas](README5.md)
