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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d44b26fb-2104-37a0-a6e4-6dce1880eee2 | -3.4201 | -50.2375 | 2024-12-02 01:30:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 36.9 |
| 302675fd-86d0-3974-82ed-feba80147f0c | -12.4358 | -63.7455 | 2024-12-02 01:30:00 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 62.4 |
| 3848146a-3e74-380a-af00-67963dd372a9 | 3.3658 | -60.5139 | 2024-12-02 01:30:00 | GOES-16 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 49.8 |
| 9d7bbfe4-8484-303e-a96c-463891bcea97 | -2.6348 | -53.3712 | 2024-12-02 01:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 77.0 |
| 16ec073d-4d28-3ac1-ae0f-a9fa795cc573 | -20.7217 | -54.4341 | 2024-12-02 01:30:00 | GOES-16 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 82.2 |
| afad4bc5-f07a-353c-89f1-57625e57a872 | -3.4017 | -50.2171 | 2024-12-02 01:30:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 38.8 |
| 5e66bfe2-bb57-31d2-adf4-9dc117de1aa1 | -4.267 | -50.8551 | 2024-12-02 01:30:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 54.0 |
| a034192f-8ca8-397b-9403-e9c965c12b54 | -3.3848 | -49.8596 | 2024-12-02 01:30:00 | GOES-16 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 35.5 |
| c210e40e-ed38-387a-9d77-846e589bd15c | -2.008 | -54.3091 | 2024-12-02 01:30:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 42.3 |
| 946172c4-885a-3d91-8806-7e361f9a4eba | -5.1369 | -43.1951 | 2024-12-02 01:30:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 31.8 |
| 526badd3-e15f-3ce7-ae6e-910f70459804 | -6.086 | -48.0557 | 2024-12-02 01:30:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 223.2 |
| 5803bd26-834e-35ba-a659-fc724eb1ea0c | -2.0263 | -54.3289 | 2024-12-02 01:30:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 44.0 |
| a5811758-43f4-31f9-8c5e-7e4706392b1f | -2.6349 | -53.351 | 2024-12-02 01:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 74.7 |
| c54ebc92-513a-307a-86de-5891a9b3d7ca | -12.4359 | -63.7264 | 2024-12-02 01:30:00 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 513b3725-b611-3885-a922-e29974a599b4 | -4.5932 | -43.3471 | 2024-12-02 01:30:00 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 45.5 |
| 0be840d0-a003-3ed8-9a38-153dcbf749b0 | -2.6076 | -45.2469 | 2024-12-02 01:30:00 | GOES-16 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 48766cde-1fd2-357e-9ae6-a1bf142ff8a2 | -6.0858 | -48.0774 | 2024-12-02 01:30:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 77.6 |
| 523b123d-598f-328e-9e57-47dffc59afa8 | 3.3841 | -60.4946 | 2024-12-02 01:30:00 | GOES-16 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 53.9 |
| a21a74bc-9209-351a-8166-a6361d08d100 | -3.7084 | -51.8301 | 2024-12-02 01:30:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 51.0 |
| 36ca98a4-4397-3a07-9e96-e8fd702ff9c2 | -6.0862 | -48.0339 | 2024-12-02 01:30:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 93.2 |
| f09eb2db-2434-3bbf-9b0c-d41a7e3ac765 | -4.9085 | -41.3371 | 2024-12-02 01:30:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 141.6 |
| 35823799-1c91-3050-a242-fe66042b31db | -2.8196 | -53.0629 | 2024-12-02 01:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 70.3 |
| 6fd54cf1-856d-3153-9af8-118ab9c400c2 | -4.5745 | -43.3483 | 2024-12-02 01:30:00 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 70.7 |
| 3630cabc-32cd-36a5-ab04-d3e70d48be94 | -3.2775 | -53.6181 | 2024-12-02 01:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 50.1 |
| 03969257-836d-30fd-b91a-1bee890e0a0c | -3.2774 | -53.6383 | 2024-12-02 01:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 52.6 |
| 3dd3e4c7-8b1a-3f0e-aa89-4719f3145782 | -5.118 | -43.2198 | 2024-12-02 01:30:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 47.5 |
| b7dd2e7f-f3f2-3b14-a160-d74fb875ce19 | 3.3841 | -60.5135 | 2024-12-02 01:30:00 | GOES-16 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 66.6 |
| 286652e4-b9c8-3029-a4bc-047d62314011 | -3.4017 | -50.2381 | 2024-12-02 01:30:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 58.0 |
| cc3cd134-909d-3d2c-9346-3dcc49767dba | -2.8013 | -53.043 | 2024-12-02 01:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 63.6 |
| defe4889-ea2e-3116-a2c0-ab05810bda10 | -5.5882 | -45.1412 | 2024-12-02 01:30:00 | GOES-16 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 64.8 |
| fd6a0587-ca13-3510-961a-a18408fc106b | -2.5612 | -53.3931 | 2024-12-02 01:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 111.9 |
| 7f91d7c1-7167-3b7d-b944-3b08bfed2b89 | -5.1181 | -43.1964 | 2024-12-02 01:30:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 57.1 |
| d296fbcc-9751-30b0-86d7-236b63114d38 | -2.2666 | -53.6212 | 2024-12-02 01:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 988b1741-7c5c-3418-a23c-b32d6ad3712b | -3.259 | -53.6388 | 2024-12-02 01:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 74.5 |
| ad9aced4-7eb7-3c81-b0bc-b0ae2c417c0c | -2.5612 | -53.4133 | 2024-12-02 01:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 117.7 |
| 3e3c7605-5467-3623-a87f-7484a2b49e8f | -5.118 | -43.2198 | 2024-12-02 01:40:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 55.5 |
| db18f050-28d3-3324-aaee-d4d9da48f8b7 | -2.6349 | -53.351 | 2024-12-02 01:40:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 76.1 |
| df8d09c1-a345-373b-b2e5-07c365a5f06c | -2.8197 | -53.0425 | 2024-12-02 01:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 0f2f93fd-a497-3e25-983a-2b51e923e0e9 | -2.008 | -54.3091 | 2024-12-02 01:40:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 20cae8ed-1ae4-365f-92d3-8e05653fdf8e | -4.5745 | -43.3483 | 2024-12-02 01:40:00 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 78.4 |
| c1b7e378-7d16-3832-9a94-f98d4667f7c2 | -6.0862 | -48.0339 | 2024-12-02 01:40:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 74.9 |
| f691f958-5ab4-36cc-a685-a8ac966e3110 | -2.2667 | -53.6011 | 2024-12-02 01:40:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 48.9 |
| 1b28eaac-c8b0-3eb3-8817-956b291f111d | 3.3658 | -60.5139 | 2024-12-02 01:40:00 | GOES-16 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 59.7 |
| dde94a40-ea3d-3fd3-98ac-c4bfce19bba1 | -3.259 | -53.6388 | 2024-12-02 01:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 80.6 |
| 86669435-fa75-382a-b00a-b668c51298ba | -3.4017 | -50.2171 | 2024-12-02 01:40:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 36.5 |
| 6ddf3b47-7feb-32de-aeb9-a7894a44c07d | -5.1367 | -43.2185 | 2024-12-02 01:40:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 42.0 |
| 25f765dd-cd62-3a4f-a81e-a3e448d65238 | -3.7084 | -51.8301 | 2024-12-02 01:40:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 51.0 |
| 6aad5678-ec24-3b60-a853-fe2675aa6373 | -2.8013 | -53.043 | 2024-12-02 01:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 65.8 |
| c8f08b2c-9d13-3a7c-a485-963081a7ea5c | -2.5612 | -53.4133 | 2024-12-02 01:40:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 107.3 |
| 10fe0914-b307-3c62-8c82-e03744510905 | -3.2591 | -53.6186 | 2024-12-02 01:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 113.9 |
| 5b0da007-476a-328b-af8c-f914f0b99fd1 | -4.9272 | -41.3358 | 2024-12-02 01:40:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 67.6 |
| fd0c49fb-0c45-3111-aa58-88ca5962752a | -3.4017 | -50.2381 | 2024-12-02 01:40:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 52.0 |
| a3f24df4-e674-318c-ac29-c8b8e9cc008e | -5.1369 | -43.1951 | 2024-12-02 01:40:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 43.9 |
| aa7548d8-cf1c-359c-b6ee-2977dc6d9a2a | -12.4359 | -63.7264 | 2024-12-02 01:40:00 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 39b98654-48a0-3542-a2b8-1ce72ae7364d | -6.086 | -48.0557 | 2024-12-02 01:40:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 204.9 |
| 7929db7b-f328-3dc1-9acb-d537e260c629 | -4.267 | -50.8551 | 2024-12-02 01:40:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 53.0 |
| 0233fa50-2e98-34e7-9c82-48a8658569fc | -20.7217 | -54.4341 | 2024-12-02 01:40:00 | GOES-16 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 79.4 |
| caf31f85-cfb7-32f4-9b3d-acef2703f553 | -1.0735 | -53.4562 | 2024-12-02 01:40:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 51.4 |
| dcf972a3-e1a8-34c1-8099-fe0a15767d6e | -2.5612 | -53.3931 | 2024-12-02 01:40:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 101.4 |
| e6aa56df-cf74-35bf-963c-4cf6a29f68ec | -6.0674 | -48.0569 | 2024-12-02 01:40:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 99.1 |
| 4d05ce91-9241-3027-a788-21f16af2ad86 | -4.0552 | -48.963 | 2024-12-02 01:40:00 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 8814c584-3053-3ffc-82d3-c6659adea24d | 3.3841 | -60.5135 | 2024-12-02 01:40:00 | GOES-16 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 59.9 |
| 0ada39f0-690b-3db1-aa2e-cadd15bfbe8e | -2.5428 | -53.4137 | 2024-12-02 01:40:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 81.4 |
| 85a76d85-7d62-3d35-9b3c-945912110f3f | -6.1047 | -48.0544 | 2024-12-02 01:40:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 5f0b98e0-6623-3579-ae99-872dbe964ddd | -12.4169 | -63.7465 | 2024-12-02 01:40:00 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 50.6 |
| 714c6c4a-06a6-39f1-9c2f-72233ce7a07f | -2.0263 | -54.3088 | 2024-12-02 01:40:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 76.3 |
| d69904f0-e9dc-3839-9066-bcb7e1f774a3 | 3.384 | -60.5325 | 2024-12-02 01:40:00 | GOES-16 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 47.9 |
| 38601e2e-2698-3313-8024-8db0bb075047 | 3.3657 | -60.5329 | 2024-12-02 01:40:00 | GOES-16 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 45.5 |
| 33b05df0-9b96-3d54-9f74-1602018ab51a | -12.4358 | -63.7455 | 2024-12-02 01:40:00 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 55.3 |
| c2181389-76b9-34ef-9f12-21eacf9f0545 | -2.2666 | -53.6212 | 2024-12-02 01:40:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 28a31f0a-c78c-3bcd-b328-3d47345e7d9a | -4.9085 | -41.3371 | 2024-12-02 01:40:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 84.4 |
| 1be2d618-71d1-31e3-92b1-88ae54fb3641 | -5.1181 | -43.1964 | 2024-12-02 01:40:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 56.0 |
| 93a8dac1-bc9b-340d-a0d1-24c17712bb0a | -2.8196 | -53.0629 | 2024-12-02 01:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 5123c060-a719-3fce-9db3-b6f6834f17bf | -2.5428 | -53.3935 | 2024-12-02 01:40:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 50.0 |
| 74201fc6-6f13-38a9-aa6c-e95bc3c9a74d | -2.8012 | -53.0633 | 2024-12-02 01:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 54.9 |
| f8edc08d-5885-3640-b114-c93ccaa29bc9 | -2.6348 | -53.3712 | 2024-12-02 01:40:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 75.1 |
| 58d7761f-f4b1-3600-9e34-7e365a9bc6b9 | -2.8013 | -53.043 | 2024-12-02 01:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 63.9 |
| 304c7cba-a7b6-333d-b6b4-111b4b768e0a | -2.8196 | -53.0629 | 2024-12-02 01:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 65.5 |
| dae997fd-fac4-3be8-8b65-5fcaa6097a50 | -6.0674 | -48.0569 | 2024-12-02 01:50:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 74.7 |
| 37576222-978e-3f7b-8ccc-7a53575ce0ca | -4.5932 | -43.3471 | 2024-12-02 01:50:00 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 56.3 |
| 5b98573f-86fb-3f7a-bbb1-dbe35fb1f004 | -2.6348 | -53.3712 | 2024-12-02 01:50:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 70.9 |
| 314ab8a9-5ee3-320d-a9ca-9dd1a3d315da | -2.2666 | -53.6212 | 2024-12-02 01:50:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 70953fe1-39dd-328d-ab89-9b0bccf2a943 | -2.5612 | -53.3931 | 2024-12-02 01:50:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 101.9 |
| 101538f9-c545-398e-8072-296a9eb5ea67 | -2.8197 | -53.0425 | 2024-12-02 01:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 69.8 |
| cc7f612b-11df-34c5-a417-94df1c68fc05 | -2.008 | -54.3091 | 2024-12-02 01:50:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 37.8 |
| 60821841-d929-32e7-bbe9-c8df6f9e9b76 | -5.1367 | -43.2185 | 2024-12-02 01:50:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 41.2 |
| 05681ae2-60de-300e-ab75-7303e2bc18a5 | -3.259 | -53.6388 | 2024-12-02 01:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 73.9 |
| 9797470c-e68c-3a5d-be6f-b68f3e360d82 | -20.7217 | -54.4341 | 2024-12-02 01:50:00 | GOES-16 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 71.9 |
| 68213759-5718-3870-b23e-150fa15d3383 | -1.0735 | -53.4562 | 2024-12-02 01:50:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 55.4 |
| 6fe0a1f6-bf3d-3edd-ac6f-5670b33ee8f0 | -2.5428 | -53.4137 | 2024-12-02 01:50:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 81.8 |
| a91be699-6c71-39d3-8d8c-4a73bc4984cc | -5.118 | -43.2198 | 2024-12-02 01:50:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 60.4 |
| 53a30eeb-b972-33da-a55b-01c3ba14018b | -2.6349 | -53.351 | 2024-12-02 01:50:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 70.9 |
| e6c811e2-aeb6-3111-be73-97cd8bdbddad | -6.0858 | -48.0774 | 2024-12-02 01:50:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 87.1 |
| bb530dfd-0ecd-38c8-bc9f-d7a57f19f19d | -4.267 | -50.8551 | 2024-12-02 01:50:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 47.5 |
| e44930eb-07e6-39d4-b4c2-949284b8d228 | -4.9085 | -41.3371 | 2024-12-02 01:50:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 89.6 |
| 0a6612ad-648b-3e95-bc2d-73dde8bd8326 | 3.3657 | -60.5329 | 2024-12-02 01:50:00 | GOES-16 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 42.8 |
| 811a6043-2ef9-37ee-a232-c040224ec931 | -2.8012 | -53.0633 | 2024-12-02 01:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 51.2 |
| b7e14b3d-ec43-334b-93b5-02040a3a2ab6 | -4.5745 | -43.3483 | 2024-12-02 01:50:00 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 94.5 |
| 862fb211-cbfb-3524-b9ac-495b41c5724a | -6.086 | -48.0557 | 2024-12-02 01:50:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 225.5 |
| c11468f9-ceb4-312f-8748-f34c0ab99195 | 3.3841 | -60.5135 | 2024-12-02 01:50:00 | GOES-16 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 50.6 |


[Clique aqui para ver as próximas entradas](README18.md)
