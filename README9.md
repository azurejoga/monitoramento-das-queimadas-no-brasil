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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4dddc49c-cc59-3b8d-a45a-9e4e9a8645b9 | -2.7602 | -54.4349 | 2024-11-03 01:05:22 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 166.7 |
| f83acae6-7fc9-3edc-ad8b-a2759bdfbdb6 | -2.7603 | -54.4149 | 2024-11-03 01:05:22 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 173.7 |
| 395a0b04-7bb5-32c8-80ee-368d79be4318 | -2.7876 | -51.6099 | 2024-11-03 01:05:22 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 1684ce39-49c5-3bf8-be12-8fd90f84839f | -3.0397 | -53.2603 | 2024-11-03 01:05:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 27e45fb7-2d65-3e78-9e94-2ffe88db3bc2 | -3.055 | -54.1474 | 2024-11-03 01:05:23 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 82.6 |
| 81e6c242-3024-3c91-a6ee-14ac19aa1b3e | -3.0734 | -54.167 | 2024-11-03 01:05:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 103.7 |
| 5f097c30-c962-3530-a2ac-5122bab73ca1 | -3.0734 | -54.147 | 2024-11-03 01:05:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 154.2 |
| c209138c-afc7-3f0d-8d6a-3d2ca84be527 | -3.0918 | -54.1465 | 2024-11-03 01:05:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 53.7 |
| 5e4230c6-ef5e-3440-b1d9-09629dc4ccdc | -3.1059 | -50.3105 | 2024-11-03 01:05:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 113.5 |
| dd818db5-3b7e-3637-80ef-cb2674c2daa8 | -3.106 | -50.2896 | 2024-11-03 01:05:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 183.6 |
| fb3bcb9a-bb96-35b6-b182-ddb1767d0bb0 | -3.1061 | -50.2686 | 2024-11-03 01:05:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 41.9 |
| 02743fac-ecc9-3712-93d5-bd7d9cc82985 | -3.1213 | -51.1036 | 2024-11-03 01:05:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 41.9 |
| 1870c953-f5e5-37fe-b401-816b5f30ce70 | -3.2047 | -53.4179 | 2024-11-03 01:05:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 9fb6cf89-796f-3922-ac88-fb185a34e9a2 | -3.2415 | -53.4169 | 2024-11-03 01:05:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 48.9 |
| 9c68f1da-4b77-3949-9319-20b406ab5f68 | -3.2415 | -53.3967 | 2024-11-03 01:05:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 56.1 |
| de045224-2f91-3c5e-b854-7d2e276e9ac7 | -3.3276 | -50.2825 | 2024-11-03 01:05:25 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 88.5 |
| f7f7f44b-065b-3cb3-8854-26435807a4be | -3.3277 | -50.2615 | 2024-11-03 01:05:25 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 96.4 |
| 823201a8-4b3a-3c94-b9b7-24e8b564c16b | -3.3872 | -45.4432 | 2024-11-03 01:05:25 | GOES-16 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 56.9 |
| 18a27f37-eb14-373e-b718-2d679c5e8262 | -3.4749 | -50.3826 | 2024-11-03 01:05:26 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 112.8 |
| 3c26c70d-8f35-30d4-94cc-5d4c19efe2ce | -3.5466 | -50.8611 | 2024-11-03 01:05:26 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 52.7 |
| 99378fc9-07c2-3fec-850e-d67fb59de21d | -3.9473 | -48.3666 | 2024-11-03 01:05:28 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 68.9 |
| b8728e1a-79ed-3191-bd94-a90d44547c67 | -3.9474 | -48.3451 | 2024-11-03 01:05:28 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 86.6 |
| 62263795-238a-3d14-85c5-0fea48da9611 | -4.4054 | -43.4746 | 2024-11-03 01:05:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 65.5 |
| 1e1345bd-6da1-3b39-b0ef-db6d965ace89 | -4.4056 | -43.4514 | 2024-11-03 01:05:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 77.6 |
| e363fb09-088a-3925-86bf-5569ab7db1c9 | -17.6469 | -57.480202 | 2024-11-03 01:05:39 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 8471fa0b-23e4-31ab-a342-dd86e5b99123 | -8.7059 | -48.0181 | 2024-11-03 01:05:55 | GOES-16 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 77.4 |
| e243c44e-336d-302c-93e3-6d2fa7dd81c0 | -8.7062 | -47.9962 | 2024-11-03 01:05:55 | GOES-16 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 66.1 |
| 7bcdd6bc-d825-3d70-9afc-03feba337cb3 | -11.2819 | -56.144 | 2024-11-03 01:06:10 | GOES-16 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 6da583f3-ec31-3be4-a4fa-3d1c30addf61 | -14.5968 | -57.1045 | 2024-11-03 01:06:27 | METOP-B | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 17b56238-bed9-36cf-bf74-83d1c6a0335e | -10.8709 | -49.090698 | 2024-11-03 01:06:57 | METOP-B | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c6a619f3-ae98-3004-bc6f-5d9401099e6b | -13.3685 | -61.313301 | 2024-11-03 01:07:01 | METOP-B | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| e7be590e-5949-3ea2-af98-db22e28fb46b | -13.3759 | -61.2994 | 2024-11-03 01:07:01 | METOP-B | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 1c7ef5da-d8bd-33af-81f7-1824554a9396 | -13.3661 | -61.301399 | 2024-11-03 01:07:01 | METOP-B | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 75fa21ae-e2d2-35d3-beb1-0fa48c1c0444 | -22.0726 | -43.0806 | 2024-11-03 01:07:06 | GOES-16 | CHIADOR | MINAS GERAIS | Brasil | 3116209 | 31 | 33 | nan | nan | nan | Mata Atlântica | 79.1 |
| 04f5255b-8c21-338d-b364-780e2b033c62 | -22.0735 | -43.055 | 2024-11-03 01:07:06 | GOES-16 | CHIADOR | MINAS GERAIS | Brasil | 3116209 | 31 | 33 | nan | nan | nan | Mata Atlântica | 71.9 |
| e04e0b76-bb50-3ce1-8920-8f95332e98b9 | -22.0936 | -43.0741 | 2024-11-03 01:07:07 | GOES-16 | TRÊS RIOS | RIO DE JANEIRO | Brasil | 3306008 | 33 | 33 | nan | nan | nan | Mata Atlântica | 80.2 |
| 2fd36267-b793-3cfb-95c0-0b9e41823de1 | -22.0945 | -43.0486 | 2024-11-03 01:07:07 | GOES-16 | TRÊS RIOS | RIO DE JANEIRO | Brasil | 3306008 | 33 | 33 | nan | nan | nan | Mata Atlântica | 71.9 |
| 533c815b-989d-304b-b218-90c5f869fe93 | -11.5046 | -54.841801 | 2024-11-03 01:07:09 | METOP-B | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| fcdf9c7a-fcdd-389f-afd7-0fa76e40fa4f | -11.2805 | -56.137699 | 2024-11-03 01:07:17 | METOP-B | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c34f50a8-c3d3-3104-9667-4e34b4a13f12 | -11.2821 | -56.144699 | 2024-11-03 01:07:17 | METOP-B | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1a52a1f5-fc51-3303-86a0-fd51675779af | -8.7155 | -48.012199 | 2024-11-03 01:07:28 | METOP-B | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 01e6e6f0-f6b0-3a11-9cc7-52f219f91c0b | -8.7013 | -47.996498 | 2024-11-03 01:07:28 | METOP-B | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 540d94db-6635-3986-bd3b-d521ffd9c8f7 | -8.7059 | -48.014599 | 2024-11-03 01:07:28 | METOP-B | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a663e958-3c4d-3f1d-83fd-cf305f272936 | -8.7104 | -48.0327 | 2024-11-03 01:07:28 | METOP-B | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 169a67e6-a744-3a1e-8ef0-5283ef3e1cce | -5.2108 | -47.452702 | 2024-11-03 01:08:22 | METOP-B | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ad1f3d87-b9c3-3997-9aff-7cd74ac0f7f0 | -3.9583 | -48.149899 | 2024-11-03 01:08:45 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9f721a0e-ed00-3ecd-a287-6d1ad614d489 | -3.9358 | -48.353699 | 2024-11-03 01:08:47 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d932ae20-9816-3ab5-a68d-e9fc3e6a6cce | -3.9407 | -48.374199 | 2024-11-03 01:08:47 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c61fe220-9933-36d7-bb11-50bd3fbbed16 | -3.641 | -50.170399 | 2024-11-03 01:08:58 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e5c372a1-894c-35c6-8c88-9ce2e197c117 | -3.6447 | -50.185902 | 2024-11-03 01:08:58 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 49c2e586-e8cf-369e-93ff-3ae84d938abc | -3.336 | -49.055698 | 2024-11-03 01:08:59 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f0aa1d33-c1ee-377f-a60a-852648eccbbd | -3.3404 | -49.074402 | 2024-11-03 01:08:59 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 81eff661-3714-3cf9-8938-e754d8c51e56 | -3.5329 | -50.2771 | 2024-11-03 01:09:01 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1ac3e426-e2a1-30a7-90a9-f78814d72da9 | -3.5365 | -50.2924 | 2024-11-03 01:09:01 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6dec2a02-5b2a-315d-a5e8-19a7693469af | -3.5401 | -50.307598 | 2024-11-03 01:09:01 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f146ddc0-d7d4-3e9b-8a23-4afc592eaeee | -3.4765 | -50.386501 | 2024-11-03 01:09:02 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f2b24b37-4666-3a4a-8711-8a4e10222b80 | -3.4632 | -50.3736 | 2024-11-03 01:09:02 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8a32fc8e-5999-31af-9c9f-0f659026e488 | -3.4668 | -50.388699 | 2024-11-03 01:09:02 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 344942d4-a1c0-3611-8045-80c85c6d0ee4 | -3.4703 | -50.403702 | 2024-11-03 01:09:02 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 64f5e6e7-fc00-3435-b026-70c93e38f445 | -3.4535 | -50.3759 | 2024-11-03 01:09:02 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 71b1c187-448d-37bf-a3a3-4e53b2e0ecfd | -3.4588 | -50.485298 | 2024-11-03 01:09:03 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d8db14db-cc0c-354d-9100-c04d855f04d6 | -3.4028 | -50.291302 | 2024-11-03 01:09:03 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 80ab0aa3-6186-3198-96df-39b50e0211b8 | -3.5371 | -50.8619 | 2024-11-03 01:09:03 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c63dbe36-68fb-3879-8af3-c89ed40cd474 | -3.5404 | -50.875801 | 2024-11-03 01:09:03 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0d9471cf-947a-3366-bdd8-75a279acb356 | -3.5306 | -50.878101 | 2024-11-03 01:09:03 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 09b172b2-a0bf-3c89-b35b-c5d14785929a | -3.2913 | -50.035801 | 2024-11-03 01:09:04 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9d870a8e-49fb-3562-a9e8-c397f4cd50fb | -3.3239 | -50.261002 | 2024-11-03 01:09:04 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 29975fa1-2336-3855-9b5e-062a547071dc | -3.3275 | -50.276402 | 2024-11-03 01:09:04 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 09ce5403-8abf-3a52-9f00-cd9f29e4ef14 | -3.3142 | -50.263302 | 2024-11-03 01:09:04 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 700618b0-4583-39eb-9f79-73519dc005f7 | -3.3178 | -50.278702 | 2024-11-03 01:09:04 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 31cbae90-aab6-3ce9-9a2c-6567a46aa020 | -3.3214 | -50.294102 | 2024-11-03 01:09:04 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| beaffd61-c40a-3884-ae3d-a06cbe4a4b87 | -4.4128 | -55.395199 | 2024-11-03 01:09:06 | METOP-B | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 62393ad7-099d-3fd1-b923-9df4e5809f71 | -3.3749 | -50.958199 | 2024-11-03 01:09:06 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 28d3eed4-2723-3f54-911a-b6089fba6cc4 | -3.2073 | -50.2882 | 2024-11-03 01:09:06 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a410f2c5-cd40-38b3-9263-69bc4f6759f4 | -3.1939 | -50.275002 | 2024-11-03 01:09:06 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8ab37f84-800b-34ed-9dbd-1f7bb4b2e538 | -3.1975 | -50.290501 | 2024-11-03 01:09:06 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0fd62dd9-8ca1-33c2-9a30-05e78b04e4c5 | -4.5363 | -56.118 | 2024-11-03 01:09:06 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 41eb0528-094a-3553-a136-1aff58064c22 | -4.5379 | -56.125099 | 2024-11-03 01:09:06 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 961b1d6d-4bc2-30ba-beba-a470d37debda | -4.2594 | -55.175098 | 2024-11-03 01:09:07 | METOP-B | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a750828c-92bb-3c0b-9761-701ceefa6105 | -3.1739 | -50.583 | 2024-11-03 01:09:08 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2dc9731d-5a66-3a67-9d60-e78094b7db8c | -2.8926 | -49.430901 | 2024-11-03 01:09:08 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4ee52f51-de17-37ee-b433-3191154d4f22 | -2.8178 | -49.1577 | 2024-11-03 01:09:08 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fbb7bfb5-e06e-3a17-8b17-e4014309c902 | -2.6531 | -48.504398 | 2024-11-03 01:09:08 | METOP-B | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8b8ed98c-05f4-34f0-94c3-dd91c08da1b8 | -2.8081 | -49.16 | 2024-11-03 01:09:08 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7227a316-90cd-3db2-ab21-4bef59018a8e | -4.2998 | -55.577301 | 2024-11-03 01:09:08 | METOP-B | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6a6493b0-ac7c-3297-babb-c94db3f74c73 | -2.8719 | -49.473598 | 2024-11-03 01:09:08 | METOP-B | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aa900602-e444-3541-8fd3-8bca61011f52 | -2.6389 | -48.573898 | 2024-11-03 01:09:09 | METOP-B | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 855e88a9-1976-3ca3-8087-29f2b527be5a | -4.2518 | -55.502399 | 2024-11-03 01:09:09 | METOP-B | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 045251be-8899-3f37-97a5-69954f0b4776 | -4.2535 | -55.5098 | 2024-11-03 01:09:09 | METOP-B | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d5a818fb-4749-3c7f-9365-ed260dbedc65 | -2.6243 | -48.555302 | 2024-11-03 01:09:09 | METOP-B | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4f9dff2c-d7c7-3f30-a537-7190592daebe | -2.6292 | -48.576199 | 2024-11-03 01:09:09 | METOP-B | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d3ea93be-9185-364a-b8a3-9e20d8c9b310 | -2.6341 | -48.596901 | 2024-11-03 01:09:09 | METOP-B | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2e89ee1b-b7cc-3bd0-b6a2-f015ba79853a | -2.6196 | -48.5784 | 2024-11-03 01:09:09 | METOP-B | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a2899643-bb54-3bd1-b08f-558b51288706 | -3.0522 | -50.501301 | 2024-11-03 01:09:09 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9833bfe1-3fbf-3189-a078-0b98a2b0b5ee | -4.0176 | -54.794201 | 2024-11-03 01:09:10 | METOP-B | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3cfe3cfb-da37-3f70-939c-931aec3da711 | -4.0194 | -54.802101 | 2024-11-03 01:09:10 | METOP-B | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 20746ab8-4ffd-36c4-aa20-cff3cb8a6baa | -4.1788 | -55.5891 | 2024-11-03 01:09:10 | METOP-B | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 01b9cd08-c12a-3d32-8983-fb44fcdc8937 | -4.1805 | -55.5965 | 2024-11-03 01:09:10 | METOP-B | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 13cca630-ab86-3df0-8939-7d7a37384d3e | -4.2406 | -55.8601 | 2024-11-03 01:09:10 | METOP-B | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 30e4181e-eb96-360d-a757-82246ed26b55 | -4.2422 | -55.867298 | 2024-11-03 01:09:10 | METOP-B | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README10.md)
