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

## Dados Diários - Página 29

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 16097e7a-7a44-39d4-944f-78cc0fb8d29f | -6.51243 | -41.43766 | 2024-11-10 04:14:00 | NOAA-21 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 41ff783c-99d0-321d-b513-79493973fc01 | -3.1314 | -45.9616 | 2024-11-10 04:14:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2af43ed6-475c-33c0-bd76-c7fee91a171d | -4.19566 | -48.54459 | 2024-11-10 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0340821e-cd26-3c2c-9656-7ffebf09f8ea | -1.24472 | -51.77079 | 2024-11-10 04:14:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a628fb08-eaff-3109-be01-50de790473b3 | -1.98067 | -49.01724 | 2024-11-10 04:14:00 | NOAA-21 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 367363f4-eec7-3e8b-86b8-78998a5b5ab2 | -3.96497 | -48.17653 | 2024-11-10 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 5cf84b46-0dfa-31b4-a0cd-7b8b79c045aa | -3.14444 | -46.51096 | 2024-11-10 04:14:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8b89535f-df5e-3788-853b-245fb37923c0 | -4.27638 | -48.18737 | 2024-11-10 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2ccd3f25-a947-30fb-bafe-c28c249bd085 | -2.76929 | -49.34982 | 2024-11-10 04:14:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| a93f7e76-b38f-322e-8561-2354d3e72fd0 | -3.23836 | -50.28524 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9f79d24c-530e-3bbc-bc71-3c399836e46a | -4.95274 | -48.4507 | 2024-11-10 04:14:00 | NOAA-21 | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e1ce0a33-19ea-3efd-98f7-0e4ca095b299 | -1.34434 | -51.40614 | 2024-11-10 04:14:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3dac6190-8bcd-350c-9708-749161b67eb2 | -4.87824 | -48.59176 | 2024-11-10 04:14:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 53feb9c6-c0fa-3e34-aa5c-6e1a015eab23 | -3.49568 | -45.86317 | 2024-11-10 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c17cdffc-a368-3f47-91c1-8642ab8b1b82 | -4.62477 | -49.08306 | 2024-11-10 04:14:00 | NOAA-21 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 99cb09a8-298b-35c6-9454-a0c73b3f1f17 | -4.60548 | -43.35645 | 2024-11-10 04:14:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b1d6583f-98e9-30ec-84a0-f792ed853120 | -3.22013 | -50.31318 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f11512ee-e333-375b-8d7e-16ebb0730ec3 | -3.5118 | -44.03291 | 2024-11-10 04:14:00 | NOAA-21 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 23.9 |
| ceb882a0-cdfc-3062-8a7e-fab82959d579 | -5.60926 | -45.93348 | 2024-11-10 04:14:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 520e3d67-7e1c-36d4-b371-b270aff6055d | -2.40674 | -48.52951 | 2024-11-10 04:14:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3d78b8d3-3d7b-3461-a2ba-b1deb2366787 | -5.47258 | -44.61627 | 2024-11-10 04:14:00 | NOAA-21 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 8c5862be-813f-3ee9-b4d1-8de3fa060037 | -5.5627 | -47.78351 | 2024-11-10 04:14:00 | NOAA-21 | SÍTIO NOVO DO TOCANTINS | TOCANTINS | Brasil | 1720804 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| dc1697ce-9767-3eb2-a0bf-a51a3ac1f7de | -0.04473 | -50.79037 | 2024-11-10 04:14:00 | NOAA-21 | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e5a8364e-89ec-3486-8638-fdb49e985215 | -3.04336 | -49.54248 | 2024-11-10 04:14:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 9c6e5a76-fe45-3f3e-9329-62661d14d21f | -2.87726 | -49.38012 | 2024-11-10 04:14:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 685a046e-4643-37cd-b18b-95e8fea2988f | -4.10589 | -49.13508 | 2024-11-10 04:14:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 83a61b96-c988-3d0f-b780-34d75093de00 | -2.31893 | -48.54165 | 2024-11-10 04:14:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 892ff05c-057b-3397-b1ff-36b1bdeee51d | -3.23901 | -50.28877 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 64f5974f-a221-3e83-a14e-e9af9ac31056 | -3.62089 | -41.57447 | 2024-11-10 04:14:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| acb9e78c-3564-3631-bb7a-e8c8cbf6a3fe | -4.07688 | -50.01019 | 2024-11-10 04:14:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| ddc282bc-de66-349c-af88-839c6d631a25 | -2.67478 | -46.8023 | 2024-11-10 04:14:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 43ff3d65-de00-3a49-a6f0-81c7b0c1e954 | -2.46311 | -46.32817 | 2024-11-10 04:14:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 41fe7434-3e15-3f9d-a9de-e52afb8c3dc9 | -5.16454 | -49.61858 | 2024-11-10 04:14:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 503ba966-2505-376a-866d-0e328913b695 | -4.02008 | -48.29439 | 2024-11-10 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0bf0ad9f-d080-3bba-86a3-270a96ba6895 | -3.1199 | -51.10732 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3d89f13c-aa97-35e9-b797-57cceef9526d | -4.1258 | -43.594 | 2024-11-10 04:14:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7e107bcb-31c1-3b42-830e-cd028c55c346 | -3.80158 | -41.2652 | 2024-11-10 04:14:00 | NOAA-21 | TIANGUÁ | CEARÁ | Brasil | 2313401 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 2c105c35-5256-386b-8a61-3b0622bd2dc3 | -4.11786 | -46.92479 | 2024-11-10 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5b3484cf-303e-3f18-b073-b6720a059e95 | -2.21646 | -46.41613 | 2024-11-10 04:14:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f7f4e090-67a4-3546-bcb1-01c8155d7109 | -2.68246 | -46.77897 | 2024-11-10 04:14:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2d5132ab-4225-3bf7-9a32-cb779eb41555 | -3.11356 | -50.15261 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 6da6453f-36b8-3474-b005-57a51f030b4a | -3.13072 | -45.96589 | 2024-11-10 04:14:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f55ed6e0-66c0-3ddd-80a3-7efc647969a6 | -3.30348 | -54.4882 | 2024-11-10 04:14:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e5bc55ba-3df6-3cf8-8529-f967c1918b4d | -2.14361 | -48.11518 | 2024-11-10 04:14:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e01c2633-5239-329a-909c-74fd23aae08d | -3.39416 | -49.7306 | 2024-11-10 04:14:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0ef44698-fa90-3bb2-abbb-568d8d5611ea | -3.20887 | -50.63358 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 148ad2d6-6271-3559-b164-59d16d9ff896 | -3.24948 | -51.55312 | 2024-11-10 04:14:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a05dde0b-5a47-3569-8e02-06169fbfa4df | -2.39682 | -50.32368 | 2024-11-10 04:14:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e2c9732e-fdb9-3220-b244-98cd11ee7c60 | -3.58613 | -50.41358 | 2024-11-10 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4045008c-9161-3f99-a9ac-bb29722295b6 | -4.27997 | -47.08022 | 2024-11-10 04:14:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fa43d973-bd50-36c7-b485-b4f273178836 | -3.9912 | -46.41854 | 2024-11-10 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 757946e0-a3dd-3359-892d-e42c5c3af5fd | -4.25333 | -48.53721 | 2024-11-10 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 5cd5c889-b981-3596-8cfc-defcbdd87093 | -3.27136 | -53.69989 | 2024-11-10 04:14:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d8af8eab-eaed-3579-9f64-479ef868266b | -3.36123 | -53.40611 | 2024-11-10 04:14:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| b49061b7-b0ef-3536-836e-bfbbdd76262f | -2.56852 | -47.33822 | 2024-11-10 04:14:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 719b8eb6-6938-3c65-b98a-c6a4708ee8f0 | -4.1022 | -49.13008 | 2024-11-10 04:14:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 799aaec9-0fe1-31a4-88af-2bb3a3bbd0df | -2.68479 | -46.78922 | 2024-11-10 04:14:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c73bf04f-2282-3e0c-9ca5-7d30001feab4 | -3.17162 | -49.10459 | 2024-11-10 04:14:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| b0bfe19a-572e-31f1-aaeb-73be3c7d6a30 | -3.94221 | -42.78992 | 2024-11-10 04:14:00 | NOAA-21 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Caatinga | 0.7 |
| af9fe846-aacf-3ca9-a500-7b24802a7b97 | -3.34118 | -50.35654 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| f161f5d6-ad7a-3b22-a2c4-50f1e3695089 | -3.45439 | -47.66806 | 2024-11-10 04:14:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 8d0072f1-948b-3ae8-a65e-6b06b19cefd1 | -3.25074 | -46.47848 | 2024-11-10 04:14:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3d5b1200-6dbb-34fc-ac4d-487c86d5462e | -3.69841 | -54.61568 | 2024-11-10 04:14:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1e2a88f6-4c9a-397e-8542-9075ab88c2ed | -2.82514 | -49.44059 | 2024-11-10 04:14:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| ab76c67e-82d2-3736-b271-67a81aaf84e5 | -3.44468 | -50.43363 | 2024-11-10 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 17a17aeb-bfb0-3059-b6ea-000a7efd09f3 | -5.31272 | -47.68917 | 2024-11-10 04:14:00 | NOAA-21 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 51f10413-2b62-3bb0-9dd3-c2e9f08665a4 | -3.22187 | -50.30243 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d3192744-b6ef-3169-b9f4-6fbf671d3805 | -1.25025 | -51.77167 | 2024-11-10 04:14:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| aa0be33f-c8af-300c-8edd-9f8d60b00b51 | -2.33572 | -46.56534 | 2024-11-10 04:14:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 387331dc-08cc-3b8e-93f8-e635221b7308 | -2.6617 | -49.85289 | 2024-11-10 04:14:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 81165162-f3f6-32de-9f34-f4d2a6d2f67e | -4.10878 | -50.73435 | 2024-11-10 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 2eafe877-9f8d-30d3-b502-d2090c5a77c2 | -3.51796 | -44.03752 | 2024-11-10 04:14:00 | NOAA-21 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 61bb3db1-120c-3ee1-b3ec-3f1a99ddbc9d | -3.25013 | -51.55276 | 2024-11-10 04:14:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 42db1d6d-7df6-3fb4-b639-7b2c416c2227 | -3.98905 | -46.41903 | 2024-11-10 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 20877ebc-dc6c-3b22-8194-2e6b1cb2de6c | -3.44231 | -50.09556 | 2024-11-10 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9f4f8b9a-207c-3cad-b262-04f68f8b46d0 | -2.31088 | -48.53608 | 2024-11-10 04:14:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 969f0cb7-23c4-3be2-a917-7aed812d089d | -4.60738 | -45.96734 | 2024-11-10 04:14:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 35211f1d-f1cb-3d09-9bc4-9c05752e5083 | -1.20418 | -53.62789 | 2024-11-10 04:14:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e7784618-952f-371f-98ec-804ca2ede162 | -2.92654 | -51.67754 | 2024-11-10 04:14:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 6d351652-1d1d-3eb2-867b-93e9b23e72c2 | -6.40693 | -42.48963 | 2024-11-10 04:14:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 98df8a16-8702-3216-b1b2-f712657ad5ba | -3.25538 | -48.75474 | 2024-11-10 04:14:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4ac00557-2979-3647-8267-506478056230 | -4.57525 | -45.4115 | 2024-11-10 04:14:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8960d4d8-bd10-3b07-b6dd-0a625c4ea2a2 | -3.2611 | -48.74701 | 2024-11-10 04:14:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 8510704c-5019-37e8-a9dc-830d09443c6f | -1.87184 | -54.17962 | 2024-11-10 04:14:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| c4f4a703-dc17-376a-bf95-58ba1a1d39af | -2.19644 | -48.37899 | 2024-11-10 04:14:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b860a814-e258-3a1a-a04f-84b2ae645750 | -4.92796 | -48.52445 | 2024-11-10 04:14:00 | NOAA-21 | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d362f988-3303-3a45-92c4-02e58f9cb83c | -3.23962 | -50.30729 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 22.3 |
| 08f0898d-67f7-3d30-95e8-ac2c20ccc991 | -2.20641 | -48.37208 | 2024-11-10 04:14:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 2bc0240e-33af-3304-89fc-2a9a60749df4 | -3.18457 | -50.59479 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ed136290-cff2-3332-bdb8-e39575ec53c1 | -2.71642 | -51.7113 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c821471d-ce36-3582-ae19-d7520f7ef5e3 | -2.90165 | -45.56321 | 2024-11-10 04:14:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 495bad15-6c21-3080-b6ce-af3743b1b387 | -1.53507 | -52.2052 | 2024-11-10 04:14:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 2dc25232-0509-3611-b38d-94d81932b433 | -2.45599 | -47.16168 | 2024-11-10 04:14:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| d6930aa1-7b34-3a74-9146-db37d02240d7 | -3.96557 | -48.17285 | 2024-11-10 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| b8465d67-1226-3ec5-8931-23afba3da184 | -3.5739 | -45.82257 | 2024-11-10 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 50592982-3e1c-30ff-9adb-c25992c8acfe | -2.20432 | -47.73509 | 2024-11-10 04:14:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 83d94c9e-cd30-37d8-a24d-e8d6f07739f9 | -4.13284 | -53.50446 | 2024-11-10 04:14:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e6d5fabd-1b03-3435-8846-0511eb2b21a3 | -5.05535 | -44.28142 | 2024-11-10 04:14:00 | NOAA-21 | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3ba82a00-8175-3cb2-bb3d-271e7d564fd0 | -1.68763 | -50.41257 | 2024-11-10 04:14:00 | NOAA-21 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5383a78c-5050-3cb5-867b-ccd84de97c86 | -5.84851 | -44.49059 | 2024-11-10 04:14:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |


[Clique aqui para ver as próximas entradas](README30.md)
