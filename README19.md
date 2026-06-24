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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d1b38f09-14d7-3651-8334-342257db0a78 | -10.38747 | -56.72474 | 2026-06-24 05:27:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 65d0a603-c0e8-3461-90a5-c8c92eccbcc7 | -10.3835 | -56.72425 | 2026-06-24 05:27:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5ffebd8c-22df-33f1-8e27-4a4891ced754 | -13.77846 | -53.07584 | 2026-06-24 05:27:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f050a689-9aae-3944-8482-0c1fd292bd1a | -11.281 | -55.79393 | 2026-06-24 05:27:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b656e6f8-b219-3011-aa2b-b1fd80bd862c | -10.3922 | -56.72008 | 2026-06-24 05:27:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 05f281ea-b826-3d2b-839e-1855e19e09ea | -9.18487 | -58.0641 | 2026-06-24 05:27:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5399a180-81d0-3b47-b6cc-06b405a44634 | -10.16168 | -56.62397 | 2026-06-24 05:27:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7bac6017-1269-3d94-ae2a-a5e222f67dea | -9.21109 | -47.92807 | 2026-06-24 05:27:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e8ec2d7b-a3bf-318f-adc1-a9f1358e4c01 | -13.06633 | -53.35225 | 2026-06-24 05:27:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7b3b7234-2ea3-34b7-ba77-7f3d1588292f | -13.06116 | -53.35155 | 2026-06-24 05:27:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 03c9a68f-e081-39f3-919a-02e0cb1fa879 | -10.76905 | -54.10654 | 2026-06-24 05:27:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e225ee54-1744-3a41-b44c-532c37364a01 | -13.77198 | -53.07165 | 2026-06-24 05:27:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 15c9bb7a-133c-3dc9-a1cf-0dc4bf5c1df8 | -8.687 | -47.85372 | 2026-06-24 05:27:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 82d49b41-d5df-335a-935a-a13401e1ee4e | -11.28013 | -55.79151 | 2026-06-24 05:27:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8303f533-a143-39e9-9809-4b9a91b4c61a | -7.92588 | -48.2903 | 2026-06-24 05:27:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| c3ca9963-3410-3711-ac7e-9cc3855f318c | -9.36767 | -50.54354 | 2026-06-24 05:27:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| bdbd405e-f16e-3aff-b967-e5e39b34d86d | -13.77314 | -53.0752 | 2026-06-24 05:27:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fb97fae8-3fc9-3a46-b0c4-390326087eb7 | -14.54034 | -49.1058 | 2026-06-24 05:27:00 | NOAA-20 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 54fce1a9-86ea-33c1-8555-4cdd13fe3737 | -9.18189 | -58.05933 | 2026-06-24 05:27:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 2e267266-4543-34cc-b404-d38dc39a16ac | -12.8552 | -44.3389 | 2026-06-24 05:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 116.0 |
| 19909783-0c96-3339-a536-3d4e2201df10 | -12.8354 | -44.3657 | 2026-06-24 05:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 320.5 |
| 39e73cd9-802c-3ed3-a810-0aefd28f15c4 | -12.8548 | -44.3625 | 2026-06-24 05:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 209.4 |
| 29c578f8-7e3e-3a90-922f-a05e28707bea | -13.0635 | -53.3546 | 2026-06-24 05:30:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 41.3 |
| df80b331-f9b2-35b6-b384-08b6705bb151 | -12.8349 | -44.3892 | 2026-06-24 05:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 44.8 |
| b4b840a7-9612-3abf-978e-6c801b696b69 | -12.8359 | -44.3422 | 2026-06-24 05:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 186.0 |
| b284d56d-624e-3e78-9593-4c3185591b44 | -12.8552 | -44.3389 | 2026-06-24 05:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 109.7 |
| 289f07ab-2c3a-373c-8bcc-bdfa9b01a9f9 | -12.8548 | -44.3625 | 2026-06-24 05:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 244.0 |
| 0249e044-dc7c-3190-82a2-820b634ac03e | -12.8354 | -44.3657 | 2026-06-24 05:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 304.3 |
| 79971ac9-325e-3411-96a6-1f57af2733b3 | -12.8359 | -44.3422 | 2026-06-24 05:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 151.9 |
| 9c91f0bf-d063-3b63-aff2-b9d0739cee0c | -12.8359 | -44.3422 | 2026-06-24 05:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 147.8 |
| d11e3a7c-4266-3249-9cfb-c1aa12c98059 | -12.8552 | -44.3389 | 2026-06-24 05:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 92.3 |
| 6d3218ef-1a41-3d09-8846-6f4c9557335e | -12.8548 | -44.3625 | 2026-06-24 05:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 244.0 |
| f5d48b32-3247-3238-92b3-adfdd42c357c | -12.8354 | -44.3657 | 2026-06-24 05:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 344.7 |
| 18d66f38-67e1-39d7-935c-914d7e570eee | -12.8354 | -44.3657 | 2026-06-24 06:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 280.0 |
| c149aef0-52ed-37b6-8001-53ecb18362c1 | -12.8548 | -44.3625 | 2026-06-24 06:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 221.8 |
| 89d9bbb7-c01a-37d1-9a59-12239b273c59 | -12.8552 | -44.3389 | 2026-06-24 06:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 112.8 |
| e9a8ffd1-166b-3937-838e-b8bc41aa295f | -12.8359 | -44.3422 | 2026-06-24 06:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 157.3 |
| 38602037-3105-3517-bfbc-94dab5857596 | -12.8359 | -44.3422 | 2026-06-24 06:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 163.9 |
| 988791e6-ea80-34ca-ae95-41f523173124 | -12.8548 | -44.3625 | 2026-06-24 06:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 254.9 |
| 7ed0c1d5-a4f4-3397-ac9f-b6cc716e70a6 | -12.8552 | -44.3389 | 2026-06-24 06:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 122.8 |
| 31d1d2f9-7d2e-3b2f-bbe2-0eb8bb1101f9 | -12.8354 | -44.3657 | 2026-06-24 06:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 285.7 |
| 6f091613-9ba6-3bba-b61f-010a92222b10 | -10.27963 | -60.54175 | 2026-06-24 06:14:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| c8a63b6e-86e4-324b-863b-ce7613473c7e | -10.27847 | -60.54634 | 2026-06-24 06:14:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 9a7151e2-95b1-3158-9c4d-87c654defe4b | -10.27921 | -60.53956 | 2026-06-24 06:14:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 912822f1-4cdd-38d6-bd33-16359a781e30 | -7.91345 | -48.28049 | 2026-06-24 06:18:00 | AQUA_M-M | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 43185410-7593-3363-bea2-0a3c1ecf4186 | -8.8533 | -46.94673 | 2026-06-24 06:18:00 | AQUA_M-M | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 58cec1ef-42a2-3546-baeb-87a8a38bdfe1 | -3.95953 | -43.11368 | 2026-06-24 06:18:00 | AQUA_M-M | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 19.0 |
| 2d50e763-cc49-3188-a50e-6485a6225529 | -8.61352 | -45.9938 | 2026-06-24 06:18:00 | AQUA_M-M | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| a1cb49e9-a4e8-3641-9cf5-beb676e8f15e | -3.95821 | -43.1224 | 2026-06-24 06:18:00 | AQUA_M-M | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| c7b40828-28d3-36df-b24a-207f5d7c289b | -8.60273 | -46.00238 | 2026-06-24 06:18:00 | AQUA_M-M | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| ed50595f-6499-3525-99c0-8e5dbd1b21dd | -7.91664 | -48.28682 | 2026-06-24 06:18:00 | AQUA_M-M | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 20.5 |
| 8df0580a-a677-35f3-92a3-5b386701e361 | -8.60429 | -45.99244 | 2026-06-24 06:18:00 | AQUA_M-M | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 24.5 |
| d8d2364b-70e2-34f4-99f9-7d98c6e83bf9 | -12.8354 | -44.3657 | 2026-06-24 06:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 291.9 |
| acae422a-fb28-3549-80d3-38980015e1cc | -12.8548 | -44.3625 | 2026-06-24 06:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 217.3 |
| 4b10ec6d-5576-3ce2-8cbf-e3f06d17ab9d | -12.8552 | -44.3389 | 2026-06-24 06:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 113.5 |
| 09575f9b-c97d-3fcd-8af5-3c98b2d89e8e | -12.8359 | -44.3422 | 2026-06-24 06:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 176.9 |
| 5662da6a-39cc-3427-a8ac-8bbf4b57d7c9 | -12.84931 | -44.36653 | 2026-06-24 06:20:00 | AQUA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 55.9 |
| df77c6a3-cfd4-381d-8410-33b80a09f018 | -11.4856 | -46.73926 | 2026-06-24 06:20:00 | AQUA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 2220f524-f101-3da6-afba-3c26820a86df | -12.83172 | -44.36384 | 2026-06-24 06:20:00 | AQUA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 173.5 |
| 439f0e5e-63f7-3cde-8bfd-c62026e35637 | -12.77218 | -44.44076 | 2026-06-24 06:20:00 | AQUA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 00c5276e-44d0-3e7d-978e-23f5d65fe0c0 | -12.83918 | -44.37418 | 2026-06-24 06:20:00 | AQUA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 15.0 |
| b76f2764-6282-3952-affc-b477218ac0f4 | -11.29666 | -43.31413 | 2026-06-24 06:20:00 | AQUA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 5dc4ed67-4436-3937-a76b-703d11ab32a4 | -9.21473 | -45.34143 | 2026-06-24 06:20:00 | AQUA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 4ea2421b-213d-3fe4-99b4-9744fadef9b1 | -12.85065 | -44.35753 | 2026-06-24 06:20:00 | AQUA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 49.7 |
| fa229b83-76f3-3d06-823c-ef5f512953a8 | -12.84052 | -44.36519 | 2026-06-24 06:20:00 | AQUA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 250.5 |
| 215138df-ea75-32ac-b4bf-d69c9956abb0 | -11.30428 | -43.32452 | 2026-06-24 06:20:00 | AQUA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 8.4 |
| 2199e980-3ac9-3833-b753-42740e2ac3fd | -12.8432 | -44.3472 | 2026-06-24 06:20:00 | AQUA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 7bfd4e85-a7a5-3685-b162-fd2f1f9fe3df | -12.78319 | -44.44832 | 2026-06-24 06:20:00 | AQUA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 0978fd9c-1056-336a-b509-112d5196e2ff | -12.83306 | -44.35485 | 2026-06-24 06:20:00 | AQUA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 155.2 |
| 670bb2ba-f8e2-3db3-8e76-9ae5968b6567 | -12.84186 | -44.35619 | 2026-06-24 06:20:00 | AQUA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 231.4 |
| 685659bf-127b-3cca-bccc-b3e91ad99335 | -12.78453 | -44.43935 | 2026-06-24 06:20:00 | AQUA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 10.8 |
| f09512ed-848d-310b-9447-350669104f42 | -11.30561 | -43.3154 | 2026-06-24 06:20:00 | AQUA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 10.5 |
| f89e64f2-4ec9-3df1-8098-67da8d49bd41 | -11.29533 | -43.32323 | 2026-06-24 06:20:00 | AQUA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 6.7 |
| b905cacc-ea80-3894-91dd-84ce98aadb86 | -15.75591 | -43.21974 | 2026-06-24 06:22:00 | AQUA_M-M | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | 7.4 |
| f9fd0289-a448-3c3e-8ec0-2c2e67d534da | -15.75445 | -43.23025 | 2026-06-24 06:22:00 | AQUA_M-M | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | 16.6 |
| 8ba40a72-d98a-3bcd-8d73-09924bc52c1c | -12.8548 | -44.3625 | 2026-06-24 06:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 217.9 |
| fb11725f-78ce-3a72-b09b-e32d2024363d | -12.8552 | -44.3389 | 2026-06-24 06:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 90.5 |
| 1a5f90ac-257e-3718-b9b6-58dbe76146d8 | -12.8359 | -44.3422 | 2026-06-24 06:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 144.5 |
| 0a8cd728-471d-33a6-ad11-780832cf73ad | -12.8354 | -44.3657 | 2026-06-24 06:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 322.2 |
| 2f8de29f-b440-3a62-b0ef-5ed953fbcce8 | -12.8548 | -44.3625 | 2026-06-24 06:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 218.9 |
| 75e0bc97-9631-3a27-af9c-c170617a79f7 | -12.8354 | -44.3657 | 2026-06-24 06:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 254.4 |
| 9aaf7189-94a5-3696-ac1b-58ef753078e0 | -12.8359 | -44.3422 | 2026-06-24 06:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 156.8 |
| 8edc6ca3-606d-38a1-b1a9-524c5ed74b7c | -12.8552 | -44.3389 | 2026-06-24 06:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 111.8 |
| 7b71ccdb-c09b-3235-a4e9-6d5e9bcbeb47 | -12.8548 | -44.3625 | 2026-06-24 06:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 198.3 |
| 5bb75e23-bfe3-3fc4-9046-3352f95e51ae | -12.8552 | -44.3389 | 2026-06-24 06:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 111.9 |
| d29a177c-5dac-3236-9c6c-edd3a9079d30 | -12.8354 | -44.3657 | 2026-06-24 06:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 208.6 |
| ea44e95d-170d-3678-acdc-ae1b9da9ced7 | -12.8359 | -44.3422 | 2026-06-24 06:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 132.8 |
| 9a24dcfa-af54-3484-bcb5-90e7392165d0 | -12.8552 | -44.3389 | 2026-06-24 07:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 88.1 |
| 4ed53794-412f-30d3-bad3-81dc7b39d137 | -12.8548 | -44.3625 | 2026-06-24 07:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 194.9 |
| 8991b63c-7e39-3a2e-b232-d2ccdf9baed7 | -12.8359 | -44.3422 | 2026-06-24 07:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 107.8 |
| 55d44d46-1d73-3ef1-ad8a-94d438b8e2d4 | -12.8354 | -44.3657 | 2026-06-24 07:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 213.1 |
| cd361ca4-5fdc-3603-9b0a-3e0a6c9f6116 | -12.8359 | -44.3422 | 2026-06-24 07:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 131.3 |
| 43a8659f-222b-3810-bb89-df4090c0ec73 | -12.8552 | -44.3389 | 2026-06-24 07:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 101.3 |
| 5f64076b-674e-3ddc-9312-958b26dd49e7 | -12.8548 | -44.3625 | 2026-06-24 07:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 181.8 |
| 4d1daa6a-bb2f-39cf-89b4-439bf1ac867a | -12.8354 | -44.3657 | 2026-06-24 07:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 190.9 |
| 88385416-e863-3771-9cd0-ccacec6b410c | -12.8552 | -44.3389 | 2026-06-24 07:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 87.0 |
| cb991b04-df6e-329c-be89-637ce1b3fcde | -12.8548 | -44.3625 | 2026-06-24 07:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 190.0 |
| 12a8c88e-a53c-3b3d-bd41-c514afc682ca | -12.8354 | -44.3657 | 2026-06-24 07:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 215.5 |
| 50fc225b-40f2-3e10-9a49-76b74cb95ce4 | -12.8359 | -44.3422 | 2026-06-24 07:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 102.5 |
| 3a13d418-b57c-30be-873c-d6bea204eb4e | -12.8548 | -44.3625 | 2026-06-24 07:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 178.8 |


[Clique aqui para ver as próximas entradas](README20.md)
