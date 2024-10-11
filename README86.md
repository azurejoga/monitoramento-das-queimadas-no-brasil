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

## Dados Diários - Página 86

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5cc87035-50a3-31a6-aaf5-fed5f17747ae | -7.08375 | -59.40958 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 118201dc-609a-38f1-9227-4f86bbd2c427 | -7.081 | -59.4056 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9fec892f-70de-3fbb-aeb7-f83431b65fe1 | -7.08045 | -59.40906 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 51434b3c-eae1-35ca-8615-f77f5b654d4d | -7.07991 | -59.41252 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7c6c6694-8335-3d04-b1b8-122d2342d2ac | -7.07824 | -59.40162 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 28446c4c-8207-3f73-8089-496f7c918c38 | -7.0777 | -59.40508 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 24b079ae-f865-3b6a-859a-2211d447860b | -7.07715 | -59.40854 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fd53ebb0-4e8f-372e-8cda-af7ecc1b2be3 | -7.07661 | -59.412 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e6f5011b-8caa-375b-81e7-a609124ed179 | -7.07494 | -59.40111 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f90eee00-d7e0-34b1-bd56-a5d268911b68 | -7.0744 | -59.40456 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| bd44126d-a58a-3cee-b295-fb3099b44fa8 | -7.07385 | -59.40802 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 77795cbe-149e-3983-a448-a21e776dd82c | -7.07331 | -59.41148 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d021c215-e004-302f-8a62-6fe170095a83 | -7.07164 | -59.40059 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 86d7e992-1bd9-323d-9508-ef52a58b4697 | -7.07109 | -59.40404 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ea006675-6f0a-39cf-a764-d3c60843ed14 | -7.07055 | -59.4075 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| aa6d98ad-a78c-340d-93a7-1d3b83da1234 | -7.07001 | -59.41095 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| db828b8d-6ae8-3795-970e-a216b43531ff | -7.06725 | -59.40698 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4ddff301-6989-3d21-be25-4a758e0131f1 | -7.05571 | -59.41579 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 62f6b5ef-6d25-34f4-8769-013249b779c5 | -7.05241 | -59.41528 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9f862600-b4e0-38a8-ad5f-522750c12f18 | -7.04966 | -59.4113 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 62c31e1c-6180-36fc-a1d8-2afbc5fd1528 | -7.04911 | -59.41476 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| accd8e43-32d7-3aef-877f-5b1d3d9b1e01 | -7.04857 | -59.41821 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9d8c3698-542e-360f-873d-afe1f471ba6f | -7.04802 | -59.42168 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4a1aef03-3059-39f0-bd6c-cf7e4abc56ee | -7.04636 | -59.41078 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ca117855-a13f-35b7-bc0f-a6914e2c4a1f | -7.04581 | -59.41424 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 746fbdae-4656-345f-bb73-256301af0fbb | -7.04527 | -59.41769 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 05a83930-1519-39a5-bac4-98d02e8e02d0 | -7.0436 | -59.40681 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 341040eb-7665-3b50-aa2c-cc1008d243cb | -7.04306 | -59.41026 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 992ddb20-486a-33fc-83e6-a9fc52727f4e | -7.04251 | -59.41372 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7977b812-ca55-3bc1-9153-85d1342972ba | -7.042 | -59.43844 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5a1abca9-cac6-3108-9273-0a283dc77370 | -7.04139 | -59.39938 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 86cba2e5-eaf3-3367-925d-73516ac738ec | -7.03975 | -59.40974 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3a970bd0-8e2b-3427-9c47-a4ecf6a75f85 | -7.03924 | -59.43446 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 312b0ac6-b4ee-390f-9b88-e577308838ee | -7.03921 | -59.4132 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ebad4230-8d4d-3151-b6d0-7be653e47d83 | -7.03649 | -59.43049 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8484c518-b1dd-3f05-9b49-dba1c5862847 | -7.03594 | -59.43394 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d9525830-3633-38f1-bd9d-e2f2aae99644 | -7.03373 | -59.42651 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1303e3ea-df9a-348a-a0d5-56f67a2cef30 | -7.03264 | -59.43342 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f3ddf089-e1e5-35bf-ab74-7498859c97f4 | -7.03152 | -59.41908 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 383edf17-2b42-364e-98ad-b61585579016 | -7.03097 | -59.42253 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 49602fa9-56c8-33fd-9929-ed42602b945d | -7.03043 | -59.42599 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9fcb8e30-3af9-359d-b7a9-ca72f5b0a190 | -7.02767 | -59.42201 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| df458f6f-97a2-334a-8917-46544ee3b91d | -7.02713 | -59.42547 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 12ef6611-0ee2-39ed-9060-b7cbc06ba0c3 | -7.02658 | -59.42892 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1ee5e14d-4991-36d5-9ed5-e7535b2f4896 | -7.02383 | -59.42495 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 47363289-56b9-3146-8f7e-d2128bd41b1a | -7.02328 | -59.4284 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 492f3459-c0dd-3925-a6d6-638927a9c211 | -7.02049 | -59.40317 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 185b4bf6-71e2-3567-8e8f-eeac940d63dd | -7.01665 | -59.40611 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e48799c8-2159-31bf-89ec-a72c0d2a2c35 | -6.9504 | -59.3067 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0f032ea9-2493-3e29-9e1a-d10c12a0a407 | -6.94985 | -59.31015 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8385acdd-0fc2-3fdb-8f0a-a031fbf3de58 | -6.81037 | -59.13962 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| af00f351-9f17-3fd9-a3c5-14ed66d47177 | -6.80983 | -59.14307 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 25267b8c-e461-3cf6-a378-f0f20f9a4efa | -6.80928 | -59.14652 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 72e082bf-ec75-31a6-9c81-c86a6dfbfb91 | -6.80653 | -59.14256 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ee66f140-b2f2-35e4-9755-5185a5d37fad | -6.80598 | -59.146 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 40fbe163-e20b-378d-827b-00ddf5d9d39d | -6.74231 | -59.28793 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 61a28185-ae1e-33ed-914f-77f1c6f03a08 | -6.73847 | -59.29086 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1b09cf9e-2167-37b3-9f75-97911928cf81 | -6.73792 | -59.29431 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1d813eab-b8ef-3de4-afff-edde65afd26e | -6.73738 | -59.29776 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5c6419c3-a492-39fc-a742-c12dd810556f | -6.73462 | -59.29379 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c697d1d9-8409-34e0-86bf-f54359b518f2 | -6.72585 | -59.30656 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 75b5e9b8-af7a-36f6-b702-27a9cdeaea5e | -6.7253 | -59.31002 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d429ba00-d91d-32d7-a046-bafb8610b1d0 | -6.72363 | -59.29914 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| df6d7055-780c-396e-adfa-b949574ee55c | -6.72309 | -59.30259 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 850e6c39-8582-3420-8e16-a89ab598f46b | -6.72255 | -59.30604 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ba7a5be4-b9f5-398c-834d-6f5eda052ebe | -6.71979 | -59.30207 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8c6eb9d1-53cf-322b-8f56-d707aee0e31f | -8.74868 | -60.48256 | 2024-10-11 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| db932c04-9109-3b4d-8f5b-c4641eb6f143 | -8.74812 | -60.48609 | 2024-10-11 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b730399a-2e70-35c4-9286-69828659fdaf | -8.74479 | -60.48555 | 2024-10-11 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4419b9dc-842a-31ea-ac3a-b12263efe066 | -9.2291 | -59.75005 | 2024-10-11 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 66b90065-ac36-307c-a6d9-d3fdb0a1f146 | -9.22856 | -59.75353 | 2024-10-11 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 61af9b7b-f2b8-3cbd-9368-a3abf5a4ac39 | -9.2258 | -59.74953 | 2024-10-11 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 04c21750-b55d-397c-91e9-bdb980960c05 | -9.222 | -59.7738 | 2024-10-11 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 429fd9d7-4696-387d-991b-c9918fb3709a | -9.22145 | -59.77726 | 2024-10-11 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 887fae3a-bf5f-3b6f-8694-46dd55a625d4 | -9.2209 | -59.78073 | 2024-10-11 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e4b44b7e-f0ff-3e79-9e8d-c4c2e40a1068 | -9.2187 | -59.77327 | 2024-10-11 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| aa7d5622-319a-345f-afcb-fc908034c14b | -9.21815 | -59.77674 | 2024-10-11 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7fad151d-a53a-3713-9f07-567c7aae52c7 | -9.2176 | -59.7802 | 2024-10-11 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 68b96f71-5829-3de5-bea1-a70354d331d6 | -9.2154 | -59.77275 | 2024-10-11 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 784974c0-20f8-315f-999d-81d383ddd824 | -9.21485 | -59.77622 | 2024-10-11 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b0704b76-fd5e-3387-a4f9-680f7fa81c8c | -9.2143 | -59.77968 | 2024-10-11 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7a5f9859-ba6e-3afb-b1be-b469610bd66f | -9.21155 | -59.77569 | 2024-10-11 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9e34a5d2-617f-3e7f-a96b-853d3c75d71a | -9.211 | -59.77917 | 2024-10-11 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| be50a49a-3cf5-3ab6-8d26-159a81ff06c1 | -9.39243 | -60.90441 | 2024-10-11 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4673275d-dbb4-344c-8f5d-8ace5efd39af | -9.38908 | -60.90387 | 2024-10-11 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 72a6e5b3-79fe-3d0c-92c6-bba88a2a6f04 | -9.94489 | -59.80482 | 2024-10-11 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 762df35c-0429-34ec-9da3-7ef9a7abbd99 | -9.86296 | -59.83097 | 2024-10-11 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ad74a423-e145-3408-9304-04f349459601 | -9.86242 | -59.83445 | 2024-10-11 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7518cf0a-8a82-30be-baf2-f4513ff56203 | -9.78377 | -59.81465 | 2024-10-11 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8adbc58b-11fe-3910-8f3f-01a7cb8734ad | -5.10222 | -60.31012 | 2024-10-11 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| abf5a83f-4f05-3982-b532-9ba807905b57 | -4.72014 | -60.8047 | 2024-10-11 05:18:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cd6ecdd4-185e-3273-8ffb-52e936892651 | -4.71773 | -60.51298 | 2024-10-11 05:18:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fe6bf0be-6d82-3824-8196-3dc9309ab1db | -4.71424 | -60.8193 | 2024-10-11 05:18:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8d0eb25f-ae74-3981-9041-edc1fc49121b | -4.71372 | -60.51614 | 2024-10-11 05:18:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1135da88-9cb4-34c1-a37b-613c31579117 | -4.71363 | -60.82309 | 2024-10-11 05:18:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1092f2bf-9678-37e9-9009-e0cc151e8b02 | -4.7114 | -60.81496 | 2024-10-11 05:18:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0cb38e68-5670-37d3-962e-d62d53bdb199 | -4.71079 | -60.81876 | 2024-10-11 05:18:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 74788423-18d7-330d-9fd5-115802cde2fe | -4.71018 | -60.82255 | 2024-10-11 05:18:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 65c1e99c-6fa4-3b5c-8318-460716215710 | -4.70734 | -60.8182 | 2024-10-11 05:18:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f9fef3fd-aa0d-346a-854c-3cdb64408f88 | -4.69822 | -60.74738 | 2024-10-11 05:18:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README87.md)
