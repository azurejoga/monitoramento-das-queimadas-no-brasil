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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 440bc8c6-21f7-3a16-9fea-c425dc0b1422 | -3.02931 | -54.19062 | 2024-12-10 04:53:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 89a83a9a-ec34-3ce2-a62a-f23410def680 | -3.77622 | -51.50019 | 2024-12-10 04:53:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| abe7f98a-15f3-3b41-ab6c-b03c9c9cda00 | -2.75366 | -54.15585 | 2024-12-10 04:53:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ce697d17-1a1c-3bb4-8820-47d05dee5138 | -13.94137 | -44.35698 | 2024-12-10 04:53:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 38cf8e68-1f56-3905-a2e2-12f0ed5927cd | -3.23239 | -42.4276 | 2024-12-10 04:53:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e9936fd5-1b38-3708-97d9-f03d3b7b8277 | -3.05559 | -54.24434 | 2024-12-10 04:53:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 05e4dfc1-9aeb-39b5-929c-8d180aad77a6 | -3.47499 | -52.7982 | 2024-12-10 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dd972d35-c23a-3d68-bce6-cae747b4dc8d | -1.64618 | -54.62051 | 2024-12-10 04:53:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4bca1007-b955-3433-a6ba-8f49a1f15290 | -3.11576 | -54.02067 | 2024-12-10 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 679f3333-125b-3200-a3ff-1dddfbc053ec | -12.37351 | -54.1603 | 2024-12-10 04:53:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 49d41e66-b208-3e9e-9ca7-46ec39aad44c | -11.20634 | -53.81766 | 2024-12-10 04:53:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 34ace8ec-ce21-367b-8c7d-8c2f1060bf75 | -12.1112 | -44.75949 | 2024-12-10 04:53:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e3da3077-d74c-3417-a98f-19c351774db4 | -3.6146 | -49.853 | 2024-12-10 04:53:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| adea0f8c-cf3b-33ef-b23e-ad67c45af94f | -3.79191 | -54.64947 | 2024-12-10 04:53:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cb0e576a-aafb-326e-a50c-4291b7dc21c6 | -2.35805 | -53.79501 | 2024-12-10 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b5e57e8f-8664-3722-a2c6-fb30aac7f992 | -1.2272 | -48.84523 | 2024-12-10 04:53:00 | NOAA-21 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1bb42c75-b8f8-37e8-97de-c88853042be0 | -2.79571 | -53.24671 | 2024-12-10 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2931d172-3d6c-3069-bc25-ef381c02cf9f | -3.00068 | -53.04778 | 2024-12-10 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| ca803174-395d-3596-813c-6d1393455344 | -3.08368 | -53.36056 | 2024-12-10 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a59b4ea7-961b-3401-bbb5-c49bc4e8d54a | -3.08641 | -54.07306 | 2024-12-10 04:53:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e4ce76f9-0941-3a7e-b8ec-ae79ed0d5423 | -2.36439 | -53.90953 | 2024-12-10 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3fd8b9db-ce1c-362a-9be1-5a39305dc1d0 | -3.37421 | -51.19877 | 2024-12-10 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 47411b3e-a08c-3723-b979-9bb0da966968 | -10.02944 | -53.75383 | 2024-12-10 04:53:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1234ac01-07f3-36c2-8f84-d28e1f4ae484 | -6.83239 | -44.38641 | 2024-12-10 04:53:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| fd886516-7d66-3a3c-9a38-755872b2522e | -2.98576 | -54.06538 | 2024-12-10 04:53:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f5fc57e2-6e15-3a80-a07d-801718253673 | -2.47745 | -53.6338 | 2024-12-10 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3289b4e8-4011-31de-af4a-f907fcbedd6f | -2.55791 | -53.41768 | 2024-12-10 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 94f5ef16-c9ff-372f-951d-4ea5da4aa97d | -12.85667 | -51.93816 | 2024-12-10 04:53:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 7f23ec11-74fa-37f6-b1c3-d40e34654f28 | -2.30411 | -54.00366 | 2024-12-10 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f605fe07-7029-38fd-b59e-a0e1f770b5e5 | -1.72266 | -52.78071 | 2024-12-10 04:53:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2b86c8d8-619d-397f-a4fd-a06fae887abc | -12.24274 | -52.45101 | 2024-12-10 04:53:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ff52cb6b-6118-323c-9909-0aabf7b3fd90 | -12.36856 | -54.17031 | 2024-12-10 04:53:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 643f571f-d2f9-380c-b8e2-1c8d9260b7fe | -4.04272 | -50.80777 | 2024-12-10 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 04033bae-fe2b-3848-8f69-524821b33f95 | -2.99734 | -53.04726 | 2024-12-10 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| c2e5a6bf-0a1c-3ff0-a467-42eacd78cf70 | -6.91845 | -43.50674 | 2024-12-10 04:53:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 1dd249ec-c9b3-315d-b424-40e00b0a70f0 | -3.81475 | -54.61777 | 2024-12-10 04:53:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9cf17404-4225-38f1-9e3b-67adafb90f25 | -2.95303 | -53.11219 | 2024-12-10 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| f38e4416-a995-30dd-a3e2-e0ac2952b860 | -3.9301 | -53.58057 | 2024-12-10 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 29d17970-8bea-373b-a90b-1eff7172b3fc | -9.83041 | -54.37095 | 2024-12-10 04:53:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1ed5fb5a-063a-31c5-b458-2ac7742e8633 | -2.45012 | -57.927 | 2024-12-10 04:53:00 | NOAA-21 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7a3b3425-3408-3c72-bb1f-0f376300ec86 | -3.11157 | -54.06927 | 2024-12-10 04:53:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cae85541-0125-349d-9b8a-1ac21bc8788b | -3.51898 | -52.19152 | 2024-12-10 04:53:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 8f3bc9df-b2c7-3707-8f62-5be59e688c7f | -12.16175 | -55.17745 | 2024-12-10 04:53:00 | NOAA-21 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f851f4ec-75b7-30ae-bba3-541d63651de8 | -3.53228 | -54.68873 | 2024-12-10 04:53:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e174aa88-333f-398a-beb8-6e1c00f9d6f4 | -12.85284 | -43.82049 | 2024-12-10 04:53:00 | NOAA-21 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0b1ee0d1-6be0-3a4b-92a9-883151142f85 | -2.83123 | -53.06455 | 2024-12-10 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 67a0875d-6455-3e17-9786-13994176d50d | -3.63024 | -52.67735 | 2024-12-10 04:53:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1add46b3-39a2-3250-ac62-8b86653d33af | -3.82089 | -51.25698 | 2024-12-10 04:53:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c9f0f8a5-5f26-3db9-adde-33faa0b52ad3 | -3.52622 | -54.59298 | 2024-12-10 04:53:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c425b7d4-ba41-34bc-8215-142c3129e3c2 | -2.32382 | -53.89974 | 2024-12-10 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a365263b-9b6c-3fc7-9c3b-284184f7ac76 | -3.4685 | -52.83978 | 2024-12-10 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bc228427-ba34-339e-b288-d3119e28e137 | -2.8041 | -54.03731 | 2024-12-10 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| eedccbe6-3741-33ed-b2c4-4a7460263240 | -3.08451 | -51.3999 | 2024-12-10 04:53:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 07390695-0cb5-3c53-964d-21733531a240 | -2.35464 | -53.79448 | 2024-12-10 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 40a51e88-30ec-30aa-8730-190d326b3791 | -4.55073 | -48.01371 | 2024-12-10 04:53:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3a12796e-caf5-321a-b067-799c0c210ada | -2.29159 | -53.79252 | 2024-12-10 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 63db5cb5-69d8-32e5-89be-1d2893412fe1 | -11.21503 | -54.15266 | 2024-12-10 04:53:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 03366e5d-61d9-3ce7-b2c6-27c780c601cf | -6.73255 | -46.29259 | 2024-12-10 04:53:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cdb3cc7d-e49b-3887-b712-fb7625572841 | -11.31993 | -54.04752 | 2024-12-10 04:53:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5f9c6eda-c5c0-3664-ac2a-8c60ff8ce1f8 | -2.55285 | -53.42791 | 2024-12-10 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 40afd3c5-3077-32c0-9df7-7e694c71056d | -3.61192 | -50.56845 | 2024-12-10 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bc3a881e-8950-3a12-9468-dc3b3b694a00 | -3.5259 | -53.5352 | 2024-12-10 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| be9f4dbc-26f4-3f46-b2d1-2f0903a9b8bd | -3.66504 | -49.9538 | 2024-12-10 04:53:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a4338f95-ce81-32f3-852f-b9b93f0cea3c | -2.43794 | -53.95533 | 2024-12-10 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a52f9d25-ade6-3c87-abdb-a8dc39a0f74c | -12.85723 | -51.93422 | 2024-12-10 04:53:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 5246420d-f172-383d-9779-4ac05976394f | -2.55005 | -53.42381 | 2024-12-10 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3fb2f32b-e86f-338d-9239-1b7e10aa6cf0 | -2.48056 | -49.03292 | 2024-12-10 04:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 62b7660b-7693-3448-9852-cd6b2438dab0 | -1.64237 | -45.90353 | 2024-12-10 04:53:00 | NOAA-21 | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a91a8b09-3fff-3749-8bba-1acd1762f3bf | -6.73316 | -46.28814 | 2024-12-10 04:53:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 681339c8-6407-3736-b69e-2084b4b46e01 | -3.18023 | -51.41819 | 2024-12-10 04:53:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2e2ce078-c13d-3cfa-aac2-049e3332e7d7 | -6.92086 | -43.51919 | 2024-12-10 04:53:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| f900016a-eab3-3efd-9dae-72a4d4a365a2 | -2.81389 | -52.97955 | 2024-12-10 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 1e391b2e-20a9-32c8-8afd-1eb42861c2d6 | -10.03275 | -53.75435 | 2024-12-10 04:53:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f183977c-db3f-3a48-a8c5-4f3aabacb6a7 | -4.39502 | -47.77127 | 2024-12-10 04:53:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2a2d62fb-97a9-3f7c-933d-7e3c599204fd | -3.85368 | -40.44663 | 2024-12-10 04:53:00 | NOAA-21 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 4.6 |
| ada6dc49-5c9d-3aa9-a173-3ae7f3ae11b9 | -2.31501 | -54.00153 | 2024-12-10 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| abca3706-7f8f-37d2-a928-9caf533682f0 | -11.34968 | -54.29282 | 2024-12-10 04:53:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 186e66a2-004b-37a7-83ff-e7e473c704cc | -2.7559 | -54.16398 | 2024-12-10 04:53:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c1e4e810-5e58-39a4-bcd2-7615dd633375 | -3.46241 | -52.83528 | 2024-12-10 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d24c03e0-cf42-33f7-8530-3e621dd1c8b1 | -12.85825 | -51.93944 | 2024-12-10 04:53:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| b5c93ba8-185f-35cb-8db0-3144168c2c9d | -4.13142 | -50.00278 | 2024-12-10 04:53:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c6c9f6e6-3e0f-3c36-918f-eb79a87e1461 | -2.45315 | -53.65599 | 2024-12-10 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ccc946af-d268-3039-9a35-15d675698fed | -2.7565 | -54.16018 | 2024-12-10 04:53:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5240fe25-71bc-3fc7-a5bc-38278410a4ea | -4.5218 | -47.9692 | 2024-12-10 04:53:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9c412cd0-677c-35f6-9885-5f5b0ce0e606 | -6.91097 | -43.51054 | 2024-12-10 04:53:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5adc4438-717a-336b-b61d-5f0d9a368b97 | -3.09004 | -53.21678 | 2024-12-10 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7c35a215-f708-3a62-9162-51a2e7eef251 | -4.12522 | -50.42857 | 2024-12-10 04:53:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 95369f3e-ef4e-3892-b1d7-88a71a5626ab | -2.79106 | -52.86521 | 2024-12-10 04:53:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 03ee697d-a962-3fbb-9c02-c00ba9e27e92 | -4.03315 | -50.80259 | 2024-12-10 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 79ba828b-471f-373b-af7d-a04d08b904d9 | -2.6218 | -48.05569 | 2024-12-10 04:53:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 390d0524-4c92-36dd-9225-912dc4915882 | -3.77935 | -50.05578 | 2024-12-10 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b58887c9-17c7-38d5-9775-9f1568e294f5 | -2.81067 | -53.06498 | 2024-12-10 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f2c084d8-ee92-39d4-a249-7df1dd24b040 | -3.17883 | -55.01588 | 2024-12-10 04:53:00 | NOAA-21 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 60e174cd-648d-3522-a17a-988bd42fd3bc | -2.80185 | -53.25126 | 2024-12-10 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 32da5fd8-3af2-3842-8121-1e5a93405036 | -4.02063 | -49.94751 | 2024-12-10 04:53:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4267a0e6-134c-3f65-9c6a-08f825666cfc | -7.17385 | -44.99118 | 2024-12-10 04:53:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fc499c8d-363c-3f01-a451-40e0e748c0c7 | -3.92674 | -53.58005 | 2024-12-10 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| de384375-05a1-39ac-b27b-534a66552f84 | -4.39182 | -47.76577 | 2024-12-10 04:53:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 8f0789f3-5619-368b-93ba-cb257eec4cb0 | -10.36829 | -52.00499 | 2024-12-10 04:53:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 232b3300-e8c5-3033-a2f7-d7994e54079f | -2.8112 | -53.03991 | 2024-12-10 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |


[Clique aqui para ver as próximas entradas](README23.md)
