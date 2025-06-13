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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f5698b04-6e65-3d86-b6ee-ee69ba7ae753 | -13.90513 | -54.62292 | 2025-06-13 04:12:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 02457794-76df-356e-878e-de4669ae551c | -17.57917 | -47.49231 | 2025-06-13 04:12:00 | NPP-375D | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4f042c76-1147-3cfb-97fd-939de4b862d2 | -14.67405 | -53.36664 | 2025-06-13 04:12:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 70d27efb-5e68-3e7a-bcd9-941d21b742fe | -15.40019 | -44.2592 | 2025-06-13 04:12:00 | NPP-375D | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Caatinga | 0.3 |
| 9b7e07be-2ca1-330b-8af6-e42455c1eb96 | -16.50294 | -45.03808 | 2025-06-13 04:12:00 | NPP-375D | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2842ab76-40cd-3d66-824c-525df394a3ab | -13.9004 | -54.63834 | 2025-06-13 04:12:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 3a8881e1-6d67-30b9-b312-68aa8b69ff77 | -16.68159 | -43.88265 | 2025-06-13 04:12:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 46032f09-66f2-313b-a964-ab68638d6902 | -13.97785 | -54.45474 | 2025-06-13 04:12:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ab911484-f12c-3f5b-9d54-115ad587a4e8 | -15.41673 | -44.28426 | 2025-06-13 04:12:00 | NPP-375D | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 572d758b-28fe-3af8-9db9-0e213da30018 | -14.20873 | -57.39918 | 2025-06-13 04:12:00 | NPP-375D | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 10.1 |
| a5dfdeba-f993-3b4d-9ca2-1171816fc5af | -14.0261 | -55.12759 | 2025-06-13 04:12:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c13d467f-8edd-3ae6-b23f-9449a8edb234 | -13.97376 | -54.44465 | 2025-06-13 04:12:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 640ac272-cc72-34e2-880a-57c3cf433991 | -14.03522 | -55.12296 | 2025-06-13 04:12:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c481d436-008f-3a9e-9175-63cff952e83a | -13.88939 | -54.63094 | 2025-06-13 04:12:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 0ee8483e-1746-348e-811d-4e9b8c2ae88a | -13.97056 | -54.4463 | 2025-06-13 04:12:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e1ca58df-42c0-3954-a4fa-081cb7839c4c | -13.9756 | -54.45195 | 2025-06-13 04:12:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c9d1862d-858a-39dc-8bbb-1fa044d9eca2 | -12.52461 | -57.2392 | 2025-06-13 04:12:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8d4dba5d-51f0-31b0-804a-9ab6607c8fe6 | -14.20029 | -57.40409 | 2025-06-13 04:12:00 | NPP-375D | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 1a151a1d-21a7-3fa2-890d-f2d16c616c0f | -15.35926 | -47.87814 | 2025-06-13 04:12:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0201ef7f-5393-3252-92ef-7c51fb2f2ae1 | -17.66356 | -47.45891 | 2025-06-13 04:12:00 | NPP-375D | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1904af56-b273-36b4-a2bc-dfd1d60d390a | -15.3868 | -47.8784 | 2025-06-13 04:12:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 69505bf8-aa19-35c1-a3fb-d6d8c7897575 | -20.10533 | -44.5856 | 2025-06-13 04:12:00 | NPP-375D | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 728b6e87-173f-3bb7-967b-67b8ba9201ee | -14.20422 | -57.39851 | 2025-06-13 04:12:00 | NPP-375D | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| dae5cc04-a4ad-331a-9f37-b12dec88238d | -15.932 | -46.7644 | 2025-06-13 04:12:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6635b805-8f47-35e6-932c-2e3c5ecde67f | -14.8441 | -48.30817 | 2025-06-13 04:12:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| eefdcc6b-c143-3c34-9e1a-25c3d55cadb7 | -13.90317 | -54.62483 | 2025-06-13 04:12:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 773fab17-4067-3271-aa88-d81841737f3d | -13.97878 | -54.45026 | 2025-06-13 04:12:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| af9ccbf3-67fd-3246-b261-9a16e0d7896e | -13.89214 | -54.61756 | 2025-06-13 04:12:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| c9a378cc-d329-35bc-8a8c-7e69ab7075bb | -17.65196 | -47.46114 | 2025-06-13 04:12:00 | NPP-375D | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b6f552f5-591a-3821-b2ba-d2bf3593a654 | -13.89031 | -54.62643 | 2025-06-13 04:12:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| e4a06185-6f5f-314c-92ae-8294003190e5 | -14.03226 | -55.12891 | 2025-06-13 04:12:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e5fc7edc-3449-3132-b98a-ada126f52efa | -13.89855 | -54.64737 | 2025-06-13 04:12:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| b7ad5c1a-5e2e-351d-81a6-76c0789af319 | -14.67483 | -53.36275 | 2025-06-13 04:12:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 70d16f82-45cb-3eda-9ee8-c7ee1199058d | -14.67327 | -53.37051 | 2025-06-13 04:12:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ee5bb2c1-38c8-3cf7-b5a3-66a04bf353d0 | -12.52125 | -57.24237 | 2025-06-13 04:12:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 916b993b-e57e-3abb-9171-89f6e9a86156 | -14.21121 | -57.40008 | 2025-06-13 04:12:00 | NPP-375D | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 02451ef8-3654-3600-8b6d-4488e0d76c75 | -15.07903 | -48.94573 | 2025-06-13 04:12:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e1ec977f-0891-3d9f-8196-06a4f048e51c | -14.67876 | -53.37157 | 2025-06-13 04:12:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| c9609613-e99e-380c-a439-8f94cf833a71 | -13.89122 | -54.622 | 2025-06-13 04:12:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 25556c0c-7f1a-3ff8-9ff3-820291ffd7c3 | -13.97282 | -54.44914 | 2025-06-13 04:12:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a75893fc-a0cf-35dc-908b-778c28f72e65 | -14.19049 | -57.41503 | 2025-06-13 04:12:00 | NPP-375D | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 45b83056-ffdd-336e-b147-0a037536bede | -13.9765 | -54.44748 | 2025-06-13 04:12:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 65a4356b-a80e-3622-b2a4-73c80e0442f9 | -17.65706 | -47.45325 | 2025-06-13 04:12:00 | NPP-375D | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| db728847-da11-3cd8-a9da-d0574f3e2f20 | -14.02808 | -55.12636 | 2025-06-13 04:12:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4a245ec4-ff1a-347e-bcc9-4f9d5d32a1fb | -15.36092 | -47.86882 | 2025-06-13 04:12:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f723802d-501f-359a-a45f-e3019cbd050d | -19.45465 | -45.3074 | 2025-06-13 04:12:00 | NPP-375D | MARTINHO CAMPOS | MINAS GERAIS | Brasil | 3140506 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a137aca1-458c-3204-99a4-987627307000 | -13.89812 | -54.61892 | 2025-06-13 04:12:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 63989a62-f177-32b6-b402-24078a137422 | -17.66068 | -47.45395 | 2025-06-13 04:12:00 | NPP-375D | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8ca36bcb-5825-3e44-8260-43ba0e8c8a21 | -14.03423 | -55.12774 | 2025-06-13 04:12:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6d39a341-8c8c-31ae-974c-26f8d05af5a6 | -19.08101 | -53.46696 | 2025-06-13 04:12:00 | NPP-375D | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| bfb02954-d8fa-3abf-94ac-6686e997c426 | -13.97239 | -54.43721 | 2025-06-13 04:12:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 899de553-0612-334d-8ba1-8ff7c5006eda | -13.89347 | -54.64157 | 2025-06-13 04:12:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 9d4da600-201c-3544-b666-9b0f10ba4028 | -15.02831 | -47.04442 | 2025-06-13 04:12:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 63ee041f-97d0-3868-8b19-98a521f08a62 | -14.19304 | -57.41616 | 2025-06-13 04:12:00 | NPP-375D | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 99fc1267-8886-3db9-b410-192459a28522 | -17.21266 | -44.79784 | 2025-06-13 04:12:00 | NPP-375D | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f8c2631d-f181-36e9-a3a4-a664646cc6a6 | -15.13771 | -49.5453 | 2025-06-13 04:12:00 | NPP-375D | NOVA GLÓRIA | GOIÁS | Brasil | 5214861 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 96c2bda3-072b-33b3-823a-37991ec85804 | -14.2157 | -57.40083 | 2025-06-13 04:12:00 | NPP-375D | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 30711afc-b361-3223-85fb-1c2225cb0fb7 | -12.5175 | -57.23759 | 2025-06-13 04:12:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 16e21e1c-f4f6-3e8e-8da5-6bcc77b28842 | -13.90418 | -54.62739 | 2025-06-13 04:12:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5d43452d-a3b6-3f27-964a-a27caf464b01 | -13.9747 | -54.44018 | 2025-06-13 04:12:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 01bd358b-206e-3308-ac07-037361ffd069 | -15.36475 | -47.86946 | 2025-06-13 04:12:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ed620aab-b989-3e5a-8969-9fa5b306d0d5 | -13.97147 | -54.44175 | 2025-06-13 04:12:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5deaa75f-ae32-309b-bbbd-e3f8ff4370b9 | -17.38086 | -53.82209 | 2025-06-13 04:12:00 | NPP-375D | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2f45e649-3375-368b-8100-31c7a077e04c | -14.20138 | -57.41159 | 2025-06-13 04:12:00 | NPP-375D | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 091bfbff-84ba-3222-918f-eeea5839bee5 | -17.65994 | -47.45823 | 2025-06-13 04:12:00 | NPP-375D | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7f20bbc3-3b70-3048-b264-876452aa54e8 | -15.36859 | -47.87002 | 2025-06-13 04:12:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0d195b0e-b0a7-3731-b83f-c2c477dc3aef | -19.08035 | -53.47016 | 2025-06-13 04:12:00 | NPP-375D | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| acd64fbc-44a7-3341-b2ee-f5a15626979b | -12.51413 | -57.24074 | 2025-06-13 04:12:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0b2b6405-1aa0-3719-834f-6feb7d233fec | -17.00734 | -49.78239 | 2025-06-13 04:12:00 | NPP-375D | CEZARINA | GOIÁS | Brasil | 5205455 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2f6241a1-3d57-3f1e-97a3-31fb1085a323 | -14.67953 | -53.36773 | 2025-06-13 04:12:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| dbe5933e-fef7-38b4-9d6e-b7693c511fc0 | -14.03938 | -55.13403 | 2025-06-13 04:12:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4e2be67c-5f0f-3ec7-9262-bbc2e61a3933 | -13.90228 | -54.63634 | 2025-06-13 04:12:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 184325df-d60b-31d5-97be-1e994e1980f1 | -17.65345 | -47.45255 | 2025-06-13 04:12:00 | NPP-375D | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 396f34af-7f9c-3aea-81f0-56538dbb7eb9 | -14.67801 | -53.37531 | 2025-06-13 04:12:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 8.0 |
| ba7dd17b-0f72-39b4-9693-4fd5c5b16900 | -14.20978 | -57.40667 | 2025-06-13 04:12:00 | NPP-375D | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 6f5245c7-e4c3-3444-a98a-1b19412fe18f | -14.20728 | -57.40567 | 2025-06-13 04:12:00 | NPP-375D | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 61bc5d1f-dcd1-3557-854a-2329d76dfd13 | -15.13857 | -49.54684 | 2025-06-13 04:12:00 | NPP-375D | NOVA GLÓRIA | GOIÁS | Brasil | 5214861 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 61da16da-66fa-377c-81e0-774f9f905bc4 | -17.65632 | -47.45754 | 2025-06-13 04:12:00 | NPP-375D | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d8fab230-d4b5-35a2-b6ca-49aa90756cad | -15.37324 | -47.86602 | 2025-06-13 04:12:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3026d70f-d14f-38a6-8eaf-66f01e8a2cc5 | -13.89722 | -54.62331 | 2025-06-13 04:12:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 61d406df-5b0e-3a13-8314-e73c5f6f9a58 | -18.8234 | -47.92916 | 2025-06-13 04:12:00 | NPP-375D | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 87fbfda0-986c-3aca-9946-42bcd183166b | -17.65558 | -47.46183 | 2025-06-13 04:12:00 | NPP-375D | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 62f23eef-fd12-36d6-8f27-0c38f7b3d284 | -14.87166 | -48.31357 | 2025-06-13 04:12:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7d8ff0c8-59af-346d-8d52-7a6e92b11f50 | -14.19882 | -57.41061 | 2025-06-13 04:12:00 | NPP-375D | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 9b56ec1e-83d5-3e78-aa93-2b9c4caec23d | -13.90408 | -54.62037 | 2025-06-13 04:12:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 2d94aa12-1cf0-30d5-8572-38148df7846b | -13.96975 | -54.43424 | 2025-06-13 04:12:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9e568c9a-b553-37b2-b59b-45e404cfc9f9 | -13.89948 | -54.64284 | 2025-06-13 04:12:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 2da8e735-d67e-3c22-af10-1a1ceceb6827 | -13.90226 | -54.6293 | 2025-06-13 04:12:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 4795ecee-f80d-3ccc-8739-fe5bcf7ae844 | -14.84016 | -48.30746 | 2025-06-13 04:12:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| eebd970e-0be5-3a94-8259-daf1b6bb1fd9 | -19.69912 | -54.61888 | 2025-06-13 04:14:00 | NPP-375D | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8e362e87-57d8-3883-a6e7-3b731ab04b41 | -21.45691 | -48.51441 | 2025-06-13 04:14:00 | NPP-375D | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 745dbe19-3ee9-3045-bb3f-4f636d4c785c | -22.77096 | -49.31534 | 2025-06-13 04:14:00 | NPP-375D | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 63a2f818-ee41-3a27-b9aa-9e307cd6d685 | -22.91961 | -45.41265 | 2025-06-13 04:14:00 | NPP-375D | PINDAMONHANGABA | SÃO PAULO | Brasil | 3538006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 4b08d920-20de-35fb-a038-c3e061764f57 | -22.53847 | -48.81434 | 2025-06-13 04:14:00 | NPP-375D | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 008a3d93-b6f1-303b-873c-7f6bdbc21ce5 | -21.34649 | -48.67089 | 2025-06-13 04:14:00 | NPP-375D | FERNANDO PRESTES | SÃO PAULO | Brasil | 3515608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| beb795af-0604-3c65-acfc-4a87176c2a1b | -21.18014 | -43.98069 | 2025-06-13 04:14:00 | NPP-375D | BARROSO | MINAS GERAIS | Brasil | 3105905 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| f0bdd872-6e73-319f-9e0e-bc79ac877165 | -21.66995 | -56.6286 | 2025-06-13 04:14:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 38e181e5-f218-3d62-87c6-d1a31f70e71f | -21.19601 | -44.93736 | 2025-06-13 04:14:00 | NPP-375D | IJACI | MINAS GERAIS | Brasil | 3130408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 8c13cb0e-f758-3e1a-a9a0-759be1cfc900 | -22.76727 | -49.31453 | 2025-06-13 04:14:00 | NPP-375D | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a55127da-bf44-3601-bf82-d45a4a630ccc | -23.59503 | -47.43715 | 2025-06-13 04:14:00 | NPP-375D | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |


[Clique aqui para ver as próximas entradas](README13.md)
