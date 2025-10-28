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

## Dados Diários - Página 86

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 74e0a089-607a-3ea5-95ee-488a314d3a48 | -14.53176 | -47.99778 | 2025-10-28 05:06:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 07100a3b-59c3-3b39-bc54-627d95be2302 | -14.55998 | -47.99139 | 2025-10-28 05:06:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6ab8b0e4-58a6-31a4-9b70-fce70cb86d3a | -14.5486 | -47.97989 | 2025-10-28 05:06:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c8c1c1aa-4bbf-3997-a3d5-b2899e42da1c | -14.42614 | -49.42144 | 2025-10-28 05:06:00 | NOAA-20 | PILAR DE GOIÁS | GOIÁS | Brasil | 5216908 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f7d53abc-056c-3ee8-b246-ebcf7592123e | -14.53325 | -47.98462 | 2025-10-28 05:06:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0ea8be83-29b1-3ae6-ab13-9cd493c953e4 | -14.72596 | -47.36347 | 2025-10-28 05:06:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3f908730-f50f-3b3d-b0fb-44ccc7cc582e | -14.53508 | -48.00077 | 2025-10-28 05:06:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 992d7d23-91f7-32ab-9627-9a74c9c42ad5 | -13.73895 | -48.41087 | 2025-10-28 05:06:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 00a8d2e4-b01b-3501-ab47-a96984efb48b | -14.41803 | -47.85721 | 2025-10-28 05:06:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 32c42d69-cfc5-32e2-b573-552e7f12013c | -15.1764 | -47.23052 | 2025-10-28 05:06:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6058d994-74bc-3240-a538-b247072f90d3 | -13.91014 | -48.48904 | 2025-10-28 05:06:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 33cbf84e-0ad5-3b3e-b265-c6a6cc425e45 | -13.73473 | -48.43749 | 2025-10-28 05:06:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 57158b04-a117-3601-84f5-4c3b1af32e3c | -7.9459 | -45.5335 | 2025-10-28 05:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 75.6 |
| 912ac2b7-abaa-35c9-82ed-a06d79eb4666 | -7.9461 | -45.5108 | 2025-10-28 05:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 65.7 |
| 4e6c60e6-9441-3606-93d6-77ba3ff4f225 | -4.4632 | -43.2386 | 2025-10-28 05:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 44.1 |
| e1fc9684-1c6e-332a-ac17-55cd60ddd448 | -2.7556 | -45.3995 | 2025-10-28 05:10:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 61438707-7aa9-3903-aed7-58b8aae763b8 | -11.2798 | -45.5052 | 2025-10-28 05:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 61.0 |
| a9aef6bc-27fa-33e3-8227-0b7a576e47ee | -7.9461 | -45.5108 | 2025-10-28 05:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 78.5 |
| 238de009-2fbe-3f61-b95a-c43c56e27ec3 | -2.7556 | -45.3995 | 2025-10-28 05:20:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 50.2 |
| c8840b67-6558-3700-8f5c-61d9cdd9684e | -7.9459 | -45.5335 | 2025-10-28 05:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 121.0 |
| c526d8b2-b111-36c1-b16d-dfa4e4d872df | -7.9693 | -46.7423 | 2025-10-28 05:20:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 26.9 |
| f6d380ad-6bbd-3b54-a1f3-9c6ee4991360 | -2.7556 | -45.3995 | 2025-10-28 05:30:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 50.0 |
| 69aa503c-82b5-30a5-9458-ba06364de632 | -4.4632 | -43.2386 | 2025-10-28 05:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 47.8 |
| 19da2c85-7054-3f1b-914d-25e8c08b8b47 | -4.4632 | -43.2386 | 2025-10-28 05:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 43.3 |
| 6e119569-a903-3cda-9f6f-4225a9e487cd | 1.59052 | -55.73246 | 2025-10-28 05:53:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f00b7d5e-68c2-326f-bcda-d24549932199 | -1.70317 | -53.69017 | 2025-10-28 05:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9678d9e1-80ed-39be-b1c9-92dc711ac02f | 3.95116 | -59.64325 | 2025-10-28 05:53:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 282a16d9-f5a6-39f3-9266-cd67b3c03086 | 3.94677 | -59.64399 | 2025-10-28 05:53:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d45d4a10-c7d8-36bc-b88d-0b5ad5538657 | 1.59576 | -55.7271 | 2025-10-28 05:53:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bfe62390-2d94-3ea4-aa45-21bb52a7708e | 2.34402 | -60.21522 | 2025-10-28 05:53:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 80e18a21-4d71-377d-a062-0b8378fb3c50 | -5.33998 | -60.18165 | 2025-10-28 05:53:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d34062cf-9d97-3f69-b864-609b2a89824d | 2.6809 | -60.16592 | 2025-10-28 05:53:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 28a5cecf-79a0-3bc8-9a1d-08a1e50c5958 | -4.96691 | -56.27279 | 2025-10-28 05:55:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| d99261a1-9f15-3d08-b125-b4c3776e84ed | -7.93857 | -45.51981 | 2025-10-28 06:14:00 | AQUA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 31.3 |
| 74d46bf6-2dd9-3730-a02f-4050f8b89242 | -4.45551 | -43.63393 | 2025-10-28 06:14:00 | AQUA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 42.1 |
| dcedc61b-b076-3728-a02f-3a749f905ece | -9.27291 | -45.57189 | 2025-10-28 06:14:00 | AQUA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 85fef5b7-fd13-3951-86a6-0817e2424d2a | -7.95214 | -45.50601 | 2025-10-28 06:14:00 | AQUA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 70a6f5b9-d1a3-3fef-a802-a83a565083e4 | -4.45352 | -43.6283 | 2025-10-28 06:14:00 | AQUA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 27.4 |
| 762d0379-6857-32da-8f0d-7c02e3cd1fc5 | -4.4584 | -43.22955 | 2025-10-28 06:14:00 | AQUA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 63.3 |
| c76f3287-c056-3d21-8ee9-4ab5805cc400 | -7.29186 | -45.06017 | 2025-10-28 06:14:00 | AQUA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 38.4 |
| 17b914fb-9b23-3cf0-beab-98a4386feccb | -5.70041 | -49.1907 | 2025-10-28 06:14:00 | AQUA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 03328dde-d388-3ba5-9cb1-262731ec6c43 | -4.19761 | -48.36025 | 2025-10-28 06:14:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 4b7e361d-d2b1-3a94-b831-29755f86d489 | -5.62955 | -47.61519 | 2025-10-28 06:14:00 | AQUA_M-M | SÍTIO NOVO DO TOCANTINS | TOCANTINS | Brasil | 1720804 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 1b94ace9-408d-39ae-8504-da13c43d018f | -7.92812 | -49.73626 | 2025-10-28 06:14:00 | AQUA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| fdeb5a6a-ee21-3721-9003-47e60eb792e4 | -7.9589 | -47.24575 | 2025-10-28 06:14:00 | AQUA_M-M | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 500c8139-4ee1-3a68-a841-402a4ce10e1a | -7.80835 | -46.44194 | 2025-10-28 06:14:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 25.6 |
| d1e1bd50-1cd2-3291-ada8-b20f711b4d12 | -7.93641 | -45.53522 | 2025-10-28 06:14:00 | AQUA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 56.5 |
| 6ed8cb6e-07d0-3273-afd6-85a810a02de8 | -7.94781 | -45.53669 | 2025-10-28 06:14:00 | AQUA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 32.7 |
| f0509e7b-ce99-31ac-a7b0-50c9dc6eccab | -6.69533 | -42.0304 | 2025-10-28 06:14:00 | AQUA_M-M | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 40.2 |
| c8aab390-34a2-318e-b688-385c7a5bc1bb | -9.22176 | -46.35784 | 2025-10-28 06:14:00 | AQUA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 8aa4e006-9f93-34a9-af27-9ef92aa7e009 | -5.10381 | -48.47778 | 2025-10-28 06:14:00 | AQUA_M-M | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 1dea2a56-d714-3e8d-8967-88affe9400de | -8.6373 | -45.28675 | 2025-10-28 06:14:00 | AQUA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 31.4 |
| 67322c49-1d7d-3c38-b77b-14557d3459e9 | -6.48703 | -42.20805 | 2025-10-28 06:14:00 | AQUA_M-M | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 17.3 |
| bd0fd227-d094-3ecb-bff8-ea40cd7f1684 | -9.21972 | -48.60122 | 2025-10-28 06:14:00 | AQUA_M-M | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 78717344-0b66-3ac7-8516-48ec1516fe22 | -2.4347 | -49.75269 | 2025-10-28 06:14:00 | AQUA_M-M | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 0a3f841a-dfa6-3de9-ba3c-313a5d18eabc | -8.19299 | -44.43472 | 2025-10-28 06:14:00 | AQUA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 28.7 |
| b68d6f70-6868-3861-84e7-ccb51f365750 | -7.77491 | -45.37598 | 2025-10-28 06:14:00 | AQUA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 8b90f64c-4c59-3f07-b406-e96272b81f57 | -8.57303 | -47.02233 | 2025-10-28 06:14:00 | AQUA_M-M | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| a0ff49cb-6584-3172-999c-ebae7d0ab310 | -7.3482 | -47.64611 | 2025-10-28 06:14:00 | AQUA_M-M | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 66af46b3-9871-30cf-b456-6e99d0f97426 | -7.34967 | -47.6359 | 2025-10-28 06:14:00 | AQUA_M-M | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| f2f2e32c-cd66-3d78-bc95-8000ec54b85e | -2.80519 | -49.13791 | 2025-10-28 06:14:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 1f5bb582-25d6-30a2-98f3-4e182eb20761 | -8.6396 | -45.27031 | 2025-10-28 06:14:00 | AQUA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 13.8 |
| aa5bf975-5f3a-3ce4-880f-97fa3e0e3240 | -2.42066 | -48.43825 | 2025-10-28 06:14:00 | AQUA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| abf4d250-27e2-31eb-a1e0-d85081355d63 | -7.83516 | -46.40565 | 2025-10-28 06:14:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 18.1 |
| f45b3f41-563c-3e20-bf8b-103f7956e895 | -3.57793 | -43.62069 | 2025-10-28 06:14:00 | AQUA_M-M | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 21.9 |
| 53d55385-f82f-3e83-8dc9-45845747027b | -2.74635 | -45.40887 | 2025-10-28 06:14:00 | AQUA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 14.1 |
| fd79ee69-4983-37ac-a0e1-38fd74ec9a5b | -4.45293 | -43.65276 | 2025-10-28 06:14:00 | AQUA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 741703e4-452a-3292-8e18-21446288efd6 | -7.96694 | -46.74368 | 2025-10-28 06:14:00 | AQUA_M-M | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 19.1 |
| e12b9932-bf49-397e-9b33-ae5478dd760a | -7.29853 | -45.06819 | 2025-10-28 06:14:00 | AQUA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 0400f260-d4cb-3379-b8a1-9c392a2e70e0 | -3.26532 | -44.51894 | 2025-10-28 06:14:00 | AQUA_M-M | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 19.4 |
| a86b05bd-d3ea-3af2-9784-a99e8dd2b99f | -4.0987 | -48.02557 | 2025-10-28 06:14:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| f398f4d7-161a-3c20-8ef7-34daecb431af | -8.693 | -50.79992 | 2025-10-28 06:14:00 | AQUA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| aaf9e4d5-a23c-368c-abde-9910e3ba4561 | -7.98369 | -46.19218 | 2025-10-28 06:14:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 24e53819-612b-3514-b748-a52eb4f17eef | -3.46634 | -49.96974 | 2025-10-28 06:14:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 589dcb70-87a8-33a6-a497-6bc6e20c7f73 | -4.22461 | -48.36417 | 2025-10-28 06:14:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 64842de6-f6d5-3f6b-b558-4d583b0a7fe3 | -8.70393 | -47.97432 | 2025-10-28 06:14:00 | AQUA_M-M | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 2fa704bf-c935-360a-a5c5-d9dab820847d | -8.63522 | -45.27528 | 2025-10-28 06:14:00 | AQUA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 19.1 |
| bbf2bb10-72b8-34c0-8aac-8f05fa954b80 | -7.83022 | -46.39848 | 2025-10-28 06:14:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 3dc88d33-d13f-3dd2-8c95-0386ba246d34 | -8.18264 | -44.43851 | 2025-10-28 06:14:00 | AQUA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 30.0 |
| 438d4ea9-2a10-3951-ab95-72f3f98da09d | -7.81523 | -46.46925 | 2025-10-28 06:14:00 | AQUA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 16.7 |
| bc1d49d7-d543-3cdb-bade-fa8e19bed0f8 | -7.26359 | -45.00618 | 2025-10-28 06:14:00 | AQUA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 9de471be-f46d-3af3-8ed4-3bcc954189de | -7.28683 | -45.06651 | 2025-10-28 06:14:00 | AQUA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 09fc024b-4410-3a89-b466-971c09b61a81 | -7.94997 | -45.52139 | 2025-10-28 06:14:00 | AQUA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 15f1f32f-be96-370a-a9e9-ec7e74e8a135 | -4.45078 | -43.64717 | 2025-10-28 06:14:00 | AQUA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 31.0 |
| c213be51-e0e3-34b1-b953-ed3584266350 | -4.267 | -48.69352 | 2025-10-28 06:14:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ce097f30-38ff-3c92-92d5-7a6b3ca9eb5a | -6.69488 | -42.02547 | 2025-10-28 06:14:00 | AQUA_M-M | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 35.0 |
| 4ca2d028-ba36-3a20-9cac-f05b581e5143 | -6.48911 | -42.21348 | 2025-10-28 06:14:00 | AQUA_M-M | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 18.8 |
| 2abba441-103f-3322-bb41-7cc472f5085f | -8.70178 | -50.80123 | 2025-10-28 06:14:00 | AQUA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| fb411c10-54d0-34c7-9693-ae1176062e0a | -7.30073 | -45.05191 | 2025-10-28 06:14:00 | AQUA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 278ce10d-6a91-3b2a-80f0-83d8c4b7e432 | -7.80468 | -46.46774 | 2025-10-28 06:14:00 | AQUA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 19.5 |
| be2a513c-4269-30f9-8596-6b533f5fee09 | -2.75876 | -45.39753 | 2025-10-28 06:14:00 | AQUA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 31.0 |
| 279c76ae-18c4-3483-8802-5db4c286a09c | -7.96971 | -46.74994 | 2025-10-28 06:14:00 | AQUA_M-M | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 24.2 |
| 8ebd0cc4-4010-37bf-ae4b-80bb5497b7bc | -7.80285 | -46.48059 | 2025-10-28 06:14:00 | AQUA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 444fee29-c1b1-31b3-8de1-59f2b8e0b233 | -7.44986 | -49.40794 | 2025-10-28 06:14:00 | AQUA_M-M | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 22.3 |
| 48322688-4716-33f2-b233-4b0fb12893a2 | -7.4512 | -49.39887 | 2025-10-28 06:14:00 | AQUA_M-M | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| af3040a6-c183-3d10-a971-091e8a3511f7 | -7.96522 | -46.7562 | 2025-10-28 06:14:00 | AQUA_M-M | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 24.2 |
| 178e893c-2b84-39ee-bfe7-cca3b393894b | -8.63306 | -45.29163 | 2025-10-28 06:14:00 | AQUA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 7e3fa364-4cac-3969-9013-d42258f891ab | -7.96052 | -47.23445 | 2025-10-28 06:14:00 | AQUA_M-M | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 5df4f347-e5d5-3e04-8875-c0f0fa40f407 | -3.57441 | -49.43176 | 2025-10-28 06:14:00 | AQUA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| e24bad3d-bf92-333e-9d74-0840f58e78ef | -7.07766 | -44.93638 | 2025-10-28 06:14:00 | AQUA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 22.8 |


[Clique aqui para ver as próximas entradas](README87.md)
