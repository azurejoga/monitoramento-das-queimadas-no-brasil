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

## Dados Diários - Página 95

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2e5ae26b-7062-3bf1-865c-7de616222eb1 | -9.70539 | -59.05195 | 2024-10-11 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 34ae3961-3d68-39e6-904a-4bf40a5f5780 | -9.68268 | -59.24184 | 2024-10-11 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7ac098cc-d54e-3907-989e-5b3513ef0167 | -9.67937 | -59.24132 | 2024-10-11 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a47168e2-5090-3c48-a775-16e27445274d | -9.51969 | -59.50149 | 2024-10-11 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 99cf0b90-2808-3288-a555-df812c19a047 | -9.51914 | -59.50496 | 2024-10-11 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8acdebd8-c36a-346b-b9a5-5d246212d6ea | -9.51639 | -59.50097 | 2024-10-11 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3d7cb550-206e-3799-ade3-8fe57c81fda6 | -9.51628 | -59.10833 | 2024-10-11 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2dbd0229-5823-3a2a-b27c-6aff497c27d8 | -9.51584 | -59.50444 | 2024-10-11 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d227898b-2c13-3bb0-81ac-243cdce8e42f | -10.21876 | -59.40281 | 2024-10-11 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a0235948-86f7-3ced-92df-04fa95fd3006 | -10.05582 | -59.35904 | 2024-10-11 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a685d959-84d5-3465-8ba1-320b79bb242b | -10.05398 | -58.28926 | 2024-10-11 05:18:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a8b7f3ef-8bdb-3e0c-be26-60b2272226b8 | -10.05116 | -58.28511 | 2024-10-11 05:18:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b6e2198f-ece6-3f56-a039-24beb7f4d2ce | -10.05061 | -58.28875 | 2024-10-11 05:18:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4e8b4de2-c73b-3155-9e88-21b344fa825e | -10.5383 | -59.31743 | 2024-10-11 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5a8f20c9-55e3-3e5e-bbac-cdf35146aa5a | -6.4682 | -59.77367 | 2024-10-11 05:18:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 72ff654e-bd68-3599-b706-8a0a41503290 | -6.46765 | -59.77716 | 2024-10-11 05:18:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 10aa0c1f-15e8-309d-aeca-de397b73fc24 | -6.46489 | -59.77314 | 2024-10-11 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| aa8499f6-7e1e-3dd3-acca-8d34e8da3022 | -6.3872 | -59.9836 | 2024-10-11 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3b60871d-f529-32c5-802f-50297e3b9408 | -6.38608 | -59.99064 | 2024-10-11 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d2898dae-fe49-3172-9629-956ddae727a8 | -6.38331 | -59.9866 | 2024-10-11 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0fd77ca8-ea38-3e1f-b8f3-33037fe59150 | -6.22584 | -60.01544 | 2024-10-11 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 50672519-9b7b-33ef-9886-297ad2824686 | -5.5742 | -60.17089 | 2024-10-11 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 802b5944-0788-32a2-afe6-ea1f3035a78b | -5.57363 | -60.17447 | 2024-10-11 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d982d8df-6b11-309b-8453-756e4b551e60 | -5.57084 | -60.17037 | 2024-10-11 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 09af4d8c-3e2a-33f9-85ce-7af33a7527a2 | -5.57027 | -60.17395 | 2024-10-11 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| f4361525-f090-34a6-8c33-81c51a981bf3 | -5.44935 | -60.18377 | 2024-10-11 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| aeac031f-01d8-3146-bf2c-1c55cddc2a85 | -5.44878 | -60.18736 | 2024-10-11 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.1 |
| 31b1f5b0-0c71-348c-b68e-8729ecf3e68d | -5.33832 | -60.11882 | 2024-10-11 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d1cfa451-ca05-3bc2-b3d8-dc1bdc44cf60 | -5.33776 | -60.1224 | 2024-10-11 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6bb09076-9d94-3bf1-b896-1c36a701af5b | -5.33719 | -60.12598 | 2024-10-11 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0889ee76-b0cc-3681-b610-72befeac09bd | -5.33663 | -60.12955 | 2024-10-11 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0fa91d6a-e9bc-39ae-8edb-1c689baf11e1 | -5.33606 | -60.13314 | 2024-10-11 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ba56b555-054b-3a65-b534-7edfac9546a2 | -5.33549 | -60.13671 | 2024-10-11 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d72ec26e-1137-31f9-97aa-8201d36ab0d4 | -5.33496 | -60.11829 | 2024-10-11 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 51b28d4b-6fd7-36c0-b19d-01f27f949866 | -5.3344 | -60.12186 | 2024-10-11 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| c6325f4b-c48e-3895-bab2-95ab34e61024 | -5.33383 | -60.12545 | 2024-10-11 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 25b538ae-65bb-340e-993d-490b0bcfbdc4 | -5.33327 | -60.12903 | 2024-10-11 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| ec38a153-d1d7-31d2-91b1-1842ad4d40a6 | -5.3327 | -60.13261 | 2024-10-11 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ef2cbf3c-4c81-3b9b-a66b-92e6e2634450 | -5.33213 | -60.13619 | 2024-10-11 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 532090a3-6396-3c56-b22a-72081c9480f9 | -5.33157 | -60.13977 | 2024-10-11 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d8413734-2bb3-3f46-b12b-5b9577a0b43d | -5.33104 | -60.12133 | 2024-10-11 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| a52350d6-3d11-31bb-ac5f-8a50182723c2 | -5.331 | -60.14336 | 2024-10-11 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| cb3aa34e-669a-3237-a814-5a32df7a4b26 | -5.33047 | -60.12492 | 2024-10-11 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 2a4a3402-f231-32ac-b6ff-4b78272a11e6 | -5.32991 | -60.1285 | 2024-10-11 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 3ed0cd44-91ae-3dc0-877f-e245df501855 | -5.32877 | -60.13565 | 2024-10-11 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 055c64ac-643d-3efa-a105-ba58a424f4a1 | -5.32821 | -60.13924 | 2024-10-11 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ccb2adfd-09c4-3ffb-8af6-6d03f500ea14 | -5.32764 | -60.14283 | 2024-10-11 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 70e54ce6-f57a-3880-b5a6-1fda55a83e64 | -5.32711 | -60.12439 | 2024-10-11 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c5f2343e-cc3a-304d-a698-0b4f369d4c69 | -5.32654 | -60.12796 | 2024-10-11 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7faf0846-1292-3578-b92a-903c08ddc527 | -5.32541 | -60.13513 | 2024-10-11 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d0936a30-386d-3fd2-8a92-e54c3f6e6b2d | -5.32484 | -60.13872 | 2024-10-11 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| bc3fa543-2921-3bd7-9163-a099cbac34f5 | -5.32428 | -60.1423 | 2024-10-11 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| db72ca6e-52ff-381d-8cdb-9280e3eacbd0 | -5.31699 | -60.14483 | 2024-10-11 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dfe8ea63-061a-34a1-9fce-cabe1cd36937 | -5.30519 | -60.15399 | 2024-10-11 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 23c2bda9-7332-394d-a8a7-f48d234f37c8 | -5.30183 | -60.15345 | 2024-10-11 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 76e06e3d-166f-34cc-a51c-19e450ec6c83 | -5.29692 | -60.09763 | 2024-10-11 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| eabd4054-53d2-31b1-a5ae-bf639b0da1e6 | -5.29636 | -60.1012 | 2024-10-11 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c07b7747-6698-3211-9611-2d2affe94219 | -5.29579 | -60.10478 | 2024-10-11 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 62fe0553-c9d3-3aca-9205-f0bd4376c110 | -5.26073 | -60.19487 | 2024-10-11 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f2240c59-d0c6-3323-83b8-a50318234817 | -5.25515 | -60.18661 | 2024-10-11 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4d831795-7e9b-3ea1-b7fa-abe3cb96ce87 | -5.19876 | -60.26962 | 2024-10-11 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 96f9e022-6ec0-3e26-aab3-e96ff7a31915 | -5.19156 | -60.22773 | 2024-10-11 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| add7031c-9663-3995-9038-4bd6c407518f | -5.3337 | -59.80159 | 2024-10-11 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2fe14245-91e5-35a0-b74b-da2b034d9c57 | -5.33315 | -59.80511 | 2024-10-11 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 66e1169d-1514-39b4-a62d-05ee9a30637f | -5.19924 | -60.07071 | 2024-10-11 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 49f59957-f027-38c6-8e80-c98fe0d7c803 | -5.19867 | -60.07427 | 2024-10-11 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 696ca389-9103-3e65-a885-85b9749701a5 | -5.19588 | -60.07019 | 2024-10-11 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1c98525d-6fa2-3416-b58a-b5f29961aa93 | -5.19531 | -60.07375 | 2024-10-11 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 000df21f-12da-35ce-a6af-0097ba4592a4 | -6.91907 | -59.78478 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9cae84b6-1e6d-3b42-ac31-cc66b2648533 | -6.91852 | -59.78827 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bc38429f-d0f9-3bec-918c-d21fe493b061 | -6.8992 | -59.80305 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 88cb6806-113c-34f1-9e2a-e7fdebbc89e9 | -6.89589 | -59.80253 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8da321d1-e0a8-30f7-8d4f-a854a51d229c | -6.89534 | -59.806 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6aac27ac-8fd6-3047-a5cb-957e39134632 | -6.89257 | -59.802 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b83ea65d-8746-3059-85b6-bb837274905f | -6.89202 | -59.80548 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1e7d7a27-c2d7-3f08-9b78-0bd3a8011ff1 | -6.82331 | -59.7018 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fb180727-6010-3328-a85e-306e48346e5e | -6.81891 | -59.70823 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ea032d69-d266-3322-881b-0d133e03d729 | -6.79844 | -59.64447 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9d15708f-ba07-333f-bc26-dc5f20ae10c8 | -6.79623 | -59.637 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e18cd878-13de-3640-976f-619d534baf13 | -6.79568 | -59.64047 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d981e333-2abf-38b1-84d9-86f41eb9756e | -6.79513 | -59.64395 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 102d6ea9-f75a-377a-a768-b6edee5e555f | -6.79458 | -59.64742 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e5f3c694-64ac-33d8-bc5e-0e5f806cfb78 | -6.79292 | -59.63647 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ea527037-2f78-32a5-b6ac-0bcb8dc105ad | -6.79237 | -59.63995 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6bef205c-9bc9-3a78-9f4f-aaa098aab7ca | -6.79182 | -59.64342 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 33e18648-0174-3175-907c-501d5cf57b08 | -6.79014 | -59.61115 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5995006d-2242-39c5-b551-b24d97ce2734 | -6.77883 | -60.0462 | 2024-10-11 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b3243661-192b-3375-aa7d-23bfdcd10715 | -6.77827 | -60.04972 | 2024-10-11 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4fdbc5f4-b1b8-3a28-b1f0-2750ae10039d | -6.7755 | -60.04566 | 2024-10-11 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 199afa6d-610f-3e3e-88e7-e1f650e0fcd9 | -6.77494 | -60.04919 | 2024-10-11 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 05b7d065-e076-31fb-a6a5-c40de0542c37 | -6.77437 | -60.05272 | 2024-10-11 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f36b6a7d-b1ed-3701-a6be-438f934e37f8 | -6.77161 | -60.04866 | 2024-10-11 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9d4f0374-b304-35e9-88ed-4a5118bc64e8 | -11.54263 | -60.29328 | 2024-10-11 05:21:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 71981c74-bd66-30dd-b078-67c7cfaa9a03 | -11.54208 | -60.29679 | 2024-10-11 05:21:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 22b384c5-1c92-3ad8-bc27-c0c0e44761b5 | -11.42547 | -60.43172 | 2024-10-11 05:21:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e8f497dc-59e4-3bd2-9c8e-803a73365d51 | -11.42216 | -60.43119 | 2024-10-11 05:21:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0105823d-e770-3cfd-886c-4bb5475d626b | -11.42161 | -60.4347 | 2024-10-11 05:21:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6cd96a04-2798-3b4a-9967-900832204b69 | -11.41829 | -60.4557 | 2024-10-11 05:21:00 | NOAA-21 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 901501e5-7aa1-3aac-96e8-e2217825b041 | -11.41553 | -60.45168 | 2024-10-11 05:21:00 | NOAA-21 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3f232a5d-ab07-37ac-9fb6-098e677bf49d | -11.41498 | -60.45517 | 2024-10-11 05:21:00 | NOAA-21 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README96.md)
