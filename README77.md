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

## Dados Diários - Página 77

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 61b601bf-0649-3475-80d7-90b59525594c | -6.13192 | -47.00564 | 2024-10-26 04:44:00 | NOAA-20 | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9aa2c2e8-c18f-332d-ba2e-268021bf3c8b | -6.08694 | -46.91894 | 2024-10-26 04:44:00 | NOAA-20 | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 76457bb8-d9c9-37e4-be3d-8c9cf31864ed | -6.08339 | -47.22475 | 2024-10-26 04:44:00 | NOAA-20 | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 32cea12c-0939-3790-b786-2abcae27ba6b | -5.99607 | -47.08496 | 2024-10-26 04:44:00 | NOAA-20 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e2505150-f070-3fab-be7e-3f6aa72f4036 | -5.85234 | -47.19374 | 2024-10-26 04:44:00 | NOAA-20 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ad893b9e-b3eb-382b-ac5c-dbab2aa233e3 | -5.84579 | -47.28749 | 2024-10-26 04:44:00 | NOAA-20 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f229f5bd-296d-3799-9ecf-febf0fb3c12f | -5.84209 | -47.28695 | 2024-10-26 04:44:00 | NOAA-20 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4cbcc115-2f0f-3fe0-a96f-cc944f2f7a47 | -5.83002 | -47.19042 | 2024-10-26 04:44:00 | NOAA-20 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 52c453ff-3a10-39a2-8d43-92f561b47964 | -5.74879 | -47.03378 | 2024-10-26 04:44:00 | NOAA-20 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1a828c08-87bc-3d7c-b9c7-38fe0d42b60b | -5.71435 | -47.11122 | 2024-10-26 04:44:00 | NOAA-20 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 63701599-fd09-3a98-b3f8-4713d79cd123 | -5.66613 | -46.99117 | 2024-10-26 04:44:00 | NOAA-20 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a1e28a00-6855-3627-9ba2-4991814a022d | -5.64925 | -47.9157 | 2024-10-26 04:44:00 | NOAA-20 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6713bc32-f1e6-37ae-b69f-06fcb93a354c | -5.55598 | -47.02788 | 2024-10-26 04:44:00 | NOAA-20 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4dcb8832-127c-309c-ab72-483a7f9aa773 | -5.5553 | -47.03241 | 2024-10-26 04:44:00 | NOAA-20 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 54eb9260-58a6-3de2-8d98-eef0c39b9caa | -5.46433 | -47.09433 | 2024-10-26 04:44:00 | NOAA-20 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a1d8735a-9b40-304d-8dbb-265e81df55bc | -5.85426 | -46.56299 | 2024-10-26 04:44:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b653f415-0858-3d2f-8955-a1c3832f2ed0 | -5.76574 | -46.5374 | 2024-10-26 04:44:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 5be29fbe-12fa-3101-966d-3a980dd1035b | -5.44938 | -46.45425 | 2024-10-26 04:44:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9a1f5f9e-4334-3395-8e86-4dfff2a0b7b8 | -5.4347 | -46.551 | 2024-10-26 04:44:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 76e6f004-9b78-39f0-94c4-f102b02f6ad3 | -5.43398 | -46.55578 | 2024-10-26 04:44:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9ddf1eb4-ea09-367b-ba40-e7c5a3a7684f | -5.24478 | -46.67916 | 2024-10-26 04:44:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5945e0dc-2cef-35d9-8964-fc2546392272 | -5.2327 | -46.68202 | 2024-10-26 04:44:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5a0850a3-ca0a-3f80-8d01-443fa131cfd1 | -5.22958 | -46.67685 | 2024-10-26 04:44:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 188cecb3-272c-3bce-8b75-42395c407429 | -7.96405 | -47.03748 | 2024-10-26 04:44:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6ad01a9e-6575-34bb-8859-ad00e99ef69f | -7.67182 | -47.31223 | 2024-10-26 04:44:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9b21e1de-6202-3f81-a26c-1f6d5b4da0be | -7.67114 | -47.31685 | 2024-10-26 04:44:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 98d8a775-0929-3552-b870-780c7763cbba | -7.66804 | -47.31165 | 2024-10-26 04:44:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e584a4e8-3c99-3d68-bb7c-025d31ff500c | -7.66736 | -47.31627 | 2024-10-26 04:44:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 475bb4d1-1700-34f6-9ea0-8bcdc1031e62 | -7.66358 | -47.3157 | 2024-10-26 04:44:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 753997fc-f929-3815-8979-34a77fda0861 | -7.652 | -47.52385 | 2024-10-26 04:44:00 | NOAA-20 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d3231dd0-aaf4-36e3-99a1-9cf0378a4620 | -7.59722 | -47.0846 | 2024-10-26 04:44:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9905ec03-e09a-3d83-95d7-8e48f6b13ee6 | -7.58471 | -47.11655 | 2024-10-26 04:44:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7d15a8a6-f037-3681-964d-2e00bb5697a7 | -7.58089 | -47.11598 | 2024-10-26 04:44:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fc448756-197d-3a5f-b35a-36321f20dcd5 | -7.48975 | -48.08298 | 2024-10-26 04:44:00 | NOAA-20 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5ade5fd0-8f74-32e2-afd6-e51975103275 | -7.47913 | -47.35904 | 2024-10-26 04:44:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8ee37ad3-07da-35ae-9f31-222fe307a2c2 | -7.44894 | -46.91621 | 2024-10-26 04:44:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 406624eb-0374-349e-b604-81d295e1d5f2 | -7.44057 | -47.38591 | 2024-10-26 04:44:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a1f3cdc4-4ea6-391a-a5c7-591c9f8e1005 | -7.35924 | -46.99118 | 2024-10-26 04:44:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 32787aeb-0c17-3492-b1b7-aae47a2136ee | -7.28549 | -47.17977 | 2024-10-26 04:44:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c3dc7663-cd5c-3022-b2da-9baa80529efb | -7.28479 | -47.18447 | 2024-10-26 04:44:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 69ae8cc2-486e-3d06-93e8-4b1653c8ce7b | -7.2475 | -48.0063 | 2024-10-26 04:44:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e766e93b-f7c8-3720-822a-9b2ff3ede7f1 | -7.15227 | -47.86814 | 2024-10-26 04:44:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 85d0fc2c-f4de-36a2-b2a4-5e86134bb2d2 | -7.07064 | -46.87881 | 2024-10-26 04:44:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d82e8860-68e8-3980-a9c9-baed930f82a0 | -7.0675 | -46.87337 | 2024-10-26 04:44:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 398d12aa-0aff-3aed-b6bf-1843fa2f658c | -7.01765 | -47.97016 | 2024-10-26 04:44:00 | NOAA-20 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8aef4d5e-6ad8-39a3-b30b-972a694a0770 | -6.92257 | -46.84211 | 2024-10-26 04:44:00 | NOAA-20 | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d0e0518b-54ec-33a1-8e55-f92cb1b7fbbd | -6.60662 | -47.34707 | 2024-10-26 04:44:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 90b4d461-cef4-341d-9cef-8342016cf873 | -9.04768 | -48.72261 | 2024-10-26 04:44:00 | NOAA-20 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6e6ce06c-f2ca-34ae-ad15-d203d83a44f0 | -8.90251 | -48.53556 | 2024-10-26 04:44:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 517ac3d4-a174-3e66-87ae-542140073b10 | -8.89174 | -48.53391 | 2024-10-26 04:44:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3c71ccc2-12c2-3aa6-a8c6-1fae4f336daf | -8.64927 | -48.58426 | 2024-10-26 04:44:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 1.3 |
| defc80a7-6100-3fe0-a99e-eda5cf84319c | -9.26633 | -47.90977 | 2024-10-26 04:44:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7a012970-43ae-392d-a9ff-48afe68cc463 | -9.26456 | -47.91163 | 2024-10-26 04:44:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bb648c17-d93c-364a-99c0-d253b28c6bf0 | -9.2626 | -47.90924 | 2024-10-26 04:44:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7c46bd1a-7943-306d-a869-658f70309f1a | -9.1022 | -47.65288 | 2024-10-26 04:44:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1ce60490-9315-3985-b813-97e48845746a | -9.0779 | -48.00465 | 2024-10-26 04:44:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0769e940-c11f-3aef-aa8b-d5f4345287bb | -9.0742 | -48.00412 | 2024-10-26 04:44:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 98dae95f-7162-320d-9cc6-782c2929604b | -9.07355 | -48.00856 | 2024-10-26 04:44:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 89d35810-da39-3560-9f18-cd2760ff6f70 | -9.0705 | -48.00359 | 2024-10-26 04:44:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 86f10feb-7028-3ed2-83e6-39be4b544bce | -9.06985 | -48.00804 | 2024-10-26 04:44:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5274ab5d-4850-3681-becd-fa69e4e55a16 | -9.0668 | -48.00307 | 2024-10-26 04:44:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d51cc6b0-a05d-3c6f-8c59-50dbb5a918f5 | -9.06615 | -48.0075 | 2024-10-26 04:44:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7cf51d51-af81-3acf-9614-573fd657f43b | -8.97652 | -47.74881 | 2024-10-26 04:44:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c394292b-fc98-3e64-9158-987e615f530e | -8.97329 | -47.66424 | 2024-10-26 04:44:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d6330fff-227d-3a21-95e9-57390a56855b | -8.97244 | -47.66604 | 2024-10-26 04:44:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c9e8b651-8ac4-32c5-8e0f-294c019f23d5 | -8.80469 | -47.86085 | 2024-10-26 04:44:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0f629c65-63b3-3063-9d7d-6c6f1c1e0f6f | -8.80097 | -47.86032 | 2024-10-26 04:44:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8c3ee3f7-2459-39f9-a79c-70a78067f4f7 | -8.47164 | -47.81287 | 2024-10-26 04:44:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 133b4d67-7e44-312f-a8a2-fad030b48f6b | -8.47097 | -47.81735 | 2024-10-26 04:44:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9799e36e-f06c-335b-b933-c588ac927e30 | -8.46793 | -47.81229 | 2024-10-26 04:44:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5b5544f7-3a28-369c-924c-0e0578f7f256 | -8.46727 | -47.81676 | 2024-10-26 04:44:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4c8c7300-ce71-3555-b024-ecceeb1857a1 | -9.26829 | -47.91216 | 2024-10-26 04:44:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 67fdcb27-106d-3dc7-b6b1-f1a04c3eb927 | -9.0548 | -48.72374 | 2024-10-26 04:44:00 | NOAA-20 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6f7a7473-12b0-32d9-8c49-fa2c46d5dee3 | -9.05124 | -48.72318 | 2024-10-26 04:44:00 | NOAA-20 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 41475b0b-cef2-3131-8b9f-068398f246af | -8.90547 | -48.54031 | 2024-10-26 04:44:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c991c416-ceb2-3c4f-8bdb-fbfc833cc62a | -8.90188 | -48.53975 | 2024-10-26 04:44:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1b03c7e7-bec9-3991-a1ba-a80d2f788611 | -8.89533 | -48.53445 | 2024-10-26 04:44:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 9.0 |
| b4aa191b-92d0-3fc0-b63d-f44dacdd03d1 | -9.93553 | -48.70246 | 2024-10-26 04:44:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a44c4ff7-8b98-33df-8341-1aff6a743646 | -9.39161 | -48.76694 | 2024-10-26 04:44:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 29909f5e-3b2b-363d-8b7a-ecd6a14b4500 | -10.28703 | -48.89505 | 2024-10-26 04:44:00 | NOAA-20 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 391f1fb8-4e9e-3f2c-9982-cc83b193b182 | -9.81568 | -47.85006 | 2024-10-26 04:44:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 3aad0910-483f-3a69-a17b-933a7bb8aa45 | -9.81502 | -47.85471 | 2024-10-26 04:44:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 6ba48966-01c6-35af-8d2e-772a92149736 | -9.81483 | -47.8519 | 2024-10-26 04:44:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| b86ed0c8-29af-3eaf-ae05-c68a9017a743 | -9.81415 | -47.85651 | 2024-10-26 04:44:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 4a8d0232-8dea-3e83-985b-2d9038bfdb57 | -9.81126 | -47.85414 | 2024-10-26 04:44:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d412cf76-b259-3bdf-9dfd-4ba29c381dfa | -9.80952 | -47.59788 | 2024-10-26 04:44:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4e649dd0-ef3b-3130-8c43-e6459a6d63b8 | -9.8057 | -47.59733 | 2024-10-26 04:44:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 22f32a83-a60a-398f-91a7-78eb60efc9e4 | -9.73422 | -48.26651 | 2024-10-26 04:44:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fa92467d-3b0b-358c-894b-1d9d7419d0aa | -9.72254 | -48.26927 | 2024-10-26 04:44:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4aa64ee2-c37e-3b5a-b08b-c03c0149962d | -9.50377 | -47.81562 | 2024-10-26 04:44:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b069367f-b9ac-39ea-8243-e17d60a452df | -9.50066 | -47.81054 | 2024-10-26 04:44:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fdb3a03f-1163-3ab3-9a97-529cfe621525 | -9.5 | -47.81512 | 2024-10-26 04:44:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| cd0884d8-49cc-3da2-aa2a-5aac8ad2c992 | -9.49624 | -47.81461 | 2024-10-26 04:44:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f30ba6e5-01a7-3fb1-a65b-930caf3257a0 | -9.49183 | -47.81865 | 2024-10-26 04:44:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c70c672a-dc27-34ee-9bd6-8402924f5143 | -9.49157 | -47.81622 | 2024-10-26 04:44:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c744a5cd-e432-31e3-88f3-9937f97943f5 | -9.48807 | -47.81808 | 2024-10-26 04:44:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 721745f2-d4e7-3fde-aaa7-3b0fd5c40d66 | -9.48782 | -47.81567 | 2024-10-26 04:44:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| be10e9c8-cc9a-3c1c-a987-7987caa8aa8e | -10.43803 | -48.08971 | 2024-10-26 04:44:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 03fac2e4-f4fb-32e3-a471-8cd8ca6c5b60 | -10.30959 | -47.79909 | 2024-10-26 04:44:00 | NOAA-20 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 3b5413ea-af40-32c7-95d7-c05d596a2e9b | -10.30647 | -47.79375 | 2024-10-26 04:44:00 | NOAA-20 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |


[Clique aqui para ver as próximas entradas](README78.md)
