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

## Dados Diários - Página 59

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cfa9080c-6261-36f2-b68a-f50cedb83fd7 | -4.69927 | -45.8508 | 2024-11-23 05:12:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 330d21ca-9e36-3539-9fdc-6d2f765daa29 | -4.26658 | -46.29053 | 2024-11-23 05:12:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0b505328-5e89-372e-a2de-15b66559f28f | -3.2237 | -54.23683 | 2024-11-23 05:12:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2fe613ae-4d0e-34c5-9789-cbf8d2319f76 | -6.33298 | -46.0352 | 2024-11-23 05:12:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 217591d5-01af-346c-8325-d89711543d1e | -3.21575 | -51.41879 | 2024-11-23 05:12:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| fda4f1f5-bed9-399a-9597-4b705f1d9afd | -3.08988 | -53.25936 | 2024-11-23 05:12:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 689cc7e8-d022-334d-b27a-05859d331b36 | -3.12006 | -53.11047 | 2024-11-23 05:12:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 24b1b2ae-a658-348c-9bcc-6057601daf61 | -3.1817 | -54.3188 | 2024-11-23 05:12:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c763b58b-ab17-3843-9a1b-4f9ffc25f502 | -3.79905 | -51.75863 | 2024-11-23 05:12:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 01f13c37-be2d-39e4-a1c4-ebc4f6863eda | -4.6099 | -46.49413 | 2024-11-23 05:12:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 21.3 |
| fb6e2ab0-71dd-3917-a2b4-0b6bdd9156b7 | -3.20602 | -54.25453 | 2024-11-23 05:12:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5ef5652f-2809-3619-b880-ad8ce7f330c0 | -3.27779 | -53.83877 | 2024-11-23 05:12:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cc713bc3-37fa-35c9-ab2f-9c7fe38958c9 | -2.95215 | -53.71702 | 2024-11-23 05:12:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| cacbcc8f-57fa-3edc-ba4b-ccf1094c38ad | -3.66549 | -54.04799 | 2024-11-23 05:12:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 95173d83-ba9c-3497-b3e1-736377ee43c2 | -4.42284 | -44.11205 | 2024-11-23 05:12:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 9608aaa4-a1e5-3e96-aede-2ab82d7472c7 | -6.14302 | -46.68596 | 2024-11-23 05:12:00 | NOAA-21 | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| c88d7363-e2e9-36ad-ada5-b5c5be5a5e3b | -4.72945 | -45.49214 | 2024-11-23 05:12:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| aac4a405-6973-3536-9072-0ec9ce61f33b | -3.50479 | -53.8106 | 2024-11-23 05:12:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0e88feff-d15b-3fb6-923c-78fd60e1ab73 | -3.1875 | -54.32768 | 2024-11-23 05:12:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 76e2afdc-83da-3891-8451-03f492ddf566 | -2.85512 | -53.96852 | 2024-11-23 05:12:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 2556b11b-a676-3e2d-8478-a6b27c6b1ea5 | -3.7985 | -51.76226 | 2024-11-23 05:12:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 569c9dbf-1906-380c-8fac-d17a1a8a98a9 | -4.38933 | -47.77541 | 2024-11-23 05:12:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 36c7f9d5-2fc3-3876-a744-37d1e784586f | -2.81052 | -54.02427 | 2024-11-23 05:12:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 848589a4-10df-385c-b5c4-dec58cf19525 | -3.26601 | -53.81993 | 2024-11-23 05:12:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0dda3a63-045b-3ff0-b748-3772e313a788 | -3.52677 | -52.90652 | 2024-11-23 05:12:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 897c7887-eb8f-36be-b80d-1730f00e0bb4 | -4.11952 | -54.34572 | 2024-11-23 05:12:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ca2d085d-a53e-3bba-af21-bd2570b03d54 | -2.99272 | -53.35685 | 2024-11-23 05:12:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 97b5df3d-c51a-3b57-a727-fe4010cc1778 | -2.78963 | -54.15857 | 2024-11-23 05:12:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| fb347676-4c04-3645-9c20-872d929d5430 | -2.96294 | -53.71868 | 2024-11-23 05:12:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9e86f2fa-fcab-330f-9bae-cb31a8d9d726 | -3.70263 | -51.78933 | 2024-11-23 05:12:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 68061761-7701-34a8-83ae-d0a8814c49ba | -3.10572 | -53.98854 | 2024-11-23 05:12:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7d935004-53f1-3318-8d5c-2880d3c46907 | -3.50789 | -53.80417 | 2024-11-23 05:12:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6a4980fa-1e9d-3a4e-87ad-d0877875b442 | -3.94841 | -47.96545 | 2024-11-23 05:12:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2d6689bb-bcbe-381a-9786-af6d5e0c6240 | -3.95226 | -47.96534 | 2024-11-23 05:12:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fcc99472-66b0-3b6b-aefd-1517268f05c7 | -3.25007 | -54.25295 | 2024-11-23 05:12:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a783864f-ff04-3ad5-9455-ab5a381b6864 | -3.24309 | -54.22775 | 2024-11-23 05:12:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 048a8090-bdde-3583-91e1-6997821d4a9c | -5.11437 | -45.83479 | 2024-11-23 05:12:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 6c776d49-0bfe-3b34-a6e8-ad987c852d2f | -3.22277 | -53.9342 | 2024-11-23 05:12:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 250f75ed-7a47-3bbe-98d1-c96c8c6eab9b | -4.44586 | -48.1942 | 2024-11-23 05:12:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| b241afc2-6270-3e59-82fe-76a5ecd8e007 | -3.23719 | -54.24292 | 2024-11-23 05:12:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bef6346d-f48d-330d-9366-912641caa242 | -4.41518 | -44.11698 | 2024-11-23 05:12:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 55d99998-8c33-3757-8ec9-3236c173f85b | -2.82051 | -54.02985 | 2024-11-23 05:12:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| e69f006f-fafd-34f4-b4b4-a1e87fcd589f | -3.35568 | -53.40543 | 2024-11-23 05:12:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ad67f21f-d4ac-3891-b56e-ba3f27038eea | -2.83704 | -54.06373 | 2024-11-23 05:12:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 07ad1a08-81d1-3506-bf75-a49f987244e5 | -3.25245 | -54.23731 | 2024-11-23 05:12:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 5afbe9db-5cf9-3a50-a916-b320f54886b7 | -3.09864 | -54.29165 | 2024-11-23 05:12:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 74f4d9d5-b235-3d9e-bf2e-78c29d0dd104 | -3.34104 | -54.62604 | 2024-11-23 05:12:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b5917497-5d20-30cc-a9fb-892aef36f280 | -4.02434 | -49.91945 | 2024-11-23 05:12:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 70d78fa4-d53a-393a-973e-8cd514a43451 | -4.16087 | -54.57702 | 2024-11-23 05:12:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f63fac4d-10b6-34c0-bc76-81dd891f576a | -3.11939 | -53.11492 | 2024-11-23 05:12:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 84d8cfb4-713d-3af4-b315-76097ddbd364 | -2.82457 | -54.09832 | 2024-11-23 05:12:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c4e62342-1eee-38f9-8ec5-ada1bc8633b3 | -3.50853 | -53.80005 | 2024-11-23 05:12:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fb9cbd0a-a381-385c-9730-d0d92f0b6759 | -3.95178 | -47.96877 | 2024-11-23 05:12:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8c65f534-2b0d-333d-892d-b91541b96ca7 | -4.47792 | -48.11691 | 2024-11-23 05:12:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| db11484d-b90e-31d7-a08a-544977b1a436 | -4.44493 | -48.19791 | 2024-11-23 05:12:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| ee70ab89-09a3-357c-8564-ba13cc86c3fe | -4.25372 | -48.69682 | 2024-11-23 05:12:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 20.5 |
| 3dcf790a-19d0-38c2-8e45-7fcf2c2f7d7b | -3.51025 | -53.79872 | 2024-11-23 05:12:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f91d0925-d7db-370e-8104-e5c5fb625f0b | -3.14255 | -53.9151 | 2024-11-23 05:12:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ddeb0540-a06a-36c5-901b-d0624112c81c | -4.26597 | -46.29478 | 2024-11-23 05:12:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| abcb8872-ef8e-3ccb-9bdf-83cff4123389 | -3.28644 | -53.84356 | 2024-11-23 05:12:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e8d3ae2f-f344-3517-bf5a-a85afbb0d580 | -3.24304 | -54.25182 | 2024-11-23 05:12:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 20d5d5a7-9a99-3b1e-83f9-479965ef952a | -2.81654 | -54.00887 | 2024-11-23 05:12:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2b638cc6-c368-3590-81e8-912224811e6b | -4.36993 | -48.56576 | 2024-11-23 05:12:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3a008323-8ec6-3d7e-9ca1-1ebaf2bdd367 | -3.68576 | -50.11645 | 2024-11-23 05:12:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| c824523e-263b-3b7f-9525-c2508e4b02bd | -4.60925 | -46.49877 | 2024-11-23 05:12:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 21.3 |
| 670ecbdb-136c-3393-a89a-41aa8538ff9c | -3.58187 | -54.52034 | 2024-11-23 05:12:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7bac868c-4423-352c-95a9-59999274fb79 | -2.73948 | -54.38919 | 2024-11-23 05:12:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 72109b99-c3e0-3737-80ea-03c37ef5d70a | -3.81416 | -51.99124 | 2024-11-23 05:12:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 067632b0-0374-3e70-b844-6cb5872ca104 | -3.23367 | -54.24237 | 2024-11-23 05:12:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a14fadde-69d9-3c8d-8854-31080f81ab84 | -5.20534 | -46.81706 | 2024-11-23 05:12:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 7625e536-976c-3120-a437-9907f0c8a68f | -3.24601 | -54.23225 | 2024-11-23 05:12:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| c8c06fbe-21f9-37be-bee3-f5cdb5af684a | -3.25013 | -54.22883 | 2024-11-23 05:12:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 89a73ff8-4b16-3895-a572-c0195a03e426 | -4.90983 | -47.85587 | 2024-11-23 05:12:00 | NOAA-21 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 58a53173-5e91-3648-87e0-2a4a72d11e97 | -3.191 | -54.32824 | 2024-11-23 05:12:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8160b78e-dc19-319b-8d2a-53cbf394ecbc | -4.44635 | -48.1909 | 2024-11-23 05:12:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 1df99052-db73-361f-9ba4-dc8ede24e332 | -3.21901 | -54.24408 | 2024-11-23 05:12:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0335a31d-01a0-3f63-97a1-84dd30982ea4 | -5.16256 | -47.04197 | 2024-11-23 05:12:00 | NOAA-21 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e07336fd-b5ba-3a3a-92b9-b2b6c18e9122 | -4.56245 | -48.02089 | 2024-11-23 05:12:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 48fa2e37-0c22-33b4-b938-34dbc9ced4b7 | -3.09946 | -53.17111 | 2024-11-23 05:12:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6a87461c-e90d-3ca9-a0d4-65a1b4d524a8 | -3.10804 | -53.99708 | 2024-11-23 05:12:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| be39d53b-bc7e-3d87-b77d-7ff45f07a7a4 | -3.11098 | -54.00164 | 2024-11-23 05:12:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6075f7a6-e646-3fda-b2a9-d4ad1d15da9e | -2.81989 | -54.03382 | 2024-11-23 05:12:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 451c5bd0-1ef1-3446-b58c-9b62eac96a63 | -3.83618 | -52.2524 | 2024-11-23 05:12:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f3c4482d-aa18-356a-a53d-aa2f0df37bb9 | -3.31812 | -53.28559 | 2024-11-23 05:12:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 55069065-8aae-3db0-a0c5-c8dadd1768cc | -2.85086 | -53.99655 | 2024-11-23 05:12:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 39da5cea-71e2-394a-adea-c05c1953f308 | -4.02864 | -48.86719 | 2024-11-23 05:12:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6d11dba8-fbfb-35c7-ac26-25c6d1703b6d | -3.3343 | -53.32809 | 2024-11-23 05:12:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 70681d1e-3f07-3a52-a228-e27df92f5021 | -3.24774 | -54.24457 | 2024-11-23 05:12:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 1ac894e7-05dd-3a32-8be2-65c945157976 | -2.8449 | -54.01196 | 2024-11-23 05:12:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| db733cfd-3771-36fe-8f14-5ba770a9ebbe | -4.74829 | -49.09842 | 2024-11-23 05:12:00 | NOAA-21 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| bdf3cee5-9aaa-3093-b534-31a6d107d61a | -2.85026 | -54.00053 | 2024-11-23 05:12:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3cddae69-a8a3-3536-8659-f85d54bbea91 | -3.23542 | -54.2546 | 2024-11-23 05:12:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fce46c56-5d54-3402-9564-00054759dfb7 | -3.17881 | -54.31432 | 2024-11-23 05:12:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f355cd4a-d663-374b-bcba-54c426a7b0dd | -5.37178 | -50.85224 | 2024-11-23 05:12:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4e89b5a1-7f9a-36a4-bd6d-f39884c1f92d | -3.50664 | -53.79821 | 2024-11-23 05:12:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a80d9ad0-1f99-394e-a783-a390ab32b16d | -3.83143 | -52.25699 | 2024-11-23 05:12:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fbecf6b6-d328-352f-900e-c32ada84acf7 | -4.17574 | -53.72719 | 2024-11-23 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 782b329c-7b69-3c8a-a384-e62708b6d2cd | -3.23601 | -54.2507 | 2024-11-23 05:12:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 90252192-8e51-371b-8931-1d4ed65735b8 | -3.8526 | -51.14683 | 2024-11-23 05:12:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 17bfda33-152a-3e9c-a7ba-ba219da47c28 | -3.70208 | -51.79292 | 2024-11-23 05:12:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |


[Clique aqui para ver as próximas entradas](README60.md)
