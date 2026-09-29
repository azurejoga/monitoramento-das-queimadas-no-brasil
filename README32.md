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

## Dados Diários - Página 32

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1fa44bb4-4134-3ca0-93bc-9c7f1e357a6e | -12.55667 | -47.15337 | 2026-09-29 04:17:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 73ec999b-36c6-35df-b2eb-1ef8a8ac3ee8 | -13.37773 | -44.02632 | 2026-09-29 04:17:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 12c1ae66-7b83-3a20-9ba8-4691e8616806 | -11.65726 | -43.52087 | 2026-09-29 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a94c2bde-90ca-3477-8599-69cce11d44f1 | -11.34538 | -54.04104 | 2026-09-29 04:17:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 985a0d90-017c-333c-87f8-cc1274d7cec7 | -11.05319 | -54.19932 | 2026-09-29 04:17:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 581e400b-3b49-34ca-ab86-09a0fd301382 | -13.17737 | -48.55773 | 2026-09-29 04:17:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f7330eb1-14bc-3afc-89e5-e9ad1ebc2d55 | -12.76994 | -50.67157 | 2026-09-29 04:17:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| feb83b0d-38ed-3aaf-989c-60b2ccc3b772 | -14.63744 | -52.13681 | 2026-09-29 04:17:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bda55ffe-1497-3cc3-a9d0-9fe85252e4b2 | -13.17369 | -48.55705 | 2026-09-29 04:17:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1cef8166-44de-30b6-9817-ef1e8c1e2018 | -10.12024 | -45.14989 | 2026-09-29 04:17:00 | NOAA-21 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 85e40c7e-cdfa-3ddf-a829-d104398a0fc8 | -10.82218 | -48.7242 | 2026-09-29 04:17:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 698bef68-ed95-3206-ae1e-2a7757ff067b | -13.45158 | -48.58439 | 2026-09-29 04:17:00 | NOAA-21 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3c9f22a5-e402-3a5c-8637-52b57fe4ffd4 | -14.52441 | -52.48606 | 2026-09-29 04:17:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 4ff0114a-8220-36f8-9741-93d9b3b76d02 | -12.95407 | -46.63974 | 2026-09-29 04:17:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 976a9e26-e5fd-3941-a638-81db1e10be3c | -11.17304 | -44.80059 | 2026-09-29 04:17:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 9326e79e-aff0-3a5b-a8f4-aeda6eedc895 | -15.44508 | -46.14484 | 2026-09-29 04:17:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f7d18dad-8864-3618-8fe5-0faa09fca85d | -15.22757 | -46.18529 | 2026-09-29 04:17:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 0021f578-7c88-3124-bb9c-59cd70eaf6f2 | -11.60956 | -44.13956 | 2026-09-29 04:17:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4f105f5e-9986-33ef-91c4-4ebcfff9b2d0 | -11.42418 | -43.44452 | 2026-09-29 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a268c22f-16c9-3883-b3c8-43ff849670c6 | -10.20874 | -50.01268 | 2026-09-29 04:17:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 15477e99-4ab5-3819-b9a7-0dc2f5fe9526 | -12.00688 | -50.9425 | 2026-09-29 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 4dfd2c43-0aa2-362f-9e26-be42906b5b4a | -9.96552 | -50.13332 | 2026-09-29 04:17:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 1c63f89a-084b-3185-add7-9762a79b5936 | -11.43641 | -43.45374 | 2026-09-29 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c2f8fe53-0359-39ba-9631-db8cc36b8ab0 | -15.89943 | -48.0708 | 2026-09-29 04:17:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1e91d01d-59f8-3efe-bfbf-4e5e3cd5d950 | -11.3826 | -54.05159 | 2026-09-29 04:17:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fef8d5ad-7f8a-36e7-8eeb-c1edac0bc988 | -11.8562 | -47.07927 | 2026-09-29 04:17:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| aebd6a85-5ee9-3428-ae48-60b45c47a308 | -9.13252 | -49.9717 | 2026-09-29 04:17:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 7871ba4e-4e93-3f74-9e9b-680f535e3988 | -11.39181 | -54.04234 | 2026-09-29 04:17:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d219be4d-4ffa-38e7-b1cd-885f34f8e162 | -21.05811 | -47.03885 | 2026-09-29 04:17:00 | NOAA-21 | ITAMOGI | MINAS GERAIS | Brasil | 3132909 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 38954e69-6c73-3599-b65b-67a6e05d9100 | -17.10077 | -43.20603 | 2026-09-29 04:17:00 | NOAA-21 | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 138f8082-9b3d-3494-b380-b189ddf8c4c4 | -13.52927 | -46.90604 | 2026-09-29 04:17:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3e26ea69-a900-3211-a442-7dabb3cec75c | -16.33482 | -47.6969 | 2026-09-29 04:17:00 | NOAA-21 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1e24e747-eb2d-3552-b0c6-dafa445d99cf | -13.3264 | -43.94077 | 2026-09-29 04:17:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7be1af28-ee83-39f6-bcf3-f9c771e49600 | -14.5233 | -48.29649 | 2026-09-29 04:17:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e4163f78-5bcd-3fdf-bd42-f55bb9e9e87f | -15.27549 | -39.40738 | 2026-09-29 04:17:00 | NOAA-21 | ARATACA | BAHIA | Brasil | 2902252 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| f11dbd8c-13dd-331d-af3b-fc9cef1fcba8 | -11.40412 | -43.41945 | 2026-09-29 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f8dfb766-b7ff-3082-9213-f8320e2dd89a | -12.60054 | -47.28596 | 2026-09-29 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 1cd0b71b-36c4-3908-8a9b-19238cd5365a | -11.42527 | -43.43738 | 2026-09-29 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 86142ee5-122f-3803-b459-4ed0c9973bf3 | -12.69339 | -47.38259 | 2026-09-29 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ce5e2fbf-3eab-3f39-a9ea-2df5832a68e2 | -11.68779 | -44.51073 | 2026-09-29 04:17:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5f72d575-6596-3d1d-8a23-160730f38ee8 | -11.42914 | -43.43434 | 2026-09-29 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 4bb65a11-199a-3bf0-9f8c-d8eb81753d8a | -12.70948 | -46.97365 | 2026-09-29 04:17:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ff1e6be5-78c5-3d69-8e36-ac758c9b045a | -11.95745 | -50.94233 | 2026-09-29 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ed475654-6c27-3da8-85a1-f6393ee19c86 | -12.94665 | -46.64235 | 2026-09-29 04:17:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 8117d5d7-ef35-3fd9-b5ee-e19dd853c9c6 | -11.18955 | -44.82481 | 2026-09-29 04:17:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d21883fd-3f50-3977-b012-88859a77cef9 | -12.14484 | -45.00232 | 2026-09-29 04:17:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| de5fc733-c700-36b4-93e9-0634f94aa2b5 | -10.26312 | -44.63504 | 2026-09-29 04:17:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b14c32c4-82fe-3904-95b8-82fd8c4b8d80 | -11.18624 | -44.82428 | 2026-09-29 04:17:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fddd9433-010c-3c60-bd65-7d1531a898e1 | -16.29181 | -43.66518 | 2026-09-29 04:17:00 | NOAA-21 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 686552fb-f2f0-3f74-ae4e-abca84104f2e | -10.93541 | -43.88057 | 2026-09-29 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4f911bcf-2468-3d3d-b953-22fae3c30229 | -12.60121 | -47.28201 | 2026-09-29 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5b559c50-3084-335c-9ec6-8c4f224c7813 | -11.93917 | -50.91396 | 2026-09-29 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ad4ac8f9-ed25-3bab-a387-dc6605c3fb13 | -14.111 | -46.29061 | 2026-09-29 04:17:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| f62420b2-d5b2-3432-b7d3-763794d6e2b3 | -9.86038 | -44.94433 | 2026-09-29 04:17:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c0706104-d2e4-3fb8-8bc5-97f84a7b7371 | -11.97363 | -50.92761 | 2026-09-29 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9b302fb5-51bc-3367-b332-f13f4be6a7f1 | -21.06161 | -48.84145 | 2026-09-29 04:17:00 | NOAA-21 | PALMARES PAULISTA | SÃO PAULO | Brasil | 3535101 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.5 |
| e03bae52-7bfe-32ea-97ec-8a12097becf4 | -15.44897 | -46.14178 | 2026-09-29 04:17:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 20e03184-8284-3274-b814-5f534d0cd1fb | -12.88139 | -44.79469 | 2026-09-29 04:17:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 161f31f3-bc58-352b-b643-20a3866deaf7 | -12.77345 | -50.67636 | 2026-09-29 04:17:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c3ada1b0-8b5a-3cb1-9b35-efd83d07f7b7 | -12.04963 | -50.95476 | 2026-09-29 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 02b30c44-3769-3de1-aea8-5b7b0b8dd576 | -13.17209 | -48.56632 | 2026-09-29 04:17:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 23069629-e250-3c33-890f-b5878c195c02 | -15.44839 | -46.1454 | 2026-09-29 04:17:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 48ade3f2-a203-3e4f-bc3e-c92deded9cdb | -11.20003 | -44.80135 | 2026-09-29 04:17:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fc90a744-d2d8-397a-a917-538698387453 | -11.44476 | -43.46601 | 2026-09-29 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4824f7f6-416b-38eb-935f-68ad15929568 | -16.78961 | -43.00684 | 2026-09-29 04:17:00 | NOAA-21 | BOTUMIRIM | MINAS GERAIS | Brasil | 3108503 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2ffedb0f-5009-3882-b7ce-8386851ef746 | -14.96722 | -41.78543 | 2026-09-29 04:17:00 | NOAA-21 | CORDEIROS | BAHIA | Brasil | 2909000 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 03ad4104-8380-38ad-b435-40a7d2a9c0b3 | -9.95411 | -50.14814 | 2026-09-29 04:17:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 86de30a7-1a12-3460-9836-c34b760897c0 | -9.95623 | -50.16109 | 2026-09-29 04:17:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 71b74bf7-e2e0-3394-b9f1-d8d9e6cbc21d | -8.72133 | -47.60779 | 2026-09-29 04:17:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7fa9517a-b4fd-3e16-b43d-b70faad1e0eb | -11.80266 | -49.0585 | 2026-09-29 04:17:00 | NOAA-21 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 04fe9bf2-563c-36b6-a52a-11b3aae7469c | -12.71231 | -46.97801 | 2026-09-29 04:17:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| cab44ff5-4a6a-312d-8313-d6f2636e5f9e | -15.13219 | -43.62315 | 2026-09-29 04:17:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 1.5 |
| fd756f9b-b85f-3c7d-a2a7-fc94d7c16f8e | -11.41806 | -43.4399 | 2026-09-29 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8260c49d-a496-3ff9-b62d-8c1218bd3ded | -11.38391 | -54.04456 | 2026-09-29 04:17:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| db7d86cd-bf5f-347f-b26c-d219cb07d4e0 | -12.06418 | -46.46918 | 2026-09-29 04:17:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bb6a7082-799b-3b22-9230-42a86854f5b7 | -12.76923 | -50.67559 | 2026-09-29 04:17:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e1c00c3b-c537-3cfa-a28d-e8ec06b78319 | -12.07491 | -46.47073 | 2026-09-29 04:17:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3504b7b1-d536-3654-8706-1d00cc5e7f64 | -9.95982 | -50.14072 | 2026-09-29 04:17:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| feb85ea5-187c-3724-847b-cd18ef155eb6 | -14.97303 | -46.26484 | 2026-09-29 04:17:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a477f4ec-567d-391c-b25b-8f7d2108e2e7 | -11.40085 | -43.44087 | 2026-09-29 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fe169413-bd84-3fbd-a99b-a87e36cb9617 | -11.43138 | -43.44199 | 2026-09-29 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 150748a1-b40c-373f-aab4-db4a72435a15 | -12.70192 | -44.50597 | 2026-09-29 04:17:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 799c23ff-8c86-3093-a5b1-75b21f0cad32 | -13.45527 | -48.58496 | 2026-09-29 04:17:00 | NOAA-21 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b44eb57e-fde3-3ef7-98e7-c23f3a5be4fc | -15.50848 | -41.57389 | 2026-09-29 04:17:00 | NOAA-21 | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| a06527c2-e1de-3acd-8dc3-91166365cbb6 | -11.1909 | -45.13879 | 2026-09-29 04:17:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 253f0e43-3c56-390d-b0af-c862fc371b91 | -14.08683 | -46.31263 | 2026-09-29 04:17:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 6ff09a37-b17b-371e-8a9f-70450231455a | -11.17467 | -48.06673 | 2026-09-29 04:17:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 92146d8e-fa05-3bb9-8a5d-080f269847c6 | -13.19581 | -48.56097 | 2026-09-29 04:17:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c7f35978-70c1-3800-b734-60cdd2cc6da1 | -15.46008 | -46.13618 | 2026-09-29 04:17:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1d16c44d-cd3a-31de-b5c6-0e0e7753a756 | -12.94264 | -46.6455 | 2026-09-29 04:17:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 207ecac8-7d23-39d3-9af1-88ffa8c2a083 | -15.08905 | -48.32727 | 2026-09-29 04:17:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 837f805f-f7ae-3c0b-9e53-215519862e70 | -13.4801 | -48.61096 | 2026-09-29 04:17:00 | NOAA-21 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 42ae3d65-11f2-3ade-ba2f-12d7787eb336 | -9.96695 | -50.12518 | 2026-09-29 04:17:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 7cb0c44b-a5b5-3308-bbc7-0b408c3cc6d7 | -12.17427 | -50.69051 | 2026-09-29 04:17:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 999ba247-ac21-314e-a8b5-e8e334b6a006 | -9.53028 | -46.36145 | 2026-09-29 04:17:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ddf0807e-c0c6-3b90-827f-e86e038fc5db | -15.17169 | -46.17217 | 2026-09-29 04:17:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 36049dd9-723d-39bb-bbd8-7c42921059b5 | -21.07665 | -48.83605 | 2026-09-29 04:17:00 | NOAA-21 | PALMARES PAULISTA | SÃO PAULO | Brasil | 3535101 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| c2297406-e007-3758-86a4-e23f610c9fea | -11.18703 | -45.14178 | 2026-09-29 04:17:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 08dab89a-fbb7-348a-a488-f7a2449c6b47 | -10.71742 | -44.42901 | 2026-09-29 04:17:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e3176ecc-c90f-32b2-96f4-39d659e23ba1 | -12.05593 | -46.4986 | 2026-09-29 04:17:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |


[Clique aqui para ver as próximas entradas](README33.md)
