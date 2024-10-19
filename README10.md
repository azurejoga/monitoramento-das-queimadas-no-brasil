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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 70bc9e7e-b5e1-3c7f-8562-a9825266d219 | -4.7061 | -45.8269 | 2024-10-19 01:35:33 | GOES-16 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 210.4 |
| c938ef0a-ba30-3ef6-8061-ce42a8a6fd30 | -4.7246 | -45.8482 | 2024-10-19 01:35:33 | GOES-16 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 79.9 |
| 6ae43d44-ff62-39c0-8fdb-33e6f521efa3 | -4.7248 | -45.8259 | 2024-10-19 01:35:33 | GOES-16 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 67.8 |
| fb7bc27c-a74e-331b-823d-fb6d34d3a980 | -9.053 | -67.4636 | 2024-10-19 01:35:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 85.6 |
| 5f79bee6-a1c7-3c91-ba15-fcc8a94ae440 | -9.053 | -67.4451 | 2024-10-19 01:35:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 78.4 |
| cd384d65-500f-377b-8c3f-abbc26e8f941 | -9.0159 | -67.4645 | 2024-10-19 01:35:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 33.2 |
| b2d77dc2-2b1c-39cd-bde2-ae9c3d462892 | -9.0344 | -67.4826 | 2024-10-19 01:35:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 32.4 |
| c0ec9cec-8093-3b40-b70b-c91d130a5c79 | -9.0344 | -67.4641 | 2024-10-19 01:35:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 169.8 |
| 71b1bff8-5021-395b-b555-4751cf75e92e | -9.0345 | -67.4455 | 2024-10-19 01:35:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 126.8 |
| ebb36396-8b7b-32fc-b01d-04dc3b0d4147 | -12.5147 | -63.3014 | 2024-10-19 01:36:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 89.1 |
| 97c01246-546b-3630-89e0-7091c3eccce9 | -1.1375 | -47.3179 | 2024-10-19 01:45:12 | GOES-16 | PEIXE-BOI | PARÁ | Brasil | 1505601 | 15 | 33 | nan | nan | nan | Amazônia | 51.6 |
| b64f97ce-0a0b-3da2-83eb-f598d4c80341 | -2.8069 | -51.3613 | 2024-10-19 01:45:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 59.7 |
| e91ddd82-6fd0-30c1-9e1e-426ad4123678 | -2.9489 | -52.9174 | 2024-10-19 01:45:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 106.5 |
| 5992d389-4f60-3359-b8d9-6be1fa565664 | -2.9489 | -52.897 | 2024-10-19 01:45:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 69.9 |
| 0a7dd1b8-e6a1-3d97-9651-8fdb8cba98a4 | -2.9674 | -47.9931 | 2024-10-19 01:45:23 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 42.4 |
| 26ac6784-3155-3822-9790-7e24a2e2d56a | -2.9673 | -52.9169 | 2024-10-19 01:45:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 095fceef-2261-3cb9-99c8-43e75679aa1c | -2.9859 | -52.8554 | 2024-10-19 01:45:23 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 71.7 |
| 30da9ee1-dba9-3604-bc40-67c6311274a5 | -3.3044 | -47.198 | 2024-10-19 01:45:25 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 41.6 |
| f07b2ebb-da57-3570-8df9-7064e5a7e8fd | -3.4202 | -50.2164 | 2024-10-19 01:45:25 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 63.8 |
| abba6224-d464-3f69-b3ef-520cf52256d6 | -3.4387 | -50.2158 | 2024-10-19 01:45:25 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 86.5 |
| 70967fce-8d0a-3676-a4c9-ebface397acd | -3.7019 | -45.7212 | 2024-10-19 01:45:27 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 24768205-38be-3c20-86c1-9148a22ea3e6 | -4.6873 | -45.8504 | 2024-10-19 01:45:32 | GOES-16 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 102.1 |
| b8135d05-cf86-3626-8807-0b7daee04813 | -4.6875 | -45.828 | 2024-10-19 01:45:32 | GOES-16 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 91.7 |
| 1bf3f5a5-0983-3c5f-88bd-5f78b397015a | -4.706 | -45.8493 | 2024-10-19 01:45:33 | GOES-16 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 175.3 |
| d8b45e15-2ff1-38a5-b88d-80cd30b083ba | -4.7061 | -45.8269 | 2024-10-19 01:45:33 | GOES-16 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 152.0 |
| 98e63f4f-c77f-3615-b544-c84ffe82d6e4 | -4.7246 | -45.8482 | 2024-10-19 01:45:33 | GOES-16 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 70.7 |
| b3b0ba98-23db-3a55-9b28-b37b7b1b53d8 | -4.7248 | -45.8259 | 2024-10-19 01:45:33 | GOES-16 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 8b0d1efc-b551-3c81-a63e-2f0d44618b42 | -9.0344 | -67.4641 | 2024-10-19 01:45:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 162.4 |
| 339af528-0966-35a2-b2bc-bc9c8a726293 | -9.0345 | -67.4455 | 2024-10-19 01:45:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 108.2 |
| 0238bfb7-b394-34c7-b2bd-1b0df212623b | -9.053 | -67.4636 | 2024-10-19 01:45:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 57.0 |
| f4674954-3736-3e95-9b7d-db6254abd665 | -9.053 | -67.4451 | 2024-10-19 01:45:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 46.9 |
| d8703c99-1dab-3ec3-95ae-6239a5588666 | -11.2854 | -54.2369 | 2024-10-19 01:46:10 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 64.5 |
| a14ba40e-fca4-3080-8782-2f822912ba57 | -12.004 | -63.5199 | 2024-10-19 01:46:15 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 70.9 |
| 8b5c630c-dacd-3cd7-a053-672b54da5112 | -12.0041 | -63.5008 | 2024-10-19 01:46:15 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 73.8 |
| 02be7848-ea21-3476-b3c3-2a0cac360cdd | -12.5147 | -63.3014 | 2024-10-19 01:46:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 79.9 |
| ce3de860-211c-3419-86bc-5487bb772a5e | -2.5635 | -47.0694 | 2024-10-19 01:55:20 | GOES-16 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 67.1 |
| e53fb115-0c7d-3eae-8575-8f171c550a0e | -2.8069 | -51.3613 | 2024-10-19 01:55:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 60.6 |
| a7e85deb-bc94-3fe5-a5ec-46224a8186f5 | -2.9859 | -52.8554 | 2024-10-19 01:55:23 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 3d519c5a-1707-3d72-a1d4-f45c28cc208a | -2.9489 | -52.897 | 2024-10-19 01:55:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 77.5 |
| 09459d7f-5f8d-31be-8864-4b9fa32287ee | -2.9489 | -52.9174 | 2024-10-19 01:55:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 97.8 |
| 6934b6b8-b5c6-32b4-92dd-3c571032d4b8 | -3.4388 | -50.1948 | 2024-10-19 01:55:25 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 52.2 |
| 23eb2683-f079-3d02-aa09-5f27e9df6365 | -3.4387 | -50.2158 | 2024-10-19 01:55:25 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 92.6 |
| dad36550-7b79-3dac-8480-ad0411476f9b | -3.4202 | -50.2164 | 2024-10-19 01:55:25 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 77.9 |
| 253cacee-33c9-31cf-aef4-98e4704a16fb | -3.702 | -45.6988 | 2024-10-19 01:55:27 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 33679e79-2691-3979-b6ea-9c7529b382e5 | -3.7019 | -45.7212 | 2024-10-19 01:55:27 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 100.3 |
| 15e7761b-66fc-3c67-9a57-6af5273d43b7 | -4.7061 | -45.8269 | 2024-10-19 01:55:33 | GOES-16 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 31bea632-5424-312b-8ad9-f304a3d1188f | -4.706 | -45.8493 | 2024-10-19 01:55:33 | GOES-16 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 62.4 |
| 484f91ff-e917-3af5-8877-b22fe721fdbe | -9.053 | -67.4451 | 2024-10-19 01:55:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 45.0 |
| ef6318c7-f2cd-3d2d-a023-cd5faf40ca9f | -9.053 | -67.4636 | 2024-10-19 01:55:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 50.0 |
| a79b4cb4-0b4a-3d14-a420-749a75eb94f1 | -9.0345 | -67.4455 | 2024-10-19 01:55:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 99.3 |
| 99a41ba9-9a31-33dc-a7d6-4dddb10e8e94 | -9.0344 | -67.4641 | 2024-10-19 01:55:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 128.5 |
| 3741863a-c19c-3a29-ad3e-5a33c505de7a | -12.0041 | -63.5008 | 2024-10-19 01:56:15 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 66.1 |
| 7fb95db1-42e7-3994-84fa-677a43197b3b | -12.004 | -63.5199 | 2024-10-19 01:56:15 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 71.6 |
| eb83edd9-ec9e-3b50-a92b-6a43779abd1f | -12.5147 | -63.3014 | 2024-10-19 01:56:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 85.8 |
| b50c2466-6157-35bb-a73e-d7aa4f461cdf | -2.9489 | -52.9174 | 2024-10-19 02:05:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 99.7 |
| 6cc9bd2b-316c-39c7-b06b-f7588d40f382 | -2.9489 | -52.897 | 2024-10-19 02:05:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 64.4 |
| ca727015-79ee-3e5e-9116-7619470d982f | -2.9673 | -52.9169 | 2024-10-19 02:05:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 78.3 |
| 6b320224-d331-3b08-8033-6a848d736ebc | -3.4388 | -50.1948 | 2024-10-19 02:05:25 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 3ce97f7d-15ad-3308-99ce-eb52da0fafd8 | -3.4387 | -50.2158 | 2024-10-19 02:05:25 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 120.9 |
| 5b4f894a-fc54-3624-8435-7a6ebc888c93 | -3.4203 | -50.1954 | 2024-10-19 02:05:25 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 76.6 |
| 9c989b65-9718-32ed-838c-32d1d95dca71 | -3.4202 | -50.2164 | 2024-10-19 02:05:25 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 164.2 |
| fef21fbf-8789-3462-927a-a06e79c93e7d | -3.7117 | -51.1053 | 2024-10-19 02:05:27 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 56.5 |
| be3ce030-59e6-30b8-80df-635b646dd78c | -9.053 | -67.4451 | 2024-10-19 02:05:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 59.9 |
| 5b39c0ee-d4f5-38b1-9e5c-623c345372cf | -9.053 | -67.4636 | 2024-10-19 02:05:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 72.5 |
| 9e6eba00-5c1c-3727-9f4e-f65accf1453a | -9.0345 | -67.4455 | 2024-10-19 02:05:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 89.2 |
| e9b2c07d-a80d-31c5-8a07-a7dff8a4d5d5 | -9.0344 | -67.4641 | 2024-10-19 02:05:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 111.6 |
| e010d900-c2c3-39a4-9c54-6d7fe2d7fb89 | -12.023 | -63.4998 | 2024-10-19 02:06:15 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 5a8c26ca-6c42-3774-9fb9-ed139d669b2a | -12.0228 | -63.5189 | 2024-10-19 02:06:15 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 08e4c2a0-ed96-3012-88ea-6474f886723a | -12.0041 | -63.5008 | 2024-10-19 02:06:15 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 4b6eed28-8974-372c-8578-49c5c35bc487 | -12.004 | -63.5199 | 2024-10-19 02:06:15 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 62.1 |
| 254d6d37-828d-392f-a932-15d3df287ad4 | -12.5147 | -63.3014 | 2024-10-19 02:06:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 85.2 |
| 6fb85620-857f-331e-8817-4ddac028838e | -12.5078 | -63.287201 | 2024-10-19 02:13:52 | METOP-C | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| e3f7d49b-507a-3d43-b71e-44c238d9000b | -12.498 | -63.2897 | 2024-10-19 02:13:52 | METOP-C | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 6753d5c4-db1b-37e6-b1d8-ffe32a096042 | -12.4814 | -63.306198 | 2024-10-19 02:13:53 | METOP-C | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| b83798b5-965c-3282-b60d-da88fb221286 | -12.4843 | -63.317699 | 2024-10-19 02:13:53 | METOP-C | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 3a50d59d-9a15-37f4-8b8d-b1d438bd35e4 | -12.4688 | -63.297199 | 2024-10-19 02:13:53 | METOP-C | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| ff9e25f4-5356-3e8a-a90f-a9f8455ddd18 | -12.4716 | -63.308701 | 2024-10-19 02:13:53 | METOP-C | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 4dfb85ca-17cf-33ee-aedd-96c3e69234cd | -12.4745 | -63.320202 | 2024-10-19 02:13:53 | METOP-C | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 31cc2ed1-a0ed-37c3-bb86-0a104fa96b68 | -12.4591 | -63.299702 | 2024-10-19 02:13:53 | METOP-C | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| f68d2a55-3468-3dbe-8b5e-1433f0c688a6 | -11.9732 | -63.508999 | 2024-10-19 02:14:02 | METOP-C | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 09caa978-e12e-3aac-8d53-59dc600f7a38 | -11.976 | -63.520302 | 2024-10-19 02:14:02 | METOP-C | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| d3027139-570c-31cd-af8b-715d079119ca | -11.9788 | -63.5317 | 2024-10-19 02:14:02 | METOP-C | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 4895092e-23a0-3cb6-a385-ba025c7e5626 | -11.9663 | -63.522701 | 2024-10-19 02:14:02 | METOP-C | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 8bf0ca51-f9dc-3854-bab7-393cc78def86 | -9.3464 | -66.705399 | 2024-10-19 02:14:56 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| bce2c0e1-5d17-3842-8384-1845e9d6e8c0 | -8.8988 | -65.909103 | 2024-10-19 02:15:01 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8ea7ac28-6c9b-36d0-9082-020f5fdf599a | -9.0057 | -67.4505 | 2024-10-19 02:15:05 | METOP-C | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3ada3bad-e98c-31a2-a305-5ecaf3e59e90 | -9.0075 | -67.458099 | 2024-10-19 02:15:05 | METOP-C | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| fc8d1e13-8c41-3775-8233-38cf4f28c537 | -9.0093 | -67.465698 | 2024-10-19 02:15:05 | METOP-C | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0b46282e-a4da-38aa-8122-34b8dd98eef9 | -9.011 | -67.473297 | 2024-10-19 02:15:05 | METOP-C | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 36d5023b-2e40-30fb-9b86-77ba0f4a5332 | -8.9959 | -67.452797 | 2024-10-19 02:15:05 | METOP-C | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 578af60f-b408-3d85-9387-9826b4629abb | -8.9977 | -67.460403 | 2024-10-19 02:15:05 | METOP-C | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b1b7b82e-1fc6-3bbd-a1dd-da721c7c3d9f | -8.9995 | -67.468002 | 2024-10-19 02:15:05 | METOP-C | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8b68230b-d959-3a61-8b7f-aefb3078b16c | -9.0012 | -67.475601 | 2024-10-19 02:15:05 | METOP-C | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 23a5f55c-ae90-3d3b-a7c7-12e75fd13384 | -8.9287 | -67.739197 | 2024-10-19 02:15:07 | METOP-C | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| de62fdc3-1323-3535-bc85-8d34d6c2a7cc | -8.5193 | -69.990303 | 2024-10-19 02:15:22 | METOP-C | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 34a95d44-74d8-3f35-b582-3b56642ef1aa | -8.5208 | -69.9972 | 2024-10-19 02:15:22 | METOP-C | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| cc65f6ea-7419-3181-bdb3-f0456395f560 | -2.9489 | -52.9174 | 2024-10-19 02:15:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 98.2 |
| 2974446c-8289-30ec-a436-72a343686110 | -2.9489 | -52.897 | 2024-10-19 02:15:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 76.3 |
| dd1b1e31-e663-32c1-ba39-c5805e0ba8ab | -2.9673 | -52.9169 | 2024-10-19 02:15:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 64.4 |
| d3a8b268-03a3-3008-94ab-aa95270f3c82 | -3.2256 | -44.2938 | 2024-10-19 02:15:24 | GOES-16 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 85.2 |


[Clique aqui para ver as próximas entradas](README11.md)
