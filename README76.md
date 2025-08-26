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

## Dados Diários - Página 76

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 84e0dfb5-b5c7-35f9-8797-8649406107e9 | -8.24443 | -61.45356 | 2025-08-26 05:36:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 5532277a-0921-37c1-b953-890b4d3e9387 | -6.79113 | -59.66652 | 2025-08-26 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d51a7d47-62bd-3e98-af82-d90336a85da3 | -8.10835 | -62.87908 | 2025-08-26 05:36:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 79b03dc0-2486-3882-a56b-0bb69e4a2eb7 | -7.39458 | -64.35179 | 2025-08-26 05:36:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b41072c6-b286-38f9-a0b7-9092561693ed | -4.95849 | -55.80748 | 2025-08-26 05:36:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 1a51ef07-e22f-39cf-b799-8fc75aa6f18d | -7.38689 | -64.35767 | 2025-08-26 05:36:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3de8acee-e7e8-3a28-8db2-e7a6a190d1b8 | -7.88091 | -63.01271 | 2025-08-26 05:36:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a551256a-42a3-3c25-b53e-150aa081e956 | -6.88082 | -59.90005 | 2025-08-26 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7f084f1d-35cd-3d7e-87d3-c2f82aec857b | -6.70549 | -58.56413 | 2025-08-26 05:36:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 83fb29d3-15ab-32df-8cfd-663c516c4c84 | -7.5445 | -63.85099 | 2025-08-26 05:36:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| be4a2ac9-3533-35ed-8736-8488f76b595f | -7.56543 | -63.84715 | 2025-08-26 05:36:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9fde37bc-06e3-324b-9df2-114f7c1d2f2d | -5.29922 | -60.19701 | 2025-08-26 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 454f8164-ed86-3529-b605-b7b126d95e70 | -5.30525 | -60.20669 | 2025-08-26 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6bf5beb4-a805-3995-bd9e-52d9a519c072 | -7.88146 | -63.00915 | 2025-08-26 05:36:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 7afb084c-d995-3d59-a7c2-aab8651450f2 | -5.52547 | -60.21044 | 2025-08-26 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 0ea0f97e-eff3-3aed-9f2b-95c7ebcb6998 | -7.29167 | -59.66648 | 2025-08-26 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 010d238f-21c7-3c34-85b0-b65ce2c84a2f | -6.78554 | -59.65101 | 2025-08-26 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b123dcc2-1233-3f22-8624-d904c6542df4 | -8.10238 | -62.88222 | 2025-08-26 05:36:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 524d5465-4cba-34c4-9293-80a4a702ee51 | -6.256 | -60.01871 | 2025-08-26 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ff7d0d0f-b85e-3020-95e4-0361e84b1119 | -6.70189 | -58.55981 | 2025-08-26 05:36:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c1a92411-c99f-3dcd-bfc3-d0b0e956f4ee | -6.23332 | -60.00841 | 2025-08-26 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5f969eb1-6489-3fbe-9e45-72cf7a337a8d | -8.10349 | -62.87502 | 2025-08-26 05:36:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 398f0a54-7bb9-33c6-a468-1c562da3f56a | -7.54282 | -63.84007 | 2025-08-26 05:36:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a94e0418-3065-3975-8515-4b58a94896b7 | -7.65649 | -63.52304 | 2025-08-26 05:36:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ac97481a-f53c-3056-ac9b-d1eb20c5fc2d | -6.7719 | -59.66365 | 2025-08-26 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 69cf33b1-0548-31ee-ab52-c3746307a7dc | -8.55786 | -55.26001 | 2025-08-26 05:36:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c74aca23-cf81-3054-a655-25e8749dca6c | -7.37806 | -64.34919 | 2025-08-26 05:36:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 4eb971e2-ec18-3132-9131-408f6a6fb8ae | -8.14701 | -62.87399 | 2025-08-26 05:36:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4eaac510-fd9b-3f43-8fb8-7892bc56b5f2 | -7.56104 | -63.85357 | 2025-08-26 05:36:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b270637e-babd-3338-8b40-5c988d779ec4 | -7.55389 | -63.856 | 2025-08-26 05:36:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6f62812e-e26e-3e43-a009-d4f4e6a4b4a9 | -8.25388 | -61.46324 | 2025-08-26 05:36:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cf74c2d7-7bfe-3979-a5b6-2e1b23f1aba7 | -5.30955 | -60.20297 | 2025-08-26 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f7a1845b-4c91-3502-934b-ca8c0ce0bff0 | -6.35188 | -55.80249 | 2025-08-26 05:36:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5411afb2-662b-3e7a-b8f3-6d9ef1ca4ee7 | -7.5749 | -63.43493 | 2025-08-26 05:36:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dc8620ac-8b69-3d05-a36d-a60adef16b6f | -6.26325 | -60.01291 | 2025-08-26 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cfdb3c9e-ae8b-32a5-8089-2f25f53b83a0 | -7.88762 | -63.01376 | 2025-08-26 05:36:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| fe4f82f5-0982-33d8-86b1-0d0673c72d24 | -6.25731 | -60.00972 | 2025-08-26 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1f381092-5624-3659-88e3-ce213da31b7e | -7.07884 | -59.20647 | 2025-08-26 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5d5d3428-5600-36cb-98f7-e534e3588383 | -7.54943 | -63.84109 | 2025-08-26 05:36:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| db18d060-76c1-3dc6-b5dc-67ba63d21911 | -7.49882 | -63.815 | 2025-08-26 05:36:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| af527c83-48f7-3a76-a04e-14762505dd17 | -7.88037 | -63.01628 | 2025-08-26 05:36:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5880ce21-adef-39f0-8d11-b5935e2f1623 | -3.98419 | -51.05548 | 2025-08-26 05:36:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 08274f69-11b9-3b5d-9f87-359c2949b3ef | -7.4045 | -64.35335 | 2025-08-26 05:36:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2783231c-45be-34d0-b73e-ed8a5c8da065 | -6.91195 | -59.36163 | 2025-08-26 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 06b180df-3077-3a72-beda-d9ba4030ebe4 | -7.38358 | -64.35715 | 2025-08-26 05:36:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 55547cfa-470c-320e-a349-6b84247bc065 | -7.54289 | -63.86138 | 2025-08-26 05:36:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| eb5a1879-81e7-375e-8019-55f509775c2a | -6.82277 | -58.9612 | 2025-08-26 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ce8583fd-0835-3541-8c0e-66de460364c3 | -7.5388 | -61.38219 | 2025-08-26 05:36:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5863fac7-bbdd-3e2f-a2df-10e3d263f392 | -6.88151 | -59.89539 | 2025-08-26 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| af2f0dea-7ffa-3b19-9988-637722bb5acd | -6.62972 | -58.54488 | 2025-08-26 05:36:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d7c0fdb5-9144-3f2b-b7be-7971d4dbcec0 | -5.44451 | -60.15166 | 2025-08-26 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 08d395a7-f129-3611-bc74-cf8793b2ffa7 | -7.62563 | -61.03604 | 2025-08-26 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| c9bf1bdb-5c33-3d1a-938d-f37aa872323b | -7.37751 | -64.35265 | 2025-08-26 05:36:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 7708591b-ec89-3bea-925f-1b18369b0cc7 | -6.66403 | -58.79676 | 2025-08-26 05:36:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a3d3aaf9-7a82-3ba4-83ed-d26aba3831db | -6.31044 | -59.88261 | 2025-08-26 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d90daff0-0417-3e5e-b7b3-cdefa4ade4f7 | -7.65942 | -61.46937 | 2025-08-26 05:36:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9e1b9fe4-a0f0-3e05-b6bb-fbd1eede5f95 | -6.78973 | -59.67609 | 2025-08-26 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d6db0ffa-d819-3406-a9a5-932249af02bc | -5.52914 | -60.21099 | 2025-08-26 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| ff5ab548-57ed-3335-beb0-271c3776a56a | -6.76359 | -62.87719 | 2025-08-26 05:36:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d8efbf78-7c9a-327a-abf0-0643fabd5904 | -6.71373 | -58.5654 | 2025-08-26 05:36:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a778a018-b99d-36fc-ac65-59e918092522 | -7.39128 | -64.35127 | 2025-08-26 05:36:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 00a50c8d-1b72-346b-be03-abaee0b49be5 | -7.62143 | -61.03965 | 2025-08-26 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| f34c647e-2f58-39c2-bdb0-789a74134f39 | -5.43757 | -60.17272 | 2025-08-26 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dc27aa98-7d01-351b-90b5-e62f95b62597 | -5.53411 | -60.2029 | 2025-08-26 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a99a925c-988f-3524-8bae-a07524f61af8 | -5.30223 | -60.20186 | 2025-08-26 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 394fa238-66f6-34ce-b930-6328dde4cebd | -8.10889 | -62.87547 | 2025-08-26 05:36:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d3c18278-2fb5-3242-9b48-9dcbf30a3146 | -5.42721 | -60.16671 | 2025-08-26 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 77707e02-6844-35ae-88ea-8592accecdcd | -6.25951 | -60.01232 | 2025-08-26 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 418db1ac-7a6f-3b20-b7d0-555de63defb3 | -6.31246 | -59.86884 | 2025-08-26 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 51cd0a08-81e9-3f84-b057-01b49c4a55c7 | -6.78274 | -59.67014 | 2025-08-26 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| dd1c6cde-048b-3883-8b39-478201701bd1 | -6.9198 | -59.36285 | 2025-08-26 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| dbc4d491-6819-39e1-92a1-5af6d83478e9 | -7.88427 | -63.01324 | 2025-08-26 05:36:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| a81c7e37-3b1e-3110-bab0-987a72f93cf4 | -7.38743 | -64.35421 | 2025-08-26 05:36:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| bd7ec8f1-0cdf-3cfa-b7d3-c46b4752864f | -7.52602 | -63.37718 | 2025-08-26 05:36:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d827fb61-7694-373b-9e94-d90107a32296 | -6.57757 | -60.0697 | 2025-08-26 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5c278207-53c5-3732-89c9-4379138a32ef | -6.24319 | -60.01903 | 2025-08-26 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 33.1 |
| adc0c43d-8d57-3eaf-98fa-090cc7e8b648 | -8.12963 | -62.87499 | 2025-08-26 05:36:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1ccc9447-0123-39fb-b52a-1059587b40ee | -4.96335 | -55.80816 | 2025-08-26 05:36:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 2c9a7b7d-f137-320f-b19b-752f4f918a28 | -4.89479 | -55.81246 | 2025-08-26 05:36:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cae1cd5c-eec7-3d58-87a7-3e46c0704172 | -8.13519 | -62.86109 | 2025-08-26 05:36:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6756ade6-8289-33ce-8a30-04d41a83a6f9 | -7.38027 | -64.35663 | 2025-08-26 05:36:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 29b80da8-c5fa-390a-977e-476660b97da1 | -7.53138 | -50.54599 | 2025-08-26 05:36:00 | NOAA-21 | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 444c3f30-3871-3a15-aa17-b7e2f33c004b | -6.7132 | -58.56907 | 2025-08-26 05:36:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 014b3f88-3f48-332f-b68a-5770510984f2 | -6.83535 | -58.95953 | 2025-08-26 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e30046d1-f5f5-321a-9f6a-3d1250e049a0 | -6.26413 | -60.01541 | 2025-08-26 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e97ce8fd-520e-3888-873e-2ae7e928092f | -5.40757 | -60.17256 | 2025-08-26 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 0e67cd35-0548-39c5-9472-dceaa36de2ab | -5.52482 | -60.21476 | 2025-08-26 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3efad745-da92-3ac9-be61-20c985974547 | -6.65592 | -58.79555 | 2025-08-26 05:36:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 42d25966-0128-3c4d-8d61-b12e79a420f8 | -5.43692 | -60.17703 | 2025-08-26 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eb67022d-c896-32a8-b389-36f4c8e0523e | -8.11508 | -62.88012 | 2025-08-26 05:36:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.9 |
| d3a75247-b0d2-3e52-9216-49db9fd944ce | -7.87702 | -63.01577 | 2025-08-26 05:36:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 37ad5844-e9b1-3749-b773-ab68bb770709 | -7.48105 | -61.35704 | 2025-08-26 05:36:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 4f1301ea-63c9-3d89-8d29-9d9b81e54b0f | -8.12564 | -62.85592 | 2025-08-26 05:36:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5bcbe69b-fdb8-30fc-b84e-e25fdc56f551 | -7.52934 | -63.37769 | 2025-08-26 05:36:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 04aaceb9-6721-3d12-bbac-3c622953d86a | -3.98444 | -51.05636 | 2025-08-26 05:36:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 967df0b1-05b3-34d2-b89c-277aa5eb67a2 | -7.62321 | -61.04086 | 2025-08-26 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 196b8fc3-ae20-3b7b-9ae1-deae7fefe335 | -8.11171 | -62.8796 | 2025-08-26 05:36:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 3024f0d4-c249-3baa-9dd5-b049121d8884 | -4.93748 | -55.82514 | 2025-08-26 05:36:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d7da1a35-ef55-3c47-925f-38bb4c1d9222 | -7.57158 | -63.43442 | 2025-08-26 05:36:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 55d5fda1-7217-38f3-abb8-5a9931572750 | -7.6598 | -63.52356 | 2025-08-26 05:36:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |


[Clique aqui para ver as próximas entradas](README77.md)
