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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 735033f3-75e8-34cc-ad82-02bed3c709a8 | -11.44333 | -45.10807 | 2025-07-06 03:40:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 5396a986-5404-392f-9d4f-5dcf67c439db | -11.45393 | -45.11443 | 2025-07-06 03:40:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d85eff60-330c-393e-920d-c37aa2584559 | -19.71824 | -40.35301 | 2025-07-06 03:40:00 | NPP-375D | JOÃO NEIVA | ESPÍRITO SANTO | Brasil | 3203130 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 4ed23492-c1dd-3467-92f9-6287b977d2b8 | -10.87726 | -47.18167 | 2025-07-06 03:40:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a7db082e-c634-3a39-8394-5dede5da80f1 | -11.44411 | -45.10408 | 2025-07-06 03:40:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 8.8 |
| f876e9da-7035-39f1-8a27-9c976757eeed | -10.87371 | -47.18966 | 2025-07-06 03:40:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 55bad39e-8ef3-392f-83d9-4d1cad0e339d | -11.45135 | -45.09728 | 2025-07-06 03:40:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 1d59e435-cf60-3868-a3dc-5386a986d292 | -16.42842 | -42.18164 | 2025-07-06 03:40:00 | NPP-375D | RUBELITA | MINAS GERAIS | Brasil | 3156502 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 9c215d4a-599f-39a7-8c02-59591f5f0b53 | -10.86966 | -47.18578 | 2025-07-06 03:40:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3ad40603-76b1-312d-8d32-b2c646a3fcfc | -17.09572 | -43.80333 | 2025-07-06 03:40:00 | NPP-375D | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7d516644-72da-3312-9b3e-f7032cbd6577 | -18.04118 | -39.92625 | 2025-07-06 03:40:00 | NPP-375D | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 9f5a4570-2454-392e-974a-076298613bf5 | -11.45626 | -45.10244 | 2025-07-06 03:40:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| dd07c6b5-2362-3fce-917a-f1248028f923 | -10.86829 | -47.18294 | 2025-07-06 03:40:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 838c1fb0-b238-3d0c-a962-b5bb5dc4bf54 | -16.43268 | -42.18273 | 2025-07-06 03:40:00 | NPP-375D | RUBELITA | MINAS GERAIS | Brasil | 3156502 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 752e2db5-00bd-367f-bc70-f58c4e4ed40a | -11.44255 | -45.11207 | 2025-07-06 03:40:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8164abb3-9c78-39fe-814c-5b8c26835484 | -11.45548 | -45.10643 | 2025-07-06 03:40:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 0a2f3ba9-6def-39d1-9195-7ee42d2d366f | -11.45471 | -45.11042 | 2025-07-06 03:40:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 10.7 |
| d2084206-be70-31e5-93c1-3a85be61fcee | -11.44902 | -45.10924 | 2025-07-06 03:40:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 59ba623f-1bd6-399a-9144-6edabeb05744 | -11.44824 | -45.11324 | 2025-07-06 03:40:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5204e2a9-6f23-3631-a628-f86d7858ce60 | -11.45703 | -45.09849 | 2025-07-06 03:40:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| b3488758-8899-3655-a047-78d51625ffac | -17.77894 | -42.80936 | 2025-07-06 03:40:00 | NPP-375D | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 23af379a-865d-32a3-b6a3-41837b41ed2b | -20.34966 | -40.36011 | 2025-07-06 03:42:00 | NPP-375D | CARIACICA | ESPÍRITO SANTO | Brasil | 3201308 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 6deb2a8b-eed4-3872-8e7d-81d201eb1864 | -23.98154 | -48.91791 | 2025-07-06 03:42:00 | NPP-375D | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c9e3baa0-0556-3a0d-a21a-417bada976d4 | -21.18011 | -43.98229 | 2025-07-06 03:42:00 | NPP-375D | BARROSO | MINAS GERAIS | Brasil | 3105905 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 9e4507b5-e6c3-3bdf-839c-26d42471eb0b | -22.67556 | -42.85578 | 2025-07-06 03:42:00 | NPP-375D | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| c1fb473b-a36a-37e2-b15b-971fe8c55868 | -21.32503 | -44.24295 | 2025-07-06 03:42:00 | NPP-375D | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 22.3 |
| 3de26f06-d00f-37d8-a58d-eb3abac9f663 | -22.54191 | -48.81411 | 2025-07-06 03:42:00 | NPP-375D | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ae3adc4b-dfba-334d-aa56-bf96a09d1115 | -21.32691 | -44.24034 | 2025-07-06 03:42:00 | NPP-375D | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 14.6 |
| 5d841256-e4b7-3c29-8638-443123360093 | -22.67543 | -42.85535 | 2025-07-06 03:42:00 | NPP-375D | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 79febfaa-83f1-3e66-a2af-01873ecfd1cd | -22.85643 | -42.98207 | 2025-07-06 03:42:00 | NPP-375D | SÃO GONÇALO | RIO DE JANEIRO | Brasil | 3304904 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 378d349d-1030-323f-835e-dade38785101 | -21.28283 | -46.17439 | 2025-07-06 03:42:00 | NPP-375D | ALTEROSA | MINAS GERAIS | Brasil | 3102001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| cb8addc2-7aca-3b2b-90c2-5e21074a7f4c | -21.28215 | -46.17756 | 2025-07-06 03:42:00 | NPP-375D | AREADO | MINAS GERAIS | Brasil | 3104304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 0640b7a2-a7a5-375a-bca9-9245f4668b45 | -21.32593 | -44.24512 | 2025-07-06 03:42:00 | NPP-375D | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.0 |
| 06f81a05-74ff-3c65-b532-1e5b384c129a | -20.17802 | -43.71478 | 2025-07-06 03:42:00 | NPP-375D | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 0efab648-76ce-3160-b3b2-be47b3d94128 | -22.90297 | -43.7546 | 2025-07-06 03:42:00 | NPP-375D | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 8800dc96-e6e9-3cb1-9d02-ef2f6fde9f76 | -19.4576 | -45.306 | 2025-07-06 03:42:00 | NPP-375D | MARTINHO CAMPOS | MINAS GERAIS | Brasil | 3140506 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3e0bed03-db18-33e9-ab38-ccc4848ac356 | -23.98717 | -48.91939 | 2025-07-06 03:42:00 | NPP-375D | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 59173ced-280f-316b-8247-11aa210f7141 | -20.76348 | -46.77073 | 2025-07-06 03:42:00 | NPP-375D | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 4b407abe-f5bb-323e-ad4c-07cccbef71a8 | -11.4584 | -45.1126 | 2025-07-06 03:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 44.1 |
| 57f63573-d2d7-3c52-baad-925016e000e9 | -12.0266 | -57.0845 | 2025-07-06 03:50:00 | GOES-19 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 60.2 |
| c9104cab-6be9-3f80-ac0e-bcbddde19090 | -2.87573 | -40.30042 | 2025-07-06 03:57:00 | NOAA-20 | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 6.1 |
| e9e65f5a-a8ce-388d-83d8-681a87683a4f | -12.0266 | -57.0845 | 2025-07-06 04:00:00 | GOES-19 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 63.0 |
| e893f5ce-5f64-3739-a386-af9754333828 | -11.4588 | -45.0895 | 2025-07-06 04:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 59.8 |
| ab42aa5b-beef-3261-a76e-d387b7e10d87 | -11.4397 | -45.0923 | 2025-07-06 04:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 47.1 |
| 42d1d191-b8b3-330a-a66b-76fe9ed36370 | -5.68475 | -41.40144 | 2025-07-06 04:00:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 74bc2fb2-dde7-382a-a6b2-7cc64eafaf23 | -7.20073 | -43.12548 | 2025-07-06 04:00:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 7a61712b-2406-3501-a24a-c059b7a84f94 | -7.25552 | -44.21709 | 2025-07-06 04:00:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a7e52eb7-a93a-3bf0-ba45-19a7360cf236 | -7.20006 | -43.12953 | 2025-07-06 04:00:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 57afee36-97a0-34b3-9ea5-26f407949b25 | -7.0831 | -44.38783 | 2025-07-06 04:00:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 6ee6bcb1-ff5e-3785-beef-5d8877f0020b | -8.026 | -45.83378 | 2025-07-06 04:00:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e3ed09b5-ca9e-313b-880c-7fe446ccd40b | -3.50327 | -43.24918 | 2025-07-06 04:00:00 | NOAA-20 | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 905b0725-dfd9-399c-9c8f-6ba3621002de | -6.16317 | -43.75714 | 2025-07-06 04:00:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 72e76753-cf46-35bf-932f-648354e52103 | -3.97747 | -48.41383 | 2025-07-06 04:00:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7f209202-581c-36e7-87c8-1543155bd6f5 | -7.70298 | -47.2881 | 2025-07-06 04:00:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 984ad3df-1aec-375f-b471-b05f1c588750 | -5.98834 | -46.76669 | 2025-07-06 04:00:00 | NOAA-20 | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d944e4ff-f8a5-313c-9a73-b3db98f938bd | -6.95128 | -42.70308 | 2025-07-06 04:00:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 915cec97-33a2-321a-9781-834d6e887cbf | -7.18938 | -43.1278 | 2025-07-06 04:00:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 17cb3aa4-ddbe-3c31-9120-915363bdb6a0 | -6.33615 | -43.7485 | 2025-07-06 04:00:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| f9cdfe5e-ebca-3e60-9d60-d1e0efab93d0 | -6.16243 | -43.76165 | 2025-07-06 04:00:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 096ed268-b581-3210-b571-5765daf6ba01 | -5.56773 | -45.21557 | 2025-07-06 04:00:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d699b070-06ed-3fe9-93a7-0dc44bee8fc9 | -5.60259 | -45.18354 | 2025-07-06 04:00:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 945f712a-c2e6-3595-a34f-7922ce223394 | -7.14282 | -44.31152 | 2025-07-06 04:00:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 06632e4b-e0d0-3245-8a65-f3f48449f96f | -5.06995 | -43.72855 | 2025-07-06 04:00:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f4f4dd3d-2eb7-3c32-91f4-bf76dde80502 | -4.00498 | -43.23483 | 2025-07-06 04:00:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b3832e4f-decc-366c-a56c-e05b8fbbfae6 | -5.56835 | -45.21189 | 2025-07-06 04:00:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 16.0 |
| dfbf4f24-cff7-330d-8f96-370a4074d26a | -8.0321 | -45.8325 | 2025-07-06 04:00:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3ae0ed28-9d05-3db7-9350-a6cdc7b59caa | -6.83732 | -43.30542 | 2025-07-06 04:00:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 8cc7fdbd-e882-33cf-8d8e-8f54e4e9a846 | -7.14203 | -44.31627 | 2025-07-06 04:00:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6c8b58cf-7fc9-3b6c-88ed-3622bb62aa2d | -6.39179 | -42.79815 | 2025-07-06 04:00:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 65f37e20-2a44-32d8-8a20-5efd8bca5298 | -5.60669 | -45.18425 | 2025-07-06 04:00:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d6132ffb-55b9-3092-8d6d-6abf0511f242 | -6.39533 | -42.79872 | 2025-07-06 04:00:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| b6b8d847-70f7-3bfb-adbd-f3a60265c9c7 | -5.06618 | -43.72796 | 2025-07-06 04:00:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 7b787b93-43a6-3947-a791-4733bea30511 | -7.0886 | -43.21286 | 2025-07-06 04:00:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| a8d5fb46-1c1d-3add-80c6-b4981e94bd3b | -6.83012 | -43.30424 | 2025-07-06 04:00:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| d2a6e8c1-5302-3aa7-b55d-e616d58e74b4 | -5.59971 | -45.17551 | 2025-07-06 04:00:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1d1a39f2-32b4-3e5f-a522-d22b655ce50a | -6.15945 | -43.75653 | 2025-07-06 04:00:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1398f617-8c8f-3c27-8a66-6e65107584d9 | -7.20294 | -43.13419 | 2025-07-06 04:00:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| b76d88b7-7876-3732-bc36-f1e64a79bf7c | -7.19717 | -43.12489 | 2025-07-06 04:00:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 8b29214a-c0d6-32d2-abd2-ffa77997e9b7 | -7.28251 | -44.68146 | 2025-07-06 04:00:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d218ddb3-325f-396d-b979-8ee935b47802 | -3.30359 | -42.65415 | 2025-07-06 04:00:00 | NOAA-20 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b5ad7078-20fc-3e2a-8b5f-253da351446f | -3.52612 | -48.43896 | 2025-07-06 04:00:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4c4af779-e4e6-3b85-9e2b-96a60a87f63a | -5.6073 | -45.18057 | 2025-07-06 04:00:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5b796ff4-ced9-34dd-a68d-a70877377eb1 | -5.59788 | -45.18655 | 2025-07-06 04:00:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 410b79de-09ee-38c9-8014-06e23b6286c0 | -6.9295 | -45.76088 | 2025-07-06 04:00:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 91560617-8a4c-3b17-b1e9-ee9edb7c31e2 | -3.809 | -42.54427 | 2025-07-06 04:00:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 86dd02fd-a9c2-37f0-890a-2ed16965acb9 | -7.19582 | -43.13302 | 2025-07-06 04:00:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| b0149736-b321-3632-a2b1-9fe83131ce62 | -3.49932 | -42.33126 | 2025-07-06 04:00:00 | NOAA-20 | LUZILÂNDIA | PIAUÍ | Brasil | 2205805 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| aa45b8d3-7fa1-3d07-be9a-40a4a5ffaed3 | -7.00715 | -43.54704 | 2025-07-06 04:00:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0452bfe3-f101-3304-a13c-4be29dc4be48 | -7.11569 | -44.14962 | 2025-07-06 04:00:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 60c5738a-4234-395d-aa69-37def78e06df | -4.80659 | -43.22836 | 2025-07-06 04:00:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e30f409e-2989-308e-8178-e36742234276 | -4.12731 | -40.57224 | 2025-07-06 04:00:00 | NOAA-20 | RERIUTABA | CEARÁ | Brasil | 2311702 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 6a09669f-89a3-3100-b22e-1949a91f0ea9 | -6.35834 | -43.24976 | 2025-07-06 04:00:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ddde7212-df42-3473-baea-bd29ecdee77a | -7.96766 | -47.22834 | 2025-07-06 04:00:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 66a8484e-4319-3b36-aec9-e27d051a95fc | -6.67929 | -43.14629 | 2025-07-06 04:00:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 36246a99-f083-3522-8d3d-38822580ab56 | -7.0823 | -44.39252 | 2025-07-06 04:00:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| dffc111a-29ce-3a3e-b591-ec0b2b9b7c0f | -8.22603 | -41.08487 | 2025-07-06 04:00:00 | NOAA-20 | ACAUÃ | PIAUÍ | Brasil | 2200053 | 22 | 33 | nan | nan | nan | Caatinga | 0.3 |
| f5a64465-6e3c-3915-b2a3-00edc501a0db | -3.48237 | -48.44843 | 2025-07-06 04:00:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 094fe094-f422-313f-9d54-e46cc64e1b18 | -3.30722 | -42.65475 | 2025-07-06 04:00:00 | NOAA-20 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f59c9688-98be-386f-88f7-a4726386b1e2 | -6.68577 | -43.15164 | 2025-07-06 04:00:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 28160379-4005-3cc5-9e2e-9570d9f6adaa | -3.504 | -43.24468 | 2025-07-06 04:00:00 | NOAA-20 | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |


[Clique aqui para ver as próximas entradas](README4.md)
