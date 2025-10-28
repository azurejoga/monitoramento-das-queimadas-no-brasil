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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 65fe56df-e8a0-3336-bb16-140c538b224c | -6.6873 | -42.0535 | 2025-10-28 01:40:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 80.7 |
| 4e000f2b-0f8d-35db-8cff-d25849496535 | -11.2794 | -45.5281 | 2025-10-28 01:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 49.5 |
| b3364e5a-eda3-36db-9f9e-8eac72c6b384 | -7.9647 | -45.5317 | 2025-10-28 01:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 133.9 |
| 6c27f350-14c6-3c00-8bb0-f96da799cbab | -2.7555 | -45.422 | 2025-10-28 01:40:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 49.6 |
| 364071c9-085e-34b0-a16c-fc2eeef14661 | -11.299 | -45.5025 | 2025-10-28 01:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 66.0 |
| a8241a64-5285-3207-aaba-18e59eb921ad | -4.4602 | -43.6569 | 2025-10-28 01:40:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 93.1 |
| d481479d-3fe1-397d-a501-2b5f922c6566 | -7.9652 | -45.4863 | 2025-10-28 01:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 60.1 |
| d469337e-b1d5-3b79-a59e-776b16b7e954 | -7.9647 | -45.5317 | 2025-10-28 01:50:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 103.9 |
| 22f3a2cd-4803-3518-b0aa-5ad2eb55663a | -15.1555 | -46.5832 | 2025-10-28 01:50:00 | GOES-19 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 140.0 |
| c5e7d160-79db-3a20-b257-fbed71344b77 | -7.9461 | -45.5108 | 2025-10-28 01:50:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 219.2 |
| 6d2d6cf2-36ba-3adc-b067-2911610a9059 | -11.2802 | -45.4823 | 2025-10-28 01:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 98.4 |
| 509f4d9c-0d67-3328-b3a1-57a8051b7111 | 0.3957 | -50.858 | 2025-10-28 01:50:00 | GOES-19 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 48.0 |
| 18891f8c-2647-3d30-8ec4-7d4347763ce3 | -2.7555 | -45.422 | 2025-10-28 01:50:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 49.0 |
| 53047526-4514-342b-8ef0-f182709c1bd4 | -4.4632 | -43.2386 | 2025-10-28 01:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 68.5 |
| a830452f-f41d-36f7-a8a3-189b7a8784b5 | -7.9882 | -46.7406 | 2025-10-28 01:50:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 63.0 |
| 13ec83ac-7607-3938-bf93-ac60f903d90c | -7.4541 | -49.4018 | 2025-10-28 01:50:00 | GOES-19 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 71.4 |
| 7a9b9e1e-d0c2-372c-a14f-78481b07f54f | -3.5831 | -43.634 | 2025-10-28 01:50:00 | GOES-19 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 56.9 |
| f6b28185-a40c-35db-b087-4316dba764fd | -6.6875 | -42.0296 | 2025-10-28 01:50:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 89.9 |
| 806fa9a9-3a00-3cab-ad9b-ce797fa32e7d | -7.9459 | -45.5335 | 2025-10-28 01:50:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 144.9 |
| 69df2f62-7445-3b78-a55c-90d6677e299c | -4.4604 | -43.6337 | 2025-10-28 01:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 93.4 |
| ad268d19-7427-3405-9333-2f36483505da | -10.5683 | -49.8018 | 2025-10-28 01:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 66.3 |
| 8046aec3-c92b-3f43-9bdc-9c22b48f4c35 | -4.4602 | -43.6569 | 2025-10-28 01:50:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 78.3 |
| 976d0f35-78ec-3c07-9064-5759d8eeef12 | -7.9464 | -45.4882 | 2025-10-28 01:50:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 115.9 |
| 05e2fbdd-ab09-3e2f-8404-625618fe3b7a | -6.7064 | -42.0278 | 2025-10-28 01:50:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 75.7 |
| a2b7e794-1fc4-3206-bc9f-9a89dcb2c92c | -6.7061 | -42.0517 | 2025-10-28 01:50:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 72.1 |
| e771cfd1-5d6e-35f6-a540-3485e78900c8 | -7.9652 | -45.4863 | 2025-10-28 01:50:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 63.2 |
| f31dd86f-5ca0-33a4-a540-1029b2dbd5a8 | -7.965 | -45.509 | 2025-10-28 01:50:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 119.0 |
| 7b9a4429-2aea-3067-82e0-90b6d7b481b1 | -11.299 | -45.5025 | 2025-10-28 01:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 58.6 |
| 9339b660-7f75-3b4e-ba10-d13e8d4c28c5 | -6.6873 | -42.0535 | 2025-10-28 01:50:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 84.1 |
| 19b04c41-3ab9-3eed-997d-a5ae5d1e71a6 | -2.7556 | -45.3995 | 2025-10-28 01:50:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 05094686-0595-38dd-a91d-37b03413f84d | -15.1751 | -46.5797 | 2025-10-28 01:50:00 | GOES-19 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 133.6 |
| 7015c4b5-8e30-3716-862b-828f71bde74c | -11.2798 | -45.5052 | 2025-10-28 01:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 275.7 |
| 6422d29e-07d4-3b39-8adf-8efbb2b28c4d | -6.7064 | -42.0278 | 2025-10-28 02:00:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 73.9 |
| 2f7bb481-250b-347f-81b0-15ca8be0e4bb | -7.4541 | -49.4018 | 2025-10-28 02:00:00 | GOES-19 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 77.6 |
| 867d6e9c-f0e9-37bf-bfd6-38d877d0e58f | -11.2798 | -45.5052 | 2025-10-28 02:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 235.5 |
| e0668b43-6489-3232-9da8-6acdeadc05f1 | -2.7556 | -45.3995 | 2025-10-28 02:00:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 42.9 |
| 6fcf7fa6-881e-3cf4-a32f-d6a34b7f9681 | -11.2802 | -45.4823 | 2025-10-28 02:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 83.8 |
| ef86a9ec-b195-3a73-a1d4-fa743e36b8fb | -4.4604 | -43.6337 | 2025-10-28 02:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 78.0 |
| 05932238-c4a4-362f-9d52-1f362c3d1774 | -10.5683 | -49.8018 | 2025-10-28 02:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 60.9 |
| 7b7c52e1-69bb-3e4e-8719-c8cc5afe24ab | -11.299 | -45.5025 | 2025-10-28 02:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 69.0 |
| ec31bc25-ba90-3062-8547-492751c06a73 | -4.4602 | -43.6569 | 2025-10-28 02:00:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 64.5 |
| 5e0b06a1-369a-3f0c-8749-c87e072618de | -6.7061 | -42.0517 | 2025-10-28 02:00:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 79.3 |
| 3e90ec10-31eb-3ede-b036-98a8e298a2b6 | -6.6873 | -42.0535 | 2025-10-28 02:00:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 78.0 |
| 92cf308f-dbda-3ac3-ac6e-5a1f848d8651 | -6.6875 | -42.0296 | 2025-10-28 02:00:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 75.3 |
| 3853ce6c-bb1b-3157-9121-aabf286f3c78 | -4.4632 | -43.2386 | 2025-10-28 02:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 5f005b99-3940-3fdc-9ccb-71d1c0864c1b | -3.5831 | -43.634 | 2025-10-28 02:00:00 | GOES-19 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 51.8 |
| 324124b4-66d8-3743-a63d-66f16099327d | -2.7555 | -45.422 | 2025-10-28 02:00:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 40.0 |
| 8f8cdd18-2667-3962-a5d6-b4e19468119b | -6.7061 | -42.0517 | 2025-10-28 02:10:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 63.9 |
| ceb50ac2-064e-365b-ac89-838ddcf01b4e | -7.9461 | -45.5108 | 2025-10-28 02:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 113.0 |
| 8875bacb-c9ec-3498-9907-5d9e1162350d | -7.965 | -45.509 | 2025-10-28 02:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 89.0 |
| 63715ee3-499b-3caf-8fdb-9452001ebb6a | 0.3957 | -50.858 | 2025-10-28 02:10:00 | GOES-19 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 40.8 |
| b0e99e71-7498-369d-b63e-3e48225ac3b6 | -7.9464 | -45.4882 | 2025-10-28 02:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 75.2 |
| c0e78abb-92bc-3a9d-b790-c3e24be980b9 | -3.3181 | -44.4042 | 2025-10-28 02:10:00 | GOES-19 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 55.4 |
| 96b25f41-81c4-3530-98b9-067cdd9bf9f6 | -6.6873 | -42.0535 | 2025-10-28 02:10:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 84.2 |
| 71f417cb-99e5-3f18-8c00-96ca3f01e26a | -11.2798 | -45.5052 | 2025-10-28 02:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 188.5 |
| 944e97b1-fde4-3666-8bfb-f77098c38c0e | -4.4604 | -43.6337 | 2025-10-28 02:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 55.5 |
| d183c4d1-d047-3032-9114-9ea3d0ccfbcb | -10.5683 | -49.8018 | 2025-10-28 02:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 66.9 |
| 5a95a327-1608-37f7-bf72-25b8ddd32d73 | -4.4632 | -43.2386 | 2025-10-28 02:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 68.1 |
| 74b31914-81b5-369c-be77-8b616192ea0f | -6.7064 | -42.0278 | 2025-10-28 02:10:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 64.4 |
| d1627175-2847-3237-82f1-c725ae42846a | -3.5831 | -43.634 | 2025-10-28 02:10:00 | GOES-19 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 51.6 |
| 8220f93e-3cef-3aec-b01f-e2f9b13dead3 | -7.9647 | -45.5317 | 2025-10-28 02:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 86.4 |
| 86d1f4b1-de2f-31c4-ac69-b8b44c0a237c | -7.4541 | -49.4018 | 2025-10-28 02:10:00 | GOES-19 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 67.2 |
| d7f0f65b-3340-35d8-a959-396fa772b452 | -7.9459 | -45.5335 | 2025-10-28 02:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 78.0 |
| 1427a095-fdce-3482-aa73-ea9df8a46542 | -11.299 | -45.5025 | 2025-10-28 02:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 93.4 |
| 892fedb2-2e49-3fe0-9c22-94be2ebf23bd | -11.2802 | -45.4823 | 2025-10-28 02:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 71.7 |
| dad59de7-f394-3ba0-bd55-acf5c35d43b1 | -6.6875 | -42.0296 | 2025-10-28 02:10:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 92.8 |
| 6078de4e-b35d-3fa4-a85f-b0bec03002b6 | -15.156 | -46.5602 | 2025-10-28 02:20:00 | GOES-19 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 223.3 |
| dc4e7d46-8b6c-32b3-95d4-a05c0cb607f0 | -11.2798 | -45.5052 | 2025-10-28 02:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 204.9 |
| 1ddfd55f-6bfc-3918-b093-d67922dd55dd | -6.7061 | -42.0517 | 2025-10-28 02:20:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 63.5 |
| e139c4e7-5ad4-350e-9895-17ec20001f32 | -15.1364 | -46.5637 | 2025-10-28 02:20:00 | GOES-19 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 94.9 |
| f4a5a738-7f2a-3077-92c1-0f0024961204 | -7.9459 | -45.5335 | 2025-10-28 02:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 95.7 |
| 86a9e0d4-d9c1-32dc-abde-d30f35fc336e | -11.299 | -45.5025 | 2025-10-28 02:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 115.0 |
| 2de92611-9059-3e0c-8668-896b5adc8ae9 | 0.4141 | -50.858 | 2025-10-28 02:20:00 | GOES-19 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 51.1 |
| 983976e7-aa73-3857-adc3-a12e65a77d72 | -6.6873 | -42.0535 | 2025-10-28 02:20:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 75.1 |
| 717a0f76-75f2-33d6-941c-8f1aa542abe3 | -7.965 | -45.509 | 2025-10-28 02:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 75.9 |
| 633ba032-5264-34b3-94c3-e0f1efbf337d | -4.4632 | -43.2386 | 2025-10-28 02:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 68.2 |
| a59cc8af-cf64-39e6-a05d-4981f19de839 | -3.5831 | -43.634 | 2025-10-28 02:20:00 | GOES-19 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 52.8 |
| 810ca2ad-edaf-3524-83c6-1275568965eb | -15.1751 | -46.5797 | 2025-10-28 02:20:00 | GOES-19 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 140.0 |
| f5ad22ce-61aa-3764-92de-1c03fd01b858 | -7.4541 | -49.4018 | 2025-10-28 02:20:00 | GOES-19 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 70.5 |
| 735556f2-dee9-3e4a-95ba-4b8d78555abb | 0.3957 | -50.858 | 2025-10-28 02:20:00 | GOES-19 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 62.5 |
| 06b026a3-b254-3d66-a268-263409ae321f | -15.1359 | -46.5867 | 2025-10-28 02:20:00 | GOES-19 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 200.1 |
| 184c4ee9-ead9-311f-9430-d3633316728a | -15.1555 | -46.5832 | 2025-10-28 02:20:00 | GOES-19 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 583.6 |
| b2734e06-2f1e-3a10-928e-f57ed295aa75 | -15.155 | -46.6062 | 2025-10-28 02:20:00 | GOES-19 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 123.1 |
| e4ab395a-06dd-3025-bc28-eda8445e7421 | -11.2802 | -45.4823 | 2025-10-28 02:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 82.0 |
| f233372c-67a1-3ff9-b89e-3c0f1b67b05c | -6.6875 | -42.0296 | 2025-10-28 02:20:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 74.2 |
| 1f371736-48d2-38c2-8067-bb84ebbd7c8e | -7.9647 | -45.5317 | 2025-10-28 02:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 102.0 |
| f8fd50f1-a92b-393e-b0c1-8ab959b37813 | -11.2794 | -45.5281 | 2025-10-28 02:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 54.3 |
| 5da2c900-1fc0-3d85-86b4-aba48e4f697f | -7.9461 | -45.5108 | 2025-10-28 02:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 95.3 |
| 52adb158-8b3d-31d9-aa92-8461ec0c05df | -7.9464 | -45.4882 | 2025-10-28 02:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 66.6 |
| 03f99e53-3809-32f0-9719-d9a3c03f1814 | -7.9693 | -46.7423 | 2025-10-28 02:20:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 50.8 |
| 98a28611-3466-3f8d-8611-22233219213c | -15.1751 | -46.5797 | 2025-10-28 02:30:00 | GOES-19 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 102.5 |
| 02a1bf8e-b720-3dd8-a7ff-4587a7670b18 | -7.9461 | -45.5108 | 2025-10-28 02:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 113.2 |
| f490c83d-0de0-3120-a12e-cc8fb6cfffbb | -3.5831 | -43.634 | 2025-10-28 02:30:00 | GOES-19 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 55.0 |
| 0488abb9-6901-311f-bfb4-7b906bc53b75 | -7.9464 | -45.4882 | 2025-10-28 02:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 67.6 |
| c78b16f6-0a9d-3728-aa23-067822e10554 | -4.4604 | -43.6337 | 2025-10-28 02:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 67.4 |
| 1a97b355-9859-3492-971a-d4b92e0948a5 | -15.1359 | -46.5867 | 2025-10-28 02:30:00 | GOES-19 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 100.5 |
| 956ea95e-9a34-365d-aabf-9b292692340c | -15.156 | -46.5602 | 2025-10-28 02:30:00 | GOES-19 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 174.7 |
| 2e1b7760-15e3-3579-9ceb-a1fd380d296f | -7.9693 | -46.7423 | 2025-10-28 02:30:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 65.9 |
| 0e94d23a-1298-3693-912b-2636aa31901a | -7.9882 | -46.7406 | 2025-10-28 02:30:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 54.7 |
| 716b7a2e-50d7-3d6a-a484-e8065f038645 | -7.965 | -45.509 | 2025-10-28 02:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 76.3 |


[Clique aqui para ver as próximas entradas](README8.md)
