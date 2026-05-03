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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 886a1606-8a69-30f5-a44d-bc0b7f87d979 | -17.949499 | -53.0093 | 2026-05-03 00:20:00 | METOP-C | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 349ac9ec-7d3d-31e1-ac82-955678a25b82 | -10.6381 | -47.9949 | 2026-05-03 00:20:00 | METOP-C | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6fc3a8d3-f073-3baf-aeed-ae5796e1542e | -17.964399 | -53.040901 | 2026-05-03 00:20:00 | METOP-C | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 73521353-e4a1-3588-be95-9982914259dd | -12.3686 | -50.016701 | 2026-05-03 00:20:00 | METOP-C | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 52b8035c-6c37-3eec-9688-05f7c04f039d | -12.4634 | -44.295799 | 2026-05-03 00:20:00 | METOP-C | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 77ce61eb-679c-3010-a9c9-52fc62493468 | -17.958099 | -52.939999 | 2026-05-03 00:20:00 | METOP-C | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| e721174d-6a84-3d66-bb69-246f5ff9f0f8 | -17.9837 | -53.037701 | 2026-05-03 00:20:00 | METOP-C | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 7eb0759d-e1d4-3d61-8738-1cb1463a981e | -21.571501 | -48.3517 | 2026-05-03 00:20:00 | METOP-C | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 759cd996-5d53-3eeb-b023-4beb1dff5eb8 | -15.4567 | -43.323898 | 2026-05-03 00:20:00 | METOP-C | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Caatinga | nan |
| 6591b377-c7ea-3be1-8ce1-97aa0eb4a6a3 | -12.3491 | -50.0205 | 2026-05-03 00:20:00 | METOP-C | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 197470d3-3f11-3fff-aa39-5c787806a3ca | -10.5896 | -44.3228 | 2026-05-03 00:20:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b14e855d-cd85-30a3-b35e-641e3d457d5f | -17.978399 | -53.004398 | 2026-05-03 00:20:00 | METOP-C | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| fc8fff36-3e3a-3a1d-9631-7a26c0dcdbab | -10.5912 | -44.330299 | 2026-05-03 00:20:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 0abb41eb-3f90-32b4-a5d1-fd31e75ea289 | -17.9485 | -52.9417 | 2026-05-03 00:20:00 | METOP-C | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| cf40657f-62e3-3eb3-bb61-0a9154527bd7 | -17.997601 | -53.001301 | 2026-05-03 00:20:00 | METOP-C | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 9b70e1cd-f98b-3ec2-a1ae-c12c7d77212f | -11.9601 | -43.964699 | 2026-05-03 00:20:00 | METOP-C | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e6de5d70-0c62-38da-8ad0-ce7601147cbf | -10.5798 | -44.325001 | 2026-05-03 00:20:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| cefa42e1-4376-32ed-841f-b1be88e2f57a | -12.37 | -50.0242 | 2026-05-03 00:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 68.3 |
| 90a5a4ec-920a-3409-90e0-7869f9d9da6f | -12.3508 | -50.0266 | 2026-05-03 00:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 8d17b4ca-e407-3b1a-82cd-fce4633e1afa | -10.9815 | -45.0874 | 2026-05-03 00:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 75.4 |
| dd7531bc-581c-3db5-80fe-d6c7f661ebac | -12.3508 | -50.0266 | 2026-05-03 00:40:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 85.1 |
| f0d84339-9ade-3dcf-8cd3-2d176adbc5ca | -12.37 | -50.0242 | 2026-05-03 00:40:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 64.9 |
| 46b5aa9c-1baa-343c-b4dc-82cb2ce014b7 | -10.9815 | -45.0874 | 2026-05-03 00:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 72.8 |
| 71f2cc14-6026-36f7-8ae2-eb78004c9b2c | -12.37 | -50.0242 | 2026-05-03 00:50:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 75.8 |
| af63aea4-e936-35c0-a828-3b6d35590d77 | -12.3508 | -50.0266 | 2026-05-03 00:50:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 83.2 |
| 6f510304-e717-3db0-b2a6-aa51867f244e | -12.37 | -50.0242 | 2026-05-03 01:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 82.2 |
| 4c0e5ec4-e013-3de9-a835-159ac879772a | -12.3508 | -50.0266 | 2026-05-03 01:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 62.2 |
| bfbdda18-43d3-329e-851e-83a6d34614dc | -17.9665 | -52.9924 | 2026-05-03 01:10:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 322.4 |
| 423bf1ac-cc93-35b7-a8f2-dc88be6ec260 | -12.3508 | -50.0266 | 2026-05-03 01:10:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 61.2 |
| a55e95ca-6ace-374a-8369-00504a182a47 | -17.9466 | -52.9955 | 2026-05-03 01:10:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 143.8 |
| 411bab3a-f62d-3e25-84bd-852b8b6636fd | -12.37 | -50.0242 | 2026-05-03 01:10:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 82.5 |
| 9949b34a-4b20-3d08-9ee2-b811a5569f02 | -17.9471 | -52.9739 | 2026-05-03 01:10:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 95.5 |
| fa3b0bbf-dbcf-3a47-b921-1a38d63a02b6 | -10.9815 | -45.0874 | 2026-05-03 01:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 61.2 |
| 963ca8cd-b4f6-3441-ba8f-2b97c7059a3e | -17.9669 | -52.9708 | 2026-05-03 01:10:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 100.0 |
| af76cc79-61de-3905-89ad-98ce4fcb00fc | -17.966 | -53.0139 | 2026-05-03 01:10:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 119.0 |
| b9e45be4-0e74-3774-b121-58860e9377fa | -17.9864 | -52.9892 | 2026-05-03 01:20:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 81.6 |
| 6bde14b3-0913-35c3-a5e5-01cffad0704e | -17.9665 | -52.9924 | 2026-05-03 01:20:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 243.6 |
| 4361bb99-df7f-3fdf-947a-2c0d93a3ec4a | -17.9471 | -52.9739 | 2026-05-03 01:20:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 137.9 |
| a049066c-8dcc-30e0-83c5-ccf75725110a | -17.9669 | -52.9708 | 2026-05-03 01:20:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 97.5 |
| 8a57053b-04fe-347b-83c6-d71a507e6ff2 | -17.9466 | -52.9955 | 2026-05-03 01:20:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 124.1 |
| 6c837130-4aeb-3fbf-96e2-cd2a98e067d7 | -12.37 | -50.0242 | 2026-05-03 01:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 87.4 |
| 05d634cf-9016-3a39-b9ba-726f01d8975d | -17.966 | -53.0139 | 2026-05-03 01:20:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 86.3 |
| 081c5bbf-a586-39ee-a4e2-7f084cc8fb8f | -13.1923 | -54.545898 | 2026-05-03 01:27:00 | METOP-B | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e54ee3dc-3d3e-3d5f-9df5-47ca762c41f6 | -17.9585 | -52.945301 | 2026-05-03 01:27:00 | METOP-B | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| fcefda89-8c2a-322b-8894-b5f1e73181e6 | -17.968 | -52.9422 | 2026-05-03 01:27:00 | METOP-B | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 7c485294-a772-3e89-932d-0549f7743ddb | -17.960199 | -53.020699 | 2026-05-03 01:27:00 | METOP-B | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 44bb97ee-c8f8-30e8-a864-50383b4870c5 | -17.9783 | -52.976898 | 2026-05-03 01:27:00 | METOP-B | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 1b4d2ca2-1553-3754-bcd2-a9a98202bd5a | -13.2209 | -54.537498 | 2026-05-03 01:27:00 | METOP-B | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3d76d0a0-115b-3f66-b804-4acb3abd5ab3 | -17.9405 | -52.9893 | 2026-05-03 01:27:00 | METOP-B | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 423e02de-61dd-3a59-8d52-8e1a79308760 | -17.9491 | -52.948502 | 2026-05-03 01:27:00 | METOP-B | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 3a0a0d96-3f4b-3ec5-933d-d3f6462e3e21 | -17.9877 | -52.973801 | 2026-05-03 01:27:00 | METOP-B | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 82586496-6347-3419-8dda-1beafb91aa49 | -17.950001 | -52.986198 | 2026-05-03 01:27:00 | METOP-B | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 09706af6-9f1a-310e-8d06-2ac76d66b979 | -17.969601 | -53.017601 | 2026-05-03 01:27:00 | METOP-B | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| bd31cabc-2eee-383f-9461-ffe03d65156b | -13.2019 | -54.506699 | 2026-05-03 01:27:00 | METOP-B | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 16b80d17-4bae-3391-a4f7-de856983d26c | -17.930201 | -52.9547 | 2026-05-03 01:27:00 | METOP-B | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 0a892f4b-e66d-329b-8671-460b6610b60e | -17.939699 | -52.951599 | 2026-05-03 01:27:00 | METOP-B | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 00aaf6f9-2022-3498-853b-93242ef8a6e2 | -17.9594 | -52.983101 | 2026-05-03 01:27:00 | METOP-B | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 315d0b7c-82ef-3113-8e6e-15748302a682 | -13.2018 | -54.543098 | 2026-05-03 01:27:00 | METOP-B | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| d195f911-7354-377e-a159-60c97998040d | -13.1924 | -54.509499 | 2026-05-03 01:27:00 | METOP-B | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 991eb05f-6d4b-3998-a5c5-f74e6c8ea6fc | -17.988501 | -53.011299 | 2026-05-03 01:27:00 | METOP-B | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| ae870b4c-6950-3945-bf46-7401d19849e3 | -13.2113 | -54.540298 | 2026-05-03 01:27:00 | METOP-B | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| eb2961be-2187-3255-a8a5-cf1cb5c13177 | -17.979 | -53.0144 | 2026-05-03 01:27:00 | METOP-B | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| c25f984b-4a0e-39a3-9a63-7f585ed229f6 | -17.9688 | -52.9799 | 2026-05-03 01:27:00 | METOP-B | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| cf22b69d-41fd-3970-b501-09e85930dae6 | -13.1829 | -54.512299 | 2026-05-03 01:27:00 | METOP-B | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| c859273e-9915-3324-afd6-3be08ed0966c | -18.0663 | -52.955 | 2026-05-03 01:30:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 60.7 |
| e104a7cf-7628-3093-a6c5-9b79ade2c2b6 | -12.37 | -50.0242 | 2026-05-03 01:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 73.3 |
| e64e0770-aef3-3e8a-91db-2958f9c30473 | -18.0668 | -52.9335 | 2026-05-03 01:30:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 62.7 |
| 93f00be3-ecdc-36df-91a2-181f4b19e593 | -12.37 | -50.0242 | 2026-05-03 01:40:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 71.5 |
| 6d8f43dd-c202-3531-b8a4-9a963f09c2b0 | -17.9864 | -52.9892 | 2026-05-03 01:50:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 348.4 |
| 861f5ef8-4f5a-3517-bd94-d016b323a6dd | -17.9859 | -53.0108 | 2026-05-03 01:50:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 189.6 |
| ca63c0fd-f4c9-3028-90ce-8ebc0989aa84 | -17.9665 | -52.9924 | 2026-05-03 01:50:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 289.7 |
| b2712d5f-a2ca-3bef-8e2d-e2a4c747b61e | -12.37 | -50.0242 | 2026-05-03 01:50:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 65.7 |
| 5e1fe377-0e52-39ed-a6fb-8e6a3a8a02eb | -17.9466 | -52.9955 | 2026-05-03 01:50:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 78.6 |
| cde371f2-8fda-3bb3-88e8-fe2b9e4c4b34 | -12.3508 | -50.0266 | 2026-05-03 01:50:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 69.3 |
| 8692cd24-82b7-3aa9-ba30-62dab0ab2c89 | -17.966 | -53.0139 | 2026-05-03 01:50:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 166.9 |
| 093e6a65-485f-3171-aa41-10d17bdbe488 | -13.2151 | -54.5588 | 2026-05-03 01:59:00 | METOP-C | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 459f36c8-67a5-3fa9-9781-1fe998d16654 | -17.9816 | -53.007999 | 2026-05-03 01:59:00 | METOP-C | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 9edd0528-f5b8-37aa-85ab-104141573d87 | -17.972099 | -53.011002 | 2026-05-03 01:59:00 | METOP-C | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| c12cbdea-e8d1-38e7-aac6-02f5509c19b1 | -17.9527 | -52.980801 | 2026-05-03 01:59:00 | METOP-C | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 00f79201-7a72-3e59-9b5d-cc35350a9c9c | -17.9622 | -52.977699 | 2026-05-03 01:59:00 | METOP-C | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| ae2962b9-414b-3857-9bf9-c87c95a3a3b4 | -13.2246 | -54.555901 | 2026-05-03 01:59:00 | METOP-C | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 25ba7dc9-518f-390a-b21a-324c02d2025b | -13.2155 | -54.523602 | 2026-05-03 01:59:00 | METOP-C | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 59fc2e0d-0ed9-386c-8c91-f7a1db9b95a7 | -17.990999 | -53.004902 | 2026-05-03 01:59:00 | METOP-C | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 6b703800-fa45-3f49-8723-1f73329c184d | -17.971701 | -52.974602 | 2026-05-03 01:59:00 | METOP-C | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 0a2df674-da47-3ed8-8e44-8e279fc4dc41 | -13.206 | -54.526402 | 2026-05-03 01:59:00 | METOP-C | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3bd60abf-375a-3f6f-9352-034c70758a42 | -17.9466 | -52.9955 | 2026-05-03 02:00:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 79.3 |
| c64fee11-83c0-3484-bbbd-315eefd71d7a | -17.9859 | -53.0108 | 2026-05-03 02:00:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 101.1 |
| c945cbaf-1bbe-32e3-a90d-adffcaaf5aaa | -17.9864 | -52.9892 | 2026-05-03 02:00:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 171.5 |
| 9b2fcbd2-ac9b-3138-b2dc-b46639b455b3 | -10.9815 | -45.0874 | 2026-05-03 02:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 57.3 |
| 408f4ad6-f0eb-351a-ad53-16e3b77bb96d | -12.3508 | -50.0266 | 2026-05-03 02:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 73.8 |
| 2c8ef78a-46e5-307b-ac37-b16afe52a0da | -17.9665 | -52.9924 | 2026-05-03 02:00:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 143.8 |
| e36b76af-a27d-3e48-861a-4eb9a8270aa6 | -17.966 | -53.0139 | 2026-05-03 02:00:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 80.7 |
| e605f082-da67-343c-8e99-8c812b5d9beb | -13.2183 | -54.5388 | 2026-05-03 02:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 133.1 |
| d24d6fec-9176-31ce-83af-ab62696f104e | -13.218 | -54.5594 | 2026-05-03 02:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 48.9 |
| 66fe2ec3-a47b-384e-8a8c-bc4318f10c69 | -13.1995 | -54.5202 | 2026-05-03 02:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 52.4 |
| 2a67e957-3c9e-3e35-a917-65edc394749e | -13.1992 | -54.5408 | 2026-05-03 02:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 106.9 |
| c099ab3b-9295-3bf4-8adb-9a95e2742630 | -13.2186 | -54.5182 | 2026-05-03 02:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 53.8 |
| 5d7ffd49-e52c-3fbc-ab9b-e5f0c670a9a5 | -12.37 | -50.0242 | 2026-05-03 02:10:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 73263f94-b749-3dae-a0e7-b840f565aae6 | -13.2374 | -54.5368 | 2026-05-03 02:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 43.1 |
| 2721ca06-1e88-3673-94c3-913efe35387c | -13.1992 | -54.5408 | 2026-05-03 02:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 99.9 |


[Clique aqui para ver as próximas entradas](README3.md)
