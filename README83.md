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

## Dados Diários - Página 83

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 413e31b1-58a4-3ee4-ab35-0a5d7783d238 | -3.9961 | -43.2418 | 2024-10-15 14:05:28 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 74.9 |
| 629423c4-dbc3-3f0c-b5c8-a2c6eb70f38c | -4.0148 | -43.2408 | 2024-10-15 14:05:29 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 147.6 |
| 91356bec-e89a-374d-a433-a89c6c894d13 | -9.1131 | -47.0741 | 2024-10-15 14:05:57 | GOES-16 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 88.8 |
| 3290a4e4-ef34-3abd-b186-a02136a90812 | -9.1137 | -47.0296 | 2024-10-15 14:05:57 | GOES-16 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 81.2 |
| 31c49f14-f9af-31c7-a4aa-635572ff0796 | -9.2012 | -47.5516 | 2024-10-15 14:05:58 | GOES-16 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 96.8 |
| 5da072eb-0d7f-3433-90ef-eba3f9d6f16f | -9.45 | -45.8951 | 2024-10-15 14:05:59 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 169.8 |
| 65c6ec16-fddf-3880-960c-3f2d47e1b8f7 | -9.4366 | -44.1787 | 2024-10-15 14:05:59 | GOES-16 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 177.3 |
| c8f01793-437f-30d8-8369-37ffca6e703b | -9.4484 | -46.0082 | 2024-10-15 14:05:59 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 79.4 |
| f7da8f31-8455-3a47-904c-2b502f3b6641 | -9.4175 | -45.5134 | 2024-10-15 14:05:59 | GOES-16 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 87.6 |
| 680419d2-dafc-3506-9360-28a8130decdf | -9.456 | -44.1531 | 2024-10-15 14:05:59 | GOES-16 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 87.0 |
| 237862e2-70a8-3d68-b7b7-df8d5b4b2eb2 | -9.5798 | -43.4835 | 2024-10-15 14:06:00 | GOES-16 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 107.8 |
| 19279745-4583-3a3a-95f7-6eb2793f1e65 | -9.7064 | -46.4963 | 2024-10-15 14:06:01 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 110.2 |
| 9c19c1bc-06dd-313b-b4dc-da1b44f44fee | -9.7067 | -46.4738 | 2024-10-15 14:06:01 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 108.5 |
| 32f6b752-f6a4-3f80-8e65-210df86c7363 | -9.9777 | -47.3795 | 2024-10-15 14:06:02 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 149.5 |
| e471cf86-91ab-3b51-bf2d-ccaad3c670bd | -9.9597 | -47.315 | 2024-10-15 14:06:02 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 153.6 |
| c7e80667-12c8-3140-ba48-7482d6b1b55d | -9.997 | -47.3551 | 2024-10-15 14:06:02 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 151.2 |
| 23a03dd4-f5a3-37c6-a797-8a5a24eae1a3 | -10.0498 | -47.6368 | 2024-10-15 14:06:03 | GOES-16 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 147.6 |
| cd68b56f-2e57-3f28-8176-1a4af56a929e | -10.0355 | -47.3064 | 2024-10-15 14:06:03 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 252.2 |
| cefe40db-cb1a-314b-8f17-e9a27be660b7 | -10.016 | -47.353 | 2024-10-15 14:06:03 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 141.7 |
| 72543343-1fc3-3f74-a40a-5cec10697222 | -10.0349 | -47.3508 | 2024-10-15 14:06:03 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 158.8 |
| 157bbab8-57db-3cce-80ef-6c605d15c2d8 | -10.0539 | -47.3487 | 2024-10-15 14:06:03 | GOES-16 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 144.4 |
| de97c544-28f3-341b-a9d6-4a4622ca1217 | -10.0548 | -47.282 | 2024-10-15 14:06:03 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 129.2 |
| 904a38c9-cce5-34b5-9a77-2ce8db266b54 | -10.0362 | -47.2619 | 2024-10-15 14:06:03 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 183.0 |
| 4b70c920-36b8-3fb0-a7b4-a4de08265cd5 | -10.0163 | -47.3308 | 2024-10-15 14:06:03 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 164.3 |
| dda7984c-ddc3-3f0f-8de1-30665de6ac5d | -10.2635 | -47.2579 | 2024-10-15 14:06:04 | GOES-16 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 140.6 |
| 6aa6f93b-b9fa-329a-b5bd-5bc14602049a | -10.2632 | -47.2802 | 2024-10-15 14:06:04 | GOES-16 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 207.7 |
| 0e072f61-87c9-3191-8c20-8265d01af4e4 | -10.2638 | -47.2357 | 2024-10-15 14:06:04 | GOES-16 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 143.8 |
| c07f7973-17bb-38ea-962c-e4beb91926fd | -10.2641 | -47.2134 | 2024-10-15 14:06:04 | GOES-16 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 145.3 |
| c775fb79-71aa-34dc-9769-739d5e84791d | -10.9307 | -44.7021 | 2024-10-15 14:06:07 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 104.7 |
| ffc66353-2c71-3c94-8b15-6be8f30b5289 | -11.0661 | -45.7399 | 2024-10-15 14:06:08 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 190.0 |
| da8c1072-388c-3a9e-95d0-35264eb91206 | -10.9358 | -45.5521 | 2024-10-15 14:06:08 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 126.0 |
| c1b47c61-527e-3537-9722-da12fe8ba084 | -11.1064 | -44.4687 | 2024-10-15 14:06:08 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 107.8 |
| 9e17931e-e8ba-383d-ade6-ee56310e80f6 | -10.9502 | -44.6762 | 2024-10-15 14:06:08 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 99.7 |
| 03db63d7-6584-3582-83e2-e1aed0c7eee5 | -10.9361 | -45.5292 | 2024-10-15 14:06:08 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 113.0 |
| 2b04be7e-c6d2-3fee-a1ac-1cf7f931c366 | -12.3167 | -45.3314 | 2024-10-15 14:06:15 | GOES-16 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 119.7 |
| 9f799db4-c21c-3c87-a1c7-ca1548b2712b | -12.2974 | -45.3343 | 2024-10-15 14:06:15 | GOES-16 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 109.1 |
| 4c286e60-fb43-3e2b-93d1-876e797bb85e | -1.5252 | -47.7037 | 2024-10-15 14:15:15 | GOES-16 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 129.9 |
| b47bd1b0-025d-3ff2-adea-48b548f24e3f | -3.9961 | -43.2418 | 2024-10-15 14:15:28 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 100.1 |
| da89aa3c-8d91-36d8-b55a-89a99b142bda | -4.0148 | -43.2408 | 2024-10-15 14:15:29 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 131.9 |
| 6e231683-3640-3703-9b4f-423a77bf992c | -4.2871 | -44.4029 | 2024-10-15 14:15:30 | GOES-16 | ALTO ALEGRE DO MARANHÃO | MARANHÃO | Brasil | 2100436 | 21 | 33 | nan | nan | nan | Cerrado | 78.5 |
| c8401b44-abc6-363a-a447-cce574311993 | -5.6784 | -43.3892 | 2024-10-15 14:15:38 | GOES-16 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 73.2 |
| 4b0d412b-e611-3022-896a-0c27b98cf6bd | -9.1137 | -47.0296 | 2024-10-15 14:15:57 | GOES-16 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 80.6 |
| 9eaa286b-d678-3e0d-9cca-f462d670bbad | -9.1131 | -47.0741 | 2024-10-15 14:15:57 | GOES-16 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 84.6 |
| 3be13c4a-b081-3555-b560-2d3b9ee61bb9 | -9.2012 | -47.5516 | 2024-10-15 14:15:58 | GOES-16 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 117.8 |
| b4dbff9c-e8c3-3f69-89da-99293fd3d14b | -9.45 | -45.8951 | 2024-10-15 14:15:59 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 103.8 |
| 375a9a65-a995-31a7-9b87-726221670864 | -9.4699 | -45.8249 | 2024-10-15 14:15:59 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 114.7 |
| 3db6cd21-1493-3660-b385-571410baf7e3 | -9.4696 | -45.8476 | 2024-10-15 14:15:59 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 97.6 |
| 642f221c-25d5-3dbf-8cb1-e81bf65b5017 | -9.4292 | -46.0329 | 2024-10-15 14:15:59 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 78.7 |
| e14fe406-1d7d-34d9-a8a7-19828caa3513 | -9.4509 | -45.8271 | 2024-10-15 14:15:59 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 100.8 |
| c0e157f4-0056-3be4-acd9-a83840e56e79 | -9.4484 | -46.0082 | 2024-10-15 14:15:59 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 82.8 |
| f98e5e05-de50-3bca-b5b5-63fa09be5d64 | -9.4295 | -46.0103 | 2024-10-15 14:15:59 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 90.7 |
| 90bdd15e-33df-3d2b-adba-ca70059f2eab | -9.4175 | -45.5134 | 2024-10-15 14:15:59 | GOES-16 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 82.0 |
| adfe591f-a5f3-37b8-a329-7dd1cf754403 | -9.4702 | -45.8023 | 2024-10-15 14:15:59 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 94.6 |
| 8ab5bfbc-bfcd-368f-97ba-6b8dfec84c20 | -9.4888 | -45.8228 | 2024-10-15 14:15:59 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 81.8 |
| f092741d-07e9-382c-9f92-ad94d6478ae1 | -9.4503 | -45.8724 | 2024-10-15 14:15:59 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 148.0 |
| 39d83398-792a-3624-a7fa-21ff05b36ddc | -9.5915 | -46.5989 | 2024-10-15 14:16:00 | GOES-16 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 111.4 |
| b90659ff-3cc1-3f64-9565-f3dc2f622384 | -9.5909 | -46.6437 | 2024-10-15 14:16:00 | GOES-16 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 96.3 |
| 1c23a129-61f2-318d-af3f-07a0c7beb700 | -9.5912 | -46.6213 | 2024-10-15 14:16:00 | GOES-16 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 113.0 |
| dfcf6c04-8e13-3c86-ae5c-21a3263f57ae | -9.5798 | -43.4835 | 2024-10-15 14:16:00 | GOES-16 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 89.3 |
| 3afd70f0-9f32-3da7-aa8c-fe1b68d19d8b | -9.7064 | -46.4963 | 2024-10-15 14:16:01 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 118.4 |
| c7ace77e-c8ca-3888-a38a-c62ab4cc4a48 | -9.8883 | -47.0119 | 2024-10-15 14:16:02 | GOES-16 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 114.9 |
| 77cbc403-7d64-39a3-a89f-c689a6510a17 | -9.9597 | -47.315 | 2024-10-15 14:16:02 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 158.5 |
| 29c5d03f-6ed8-346e-bd44-c5d59e36d6f3 | -9.9411 | -47.2949 | 2024-10-15 14:16:02 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 151.0 |
| 0c265498-feb8-3533-8fa0-e6b711c34d34 | -9.96 | -47.2928 | 2024-10-15 14:16:02 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 153.4 |
| 84c756be-e94c-3df1-a25e-c7c7dbe06d79 | -9.997 | -47.3551 | 2024-10-15 14:16:02 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 150.8 |
| 7deddc48-0359-3296-a968-dda625b8cdf8 | -9.9967 | -47.3773 | 2024-10-15 14:16:02 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 148.8 |
| 83fe0839-2f18-3359-9948-7c2efaad84b8 | -9.9787 | -47.3128 | 2024-10-15 14:16:02 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 149.7 |
| 90431c4a-ba5a-37d0-8f98-ce275664ce2e | -10.0498 | -47.6368 | 2024-10-15 14:16:03 | GOES-16 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 140.5 |
| 684e7c31-62cd-327d-9678-51f6fa0b335b | -10.0536 | -47.3709 | 2024-10-15 14:16:03 | GOES-16 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 128.5 |
| aca92b57-b661-3b7e-be9b-02ac3988e274 | -10.2442 | -47.2824 | 2024-10-15 14:16:04 | GOES-16 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 136.5 |
| fd92fcee-e4c9-3bbc-a654-f2bfd42d0026 | -10.2641 | -47.2134 | 2024-10-15 14:16:04 | GOES-16 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 146.0 |
| 9c771b7f-3ef6-3c16-a760-8e4d0e66e662 | -10.2635 | -47.2579 | 2024-10-15 14:16:04 | GOES-16 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 143.4 |
| 74d0afa2-2ec1-3634-a83b-c15e91c3df6d | -10.9361 | -45.5292 | 2024-10-15 14:16:08 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 112.9 |
| b4787de2-3582-3402-bac7-8a4086e625d9 | -11.222 | -43.3255 | 2024-10-15 14:16:09 | GOES-16 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 104.7 |
| c99b7af4-687d-3638-81a4-5e3204c44a94 | -11.1399 | -45.8893 | 2024-10-15 14:16:09 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 141.6 |
| 8b4ba244-f382-34d3-bfc0-a6746186ed2b | -11.7946 | -44.5072 | 2024-10-15 14:16:12 | GOES-16 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 124.5 |
| 2d14122e-8f9f-3487-9ee5-274dbb6960fb | -11.7566 | -44.4897 | 2024-10-15 14:16:12 | GOES-16 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 118.3 |
| fa7095f6-dcee-3dba-a0f5-45fdb9cb44ae | -11.7753 | -44.5101 | 2024-10-15 14:16:12 | GOES-16 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 124.7 |
| 9217ed4b-2e2e-35a9-9cda-adb108dfd16c | -11.7373 | -44.4926 | 2024-10-15 14:16:12 | GOES-16 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 116.0 |
| 4f469ab6-0bc9-3d81-bc15-223dad51564d | -12.1073 | -43.1861 | 2024-10-15 14:16:14 | GOES-16 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 114.3 |
| 35c0492e-0327-3896-8c77-f2ea4a95c3e0 | -3.2898 | -42.6918 | 2024-10-15 14:35:24 | GOES-16 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 98.3 |
| ed7ff81f-17b3-3eb2-87d8-0160c86b050e | -3.1098 | -54.2464 | 2024-10-15 14:35:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 61.9 |
| acebea95-15ab-3cf7-bc38-d8df45f2cd7e | -3.9961 | -43.2418 | 2024-10-15 14:35:28 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 107.7 |
| b28b7d99-b83e-3378-a254-5463dbded635 | -4.0148 | -43.2408 | 2024-10-15 14:35:29 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 198.5 |
| 6c5ab07a-8253-3c95-a35d-c861f203a28c | -7.7658 | -43.295 | 2024-10-15 14:35:50 | GOES-16 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 56.5 |
| 0d0e1078-5458-35c2-97b7-c6400f26d62b | -7.9433 | -42.6868 | 2024-10-15 14:35:51 | GOES-16 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 71.9 |
| 45716270-fdbe-3a87-b927-5c68de3d6759 | -3.2898 | -42.6918 | 2024-10-15 14:45:24 | GOES-16 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 100.7 |
| a38538e8-c9bf-3cd4-8d18-e8a748b8eb62 | -3.2906 | -42.5271 | 2024-10-15 14:45:24 | GOES-16 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 97.3 |
| 36dcd084-3a67-3237-a359-5b8efe617c5b | -3.6457 | -42.5101 | 2024-10-15 14:45:26 | GOES-16 | LUZILÂNDIA | PIAUÍ | Brasil | 2205805 | 22 | 33 | nan | nan | nan | Caatinga | 82.8 |
| 44cf9e1a-a688-3643-985c-f1afb06ae957 | -4.0957 | -42.2969 | 2024-10-15 14:45:29 | GOES-16 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 93.1 |
| ac1e8036-21c0-30ce-8885-04250d78fd60 | -6.82 | -43.6901 | 2024-10-15 14:45:44 | GOES-16 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 70.4 |
| 41675ccd-595a-3a46-8fd2-9357b4355897 | -6.9309 | -47.4929 | 2024-10-15 14:45:45 | GOES-16 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 59.0 |
| 7891c4f0-c1a4-3b47-89f0-f10a31d132ca | -6.9311 | -47.4709 | 2024-10-15 14:45:45 | GOES-16 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 68.8 |
| 23472cf9-e862-38a6-a23c-7d2391b03e80 | -6.9163 | -43.4718 | 2024-10-15 14:45:45 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 64.4 |
| f1e75957-0898-3c40-9ffa-60dbbf409f43 | -7.9433 | -42.6868 | 2024-10-15 14:45:51 | GOES-16 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 59.2 |
| 20d48d68-137a-3e60-b7eb-ab78a2691950 | -8.9513 | -45.0419 | 2024-10-15 14:45:56 | GOES-16 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 89.2 |
| d5d32263-b69f-3e98-a863-8487fa932c0d | -9.1137 | -47.0296 | 2024-10-15 14:45:57 | GOES-16 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 85.9 |
| c03441b7-8a7b-3675-9b9a-c7b2e21ec266 | -9.2012 | -47.5516 | 2024-10-15 14:45:58 | GOES-16 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 133.1 |
| 06be3003-8247-3bd1-8d82-dd8873b1d322 | -9.4509 | -45.8271 | 2024-10-15 14:45:59 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 105.0 |
| 89cd4e6a-9ebe-3c77-9b6f-adb4edaa2e48 | -9.4484 | -46.0082 | 2024-10-15 14:45:59 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 96.8 |


[Clique aqui para ver as próximas entradas](README84.md)
