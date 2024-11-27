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

## Dados Diários - Página 67

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 65cf7c8b-b50e-377c-bdef-8414bb7ebaad | -3.27087 | -50.62655 | 2024-11-27 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a332fb1e-34fb-3cda-b6af-bbbaaf44b27b | -2.99158 | -53.36178 | 2024-11-27 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d7e76b15-e878-3fc2-9181-04b10cc568b2 | -1.75407 | -52.03147 | 2024-11-27 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bf25e98e-7c26-3aaf-937d-102b89d82796 | -1.98859 | -53.289 | 2024-11-27 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cc0a9463-3f35-3a44-b5c4-9da28a1780c2 | -2.93464 | -48.82932 | 2024-11-27 04:42:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9948bc5b-4d66-309c-b301-c9fceaf9ddff | -2.49628 | -52.14899 | 2024-11-27 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7d2b1624-d50d-3797-9540-9b469991be85 | -2.44225 | -50.40839 | 2024-11-27 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4c4435b4-4d0f-354d-ba8b-421ab8d0ae6d | -4.14586 | -43.79813 | 2024-11-27 04:42:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 76f30785-133f-309b-b548-03846aad4cd9 | -0.98656 | -51.72036 | 2024-11-27 04:42:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 3.3 |
| adbb446f-5464-3468-960c-35e29f7d7661 | -1.71334 | -52.49213 | 2024-11-27 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| eb2a8531-fb75-35fd-9aa3-86cf79f69d67 | -2.69569 | -45.66043 | 2024-11-27 04:42:00 | NOAA-20 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3234eaaf-6428-3a54-8054-a9e044cfc87a | -4.12412 | -51.07547 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cfa0cf75-e120-3def-930d-77be11881867 | -3.23181 | -50.31382 | 2024-11-27 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d08a33ef-b5f4-354c-8528-b465e2625b73 | -4.72956 | -47.22434 | 2024-11-27 04:42:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a0bc20b2-3ab9-3c91-ae74-54bb73315206 | -2.53293 | -53.9822 | 2024-11-27 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 684bc6fc-4e19-3661-ab43-8be17e36886c | -3.38887 | -50.09195 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d635733d-7937-38a0-bc90-9bcafd2c7568 | -3.24873 | -53.28419 | 2024-11-27 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3c95abad-4b40-3525-9557-cea134c0da45 | -1.62437 | -53.87091 | 2024-11-27 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6d8a0143-293a-330a-b124-93f740ff896a | -3.25949 | -46.41847 | 2024-11-27 04:42:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8db54b25-9d71-3cd0-86ca-02eea29f7aba | -2.58608 | -54.06083 | 2024-11-27 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f5e495b8-8be8-38ad-8c44-fca311f07793 | -3.658 | -50.23978 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1628195b-aaea-303b-ba7e-bb6bf0bdf1b1 | -2.72658 | -49.33391 | 2024-11-27 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f13ae397-001d-3ed1-9596-e1587e58be74 | -3.2877 | -50.75639 | 2024-11-27 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9bb8dfcf-78f2-3f28-a513-a340a734012a | -3.04617 | -48.50006 | 2024-11-27 04:42:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 024ea270-bbd1-3ce8-a44e-eb3d28378586 | -3.28482 | -51.11876 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 37aac5e6-cea9-3266-b51a-adcf11529e39 | -2.71885 | -48.66501 | 2024-11-27 04:42:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 260bba70-0329-3551-8d68-441144d89769 | -2.61444 | -51.8044 | 2024-11-27 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a59aa2e9-15d9-3b67-b1bb-f0e40da3b187 | -2.52793 | -47.32949 | 2024-11-27 04:42:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 302db600-3059-3b09-a60e-62416faacd25 | -2.46241 | -48.57428 | 2024-11-27 04:42:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 84d51a88-4cb6-3fa7-81e7-9be60242b690 | -4.22293 | -47.21415 | 2024-11-27 04:42:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f5326a58-9586-3055-8e75-df0e08d15e00 | -2.64371 | -51.61286 | 2024-11-27 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8787940c-77a9-322b-9f88-2117a1be5f70 | -4.0653 | -54.67442 | 2024-11-27 04:42:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3c615133-9251-3998-990f-d63ade0b3179 | -3.24589 | -53.4152 | 2024-11-27 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 61741537-53d7-305a-b162-64595b163157 | -2.60074 | -54.21223 | 2024-11-27 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 5ef38383-1e14-3b94-bd6d-266a81c0ea13 | -1.29023 | -51.7286 | 2024-11-27 04:42:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9dc06582-58fd-371c-978b-e68ab1695557 | -1.59138 | -52.26001 | 2024-11-27 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 63c0c57f-e3df-31aa-a6a7-c9231430a2d3 | -3.37133 | -50.1174 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 9cf4196b-f11c-3638-ac1d-7f032c1c912c | -1.64525 | -52.44538 | 2024-11-27 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c3d4d3e1-d531-3822-8ae2-e10918429b39 | -3.94066 | -48.15513 | 2024-11-27 04:42:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9dc738c8-3652-3f48-9b7e-0aa58e8ebf9a | -3.65561 | -49.95051 | 2024-11-27 04:42:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 175dfc0c-1aef-3d1a-9438-40d74e3292b8 | -2.14791 | -50.61635 | 2024-11-27 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2fc478d9-2fc1-3979-b668-585a2be0ceb3 | -2.17237 | -46.61114 | 2024-11-27 04:42:00 | NOAA-20 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 02059782-dd05-3d72-81e1-64ea763ff697 | -2.63043 | -51.76967 | 2024-11-27 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 87ae2efd-0ead-33bb-870f-89a6b31a5194 | -2.6918 | -45.65983 | 2024-11-27 04:42:00 | NOAA-20 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b4dfa81c-57d7-366e-891c-abb3370a5bd6 | -4.70708 | -47.93072 | 2024-11-27 04:42:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ba246563-152f-3215-82a4-e561b9a3cba6 | -2.49589 | -54.53575 | 2024-11-27 04:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 53d89784-2072-3fad-bc36-b2a8df7acba1 | -1.39215 | -51.59359 | 2024-11-27 04:42:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b363d735-2748-357d-93a9-76fefbff23fd | -1.72046 | -52.69911 | 2024-11-27 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f52be371-bd54-3539-a499-d620ac8da95b | -3.50876 | -53.8043 | 2024-11-27 04:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ccb4c619-35dd-30cf-ad3b-7703d0f10d15 | -2.86735 | -46.81116 | 2024-11-27 04:42:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3e37b92c-ea14-36e0-ad39-f69c03146006 | -1.20157 | -51.75719 | 2024-11-27 04:42:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1a98386e-f6aa-306c-bf9b-975edcb4121c | -2.18183 | -53.77371 | 2024-11-27 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 25.0 |
| 34fb7b68-8b86-397c-ad62-0aa9c9736a24 | -2.09184 | -46.55233 | 2024-11-27 04:42:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a2489a24-e33d-3c2d-bd63-4057c3fce1d6 | -3.97608 | -48.07781 | 2024-11-27 04:42:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d82397f1-f879-31a9-b65a-403ccbaac16a | -3.97591 | -48.19466 | 2024-11-27 04:42:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 603648c5-339b-3faa-86fa-d3203e7e6d28 | -1.29032 | -52.46526 | 2024-11-27 04:42:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5a2c9a85-7481-32f4-85ab-da6c25e6472c | -1.3465 | -52.54625 | 2024-11-27 04:42:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d5a06918-49c9-364e-97c1-a37e9a4a4a1d | -3.10322 | -53.27235 | 2024-11-27 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d3fb3924-07a8-3e85-a702-15c406486578 | -2.03627 | -51.19682 | 2024-11-27 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a896d444-6b5f-3fa4-80ca-39bdb4a86b56 | -3.75195 | -52.65452 | 2024-11-27 04:42:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 58c7e012-9cd5-3871-b83b-ed49a88d7919 | -1.26928 | -52.16764 | 2024-11-27 04:42:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 86ead5c3-ae43-3441-b90c-c8046d8d1637 | -4.23108 | -48.67493 | 2024-11-27 04:42:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 92c2559b-0601-3cb0-a169-9f439703220c | 0.64907 | -50.86155 | 2024-11-27 04:42:00 | NOAA-20 | ITAUBAL | AMAPÁ | Brasil | 1600253 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9aaacafc-3b95-32e3-b6bb-980013353a90 | -5.19621 | -48.18433 | 2024-11-27 04:42:00 | NOAA-20 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9685413d-83ed-311c-bb35-c160277523ad | -2.8166 | -48.6022 | 2024-11-27 04:42:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 59ecb20f-c4e8-37a1-b863-5183ab23fb36 | -2.97152 | -51.57893 | 2024-11-27 04:42:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 48dde790-6343-3aa1-8fa4-27e9209a8f9a | -3.78882 | -50.27081 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 75aa3004-7536-30dc-9aaf-1724c7d7adba | -2.78756 | -53.20888 | 2024-11-27 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 92fe4a36-d04b-353b-ab68-ae5d2dc1b94b | -3.95102 | -46.91232 | 2024-11-27 04:42:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0d313781-0def-3b20-b11e-688d9ea4528c | -3.97606 | -49.94397 | 2024-11-27 04:42:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 97cb89f9-4812-329c-8c4a-8026f0d0cd66 | -3.90987 | -50.60369 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 23106cf1-08fe-354f-8c79-ccc1629090b7 | -1.2628 | -51.59248 | 2024-11-27 04:42:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b70bc1ce-d724-3238-befa-216e5f46e679 | -3.75624 | -49.93769 | 2024-11-27 04:42:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6107b303-8233-3929-91c5-9594fa852161 | -2.22777 | -53.6884 | 2024-11-27 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a500cd3e-6b7c-304b-96a0-7052e5555f29 | -4.48248 | -48.11773 | 2024-11-27 04:42:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 91f70745-630c-3a1e-903e-9b97bc92b13d | -4.29486 | -48.19139 | 2024-11-27 04:42:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dfe864dd-abaa-39b9-a8c0-0d08a777999a | -2.81184 | -46.82985 | 2024-11-27 04:42:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| ee8da0a1-ebca-3177-9ec2-ed11643ca9f8 | -3.81919 | -50.7906 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c5fdaf8a-35f8-312f-ab2a-bb1a1580546a | -3.51063 | -50.46345 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a74e147d-1640-310c-a01e-37a9f7d21dcf | -4.29884 | -48.23483 | 2024-11-27 04:42:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 318bcaa7-bb6c-3674-8e2e-cba9e067d3d4 | -3.94366 | -46.91125 | 2024-11-27 04:42:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2d7915e5-c102-3cf5-bc4e-38fbc71065a3 | -4.19716 | -50.69786 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 80227973-1af8-3d55-947c-0ac827b9a124 | -4.71772 | -46.57425 | 2024-11-27 04:42:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 3ab74ce7-c0be-35b6-a96e-19774b955bcf | -3.11384 | -51.25666 | 2024-11-27 04:42:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 30ec30f8-706b-3b57-afb8-1e88a71e9e66 | -3.94781 | -46.69421 | 2024-11-27 04:42:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 80866488-fc10-3ec3-8814-6acf68e7d16b | -3.27424 | -48.56464 | 2024-11-27 04:42:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7dc60dae-77d2-3205-b096-34b08f3e8c0c | -1.6554 | -55.23924 | 2024-11-27 04:42:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f49f8848-2b61-3c5e-8c9b-f0138350c09e | -2.81942 | -48.60632 | 2024-11-27 04:42:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9aa83f63-e674-3157-8368-7bcfbd25db48 | -1.30617 | -51.73868 | 2024-11-27 04:42:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 64745f06-62ff-3a38-b793-2d2b7bcdaf7e | -1.51958 | -52.05018 | 2024-11-27 04:42:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4002bde4-7ab9-397f-9dbb-50235d5d488e | -3.26864 | -50.61914 | 2024-11-27 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d4b811ae-43e2-3f2e-aa2c-70c4da9b1db1 | -3.97438 | -46.73288 | 2024-11-27 04:42:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| ec0954cb-318c-3e6b-b8e6-5d64891e6bd3 | -3.58082 | -41.95826 | 2024-11-27 04:42:00 | NOAA-20 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 50de1c8d-2213-34f0-8de1-6274c39e40bb | -2.82407 | -46.82309 | 2024-11-27 04:42:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 99bab974-9e04-3213-a234-aacec2220db8 | -1.62367 | -53.87539 | 2024-11-27 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 98abf462-d691-30cb-bcaf-2ff55ca1c359 | -4.21519 | -48.66492 | 2024-11-27 04:42:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 22.5 |
| f8cdab2f-d92d-3f3c-a841-d9f6b2d1818d | -1.29365 | -51.72914 | 2024-11-27 04:42:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 09ab4541-f791-3b71-a394-e9a069802cfe | -1.31359 | -51.73605 | 2024-11-27 04:42:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cb19a626-82a7-324f-a850-eda5c8a295a1 | -4.20947 | -50.90145 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 38e94db9-e9b3-3629-b073-cb9d20a7e2c4 | -5.90731 | -43.41187 | 2024-11-27 04:42:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README68.md)
