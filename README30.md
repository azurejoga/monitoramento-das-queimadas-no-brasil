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

## Dados Diários - Página 30

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d9c01981-c729-3170-a924-e367ed098046 | -4.32485 | -48.63185 | 2024-10-17 04:12:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9184d889-c8fb-3efd-92ce-1b1abff73fc8 | -3.92624 | -48.34854 | 2024-10-17 04:12:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 261345b6-c440-3568-8472-835a9b21a98e | -3.9256 | -48.35255 | 2024-10-17 04:12:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7c7d4d73-4a7d-3db2-b7ec-d355270351e8 | -3.90176 | -48.36507 | 2024-10-17 04:12:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f3717840-8235-3d6f-baa0-b7d4a7d9ccf0 | -3.7623 | -47.73419 | 2024-10-17 04:12:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7589f1f6-f8d5-3386-82c4-8bed76af822f | -4.35717 | -48.49247 | 2024-10-17 04:12:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6a5751f4-f72b-3c0e-985a-3cf26821f277 | -4.35651 | -48.49638 | 2024-10-17 04:12:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| aa635261-e261-39a1-b634-1345eace2e35 | -4.33484 | -48.62503 | 2024-10-17 04:12:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b564715a-5407-3378-8084-c0a0111f06fe | -4.33226 | -48.62532 | 2024-10-17 04:12:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3dd4d380-16f0-36a3-a2eb-4e564e39b6ea | -4.33054 | -48.62432 | 2024-10-17 04:12:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a0248905-8909-3856-979e-a42be4ea4581 | -4.3273 | -48.62873 | 2024-10-17 04:12:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 933e814d-47ce-3d68-abf9-3d148c0d4d83 | -4.2886 | -48.62244 | 2024-10-17 04:12:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6577a8c1-12aa-306c-b7da-e9c994bda094 | -4.28793 | -48.6265 | 2024-10-17 04:12:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f82488f1-5da7-3f56-9ae1-8c400d98f86a | -4.28429 | -48.62177 | 2024-10-17 04:12:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 06640cb8-3eab-3a28-a48c-561d1c688aea | -3.92199 | -48.34793 | 2024-10-17 04:12:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| e07fc9f9-8bb2-3f19-a585-9f3fd2b72f58 | -3.90601 | -48.36579 | 2024-10-17 04:12:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9fc04fb2-c3ea-3d3b-89f5-a66bb6b9136e | -3.90208 | -48.33635 | 2024-10-17 04:12:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5c0fee90-4506-32f9-b4ac-f4a27c5cfbfd | -3.89784 | -48.33568 | 2024-10-17 04:12:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 35df0ef0-c197-3b48-af7d-60f320f9476f | -3.89751 | -48.36438 | 2024-10-17 04:12:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d8766c5b-6021-347f-992f-36d00eb8f413 | -3.79546 | -47.78858 | 2024-10-17 04:12:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 43c46a84-fafa-343f-8019-02b289f2d59a | -3.76579 | -47.7385 | 2024-10-17 04:12:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4a0a4373-255f-3ab9-9346-63d73de52632 | -3.7617 | -47.73782 | 2024-10-17 04:12:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2d6f97a0-87d1-3e4b-b6b0-3047efe7d576 | -5.66571 | -48.68322 | 2024-10-17 04:12:00 | NOAA-20 | SÃO DOMINGOS DO ARAGUAIA | PARÁ | Brasil | 1507151 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ecdefa65-a906-3067-9796-06dd2e1543b4 | -5.66149 | -48.68253 | 2024-10-17 04:12:00 | NOAA-20 | SÃO DOMINGOS DO ARAGUAIA | PARÁ | Brasil | 1507151 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 30969132-990c-3449-947e-234f6db9e0db | -5.22746 | -47.95826 | 2024-10-17 04:12:00 | NOAA-20 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| db81e685-9e77-38e9-830c-388936ae48df | -5.22342 | -47.95753 | 2024-10-17 04:12:00 | NOAA-20 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 471afae7-52bc-38d3-85c7-01359d507056 | -5.21998 | -47.95322 | 2024-10-17 04:12:00 | NOAA-20 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c43f2d98-8303-3c0c-adfe-b8c25a2643f2 | -5.22282 | -47.96112 | 2024-10-17 04:12:00 | NOAA-20 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dada23ca-2949-37dd-96a9-3b1401c924c7 | -3.28576 | -49.0819 | 2024-10-17 04:12:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| afafaae5-f4ce-347e-8c4e-1c5b8916265a | -2.83835 | -49.14828 | 2024-10-17 04:12:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 23.5 |
| 44c24f2d-97a7-3dd3-8623-e623e060b03d | -2.83828 | -49.15051 | 2024-10-17 04:12:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 38.4 |
| 48bc6436-3848-3ae0-ba7e-c1eb9c3ea769 | -2.83759 | -49.15305 | 2024-10-17 04:12:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 23.5 |
| c13559a7-7b33-3e95-beeb-736b04a40e93 | -2.83749 | -49.15523 | 2024-10-17 04:12:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 225135c2-7b15-3473-afb2-98fd4ce46292 | -2.83372 | -49.14978 | 2024-10-17 04:12:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 30ab33ba-efcd-37bd-943e-79d8c0738a08 | -2.83365 | -49.52368 | 2024-10-17 04:12:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 288d2929-9535-35f5-aec1-0db2d5bfc5d3 | -2.82896 | -49.52293 | 2024-10-17 04:12:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| e85818c4-16e4-3430-a029-8ad04df236f6 | -2.81409 | -49.52565 | 2024-10-17 04:12:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e9298390-716c-34c8-8030-a308e5764763 | -2.80941 | -49.52486 | 2024-10-17 04:12:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| decb21cb-a1f3-39ff-8b51-a09fe6c4f989 | -3.28787 | -49.07889 | 2024-10-17 04:12:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1ba49ff7-120b-3527-9252-1bc210cf43b3 | -3.28338 | -49.07805 | 2024-10-17 04:12:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 76f552ad-b9d9-3083-a478-10bc294c52b6 | -3.2701 | -49.09296 | 2024-10-17 04:12:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 408acaa3-9477-3724-8217-3848abba365d | -3.45734 | -50.60877 | 2024-10-17 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a6b720ea-b9a5-35c1-ae1f-7e672d28c26a | -3.45706 | -50.61051 | 2024-10-17 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 35c9f256-33ff-3214-8ac1-0a1e3cdb5d16 | -3.45686 | -50.61155 | 2024-10-17 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c5e8da8f-1003-308b-904e-061b463284d1 | -3.45207 | -50.60961 | 2024-10-17 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 76b258cb-8866-3bde-a903-4db44ee2356b | -3.43659 | -50.16282 | 2024-10-17 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| cab44aab-8b8d-3047-9595-0ca401043377 | -3.4357 | -50.15941 | 2024-10-17 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 35445886-4e86-30a4-97d8-cac3383ac612 | -3.43481 | -50.16473 | 2024-10-17 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 6ccedc8a-7397-3cbe-93bf-97538853885a | -3.43173 | -50.16213 | 2024-10-17 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| a4d6995f-7c05-3464-8396-f3a5d25b5bc7 | -3.40469 | -50.39273 | 2024-10-17 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 238b3fc3-1217-3930-9914-6fe41e992d88 | -3.40112 | -50.39413 | 2024-10-17 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 428e6ba3-986f-3985-b1d5-073011a6eb82 | -3.39976 | -50.39196 | 2024-10-17 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6d0a66f4-24ea-3ed1-9bc2-746e2ad0e25a | -3.39887 | -50.39746 | 2024-10-17 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3ffb37ff-1377-308d-9a94-657389fe49d2 | -3.30307 | -50.04591 | 2024-10-17 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 792586c1-0f82-3552-88e8-728307b05ef2 | -3.19325 | -50.31583 | 2024-10-17 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d32eff57-9178-3687-9fb0-21e05c8fcc8d | -3.19166 | -50.31365 | 2024-10-17 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5ed9453d-0967-3b72-a46d-aba777c322f1 | -3.19078 | -50.31913 | 2024-10-17 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 85a86885-9bd1-3fb5-857a-40aac7dbab24 | -3.18833 | -50.31503 | 2024-10-17 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 75bbaf64-8eab-3124-bfe4-6e8144938593 | -3.18394 | -50.20576 | 2024-10-17 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 6d6874f2-3f10-3643-b6fe-26c44efef312 | -3.17905 | -50.205 | 2024-10-17 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b1d64451-f7b0-3070-a21f-9dae0b8e1a24 | -3.07628 | -50.3685 | 2024-10-17 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 20520458-46d3-39ca-8c8d-7f3fa6997a4c | -3.07534 | -50.37409 | 2024-10-17 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| a0309121-5151-3490-8cc9-6bd03b84e2b9 | -3.07512 | -50.36862 | 2024-10-17 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 0c9d297e-0ff6-3e44-99f0-dfb80ee721b6 | -3.07422 | -50.37423 | 2024-10-17 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 78a6c31d-3d4d-34d5-a938-7cf6a6e02712 | -3.07332 | -50.37985 | 2024-10-17 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d0c5b92b-09df-3f37-a45d-60fb2101c9a6 | -3.07134 | -50.36769 | 2024-10-17 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 870d67c3-ef32-3821-b9be-5ef4e51e6046 | -3.0704 | -50.37327 | 2024-10-17 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| eee1f0bb-f50c-3586-9808-881ef0dec458 | -3.07017 | -50.3678 | 2024-10-17 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| f0710a70-cfaf-30ab-9de0-a0800f13afa5 | -3.06944 | -50.3789 | 2024-10-17 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| b4283b92-c534-3d8d-9463-61bf5bd647b0 | -3.06927 | -50.3734 | 2024-10-17 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 5bfee4c2-01b0-3544-b1a7-bee09383b24c | -3.06639 | -50.36689 | 2024-10-17 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 03ded7ae-e9f5-3be8-8b76-4fecd07c9ee7 | -3.0663 | -50.48863 | 2024-10-17 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4134f2ab-6643-36b2-aa5b-751207699f08 | -3.06602 | -50.48912 | 2024-10-17 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ae26433f-d6cd-3c54-a3ef-af7e907dfb75 | -3.06534 | -50.49432 | 2024-10-17 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f7947026-fb49-32b0-951b-e7c6cc0cd924 | -3.06523 | -50.36699 | 2024-10-17 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 79d81ba5-1482-3ffd-b5b7-d7853ce2f34d | -2.83651 | -49.86824 | 2024-10-17 04:12:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f5ba0a42-b0d3-3e51-8aab-717a3f00de80 | -5.13356 | -49.57496 | 2024-10-17 04:12:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c7b2d1f2-ddde-346a-a5cf-04e53da24c6a | -4.48818 | -50.15223 | 2024-10-17 04:12:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3307e06f-47d2-3177-9daa-6d08b9e2f6dc | -4.14841 | -50.21857 | 2024-10-17 04:12:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 13eebe85-c606-3838-bb92-cc19bfabb651 | -4.0953 | -50.75778 | 2024-10-17 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8e82252e-2734-3c3e-91b2-08112dde528d | -4.09482 | -50.76059 | 2024-10-17 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| aa35eacf-c644-3fd9-8756-9a69772c04b8 | -4.09432 | -50.76347 | 2024-10-17 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| eb59f2ad-7382-3624-b5b4-ae0b1662577b | -4.09382 | -50.76644 | 2024-10-17 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3d042213-fef8-324a-b488-47d507963c1d | -4.03405 | -50.37819 | 2024-10-17 04:12:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 38fee14a-a834-3d07-a457-7ee11ccc0972 | -3.87188 | -50.05004 | 2024-10-17 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2e5eb8ae-227c-3293-8406-d4e8b5ae9089 | -3.65178 | -50.19723 | 2024-10-17 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 7cc8cd6c-3c6e-3859-ac71-f5627f442bf0 | -3.65094 | -50.20243 | 2024-10-17 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 79cd95b1-9f70-36f6-aeb2-78debee4cbfe | -3.65034 | -50.19782 | 2024-10-17 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 7763bdc7-577a-3792-b601-f62d7d1968f7 | -3.64947 | -50.203 | 2024-10-17 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4fafc1a0-3c83-38fb-82b3-2eeee94349ba | -3.64694 | -50.19641 | 2024-10-17 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 3665d4c0-c237-3778-b757-fe94be10bcf2 | -3.6455 | -50.19701 | 2024-10-17 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 85e1f33f-4d58-3625-a980-9f865178e1dc | -3.63765 | -49.83274 | 2024-10-17 04:12:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e90af028-580f-323b-ae81-0cffb3bbb027 | -3.58569 | -50.57608 | 2024-10-17 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5f60dc3c-5703-3a53-97bd-67572d7338a8 | -3.5813 | -50.57576 | 2024-10-17 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 0e4d4c24-5263-3e93-be55-bd346b27174e | -3.58072 | -50.57524 | 2024-10-17 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 76483b4d-1c4f-3de8-886c-21f9281c1eb1 | -3.57981 | -50.58087 | 2024-10-17 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8843caee-5d30-380d-add0-284dc11169d6 | -3.57825 | -50.56363 | 2024-10-17 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 592d6ddf-530d-38d9-a43c-0d4807860475 | -3.57758 | -50.56306 | 2024-10-17 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 159aea0e-c48a-3a54-b425-21a12a032d66 | -3.5773 | -50.56926 | 2024-10-17 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 509587a2-77e5-333a-b4de-9cf2fe0f9089 | -3.57667 | -50.56869 | 2024-10-17 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |


[Clique aqui para ver as próximas entradas](README31.md)
