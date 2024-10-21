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

## Dados Diários - Página 41

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| df4f205f-e74e-3cf8-9e61-8ee463cdde15 | -3.22674 | -51.2552 | 2024-10-21 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| fb582b37-cdcb-3311-858d-2d65e139818b | -3.22613 | -51.25908 | 2024-10-21 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5fbffc54-e984-34b1-b556-758eed61a5ab | -3.22263 | -51.25851 | 2024-10-21 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 511475df-76c6-32cb-81ce-5b95c08b40ab | -3.21975 | -51.25405 | 2024-10-21 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b3c32797-c34a-3d3e-944d-00593975d381 | -2.87697 | -51.65426 | 2024-10-21 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a61deb28-8d75-3ff0-b2e8-90162f1aa845 | -2.85205 | -51.28987 | 2024-10-21 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 785d9ed0-361c-39c0-a52c-3fefa544a927 | -2.84915 | -51.28539 | 2024-10-21 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 090488b0-c092-3756-9810-164a61ecff80 | -2.84853 | -51.28932 | 2024-10-21 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 9f0c4cad-a9d0-3eef-b468-99dd344f9eaf | -2.83545 | -51.30339 | 2024-10-21 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fa326be3-be15-3015-b19d-785e5e5a2788 | -2.83482 | -51.30733 | 2024-10-21 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e774bfa4-e99f-30f8-a3fb-93625bea4f39 | -2.83193 | -51.30285 | 2024-10-21 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d083749e-9c7e-3675-a2b7-ea03d45bf734 | -2.82516 | -51.2776 | 2024-10-21 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e0b56ea0-ef32-3f15-8b63-7c57225138d7 | -2.81812 | -51.90406 | 2024-10-21 04:36:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5be1f4e6-c08c-37d4-8336-35c950963898 | -2.81792 | -51.34513 | 2024-10-21 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 03258da1-ebc4-3f16-8fb7-66d57b2b415f | -2.81728 | -51.34909 | 2024-10-21 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 36205386-25f1-3b56-8177-1ca40dbd1ffa | -2.81503 | -51.34062 | 2024-10-21 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9688a8ed-65ba-30e8-901c-8f7ad4f00709 | -2.81439 | -51.34457 | 2024-10-21 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d99ebfc6-8a25-3fea-878f-4627285d96ef | -2.81376 | -51.34853 | 2024-10-21 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c50ec0f0-21e2-3df8-91c8-aa982e5a3aaf | -2.8115 | -51.34006 | 2024-10-21 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 24ec54a9-a8d7-330e-a96d-d507f00ae1f6 | -2.81086 | -51.34402 | 2024-10-21 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6c57261e-dcf6-3216-8f0f-847d75146921 | -2.81023 | -51.34798 | 2024-10-21 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 652deb8f-d3ba-3c97-849c-c0d593370dd6 | -2.80959 | -51.35193 | 2024-10-21 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 6d7c9d43-fcac-3b8f-a287-06d69ca6804c | -2.80589 | -51.60223 | 2024-10-21 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3138eaa0-c1b6-3ef7-99af-06ba6c977a36 | -2.80232 | -51.60166 | 2024-10-21 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f968e251-a3fd-3c52-8aee-2334458d6d15 | -2.80061 | -51.36271 | 2024-10-21 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 814066c7-a508-3f0f-8f34-b509a6a54bc3 | -2.79997 | -51.36667 | 2024-10-21 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 552d0009-d807-34c5-b5f7-c622c3956215 | -2.79772 | -51.35819 | 2024-10-21 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| f297580e-d8fc-3669-b117-5912a819d910 | -2.79708 | -51.36215 | 2024-10-21 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| ef46e522-f6f0-34cb-8452-949d55df45fb | -2.79644 | -51.36611 | 2024-10-21 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 16.2 |
| f97012bb-3505-3d60-b09f-7f53a0576434 | -2.7958 | -51.37008 | 2024-10-21 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 16.2 |
| 29e0f3fa-c770-3725-bb24-b962ff900c13 | -2.79419 | -51.35763 | 2024-10-21 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 0818b6e2-2417-34d1-b0f4-7c19dc19c856 | -2.79355 | -51.3616 | 2024-10-21 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| bd083b15-cfcd-3501-86ca-a4e8521a21a1 | -2.79291 | -51.36556 | 2024-10-21 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 16.2 |
| c9fbd741-519b-3a0d-801f-23ac4868f1a7 | -2.79227 | -51.36953 | 2024-10-21 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 16.2 |
| 705276a9-31a4-3d38-9816-bbd7c78738f5 | -2.79002 | -51.36103 | 2024-10-21 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f5b781eb-13ab-39b9-97e6-24e8f9c0d5c4 | -2.78979 | -51.36279 | 2024-10-21 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| b6112f33-827c-37dc-a4ea-99c6e54febef | -2.78938 | -51.36501 | 2024-10-21 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 144308ed-b48c-38d1-a203-3770bc307d67 | -2.78916 | -51.36678 | 2024-10-21 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 27b00161-350d-3a12-a5fd-a5014484b38c | -2.75557 | -51.96447 | 2024-10-21 04:36:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 242d738a-f13b-31f5-8aef-7bec9915f3b3 | -2.55184 | -51.24165 | 2024-10-21 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b33520a2-b31d-36fc-b084-b96bbcb3e64c | -3.62649 | -50.78682 | 2024-10-21 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d24ea799-d6e0-3997-87c6-c18458b78369 | -3.62591 | -50.79052 | 2024-10-21 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1bb802e8-d162-3284-9aea-90093da905b4 | -3.62532 | -50.79424 | 2024-10-21 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| e6762a48-8fa5-3f36-b269-06d335aac9a6 | -3.62307 | -50.78626 | 2024-10-21 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 34b7e6b1-f33f-3c2e-8351-948fdf187562 | -3.62248 | -50.78997 | 2024-10-21 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b56c98d6-1434-3403-abb9-65c94748f783 | -3.3923 | -50.80437 | 2024-10-21 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0a8a25a5-6dd0-3a30-b86b-c1168ef5740b | -3.3821 | -50.66962 | 2024-10-21 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cb20ade2-94e2-3141-81b9-7caa204f0a1b | -2.25464 | -51.93639 | 2024-10-21 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 033a2535-8ae2-3dcc-a235-e3a8418bfba4 | -2.25165 | -51.93152 | 2024-10-21 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 0cce1d4e-70b8-3324-8c20-bd07e8b272a5 | -2.25098 | -51.9358 | 2024-10-21 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 36afddf5-4cc1-30e3-97b7-def7d4d3e677 | -2.24799 | -51.93093 | 2024-10-21 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 36630043-bfb0-3dd9-a5a6-e8feb506a7ec | -2.24732 | -51.93522 | 2024-10-21 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 144251db-6b0b-378b-a5ca-50d313149f98 | -2.22916 | -51.88421 | 2024-10-21 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| e416d9f4-5184-32f7-b7b2-d791bcdfe5c3 | -2.22848 | -51.88847 | 2024-10-21 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8496fd8c-b33b-35fb-b880-5386b6e6c2d2 | -2.22483 | -51.88789 | 2024-10-21 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bfcb62d6-d897-325c-9408-d5f528019095 | -2.22118 | -51.88733 | 2024-10-21 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 998490c8-9226-3a3f-b08c-9f79735535c7 | -3.44492 | -51.6146 | 2024-10-21 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ba1ed9c8-d555-32e1-a6a4-9966fafa2b4b | -3.4417 | -51.63468 | 2024-10-21 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cb023628-eb2d-37f9-962c-a9f9d2115108 | -3.24141 | -51.73424 | 2024-10-21 04:36:00 | NOAA-20 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c63e1954-5e58-3112-9f7d-e79968905398 | -2.40532 | -50.43957 | 2024-10-21 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 412bddd3-d481-382d-8961-96b0d8f5c5ec | -2.3893 | -50.45217 | 2024-10-21 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 63594ad5-9f42-32d1-a51d-c138b50fc0a0 | -2.38894 | -50.4528 | 2024-10-21 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 96361423-ee5c-3bc1-b880-d8d8eff0ca0c | -2.3887 | -50.45586 | 2024-10-21 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 59541d8c-b5a3-3b62-b880-0c26cd29a4dc | -2.38552 | -50.45226 | 2024-10-21 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d45ad5e1-a0f2-37a3-8fe4-ee46ab5e672b | -2.28217 | -51.14012 | 2024-10-21 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ddc179d4-297c-38e8-962c-d214ce3340d0 | -2.28154 | -51.14403 | 2024-10-21 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0296c3aa-69b3-3bf3-8c96-af4fad5a10c8 | -2.28133 | -51.14116 | 2024-10-21 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 409ef0cf-043e-329b-aaf6-75f626b02bc0 | -2.28072 | -51.14509 | 2024-10-21 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5ce48c5d-e29d-3a6e-bb7c-5250deef0ecb | -2.265 | -51.24654 | 2024-10-21 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 05277094-6264-3152-9b8d-3e22d8521ab7 | -2.26468 | -51.24778 | 2024-10-21 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 3b73278c-7e1a-3994-bfe5-68bd7d970b61 | -2.26436 | -51.2505 | 2024-10-21 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bff69745-cc90-3b9c-b4c6-7c94bdf4bc3e | -3.38835 | -50.67437 | 2024-10-21 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1471ad0f-3986-392b-961a-b470bf445479 | -3.38552 | -50.67014 | 2024-10-21 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9ef6a548-a9ad-3551-a8be-950fbe7a287c | -3.36558 | -51.06312 | 2024-10-21 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b136f317-49c4-3759-b80d-380e1504f8eb | -3.28114 | -51.05759 | 2024-10-21 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a206e6eb-ff89-3d93-9a23-ce6df54bd1c7 | -3.27829 | -51.05325 | 2024-10-21 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7c1cf23a-81c5-3453-b6fa-05582ce0fa1f | -3.24868 | -50.93628 | 2024-10-21 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ab7f9119-354b-3674-8c12-4f932fd1f4dd | -3.24808 | -50.94007 | 2024-10-21 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fa0a41ef-c585-3d21-ad9f-1a6ee9809908 | -3.24119 | -50.85012 | 2024-10-21 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6a1a1a77-0caf-353c-8c72-78f1df0135a9 | -3.23775 | -50.84957 | 2024-10-21 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f6da9de2-5fa6-355d-8b5f-244fc3ba5b77 | -3.23715 | -50.85332 | 2024-10-21 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ef00c49e-f080-3a96-b12c-d6e7afd96b7b | -3.21933 | -51.00939 | 2024-10-21 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3534b3d1-f296-3a2c-91f3-d46993789f26 | -3.21282 | -50.8071 | 2024-10-21 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b642091d-3d28-3013-81fc-8d80eb70df9f | -3.21058 | -50.79911 | 2024-10-21 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| becd8d2c-644e-329f-8b5b-e29feced65a2 | -3.20998 | -50.80283 | 2024-10-21 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 17a5f23c-ee3e-30e7-8651-4c3b6ed1b3ef | -3.20938 | -50.80656 | 2024-10-21 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6c11717d-7776-3160-a09c-2fde3c2836e9 | -3.20714 | -50.79858 | 2024-10-21 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 1a11e862-8422-3a72-9972-990e8d1eab1f | -3.20655 | -50.8023 | 2024-10-21 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 5fda0a68-ed6f-3dfb-bbe9-769edd72103e | -3.20595 | -50.80602 | 2024-10-21 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 8e5abc49-92fc-3bd5-8393-ae9f571b7cd1 | -3.20466 | -50.79451 | 2024-10-21 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5166a71d-a088-3e4d-9717-aa0805958a38 | -3.20431 | -50.79431 | 2024-10-21 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7ead5e2b-3f45-33f8-ad16-b7df00127509 | -3.20408 | -50.79824 | 2024-10-21 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 5b390a70-b426-3ac4-9b3b-4e808badaf3d | -3.20371 | -50.79804 | 2024-10-21 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 70708743-82f0-3cbb-a7f7-0f72f24e96d3 | -3.20349 | -50.80196 | 2024-10-21 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| d39fa26f-f503-3999-a057-2a938dc42464 | -3.20311 | -50.80176 | 2024-10-21 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 7b0eae6d-a996-3626-a114-d086435556d2 | -3.20304 | -51.0224 | 2024-10-21 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| eb402320-30f8-3b72-bd4a-847007aec61b | -3.20064 | -50.7977 | 2024-10-21 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| e50fb3d3-1076-3688-8e8c-6173c5fa9de0 | -3.1696 | -50.81582 | 2024-10-21 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 050c42e8-37ce-3189-a34a-a2bdd6827e8f | -3.06748 | -51.05601 | 2024-10-21 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 53f869cf-ef4b-30ff-bd0d-bc7aee720e6e | -3.05528 | -51.0548 | 2024-10-21 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README42.md)
