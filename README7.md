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
| 5727440e-8ebb-3012-8d6d-b194a0445646 | -5.9938 | -43.7366 | 2025-07-03 03:20:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 74.0 |
| 4865f896-a4a2-367c-ad09-6ae9bab79b87 | -6.2943 | -43.6891 | 2025-07-03 03:20:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 60.9 |
| 8ead4872-cfdb-344e-bccb-8dc164056a04 | -18.22 | -51.3446 | 2025-07-03 03:20:00 | GOES-19 | APARECIDA DO RIO DOCE | GOIÁS | Brasil | 5201454 | 52 | 33 | nan | nan | nan | Cerrado | 65.8 |
| d0b24278-bfa8-3e69-ac85-c5dd85e11e51 | -6.2945 | -43.6659 | 2025-07-03 03:20:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 71.2 |
| d787fff9-cadb-3f1c-ae90-fdace3e131f0 | -6.9605 | -42.8816 | 2025-07-03 03:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 372.7 |
| fa9eef81-e8ab-338a-997a-2edbb0cd6c0e | -6.9602 | -42.9052 | 2025-07-03 03:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 111.9 |
| d852601f-7ddc-35fd-b6cb-5c49f3bbbcb6 | -6.9607 | -42.858 | 2025-07-03 03:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 69.3 |
| 088f9aa5-9079-33bf-a4eb-4a3890c3b6ec | -6.1792 | -48.0494 | 2025-07-03 03:20:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 63.4 |
| ba3dfecf-9da5-3178-aa73-2d0e3861da27 | -6.9793 | -42.8798 | 2025-07-03 03:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 85.4 |
| cad9690d-7a22-3147-9257-e34584b4a8f3 | -7.2222 | -43.0447 | 2025-07-03 03:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 75.0 |
| 283219e8-8464-3bc2-aa36-719f5c36a5bb | -7.2408 | -43.0664 | 2025-07-03 03:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 84.3 |
| b472026c-3918-3918-8b92-9ffde7652329 | -6.9416 | -42.8834 | 2025-07-03 03:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 151.3 |
| 83ae48c2-4a9c-39c0-9ab6-07b034eaca1a | -7.2219 | -43.0682 | 2025-07-03 03:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 129.4 |
| 24c18d75-c3c2-351c-b356-c821b74ae922 | -7.2408 | -43.0664 | 2025-07-03 03:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 90.7 |
| b4081838-8165-33ae-8258-3147f4643d0b | -6.1792 | -48.0494 | 2025-07-03 03:30:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 57.0 |
| 35ddf7a8-6a2d-3401-b77f-ae1482927a7c | -6.9607 | -42.858 | 2025-07-03 03:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 90.4 |
| c9a28bda-914d-3c21-b842-3d90b83db3d6 | -6.2943 | -43.6891 | 2025-07-03 03:30:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 73.8 |
| dfe66851-7fe7-36ea-8ab6-4d06cebb5249 | -6.9605 | -42.8816 | 2025-07-03 03:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 315.0 |
| ba8299cf-26ba-3bd9-88e4-f190f1e31b44 | -6.9416 | -42.8834 | 2025-07-03 03:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 145.0 |
| cc533c28-aa06-3073-b603-4af593ad0e6f | -6.9793 | -42.8798 | 2025-07-03 03:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 88.2 |
| 11642c9a-2e4b-37f5-bc05-dea0f7c485b9 | -11.6588 | -44.5974 | 2025-07-03 03:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 54.5 |
| 7e43529b-d38d-3007-97da-b08978c2bce2 | -7.2222 | -43.0447 | 2025-07-03 03:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 81.6 |
| b4c425f7-ec9b-3832-9c71-ea99ec3a2299 | -6.9602 | -42.9052 | 2025-07-03 03:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 93.7 |
| 1591e450-e1f3-31cc-aa2c-dca3f254a012 | -5.9938 | -43.7366 | 2025-07-03 03:30:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 99.6 |
| 642d3002-f3b0-314a-b046-88a22e9cb09d | -18.22 | -51.3446 | 2025-07-03 03:30:00 | GOES-19 | APARECIDA DO RIO DOCE | GOIÁS | Brasil | 5201454 | 52 | 33 | nan | nan | nan | Cerrado | 52.0 |
| 230af24a-ab53-319c-a80d-a464f6fda7b4 | -6.2945 | -43.6659 | 2025-07-03 03:30:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 74.1 |
| 8414c009-7f99-3b64-85b8-09868d9951a2 | -6.9416 | -42.8834 | 2025-07-03 03:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 139.3 |
| 5854cccc-5c84-3cb4-a9ac-d77526e612a4 | -7.2219 | -43.0682 | 2025-07-03 03:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 121.9 |
| 5037e73a-3284-3b81-b52c-81f30e1b3b93 | -6.9793 | -42.8798 | 2025-07-03 03:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 90.2 |
| 627eb1e9-9706-3669-ae2d-afa37a3f79b9 | -18.22 | -51.3446 | 2025-07-03 03:40:00 | GOES-19 | APARECIDA DO RIO DOCE | GOIÁS | Brasil | 5201454 | 52 | 33 | nan | nan | nan | Cerrado | 62.1 |
| ee78e540-a391-3fb4-bea9-c9e3431b8f53 | -5.9938 | -43.7366 | 2025-07-03 03:40:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 89.2 |
| b475f044-ddca-3d03-90bc-e6b7ef796e63 | -7.2408 | -43.0664 | 2025-07-03 03:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 74.7 |
| e28645af-f975-359f-86a3-78aad29fdf1a | -14.6291 | -53.8809 | 2025-07-03 03:40:00 | GOES-19 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 58.2 |
| 23848dfa-f544-3745-b7c7-fee9a4790dcb | -6.9607 | -42.858 | 2025-07-03 03:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 79.1 |
| 4add938b-68a7-3cf8-8ef3-12ad15d6a85e | -6.9605 | -42.8816 | 2025-07-03 03:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 282.9 |
| 3affdcc7-e96a-3eb9-8056-0f71a4c0ae91 | -6.9602 | -42.9052 | 2025-07-03 03:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 112.2 |
| 0bb59f53-917a-3d90-9de4-f0ef630e1443 | -6.2945 | -43.6659 | 2025-07-03 03:40:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 85.0 |
| b4a023d7-0158-3ee4-a148-907369a7e170 | -7.2222 | -43.0447 | 2025-07-03 03:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 89.6 |
| 04f7e3a4-df42-3797-8c2d-50631c55f62a | -6.2943 | -43.6891 | 2025-07-03 03:40:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 72.6 |
| a9318d0e-8639-3998-b0c0-a43da93a4cf2 | -7.2219 | -43.0682 | 2025-07-03 03:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 135.4 |
| f7143687-3bb1-3626-96a0-f00a4c267b0f | -18.22 | -51.3446 | 2025-07-03 03:50:00 | GOES-19 | APARECIDA DO RIO DOCE | GOIÁS | Brasil | 5201454 | 52 | 33 | nan | nan | nan | Cerrado | 50.5 |
| fefc8308-4932-3f0e-ae10-a91e40cebb07 | -6.9793 | -42.8798 | 2025-07-03 03:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 89.5 |
| 45fc109c-e210-3620-9d72-f8b966c2fe0f | -6.9605 | -42.8816 | 2025-07-03 03:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 351.9 |
| ac50476d-2bb8-36aa-8ddd-6aeb9a15d2d2 | -5.9938 | -43.7366 | 2025-07-03 03:50:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 78.2 |
| ea1522d0-aebd-3aed-aaa3-9532786f3db5 | -7.2222 | -43.0447 | 2025-07-03 03:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 75.8 |
| 446207db-105f-30a2-bc33-969edbb33b19 | -6.9607 | -42.858 | 2025-07-03 03:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 80.3 |
| 8422c07a-2d5c-381a-85bf-3bcbbd855b07 | -6.0125 | -43.7352 | 2025-07-03 03:50:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 70.2 |
| 9588cc42-08e1-3321-8812-41fae9cccae0 | -6.2945 | -43.6659 | 2025-07-03 03:50:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 83.1 |
| 4e420e66-ad76-350d-b36e-ab01dc083a86 | -6.9602 | -42.9052 | 2025-07-03 03:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 77.5 |
| a441defd-54de-3f12-acd3-11d347a0f76f | -6.2943 | -43.6891 | 2025-07-03 03:50:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 87.2 |
| 76c27c08-21da-31a9-9f1a-f8e247e03612 | -6.9416 | -42.8834 | 2025-07-03 03:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 129.8 |
| dfb25c05-c5ba-3269-b1f5-512229ae9e86 | -6.9602 | -42.9052 | 2025-07-03 04:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 105.5 |
| 26270586-14db-31b7-bd40-4e0858c85f0a | -16.2962 | -49.9354 | 2025-07-03 04:00:00 | GOES-19 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 56.0 |
| 6669b2fe-da27-3d5d-bf8b-afc9af19e7a1 | -6.9607 | -42.858 | 2025-07-03 04:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 64.3 |
| 44c0f4a8-70fc-3f66-83d8-a255b6e2e148 | -6.9605 | -42.8816 | 2025-07-03 04:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 317.6 |
| dcf51cc8-c090-3cd1-b3a2-26d1c383ad34 | -6.0125 | -43.7352 | 2025-07-03 04:00:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 73.1 |
| 8b218a14-52e1-3c23-bcc9-cf6451f39ea6 | -6.2945 | -43.6659 | 2025-07-03 04:00:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 83.8 |
| eadd3bcf-40b2-33a9-8fe7-f03e3debe618 | -18.22 | -51.3446 | 2025-07-03 04:00:00 | GOES-19 | APARECIDA DO RIO DOCE | GOIÁS | Brasil | 5201454 | 52 | 33 | nan | nan | nan | Cerrado | 51.9 |
| 518b6b96-e25e-35d8-92cd-f9e9acd14577 | -5.9938 | -43.7366 | 2025-07-03 04:00:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 79.2 |
| da1da32d-0930-39d2-b7e9-019c9aec22f5 | -16.2958 | -49.9575 | 2025-07-03 04:00:00 | GOES-19 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 38.8 |
| 74e70b10-0c01-34ff-b037-363be06121a3 | -7.2222 | -43.0447 | 2025-07-03 04:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 71.4 |
| c7642f4f-4d22-312d-bb7c-2823c810189a | -6.9416 | -42.8834 | 2025-07-03 04:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 123.5 |
| 4d4625fd-eb46-3466-ba7e-11845abf7e3a | -11.6588 | -44.5974 | 2025-07-03 04:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 83.7 |
| baf8a636-c354-3f29-bc09-4d54d159befd | -6.2943 | -43.6891 | 2025-07-03 04:00:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 75.3 |
| 593cef06-f6dd-357d-b44b-856d3e51f0eb | -16.3159 | -49.9321 | 2025-07-03 04:00:00 | GOES-19 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 35.9 |
| 18f2e456-b631-3e7b-9eb5-f867d15ca022 | -7.2219 | -43.0682 | 2025-07-03 04:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 110.5 |
| 4329fccd-78bd-3c71-9f6a-75a42223a900 | -6.9793 | -42.8798 | 2025-07-03 04:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 95.3 |
| 0f11b4cf-74b6-3dd1-a178-9056a91e1194 | -2.91242 | -48.24107 | 2025-07-03 04:06:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 5099d565-bed6-3039-ad11-d8292194ca39 | -2.91323 | -48.23605 | 2025-07-03 04:06:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 80d0d5e4-0fe0-335c-94a3-19e51917c311 | -3.09096 | -40.06198 | 2025-07-03 04:06:00 | NOAA-21 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| b3355e52-c498-3490-93b9-b353274bf29d | -2.89317 | -48.03497 | 2025-07-03 04:06:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1d07ec30-4dbc-334f-bc2b-1f304a58f6e4 | -2.92561 | -47.80989 | 2025-07-03 04:06:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6406eb21-4767-30e8-932d-d3ab2d9c4551 | -2.91714 | -48.24183 | 2025-07-03 04:06:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 19e02438-458e-3ba4-91ac-0e15b94f2f9f | -5.61158 | -45.97183 | 2025-07-03 04:08:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| edef2bc0-7ddb-3593-b42c-5ac42975e082 | -10.99362 | -45.19979 | 2025-07-03 04:08:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6583a9b3-7f0c-367b-9b61-1372e4b13caf | -6.28696 | -43.67554 | 2025-07-03 04:08:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 028cea1c-dd74-327b-beeb-c8c6b1f007af | -7.22338 | -43.0667 | 2025-07-03 04:08:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 9a08e056-b792-3ea9-8570-bfc02e3bb004 | -5.41892 | -47.56875 | 2025-07-03 04:08:00 | NOAA-21 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| aa644454-9e47-3f42-a420-1c2c24b0e726 | -7.23008 | -43.06775 | 2025-07-03 04:08:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 16.3 |
| 9c40c102-e75b-3bb0-99a6-e69169c2e330 | -7.73918 | -44.01704 | 2025-07-03 04:08:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 02568bea-23e9-3342-bffd-1dd33a7cd8e4 | -5.99395 | -43.74948 | 2025-07-03 04:08:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 414cb2f1-c2c7-3b7d-b495-bb1e5d586388 | -6.72209 | -42.12489 | 2025-07-03 04:08:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 7afe244a-ca3e-3e6e-82c0-6bf5031038ac | -6.72375 | -43.14438 | 2025-07-03 04:08:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 989af31e-452a-36a5-b62e-fd66dda547c8 | -6.33812 | -43.38047 | 2025-07-03 04:08:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f3eaf7b9-b4b5-3809-b700-811bda732e13 | -6.29718 | -43.67674 | 2025-07-03 04:08:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 3ec20765-b056-308b-9bca-328b81016473 | -6.71405 | -43.18336 | 2025-07-03 04:08:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 6fd39600-f135-3b15-80a0-7bd53609eaf0 | -7.09521 | -44.39158 | 2025-07-03 04:08:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 641b5e70-a39f-3d75-8331-569ce63bd303 | -11.14279 | -43.33049 | 2025-07-03 04:08:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 87bd6eab-997d-3f8b-8bfc-84940e0b96ac | -6.95556 | -42.88921 | 2025-07-03 04:08:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 43.7 |
| 4c3d143a-2a65-38b5-ac4e-aa68d73779db | -9.17262 | -48.77588 | 2025-07-03 04:08:00 | NOAA-21 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 2ece21d1-66fb-3cd1-b870-95f7103b02e6 | -7.43843 | -44.44495 | 2025-07-03 04:08:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fbfe3001-9143-39a4-9986-c11ce66da035 | -4.53473 | -48.02173 | 2025-07-03 04:08:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7cc4ac40-9fce-35c3-b1d2-90caf74f5215 | -5.99232 | -43.73765 | 2025-07-03 04:08:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ea34dd24-8d5b-3ffb-b563-985554e7128a | -6.58709 | -43.04569 | 2025-07-03 04:08:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 889dc7f3-b75f-3cd8-b6f7-efe72627c0dd | -4.40083 | -47.63269 | 2025-07-03 04:08:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 513b53ae-fa5c-33f0-b8b4-0bee5ddedd13 | -8.63219 | -50.03841 | 2025-07-03 04:08:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 72f5bc0d-52bd-37c1-adf6-c0b9f4d30277 | -6.96397 | -42.87601 | 2025-07-03 04:08:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 1a85952b-e790-3304-a3f8-5e08665f8897 | -9.79634 | -47.74672 | 2025-07-03 04:08:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fb7e9cf8-1dbf-3fc0-ba03-0aa41f74c712 | -9.26755 | -47.9061 | 2025-07-03 04:08:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ab2d7db5-56ea-37a4-ac46-1476a05e2b5e | -6.69584 | -43.15496 | 2025-07-03 04:08:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 2.9 |


[Clique aqui para ver as próximas entradas](README8.md)
