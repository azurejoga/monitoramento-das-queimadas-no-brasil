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

## Dados Diários - Página 104

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5e0e5dfb-92bc-3443-9271-febaa5b98745 | -3.92423 | -60.55367 | 2026-09-22 05:42:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 11bf9782-3117-3a7f-ba33-e9ae0cf0b13a | -4.43052 | -55.08393 | 2026-09-22 05:42:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5ad9fe5d-9e7f-34f7-989c-6a299e4d9196 | -8.60417 | -54.63371 | 2026-09-22 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6d890793-775f-3018-97a2-d06a4e7e1a16 | -6.45586 | -59.992 | 2026-09-22 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8c115d3b-c30e-3477-92c8-55d704902e33 | -6.72512 | -55.09421 | 2026-09-22 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1d157a13-596a-3ffd-bedd-3bfd825fe2ca | -6.74091 | -59.42563 | 2026-09-22 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 83e178bc-99f8-396a-9675-4cc9ba7b18a9 | -4.56269 | -54.92043 | 2026-09-22 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 52be79f0-920b-3304-a055-485cac4f03ed | -8.92252 | -50.90361 | 2026-09-22 05:42:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e9714652-7a86-3f55-b33c-5337805134e0 | -6.64354 | -59.92576 | 2026-09-22 05:42:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 27.1 |
| eaf271f2-2778-31f3-b5ec-46a151c9f566 | -6.98337 | -59.78001 | 2026-09-22 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ab87c843-5ffc-38d7-b69e-dbdbecfa8912 | -7.549 | -61.31608 | 2026-09-22 05:42:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 07d8e3f9-55ff-313f-a865-1cf668439476 | -6.79509 | -59.14061 | 2026-09-22 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e38c428d-317e-30cf-854f-aacf60f80235 | -8.26399 | -55.30498 | 2026-09-22 05:42:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f4f888c5-d660-30fc-a3f8-6f66ea1bce9d | -6.9156 | -59.62685 | 2026-09-22 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 185ae010-9511-374a-b3d5-78e0147d59f0 | -3.06634 | -54.41752 | 2026-09-22 05:42:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a666f1ae-cb50-3a20-a711-913cd7794e0e | -7.71053 | -61.23158 | 2026-09-22 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 831974b8-19f5-366f-89cf-1f4412718803 | -3.51104 | -59.58381 | 2026-09-22 05:42:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 360842e1-e681-30aa-838e-c263aaa0a6c9 | -6.63599 | -59.92707 | 2026-09-22 05:42:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 8.6 |
| ede45d25-41b5-336c-a1e0-834ef06902d7 | -3.68214 | -60.62056 | 2026-09-22 05:42:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1a1d2c96-95d4-3b83-9424-55d04e8de53e | -3.33036 | -59.80741 | 2026-09-22 05:42:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e4c438cd-ffb9-3c31-9e3d-f15d54d100af | -6.91489 | -59.63167 | 2026-09-22 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 262e9447-b40c-3bb0-9872-dd57d9a69ed2 | -3.42169 | -61.29665 | 2026-09-22 05:42:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ade269e4-24e6-38b5-9edd-4155a228f28f | -3.68772 | -60.58497 | 2026-09-22 05:42:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 93f60d09-19b9-30ee-ae70-a5bf535aa6f0 | -2.95121 | -57.71896 | 2026-09-22 05:42:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b671ce8b-d534-3d8a-b536-ad13c4b07425 | -7.7099 | -61.23566 | 2026-09-22 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 4def038b-da3e-3cec-b9f0-79f4af098edf | -6.14394 | -59.93253 | 2026-09-22 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cfde9b4b-1dd2-34c2-b77b-44d82233025e | -6.3115 | -57.74094 | 2026-09-22 05:42:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| dde39b08-1247-3e62-9fda-c70a6b217a4b | -6.7287 | -55.06855 | 2026-09-22 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c302dc34-c113-37d2-807d-823d089db838 | -8.62087 | -54.6359 | 2026-09-22 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 265f4235-f84e-3626-ac3e-d5e66f673214 | -2.86216 | -57.80391 | 2026-09-22 05:42:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 00afeec7-5957-3a48-a1d5-74d039bb9340 | -6.12992 | -59.94896 | 2026-09-22 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f957e518-dde1-36c7-b0ca-6747cfef97fd | -6.42332 | -59.97763 | 2026-09-22 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0a5c90dc-b9d1-3c3a-bb40-5f3720599f00 | -5.13052 | -60.28145 | 2026-09-22 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| aab04cf7-0106-3b8e-b51c-8e38ea821fde | -6.46034 | -60.03889 | 2026-09-22 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f394fd07-db52-3b01-9c5c-e36ffd260a5f | -6.69248 | -59.9613 | 2026-09-22 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 43420846-5f72-3b9a-bac8-a3041e8baa3b | -3.06156 | -61.26928 | 2026-09-22 05:42:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d2a700cd-c4d6-30eb-8e0f-a23bebfdee68 | -6.42798 | -55.61116 | 2026-09-22 05:42:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1370c225-608a-382d-9575-9172e11237c5 | -6.86272 | -59.9066 | 2026-09-22 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 76615160-1a1c-3f45-aa35-f64ea83a66fb | -3.06729 | -54.41111 | 2026-09-22 05:42:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 59df3810-db31-3a38-9b77-1ff661adcb80 | -7.29135 | -59.52276 | 2026-09-22 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 5d35cdbb-4ff3-3ed9-97a4-84ca5a62e4df | -3.76894 | -51.35765 | 2026-09-22 05:42:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0365a61d-6725-339e-8111-9122f3e4294e | -2.5285 | -59.5524 | 2026-09-22 05:42:00 | NOAA-20 | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 4794e019-fc35-3627-afa2-c41bd8589f56 | -3.24232 | -53.9542 | 2026-09-22 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 180f9181-28b7-35b1-9d7e-8239e9f23139 | -6.19442 | -57.78373 | 2026-09-22 05:42:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| b9a3b44b-b98b-34a9-8db0-5b66b42a601a | -3.06207 | -54.41039 | 2026-09-22 05:42:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2a52fcff-6e2c-32a6-af3f-e2556cb62eca | -3.71378 | -60.55532 | 2026-09-22 05:42:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 596cb2ea-fc5a-3911-8b6e-0e99bf47f372 | -4.41622 | -55.24551 | 2026-09-22 05:42:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b20efae2-b795-3dfb-986a-bcbfc9ec47cc | -3.39486 | -61.06713 | 2026-09-22 05:42:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 65daa967-e899-3cd3-9432-93ef126229e4 | -6.35184 | -59.9644 | 2026-09-22 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ad2fe9ee-d354-3650-8d52-98d95642c5e0 | -2.56558 | -57.50869 | 2026-09-22 05:42:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| de318f0c-5de1-3d9f-9185-8ec850c994d4 | -7.97034 | -62.04307 | 2026-09-22 05:42:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1313e1ca-09c1-32c7-9f33-1b0dd3c6b06d | -3.23156 | -53.95252 | 2026-09-22 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 147e40df-05e0-35bc-8fea-ab11e806d8ab | -4.25637 | -60.00853 | 2026-09-22 05:42:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b684296a-30f6-30d1-b807-5115cd67ed4e | -6.73251 | -55.07972 | 2026-09-22 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b7fa15f8-354a-3aec-9825-ff2cc729499a | -3.68667 | -60.56857 | 2026-09-22 05:42:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 71acf177-194a-35a2-b33e-1ea68daac3b6 | -6.35895 | -58.28963 | 2026-09-22 05:42:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6e9323cc-8d12-3dfe-9a1c-d9541f250a0e | -4.9619 | -55.82823 | 2026-09-22 05:42:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6c09ce9b-a398-36a5-8beb-27fbe578b000 | -3.48337 | -59.56603 | 2026-09-22 05:42:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 37b66d0a-de6f-3b1a-b289-cf890b0dbc9f | -6.39336 | -60.02419 | 2026-09-22 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 86527ee5-6a41-310c-8b97-6c8d2cef1707 | -3.54021 | -60.57914 | 2026-09-22 05:42:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 805370bb-8b08-3605-bd5b-d5d204e6c1b6 | -6.91877 | -59.63226 | 2026-09-22 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 956cbb84-4eb3-3a1d-a2c0-bce7726306d7 | -3.91248 | -59.61976 | 2026-09-22 05:42:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4c423379-35ee-350d-a573-38e42ad05d79 | -5.81347 | -57.74084 | 2026-09-22 05:42:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| d3a787d0-2460-372e-b869-e40412b3c933 | -3.60998 | -59.02302 | 2026-09-22 05:42:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 61a88e52-e320-3c52-96d4-8be7e4c2fbf4 | -6.85892 | -59.90601 | 2026-09-22 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 94067fb2-a2a2-328d-a0d6-6a7ef14a68b3 | -3.684 | -60.60872 | 2026-09-22 05:42:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 472b6643-d98a-3ba3-9d12-f0f7879feb77 | -5.73059 | -53.46247 | 2026-09-22 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8ec20485-4f8c-3637-b71d-6f426e3c3e8d | -6.35588 | -58.28129 | 2026-09-22 05:42:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 27987134-eec7-32c1-ab22-db107e8a5c21 | -4.44945 | -55.4366 | 2026-09-22 05:42:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 323a8cae-36cf-388a-b993-6afc3604e9ba | -3.23102 | -53.95613 | 2026-09-22 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 0fc1986a-47a9-377b-a0c5-5328037cf939 | -6.43904 | -55.64222 | 2026-09-22 05:42:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a53365a2-cc1a-332d-81d1-074a36d440e8 | -5.46564 | -60.21782 | 2026-09-22 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2c734a37-53a3-3d07-bb45-19a04aa490f6 | -3.90379 | -60.59138 | 2026-09-22 05:42:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f64f98c2-e68a-3b8c-8ae9-5dc91df3a254 | -2.96528 | -57.62895 | 2026-09-22 05:42:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9393ebb1-877d-395f-9fca-5f97e568c362 | -6.35476 | -58.28901 | 2026-09-22 05:42:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c04db3ca-9c05-36ba-b894-fa7adee2fadf | -3.47863 | -59.59686 | 2026-09-22 05:42:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 09b25d34-e93b-382a-8545-ebbb2b3ab9dc | -6.79289 | -58.79065 | 2026-09-22 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5c6a7a85-6232-3027-a296-12f6916345ac | -6.28853 | -57.74606 | 2026-09-22 05:42:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d66e8968-677f-3401-8b70-e1d85afeb7a4 | -3.71748 | -60.55696 | 2026-09-22 05:42:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 84c556e9-6e6b-334c-8eff-80e07f46bcdb | -3.19051 | -60.4313 | 2026-09-22 05:42:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 56eba241-8312-3483-afa9-c23b30bc8357 | -6.10546 | -57.6824 | 2026-09-22 05:42:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| cb0b726a-1b97-3962-a17c-a68d19f31e98 | -5.37492 | -56.05371 | 2026-09-22 05:42:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 290d6a2a-c5b9-3dc1-b697-8895c41a1a16 | -6.12067 | -57.76133 | 2026-09-22 05:42:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| cb7d8101-5f0d-357d-87f9-3b44bde31e2e | -5.85069 | -53.534 | 2026-09-22 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d5b10551-bfbc-3c3d-9e9a-3ff4bd1ad016 | -7.70632 | -61.23513 | 2026-09-22 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4d018fb9-967c-344d-8c78-62afcdf389cd | -6.8379 | -55.53871 | 2026-09-22 05:42:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0a256066-5a0c-3773-9e3a-6e80780bc510 | -3.06573 | -61.28872 | 2026-09-22 05:42:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 61433745-0817-3a11-a746-0dbbc740139a | -4.41622 | -55.24667 | 2026-09-22 05:42:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4e499743-5ce0-3da6-8d8d-bafba3993a98 | -3.37046 | -61.28919 | 2026-09-22 05:42:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 5e9064e2-e113-387c-9dd8-1feeedef0fc9 | -4.96303 | -55.83165 | 2026-09-22 05:42:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 6f5ddd6e-d23c-3e2d-9128-d96ccb4efc31 | -4.18306 | -51.24856 | 2026-09-22 05:42:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| fa3348df-19f1-348d-9ed7-ade6303f55b6 | -3.49619 | -59.58154 | 2026-09-22 05:42:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1f9c0c31-df91-3dc3-bb2e-e2a466606766 | -3.59896 | -59.44509 | 2026-09-22 05:42:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5e21f5fe-088c-37d7-b263-aa758695f72b | -5.88592 | -51.57672 | 2026-09-22 05:42:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| dc5983be-72dc-30fd-8d5f-4bb8877e5bdc | -6.71142 | -59.00378 | 2026-09-22 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 15349593-d404-3805-aa6b-49e98326b193 | -3.87322 | -51.18884 | 2026-09-22 05:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5f2be4e2-fb43-3ccc-bfb3-8e35ae2f3751 | -2.8581 | -60.91364 | 2026-09-22 05:42:00 | NOAA-20 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9614f2a3-d03a-3f7e-bcda-1ba2dcad7cac | -3.05473 | -61.26822 | 2026-09-22 05:42:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c1440dd2-699f-3899-9bc5-12907967105c | -3.37573 | -64.91452 | 2026-09-22 05:42:00 | NOAA-20 | ALVARÃES | AMAZONAS | Brasil | 1300029 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 03b6aad4-64a2-3e55-8459-6aa0f9b2f5f7 | -6.72957 | -55.0623 | 2026-09-22 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README105.md)
