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

## Dados Diários - Página 99

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4353bd59-8a71-3cb2-b34e-c9d58f055c31 | -20.08165 | -55.95715 | 2024-10-09 04:17:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| f5e5d944-009e-3917-a221-40086a9b6862 | -20.08091 | -55.96056 | 2024-10-09 04:17:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| c77d2a13-8717-3ab5-b97a-489bad5bcaec | -20.08017 | -55.96398 | 2024-10-09 04:17:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 9eb385d1-037c-3791-98ce-e7bbe8a2a39e | -20.07568 | -55.95934 | 2024-10-09 04:17:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| ea1b83ff-0e10-3a77-a0f9-a7d0c437d176 | -20.07494 | -55.96276 | 2024-10-09 04:17:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| b84797df-73a6-33b0-826d-67b61efc9410 | -7.95679 | -54.76638 | 2024-10-09 04:17:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| d78993bd-1a4e-340c-86d2-a73fbea6c633 | -7.95592 | -54.77096 | 2024-10-09 04:17:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 39117212-51b4-31a5-badc-6deab81eea94 | -7.95584 | -54.766 | 2024-10-09 04:17:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 10f9b0be-d2c9-3b2d-86e4-af4573bff4be | -7.955 | -54.7706 | 2024-10-09 04:17:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1a116c03-aaac-3fe4-8faf-293003d0a262 | -8.6221 | -54.93151 | 2024-10-09 04:17:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| e2c69a1d-e99d-37ee-96cc-e3d18a1998c1 | -8.51044 | -55.15134 | 2024-10-09 04:17:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 79a7596d-95b6-3ef9-8142-d11f48bb6016 | -8.50952 | -55.15609 | 2024-10-09 04:17:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f7c30d42-453d-36f1-a101-76abcfba7ef1 | -8.30405 | -55.10844 | 2024-10-09 04:17:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 90967bd1-c435-30d6-a39b-0d8342b74aa7 | -8.30323 | -55.10851 | 2024-10-09 04:17:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 7f2b0d27-6ee7-31d2-9951-6e583d29741c | -8.30315 | -55.1133 | 2024-10-09 04:17:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 19.8 |
| 2568dc30-3e1d-3d5d-bc33-bd418728b15b | -8.30229 | -55.11334 | 2024-10-09 04:17:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 17.6 |
| 18add5f2-57d3-358b-bc37-b0b001fad494 | -8.22393 | -54.89266 | 2024-10-09 04:17:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 97a16cb4-1a20-32e4-ba2d-a9fbdc261768 | -8.22384 | -54.89548 | 2024-10-09 04:17:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f5d435c9-23e4-35c3-867b-fe8bd118debb | -8.22307 | -54.89729 | 2024-10-09 04:17:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2c298ac2-39fd-329f-9466-f80eff1e4e0d | -8.13921 | -55.17546 | 2024-10-09 04:17:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| de7bdcc2-ccde-31c5-8ddb-23e276766df7 | -10.63678 | -55.89518 | 2024-10-09 04:17:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e1ea4feb-ab8b-3078-acf6-2f6d8b80d384 | -10.63535 | -55.89221 | 2024-10-09 04:17:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 144c87fb-6d00-358d-bfbd-4d1603f92003 | -10.63433 | -55.89722 | 2024-10-09 04:17:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| aeb54e19-7743-35c3-ace7-63fbac2bd03f | -10.63331 | -55.90229 | 2024-10-09 04:17:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| a029b5e6-8cf5-3e84-a155-d1be7ddf5714 | -10.63231 | -55.90725 | 2024-10-09 04:17:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| be133eb4-cdf5-315b-acde-cb33b14e7f6b | -10.63156 | -55.88884 | 2024-10-09 04:17:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 5c929494-b02b-396e-b2d6-c81c1a9215e9 | -10.63133 | -55.91212 | 2024-10-09 04:17:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 8597b34e-8021-3e66-a976-6d915b61f5ea | -10.63055 | -55.89404 | 2024-10-09 04:17:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 84a9f89f-48b1-3406-850f-b169ed05191c | -10.63019 | -55.88576 | 2024-10-09 04:17:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| f62eee14-87eb-332a-a1fe-c71bde6774d6 | -10.62955 | -55.89918 | 2024-10-09 04:17:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 61010f53-fc81-33c8-b1a1-42fb20e37d9d | -10.62935 | -55.92192 | 2024-10-09 04:17:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 16.0 |
| 225b0ce6-aaed-33fd-b5b4-3e5f44704d70 | -10.62915 | -55.89092 | 2024-10-09 04:17:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 68f9269b-cfca-3453-a0d3-5370da566ee5 | -10.62857 | -55.90421 | 2024-10-09 04:17:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 9929f65d-a987-3623-b1d5-45da7ede1909 | -10.62808 | -55.89619 | 2024-10-09 04:17:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 23d143c8-b207-30be-b7e0-f898e58aef90 | -10.62762 | -55.90907 | 2024-10-09 04:17:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| b9b522ba-2373-37df-9aa8-cd07608d002e | -10.62707 | -55.90122 | 2024-10-09 04:17:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 20b2183b-8e31-34f5-a30b-6b3de29b1cdc | -10.62667 | -55.91396 | 2024-10-09 04:17:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 12.1 |
| fa1ffff1-b8a6-36d5-8097-81336670b7a8 | -10.62607 | -55.90615 | 2024-10-09 04:17:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| f5afed13-f6e7-30f6-ac68-44159c0033d1 | -10.62571 | -55.91886 | 2024-10-09 04:17:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 6d174a4e-b29c-3157-a08d-0c24072f714d | -10.62533 | -55.88773 | 2024-10-09 04:17:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| ce75ac05-545d-3006-9522-22897b60047c | -10.62508 | -55.91105 | 2024-10-09 04:17:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 0dabb119-4061-3cf1-8b69-97d18583383c | -10.62474 | -55.92383 | 2024-10-09 04:17:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 18.6 |
| 650fcc4d-9df5-3572-8aab-27ee2861d304 | -10.6243 | -55.89296 | 2024-10-09 04:17:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| f87d8821-705c-3824-9f03-1931bad2477c | -10.62409 | -55.91594 | 2024-10-09 04:17:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 7fc9e9d2-798f-3840-ac80-75e9d31e7f72 | -10.62377 | -55.92881 | 2024-10-09 04:17:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 18.6 |
| 0ba30af6-087a-3d0f-9b6d-5371d513956b | -10.62331 | -55.89802 | 2024-10-09 04:17:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| f6c7e0b5-0790-3a76-8cc1-72f980965c38 | -10.6231 | -55.92083 | 2024-10-09 04:17:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 16.0 |
| 71bdaea0-8e20-32e6-a034-3194c2a0b921 | -10.62235 | -55.90299 | 2024-10-09 04:17:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 1c4d2fac-956c-329e-9af0-0314098eeacc | -10.62211 | -55.92572 | 2024-10-09 04:17:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 16.0 |
| 2cc40f68-b676-384e-b0a9-f0781b66eb5f | -10.62184 | -55.8951 | 2024-10-09 04:17:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4f388aed-14e6-3d34-82eb-f8e8055789ea | -10.62138 | -55.90795 | 2024-10-09 04:17:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| ddd03d24-6e88-3d92-a83c-dddffb0e8c05 | -10.6211 | -55.93073 | 2024-10-09 04:17:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 139f736f-62c1-3c85-856d-3a07eaf6bdb3 | -10.61946 | -55.91777 | 2024-10-09 04:17:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 5c69e0dd-a053-3098-b7f3-09d52edc7f5e | -10.61851 | -55.92262 | 2024-10-09 04:17:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 18.6 |
| 52ba4e8a-8e70-3dcf-a0b3-81da867b8d43 | -10.61754 | -55.92761 | 2024-10-09 04:17:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 18.6 |
| 27ff7978-463f-3a13-a430-6b80334438e2 | -10.61688 | -55.9196 | 2024-10-09 04:17:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 25e481e2-1616-3cf5-9c26-2ac23fb2a7f0 | -10.61587 | -55.92457 | 2024-10-09 04:17:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 15.7 |
| ac1daee4-4843-31fc-8e7a-b9c41d25c290 | -9.95803 | -55.3389 | 2024-10-09 04:17:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3f4b7eac-3a3f-3434-b188-d38d9c899e8c | -9.95286 | -55.33306 | 2024-10-09 04:17:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 970e5539-ca8d-38de-b587-09f1e0153baa | -9.58818 | -56.47841 | 2024-10-09 04:17:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c84d200d-87e0-3727-8a36-cc80c373a05e | -9.58163 | -56.47715 | 2024-10-09 04:17:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6f232886-6e54-39de-b69f-242a4605b1d9 | -9.49222 | -56.07703 | 2024-10-09 04:17:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 20082618-7cc0-3ee0-9eab-22d9d2d95d5a | -9.49116 | -56.0825 | 2024-10-09 04:17:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 1a4452a6-bec3-319a-8266-fc597e7f03b0 | -10.36249 | -55.86588 | 2024-10-09 04:17:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 5cfad2be-132d-3207-aff4-a7212fd03d0a | -10.35627 | -55.86459 | 2024-10-09 04:17:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 88b88660-1fc0-39c4-8579-a8da3ba44d89 | -12.80279 | -56.95876 | 2024-10-09 04:17:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a772662e-9a1d-3e12-8863-8dc7723072bd | -12.61895 | -56.51324 | 2024-10-09 04:17:00 | NOAA-21 | TAPURAH | MATO GROSSO | Brasil | 5108006 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 43c8b168-b545-303b-a654-b4945f1bce4a | -12.61274 | -56.51188 | 2024-10-09 04:17:00 | NOAA-21 | TAPURAH | MATO GROSSO | Brasil | 5108006 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| de198a0a-0aad-37d3-9ffb-8dc9d678485f | -12.61173 | -56.51678 | 2024-10-09 04:17:00 | NOAA-21 | TAPURAH | MATO GROSSO | Brasil | 5108006 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2cc7c35b-2fb7-37f8-b76f-45e9ea0ff055 | -14.33826 | -57.58892 | 2024-10-09 04:17:00 | NOAA-21 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 89cd2953-b1f8-3202-8826-f886d7d90f44 | -18.64682 | -57.2105 | 2024-10-09 04:17:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.5 |
| a5e8b8cb-ca14-39d7-8426-b8957afc7b07 | -17.75715 | -57.11054 | 2024-10-09 04:17:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 35755916-6f29-3061-ba2d-efa3895ad895 | -17.75479 | -57.11071 | 2024-10-09 04:17:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| c1507e42-79c4-3285-be10-790951b65e6e | -17.73331 | -57.09632 | 2024-10-09 04:17:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 599be366-ac0f-3327-aa19-f956ea79dab6 | -17.16806 | -57.41713 | 2024-10-09 04:17:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| e110b888-8879-3e2a-99aa-022e73eff1ee | -17.16169 | -57.44594 | 2024-10-09 04:17:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.8 |
| ec9c8067-300c-34d6-9276-74b679881e3e | -17.16096 | -57.42052 | 2024-10-09 04:17:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 11.1 |
| c5d99cfb-d3db-3d03-9e46-655b516d42d7 | -17.16062 | -57.45076 | 2024-10-09 04:17:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.0 |
| e9c1d4a3-1ee8-395b-87f9-3f56613bbd74 | -17.1599 | -57.42531 | 2024-10-09 04:17:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 11.1 |
| f81972f7-be9f-3dbd-bfe7-a3728a0dcd47 | -17.15883 | -57.43011 | 2024-10-09 04:17:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 19.3 |
| a6b62027-3964-3e91-bfd3-b85c7144661c | -17.15777 | -57.43492 | 2024-10-09 04:17:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 19.3 |
| 2e858902-f668-3ed3-b704-98932b04f5c3 | -17.1567 | -57.43972 | 2024-10-09 04:17:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 68.3 |
| e0b8494e-8955-3166-8df4-018f2f6cd80d | -18.6323 | -57.2209 | 2024-10-09 04:17:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 3e1c9605-aa36-3c79-b719-4e6a60d0359c | -18.62552 | -57.22389 | 2024-10-09 04:17:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 04a486e9-f42c-3028-b586-b02e51d8f8bd | -18.61097 | -57.23428 | 2024-10-09 04:17:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 03c7ecab-322e-3930-9226-a27b4fa04e52 | -17.11328 | -57.43468 | 2024-10-09 04:17:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.4 |
| e1f31a8c-d710-30d1-a4d6-fe438842303d | -17.1122 | -57.4395 | 2024-10-09 04:17:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 14.9 |
| 890ccd55-49f4-3205-9e2d-486363320dcc | -17.11112 | -57.4443 | 2024-10-09 04:17:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 14.9 |
| 0fcf4c4a-ee39-3faa-a335-1010debe6d3a | -17.11003 | -57.44912 | 2024-10-09 04:17:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 15.6 |
| 654310af-0d63-30d2-8e79-f61498d9b325 | -17.10895 | -57.45395 | 2024-10-09 04:17:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 15.6 |
| 56a798bd-c416-3405-b7ac-bbd8959ebf82 | -17.13534 | -57.44993 | 2024-10-09 04:17:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 16.7 |
| 060214e6-5b3d-3f5b-a97a-b7b17ce158cf | -17.13426 | -57.45476 | 2024-10-09 04:17:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 17.2 |
| 0f8a2555-3fe1-34ce-a9ef-302d02cae363 | -17.13251 | -57.43406 | 2024-10-09 04:17:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.6 |
| 465cce30-7307-3360-8979-54826d0dde32 | -18.6062 | -57.23458 | 2024-10-09 04:17:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 74e1c4e4-5ba9-37ca-af4c-0aa4ff368cc7 | -17.13144 | -57.43887 | 2024-10-09 04:17:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.6 |
| 63a73801-bdf6-36e6-bd26-64bb103473cf | -17.13036 | -57.44369 | 2024-10-09 04:17:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 12.8 |
| bba26f1f-485b-3514-ac9d-cee954835362 | -17.12929 | -57.4485 | 2024-10-09 04:17:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 12.8 |
| 9bec733f-357a-31b8-9ad0-b4306e0ac15d | -17.12821 | -57.45334 | 2024-10-09 04:17:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 23.8 |
| af34c0e2-dffc-33ba-86fb-34ec929c9855 | -17.12646 | -57.43264 | 2024-10-09 04:17:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.6 |
| 8f11cbdf-9914-305d-b76c-131da080a51c | -17.12538 | -57.43748 | 2024-10-09 04:17:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.6 |


[Clique aqui para ver as próximas entradas](README100.md)
