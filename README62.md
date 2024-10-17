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

## Dados Diários - Página 62

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| db0b4e66-563a-398e-af74-971130a34b68 | -9.30817 | -68.04558 | 2024-10-17 05:53:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 07ac44e6-5366-3066-ba01-dcb524ac9697 | -9.07071 | -67.73031 | 2024-10-17 05:53:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f21617dc-bdb9-38a6-8974-e83878d130f7 | -9.05821 | -67.83495 | 2024-10-17 05:53:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1b857737-4d05-3497-a687-51e25c3c5357 | -9.0554 | -67.83083 | 2024-10-17 05:53:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ffb48eff-2760-3201-bb86-4fdf8b646710 | -9.05486 | -67.83441 | 2024-10-17 05:53:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b5593a39-7f1e-3a09-a64d-1dd007ae97a1 | -8.97884 | -67.49762 | 2024-10-17 05:53:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bdec90df-9283-3475-bc78-33f7efcac96e | -8.943 | -67.61833 | 2024-10-17 05:53:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 59b92338-cef1-34d9-bede-421d379fd043 | -8.92206 | -67.82114 | 2024-10-17 05:53:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ac059060-71a8-334a-855f-64c042fc6085 | -9.41332 | -67.8454 | 2024-10-17 05:53:00 | NOAA-20 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8b8d016d-c52a-36c1-bf07-ab9114c7a06a | -9.3809 | -68.25619 | 2024-10-17 05:53:00 | NOAA-20 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| be698b17-b2c9-3c64-80ca-3ec493f1194b | -9.37703 | -68.25919 | 2024-10-17 05:53:00 | NOAA-20 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 30cd058e-ca8d-3c1a-b754-8c33232a213f | -9.30227 | -68.15006 | 2024-10-17 05:53:00 | NOAA-20 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f616696b-2f87-36cf-aab4-f1a422e1bff5 | -9.302 | -68.30558 | 2024-10-17 05:53:00 | NOAA-20 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9deb537c-a0bc-32f9-8900-8472cbdc0f59 | -9.27325 | -68.33716 | 2024-10-17 05:53:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 859b491a-3c15-3b4f-b8dd-d7de1131503f | -9.26993 | -68.33663 | 2024-10-17 05:53:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5d393507-108a-3dd4-82e6-77a432f871fc | -9.2661 | -68.36126 | 2024-10-17 05:53:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f32b7039-ce27-3697-ad9d-0341273843d8 | -9.22566 | -68.15982 | 2024-10-17 05:53:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 306f62e0-de2b-354a-b978-eb4a973bf6de | -9.22512 | -68.16336 | 2024-10-17 05:53:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d2b4c2bd-9d49-358c-b109-ba729085f0c6 | -9.16473 | -67.67841 | 2024-10-17 05:53:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 211369e4-5e21-368b-8166-204deb244ecc | -9.16136 | -67.67789 | 2024-10-17 05:53:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b0312363-974e-306e-ba2c-5981d8ccc717 | -9.07743 | -67.73135 | 2024-10-17 05:53:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d9d06baa-0dc8-38ad-a02e-fd98c5200a2d | -9.07407 | -67.73083 | 2024-10-17 05:53:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| affc0dd6-2676-38a8-aba7-6dbc5b184dd0 | -9.05875 | -67.83136 | 2024-10-17 05:53:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ca3537ea-7623-3746-971b-89ab77727502 | -9.03409 | -68.12617 | 2024-10-17 05:53:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4e057b98-60e5-3ea7-933e-a3c36c803cc7 | -9.03355 | -68.12971 | 2024-10-17 05:53:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6f809e5a-90e2-3226-a456-f2ba62815d23 | -9.03022 | -68.12919 | 2024-10-17 05:53:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f5e2bf87-ac42-3340-9655-d456552ce5a3 | -8.97546 | -67.4971 | 2024-10-17 05:53:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 2c0c0024-aaea-3592-b73a-d110870fb7a7 | -8.97362 | -67.35079 | 2024-10-17 05:53:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6692f5de-d1c5-3b14-917d-c59cbcdcf9a4 | -8.80662 | -67.62038 | 2024-10-17 05:53:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 79bcb1ce-4216-320e-a96b-1db10cf0b3bb | -8.80271 | -67.62346 | 2024-10-17 05:53:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1aee9970-0240-3d36-9e62-8dccb50fbafe | -9.30731 | -68.72957 | 2024-10-17 05:53:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4c4d0b8d-d39d-33b6-9316-8ffda646c521 | -9.20281 | -68.48428 | 2024-10-17 05:53:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1b1ee149-6f5b-3355-aaef-846e9c5145b1 | -9.15254 | -68.67678 | 2024-10-17 05:53:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 572d0d7a-d130-3e6b-b2c7-ced86e112e92 | -9.15199 | -68.68027 | 2024-10-17 05:53:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2a7c39f1-da54-32a3-9519-0883db0a65e7 | -9.14814 | -68.68324 | 2024-10-17 05:53:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d2badf03-d465-39db-b998-0fb375cb2663 | -9.1476 | -68.68672 | 2024-10-17 05:53:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8f8ccfcb-c70f-3d3f-9bcf-51f0c7f635ee | -9.08527 | -68.47653 | 2024-10-17 05:53:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| a0a60901-54dc-3a83-ba7a-fdb9aba99bd8 | -9.04499 | -68.51654 | 2024-10-17 05:53:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 12a3a094-542c-3667-a995-78d6dd1417b8 | -9.03505 | -68.51498 | 2024-10-17 05:53:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 81ccb183-5e6c-33ad-a864-da851c672b53 | -8.94631 | -68.56185 | 2024-10-17 05:53:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| eae05027-1d6a-3cfd-a298-a88a7d1d3c8a | -8.94436 | -68.66154 | 2024-10-17 05:53:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8460f4eb-e08e-316c-96ef-7b6c88c81816 | -8.94246 | -68.56481 | 2024-10-17 05:53:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a1d32d5b-597c-3221-a773-12f00b1dc75b | -8.89707 | -68.50764 | 2024-10-17 05:53:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 43d5560a-4e5a-330e-af73-0155d8beb525 | -8.88271 | -68.75164 | 2024-10-17 05:53:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 52757eb0-3a8c-3c68-8b17-982d55eb5817 | -8.88216 | -68.75512 | 2024-10-17 05:53:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d81d6fe8-07bb-3852-8151-ff81f3c2e43a | -8.88108 | -68.76208 | 2024-10-17 05:53:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5574bab8-7235-37ae-a571-64f2b04a39f9 | -8.84175 | -68.66676 | 2024-10-17 05:53:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 16000786-56a9-3783-b0e6-b4896052cd38 | -9.95644 | -68.922 | 2024-10-17 05:53:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9e1170cf-61d3-31b5-928f-3b9d26ccef92 | -9.95259 | -68.92497 | 2024-10-17 05:53:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 863b9ca1-92f1-3b32-951a-bc800155c8ff | -9.95204 | -68.92846 | 2024-10-17 05:53:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8ca83909-d187-393f-a1f8-1902b84344c6 | -9.93891 | -68.99075 | 2024-10-17 05:53:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 68f4df89-5605-3c97-a321-0af49fdfe05e | -9.93837 | -68.99424 | 2024-10-17 05:53:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 145b603f-d793-3de9-b3c3-31843d4dc476 | -9.87054 | -68.7756 | 2024-10-17 05:53:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 81ee28c7-1203-3611-87a9-b17756ba0ada | -9.86723 | -68.77508 | 2024-10-17 05:53:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 25116203-be41-3dcb-afd3-7b8768d3187f | -9.76731 | -68.80644 | 2024-10-17 05:53:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0c02685a-3040-3a00-b062-309e3b866a68 | -9.76622 | -68.81344 | 2024-10-17 05:53:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e84ae4e7-3c20-325d-8fd9-3c77c854ac00 | -9.73938 | -68.41748 | 2024-10-17 05:53:00 | NOAA-20 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1b20d359-e7bc-339e-9674-eba575fc5d64 | -9.72199 | -68.53013 | 2024-10-17 05:53:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2551cc46-3ca4-3ec7-855e-28ef8a48c497 | -9.68516 | -68.59238 | 2024-10-17 05:53:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 091d5192-4d7a-3092-9d34-577e23386b06 | -9.68185 | -68.59187 | 2024-10-17 05:53:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9da00742-e873-3825-8e65-bb250c3d0ff0 | -9.6813 | -68.59537 | 2024-10-17 05:53:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 55040d0f-5d60-386e-b404-41528f69b8bb | -9.67908 | -68.58784 | 2024-10-17 05:53:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b0f41b54-0b2f-3263-98bf-127ba453ec82 | -9.67853 | -68.59134 | 2024-10-17 05:53:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4e754ca7-4bd0-3839-9be6-2b668c578a70 | -9.67244 | -68.58679 | 2024-10-17 05:53:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 470ba81a-d91d-3318-b3f6-b9b972c546c8 | -9.66913 | -68.58627 | 2024-10-17 05:53:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e7a49fab-599f-379a-92ba-8848ce53bd0d | -9.66741 | -68.55364 | 2024-10-17 05:53:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e82c76cf-93d9-32f9-81d2-c8b50584b3c8 | -9.66413 | -68.5747 | 2024-10-17 05:53:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 03fe41d4-bb09-39ca-9503-c849087d8fd8 | -9.65736 | -68.50888 | 2024-10-17 05:53:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e0980400-e40c-3fbc-998d-c89a37306afa | -9.65586 | -68.58417 | 2024-10-17 05:53:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 632bd5cb-df15-36a4-b04c-cd9c5de4f4b9 | -9.65532 | -68.58767 | 2024-10-17 05:53:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 653ddb98-2631-325a-a50f-d8650fc6be70 | -9.65418 | -68.57313 | 2024-10-17 05:53:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8490db89-7aca-30ca-8f11-f7868dc22dbd | -9.65205 | -68.60872 | 2024-10-17 05:53:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 198719ff-796c-3a76-8c42-492e2a2c1766 | -9.6515 | -68.61222 | 2024-10-17 05:53:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e1162eea-0467-37f7-8a49-6478edf7aaeb | -9.64923 | -68.58311 | 2024-10-17 05:53:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e96b9b3c-2592-3260-8573-abb95bf2168b | -9.64819 | -68.6117 | 2024-10-17 05:53:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 98a88b4a-bbcc-3dfc-95a2-40f680c18d20 | -9.6323 | -68.67019 | 2024-10-17 05:53:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 78ea452d-15a7-3d5f-8903-7bb6b2fbd614 | -9.6235 | -68.68313 | 2024-10-17 05:53:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6b26645f-2d98-3740-8959-2212127150c2 | -9.58957 | -68.50907 | 2024-10-17 05:53:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3aa5d179-632f-3163-a655-75f54d67316f | -9.5883 | -68.73486 | 2024-10-17 05:53:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a888850e-f9e5-31e6-9ad5-81c1ffee6d2e | -9.58776 | -68.73836 | 2024-10-17 05:53:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0ebb442b-0f3f-33b7-ae37-9f4d7837ab66 | -9.5852 | -68.53716 | 2024-10-17 05:53:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 307c74f7-2519-39af-975d-3c26aced8074 | -9.57075 | -68.49892 | 2024-10-17 05:53:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 50473935-4b13-39dc-9a74-dba343ce5ebc | -9.56764 | -68.60625 | 2024-10-17 05:53:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f4a4d9a6-0719-3b44-a457-600a602a360b | -9.56432 | -68.60572 | 2024-10-17 05:53:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 97d13926-5899-360e-b444-46cc295e5d92 | -9.53172 | -68.59699 | 2024-10-17 05:53:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f3c0bb90-a85e-3e46-a182-9a0605b3bb6f | -9.53041 | -68.75793 | 2024-10-17 05:53:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e19ee225-8fef-324d-95c1-b633a4132852 | -9.52483 | -68.72842 | 2024-10-17 05:53:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6c958a51-3857-3375-8f6a-4cf96e27a130 | -9.51318 | -68.47548 | 2024-10-17 05:53:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8f780d3d-a9e3-367f-a0e5-4afab6cd8ee0 | -9.51009 | -68.56127 | 2024-10-17 05:53:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0737137f-f610-330d-a034-33e739fe73aa | -9.48352 | -68.53529 | 2024-10-17 05:53:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| db5c35c4-0da5-342a-8d45-aa240585dd5f | -9.47806 | -68.57033 | 2024-10-17 05:53:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2230a708-6bd4-373a-a052-4ccc34dccc8f | -9.47752 | -68.57383 | 2024-10-17 05:53:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9a4cc73e-0cfc-3827-89db-c35416711f4a | -9.4742 | -68.5733 | 2024-10-17 05:53:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ab60d703-4d38-3e45-9f09-431571923f99 | -9.4674 | -68.48603 | 2024-10-17 05:53:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| db686ba3-1a08-3895-9bee-d40ececb2d3e | -9.46362 | -68.53217 | 2024-10-17 05:53:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7dd06d27-3a15-34c9-bb33-dc6cee7b45ee | -9.46331 | -68.84027 | 2024-10-17 05:53:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d0d71542-46fe-3be4-a6d6-5da783877f61 | -9.45817 | -68.56721 | 2024-10-17 05:53:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3d1c44e1-8284-3730-befe-caa193544044 | -9.45758 | -68.54917 | 2024-10-17 05:53:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9c79010f-1054-3bf3-a056-5df81e45c4cd | -9.45704 | -68.55267 | 2024-10-17 05:53:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4e9bafa2-ffa7-3678-a53b-a59660f9c603 | -9.4554 | -68.56318 | 2024-10-17 05:53:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README63.md)
