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
| a7868160-f275-34e8-a411-fc79dcb54c22 | -7.2597 | -43.0645 | 2025-07-08 00:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 156.4 |
| 55951ab0-a483-3849-8755-114f16c0e239 | -11.4205 | -45.095 | 2025-07-08 00:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 65.0 |
| a8b12b4a-0302-38e7-b0fc-436272f870d0 | -7.2405 | -43.0899 | 2025-07-08 00:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 171.5 |
| ca3662a1-dc56-3cac-96b9-0cff676894d5 | -10.9811 | -45.1104 | 2025-07-08 00:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 180.0 |
| ac482a0f-f93e-31bc-9bc4-4b80ba25fbb1 | -9.2255 | -48.6 | 2025-07-08 00:00:00 | GOES-19 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 48.9 |
| d9c6794d-1d66-323e-a214-7b56b87dda15 | -7.2408 | -43.0664 | 2025-07-08 00:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 132.3 |
| 2ec62fb2-beae-3b70-b34a-f988e116d182 | -7.2025 | -43.1171 | 2025-07-08 00:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 122.3 |
| 671ddbc7-f9cd-34a2-98f2-bd4b5c6d8888 | -10.6489 | -49.4483 | 2025-07-08 00:00:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 83.2 |
| 2a0d4ba4-4fdd-3ff1-9201-b36fe0392dcc | -7.2023 | -43.1406 | 2025-07-08 00:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 120.8 |
| 8e1912cd-fda6-3a2f-8056-8337fca9f72b | -10.6486 | -49.47 | 2025-07-08 00:00:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 93.1 |
| daf8c0c0-a779-3036-8c65-e84cb0d6a96e | -7.2594 | -43.0881 | 2025-07-08 00:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 215.8 |
| 09c7b535-0436-3fa0-a0cd-7193385d69b1 | -11.4397 | -45.0923 | 2025-07-08 00:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 64.1 |
| c3ef3b62-898c-31a0-b4cc-a03c87672338 | -10.9808 | -45.1335 | 2025-07-08 00:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 43.4 |
| 11862d89-5d4d-3861-9143-5ec3b8040d3a | -10.6299 | -49.4504 | 2025-07-08 00:00:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 63.5 |
| 74338a80-e60f-308d-a825-1992340b9791 | -11.0003 | -45.1078 | 2025-07-08 00:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 49.6 |
| d51d825a-6042-3418-8d7b-094292edc3dc | -10.962 | -45.113 | 2025-07-08 00:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 101.8 |
| 12271341-bb23-3302-9094-4c3c794a1853 | -10.6299 | -49.4504 | 2025-07-08 00:10:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 95.6 |
| 2d9916d4-2d7d-3824-98f3-dce1097e6447 | -10.6489 | -49.4483 | 2025-07-08 00:10:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 85.5 |
| 40c1749a-38ca-3119-887e-6fa0dbd645ac | -7.2408 | -43.0664 | 2025-07-08 00:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 108.5 |
| fac6597b-0979-35cc-a045-a0ada3a55b50 | -10.6296 | -49.472 | 2025-07-08 00:10:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 55.6 |
| fb88cea6-6481-36fe-961e-3db2ee348363 | -10.9811 | -45.1104 | 2025-07-08 00:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 72.3 |
| 33867b2e-196b-3017-95be-37a85b7fdbdf | -7.2594 | -43.0881 | 2025-07-08 00:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 217.5 |
| 88a4a598-f3df-3e08-b231-8073fc1801c2 | -7.2405 | -43.0899 | 2025-07-08 00:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 117.1 |
| 4f140e0b-1599-34dc-a02f-6098c28269fe | -11.4205 | -45.095 | 2025-07-08 00:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 42.2 |
| 448b125a-f4c8-3f28-b9e6-98993cffa9db | -7.2023 | -43.1406 | 2025-07-08 00:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 122.0 |
| 7bb4b4ed-6b5a-3805-aaf7-57c32025c684 | -11.4397 | -45.0923 | 2025-07-08 00:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 53.0 |
| c1b32142-71c1-3f31-aae8-d65f3acd81cc | -7.2597 | -43.0645 | 2025-07-08 00:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 167.1 |
| 40b2ffab-51f0-3ac0-b924-8ab847891d42 | -10.6486 | -49.47 | 2025-07-08 00:10:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 98.9 |
| a437bb9d-28b4-32f4-8082-dfbb20ad87d2 | -7.2025 | -43.1171 | 2025-07-08 00:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 112.7 |
| 164536c9-484e-399a-a341-d219dd53f0fd | -11.4205 | -45.095 | 2025-07-08 00:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 144.2 |
| 5ee9e951-1da8-39a8-bc8a-928619fe25f0 | -10.6489 | -49.4483 | 2025-07-08 00:20:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 105.6 |
| 14686261-ea8d-31f0-be1b-5806e997980b | -11.4397 | -45.0923 | 2025-07-08 00:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 101.9 |
| 7a37f072-9531-3238-8d8d-8402f55e868f | -7.2408 | -43.0664 | 2025-07-08 00:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 101.6 |
| c742de2f-4097-3930-9af4-b31b55520c9e | -11.4393 | -45.1154 | 2025-07-08 00:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 69.0 |
| b1c6387f-2ab2-39e7-a91d-10c983e1e7e2 | -7.2025 | -43.1171 | 2025-07-08 00:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 99.5 |
| b6c39e13-d466-3fa5-a387-1cb71e35c52d | -10.6299 | -49.4504 | 2025-07-08 00:20:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 78.1 |
| c3ea559b-8db1-3d79-ae4a-7efcdfe77d60 | -11.4201 | -45.1181 | 2025-07-08 00:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 80.7 |
| 2d7bae68-d454-35b5-96e7-d26e72fb97a0 | -10.6296 | -49.472 | 2025-07-08 00:20:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 56.1 |
| e0ea4bde-4b12-3ece-8d79-2746139a75f0 | -7.2023 | -43.1406 | 2025-07-08 00:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 97.4 |
| 7e1c699d-ef5e-3a59-9fa4-7493c306eb73 | -7.2597 | -43.0645 | 2025-07-08 00:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 159.2 |
| f7016629-2950-3fd6-a953-3c0eda7f5f23 | -7.2405 | -43.0899 | 2025-07-08 00:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 124.2 |
| c17e63af-4158-33ba-bb9e-904241e4ab0c | -10.6486 | -49.47 | 2025-07-08 00:20:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 126.3 |
| e5e0e70d-1f67-34a1-b32e-ba075492bb7e | -7.1837 | -43.1189 | 2025-07-08 00:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 83.1 |
| 6bf1afb2-4371-33f1-a965-3c45fd7a640a | -7.2594 | -43.0881 | 2025-07-08 00:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 213.6 |
| 76b038b1-76fd-30cb-b46b-f031b2f1bef6 | -10.962 | -45.113 | 2025-07-08 00:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 68.6 |
| 2868edcb-3c0b-30b1-bcd3-c34b07a8ba92 | -7.1834 | -43.1424 | 2025-07-08 00:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 82.9 |
| 98f32846-07ae-3d30-a794-f48ab9db91d3 | -10.9811 | -45.1104 | 2025-07-08 00:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 103.5 |
| 5e589a76-1c72-36fb-9e18-46d5451851d1 | -10.9811 | -45.1104 | 2025-07-08 00:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 82.2 |
| e64018bf-07ae-3387-9545-d7f869c2566a | -10.6299 | -49.4504 | 2025-07-08 00:30:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 92.2 |
| 0ee66b6f-0f3b-32b1-bfbe-17745834adbd | -12.3241 | -49.3144 | 2025-07-08 00:30:00 | GOES-19 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 53.1 |
| 7855c696-6307-38ff-8a3f-089e97cd6b16 | -7.2408 | -43.0664 | 2025-07-08 00:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 104.8 |
| de0d48b4-a896-359c-a981-5ff37cf45952 | -11.4205 | -45.095 | 2025-07-08 00:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 37.7 |
| 565e3d8c-2721-3351-b750-82e35d607acb | -7.2025 | -43.1171 | 2025-07-08 00:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 85.9 |
| b2236b6b-9afd-3c4a-9870-5aec6bd689fc | -7.2597 | -43.0645 | 2025-07-08 00:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 175.9 |
| 70223513-bf38-365e-98e0-87fe6f6f0889 | -10.6296 | -49.472 | 2025-07-08 00:30:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 69.4 |
| dc3ee3cc-7e2f-3f59-ba0a-9a727697b84c | -10.962 | -45.113 | 2025-07-08 00:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 44.7 |
| e4b2877a-4044-36e9-bf28-dc9696196407 | -7.1834 | -43.1424 | 2025-07-08 00:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 83.5 |
| 669757aa-db32-3f4a-85a3-3c0469bfc901 | -7.2023 | -43.1406 | 2025-07-08 00:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 97.3 |
| 7fd9590c-199e-36fd-9446-e235da3120f2 | -10.6486 | -49.47 | 2025-07-08 00:30:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 132.1 |
| f72bbeb9-acfe-3161-8bf5-ecdab7f68205 | -7.2594 | -43.0881 | 2025-07-08 00:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 192.0 |
| 1199ae47-7360-30b0-a68c-2e60a7af97e4 | -7.2405 | -43.0899 | 2025-07-08 00:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 94.3 |
| 4311c6eb-0964-39fa-92dc-e05077cd7097 | -10.6489 | -49.4483 | 2025-07-08 00:30:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 87.6 |
| 54a1a78d-a64b-317b-b76d-620919da737c | -11.4397 | -45.0923 | 2025-07-08 00:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 49.8 |
| d4d5119e-7b81-3b95-934a-77ea7e01be04 | -10.9811 | -45.1104 | 2025-07-08 00:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 53.7 |
| b9b8d63a-e330-3ef7-881f-7291caeb6eab | -7.2023 | -43.1406 | 2025-07-08 00:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 105.1 |
| 9ca480f6-7bff-32cd-9169-e20c54364554 | -7.2594 | -43.0881 | 2025-07-08 00:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 181.0 |
| 9c21f7e1-28cf-3663-be25-5956e38b81f9 | -11.4205 | -45.095 | 2025-07-08 00:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 93.8 |
| a8b7f1c0-8958-3d97-a0e2-0e4ae32574a8 | -7.1834 | -43.1424 | 2025-07-08 00:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 86.5 |
| 0350272f-55eb-358d-b9ad-4aee03c7009f | -7.2597 | -43.0645 | 2025-07-08 00:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 166.2 |
| 4d326b3b-acd1-3599-b5e3-7558f714a18e | -7.2408 | -43.0664 | 2025-07-08 00:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 116.6 |
| 1d909050-0306-3d38-9560-9c8f3dd171a3 | -11.4397 | -45.0923 | 2025-07-08 00:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 85.5 |
| c0914bd6-408a-334f-b284-6af057c15648 | -7.2025 | -43.1171 | 2025-07-08 00:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 87.8 |
| 0f58e762-0cc1-3583-b1fd-deae71b8e7a8 | -7.2405 | -43.0899 | 2025-07-08 00:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 104.5 |
| a59d7eaf-b096-35d2-9c3c-d89360a9032e | -11.4393 | -45.1154 | 2025-07-08 00:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 67.3 |
| 42c82158-9baf-39de-8e5a-60a2aaef0250 | -10.6486 | -49.47 | 2025-07-08 00:40:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 45.2 |
| 88ff9251-3d44-309a-9dd6-7c9b4dc09857 | -11.4201 | -45.1181 | 2025-07-08 00:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 59.5 |
| bb89c4aa-7b11-31da-ad3b-3965eec2774f | -11.4397 | -45.0923 | 2025-07-08 00:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 130.7 |
| ea72b1d7-94e2-337f-a16a-d5384a0ec2d7 | -10.6299 | -49.4504 | 2025-07-08 00:50:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 67.4 |
| f9539d1f-c033-32fb-b2f1-a712a8bdf5b6 | -10.6296 | -49.472 | 2025-07-08 00:50:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 47.8 |
| 9e9296b4-c310-3102-a3f6-e7c740c489e3 | -15.8068 | -49.9492 | 2025-07-08 00:50:00 | GOES-19 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 56.2 |
| 47cfc813-1132-3451-a534-ff38883a6d6e | -11.4393 | -45.1154 | 2025-07-08 00:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 81.7 |
| 8bfb47d7-edd6-33d0-a0b6-e4a86e26cce5 | -11.4205 | -45.095 | 2025-07-08 00:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 97.6 |
| b50eeb35-3922-3449-b30c-7b96e66ea2dc | -15.8063 | -49.9712 | 2025-07-08 00:50:00 | GOES-19 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 51.8 |
| c35d3eb7-312c-3b74-83f8-9b34b48c2665 | -15.8264 | -49.946 | 2025-07-08 00:50:00 | GOES-19 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 57.1 |
| 82f8d32e-c577-3a7d-9d8d-ce52f0d8ba91 | -10.6486 | -49.47 | 2025-07-08 00:50:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 79.3 |
| 37ef0c6c-e7d6-339c-a582-4bd396f78884 | -10.9811 | -45.1104 | 2025-07-08 00:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 73.3 |
| 1972e539-ab5d-31e7-8bf2-8bb840d3b112 | -7.2597 | -43.0645 | 2025-07-08 00:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 135.1 |
| 51d249fc-58b7-3085-82d0-c34b0a768dec | -10.6489 | -49.4483 | 2025-07-08 00:50:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 87.3 |
| 872315c0-b49c-3ab1-a806-8356205e9d15 | -7.2594 | -43.0881 | 2025-07-08 00:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 178.2 |
| 72a22b65-b18a-3715-a411-9e2c668985d5 | -7.2405 | -43.0899 | 2025-07-08 00:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 116.2 |
| 615235f1-5078-3822-ba52-6efc2d3cf59c | -11.4201 | -45.1181 | 2025-07-08 00:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 57.6 |
| c46dd88e-a072-320f-8cd6-20c8cc8bff0f | -15.8259 | -49.9681 | 2025-07-08 00:50:00 | GOES-19 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 52.1 |
| 2bb66f97-a702-32b0-b8d4-e794a8f5ab69 | -7.2023 | -43.1406 | 2025-07-08 00:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 105.2 |
| 127dba2f-20e4-3881-9b92-d0d282540981 | -7.2408 | -43.0664 | 2025-07-08 00:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 107.1 |
| f4ef7955-e476-3c97-9619-d76361b5fe9b | -7.2025 | -43.1171 | 2025-07-08 00:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 116.0 |
| 9fb1def0-274d-375b-be27-79724cfbf51c | -7.2023 | -43.1406 | 2025-07-08 01:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 94.2 |
| 059af096-c975-3e97-b7df-0e1499758bae | -7.2408 | -43.0664 | 2025-07-08 01:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 99.1 |
| 33888a53-0610-3299-b6eb-33896cfa7525 | -11.4393 | -45.1154 | 2025-07-08 01:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 54.2 |
| 4436f3dc-1a2e-31fa-a37f-5d0ecacf0cb2 | -7.2597 | -43.0645 | 2025-07-08 01:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 158.8 |
| b8180ef2-95ac-3c4c-b0d1-c9cd0fc0e74a | -11.4397 | -45.0923 | 2025-07-08 01:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 45.1 |


[Clique aqui para ver as próximas entradas](README2.md)
