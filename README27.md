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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fdda9b09-0493-3894-81a8-1077467d8c77 | -7.79031 | -66.9541 | 2026-09-04 05:23:00 | NOAA-21 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8311d464-4e67-3146-b41b-33c1c0478721 | -6.69773 | -59.98106 | 2026-09-04 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ec9881fa-6a69-309b-b3a5-069ff3d06b84 | -7.56032 | -61.34291 | 2026-09-04 05:23:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4a706aaa-22e4-3a73-ba8e-0ed9038e7550 | -7.58924 | -57.6901 | 2026-09-04 05:23:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e745bcd7-5d2b-3efe-ae00-f3bb733bae88 | -6.64697 | -59.45229 | 2026-09-04 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1505706a-44fc-33f1-bf71-9f300306bb7e | -8.89958 | -62.36327 | 2026-09-04 05:23:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 96569c84-827c-329a-b891-7a1e150e0cd5 | -7.42808 | -61.72952 | 2026-09-04 05:23:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b63e6cea-7c08-3630-b78f-45b6a7966d5e | -6.99767 | -62.99101 | 2026-09-04 05:23:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c6ad1a4d-89e3-3542-8afc-6f751f37e07d | -10.50152 | -51.3285 | 2026-09-04 05:23:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 9f69e095-d40e-378b-8a25-a74ae34de917 | -6.68906 | -59.95054 | 2026-09-04 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a9ce1271-933e-3525-a63f-1aea3430d1c1 | -7.98063 | -61.15731 | 2026-09-04 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f3118e6e-73ad-3970-82c0-89f4a9688767 | -6.69524 | -59.97655 | 2026-09-04 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 10.6 |
| d7f2a1bb-521e-3819-a707-16a1b634eb13 | -6.68913 | -59.97203 | 2026-09-04 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 08472f49-f0f6-3405-81be-90cad476b9a2 | -8.43726 | -54.69624 | 2026-09-04 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0b028210-7a0e-368e-b550-2aa60e3d902d | -8.10545 | -54.78583 | 2026-09-04 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 17ce4a4e-4dc5-375f-ac51-b121ed4633d6 | -6.68624 | -62.85307 | 2026-09-04 05:23:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9a866ead-da4e-3d34-9371-42130b93815f | -8.11921 | -54.78673 | 2026-09-04 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| d4bd740e-3dff-3732-a381-f49d3d08a2c1 | -8.10667 | -54.77732 | 2026-09-04 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e8b3ab9a-23aa-3c9e-9841-9591c8cb3378 | -7.57015 | -61.3018 | 2026-09-04 05:23:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1b175ae9-9b34-32b3-99e6-49e3d281ec3a | -6.13076 | -59.8892 | 2026-09-04 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 36dad37f-0ed7-3ac7-b9f2-a53af1cbe9ce | -8.0741 | -55.33461 | 2026-09-04 05:23:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a1607dfa-e2ab-3cc7-a3e9-dec6330e8946 | -3.44684 | -56.31937 | 2026-09-04 05:23:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1c35983a-7a45-36d0-8608-9a361fa0d0c9 | -8.42979 | -54.71713 | 2026-09-04 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 29b44f85-fd0d-385c-82a7-00f34d353f52 | -7.4728 | -63.74902 | 2026-09-04 05:23:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| de51eb1a-8b47-3f62-9e7b-f7ec32a34311 | -6.13794 | -59.88674 | 2026-09-04 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8c5db806-1828-3be6-93ef-a2904815c048 | -5.85385 | -61.16387 | 2026-09-04 05:23:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9558a51f-0228-3875-b2f7-01b08837ed6d | -6.60028 | -59.11708 | 2026-09-04 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d4c9111b-35f6-3c24-b71d-67f82ad4b318 | -3.18451 | -60.24777 | 2026-09-04 05:23:00 | NOAA-21 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d9277fa3-c1c0-3344-9168-4392a93cbabf | -6.68403 | -59.93903 | 2026-09-04 05:23:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5abfe20c-1cf5-353b-b773-ef64eb50e578 | -3.44379 | -57.79709 | 2026-09-04 05:23:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 056cabc4-f9d7-3d26-bcf3-64d398cc8cd4 | -7.46571 | -63.74786 | 2026-09-04 05:23:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| df2f576c-8b6b-3164-9302-8fbb80bfc950 | -6.6896 | -59.94704 | 2026-09-04 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9e53388c-3502-3455-b733-1437f99b4ae9 | -6.97246 | -59.78584 | 2026-09-04 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7b9263c4-9556-37e1-96ea-07f9a3222689 | -6.69939 | -62.85903 | 2026-09-04 05:23:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5fbfd05b-aab9-3214-b7e1-415f0a000133 | -3.0818 | -61.18379 | 2026-09-04 05:23:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7fe4017d-f198-3a3f-bd5c-828f25bb7e65 | -4.36495 | -47.78091 | 2026-09-04 05:23:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 04f8981d-9c5c-3e4c-8a52-11add04450eb | -7.27885 | -60.64192 | 2026-09-04 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6912a423-8f54-3982-b87a-162781bd734c | -6.68472 | -59.97852 | 2026-09-04 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 27.7 |
| bfd7cc73-6d2e-3464-8ecf-cca7d018098a | -3.3323 | -58.15415 | 2026-09-04 05:23:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| bcc7f01b-eed9-31e5-8d6f-91fcbfa326a1 | -7.55754 | -61.33896 | 2026-09-04 05:23:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 44ba0653-7d37-39a1-a570-1b9e1bd533ee | -6.53456 | -59.93753 | 2026-09-04 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e72d5884-feb4-3937-bd9b-a7281a456d15 | -6.69191 | -59.97604 | 2026-09-04 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 0d9eed36-45d9-3baf-84e0-e8157501f438 | -6.48509 | -61.71267 | 2026-09-04 05:23:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b4d1262a-5bc3-3beb-ada8-d37028947a08 | -8.44138 | -54.69524 | 2026-09-04 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d9cb6798-ec54-3e85-87aa-11f7001963ab | -3.02667 | -61.49015 | 2026-09-04 05:23:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0fa2e5f6-eaeb-370b-b7fe-bb9e60379b46 | -8.52039 | -67.15791 | 2026-09-04 05:23:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 78a56649-f4e2-3335-8dde-849e965d53ec | -10.50729 | -51.32892 | 2026-09-04 05:23:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 33.6 |
| 4e61a699-448c-3200-a2bd-332ad667d14d | -6.37347 | -58.28397 | 2026-09-04 05:23:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 31def174-edd0-3a0e-af2a-fdf737369e59 | -1.74154 | -54.98926 | 2026-09-04 05:23:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 452ba4d7-cb7d-3183-bc3c-f81f9b9d3edd | -8.11358 | -54.79145 | 2026-09-04 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 72aadb36-a786-3442-8e06-d50b8e60def9 | -3.0941 | -61.19295 | 2026-09-04 05:23:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1670561a-a4e6-381a-b1bf-faf535006114 | -6.87657 | -59.396 | 2026-09-04 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3b61940d-c9c2-3d7b-89d1-6000ac1d1815 | -3.07673 | -61.08522 | 2026-09-04 05:23:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| fd1dcd89-915d-3b23-a4a3-411a1d825d3c | -6.69416 | -59.98354 | 2026-09-04 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 13.3 |
| e249b1df-19c3-35d2-817e-af64c69960c7 | -7.00451 | -56.51958 | 2026-09-04 05:23:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2139e6b2-4578-3e11-8a35-e3e0c8f53be1 | -1.24813 | -54.53478 | 2026-09-04 05:23:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e698c035-b3df-34c9-a59b-2b808c0240b6 | -6.67855 | -58.76667 | 2026-09-04 05:23:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fbcce2b1-d7de-381e-b866-a53d4ac8be97 | -8.11672 | -54.80068 | 2026-09-04 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1f5582aa-9273-3a8a-8809-d165f8369afe | -3.47234 | -58.4322 | 2026-09-04 05:23:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c54766ac-720a-3e84-812b-28ab7fa923db | -10.00586 | -50.28645 | 2026-09-04 05:23:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 2b90df5e-58f8-3955-ae65-112f6181bdb5 | -9.50956 | -60.50484 | 2026-09-04 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6d76b4d1-a53c-32ab-aaa1-98339d76bcdd | -8.90292 | -62.36381 | 2026-09-04 05:23:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 46b7b95c-49d7-33f9-a46c-76b0dcb1eeee | -6.67792 | -59.9345 | 2026-09-04 05:23:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 881a49bc-2d23-36be-93f1-ae517e8cb137 | -6.52737 | -59.93999 | 2026-09-04 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| af5047d9-4ab5-3e74-b435-bf335c1fe778 | -3.17686 | -61.16279 | 2026-09-04 05:23:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e45a6a0f-0f9a-3943-b562-4bcaf39139bf | -6.68751 | -59.98252 | 2026-09-04 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 4ab74291-db5e-35d1-887d-b9e9466d3057 | -3.01653 | -61.48857 | 2026-09-04 05:23:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 236a7fa1-637f-3b5b-813d-66afffa0392a | -8.71521 | -62.94607 | 2026-09-04 05:23:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 50d05312-36f2-3b20-9cf4-90812e8e6d58 | -8.75436 | -62.83909 | 2026-09-04 05:23:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bf0c55a9-10a8-3363-a77c-6ab6d3c10d23 | -8.52396 | -67.16271 | 2026-09-04 05:23:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 297eceeb-2545-3b52-911a-19dc70aa92b6 | -2.9919 | -61.26089 | 2026-09-04 05:23:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2c751c99-bdbe-3204-8b93-b4c49d88b5e2 | -2.94723 | -51.29155 | 2026-09-04 05:23:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cb2e1bc6-7079-3c6c-97bd-33ccfca06f3a | -6.67359 | -59.9625 | 2026-09-04 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 9ed247e2-5a8a-3201-af62-9e207bc74ada | -6.11996 | -59.9589 | 2026-09-04 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fb5a11f1-2fb9-35fa-b0f9-9df4eb52d011 | -6.96804 | -59.79239 | 2026-09-04 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 762937e1-492a-3e5e-92aa-b1b11fd4b3c0 | -8.49236 | -54.65303 | 2026-09-04 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 3f76b27d-b47f-3c4f-851e-f6c831050418 | -3.18188 | -61.1527 | 2026-09-04 05:23:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e4cfda03-975f-3518-b8e7-fc5073ca28dc | -7.58561 | -57.68954 | 2026-09-04 05:23:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8813819f-57bf-394a-af2e-1fdb63af59d9 | -6.68573 | -59.95003 | 2026-09-04 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 53facf8d-1b96-3254-b9ba-e4ea71e982e0 | -7.72422 | -61.12355 | 2026-09-04 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3767929a-9ec4-3db1-b7ba-58b210eb189b | -7.08425 | -56.51232 | 2026-09-04 05:23:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 86bfdca2-8185-3c05-8e79-296c7268ebd5 | -7.27211 | -61.11946 | 2026-09-04 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2da68113-6ed0-374f-952f-b61f8989c41d | -7.78604 | -66.95338 | 2026-09-04 05:23:00 | NOAA-21 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 02219305-9e8c-31bf-b10d-61ad21cef267 | -8.55662 | -63.19173 | 2026-09-04 05:23:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c8bb6b78-4794-343e-bb72-f96067672f31 | -8.48914 | -54.64347 | 2026-09-04 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4180b4d3-428a-390c-b16a-c061a44c8ec5 | -6.70223 | -62.86333 | 2026-09-04 05:23:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d6d8f69b-35ed-3ba3-9dc9-07cbe0be465f | -8.91799 | -62.35527 | 2026-09-04 05:23:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d75e1b07-95c3-3ea2-893a-4d0d73c740c5 | -6.15084 | -59.93513 | 2026-09-04 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a2d81700-2904-341e-984e-ffb0e9aef12c | -6.65423 | -59.44976 | 2026-09-04 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e84972d4-f4b3-382c-95bd-39bd0a1c3ae3 | -7.79956 | -62.34834 | 2026-09-04 05:23:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b6275e84-32e8-345c-9332-352fbf242a6d | -6.53177 | -59.93353 | 2026-09-04 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 71f816f3-78e8-33cd-abc1-aa83a5af3dd0 | -8.83407 | -62.30555 | 2026-09-04 05:23:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d15f63b7-f1d1-35fb-bf29-fddb53d4df6c | -8.20531 | -62.79631 | 2026-09-04 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c2ccfb4e-9081-3616-b518-308866eaf396 | -8.78387 | -62.55777 | 2026-09-04 05:23:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 56173206-17f1-3edc-9588-1a683c66375b | -8.49558 | -54.66262 | 2026-09-04 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 1e57345f-fa08-3f47-89d3-09e616e9db7b | -7.08355 | -56.51707 | 2026-09-04 05:23:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 076f681d-d743-39e6-b6b8-4f7a40609e16 | -8.50246 | -54.64558 | 2026-09-04 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 3b9bb7e2-0da4-3d59-bf14-c900569d489c | -6.79443 | -58.95077 | 2026-09-04 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 47edf02f-951d-35ca-931d-4a9887263021 | -3.33287 | -58.15047 | 2026-09-04 05:23:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9942e1c4-16a1-31ce-b37f-f4eb3f4a8504 | -6.64189 | -59.44062 | 2026-09-04 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |


[Clique aqui para ver as próximas entradas](README28.md)
