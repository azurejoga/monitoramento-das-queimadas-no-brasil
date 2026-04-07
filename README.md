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
| 12491cd7-5d9c-3e62-8017-d2ec45ce0375 | -18.4921 | -55.505 | 2026-04-07 00:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 92.4 |
| 07eae0d6-f399-3b97-bfe9-28a6ded7e5bb | -5.529 | -35.5218 | 2026-04-07 00:10:00 | GOES-19 | TAIPU | RIO GRANDE DO NORTE | Brasil | 2413904 | 24 | 33 | nan | nan | nan | Caatinga | 125.8 |
| 674244f9-2d65-3b37-8d84-2fea23a9256e | -18.4921 | -55.505 | 2026-04-07 00:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 90.6 |
| 78f42a70-d2ad-3e8e-b8fc-24f2796b7d16 | -18.4921 | -55.505 | 2026-04-07 00:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 83.5 |
| e680d38b-2d57-34e6-9782-66fbcdfe1259 | -25.331301 | -49.422798 | 2026-04-07 00:24:00 | METOP-B | CAMPO MAGRO | PARANÁ | Brasil | 4104253 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 5f3402b7-88d0-3498-a923-793f4e65c3cf | -25.3281 | -49.407101 | 2026-04-07 00:24:00 | METOP-B | CAMPO MAGRO | PARANÁ | Brasil | 4104253 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 58743ab6-dcb4-3162-b6db-c8a83829dc85 | -25.3297 | -49.415001 | 2026-04-07 00:24:00 | METOP-B | CAMPO MAGRO | PARANÁ | Brasil | 4104253 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 8316156f-372a-34d6-a53a-a64db8aee4ca | -18.4921 | -55.505 | 2026-04-07 00:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 84.8 |
| a4849696-a2b6-3590-8867-a290cb0ecbbf | -18.4921 | -55.505 | 2026-04-07 00:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 85.2 |
| a7089be7-2cb0-3bc3-af14-39b5ce3a71b3 | -25.327999 | -49.419998 | 2026-04-07 00:57:00 | METOP-C | CAMPO MAGRO | PARANÁ | Brasil | 4104253 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| bc42da03-b61b-3946-a160-35be2b71492a | -25.329599 | -49.4277 | 2026-04-07 00:57:00 | METOP-C | CAMPO MAGRO | PARANÁ | Brasil | 4104253 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 53fabb3c-b37d-3d17-b211-f43ce837e5a3 | -18.4921 | -55.505 | 2026-04-07 01:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 82.6 |
| 22c4fb36-b9fe-39b5-94b9-e5e5293b4675 | -18.4921 | -55.505 | 2026-04-07 01:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 82.6 |
| ea339bcc-43fa-3a5b-b93e-7f0a15387d13 | -18.49594 | -55.52186 | 2026-04-07 01:17:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 35.2 |
| 1722bc85-115f-3ed6-8c6f-e1cf7c7cbf64 | -18.50883 | -55.51926 | 2026-04-07 01:17:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 18.6 |
| 8b3e3a9f-1d27-3240-8438-ec9c2127efab | -18.49219 | -55.50063 | 2026-04-07 01:17:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 44.6 |
| 186714d4-7d9d-3b5c-af32-ca007258e143 | -18.4921 | -55.505 | 2026-04-07 01:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 81.1 |
| 9eee0f8f-09ec-309e-bd68-25633fa27446 | -12.82158 | -38.40664 | 2026-04-07 03:08:00 | NOAA-20 | SIMÕES FILHO | BAHIA | Brasil | 2930709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| ee2286dd-6149-369f-af32-cd2bf1651909 | -19.59585 | -40.07652 | 2026-04-07 03:10:00 | NOAA-20 | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 2adfff3f-5e8a-3ea9-84ce-eeff3635b4e7 | -19.59487 | -40.08091 | 2026-04-07 03:10:00 | NOAA-20 | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| e1a38a08-0239-3343-9656-e0d0595ee326 | -5.90509 | -37.44947 | 2026-04-07 03:55:00 | NOAA-21 | JANDUÍS | RIO GRANDE DO NORTE | Brasil | 2405207 | 24 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 11d38080-87de-3b1b-bc49-4a230789b931 | -10.1926 | -36.95903 | 2026-04-07 03:55:00 | NOAA-21 | CANHOBA | SERGIPE | Brasil | 2801108 | 28 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 5d454ef2-aab1-3f61-b96c-954e281262d3 | -8.07646 | -37.2771 | 2026-04-07 03:55:00 | NOAA-21 | SERTÂNIA | PERNAMBUCO | Brasil | 2614105 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| bbcecb91-9c4c-3b59-879c-c16ffa117f7d | -10.47562 | -37.42918 | 2026-04-07 03:55:00 | NOAA-21 | RIBEIRÓPOLIS | SERGIPE | Brasil | 2806008 | 28 | 33 | nan | nan | nan | Caatinga | 0.7 |
| a3a8ea27-03e1-3f1d-812c-835ac79caa64 | -10.19605 | -36.95959 | 2026-04-07 03:55:00 | NOAA-21 | CANHOBA | SERGIPE | Brasil | 2801108 | 28 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 69b7f9df-5a0f-3fd8-89d1-b4e637ec89f4 | -9.72513 | -37.20174 | 2026-04-07 03:55:00 | NOAA-21 | BELO MONTE | ALAGOAS | Brasil | 2700904 | 27 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 7b57bdf1-4e92-3958-be04-504560914ac1 | -10.19662 | -36.95577 | 2026-04-07 03:55:00 | NOAA-21 | CANHOBA | SERGIPE | Brasil | 2801108 | 28 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 45503f90-db30-33d5-9fd6-3a6068d7af28 | -10.05266 | -38.28381 | 2026-04-07 03:55:00 | NOAA-21 | JEREMOABO | BAHIA | Brasil | 2918100 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 02a42d7f-40ae-3367-92ef-3892061fb2a5 | -12.40987 | -39.21574 | 2026-04-07 03:57:00 | NOAA-21 | SANTO ESTÊVÃO | BAHIA | Brasil | 2928802 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| d0820a0e-2e8e-35ef-8f81-234c9e3c52b6 | -13.03587 | -45.06623 | 2026-04-07 03:57:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ad2643d6-8686-3563-ac89-f28a956690ee | -13.03523 | -45.06984 | 2026-04-07 03:57:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0297aa67-cbf2-32bb-97f1-01df8e89e81f | -13.04055 | -45.06339 | 2026-04-07 03:57:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bc7717ed-5627-3ddf-b609-de24f2d1e954 | -11.71178 | -44.7359 | 2026-04-07 03:57:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 98a9c41d-c39c-3ea8-9973-639e0566466e | -13.03459 | -45.07349 | 2026-04-07 03:57:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| aef67aea-e4c6-3cca-b905-54183d972298 | -13.03992 | -45.06699 | 2026-04-07 03:57:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5dfbc7d8-a0bd-386f-849b-d775609bd99e | -11.71521 | -44.74028 | 2026-04-07 03:57:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6311fc2f-de20-3314-b65d-1ec62c91f5dc | -11.7155 | -44.74022 | 2026-04-07 03:57:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 63056342-8eca-31c7-a2b1-40efdb80de3c | -17.59619 | -46.63686 | 2026-04-07 03:57:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 853c1303-cf6b-340e-9677-3de2bc6e1893 | -13.03928 | -45.07059 | 2026-04-07 03:57:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8482e728-0026-361f-a185-901699007d78 | -15.41241 | -43.06882 | 2026-04-07 03:57:00 | NOAA-21 | CATUTI | MINAS GERAIS | Brasil | 3115474 | 31 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 65130e29-4ac4-3760-a93f-2aa83ae81049 | -13.21419 | -43.69025 | 2026-04-07 03:57:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3d81f130-92f4-3671-8762-289ad8e1a329 | -12.03664 | -45.3463 | 2026-04-07 03:57:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8b7ae611-ca16-36d8-b2c5-750e09e86082 | -15.4089 | -43.06818 | 2026-04-07 03:57:00 | NOAA-21 | CATUTI | MINAS GERAIS | Brasil | 3115474 | 31 | 33 | nan | nan | nan | Caatinga | 0.7 |
| e29ba06d-227d-3e13-bd58-aa162f814cd9 | -19.57328 | -42.37106 | 2026-04-07 04:00:00 | NOAA-21 | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 02d5d63f-f7af-36ea-85ca-07cb46c96090 | -18.49984 | -55.51908 | 2026-04-07 04:00:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 13.0 |
| 4a9c83c9-2e8d-39b6-9a75-5a36c4a418cd | -18.5015 | -55.51214 | 2026-04-07 04:00:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.3 |
| 5de0c7ce-990e-3f64-ab50-745cda952eea | -19.59878 | -40.07365 | 2026-04-07 04:00:00 | NOAA-21 | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 75d74209-dcdc-37ca-8d1e-bac6adf94ae5 | -22.03795 | -56.30489 | 2026-04-07 04:00:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 697a5390-fee6-3e86-89bf-637637bdce80 | -18.50396 | -55.52457 | 2026-04-07 04:00:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.0 |
| 98073f62-ce1c-35e1-a776-1eb394d07055 | -19.59822 | -40.07742 | 2026-04-07 04:00:00 | NOAA-21 | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 430b1cda-e10b-3f1f-9c48-d1a44393c1ef | -19.59765 | -40.08118 | 2026-04-07 04:00:00 | NOAA-21 | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| f09c1aeb-b3e0-3a84-b78f-32d29f16f4af | -18.50566 | -55.51764 | 2026-04-07 04:00:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.0 |
| e8da31bd-060c-300e-ae79-320e94e0e784 | -21.6935 | -41.98719 | 2026-04-07 04:00:00 | NOAA-21 | ITAOCARA | RIO DE JANEIRO | Brasil | 3302106 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| a7e90d6b-3e14-317f-a1bf-91eda963b96e | -18.50044 | -55.50894 | 2026-04-07 04:00:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.4 |
| 183b2442-1889-3b84-99ac-2a199f12f8e9 | -19.14991 | -45.11079 | 2026-04-07 04:00:00 | NOAA-21 | ABAETÉ | MINAS GERAIS | Brasil | 3100203 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| bf556be7-e9db-34be-985a-8ab6639f54d0 | -18.49459 | -55.51034 | 2026-04-07 04:00:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.3 |
| 2446f9dd-3842-3d71-96a6-bc33a45961b6 | -18.49625 | -55.50339 | 2026-04-07 04:00:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.3 |
| db251505-c0fa-3e9d-adf9-f4e34bcaca13 | -18.49875 | -55.51587 | 2026-04-07 04:00:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.0 |
| e4950821-2ab0-3a37-8f23-9b458b35a464 | -19.59485 | -40.07685 | 2026-04-07 04:00:00 | NOAA-21 | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| ad69304b-78bc-3083-9889-275ce32bd1f2 | -19.39421 | -53.35053 | 2026-04-07 04:00:00 | NOAA-21 | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9f6955b1-5c8b-3d5a-a25a-bb71045d3147 | -25.32522 | -49.42202 | 2026-04-07 04:02:00 | NOAA-21 | CAMPO MAGRO | PARANÁ | Brasil | 4104253 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| b193fa29-9401-3a7e-9c6e-0f708cbcc02e | -26.99519 | -52.07451 | 2026-04-07 04:02:00 | NOAA-21 | LINDÓIA DO SUL | SANTA CATARINA | Brasil | 4209854 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 4d727a4b-8aac-3bc2-8b37-2e3850a13b2f | -25.32948 | -49.42302 | 2026-04-07 04:02:00 | NOAA-21 | CAMPO MAGRO | PARANÁ | Brasil | 4104253 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 9757b03a-7331-39c0-be25-f4dde3b1d8fb | -11.71423 | -44.74209 | 2026-04-07 04:27:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ebe11d73-4dc7-3a80-884c-12087c43cd3f | -13.03668 | -45.06736 | 2026-04-07 04:27:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 930a0898-1503-3bb9-a7a3-13fbfa4c8e5b | -9.45826 | -46.07374 | 2026-04-07 04:27:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6d05742a-7dba-3d07-8435-57e477d00545 | -11.71143 | -44.73794 | 2026-04-07 04:27:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 66802f32-e7e5-3d89-9ca3-4f0a154d0cdc | -11.60413 | -55.32289 | 2026-04-07 04:27:00 | NPP-375D | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1b2488f0-f558-3fa0-aeb8-7e64795380ba | -13.03556 | -45.07463 | 2026-04-07 04:27:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 091051ae-dbec-3ea7-ae84-87a667f77025 | -9.46159 | -46.07427 | 2026-04-07 04:27:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| dea03cc5-7e56-3c64-b564-1d583298f21f | -13.04004 | -45.06789 | 2026-04-07 04:27:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 394f0050-4bf7-341a-9037-6b29073cf493 | -11.60947 | -55.32398 | 2026-04-07 04:27:00 | NPP-375D | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 93e6adb8-6b6e-3fd3-ae0d-2f4fe913343f | -13.03612 | -45.071 | 2026-04-07 04:27:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b9e33c8e-5f8e-3400-936d-411a035a0985 | -12.03858 | -45.34843 | 2026-04-07 04:27:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0fb18067-5077-37f2-a35b-84b025725102 | -13.0406 | -45.06424 | 2026-04-07 04:27:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fb5ced39-2c23-3b9c-90f6-7d9be2dfa7b9 | -10.19484 | -36.95756 | 2026-04-07 04:27:00 | NPP-375D | CANHOBA | SERGIPE | Brasil | 2801108 | 28 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 72149bea-09f8-3381-ac2f-f20327c3fe18 | -13.03724 | -45.06371 | 2026-04-07 04:27:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f913fbf7-d35e-303e-9127-756f0ec377ae | -12.03525 | -45.3479 | 2026-04-07 04:27:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4a4e17f7-0b4e-3ff9-935c-615f2fe7d540 | -13.04341 | -45.06842 | 2026-04-07 04:27:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 70eaac42-b2c5-387b-b379-0dd646924444 | -13.21219 | -43.69015 | 2026-04-07 04:27:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 137ce2fd-48d0-3558-8dd3-05e1a3af6d80 | -6.08542 | -46.05637 | 2026-04-07 04:27:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 95a4c392-125b-3261-90de-eb08f1980f4f | -10.19443 | -36.96071 | 2026-04-07 04:27:00 | NPP-375D | CANHOBA | SERGIPE | Brasil | 2801108 | 28 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 6435305f-dc85-35f7-bf90-575442d153b7 | -19.59864 | -40.08281 | 2026-04-07 04:29:00 | NPP-375D | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 2e542181-0951-36ea-ae5f-cd46186c7bc3 | -18.24638 | -51.72712 | 2026-04-07 04:29:00 | NPP-375D | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 77a00a78-2f8c-3623-9dd8-fa9de0ac01dc | -19.59448 | -40.07684 | 2026-04-07 04:29:00 | NPP-375D | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 4fbe70b1-9f2c-3565-a9c7-896a2ac2ca50 | -17.90392 | -54.11863 | 2026-04-07 04:29:00 | NPP-375D | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| aee58823-afad-3732-844f-099b93318d97 | -18.25104 | -51.72296 | 2026-04-07 04:29:00 | NPP-375D | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 35690035-3b13-320f-9df0-803aa62858cc | -19.59925 | -40.07747 | 2026-04-07 04:29:00 | NPP-375D | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 238f3e53-301d-32cb-9f8e-ae4619352bf2 | -17.90306 | -54.12313 | 2026-04-07 04:29:00 | NPP-375D | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 67b8ebdc-2712-3cf7-9581-44d635666a4f | -15.41236 | -43.07035 | 2026-04-07 04:29:00 | NPP-375D | CATUTI | MINAS GERAIS | Brasil | 3115474 | 31 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 9c10aead-2ab6-32bd-8f50-21fd2d63de3c | -13.23278 | -53.32133 | 2026-04-07 04:29:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 67960286-67c1-3d6e-8237-95e2ae5ec8c0 | -22.0454 | -56.30414 | 2026-04-07 04:32:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 061a6e1d-70fa-357b-9f1f-d0033d0fd1ec | -18.49535 | -55.51068 | 2026-04-07 04:32:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.4 |
| 1a1a1943-97f2-3c37-bde7-f46af186abb5 | -18.49903 | -55.51716 | 2026-04-07 04:32:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.6 |
| a541b8af-b2e9-39d5-a642-c779b2192f8e | -18.50271 | -55.52364 | 2026-04-07 04:32:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| e7e9b910-14b6-3aad-9831-5518dfa209cc | -18.50486 | -55.51283 | 2026-04-07 04:32:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.6 |
| 10fee7f5-376a-31b5-9be9-2b8b144092cd | -18.49643 | -55.50528 | 2026-04-07 04:32:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.4 |
| 43b6b8eb-56f8-3e64-826e-9c4b13292067 | -18.5001 | -55.51176 | 2026-04-07 04:32:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.6 |
| f11d6edb-bc1c-3806-8623-b121f55198ed | -18.50379 | -55.51824 | 2026-04-07 04:32:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.6 |
| 26708343-dd9b-34b8-bffa-c626c6b72cf8 | -20.3802 | -55.03962 | 2026-04-07 04:32:00 | NPP-375D | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README2.md)
