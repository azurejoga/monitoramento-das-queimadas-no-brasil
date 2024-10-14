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

## Dados Diários - Página 56

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2007ca73-36f5-3f6b-8d74-abc4f7928e83 | -9.97061 | -47.3422 | 2024-10-14 04:21:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| e8454bba-ec29-36c8-9eaf-5f716e20d5e8 | -9.97 | -47.34592 | 2024-10-14 04:21:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| db6cac70-b26d-3623-a46d-28ad291947b2 | -9.96982 | -47.34244 | 2024-10-14 04:21:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 79d2b6fc-d393-326c-b268-0b2011dcd93e | -9.96922 | -47.34616 | 2024-10-14 04:21:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 4b80679d-b461-30de-9b54-4df38aefd60b | -9.96642 | -47.34187 | 2024-10-14 04:21:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 596c7d88-7b50-3b0c-b0be-97d4d5b89876 | -9.9622 | -47.30303 | 2024-10-14 04:21:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 6654b18c-3a6f-330a-b395-ce3588d72a50 | -9.96022 | -47.337 | 2024-10-14 04:21:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 72462b08-f7f2-3f70-8081-cb86f927d6da | -9.95962 | -47.34073 | 2024-10-14 04:21:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7b36b062-745f-3ca0-b4ee-0da04e756d48 | -9.94561 | -47.31932 | 2024-10-14 04:21:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 455b26eb-7ac2-3788-9940-835062afdcb6 | -9.94342 | -47.31131 | 2024-10-14 04:21:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| b1f18508-0cca-33df-a012-8a44187f1a3e | -9.83825 | -46.98812 | 2024-10-14 04:21:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f59262f3-1ebf-3af3-9d2d-025c7c1b9a74 | -9.83488 | -46.98756 | 2024-10-14 04:21:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d9019ed1-12cf-3c21-93ac-aa0cb8f81735 | -10.02647 | -47.32092 | 2024-10-14 04:21:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| ec357288-a9dc-3f79-8cf5-8859a1b8cd57 | -10.02586 | -47.32462 | 2024-10-14 04:21:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| d00143d1-d7ff-327e-a64a-9708e86eaff7 | -10.02526 | -47.32832 | 2024-10-14 04:21:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 3a0b8cc5-47c7-3097-93de-f19f9f57e48d | -10.02345 | -47.33945 | 2024-10-14 04:21:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| f786cd2c-88ca-378a-8d7f-128aec9bf389 | -10.02247 | -47.32405 | 2024-10-14 04:21:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 1d692f2a-964b-3f6f-8f50-652d06317ba3 | -10.02186 | -47.32776 | 2024-10-14 04:21:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| b1e1adbb-1bc1-306d-ba4a-9f0275489c39 | -10.02126 | -47.33147 | 2024-10-14 04:21:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c6dde4dc-d87f-3569-b166-5bd199dd9b34 | -10.02065 | -47.33518 | 2024-10-14 04:21:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d674163d-89a6-3f5a-bd44-66c4ea776f38 | -10.01907 | -47.32349 | 2024-10-14 04:21:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 05939fea-16e6-395b-a416-948ed1cf5ee6 | -10.01846 | -47.3272 | 2024-10-14 04:21:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 8c547585-551a-303f-bd8a-af767a79546e | -10.01726 | -47.33461 | 2024-10-14 04:21:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 85a6a882-cbf8-325a-96af-cbcca7a8fa8a | -10.01506 | -47.32664 | 2024-10-14 04:21:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 363959c1-a165-3a60-92a1-048c5a643c81 | -10.01399 | -47.37611 | 2024-10-14 04:21:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2fe8c303-03f0-3452-8f85-dc658743dfec | -10.01227 | -47.32238 | 2024-10-14 04:21:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 062c7c3b-274e-3349-882e-352764c07967 | -10.01166 | -47.32608 | 2024-10-14 04:21:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 71ee519d-51c9-3ea0-b972-67409f05d03b | -10.00985 | -47.33719 | 2024-10-14 04:21:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 6f5fbd8e-23a5-330f-9abb-d2a3e7f5fb97 | -10.00887 | -47.32182 | 2024-10-14 04:21:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 53d56112-4085-3ba2-b15e-0e1425c7dcbc | -10.00827 | -47.32553 | 2024-10-14 04:21:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e34fc00d-ef8e-335a-9cac-4a78f89cc543 | -10.00487 | -47.32497 | 2024-10-14 04:21:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| dbce8724-49fa-3b5d-be00-35eb807d071c | -9.49672 | -45.82625 | 2024-10-14 04:21:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f75b7ded-1ccf-3f3c-850e-b32331bb9302 | -12.51483 | -46.81788 | 2024-10-14 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4e84566f-c310-3882-a0b0-20a85a59b468 | -8.01209 | -47.21563 | 2024-10-14 04:21:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e67a8be0-98d3-325c-87fa-5961469a0c1a | -7.67185 | -47.32232 | 2024-10-14 04:21:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 76d9080e-a397-3d9c-95c0-52759100bf69 | -7.67123 | -47.32616 | 2024-10-14 04:21:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3e7ca41c-1d06-3ca3-9070-1cd67702d72b | -7.66962 | -47.31407 | 2024-10-14 04:21:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b4a9be01-4849-3318-95f6-fee3c59d47d4 | -9.3038 | -48.24871 | 2024-10-14 04:21:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c33498fa-1f56-3b74-aa00-5fe320378655 | -9.29249 | -48.25094 | 2024-10-14 04:21:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cf5b871c-8b1f-35d3-ab9c-817e280c4ef4 | -9.20293 | -47.56241 | 2024-10-14 04:21:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b91a34d1-b392-3a08-bace-c31d40053de5 | -9.19603 | -47.56126 | 2024-10-14 04:21:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ad7dd107-802b-3b93-aca4-8e8a00460612 | -9.16193 | -47.60282 | 2024-10-14 04:21:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c2b1d052-7a4b-3284-87dc-886b1758b52e | -9.11749 | -48.68901 | 2024-10-14 04:21:00 | NOAA-21 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c612c29e-6009-3582-a65e-c68423deeed3 | -9.11419 | -47.72175 | 2024-10-14 04:21:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a8627699-0039-37c3-b540-a3291077353e | -9.11167 | -47.73723 | 2024-10-14 04:21:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 925302f0-5950-3526-a877-c4ed8c0cb007 | -9.10819 | -47.73668 | 2024-10-14 04:21:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d939471d-2d80-3170-89e3-d0cae72cafa1 | -9.10058 | -47.78339 | 2024-10-14 04:21:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a1f57c4f-a77e-36d0-92de-86475dcf7ec8 | -9.09942 | -47.94504 | 2024-10-14 04:21:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2154feef-ef85-3d01-9cad-c89eae789e00 | -9.09849 | -47.92859 | 2024-10-14 04:21:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 5b2771b7-a896-36d3-abbd-aa4fd5d1c3b1 | -9.09785 | -47.93255 | 2024-10-14 04:21:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 5157c10b-1214-3338-a684-8078f04b2b01 | -9.0972 | -47.93652 | 2024-10-14 04:21:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3e5bd815-ca1e-3298-bf62-b5cae505ea44 | -9.09709 | -47.78283 | 2024-10-14 04:21:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bd8053de-448a-3888-8d54-63937ad5c414 | -9.09655 | -47.9405 | 2024-10-14 04:21:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5d9a6e43-a422-3980-9a1b-67b1a7e7f207 | -9.09591 | -47.94447 | 2024-10-14 04:21:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9bc0c1de-7ec5-3835-8722-d6ab972d0af3 | -9.09563 | -47.92403 | 2024-10-14 04:21:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ef81c28d-f01d-37c7-8618-7eeec1a38d9e | -9.09527 | -47.94843 | 2024-10-14 04:21:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 950eb155-061a-37e4-b8a3-49b9b4aff407 | -9.09498 | -47.92801 | 2024-10-14 04:21:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 9cbb10fa-e6b9-34eb-ac29-30f2cbbfc565 | -9.09434 | -47.93197 | 2024-10-14 04:21:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| ab6ca00b-1c9e-3b5a-9152-c5e4783a8bc1 | -9.09369 | -47.93594 | 2024-10-14 04:21:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f0dbdbdc-2090-3cd3-9b88-5aba0e8a5ba1 | -9.09305 | -47.93991 | 2024-10-14 04:21:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 503572a9-74a5-33bb-bc92-126c0fff8868 | -9.0924 | -47.94389 | 2024-10-14 04:21:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c71cfe0f-b0c9-32a0-a81a-844a99eec201 | -9.09019 | -47.93534 | 2024-10-14 04:21:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7b6a6fcb-5f49-3ced-8a32-559a8d019d6b | -9.08954 | -47.93932 | 2024-10-14 04:21:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4a1462a2-d86e-3ba7-a893-cee29bcb48a3 | -9.08948 | -47.78559 | 2024-10-14 04:21:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c08a4117-4e3e-3448-a329-adaaadd7f5c9 | -9.086 | -47.78502 | 2024-10-14 04:21:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fc2ac6a5-e3f1-358a-9426-d81119b9550e | -9.08251 | -47.78444 | 2024-10-14 04:21:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a5c96a04-68f1-3bc8-8e60-34d56956c306 | -9.05894 | -47.68884 | 2024-10-14 04:21:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f2545114-fdec-37ec-b303-72ae8bbcc753 | -9.05546 | -47.68828 | 2024-10-14 04:21:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 523eb208-cb02-370b-b30a-58bec379df75 | -9.02969 | -47.68088 | 2024-10-14 04:21:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| eb236ef9-88ee-3881-ba3a-5e325141813f | -9.01618 | -47.41512 | 2024-10-14 04:21:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 0ca7a05b-4363-3e08-b199-f1274b631a31 | -8.98638 | -47.74953 | 2024-10-14 04:21:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 347bb07e-f30b-3f24-8c0f-7eb0b80a8d5d | -8.98574 | -47.75343 | 2024-10-14 04:21:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e4cdea8b-03ed-3147-aa99-6e7bd1094ab0 | -8.98289 | -47.74899 | 2024-10-14 04:21:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| e7b02eda-ef49-3009-885d-4d51fc8c9dc0 | -8.97979 | -47.68067 | 2024-10-14 04:21:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c855cdf2-c8ff-3436-b1ee-b152e2689ad5 | -8.9794 | -47.74844 | 2024-10-14 04:21:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| f69b7e9d-039a-3d97-913c-8f7985a010bf | -8.97916 | -47.68454 | 2024-10-14 04:21:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 15bbaea7-52ea-3932-bbd4-e1fc24ad988c | -8.97631 | -47.6801 | 2024-10-14 04:21:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8560a6a4-7f95-3b91-9fb4-60d23ccd564b | -8.92009 | -47.9123 | 2024-10-14 04:21:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| fad621f5-770e-3065-872a-20c601de827f | -8.91943 | -47.91628 | 2024-10-14 04:21:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 67bd91fc-fc86-3100-805a-4638d8d7f207 | -8.91657 | -47.91175 | 2024-10-14 04:21:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 735fdad2-3262-346d-aad1-bf94d788f243 | -8.91591 | -47.91572 | 2024-10-14 04:21:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0d2cd84d-9849-3fc0-8510-c2b6bd227d6e | -8.91306 | -47.9112 | 2024-10-14 04:21:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| e1b3b32f-fae7-3620-8714-a2610031e262 | -8.90954 | -47.91064 | 2024-10-14 04:21:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 10f4d7a3-6a0c-3ae6-b608-06e052548b5e | -8.90889 | -47.9146 | 2024-10-14 04:21:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 300d1ed0-22a7-3ae7-9962-3d041b73ce85 | -8.60312 | -48.61832 | 2024-10-14 04:21:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 4fd75c35-d10f-3cae-8956-230fe43fb332 | -8.60242 | -48.62251 | 2024-10-14 04:21:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 39db6d67-8a9c-37bb-8a84-aa7821e479da | -8.59947 | -48.61774 | 2024-10-14 04:21:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 504d6d64-c249-38f0-ba68-223a895fb057 | -8.48235 | -48.62215 | 2024-10-14 04:21:00 | NOAA-21 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 46260622-7b20-3a54-a2d3-0a7c7fda1557 | -8.48164 | -48.62641 | 2024-10-14 04:21:00 | NOAA-21 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Amazônia | 16.0 |
| 1d6a24cf-2f25-3224-a8f7-935b1238b4b1 | -8.47869 | -48.62157 | 2024-10-14 04:21:00 | NOAA-21 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Amazônia | 4.8 |
| eaf9de3f-ca3e-3f32-a18b-6809b9f83f57 | -8.47798 | -48.62581 | 2024-10-14 04:21:00 | NOAA-21 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Amazônia | 16.0 |
| 4eca49cd-be64-3000-8630-d8382fba4c85 | -8.42912 | -47.98233 | 2024-10-14 04:21:00 | NOAA-21 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| ac0cb638-ab74-3767-a4d7-d32f8287a734 | -9.99827 | -48.85863 | 2024-10-14 04:21:00 | NOAA-21 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 58b297f6-6142-3218-9989-15b70a6384ee | -9.99533 | -48.85386 | 2024-10-14 04:21:00 | NOAA-21 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ffba42db-07f2-36ce-84cd-2b8ebe15d8dd | -9.99463 | -48.85804 | 2024-10-14 04:21:00 | NOAA-21 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 661c7b58-0588-394d-a710-efab1c1f602e | -9.9917 | -48.85324 | 2024-10-14 04:21:00 | NOAA-21 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| be7a0aaf-ccd6-3cdb-910e-14f2db09908a | -9.991 | -48.85744 | 2024-10-14 04:21:00 | NOAA-21 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0a3c338e-f051-3081-83cd-744250b377c2 | -9.94357 | -47.41856 | 2024-10-14 04:21:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cfbed909-5adf-32f1-ae23-0048065d516e | -9.94297 | -47.42229 | 2024-10-14 04:21:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 44d87301-6153-394c-a401-698ef6c0bfc8 | -9.92864 | -48.138 | 2024-10-14 04:21:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |


[Clique aqui para ver as próximas entradas](README57.md)
