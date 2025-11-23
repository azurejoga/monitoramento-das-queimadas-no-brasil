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
| 754e913f-7e6c-307b-bdcc-7bd730b0d6ad | -1.3017 | -53.127998 | 2025-11-23 00:08:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7ae8494d-8907-3e01-87cd-d6d4508139a4 | -2.8699 | -45.122601 | 2025-11-23 00:08:00 | METOP-B | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 06e3e37e-7d09-399d-a73f-f93f1d3453f9 | -3.3842 | -47.182201 | 2025-11-23 00:08:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 19024c9b-42b6-3a17-a18f-448b63946013 | -2.9533 | -45.4394 | 2025-11-23 00:08:00 | METOP-B | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 20396e1e-8997-3e11-bfc5-a5fa2fa26fb0 | -2.6261 | -47.2924 | 2025-11-23 00:08:00 | METOP-B | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0893a387-4bd0-3268-b923-c2f212b72d7b | -2.9437 | -45.040699 | 2025-11-23 00:08:00 | METOP-B | OLINDA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2107456 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 3a6f0215-69b4-37f7-91ef-2e40bf19df09 | -3.4478 | -45.529301 | 2025-11-23 00:08:00 | METOP-B | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 513fe307-790d-3a75-9045-19ca6a234fff | -1.3115 | -53.125801 | 2025-11-23 00:08:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| df9d77f1-f2a1-3ec2-beba-20d1299640e7 | -2.0242 | -47.137901 | 2025-11-23 00:08:00 | METOP-B | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ecc49cce-341b-37aa-8077-edae5549d6f2 | -2.9148 | -40.266102 | 2025-11-23 00:08:00 | METOP-B | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 57d594e6-a01e-3364-8358-4ad279e41e8f | -4.0323 | -42.517101 | 2025-11-23 00:08:00 | METOP-B | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| cf442ea1-7b62-32b3-a1d3-ccc6a8812e0d | -3.0443 | -45.655701 | 2025-11-23 00:08:00 | METOP-B | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| be7d58d8-510c-3d7c-a3b9-b64044faedf9 | -3.826 | -45.338001 | 2025-11-23 00:08:00 | METOP-B | BELA VISTA DO MARANHÃO | MARANHÃO | Brasil | 2101772 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 50d29b65-771b-3004-8f79-9f6ef01d4453 | -3.1808 | -50.236599 | 2025-11-23 00:08:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 81a766ba-f62c-3248-8a64-808ad42566f4 | -2.4374 | -49.089699 | 2025-11-23 00:08:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d6528147-4863-368c-9f8e-de0075accae2 | -4.71 | -46.4464 | 2025-11-23 00:08:00 | METOP-B | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| be9727eb-6359-3f3d-8676-b4e108477450 | -4.0352 | -42.529301 | 2025-11-23 00:08:00 | METOP-B | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 7162a51d-5911-33f6-a4f7-5c606d31a970 | -2.6968 | -49.506901 | 2025-11-23 00:08:00 | METOP-B | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 421817e8-7f3f-3cbe-bc95-ae8a49e033ac | -2.9852 | -44.419399 | 2025-11-23 00:08:00 | METOP-B | BACABEIRA | MARANHÃO | Brasil | 2101251 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d5614baf-c6d7-31f0-b8e8-226db56ea693 | -4.3244 | -48.597 | 2025-11-23 00:08:00 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5050c7f0-c025-3336-b8e6-0be8b140eadc | -2.8719 | -45.131401 | 2025-11-23 00:08:00 | METOP-B | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 4484df6b-adfe-3315-abef-a9fc69cf36ce | -3.2879 | -45.7295 | 2025-11-23 00:08:00 | METOP-B | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 1440ec26-cf8f-3b22-97e4-1e825932aa0a | -3.0382 | -45.093601 | 2025-11-23 00:08:00 | METOP-B | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 60953738-e326-35a3-8ac5-7490fa58f33c | -3.4532 | -47.6203 | 2025-11-23 00:08:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dccb76d2-d682-3b87-a867-0e06d87e9f64 | -4.7134 | -46.461201 | 2025-11-23 00:08:00 | METOP-B | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| cd928a5c-f9d3-368f-99fd-dc406e6c45c1 | -1.3213 | -53.1236 | 2025-11-23 00:08:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5e6d075f-2aee-328b-8037-dea2186d56c5 | -2.6343 | -47.283001 | 2025-11-23 00:08:00 | METOP-B | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| daf32581-ba01-31de-9b85-b6b245fb7a7b | -2.0259 | -47.145199 | 2025-11-23 00:08:00 | METOP-B | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 71cc204c-572c-3c3a-b5e9-bf628ea8b439 | -1.3038 | -53.1371 | 2025-11-23 00:08:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cea04b4c-e12e-37b8-b179-2c04c5849cb7 | -2.6457 | -47.3783 | 2025-11-23 00:08:00 | METOP-B | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 764e1cfa-286c-33fe-8a48-31c65d8619c0 | -1.3254 | -53.1418 | 2025-11-23 00:08:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 536f65f5-6679-3dcf-8a3e-3cfa9c7aef2e | -3.7285 | -46.930401 | 2025-11-23 00:08:00 | METOP-B | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 4f38d40c-7aaf-355b-82e4-f50a39e2998e | -2.4472 | -49.087601 | 2025-11-23 00:08:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2981db22-c96c-3c58-96e0-689dd8c260c1 | -2.6359 | -47.380501 | 2025-11-23 00:08:00 | METOP-B | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 55e99160-d4bb-3b72-85b8-b74ed3c07b86 | -4.3228 | -48.590199 | 2025-11-23 00:08:00 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a1ee5f4d-ec07-361f-b7a1-75ae0870970f | -3.3009 | -45.786098 | 2025-11-23 00:08:00 | METOP-B | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 073aabff-c00e-3660-9afd-c03d235bb3aa | -3.1763 | -45.468498 | 2025-11-23 00:08:00 | METOP-B | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 570f214f-4b3a-34f8-9df2-42a58036a9b5 | -4.0295 | -42.504902 | 2025-11-23 00:08:00 | METOP-B | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| e3ba9e45-2aa5-3afa-b5b5-73d91a256952 | -1.3233 | -53.132702 | 2025-11-23 00:08:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bc6c38e1-9c76-37ec-a34c-3666a68edf89 | -2.4412 | -47.159302 | 2025-11-23 00:08:00 | METOP-B | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5f5baab5-6b0c-317c-8283-23172888012b | -2.983 | -44.409698 | 2025-11-23 00:08:00 | METOP-B | BACABEIRA | MARANHÃO | Brasil | 2101251 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| dff1d687-754f-38ac-ab78-49c6448d35c1 | -2.9611 | -45.428799 | 2025-11-23 00:08:00 | METOP-B | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ba737449-0245-3204-ab64-b8ff2b0a900f | -1.3136 | -53.134899 | 2025-11-23 00:08:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1a652213-9c88-32e7-8f09-b3c30bb4383e | -3.828 | -45.346401 | 2025-11-23 00:08:00 | METOP-B | SANTA INÊS | MARANHÃO | Brasil | 2109908 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 271b94f1-ac59-354a-8de4-8782ae9bfe74 | -2.6376 | -47.3876 | 2025-11-23 00:08:00 | METOP-B | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6824acf0-fbcd-3944-97a3-cd615eb41853 | -2.9514 | -45.431 | 2025-11-23 00:08:00 | METOP-B | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| fabd6661-636b-30b5-bf85-e3dbc8eb11e5 | -4.5637 | -45.498299 | 2025-11-23 00:08:00 | METOP-B | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3dd9fbb7-c7f3-3b8a-bbb3-2fda2cd0d716 | -4.0393 | -42.502602 | 2025-11-23 00:08:00 | METOP-B | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| d63e1b2c-0d4a-3975-a9c4-c4c1a1e1a4f4 | -4.2268 | -48.439201 | 2025-11-23 00:08:00 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c6ba38e4-f8ba-310b-9cee-e13f1cfd5233 | -4.7117 | -46.4538 | 2025-11-23 00:08:00 | METOP-B | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 8ed1914a-d455-338a-a917-562ec1f69939 | -2.6376 | -47.297298 | 2025-11-23 00:08:00 | METOP-B | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| caf3b49e-4559-31ba-9b63-f39bc18ff029 | -3.7302 | -46.937599 | 2025-11-23 00:08:00 | METOP-B | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 6e283342-527d-3eea-87bc-7b889ef1adf2 | -4.552 | -45.4925 | 2025-11-23 00:08:00 | METOP-B | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b403eb02-8e59-3af4-ae63-90d270a612a5 | -4.2283 | -48.445999 | 2025-11-23 00:08:00 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bca73236-3a28-396f-b508-48e5e4461f82 | -2.963 | -45.437199 | 2025-11-23 00:08:00 | METOP-B | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 12bfd5bf-569e-3a13-ba9f-9442f60b7f90 | -2.4396 | -47.1521 | 2025-11-23 00:08:00 | METOP-B | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 319f8b75-7793-379f-8c82-dc4efb534c32 | -2.6359 | -47.290199 | 2025-11-23 00:08:00 | METOP-B | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 153b6a20-088a-38df-803a-425874ace388 | -4.5502 | -45.484402 | 2025-11-23 00:08:00 | METOP-B | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b74d961f-b4cb-3fa7-993d-d36526d50080 | -2.6343 | -47.373402 | 2025-11-23 00:08:00 | METOP-B | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 28d0994f-ad40-3958-9bdc-ea1aa133d9ef | -3.0402 | -45.102402 | 2025-11-23 00:08:00 | METOP-B | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a2114d07-852b-3f4a-a025-25c6e5c8b4d0 | -3.3825 | -47.174999 | 2025-11-23 00:08:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3277d881-b0df-3563-9df1-1220f1bc0ac9 | -4.045 | -42.527 | 2025-11-23 00:08:00 | METOP-B | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 4c30671c-434d-3672-b7ac-fed87d916944 | -3.7728 | -46.0457 | 2025-11-23 00:08:00 | METOP-B | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 3afbaedb-5483-385f-8805-b547f8e79040 | -4.0421 | -42.514801 | 2025-11-23 00:08:00 | METOP-B | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| ccb1b7fc-36d7-35de-ab6c-e35ebe3879a2 | -1.7588 | -53.378101 | 2025-11-23 00:08:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 09608cd0-4dfe-37ff-9152-4ce195765d30 | -3.3858 | -47.189301 | 2025-11-23 00:08:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7682c5f1-f240-36cb-8363-b1c6861e4ba5 | -2.0973 | -45.344101 | 2025-11-23 00:08:00 | METOP-B | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 74987f82-5c1a-37ff-8de3-a22dfdc63a82 | -2.2869 | -50.4272 | 2025-11-23 00:08:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 39a28263-f67e-3411-b40a-155fd2d9e457 | -3.4548 | -47.6273 | 2025-11-23 00:08:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3f720fcc-7927-3e66-ae83-f6cee4edf094 | -2.8739 | -45.140202 | 2025-11-23 00:08:00 | METOP-B | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d31945d5-5f2f-3f81-b1a3-b1a0400c64aa | -2.9591 | -45.4203 | 2025-11-23 00:08:00 | METOP-B | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 8a6c24bf-d5af-3838-990d-d57ae123fbdc | -3.4497 | -45.537601 | 2025-11-23 00:08:00 | METOP-B | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 79dc57b2-1dd7-3089-b90c-22a0e75bfd44 | -2.9494 | -45.422501 | 2025-11-23 00:08:00 | METOP-B | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| da368f96-6acf-3417-9b33-c70961a4646a | -1.3157 | -53.144001 | 2025-11-23 00:08:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fde85456-de23-3268-af5d-9f3624c1badc | -3.7826 | -46.0434 | 2025-11-23 00:08:00 | METOP-B | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 32c55e54-409b-36d9-9489-17b9f5d0689f | -4.5618 | -45.4902 | 2025-11-23 00:08:00 | METOP-B | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0a45d8cc-7453-30a7-9d9f-39ad165f4a66 | -4.7785 | -46.430801 | 2025-11-23 00:08:00 | METOP-B | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 756b5116-46a1-38d3-b671-0d8add6d9194 | -3.0541 | -45.6535 | 2025-11-23 00:08:00 | METOP-B | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 8e34c27f-3bef-3625-bab7-3d34e800918d | -2.0953 | -45.3354 | 2025-11-23 00:08:00 | METOP-B | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 901078a6-1407-32cb-99e4-678657edff3f | -3.9878 | -47.7052 | 2025-11-23 00:08:00 | METOP-B | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 239e6a63-5536-33b5-a719-e6fb71a761d9 | -2.9598 | -45.4373 | 2025-11-23 00:10:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 174.1 |
| 5413ca21-6e96-3a92-af71-3f742755e189 | -4.7017 | -46.4729 | 2025-11-23 00:10:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 53.1 |
| fdd8674a-e918-3f4d-aaad-00f45d39ad41 | -1.3126 | -53.1503 | 2025-11-23 00:10:00 | GOES-19 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 153.7 |
| 64d265f0-5e4e-3cfc-982a-28d133232795 | -4.7203 | -46.4719 | 2025-11-23 00:10:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 3db5f6bf-f622-36b2-8e8b-d90701b1581c | -1.331 | -53.1501 | 2025-11-23 00:10:00 | GOES-19 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 69.5 |
| 3d65f829-6a5b-33b1-abe3-16658893285c | -2.6364 | -47.3951 | 2025-11-23 00:10:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 69.7 |
| be49826c-1ba0-3f52-bee0-c982f018d3ad | -2.6365 | -47.3733 | 2025-11-23 00:10:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 7f43cb7c-e3c6-3541-8466-7f0609c6115c | -2.8681 | -45.148 | 2025-11-23 00:10:00 | GOES-19 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 104.6 |
| ad95e71e-73d2-333d-8031-369036d5cfd3 | -5.6706 | -48.7947 | 2025-11-23 00:10:00 | GOES-19 | SÃO DOMINGOS DO ARAGUAIA | PARÁ | Brasil | 1507151 | 15 | 33 | nan | nan | nan | Amazônia | 61.8 |
| e11346f1-4327-367f-b135-87554e4ac1f1 | -7.4096 | -40.0563 | 2025-11-23 00:10:00 | GOES-19 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 59.6 |
| 57a0022d-fef5-3e07-b2aa-2f1bd1bd1b5f | -2.8867 | -45.1473 | 2025-11-23 00:10:00 | GOES-19 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 152.6 |
| 86b6ba21-f20b-359e-adc0-c701ed7f02cb | -4.038 | -42.5365 | 2025-11-23 00:10:00 | GOES-19 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 91.3 |
| 6984fbf4-e2d0-33cb-9401-e4fc4bfb5ece | -2.8868 | -45.1248 | 2025-11-23 00:10:00 | GOES-19 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 96.2 |
| ad21b1a1-7de3-3610-9087-88e74a308f0d | -2.8682 | -45.1254 | 2025-11-23 00:10:00 | GOES-19 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 69.6 |
| 3b70ac9c-9256-3cb9-9d3f-e044a41953f2 | -4.5594 | -45.4987 | 2025-11-23 00:10:00 | GOES-19 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 52.4 |
| 2c6b9154-e8e8-339b-879f-4e4c7f4388d7 | -4.7204 | -46.4497 | 2025-11-23 00:10:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 54.4 |
| e6343938-cc3c-396f-9e4f-e54a0c37dc30 | -4.0382 | -42.5129 | 2025-11-23 00:10:00 | GOES-19 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 110.2 |
| fc76c6fb-7606-3b57-af16-4026e9098d7d | -3.4507 | -47.6289 | 2025-11-23 00:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 61.8 |
| b12a978b-0064-37d2-aaea-57f50a19cb2b | -1.3126 | -53.1301 | 2025-11-23 00:10:00 | GOES-19 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 94.6 |
| 8f524a2f-40db-34af-9a99-1630dc7fdded | -1.3062 | -53.136799 | 2025-11-23 00:51:00 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README2.md)
