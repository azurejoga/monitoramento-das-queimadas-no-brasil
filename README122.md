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

## Dados Diários - Página 122

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4c2e07dd-d8c9-3df5-bc4b-8619f81ca805 | -6.67936 | -55.06 | 2026-09-23 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7c1b3b01-ee9e-3bb7-94db-ee97da6b30cd | -6.75228 | -63.14317 | 2026-09-23 05:25:00 | NOAA-20 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7adaec80-d793-3605-962c-f3394eec5b76 | -6.7386 | -59.42897 | 2026-09-23 05:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b2f52d09-d569-3a17-8ca3-069c87772560 | -6.61315 | -59.96127 | 2026-09-23 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 463e5e62-daa7-3c64-97c1-6bcf48d3cd96 | -7.03629 | -59.50187 | 2026-09-23 05:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 513c00c7-9549-3278-87d1-12f529aada33 | -6.43257 | -55.61837 | 2026-09-23 05:25:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d8c5f2ec-700b-311f-847e-d0baf94ae348 | -7.5595 | -57.66843 | 2026-09-23 05:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1ff7c1f7-9aab-3f55-8d1b-be80d7e909ca | -6.66883 | -58.55883 | 2026-09-23 05:25:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 69237e75-89a1-32c9-973a-608aa55681c5 | -6.16297 | -57.7093 | 2026-09-23 05:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 39f4b52c-4f91-3b67-b08b-db65746ff851 | -7.55853 | -55.01875 | 2026-09-23 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| d17f6175-3d91-35c8-b6a3-c11c91e79bd7 | -7.56859 | -57.67739 | 2026-09-23 05:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| aec81300-fdfc-3995-b939-9d96ea28c48b | -6.02426 | -55.35386 | 2026-09-23 05:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 39288676-5cbb-3579-a1e0-119228842cfc | -8.20286 | -54.72427 | 2026-09-23 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 92949b3d-09cd-302f-aa34-ddcf7f5ee929 | -6.69365 | -60.01038 | 2026-09-23 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d0d82b88-1c7f-3bee-b07c-c7075c7a96b8 | -7.29309 | -59.53188 | 2026-09-23 05:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 406551b7-2766-322d-a589-48b267be46e3 | -5.45468 | -60.14876 | 2026-09-23 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d66d749a-d38f-3e07-b77b-41e51292200a | -5.42181 | -60.16973 | 2026-09-23 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 804ba44c-0e66-34a2-b595-da0c6c58cf2c | -6.74319 | -55.3085 | 2026-09-23 05:25:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2765860a-e085-3214-9ba9-5bc543cc4414 | -6.18997 | -57.77959 | 2026-09-23 05:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 499e6584-ac11-3099-ab8d-e6480853f4a6 | -7.10236 | -52.75662 | 2026-09-23 05:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9fa6888d-8635-3443-9996-9da89fa47419 | -6.45934 | -59.98758 | 2026-09-23 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| a5fb2881-8cf6-36dc-8e3d-3458dd8bbbb6 | -6.0995 | -57.68471 | 2026-09-23 05:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9cf20cf0-cb1d-3b2c-bf03-acc3b86ae7a8 | -5.79589 | -57.60907 | 2026-09-23 05:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| df971e24-96ea-3c6f-b0f1-c7b2fb6c1802 | -7.09857 | -52.75106 | 2026-09-23 05:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 48124a86-91b2-3598-a86e-19ab56587564 | -6.16693 | -57.72829 | 2026-09-23 05:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 16dbd1c0-6c70-304f-9a40-3c49006f8271 | -6.67993 | -58.57486 | 2026-09-23 05:25:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b9e87685-28b0-329d-bb9e-5592d8228bd2 | -6.3591 | -58.28401 | 2026-09-23 05:25:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0dd6b99d-a109-3388-b180-ccaeff687b8a | -6.2937 | -57.74393 | 2026-09-23 05:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 64ce2883-5bc2-3a16-baff-7aa8c48e3b1c | -8.4622 | -51.48556 | 2026-09-23 05:25:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d6e68ade-0d6d-356b-8910-7132c767227e | -6.30675 | -59.945 | 2026-09-23 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 642a42a6-4a82-3114-80e2-d6588542b17c | -6.92262 | -62.90792 | 2026-09-23 05:25:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 31eace99-c31d-309b-a959-9847d60690f3 | -6.37885 | -55.28569 | 2026-09-23 05:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ba49a12f-847f-3891-a789-1ccd16247f96 | -7.4215 | -49.83511 | 2026-09-23 05:25:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 41b17770-be08-34c1-b3d7-b12cfced7a69 | -5.6515 | -60.21303 | 2026-09-23 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d40b020c-30a8-38dc-9130-74f3390c6ba3 | -6.63535 | -59.92896 | 2026-09-23 05:25:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 20.6 |
| ceade794-3776-3d15-92fc-b7f48917ee88 | -5.60257 | -60.20541 | 2026-09-23 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 299e6d52-17e9-3dea-8342-dd516579dcb2 | -6.63423 | -59.93595 | 2026-09-23 05:25:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 7.9 |
| edaca165-d58a-3bf4-8e4a-1bea7aeea84d | -5.45917 | -60.14219 | 2026-09-23 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6be25f1d-e073-3e8c-9cae-b4490ff2e9ec | -7.09913 | -52.75872 | 2026-09-23 05:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dd0007d3-10c0-38f8-98bd-a6e5c514bef4 | -6.75365 | -59.05543 | 2026-09-23 05:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d22c513e-8ed8-3f8d-8e25-723d196fb3ed | -7.17479 | -48.62902 | 2026-09-23 05:25:00 | NOAA-20 | MURICILÂNDIA | TOCANTINS | Brasil | 1713957 | 17 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 373ae7b9-3bb6-3665-8a62-2f72bc7f51fe | -5.22002 | -60.05008 | 2026-09-23 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7f0b1e53-9272-398a-80b1-1d4412b8cb5a | -6.89386 | -55.33321 | 2026-09-23 05:25:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5a8b9d6f-06bf-36ec-a4bb-edf1f712bc40 | -7.39534 | -55.21465 | 2026-09-23 05:25:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 11bc5ae5-7616-3a89-bfa4-c20272e2844e | -6.39318 | -60.01989 | 2026-09-23 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ce98fccc-74b8-3ebc-a86b-3c2755380fea | -13.70634 | -48.79345 | 2026-09-23 05:25:00 | NOAA-20 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 62a0694d-87fa-3dab-b0c0-aea9904b8801 | -6.66664 | -58.57276 | 2026-09-23 05:25:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 283425b8-2cf0-3660-b83d-fc8fdff6f3f1 | -6.34003 | -59.94666 | 2026-09-23 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0b527b98-464f-3d2f-96f9-bdd4a82bd8c9 | -6.6204 | -59.91581 | 2026-09-23 05:25:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d75677e5-0c5d-30e8-b67f-fba463dcaf3c | -6.83924 | -59.5873 | 2026-09-23 05:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0c9340cc-6312-3f8a-81ee-c1faf1bc47ca | -5.98346 | -57.77696 | 2026-09-23 05:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d1c47653-ae2c-3ad2-980f-49173410f591 | -6.28696 | -57.74289 | 2026-09-23 05:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 17b96a9d-7973-3988-a2d3-e59445e89eee | -8.25448 | -54.776 | 2026-09-23 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 80883518-a01b-3ac5-a0a4-b3328c27c98f | -6.26343 | -55.43096 | 2026-09-23 05:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 367c5979-bf0e-3efd-aafe-cbf93df8e748 | -7.38947 | -55.2276 | 2026-09-23 05:25:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ffcedf52-3c20-3688-935d-e809281df0d0 | -5.48827 | -60.13227 | 2026-09-23 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 94220eeb-787e-36a1-93d6-366a554e5e95 | -7.59127 | -57.66582 | 2026-09-23 05:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1f11e985-8765-3d2c-922b-77463e9a4275 | -6.34854 | -57.89123 | 2026-09-23 05:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| de2aab46-523e-3a9d-9dbb-d8a4ed016c2c | -6.60876 | -59.9247 | 2026-09-23 05:25:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ae80593a-942e-3755-8b96-1dbb4f2ac1e0 | -6.6777 | -58.56736 | 2026-09-23 05:25:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a9631533-8b39-3b7f-8310-0148826b2e42 | -6.17358 | -53.28938 | 2026-09-23 05:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b384f50c-8f93-35b3-8c31-173936c745b8 | -7.29087 | -59.50311 | 2026-09-23 05:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2ca5ab5e-4c2e-302a-9f04-6bb07cafd696 | -6.00532 | -57.68122 | 2026-09-23 05:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 81de744c-2297-376b-9c1c-e24a331d08db | -6.67274 | -58.57729 | 2026-09-23 05:25:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| ec9c03d3-a3ce-35f4-a20b-a375e57e8d3d | -5.15889 | -60.30377 | 2026-09-23 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 65fdfd78-7028-31db-bf47-d769552d2045 | -6.61264 | -59.92173 | 2026-09-23 05:25:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 30.0 |
| 3fcb19a7-38a7-369f-80d0-7c0c56235db0 | -6.34279 | -59.95068 | 2026-09-23 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a81a7b8d-ed5e-3d1c-bcd1-427d8fd1d5e5 | -6.70316 | -58.9238 | 2026-09-23 05:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| daaa0326-5cf9-3044-8913-49a3e985d1b6 | -6.73759 | -55.08798 | 2026-09-23 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 608e0d56-eb87-3e35-9649-3cacca034fbe | -7.04263 | -62.93066 | 2026-09-23 05:25:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4e942f02-e871-3d23-9a41-4e33cbc0a415 | -6.61485 | -59.92926 | 2026-09-23 05:25:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 22.4 |
| 89200ef8-114f-3b11-bd47-5a161f2a611f | -5.98511 | -57.70022 | 2026-09-23 05:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d486ac38-754a-3f08-bf3a-5f2a714dba6f | -6.60873 | -59.94622 | 2026-09-23 05:25:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6b318d1e-8234-3885-9d87-7eb6d4d8ad10 | -6.77746 | -59.63434 | 2026-09-23 05:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bb27854e-9802-3b83-8a0b-de2f7582c69d | -6.61592 | -59.96529 | 2026-09-23 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| db5926af-3764-344d-bc13-61eb3c83ea24 | -6.46271 | -59.96658 | 2026-09-23 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 59ee72e0-086f-3f8f-bfdb-77221a30cf7b | -7.15462 | -59.59154 | 2026-09-23 05:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 79156958-ece2-340b-a757-1bd6f83a30d6 | -6.85833 | -63.02024 | 2026-09-23 05:25:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 60d1c6dc-572a-3a74-8111-dc40c6a48353 | -6.1391 | -59.92865 | 2026-09-23 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 396885eb-1232-30e2-8859-8bdf4b48c930 | -6.59273 | -59.89706 | 2026-09-23 05:25:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 217af5a4-9f4d-3dde-8f9d-5165d7961348 | -6.69705 | -56.16047 | 2026-09-23 05:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4ea27627-b497-3740-b6d0-be83fc857de3 | -6.67329 | -58.57381 | 2026-09-23 05:25:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 7148935d-7ec1-385c-9907-ea930f86900b | -6.62198 | -59.9914 | 2026-09-23 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7154675e-08ce-3cd0-b23b-708a0fe97cca | -6.33834 | -59.95716 | 2026-09-23 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 79be4289-4f76-36a6-aab3-0521165e7618 | -7.58786 | -57.66529 | 2026-09-23 05:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0fe29145-36bd-3197-baf1-4561af63e39b | -7.42948 | -49.85881 | 2026-09-23 05:25:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 00bf2327-6ccb-38bb-a3a4-d024af567a21 | -6.13681 | -59.96428 | 2026-09-23 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9efdc3d6-5c5b-34cf-bf22-914d8ae700e9 | -5.99577 | -57.72021 | 2026-09-23 05:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f4750e37-1f6b-360a-ba38-5c4a525c26e2 | -6.63812 | -59.93298 | 2026-09-23 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 20.6 |
| 69d27066-0a98-344f-9683-de255099857d | -5.41107 | -60.21553 | 2026-09-23 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 994039f5-8b32-3890-bc3a-0932b50a2328 | -6.6132 | -59.91824 | 2026-09-23 05:25:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 30.0 |
| 7903d424-9195-32c4-9650-7bb590290eb3 | -8.46668 | -48.69033 | 2026-09-23 05:25:00 | NOAA-20 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5ee5e822-9a70-38b6-9bd3-b237f4689029 | -6.06653 | -57.80786 | 2026-09-23 05:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 06dcdea7-47dd-3a32-9916-762948c9bd8b | -6.09053 | -57.69802 | 2026-09-23 05:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e69cf850-2461-3375-9f49-3bdc8c8031ea | -5.27865 | -60.21248 | 2026-09-23 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9c8e6075-df89-3cb2-afb7-323fd8205dc3 | -7.39403 | -55.21706 | 2026-09-23 05:25:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7ad062b4-6389-3848-b443-8d1f050a5662 | -7.78448 | -50.23117 | 2026-09-23 05:25:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 294ebdaa-5675-3e72-99ab-81ced02947dc | -8.15106 | -49.55042 | 2026-09-23 05:25:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e5c88493-1f87-3d4c-8781-27e49dd9911d | -6.2839 | -52.95513 | 2026-09-23 05:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 019fafc5-2ba5-3135-977e-a76130b8b863 | -8.73364 | -47.60145 | 2026-09-23 05:25:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README123.md)
