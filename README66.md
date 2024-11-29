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

## Dados Diários - Página 66

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7d3cf151-c244-3464-8493-67ac6df455e2 | -3.65735 | -50.23712 | 2024-11-29 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8c6ed31d-2e41-383d-93b2-b9d66beeb97d | -2.82607 | -54.06364 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d2f50d2a-07d5-3437-ac81-8644c4e1a6cc | -2.59226 | -54.07978 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 476079a7-4a8b-32b9-99ec-15c993a7832b | -1.57016 | -51.21733 | 2024-11-29 04:57:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 807a826e-7986-3dc8-b0b1-86729200030f | -4.07329 | -47.03127 | 2024-11-29 04:57:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4a103ad1-a2dd-37ce-b2d7-9a038ef7b0a9 | -2.95642 | -53.88309 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a5495b72-ff67-3b8d-ae42-0c532265562f | -1.20851 | -53.92297 | 2024-11-29 04:57:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6399f888-022e-32db-ab4b-9a50a6172a17 | -1.09649 | -53.39795 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 17.3 |
| b745ce38-4702-32be-aba1-4cbdb64c26b7 | -1.74149 | -52.79533 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8742777e-a9c8-3669-b51a-629c3e9c9ff1 | -2.36343 | -50.52207 | 2024-11-29 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 783c2408-9aca-323a-b5f3-21f92a075488 | -2.65202 | -51.77434 | 2024-11-29 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 63b94eaa-80ce-37e0-be35-c047fd79af73 | 1.87744 | -55.74394 | 2024-11-29 04:57:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ac2d589f-5750-3542-b6ee-e7b61d4b9e2a | -3.98042 | -46.74195 | 2024-11-29 04:57:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e11597af-97ec-33d2-b032-72a564b6d6b1 | -1.09193 | -53.36216 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 2dc97f6c-f924-357d-b297-3b634135a52f | -1.78159 | -55.21729 | 2024-11-29 04:57:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2ee42fbc-1bc2-3be3-8782-d9ee5b8d0f62 | -1.68905 | -52.45614 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 36572288-41f2-37ca-a968-4de792c86125 | -3.50229 | -53.80719 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 983bc959-4f28-3538-b929-6fa9e8b207b6 | -2.34039 | -46.87226 | 2024-11-29 04:57:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a966dba8-5587-3019-978a-881fde37046b | -3.91544 | -53.66771 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 27bdf5b1-b682-3c76-8584-8722bbb65c02 | -3.317 | -52.15036 | 2024-11-29 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e68cc85b-e9a4-389a-bcce-217b4fb3420a | -3.42134 | -53.88896 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1295978f-51a6-3285-8954-ae0605ae6fde | -3.70987 | -51.80758 | 2024-11-29 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5acd2a82-b2fa-3e53-8732-10e81f3a3fbd | -1.55913 | -52.01814 | 2024-11-29 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 90885fb2-fa03-37cd-bb3d-479093eea4e7 | -1.19629 | -53.89272 | 2024-11-29 04:57:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8edd4d09-baee-32fe-8ed1-549fdadc6beb | -3.61532 | -49.85395 | 2024-11-29 04:57:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 47db43d8-ecf8-3164-a917-8cb6f640479c | -2.36743 | -53.82234 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f39ec851-b4f3-3432-b4fd-3273f3b164f6 | -2.89005 | -55.22059 | 2024-11-29 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 840dce83-7a4d-31ed-994e-a0876e056980 | -1.19575 | -53.89616 | 2024-11-29 04:57:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d768b19e-f441-3b51-afac-c82bde357733 | -4.17024 | -48.61988 | 2024-11-29 04:57:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 87f9db5e-ff94-3daf-b6b5-95399d5f6d6a | -2.38499 | -56.08879 | 2024-11-29 04:57:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| fc4fc308-6c92-329e-8225-a0b8768efef7 | -1.37684 | -52.84444 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a5717c93-3619-3d48-9ab8-567b9edc6a5b | -3.91443 | -50.10092 | 2024-11-29 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 12758c88-604c-30f7-80b3-12eb240d2792 | -2.59057 | -54.06892 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3904d5b9-1c8a-3bc0-9d65-4253d873163d | -2.26803 | -53.47644 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 86aa0775-824d-3e53-957b-e1092509b58e | -2.83976 | -54.04108 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| db0515c1-a21e-34ba-b2ec-362723beb651 | -2.11565 | -50.62689 | 2024-11-29 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3f87788e-f797-3e3f-a022-a592d1dfe655 | -3.34526 | -50.5166 | 2024-11-29 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f8523f9d-761d-3664-8336-4315d8d83f5b | -3.09557 | -54.03904 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5cf1dd18-2b5d-3f28-8728-9cd439cb490a | -4.08525 | -54.34278 | 2024-11-29 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3ccd2bbb-810b-352c-8551-112e2f55783c | -2.98286 | -53.88717 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7c1d0dd0-ce3a-3ba9-87c9-390c6560f4fc | -1.33731 | -51.42938 | 2024-11-29 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2e29c813-90a2-38fe-807f-921d8feef866 | -2.05235 | -53.46354 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 01e39a91-d5ba-318a-9214-9d7c548d3660 | -4.08712 | -50.73469 | 2024-11-29 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 181df0a6-e98a-36ae-8abe-f9296b66c91d | -1.14689 | -48.34202 | 2024-11-29 04:57:00 | NOAA-21 | BELÉM | PARÁ | Brasil | 1501402 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6e9db517-35ee-3e84-b295-d74e0699c47c | -2.87266 | -54.00385 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 01ee424d-7826-3ce5-a8e3-ea87772d5ecb | -1.45665 | -51.49614 | 2024-11-29 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 522ddb3e-d3ac-37b7-a592-0b76416b7339 | -1.18411 | -53.88383 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6fc7fb04-3cbb-3640-a015-b5b9022cb986 | -2.61075 | -54.00494 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 78555f1b-f525-34cb-9d4a-3c41fdad78de | -5.10969 | -44.77605 | 2024-11-29 04:57:00 | NOAA-21 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dc8d7477-04e0-3906-93de-05a3bcc47a5e | -2.84161 | -54.09427 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3277df69-b68c-3541-9bfb-7a02b15d7a9b | -3.39387 | -54.28368 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dd2107a7-5be0-3b58-9ac0-ae56d37ae1ea | -3.25862 | -53.27585 | 2024-11-29 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 93802546-2f65-38dd-8c8d-31b3949dc6ab | -1.25754 | -53.37086 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a348cbe4-2d99-3d82-af62-5c558f4cf784 | -1.43204 | -53.7989 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ccd4d693-764b-372e-894f-0cbbd8a3325b | -2.95696 | -53.87966 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 820d9050-3bfc-3c1e-b079-c0090b8f2d1c | -1.30205 | -55.73997 | 2024-11-29 04:57:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 0ec36424-6e75-3372-a6dd-7c0eee9ce49f | -1.28116 | -52.17087 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d072b4f1-766e-3ba6-9c34-3e32cdd12469 | -2.97092 | -53.28733 | 2024-11-29 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| b2431887-0087-3c3d-897a-7b8a92101adb | -3.25578 | -53.64161 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 6977b84d-a0cf-3597-bbf4-fcea1489e422 | -3.12152 | -53.26127 | 2024-11-29 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 40655ba4-78d5-3ad0-b5ac-7913201c1a10 | -3.17159 | -53.63918 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 22fe5435-8d0f-33d4-bc1e-de22aef59916 | -1.46211 | -54.49846 | 2024-11-29 04:57:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0e820fe6-3ed4-389b-b11d-91fd08780aaa | -1.32449 | -52.80763 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a8aa35ca-9919-3b32-8508-fae4b4d06ddc | -1.39009 | -53.63029 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 40f4d59e-7f34-3cf7-a1ad-53b2ac91e750 | -1.61527 | -52.44837 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 92d5cbc7-b8b7-3889-bb17-1598a1fb899d | -3.47679 | -49.92373 | 2024-11-29 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 75ecaa72-1da2-38c8-a972-2d0b7146b2c9 | -2.20256 | -52.04374 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ffb232be-6193-38f0-b013-a6ebe04a696e | -2.86927 | -53.98219 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| f32443e2-a584-36cc-aac8-af211ec1ef51 | -4.04635 | -46.83265 | 2024-11-29 04:57:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d986ec0a-6cff-3dd7-aeff-86c1d7b756e2 | 0.94216 | -50.74084 | 2024-11-29 04:57:00 | NOAA-21 | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 9bf97c75-a6d3-32e6-be6f-4dc321143f06 | -1.42789 | -55.27995 | 2024-11-29 04:57:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 17e18104-45d6-3319-a5b6-5e2da448e6e5 | -3.27586 | -50.64694 | 2024-11-29 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ab1fb14e-b6e0-3ac4-a95a-1735d225d240 | -4.25839 | -42.60992 | 2024-11-29 04:57:00 | NOAA-21 | MIGUEL ALVES | PIAUÍ | Brasil | 2206209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1b2f0926-de0b-3eaa-a5c7-8b5601ff2f5e | -1.66317 | -52.51284 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 94a211a1-0de7-39c8-9046-b53f85577462 | -1.56724 | -55.26337 | 2024-11-29 04:57:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2db783df-8dae-3330-8acd-3a777f1379a4 | -1.12235 | -51.90356 | 2024-11-29 04:57:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bec6f1d9-9b3d-3964-831d-8e8e480e1020 | -1.78739 | -52.74216 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 07311ce6-00c8-349f-8369-dd13032eb20e | -1.10853 | -53.38577 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8723a517-c29f-3fe6-a237-5ad91298b75c | -2.24831 | -53.62446 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d685318d-85ff-32eb-8c19-db11d085167b | -2.00561 | -51.17037 | 2024-11-29 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f48217fa-2b65-329e-aeb0-73b6d83772fa | -1.88116 | -53.31703 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| effa7c88-186a-3333-81c6-4d98fb947817 | -2.82953 | -54.10653 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 842c39f6-a3eb-386b-9b69-71cf579f2435 | -3.22714 | -54.0666 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 70834b83-902b-3423-a9e1-c537a52da0e6 | -2.58674 | -54.24517 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 06011c36-31f7-3dcf-84fb-6fec224152c5 | -2.95093 | -48.33988 | 2024-11-29 04:57:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1f19a552-d93a-3f99-b939-18a3281ef0dd | -3.26225 | -50.09707 | 2024-11-29 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a0d9dbba-d119-3fae-b365-658634f2d984 | -1.07926 | -53.3567 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a878eee3-e7ef-35f6-b1f1-3dae247a0ae4 | -1.69786 | -52.52945 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b30372c0-1c98-351d-8835-7c8020333526 | -3.69122 | -50.23176 | 2024-11-29 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b798d282-6d12-3123-945a-477b99218cf6 | 1.29529 | -60.41578 | 2024-11-29 04:57:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3dd2ed5b-b18b-3ebc-a6c3-a443530fe079 | -3.46683 | -50.52913 | 2024-11-29 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 36601312-3bb8-3e17-9ac5-b882910abbf4 | -2.73864 | -54.03527 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ce9e5804-8a24-36cb-bfdd-64521b5918a9 | -0.99781 | -51.71643 | 2024-11-29 04:57:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e67cfaa2-8b45-3515-abfc-60045de85dcd | -1.23784 | -51.61655 | 2024-11-29 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dd387a7f-fdcc-3860-a7be-6a544ffd628f | -3.44073 | -50.00993 | 2024-11-29 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 96bc5f66-0aef-3417-a7f4-57a8034a748b | -1.32762 | -51.91704 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8c85b5e3-35fd-37cb-9454-77b7a7734407 | -3.10301 | -53.26892 | 2024-11-29 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b9a62981-cae7-33ce-8581-82b9c211fed1 | -2.38245 | -54.35531 | 2024-11-29 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 49c57e62-5167-39bf-9006-789b732ae72f | -6.09848 | -43.96398 | 2024-11-29 04:57:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| add2d36f-8b44-3cf0-aa2e-00157abc3f7c | -5.75668 | -43.40043 | 2024-11-29 04:57:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |


[Clique aqui para ver as próximas entradas](README67.md)
