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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 496115b2-ec14-3648-b542-3d42f3d00ab8 | -2.8514 | -49.262 | 2024-10-27 01:55:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 0dcd4f9e-e560-3c8a-bac5-cc500f75b4c3 | -2.8515 | -49.2408 | 2024-10-27 01:55:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 69.8 |
| 7b406705-61c6-3fd9-aaf0-2945da745538 | -2.9214 | -50.295 | 2024-10-27 01:55:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 50.7 |
| 916d72ee-3092-3eed-ad2f-f76a098c7652 | -2.916 | -51.7716 | 2024-10-27 01:55:22 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 64.2 |
| 19332efa-87f5-329d-aa1e-756795445389 | -2.9161 | -51.751 | 2024-10-27 01:55:22 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 83.0 |
| 1c0c67c1-8f61-3780-9afc-0ee377c84ea5 | -2.9215 | -50.274 | 2024-10-27 01:55:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 88.1 |
| 26704f14-fe91-3ac6-91d4-231b7cbc1873 | -2.9345 | -51.7711 | 2024-10-27 01:55:22 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 68.0 |
| e1432461-4490-3268-90b0-0f953cf1fcba | -2.9345 | -51.7505 | 2024-10-27 01:55:22 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 89.4 |
| f6c98191-8473-3cc4-a266-f2d6a3097813 | -2.9399 | -50.2735 | 2024-10-27 01:55:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 69.5 |
| 02919c98-9dab-3386-96e9-9449b4e739db | -2.9669 | -53.0389 | 2024-10-27 01:55:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 67ffe54f-5d1f-31d1-8c18-74a428204bf2 | -3.1106 | -44.9809 | 2024-10-27 01:55:23 | GOES-16 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 71.0 |
| 99548619-bd0f-3cd3-a323-ac73b903b391 | -3.1116 | -53.7234 | 2024-10-27 01:55:23 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 41.1 |
| 529c39dc-e217-39e8-9250-346ea593e30a | -3.1242 | -50.3519 | 2024-10-27 01:55:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 66.9 |
| a246156b-7c0a-3f51-a77d-3b084caf1fe3 | -3.344 | -50.7635 | 2024-10-27 01:55:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 53.1 |
| db198e2a-5128-3087-bf57-83e33beceaac | -3.3441 | -50.7426 | 2024-10-27 01:55:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 45.8 |
| 064fa437-d899-378e-984e-aff133721777 | -3.4762 | -54.5772 | 2024-10-27 01:55:25 | GOES-16 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 54.4 |
| 8f30126a-1bcd-37a4-81f9-cf7898c872c4 | -4.254 | -63.153 | 2024-10-27 01:55:30 | GOES-16 | COARI | AMAZONAS | Brasil | 1301209 | 13 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 9d1526e2-76b7-39d5-8027-f6d7bfb5340c | -4.2723 | -63.1526 | 2024-10-27 01:55:30 | GOES-16 | COARI | AMAZONAS | Brasil | 1301209 | 13 | 33 | nan | nan | nan | Amazônia | 56.1 |
| f38dfcac-cfee-35f4-b60b-4d7628474107 | -7.2452 | -46.0482 | 2024-10-27 01:55:46 | GOES-16 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 56.2 |
| 38f514ad-16e6-328e-b145-43a428e8cbfc | -10.5424 | -45.1463 | 2024-10-27 01:56:05 | GOES-16 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 81.0 |
| 46b25c1a-77b1-3def-a19f-6e002327acdd | -12.8883 | -44.6143 | 2024-10-27 01:56:17 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 68.7 |
| 38f48638-dfc0-3152-8154-223b894ff49e | -0.9815 | -53.7192 | 2024-10-27 02:05:11 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 72.3 |
| b7eb07b0-f2be-3ebc-92a0-0e9e6234a85e | -0.9815 | -53.699 | 2024-10-27 02:05:11 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 212.1 |
| 37539703-4e30-3815-abc2-41b8345c9d2e | -0.9815 | -53.6789 | 2024-10-27 02:05:11 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 68.9 |
| 25b58ba6-5005-3830-a917-0bf6eb9f5873 | -0.9998 | -53.6989 | 2024-10-27 02:05:11 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 149.5 |
| 26e70f50-32a5-3ed6-a636-7006af939e30 | -2.4598 | -50.412 | 2024-10-27 02:05:19 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 43.6 |
| 9d666ea4-3f2b-366d-b580-3724dd74e5b0 | -2.4753 | -45.8561 | 2024-10-27 02:05:19 | GOES-16 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 66.9 |
| c92e1508-f6b5-3799-b51f-372e53e5b752 | -2.4753 | -45.8338 | 2024-10-27 02:05:19 | GOES-16 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 66.7 |
| 654c7a7e-6f9f-3e41-b405-e677bd37fc16 | -2.4786 | -50.2858 | 2024-10-27 02:05:19 | GOES-16 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 45.8 |
| 811a1023-af85-3ea2-aef9-bbfe0d5cedc5 | -2.6321 | -54.2975 | 2024-10-27 02:05:20 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 46.3 |
| 741197e9-ea0e-328f-a4fd-a3bfb6a0b514 | -2.6482 | -49.2465 | 2024-10-27 02:05:20 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 48.1 |
| d0b77b92-fbe5-3b76-8345-2f26ecc5fcf1 | -2.6505 | -54.2971 | 2024-10-27 02:05:20 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 7d969dbd-999d-312a-a8ea-4c4d2be92237 | -2.8397 | -52.5532 | 2024-10-27 02:05:21 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 46.6 |
| 9cb01cb1-072e-3841-a1fd-082648b0e6d8 | -2.8422 | -51.8148 | 2024-10-27 02:05:21 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 49.7 |
| 91f638dc-3bf0-3fc4-8568-ad334f0772ee | -2.8423 | -51.7942 | 2024-10-27 02:05:21 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 42.7 |
| 90085701-c719-34f0-b288-0f838551b5fd | -2.8515 | -49.2408 | 2024-10-27 02:05:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 05285fc4-5da5-3ee3-b5d3-1ff1245c6176 | -2.7033 | -49.33 | 2024-10-27 02:05:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 81.9 |
| 3797a34f-6ec4-3ee5-8160-f2dce45d78de | -2.7034 | -49.3088 | 2024-10-27 02:05:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 79.1 |
| 13fba8d8-e5e8-39ff-9a87-3821c82a9d6b | -2.8145 | -49.2418 | 2024-10-27 02:05:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 47.1 |
| 21f18a71-6133-3d06-8057-fb7cde1fd5f2 | -2.8329 | -49.2626 | 2024-10-27 02:05:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 83.2 |
| 175b59fc-afa5-3a64-bf9e-219280c50de1 | -2.833 | -49.2413 | 2024-10-27 02:05:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 139.2 |
| 7adac246-53e4-3c87-8332-7956e58655b9 | -2.916 | -51.7716 | 2024-10-27 02:05:22 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 64.5 |
| 662b85ee-325b-3304-98eb-9e99affe7a97 | -2.9161 | -51.751 | 2024-10-27 02:05:22 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 89.5 |
| 60d30083-d0e7-31bd-af66-63e17fe93f98 | -2.9214 | -50.295 | 2024-10-27 02:05:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 54.1 |
| f5151e59-476b-3b73-ae7b-65124d3f7ae6 | -2.9215 | -50.274 | 2024-10-27 02:05:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 82.9 |
| 42c57897-1719-324d-a122-9a4b4e368a56 | -2.9345 | -51.7711 | 2024-10-27 02:05:22 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 5c659b7a-2927-317a-a85b-21082cb7e2a3 | -2.9345 | -51.7505 | 2024-10-27 02:05:22 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 094fe39b-1576-3cc5-8355-5f5ea39d4d5c | -2.9399 | -50.2735 | 2024-10-27 02:05:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 4c04ac40-c0fe-3461-98aa-7945fb615ba8 | -2.9669 | -53.0389 | 2024-10-27 02:05:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 46.4 |
| 78083706-9722-3bbf-98c5-93fc14b367cc | -3.1057 | -50.3525 | 2024-10-27 02:05:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 41.4 |
| 390ecf1c-d5d2-3f77-a98c-ba8a32031f9f | -3.1242 | -50.3519 | 2024-10-27 02:05:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 60.2 |
| faae33fc-b3ef-3871-bcbc-0acbccda6706 | -3.344 | -50.7635 | 2024-10-27 02:05:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 51.0 |
| 908e4166-2154-3a95-a773-9094612403c9 | -3.3256 | -50.7641 | 2024-10-27 02:05:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 44.3 |
| 2a7282b5-e0ec-3268-bce3-928023fb7e6f | -3.4762 | -54.5772 | 2024-10-27 02:05:25 | GOES-16 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 192f30b1-efe8-3be2-9e48-315854659d1a | -4.254 | -63.153 | 2024-10-27 02:05:30 | GOES-16 | COARI | AMAZONAS | Brasil | 1301209 | 13 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 1587e7e1-a8c9-36cb-bed1-d3026e25125f | -7.2264 | -46.0498 | 2024-10-27 02:05:46 | GOES-16 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 55.4 |
| 6ed8bb23-677d-34e7-9b2c-8da9d77d3336 | -0.9815 | -53.7192 | 2024-10-27 02:15:11 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 68.9 |
| ba532c7c-898d-3812-afa0-262370206f37 | -0.9815 | -53.699 | 2024-10-27 02:15:11 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 184.7 |
| 56b71b27-97d1-3e05-a81b-496e63641704 | -0.9815 | -53.6789 | 2024-10-27 02:15:11 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 0f3cf3a4-21f6-376b-a301-8a9e2f5b0e24 | -0.9998 | -53.6989 | 2024-10-27 02:15:11 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 134.3 |
| a9cce672-da76-3980-8eee-1e6eb8eb9c0f | -1.1831 | -53.8985 | 2024-10-27 02:15:12 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 55.1 |
| dba74b48-6709-3d8b-84ba-88ede4f63e43 | -2.4753 | -45.8561 | 2024-10-27 02:15:19 | GOES-16 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 250c162b-a1dd-3b33-8d94-10818dc03226 | -2.4753 | -45.8338 | 2024-10-27 02:15:19 | GOES-16 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 48b04ca7-3e81-3184-b165-42b0b35fe0e8 | -2.4786 | -50.2858 | 2024-10-27 02:15:19 | GOES-16 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 43.2 |
| b73b3174-b323-3154-b915-91307e86805a | -2.486 | -48.0507 | 2024-10-27 02:15:19 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 37.7 |
| 75758f3c-ac55-3a49-8997-d4ff7d3dbefa | -2.6321 | -54.2975 | 2024-10-27 02:15:20 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 44.1 |
| dc67a637-f20d-34ac-8ff8-692f2711db98 | -2.6482 | -49.2465 | 2024-10-27 02:15:20 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 48.3 |
| f63ffc9d-6104-3221-abf3-582845302643 | -2.6505 | -54.2971 | 2024-10-27 02:15:20 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 52.4 |
| 289392ac-4153-3d53-8b0d-78dff502f452 | -2.8422 | -51.8148 | 2024-10-27 02:15:21 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 50.6 |
| dea54cbf-1ce7-379c-ad9c-49b3d3f2856e | -2.8423 | -51.7942 | 2024-10-27 02:15:21 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 42.4 |
| e3b5ef59-d813-3eca-b15a-3fe7e03a1c1e | -2.8514 | -49.262 | 2024-10-27 02:15:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 37.2 |
| 73aa50b1-dafa-32be-87b8-f4a77be83ec9 | -2.8515 | -49.2408 | 2024-10-27 02:15:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 48.2 |
| f230ed62-08ef-399a-8af4-4b32a62e7554 | -2.7033 | -49.33 | 2024-10-27 02:15:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 83.6 |
| 1c7cf5e1-8b7a-33c8-9066-15c5ac568130 | -2.7034 | -49.3088 | 2024-10-27 02:15:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 80.1 |
| 91d3c4f0-54a9-312f-ba3f-989f9dfb9f49 | -2.8145 | -49.2418 | 2024-10-27 02:15:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 42.3 |
| ed0422c4-4ad2-3b1c-907a-d601994e85cf | -2.8329 | -49.2626 | 2024-10-27 02:15:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 82.5 |
| 8cb0b712-b580-33e5-b835-3e45f04e1e5c | -2.833 | -49.2413 | 2024-10-27 02:15:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 123.0 |
| 4f0a7ace-f42e-3a6c-91fe-526feff0789b | -2.8397 | -52.5532 | 2024-10-27 02:15:21 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 45.2 |
| 460c105f-9985-328d-894c-9fb8c567bddd | -3.017 | -45.12 | 2024-10-27 02:15:22 | GOES-16 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 65.2 |
| a5422694-52c8-3472-b290-9ccbbfbf13a5 | -2.916 | -51.7716 | 2024-10-27 02:15:22 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 67eb0bc9-4bd9-3f9e-ba2c-e8334e5dbb93 | -2.9161 | -51.751 | 2024-10-27 02:15:22 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 69.9 |
| 697c2adf-b7dc-3736-bf66-c17437db1137 | -2.9214 | -50.295 | 2024-10-27 02:15:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 54.6 |
| bba7f430-f150-3c92-b918-87376d33d160 | -2.9215 | -50.274 | 2024-10-27 02:15:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 84.4 |
| 1fe8bf0a-7354-323c-b3e7-5f9f070a5bef | -2.9345 | -51.7711 | 2024-10-27 02:15:22 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 47.2 |
| c0980b0b-0bfe-3503-b967-5e0fa12d2eca | -2.9345 | -51.7505 | 2024-10-27 02:15:22 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 58.5 |
| b63aea24-69f0-3d82-9fd8-ad3e3d45ce2d | -2.9399 | -50.2735 | 2024-10-27 02:15:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 66.8 |
| 1fa0eb5c-d302-3648-81dd-3ce6764f7cfa | -2.9669 | -53.0389 | 2024-10-27 02:15:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 39.9 |
| b38a46ba-db64-34dc-b1a2-2e4890d16125 | -2.9984 | -45.1207 | 2024-10-27 02:15:22 | GOES-16 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 791c2f9c-3be0-3606-8cbb-428b7c011d99 | -3.1242 | -50.3519 | 2024-10-27 02:15:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 57bed5fc-f59c-3fce-b435-ed057ee7d46f | -3.344 | -50.7635 | 2024-10-27 02:15:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 40.4 |
| fd667ebc-427c-3fdd-85d9-1aa6e6cd7596 | -3.4762 | -54.5772 | 2024-10-27 02:15:25 | GOES-16 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 54.9 |
| b654b26f-f0cd-3e7a-aaf4-7d3dd977ef5c | -4.254 | -63.153 | 2024-10-27 02:15:30 | GOES-16 | COARI | AMAZONAS | Brasil | 1301209 | 13 | 33 | nan | nan | nan | Amazônia | 50.1 |
| a8637a33-8965-3396-8a4b-e38dd4eddd2f | -0.9815 | -53.7192 | 2024-10-27 02:25:11 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 87.5 |
| 5fe414a9-a91a-3f78-827b-f729231dde5a | -0.9815 | -53.699 | 2024-10-27 02:25:11 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 197.4 |
| 61808e32-2003-3569-a2ec-24fc0db3993a | -0.9815 | -53.6789 | 2024-10-27 02:25:11 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 51.8 |
| c99b6f2e-fea5-33c6-bd33-376aece7584f | -0.9998 | -53.719 | 2024-10-27 02:25:11 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 51.2 |
| e869ebbf-433f-39aa-b2cb-06810b483b60 | -0.9998 | -53.6989 | 2024-10-27 02:25:11 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 109.2 |
| e26bb648-a310-362a-8d07-9357cc6da4f0 | -1.1831 | -53.8985 | 2024-10-27 02:25:12 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 50.2 |
| bee7e73b-ae56-3f6a-aa30-dc9df243753e | -2.4753 | -45.8561 | 2024-10-27 02:25:19 | GOES-16 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 48.2 |
| 47b37ba7-6740-3339-b42f-34e732190341 | -2.4753 | -45.8338 | 2024-10-27 02:25:19 | GOES-16 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 55.0 |


[Clique aqui para ver as próximas entradas](README24.md)
