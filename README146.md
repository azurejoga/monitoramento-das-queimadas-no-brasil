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

## Dados Diários - Página 146

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 86e29328-c4c9-3888-ae5e-15d0a9b80c5d | -7.81757 | -61.64268 | 2024-10-12 05:48:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0edf961b-4395-3920-b6cc-e1ba168bc1d7 | -7.81396 | -61.63828 | 2024-10-12 05:48:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9b108465-39cc-3cee-8fe8-b31d1569411c | -7.80924 | -61.64147 | 2024-10-12 05:48:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8131b6ed-7df7-3ddd-88cf-0f23b97dfa75 | -7.80869 | -61.64529 | 2024-10-12 05:48:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cb15b970-eb00-37e7-a541-88a6fb89ee8c | -9.12994 | -61.30069 | 2024-10-12 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| db687309-1c7b-36d3-af9b-760fef2895e4 | -9.1256 | -61.30005 | 2024-10-12 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 63b31e74-dafa-390b-b457-505f282206da | -9.08992 | -61.16663 | 2024-10-12 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a4918dc9-df6a-3475-8f6c-c26e3664ad79 | -9.08931 | -61.17089 | 2024-10-12 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 27b7aa08-c25f-310b-9dd7-0d45caaccbef | -9.0372 | -61.62533 | 2024-10-12 05:48:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 218522a3-3798-33a7-ae4f-b8b16bf3eeb0 | -9.22992 | -62.21284 | 2024-10-12 05:48:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4614a636-ce75-3f89-a9ee-122876f343dd | -8.97129 | -62.36752 | 2024-10-12 05:48:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b5fa34a1-f8e9-397c-9d8a-490362691178 | -8.97078 | -62.37108 | 2024-10-12 05:48:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1229c394-9d83-34af-9fc1-7ebd8be9a1d3 | -8.96827 | -62.35977 | 2024-10-12 05:48:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ac250a06-21fd-3ca6-86ec-04ffb4ff51d7 | -8.96776 | -62.36336 | 2024-10-12 05:48:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3de05c53-2b34-34b5-88cf-44c228f30180 | -8.96575 | -62.34843 | 2024-10-12 05:48:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| eeb78a2b-3b88-3221-aed0-aad1715c0f5e | -8.96524 | -62.35201 | 2024-10-12 05:48:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0ee5b716-9a2c-3281-b52e-4af1a558b988 | -8.96474 | -62.3556 | 2024-10-12 05:48:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 478a9c02-5656-39e8-abb8-7395574a877b | -8.96423 | -62.3592 | 2024-10-12 05:48:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e7e26545-424d-31ae-bb4f-0d8a001f63b7 | -8.96372 | -62.36279 | 2024-10-12 05:48:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a7fd4dca-00f2-323c-9ab6-2b10d8ec29cb | -8.96322 | -62.36636 | 2024-10-12 05:48:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ea531221-3da5-321c-bfa2-af6165d6fd68 | -8.96221 | -62.34427 | 2024-10-12 05:48:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 787bf7ea-ffe0-33d8-a318-c5181e5e02fe | -8.96171 | -62.34786 | 2024-10-12 05:48:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 52075fe7-083e-36ed-88c8-194788a1611d | -8.9612 | -62.35144 | 2024-10-12 05:48:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 3e6a51b9-1ce8-3ea3-b259-5a6d0e3cbe9e | -8.96019 | -62.35861 | 2024-10-12 05:48:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 93fbff88-be23-34f0-98a5-68619b2603ab | -8.95968 | -62.36219 | 2024-10-12 05:48:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| df8f7012-e8b5-3e9f-af9b-40a8f186c456 | -8.90475 | -62.36473 | 2024-10-12 05:48:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 19396d36-9595-3391-81f5-4997d45ac25b | -8.90423 | -62.36831 | 2024-10-12 05:48:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d5c23354-2c2c-3d72-8bd1-f591574b29a3 | -8.90072 | -62.36414 | 2024-10-12 05:48:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 2fe76201-1ee5-3eb7-8fcc-4a58c90e03ed | -8.9002 | -62.36771 | 2024-10-12 05:48:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a6424a63-417c-3770-ab2e-f90b56247b4a | -8.23201 | -61.18028 | 2024-10-12 05:48:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| f4129117-240d-30f5-89ad-b44f0403ff6a | -8.23179 | -61.19796 | 2024-10-12 05:48:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 11742067-5a37-3adb-98a0-0b0a57425dc2 | -8.23144 | -61.1844 | 2024-10-12 05:48:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1d212b17-8725-3440-8d8d-e04132fc22c2 | -8.23106 | -61.17258 | 2024-10-12 05:48:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 81b3d646-aa37-39bd-a95c-600fa82e8c32 | -8.23087 | -61.18855 | 2024-10-12 05:48:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5f847cae-df73-3872-8ce9-3f4f32640776 | -8.23046 | -61.17674 | 2024-10-12 05:48:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6c81678d-4ad6-30a7-a943-a553bda5f732 | -8.2303 | -61.19268 | 2024-10-12 05:48:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7c1f8a61-8dd1-36a4-8017-fca9c6038be5 | -8.22986 | -61.18088 | 2024-10-12 05:48:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d6bec5c3-c558-365e-8c8f-3cadd7cce970 | -8.22973 | -61.19682 | 2024-10-12 05:48:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 66df1ea4-4a2f-333f-9c62-b34cdb888851 | -8.22926 | -61.185 | 2024-10-12 05:48:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d7c2b52c-395d-3d23-b144-350c67710000 | -8.22867 | -61.18911 | 2024-10-12 05:48:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 475966d9-8d7a-378e-a05a-831327a012e9 | -8.22807 | -61.19324 | 2024-10-12 05:48:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1c448fe0-895c-33fd-911a-2510e48fec08 | -8.22747 | -61.19737 | 2024-10-12 05:48:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 95be7bf4-7427-37f8-8850-255c83295f10 | -8.22554 | -61.18026 | 2024-10-12 05:48:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 19a95987-a553-388a-8d2f-8e76ff4ab31a | -8.22494 | -61.18439 | 2024-10-12 05:48:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 490b389b-b6b0-312e-a87c-7cb1c5e9de4b | -8.22435 | -61.1885 | 2024-10-12 05:48:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 7cc15046-daf8-38c4-825a-6e749b59489a | -8.22375 | -61.19262 | 2024-10-12 05:48:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| cab90cfb-e804-3c67-acb5-a0ed525a7787 | -8.22316 | -61.19674 | 2024-10-12 05:48:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 43aea6c3-702b-3aad-aaf2-0e617ab6afd8 | -8.22129 | -61.50806 | 2024-10-12 05:48:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c8593420-993f-3b2f-a763-79896f10bf02 | -8.22073 | -61.51201 | 2024-10-12 05:48:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ea57b41a-d3e6-3215-94b5-14a698e3015d | -8.22003 | -61.18787 | 2024-10-12 05:48:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 65c54f00-46b6-3e14-bbfc-4b835842bdf1 | -8.21943 | -61.19199 | 2024-10-12 05:48:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e660733f-6040-32b5-a592-78d8346ab7a8 | -8.21572 | -61.18723 | 2024-10-12 05:48:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 60168fd7-0b26-3b83-9534-a0410f79d276 | -8.21512 | -61.19135 | 2024-10-12 05:48:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 67960a5f-c582-31de-b9c8-6c7fab7180e1 | -8.21081 | -61.19072 | 2024-10-12 05:48:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 46a7af92-4f9a-3d7c-84ee-7a9f27c87353 | -8.10493 | -61.26909 | 2024-10-12 05:48:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b0bc4963-27d2-39d1-b112-193fea560760 | -8.09212 | -61.26694 | 2024-10-12 05:48:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b510a1f1-8a52-343d-974a-9b974d65a5f5 | -8.0664 | -61.26323 | 2024-10-12 05:48:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 299dbde4-e112-3256-a5af-fb4157bc0111 | -8.06582 | -61.26728 | 2024-10-12 05:48:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fed9ba54-830e-38f7-b459-bc0fb3df0973 | -8.55895 | -62.45825 | 2024-10-12 05:48:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0928f6b3-37d1-3a54-8c9a-2bd77c99e047 | -10.12431 | -62.49113 | 2024-10-12 05:48:00 | NOAA-20 | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 27c9df36-5778-382c-805f-9f54d8ff519b | -10.5005 | -62.97621 | 2024-10-12 05:48:00 | NOAA-20 | GOVERNADOR JORGE TEIXEIRA | RONDÔNIA | Brasil | 1101005 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 34d09fca-9921-3dd5-87dd-9dc9df8f5f0c | -10.49657 | -62.97539 | 2024-10-12 05:48:00 | NOAA-20 | GOVERNADOR JORGE TEIXEIRA | RONDÔNIA | Brasil | 1101005 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| be63d54f-9b86-3fc4-910f-5d30eaf21918 | -10.47235 | -62.90045 | 2024-10-12 05:48:00 | NOAA-20 | CACAULÂNDIA | RONDÔNIA | Brasil | 1100601 | 11 | 33 | nan | nan | nan | Amazônia | 3.9 |
| f00434ae-6d82-3118-bad0-6547df1b72d1 | -10.47029 | -62.9019 | 2024-10-12 05:48:00 | NOAA-20 | CACAULÂNDIA | RONDÔNIA | Brasil | 1100601 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ae1fcede-07b7-3001-aa09-cd0247878150 | -10.13251 | -62.75459 | 2024-10-12 05:48:00 | NOAA-20 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3dea9837-f84d-30e7-a13b-b67bf5090f59 | -10.12146 | -62.74615 | 2024-10-12 05:48:00 | NOAA-20 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 84e084e1-fe4c-336e-8ec5-85307dd8101e | -10.32561 | -61.64941 | 2024-10-12 05:48:00 | NOAA-20 | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6088a37e-3514-3f93-8f2d-58837213c8d7 | -10.32505 | -61.65363 | 2024-10-12 05:48:00 | NOAA-20 | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1feafe93-564c-3ec9-adae-de6cfa122fb6 | -10.3233 | -61.65015 | 2024-10-12 05:48:00 | NOAA-20 | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ed6388e5-a398-3892-a9e5-0843097b86da | -9.92803 | -62.26019 | 2024-10-12 05:48:00 | NOAA-20 | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f254d1c5-061d-38c1-bd0e-2d376592905d | -9.6258 | -62.43586 | 2024-10-12 05:48:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 163149e2-bba4-3a29-8416-59ae16642ff4 | -9.52891 | -62.50185 | 2024-10-12 05:48:00 | NOAA-20 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a44a1324-15bb-30a0-8120-e06521dc906c | -9.52488 | -62.50127 | 2024-10-12 05:48:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5697cc5c-9e23-3de7-999b-a088eea92ea9 | -10.77898 | -61.50906 | 2024-10-12 05:48:00 | NOAA-20 | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 565bee7d-78f1-34c4-b2b2-5419187ec931 | -10.77897 | -61.5059 | 2024-10-12 05:48:00 | NOAA-20 | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 03e869f5-5001-3164-8903-900010f58736 | -10.77842 | -61.51331 | 2024-10-12 05:48:00 | NOAA-20 | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f0faaa2e-8d8f-3d1a-b39e-99f302f48acc | -10.77837 | -61.51017 | 2024-10-12 05:48:00 | NOAA-20 | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 57b7b59b-cc22-37c4-b9e3-4b05d3ad0cca | -10.77788 | -61.51739 | 2024-10-12 05:48:00 | NOAA-20 | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2aeb818c-1aac-3bc6-b917-f161e871c0c3 | -10.77778 | -61.51436 | 2024-10-12 05:48:00 | NOAA-20 | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 610839b5-916b-3827-963d-d21d8a596689 | -11.84098 | -62.51756 | 2024-10-12 05:48:00 | NOAA-20 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 606c85cf-9496-356a-a16d-02552b9fa12a | -10.85825 | -62.32025 | 2024-10-12 05:48:00 | NOAA-20 | TEIXEIRÓPOLIS | RONDÔNIA | Brasil | 1101559 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| dd18f793-ad85-3345-912d-1632228f4582 | -10.8577 | -62.32416 | 2024-10-12 05:48:00 | NOAA-20 | OURO PRETO DO OESTE | RONDÔNIA | Brasil | 1100155 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 202ef367-deda-3a9b-9a4e-024785f95c68 | -10.85356 | -62.32345 | 2024-10-12 05:48:00 | NOAA-20 | OURO PRETO DO OESTE | RONDÔNIA | Brasil | 1100155 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b9b2c270-cfdd-3f86-bf12-c7e8606405fb | -11.80441 | -62.99966 | 2024-10-12 05:48:00 | NOAA-20 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 94c8a6a7-2156-3d94-a1db-ec9cac574d34 | -11.93371 | -62.69207 | 2024-10-12 05:48:00 | NOAA-20 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b1323e3a-2ad3-38da-866b-f265efd2ad48 | -11.92959 | -62.69148 | 2024-10-12 05:48:00 | NOAA-20 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2dc1e661-bd54-3b81-a345-1665cb052db6 | -11.84047 | -62.5214 | 2024-10-12 05:48:00 | NOAA-20 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| aaf84ee0-1899-3ba2-b0e4-f3b024b2d654 | -11.71782 | -62.60178 | 2024-10-12 05:48:00 | NOAA-20 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7d4e3037-b0e2-3a41-ba04-d17e28f0834c | -11.71369 | -62.6012 | 2024-10-12 05:48:00 | NOAA-20 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 530a7a0c-cb3f-383d-8060-65bf12c99a29 | -13.001 | -62.47403 | 2024-10-12 05:48:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5de65d30-3e6d-365d-94da-da45ea1bdb39 | -12.99675 | -62.47345 | 2024-10-12 05:48:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| afd9160e-ebf9-3c33-960b-d998bc11c2e8 | -12.99563 | -62.48167 | 2024-10-12 05:48:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| dcaadbe8-52e0-3659-970e-5b534e9afe7d | -12.99139 | -62.48108 | 2024-10-12 05:48:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ab8f1301-8849-38f6-88ed-6da1e0d34bca | -12.98238 | -62.4838 | 2024-10-12 05:48:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7560c324-e5b6-39ee-9002-32aebc747e05 | -12.97815 | -62.48313 | 2024-10-12 05:48:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8f3dc5ae-520f-3836-909b-a6ae530dabcc | -12.9426 | -62.52296 | 2024-10-12 05:48:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e40f4afb-b45b-390f-a50f-cf687ef64459 | -12.9257 | -62.5206 | 2024-10-12 05:48:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4876d91e-e351-363e-a8b3-cb4e200fea95 | -12.9188 | -62.5076 | 2024-10-12 05:48:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ed18ed33-42ef-30d1-9554-9cda882e1ac9 | -12.91457 | -62.50699 | 2024-10-12 05:48:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 82a4fc97-bd78-344e-8d58-f3b3d4bb6f11 | -12.91404 | -62.51102 | 2024-10-12 05:48:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README147.md)
