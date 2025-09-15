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

## Dados Diários - Página 67

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dde4b3d0-1d69-30ce-bdbc-7f54bc20c91b | -7.8753 | -43.5876 | 2025-09-15 09:40:00 | GOES-19 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 217.5 |
| ace29308-71f8-39f7-89ee-6e0593a7267c | -7.8945 | -43.5623 | 2025-09-15 09:40:00 | GOES-19 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 105.5 |
| 64f7ee1e-733d-3764-9a40-542e572504e6 | -7.8753 | -43.5876 | 2025-09-15 09:50:00 | GOES-19 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 318.6 |
| e2765c9e-08b4-30fc-83ef-44d254ed998f | -7.8756 | -43.5643 | 2025-09-15 09:50:00 | GOES-19 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 213.7 |
| a027f67a-1a90-32a4-ac8f-6589497ea243 | -7.8945 | -43.5623 | 2025-09-15 09:50:00 | GOES-19 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 126.9 |
| 40f91a9c-7db5-3592-ba0a-106f6415dea6 | -7.8942 | -43.5857 | 2025-09-15 09:50:00 | GOES-19 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 124.3 |
| e7348f31-7482-30ef-aeb2-cd44f4df30b3 | -7.8753 | -43.5876 | 2025-09-15 10:00:00 | GOES-19 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 287.5 |
| 4323fe70-c34a-3b57-b952-ec2042c4f4f4 | -7.8942 | -43.5857 | 2025-09-15 10:00:00 | GOES-19 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 135.3 |
| 10ffffd6-6ae7-3829-a7e6-ef07a895215e | -8.651 | -46.3637 | 2025-09-15 10:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 121.5 |
| 81da0713-1349-3c71-a11b-bb7eb68aa13e | -7.8756 | -43.5643 | 2025-09-15 10:00:00 | GOES-19 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 195.5 |
| a7b5ee2f-20d8-3e85-9a80-c7de02543182 | -7.8945 | -43.5623 | 2025-09-15 10:00:00 | GOES-19 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 128.4 |
| 8484080f-0827-3791-a0c4-c69fc26ce082 | -7.8753 | -43.5876 | 2025-09-15 10:10:00 | GOES-19 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 269.2 |
| d08cacab-5dae-300a-90cc-a7bf0b208848 | -7.8945 | -43.5623 | 2025-09-15 10:10:00 | GOES-19 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 137.0 |
| 808a49f5-aca4-35a4-9d9e-070e831f3c93 | -7.8756 | -43.5643 | 2025-09-15 10:10:00 | GOES-19 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 309.0 |
| 05da362a-fe3c-3be9-ab02-7aee74e7a7ce | -7.8942 | -43.5857 | 2025-09-15 10:10:00 | GOES-19 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 91.7 |
| c5d1907e-f1af-3615-8ab0-ba3d4ab70fa0 | -7.8942 | -43.5857 | 2025-09-15 10:20:00 | GOES-19 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 157.9 |
| eee22e81-6731-32c9-8e6f-b3ffdec26887 | -7.8756 | -43.5643 | 2025-09-15 10:20:00 | GOES-19 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 291.7 |
| 9edfcbcf-e706-39f4-9408-12a568b1056b | -8.651 | -46.3637 | 2025-09-15 10:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 127.9 |
| 0ad9c329-874c-3369-8020-3c41308e4735 | -7.8945 | -43.5623 | 2025-09-15 10:20:00 | GOES-19 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 228.1 |
| f4cb281f-bc42-3145-b836-1387b4cc5bec | -8.6507 | -46.3862 | 2025-09-15 10:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 141.4 |
| 845b5f80-48ab-3296-a531-8dea40a2335c | -7.8753 | -43.5876 | 2025-09-15 10:20:00 | GOES-19 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 269.9 |
| 57505cb0-e1f3-38fc-ad74-995f4a2c571c | -7.8942 | -43.5857 | 2025-09-15 10:30:00 | GOES-19 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 140.4 |
| 83d57558-2dc0-370e-8e85-bde5ea4f2159 | -7.8945 | -43.5623 | 2025-09-15 10:30:00 | GOES-19 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 242.1 |
| da20cf70-6180-3bee-b9d7-0153354ec674 | -7.8756 | -43.5643 | 2025-09-15 10:30:00 | GOES-19 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 329.4 |
| b667ce1b-ab08-364e-8d91-72f773d2a979 | -16.673 | -49.7615 | 2025-09-15 10:30:00 | GOES-19 | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 117.9 |
| 8dfb9ade-0a8d-3e50-8e27-1996b5707e12 | -7.8753 | -43.5876 | 2025-09-15 10:30:00 | GOES-19 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 269.5 |
| 8c933f01-52c6-3ddb-9bde-1624bccb3535 | -8.651 | -46.3637 | 2025-09-15 10:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 111.7 |
| f5b527ca-2f0a-3015-a81f-d0cd40332fea | -7.8753 | -43.5876 | 2025-09-15 10:40:00 | GOES-19 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 213.9 |
| 853e34df-7955-3917-be5d-0bdef6f25e6a | -7.8942 | -43.5857 | 2025-09-15 10:40:00 | GOES-19 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 147.5 |
| da98d36d-55e8-3f83-ba6a-18a39ca94c77 | -10.935 | -45.5978 | 2025-09-15 10:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 117.2 |
| 3cf17e6c-3673-3e63-97ab-a6c555cba63b | -7.8756 | -43.5643 | 2025-09-15 10:40:00 | GOES-19 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 278.4 |
| 64ac2fb9-7513-3b5e-b0bf-d2cf9464dbb3 | -8.6507 | -46.3862 | 2025-09-15 10:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 134.0 |
| 18ea9dc7-416d-3d99-9f16-b0fc2fa0dece | -12.8003 | -47.2375 | 2025-09-15 10:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 105.5 |
| e3792793-7203-3d50-a48a-9d6691f63668 | -12.6164 | -45.7452 | 2025-09-15 10:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 89.1 |
| 5c44cf6d-1055-3d46-9892-5be7fa1c6f7f | -7.8945 | -43.5623 | 2025-09-15 10:40:00 | GOES-19 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 257.5 |
| 0b5f9e3f-5fde-378d-b8de-9a6412dd1dca | -7.8753 | -43.5876 | 2025-09-15 10:50:00 | GOES-19 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 340.5 |
| 2a7b3b7a-b79d-3e59-80f2-78a10040a950 | -12.7626 | -47.1981 | 2025-09-15 10:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 102.5 |
| 919f2dc4-040d-3408-ae93-3f954673737b | -18.4137 | -49.8487 | 2025-09-15 10:50:00 | GOES-19 | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Cerrado | 131.1 |
| 80364b91-03f6-332f-af38-738133174ecb | -10.948 | -47.1753 | 2025-09-15 10:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 100.3 |
| ec1a2b6a-f0a5-3ac2-8a6e-b7b72b07e3ad | -12.7818 | -47.1952 | 2025-09-15 10:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 94.7 |
| 80798f03-9d34-3f6b-a6a9-ce4625f3a65b | -6.9798 | -44.5529 | 2025-09-15 10:50:00 | GOES-19 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 92.0 |
| 7d3f43a8-9dcc-32e9-8b32-dde1c8ee8154 | -7.8942 | -43.5857 | 2025-09-15 10:50:00 | GOES-19 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 182.1 |
| c9712e80-c3f7-3688-a12f-eff43f553286 | -7.8756 | -43.5643 | 2025-09-15 10:50:00 | GOES-19 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 428.1 |
| 0ee5f2ca-0e91-3a9a-8f9e-7918f543ef17 | -7.8945 | -43.5623 | 2025-09-15 10:50:00 | GOES-19 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 257.6 |
| fd34c7ec-9d33-37c8-8398-6af0914e48a5 | -12.8003 | -47.2375 | 2025-09-15 10:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 91.2 |
| 8e22966c-e83c-3c0d-8d37-28f558e0b69b | -10.935 | -45.5978 | 2025-09-15 10:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 142.2 |
| a032d66a-5f2c-30f3-a81d-52a33b4e12bb | -12.7814 | -47.2178 | 2025-09-15 10:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 114.7 |
| 4f6609f3-3072-3092-9ce7-22f5b5b6921a | -7.8753 | -43.5876 | 2025-09-15 11:00:00 | GOES-19 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 339.0 |
| 91371b8d-d462-30c0-b730-db37762c147b | -6.9798 | -44.5529 | 2025-09-15 11:00:00 | GOES-19 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 91.7 |
| 8a246459-1c76-31fc-9662-2afd1ef2352a | -7.8945 | -43.5623 | 2025-09-15 11:00:00 | GOES-19 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 305.6 |
| 1280427a-2c77-3d7f-83c5-abc2f8b9fe7c | -7.8942 | -43.5857 | 2025-09-15 11:00:00 | GOES-19 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 171.5 |
| d076bfdf-e496-3bfb-9c8c-3c836b2f5e6a | -10.948 | -47.1753 | 2025-09-15 11:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 139.8 |
| 0db52c6e-8406-3478-834b-1ac5e15de691 | -7.8756 | -43.5643 | 2025-09-15 11:00:00 | GOES-19 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 544.3 |
| 54e9c960-ab76-3106-8c0a-84c76867dc47 | -8.9784 | -45.8344 | 2025-09-15 11:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 81.4 |
| 2453e8a6-3c5b-351a-b67f-b624275f848e | -6.98 | -44.5299 | 2025-09-15 11:00:00 | GOES-19 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 88.0 |
| 054e69d2-974f-379e-9c9e-b6bb33ff63ca | -12.5975 | -45.7251 | 2025-09-15 11:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 125.5 |
| df0d1536-e184-3382-979c-dcf617590ec7 | -7.8942 | -43.5857 | 2025-09-15 11:10:00 | GOES-19 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 186.1 |
| 42c98f32-436a-3a14-b386-acabf09e2101 | -8.6507 | -46.3862 | 2025-09-15 11:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 136.5 |
| 6f8d4373-5430-3438-8999-e48ffce6af78 | -7.8753 | -43.5876 | 2025-09-15 11:10:00 | GOES-19 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 268.8 |
| cc42366c-f4db-34f7-9ff3-454bc8ce537d | -16.673 | -49.7615 | 2025-09-15 11:10:00 | GOES-19 | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 107.1 |
| 5f6bc0ce-8a35-3202-9022-72a1e31f0d63 | -6.9798 | -44.5529 | 2025-09-15 11:10:00 | GOES-19 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 80.3 |
| 979aabc7-c425-3522-90f3-37a047e65ffe | -7.8945 | -43.5623 | 2025-09-15 11:10:00 | GOES-19 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 496.4 |
| 6e22053f-2a1f-3672-a973-ca064c510dfe | -12.8204 | -47.1896 | 2025-09-15 11:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 106.1 |
| 1a77f16e-9f2c-3bc5-b503-06fc50a90114 | -8.651 | -46.3637 | 2025-09-15 11:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 94.8 |
| 1a5ec39c-e516-3493-904f-c4f950e99dc1 | -9.2235 | -44.5052 | 2025-09-15 11:10:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 144.4 |
| ef5978b0-e2e3-39de-bae9-f591874ba568 | -7.8756 | -43.5643 | 2025-09-15 11:10:00 | GOES-19 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 390.8 |
| 35235a16-4f4b-367f-acb2-7a96e3842e0a | -7.90115 | -38.68085 | 2025-09-15 11:17:00 | TERRA_M-M | SÃO JOSÉ DO BELMONTE | PERNAMBUCO | Brasil | 2613503 | 26 | 33 | nan | nan | nan | Caatinga | 21.9 |
| b7c102e7-1b3a-399b-88fb-f4c0e83feae6 | -6.18511 | -41.17854 | 2025-09-15 11:17:00 | TERRA_M-M | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 53.1 |
| 548f4aca-9d17-37e8-9ebc-c89d479dfcc3 | -5.54488 | -37.02541 | 2025-09-15 11:17:00 | TERRA_M-M | AÇU | RIO GRANDE DO NORTE | Brasil | 2400208 | 24 | 33 | nan | nan | nan | Caatinga | 22.8 |
| ed786e45-810f-3cbe-a740-a7623aa1d7c8 | -8.7443 | -37.01 | 2025-09-15 11:17:00 | TERRA_M-M | BUÍQUE | PERNAMBUCO | Brasil | 2602803 | 26 | 33 | nan | nan | nan | Caatinga | 11.1 |
| 01f34cf0-6cb1-3ba1-8c49-d361fee108c1 | -5.50623 | -37.03659 | 2025-09-15 11:17:00 | TERRA_M-M | AÇU | RIO GRANDE DO NORTE | Brasil | 2400208 | 24 | 33 | nan | nan | nan | Caatinga | 14.9 |
| 4d9dac8e-ee88-3251-9dd1-dab9b95d3741 | -6.17406 | -41.18401 | 2025-09-15 11:17:00 | TERRA_M-M | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 73.2 |
| a9d6387e-97ef-3b7c-86aa-0bd0a7b47782 | -5.03472 | -37.79617 | 2025-09-15 11:17:00 | TERRA_M-M | QUIXERÉ | CEARÁ | Brasil | 2311504 | 23 | 33 | nan | nan | nan | Caatinga | 46.6 |
| 758873bb-d11b-3265-8847-904a0b627bcf | -6.95851 | -38.00774 | 2025-09-15 11:17:00 | TERRA_M-M | COREMAS | PARAÍBA | Brasil | 2504801 | 25 | 33 | nan | nan | nan | Caatinga | 16.5 |
| a1945695-8dcc-38c5-916e-f9e8e44ef94d | -4.87509 | -37.99146 | 2025-09-15 11:17:00 | TERRA_M-M | RUSSAS | CEARÁ | Brasil | 2311801 | 23 | 33 | nan | nan | nan | Caatinga | 22.4 |
| 730536b3-c269-383d-b00b-5fe0b6714139 | -3.80798 | -38.9128 | 2025-09-15 11:17:00 | TERRA_M-M | CAUCAIA | CEARÁ | Brasil | 2303709 | 23 | 33 | nan | nan | nan | Caatinga | 42.3 |
| 1d891cb2-0a20-3386-97fd-50bb9d917c35 | -3.80545 | -38.94634 | 2025-09-15 11:17:00 | TERRA_M-M | CAUCAIA | CEARÁ | Brasil | 2303709 | 23 | 33 | nan | nan | nan | Caatinga | 23.5 |
| 7e87e57c-4f28-3241-bdee-c07781f32550 | -12.33898 | -42.60073 | 2025-09-15 11:19:00 | TERRA_M-M | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 36.3 |
| b39a0563-4027-3793-bad9-ea85d6496317 | -12.34322 | -42.63117 | 2025-09-15 11:19:00 | TERRA_M-M | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 43.3 |
| daf22c8e-74ea-309e-96a0-cf80ef6091ff | -8.651 | -46.3637 | 2025-09-15 11:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 117.3 |
| 599c5e1d-5fc7-31c1-be84-f49c8f994c56 | -6.9798 | -44.5529 | 2025-09-15 11:20:00 | GOES-19 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 107.9 |
| 08f6efb0-b4b9-3fe0-b3fc-777846248718 | -7.8942 | -43.5857 | 2025-09-15 11:20:00 | GOES-19 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 287.5 |
| ad3701d3-8d24-30b2-9a8b-fae4d90a4647 | -8.6507 | -46.3862 | 2025-09-15 11:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 154.0 |
| d6654b77-5323-3683-9d66-bab583bcb6ff | -7.8753 | -43.5876 | 2025-09-15 11:20:00 | GOES-19 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 494.7 |
| 921308b2-bd96-3e4f-82ba-7d7f1e8ec2b5 | -12.5975 | -45.7251 | 2025-09-15 11:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 94.9 |
| 018c29a6-cbeb-3911-b3f2-f245cf292195 | -6.2723 | -44.015 | 2025-09-15 11:20:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 90.4 |
| 603f1796-39b8-3353-a6f9-bf08c17cbc70 | -6.98 | -44.5299 | 2025-09-15 11:20:00 | GOES-19 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 81.4 |
| 208d0439-91e8-3a26-b29f-724b6dcab8e9 | -7.8756 | -43.5643 | 2025-09-15 11:20:00 | GOES-19 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 1006.2 |
| df774b3b-f217-31b3-99be-6810d2611256 | -7.8945 | -43.5623 | 2025-09-15 11:20:00 | GOES-19 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 602.5 |
| ee9b73e0-be1f-339f-86d8-dc8563dc8cb4 | -8.6319 | -46.3881 | 2025-09-15 11:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 73.2 |
| bc0cc793-599c-32f5-ac14-8d16cb6ac7fc | -9.2235 | -44.5052 | 2025-09-15 11:30:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 74.4 |
| 0c79aef9-bb61-36f1-96ad-75cbbb68f63b | -9.9388 | -50.2945 | 2025-09-15 11:30:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 85.1 |
| b3b32f68-daa5-3909-a80a-045a8ff59cdd | -6.9798 | -44.5529 | 2025-09-15 11:30:00 | GOES-19 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 125.8 |
| 65c76c0f-b7bf-353f-b2db-136c7594936d | -8.9604 | -45.7686 | 2025-09-15 11:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 71.8 |
| f6227f01-19e4-3faa-8cce-c33377016436 | -8.651 | -46.3637 | 2025-09-15 11:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 79.8 |
| 80f081f8-a2ba-3ab6-92bc-60fd12b69498 | -7.8945 | -43.5623 | 2025-09-15 11:30:00 | GOES-19 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 529.4 |
| 1637052d-b135-309c-bb31-1268870782cf | -8.5944 | -46.3695 | 2025-09-15 11:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 81.7 |
| f54f3af9-ae04-304c-a4ec-f7ecf978ac83 | -6.98 | -44.5299 | 2025-09-15 11:30:00 | GOES-19 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 86.1 |
| 36be8a0b-a18e-3367-9288-904f38d24d63 | -7.8756 | -43.5643 | 2025-09-15 11:30:00 | GOES-19 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 826.6 |
| 2860e362-7c5d-3bb5-8d82-70079a434ddd | -12.5975 | -45.7251 | 2025-09-15 11:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 136.9 |


[Clique aqui para ver as próximas entradas](README68.md)
