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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ab162e8d-e1d3-3c98-a3f4-5f4d725cc0c7 | -11.3987 | -52.9496 | 2025-04-10 00:44:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| cf96c00e-fa5d-31a9-9fc1-c091307e9437 | -11.4006 | -52.958698 | 2025-04-10 00:44:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| eefcbdaa-92cd-3df5-8084-95bdf2816130 | -8.3732 | -41.817402 | 2025-04-10 00:44:00 | METOP-C | CAMPO ALEGRE DO FIDALGO | PIAUÍ | Brasil | 2202117 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| be3adcca-6e28-35c2-a20c-a66f3e8f9c19 | -8.1181 | -43.113701 | 2025-04-10 00:44:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 1196067b-f0ab-36f6-87f4-f0d43baa623e | -11.272 | -52.453499 | 2025-04-10 00:44:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3ede67b6-ca8f-3598-a6dd-d9ae25c52058 | -10.5428 | -44.666302 | 2025-04-10 00:44:00 | METOP-C | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| a6f1aa03-19c7-3f78-adcd-154f7e443845 | -12.0847 | -45.617199 | 2025-04-10 00:44:00 | METOP-C | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 7386242b-072f-38dc-98ba-955f0839aaed | -22.25681 | -53.17905 | 2025-04-10 01:22:00 | TERRA_M-M | BATAYPORÃ | MATO GROSSO DO SUL | Brasil | 5002001 | 50 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| ea84c8d5-6f71-3ddf-96f8-bef78da3c044 | -22.21539 | -49.85792 | 2025-04-10 01:22:00 | TERRA_M-M | VERA CRUZ | SÃO PAULO | Brasil | 3556602 | 35 | 33 | nan | nan | nan | Mata Atlântica | 14.0 |
| 5b9c24b0-c4d2-33a7-90af-1adb3bb36c24 | -22.20958 | -49.85255 | 2025-04-10 01:22:00 | TERRA_M-M | VERA CRUZ | SÃO PAULO | Brasil | 3556602 | 35 | 33 | nan | nan | nan | Mata Atlântica | 17.3 |
| 102ef3bb-58a7-38dd-8261-5330cf5bd9c9 | -21.96848 | -57.58818 | 2025-04-10 01:22:00 | TERRA_M-M | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 2164b4f7-b4a1-360c-af6f-d6b9fce82791 | -20.5865 | -56.05279 | 2025-04-10 01:24:00 | TERRA_M-M | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 3.4 |
| dbaa8345-dc2c-334d-8a96-d8e57e0f1909 | -20.59538 | -56.05136 | 2025-04-10 01:24:00 | TERRA_M-M | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 9ad4363f-4141-3821-9f2b-727310cd7cb6 | -11.39374 | -52.95924 | 2025-04-10 01:24:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 10.1 |
| f48395ae-eb87-30e2-a989-51a25cedfa81 | -11.39428 | -52.94881 | 2025-04-10 01:24:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 4f193012-4b84-3841-bbca-4b398505881f | -11.4052 | -52.95727 | 2025-04-10 01:24:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 32bf4848-ffe0-3472-a053-7247ef90837d | -11.39667 | -52.96443 | 2025-04-10 01:24:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 5e5fef76-0b4c-361d-9435-ef03bb2fa884 | -8.09972 | -43.12798 | 2025-04-10 03:42:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 22.5 |
| dc44d18a-1621-32e6-ab90-38aadbec08c6 | -9.77754 | -39.76823 | 2025-04-10 03:42:00 | NOAA-21 | CURAÇÁ | BAHIA | Brasil | 2909901 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 743e17e1-8bbf-3f40-b683-33bbab44c674 | -6.23218 | -43.37325 | 2025-04-10 03:42:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 02975120-aa70-3351-9d75-a43da0a6548e | -6.67957 | -41.71655 | 2025-04-10 03:42:00 | NOAA-21 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 54e5fad3-abef-3d3b-8602-1eeda7307eb6 | -9.91523 | -37.08645 | 2025-04-10 03:42:00 | NOAA-21 | TRAIPU | ALAGOAS | Brasil | 2709202 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 9dc9eb1b-a59f-3ea1-a25f-1dd16630c76f | -7.38795 | -36.0521 | 2025-04-10 03:42:00 | NOAA-21 | CATURITÉ | PARAÍBA | Brasil | 2504355 | 25 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 851c82dd-b8b1-3b72-b3df-a8a08774543b | -8.11584 | -43.12005 | 2025-04-10 03:42:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 11.9 |
| a33c6b68-de13-314f-a107-5b40196955b6 | -6.6961 | -42.13913 | 2025-04-10 03:42:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 628ed35f-b08f-383f-b594-a0c6a30f7110 | -9.32585 | -40.5901 | 2025-04-10 03:42:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.8 |
| e35c34e0-4aad-3546-850a-06992f90ee41 | -9.38898 | -37.15901 | 2025-04-10 03:42:00 | NOAA-21 | SANTANA DO IPANEMA | ALAGOAS | Brasil | 2708006 | 27 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 3c3627fc-7b2b-39f3-80dc-54c425733687 | -6.01505 | -43.85343 | 2025-04-10 03:42:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e190627a-8a79-3bce-8d42-43608dbe973d | -9.61713 | -37.03048 | 2025-04-10 03:42:00 | NOAA-21 | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 22218a75-813a-3b3e-8fe4-92d030983f7a | -8.37047 | -41.82452 | 2025-04-10 03:42:00 | NOAA-21 | CAMPO ALEGRE DO FIDALGO | PIAUÍ | Brasil | 2202117 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| dedc4d11-1225-3226-ab49-c4f55a06f077 | -8.36975 | -41.8288 | 2025-04-10 03:42:00 | NOAA-21 | CAMPO ALEGRE DO FIDALGO | PIAUÍ | Brasil | 2202117 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| c1d93789-c9a1-34da-8c4e-46c0a108f47b | -9.61598 | -37.03762 | 2025-04-10 03:42:00 | NOAA-21 | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 3.4 |
| fa72ef83-f437-3cbb-b428-e99bf5bea0e2 | -6.2362 | -43.37991 | 2025-04-10 03:42:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| cf7e3ddf-adeb-3964-9ef2-f862c1f4e2f8 | -8.93501 | -44.23329 | 2025-04-10 03:42:00 | NOAA-21 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3ec432d4-0f71-3b48-8235-19cf9faca3aa | -8.10062 | -43.12283 | 2025-04-10 03:42:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 22.5 |
| cdc5a1b2-683d-3b79-ba87-a809353475a9 | -8.52093 | -40.24852 | 2025-04-10 03:42:00 | NOAA-21 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 1b12c345-5af4-3246-a89d-eb0744027c75 | -9.9158 | -37.08286 | 2025-04-10 03:42:00 | NOAA-21 | TRAIPU | ALAGOAS | Brasil | 2709202 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| a49d5b56-6326-3dd3-9d10-db8b280ad63b | -6.23669 | -43.377 | 2025-04-10 03:42:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 997ebc67-91d4-3584-86fd-793273723943 | -7.07303 | -44.38163 | 2025-04-10 03:42:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6ef49c83-1f18-3e6d-a372-e31827d95ec4 | -8.37481 | -41.82532 | 2025-04-10 03:42:00 | NOAA-21 | CAMPO ALEGRE DO FIDALGO | PIAUÍ | Brasil | 2202117 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 267b555e-f097-3f3e-9f56-105959bc64cf | -6.23168 | -43.37616 | 2025-04-10 03:42:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a0e0ba69-c7a9-36dc-8be7-2f49d252fe56 | -6.0156 | -43.85025 | 2025-04-10 03:42:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b5cdedd8-e0f6-3473-af0c-44d76a94071a | -6.69649 | -42.13821 | 2025-04-10 03:42:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 04fd1ad4-e372-3cc0-a437-4d68d2724f38 | -8.93556 | -44.23027 | 2025-04-10 03:42:00 | NOAA-21 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ed34c27d-a749-3d68-90c5-9b404365bf61 | -9.62791 | -36.81682 | 2025-04-10 03:42:00 | NOAA-21 | CRAÍBAS | ALAGOAS | Brasil | 2702355 | 27 | 33 | nan | nan | nan | Caatinga | 1.6 |
| f45127f4-9f2c-37c6-9be2-b0502ee979cc | -8.76705 | -36.21568 | 2025-04-10 03:42:00 | NOAA-21 | CANHOTINHO | PERNAMBUCO | Brasil | 2603702 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 5fcf9549-a23d-3c2c-9c35-3e5bcf31cc04 | -8.37179 | -41.82433 | 2025-04-10 03:42:00 | NOAA-21 | CAMPO ALEGRE DO FIDALGO | PIAUÍ | Brasil | 2202117 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| a74878bc-d592-3b34-8fd2-0d87a533f05a | -8.37103 | -41.82861 | 2025-04-10 03:42:00 | NOAA-21 | CAMPO ALEGRE DO FIDALGO | PIAUÍ | Brasil | 2202117 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 2e22e14c-6969-3668-9bda-f3f2ef793610 | -6.05308 | -39.43748 | 2025-04-10 03:42:00 | NOAA-21 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 172fad08-2f14-35f8-adee-f8f769ddd22d | -16.09385 | -42.28125 | 2025-04-10 03:45:00 | NOAA-21 | SALINAS | MINAS GERAIS | Brasil | 3157005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 9f34b106-2252-3ea2-90ec-b83d090f5d04 | -17.75281 | -42.89576 | 2025-04-10 03:45:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 67529286-5ebe-35c9-bde0-c9025cbcd69c | -15.71334 | -42.26015 | 2025-04-10 03:45:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 01c3540e-52fc-3f9b-afdb-cb96de427b86 | -11.69339 | -44.62463 | 2025-04-10 03:45:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fa93b0aa-9789-33d7-a9e4-d59e762249ca | -15.37644 | -39.2483 | 2025-04-10 03:45:00 | NOAA-21 | SANTA LUZIA | BAHIA | Brasil | 2928059 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| e3c627a9-1ec0-391d-90a5-1f1b685bd7e8 | -16.42244 | -42.51471 | 2025-04-10 03:45:00 | NOAA-21 | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 23eb1d43-2c2c-33df-bc21-64de8ee1530e | -14.86818 | -42.29216 | 2025-04-10 03:45:00 | NOAA-21 | MORTUGABA | BAHIA | Brasil | 2921807 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| e27511c0-8cde-350e-a57d-c2b32512c410 | -16.61434 | -43.33617 | 2025-04-10 03:45:00 | NOAA-21 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| f9b20f79-e558-31df-a548-c59ebbb2bca5 | -12.08386 | -45.62289 | 2025-04-10 03:45:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7657cb2d-5467-3e60-a117-7fdcfa744ce8 | -18.04118 | -39.92674 | 2025-04-10 03:45:00 | NOAA-21 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 066ceb7b-8098-32ca-88ad-0ba12ad5cc9c | -16.6109 | -43.3315 | 2025-04-10 03:45:00 | NOAA-21 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 68f41e38-a492-35e3-920c-9f6006afc0f6 | -12.07861 | -45.62187 | 2025-04-10 03:45:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a9f36bc5-cc8b-3b51-948a-13abdd1501e9 | -15.65666 | -39.19048 | 2025-04-10 03:45:00 | NOAA-21 | CANAVIEIRAS | BAHIA | Brasil | 2906303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 67d5d7ef-4b1b-34d0-81f1-d659550b8102 | -11.79607 | -38.15065 | 2025-04-10 03:45:00 | NOAA-21 | ESPLANADA | BAHIA | Brasil | 2910602 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 3d04be96-608d-303c-a3bf-372079d91fb1 | -12.08973 | -45.62064 | 2025-04-10 03:45:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| acfb1031-ec1b-3668-94f5-e34a3934da57 | -18.3703 | -39.95682 | 2025-04-10 03:45:00 | NOAA-21 | PINHEIROS | ESPÍRITO SANTO | Brasil | 3204104 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| ccc240fc-a634-30a3-8e1a-daedeb244c0b | -16.61162 | -43.32762 | 2025-04-10 03:45:00 | NOAA-21 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cf6f373e-8a80-3456-84cc-87042df044d4 | -16.09293 | -42.2864 | 2025-04-10 03:45:00 | NOAA-21 | SALINAS | MINAS GERAIS | Brasil | 3157005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 5d37f6d0-05ef-377e-b7fa-0f29f6a11941 | -14.88478 | -42.26906 | 2025-04-10 03:45:00 | NOAA-21 | MORTUGABA | BAHIA | Brasil | 2921807 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| e2ec2e9f-6563-3d57-a608-f4859f48f4b4 | -16.35071 | -43.69596 | 2025-04-10 03:45:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f92d631e-a437-3d0b-9fe1-d1b5ed40f4bc | -15.65324 | -39.18988 | 2025-04-10 03:45:00 | NOAA-21 | CANAVIEIRAS | BAHIA | Brasil | 2906303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 758d645a-334d-3f32-b40b-d36c3eae3037 | -13.28826 | -39.86558 | 2025-04-10 03:45:00 | NOAA-21 | SANTA INÊS | BAHIA | Brasil | 2927903 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| c2ff5679-57a0-3e54-8bd5-e1d1113ad21c | -10.62058 | -40.51121 | 2025-04-10 03:45:00 | NOAA-21 | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| d8b9a877-3c97-3a3c-ad60-bd85bd1ce2c2 | -12.43847 | -39.24117 | 2025-04-10 03:45:00 | NOAA-21 | SANTO ESTÊVÃO | BAHIA | Brasil | 2928802 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 46282e5f-0610-3d20-82e9-29f126594dcc | -13.01974 | -44.03422 | 2025-04-10 03:45:00 | NOAA-21 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5bda7df6-59ea-3deb-9285-d58a62371c46 | -10.98245 | -38.27217 | 2025-04-10 03:45:00 | NOAA-21 | ITAPICURU | BAHIA | Brasil | 2916500 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 028fb43d-2674-3a96-bc43-4f21d4276c39 | -12.40535 | -39.24406 | 2025-04-10 03:45:00 | NOAA-21 | SANTO ESTÊVÃO | BAHIA | Brasil | 2928802 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 68eabab3-4f24-3e1a-8fad-7aa25461dd01 | -21.09314 | -48.69461 | 2025-04-10 03:47:00 | NOAA-21 | PIRANGI | SÃO PAULO | Brasil | 3539004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 3fcec571-be0d-3278-b456-b48fc6848d9a | -20.98525 | -43.03596 | 2025-04-10 03:47:00 | NOAA-21 | DIVINÉSIA | MINAS GERAIS | Brasil | 3121902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| c6160503-3100-30c2-8581-7d0b672c336b | -22.20917 | -49.85325 | 2025-04-10 03:47:00 | NOAA-21 | VERA CRUZ | SÃO PAULO | Brasil | 3556602 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| ce2509b7-724c-33e8-aed9-8dd6e3f7a2a3 | -21.04432 | -43.20236 | 2025-04-10 03:47:00 | NOAA-21 | DORES DO TURVO | MINAS GERAIS | Brasil | 3123304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 10bf675e-b77b-307f-a6af-185d966632b5 | -22.21011 | -49.8491 | 2025-04-10 03:47:00 | NOAA-21 | VERA CRUZ | SÃO PAULO | Brasil | 3556602 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 3e18c9b3-157f-3119-a2d1-68a28495e680 | -8.10041 | -43.1217 | 2025-04-10 04:08:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 10.2 |
| 90a539f6-336d-3970-9c9d-e47b2f9412ba | -7.07718 | -44.37844 | 2025-04-10 04:08:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d8db7116-1058-3c1f-acf8-2f3513d07021 | -10.60989 | -44.76651 | 2025-04-10 04:08:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5a2a2c1b-5586-3d1c-bedf-2c290c0bbf81 | -10.53952 | -44.66787 | 2025-04-10 04:08:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e396e9db-8503-361f-b988-7c1dad7673ae | -10.88829 | -46.02555 | 2025-04-10 04:08:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 18fd12e1-4ab0-3dfa-86f0-317c7350393b | -10.78382 | -44.43613 | 2025-04-10 04:08:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e6d1aca7-d830-3b00-b39d-472b30e035dd | -10.49806 | -40.45257 | 2025-04-10 04:08:00 | NPP-375D | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 93de9541-bbf9-3a48-ab0f-22e820a5feca | -9.3872 | -37.15845 | 2025-04-10 04:08:00 | NPP-375D | SANTANA DO IPANEMA | ALAGOAS | Brasil | 2708006 | 27 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 0c9429b6-e95e-3222-ba8b-3bb62c7421be | -8.10321 | -43.12583 | 2025-04-10 04:08:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 10.2 |
| ace163fe-4f71-3638-a2fa-d1c34d0c6d19 | -9.17008 | -43.13639 | 2025-04-10 04:08:00 | NPP-375D | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| d4cbb0cc-de4d-3219-80fe-8ef275cb5fa9 | -6.60044 | -44.18123 | 2025-04-10 04:08:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6842df20-ad54-3c6a-8ef9-12cab26f7f67 | -9.32277 | -40.58636 | 2025-04-10 04:08:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.2 |
| e3f69912-8c83-301e-80b4-0c17745ab4d8 | -7.43563 | -45.42281 | 2025-04-10 04:08:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 44f5b60d-6e31-3fda-8459-d80e0da836c0 | -8.37101 | -41.82358 | 2025-04-10 04:08:00 | NPP-375D | CAMPO ALEGRE DO FIDALGO | PIAUÍ | Brasil | 2202117 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| d2d60d5c-3666-3295-85c9-50d861c3357e | -8.52107 | -40.24639 | 2025-04-10 04:08:00 | NPP-375D | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 9c1cd03f-7266-3060-b178-564487de241e | -6.23278 | -43.37418 | 2025-04-10 04:08:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 20267b9f-3593-3779-9d01-b4dcc60f9690 | -9.77843 | -39.76552 | 2025-04-10 04:08:00 | NPP-375D | CURAÇÁ | BAHIA | Brasil | 2909901 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 5082508b-d7f6-3e85-945d-3a8b0f87e5dc | -10.14509 | -48.07732 | 2025-04-10 04:08:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 463da56a-0442-3fd4-9b42-aeb900ccc8f8 | -8.37047 | -41.82706 | 2025-04-10 04:08:00 | NPP-375D | CAMPO ALEGRE DO FIDALGO | PIAUÍ | Brasil | 2202117 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |


[Clique aqui para ver as próximas entradas](README2.md)
