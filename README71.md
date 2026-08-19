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

## Dados Diários - Página 71

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3ea022d1-8d4b-36f6-b042-70fdad3be854 | -8.5598 | -54.7579 | 2026-08-19 06:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 1a111aca-7f9f-3add-8a96-8d292529d652 | -8.5785 | -54.7566 | 2026-08-19 06:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 41d75b7b-a33b-3a56-8aad-cf89d5b91061 | -9.4256 | -60.4353 | 2026-08-19 06:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 43.2 |
| 2b9e15b1-a852-3beb-b4c4-5d988fc908f1 | -5.4317 | -48.4212 | 2026-08-19 06:20:00 | GOES-19 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 66b2c0b5-bdcb-3343-8b3a-2f4b2c2f664b | -5.9994 | -57.8639 | 2026-08-19 06:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 50.1 |
| ea992c5b-a1cc-3bf4-b3bc-f271ff991888 | -6.0912 | -57.9187 | 2026-08-19 06:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 61.8 |
| 82b0f4a1-cb23-3ec2-8560-fe833b20b362 | -19.7442 | -57.9425 | 2026-08-19 06:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 99.7 |
| ddbde5eb-3f08-36b7-880d-386229bc2cef | -9.5516 | -63.52433 | 2026-08-19 06:20:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5be76cd4-57fb-3bd0-adca-07eaeb7e69ea | -7.05781 | -59.84159 | 2026-08-19 06:20:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b6d2023b-9a4a-335d-8183-088d1d282044 | -9.42067 | -60.44781 | 2026-08-19 06:20:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c43c6b79-4ff1-35c0-ad13-51bb2256724d | -7.0535 | -59.84364 | 2026-08-19 06:20:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0903212c-628a-3925-bc81-362964ab060f | -7.60389 | -60.95437 | 2026-08-19 06:20:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| ef2bceb1-669f-3cac-97bf-1bd0c66e9c08 | -9.42506 | -60.43496 | 2026-08-19 06:20:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| dc34c2fb-7990-3f36-a0a9-86a146d29d90 | -9.41985 | -60.45471 | 2026-08-19 06:20:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 570b6c13-0d20-3af7-b498-9897ec241f42 | -7.60832 | -60.97289 | 2026-08-19 06:20:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3d77ff9f-ad04-3e34-9285-dbd54667dd3e | -9.40112 | -60.56973 | 2026-08-19 06:20:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 008e9fd6-0f04-304b-99d0-94c709b079a5 | -9.3879 | -60.56146 | 2026-08-19 06:20:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| a9dbd1de-5641-3d6b-aaf2-08381f8f4292 | -9.40465 | -60.5835 | 2026-08-19 06:20:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 59903830-4620-3ece-aa11-444e1012d7be | -7.0526 | -59.85046 | 2026-08-19 06:20:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f14b21ae-cb55-32dc-8c9a-232b70394d97 | -9.39494 | -60.56217 | 2026-08-19 06:20:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 8d7e8dd7-ef08-3c5d-8dc0-3b30d582dd2e | -7.61503 | -60.97377 | 2026-08-19 06:20:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 24fe8e71-c2a8-3638-95a8-06c879ca17df | -9.07583 | -65.41029 | 2026-08-19 06:20:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 15acf0ea-6f01-3fee-b3ef-4cef322c5449 | -9.0792 | -65.38554 | 2026-08-19 06:20:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| db036242-49e0-3a8f-8437-1794d5cf5cfe | -9.42422 | -60.4417 | 2026-08-19 06:20:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 050da6b2-4814-393a-bd16-140d7d85e345 | -9.42147 | -60.44102 | 2026-08-19 06:20:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 8a7b458d-9c60-3e5d-87ea-7f93b1ddefaa | -7.04636 | -59.84293 | 2026-08-19 06:20:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2cc24f3d-f9b0-39b3-8d76-9f3be6c62819 | -7.05694 | -59.84852 | 2026-08-19 06:20:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 25f2e931-e056-3bef-b4ce-654464ad771e | -9.39842 | -60.576 | 2026-08-19 06:20:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 838d7789-1bc9-3915-960d-0af77ed01451 | -9.42386 | -60.42071 | 2026-08-19 06:20:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 423db921-3d1e-3382-a7ca-a145dfebe165 | -5.49647 | -60.13076 | 2026-08-19 06:20:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 71398b87-4567-3de1-9aab-b947b80a5ff3 | -9.42226 | -60.43427 | 2026-08-19 06:20:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 0c546132-4f98-3a70-83e1-a1375058bd20 | -9.39411 | -60.56889 | 2026-08-19 06:20:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 1a31aa54-c0cd-36d8-952a-2a5180a97be1 | -9.4259 | -60.42817 | 2026-08-19 06:20:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 4180e651-c6c6-39ec-99ed-7c036297e7d9 | -5.49561 | -60.13705 | 2026-08-19 06:20:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 628ea351-debe-3a6e-8e15-086f8f2e7a92 | -9.40196 | -60.56303 | 2026-08-19 06:20:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 70ddf029-d0b3-3a1e-b5b0-ff29a4ec9617 | -7.04979 | -59.84785 | 2026-08-19 06:20:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 440a1591-055c-3eef-bef4-769322121ef0 | -9.40029 | -60.57647 | 2026-08-19 06:20:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 9588e0dd-697c-34eb-8e61-8d6aba72fcd2 | -7.60983 | -60.96121 | 2026-08-19 06:20:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 262c2209-1ceb-3b98-aa04-558b23762501 | -7.8831 | -61.19175 | 2026-08-19 06:20:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 80c12665-f092-32a6-9722-d37d078cb4f2 | -9.3922 | -60.56837 | 2026-08-19 06:20:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9976e02f-494f-3c48-a870-b8146436896e | -9.40001 | -60.56251 | 2026-08-19 06:20:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| e70f91ca-8297-3a00-9bc2-95d37a9c295a | -9.42675 | -60.42135 | 2026-08-19 06:20:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 92b56494-9b00-35f8-94da-2e6e6c742de0 | -9.42337 | -60.44852 | 2026-08-19 06:20:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| cf1fed8d-e54d-33a0-a87f-b8c5aa313f26 | -9.39298 | -60.56168 | 2026-08-19 06:20:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 279ee05d-d87a-33c2-81e6-2569df0d2e1a | -9.39576 | -60.55556 | 2026-08-19 06:20:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| eaefc04b-49e2-329c-bcf5-53d7460f87e1 | -9.39376 | -60.55503 | 2026-08-19 06:20:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 581553db-1c24-3992-9b79-a4641d7b806a | -9.38673 | -60.55423 | 2026-08-19 06:20:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| cf65b7d0-6680-35ae-bd92-6d41c27ac085 | -9.07625 | -65.40719 | 2026-08-19 06:20:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 8b3bb50d-89fd-3b8e-9256-20e085e8e827 | -9.0814 | -65.40792 | 2026-08-19 06:20:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 0d692d26-37e6-3acb-b11c-35a32965ad5f | -9.39922 | -60.56924 | 2026-08-19 06:20:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e51ce4a7-32b4-3275-998b-e4c293a0857f | -9.07499 | -65.41644 | 2026-08-19 06:20:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 7.8 |
| bf0ee611-98ab-38d5-92c2-6234bedfbd32 | -9.42306 | -60.42751 | 2026-08-19 06:20:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 63bfd259-f418-37f0-89f5-b7f19d46ff1c | -9.08055 | -65.41409 | 2026-08-19 06:20:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 78fa4be3-f751-3832-9a81-18f591267478 | -9.38873 | -60.55477 | 2026-08-19 06:20:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 726d968e-3091-38ed-a65e-cc34dda4d0ae | -5.49476 | -60.14329 | 2026-08-19 06:20:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c4792510-69c9-373e-b58f-fbcd4ed548e2 | -7.89049 | -61.18681 | 2026-08-19 06:20:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 68d9cb74-d647-31fb-888f-8e2e116c3216 | -7.88236 | -61.19751 | 2026-08-19 06:20:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 39d81449-e942-3639-b9ff-2894cab087fb | -9.07541 | -65.41337 | 2026-08-19 06:20:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 7.8 |
| c7d45c0a-28e0-389d-89e6-816549caafb1 | -7.60313 | -60.96025 | 2026-08-19 06:20:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 64be8c3e-18ef-3b07-bd2e-094887c74c32 | -9.07836 | -65.39173 | 2026-08-19 06:20:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 77c31c1b-f236-39ab-8bdf-7bc57185c68a | -7.61058 | -60.95548 | 2026-08-19 06:20:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a5906213-0021-3f23-9eab-99b5ad054712 | -7.05066 | -59.84087 | 2026-08-19 06:20:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 127e0ec1-98d2-3b3d-bdca-7415d9aa7b9a | -9.42251 | -60.45542 | 2026-08-19 06:20:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| afddd37c-f7f4-3e21-93f3-a87d8720d69b | -9.08097 | -65.41101 | 2026-08-19 06:20:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 7.5 |
| f02e607e-2462-36c1-8684-e0b08c2a05ff | -9.07878 | -65.38864 | 2026-08-19 06:20:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 29731589-bc57-35b6-873f-0e654a56f6dc | -7.60465 | -60.94849 | 2026-08-19 06:20:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9bf5844c-3d63-306f-8b74-9845718e5cde | -19.7442 | -57.9425 | 2026-08-19 06:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 106.3 |
| 1aa1d5a7-eaeb-3641-b151-23d9fecd5c8e | -8.5785 | -54.7566 | 2026-08-19 06:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 66.6 |
| c19d25b1-d323-3d86-946d-beb9be60a86e | -9.4256 | -60.4353 | 2026-08-19 06:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 51.1 |
| bd1b3893-521c-3f73-9e14-f5ec5f051b7f | -19.7647 | -57.9191 | 2026-08-19 06:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 71.5 |
| e84f71af-32c2-3c37-9c7c-0105fd97a5a8 | -5.4317 | -48.4212 | 2026-08-19 06:30:00 | GOES-19 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 5a6f71e0-995d-3887-8fa5-c4ef908b13a8 | -9.08 | -65.4163 | 2026-08-19 06:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 56.0 |
| ffb7f7bf-4ffa-37cd-a03c-8a90098a848c | -6.0912 | -57.9187 | 2026-08-19 06:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 63.5 |
| 00b47cbd-f52f-3353-9c9f-9d69ac0db546 | -9.0801 | -65.3976 | 2026-08-19 06:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 46.8 |
| b2001a73-fc34-34a9-994f-0b259bf1e76a | -19.7643 | -57.9399 | 2026-08-19 06:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 106.6 |
| 8a077929-45c9-33ac-8ccf-0810af105d44 | -21.5343 | -52.0046 | 2026-08-19 06:30:00 | GOES-19 | PRESIDENTE EPITÁCIO | SÃO PAULO | Brasil | 3541307 | 35 | 33 | nan | nan | nan | Mata Atlântica | 63.8 |
| f0c60b7c-b9fd-306a-90db-a75ee6e536ff | -5.9994 | -57.8639 | 2026-08-19 06:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 53.0 |
| 879b88bf-1bbc-37da-8685-0340f59d0fee | -8.5598 | -54.7579 | 2026-08-19 06:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 65.7 |
| 6ac5782d-3b9e-31ef-ae03-7955e9fe0de1 | -14.8033 | -46.6453 | 2026-08-19 06:30:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 53.9 |
| f25f1dfa-c658-3ce2-9478-38488573f4b0 | -19.7446 | -57.9217 | 2026-08-19 06:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 72.3 |
| 1a4ccf51-4a78-3452-9bdb-05aab6d65859 | -5.9198 | -43.6264 | 2026-08-19 06:30:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 99.0 |
| fc037d85-6786-3244-acc6-5092f39b7f32 | -8.56 | -54.7377 | 2026-08-19 06:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 54.9 |
| 9142ae46-ff96-3852-970c-f5b5d47ae80a | -11.6409 | -54.5315 | 2026-08-19 06:30:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 28.8 |
| 777d226b-c13b-3e9d-aad8-39440057adf4 | -9.08 | -65.4163 | 2026-08-19 06:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 1a6ef368-fa34-3d76-ad22-2cc6612d25ed | -19.7643 | -57.9399 | 2026-08-19 06:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 137.1 |
| bfbb9185-130a-331d-b372-7bed1cfda864 | -5.9994 | -57.8639 | 2026-08-19 06:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 48.4 |
| c9ae5261-264a-3d24-8b59-622ac415b3a2 | -19.7446 | -57.9217 | 2026-08-19 06:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 86.5 |
| 413c2606-7ee6-3a0f-958c-2ef37bab3184 | -8.56 | -54.7377 | 2026-08-19 06:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 54.4 |
| a3a65030-6d0c-3ddc-950b-7d1fb724ca27 | -5.4317 | -48.4212 | 2026-08-19 06:40:00 | GOES-19 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 8fc72163-adeb-3fd7-81a7-bfd6365f5c21 | -6.0912 | -57.9187 | 2026-08-19 06:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 78.8 |
| 6f2c83b5-1bae-30fb-b35e-d4eea17b1a6a | -19.7647 | -57.9191 | 2026-08-19 06:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 100.9 |
| 9b1599af-29a2-3717-8fff-11d6f6f97e1a | -5.9198 | -43.6264 | 2026-08-19 06:40:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 100.0 |
| 672ff32b-701b-32b0-8a91-016fe0ecade4 | -19.7442 | -57.9425 | 2026-08-19 06:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 114.1 |
| dbe785ec-8ec6-3d45-bb6a-bafa0db23fcd | -8.5598 | -54.7579 | 2026-08-19 06:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 62.4 |
| 4c6ab6b3-0c9f-336e-8402-f703a7f35d76 | -8.5785 | -54.7566 | 2026-08-19 06:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 861442c4-233b-332d-8352-3bb01cb72dfb | -9.4256 | -60.4353 | 2026-08-19 06:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 46.3 |
| cb14ed85-c4db-3b66-b624-271ccd7215e3 | -19.7442 | -57.9425 | 2026-08-19 06:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 126.5 |
| ded513ae-074e-3729-bbb0-0ef9b2343c36 | -8.56 | -54.7377 | 2026-08-19 06:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 53.4 |
| b767e362-a569-3ea7-abde-a39202caf6ec | -19.7647 | -57.9191 | 2026-08-19 06:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 86.3 |
| 16f00051-4372-3488-846f-7e195c1e790d | -19.7643 | -57.9399 | 2026-08-19 06:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 93.2 |


[Clique aqui para ver as próximas entradas](README72.md)
