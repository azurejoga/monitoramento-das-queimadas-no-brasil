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
| 1d6e8a4d-d051-3ba6-b7d3-5e107a7ae510 | -10.33733 | -64.47529 | 2025-08-16 05:53:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 62ccd349-aa86-3d22-a581-c3ad0ae12c4e | -10.04807 | -59.11705 | 2025-08-16 05:53:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d7998c33-399d-366c-a984-c7a62fc37b92 | -9.81601 | -63.01163 | 2025-08-16 05:53:00 | NPP-375D | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 50baf1da-9a05-35e7-b54d-605356324e73 | -14.95304 | -54.75352 | 2025-08-16 05:53:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| ac252753-2815-317e-a20d-4788e8314a75 | -13.00033 | -56.86204 | 2025-08-16 05:53:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4b350be1-b55e-37e6-9e56-7efe9428bf5a | -14.94867 | -54.76042 | 2025-08-16 05:53:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d3641dd8-bf11-363b-b981-076efd1bab60 | -13.12549 | -57.12774 | 2025-08-16 05:53:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 34199c79-b556-3977-8aed-bd4200934858 | -10.04258 | -59.11932 | 2025-08-16 05:53:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 13337341-c2fe-3108-b454-1223c4b1c97f | -11.73702 | -64.89762 | 2025-08-16 05:53:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 79bfe907-0a86-3967-a2aa-e4f3f92c47e9 | -14.94217 | -54.75329 | 2025-08-16 05:53:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 54d5cc32-9143-32b6-a64d-9c48be56ad37 | -9.28699 | -68.2622 | 2025-08-16 05:53:00 | NPP-375D | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2b2418aa-3997-32e6-ba5f-f9da49f72413 | -9.827 | -63.01486 | 2025-08-16 05:53:00 | NPP-375D | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 19dbc852-974b-3f44-8c52-2792ce6b1f5b | -10.00877 | -59.22105 | 2025-08-16 05:53:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 552afdde-3989-37ce-a0e4-40f4f29e05b6 | -13.12051 | -57.17274 | 2025-08-16 05:53:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4d9fb41c-6eca-3d91-8425-15580f6511b1 | -8.37489 | -70.14725 | 2025-08-16 05:53:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4f4c751e-4f43-3b9d-90eb-4f63c4f30418 | -9.0439 | -67.42844 | 2025-08-16 05:53:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 3b5e22b4-a388-3a21-bb96-d9f2e90ef8e8 | -9.34431 | -62.58556 | 2025-08-16 05:53:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 9d74f789-fb2d-3c6f-93bf-6104e442e8ae | -13.13966 | -57.16603 | 2025-08-16 05:53:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9a1a55cd-ea3c-374b-9af7-6bc4a4e57101 | -20.2025 | -47.6271 | 2025-08-16 06:00:00 | GOES-19 | BURITIZAL | SÃO PAULO | Brasil | 3508207 | 35 | 33 | nan | nan | nan | Cerrado | 60.8 |
| 95a73b9e-0cbb-3169-9f68-23b2986ea652 | -8.9709 | -61.6842 | 2025-08-16 06:00:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 869ce0c3-daa2-3024-9fb3-e00e537bb2d2 | -6.9486 | -59.549 | 2025-08-16 06:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 49.3 |
| 8e99c1e4-da9e-3ede-ba3a-15051f6ae308 | -9.1709 | -59.6374 | 2025-08-16 06:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 031e292c-addf-3028-a9e9-d4e8611ab1e5 | -6.9487 | -59.5297 | 2025-08-16 06:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 50.2 |
| 365d1a46-02b8-312a-9db8-cf57b3a31363 | -14.9441 | -54.6959 | 2025-08-16 06:00:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 57.8 |
| e27974ff-cbda-35d3-bed4-c9ab77d875e8 | -6.545 | -43.0373 | 2025-08-16 06:00:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 68.0 |
| a798169f-c4e6-3d37-a5c7-0c40e53e513f | -6.5638 | -43.0357 | 2025-08-16 06:00:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 117.7 |
| 33ce55e1-7996-3756-a958-345e0b037a65 | -6.5641 | -43.0122 | 2025-08-16 06:10:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 51.4 |
| b074d96a-4774-3a9d-8a90-2aebaa67fa8e | -6.5636 | -43.0592 | 2025-08-16 06:10:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 65.5 |
| b2566f5f-b8c6-3cf3-807e-41d729234b82 | -9.1709 | -59.6374 | 2025-08-16 06:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 3abf57c2-a3ff-3618-99af-d5c5cfcfdc66 | -8.9708 | -61.7033 | 2025-08-16 06:10:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 49.4 |
| aea24a35-720e-35dd-ba19-70a15d5a22ac | -8.9785 | -60.5349 | 2025-08-16 06:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 69.1 |
| a0c09b3a-56e6-3483-8c96-3830a626e1e3 | -8.9787 | -60.5156 | 2025-08-16 06:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 74.5 |
| 0efac5cd-fd62-3826-b0f6-3ee1289f0d54 | -8.9974 | -60.4955 | 2025-08-16 06:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 77.2 |
| 74f195b9-576a-34ce-a272-252ae54cd6bd | -8.9709 | -61.6842 | 2025-08-16 06:10:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 77530f15-5245-39ff-97a6-56343edad8f4 | -8.9973 | -60.5147 | 2025-08-16 06:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 94.6 |
| bf362ae0-5e08-3e29-96f3-286d89be258a | -6.9486 | -59.549 | 2025-08-16 06:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 39.9 |
| 5c784f58-64f5-3e33-aba7-75880430c0ee | -6.5638 | -43.0357 | 2025-08-16 06:10:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 165.9 |
| 4731bdc9-650c-341d-9afe-515b0dc60b0e | -8.9788 | -60.4964 | 2025-08-16 06:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 65.1 |
| bcb150c6-168e-3de2-bc5b-6b29f864d9c2 | -8.9971 | -60.5339 | 2025-08-16 06:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 92.2 |
| f16d51b9-1cc2-3877-932a-89e0fae6a0d2 | -6.545 | -43.0373 | 2025-08-16 06:10:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 88.0 |
| da290cac-6a71-3234-8d0d-033328e1d61d | -6.9487 | -59.5297 | 2025-08-16 06:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 41.6 |
| 42eb36cf-3099-3e94-9f6c-51716d8e0ca7 | -6.07843 | -59.95296 | 2025-08-16 06:12:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4d8dd754-3b1c-3c10-b219-a54328d19c1a | -6.07758 | -59.95938 | 2025-08-16 06:12:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6bb5620d-6e6b-307b-9bf6-7e472038d145 | -6.07674 | -59.96581 | 2025-08-16 06:12:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d1c47102-bc42-3d86-a93e-fea595f3be97 | -8.98198 | -60.52309 | 2025-08-16 06:14:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 9d9312d4-1dcc-365f-ae72-73dd2364f11c | -9.03326 | -67.43079 | 2025-08-16 06:14:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bfa53c3e-85ba-38c0-9eb0-078194b183d8 | -7.91757 | -61.74842 | 2025-08-16 06:14:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 676f3679-db47-3841-a063-a044f2dc2557 | -8.9741 | -61.71085 | 2025-08-16 06:14:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 9.7 |
| d4869e5e-bc2d-30b5-8d47-71a103fae1cb | -7.95109 | -61.75418 | 2025-08-16 06:14:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ba882474-eb89-3b63-956b-4fccd8fa9bcd | -8.96387 | -61.68743 | 2025-08-16 06:14:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 057e39a3-53d1-37fb-bf7a-46fdde48e50a | -7.82673 | -61.3286 | 2025-08-16 06:14:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fc749c9e-db96-37b1-9040-69f3cd7a4c5c | -7.9253 | -61.73901 | 2025-08-16 06:14:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d42a1bdb-0239-3c6f-9608-949de38db221 | -7.5297 | -61.32747 | 2025-08-16 06:14:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 561a8a95-8ed0-3f9a-8e4d-f2786156e7ed | -9.39252 | -60.54649 | 2025-08-16 06:14:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8ba3866e-9e82-3be1-b2d5-97f225aeb09f | -7.95279 | -63.21368 | 2025-08-16 06:14:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 32a8a341-9421-3ef0-bfdf-c1657c2885e9 | -8.99751 | -60.51169 | 2025-08-16 06:14:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 7f2e3b7a-0548-3720-800b-e098cf930d1f | -8.89222 | -60.74011 | 2025-08-16 06:14:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 404fc739-3702-37d8-8b08-ba147ddad9d6 | -9.0478 | -67.4239 | 2025-08-16 06:14:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 1953babd-6171-3c8f-9121-90fbf142c51c | -9.38553 | -60.54573 | 2025-08-16 06:14:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| be0034b0-85e7-39e9-a1ec-c8a98ee42c38 | -10.67894 | -69.48528 | 2025-08-16 06:14:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e093a9dc-3d7e-3f36-a0cc-c33fed39cb53 | -7.61703 | -63.34004 | 2025-08-16 06:14:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a2f0ec93-238d-3e39-8d02-e5c9ff429a57 | -7.61155 | -63.32745 | 2025-08-16 06:14:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 41bc909a-eb81-3fa8-b0ef-e57f260afa32 | -6.93706 | -59.54039 | 2025-08-16 06:14:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 02063fac-9a32-3106-84fd-2c99cd79a2f6 | -7.62361 | -63.325 | 2025-08-16 06:14:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d2379511-ed64-3293-ae93-610dbf8ed7a4 | -8.05805 | -70.58793 | 2025-08-16 06:14:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 46a5b277-b39d-3f08-8b3a-ecc2ae6d2c14 | -8.9844 | -60.50316 | 2025-08-16 06:14:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| fc418fb5-1e08-3436-8a13-c230a345138f | -9.50085 | -60.52076 | 2025-08-16 06:14:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a1846e34-c521-3282-82b9-2b1104fa81ab | -8.10873 | -61.19709 | 2025-08-16 06:14:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c5f30c60-6992-3601-9aef-f7071412b290 | -7.61045 | -63.33548 | 2025-08-16 06:14:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e60e2d5f-070c-34af-a92a-19cf6861a53f | -7.52467 | -61.31527 | 2025-08-16 06:14:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 1a451057-6b67-38f1-af11-d133ee8e4aed | -8.99667 | -60.51855 | 2025-08-16 06:14:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 5bd5c460-d60b-37d4-91d5-dabdc2442c22 | -8.97479 | -61.70539 | 2025-08-16 06:14:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 9.7 |
| afe4fe3f-bbc4-31b5-a927-cb9a6ae2d7c9 | -7.95042 | -61.75945 | 2025-08-16 06:14:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ff2034a9-6d9a-3356-b37d-6099b80c389d | -9.51171 | -60.54871 | 2025-08-16 06:14:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 81c5d622-3a39-3dcc-ae70-674969abf6fb | -9.5047 | -60.54803 | 2025-08-16 06:14:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b333769d-229f-3c0b-80ff-3a87e1e9727a | -8.99427 | -60.53812 | 2025-08-16 06:14:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 2a125ce6-637a-3e29-8f48-749276d9a436 | -8.98522 | -60.49644 | 2025-08-16 06:14:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| b3e0e7de-7c18-3e5c-a403-a1a144307a00 | -6.93543 | -59.53349 | 2025-08-16 06:14:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 7e34e399-4a14-3e08-9ab8-91e4baeaee21 | -11.73054 | -64.89825 | 2025-08-16 06:14:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1b009026-13a1-3a60-ba5d-c926e785905f | -9.38612 | -60.55239 | 2025-08-16 06:14:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a65cddfb-9f9d-3501-b74a-f7fb5f5a68f4 | -8.97856 | -60.50237 | 2025-08-16 06:14:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| c413425a-e1ca-3afc-a3f3-6a8e419fddbc | -7.43812 | -60.0239 | 2025-08-16 06:14:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| c749a7d4-6923-3e07-8abe-b4f7caf8f935 | -8.05868 | -70.58376 | 2025-08-16 06:14:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 23be57b0-5bb2-3f79-9d64-6cc537d831e1 | -8.55597 | -63.93193 | 2025-08-16 06:14:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3e30bec0-8b5f-3982-b64e-d43a38ab0fe9 | -8.98059 | -61.71166 | 2025-08-16 06:14:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 28c55525-122c-3575-ac75-bc45deee97b0 | -7.94881 | -61.75773 | 2025-08-16 06:14:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0f1fa6c9-4d3b-3f32-9052-b12fd57bb5d4 | -8.14851 | -62.77707 | 2025-08-16 06:14:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 006bef7e-fa50-3826-bfe9-ac9c9acccf97 | -7.56223 | -61.43121 | 2025-08-16 06:14:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7722356f-5a9f-3508-a210-7dcec97c776d | -8.99348 | -60.54452 | 2025-08-16 06:14:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 10.7 |
| c21a1343-5f20-300e-b21a-b75166aab398 | -9.28357 | -68.26218 | 2025-08-16 06:14:00 | NOAA-20 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 900d00d7-932d-3eea-aadd-38511ae3a59f | -6.94421 | -59.54167 | 2025-08-16 06:14:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 0019e651-1b5b-32a6-a96f-b683b6f597e2 | -7.9518 | -63.21815 | 2025-08-16 06:14:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8d8ec916-1f53-303f-96fc-2bb924634c89 | -8.46733 | -64.0533 | 2025-08-16 06:14:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 959273f2-f8c9-3341-a557-4e18b48096e8 | -8.6579 | -70.0422 | 2025-08-16 06:14:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d468befd-7071-3aa3-80a6-4fe238769341 | -8.37135 | -71.10007 | 2025-08-16 06:14:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d33fa8e5-93f7-316e-b67b-b4baf1ecd73f | -7.91825 | -61.74326 | 2025-08-16 06:14:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 73e5d1ba-20e7-30c2-aebf-4ccdc0b06256 | -8.97743 | -60.50233 | 2025-08-16 06:14:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 02f5cdb4-045d-3911-afe0-50e599e61e89 | -7.61755 | -63.33602 | 2025-08-16 06:14:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2658b3b6-f348-3b5c-927d-3d96dc5cb6cd | -6.9326 | -59.55506 | 2025-08-16 06:14:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8f4bb67b-c9f2-3987-8e21-61c299215ca2 | -7.67306 | -63.31499 | 2025-08-16 06:14:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |


[Clique aqui para ver as próximas entradas](README72.md)
