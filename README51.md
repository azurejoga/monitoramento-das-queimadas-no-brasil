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

## Dados Diários - Página 51

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6a04aa68-fb8b-34f1-aa3d-ef95b8a5ae47 | -0.89534 | -47.54795 | 2025-10-15 06:03:00 | AQUA_M-M | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 27.7 |
| c838bf3f-2042-391d-9bc9-efc13c1d1562 | -5.00738 | -44.4903 | 2025-10-15 06:03:00 | AQUA_M-M | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 982ec04d-4f17-3c0a-9776-6b65403abb76 | -3.83156 | -44.54123 | 2025-10-15 06:03:00 | AQUA_M-M | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 0b8df98d-115f-3cf9-9e63-786e02e96d79 | -4.76853 | -45.72936 | 2025-10-15 06:03:00 | AQUA_M-M | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 02c3a049-6563-38e7-aeae-84a7b681fcb2 | -5.5761 | -44.74243 | 2025-10-15 06:03:00 | AQUA_M-M | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| da8ccd43-de91-34f3-91f2-d833b847c2bc | -4.89183 | -43.46274 | 2025-10-15 06:03:00 | AQUA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 102.6 |
| fa562dac-8945-3bff-af0a-09f92f492dab | -3.05562 | -44.45886 | 2025-10-15 06:03:00 | AQUA_M-M | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 13.1 |
| cf66ae37-bef3-3847-8ea9-8b959547752b | -3.57427 | -49.43713 | 2025-10-15 06:03:00 | AQUA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| c4832dd8-6ad3-3b8d-b176-ef4fd340ba53 | -6.0493 | -41.89191 | 2025-10-15 06:03:00 | AQUA_M-M | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 20.6 |
| 63e1862c-87d9-3f7e-af47-2a0bc4242ca1 | -5.43744 | -44.21265 | 2025-10-15 06:03:00 | AQUA_M-M | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 41.9 |
| af5e8989-de31-3056-9fba-08967ac6d811 | -4.27855 | -48.58185 | 2025-10-15 06:03:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 6728c716-fe9a-3110-bd5f-1a816d72e06f | -2.80091 | -48.93796 | 2025-10-15 06:03:00 | AQUA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 3b3ed7ed-8341-331c-bf47-7718a7ee6bf4 | -4.36631 | -46.77198 | 2025-10-15 06:03:00 | AQUA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 14515ea0-9c09-3ebc-8d08-157fbba0a8cd | -4.4218 | -47.75484 | 2025-10-15 06:03:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| bdf8be36-02cb-3b37-aace-80938521ba7f | -4.66568 | -43.11562 | 2025-10-15 06:03:00 | AQUA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 57.2 |
| 25c9702a-d42b-3f3b-b0a8-742adb1709a2 | -4.90892 | -43.44422 | 2025-10-15 06:03:00 | AQUA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 1a00bcac-42f2-3076-bb8b-cf588a5058c6 | -4.90261 | -43.46427 | 2025-10-15 06:03:00 | AQUA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 344.7 |
| 34a8b7d2-fe96-3027-9ab7-bad8b31a6ca2 | -4.90459 | -43.45078 | 2025-10-15 06:03:00 | AQUA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 379.2 |
| 2c334c4d-12d6-32e7-87bc-2bfd9db2620d | -2.81573 | -49.19962 | 2025-10-15 06:03:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 6eb23ee6-4b85-31ad-9663-46bd3c84ef6f | -3.83225 | -44.54795 | 2025-10-15 06:03:00 | AQUA_M-M | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| bf816f8a-5bb9-3848-84c7-765adba0ea40 | -3.53008 | -44.01987 | 2025-10-15 06:03:00 | AQUA_M-M | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 18.2 |
| a73b04d3-5112-30f1-a21a-ea350050b115 | -4.42312 | -47.74611 | 2025-10-15 06:03:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| be21951c-2b3c-31c0-bdf5-3e0e12cb0acf | -4.76711 | -45.73918 | 2025-10-15 06:03:00 | AQUA_M-M | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 51578ab9-429c-34a6-a1a9-1b06fd812d1f | -3.5397 | -44.0159 | 2025-10-15 06:03:00 | AQUA_M-M | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 6b093845-7a1e-3b3b-b823-1b19eef7f9b5 | -5.33904 | -43.7397 | 2025-10-15 06:03:00 | AQUA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 15.4 |
| d0225a98-2987-38a9-841e-8955911983c0 | -3.42554 | -50.24189 | 2025-10-15 06:03:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 33d7cec1-585d-33a1-9ffe-1fd42202f58e | -4.11254 | -48.02236 | 2025-10-15 06:03:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 41f48415-f62f-36a8-96d8-1f6963bf6b1a | -4.90514 | -43.47133 | 2025-10-15 06:03:00 | AQUA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 30.8 |
| b202a5f0-51d8-334f-a405-fd01e952d26e | -3.98303 | -45.48894 | 2025-10-15 06:03:00 | AQUA_M-M | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 8.1 |
| f800c0a0-4cec-3449-aa44-c18a1f9f07ea | -4.91229 | -46.70533 | 2025-10-15 06:03:00 | AQUA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 27e1908b-ac1e-3d05-88d1-a198ea5560e1 | -2.24093 | -47.87495 | 2025-10-15 06:03:00 | AQUA_M-M | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| f6d2b314-48d0-3588-b7e4-3344e0f40c00 | -5.43564 | -44.22493 | 2025-10-15 06:03:00 | AQUA_M-M | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 85.3 |
| 5dd5f2a2-9728-3160-88c6-27c18a73774d | -4.89379 | -43.44929 | 2025-10-15 06:03:00 | AQUA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 224.4 |
| d7f25283-53cd-3618-a948-603c6ca61314 | -0.90417 | -47.54924 | 2025-10-15 06:03:00 | AQUA_M-M | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 5ea6ff4d-9c55-3683-a7a0-4cb07acb3926 | -2.24226 | -47.86613 | 2025-10-15 06:03:00 | AQUA_M-M | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 90d9f606-0700-3653-880a-9dd0ad9f7a4c | -3.07562 | -49.50584 | 2025-10-15 06:03:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| fdeb74dc-2a49-334f-985c-1f2b2b979ab7 | -0.89668 | -47.53913 | 2025-10-15 06:03:00 | AQUA_M-M | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 18.1 |
| a807e7a6-9ab8-368a-9b3c-4262ff8dbd83 | -4.35558 | -48.19344 | 2025-10-15 06:03:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 34388e58-b89c-397c-95ee-ca349eaa768c | -4.66361 | -43.12986 | 2025-10-15 06:03:00 | AQUA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 25.6 |
| 0cc5677b-b42b-3503-b56c-648d7a28eeb4 | -4.65259 | -43.1283 | 2025-10-15 06:03:00 | AQUA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 74.8 |
| b118c835-9d12-39e7-917a-5fbb059f97d3 | -4.65465 | -43.11406 | 2025-10-15 06:03:00 | AQUA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 83.7 |
| 204f4de9-d847-3b4c-aa1a-f935e63b27ff | -4.90702 | -43.45786 | 2025-10-15 06:03:00 | AQUA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 169.4 |
| 33ba7579-0d88-3bde-9baf-6c2028dd1599 | -2.95217 | -49.33138 | 2025-10-15 06:03:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 80c625dd-fcd7-3351-9098-d309d745f8ca | -2.92392 | -48.30708 | 2025-10-15 06:03:00 | AQUA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 893f818d-76a7-38d8-a4bc-dea3259eafa4 | -2.81426 | -49.20927 | 2025-10-15 06:03:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 22.9 |
| f85f7683-7a34-3a6d-b295-de7c2baf5c74 | -5.42716 | -44.21128 | 2025-10-15 06:03:00 | AQUA_M-M | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 24.8 |
| 471d0f1c-68d3-3bf0-89c6-94535ed7f9b2 | -3.42391 | -50.25266 | 2025-10-15 06:03:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 4449357c-5f92-3986-bf1f-482944b15b9f | -3.83384 | -44.5369 | 2025-10-15 06:03:00 | AQUA_M-M | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| c77aedc8-2039-3599-bf44-254693632cc0 | -5.42536 | -44.22359 | 2025-10-15 06:03:00 | AQUA_M-M | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 57.6 |
| d02451b9-6cad-3a53-823b-01ad3270b5f3 | -2.87985 | -50.73535 | 2025-10-15 06:03:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 683c7f00-8800-3158-aa00-bba75478bb1b | -2.92528 | -48.29811 | 2025-10-15 06:03:00 | AQUA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 39.3 |
| 5a29a6a9-11eb-32ff-8440-bb21d52e26fa | -7.93988 | -44.13314 | 2025-10-15 06:05:00 | AQUA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 24.2 |
| 29f783ac-eff2-3bd1-82f6-6a20ae709939 | -6.05285 | -41.88054 | 2025-10-15 06:05:00 | AQUA_M-M | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 16.2 |
| 6597e261-099a-3094-b41c-7654c295dde1 | -7.94798 | -44.12732 | 2025-10-15 06:05:00 | AQUA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 19.2 |
| 055adf10-a312-3df9-9d6b-d1c515faf879 | -8.21733 | -44.01498 | 2025-10-15 06:05:00 | AQUA_M-M | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 274.4 |
| eedc7ad8-b345-346a-800b-1a9386909871 | -5.77153 | -46.01044 | 2025-10-15 06:05:00 | AQUA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 147.0 |
| be4ae73a-0372-3c0a-8492-c11d8b809b2c | -5.76231 | -46.00904 | 2025-10-15 06:05:00 | AQUA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 8c689939-9b01-3b6d-9bec-c74834eeb525 | -8.22711 | -44.05045 | 2025-10-15 06:05:00 | AQUA_M-M | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 59.0 |
| 0a1c81bd-930f-3b83-808d-7b46242b5f50 | -8.2193 | -44.00103 | 2025-10-15 06:05:00 | AQUA_M-M | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 22.9 |
| 0edd476a-7577-3b1d-ab60-701697bc6f0b | -8.21341 | -44.04284 | 2025-10-15 06:05:00 | AQUA_M-M | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 68.9 |
| 27858a81-f19d-3775-a0ed-0356bde05b97 | -6.55226 | -43.92393 | 2025-10-15 06:05:00 | AQUA_M-M | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 323fb49f-1a99-3d34-86e5-cc7e229cff8c | -8.22428 | -44.04441 | 2025-10-15 06:05:00 | AQUA_M-M | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 111.1 |
| 3ed11df5-83c9-3288-a31a-fb7cc4a9f750 | -8.22899 | -44.0365 | 2025-10-15 06:05:00 | AQUA_M-M | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 05198b8f-9b16-3686-9e05-08fc98812136 | -8.22626 | -44.03047 | 2025-10-15 06:05:00 | AQUA_M-M | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 23.9 |
| 9b640194-3e1a-382d-be7a-e233087dafa6 | -8.20839 | -43.99946 | 2025-10-15 06:05:00 | AQUA_M-M | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 23.5 |
| 37ebf709-bb4a-3598-9ea6-1065aa77fc1a | -8.18086 | -44.03758 | 2025-10-15 06:05:00 | AQUA_M-M | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 0f84e811-0620-3af6-8bae-db8473359efb | -5.88604 | -43.73935 | 2025-10-15 06:05:00 | AQUA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 14.7 |
| cca1d2ee-a006-3ae4-81c8-81dc1c426bf9 | -6.84634 | -44.37106 | 2025-10-15 06:05:00 | AQUA_M-M | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 947b185f-8ba1-3e58-91c1-f3ec5426eb38 | -5.76373 | -45.99932 | 2025-10-15 06:05:00 | AQUA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| e5e0b461-b539-3bfc-a0a2-de8608afcfa4 | -8.19042 | -43.96835 | 2025-10-15 06:05:00 | AQUA_M-M | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 17.3 |
| c1b65fbd-a849-3e33-aba3-b49ee91011b0 | -8.24172 | -43.33744 | 2025-10-15 06:05:00 | AQUA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 10.5 |
| 5cbd9933-aacd-3c7b-964c-7c1e3a00be36 | -5.77295 | -46.00069 | 2025-10-15 06:05:00 | AQUA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 68.6 |
| 2b150665-bb92-3e65-8f3d-9530f25d8d48 | -8.45762 | -44.19292 | 2025-10-15 06:05:00 | AQUA_M-M | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 36.2 |
| 37e7c631-36b9-3466-a999-97d801765523 | -8.19942 | -43.9839 | 2025-10-15 06:05:00 | AQUA_M-M | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 16.1 |
| bfbf1eda-835c-3690-9128-06dc5a904e56 | -6.17086 | -44.29641 | 2025-10-15 06:05:00 | AQUA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 5131d166-827a-3dea-9db5-e30c52edef05 | -8.22231 | -44.0583 | 2025-10-15 06:05:00 | AQUA_M-M | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 32.2 |
| 4155f748-9e3b-33e4-9c8b-c72ac34bff9a | -5.89023 | -43.74537 | 2025-10-15 06:05:00 | AQUA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 29.3 |
| d014692f-17ed-3eda-a4a3-4647b3cb3f18 | -7.95064 | -44.13461 | 2025-10-15 06:05:00 | AQUA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 14.0 |
| fa2847fe-88aa-3646-8edf-2e39ad38f8d4 | -8.45951 | -44.17944 | 2025-10-15 06:05:00 | AQUA_M-M | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 37.8 |
| 31733ffd-db10-3538-9c18-855810849643 | -6.17384 | -44.29132 | 2025-10-15 06:05:00 | AQUA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| d5da3582-4f47-3127-8447-931c76ad33cf | -7.94602 | -44.14093 | 2025-10-15 06:05:00 | AQUA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 13.8 |
| de211706-efb4-36f0-a71a-21ac4e2ae295 | -6.3337 | -44.01488 | 2025-10-15 06:05:00 | AQUA_M-M | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 1be09ebf-e714-3833-957b-e25cbef1b086 | -6.23168 | -44.16512 | 2025-10-15 06:05:00 | AQUA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 5f5d2225-a7dc-34dd-ad7a-a4398a1e8270 | -5.736 | -44.98302 | 2025-10-15 06:05:00 | AQUA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 91aec247-551c-3a8e-8805-5e72028ac208 | -6.05034 | -41.89921 | 2025-10-15 06:05:00 | AQUA_M-M | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 21.2 |
| ff4a0311-62e6-3b02-b101-763a987f024f | -7.93721 | -44.12585 | 2025-10-15 06:05:00 | AQUA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 2e23ebf0-954d-315d-8b36-621095fa2af1 | -8.20643 | -44.01342 | 2025-10-15 06:05:00 | AQUA_M-M | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 69.8 |
| 787419c8-44f5-36ec-be57-378cf100ccc9 | -6.45871 | -44.58007 | 2025-10-15 06:05:00 | AQUA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| d3d8dba4-4366-3229-bcae-4d8c40d2aee2 | -8.21537 | -44.0289 | 2025-10-15 06:05:00 | AQUA_M-M | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 155.2 |
| 6ee5d0f2-7f94-3e4d-a57c-126764f02b4d | -5.86852 | -43.85915 | 2025-10-15 06:05:00 | AQUA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 20.5 |
| e83f6170-2623-305c-86ea-1ca3c9748c93 | -6.44855 | -44.57858 | 2025-10-15 06:05:00 | AQUA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 15.5 |
| ea2ca7e9-f840-3051-aaf3-7d0f50e49f29 | -9.32458 | -46.95791 | 2025-10-15 06:08:00 | AQUA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 484204d4-bec7-3713-ac2d-3f939086d986 | -12.21445 | -47.1333 | 2025-10-15 06:08:00 | AQUA_M-M | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 23.6 |
| 1f8d89e9-a21b-3bcd-99a4-b828b5d7a569 | -12.22124 | -50.38147 | 2025-10-15 06:08:00 | AQUA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 66.9 |
| 3b58afaa-79c0-3b6f-b531-68b4234dfbf9 | -10.15347 | -44.91492 | 2025-10-15 06:08:00 | AQUA_M-M | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 372ff36e-6718-38dc-b08e-2ba84dca5ae9 | -12.25828 | -50.37788 | 2025-10-15 06:08:00 | AQUA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 26.2 |
| f6affdc5-6d7d-3763-8948-de2178c9aada | -13.39143 | -43.65497 | 2025-10-15 06:08:00 | AQUA_M-M | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 54d161ed-278b-33d6-818f-5d7777d451ed | -12.19493 | -50.3707 | 2025-10-15 06:08:00 | AQUA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 41.5 |
| dd78eb8e-9732-3079-a15e-0c5cffffc17c | -12.21233 | -50.38007 | 2025-10-15 06:08:00 | AQUA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 41.7 |
| 9024e2ae-3a19-3297-aef0-b7532867e49c | -12.21376 | -50.37089 | 2025-10-15 06:08:00 | AQUA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 11.4 |


[Clique aqui para ver as próximas entradas](README52.md)
