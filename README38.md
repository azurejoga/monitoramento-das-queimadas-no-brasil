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

## Dados Diários - Página 38

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 05bc6ad0-39ec-3dc8-88b2-fa8c0dbc1de2 | -3.40242 | -53.20132 | 2024-11-27 04:18:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3f702160-f474-35a8-9c58-7dd33e7df66d | -2.18468 | -53.77907 | 2024-11-27 04:18:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 7cfdb4b1-cce9-3af7-a914-51387a55f9f4 | -3.46547 | -50.25318 | 2024-11-27 04:18:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3d02612a-eb9c-308c-8177-efcf30838536 | -2.84708 | -46.83289 | 2024-11-27 04:18:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ad7b02a1-aae6-35c9-82dc-e3778af1381a | -3.97209 | -46.64914 | 2024-11-27 04:18:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8cae5fd4-ce50-3543-b5c4-2f67be5cb42b | -3.27144 | -43.03949 | 2024-11-27 04:18:00 | NPP-375D | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3d331b21-b94f-3411-96bd-bd08d29f5216 | -3.08577 | -49.20961 | 2024-11-27 04:18:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 841b57a2-1c3e-3f9a-98f8-a42bbd950249 | -3.14547 | -48.53524 | 2024-11-27 04:18:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 83e539ef-557d-3fa8-85ab-d17a89cc5fee | -2.82513 | -46.80832 | 2024-11-27 04:18:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f54bea8d-4cf4-395e-90ba-2387d16ab703 | -3.94707 | -46.91504 | 2024-11-27 04:18:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ebbfc659-dfde-3c1d-a9d2-4c346221ebe2 | -1.71824 | -53.06156 | 2024-11-27 04:18:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 66fedc83-23d5-39af-bf76-a98aa2e9e772 | -2.82121 | -46.833 | 2024-11-27 04:18:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 85aec4f4-b866-36c9-9dfe-cc20e37490a0 | -4.00172 | -50.35092 | 2024-11-27 04:18:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 029e2e43-7bd0-3f90-b112-0fcdf094d595 | -5.31866 | -43.07259 | 2024-11-27 04:18:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b6a19dc9-fe1a-3ccb-9ae5-0ce42c0fa9d2 | -2.59879 | -53.96523 | 2024-11-27 04:18:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c688bdb8-1b7a-3506-8fd5-85ac4c6523f9 | -4.24012 | -41.92583 | 2024-11-27 04:18:00 | NPP-375D | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| ebe82ffd-351c-39e7-91eb-be8df7b14a13 | -2.56617 | -46.41883 | 2024-11-27 04:18:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f8ce0c14-f273-384e-9b16-d9dfa9b96018 | -4.20871 | -50.8953 | 2024-11-27 04:18:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 34851aeb-1d24-394e-81de-b88c6d024f8f | -3.71501 | -47.12508 | 2024-11-27 04:18:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9f090520-7717-323c-b5d3-74b1ff5b4f76 | -2.72125 | -46.28082 | 2024-11-27 04:18:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d6794564-099d-3bea-ab02-a78a6c95737d | -4.94901 | -45.87949 | 2024-11-27 04:18:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8a494a16-c79f-3c93-b97b-6df8273f9551 | -2.78326 | -49.21191 | 2024-11-27 04:18:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 23e76845-8c32-3a18-b336-46c1435fc6d7 | -3.90062 | -45.61968 | 2024-11-27 04:18:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b6432c02-9521-35a9-8008-77feea6c6069 | -2.28168 | -47.91511 | 2024-11-27 04:18:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b2715821-69eb-314e-a99a-e3da68fd9df3 | -1.9903 | -53.29158 | 2024-11-27 04:18:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 034ecf89-2032-37f0-b2e0-93a92ce38162 | -3.85409 | -46.50794 | 2024-11-27 04:18:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 988a1281-71b1-38bd-ab57-2f9cb0464943 | -1.42325 | -45.95884 | 2024-11-27 04:18:00 | NPP-375D | LUÍS DOMINGUES | MARANHÃO | Brasil | 2106201 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b7baa76b-3eec-3ad9-9d2f-18a8422b33eb | -4.05776 | -49.07988 | 2024-11-27 04:18:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 704be333-38ac-3fde-8c3d-260c3c64b1c5 | -3.97171 | -48.06585 | 2024-11-27 04:18:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 28ad89d6-6f3c-3e2c-be4c-88bee990e7df | -3.69866 | -50.22774 | 2024-11-27 04:18:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a069df48-4cd4-3cbe-b5c8-90cc6acebd8f | -2.71542 | -46.11314 | 2024-11-27 04:18:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b4e54630-22e6-30c7-b8ae-b9ba56f344fe | -4.59201 | -46.1214 | 2024-11-27 04:18:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3dd214f9-878a-393e-baba-e4b5a1c0aa83 | -4.29491 | -48.07264 | 2024-11-27 04:18:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 89fefc36-31e3-3680-9518-5a6fdd30a3b1 | -3.57786 | -41.96619 | 2024-11-27 04:18:00 | NPP-375D | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 450867d7-3747-3a22-860a-a7c235e144dc | -4.93292 | -38.74919 | 2024-11-27 04:18:00 | NPP-375D | QUIXADÁ | CEARÁ | Brasil | 2311306 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 81f3e276-82fb-3e50-8b8f-5c5592ba7bc0 | -2.90357 | -45.23815 | 2024-11-27 04:18:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5270f93d-5919-3cb1-8c3d-0ee0df7b1b4f | -2.34818 | -47.64776 | 2024-11-27 04:18:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 66ab5657-57f6-3e64-91b0-0dd4df7aa1ce | -3.98269 | -46.65075 | 2024-11-27 04:18:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 58d25037-99cf-3fd1-b6fe-22c24dbc51d6 | -3.24472 | -50.146 | 2024-11-27 04:18:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 2d28b0ea-272e-3ae6-a282-df30a40c2ec4 | -3.18071 | -48.44326 | 2024-11-27 04:18:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 3f00097e-c9d9-3652-b398-3bb06e858704 | -2.92971 | -48.63303 | 2024-11-27 04:18:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 8c6e969e-849b-351f-88e7-116204f4985c | -1.66138 | -52.7131 | 2024-11-27 04:18:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f2f29967-66e5-3b32-bb77-b6147a720587 | 0.94633 | -50.73765 | 2024-11-27 04:18:00 | NPP-375D | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ece9378e-6524-3d79-a638-868e881c9ed3 | -2.94222 | -54.80056 | 2024-11-27 04:18:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8e16dbbe-60b0-3e38-976d-dbadf5ed4557 | -3.84407 | -51.38641 | 2024-11-27 04:18:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| db8ed917-45ac-3620-862a-15e9bfe89793 | -2.25415 | -53.74954 | 2024-11-27 04:18:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 7c2389cf-ad6e-3528-a49c-5c2dac828db9 | -1.77673 | -46.95125 | 2024-11-27 04:18:00 | NPP-375D | SANTA LUZIA DO PARÁ | PARÁ | Brasil | 1506559 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d6530693-32a7-3711-b236-c94f440b8b6c | -3.49854 | -50.45737 | 2024-11-27 04:18:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 46e8cb13-1620-37ce-8655-48ce3f8b6d12 | -1.26708 | -52.23257 | 2024-11-27 04:18:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f65e34fa-b59b-34b0-b112-e0f8183e889c | -4.47528 | -46.66216 | 2024-11-27 04:18:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b9e1c204-1b4e-3d6d-9e19-de4455b2c343 | -3.84287 | -46.64679 | 2024-11-27 04:18:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 53b81d49-1e9a-3b20-9064-9d8e8fe01733 | -3.93846 | -47.9866 | 2024-11-27 04:18:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 47968471-44b2-3685-ba27-3531882ab463 | -4.8109 | -46.84086 | 2024-11-27 04:18:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bfcbe3d0-b7da-3d6f-b4ef-f1227c889c2a | -3.10182 | -50.36015 | 2024-11-27 04:18:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 377fc4e6-7415-37b7-9e9e-93bc62e53878 | -2.84289 | -49.40496 | 2024-11-27 04:18:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 61dc1fb2-4211-3444-9808-90707aadfc8b | -3.3756 | -50.11346 | 2024-11-27 04:18:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 0f78a5c8-3e65-3b1c-b36c-2ad9cbd47178 | -3.10909 | -53.26782 | 2024-11-27 04:18:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b5f4df40-09b1-3663-b7fe-d4f4c430028f | -1.20288 | -51.75589 | 2024-11-27 04:18:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c00a44b2-da6e-3d58-acf3-a57ff773f901 | -1.18494 | -51.98211 | 2024-11-27 04:18:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2764c126-c1fa-38fc-a143-58ee379b7adb | -2.4373 | -50.41513 | 2024-11-27 04:18:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| da5d97f2-6a93-3f19-998e-93ea6f1ae7d6 | -1.71882 | -53.05798 | 2024-11-27 04:18:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 71bf62b9-633f-3525-b08a-7bf31865643a | -3.96107 | -46.89648 | 2024-11-27 04:18:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 24937622-628e-305c-ab13-052adfe0439f | -3.09875 | -53.26246 | 2024-11-27 04:18:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fe7370ea-4d26-3445-aee8-a93e979896a2 | -3.78226 | -46.6856 | 2024-11-27 04:18:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e96afd1b-46dc-3986-a6b5-192f6528648a | -2.80287 | -52.9058 | 2024-11-27 04:18:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d43ba647-00ec-3a50-a7d2-5ef4644c4488 | -3.9061 | -50.59981 | 2024-11-27 04:18:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3b025df0-6b93-31fc-b871-b37af1341d45 | -3.09211 | -53.26878 | 2024-11-27 04:18:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2582412c-a257-3d42-83ba-0883552f0c8d | -3.95618 | -46.90403 | 2024-11-27 04:18:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 846c374e-a82c-3fdd-a0e9-f57d4b0feaa8 | -2.85148 | -46.83644 | 2024-11-27 04:18:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 31212be1-55b7-35a1-8187-72a2a6da1dbf | -2.44258 | -50.41132 | 2024-11-27 04:18:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5f1d1523-7190-3958-8a31-3d181bdc108b | -5.20703 | -40.63365 | 2024-11-27 04:18:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 8e99c3e2-c207-352f-a1c8-6c6692420d6a | -5.14424 | -37.74408 | 2024-11-27 04:18:00 | NPP-375D | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 200f55f5-32ba-3509-a37b-5a02807fb1c8 | -4.35775 | -44.67518 | 2024-11-27 04:18:00 | NPP-375D | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 514e2ece-fe1f-363d-a0ae-6612b7a56cb0 | -4.65146 | -43.81777 | 2024-11-27 04:18:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fd8efa12-5c6b-334f-807f-d306924519ba | -3.24553 | -51.15374 | 2024-11-27 04:18:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8a47e13d-3f96-3273-81ca-1f05627b8eef | -4.9605 | -47.592 | 2024-11-27 04:18:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3bbfb4fa-d197-3815-82b1-02dac8231ac2 | -3.96867 | -48.06063 | 2024-11-27 04:18:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 730f0124-d7d7-3be1-8bee-86816e4f5a68 | -2.69295 | -45.662 | 2024-11-27 04:18:00 | NPP-375D | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3f141410-39cd-32d5-999e-8d03e252cd0c | -3.70581 | -51.80095 | 2024-11-27 04:18:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a6921663-4dd1-3781-a9aa-8bacdb2d3526 | -1.89868 | -50.59455 | 2024-11-27 04:18:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fb4d3d31-06a3-3278-b06a-0d78f1abbf79 | -2.78802 | -49.20881 | 2024-11-27 04:18:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ab4023c5-8013-31dc-959b-dad339ef16b6 | -2.79257 | -48.60139 | 2024-11-27 04:18:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6a588c28-feb8-383c-84ac-44978341bebf | -1.42676 | -45.95938 | 2024-11-27 04:18:00 | NPP-375D | LUÍS DOMINGUES | MARANHÃO | Brasil | 2106201 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 71679e52-791a-34f9-b5b0-a8817745df88 | -1.77604 | -46.95555 | 2024-11-27 04:18:00 | NPP-375D | SANTA LUZIA DO PARÁ | PARÁ | Brasil | 1506559 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 64c1ede8-fe32-3bef-81f4-fef49420b61e | -2.09969 | -46.56314 | 2024-11-27 04:18:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 326fbc6e-f2e2-3188-93c6-e0224a0f9f01 | -3.04149 | -48.51159 | 2024-11-27 04:18:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 17.7 |
| 6d89073f-db2a-3640-a2f4-b67cac0e87ad | -5.35978 | -42.12561 | 2024-11-27 04:18:00 | NPP-375D | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 786aa724-4c3f-3181-a5cc-62ac387d8ae6 | -4.1095 | -46.80418 | 2024-11-27 04:18:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 29776835-d681-3a82-afff-7aea0014c36f | -2.94244 | -54.79473 | 2024-11-27 04:18:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| b8272f74-da84-3cba-b82f-ea6f1080a41f | -2.82153 | -46.80776 | 2024-11-27 04:18:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ea41688c-9e06-30e6-bf94-8b68285fddee | -3.0908 | -53.28126 | 2024-11-27 04:18:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3a31676c-6d52-3bbc-bc26-88425e69170e | -2.24971 | -53.63364 | 2024-11-27 04:18:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ada4bdb7-d812-3ef3-ae91-1c3e6536fb89 | -3.80972 | -46.60501 | 2024-11-27 04:18:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 176cb14b-bc5f-3cf8-a30f-9fd50fc9ce35 | -4.37874 | -45.97543 | 2024-11-27 04:18:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 76592703-beea-3460-8c24-31eef4492df3 | -2.94297 | -54.79622 | 2024-11-27 04:18:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| de663752-99fc-395f-967f-cb83f0f36346 | -1.78748 | -52.74557 | 2024-11-27 04:18:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d98ebbb4-8f23-3fee-b8c7-15678055606f | -2.68323 | -45.65667 | 2024-11-27 04:18:00 | NPP-375D | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f2d1041b-f9d3-3c75-87f8-d476aec9d6bc | -3.58305 | -41.95553 | 2024-11-27 04:18:00 | NPP-375D | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 90a293aa-1d36-3ac1-ae19-e3b145a9aa3f | -4.30785 | -48.18395 | 2024-11-27 04:18:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8ad4a320-861c-32e6-a83a-784f6d045c00 | -3.08606 | -53.2715 | 2024-11-27 04:18:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README39.md)
