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

## Dados Diários - Página 66

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 550411bf-a09a-3d81-809c-38416a4dc3e3 | -5.43544 | -60.17416 | 2025-08-25 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 8.8 |
| a064a29d-5009-3640-8e1b-e9c6c5d037bb | -8.98679 | -65.41819 | 2025-08-25 05:04:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 352715f4-c01a-3156-a58e-ff112c8aee2e | -6.90839 | -44.41817 | 2025-08-25 05:04:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 48e99fcb-db0b-34b4-ac66-1157ab51c722 | -12.73586 | -48.13807 | 2025-08-25 05:04:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7756ee17-0729-32b1-97fd-f21ec8516762 | -8.22162 | -61.37873 | 2025-08-25 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| ab3ca2a8-abe8-31f2-be69-c954007f11bb | -5.74428 | -57.58352 | 2025-08-25 05:04:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 38221d9c-f45c-3c20-9b53-ede3eabfadc7 | -9.22676 | -59.67766 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3ee0f5c0-44ea-3be9-8149-162e79e4bc98 | -7.32896 | -44.54128 | 2025-08-25 05:04:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7bc9515e-58bf-365b-bdf3-8f0273a57385 | -8.97575 | -65.41946 | 2025-08-25 05:04:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 59cf137b-2c08-3128-b047-918850c6cb1c | -12.75107 | -48.13767 | 2025-08-25 05:04:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a2fa1fed-d233-3bb2-9a9e-ff6cd5dcf7dd | -10.46557 | -48.32109 | 2025-08-25 05:04:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3a11032e-199c-3aa9-b787-f7bc96b0894a | -6.77485 | -59.6582 | 2025-08-25 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 252f6190-a67e-3596-be5c-566b8c6c8a04 | -5.41915 | -60.17451 | 2025-08-25 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6a35cd31-6fec-3795-b396-ef966e57b422 | -7.35297 | -57.6312 | 2025-08-25 05:04:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1b0dba20-8a43-39b6-8e65-55bc5d8367a8 | -9.18994 | -59.64685 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 67a27995-ee3d-3ba6-8458-146803384130 | -6.82779 | -58.95323 | 2025-08-25 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| b489f1b4-dfed-3c35-bd1d-72a48a4762e3 | -9.04336 | -65.7253 | 2025-08-25 05:04:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0a07b1bf-c6f6-3aa8-a413-4c16fc041047 | -8.22304 | -61.41949 | 2025-08-25 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fe276ad6-ca2d-3cbd-80e6-b50437ab1c96 | -8.22589 | -61.42731 | 2025-08-25 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 48011490-d1b6-3a8e-812d-02ac5b197238 | -9.19811 | -59.50754 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cb558755-99ae-3ac6-b641-725965cf5507 | -9.16746 | -60.80763 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7b9f3123-ce36-39b9-83dc-c561951e49c2 | -5.41134 | -60.17322 | 2025-08-25 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 40d9118d-4e72-33e3-a8d6-b00e9be3748f | -8.91463 | -62.4285 | 2025-08-25 05:04:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 259664bc-6b5a-3457-9172-a2bac3153cc7 | -12.73479 | -48.13858 | 2025-08-25 05:04:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4ec0077f-c646-3b7f-9d7e-9ff1aa27fa1a | -8.21729 | -69.86311 | 2025-08-25 05:04:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 48c051fd-4e1e-3bad-b1eb-4880ef4a7411 | -8.87398 | -62.45916 | 2025-08-25 05:04:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 56.3 |
| 1e0e398c-84ed-3fd6-89ed-41818749cd69 | -7.29821 | -59.66327 | 2025-08-25 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9fce1d08-0ff5-3b30-8b84-0a37bca81a8f | -10.40345 | -57.69216 | 2025-08-25 05:04:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 706b870c-9ef8-3b5c-afe5-09eecef4de1d | -8.61114 | -62.64322 | 2025-08-25 05:04:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| fb0a67f0-7f57-302c-a9e3-7b28a70bf624 | -6.79231 | -58.64193 | 2025-08-25 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 117deb97-d011-3eb5-bfda-bbd5c88117a4 | -8.65054 | -63.43259 | 2025-08-25 05:04:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8adbfd5b-07e2-3504-ad53-02d3b6620231 | -11.18208 | -55.02826 | 2025-08-25 05:04:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5e35b49b-f6fb-341e-8d9d-538f82a8cb70 | -9.1379 | -60.77255 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d52b8e0a-c086-3610-83dc-8967e652e7f4 | -8.87255 | -62.46735 | 2025-08-25 05:04:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c231969f-3cd8-3168-b1e4-c4e86315ab6d | -9.20729 | -60.92441 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f5d1d10d-9f0e-3b22-806a-3560beb7f19b | -12.93982 | -46.31216 | 2025-08-25 05:04:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2a6749c9-e586-340d-85f2-3b54526e786f | -8.10855 | -62.87518 | 2025-08-25 05:04:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 55c35fb9-d207-32d1-828e-d24c8ba00c39 | -9.47228 | -57.82372 | 2025-08-25 05:04:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 8.7 |
| af985d0d-615e-3aa6-833d-12e3c3a3d7b1 | -5.42306 | -60.17516 | 2025-08-25 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 446adbb6-5b29-3ba2-bda6-dacebadc2511 | -6.81333 | -58.9609 | 2025-08-25 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| bdabc197-cff4-36ce-8e55-4e9f24bc69a0 | -7.91979 | -45.89394 | 2025-08-25 05:04:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2f729cc3-a7bd-3ac7-a7fd-4855bbd66d38 | -8.22649 | -61.42374 | 2025-08-25 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5a054436-ce4f-30fc-9c2f-88c84dd0e978 | -6.78016 | -58.62772 | 2025-08-25 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 670752d4-f36c-32cc-95ec-ea84fda0cfb5 | -9.70856 | -54.98136 | 2025-08-25 05:04:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fe95548e-fb65-3af8-8cf7-33daf6487f7a | -9.19468 | -59.43939 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e3d70d3c-1b53-348a-a968-4f87dc86753e | -9.47286 | -57.82012 | 2025-08-25 05:04:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 13.5 |
| a4cb791f-0fb9-3190-8d35-0187c95d2b30 | -7.5275 | -63.81116 | 2025-08-25 05:04:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| b210a0e6-84a5-39b5-94f1-da4285734210 | -8.50548 | -63.87188 | 2025-08-25 05:04:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 80163627-6598-3f05-9eba-4a326bad7a02 | -9.18789 | -59.48041 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 275e447b-e140-38d5-92bc-6ca00237eb88 | -4.96668 | -55.82154 | 2025-08-25 05:04:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f7a81d26-0cb9-30ab-8391-311d9c3ecfbf | -8.59791 | -62.61136 | 2025-08-25 05:04:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a0563cf7-e9c6-3227-8c48-c569748eb377 | -12.75439 | -48.11009 | 2025-08-25 05:04:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 597c43c4-8be9-38d8-bd2a-a448cd1bb7e9 | -12.75067 | -48.14096 | 2025-08-25 05:04:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 11.0 |
| dfe63cdf-fd47-32c0-b258-17ecd43e5732 | -9.21459 | -59.70584 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d4e86dff-6d38-3991-89f5-06b492f75170 | -11.19654 | -48.46972 | 2025-08-25 05:04:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4220035c-3bd3-30fd-9e1b-6ab22de1f32f | -9.19707 | -59.4693 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6ab205a4-0bd7-3819-a790-9359fbe370d6 | -9.04274 | -65.72865 | 2025-08-25 05:04:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b27a250b-57c9-32ca-ae57-4fb055a61da2 | -9.81496 | -64.2583 | 2025-08-25 05:04:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 53e2633b-b373-3a12-9b6a-f7e9bc90ccd4 | -7.20422 | -49.61185 | 2025-08-25 05:04:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ec595356-c2cb-34b7-9944-da5584d4d60c | -5.41995 | -60.16958 | 2025-08-25 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 7c8d6cfe-8bbe-33e6-acfb-b2c6772e4a28 | -6.52632 | -44.43018 | 2025-08-25 05:04:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4e5ccf74-995e-3347-b816-bd2409bd758c | -9.03802 | -65.72436 | 2025-08-25 05:04:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 61b0fd35-8813-39a4-aa79-f82859711214 | -8.90324 | -62.44336 | 2025-08-25 05:04:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1e7caba7-b110-3888-b6a2-0b554515e4fd | -7.90845 | -63.06913 | 2025-08-25 05:04:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 148481ad-2338-3294-8192-a68cf8c7d3d8 | -6.83272 | -58.94565 | 2025-08-25 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e4a4a859-009e-36dc-bf4c-5baa0b0ef9eb | -6.77113 | -59.65759 | 2025-08-25 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 8cbbfedc-5566-3b8a-9beb-3019b8f870bb | -9.25973 | -59.76955 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 913c30a1-73bf-36b8-b2cf-879ff5db0d10 | -9.20343 | -60.92372 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 927f926f-f4ce-3e29-9ad1-a0f010b6b9f0 | -8.98619 | -65.42142 | 2025-08-25 05:04:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 02e37f1a-1f55-32c2-b6df-bc19d8a96530 | -5.42846 | -60.16793 | 2025-08-25 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 87f51fd9-e32b-34f3-aa50-2dc01d050650 | -10.60312 | -44.33248 | 2025-08-25 05:04:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 411d3bd1-ed88-3d28-b36f-6aa94575bff3 | -7.29299 | -44.52553 | 2025-08-25 05:04:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2b2f7292-cd3e-3eea-91b6-5b1b42320551 | -8.60078 | -62.59446 | 2025-08-25 05:04:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 202ce820-19fb-3468-a5f9-29aa6cc6fd34 | -6.19172 | -44.13217 | 2025-08-25 05:04:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d61db719-3398-3089-8e40-0ebeec80e484 | -9.14063 | -60.73381 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 4e741764-37f4-3881-8dd6-7b079f32656d | -11.63193 | -46.23262 | 2025-08-25 05:04:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e34ebe2b-5f98-3e9b-bc54-8b736086ae17 | -7.54217 | -63.8639 | 2025-08-25 05:04:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3dc4154a-65a8-35ff-a53b-0cede2cf5e3a | -10.39985 | -57.6772 | 2025-08-25 05:04:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 82e65a45-ddee-3056-a91b-c291a6d3e2a1 | -9.16934 | -59.48151 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4ce280c7-8330-3357-b8cf-ca158fed826a | -6.89724 | -47.93048 | 2025-08-25 05:04:00 | NOAA-20 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6582ed30-7b6c-3b32-a6f7-affcdb7640ce | -9.26125 | -59.78285 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 48712132-18a3-3a90-9e67-848cb057264e | -6.63068 | -58.54393 | 2025-08-25 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 18a0b37f-abd7-3e2f-a51a-ae7b5f7bccce | -8.92676 | -62.43488 | 2025-08-25 05:04:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f98d9e40-783e-3084-ae3a-50ffe0facb36 | -11.18607 | -55.02503 | 2025-08-25 05:04:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b73a2a60-4c2e-32eb-892b-c5eaf820b7a2 | -6.82643 | -58.96142 | 2025-08-25 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 45c655f6-52c8-33ef-aed9-cc027769c640 | -10.25358 | -59.10495 | 2025-08-25 05:04:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| a8c76922-b683-3f98-a7ed-1c88a568973a | -11.10856 | -44.7937 | 2025-08-25 05:04:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e9e2d8ad-9503-37f4-b20f-658c67793550 | -7.59238 | -45.23756 | 2025-08-25 05:04:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 651bd418-c6f1-307b-96b6-165667ff7813 | -12.73538 | -48.14182 | 2025-08-25 05:04:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7e3f5de7-c1f0-3c66-b1ac-6801b585dffc | -9.80412 | -61.2042 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6edcf4b9-fe22-3998-b637-b37d4be9c596 | -10.72241 | -47.11934 | 2025-08-25 05:04:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c4f279d9-4cb8-349e-a777-8136dc82f703 | -9.17701 | -59.45747 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 091a6ee0-d0f8-3e87-b563-480a43c3afe1 | -9.15435 | -59.48324 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a30c95f5-abee-391b-96ce-b3733fdfb3b0 | -12.75186 | -48.1311 | 2025-08-25 05:04:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 87a5f755-ea32-39ad-84b4-e20481f77a28 | -9.81019 | -64.25742 | 2025-08-25 05:04:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 39990dfb-227a-3943-8721-e68e12e22aeb | -8.86686 | -62.42426 | 2025-08-25 05:04:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ea849f4a-3b1d-3be9-88ee-edefaf3fee03 | -6.79714 | -58.63456 | 2025-08-25 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3deef18e-0944-3b0b-9c46-e29c4eac89d2 | -8.90818 | -62.41482 | 2025-08-25 05:04:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b7f16254-2c4a-3efc-a1ff-f4a4b8329dc1 | -4.95675 | -55.81998 | 2025-08-25 05:04:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| eec728e0-a90b-3b58-a344-e639aed3e1d1 | -8.47087 | -63.92797 | 2025-08-25 05:04:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README67.md)
