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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e63c19d9-b359-3587-9114-3305779d0900 | -6.09535 | -59.92579 | 2025-08-08 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 32425a19-78b3-3986-b7d9-0806a6ef14ba | -7.41826 | -60.02128 | 2025-08-08 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f24d3d04-bdc8-32ee-964a-2da0e045a224 | -7.0422 | -59.18474 | 2025-08-08 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 16.2 |
| 1c8117c6-8e94-394d-8f8b-dffd5a7cd12b | -7.05575 | -59.16439 | 2025-08-08 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 606a78c6-9db0-3518-a9e6-2272cc04bc20 | -7.03543 | -59.18367 | 2025-08-08 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 48bf2439-b8a9-39bb-b1b9-a2b98a56834f | -7.05462 | -59.17168 | 2025-08-08 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 0a673d77-a885-3682-9b47-2bb2d3623b0f | -6.64591 | -58.82449 | 2025-08-08 05:23:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 18e12b1c-4cd9-3736-a3a5-fc4b80279a97 | -7.05291 | -59.18269 | 2025-08-08 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 685d321e-a22f-3ca6-af2c-3c3ff69e23c5 | -8.9256 | -60.74169 | 2025-08-08 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| cce2ebd8-d9fc-3c4f-a75c-c124deb5d67f | -9.70661 | -61.30575 | 2025-08-08 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 91983a7b-989f-3c9f-b43e-0cfc3fb131f5 | -11.20067 | -51.43843 | 2025-08-08 05:25:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 50514051-98cd-32b2-b791-8d3689d49b0b | -8.90586 | -62.42942 | 2025-08-08 05:25:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 49135c12-abf3-3bfe-ad08-dd57ae149d3c | -9.70716 | -61.30227 | 2025-08-08 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4bec0f84-44c9-3223-9916-8a6b99f2ba1d | -8.90539 | -60.54556 | 2025-08-08 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 423bc786-2361-3997-abd0-eed0bc13095c | -8.92174 | -60.74466 | 2025-08-08 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 430fe524-6d12-3f14-a410-8710c2bec93e | -8.90707 | -60.5566 | 2025-08-08 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| de7e7a8c-249e-357e-9f1d-7a0dd88bb5f9 | -8.90262 | -60.54153 | 2025-08-08 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 086373c0-56fa-3bf2-be21-fb5948fdf0ec | -8.91046 | -60.60023 | 2025-08-08 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bdd9e60e-be9e-3119-adbc-2e8aef172800 | -8.90543 | -60.56711 | 2025-08-08 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3f80e472-19f2-3a2e-a8e7-e869004bdfc4 | -8.90926 | -60.54258 | 2025-08-08 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 56cc0d8d-739e-30bc-8178-e257848a1600 | -9.70385 | -61.30174 | 2025-08-08 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 844f2cec-3d60-380c-b9aa-f63bd0221a34 | -8.91207 | -60.56816 | 2025-08-08 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 98c8ffda-f6f1-36a7-8ebc-c9a0095bfdaa | -8.92065 | -60.75164 | 2025-08-08 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 681cbc26-3b11-379a-bd2b-99474330ac83 | -9.92828 | -60.49606 | 2025-08-08 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1ac83bdc-74f7-3e3a-a48a-94f9a027cd98 | -11.19856 | -51.44257 | 2025-08-08 05:25:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 14b97773-2dff-33fa-ae16-e1b01613dfd7 | -9.24829 | -58.76199 | 2025-08-08 05:25:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a9225dd9-41ca-33b8-8c88-ad925e672d1e | -9.94201 | -60.46928 | 2025-08-08 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bf5917bd-1a0e-3204-b5f2-eb80b21bd08e | -9.71102 | -61.29931 | 2025-08-08 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 64e14b61-b2eb-3293-855f-b72cd04aa53b | -8.92342 | -60.75565 | 2025-08-08 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b22bfe0c-8281-3034-97f7-a9ae2e8a2c5b | -9.31562 | -62.65026 | 2025-08-08 05:25:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 08949728-7b64-343d-8b1c-f4b1ccd6e971 | -9.93436 | -60.457 | 2025-08-08 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 779aa3af-e839-3407-a987-cdb1bf21e663 | -8.92891 | -60.74222 | 2025-08-08 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0ea31e48-e988-34e6-9018-53ff5f7355ef | -9.31678 | -62.64307 | 2025-08-08 05:25:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e85ec845-72f4-36ba-b3e3-8dbd8ee66587 | -9.71542 | -61.29287 | 2025-08-08 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bcdd1a27-a89b-38e3-a0de-b426fcd69fc8 | -8.92397 | -60.75217 | 2025-08-08 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fc22e277-8507-311a-9e28-02296c27da4f | -9.93096 | -60.49665 | 2025-08-08 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 609119f1-193d-3af7-be8e-ec56d0c687d2 | -9.93758 | -60.47586 | 2025-08-08 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ab773499-683d-3cb9-81da-1c5afb855eba | -9.93709 | -60.50126 | 2025-08-08 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bebc82ee-0183-317c-8718-5576a2328077 | -9.936 | -60.50837 | 2025-08-08 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5d04609a-5497-3b9c-8191-b252df684a1e | -8.90872 | -60.54609 | 2025-08-08 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 331dab0d-0389-36c9-93fe-73e0334aeb21 | -8.91101 | -60.59673 | 2025-08-08 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2d120481-d2fc-30c4-bbe3-bbda87ecb9c4 | -8.92011 | -60.75513 | 2025-08-08 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 99c948c0-bfcc-3a43-aab9-4c3e2d7bd441 | -8.91375 | -60.57919 | 2025-08-08 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fa671bfd-38fd-3446-bfba-b8f1f3f645eb | -9.92713 | -60.45951 | 2025-08-08 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 77b7c6d9-1dd1-3eab-b9b8-23b61dc2323d | -8.92946 | -60.73873 | 2025-08-08 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 1601288b-68e7-3fd3-b216-8462b81c42d5 | -8.90437 | -60.59568 | 2025-08-08 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a32c7c96-e4c6-3244-9b51-e3f93dfc0e3f | -9.64463 | -62.91258 | 2025-08-08 05:25:00 | NOAA-20 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 330adf6e-95ea-3026-bffa-89605f03285e | -8.90992 | -60.60374 | 2025-08-08 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f7667ba2-d09f-3adb-afe1-1539d68e97d4 | -9.93654 | -60.50481 | 2025-08-08 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| df1c908b-ace0-3310-ae27-d129ba2365cf | -8.9093 | -60.56413 | 2025-08-08 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 21f7cc09-157a-3ef8-9bee-8e74f0281106 | -9.93321 | -60.50428 | 2025-08-08 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4080c9f3-e14e-3bdd-93df-660c9c7aae61 | -8.91902 | -60.76212 | 2025-08-08 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 42cec6e9-a4c6-3246-a2f0-f7f37f9ab23c | -8.92337 | -60.73418 | 2025-08-08 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a986854a-6efa-3bae-97fb-448549cb83c7 | -8.90485 | -60.54907 | 2025-08-08 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fa209537-daeb-3903-aad4-8726654aaa47 | -11.19907 | -51.43856 | 2025-08-08 05:25:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 74cd58f5-0eb0-3e68-80b3-26167cb51624 | -9.93478 | -60.47179 | 2025-08-08 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f70352b3-1ac2-3dce-8d51-5c9b7e821aa4 | -9.7055 | -61.29128 | 2025-08-08 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 29a3b784-aa2c-3ec1-a620-7685ae5fdb2d | -8.92837 | -60.74571 | 2025-08-08 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 399d7f9d-a513-36ca-ac5f-e9c74fe3bbf3 | -9.93049 | -60.48186 | 2025-08-08 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3fdffafb-9112-3fdc-b825-2168f99b32e5 | -8.90875 | -60.56764 | 2025-08-08 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 723fcb1e-82ed-339f-a735-c4e247433da1 | -9.93933 | -60.50888 | 2025-08-08 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| cc4895d3-b42a-350e-a859-d34f84c73ad6 | -9.93485 | -60.49363 | 2025-08-08 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2ee4463d-a5ad-3bcb-86dc-49be8d675d9c | -9.26301 | -60.77763 | 2025-08-08 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 96a33d6b-e3e9-328c-b629-23c794a8b921 | -10.04086 | -59.35572 | 2025-08-08 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4a8f9d1f-fed5-36df-b452-6fa8c664b7f9 | -8.90824 | -60.5927 | 2025-08-08 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b8562548-486c-3cdf-9a9a-e5db91d1898c | -8.92505 | -60.74518 | 2025-08-08 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9e9ea43f-68f3-3090-a4fe-cd604dbeb80d | -16.3612 | -53.34191 | 2025-08-08 05:25:00 | NOAA-20 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 7.0 |
| b072cbd0-a391-304d-9453-2548e56a511d | -9.92379 | -60.45898 | 2025-08-08 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 79d3711c-4093-3768-84a1-12206db8d7fc | -9.93375 | -60.50073 | 2025-08-08 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8af044e6-bc5c-3ba4-aae2-b3f4e728977e | -8.90985 | -60.56063 | 2025-08-08 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d59d5eee-40a4-3bb9-9112-5532837852a0 | -8.90594 | -60.54206 | 2025-08-08 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 8d64703e-1ec1-336c-9717-91285703674f | -9.64801 | -62.91314 | 2025-08-08 05:25:00 | NOAA-20 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7b1380f4-13b7-3916-bddf-efa42cd8b083 | -9.93315 | -60.48245 | 2025-08-08 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f6787688-5cd4-3cd4-b88a-eae001f89bbc | -9.70495 | -61.29477 | 2025-08-08 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3cac00b4-49d7-3449-a408-44bfba56d1f8 | -11.20019 | -51.44246 | 2025-08-08 05:25:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1f8eec64-6acf-39ce-927b-73af7250551c | -8.91258 | -60.5431 | 2025-08-08 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5a406468-b7dd-3116-89ba-6ce81077e3b8 | -9.94146 | -60.47283 | 2025-08-08 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| eefbe1a4-9fbe-3751-b975-c78003d9e2f3 | -8.91094 | -60.55362 | 2025-08-08 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8687f0ac-5159-33e5-a5de-c60e136be9bf | -8.91875 | -60.59077 | 2025-08-08 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 645f9bcd-43f9-3d80-92d3-4181c57765cf | -9.70331 | -61.30523 | 2025-08-08 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| df37db47-3817-3999-8b87-d2023da8df96 | -9.3162 | -62.64667 | 2025-08-08 05:25:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a0602818-1573-3e26-a5b6-aaf4af5c33a7 | -9.93539 | -60.49008 | 2025-08-08 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b657553d-a161-399d-b77f-1acaf40dfe7b | -9.9343 | -60.49718 | 2025-08-08 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fbe9e53c-5895-3aeb-8562-18694065115b | -9.92326 | -60.48438 | 2025-08-08 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0b25f02f-5d57-31fa-bc7d-905fa9727404 | -9.92715 | -60.48134 | 2025-08-08 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 16f41465-c647-3f87-895d-3b383d4fd163 | -9.70771 | -61.29878 | 2025-08-08 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b4c59a55-30be-3fe3-95dc-62f988b17092 | -9.9266 | -60.48489 | 2025-08-08 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e292e705-4a2a-3871-bffb-c3a731714bdd | -8.90921 | -62.42996 | 2025-08-08 05:25:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e363c796-d760-39e3-8e4f-9240b20b5d23 | -9.70274 | -61.28727 | 2025-08-08 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6a1f01bd-f6e5-3b43-a206-f512d8a7b692 | -8.90207 | -60.54504 | 2025-08-08 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f404bfcb-ff20-38bd-b024-76b208b0a3fe | -9.93642 | -60.46112 | 2025-08-08 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3948d721-7a77-3449-b859-db1b5cd4c768 | -8.90817 | -60.54959 | 2025-08-08 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d28eb89a-8ef3-3993-9662-2a88ebcd12ee | -8.92288 | -60.75914 | 2025-08-08 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 05225169-9970-3656-a4c2-c33bd10327db | -9.71378 | -61.30333 | 2025-08-08 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| a6dcc608-a8d2-36c1-a15c-787dead34a00 | -9.93697 | -60.45757 | 2025-08-08 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3c593d6a-518d-3d13-9c79-b3453033a3fd | -11.19493 | -51.43767 | 2025-08-08 05:25:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6e8e2d34-7878-30a5-9989-20f87a3f2f13 | -8.91788 | -60.74763 | 2025-08-08 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 20016af8-570a-30dc-bd86-b79212eb477b | -9.70604 | -61.2878 | 2025-08-08 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6eec5b34-4086-3e9b-bff9-924247d0a432 | -9.70826 | -61.2953 | 2025-08-08 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 61ea719f-0826-3f96-9eeb-95246f7749a3 | -9.92994 | -60.48542 | 2025-08-08 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |


[Clique aqui para ver as próximas entradas](README25.md)
