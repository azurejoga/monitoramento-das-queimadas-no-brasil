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
| 40d742a3-97d4-3f61-a272-8dda921444a4 | -21.33 | -48.95 | 2024-10-04 00:03:23 | MSG-03 | ITAJOBI | SÃO PAULO | Brasil | 3521903 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 5b8d7830-199c-36a0-bf41-870a39d067c7 | -21.32 | -48.89 | 2024-10-04 00:03:23 | MSG-03 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 5c0de2f7-504a-3fb0-9211-1839032190ba | -21.36 | -48.91 | 2024-10-04 00:03:23 | MSG-03 | ITAJOBI | SÃO PAULO | Brasil | 3521903 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 5a688381-4dc6-3ea6-9326-1f4f25661d44 | -18.85 | -43.6 | 2024-10-04 00:03:36 | MSG-03 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 5ec4031b-9b8d-384f-a8ae-baa85d58aad5 | -17.0 | -56.84 | 2024-10-04 00:03:49 | MSG-03 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 92e14e48-6f56-3a0f-ad7b-ead5984667f1 | -17.0 | -56.76 | 2024-10-04 00:03:49 | MSG-03 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| b70b90e0-ef4c-3c30-8ddb-023171c4202d | -17.03 | -56.86 | 2024-10-04 00:03:49 | MSG-03 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 09935eb9-9eb4-3ef8-8181-c9fa11ae7d5b | -17.03 | -56.78 | 2024-10-04 00:03:49 | MSG-03 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| a77ee1da-7f63-3031-83e5-aefec13d8c29 | -13.1 | -51.19 | 2024-10-04 00:04:10 | MSG-03 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 4ca459a9-a506-3b89-9dcb-66ba12f819ec | -9.32 | -50.83 | 2024-10-04 00:04:34 | MSG-03 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f35a4684-da6d-3840-a69b-3e59e02ca02e | -9.32 | -50.78 | 2024-10-04 00:04:34 | MSG-03 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0062cbcc-ee45-33e1-8aab-126d68e2f135 | -3.29 | -50.49 | 2024-10-04 00:05:08 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 46f34c6a-6484-37e6-a01c-14a6ad97f410 | -3.29 | -50.43 | 2024-10-04 00:05:08 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1f97e421-e4a4-3d3d-8707-b0819633e8b5 | -3.2349 | -50.3695 | 2024-10-04 00:05:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 104.4 |
| de94fa23-9c14-3f1f-a11c-5b678b394112 | -3.2534 | -50.3689 | 2024-10-04 00:05:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 115.5 |
| 22f686c8-8550-300c-b42c-a1d6685deb0a | -3.4039 | -42.3094 | 2024-10-04 00:05:25 | GOES-16 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | 88.8 |
| bb4468f8-3696-3299-b8f4-01f9f6c642af | -3.404 | -42.2858 | 2024-10-04 00:05:25 | GOES-16 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 288.8 |
| f7fd4220-f2b8-3f62-9a48-d5f352a12464 | -3.4042 | -42.2621 | 2024-10-04 00:05:25 | GOES-16 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 80.5 |
| 46bda84c-9ae0-3acf-8a0b-2fbaecd95694 | -3.4227 | -42.2849 | 2024-10-04 00:05:25 | GOES-16 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 81.1 |
| c1d30842-9446-30ec-bcf1-c502fcb08ca3 | -3.2899 | -50.4725 | 2024-10-04 00:05:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 140.7 |
| 4af35080-f8d7-3f53-8c4a-b0e5d42bbb4b | -3.2899 | -50.4516 | 2024-10-04 00:05:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 351.4 |
| 7f2fdaf8-3ff4-3902-b9b0-dcaf77f7af99 | -3.29 | -50.4306 | 2024-10-04 00:05:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 94.3 |
| 4165c63f-01a6-3e83-9121-85dfbd796213 | -3.3083 | -50.4719 | 2024-10-04 00:05:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 112.9 |
| 5c514a67-c2fb-3631-bce5-63a31abe8602 | -3.3084 | -50.451 | 2024-10-04 00:05:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 260.6 |
| b50c2a92-52b1-36af-9afe-ad0400306038 | -3.4915 | -50.8004 | 2024-10-04 00:05:26 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 93.4 |
| 9f76ff94-630a-3b6b-b493-9fcdfb3ef489 | -4.0949 | -48.4894 | 2024-10-04 00:05:29 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 95.2 |
| ce6c0f53-ea65-36ff-9224-d2a13bb66754 | -4.095 | -48.4679 | 2024-10-04 00:05:29 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 98.3 |
| a686a1b5-fda3-37c5-bad0-59cb6f7899c8 | -4.447 | -42.8889 | 2024-10-04 00:05:31 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 63.0 |
| 641426bf-e1f5-3df9-b08c-36d623275260 | -4.4657 | -42.8877 | 2024-10-04 00:05:31 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 173.1 |
| 1c9ef396-4743-350f-8341-fca0d8df9c0b | -4.5375 | -43.304 | 2024-10-04 00:05:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 139.1 |
| 7e13f3d9-4e98-3e4c-8391-9862cabe8133 | -4.5949 | -45.7436 | 2024-10-04 00:05:32 | GOES-16 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 42.3 |
| 7c4cf013-885f-3198-a203-862bf6e6447c | -4.6397 | -47.4007 | 2024-10-04 00:05:32 | GOES-16 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 76.1 |
| 22ee73f8-711b-3ded-82cf-2501378fde0c | -4.6686 | -45.8738 | 2024-10-04 00:05:32 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 48.9 |
| dfa96ee4-db50-3f8c-a6aa-f29c9450e213 | -4.687 | -45.8951 | 2024-10-04 00:05:32 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 47.4 |
| 2628370f-5aad-343f-bdbe-c5354912e4fa | -4.6872 | -45.8727 | 2024-10-04 00:05:32 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 87.7 |
| 6dd0da8d-38fa-38d1-9eba-61470150035e | -5.5033 | -48.8046 | 2024-10-04 00:05:37 | GOES-16 | SÃO DOMINGOS DO ARAGUAIA | PARÁ | Brasil | 1507151 | 15 | 33 | nan | nan | nan | Amazônia | 59.5 |
| c103c6ae-7ae4-3a18-ada4-fafe67880c62 | -5.8214 | -44.1426 | 2024-10-04 00:05:39 | GOES-16 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 73.4 |
| f8fc72a7-c28a-3e8b-a68d-00e0af71fcaa | -5.8216 | -44.1196 | 2024-10-04 00:05:39 | GOES-16 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 97.5 |
| 79633239-3537-3152-b7b0-190093ae4bc3 | -5.8403 | -44.1181 | 2024-10-04 00:05:39 | GOES-16 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 66.6 |
| 32273191-70bb-3066-ab91-4146759a7f8b | -5.9599 | -45.3861 | 2024-10-04 00:05:40 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 56.6 |
| a22c60d0-d143-37b6-bdee-d3e9d5954cfb | -6.2524 | -44.132 | 2024-10-04 00:05:41 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 61.4 |
| 2911ed1a-67fa-3a37-afcc-75840a899855 | -7.0345 | -71.7727 | 2024-10-04 00:05:47 | GOES-16 | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 69.6 |
| 2c2f709f-c598-3222-a61c-680231b56287 | -7.0345 | -71.7545 | 2024-10-04 00:05:47 | GOES-16 | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 73.2 |
| cdd21201-22b5-3ce1-85ae-483b15752615 | -7.0529 | -71.7726 | 2024-10-04 00:05:47 | GOES-16 | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 136.2 |
| 5bfd4494-0786-3057-b803-a249612404f3 | -7.0529 | -71.7544 | 2024-10-04 00:05:47 | GOES-16 | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 156.6 |
| 6100eb16-a191-3213-a843-9f5c98d8d817 | -7.3821 | -72.9355 | 2024-10-04 00:05:49 | GOES-16 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 75.8 |
| 0a869acf-f572-3a87-9819-5c5a51dac784 | -7.4557 | -72.6984 | 2024-10-04 00:05:49 | GOES-16 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 131.3 |
| e38873df-b002-38da-9d35-7b7e384c6347 | -7.8166 | -50.5219 | 2024-10-04 00:05:50 | GOES-16 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 59.3 |
| e624a140-447d-3133-bd5a-c4be6b7f37b2 | -7.8351 | -50.5416 | 2024-10-04 00:05:50 | GOES-16 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 87.3 |
| 2d3a9ca4-632d-3167-9534-3e69986a3e9b | -7.8353 | -50.5204 | 2024-10-04 00:05:50 | GOES-16 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 75.7 |
| ae0d864a-5d65-30b6-96bf-bd904fb23105 | -8.172 | -50.4941 | 2024-10-04 00:05:52 | GOES-16 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 69.7 |
| c7f77eb8-e8ea-38d8-8edf-4b61c67566a4 | -8.1722 | -50.473 | 2024-10-04 00:05:52 | GOES-16 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 76c00abb-1455-36b1-a16f-d19406e60034 | -8.2986 | -50.9059 | 2024-10-04 00:05:53 | GOES-16 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 53.7 |
| b479b4f6-4e96-34bf-a7e7-5664b13b992c | -8.3128 | -49.5679 | 2024-10-04 00:05:53 | GOES-16 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 94.4 |
| 030c686b-ef87-32d9-a7b6-5375aeb48e1f | -8.6448 | -50.0518 | 2024-10-04 00:05:55 | GOES-16 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 148.5 |
| 8ccdac4c-e8ac-3020-8daf-5cdc251686c7 | -8.6451 | -50.0304 | 2024-10-04 00:05:55 | GOES-16 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 82.7 |
| 1733f9b4-43e0-3656-8ae0-d1d3a6e1945e | -8.6636 | -50.0501 | 2024-10-04 00:05:55 | GOES-16 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 86.0 |
| 85d9266a-53ea-31eb-b72b-d75ca8ec5928 | -9.1481 | -43.1611 | 2024-10-04 00:05:57 | GOES-16 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 77.9 |
| f7c985a7-ca53-35df-8db5-eb349183d4ac | -9.1041 | -50.902 | 2024-10-04 00:05:58 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 76.6 |
| 87615f88-498e-379f-8d37-c8bd93218177 | -9.293 | -50.8008 | 2024-10-04 00:05:59 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 105.4 |
| c8ac8e21-8b8e-3b51-a825-6f302ea193f4 | -9.3115 | -50.8203 | 2024-10-04 00:05:59 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 246.9 |
| 1ac17d1e-6b38-3c4b-8c67-8cee72a963a2 | -9.3118 | -50.7991 | 2024-10-04 00:05:59 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 492.5 |
| 51354dc6-96fb-3cf4-8316-2bf9ddd0ceb6 | -9.312 | -50.7779 | 2024-10-04 00:05:59 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 102.9 |
| db7246d5-0200-3251-82ed-5e20ed599bbb | -9.3306 | -50.7974 | 2024-10-04 00:05:59 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 120.4 |
| 04eeb786-1917-3c92-b5f5-fa82e2a000cd | -9.6012 | -50.1779 | 2024-10-04 00:06:00 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 92.9 |
| 485c1897-7747-3286-b64d-5cf7c3df1656 | -9.55 | -64.2179 | 2024-10-04 00:06:01 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 59.0 |
| bd5e8f40-b707-3032-9e8e-359b16e93f79 | -9.5686 | -64.2171 | 2024-10-04 00:06:01 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 74.7 |
| 4f2ac2d8-1b11-38cf-909b-c19e5d30dd33 | -9.8263 | -68.9997 | 2024-10-04 00:06:02 | GOES-16 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 6d74b10d-d93f-34f5-90b7-11563f6cf6f1 | -10.2188 | -47.7281 | 2024-10-04 00:06:04 | GOES-16 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 80.7 |
| 7c543c24-1460-3bf8-87aa-457897881edc | -10.2378 | -47.726 | 2024-10-04 00:06:04 | GOES-16 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 78.7 |
| c3659dc6-53ae-3113-80da-ae3f01f661bd | -10.4424 | -50.7336 | 2024-10-04 00:06:05 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 2ee41af7-d604-3402-9aa4-435bd922ff5a | -10.4613 | -50.7317 | 2024-10-04 00:06:05 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 74.9 |
| e5347471-fc2c-3925-aad0-81f6c12ae9df | -11.0536 | -46.5118 | 2024-10-04 00:06:08 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 66.5 |
| ad77d32a-0194-353f-8e83-8924fb7a5237 | -11.6631 | -47.707 | 2024-10-04 00:06:12 | GOES-16 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 96.4 |
| 5e0b2863-ebfc-3277-863e-8c5b9ae907c8 | -11.6635 | -47.6847 | 2024-10-04 00:06:12 | GOES-16 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 96.3 |
| a9aeab8d-949f-3956-a9a9-06ce1f5ab574 | -11.5238 | -65.0615 | 2024-10-04 00:06:12 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 8bea4c7f-a1d2-351a-afea-99c47c2cc5a7 | -11.5425 | -65.0607 | 2024-10-04 00:06:12 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 81.1 |
| 847e9e1f-f548-3b04-a7c3-74883bb6dc1f | -11.5426 | -65.0418 | 2024-10-04 00:06:12 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 50.5 |
| 0e7ce968-04e2-30fe-86c9-d01cc5501b8d | -11.6932 | -64.9785 | 2024-10-04 00:06:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 87d33332-367f-30ab-a0bd-5c606089c2f6 | -11.8052 | -56.6024 | 2024-10-04 00:06:13 | GOES-16 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 76.7 |
| a9d1cdfb-cbc6-3291-886c-7cc681c44315 | -11.8242 | -56.6009 | 2024-10-04 00:06:13 | GOES-16 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 134.7 |
| d13f71bf-0808-3713-babd-1751c206f02d | -11.8244 | -56.5808 | 2024-10-04 00:06:13 | GOES-16 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 80.4 |
| 9d1f7cb9-7c9b-3865-9a62-017fcd03a100 | -12.1528 | -40.8943 | 2024-10-04 00:06:14 | GOES-16 | UTINGA | BAHIA | Brasil | 2932804 | 29 | 33 | nan | nan | nan | Caatinga | 57.0 |
| 41237c37-e5eb-3831-9e4a-bd36ba036d9c | -11.8957 | -56.9554 | 2024-10-04 00:06:14 | GOES-16 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 61.3 |
| aea0f327-3cd4-3b1e-a35e-b79e960495cc | -11.9147 | -56.9539 | 2024-10-04 00:06:14 | GOES-16 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 30e8fd92-e8ce-378d-9f93-af148c8e62ea | -11.874 | -63.2784 | 2024-10-04 00:06:14 | GOES-16 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 47.2 |
| a80a4a5f-9f91-32e9-ac13-8744514b1b5d | -12.5898 | -53.1359 | 2024-10-04 00:06:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 109.5 |
| dc7fe9e4-93ad-3831-9ac8-055d3f985f9a | -12.5901 | -53.115 | 2024-10-04 00:06:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 147.3 |
| baab681f-ccda-32f1-ac79-1002e4334d5f | -12.6092 | -53.1129 | 2024-10-04 00:06:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 95.9 |
| fb5e165c-b40b-3dc7-ad00-cf010cc683a4 | -12.6295 | -63.1225 | 2024-10-04 00:06:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 87.1 |
| 4b9f30c1-4301-33fc-9075-d55e283825c1 | -12.6296 | -63.1033 | 2024-10-04 00:06:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 75.5 |
| 932b5258-1712-3241-b73c-d3b81ce24d52 | -12.6484 | -63.1214 | 2024-10-04 00:06:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 53.4 |
| d4d2c8a6-6361-3bc1-93e7-dd355931620b | -12.6486 | -63.1022 | 2024-10-04 00:06:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 64.2 |
| 15398cc7-1244-38b2-8097-2aaa6d8cec9e | -13.0786 | -51.1385 | 2024-10-04 00:06:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 106.1 |
| 13e28614-ee94-327d-b945-ae131781cacb | -13.0971 | -51.1789 | 2024-10-04 00:06:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 150.2 |
| 0da569c4-c3dd-3af9-8032-590835e16fb1 | -13.0975 | -51.1575 | 2024-10-04 00:06:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 224.1 |
| 45a237c9-aee7-3122-b89e-a46fde508bc3 | -13.1163 | -51.1765 | 2024-10-04 00:06:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 128.4 |
| fa039bb1-dab5-3967-b7fb-ace19161ec98 | -13.1166 | -51.1551 | 2024-10-04 00:06:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 177.5 |
| 5d441542-e926-314c-9852-d9753233d92d | -13.6143 | -51.22 | 2024-10-04 00:06:23 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 120.2 |
| c8e51a87-63f4-37fb-8719-cc8b315c05f7 | -13.6146 | -51.1986 | 2024-10-04 00:06:23 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 121.2 |


[Clique aqui para ver as próximas entradas](README2.md)
