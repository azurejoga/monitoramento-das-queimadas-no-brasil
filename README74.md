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

## Dados Diários - Página 74

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6e5e7f5c-6ba3-30d3-8304-7a87e3a2bd9f | -6.6357 | -45.1752 | 2026-08-25 13:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 357.7 |
| fdf440d0-4a9b-3d01-8a62-031e515c3801 | -8.5775 | -54.8575 | 2026-08-25 13:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 101.7 |
| c0168a0c-b021-361c-b3a4-573c61c4bb23 | -13.8765 | -54.0322 | 2026-08-25 13:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 91.7 |
| 9bdc2c31-a551-3446-a2c4-17e21d70621f | -9.5753 | -49.2367 | 2026-08-25 13:30:00 | GOES-19 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 118.0 |
| 4d732d72-5ca0-3a86-9ebe-f3e5c3728c43 | -6.6359 | -45.1525 | 2026-08-25 13:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 113.6 |
| 7509cbe2-756e-3c49-ade0-5db98c445e1d | -14.7397 | -48.7943 | 2026-08-25 13:30:00 | GOES-19 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 144.5 |
| 9ec46c19-96d5-35db-bf55-7f29fa844c1b | -7.4477 | -43.0928 | 2026-08-25 13:30:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 160.1 |
| fdd37001-3dd0-392f-92ef-c9a77f404261 | -6.641 | -58.4987 | 2026-08-25 13:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 274.7 |
| face908f-9eaa-37e4-81bf-672a8a6c0984 | -6.6409 | -58.5181 | 2026-08-25 13:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 64.7 |
| a4cd5405-eb2c-3b1a-a9de-62a666cd9a4b | -7.0242 | -59.2374 | 2026-08-25 13:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 69.6 |
| c0401103-e5ee-3f73-b86b-92e9e75032df | -3.4167 | -43.3867 | 2026-08-25 13:30:00 | GOES-19 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 83.7 |
| f5a805af-6254-3641-8cd8-276937a20942 | -6.6411 | -58.4793 | 2026-08-25 13:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 68.4 |
| 1bde132d-8121-3169-a875-9b4fc30787b6 | -6.3322 | -54.7473 | 2026-08-25 13:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 77.2 |
| b92dd74a-e67d-31eb-8ec5-0e29b3d303c4 | -8.073 | -47.5287 | 2026-08-25 13:30:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 87.3 |
| 76d58d49-918e-318f-b9cc-6dcd7fdbb009 | -13.3595 | -48.2051 | 2026-08-25 13:40:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 108.6 |
| 4d1c1135-e4eb-3ee5-87a1-edc9507d7b2b | -6.6169 | -45.1767 | 2026-08-25 13:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 196.4 |
| 1f629837-81ea-3cfd-89ad-33be487b7820 | -7.2901 | -45.3683 | 2026-08-25 13:40:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 191.4 |
| a8218491-87cd-3a15-8f5a-45a26917585d | -7.2713 | -45.37 | 2026-08-25 13:40:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 96.1 |
| 39690964-87e5-34ba-ba6d-08b04661ec15 | -6.9873 | -59.2389 | 2026-08-25 13:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 69.5 |
| 5f0e4671-ec6b-30d9-8d30-3ce20d3c1a3c | -7.3089 | -45.3666 | 2026-08-25 13:40:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 82.8 |
| 5cff658c-c851-3005-bfa5-6e856e072b93 | -9.5753 | -49.2367 | 2026-08-25 13:40:00 | GOES-19 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 164.9 |
| f241fc95-a947-3a77-8977-af9d53b09653 | -7.0057 | -59.2575 | 2026-08-25 13:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 120.7 |
| 3006e1a7-53e5-3499-86f8-09c5e4d1e6f2 | -11.9991 | -45.9287 | 2026-08-25 13:40:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 89.1 |
| 8f7a9012-0c44-32d7-8b3b-ca2c2c2d93cd | -6.3322 | -54.7473 | 2026-08-25 13:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 97.1 |
| 82805a23-2700-3ef2-b07d-be207f12c667 | -8.0918 | -47.527 | 2026-08-25 13:40:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 96.9 |
| c6d5f476-be0f-37df-a262-f1a98b5037c0 | -8.5775 | -54.8575 | 2026-08-25 13:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 99.7 |
| e7baa785-04df-3be5-85c2-0e689b690377 | -6.6357 | -45.1752 | 2026-08-25 13:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 321.9 |
| a12688a6-b118-3bae-bf87-0247a84853b9 | -8.6078 | -50.0124 | 2026-08-25 13:40:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 82.6 |
| 1e37511f-753e-3c03-890e-1dffc10c721f | -4.1934 | -54.5755 | 2026-08-25 13:40:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 66.4 |
| 5dcf82a4-da45-33dd-9c80-ba9031591c42 | -7.0242 | -59.2374 | 2026-08-25 13:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 77.3 |
| dd420a74-6f5a-3a78-a08b-e98d46ec5842 | -8.1765 | -46.7007 | 2026-08-25 13:40:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 97.8 |
| ef240a20-7672-3aa0-9ced-de19e7c5b64c | -12.151 | -50.6098 | 2026-08-25 13:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 116.8 |
| 1bbc0399-2bd6-3897-a978-84bfb9cf937e | -3.4167 | -43.3867 | 2026-08-25 13:40:00 | GOES-19 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 83.2 |
| 9f86c7b2-d2f4-3108-9f07-7ea863c9eead | -6.9872 | -59.2582 | 2026-08-25 13:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 157.0 |
| a1c03d8b-5335-3b06-80ad-cdb472e9b918 | -8.0921 | -47.5049 | 2026-08-25 13:40:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 89.3 |
| a1423e7c-b7de-3e87-ac0c-8aa060a9760e | -7.4474 | -43.1163 | 2026-08-25 13:40:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 202.8 |
| 7f8cc77d-3cd5-37c9-a791-834b55216d56 | -14.7397 | -48.7943 | 2026-08-25 13:40:00 | GOES-19 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 83.6 |
| d8f02e8c-f376-3f7f-baa9-879f709b5c7d | -6.641 | -58.4987 | 2026-08-25 13:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 319.7 |
| 47730613-2ba9-3b2c-a353-b1d371c346d1 | -7.4477 | -43.0928 | 2026-08-25 13:40:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 138.6 |
| 583337a7-186e-3ad0-ae6c-f1c7fe962388 | -13.8762 | -54.053 | 2026-08-25 13:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 89.8 |
| 113cce3d-e23b-3fd9-a145-e542076a1993 | -13.3402 | -48.2079 | 2026-08-25 13:40:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 100.9 |
| 9755c82c-22ca-3a3b-a154-f8f20c295fea | -6.6409 | -58.5181 | 2026-08-25 13:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 96.8 |
| 3efbdf94-eec5-3b96-9582-aa6c6ef44174 | -6.6359 | -45.1525 | 2026-08-25 13:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 121.3 |
| 9c7e13ef-70c4-3f84-919a-c644137c13a9 | -7.2715 | -45.3473 | 2026-08-25 13:40:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 85.5 |
| 77d0a43a-f428-354a-a3a2-df415cab5000 | -6.6411 | -58.4793 | 2026-08-25 13:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 87.8 |
| b2a3b761-d0cf-3965-a945-7c829e88ed3b | -6.7107 | -45.169 | 2026-08-25 13:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 111.1 |
| dc43566a-24cc-39e0-a4c0-57a0398deb36 | -13.8765 | -54.0322 | 2026-08-25 13:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 113.8 |
| 794115ed-9ce8-3b0d-baaa-ead6f193e35a | -7.0058 | -59.2382 | 2026-08-25 13:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 101.2 |
| b1302d13-566a-3a2a-90f8-50d78277f5bf | -7.0241 | -59.2567 | 2026-08-25 13:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 75.9 |
| fc7c24e4-8fd4-3ce6-ae63-6a4e843bd74a | -14.7592 | -48.7913 | 2026-08-25 13:40:00 | GOES-19 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 292.6 |
| 14367734-160d-3405-be67-9c0953b8650f | -14.7592 | -48.7913 | 2026-08-25 13:50:00 | GOES-19 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 225.9 |
| b8e5e270-ae7f-3f16-9df8-bee10abac570 | -8.5775 | -54.8575 | 2026-08-25 13:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 95.3 |
| e6d86d83-3201-3e3d-bb51-aef5bd8f3f9b | -4.1934 | -54.5755 | 2026-08-25 13:50:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 62.7 |
| ed6b15f8-5afb-3017-bd1e-f90dcbdd836d | -12.757 | -46.4538 | 2026-08-25 13:50:00 | GOES-19 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 81.8 |
| 0001e273-4689-3404-a9d2-99ab01887885 | -7.0241 | -59.2567 | 2026-08-25 13:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 86.4 |
| 10a257cf-0390-32e3-9555-13686e01b921 | -10.8416 | -50.5646 | 2026-08-25 13:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 81.4 |
| b5087185-9f97-3e50-a274-4df1fcc58b7a | -7.4474 | -43.1163 | 2026-08-25 13:50:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 136.7 |
| c0641bc7-e674-3d07-8977-b0b4ba2ad99e | -7.4694 | -44.4619 | 2026-08-25 13:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 86.2 |
| 1d08b1c4-d2ee-3f2f-9a5a-48dbf4a84721 | -8.073 | -47.5287 | 2026-08-25 13:50:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 83.5 |
| 947dea4e-b204-36f6-9104-c8666482b4bd | -15.1053 | -48.0209 | 2026-08-25 13:50:00 | GOES-19 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 90.1 |
| 3a1c5f1f-f991-3aec-a453-a46e64770751 | -12.151 | -50.6098 | 2026-08-25 13:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 135.4 |
| 3bcba82f-a3ab-382d-b636-121481e8d128 | -6.6227 | -58.4801 | 2026-08-25 13:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 61.5 |
| b4c781e7-4dff-3655-8d2a-06b0a244f7d6 | -13.3402 | -48.2079 | 2026-08-25 13:50:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 97.5 |
| ca8599d9-fa67-3f90-80b6-6ebff4d54736 | -6.3322 | -54.7473 | 2026-08-25 13:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 103.0 |
| 69e12899-b356-3031-bb33-346a81d5cb0d | -8.0918 | -47.527 | 2026-08-25 13:50:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 114.5 |
| 0e05a3e9-e8b8-324d-aedb-5c38484147d7 | -6.6411 | -58.4793 | 2026-08-25 13:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 106.7 |
| 7cf42524-b288-31ed-956e-6eaaef7052db | -6.641 | -58.4987 | 2026-08-25 13:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 384.2 |
| 69fd5fee-70fe-3462-ac0b-a0a55de7ede0 | -14.7787 | -48.7882 | 2026-08-25 13:50:00 | GOES-19 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 131.6 |
| c0b038e3-e4a1-3ceb-ac5a-1abdb7b0afb0 | -13.3595 | -48.2051 | 2026-08-25 13:50:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 111.1 |
| 5b56b245-d0e1-3837-96d4-79a54f56a82e | -7.2901 | -45.3683 | 2026-08-25 13:50:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 176.1 |
| 87deacbb-266d-37ab-9d3f-4f0d37ec976a | -6.1284 | -57.8588 | 2026-08-25 13:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 69.3 |
| 8f10eb1e-0c3c-3c9b-816a-50a41513ae33 | -6.6169 | -45.1767 | 2026-08-25 13:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 173.5 |
| 0426731e-fead-3edc-bb5c-e9bf892a7482 | -14.335 | -51.8517 | 2026-08-25 13:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 89.7 |
| 96d76488-0a7e-3785-80c1-f6e53bfc2a8a | -8.1765 | -46.7007 | 2026-08-25 13:50:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 97.1 |
| 1333b97c-459c-3d1c-8d20-b2eb9c10903d | -6.6409 | -58.5181 | 2026-08-25 13:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 104.7 |
| b03a13cb-4fd5-33c7-bf83-015e788e2628 | -7.0057 | -59.2575 | 2026-08-25 13:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 125.6 |
| 938c84a1-fb6d-3e92-a717-ec576b1e63b8 | -6.8192 | -59.5927 | 2026-08-25 13:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 69.5 |
| bad44135-a58c-372b-bb70-1eda9812af91 | -6.6357 | -45.1752 | 2026-08-25 13:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 271.7 |
| 294991fd-fb86-3439-8e6a-c3fb2c487186 | -7.4477 | -43.0928 | 2026-08-25 13:50:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 117.6 |
| dbce24df-aa58-3f5e-980c-e69642c5f72f | -7.2713 | -45.37 | 2026-08-25 13:50:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 99.1 |
| 6104014f-739b-3411-9132-e7b701ee1395 | -9.5753 | -49.2367 | 2026-08-25 13:50:00 | GOES-19 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 295.0 |
| 22f4d385-0db9-3d49-9932-8793191c5b43 | -6.8008 | -59.5934 | 2026-08-25 13:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 61.1 |
| d6b9988e-0414-3d0f-af2f-04da7a60bdda | -8.6078 | -50.0124 | 2026-08-25 13:50:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 107.7 |
| 58c532d2-f12c-31ea-ab6e-90eba646a042 | -13.8759 | -54.0737 | 2026-08-25 13:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 185.1 |
| da444bc1-8b78-3543-909e-b074cef30847 | -6.9872 | -59.2582 | 2026-08-25 13:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 146.9 |
| f6e0b715-3148-3fdf-9add-edd26434fee1 | -7.0058 | -59.2382 | 2026-08-25 13:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 107.7 |
| b9a39092-8dbc-337b-8f1f-7a8e309b3441 | -7.0242 | -59.2374 | 2026-08-25 13:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 74.6 |
| 47e610a6-858a-3f32-af30-bfa689e275bc | -3.4167 | -43.3867 | 2026-08-25 13:50:00 | GOES-19 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 105.7 |
| 727bcdac-604b-3252-94a8-63a562d3e5d3 | -13.8762 | -54.053 | 2026-08-25 13:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 125.9 |
| ba372ebb-3d96-361c-ba4f-b660efb9f44f | -7.4882 | -44.4601 | 2026-08-25 13:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 135.2 |
| 6d59e020-cdb6-3adb-bc9f-901249b2145e | -7.2715 | -45.3473 | 2026-08-25 13:50:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 97.9 |
| 0f843e57-0825-3efe-a1c3-2a41dd0daa64 | -13.8765 | -54.0322 | 2026-08-25 13:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 98.9 |
| c7d71954-f204-3833-bca0-007bf499ebca | -6.641 | -58.4987 | 2026-08-25 14:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 338.4 |
| 9c3975ee-b14f-38f8-92f0-1881c94fb7de | -7.4474 | -43.1163 | 2026-08-25 14:00:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 251.1 |
| 82b56224-4f31-3ace-99b0-d1ea8ed13a5e | -10.8605 | -50.5626 | 2026-08-25 14:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 74.3 |
| 3fcec41b-03e8-3af6-adf3-dfa8b0477fd1 | -7.4477 | -43.0928 | 2026-08-25 14:00:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 134.9 |
| 136c6895-209e-3da6-9dda-7b5d1b5cc640 | -12.6368 | -47.7974 | 2026-08-25 14:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 75.4 |
| c142a74a-9251-39c4-8297-bf6bbe94a2fa | -13.3595 | -48.2051 | 2026-08-25 14:00:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 117.3 |
| 25af8f37-4a08-31e9-b73a-64e662368c87 | -6.6409 | -58.5181 | 2026-08-25 14:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 91.1 |
| f9ce5e7c-01cd-37d1-b468-b59fc78e04e8 | -6.6225 | -58.5189 | 2026-08-25 14:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 54.5 |


[Clique aqui para ver as próximas entradas](README75.md)
