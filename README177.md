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

## Dados Diários - Página 177

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 46f8acc2-9944-32c5-85b4-88393d10cae5 | -3.59183 | -54.67212 | 2026-10-08 05:42:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 250d2c99-c7dc-336f-9c09-317eed258ba6 | -3.29778 | -54.67625 | 2026-10-08 05:42:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 07998ad3-2ced-3b20-b5a2-1a038b0d9334 | -2.57252 | -56.16903 | 2026-10-08 05:42:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 383e6e31-e4ca-3415-b38b-4de6d7d42e6b | -3.02189 | -54.07416 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3af1bf0f-ff00-361f-9e17-ce03df28c12b | -3.84008 | -55.97445 | 2026-10-08 05:42:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 2421e019-c7af-3890-a54c-8d3e5b1996f8 | -3.28674 | -60.99556 | 2026-10-08 05:42:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8bfd387a-9e90-3e9b-853f-605c167405a8 | -2.50724 | -56.16636 | 2026-10-08 05:42:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 15.2 |
| bc4a64ec-0646-3116-82ed-129cf5176184 | -3.13321 | -54.36516 | 2026-10-08 05:42:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8ab96006-89b1-3e2b-88fd-714c124ffd74 | -3.74652 | -59.44589 | 2026-10-08 05:42:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 59c8dbd0-1b5a-394d-8795-625f1932b9dc | -3.59847 | -61.64388 | 2026-10-08 05:42:00 | NOAA-20 | ANAMÃ | AMAZONAS | Brasil | 1300086 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2780e3f3-118c-3738-84fa-1b963dfedb28 | -3.5538 | -59.49608 | 2026-10-08 05:42:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2e545e2d-1523-3e12-970d-d4dc14957c1e | -3.59605 | -54.67901 | 2026-10-08 05:42:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 76b5e373-44a3-37ff-a841-f8abf4c80247 | -4.12647 | -59.88842 | 2026-10-08 05:42:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 52fafa83-2cdc-3473-9906-4f479bd6578e | -3.00978 | -54.08241 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| a99bb9bf-c8db-3e91-b872-cad5bfaa17cc | -2.46306 | -56.08781 | 2026-10-08 05:42:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cbe1373a-f3d4-3a67-ba1f-cced86e0e2b9 | -3.85984 | -56.00299 | 2026-10-08 05:42:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ff1b618b-148c-3485-8fbf-0cfa74a3c743 | -6.23533 | -52.85328 | 2026-10-08 05:42:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 50f74de8-0588-381a-b2c7-4b58f50b2cc8 | -3.19566 | -50.56057 | 2026-10-08 05:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 3b3600d0-a209-3659-9dd4-cce5dba7c73c | -3.10438 | -54.27331 | 2026-10-08 05:42:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| db3867bd-fa88-36c4-b082-57090089daaa | -3.30134 | -54.70309 | 2026-10-08 05:42:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| df849580-1ab8-391f-8c95-96c513dcf168 | -3.18764 | -58.654 | 2026-10-08 05:42:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 437eba3d-87e8-3c54-ab59-14040052a0ac | -2.87476 | -54.47629 | 2026-10-08 05:42:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8e32a9ef-7d5e-3107-9299-4613cb83e9fa | -3.30112 | -54.06511 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 668cb499-4554-3198-9031-a12482a682ce | -2.83885 | -57.48602 | 2026-10-08 05:42:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8b994f2d-d843-32e0-bcaa-d199d04f4641 | -2.86887 | -54.8829 | 2026-10-08 05:42:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7232ca1a-c5fd-38e2-8f63-653389f41e54 | -3.95976 | -56.11568 | 2026-10-08 05:42:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b696a99a-1b62-3ea5-93c0-df3c70d63b02 | -3.49799 | -59.27736 | 2026-10-08 05:42:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 60644b42-d6d9-3c13-a32a-28c17a9e87d9 | -2.76396 | -54.11076 | 2026-10-08 05:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9ab4caa7-9446-3165-a151-133360ed4418 | -3.64589 | -59.17012 | 2026-10-08 05:42:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7ad1f6c1-1878-3683-99b9-ffec7ef4f246 | -3.98023 | -56.21986 | 2026-10-08 05:42:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 6b8a8c14-1df9-3a54-b853-c622dbdbbd27 | -2.99877 | -54.04696 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1a2da5a0-a84d-3b03-86c2-67ae15d14124 | -3.95936 | -59.99983 | 2026-10-08 05:42:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 05988cf4-7f9e-347b-8c3f-ee12c6b5415a | -3.00359 | -54.05109 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 881351fd-d81d-3b0b-bd21-b15f44276cfa | -2.98758 | -54.08569 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 20.0 |
| d2a74e02-811b-3c7f-b916-b638e067bafe | -3.08823 | -53.96122 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 22.2 |
| 1647d9cf-9e64-3e38-bcfa-df4405df5c02 | -3.16723 | -58.63074 | 2026-10-08 05:42:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 273770f5-2090-3f01-a739-f6daffcd70ed | -3.30203 | -54.0376 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6deae048-0955-3d2a-a4ce-48f23464fef9 | -3.07577 | -54.24919 | 2026-10-08 05:42:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9313952d-a31b-3daf-b437-e230c7fbce05 | -3.7168 | -59.33934 | 2026-10-08 05:42:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 01588daa-3f49-341d-af19-dbcf63e25367 | -3.63488 | -55.51545 | 2026-10-08 05:42:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8480f842-c61f-328f-9364-52be2b453d03 | -3.09052 | -54.29413 | 2026-10-08 05:42:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6714d10f-1b96-39fa-ab5f-be020b9c359f | -3.28802 | -54.04261 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a463432c-6b2e-307e-b0e6-855316378c74 | -5.29587 | -60.10808 | 2026-10-08 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d17405c6-1c31-3fd9-89d7-cde2e4fb9caa | -1.83574 | -59.95774 | 2026-10-08 05:42:00 | NOAA-20 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ad1ddfcf-3231-3350-bcaa-d0bc43fe04cf | -3.04666 | -57.48513 | 2026-10-08 05:42:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1e8e48a1-ed1a-3187-a657-11997184acc9 | -3.05133 | -54.27026 | 2026-10-08 05:42:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 865ee858-b22f-3a05-894c-28f97750a21e | -2.61448 | -56.48412 | 2026-10-08 05:42:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dcb7ca8e-4b56-30ba-a6c2-108a1070875f | -3.05182 | -54.26713 | 2026-10-08 05:42:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e3a69858-6180-3161-86b9-7f59b2ca5708 | -3.11503 | -53.78716 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ecebe188-632d-3619-abf2-f66f3a1f8c7e | -3.09004 | -54.29731 | 2026-10-08 05:42:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8c542c32-ec70-3ff0-976a-f5a908048b9c | -5.3002 | -60.1043 | 2026-10-08 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 861019ec-6765-3bb5-bf26-46edc1ba7d49 | -4.07101 | -51.0426 | 2026-10-08 05:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 38f05b52-9d2c-30a3-b089-8c89b8445734 | -3.16979 | -50.46074 | 2026-10-08 05:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e9fc04bd-d65f-3349-a88a-c2b29af34838 | -3.58389 | -54.68991 | 2026-10-08 05:42:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ab98aaa1-8f09-3f00-bb54-992c3ce953de | -3.0282 | -54.06836 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1b915ba5-c76d-378e-a113-e4515a61127b | -3.00694 | -54.06513 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| cc03af0e-e2d2-3c3c-b957-7919eea5f95e | -3.29093 | -54.06016 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6329bf94-e1ab-38f0-a0c0-984728debf40 | -3.92428 | -56.06526 | 2026-10-08 05:42:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2998282a-deb2-3421-9e5b-fa811b364855 | -3.62593 | -55.50873 | 2026-10-08 05:42:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 65e5c264-6a31-3048-9011-5f8a4a1c8a75 | -7.75275 | -54.95129 | 2026-10-08 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0ab06554-2a5c-385c-bdbc-662c9374f69f | -3.52528 | -54.65959 | 2026-10-08 05:42:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8438a8e8-1613-3b3d-978c-4e0db494886c | -3.02805 | -54.10525 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 105bf3dd-f432-379a-b18a-b4b5e05dd0f7 | -2.48141 | -56.09055 | 2026-10-08 05:42:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 49ad66dc-842a-33d9-a191-e1f13c526da2 | -3.26023 | -54.02459 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| eb63a497-0343-3b4f-a53e-ee8419918652 | -6.24013 | -52.86329 | 2026-10-08 05:42:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 8a9c3610-d0c0-329b-b743-a78f55b5031e | -7.89774 | -54.71932 | 2026-10-08 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 01948838-cdab-3892-ac7f-71773bfc8695 | -5.33483 | -50.98523 | 2026-10-08 05:42:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 12ed0b4d-3a8c-35bb-9c51-73a019859a9e | -2.84654 | -54.13036 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 256f3850-a883-37c3-a0d6-1d6f91c8d3cc | -3.53821 | -59.49825 | 2026-10-08 05:42:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a4e2c50a-0a3d-3474-960f-48f3f5c7ba9b | -3.59584 | -54.57508 | 2026-10-08 05:42:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1d95218c-5405-372b-a3d5-c1abd5db7fba | -3.30008 | -53.87068 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6deea103-dd5a-3305-a5e8-bef1a6b5bea3 | -2.57709 | -56.16972 | 2026-10-08 05:42:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bd5f3d13-f900-39b5-932f-4402fb058ad9 | -4.9821 | -56.22525 | 2026-10-08 05:42:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 28e9b167-ea5b-3659-8391-1390467e7480 | -3.24934 | -57.86829 | 2026-10-08 05:42:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4a52e613-d7a3-318d-9353-f1324283c603 | -3.28471 | -54.00766 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 97489083-4568-3772-aefe-c05b291114b3 | -3.40232 | -59.59016 | 2026-10-08 05:42:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d860f9a7-6c79-34fe-9348-d3079c6f825f | -3.0512 | -53.95241 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 08767d52-1a18-3604-9b50-58ee65a79df3 | -3.03903 | -54.53136 | 2026-10-08 05:42:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3c7561e5-d153-32af-af9f-4de8608e2693 | -2.78829 | -57.64858 | 2026-10-08 05:42:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8ff95645-dbce-3b5b-8acf-118969bb3b6d | -3.54303 | -54.64622 | 2026-10-08 05:42:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0706bd30-1f33-3629-bcdb-5f5e2fc31e41 | -6.11486 | -55.69704 | 2026-10-08 05:42:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 70f0be66-1f8c-3088-8c01-a19357d9d274 | -3.2852 | -54.07595 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a629d7aa-a155-3f89-8da6-3dfa48173eea | -3.10998 | -54.16454 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| b68bb30d-c621-3df7-8c23-bc0fe94dcaf5 | -6.05824 | -59.94379 | 2026-10-08 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5910b155-7c69-344b-adc0-b4ab0e102749 | -3.32678 | -58.15609 | 2026-10-08 05:42:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c4b86f12-4c35-3f58-aa78-6ef6789ec233 | -5.70373 | -53.4953 | 2026-10-08 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f6f070a2-c9f0-3e50-94b0-d66669e58998 | -3.82513 | -55.4621 | 2026-10-08 05:42:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 18fe24f4-cb76-3247-9e60-afbffe024209 | -3.10735 | -53.76482 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4988c58c-b97b-35f7-ad14-f493226f4767 | -3.01496 | -54.12012 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 19.8 |
| e3e879f4-62b5-3916-ace8-510fb070bd8a | -2.5778 | -56.16504 | 2026-10-08 05:42:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c73137ad-5d59-3054-9b70-6af701ace488 | -2.75916 | -54.10672 | 2026-10-08 05:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1c6fd0ab-d90f-345f-99c2-14a152d2b58a | -2.99926 | -54.04364 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 585ac81f-f57a-3853-b3f1-d08553e7a1f2 | -3.28755 | -54.08331 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cf2a2ee7-d81d-304a-b90e-eee93af11ae2 | -4.60686 | -55.72194 | 2026-10-08 05:42:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| beef68f1-595b-315d-8e74-cb97dfdfea2e | -4.57012 | -54.96048 | 2026-10-08 05:42:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 15b90fd7-53e5-3d4b-b293-eb00dfd07535 | -3.59903 | -61.64025 | 2026-10-08 05:42:00 | NOAA-20 | ANAMÃ | AMAZONAS | Brasil | 1300086 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 059ccad2-5183-3af5-add1-2ecc748f0b06 | -3.28721 | -54.06282 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 343b4a29-ffc4-320e-bb0d-cf04bd39c2e6 | -3.02458 | -53.91034 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2ba84d70-3c4b-3dc9-a7bf-d6b075fe40e4 | -2.48314 | -56.11005 | 2026-10-08 05:42:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 033b31b2-2f55-3be5-81e5-25bcb0c24521 | -3.47992 | -50.08699 | 2026-10-08 05:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |


[Clique aqui para ver as próximas entradas](README178.md)
