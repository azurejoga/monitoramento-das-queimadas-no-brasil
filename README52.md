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

## Dados Diários - Página 52

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 92a40f06-2e83-356b-812f-519f01dad833 | -7.67849 | -47.31052 | 2024-10-26 04:19:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 00d550a4-56e7-3219-b4f4-13f54fc7e840 | -7.67435 | -47.31386 | 2024-10-26 04:19:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f3106896-635a-3602-b8d0-e6a1d3f8bfb6 | -7.67149 | -47.30939 | 2024-10-26 04:19:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1c536a74-10cd-3d25-ace7-bf40c532ed91 | -7.67085 | -47.3133 | 2024-10-26 04:19:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e8a9bd54-f3be-3cf2-b488-2ecdb88924fb | -7.66799 | -47.30882 | 2024-10-26 04:19:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fcb623cd-0191-370d-afd7-c6d1e8f7e9e1 | -7.66735 | -47.31273 | 2024-10-26 04:19:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 54e14a78-e9b1-3508-b5b2-b15fa6b397c6 | -7.66671 | -47.31663 | 2024-10-26 04:19:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a7ae9820-c67f-35a3-9911-0aacabfec2c2 | -7.65156 | -47.52014 | 2024-10-26 04:19:00 | NPP-375D | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1802f028-adb3-309f-9c92-2053e8f743f6 | -7.59672 | -47.08326 | 2024-10-26 04:19:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 15c35402-7b35-39f4-9eb1-ffc991e933c2 | -7.59263 | -47.08649 | 2024-10-26 04:19:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 056c9afa-283c-3cbd-bebf-6d76f8932754 | -7.58477 | -47.11279 | 2024-10-26 04:19:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b8fdd770-6740-32c8-bede-decbb4f98504 | -7.58414 | -47.11665 | 2024-10-26 04:19:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5f40c8eb-23b4-300e-857c-7cfc8dea1752 | -7.47988 | -47.35556 | 2024-10-26 04:19:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2e656145-78c6-3780-b133-365015acb588 | -7.47924 | -47.35949 | 2024-10-26 04:19:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 692458ec-ba6b-3f0a-852e-eeeb2a89d562 | -7.45044 | -46.91239 | 2024-10-26 04:19:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6420debb-10be-3dc6-8ecc-653dfc860bcb | -7.44983 | -46.91616 | 2024-10-26 04:19:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d7335af9-e0b4-3fa5-854e-34d30f176b17 | -7.44699 | -46.91181 | 2024-10-26 04:19:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 13d17e1e-4a85-3586-adca-8879cbbc645d | -7.43354 | -47.35201 | 2024-10-26 04:19:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 34bd7f51-4766-3df2-8771-9830fc361f63 | -7.36361 | -46.98789 | 2024-10-26 04:19:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2b7458fe-423e-3b1d-8038-5bb9f21b2edf | -7.36015 | -46.98734 | 2024-10-26 04:19:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 354aac19-8f56-3df4-a8bc-14391c2b3399 | -7.33077 | -47.23172 | 2024-10-26 04:19:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 38f953ce-cd8f-3f3f-9dbd-e2aaae58fd72 | -7.28439 | -47.1808 | 2024-10-26 04:19:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 54ef03b5-a2cc-3b43-aa48-21eef00092f2 | -7.23816 | -46.9521 | 2024-10-26 04:19:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| be21902f-a1ef-3bc4-84c6-2854666ef4d3 | -7.23753 | -46.95603 | 2024-10-26 04:19:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f96fb8ee-c9e1-3324-bcef-597de29ff017 | -7.07384 | -46.87949 | 2024-10-26 04:19:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2d74df5a-d677-3219-b18a-0ee662487dbd | -7.071 | -46.87516 | 2024-10-26 04:19:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e9829dc1-84c2-3dd9-8334-f1c2ae290db4 | -7.06753 | -46.8746 | 2024-10-26 04:19:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 39170a30-6725-3d64-869f-3bff047865d1 | -6.92369 | -46.84125 | 2024-10-26 04:19:00 | NPP-375D | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3fe119d3-716d-3947-a4aa-f06a2b8549c7 | -9.26955 | -47.91177 | 2024-10-26 04:19:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 875f6df7-9f74-3c05-b4b8-c35b01201cc7 | -9.26602 | -47.91116 | 2024-10-26 04:19:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4860730a-98e8-3b4e-bc8e-18ef39fc2380 | -9.26249 | -47.91056 | 2024-10-26 04:19:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4d9fd466-8386-3345-ad04-a7db122aec90 | -9.10271 | -47.65445 | 2024-10-26 04:19:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3a0d4dd3-c0e6-350b-bcb1-dbf0d0f10e90 | -9.0772 | -48.00607 | 2024-10-26 04:19:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1f8493cb-b004-3a5b-af6b-a96e33effece | -9.07365 | -48.00547 | 2024-10-26 04:19:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6b38748b-3d0b-3e60-a56c-e38e3c806778 | -9.07077 | -48.0008 | 2024-10-26 04:19:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a34aa6c0-d54d-3be6-a852-d903e2083384 | -9.0701 | -48.00485 | 2024-10-26 04:19:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5f647e61-8974-3088-939f-d5ff95e3da3c | -9.06721 | -48.00019 | 2024-10-26 04:19:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e30441f7-e2a2-3619-9791-8f5ed6af5a37 | -9.06654 | -48.00423 | 2024-10-26 04:19:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a7a3c7d0-dff6-3b26-8864-e5aa439741ea | -8.97902 | -47.74831 | 2024-10-26 04:19:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 37f36e9f-4384-3b2b-b205-6a75a639284e | -8.97549 | -47.74776 | 2024-10-26 04:19:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a16bf3d1-3eac-3b1c-baf5-7ffc6844c9db | -8.97519 | -47.66265 | 2024-10-26 04:19:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d0ef5666-ea5b-3bf9-870d-9261ba20e070 | -8.97473 | -47.66286 | 2024-10-26 04:19:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5f56da23-4227-3f76-91d0-4a67a7cca8c4 | -8.86412 | -47.54509 | 2024-10-26 04:19:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 03648b08-88de-34b3-9181-1c2b5c506eaa | -8.8056 | -47.86024 | 2024-10-26 04:19:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7dd3c1b6-84b3-3cb4-9938-b8a4b2fcd8b1 | -8.80206 | -47.85963 | 2024-10-26 04:19:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 968052c9-051b-3f67-a197-54db9e4db83d | -8.47317 | -47.8159 | 2024-10-26 04:19:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3e53d788-f5eb-361c-a215-8db0a38c4a42 | -8.47028 | -47.81132 | 2024-10-26 04:19:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 741563be-4b93-3b82-8e3a-d5e02e6ca730 | -8.46962 | -47.81532 | 2024-10-26 04:19:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4feb291b-41d8-3225-93af-779bc8414eb9 | -8.46896 | -47.81933 | 2024-10-26 04:19:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 95475290-ed05-37c2-8ba3-e3f21c73a18b | -8.46607 | -47.81475 | 2024-10-26 04:19:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4dae7986-2480-322a-872d-1a2e65d53564 | -9.22894 | -48.62455 | 2024-10-26 04:19:00 | NPP-375D | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4d74988d-98c6-37e9-bb6c-e4b7bed73820 | -9.05548 | -48.72201 | 2024-10-26 04:19:00 | NPP-375D | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 67c5ed02-0cc0-3609-b19b-f8dacc144d18 | -9.05474 | -48.72639 | 2024-10-26 04:19:00 | NPP-375D | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 362d6482-d4bd-3f02-9142-bf3aadc85b2c | -9.05179 | -48.72141 | 2024-10-26 04:19:00 | NPP-375D | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 36a346a3-0b84-3ed8-959a-75af2c6127ae | -9.05105 | -48.72579 | 2024-10-26 04:19:00 | NPP-375D | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1d6f6743-466d-3475-80da-1bc01343487d | -9.04809 | -48.72081 | 2024-10-26 04:19:00 | NPP-375D | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cd99181c-c02c-3ba5-b7fb-e88e0293d0fe | -8.90692 | -48.54013 | 2024-10-26 04:19:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a812b4d5-85a5-3cd0-a5bc-3b37aa5c60e9 | -8.90395 | -48.53531 | 2024-10-26 04:19:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 461e36bc-3038-361d-b3ea-8c38048e216d | -8.90325 | -48.53956 | 2024-10-26 04:19:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 10363a3a-e3d6-34f3-ab7c-6190a764f010 | -8.89663 | -48.53411 | 2024-10-26 04:19:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 5.8 |
| b9da150c-9915-3ab1-9f0c-d137e32dd013 | -8.89297 | -48.5335 | 2024-10-26 04:19:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 5.8 |
| c99c6e6a-db80-34a2-bacf-7a91f3e1cbf7 | -8.64911 | -48.58387 | 2024-10-26 04:19:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b5d072af-ccc0-3b6a-9f7b-e9cdc6c9856f | -9.99301 | -48.85284 | 2024-10-26 04:19:00 | NPP-375D | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 234bee76-0f58-3f2c-a9c1-5d8d234c026d | -9.99297 | -48.80852 | 2024-10-26 04:19:00 | NPP-375D | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 718d1981-d1cb-35de-8191-5c2cad01e05f | -9.94743 | -48.95472 | 2024-10-26 04:19:00 | NPP-375D | MONTE SANTO DO TOCANTINS | TOCANTINS | Brasil | 1713700 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f889c678-8add-319f-a117-13b7a299b8fd | -9.94651 | -48.94805 | 2024-10-26 04:19:00 | NPP-375D | MONTE SANTO DO TOCANTINS | TOCANTINS | Brasil | 1713700 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| efd471cc-5be1-33f2-bb50-2d3b5d9ade64 | -9.93715 | -48.69897 | 2024-10-26 04:19:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b92ed590-2ba9-3028-81cd-92613681dcd0 | -9.39202 | -48.76494 | 2024-10-26 04:19:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8639ef3d-d4a3-32f6-9f79-4a5c4198f5f6 | -9.87139 | -47.72471 | 2024-10-26 04:19:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 83f03c67-1f15-30d7-be64-be621e2faa2a | -9.81789 | -47.85237 | 2024-10-26 04:19:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| aaa39cf4-054f-3186-86ba-d62a9e459020 | -9.81439 | -47.85178 | 2024-10-26 04:19:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c8210898-51cc-3f7c-834f-e901160a6977 | -9.80901 | -47.59597 | 2024-10-26 04:19:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 199af1d8-a5ae-3af8-977e-4a714c438b5d | -9.77571 | -48.23598 | 2024-10-26 04:19:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7b37325a-a447-329e-9f45-ec063f00251b | -9.74021 | -48.2606 | 2024-10-26 04:19:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 827090fe-93bb-3856-bf4e-3f04998c6484 | -9.73881 | -48.25902 | 2024-10-26 04:19:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| c2c542f6-cbca-3ed1-8cd7-b0879abb408f | -9.73812 | -48.26311 | 2024-10-26 04:19:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| b94d77fa-a474-30d4-a3ce-f09269f50395 | -9.73743 | -48.26721 | 2024-10-26 04:19:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ed0caf05-e277-3f75-a6ca-2047220b3bf5 | -9.73664 | -48.25995 | 2024-10-26 04:19:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| cb1ebf34-7a57-37ec-adb5-1474b738134d | -9.73598 | -48.26403 | 2024-10-26 04:19:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 3862e177-8a6d-3e1d-9041-0584fc224dcc | -9.73306 | -48.25938 | 2024-10-26 04:19:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 053a26f5-760d-3129-94d5-2a38b2574863 | -9.7324 | -48.26342 | 2024-10-26 04:19:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 16f10d4a-56c0-3677-b4bb-706f1b8b74c7 | -9.72883 | -48.26281 | 2024-10-26 04:19:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c968fdef-40a4-3b4f-a880-7f600bc6996c | -9.70623 | -47.73904 | 2024-10-26 04:19:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1ce5fc0d-01ca-3fad-a573-997c47988943 | -9.63665 | -47.59592 | 2024-10-26 04:19:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6254f25d-b2a3-32e6-9991-4e0c181a225b | -9.63517 | -47.59642 | 2024-10-26 04:19:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1df2ccc0-0348-393f-9d5e-9dc3b98111c0 | -9.63318 | -47.59534 | 2024-10-26 04:19:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b5b8e639-57a3-31f7-be77-9876db6d6b9e | -9.63169 | -47.59583 | 2024-10-26 04:19:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8541d24f-24f6-33c6-8270-1f34d0bc8967 | -9.62382 | -47.62238 | 2024-10-26 04:19:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1be86d88-49f2-398e-aa28-d00076f22f8d | -9.62034 | -47.62179 | 2024-10-26 04:19:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c5fda25e-94e4-31f6-99b4-950f92ea00fd | -9.50729 | -47.80737 | 2024-10-26 04:19:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4a371909-b6f6-3751-8f48-86968b318e16 | -9.50663 | -47.81129 | 2024-10-26 04:19:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b1f73c2a-d239-3c55-848a-c66d3293e12a | -9.50598 | -47.81525 | 2024-10-26 04:19:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| becd032b-046d-3dfc-ab00-4eafb6ad13cf | -9.50378 | -47.80676 | 2024-10-26 04:19:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c5dccbfb-601b-33c9-92df-27091c2badc8 | -9.50313 | -47.81069 | 2024-10-26 04:19:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5e51045f-b432-3254-9935-50c772020702 | -9.50247 | -47.81465 | 2024-10-26 04:19:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d41b926a-16ea-3473-8fa2-3c06afa49071 | -9.49962 | -47.81009 | 2024-10-26 04:19:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0c3e2ada-22fc-3fbe-b134-bad662e63ea5 | -9.49896 | -47.81403 | 2024-10-26 04:19:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b5efeeaf-33e8-331b-bb63-e2d462a27a7e | -9.49545 | -47.81342 | 2024-10-26 04:19:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 79dd6b25-2d33-38f3-93e8-c0675c5b3043 | -9.4948 | -47.81736 | 2024-10-26 04:19:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d6d3fd01-a7f9-3090-95b5-e2981c6a9899 | -9.49135 | -47.81732 | 2024-10-26 04:19:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README53.md)
