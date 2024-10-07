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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5a6c6fa3-6cf3-3558-93c0-50a76b03690f | -3.2177 | -48.910599 | 2024-10-07 00:29:56 | METOP-B | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8668b7ea-1f48-3ce8-936e-37f51cd7fc25 | -3.2193 | -48.917702 | 2024-10-07 00:29:56 | METOP-B | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0ac4eed4-8b2a-36d5-8a91-2bb5f87c6a32 | -3.2627 | -49.111099 | 2024-10-07 00:29:56 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f24b491a-2da3-39e0-9b0f-84f1c90eeae5 | -3.2643 | -49.118301 | 2024-10-07 00:29:56 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1fe77161-19f3-3fb1-9dc3-e2e0b7802423 | -2.7103 | -46.795101 | 2024-10-07 00:29:56 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| eb8a7467-992d-38af-857d-4e3115082ad6 | -2.7119 | -46.801998 | 2024-10-07 00:29:56 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f0c90f7a-7a49-3884-b19b-05c58f62c4e5 | -3.3569 | -49.901299 | 2024-10-07 00:29:57 | METOP-B | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f2d6d221-1080-310c-87ae-e348e32e89ca | -3.4837 | -50.794498 | 2024-10-07 00:29:58 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9b6d3e5d-ef09-3d96-a0db-749fb5babda1 | -2.785 | -49.506401 | 2024-10-07 00:30:05 | METOP-B | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f4bdbdff-b7ad-382f-a7d1-e289c6357b42 | -2.7867 | -49.513802 | 2024-10-07 00:30:05 | METOP-B | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 35b1d314-ea93-3df4-9598-c6fd90881f54 | -2.7458 | -49.514999 | 2024-10-07 00:30:06 | METOP-B | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8a915a9d-b633-3ad7-a133-e17ad063afdc | -2.7475 | -49.5224 | 2024-10-07 00:30:06 | METOP-B | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1a373c59-9a7a-3ba6-8539-1ada454b1498 | -3.0436 | -51.079201 | 2024-10-07 00:30:06 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b0c5cc85-4ab7-3679-bb7d-54b719d96104 | -2.9652 | -51.096298 | 2024-10-07 00:30:08 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0059a109-8d08-37ab-87fe-cf0c0c536acf | -3.2569 | -52.828602 | 2024-10-07 00:30:09 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 53e8ef71-5ec9-3925-80bf-fdc102300b2e | -3.3226 | -53.358398 | 2024-10-07 00:30:10 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c2719997-2781-34b5-a9eb-d38a1ac0d02d | -3.3253 | -53.370399 | 2024-10-07 00:30:10 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| acb95744-a9a3-3b3e-9319-d8be0ba48da5 | -2.4547 | -50.237099 | 2024-10-07 00:30:13 | METOP-B | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 00af047f-80c6-3d77-88d0-f568b622d339 | -2.4564 | -50.2449 | 2024-10-07 00:30:13 | METOP-B | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 34227d94-b718-359d-a27c-559e3af20b81 | -3.0324 | -53.017899 | 2024-10-07 00:30:14 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 82319e79-b209-3a4b-b36a-ec1616f75688 | -2.8805 | -52.886902 | 2024-10-07 00:30:16 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6e51e0b4-67d2-39a0-95a3-74b05a763790 | -2.8756 | -52.864799 | 2024-10-07 00:30:16 | METOP-B | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fa440ca9-5432-354f-8382-548979089caf | -2.878 | -52.875801 | 2024-10-07 00:30:16 | METOP-B | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7e7b9a8c-db90-3ea1-a418-5cbfb941b070 | -2.8829 | -52.8979 | 2024-10-07 00:30:16 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f6ca4ee8-aa9a-3d8e-9604-903257caf758 | -2.8658 | -52.867001 | 2024-10-07 00:30:16 | METOP-B | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 034db6ef-b249-3b87-ab35-50623f301d65 | -2.8682 | -52.877998 | 2024-10-07 00:30:16 | METOP-B | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1b77f311-7344-3b6c-84d5-1f79f1e74258 | -2.8707 | -52.889099 | 2024-10-07 00:30:16 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f00957ed-323c-3a58-8e92-f4631bc0f26d | -2.8731 | -52.900101 | 2024-10-07 00:30:16 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 02d37f03-7c02-37ca-813d-47bded4d0c41 | -2.856 | -52.869099 | 2024-10-07 00:30:16 | METOP-B | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4744556c-cfd7-3336-88d5-c1fe1fe551d9 | -2.8584 | -52.8801 | 2024-10-07 00:30:16 | METOP-B | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a84aa05b-f72b-3869-aefe-d7a500ba3be1 | -2.8609 | -52.891201 | 2024-10-07 00:30:16 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ad1fad33-f81c-3fdd-9642-e2de667d72af | -2.8633 | -52.902199 | 2024-10-07 00:30:16 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 33911253-be5a-3723-a49b-b156f6e0cdd5 | -1.123 | -53.6021 | 2024-10-07 00:30:16 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1c791543-2625-3342-b644-fa1003a3ca72 | -1.1256 | -53.613701 | 2024-10-07 00:30:16 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| da6864dc-e70c-3a2c-a288-106017e15610 | -1.0411 | -53.5117 | 2024-10-07 00:30:17 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0ee9dbdd-1544-354c-93ee-2dfd59329f91 | -1.0314 | -53.513802 | 2024-10-07 00:30:17 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6eb9c641-3cb5-3006-9b1d-0fa71da13568 | -2.7716 | -53.1819 | 2024-10-07 00:30:18 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 909ec94e-4465-301c-9820-d42945dce864 | -2.7741 | -53.193401 | 2024-10-07 00:30:18 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 61640a64-2c0f-3fc0-bdaa-de027fa91de2 | -1.0339 | -53.707199 | 2024-10-07 00:30:18 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c999395d-5cb8-32ed-875c-61f3db01ab6d | -1.0365 | -53.719002 | 2024-10-07 00:30:18 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7f3ed44f-c906-36c0-88f2-08ebd0cce0b1 | -1.0215 | -53.697601 | 2024-10-07 00:30:18 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6cf17969-e518-3e86-b752-838466de5304 | -1.0267 | -53.7211 | 2024-10-07 00:30:18 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 27fb2d3f-74c5-3670-bdc8-94094eae8d9d | -2.7619 | -53.183998 | 2024-10-07 00:30:19 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f1222826-b6b0-333c-8451-cd02da158e4a | -2.7644 | -53.195499 | 2024-10-07 00:30:19 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f8f82bac-8c03-3770-9fce-4bcc80997b95 | -1.1973 | -46.575199 | 2024-10-07 00:30:20 | METOP-B | AUGUSTO CORRÊA | PARÁ | Brasil | 1500909 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 48d405a4-7b83-3ce8-a248-d5e2747dab16 | -2.8108 | -54.330101 | 2024-10-07 00:30:22 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 716e70fc-ae28-3133-9083-d0e79b60dfbe | -1.1832 | -47.652401 | 2024-10-07 00:30:24 | METOP-B | IGARAPÉ-AÇU | PARÁ | Brasil | 1503200 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7ca2afa5-5f76-3908-acb9-68d1f5cb4a1c | -1.1848 | -47.659199 | 2024-10-07 00:30:24 | METOP-B | IGARAPÉ-AÇU | PARÁ | Brasil | 1503200 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 34b9077b-6bfe-32db-acf7-f472f19992a1 | -2.2222 | -53.66 | 2024-10-07 00:30:29 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0f364a34-c2f8-36ce-a30d-e0e86e573dd1 | -2.2249 | -53.672199 | 2024-10-07 00:30:29 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 61a09924-769c-3866-bb2e-17c6ca31cd81 | -2.2098 | -53.650002 | 2024-10-07 00:30:29 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a431723e-6be1-3361-8cf0-62b6fe768ddf | -2.2125 | -53.662102 | 2024-10-07 00:30:29 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 10fee839-2ac0-3941-86d4-c69e965eb06d | -2.2152 | -53.674301 | 2024-10-07 00:30:29 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5daf3c8e-2f09-3a6b-8946-4ed361fe57ca | -2.2179 | -53.686401 | 2024-10-07 00:30:29 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1512e43d-24f8-30bf-bce7-d8dd8b63ee09 | 1.8153 | -50.796101 | 2024-10-07 00:30:53 | METOP-B | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| d5410c2c-af9c-32d8-8f91-a08605a2f996 | -1.0182 | -53.739 | 2024-10-07 00:35:12 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 68.5 |
| ac3effec-7777-3dea-9736-7d33f7f02099 | -1.0365 | -53.7389 | 2024-10-07 00:35:12 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 115.3 |
| e2c75536-c058-3211-a0ce-06afd6779a75 | -1.0365 | -53.7187 | 2024-10-07 00:35:12 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 91.5 |
| 48ff8bfe-7a31-3a30-b60c-292c87c1a90c | -2.2113 | -53.7029 | 2024-10-07 00:35:19 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 100.7 |
| a474dbb9-11a4-3d22-aa42-9e454c1705ec | -2.2114 | -53.6828 | 2024-10-07 00:35:19 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 86.4 |
| 953f1ef7-fb8e-3e36-899c-9b7eae85069f | -2.2297 | -53.7026 | 2024-10-07 00:35:19 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 124.2 |
| 5d915aab-b308-3bf1-8baa-6a52289e5728 | -2.2297 | -53.6824 | 2024-10-07 00:35:19 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 107.7 |
| fe010de0-a4b8-35be-9e97-9ffa076ea58e | -2.8569 | -52.9197 | 2024-10-07 00:35:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 120.8 |
| 3851bccf-0e1e-3e03-9ec2-d3860acb0389 | -2.857 | -52.8993 | 2024-10-07 00:35:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 153.0 |
| 707384d5-4c5f-35c6-926d-1190fd57b1b7 | -2.8753 | -52.9192 | 2024-10-07 00:35:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 261.5 |
| 9a88fac6-bf4d-38ec-b8a5-479ffae4da52 | -2.8754 | -52.8989 | 2024-10-07 00:35:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 349.2 |
| 9debae67-109e-3246-b8a4-eb1da0065174 | -2.8937 | -52.9188 | 2024-10-07 00:35:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 92.6 |
| 727e5d9d-2638-3a61-9389-9a5c8733668d | -2.8937 | -52.8984 | 2024-10-07 00:35:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 102.4 |
| 5ad7931b-af90-3bbb-bbe9-5dd1ced1141e | -4.2729 | -43.737 | 2024-10-07 00:35:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 212.2 |
| e56aedc8-2927-3e2d-98c7-df39be22f690 | -4.2728 | -43.7601 | 2024-10-07 00:35:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 73.1 |
| 971f8d64-e378-3b3a-b289-ac989384feb7 | -4.2916 | -43.736 | 2024-10-07 00:35:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 75.2 |
| c7159860-1c7a-38d7-882e-cca1c5fe25d1 | -10.3316 | -64.262 | 2024-10-07 00:36:05 | GOES-16 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 55.0 |
| c7dd489b-c24f-34f9-8179-89b0596e2f68 | -10.3503 | -64.2612 | 2024-10-07 00:36:05 | GOES-16 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 084b290d-a331-3a9b-8e5c-ade48105a540 | -11.2467 | -51.3918 | 2024-10-07 00:36:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 84.2 |
| ae5587d6-054e-36a9-b9a7-a816dc7d3237 | -11.247 | -51.3706 | 2024-10-07 00:36:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 86.2 |
| 4c433af6-de66-3530-97f8-900f831d0eee | -11.2654 | -51.411 | 2024-10-07 00:36:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 65.7 |
| 82434e83-bb9f-351e-8be6-4c5e5df3c9a9 | -11.2657 | -51.3898 | 2024-10-07 00:36:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 144.7 |
| 2e5a618f-d580-393f-a217-d1f50c52d592 | -11.266 | -51.3686 | 2024-10-07 00:36:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 89.7 |
| d0a2c5b7-e7ff-3309-be3e-ef6663742542 | -11.2847 | -51.3878 | 2024-10-07 00:36:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 70.6 |
| 9200302e-2446-3a14-bac5-220cc72387ee | -11.7369 | -44.5159 | 2024-10-07 00:36:12 | GOES-16 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 53.6 |
| 669f49cd-a59e-3200-88fc-5423e2ace6e5 | -11.7373 | -44.4926 | 2024-10-07 00:36:12 | GOES-16 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 111.7 |
| 882157e8-834d-3d95-ab20-4995c908c6c6 | -11.7561 | -44.513 | 2024-10-07 00:36:12 | GOES-16 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 65.4 |
| a2c90135-5343-380a-9c2e-9e1372f3f820 | -11.7566 | -44.4897 | 2024-10-07 00:36:12 | GOES-16 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 115.7 |
| f174e584-166f-3dd9-b95c-6f2b94863ab5 | -12.0585 | -63.7841 | 2024-10-07 00:36:15 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 87.1 |
| 90df89d0-88b5-3c5d-9428-295186c007a5 | -12.0587 | -63.765 | 2024-10-07 00:36:15 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 727393a7-f844-3ce7-82a3-c8ac8e71e258 | -12.7284 | -40.2117 | 2024-10-07 00:36:17 | GOES-16 | ITABERABA | BAHIA | Brasil | 2914703 | 29 | 33 | nan | nan | nan | Caatinga | 66.8 |
| d509cadc-f8ac-3915-9e2a-2cbb264f934e | -13.5719 | -50.3223 | 2024-10-07 00:36:23 | GOES-16 | MUNDO NOVO | GOIÁS | Brasil | 5214051 | 52 | 33 | nan | nan | nan | Cerrado | 126.6 |
| 979e33cc-0946-3698-b50f-97a2cccf0ad0 | -13.5723 | -50.3006 | 2024-10-07 00:36:23 | GOES-16 | MUNDO NOVO | GOIÁS | Brasil | 5214051 | 52 | 33 | nan | nan | nan | Cerrado | 132.7 |
| 627e639d-5e44-3b9f-997e-f2c2f88daec0 | -13.5915 | -50.298 | 2024-10-07 00:36:23 | GOES-16 | MUNDO NOVO | GOIÁS | Brasil | 5214051 | 52 | 33 | nan | nan | nan | Cerrado | 96.9 |
| 8a00add2-0a33-31a6-bbca-f9983b3d78d8 | -13.8354 | -44.6398 | 2024-10-07 00:36:23 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 88.7 |
| e5ab71b1-83a1-3dba-bd80-0db07a2b16e2 | -13.8359 | -44.6162 | 2024-10-07 00:36:23 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 88.9 |
| 7ceb7caf-6e33-35d3-bc77-6205991f195e | -13.7342 | -60.6471 | 2024-10-07 00:36:24 | GOES-16 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 5db3e924-f763-3084-bb46-0e5a11d55f6c | -16.4918 | -53.9543 | 2024-10-07 00:36:39 | GOES-16 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 116.5 |
| 49a2eb73-f2ef-3681-b2d5-10f018f1d1a4 | -16.5072 | -57.7387 | 2024-10-07 00:36:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 105.3 |
| 498ee96a-712e-3e73-8d58-49873bff0640 | -16.5267 | -57.7365 | 2024-10-07 00:36:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 116.1 |
| 147632f5-e5ce-321c-b4e1-04ac41569fbd | -16.527 | -57.7161 | 2024-10-07 00:36:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 65.2 |
| ed0926c5-22a8-37aa-8958-5c5ab24edba2 | -16.6199 | -55.5684 | 2024-10-07 00:36:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 96.4 |
| 567aa91b-15fe-3d83-8ba9-927a91c4d889 | -16.825 | -57.3765 | 2024-10-07 00:36:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 81.2 |
| becb1678-8e19-3f03-831f-78b9b8a809b9 | -16.8254 | -57.3561 | 2024-10-07 00:36:41 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 50.0 |
| ea31f80e-ed8e-3865-bb01-3a5d98c1f085 | -16.8446 | -57.3743 | 2024-10-07 00:36:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 58.6 |


[Clique aqui para ver as próximas entradas](README12.md)
