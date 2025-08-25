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

## Dados Diários - Página 82

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 52074ee1-27e0-3133-8736-cf8169aaf981 | -8.22118 | -61.39714 | 2025-08-25 05:55:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2e77f138-4803-37a8-96ac-5bc3bea35d23 | -8.22457 | -61.40829 | 2025-08-25 05:55:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e61383bf-e537-3c3d-b6ee-0666f6bed04f | -8.59981 | -62.59717 | 2025-08-25 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 973364ac-b73f-36d0-991d-ff3b2db27f63 | -8.89262 | -62.44836 | 2025-08-25 05:55:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 08f39a05-1433-3a2d-80eb-b496ab0ebcf2 | -6.79704 | -58.62547 | 2025-08-25 05:55:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1d4df04a-888f-30d3-8f8e-bef3c204e7c3 | -12.07332 | -63.14974 | 2025-08-25 05:55:00 | NOAA-21 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 40f5fdc1-0ce6-3b78-9ec8-1fb5d8f4aab0 | -10.09347 | -67.95406 | 2025-08-25 05:55:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9f29806e-bcb2-3cf8-846c-035c8b9f0608 | -9.15721 | -59.47377 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f61d3b39-67f9-3338-897e-152e0379f2a9 | -9.19438 | -59.4428 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 246c59e0-f203-3fd8-97ea-b624001effca | -9.19485 | -59.43904 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 166a5f1e-1f40-322c-9d85-a17c9ac30535 | -9.04001 | -65.72048 | 2025-08-25 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4b4398b5-895a-3f75-a559-9d6f20a0479a | -8.98697 | -65.42046 | 2025-08-25 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| b069c6ef-b0a8-32d8-97a7-9dab60613e03 | -12.59467 | -60.36148 | 2025-08-25 05:55:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4b4098d2-5e8e-345e-b7b4-ce1358176c60 | -9.61383 | -67.97751 | 2025-08-25 05:55:00 | NOAA-21 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8b53e5d4-e6a3-341e-8004-11f3490e8ba2 | -7.54828 | -63.84176 | 2025-08-25 05:55:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5b0741d2-f10d-3928-bfa6-82dc3ad32360 | -8.8913 | -62.44637 | 2025-08-25 05:55:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| cdea0067-e035-35e8-b73d-c8bf78fe70e8 | -9.13225 | -60.73056 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ab6dd726-e5e7-308f-95c7-d2148fda2552 | -7.5276 | -63.81319 | 2025-08-25 05:55:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| eb7ac16a-36c9-383f-892b-73b5cb70a1c6 | -8.11685 | -62.87329 | 2025-08-25 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 20db138d-eb62-327b-87fc-3e657ee587ac | -9.51326 | -60.51162 | 2025-08-25 05:55:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 95734edf-765a-35fc-a31d-9c25fd2463f7 | -10.42434 | -64.43273 | 2025-08-25 05:55:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 383675bb-e1d8-3329-b4d9-3a480f828d59 | -6.92056 | -62.99851 | 2025-08-25 05:55:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1612ef74-1696-3bb1-9dcc-9457fe956d90 | -8.7326 | -64.16476 | 2025-08-25 05:55:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5710d5ef-4653-3753-9fa3-385c9cf17a07 | -9.18682 | -67.75637 | 2025-08-25 05:55:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b055e933-485f-3e81-bb16-4efb1ea760bb | -10.41576 | -64.43508 | 2025-08-25 05:55:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c0e2c581-6e51-3e10-8000-c8a336ba5985 | -8.4751 | -63.931 | 2025-08-25 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e6ade083-1042-34ef-89c6-85b093b1831f | -9.17534 | -59.46492 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| ed70b286-19b8-34ba-91f3-118f7ad88403 | -9.80586 | -61.2026 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 107ecdd5-7a4f-363c-9563-0a9a6c9dea39 | -6.83021 | -58.95713 | 2025-08-25 05:55:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| c39bf1d2-8742-323b-862b-9c86d9f3c397 | -9.14247 | -60.77193 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c355c951-b575-3af5-a378-a37c65999be3 | -8.90421 | -62.45289 | 2025-08-25 05:55:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9c1e4e9e-c7c4-3a6e-a3f1-ce519e6c1e3d | -9.22194 | -59.71098 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5fb27ca5-d881-3d2b-bc3b-a5d15e2d7b22 | -9.17443 | -59.4665 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 971f54ee-c0d4-34ae-9977-82a7e5491e25 | -9.00821 | -65.70686 | 2025-08-25 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1011889b-f5ad-365b-b16a-f8dd810d4e5b | -9.20639 | -59.48227 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f83b8b2a-c2d8-3676-bc1c-1126bd187b5c | -8.89583 | -62.41427 | 2025-08-25 05:55:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1c026283-30bb-366d-a27b-9a157c95b24e | -8.87905 | -62.46794 | 2025-08-25 05:55:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3bafa94f-c279-3237-9de1-bd0bda49922f | -9.20686 | -59.47856 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f3f231ae-4176-33f6-86c9-1244040d9649 | -8.67881 | -62.86904 | 2025-08-25 05:55:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c2cf072f-d450-31a3-8107-f1966f45a59d | -9.00579 | -65.69758 | 2025-08-25 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 29644f86-ec4d-3f4e-bc6b-f1a5b26d01c2 | -7.90994 | -63.05928 | 2025-08-25 05:55:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7b9cb95e-a688-3f89-84bb-852c496ca2d8 | -9.17028 | -59.46039 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| c7ea293b-4823-31e4-acf7-2b811a94a5a8 | -9.02899 | -65.71881 | 2025-08-25 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5ea44655-8db7-3d02-b4a0-84e8c65dd32f | -9.10532 | -61.434 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 00352727-beaf-328a-9844-9b9bfc6e3ccf | -6.6305 | -58.551 | 2025-08-25 05:55:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 0445e992-cf0c-301e-984e-e7fd6af5094c | -9.16735 | -59.48268 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b9d41eb8-891c-3294-a5fb-a26d2795dab1 | -8.89054 | -62.42932 | 2025-08-25 05:55:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 410d9933-71f6-3f49-a808-bf9a4ff54f0d | -9.06571 | -65.72443 | 2025-08-25 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 12.5 |
| ec16a40a-f5df-361a-8fff-e290f51d419f | -9.19948 | -59.44726 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3a9c026b-f14f-3677-b46b-3618c488e950 | -8.88614 | -62.4503 | 2025-08-25 05:55:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 4296cc58-72e4-3c3f-a108-32e6f2db33d4 | -9.17416 | -60.80679 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 208c9c75-5ffa-3946-9de4-64e61d737242 | -8.50421 | -63.87238 | 2025-08-25 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 8.7 |
| d3498ff4-b583-3f6c-aa58-f4e3315a9403 | -9.12674 | -60.73296 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d534f84d-25dd-3574-8da2-9af425cab68c | -8.98017 | -65.41482 | 2025-08-25 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 791c440f-ee65-34c5-84c6-4469b38821c1 | -8.89647 | -62.44243 | 2025-08-25 05:55:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 24c60f1c-7c12-31f8-99f0-56d2c829599c | -8.89582 | -62.44701 | 2025-08-25 05:55:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 01bc82d4-c414-36be-a0a4-24ecd8d17307 | -7.55028 | -63.85654 | 2025-08-25 05:55:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 75589667-44a0-36a3-aa6d-2c03bd559b24 | -8.86645 | -63.0386 | 2025-08-25 05:55:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 52d190ec-1806-3243-8ba4-23b167cd3d29 | -8.2267 | -61.39267 | 2025-08-25 05:55:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 02de20ea-5dd6-3738-9082-e0a995bf35d5 | -6.83628 | -58.95424 | 2025-08-25 05:55:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| d5721ce6-b077-32e2-ad54-3455dbbdd415 | -8.10759 | -62.87616 | 2025-08-25 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.9 |
| bb618fd3-aa4a-3170-8fe5-5c099df6fb2e | -8.21227 | -61.39048 | 2025-08-25 05:55:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a136a0fe-703d-3a52-b424-f4ceeb12a371 | -7.91307 | -63.06793 | 2025-08-25 05:55:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 22.8 |
| 6e1f4d83-1afe-35d1-b730-c061deee6147 | -6.69059 | -58.86311 | 2025-08-25 05:55:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 968cd915-71cd-3b94-9809-6967869dd857 | -11.69632 | -60.1833 | 2025-08-25 05:55:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 504a02f9-750a-3c40-8615-c8f88eb9c7f9 | -6.78977 | -58.63639 | 2025-08-25 05:55:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c510712f-0cff-3ea6-934c-65df69dbb4eb | -7.62486 | -62.72434 | 2025-08-25 05:55:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 7cf79701-622d-3391-99fe-a3fa4bbbe983 | -9.4936 | -58.93805 | 2025-08-25 05:55:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 37a25fe2-ef69-3a86-a809-4c9889bca588 | -8.89906 | -62.42407 | 2025-08-25 05:55:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 31f79b58-9059-31ae-8bde-9de7cd562988 | -9.21147 | -59.70572 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7e8dfcd8-c34f-3f98-8077-09c06c8a0a7e | -9.18188 | -59.45829 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 8dc6fbbf-fdb9-31d8-b63e-6500df8ee6c1 | -7.62427 | -62.72853 | 2025-08-25 05:55:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 42a9d45f-7647-366a-9e2c-bc1e313f916a | -9.19662 | -59.51493 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 70c6a3dd-9ede-392e-b470-26d9fb459cb6 | -8.22599 | -61.39783 | 2025-08-25 05:55:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fc5420d2-ecee-3aaf-b134-98775cff85a2 | -9.20416 | -60.92895 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9e587c33-56b6-327a-8f36-a9bcb94de487 | -9.00283 | -65.39056 | 2025-08-25 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 7.2 |
| a54494a8-2704-3128-9af1-dcec63f5ee16 | -5.809 | -59.22596 | 2025-08-25 05:55:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 039d7eb3-6a83-3597-967f-c506d16b9b23 | -9.19251 | -59.45772 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 22142bc8-763d-343b-9dad-a60a81dba4b1 | -9.02354 | -65.70473 | 2025-08-25 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 579d2aa2-962d-347d-a296-40d4420ce096 | -9.19481 | -59.48446 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 38407983-6fc2-3697-b7ce-25fe2b5cdefa | -8.4549 | -64.10673 | 2025-08-25 05:55:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 04c188ca-b7f2-3d85-b648-a2f9e33e6078 | -8.23009 | -61.40376 | 2025-08-25 05:55:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4410bf40-ae07-3424-b075-f49621b73c4e | -9.00758 | -65.71117 | 2025-08-25 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a2db0196-0493-3020-8bed-1d105969aee1 | -9.20969 | -60.92181 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 73249881-2be7-370b-a1ec-922fc5e136f1 | -6.7903 | -58.63246 | 2025-08-25 05:55:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3aad0295-7dfc-3b53-bd4e-fcb5bc6f8e0e | -9.14286 | -60.76894 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 37a86ce6-c879-3a90-ba2f-7bda2af97cec | -8.9157 | -60.72279 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ab242cd6-a385-3784-8e05-0f3999d2f53b | -9.19527 | -59.48078 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 41d60644-80ef-3e60-88f2-919ba3ba9e33 | -6.35852 | -57.9707 | 2025-08-25 05:55:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b8c13403-25a3-33b2-88ea-e86df32cfdf1 | -8.89195 | -62.40898 | 2025-08-25 05:55:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a932100c-f35b-34b2-ad6a-38363e81ce82 | -9.22662 | -59.675 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5e157fe9-55f5-37c6-9c66-70024ec74709 | -8.8914 | -62.45755 | 2025-08-25 05:55:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 4.7 |
| f614c90c-047a-3901-8097-0dbaf6dba490 | -8.97329 | -67.48007 | 2025-08-25 05:55:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 750fd9bf-73f5-3943-bad4-e3877fd2346d | -8.22188 | -61.39199 | 2025-08-25 05:55:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 35eee34e-df27-3057-a21f-09977c8e14a3 | -7.32648 | -59.61145 | 2025-08-25 05:55:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 885337e6-4bac-3170-b818-98cc8c610d6f | -9.17217 | -60.8218 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 576c51ce-b9dc-3ed9-912c-d4f0eb00485f | -7.65623 | -63.52718 | 2025-08-25 05:55:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 47afe095-1628-3b3c-a5ac-3e271c1efb44 | -9.82104 | -64.28819 | 2025-08-25 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 772a7a1b-fb1f-3aa5-9478-54fe04d1521f | -9.22569 | -59.6822 | 2025-08-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a4c1491e-706d-397d-a131-13063b86264c | -8.89385 | -62.43916 | 2025-08-25 05:55:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 4.2 |


[Clique aqui para ver as próximas entradas](README83.md)
