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

## Dados Diários - Página 85

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b0ee74b2-26fe-3720-88b0-b4dcc49430e7 | -16.4914 | -55.0858 | 2025-09-16 08:30:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 88.9 |
| c7438a69-1873-364a-91d9-a5c838b59ce9 | -16.491 | -55.1067 | 2025-09-16 08:40:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 86.9 |
| b49e8ecf-53ba-39ec-a836-e43a1a0ae6a0 | -16.0557 | -59.4195 | 2025-09-16 08:40:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 74.7 |
| 02230da5-5dab-3dd3-94dd-9b55b24a8002 | -16.4714 | -55.1092 | 2025-09-16 08:40:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 90.7 |
| eecbfdb6-7bec-3f1f-bb7c-57e563f15e96 | -16.491 | -55.1067 | 2025-09-16 08:50:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 73.3 |
| 09da34ad-3051-38c6-8332-9657a51eadd3 | -16.4714 | -55.1092 | 2025-09-16 08:50:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 87.1 |
| a44dd905-99e3-3547-85f0-bf73cce8dfe1 | -9.086 | -44.8663 | 2025-09-16 09:00:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 194.5 |
| b623d54a-7314-31f7-ab83-df8d370327aa | -9.105 | -44.8641 | 2025-09-16 09:00:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 112.4 |
| cc5ee825-2aac-350f-9b55-e4df30228446 | -15.9998 | -59.2446 | 2025-09-16 09:10:00 | GOES-19 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 78.5 |
| 0933ab13-e4c1-36f7-ad60-be03ba624936 | -9.105 | -44.8641 | 2025-09-16 09:10:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 127.2 |
| fa9adf1c-dac2-3659-864c-c44a397bc3b2 | -9.086 | -44.8663 | 2025-09-16 09:10:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 134.1 |
| 6aa7a0aa-5f7a-34fd-9ccc-a234b339988f | -9.086 | -44.8663 | 2025-09-16 09:20:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 172.7 |
| 7cf85e03-9d46-339e-9da2-d619c7dc0a6c | -9.086 | -44.8663 | 2025-09-16 09:30:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 188.1 |
| 7130df82-6aef-3abd-b585-0229661cef1b | -9.0857 | -44.8893 | 2025-09-16 09:30:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 122.3 |
| b33170c5-1f64-397a-a23f-b004d1173f7e | -9.086 | -44.8663 | 2025-09-16 09:40:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 194.9 |
| e026180e-623d-350d-abd8-b4ee4c86b4ba | -9.0857 | -44.8893 | 2025-09-16 09:40:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 137.4 |
| 4e7edef9-8cc6-397f-973e-4c3819c65b57 | -9.0857 | -44.8893 | 2025-09-16 09:50:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 123.8 |
| 579fdfdb-083d-3e4c-96cb-45d9a6d852e3 | -9.086 | -44.8663 | 2025-09-16 09:50:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 237.0 |
| 23e689f1-c0a9-3745-8a1b-1998d0274825 | -13.2993 | -54.2207 | 2025-09-16 10:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 106.7 |
| d040e4b3-5734-38b0-ad40-b76a778bc9ac | -9.0857 | -44.8893 | 2025-09-16 10:00:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 144.7 |
| 2a6da031-a646-3e71-a37c-9237587d2eb6 | -9.086 | -44.8663 | 2025-09-16 10:00:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 257.7 |
| d90d5847-e29a-3408-a321-4a46292dadd0 | -9.105 | -44.8641 | 2025-09-16 10:00:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 94.1 |
| c5873141-99db-3c85-b9aa-e55d4d7a945c | -9.086 | -44.8663 | 2025-09-16 10:10:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 159.7 |
| 1fe9c09b-558e-35e2-aabd-a7e992ecd920 | -9.0857 | -44.8893 | 2025-09-16 10:10:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 142.1 |
| 4673336f-bc4f-392e-9aee-f4eee011abd8 | -9.086 | -44.8663 | 2025-09-16 10:20:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 182.2 |
| b4e6b177-a0c2-3246-8eb8-104915495e91 | -9.0857 | -44.8893 | 2025-09-16 10:20:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 187.4 |
| a302cbbf-c4a1-3c89-96ef-26149dec9f2e | -9.0857 | -44.8893 | 2025-09-16 10:30:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 158.8 |
| bf76c809-022d-3045-ac5e-bde4e75e7272 | -9.086 | -44.8663 | 2025-09-16 10:30:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 232.0 |
| 49812915-3a4b-306b-8f06-816903716a34 | -9.0857 | -44.8893 | 2025-09-16 10:40:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 233.6 |
| a1324c19-b38f-3336-8868-0afa7268e16e | -12.6352 | -45.7652 | 2025-09-16 10:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 337.5 |
| fd97af6a-2623-3362-bec8-a0cfcc270cdc | -9.105 | -44.8641 | 2025-09-16 10:40:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 98.7 |
| 5df94297-ac66-3160-b4ae-2c24f3467a76 | -9.086 | -44.8663 | 2025-09-16 10:40:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 293.0 |
| b5ebf648-6724-31a4-90cc-18e3f6d85a8c | -12.6356 | -45.7422 | 2025-09-16 10:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 191.5 |
| 4ccf7545-037f-36cb-b860-367837b6659b | -9.0857 | -44.8893 | 2025-09-16 10:50:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 199.8 |
| 0cc029d1-e0d5-3529-ac84-604fd25f7490 | -12.6356 | -45.7422 | 2025-09-16 10:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 312.4 |
| 481dd37f-97dc-340f-b627-ea34f6e49b92 | -12.6729 | -47.9258 | 2025-09-16 10:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 215.0 |
| f0c331b6-e89e-3f6e-be91-e3253188025b | -9.086 | -44.8663 | 2025-09-16 10:50:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 160.2 |
| 3d949551-a3a4-32e4-aa81-4fce0b3e5deb | -12.6164 | -45.7452 | 2025-09-16 10:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 97.7 |
| 4bf9e9ba-128b-3b78-a5d6-f11d327cdc1a | -9.1709 | -46.9792 | 2025-09-16 10:50:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 89.3 |
| 777c0541-4e5f-3853-91ae-1bdd4b731b02 | -12.6352 | -45.7652 | 2025-09-16 10:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 256.1 |
| c113c187-3afe-3165-8382-884adae4d3d9 | -9.0668 | -44.8914 | 2025-09-16 10:50:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 115.2 |
| f240f480-d526-3fa8-91f9-b526600b979d | -12.6356 | -45.7422 | 2025-09-16 11:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 463.0 |
| 4235cbd3-1ee4-3f51-bdca-532c3cacc394 | -8.5944 | -46.3695 | 2025-09-16 11:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 91.2 |
| 8d09a8f6-d360-3ab8-a821-039f6afcd367 | -8.0007 | -45.6638 | 2025-09-16 11:00:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 86.9 |
| 36fee481-44e2-3c9f-a302-2d237a943851 | -9.0857 | -44.8893 | 2025-09-16 11:00:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 111.6 |
| b0d6c321-af84-3113-97a3-f403ec079ced | -12.6352 | -45.7652 | 2025-09-16 11:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 649.7 |
| 4df0f6f4-c679-37e6-baf2-2c5853dd8ca3 | -12.6725 | -47.948 | 2025-09-16 11:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 109.8 |
| 1088f86a-ba6b-35f9-84b6-6ad7e3e6a269 | -12.6729 | -47.9258 | 2025-09-16 11:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 130.0 |
| bddb8539-869b-362c-8244-4bf0e70b1b4e | -9.105 | -44.8641 | 2025-09-16 11:00:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 90.4 |
| cf65ccd8-6473-3ebf-ac0f-1c9295df6d42 | -12.6909 | -47.9899 | 2025-09-16 11:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 96.2 |
| f201e4be-c8b9-33b7-bd6a-9dbd0dc85b61 | -9.086 | -44.8663 | 2025-09-16 11:00:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 115.4 |
| 6be26b1e-e6f2-3d1d-9658-2c9244d9bdfe | -12.6725 | -47.948 | 2025-09-16 11:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 172.7 |
| 01bfcde9-d60e-3c18-a667-b2f561c07f3f | -12.6729 | -47.9258 | 2025-09-16 11:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 185.8 |
| fc0923c0-ba19-3504-89fa-0bc096afc8fb | -12.6352 | -45.7652 | 2025-09-16 11:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 250.3 |
| aa9c08fd-057f-358e-901b-95c872b79eb7 | -10.7302 | -46.5082 | 2025-09-16 11:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 111.4 |
| 8f9a27a0-9135-386a-a5f1-520b3d8515d3 | -9.0857 | -44.8893 | 2025-09-16 11:10:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 211.7 |
| 5c55d340-5c56-3a0b-8e6f-97980a07bdfd | -12.6356 | -45.7422 | 2025-09-16 11:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 237.8 |
| d9844a0f-fdac-3978-a235-c2703c14b4f7 | -12.6906 | -48.0121 | 2025-09-16 11:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 90.9 |
| ca2656e8-e9bd-3870-86ac-21f23c6dec6c | -8.0007 | -45.6638 | 2025-09-16 11:10:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 92.9 |
| 4da9e30c-a94e-3f34-a7ae-b0f26bb1422c | -12.6909 | -47.9899 | 2025-09-16 11:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 92.8 |
| 9a9246aa-21dc-3e72-9e5a-f4797b014e87 | -9.086 | -44.8663 | 2025-09-16 11:10:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 167.5 |
| 4adb637b-2d69-3471-b44d-587fcd2991fc | -9.5309 | -45.523 | 2025-09-16 11:10:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 81.9 |
| 35f4578e-9705-371e-b4dd-2c0d738571de | -9.086 | -44.8663 | 2025-09-16 11:20:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 228.5 |
| ba0e6872-557c-37f9-9d66-aa1c7761030f | -12.6729 | -47.9258 | 2025-09-16 11:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 211.1 |
| 7a91d0f0-b885-32ca-bbae-937e4d78d74d | -9.0857 | -44.8893 | 2025-09-16 11:20:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 194.4 |
| 8e2608d8-98e6-38ae-8e50-3a36c1166210 | -12.6909 | -47.9899 | 2025-09-16 11:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 131.5 |
| 4d81fc2e-fcff-365a-98c7-22ad46e2e238 | -9.0671 | -44.8685 | 2025-09-16 11:20:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 132.6 |
| e49ad3f7-a557-3c4d-ae7f-b5698d0f3cb6 | -12.6356 | -45.7422 | 2025-09-16 11:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 116.5 |
| 286c9050-7404-3281-9c75-8e18e2f79e3f | -12.6352 | -45.7652 | 2025-09-16 11:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 168.0 |
| 471b1373-3c09-311b-b101-d22b2c57d2f1 | -8.0007 | -45.6638 | 2025-09-16 11:20:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 81.4 |
| a27cf4eb-d1a1-3c57-9128-f77419e913f2 | -12.6725 | -47.948 | 2025-09-16 11:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 244.4 |
| 450a7f5d-7ab6-32ae-9043-4713bfe12e05 | -12.6917 | -47.9454 | 2025-09-16 11:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 150.4 |
| 746ce36c-e9c6-3259-b93a-4ec5fac1685c | -10.7302 | -46.5082 | 2025-09-16 11:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 97.5 |
| 06e6f510-beb9-38df-96aa-f1d48e600523 | -9.5309 | -45.523 | 2025-09-16 11:20:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 86.6 |
| df79147b-caa1-3593-8776-5662f365e6ad | -9.105 | -44.8641 | 2025-09-16 11:20:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 86.7 |
| 74a6a245-9e73-3199-be9c-e09515993020 | -12.6906 | -48.0121 | 2025-09-16 11:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 190.7 |
| bc4f3c4e-6cec-303c-b8eb-6900d893da4c | -12.6909 | -47.9899 | 2025-09-16 11:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 112.4 |
| 7d35f0ec-7a10-367a-8408-8702e48e889f | -9.0857 | -44.8893 | 2025-09-16 11:30:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 148.9 |
| 27c19315-14f7-3097-8f22-e05b2a6fd967 | -10.7302 | -46.5082 | 2025-09-16 11:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 108.0 |
| ce360682-cbe1-3021-a6a8-164a277aa6bc | -12.6725 | -47.948 | 2025-09-16 11:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 143.3 |
| 58323c2e-586e-3153-adb6-557e71456638 | -12.6906 | -48.0121 | 2025-09-16 11:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 125.4 |
| d4469a52-089f-31fc-9fa3-41c715221b3b | -12.6917 | -47.9454 | 2025-09-16 11:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 90.8 |
| d3bcc6e9-ee51-3462-b6ce-fd9b8b401003 | -9.086 | -44.8663 | 2025-09-16 11:30:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 133.5 |
| 6d15c991-26ba-374f-90f0-f334d122ac71 | -9.105 | -44.8641 | 2025-09-16 11:30:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 104.2 |
| 81556d65-7c13-32d0-8652-ec9567251329 | -8.0007 | -45.6638 | 2025-09-16 11:30:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 118.7 |
| 3b177300-7471-3fee-ad77-1b15f0bb2b57 | -12.6352 | -45.7652 | 2025-09-16 11:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 116.7 |
| 83cb97fd-ed25-3baf-9f2b-20aec839d4ec | -9.5309 | -45.523 | 2025-09-16 11:30:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 89.2 |
| 6617da89-e714-3fac-991f-ab2c5ab307be | -8.0196 | -45.662 | 2025-09-16 11:30:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 147.8 |
| bc33e26d-e6b2-3cee-905e-76c39ded2a4f | -12.6729 | -47.9258 | 2025-09-16 11:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 189.1 |
| 4ab17005-9ea7-313d-ba3b-31c187562dd7 | -12.6356 | -45.7422 | 2025-09-16 11:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 105.5 |
| fa9a4ac7-cc05-389c-bf41-caa72655864f | -12.6713 | -48.0148 | 2025-09-16 11:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 80.6 |
| 4894fe80-b013-359d-bff4-962ece1f5985 | -12.6725 | -47.948 | 2025-09-16 11:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 128.6 |
| 7333b52d-0859-38c6-8c5a-77e1fe7a4ac7 | -12.6917 | -47.9454 | 2025-09-16 11:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 112.5 |
| d720e1ca-607f-3492-b61e-dc9d665acc48 | -12.6906 | -48.0121 | 2025-09-16 11:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 229.7 |
| 0783def1-7b8a-3d75-b711-587b446d7b34 | -8.0007 | -45.6638 | 2025-09-16 11:40:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 144.2 |
| 2b043706-fd78-37df-a624-b13e41e72fa1 | -6.7569 | -48.1173 | 2025-09-16 11:40:00 | GOES-19 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Amazônia | 71.6 |
| 6c46a44a-0998-35dd-9b00-1198f4690674 | -9.5309 | -45.523 | 2025-09-16 11:40:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 108.7 |
| 07ed39dc-103e-30dd-aada-d7e9741af9c9 | -8.0196 | -45.662 | 2025-09-16 11:40:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 171.6 |
| 11c386ea-f85f-3258-bb8c-381cad19dd45 | -10.7302 | -46.5082 | 2025-09-16 11:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 287.6 |
| 822d6c01-e7b5-3dd0-81c8-8ea101fcec3b | -9.0857 | -44.8893 | 2025-09-16 11:40:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 105.8 |


[Clique aqui para ver as próximas entradas](README86.md)
