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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4bb2b4ba-4b54-34bc-856c-badef06b0a0e | -4.9272 | -41.3358 | 2024-12-02 01:50:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 54.4 |
| 55448eaf-0114-3f8f-aef2-a4b02c2e4caf | -5.1181 | -43.1964 | 2024-12-02 01:50:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 62.5 |
| 9ea028fc-4553-3cbb-92b4-e659e589c9ee | -6.0862 | -48.0339 | 2024-12-02 01:50:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 86.5 |
| 598c096f-72cc-3c18-adab-b73ae120d28d | -5.5882 | -45.1412 | 2024-12-02 01:50:00 | GOES-16 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 63.3 |
| bc58219b-3ca6-36f8-ad78-fd6a62e0931b | -2.5612 | -53.4133 | 2024-12-02 01:50:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 104.9 |
| 6e6f0818-a360-3276-b27f-70e1d39bf5d1 | -3.2591 | -53.6186 | 2024-12-02 01:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 105.3 |
| 7a5fda11-4c4a-325d-8bd6-786ffe27bef2 | -3.2774 | -53.6383 | 2024-12-02 01:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 49.9 |
| 84c3c03a-16a8-3ac3-8219-9c75995321a6 | 3.3658 | -60.5139 | 2024-12-02 01:50:00 | GOES-16 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 42.7 |
| 3a3701bb-b8f2-35a4-b474-1d6e502ecbc8 | 3.384 | -60.5325 | 2024-12-02 01:50:00 | GOES-16 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 49.4 |
| 1ec67c7c-92e1-3525-8054-1ba33f441dd9 | -5.1369 | -43.1951 | 2024-12-02 01:50:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 43.7 |
| 4f224538-b44f-3954-9bd2-6b760e8a2716 | -2.0263 | -54.3088 | 2024-12-02 01:50:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 65.1 |
| c794303f-0470-3b55-a56d-6d530e73988e | -20.7148 | -54.4231 | 2024-12-02 01:55:00 | METOP-C | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 93b431c4-28a0-3b12-a482-869e0b0c0be2 | -20.7243 | -54.419998 | 2024-12-02 01:55:00 | METOP-C | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 22e35f2d-ce8a-34a2-bc25-4857c7af6d06 | -20.7304 | -54.441399 | 2024-12-02 01:55:00 | METOP-C | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| b3698bbf-aaa6-3230-842f-933508a19542 | -12.2522 | -63.456699 | 2024-12-02 01:57:00 | METOP-C | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 17519126-e759-34b0-a69e-e302c3ec1758 | -12.4242 | -63.7463 | 2024-12-02 01:57:00 | METOP-C | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| e8402868-f2af-393f-9fa6-21ec298eac17 | -12.4321 | -63.736 | 2024-12-02 01:57:00 | METOP-C | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| b290c978-20e2-3bbb-9125-9b9677973d85 | -12.2542 | -63.464901 | 2024-12-02 01:57:00 | METOP-C | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 4ac44130-ff3b-38dc-9de3-536ea2bc0fae | -12.4223 | -63.7384 | 2024-12-02 01:57:00 | METOP-C | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| cab37bd1-c85a-3fee-9c89-ef1d5cadf2a4 | -12.434 | -63.7439 | 2024-12-02 01:57:00 | METOP-C | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 64a01b8a-4d41-355e-82a8-e2c6d6afc488 | -12.4126 | -63.7407 | 2024-12-02 01:57:00 | METOP-C | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 818b339c-1c13-3771-b674-c240307b7513 | 3.3728 | -60.544201 | 2024-12-02 01:57:00 | METOP-C | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 6c0f8d29-6709-3b1f-8f46-f77a835b33b8 | 3.3825 | -60.546299 | 2024-12-02 01:57:00 | METOP-C | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| bd86e79b-5e27-365b-b9d9-18d41ab41cf4 | -12.4028 | -63.743099 | 2024-12-02 01:57:00 | METOP-C | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 201a1d41-41d1-325d-8166-7cc83665d4ca | 3.3775 | -60.5233 | 2024-12-02 01:57:00 | METOP-C | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 652e7901-b673-35fe-9b82-f1f3d38eec59 | 1.1072 | -55.9874 | 2024-12-02 02:00:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 87714e24-b475-3ea2-a603-fe9035549797 | 3.3657 | -60.5329 | 2024-12-02 02:00:00 | GOES-16 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 47.0 |
| d8c56553-03ed-395d-a95c-5c8546a0f8f0 | -3.4017 | -50.2171 | 2024-12-02 02:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 37.5 |
| d5c07149-49cd-3f04-a4aa-d949a6dcd311 | -3.4201 | -50.2375 | 2024-12-02 02:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 33.8 |
| f016f308-4d4d-39b4-a7bd-92390e284564 | -2.8013 | -53.043 | 2024-12-02 02:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 58.5 |
| a4d8de41-6ccb-3ffc-826c-6bb8eb180cb3 | -6.4477 | -35.0111 | 2024-12-02 02:00:00 | GOES-16 | BAÍA FORMOSA | RIO GRANDE DO NORTE | Brasil | 2401404 | 24 | 33 | nan | nan | nan | Mata Atlântica | 93.0 |
| 0076662f-3dd7-3209-b60d-20aaaaf2d54a | -3.259 | -53.6388 | 2024-12-02 02:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 82.9 |
| 8e68c226-cc1f-3f74-b13c-3768896ee4e6 | 1.1072 | -56.007 | 2024-12-02 02:00:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 354a6e96-058d-3660-9a81-b79109115f07 | 1.1256 | -55.9872 | 2024-12-02 02:00:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 114.0 |
| 8360a281-e340-38dd-80c5-8b8b009cb877 | -4.5745 | -43.3483 | 2024-12-02 02:00:00 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 148.5 |
| 46ea55c8-3897-3a08-84bf-49279cfcdfe6 | -2.5612 | -53.4133 | 2024-12-02 02:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 104.6 |
| 9c92990e-a915-391c-ab49-7c62e92b42ed | -5.5882 | -45.1412 | 2024-12-02 02:00:00 | GOES-16 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 69.1 |
| 45fefaff-dba4-389b-b110-17fa05f9f8e0 | -12.4169 | -63.7465 | 2024-12-02 02:00:00 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 47.8 |
| bea9415c-2a84-37d8-80ed-1befd3c39f0c | -5.118 | -43.2198 | 2024-12-02 02:00:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 72.6 |
| 3de38c2f-0dd9-33f8-92c5-fdd96301e024 | -6.1047 | -48.0544 | 2024-12-02 02:00:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 73.6 |
| c5895000-d3de-342d-8afc-d54f76fe059a | -3.2591 | -53.6186 | 2024-12-02 02:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 97.1 |
| 1bca9db2-c42b-3767-b4b3-0b3f0fcaee4e | 1.1255 | -56.0069 | 2024-12-02 02:00:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 70.1 |
| 48c716c4-b19c-37a9-bdf0-2667a822c75e | -6.086 | -48.0557 | 2024-12-02 02:00:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 233.7 |
| 4117b0f4-e3e7-3b39-8a92-47d707f1adc2 | -6.0858 | -48.0774 | 2024-12-02 02:00:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 760418b2-f5a4-3b68-9a84-f014fda0a5f5 | -2.008 | -54.3091 | 2024-12-02 02:00:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 52.6 |
| 799d3d16-a1ad-385e-a47b-c35506592826 | -3.4017 | -50.2381 | 2024-12-02 02:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 64.3 |
| b635d804-d2b3-331a-92ec-000d23467e1b | -2.0263 | -54.3088 | 2024-12-02 02:00:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 73.2 |
| 79725ba6-a2cd-3e06-8eef-121da180e4ea | -1.0735 | -53.4562 | 2024-12-02 02:00:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 53.7 |
| 6b7f6034-4dd8-330c-bc8f-005e69eb3d86 | -2.8012 | -53.0633 | 2024-12-02 02:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 65728018-e49d-39f4-b01e-c5afb0442498 | -2.8197 | -53.0425 | 2024-12-02 02:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 64.4 |
| aefcc8e0-b480-328e-9829-e8c98bfe4a9f | -2.2666 | -53.6212 | 2024-12-02 02:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 52.4 |
| 82332597-44ca-335f-a869-6fe70df4cb7d | -2.6349 | -53.351 | 2024-12-02 02:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 59.2 |
| 9aeab3f4-00b0-3b2f-bc96-07a1a7267690 | -4.9085 | -41.3371 | 2024-12-02 02:00:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 63.7 |
| b19619ed-76d4-3e66-8c26-e1139b117a02 | -2.8196 | -53.0629 | 2024-12-02 02:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 6b6b4f56-d1c0-36a3-964d-58f5096612be | -4.5743 | -43.3716 | 2024-12-02 02:00:00 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 82.3 |
| 886feae2-ecb0-306a-b095-fbab93cb49b1 | -4.5932 | -43.3471 | 2024-12-02 02:00:00 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 79.8 |
| 36b01221-f6aa-3a2f-8eb6-3a12888b4327 | -20.7217 | -54.4341 | 2024-12-02 02:00:00 | GOES-16 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 73.6 |
| 5ed72ed5-457c-3926-ba6f-6b8fa7620eea | -5.1181 | -43.1964 | 2024-12-02 02:00:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 70.6 |
| ede7d0ae-4812-37b0-83f0-c4521636c089 | -2.5612 | -53.3931 | 2024-12-02 02:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 86.7 |
| 38726d20-3da3-3344-bd13-9721be376e85 | -2.5428 | -53.4137 | 2024-12-02 02:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 70.9 |
| 90b5b84a-8d69-33c4-93dd-5c1e86d4a05c | -2.6348 | -53.3712 | 2024-12-02 02:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 76.8 |
| 486d1048-f409-3a53-a0d7-e9f35148465e | -6.0862 | -48.0339 | 2024-12-02 02:00:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 98.7 |
| e626e32f-f894-355b-917d-cc2022c1242f | 1.1439 | -55.9871 | 2024-12-02 02:00:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 51.8 |
| faecfea9-36f2-33e8-a1d7-6c64074fb1df | -5.1181 | -43.1964 | 2024-12-02 02:10:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 23a66f68-c336-3ae6-802b-60c78534621b | -6.0862 | -48.0339 | 2024-12-02 02:10:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 97.7 |
| b6f976f7-5f05-390a-9837-2c816e175e4e | -2.5612 | -53.3931 | 2024-12-02 02:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 89.4 |
| 033b214d-bf0d-3d6b-b215-6ad67f45136a | 1.1256 | -55.9872 | 2024-12-02 02:10:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 35.8 |
| 19093d36-6671-30bb-a764-e1485af7e007 | 1.1072 | -56.007 | 2024-12-02 02:10:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 35.9 |
| 732d981e-822f-3fce-8172-5aae7630cde9 | -2.6349 | -53.351 | 2024-12-02 02:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 69069c9b-d45b-33e1-92f2-800539c49b00 | -12.4359 | -63.7264 | 2024-12-02 02:10:00 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 58.0 |
| eecc92ad-a5aa-387c-a71a-2dc4bc1a95f9 | -6.0858 | -48.0774 | 2024-12-02 02:10:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 76.2 |
| e4d01c97-2bba-3fff-a306-eaf20c5b05d0 | -1.0735 | -53.4562 | 2024-12-02 02:10:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 48.1 |
| 2d196ffc-457e-35db-9da8-d7dffafbf0a1 | -12.4169 | -63.7465 | 2024-12-02 02:10:00 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 74.6 |
| 6da88b78-da3f-368c-b2ec-200d8c181e74 | -3.2591 | -53.6186 | 2024-12-02 02:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 85.2 |
| 754cada5-2131-3d85-866a-9a62987630ab | -4.5745 | -43.3483 | 2024-12-02 02:10:00 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 90.2 |
| 4066a51e-840e-3699-9a30-44e66fdfc715 | -2.6348 | -53.3712 | 2024-12-02 02:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 70.6 |
| fdd24101-51a8-375a-aa6a-a04bc99581ea | -3.2775 | -53.6181 | 2024-12-02 02:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 47.5 |
| 68ec3cd0-2fd4-3948-83ef-a83d3d3e3f1f | -5.5882 | -45.1412 | 2024-12-02 02:10:00 | GOES-16 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 65.2 |
| b4f507c8-55cb-3cc6-9353-4cc5ac5fb6e2 | -2.5612 | -53.4133 | 2024-12-02 02:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 99.3 |
| 3594fd39-a717-3435-ac19-347a881d3c3c | -4.267 | -50.8551 | 2024-12-02 02:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 49.5 |
| 73e7103d-28fa-36c9-8fa7-59a5e7deebd9 | -3.259 | -53.6388 | 2024-12-02 02:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 69.6 |
| 5f04ddab-7f70-3573-8e70-9b637b1654b7 | -2.8012 | -53.0633 | 2024-12-02 02:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 53.9 |
| c0ebd90a-4024-3250-9974-e2e246a079c9 | -6.086 | -48.0557 | 2024-12-02 02:10:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 232.4 |
| dc1d790a-4d22-39e0-a6a8-a08906fd5f90 | -12.4358 | -63.7455 | 2024-12-02 02:10:00 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 84.5 |
| 7f9f39c2-f6fa-3802-8547-4364946a2ee3 | -5.118 | -43.2198 | 2024-12-02 02:10:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 76.5 |
| d4e004e8-b297-3990-a882-f68c8b22a756 | -2.8197 | -53.0425 | 2024-12-02 02:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 65.8 |
| fcb95e49-125d-3399-ab82-986660cace36 | -2.5428 | -53.4137 | 2024-12-02 02:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 9abcc34c-93c6-3638-bbea-29e7399cd065 | -2.0263 | -54.3088 | 2024-12-02 02:10:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 61.6 |
| 34fd2140-3136-329e-be61-6c947e69ce03 | -12.4171 | -63.7274 | 2024-12-02 02:10:00 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 51.4 |
| bde40bdb-6e32-348a-a71a-e89b6d284633 | -3.4017 | -50.2381 | 2024-12-02 02:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 43.2 |
| 38fabe85-4616-38da-a068-5ea4ee2577b9 | -2.8013 | -53.043 | 2024-12-02 02:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 58.3 |
| dd07229b-1789-3203-a3e2-6b0ee49a0a0e | -2.8196 | -53.0629 | 2024-12-02 02:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 67.6 |
| 320ec6f2-311e-339d-aa48-462bbbd1c540 | -4.5932 | -43.3471 | 2024-12-02 02:10:00 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 79.7 |
| 3f63d1db-699e-39ff-a6e9-154fecb5fdbf | -2.7759 | -55.3509 | 2024-12-02 02:10:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 51.0 |
| c6e7a363-c039-34a3-8d7e-7b01dddfdc36 | -5.5882 | -45.1412 | 2024-12-02 02:20:00 | GOES-16 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 54.8 |
| 46b9e449-b6ad-3308-b284-0c4c19f1e230 | 3.3658 | -60.4949 | 2024-12-02 02:20:00 | GOES-16 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 54.1 |
| 6e05a065-be8e-33a9-8157-da5677149789 | -3.2591 | -53.6186 | 2024-12-02 02:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 96.2 |
| 2fb54b5d-2169-35e6-94b6-a238fba22046 | -1.0735 | -53.4562 | 2024-12-02 02:20:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 49.5 |
| 1babb920-281e-3e28-8f37-7cfcba3accf4 | -2.6348 | -53.3712 | 2024-12-02 02:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 73.4 |
| bfbc246c-a78c-384f-ad61-eaf1c549754a | -12.4359 | -63.7264 | 2024-12-02 02:20:00 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 49.4 |


[Clique aqui para ver as próximas entradas](README19.md)
