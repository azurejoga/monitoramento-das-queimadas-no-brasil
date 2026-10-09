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

## Dados Diários - Página 48

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0b29b3eb-25ca-3947-8eb8-53524fb4d4c4 | -6.1217 | -53.0584 | 2026-10-09 01:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 36.8 |
| 1dfdd124-bae3-3106-9630-c3400a7ab1d6 | -11.7601 | -61.0743 | 2026-10-09 01:20:00 | GOES-19 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 59.8 |
| fb81d7e9-93e8-316b-9b0b-a788285de95d | -3.5677 | -54.6746 | 2026-10-09 01:20:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 83.0 |
| 9c413995-d348-38d2-9cbe-0351f246b70c | -6.0207 | -40.982 | 2026-10-09 01:20:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 64.7 |
| 3eef5b97-1f84-3ff9-a42b-aec6cbe4705e | -3.1971 | -50.5801 | 2026-10-09 01:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 83.9 |
| ff80b68a-881a-36de-a62e-11ff2d6acb83 | -3.5676 | -54.6946 | 2026-10-09 01:20:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 111.6 |
| 8326942e-cd9a-3cee-a6d9-833325e9bb30 | -3.0002 | -54.0684 | 2026-10-09 01:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 649ff707-5113-3fb4-b787-96387ea267cf | -13.1663 | -43.2913 | 2026-10-09 01:20:00 | GOES-19 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 71.8 |
| 5c4cae94-79a4-39c0-8dae-280d9c96327a | -5.9587 | -55.3448 | 2026-10-09 01:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 51.5 |
| 2c6b4eb0-806e-3916-b0da-0bc7eb82376d | -5.7119 | -53.4658 | 2026-10-09 01:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 276be2aa-40d8-3b0a-8f55-1e79d0a581e6 | -3.1285 | -54.1657 | 2026-10-09 01:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 142.4 |
| 7770aac4-da00-3a40-af91-e2a887ff2c12 | -6.8907 | -45.8988 | 2026-10-09 01:20:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 52.7 |
| cc071ca5-f37d-3fc6-964f-8866b071ce08 | -7.2182 | -55.1416 | 2026-10-09 01:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 78.0 |
| 273acec6-a022-31b4-94a2-a0f9f2a09717 | -9.6867 | -58.0865 | 2026-10-09 01:20:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 45.2 |
| 55b896b3-2782-35ef-a3d1-9a4f341da3fb | -15.4287 | -43.2373 | 2026-10-09 01:20:00 | GOES-19 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 108.6 |
| 78194e86-2111-3f15-b5d1-e6c3a88021d7 | -4.2767 | -49.1029 | 2026-10-09 01:20:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 87.7 |
| 85b00d37-7547-3202-a530-9cf5f4dc2cc9 | -5.7119 | -53.4658 | 2026-10-09 01:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 68.1 |
| 9b2545d6-1941-37f4-b627-5fbfc6349503 | -13.1668 | -43.2673 | 2026-10-09 01:30:00 | GOES-19 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 115.9 |
| 44eb103c-18ae-369c-bf26-75c3a459ced5 | -5.7117 | -53.4862 | 2026-10-09 01:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 96.1 |
| 40bd57b9-8d75-351b-b073-1b12ed030c09 | -7.4442 | -63.5589 | 2026-10-09 01:30:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 48.9 |
| 464a030f-691d-3bfc-a50f-4e07683299d7 | -12.0058 | -43.464 | 2026-10-09 01:30:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 80.3 |
| ab0cbd56-9bc8-342c-8fc4-107d05e4ff0d | -3.5493 | -54.6752 | 2026-10-09 01:30:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 87.7 |
| ddc0c5f8-180c-3c60-8b56-c6fab2f23f54 | -5.6934 | -53.4667 | 2026-10-09 01:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 78254ad0-1c06-369a-8994-26e030e5886e | -4.2768 | -49.0816 | 2026-10-09 01:30:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 73.5 |
| e3d8929b-b519-311a-bf0e-ca12e206f71b | -10.6199 | -60.4852 | 2026-10-09 01:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 35.7 |
| 898dc6da-d654-3ef5-8afd-9fbd78bce411 | -7.2187 | -55.0815 | 2026-10-09 01:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 816bc6d9-c7e6-3ca0-9f74-9d6f805dc22c | -13.1636 | -54.3591 | 2026-10-09 01:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 69.4 |
| e1424cda-a508-3d5a-942f-1b039a9d8af4 | -13.1639 | -54.3385 | 2026-10-09 01:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 79.8 |
| fc9a2c3b-2630-370e-9759-0ad4f9676e50 | -8.9107 | -45.2519 | 2026-10-09 01:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 124.2 |
| d933d703-7452-32c6-b877-a12214d6c18f | -5.9833 | -40.961 | 2026-10-09 01:30:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 70.3 |
| e70c4cf0-9eaf-30a3-a39c-e93ad6d7e382 | -6.4903 | -62.8554 | 2026-10-09 01:30:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 81.1 |
| 8452d34c-65e6-38db-b215-01a3af8070c6 | -6.1402 | -53.0574 | 2026-10-09 01:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 36.7 |
| 7ac55ebc-a194-3a16-aa4c-4c15a6f858cb | -15.4287 | -43.2373 | 2026-10-09 01:30:00 | GOES-19 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 81.3 |
| 46b80f31-e4bd-36ac-8fe2-6a7a2686773e | -3.9912 | -59.356 | 2026-10-09 01:30:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 64.5 |
| 24901784-5f4a-3cc7-8bd5-9ddcad302426 | -13.1663 | -43.2913 | 2026-10-09 01:30:00 | GOES-19 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 94.6 |
| 444f1b26-0692-30c3-a537-0e027ae7f16a | -12.2156 | -57.1087 | 2026-10-09 01:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 76.2 |
| da8a7e73-61c6-32a0-aef3-9bc3f8187da2 | -7.1994 | -55.1827 | 2026-10-09 01:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 59.1 |
| cde3ac59-9246-3702-8c01-45bab9cd5fa5 | -7.2182 | -55.1416 | 2026-10-09 01:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 71.1 |
| af1d6c19-0da5-3bf5-a900-0e20ca9983ae | -3.1114 | -53.7839 | 2026-10-09 01:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 78.1 |
| 16a6d853-f7aa-3f0b-8cce-2f1191c579c6 | -7.2367 | -55.1406 | 2026-10-09 01:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 61.6 |
| 26df7bb4-6ce1-3d48-9b8a-dd464f055161 | -13.1827 | -54.3571 | 2026-10-09 01:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 93.5 |
| d6302abb-f09b-3c01-b7a3-13aa3cdd0d0d | -3.0925 | -53.9455 | 2026-10-09 01:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 84.1 |
| 5e1b0c74-f686-3487-bdf6-ee3c8d636460 | -3.0007 | -53.9075 | 2026-10-09 01:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 99.4 |
| 65bdb94b-eb1c-318d-98c6-1a19142a4d25 | -8.7234 | -45.1355 | 2026-10-09 01:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 199.8 |
| d4b3e73b-7d84-3573-a31d-184d44b8df6d | -9.7054 | -58.0854 | 2026-10-09 01:30:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 38.4 |
| 2452d17b-707e-3cd0-8056-cd1dec212962 | -3.1787 | -50.5597 | 2026-10-09 01:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 41.6 |
| 12c2772d-75e4-3e28-9857-260be13fe3b5 | -5.9587 | -55.3448 | 2026-10-09 01:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 50.5 |
| 9cef221f-2ddd-3235-83ab-81a16a0dda37 | -3.4396 | -54.5382 | 2026-10-09 01:30:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 4b5cb277-f568-35f8-b456-70d6d7f3b119 | -3.11 | -54.1862 | 2026-10-09 01:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 76.4 |
| 5b3ae558-2a2b-3981-a367-4c4f4b53f0e9 | -4.6282 | -49.2147 | 2026-10-09 01:30:00 | GOES-19 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 68.5 |
| 1d233ae3-452e-37de-b6d4-5b19bfc7b53f | -8.8918 | -45.2539 | 2026-10-09 01:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 140.1 |
| eafa76dc-b5cf-3be5-be54-4144e12cbb6a | -3.1971 | -50.5801 | 2026-10-09 01:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 67.0 |
| eed4a23e-0eac-311e-9c20-4ab6bd3786e5 | -3.1101 | -54.1661 | 2026-10-09 01:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 92.4 |
| 4c7ff0b3-9bcc-39ce-aae3-8e2f4f00d681 | -8.7423 | -45.1334 | 2026-10-09 01:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 419.5 |
| 026463e3-aa2a-3de8-8e7f-b484b70a2a28 | -12.2154 | -57.1287 | 2026-10-09 01:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 35.7 |
| 704c371b-3dfd-3b2d-a9a1-aef0ade99c4e | -8.911 | -45.229 | 2026-10-09 01:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 168.0 |
| 71ef9548-8bf6-3e83-9be4-9905f4673d9e | -3.364 | -50.4072 | 2026-10-09 01:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 75.6 |
| 3fd58160-b480-3736-83b0-50dfb31723fb | -3.5676 | -54.6946 | 2026-10-09 01:30:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 105.4 |
| 25802b72-d7a0-34c4-a637-4a7ef7545b88 | -7.5649 | -61.5523 | 2026-10-09 01:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 6151d7c3-729a-3031-aefa-3f3e86740e67 | -3.1284 | -54.1857 | 2026-10-09 01:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 85.0 |
| 1448ce6f-e8db-39fa-a158-ea7e91010c61 | -8.7231 | -45.1583 | 2026-10-09 01:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 179.8 |
| 66f078fe-4aed-3926-bc60-4e1e62801075 | -3.1285 | -54.1657 | 2026-10-09 01:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 127.6 |
| 20b00ae0-52a0-32eb-9d71-8c764ab7a971 | -8.742 | -45.1563 | 2026-10-09 01:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 281.3 |
| 8c04a8b3-caee-3e64-a318-f6d7a38d821d | -12.2346 | -57.1071 | 2026-10-09 01:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 78.4 |
| 73709836-23fc-3c5a-8dcb-fb6ebac44ada | -3.1879 | -58.6433 | 2026-10-09 01:30:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 49.8 |
| 23abcbac-88cc-3fa5-b82a-f925050e7258 | -5.6932 | -53.487 | 2026-10-09 01:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 50.6 |
| 33b9bc0d-e405-3393-94be-875e34cdffa3 | -3.5493 | -54.6951 | 2026-10-09 01:30:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 114.1 |
| e1644c64-44e2-31be-acef-621dca7d5141 | -11.47 | -43.3824 | 2026-10-09 01:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 70.5 |
| 95b71ec8-c824-38a2-8d85-648da445dec0 | -13.2018 | -54.3551 | 2026-10-09 01:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 68.0 |
| 13edbbd0-bd96-3fdd-80a4-65d9d101b0e0 | -4.2953 | -49.1021 | 2026-10-09 01:30:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 519eea8b-24a8-3e25-8169-85e2f2a81d8d | -7.1995 | -55.1627 | 2026-10-09 01:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 136.3 |
| a58cca17-c72b-320f-9902-5020bfa1f984 | -3.1109 | -53.945 | 2026-10-09 01:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 94.6 |
| da35ba84-6676-31ee-a0ae-7fe88c1ab238 | -12.2158 | -57.0887 | 2026-10-09 01:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 36.2 |
| 2ff3f91e-a621-3df7-ad43-d530df84ae05 | -4.6096 | -49.2156 | 2026-10-09 01:30:00 | GOES-19 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 80d78bfb-be33-3bfd-95a7-28fde0936370 | -3.3455 | -50.4078 | 2026-10-09 01:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 74.4 |
| ae7f4455-b2f2-3388-a782-0abe90852d09 | -6.0207 | -40.982 | 2026-10-09 01:30:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 136.6 |
| 4e0e27a8-7b2d-3270-8931-d062b443ef58 | -6.021 | -40.9577 | 2026-10-09 01:30:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 199.6 |
| ed252689-e424-38c1-8c4f-999515a9fa12 | -3.1786 | -50.6016 | 2026-10-09 01:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 115f3967-b3d5-31ca-9444-6a792b133fdc | -6.0019 | -40.9837 | 2026-10-09 01:30:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 431.4 |
| 89a77718-775b-3310-826f-b0ad8f823aaa | -3.1787 | -50.5807 | 2026-10-09 01:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 124.5 |
| 3944ecbe-0c29-367a-ac46-175ef3fe70f2 | -12.2348 | -57.0871 | 2026-10-09 01:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 30.9 |
| f3d115c4-db02-39d6-aad1-67ca75fe3a9d | -6.8719 | -45.9003 | 2026-10-09 01:30:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 54.6 |
| b36c3e95-4ccf-31db-9ecb-4cfe0e409aed | -6.7365 | -55.1474 | 2026-10-09 01:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 64.4 |
| 7463b724-04dd-3192-b7f9-a3902fcce955 | -7.218 | -55.1617 | 2026-10-09 01:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 116.7 |
| a3fb6d50-1553-3aa4-b9fb-133ef4e1d518 | -11.6562 | -43.6846 | 2026-10-09 01:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 128.8 |
| a8981ada-3a51-30f0-9ef8-dcf35a588512 | -8.9113 | -45.2062 | 2026-10-09 01:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 48.2 |
| 6087f597-bc79-3db5-b9eb-c3e7e1b77a49 | -6.0024 | -40.935 | 2026-10-09 01:30:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 188.6 |
| ef566578-899e-3dd6-89da-4c957b090357 | -2.499 | -56.0675 | 2026-10-09 01:30:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 68.7 |
| a6767e46-70c5-390e-b9e6-81c6fee45cb8 | -3.2577 | -54.0217 | 2026-10-09 01:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 58.5 |
| dfe78823-04d9-38be-8828-0b20fb6bf7cd | -8.8921 | -45.2311 | 2026-10-09 01:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 113.2 |
| dae715f3-aa15-3aa0-bef6-b698459ab875 | -4.2954 | -49.0807 | 2026-10-09 01:30:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 99.9 |
| 358b755c-fb87-3321-b0e3-d65a8258d2b7 | -6.0021 | -40.9594 | 2026-10-09 01:30:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 757.8 |
| a2db35c0-704e-3a9d-9c0d-b1cfe9225ff3 | -2.7428 | -54.1146 | 2026-10-09 01:30:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 78.0 |
| 899bff4a-4c75-31d6-8d8a-588d42c2314e | -13.2015 | -54.3757 | 2026-10-09 01:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 54.8 |
| 25a3a74e-040e-399d-8871-7c4a30959da8 | -11.014 | -45.4272 | 2026-10-09 01:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 71.5 |
| 7814364f-5487-34b1-8133-50d22c9670a4 | -6.8907 | -45.8988 | 2026-10-09 01:30:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 54.2 |
| f5e2fa12-8523-3b1b-bd8d-a81e09bed421 | -3.5677 | -54.6746 | 2026-10-09 01:30:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 87.8 |
| 6c6b359d-4766-30bf-a0e0-f425e23013b2 | -11.6562 | -43.6846 | 2026-10-09 01:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 100.1 |
| dd61346d-6ec1-3da2-992c-ee69b1feb875 | -2.7428 | -54.1146 | 2026-10-09 01:40:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 69.0 |
| 3807fe2d-f4e5-3d06-aafc-9e8c10a8427d | -10.6199 | -60.4852 | 2026-10-09 01:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 44.1 |


[Clique aqui para ver as próximas entradas](README49.md)
