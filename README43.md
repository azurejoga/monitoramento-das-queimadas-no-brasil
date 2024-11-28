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
| 12f1ab72-87ae-3258-8232-a27163180969 | -8.4774 | -47.81526 | 2024-11-28 04:23:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 944c26d2-2134-31e0-9d71-eea9ad6348f3 | -2.70981 | -46.11651 | 2024-11-28 04:23:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 17d9f564-3db5-3afd-82b3-338aab30a0de | -1.16684 | -51.93752 | 2024-11-28 04:23:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f7bb2e8d-ac47-3e9e-b63e-2a57112607b3 | -1.69732 | -52.62909 | 2024-11-28 04:23:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b45e0997-5032-3f5c-b38a-7278a9791fcb | -2.51766 | -47.40587 | 2024-11-28 04:23:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ec2eeccc-d98f-3ab5-8a58-e85a6ba9df96 | -1.87212 | -50.59894 | 2024-11-28 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 33a605a3-a34d-3b6b-bad3-d274806d6935 | -2.69942 | -46.18259 | 2024-11-28 04:23:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4e99072f-62b6-3ff6-933a-5dc303aa62e9 | -1.71564 | -52.48082 | 2024-11-28 04:23:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 23c1f40d-6027-3e58-b8b6-3472442528c6 | -6.23913 | -46.18389 | 2024-11-28 04:23:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0680d66a-40b3-3678-b758-0cfe1021e75b | -5.60532 | -46.49808 | 2024-11-28 04:23:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c9aa1f80-dc29-369e-8228-177b3ff6eb21 | -1.69916 | -46.16938 | 2024-11-28 04:23:00 | NOAA-20 | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b3218b46-5379-3592-a26b-2d58a1f2543f | -6.34836 | -44.80839 | 2024-11-28 04:23:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e73178d2-15ff-3913-9cf4-c04c2ac625d5 | -6.35116 | -44.81254 | 2024-11-28 04:23:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 199ee5bb-d5ca-32af-92b8-4642724b2659 | -5.41951 | -47.91875 | 2024-11-28 04:23:00 | NOAA-20 | AUGUSTINÓPOLIS | TOCANTINS | Brasil | 1702554 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4b7b251e-b4e0-313a-864a-3e5e86095d84 | -8.5648 | -49.19764 | 2024-11-28 04:23:00 | NOAA-20 | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 85b6e837-bc0b-3bae-aa89-81db80257ac4 | -0.95772 | -51.65531 | 2024-11-28 04:23:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6319cc53-bb75-354b-87ac-a3b4c5fcb379 | -1.58658 | -52.27932 | 2024-11-28 04:23:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 9a109298-0ad4-3ba2-a433-a865078184cb | -1.4046 | -45.94772 | 2024-11-28 04:23:00 | NOAA-20 | LUÍS DOMINGUES | MARANHÃO | Brasil | 2106201 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5412714d-c72c-356a-bc1e-660fc5a99fa3 | -1.57798 | -52.01086 | 2024-11-28 04:23:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2d770357-f00c-3d6a-bff1-9659262a731c | -2.43678 | -48.24131 | 2024-11-28 04:23:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 2a7c2b0e-a67f-35dc-b088-831f242372f3 | -0.99069 | -51.7189 | 2024-11-28 04:23:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f805c7c9-7f78-37e4-b3fa-cf9787997a58 | -2.30498 | -47.86297 | 2024-11-28 04:23:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| f846e2e1-071d-390b-8e75-67a9558190f5 | -2.72291 | -46.28992 | 2024-11-28 04:23:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ae7f2990-2dc4-3a6c-ac83-0c9382ffdce1 | -8.85461 | -39.87903 | 2024-11-28 04:23:00 | NOAA-20 | CURAÇÁ | BAHIA | Brasil | 2909901 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 8f4c974f-c7f3-3b24-ae98-0aebcb70a861 | -2.35048 | -48.42638 | 2024-11-28 04:23:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 719b9449-41d7-31d8-9b27-21a105910843 | -1.06749 | -52.42604 | 2024-11-28 04:23:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b8912b9e-3dd0-3c15-acc9-10b6d5beeb88 | -1.57804 | -52.27291 | 2024-11-28 04:23:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 11229398-52d0-35c3-ac38-b8571768ff9e | -0.83955 | -48.18156 | 2024-11-28 04:23:00 | NOAA-20 | COLARES | PARÁ | Brasil | 1502608 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7cd243ea-4f5b-3dc8-b4c1-da0994444ac3 | -1.15928 | -54.07132 | 2024-11-28 04:23:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 78e89812-879d-316c-8c01-bd9ed136a173 | -2.40914 | -46.16906 | 2024-11-28 04:23:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e9653edc-b33d-37cd-859d-f92a8529b2ea | -6.09171 | -48.0355 | 2024-11-28 04:23:00 | NOAA-20 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 21d978f4-eedf-3d61-8f3a-785d043f9e10 | -5.975 | -45.35479 | 2024-11-28 04:23:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 621018eb-0bea-32d8-8f25-eeb4884f8a02 | -0.19766 | -51.41534 | 2024-11-28 04:23:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 63ce13f7-6b00-34ce-9d52-7ff8f56a79ee | -5.87593 | -46.54821 | 2024-11-28 04:23:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3e29fd59-d05e-3286-b002-afb4756b6690 | -2.53751 | -46.41152 | 2024-11-28 04:23:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9c79cab0-43e0-3308-a2ca-a0c626f01f11 | -1.87626 | -50.59962 | 2024-11-28 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 20ed9a93-9011-398e-be1b-2117aa143321 | -1.27185 | -53.02498 | 2024-11-28 04:23:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cc7fdfaf-2ea7-34ef-b6a5-283cfaa2eb50 | -2.58393 | -46.20344 | 2024-11-28 04:23:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 271ecd30-f9f6-3777-8dd7-dcc491c2b2e0 | -1.66971 | -52.73798 | 2024-11-28 04:23:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 22d9963d-c646-3648-833b-62736a116ed1 | -6.10194 | -43.96997 | 2024-11-28 04:23:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| bec4b90b-e198-3b24-9155-2d2ca684649b | -2.58115 | -46.19944 | 2024-11-28 04:23:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1ae8e31b-5d0d-3c4c-a5c3-28cd5d37f0bd | -0.99522 | -51.71963 | 2024-11-28 04:23:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 7ceeab1f-f28a-332b-bb47-43c5b545e719 | -5.42352 | -47.91559 | 2024-11-28 04:23:00 | NOAA-20 | AUGUSTINÓPOLIS | TOCANTINS | Brasil | 1702554 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ad6ce56c-c2c2-3528-a3cd-2806120f1fce | 2.08931 | -50.63604 | 2024-11-28 04:23:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 3.5 |
| eac1bf39-04d6-3115-9398-7deebbe12478 | -5.75509 | -46.25955 | 2024-11-28 04:23:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 39964b87-9b84-37e3-862e-47eac8a97e51 | -5.98219 | -45.35234 | 2024-11-28 04:23:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 26.9 |
| 68028186-582f-3bf8-9818-062ad69c03b6 | -5.66025 | -47.05022 | 2024-11-28 04:23:00 | NOAA-20 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d9b5f1bf-e07c-3774-bee1-a83a1279565e | -2.15566 | -48.71244 | 2024-11-28 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| e078cbc1-4958-3453-8488-f783823be6f9 | -2.55422 | -46.41412 | 2024-11-28 04:23:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 804a8adb-ecd3-37a0-a805-04b92d2d548f | -2.52878 | -47.33496 | 2024-11-28 04:23:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c371a1d9-0159-3c70-864f-194e81a24355 | -1.35548 | -51.96245 | 2024-11-28 04:23:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1203d9ba-d20f-3031-b35e-93e9e3a98853 | -1.38057 | -53.63086 | 2024-11-28 04:23:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9f76d233-e6f5-3230-ab67-67714e43dedb | -2.64109 | -46.95728 | 2024-11-28 04:23:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 78f085f5-e34a-36a6-b2bc-34f627db65d5 | -1.10003 | -53.39817 | 2024-11-28 04:23:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2f9d3e6d-5ecc-3db8-a1fd-b6d74c3ab107 | -5.98 | -45.36631 | 2024-11-28 04:23:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 816e2212-a797-3ade-8bc0-d6362cd57e2c | -5.50929 | -46.26639 | 2024-11-28 04:23:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1607d1d7-0e0a-39cb-9135-af433c4a7e3e | -1.31523 | -51.74682 | 2024-11-28 04:23:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| b1ee981f-55e5-33c5-83c5-62c846670e0b | -2.74106 | -46.08941 | 2024-11-28 04:23:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 26612067-feeb-340e-85b6-e29d5ec3390f | -1.71191 | -52.48199 | 2024-11-28 04:23:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 14ca9c06-6281-3cdd-be1f-5583d7c67b74 | -1.08877 | -48.21324 | 2024-11-28 04:23:00 | NOAA-20 | SANTO ANTÔNIO DO TAUÁ | PARÁ | Brasil | 1507003 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 8addd8b9-3f37-3474-bb23-aa3cc1a3c6ae | -0.93378 | -47.55845 | 2024-11-28 04:23:00 | NOAA-20 | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1db893d7-bfeb-3131-ba15-9b111062cda1 | -1.35929 | -51.96786 | 2024-11-28 04:23:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 95c343d4-36ba-3f0a-983c-a5b9a8d83525 | -1.31072 | -51.74611 | 2024-11-28 04:23:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3a5630b8-a4ee-3121-9319-71ea03a97a5f | -2.55253 | -46.40306 | 2024-11-28 04:23:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1264014f-a4ed-373f-a37a-068f360e9aa3 | -1.06781 | -52.42779 | 2024-11-28 04:23:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ff17ee98-9272-30d0-a90f-c86787005344 | -5.51037 | -46.25948 | 2024-11-28 04:23:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 75b4d3ae-5f5e-38c8-8cd5-1d6553881cd0 | -1.68028 | -52.45958 | 2024-11-28 04:23:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| afe34ab8-abc8-3f4d-b5af-de2b7977bbc0 | -1.0847 | -53.63865 | 2024-11-28 04:23:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 601145e0-aeeb-3be7-a9aa-6e08644198f5 | -1.65792 | -52.72369 | 2024-11-28 04:23:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a56ac372-3b49-399b-ac9f-a2aa858ab060 | -5.20175 | -46.81592 | 2024-11-28 04:23:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6386bc93-5bee-321d-a495-ebbb8fea39e5 | -1.32972 | -51.94769 | 2024-11-28 04:23:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 38562720-9549-3855-80bf-3389efbff199 | -7.94754 | -49.75353 | 2024-11-28 04:23:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 777ff487-4768-3158-9e0e-d00df55d5823 | -1.52106 | -48.63073 | 2024-11-28 04:23:00 | NOAA-20 | BARCARENA | PARÁ | Brasil | 1501303 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 176221a9-0258-3461-bd1c-3ff259d3defa | -1.69437 | -52.49282 | 2024-11-28 04:23:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9dd2ed86-1faa-305d-9c65-b316267665bc | 0.9806 | -50.12893 | 2024-11-28 04:23:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 0c1c4875-55bb-38f7-b210-4157c0ef0344 | -2.56959 | -46.42045 | 2024-11-28 04:23:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fb6bc119-8456-33f7-b7d6-87f3db1a312e | -4.15208 | -54.81056 | 2024-11-28 04:23:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 03f5fc67-0b2d-32a6-9abe-0287739e8c1e | -2.71313 | -46.11703 | 2024-11-28 04:23:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6caa5b76-9a89-330e-adc4-71fe71cf59b9 | 0.94372 | -50.73701 | 2024-11-28 04:23:00 | NOAA-20 | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f6e55d9c-dc3d-3c6c-ab68-0bef16613425 | -5.56309 | -45.38305 | 2024-11-28 04:23:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 46dd974a-e4bc-3783-8287-5f9e729d5dd6 | -5.68136 | -46.42491 | 2024-11-28 04:23:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8e098a99-8125-38bf-87e5-5376e2177d1d | -2.83998 | -45.33194 | 2024-11-28 04:23:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| dda24dce-3b05-34a4-9e7b-ebd1a6693ee7 | -5.75464 | -47.90616 | 2024-11-28 04:23:00 | NOAA-20 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d96a8355-5879-3924-b615-e325af41cb32 | -5.90801 | -43.40846 | 2024-11-28 04:23:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 665e4386-e31d-3a83-8ef1-0d4b3d638625 | -1.67057 | -52.73275 | 2024-11-28 04:23:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| ab16dbf2-76c1-3ac6-8ce9-58d26619f487 | -1.05914 | -52.42125 | 2024-11-28 04:23:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 09640992-8104-39e9-8702-15b3f65c834a | -1.7187 | -46.2192 | 2024-11-28 04:23:00 | NOAA-20 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4d00a0b5-a3b7-316a-95d6-14993420dc4c | -0.23907 | -51.60174 | 2024-11-28 04:23:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a6a50a0d-4937-352c-8e8c-a9017a7991a9 | -2.06809 | -48.14959 | 2024-11-28 04:23:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| aa09f518-bc75-3d3e-bb43-610ce44dda51 | -0.9487 | -51.65389 | 2024-11-28 04:23:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 480faec7-d261-3ca8-8802-a440cbb214aa | -1.05798 | -52.42456 | 2024-11-28 04:23:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 890bdddc-ba6c-3de5-b71f-779d9d9ac0c9 | 0.98758 | -50.25873 | 2024-11-28 04:23:00 | NOAA-20 | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 58191d59-3c02-3d95-ab36-00e15e218bb8 | -2.55032 | -47.17528 | 2024-11-28 04:23:00 | NOAA-20 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3ec9efce-26b1-3877-a81c-ede348d3c063 | -6.92187 | -38.14121 | 2024-11-28 04:23:00 | NOAA-20 | SÃO JOSÉ DA LAGOA TAPADA | PARAÍBA | Brasil | 2514206 | 25 | 33 | nan | nan | nan | Caatinga | 0.7 |
| fa381c24-eb60-3cf5-9827-8eecf38faa12 | -2.11168 | -47.8943 | 2024-11-28 04:23:00 | NOAA-20 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1bea8a0f-b54f-3e81-baff-beef396098d6 | -2.3551 | -48.07283 | 2024-11-28 04:23:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f7c671e0-91d4-3dca-bc0e-5a53da5993b3 | -1.30316 | -51.73561 | 2024-11-28 04:23:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 19764ad7-5273-3cf7-831f-14e9be0809d2 | -5.33357 | -46.19657 | 2024-11-28 04:23:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 01f99f42-b739-3ee8-94a5-eeaf0f99a1e8 | -9.17955 | -44.72576 | 2024-11-28 04:23:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5110c672-9691-3252-95d0-5e315e6c769b | -2.53807 | -46.40798 | 2024-11-28 04:23:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README44.md)
