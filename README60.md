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

## Dados Diários - Página 60

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3159239b-75a4-33a7-a4ab-bf9689f7acfa | -1.76099 | -54.09757 | 2024-10-23 05:38:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b89fd983-5e5a-36f1-9e7c-f69b96f0bfd3 | -1.54507 | -55.34835 | 2024-10-23 05:38:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f721e115-6968-345c-b918-bc912a666c84 | -1.54484 | -55.34868 | 2024-10-23 05:38:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 70633488-5a18-35dc-aa6a-bcbc498b7444 | -1.53982 | -55.34754 | 2024-10-23 05:38:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c50bf29d-a251-37d0-a24e-832edc4f5e40 | -1.53959 | -55.34787 | 2024-10-23 05:38:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6e178de5-b714-3731-b24b-d01d0a94d15e | 0.756 | -59.65071 | 2024-10-23 05:38:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f95efdab-4bb1-35e8-9fed-1902434e194a | 0.75549 | -59.64915 | 2024-10-23 05:38:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 56ff5669-7c7b-37c4-89dc-00a030afde10 | -2.79717 | -51.36774 | 2024-10-23 05:40:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 98a6bf4e-5da3-31f0-8751-ada5ae112e57 | -2.7903 | -51.36666 | 2024-10-23 05:40:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7ea86baa-9eb9-37ad-a535-c1ebc9497947 | -2.47088 | -51.98074 | 2024-10-23 05:40:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f07baecf-30c4-386b-bdd8-d35eb44940f6 | -2.47045 | -51.97185 | 2024-10-23 05:40:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 54086a33-c208-3410-be5e-0399799d5ca0 | -2.46962 | -51.97751 | 2024-10-23 05:40:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 20c14605-5250-302c-a29a-82c1629527e0 | -2.46512 | -51.97422 | 2024-10-23 05:40:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ce7c3f68-da83-3216-ae83-ec43a48ad3d5 | -3.52154 | -52.82539 | 2024-10-23 05:40:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e1c49203-f8dd-375f-89fc-b28d44e8dede | -3.52082 | -52.83044 | 2024-10-23 05:40:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b2af1db5-c9b1-3a85-84ac-7feaac42b226 | -3.51937 | -52.82599 | 2024-10-23 05:40:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1f4a11fd-62eb-3de4-a1cc-739494e092b0 | -3.51862 | -52.83105 | 2024-10-23 05:40:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 18e9786d-98be-3145-a21d-11c9973e74dc | -3.0736 | -53.24711 | 2024-10-23 05:40:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 2253d1e0-4c7b-3226-9883-f438d77838a7 | -3.07288 | -53.25204 | 2024-10-23 05:40:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 9471ad5d-5500-39cb-a944-d46b0d66e597 | -3.06673 | -53.25105 | 2024-10-23 05:40:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0c1d7f4b-410a-3382-8cd5-24f289d3455f | -3.06602 | -53.25589 | 2024-10-23 05:40:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| ffa6d53a-fce5-3d9c-a165-dce18293a13c | -2.78884 | -52.92622 | 2024-10-23 05:40:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ab48b19b-4493-3871-b67d-ae7fccc6b39b | -3.87801 | -52.32839 | 2024-10-23 05:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 1b788080-28a1-3eb5-94d3-1650c2efc575 | -3.79004 | -52.38925 | 2024-10-23 05:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 98d96987-9f86-3b21-9d07-506ac3ba2671 | -3.78918 | -52.39509 | 2024-10-23 05:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d5a01327-129b-3c20-90a1-3985b124e677 | -3.7886 | -52.39029 | 2024-10-23 05:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 03c829d1-2b54-31d8-874c-8fe547cbd6e2 | -3.78352 | -52.38805 | 2024-10-23 05:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e342f2a5-16d8-3ea8-acda-be9f1696d344 | -3.56281 | -53.75658 | 2024-10-23 05:40:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 00d5c1c2-07ef-3655-8329-3f8728c332ab | -3.56215 | -53.76104 | 2024-10-23 05:40:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| b648701e-0dfd-3e3c-81e6-2d6be972218f | -3.65459 | -54.21814 | 2024-10-23 05:40:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 29b1c4d0-e78e-30a9-aaa9-d6cbc75eed35 | -3.64899 | -54.21827 | 2024-10-23 05:40:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 64081e7d-b8c6-3a3c-8ee2-b0bd343271a6 | -3.64868 | -54.21777 | 2024-10-23 05:40:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 07b78df6-9338-3565-9889-81018c6fb762 | -3.64837 | -54.22239 | 2024-10-23 05:40:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 402b9c64-5add-32b4-924f-ebe446060d8b | -3.63183 | -53.97001 | 2024-10-23 05:40:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| eebaead7-45c7-38e5-a3aa-ec7c03e755d9 | -3.54134 | -54.74044 | 2024-10-23 05:40:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| b16490ee-fa17-3362-91db-e043afa66e0d | -3.54077 | -54.74422 | 2024-10-23 05:40:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 2d3fb6c0-d335-3aa4-98fb-5b607d03a205 | -3.53568 | -54.73977 | 2024-10-23 05:40:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 25ba5763-feb0-3231-b790-b5fd535ea42e | -3.53512 | -54.74356 | 2024-10-23 05:40:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| b0fdc634-b74a-3f93-ada3-839deac0acce | -3.49228 | -54.15329 | 2024-10-23 05:40:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cf34e1d9-bbdb-3180-b413-d26a1bcd1253 | -3.48644 | -54.15241 | 2024-10-23 05:40:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3820fdac-3a7f-36a9-b361-58ac61a7ca72 | -3.21938 | -54.8604 | 2024-10-23 05:40:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cb2e6cf0-1047-3ca0-9c3d-430a337582cf | -3.2188 | -54.86419 | 2024-10-23 05:40:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7f5d75ec-2c1a-33c1-a93c-0fcaa6b7087a | -3.21809 | -54.86153 | 2024-10-23 05:40:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| dcd22601-1ef5-3039-abec-96a5cef38058 | -3.10986 | -54.17119 | 2024-10-23 05:40:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b4f63dd4-840a-3b91-b353-30590ff6f9cd | -3.10985 | -54.16978 | 2024-10-23 05:40:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5d7c8dbf-dc0b-38e7-a692-f14415329ef2 | -3.10926 | -54.1739 | 2024-10-23 05:40:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ff2c0cda-622e-3de8-839e-f6cecb7fbfd9 | -3.10925 | -54.17523 | 2024-10-23 05:40:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d4df0207-9328-330d-96bd-8174e4eaf7bd | -3.10602 | -54.15732 | 2024-10-23 05:40:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| f4ad2c46-b2df-303c-aa43-b859f99ff007 | -3.10536 | -54.16169 | 2024-10-23 05:40:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| a84f7479-a236-3d4c-9841-5a9ee894e7ab | -3.10529 | -54.16019 | 2024-10-23 05:40:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 9721cf65-8c71-3e92-a6d8-f57c8de27a41 | -3.1047 | -54.16604 | 2024-10-23 05:40:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| e40fb906-7ed0-32d2-8939-a5a15a600f26 | -3.10467 | -54.16456 | 2024-10-23 05:40:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| ae4b700b-82c9-36fb-afa5-13bf01506aae | -3.10405 | -54.17036 | 2024-10-23 05:40:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 4c467223-14d2-3f51-ba6f-f42bb4f6ffd3 | -3.10404 | -54.16891 | 2024-10-23 05:40:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 3ba1b7eb-eb15-354a-aed3-572e5ebe244b | -3.10343 | -54.17313 | 2024-10-23 05:40:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 2ac4d244-5423-3c69-9352-e561505814af | -3.10342 | -54.17451 | 2024-10-23 05:40:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| cd1fff1e-f571-35b3-89dc-08d5009cb424 | -3.10284 | -54.17727 | 2024-10-23 05:40:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1ee97efc-4aee-3bc1-9bc2-5402a56a05f8 | -3.1028 | -54.17862 | 2024-10-23 05:40:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d3faffd5-8b7a-30ae-838d-89379b7d3c90 | -3.10226 | -54.18129 | 2024-10-23 05:40:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dc1b8672-88a0-3a1c-8187-dd786e20b39f | -3.1022 | -54.1826 | 2024-10-23 05:40:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cce6c19f-54e8-34a9-a7d0-6428fe1b0f63 | -3.10086 | -54.1521 | 2024-10-23 05:40:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| b6c853cc-cc01-3e03-832d-1b75f77df285 | -3.10072 | -54.15062 | 2024-10-23 05:40:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 557d5f81-1c0f-3341-89ba-90d8891b5a94 | -3.10022 | -54.1564 | 2024-10-23 05:40:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 38e28935-d9fb-30c6-87da-44624c4eb9fe | -3.10012 | -54.15487 | 2024-10-23 05:40:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 8e6e2886-1212-3c84-b157-1baf9c6cc604 | -3.09955 | -54.16081 | 2024-10-23 05:40:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 317377f6-4ab5-395b-a52a-b8f0d218066c | -3.09948 | -54.15928 | 2024-10-23 05:40:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 89efbbde-d1da-32ac-881e-3b7a6436283f | -3.09889 | -54.16517 | 2024-10-23 05:40:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| fd69664f-79a9-358c-bf4b-7cbdba5de2b4 | -3.09886 | -54.16367 | 2024-10-23 05:40:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 124421e8-a045-3c6b-b64e-3da22a75354d | -3.09824 | -54.16949 | 2024-10-23 05:40:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 5958de59-78e9-397a-8806-7e55fb4acb3c | -3.09823 | -54.16801 | 2024-10-23 05:40:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| c34ec51c-5153-3d4f-907a-7e7a141220bb | -3.09762 | -54.17228 | 2024-10-23 05:40:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 0f9af070-8b5c-318b-83a5-de655cd1f945 | -3.0976 | -54.1737 | 2024-10-23 05:40:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 4c33a98f-0166-3240-8a07-34398a8959d5 | -3.09702 | -54.17645 | 2024-10-23 05:40:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0f781fa2-87ce-305c-b497-9ef8b08ef3e7 | -3.09698 | -54.17786 | 2024-10-23 05:40:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 52f2609a-219a-302a-93ec-e0f7f1b6ec9d | -3.09643 | -54.18058 | 2024-10-23 05:40:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 071bb2fc-c01c-3077-a9a2-8d0802757f74 | -3.09636 | -54.18194 | 2024-10-23 05:40:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8557116b-d728-3b2f-8f83-7aadc62fc5fc | -3.09585 | -54.18464 | 2024-10-23 05:40:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a3b05b2c-78dd-3372-a92a-d010aefc99ea | -3.0944 | -54.15553 | 2024-10-23 05:40:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a2c16155-bc97-3c91-a9de-6f959bd7e95a | -3.09374 | -54.15991 | 2024-10-23 05:40:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c516a682-fcf1-34fb-af3a-cc9091ab67b1 | -3.09309 | -54.16423 | 2024-10-23 05:40:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bf91f38f-6f41-375c-8339-bab3b6cb680a | -3.09244 | -54.16854 | 2024-10-23 05:40:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4f3e6c25-2dbf-3d9f-81c0-57fbcdad22f1 | -3.0918 | -54.17278 | 2024-10-23 05:40:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 210ad016-6454-3a97-bad1-2a9fb0c45405 | -3.09118 | -54.17696 | 2024-10-23 05:40:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 215eb11c-32ce-3fd0-b397-4eaa15e4ba98 | -3.0873 | -54.16322 | 2024-10-23 05:40:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1cb5bb23-796c-3b11-b81d-e31936c160dc | -2.90069 | -54.25641 | 2024-10-23 05:40:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 23212cce-e325-38f8-8814-3a2d3361f6b4 | -2.89433 | -54.25945 | 2024-10-23 05:40:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 30da5984-6422-390d-80d5-aab44d1ea7e1 | -2.75539 | -54.03905 | 2024-10-23 05:40:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d59db119-3338-315a-8782-1ed7835789ed | -2.75019 | -54.03397 | 2024-10-23 05:40:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| d44ef24c-4dd0-3dae-add6-14e106a687de | -2.74957 | -54.03816 | 2024-10-23 05:40:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d58c25f9-593f-33b1-8fe1-e5a90f65c9f9 | -2.58038 | -54.0192 | 2024-10-23 05:40:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 9138b3d0-8217-3036-8314-8a4877c8e9dd | -2.51366 | -54.1077 | 2024-10-23 05:40:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6a0d3b17-81c9-361c-90aa-e75ddd695047 | -2.51302 | -54.11201 | 2024-10-23 05:40:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cc60724d-e41c-3316-9617-451709baca91 | -2.33214 | -54.33645 | 2024-10-23 05:40:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c5d5fd08-b7a8-3308-9e11-e1875dc13cb2 | -2.33157 | -54.34034 | 2024-10-23 05:40:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0e194147-4595-3550-9a81-78ede0c0e5b5 | -2.32963 | -54.33614 | 2024-10-23 05:40:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 150e022b-47f0-3d5a-baf4-cb2323ed9042 | -2.32904 | -54.34002 | 2024-10-23 05:40:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 23ec5338-c3d6-3882-bb4e-d754c76ac7ef | -3.58898 | -53.78683 | 2024-10-23 05:40:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1c912c51-388e-3774-a4ba-a3b6d0a00095 | -3.06964 | -53.83588 | 2024-10-23 05:40:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d764ad31-6a96-30a8-92b2-d10a03dcc03c | -2.94826 | -53.70758 | 2024-10-23 05:40:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 46c95537-e865-3551-b716-309adeaa0681 | -2.94295 | -53.70229 | 2024-10-23 05:40:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README61.md)
