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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2b3a48b8-a2a2-3b5b-8e9a-98e4e5e69066 | -10.0917 | -46.0458 | 2026-09-24 02:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 67.2 |
| 2e1c4f52-fc73-34e6-b5bb-372617be61d2 | -10.0921 | -46.0232 | 2026-09-24 02:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 96.0 |
| 532ee3b2-d504-3548-89eb-c409ae84a1cd | -3.4577 | -50.089 | 2026-09-24 02:20:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 75.1 |
| 727fce7a-1413-354b-9f90-62d54d058207 | -8.9202 | -45.9536 | 2026-09-24 02:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 206.2 |
| e4f6e610-5b1d-3376-935b-e5f97164ca52 | -10.1098 | -50.1921 | 2026-09-24 02:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 62.6 |
| 63c527d1-2d8b-3c70-8ba7-f7c47a4222e0 | -6.3501 | -57.7717 | 2026-09-24 02:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 239a78bd-c1e3-37b0-946b-9f5d53de54a2 | -8.9205 | -45.931 | 2026-09-24 02:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 133.3 |
| 87f44934-6652-3050-bb0c-94f6ea3f90e3 | -7.8996 | -61.1772 | 2026-09-24 02:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 117.9 |
| 53055006-e6fa-3e4b-869f-f6dcdd5a8f0b | -5.0064 | -45.5401 | 2026-09-24 02:30:00 | GOES-19 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 577.2 |
| eb8ac838-474f-3cd2-8d7c-cec989d7df50 | -11.9906 | -52.4695 | 2026-09-24 02:30:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 78.4 |
| 1799fe89-aa18-3f33-aa12-d431449469e2 | -1.842 | -54.7313 | 2026-09-24 02:30:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 43.9 |
| 032e0b15-f4d1-3e82-883e-89e502270525 | -10.1095 | -50.2135 | 2026-09-24 02:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 95.9 |
| 1a7380b4-dd01-3320-ae22-b39bdbac24c1 | -7.8997 | -61.1581 | 2026-09-24 02:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 58.8 |
| ddfd69ac-7412-31ad-9243-ceabebb1a7ce | -10.0917 | -46.0458 | 2026-09-24 02:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 79.6 |
| 3009b486-eb7a-3e95-ac97-a50c3db5b82d | -11.9202 | -50.7651 | 2026-09-24 02:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 56.1 |
| 4ba10174-1f83-32a0-9a5c-545d4bd3ca72 | -3.4577 | -50.089 | 2026-09-24 02:30:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 81.1 |
| 8bcd59b0-c6c8-3ddf-a9ca-91e1335154ed | -5.0062 | -45.5626 | 2026-09-24 02:30:00 | GOES-19 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 539.2 |
| 22c1ab78-8ecb-3b3f-ab31-90110f9b8f5b | -10.1284 | -50.2116 | 2026-09-24 02:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 54.7 |
| 1e24219d-5bc4-3cea-a954-85bf1453f5a0 | -11.2473 | -51.3495 | 2026-09-24 02:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 72.4 |
| 40e5f989-ff12-39f3-8cea-7ff319596e37 | -6.7211 | -44.1618 | 2026-09-24 02:30:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 59.9 |
| a546c7bb-2687-34ce-90f4-0ec35c0a1022 | -12.0096 | -52.4675 | 2026-09-24 02:30:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 83.6 |
| cd57141e-4629-31b5-822d-00a8ecde24b1 | -8.9202 | -45.9536 | 2026-09-24 02:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 74.4 |
| aeb349c3-4ceb-34e5-a01e-fdd0cbf7f56c | -6.4303 | -59.9532 | 2026-09-24 02:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 55.9 |
| 9c214315-1fd9-3090-aa76-8dd831b28864 | -6.6145 | -59.9464 | 2026-09-24 02:30:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 71.0 |
| c6498650-f397-305f-b39d-7d3c04271660 | -6.6146 | -59.9272 | 2026-09-24 02:30:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 97.1 |
| ab3e970e-6241-3185-ad4a-9c931781306d | -6.633 | -59.9457 | 2026-09-24 02:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 9a517a2e-72c5-39e7-afe1-0de25f971caf | -6.0739 | -47.2922 | 2026-09-24 02:30:00 | GOES-19 | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 82.4 |
| 0b67a5fc-2453-3607-a448-bff587872123 | -1.8421 | -54.7113 | 2026-09-24 02:30:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 45.6 |
| 57df3403-5b05-3478-85e5-100f274306b0 | -11.9392 | -50.7629 | 2026-09-24 02:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 61.2 |
| 6f4d5a9f-d89f-3d3d-a343-109c2f792c18 | -8.9394 | -45.929 | 2026-09-24 02:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 100.0 |
| 43682af7-27cd-35a7-ba55-c32be04b58ff | -10.0906 | -50.2154 | 2026-09-24 02:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 42.2 |
| 14cabca2-e07e-3697-a3d9-56386dca1943 | -6.3501 | -57.7717 | 2026-09-24 02:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 36.4 |
| 13e2ef50-8a01-3574-9279-cc6d0d2eeb51 | -11.9396 | -50.7415 | 2026-09-24 02:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 96.7 |
| 93900bda-67f8-3f68-9bd1-a733c8ad6b06 | -7.8811 | -61.1779 | 2026-09-24 02:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 54.4 |
| c0e65f78-a192-346a-aae8-7dc78f5374a6 | -5.7754 | -45.1053 | 2026-09-24 02:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 77.0 |
| eb261f86-0790-3305-aa5a-287e35b5a9c7 | -6.6331 | -59.9265 | 2026-09-24 02:30:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 57.0 |
| ae387a43-bf78-35a3-8b34-fd3216896bcd | -4.9691 | -45.5424 | 2026-09-24 02:30:00 | GOES-19 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 74.3 |
| 0ab4b631-53dc-331e-aa55-a2b2be8aa65f | -4.9876 | -45.5637 | 2026-09-24 02:30:00 | GOES-19 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 976.1 |
| 88d9416e-7b4b-34fb-a6b2-42bf54300ec8 | -5.1996 | -44.6903 | 2026-09-24 02:30:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 76.1 |
| dab13ccb-bc9e-39b7-8e42-084f63995520 | -11.2281 | -51.3727 | 2026-09-24 02:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 93.8 |
| b5312f1e-da63-3c38-ae83-c5905115e381 | -10.0921 | -46.0232 | 2026-09-24 02:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 137.2 |
| 798f3cb1-8546-3e8a-a8f0-db85a3436c76 | -4.9877 | -45.5412 | 2026-09-24 02:30:00 | GOES-19 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 1025.7 |
| 57bba562-aebe-37a7-9588-8e7ea03ae9d7 | -11.247 | -51.3706 | 2026-09-24 02:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 81.9 |
| 58c3fbcd-6797-342f-935c-b56c1826f220 | -10.0924 | -46.0005 | 2026-09-24 02:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 122.2 |
| b03b01d6-369b-3131-83dc-ad04d8cf3cf4 | -8.9391 | -45.9515 | 2026-09-24 02:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 150.1 |
| 344483c9-04c1-31a8-9394-97f3eb604801 | -11.2284 | -51.3515 | 2026-09-24 02:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 78.3 |
| 9078c2eb-3585-30c6-bb38-0eb98e29be1f | -10.1098 | -50.1921 | 2026-09-24 02:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 49.5 |
| ad29f8f0-ed3b-3cb6-8a7e-af3f5e5a5282 | -3.4392 | -50.0896 | 2026-09-24 02:30:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 51.3 |
| aabf6fab-6882-3c84-8766-9e99deee8554 | -11.9205 | -50.7437 | 2026-09-24 02:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 95.4 |
| 2a315373-d452-3799-aea4-d46f984e93a2 | -6.4487 | -59.9526 | 2026-09-24 02:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 57.6 |
| a5d5ea5a-c708-326a-9079-d56584b82348 | -6.6145 | -59.9464 | 2026-09-24 02:40:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 59.4 |
| c98f48ab-aad7-3cb6-a480-d78a06e9e186 | -10.0921 | -46.0232 | 2026-09-24 02:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 170.4 |
| 14293994-4b75-37ac-9439-c9e91f359e4b | -3.4392 | -50.0896 | 2026-09-24 02:40:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 54.8 |
| 26c371fc-1d32-35b7-a605-34a5fda7cae4 | -6.0928 | -57.6262 | 2026-09-24 02:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 28.7 |
| 75e1c978-f499-34f2-895c-88b041b2b3a8 | -5.0064 | -45.5401 | 2026-09-24 02:40:00 | GOES-19 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 458.6 |
| 4e702c0b-b7b8-33e4-b856-f0282888f6e7 | -6.6331 | -59.9265 | 2026-09-24 02:40:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 10f1eb5c-8b61-3d4c-b5bf-bb6720200fd7 | -11.9906 | -52.4695 | 2026-09-24 02:40:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 50.7 |
| c316fc69-258d-3807-a8b1-4d72bbba7b93 | -4.9879 | -45.5187 | 2026-09-24 02:40:00 | GOES-19 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 60.1 |
| 8f9b974c-95d0-3875-ac1a-8cade4d59cd1 | -12.0096 | -52.4675 | 2026-09-24 02:40:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 94.6 |
| 08fe0a79-2b3c-3cd2-9703-2d03fb872e35 | -6.6146 | -59.9272 | 2026-09-24 02:40:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 84.4 |
| d4ecc926-da73-3a4a-90f7-de615c331dec | -8.9391 | -45.9515 | 2026-09-24 02:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 91.1 |
| 087f89b8-6e1e-30f0-9af5-5ded5f068798 | -4.9876 | -45.5637 | 2026-09-24 02:40:00 | GOES-19 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 1018.7 |
| 449d5a8d-6c80-3fac-9e73-d19a7d341ab8 | -5.0062 | -45.5626 | 2026-09-24 02:40:00 | GOES-19 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 418.9 |
| 6c013be4-857e-3878-9b52-b6bca6514b26 | -1.8421 | -54.7113 | 2026-09-24 02:40:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 47.6 |
| 13c3931b-2b8d-3cd8-ad25-6d7abb7c04a0 | -8.9394 | -45.929 | 2026-09-24 02:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 71.4 |
| aa1fef32-f2ce-3745-b543-e4a661b09a2f | -7.8996 | -61.1772 | 2026-09-24 02:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 62.5 |
| 595c8837-757f-3d51-9f86-3e2b92d53bf2 | -6.633 | -59.9457 | 2026-09-24 02:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 1e086594-ee8f-32d0-a9a5-5ec4dd6ef378 | -10.0917 | -46.0458 | 2026-09-24 02:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 84.5 |
| eb3738a7-b178-3e4c-bbe4-166af93f45a3 | -11.2473 | -51.3495 | 2026-09-24 02:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 107.5 |
| 167d9392-174a-3837-84d4-2d64d417a6e4 | -11.2281 | -51.3727 | 2026-09-24 02:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 107.1 |
| 25fa3640-22f9-3ef0-b24f-d4ea226f8e30 | -11.247 | -51.3706 | 2026-09-24 02:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 102.5 |
| 797c37b7-ba51-3510-a4ba-2d99717c964e | -6.4487 | -59.9526 | 2026-09-24 02:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 55.6 |
| 2cf3f226-4c0a-3a48-884a-ce32840f80c9 | -5.1996 | -44.6903 | 2026-09-24 02:40:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 64.1 |
| afb27f5e-6489-3f87-aa55-54d06663b464 | -10.1098 | -50.1921 | 2026-09-24 02:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 54.4 |
| 5a12d039-40fa-3d43-a507-647d14718dd8 | -8.9202 | -45.9536 | 2026-09-24 02:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 70.7 |
| 34e9093d-c080-3cf7-83cd-986a7b646b7b | -3.4577 | -50.089 | 2026-09-24 02:40:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 63.6 |
| e790ae9e-9dd7-3fa6-bb15-8d672ca36c51 | -4.9877 | -45.5412 | 2026-09-24 02:40:00 | GOES-19 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 1139.0 |
| f5d2e232-8362-3d7c-8e9b-265db91258ea | -10.1095 | -50.2135 | 2026-09-24 02:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 77.6 |
| 5f7f5f14-4990-3e6a-8c87-619d25192fa8 | -11.2284 | -51.3515 | 2026-09-24 02:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 97.7 |
| 404f2809-2939-30dc-835c-cb6e4ffeb4c0 | -1.842 | -54.7313 | 2026-09-24 02:40:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 36.8 |
| de493df2-6a10-3d0a-bc4e-b7ae1c975266 | -12.0099 | -52.4465 | 2026-09-24 02:40:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 49.3 |
| 694cad9c-766c-3d38-9dac-0cdfadfcefbb | -10.0924 | -46.0005 | 2026-09-24 02:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 129.7 |
| ea99c6a3-2838-3436-969a-e4fe3095cc7e | -13.7993 | -54.0617 | 2026-09-24 02:50:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 65.7 |
| 3bb7ad05-0184-388c-8e34-2d678754e8b9 | -11.2281 | -51.3727 | 2026-09-24 02:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 58.9 |
| 0db3e35f-22d2-32be-bac7-13ba9a3cbbf4 | -11.2473 | -51.3495 | 2026-09-24 02:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 68.1 |
| 33354dcb-782f-36bc-b541-65ef7d4c45ca | -4.9877 | -45.5412 | 2026-09-24 02:50:00 | GOES-19 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 573.5 |
| 8358e7bd-015b-32af-a298-d2d5c48bc218 | -12.0096 | -52.4675 | 2026-09-24 02:50:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 100.1 |
| a8e9a0d6-f4a4-38bb-86af-e53fc9d5bf71 | -11.247 | -51.3706 | 2026-09-24 02:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 67.6 |
| d47bc372-b74b-33f4-8658-087316b6715f | -6.4487 | -59.9526 | 2026-09-24 02:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 7db4e8f4-84cf-3d50-a2d7-76a0ebb59547 | -6.6331 | -59.9265 | 2026-09-24 02:50:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 52.7 |
| 83710b82-610a-36f2-9f2b-7835f41c94da | -10.1098 | -50.1921 | 2026-09-24 02:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 53.9 |
| 264af7d3-dd8a-3cbf-adca-44c4f499814e | -5.0064 | -45.5401 | 2026-09-24 02:50:00 | GOES-19 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 361.9 |
| 15928fc2-e079-3eb7-8edc-6c17eeb6cb1e | -13.7801 | -54.0639 | 2026-09-24 02:50:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 67.3 |
| d215d605-352e-325f-ba92-d22f9584e7e0 | -10.0924 | -46.0005 | 2026-09-24 02:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 118.7 |
| e7d1e51c-e031-3b9f-8ddf-e928e20984d9 | -1.842 | -54.7313 | 2026-09-24 02:50:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 52.9 |
| 29567539-fda7-3f23-8cbc-b031d4e8a9d7 | -8.9391 | -45.9515 | 2026-09-24 02:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 70.3 |
| e9a05fd7-5e81-3096-b100-f035c83e26a0 | -3.4392 | -50.0896 | 2026-09-24 02:50:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 48.2 |
| 6b89ab14-4bf5-352b-97c9-7ee50885c0bc | -3.4577 | -50.089 | 2026-09-24 02:50:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 83.0 |
| 493592b6-87de-3f48-b0cc-52bff3d80988 | -1.8421 | -54.7113 | 2026-09-24 02:50:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 61.9 |
| d7820831-c989-3bba-887a-22f46d15a753 | -10.1095 | -50.2135 | 2026-09-24 02:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 65.7 |


[Clique aqui para ver as próximas entradas](README26.md)
