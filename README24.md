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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5d4c56b9-0a89-3f32-ae87-a765e21215c8 | -3.4392 | -50.0896 | 2026-09-24 02:00:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 1ee328a0-32e4-3fa8-ad87-68195d02e71b | -12.4024 | -46.9579 | 2026-09-24 02:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 79.7 |
| 64b6a275-0b71-3b90-8d27-ec499de0ab27 | -1.842 | -54.7313 | 2026-09-24 02:00:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 44.0 |
| 91ce3b4b-ff18-34b9-a4f5-40bd16a823d9 | -7.7679 | -72.9879 | 2026-09-24 02:00:00 | GOES-19 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 17fd46b0-99e7-3a69-95f7-f91312f763d9 | -3.4577 | -50.089 | 2026-09-24 02:00:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 72.0 |
| 7ace5c01-6040-32ba-9f45-66434ddf95b0 | -7.8811 | -61.1779 | 2026-09-24 02:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 50.2 |
| 363304fd-9de5-3f58-b7c1-6d2ae0aafbc8 | -5.7754 | -45.1053 | 2026-09-24 02:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 77.6 |
| 3eb14ce6-2786-3c4d-a40b-857a35f70c64 | -10.0924 | -46.0005 | 2026-09-24 02:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 95.0 |
| 3660227b-7dfe-36c6-b3e2-8aab4c0af194 | -10.1095 | -50.2135 | 2026-09-24 02:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 93.5 |
| 126b73a0-445f-3a92-8774-558361a0ae17 | -12.4216 | -46.9551 | 2026-09-24 02:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 97.2 |
| 9f54fd19-732f-31e5-b91b-091618729739 | -3.4578 | -50.0679 | 2026-09-24 02:00:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 54.3 |
| 1b91d37a-5bf8-3be8-b375-c08ce7eb56f0 | -11.9396 | -50.7415 | 2026-09-24 02:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 275.9 |
| 3f9dc666-9c8d-3bc4-a87a-5bea12785f70 | -4.1181 | -51.0695 | 2026-09-24 02:00:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 48.5 |
| b82c406a-d8dc-3fce-ae2a-77d75a408f04 | -12.1494 | -50.717 | 2026-09-24 02:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 69.4 |
| 9ba4b760-bd1b-3d82-a106-873224449416 | -6.7211 | -44.1618 | 2026-09-24 02:00:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 67.4 |
| d2339ad0-1513-3ddf-9bfc-2f7087426fbe | -11.9586 | -50.7393 | 2026-09-24 02:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 106.0 |
| 45c93005-acaa-32c5-a0e2-a6ad646dcc0c | -6.4486 | -59.9717 | 2026-09-24 02:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 48.5 |
| 51600e6e-2162-398f-aa5f-9fa84890cceb | -7.8997 | -61.1581 | 2026-09-24 02:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 43.9 |
| eca353bb-4b09-3d7d-a955-22812b883262 | -4.9877 | -45.5412 | 2026-09-24 02:00:00 | GOES-19 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 513.3 |
| cc345771-30a2-3146-9111-f404aad77142 | -6.4303 | -59.9532 | 2026-09-24 02:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 184d6eb7-7e9d-376b-aefa-85d100f9d6fa | -4.9691 | -45.5424 | 2026-09-24 02:00:00 | GOES-19 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 66.4 |
| 4b4e84dc-076b-36f5-aae0-e223d0f68360 | -12.0096 | -52.4675 | 2026-09-24 02:10:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 72.7 |
| 0ea3552e-d946-3c82-8cae-1a28b1f880b5 | -10.1098 | -50.1921 | 2026-09-24 02:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 44.6 |
| f9b9a8eb-a6a9-3abc-b70e-2df4f36a934e | -4.9877 | -45.5412 | 2026-09-24 02:10:00 | GOES-19 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 577.1 |
| ed35bc39-63bd-349f-b710-3705569bece4 | -10.1095 | -50.2135 | 2026-09-24 02:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 139.5 |
| c7d35694-74b9-33fa-9f6e-aca548c84f37 | -11.9906 | -52.4695 | 2026-09-24 02:10:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 78.1 |
| d4174eaf-9f5c-3aa3-b572-d0a234d5a5e5 | -8.9202 | -45.9536 | 2026-09-24 02:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 177.1 |
| 0b81326e-4b27-333d-9d3a-0171d3bf2332 | -5.0062 | -45.5626 | 2026-09-24 02:10:00 | GOES-19 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 310.7 |
| 2cab9f81-bf4e-353d-aedb-b4c031d2f9cc | -5.0064 | -45.5401 | 2026-09-24 02:10:00 | GOES-19 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 404.2 |
| 0b30846b-9634-3cec-ab11-cefb02a8ddeb | -4.9691 | -45.5424 | 2026-09-24 02:10:00 | GOES-19 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 101.6 |
| a9d9ca2e-04c3-3274-b2ea-121cfa7ff4ae | -1.842 | -54.7313 | 2026-09-24 02:10:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 30.2 |
| be67a0d7-9a82-367e-98a1-6440a587d546 | -12.4216 | -46.9551 | 2026-09-24 02:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 68.2 |
| e7132b01-9099-34d7-b2d0-18598946c402 | -4.9876 | -45.5637 | 2026-09-24 02:10:00 | GOES-19 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 463.1 |
| b9f41c1d-70fe-3a5d-92ae-cd39b445ade5 | -6.7211 | -44.1618 | 2026-09-24 02:10:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 61.5 |
| 391f4920-80b3-335f-b8de-b8a99d34d276 | -8.9205 | -45.931 | 2026-09-24 02:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 80.8 |
| c6c9b9d3-3baf-3fa6-a87e-9dc584c417c1 | -5.1058 | -60.2639 | 2026-09-24 02:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 68.9 |
| 0ea8572b-7481-390c-975a-d3d7b22c38ca | -7.8996 | -61.1772 | 2026-09-24 02:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 99.0 |
| 245045b7-c258-3c9c-85db-e7c606851c17 | -11.9202 | -50.7651 | 2026-09-24 02:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 70.5 |
| 61dd8639-ac4a-3792-afe0-e68a91b39b2f | -6.4486 | -59.9717 | 2026-09-24 02:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 49.0 |
| 9a18276e-6988-3c06-9dc3-f07905bad495 | -7.8997 | -61.1581 | 2026-09-24 02:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 2a59e712-5cce-3599-8636-be80270c8569 | -12.0418 | -50.2796 | 2026-09-24 02:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 73.6 |
| 6b543ffe-7530-3ab6-b116-eeb1f508a79b | -11.9205 | -50.7437 | 2026-09-24 02:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 115.0 |
| 517c7fc9-e8d3-3e39-bb3a-c8b4e0b5d0a2 | -1.8421 | -54.7113 | 2026-09-24 02:10:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 40.3 |
| 03bd4f2f-1bef-32f5-a845-90c663ef443c | -8.9391 | -45.9515 | 2026-09-24 02:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 131.0 |
| 9fe51e83-9dba-30da-a27f-c728cf38c92b | -6.4303 | -59.9532 | 2026-09-24 02:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 52.7 |
| 190068e0-4584-3d75-acf8-070ec14d3165 | -8.9394 | -45.929 | 2026-09-24 02:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 69.5 |
| 4c54e7ad-25bc-39bf-b155-e0f3fd789e8a | -10.0924 | -46.0005 | 2026-09-24 02:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 84.2 |
| f9f9408c-32e9-39d7-9193-18cd6e627c78 | -10.1092 | -50.2349 | 2026-09-24 02:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 67.0 |
| 574cb927-94a1-33ca-8808-69d4520bf080 | -4.9689 | -45.5649 | 2026-09-24 02:10:00 | GOES-19 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 86.7 |
| dfe7355f-2936-37fc-8ab4-96b3d8d5df75 | -10.0921 | -46.0232 | 2026-09-24 02:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 81.5 |
| e1f2651d-f04c-3453-bbf0-61ea61509a75 | -6.6146 | -59.9272 | 2026-09-24 02:10:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 77.1 |
| a333ff95-1cc1-3a0f-91d1-693e4ca5c64e | -7.8811 | -61.1779 | 2026-09-24 02:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 53.0 |
| 704a4c4c-640d-3ef9-a6c4-b4c8a01a4d2d | -10.1281 | -50.233 | 2026-09-24 02:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 88.7 |
| 4c2a606e-cf7d-309e-8c47-4a05e59a2112 | -11.9396 | -50.7415 | 2026-09-24 02:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 148.2 |
| b4d0c18e-9cb0-3a3f-a1e9-06b9a3896b30 | -5.7754 | -45.1053 | 2026-09-24 02:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 73.7 |
| cfc41234-4ae5-3ae2-a63f-25ec853dedc7 | -12.4024 | -46.9579 | 2026-09-24 02:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 53.5 |
| 1f22d972-a15f-36b9-b003-7b5401e64373 | -6.4487 | -59.9526 | 2026-09-24 02:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 70.0 |
| efe1330a-578c-31c8-bd0b-5c8b16c62a7f | -10.1284 | -50.2116 | 2026-09-24 02:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 135.1 |
| 8a1ff246-731e-38ab-850d-aee6e584ae54 | -3.4577 | -50.089 | 2026-09-24 02:10:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 91.2 |
| dcc65cb1-3e58-3eda-ac11-12e961053d1d | -6.3501 | -57.7717 | 2026-09-24 02:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 61.4 |
| f6ca7b3f-7f3d-33e4-99d2-3f10afba2f0f | -7.7679 | -72.9879 | 2026-09-24 02:10:00 | GOES-19 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 82a448de-69f7-3178-9f73-86cc2bff41cd | -7.918 | -61.1764 | 2026-09-24 02:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 36.8 |
| 84423332-ce4c-3877-ba57-0a4f4dbd44f1 | -3.4578 | -50.0679 | 2026-09-24 02:10:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 664eeb41-f124-36e3-b384-2ed2a0687cfb | -11.9392 | -50.7629 | 2026-09-24 02:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 101.5 |
| d33d538a-7e21-3ec7-9207-7af9ffa66ad5 | -4.98 | -45.52 | 2026-09-24 02:15:00 | MSG-03 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a05bd1a0-f2f7-3d38-b5a6-bc944956d552 | -4.98 | -45.56 | 2026-09-24 02:15:00 | MSG-03 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d59c83da-bcbe-3c61-ac9a-d72d464da59d | -10.1095 | -50.2135 | 2026-09-24 02:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 116.2 |
| d165a8c9-5424-3f58-ac30-7c4cdd4f0984 | -5.0064 | -45.5401 | 2026-09-24 02:20:00 | GOES-19 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 753.6 |
| f38f6b3b-1e31-36ca-bd95-7ca5c0625939 | -1.8421 | -54.7113 | 2026-09-24 02:20:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 49.5 |
| c567cffc-2f17-3181-8fac-8f8705894ec8 | -5.0062 | -45.5626 | 2026-09-24 02:20:00 | GOES-19 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 426.5 |
| 609ea9ea-400f-3b3a-a9c7-7ec3552631b2 | -6.6145 | -59.9464 | 2026-09-24 02:20:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 66.7 |
| 004e6e2e-0ccd-33af-837d-58d8a71c70d2 | -4.9691 | -45.5424 | 2026-09-24 02:20:00 | GOES-19 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 121.1 |
| a59bcd9e-b2ce-3e03-8f68-8fcc0928abdb | -1.842 | -54.7313 | 2026-09-24 02:20:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 28.9 |
| be198ac1-67f6-3afb-a36e-0299be8075fe | -11.9906 | -52.4695 | 2026-09-24 02:20:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 124.1 |
| 98a4e149-0169-3cc7-bfca-e72438607f71 | -4.9877 | -45.5412 | 2026-09-24 02:20:00 | GOES-19 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 1076.8 |
| b9e8e605-f4ff-3e76-8641-f9b68eb7e2ac | -11.9392 | -50.7629 | 2026-09-24 02:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 77.4 |
| 6e3a0ae8-22fa-3819-b3b8-80e534cef6aa | -10.1284 | -50.2116 | 2026-09-24 02:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 69.4 |
| 5405769c-1415-3168-a3e7-4b824ce9f82f | -7.8996 | -61.1772 | 2026-09-24 02:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 90.6 |
| 9fdfbd9d-04b8-3367-9480-30ba5e22e7dd | -6.6146 | -59.9272 | 2026-09-24 02:20:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 105.8 |
| aa518e18-fe1d-33b2-b3bf-5e538e583181 | -10.1092 | -50.2349 | 2026-09-24 02:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 46.0 |
| d229f23e-c2f0-309d-8423-3e607f5d1bb2 | -4.9689 | -45.5649 | 2026-09-24 02:20:00 | GOES-19 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 74.3 |
| e63fb53c-a912-381b-a140-19dea7eb6358 | -11.9396 | -50.7415 | 2026-09-24 02:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 193.4 |
| 4ec97f2f-caaf-389e-ab3c-81a9287ba045 | -6.633 | -59.9457 | 2026-09-24 02:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 53.1 |
| a947455f-514e-3902-a2b0-0e3b16ea5cc4 | -5.7754 | -45.1053 | 2026-09-24 02:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 586a79e3-7348-3c69-bc5b-be25a1b6185c | -8.9391 | -45.9515 | 2026-09-24 02:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 178.6 |
| c4cac859-8bb2-3a29-a423-023443d30f26 | -7.8811 | -61.1779 | 2026-09-24 02:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 781f7e8d-def4-365e-82cb-3f4e9c606326 | -8.9394 | -45.929 | 2026-09-24 02:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 121.6 |
| 65e0241d-2216-39a3-b55d-d741e98d1e3f | -10.0924 | -46.0005 | 2026-09-24 02:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 99.7 |
| 6e18ece0-91b3-3e42-bdf6-641844bb5088 | -11.9586 | -50.7393 | 2026-09-24 02:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 84.1 |
| c4151c12-5a10-3d56-9bea-66966d7069c7 | -6.6331 | -59.9265 | 2026-09-24 02:20:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 1395ff86-1a90-3c67-80cf-7a0a23a9f772 | -7.8997 | -61.1581 | 2026-09-24 02:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 54.6 |
| d08a5584-db00-3ff3-9029-d663edcc8f6d | -6.4487 | -59.9526 | 2026-09-24 02:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 76.5 |
| 99f0787d-7dbb-35c6-a866-f84c422f1267 | -4.9876 | -45.5637 | 2026-09-24 02:20:00 | GOES-19 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 614.5 |
| d7477cf7-a941-32d3-bfe7-c0b130801833 | -6.0739 | -47.2922 | 2026-09-24 02:20:00 | GOES-19 | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 73.3 |
| c5f26568-e55e-3c57-9bea-c8714239fa0a | -5.1996 | -44.6903 | 2026-09-24 02:20:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 115.5 |
| 1b1fed6c-e13c-3b79-9ea4-708aab208c8c | -6.7211 | -44.1618 | 2026-09-24 02:20:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 49.6 |
| e3f37824-c296-344d-916c-cedf5a5b76f0 | -11.9205 | -50.7437 | 2026-09-24 02:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 114.5 |
| 20c297db-7914-36c4-aa21-5deb3f5cd309 | -12.0418 | -50.2796 | 2026-09-24 02:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 63.5 |
| 3511fcb9-d487-36c3-a707-117a12373c3d | -12.0096 | -52.4675 | 2026-09-24 02:20:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 125.1 |
| f1978b34-89ce-3a03-a7b5-5e0aaf13c776 | -3.4578 | -50.0679 | 2026-09-24 02:20:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 60.0 |


[Clique aqui para ver as próximas entradas](README25.md)
