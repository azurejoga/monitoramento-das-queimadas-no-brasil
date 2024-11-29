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

## Dados Diários - Página 111

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 86258312-c315-32d8-8d1b-3365c49484bf | -6.3687 | -45.6709 | 2024-11-29 13:30:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 72.6 |
| 8a3973dd-d4b7-3fe6-b1b3-a254135d6eaf | -8.3108 | -44.951 | 2024-11-29 13:30:00 | GOES-16 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 117.6 |
| 02a6d3ce-6b2f-3b87-9bb8-74f964304951 | -2.4662 | -48.4391 | 2024-11-29 13:30:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 69.7 |
| fb59fc86-c01e-3681-9146-0fe46a565487 | -6.9422 | -42.8362 | 2024-11-29 13:30:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 166.2 |
| d6be8821-f6e3-3c37-b776-14676efc3fdd | -2.6499 | -48.7772 | 2024-11-29 13:30:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 101.4 |
| bb8a9129-646c-3a89-91bf-0ea46f850f67 | -6.9613 | -42.8108 | 2024-11-29 13:30:00 | GOES-16 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 86.5 |
| 55a8ed50-f05f-3622-9247-065f3ed1ce75 | -2.6684 | -48.7767 | 2024-11-29 13:30:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 76.8 |
| 2846bfb8-5c8b-3bb2-a1f3-c96e7b8f46d6 | 1.6476 | -50.929 | 2024-11-29 13:30:00 | GOES-16 | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 130.7 |
| e0471aef-452e-330f-90e4-d707e3e2fac2 | 1.2171 | -55.9471 | 2024-11-29 13:30:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 68.8 |
| f670e871-d3c2-3b49-a1c8-3ded95618256 | -4.2341 | -46.8947 | 2024-11-29 13:30:00 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 101.0 |
| 5b779ae1-f94b-3b36-b064-76836944a9bc | -3.6943 | -47.1168 | 2024-11-29 13:30:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 73.7 |
| f6941c2c-dbe2-3ae0-9033-9f4a20705fc9 | -3.4532 | -43.5243 | 2024-11-29 13:30:00 | GOES-16 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 78.0 |
| 7b8472f5-3202-3956-b741-b7fc2b980a00 | -3.0311 | -42.1604 | 2024-11-29 13:30:00 | GOES-16 | ÁGUA DOCE DO MARANHÃO | MARANHÃO | Brasil | 2100154 | 21 | 33 | nan | nan | nan | Cerrado | 82.7 |
| e429af38-3170-3784-8f4a-baa5fc511742 | -2.6498 | -48.7986 | 2024-11-29 13:30:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 151.2 |
| 80d145a9-f368-3fba-9b09-ff0e7c4d6fbc | -3.273 | -42.3391 | 2024-11-29 13:30:00 | GOES-16 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 81.2 |
| 5107d87a-f5d8-3c21-bb14-b9554606c042 | -3.0489 | -42.3254 | 2024-11-29 13:30:00 | GOES-16 | TUTÓIA | MARANHÃO | Brasil | 2112506 | 21 | 33 | nan | nan | nan | Cerrado | 89.4 |
| 747ca7d0-1dd5-319b-8e2c-23fbe84439d2 | -3.7129 | -47.116 | 2024-11-29 13:30:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 70.3 |
| 11360abf-1cea-30f1-908a-3098545f8f07 | -2.6683 | -48.7981 | 2024-11-29 13:30:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 105.3 |
| 2b683a4b-b75e-3126-94db-4dcb7280761f | -1.5869 | -53.8336 | 2024-11-29 13:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 66.4 |
| 3ecdf8e2-aa95-333f-9dea-8a93a13ed56c | -4.1761 | -44.2716 | 2024-11-29 13:30:00 | GOES-16 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 113.7 |
| 78558005-1f83-377f-accd-062c417ab8d1 | -2.966 | -53.2824 | 2024-11-29 13:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 90.4 |
| 92edd7f5-4899-33e0-a8a6-34711a73aaf5 | -2.8425 | -46.8193 | 2024-11-29 13:30:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 116.6 |
| f85d80cf-9758-31e5-8874-d0e457c15d3b | -3.7128 | -47.1379 | 2024-11-29 13:30:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 74.6 |
| 91b52ed0-d087-3ba0-af0a-eb01eb58cfae | -2.0439 | -54.6883 | 2024-11-29 13:30:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 64.6 |
| aec090c9-4ce3-3796-9fe6-deaebdac40fe | -2.966 | -53.3027 | 2024-11-29 13:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 66.4 |
| 4386f678-d348-35c0-969a-03d0046db80a | -4.2342 | -46.8726 | 2024-11-29 13:30:00 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 115.1 |
| 4179bad6-f340-3e63-b6af-cd79bea03980 | -3.6584 | -40.4203 | 2024-11-29 13:30:00 | GOES-16 | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 118.6 |
| 6b73874c-3166-3562-993a-dcfc1b8cab49 | -5.0586 | -43.6193 | 2024-11-29 13:30:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 83.6 |
| 147e94a8-52d7-3d7f-8b70-c8cf08feef37 | -1.6419 | -53.8731 | 2024-11-29 13:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 7f3ba0d0-0e58-3122-b90c-dab3058789ed | -2.0439 | -54.6683 | 2024-11-29 13:30:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 63.8 |
| 236c43d1-c0a8-3a7c-b492-bc872efa03f2 | -10.1857 | -42.4771 | 2024-11-29 13:30:00 | GOES-16 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 127.3 |
| a04b0bfe-c8f7-369f-a19b-93b6e5d1f432 | -2.9844 | -53.2819 | 2024-11-29 13:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 124.5 |
| 5e29227d-3e73-3019-a411-cb08a18d8d71 | -2.8611 | -46.8186 | 2024-11-29 13:40:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 143.8 |
| 57d498c5-2671-343e-9fdf-fcdbb642206a | -6.9422 | -42.8362 | 2024-11-29 13:40:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 179.7 |
| a19d9312-12b7-39b3-b823-d3e378c821f9 | -2.8795 | -46.84 | 2024-11-29 13:40:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 105.2 |
| 3bdcb873-6b03-38d8-8404-6de7cc6187ac | 1.2171 | -55.9471 | 2024-11-29 13:40:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 67.2 |
| e4d9a66f-04dc-3934-8197-81b82659e33e | -2.0439 | -54.6683 | 2024-11-29 13:40:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 66.4 |
| 7610c4c2-996f-3e76-b3d9-c1b9000eac72 | -2.4662 | -48.4391 | 2024-11-29 13:40:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 65.9 |
| 7d8b1451-723b-325d-a88d-c64669b77218 | -11.4018 | -45.0746 | 2024-11-29 13:40:00 | GOES-16 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 109.3 |
| 4ae7991d-1bac-34fd-8bc1-ed404b53d621 | -4.1574 | -44.2726 | 2024-11-29 13:40:00 | GOES-16 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 159.3 |
| 3525b229-ae49-3017-96c1-d3a1bccb3c04 | -3.7128 | -47.1379 | 2024-11-29 13:40:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 126.0 |
| 60f890c5-06a2-3800-97f1-d96834f9dcd6 | -6.9613 | -42.8108 | 2024-11-29 13:40:00 | GOES-16 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 73.5 |
| d5028bd9-bb32-3a54-82bf-643555c3ebe4 | -5.4546 | -43.2659 | 2024-11-29 13:40:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 100.3 |
| 5253e6db-f749-32c7-83ec-fe9da286d7da | -2.6499 | -48.7772 | 2024-11-29 13:40:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 74.9 |
| 8dc6d4b8-31d0-32cb-b1b2-732bc6105be7 | -6.3685 | -45.6934 | 2024-11-29 13:40:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 58.9 |
| fc2ea62f-dbae-3de8-8c51-12f7c7508f4c | -4.1761 | -44.2716 | 2024-11-29 13:40:00 | GOES-16 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 159.8 |
| 7d0a0e0e-37b0-3e70-bf2a-22d16691898d | -6.7782 | -44.0876 | 2024-11-29 13:40:00 | GOES-16 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 66.3 |
| 58cfcd6d-5b14-3a19-b76f-87e142946590 | -3.5858 | -50.3577 | 2024-11-29 13:40:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 71.4 |
| 702f8e89-495e-39d1-a532-6ebf2c0aa5cb | -2.8851 | -45.5073 | 2024-11-29 13:40:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 73.9 |
| 525d6706-e096-33ce-8870-6880aed7e0f5 | -4.2342 | -46.8726 | 2024-11-29 13:40:00 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 73.9 |
| cf69328a-54d5-3259-93dc-74c26a855458 | -10.1857 | -42.4771 | 2024-11-29 13:40:00 | GOES-16 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 98.1 |
| 40ebc2e0-63cd-3293-974c-71f5a5dae14d | -3.7129 | -47.116 | 2024-11-29 13:40:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 87.5 |
| c1ddcab4-3c2d-35ee-93ab-2d78d7374f31 | -1.6235 | -53.8733 | 2024-11-29 13:40:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 21fad4ac-2aa0-38e8-be76-b19277e24b9e | -2.8425 | -46.8193 | 2024-11-29 13:40:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 109.9 |
| b804d7cc-0207-366a-b081-59f3adb608e5 | -2.6683 | -48.7981 | 2024-11-29 13:40:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 186.6 |
| 78263268-8b76-3299-9927-cfaf2a9ff610 | -3.6943 | -47.1168 | 2024-11-29 13:40:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 98.1 |
| ea7a5f82-084b-34e3-8ee2-d64303783b65 | -0.3586 | -51.542 | 2024-11-29 13:40:00 | GOES-16 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 82.4 |
| 1f04bb45-8e3c-3ac9-a9e7-2079b2f7a457 | 1.4552 | -55.9053 | 2024-11-29 13:40:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 96.3 |
| ce4d57cb-ac12-39d0-8ca1-674a575ae098 | -3.6027 | -40.3254 | 2024-11-29 13:40:00 | GOES-16 | MASSAPÊ | CEARÁ | Brasil | 2308005 | 23 | 33 | nan | nan | nan | Caatinga | 107.0 |
| ba704fa3-7641-3cd7-9dd9-85dc8454f4e4 | -2.966 | -53.2824 | 2024-11-29 13:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 74.4 |
| 7bf18a51-eb99-3b92-a75a-713e31430897 | -3.2396 | -53.9216 | 2024-11-29 13:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 71.0 |
| 290366d4-82c8-3932-9849-dffa506d8d29 | -11.4014 | -45.0977 | 2024-11-29 13:40:00 | GOES-16 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 139.0 |
| edc0d2f4-14a5-312d-ba8c-2656fb2bc2ac | -1.5869 | -53.8336 | 2024-11-29 13:40:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 74.1 |
| eb924bb2-7fa5-3a1b-acf8-23e8135993ba | -4.0546 | -49.0698 | 2024-11-29 13:40:00 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 81.7 |
| a6212c33-2c1e-33e7-83fa-48cace498726 | -2.6684 | -48.7767 | 2024-11-29 13:40:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 127.3 |
| 607eca82-7701-3817-b2dc-6ff5cbc7dfc0 | -6.3687 | -45.6709 | 2024-11-29 13:40:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 76.7 |
| 4bda1dc0-f601-3872-bf10-d52b2695bbc7 | -2.6498 | -48.7986 | 2024-11-29 13:40:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 110.0 |
| 2e7bc366-cfba-3c49-a2be-966f90d3467c | -2.9399 | -45.7293 | 2024-11-29 13:40:00 | GOES-16 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 79.8 |
| 9bf5a87c-9c77-37ae-9b8d-de917a08dacb | -2.0439 | -54.6883 | 2024-11-29 13:40:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 15690371-80c3-330e-b5e9-da043012193e | -3.996 | -46.3094 | 2024-11-29 13:40:00 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 70.6 |
| e511e169-4127-3fdd-8453-b733f3b0d7e6 | -1.5667 | -45.6773 | 2024-11-29 13:40:00 | GOES-16 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 72.7 |
| a53dace3-b6cb-3306-bd83-85c5ee3e9a0a | -3.0311 | -42.1604 | 2024-11-29 13:40:00 | GOES-16 | ÁGUA DOCE DO MARANHÃO | MARANHÃO | Brasil | 2100154 | 21 | 33 | nan | nan | nan | Cerrado | 89.0 |
| 1ab42cc4-6bab-3d64-b77f-4221323b8872 | -8.3108 | -44.951 | 2024-11-29 13:40:00 | GOES-16 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 92.8 |
| 2f6b945c-6e7c-3e9c-a4e3-5b5406546b55 | -3.6584 | -40.4203 | 2024-11-29 13:40:00 | GOES-16 | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 93.0 |
| f46983a7-7390-3e1b-9be6-8f00bff979f8 | -1.7507 | -46.2523 | 2024-11-29 13:40:00 | GOES-16 | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | 88.6 |
| 0c07d456-f29a-329f-a7c9-7aea77ba047a | -3.0673 | -42.3955 | 2024-11-29 13:40:00 | GOES-16 | TUTÓIA | MARANHÃO | Brasil | 2112506 | 21 | 33 | nan | nan | nan | Cerrado | 98.9 |
| 28fdebe4-060b-31af-85bc-aaae74b2b15e | -2.6498 | -48.7986 | 2024-11-29 13:50:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 166.7 |
| 5dd8718d-e69d-32bc-91ae-37a0a40fa5b7 | -1.7507 | -46.2523 | 2024-11-29 13:50:00 | GOES-16 | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | 228.9 |
| 9fa35c0d-422e-3ed7-80a4-37d7a9f54933 | -2.8611 | -46.8186 | 2024-11-29 13:50:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 141.7 |
| 3dd8920b-5606-34ce-817b-2fdafa2ef3c5 | -5.0401 | -43.5973 | 2024-11-29 13:50:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 80.9 |
| 0286c3c8-39b8-3695-8936-4b9ad42b3f76 | -11.4014 | -45.0977 | 2024-11-29 13:50:00 | GOES-16 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 144.5 |
| 85796a6c-cd32-306c-985a-23ac197d94cc | -2.3059 | -46.5488 | 2024-11-29 13:50:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 88.4 |
| 1831b778-a08e-3207-a5f1-bb229d147af9 | -8.3108 | -44.951 | 2024-11-29 13:50:00 | GOES-16 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 125.8 |
| f0f6a8af-378e-3a1d-85a9-087fde37b7bb | -3.0673 | -42.3955 | 2024-11-29 13:50:00 | GOES-16 | TUTÓIA | MARANHÃO | Brasil | 2112506 | 21 | 33 | nan | nan | nan | Cerrado | 83.5 |
| cc52545a-4f5a-3944-ab06-69bb3f7cb818 | -2.8424 | -46.8413 | 2024-11-29 13:50:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 84.8 |
| d961f0f3-ab93-3bd5-8eab-bc7a279314d5 | -2.8795 | -46.84 | 2024-11-29 13:50:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 96.3 |
| 3edb1b9f-3b71-34cf-9f47-91546f1f7b03 | -2.4662 | -48.4391 | 2024-11-29 13:50:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 69.9 |
| c25a1d65-01cc-3ab8-8516-bcc502222a6f | -4.1574 | -44.2726 | 2024-11-29 13:50:00 | GOES-16 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 98.3 |
| d36893d7-f913-3818-8160-af4c6ced3482 | -3.6943 | -47.1168 | 2024-11-29 13:50:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 94.4 |
| ca3615ae-7cf2-3b6b-8d53-657264457687 | -2.0439 | -54.6683 | 2024-11-29 13:50:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 65.0 |
| aa3bed63-861f-3e91-bd9b-43a4d636446f | -8.2737 | -48.0364 | 2024-11-29 13:50:00 | GOES-16 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 111.0 |
| fe96764b-1193-3d32-8b15-7c01cb2f1eef | -17.5688 | -57.4529 | 2024-11-29 13:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 85.0 |
| 7ee4089f-e5dc-3604-bebd-de1574a78a54 | -3.2396 | -53.9216 | 2024-11-29 13:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 74.0 |
| 744b5af3-ce92-3ab9-9b84-3e7504fb08b8 | -17.2824 | -58.1813 | 2024-11-29 13:50:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 85.1 |
| c389de29-010e-33e0-aac4-04ee807173c4 | 1.2171 | -55.9471 | 2024-11-29 13:50:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 66415a57-a073-3b49-8108-6789006911c5 | -3.6584 | -40.4203 | 2024-11-29 13:50:00 | GOES-16 | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 98.1 |
| e91ee8d9-183d-3cee-91cd-3f1a29dff412 | -3.1787 | -46.2995 | 2024-11-29 13:50:00 | GOES-16 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 68.2 |
| 727a635e-d486-34ee-be38-165d6c25a676 | -2.3419 | -46.8562 | 2024-11-29 13:50:00 | GOES-16 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 84.7 |
| e5792972-c270-3ba7-8484-363eda2ff5a1 | -3.7129 | -47.116 | 2024-11-29 13:50:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 93.2 |
| cc52c9e7-3094-3c12-9f07-4e6b579a1554 | -2.6684 | -48.7767 | 2024-11-29 13:50:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 82.6 |


[Clique aqui para ver as próximas entradas](README112.md)
