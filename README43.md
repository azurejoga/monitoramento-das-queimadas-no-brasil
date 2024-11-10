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

## Dados Diários - Página 43

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f038c7bb-1905-339d-9da7-0ab7d2b7846a | -5.78869 | -46.53497 | 2024-11-10 04:14:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b5b2e430-e1e1-35ac-a997-6cdc8ef28e0e | -5.23525 | -46.66639 | 2024-11-10 04:14:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fc737c80-11c3-34a5-a364-8ee9af073e6d | -2.38731 | -54.09318 | 2024-11-10 04:14:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f7f2356e-0673-309d-b630-38ac8f840497 | -3.92218 | -46.40861 | 2024-11-10 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0e2aea86-8989-3377-875e-d0cc0ae0928b | -2.48359 | -48.81125 | 2024-11-10 04:14:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b100d477-d648-31c0-a183-34f856a647a3 | -5.81576 | -44.11874 | 2024-11-10 04:14:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 7f94df39-04b4-3f46-9a81-e4054217c75d | -2.93216 | -49.36 | 2024-11-10 04:14:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 108c0442-43bd-3940-80c1-fc6f1a54d52e | -3.94957 | -48.1667 | 2024-11-10 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 5e82c0f5-163b-319d-90a5-557fa049dc32 | -2.31524 | -48.53675 | 2024-11-10 04:14:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 9cc1f6a1-9633-316c-a34c-7bb614cb8484 | -2.63118 | -46.7676 | 2024-11-10 04:14:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 0dbd0853-602b-3773-80f2-cc241e726ad6 | -3.24447 | -50.30806 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 7148dde6-e099-3351-9c83-9e2882eaa179 | -2.57253 | -47.33883 | 2024-11-10 04:14:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fa7a35e0-3cef-37d5-b117-a6ef609817d3 | -5.13874 | -48.25283 | 2024-11-10 04:14:00 | NOAA-21 | SÃO PEDRO DA ÁGUA BRANCA | MARANHÃO | Brasil | 2111532 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4bafbe2b-b648-3064-a80f-4efb0f8661b3 | -1.42556 | -52.27501 | 2024-11-10 04:14:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 3b9d4d6a-bdd7-39cd-a96c-4cb4bd5b6c6e | -6.18354 | -41.88812 | 2024-11-10 04:14:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 18accab2-86fe-3bb0-a596-edf9fe9b34f2 | -2.31842 | -50.67221 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b91ef285-daff-37b8-9421-e18c1095ba20 | -3.22361 | -50.29173 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 25.1 |
| 6754c510-c9b4-3dd7-8cc0-0d530d2a35ff | -3.26043 | -48.75118 | 2024-11-10 04:14:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| ab379097-acd5-3c1d-8a62-1e94f2367400 | -5.69354 | -45.17548 | 2024-11-10 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 62b49332-f7db-3bf9-b687-c37b4a083281 | -3.40564 | -50.28799 | 2024-11-10 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4fcda9c0-8b78-3535-ba4f-9bb492e1fc14 | -4.38543 | -48.57812 | 2024-11-10 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6653aa4a-8ac0-3b4c-941a-822490d16419 | -2.65778 | -49.39727 | 2024-11-10 04:14:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d19d873f-96ac-333d-bf0e-28aaeab76470 | -2.50545 | -47.46812 | 2024-11-10 04:14:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| de2fd190-bc87-3c1a-a372-198aa8097a7a | -5.37867 | -42.76167 | 2024-11-10 04:14:00 | NOAA-21 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 31093a9c-66fc-3ce1-91c7-61941ee8a261 | -3.98824 | -46.41339 | 2024-11-10 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 822b9835-3a85-3063-aa23-c19f34d85cfb | -3.33891 | -50.35961 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 6ecfb59b-b0a2-39cb-ad39-9283f03e2392 | -3.41354 | -50.30031 | 2024-11-10 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 518fb843-89e3-3b60-8142-18f5ae8ae52f | -4.36189 | -48.14771 | 2024-11-10 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a8f022ac-f97d-3107-bbf1-d823fd058f53 | -3.75876 | -41.02797 | 2024-11-10 04:14:00 | NOAA-21 | TIANGUÁ | CEARÁ | Brasil | 2313401 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| ac010bc7-c5b0-3b9f-b5c9-c5d32df1d84a | -3.24551 | -46.48701 | 2024-11-10 04:14:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| eae74e8f-b09a-330f-b5dc-bf7162a58d6c | -2.09309 | -48.82141 | 2024-11-10 04:14:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 17.0 |
| 2e93a451-3567-372a-aba7-8e68a59349f0 | -1.5401 | -52.20995 | 2024-11-10 04:14:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 902757ac-4206-3de5-9a04-812cb0330c15 | -5.68966 | -38.04087 | 2024-11-10 04:14:00 | NOAA-21 | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 1.2 |
| de3d53da-b0fc-311f-808e-0283f16f4b33 | -3.35393 | -51.67792 | 2024-11-10 04:14:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d70b6971-14ec-3301-a3ff-df89f7c56796 | -2.84614 | -46.65573 | 2024-11-10 04:14:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ecb7be52-bfbd-3be5-876f-58cb07c79b2d | -1.93443 | -47.85147 | 2024-11-10 04:14:00 | NOAA-21 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8ca61331-f29f-3116-9b32-3a890aa128b0 | -3.06734 | -48.03148 | 2024-11-10 04:14:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| d1f43b29-c592-38e2-8294-1bf75f0651a4 | -2.41243 | -48.52183 | 2024-11-10 04:14:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| decd4ef9-62cd-3478-b69f-99e23b2b93ef | -3.8348 | -54.59858 | 2024-11-10 04:14:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| eab839cf-2d17-3702-a06d-fffdec21e726 | -3.23384 | -50.32087 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a64328f6-4e57-3a20-987f-ad9c86ea40a6 | -5.72 | -42.70933 | 2024-11-10 04:14:00 | NOAA-21 | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 3732f0e8-a27d-34a5-80ce-d7f84127ab53 | -5.51032 | -41.68673 | 2024-11-10 04:14:00 | NOAA-21 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| de83f029-0c26-34fc-b685-efc43c1304fb | -6.23373 | -42.92743 | 2024-11-10 04:14:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 90a0297c-375b-3eda-8896-ed0b35f993d8 | -3.28281 | -53.66909 | 2024-11-10 04:14:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| d6903bce-e8f4-3ab3-8549-4592df0b9454 | -4.28392 | -46.28201 | 2024-11-10 04:14:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8470a084-22e7-3e6a-b747-1b24491c8bab | -3.35022 | -54.13102 | 2024-11-10 04:14:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3fe3624b-29d8-34e2-946f-d9ba3708912a | -4.11827 | -46.87917 | 2024-11-10 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9f81de32-4af5-3e71-b8b6-7a312e93bcff | -5.465 | -41.65386 | 2024-11-10 04:14:00 | NOAA-21 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 786416a3-d264-365f-86a0-e3b1b787587f | -1.49184 | -55.43896 | 2024-11-10 04:14:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| f3fbafcc-bbdf-3a6b-900d-09f1c9554429 | -2.72955 | -45.06799 | 2024-11-10 04:14:00 | NOAA-21 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5513391b-3158-3f26-a61d-ac733748c03f | -5.23804 | -46.23048 | 2024-11-10 04:14:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 56f7fef9-27b4-3806-8113-8eb91cf9d202 | -2.10983 | -50.56768 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 9e1836ce-f23c-3438-a260-db3668a46556 | -3.13342 | -50.44415 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 203.7 |
| ca57954d-4364-36b1-b952-d14ddacd7b5c | -3.15242 | -45.94731 | 2024-11-10 04:14:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1a479215-22da-3943-ae5c-a97218dfbb51 | -2.81092 | -49.86967 | 2024-11-10 04:14:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 48791a52-dcb0-365d-ac1b-b66032c1ebd2 | -3.0174 | -51.04296 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fc3d517c-1842-35f8-8377-c081347be97e | -4.28342 | -48.19613 | 2024-11-10 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e26d1602-7efe-3078-a4a3-10fddaaeeeb0 | -2.91931 | -49.49827 | 2024-11-10 04:14:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f4572fb4-f19a-3168-becd-800248cc3253 | -2.39766 | -46.18354 | 2024-11-10 04:14:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 83b5b1d4-b172-3ca3-8f55-240016f61334 | -3.88965 | -49.95007 | 2024-11-10 04:14:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d1d0fa6e-f3bb-3adf-a1d3-c427680759e5 | -1.59047 | -52.18623 | 2024-11-10 04:14:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 224e7d0e-fa0e-32c6-ae00-904d5e4895aa | -2.87497 | -50.41328 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c53ff0dd-06e4-3613-9a51-dcb82b42515e | -1.29023 | -53.71474 | 2024-11-10 04:14:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 23.0 |
| 88444d2a-0eb1-3e90-814c-5d7b959edea6 | -5.58854 | -42.81189 | 2024-11-10 04:14:00 | NOAA-21 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| ef563cf3-a303-360a-9d86-dfd1aa2c5e55 | -2.67627 | -51.81819 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 0e6f367b-7556-3cfd-99fd-bc352a2fdabf | -2.91464 | -49.35249 | 2024-11-10 04:14:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a7c40350-1418-3e1e-9ee4-3a0bf9a20954 | -4.06243 | -49.28534 | 2024-11-10 04:14:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1f2f4628-6ec2-3358-aa10-3cf949dcdecc | -1.83574 | -52.06986 | 2024-11-10 04:14:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e5841153-a6a2-3947-9f71-5ae9c380377b | -2.29648 | -46.4981 | 2024-11-10 04:14:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ee0c5231-50d9-3251-b80f-6c67ec6dcc2d | -2.18913 | -48.3694 | 2024-11-10 04:14:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4885c5fb-13a8-3cef-89a6-e0a6aff3c825 | -2.097 | -46.53455 | 2024-11-10 04:14:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bd07fbac-35c6-3618-9483-42458a2ef0fe | -2.84993 | -51.36432 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| cc7f5584-ecc6-3146-9de1-d1e3fd4d67b7 | -2.69658 | -51.69773 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ed60a6c2-918c-3924-9657-117ab5a4955c | -4.12247 | -43.59349 | 2024-11-10 04:14:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 308c7343-7a8e-33f6-a6e1-173ce5337cfd | -3.59398 | -47.34416 | 2024-11-10 04:14:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| a8ca5390-f011-39e1-bbbf-c7d0a19a64eb | -3.81162 | -44.46526 | 2024-11-10 04:14:00 | NOAA-21 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d65cf1f6-fcd3-38a9-9344-ef7f3c37bfcd | -3.94894 | -48.17052 | 2024-11-10 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| e4a6d60e-f299-3ed2-9a7d-e0b13e35cdba | -3.95564 | -49.43998 | 2024-11-10 04:14:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c75a969b-e21d-3016-a6c9-b5a76f180563 | -4.27929 | -48.19546 | 2024-11-10 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 25c1817c-d4a3-3731-8f85-77ce9673c964 | -2.27799 | -48.71427 | 2024-11-10 04:14:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| aabb72d0-61e3-3b58-a249-3b3fd448a170 | -1.49291 | -55.43244 | 2024-11-10 04:14:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 17e712fb-fc70-3691-9df4-dc1946171753 | -5.01972 | -45.04003 | 2024-11-10 04:14:00 | NOAA-21 | SÃO ROBERTO | MARANHÃO | Brasil | 2111672 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3791c5be-66f8-31cd-816c-c746f0b0f00a | -3.36048 | -53.41039 | 2024-11-10 04:14:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| b5c03db2-a2ad-30c3-94a4-63aaf301cd3a | -4.5611 | -45.59395 | 2024-11-10 04:14:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ff32b61a-5518-3593-b824-cfa2dada0033 | -5.01225 | -45.04262 | 2024-11-10 04:14:00 | NOAA-21 | SÃO ROBERTO | MARANHÃO | Brasil | 2111672 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| bd411fd7-3867-3bba-9c85-eddaebc1fbf7 | -3.18142 | -51.2473 | 2024-11-10 04:14:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 852f8edb-ba20-344a-b33c-1d5946249134 | -4.10155 | -45.70319 | 2024-11-10 04:14:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ef77951b-cc96-3ce1-b84a-c21dd2408c93 | -2.40852 | -46.7778 | 2024-11-10 04:14:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d761f4be-b998-389e-8836-f88b6873497e | -5.47357 | -44.61987 | 2024-11-10 04:14:00 | NOAA-21 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e09493b0-26d4-3678-92f8-ed20c69b03b9 | -3.24556 | -50.27894 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7c4356ab-5236-3bfa-ae22-4031879600fa | -2.68169 | -46.78378 | 2024-11-10 04:14:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d7420510-89c0-327f-8ae0-1497e77873d7 | -4.37607 | -45.57058 | 2024-11-10 04:14:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 94b55949-e436-3d54-ac9f-ff01c5c3cf23 | -2.03661 | -52.05139 | 2024-11-10 04:14:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 5d090a05-858b-3340-8d3e-b77b98b44f3c | -3.35176 | -51.68156 | 2024-11-10 04:14:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ca9c6033-4355-3c9d-ad5e-649c65939bef | -4.42579 | -45.623 | 2024-11-10 04:14:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a041179c-123f-3cd2-aa94-f33c1a61ad20 | -3.58923 | -47.34857 | 2024-11-10 04:14:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| e9d2a7ed-8cb9-34b1-83da-2f4260fa79ad | -3.4533 | -49.11832 | 2024-11-10 04:14:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| af87ee37-06ef-304d-ada6-4ac99fb5d0ce | -2.39911 | -46.17458 | 2024-11-10 04:14:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 299adee4-a7f1-30d6-82ca-94e43b5509d1 | -3.97204 | -48.18531 | 2024-11-10 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| f8366775-2df2-31ff-9bef-17b5f38a0771 | -1.2194 | -51.75191 | 2024-11-10 04:14:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README44.md)
