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
| fe91a09c-2319-365f-a11d-c0a546bb43c6 | -3.2571 | -45.4485 | 2024-11-23 02:10:00 | GOES-16 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 98.1 |
| b29ab074-4051-374e-b8a8-4b46d3911a95 | -1.6075 | -52.5977 | 2024-11-23 02:10:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 70.7 |
| 45927498-acb2-33b9-963b-f709c66a94af | -4.5898 | -46.5012 | 2024-11-23 02:10:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 50b741f4-242d-3813-9a81-0e7723d49cc9 | -1.7359 | -52.7385 | 2024-11-23 02:10:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 78.3 |
| 95710ce6-bb61-35ac-afe8-13326af6d401 | -4.5402 | -42.93 | 2024-11-23 02:10:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 72.1 |
| 854e9dc5-c1b3-3467-acc7-38c71d33ce02 | -3.2758 | -45.4253 | 2024-11-23 02:10:00 | GOES-16 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 51.6 |
| c2836da9-8e45-3ed9-96ac-e4cba23e47e9 | -4.6085 | -46.5002 | 2024-11-23 02:10:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 139.8 |
| 217368a4-f8d4-3b0f-9889-97c50b095c0d | -3.2569 | -54.2226 | 2024-11-23 02:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 85.1 |
| 936d3c4c-f23d-3c6d-9762-8f969cdce3e0 | -3.1691 | -44.4104 | 2024-11-23 02:10:00 | GOES-16 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 48.5 |
| 9e93fac7-ee18-3467-90f9-4d97bd704885 | -3.2757 | -45.4477 | 2024-11-23 02:10:00 | GOES-16 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 87.2 |
| d4d723d3-090f-318e-b883-c47b02ffa1c9 | -4.5216 | -42.9078 | 2024-11-23 02:10:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 80.4 |
| 9b661c2a-45c1-31b7-a8a8-270aa1fb1d6d | -3.2386 | -54.223 | 2024-11-23 02:10:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 75.2 |
| f69f1674-369d-3dae-b215-f9cd0e5021ed | -3.0882 | -45.791 | 2024-11-23 02:10:00 | GOES-16 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 47.6 |
| 40ad9c74-aba6-3e48-8250-5c4e7fcee88c | -3.2385 | -54.2431 | 2024-11-23 02:10:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 88.7 |
| 02d98e9a-01e7-3041-b477-5ca0215007a1 | -4.5215 | -42.9312 | 2024-11-23 02:10:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 59.0 |
| e2e39ea5-2a75-3cee-91de-61df3504cae2 | -4.5402 | -42.93 | 2024-11-23 02:20:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 75.4 |
| 62fb52de-223e-3447-9883-aef360a7926d | -4.5382 | -45.881 | 2024-11-23 02:20:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 71.0 |
| fccba7ff-7846-3e91-ae30-b20195792c16 | -4.6085 | -46.5002 | 2024-11-23 02:20:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 123.8 |
| bf2d542c-3ffd-3cd2-8d20-1389eaec15ea | -2.7149 | -46.2713 | 2024-11-23 02:20:00 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 51.5 |
| 10110870-5ec0-3e6a-89dc-5a32fe7582b0 | -3.2768 | -53.8199 | 2024-11-23 02:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 66.5 |
| 50a0f990-c6ec-35e8-99a9-551d82e0e09e | -3.1691 | -44.4104 | 2024-11-23 02:20:00 | GOES-16 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 48.9 |
| 4e7b471b-3d84-3c29-9469-c8b88df4912d | -4.5403 | -42.9066 | 2024-11-23 02:20:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 119.1 |
| 6c6d8ec7-83ae-324c-b05e-a9edb1ea206e | -4.6086 | -46.478 | 2024-11-23 02:20:00 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 64.4 |
| 039b6718-bf7a-3f1d-818c-2142b8a54371 | -3.2757 | -45.4477 | 2024-11-23 02:20:00 | GOES-16 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 48.0 |
| 9ab82de5-67f3-371f-b719-6217e85e2a27 | -1.7359 | -52.7181 | 2024-11-23 02:20:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 120.3 |
| e187bdff-a25d-338d-8ab1-a43d54da3134 | -1.7359 | -52.7385 | 2024-11-23 02:20:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 70.3 |
| e776030f-97a8-343e-bea4-538b006ec368 | -4.5216 | -42.9078 | 2024-11-23 02:20:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 62.1 |
| 3636cecd-6255-3e23-8943-30d094ec9412 | -1.7175 | -52.7184 | 2024-11-23 02:20:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 72.1 |
| ba6f905b-04e8-320d-85e3-035dff9b207b | -3.2569 | -54.2226 | 2024-11-23 02:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 57.2 |
| b9f8fb70-d429-3216-aeaf-7bcfaa585789 | -3.2768 | -53.8199 | 2024-11-23 02:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 26917446-ee32-3377-af68-f7f63c268009 | -3.5159 | -53.8132 | 2024-11-23 02:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 3a6920e8-3d31-32a2-8a98-708f00422ea7 | -4.6085 | -46.5002 | 2024-11-23 02:30:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 109.5 |
| 95fd75e0-3f0e-3ad0-95a1-07b4ac293447 | -4.5216 | -42.9078 | 2024-11-23 02:30:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 65.5 |
| 10f95604-dd25-3d5c-aa15-22f3a86971a6 | -1.7175 | -52.7184 | 2024-11-23 02:30:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 71.0 |
| 8e35a7ff-ab43-39f9-a7ab-a570dfb0051b | -3.3319 | -45.3555 | 2024-11-23 02:30:00 | GOES-16 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 49.9 |
| ad471081-efae-3154-a708-d80ebb7215d6 | -4.5403 | -42.9066 | 2024-11-23 02:30:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 121.1 |
| 77fd0062-e591-3f20-bf32-ab2438c2d772 | -4.5402 | -42.93 | 2024-11-23 02:30:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 77.6 |
| d7b96461-67ec-3cea-86b3-33f48bb06483 | -4.5382 | -45.881 | 2024-11-23 02:30:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 71.5 |
| 879d386e-60c1-3c8e-b0a1-b2cabb2a3027 | -1.7359 | -52.7385 | 2024-11-23 02:30:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 81.5 |
| 535d2e72-fb0a-3b96-9ec3-544922daec8e | -1.7359 | -52.7181 | 2024-11-23 02:30:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 133.3 |
| d85e9c87-44c5-394e-bc28-19886c0a1c7a | -4.2605 | -48.697 | 2024-11-23 02:40:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 61.7 |
| ee5f0b87-b368-3fe1-8488-4b4076f3e1b2 | -4.5216 | -42.9078 | 2024-11-23 02:40:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 83.3 |
| b7906d38-87f3-39a4-bb07-3125ba48fd47 | -3.2569 | -54.2426 | 2024-11-23 02:40:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 53.4 |
| ac3e7e63-30cb-3961-b86e-0c01bb784253 | -3.2385 | -54.2431 | 2024-11-23 02:40:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 7ef87b3e-25f8-3a08-927c-665802fe6118 | -1.7359 | -52.7385 | 2024-11-23 02:40:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 88.2 |
| a4fbf96a-7090-3f68-8400-b4c6822b2a25 | -3.2768 | -53.8199 | 2024-11-23 02:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 50.7 |
| b1496d68-ef97-3b5b-8074-b24b6f5aa9f4 | -4.5402 | -42.93 | 2024-11-23 02:40:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 64.5 |
| 96fb9256-3bcd-3f83-8db5-29ba2cf4fd42 | -4.5403 | -42.9066 | 2024-11-23 02:40:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 110.2 |
| 9b42774b-2cc2-3dc0-ae90-1b9f8ffcef7e | -3.2386 | -54.223 | 2024-11-23 02:40:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 64c8fd16-d894-3536-b7f8-7be26850ddaf | -3.3319 | -45.3555 | 2024-11-23 02:40:00 | GOES-16 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 7338395b-005f-30dc-a591-d149ce709338 | -4.6085 | -46.5002 | 2024-11-23 02:40:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 90.8 |
| a375284c-8283-3628-bd32-db832737b366 | -3.2569 | -54.2226 | 2024-11-23 02:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 56.5 |
| e9c6a70b-e100-3cf4-9e57-45bb9afeabd7 | -1.7359 | -52.7181 | 2024-11-23 02:40:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 123.0 |
| 93fca7b2-b82d-3d41-ae23-1d4e16df5015 | -3.5159 | -53.8132 | 2024-11-23 02:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 67.5 |
| a17c0205-9cae-3b5a-b3aa-879275935d59 | -1.7359 | -52.7385 | 2024-11-23 02:50:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 79.1 |
| e8cefa34-e5fc-3947-8dab-e22d48474f36 | -3.2386 | -54.223 | 2024-11-23 02:50:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 57.3 |
| d4adf3b6-dd2f-367c-b9a6-c3a2634f58de | -3.2569 | -54.2226 | 2024-11-23 02:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 57.5 |
| b4bcb945-2e78-3a82-b39d-9b575b04a468 | -4.6085 | -46.5002 | 2024-11-23 02:50:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 153.3 |
| fc3afae9-fd85-3cd4-a6ff-e59fd1024b5f | -4.5403 | -42.9066 | 2024-11-23 02:50:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 104.2 |
| c6cfc548-79df-30da-a292-b0244c78a3d2 | -1.7359 | -52.7181 | 2024-11-23 02:50:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 111.4 |
| 8b823a9d-f140-3f90-89e0-c0765304d439 | -3.2569 | -54.2426 | 2024-11-23 02:50:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 59.3 |
| eb10fd2b-b876-3d3f-a2e2-87def15b6afc | -4.242 | -48.6978 | 2024-11-23 02:50:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 45680c65-7036-3a2c-9da4-2ab3d71c09dc | -3.2385 | -54.2431 | 2024-11-23 02:50:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 64.5 |
| 2d749e67-2eba-35c3-ab3b-01b89a41551b | -4.2605 | -48.697 | 2024-11-23 02:50:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 97.9 |
| a16fd2f9-7135-3233-be20-02bc803dba4f | -4.6271 | -46.4992 | 2024-11-23 02:50:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 72.9 |
| d9142e4a-336e-325d-806e-038edaedb368 | -3.2386 | -54.223 | 2024-11-23 03:00:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 9d134280-e87d-31a5-ac98-ace0bea6cf2b | -3.2569 | -54.2226 | 2024-11-23 03:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 91579338-3e6c-39a6-8cc8-e003fe686b00 | -1.7359 | -52.7181 | 2024-11-23 03:00:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 102.7 |
| 219e4962-9786-3bdb-8062-7214f0c4b8bb | -3.5159 | -53.8132 | 2024-11-23 03:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 55.1 |
| ad23ea75-ac11-3327-bf50-899785966663 | -3.2768 | -53.8199 | 2024-11-23 03:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 50.1 |
| b78dbd8b-240d-3103-af3f-053dd0e5624c | -4.6083 | -46.5223 | 2024-11-23 03:00:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 86.8 |
| 5146da3f-0802-309a-8bee-af17eabf8c01 | -3.2569 | -54.2426 | 2024-11-23 03:00:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 4d663fb3-2934-34ed-adca-a235501bf46d | -1.7175 | -52.7184 | 2024-11-23 03:00:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 77.9 |
| e01f8c56-61c1-37e6-9f10-7b4667ce24cf | -4.6085 | -46.5002 | 2024-11-23 03:00:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 235.3 |
| 15dabc72-963e-3ca3-81f6-54ccba6678ce | -4.6086 | -46.478 | 2024-11-23 03:00:00 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 78.0 |
| 6505a293-3c8f-3f02-aa24-a84ba6852660 | -4.5403 | -42.9066 | 2024-11-23 03:00:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 71.5 |
| 8b284b86-47b8-33fb-b268-5d7437d9afb4 | -3.2385 | -54.2431 | 2024-11-23 03:00:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 70.7 |
| 14adccab-eeec-3fee-8cc1-2d8f6c35b5e8 | -4.5898 | -46.5012 | 2024-11-23 03:10:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 84.9 |
| 7173f0b1-a48d-3bb6-aa18-e50a64f70309 | -4.5403 | -42.9066 | 2024-11-23 03:10:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 73.2 |
| 49aed329-8a71-333f-9371-d856fd916af2 | -4.6086 | -46.478 | 2024-11-23 03:10:00 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 43fd6c6c-7eda-3bba-9b99-62416baa61d8 | -4.6083 | -46.5223 | 2024-11-23 03:10:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 103.3 |
| bbb92961-3aee-3af6-9d0f-54fbc4c2affb | -4.5382 | -45.881 | 2024-11-23 03:10:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 65.6 |
| 7bca2364-c00b-3a01-910d-9f5a3259d1cf | -3.2385 | -54.2431 | 2024-11-23 03:10:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 51.1 |
| 74c04fa8-2757-3895-9bdb-6efd396ab433 | -4.6269 | -46.5213 | 2024-11-23 03:10:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 0920af5c-7486-3696-8294-dd7c8cdb0010 | -1.7359 | -52.7181 | 2024-11-23 03:10:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 118.1 |
| 4f721356-0748-3b2b-b0ee-653b3c66db99 | -4.6085 | -46.5002 | 2024-11-23 03:10:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 308.1 |
| 217475de-e145-3be0-b5b2-21c26fa73132 | -4.6271 | -46.4992 | 2024-11-23 03:10:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 167.4 |
| 757e5887-3226-346d-9e72-1b9d421429d6 | -4.5216 | -42.9078 | 2024-11-23 03:10:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 57.5 |
| 4a26e24a-b3a8-3421-805f-c4b65f797f6b | -3.2768 | -53.8199 | 2024-11-23 03:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 69.6 |
| 0d251384-8a1b-3938-9f9e-60a94dc5f1ff | -1.7359 | -52.7385 | 2024-11-23 03:10:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 85.5 |
| d0238e30-af01-3177-b7dc-55ecd15e0a10 | -3.2768 | -53.8199 | 2024-11-23 03:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 61.8 |
| 1fbb614e-b161-3daa-a03f-b92e73aaa962 | -4.5898 | -46.5012 | 2024-11-23 03:20:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 5a15fd6a-f22d-3ae4-ba5f-ce4e9e17361a | -4.6085 | -46.5002 | 2024-11-23 03:20:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 415.3 |
| 41a7d9ca-e2a0-312c-af77-e94bff5e77b3 | -3.7538 | -50.0152 | 2024-11-23 03:20:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 5809ccfc-44a3-3423-9271-83cb7d3e6dab | -4.6086 | -46.478 | 2024-11-23 03:20:00 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 80.5 |
| 614b240a-35b8-3302-ad27-5b0746779bae | -1.7359 | -52.7181 | 2024-11-23 03:20:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 103.9 |
| c3ef25ac-3328-349d-82db-2d084bc42ee6 | -4.6083 | -46.5223 | 2024-11-23 03:20:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 119.2 |
| 934aad06-69d9-3dd6-bf88-782142ca61ae | -4.6271 | -46.4992 | 2024-11-23 03:20:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 132.6 |
| 584bf98e-6cf7-3e20-b919-43abc0685f1f | -1.7359 | -52.7385 | 2024-11-23 03:20:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 74.0 |
| 92c5947a-d203-357d-a55f-2dd98d457a2e | -4.5403 | -42.9066 | 2024-11-23 03:20:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 68.7 |


[Clique aqui para ver as próximas entradas](README19.md)
