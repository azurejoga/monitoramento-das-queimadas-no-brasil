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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 172d7133-9899-375d-92a5-38d07401e312 | -13.29211 | -43.54821 | 2026-06-28 03:53:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 42332842-1e6b-3b7e-8aea-3944b778f53d | -13.88874 | -47.177 | 2026-06-28 03:53:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c13a20b3-16ca-3c83-8232-92c198360c2b | -10.8475 | -49.13411 | 2026-06-28 03:53:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b69403ad-ed42-3758-9eba-917d057e4917 | -11.60545 | -43.11004 | 2026-06-28 03:53:00 | NPP-375D | MORPARÁ | BAHIA | Brasil | 2921609 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |
| b206b0d5-141a-343b-b969-7e43572f4e92 | -11.60465 | -43.11444 | 2026-06-28 03:53:00 | NPP-375D | MORPARÁ | BAHIA | Brasil | 2921609 | 29 | 33 | nan | nan | nan | Caatinga | 4.5 |
| e7b590af-3306-3885-8c5d-8208897c8f9a | -11.60908 | -43.1153 | 2026-06-28 03:53:00 | NPP-375D | MORPARÁ | BAHIA | Brasil | 2921609 | 29 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 9494d138-c714-3ab0-ac98-f41e7f510267 | -13.9468 | -47.34097 | 2026-06-28 03:53:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d8e1062f-5b0b-3bd2-8fbc-79a88f4a5379 | -12.27238 | -50.1067 | 2026-06-28 03:53:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fe391a86-4575-3321-a2fa-7b792bcc045f | -13.29317 | -43.55014 | 2026-06-28 03:53:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6b53f3fc-d544-3c84-920b-a6bee24f206f | -12.2661 | -43.51432 | 2026-06-28 03:53:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cc642db6-cd2f-3538-98fb-105813b5c091 | -13.45245 | -44.0449 | 2026-06-28 03:53:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bc1262a9-f956-30f9-b23c-50fda9d4a8e4 | -14.86466 | -43.59171 | 2026-06-28 03:53:00 | NPP-375D | MATIAS CARDOSO | MINAS GERAIS | Brasil | 3140852 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7d05f63e-cfe7-3876-86ba-690d05a4fc0b | -14.04348 | -46.33152 | 2026-06-28 03:53:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d3807dcb-3a73-3576-a0ea-d81cb3bb0be3 | -17.49615 | -39.45335 | 2026-06-28 03:55:00 | NPP-375D | ALCOBAÇA | BAHIA | Brasil | 2900801 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 08aecd28-8892-30e1-953c-20e9ff4fe2a2 | -19.81637 | -42.87812 | 2026-06-28 03:55:00 | NPP-375D | SÃO DOMINGOS DO PRATA | MINAS GERAIS | Brasil | 3161007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| e222d89e-126c-38df-ba48-0ed70a5e6d47 | -17.69867 | -46.77905 | 2026-06-28 03:55:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7909ce5b-8902-3bc1-9115-505aa1810077 | -20.97373 | -49.74542 | 2026-06-28 03:55:00 | NPP-375D | JOSÉ BONIFÁCIO | SÃO PAULO | Brasil | 3525706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| cbf2153e-f7bc-3feb-bfb1-e993a9466432 | -21.82145 | -41.36347 | 2026-06-28 03:55:00 | NPP-375D | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| eb36493b-5f22-3352-8cc8-7c13c25bf410 | -20.39572 | -45.27229 | 2026-06-28 03:55:00 | NPP-375D | ITAPECERICA | MINAS GERAIS | Brasil | 3133501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| dcecf925-080e-3872-a3d7-612d5b595e8f | -17.34766 | -42.62659 | 2026-06-28 03:55:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 50811bf5-a597-3b68-be46-5d081627c3f4 | -17.50352 | -44.8961 | 2026-06-28 03:55:00 | NPP-375D | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 38b1a82d-a517-39a0-a945-2a25db73e2d8 | -19.33847 | -42.16008 | 2026-06-28 03:55:00 | NPP-375D | SÃO JOÃO DO ORIENTE | MINAS GERAIS | Brasil | 3162609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 31d0a8a9-07eb-37bf-911a-8dfffa7d4cf7 | -17.97076 | -44.56635 | 2026-06-28 03:55:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a95d1431-6993-3876-a1cf-42311113da25 | -21.82055 | -41.36481 | 2026-06-28 03:55:00 | NPP-375D | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| ac417f5d-e391-3a98-b9e3-33feaf6f2534 | -17.97485 | -44.56924 | 2026-06-28 03:55:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c370b2aa-371b-3103-bd03-8d2636fd89a2 | -17.30213 | -42.65485 | 2026-06-28 03:55:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 41dc0d20-d674-3b63-b910-dacad471f9a7 | -17.35063 | -42.63251 | 2026-06-28 03:55:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 0dbb551e-c1ca-386e-8dec-3c85ca094298 | -20.40004 | -45.27337 | 2026-06-28 03:55:00 | NPP-375D | ITAPECERICA | MINAS GERAIS | Brasil | 3133501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 482d22ed-a504-3653-a001-0bc7576a38ec | -14.83838 | -48.14354 | 2026-06-28 03:55:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 2d39b445-3823-3e1b-a93a-f0b8b0821233 | -17.30992 | -42.65649 | 2026-06-28 03:55:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 51.9 |
| 55a92424-a5f8-3f7e-aa14-9978a2c15b1e | -17.70498 | -46.77389 | 2026-06-28 03:55:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 36d47998-a4d5-380a-93a7-8f15de4b5f3f | -17.34674 | -42.63173 | 2026-06-28 03:55:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 22a92f4b-b53e-3271-b59b-017c88cec3f6 | -17.50798 | -44.8971 | 2026-06-28 03:55:00 | NPP-375D | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1cca9995-65e4-36ca-bae6-151b5c045e1c | -17.97511 | -44.56724 | 2026-06-28 03:55:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 64788f02-ac16-3507-9662-3fe87ea0bd29 | -20.9728 | -49.74953 | 2026-06-28 03:55:00 | NPP-375D | JOSÉ BONIFÁCIO | SÃO PAULO | Brasil | 3525706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| db0b84ed-98cb-3c65-9950-ee4196fd8597 | -17.70373 | -46.78003 | 2026-06-28 03:55:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| f606eaac-272d-3d9f-8c38-5565e9317b5e | -17.70436 | -46.77695 | 2026-06-28 03:55:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 532e0efd-5a8e-3ccd-8c34-90c1e1de72f0 | -17.30603 | -42.65565 | 2026-06-28 03:55:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 51.9 |
| 6cb89ff2-5b78-3c20-bdb6-50d434a0d30c | -17.35156 | -42.62735 | 2026-06-28 03:55:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 2d29a591-73b8-3979-aac9-008a32f24042 | -14.83918 | -48.13967 | 2026-06-28 03:55:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 9f4b2d40-69b7-3f24-987e-e06257d4075f | -19.90879 | -44.04903 | 2026-06-28 03:55:00 | NPP-375D | CONTAGEM | MINAS GERAIS | Brasil | 3118601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 93bb5934-c5da-331d-a484-c2bdaf62a82a | -17.9705 | -44.56835 | 2026-06-28 03:55:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6eea64c9-0f37-3804-94cd-dba14e8e6a52 | -17.6993 | -46.77598 | 2026-06-28 03:55:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b56a3e2f-d939-3da3-92d7-a21cb5ca4d4a | -11.2279 | -54.3036 | 2026-06-28 04:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 104.0 |
| fa10d46d-0412-323c-b1ac-630f1b94d91d | -11.209 | -54.3053 | 2026-06-28 04:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 223.6 |
| 61ae30ad-e735-3e08-946b-0dcb59021cfd | -12.1937 | -52.8866 | 2026-06-28 04:00:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 113.6 |
| ef007afc-cf7a-3d93-bd4e-ce5d475481de | -11.2093 | -54.2848 | 2026-06-28 04:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 72.7 |
| e426dc77-a7e0-3ce4-bdbb-6aca8b4606d9 | -12.1934 | -52.9075 | 2026-06-28 04:00:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 2cd0ba60-27ec-3beb-93c3-527c1105e749 | -11.2088 | -54.3258 | 2026-06-28 04:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 68722734-3f84-3b3b-940b-94da20c470ed | -12.194 | -52.8657 | 2026-06-28 04:00:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 107.0 |
| aacd6b6b-53d5-36db-9157-30f41ce50de6 | -12.2131 | -52.8637 | 2026-06-28 04:00:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 61.8 |
| ea99b060-9658-38e0-91f3-7d1b5e02d07e | -12.1775 | -57.1319 | 2026-06-28 04:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 45.8 |
| 735a30b9-b0af-3a46-8ce5-5178c6e85f6f | -12.1775 | -57.1319 | 2026-06-28 04:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 45.8 |
| b7a683ab-8c30-3430-ae17-443dacdcbc1d | -12.1937 | -52.8866 | 2026-06-28 04:10:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 110.2 |
| 6f47c45a-5fe2-30f7-8266-9cba9bfe00f6 | -12.2131 | -52.8637 | 2026-06-28 04:10:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 775e8258-ba32-32ef-8dff-c78af392cfc9 | -12.1934 | -52.9075 | 2026-06-28 04:10:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 63.5 |
| 2c4894e4-037d-39d1-acef-9fec60eccaa1 | -12.194 | -52.8657 | 2026-06-28 04:10:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 92.0 |
| f0fc781f-d4ee-3ae2-a926-fbc2326f4892 | -11.209 | -54.3053 | 2026-06-28 04:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 244.8 |
| e37748e1-df39-3974-af3b-18977e9befaf | -11.2093 | -54.2848 | 2026-06-28 04:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 105.4 |
| 68201b2f-bfd9-33b0-a948-ee0a6ebafabf | -11.2279 | -54.3036 | 2026-06-28 04:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 83.5 |
| e7ec3dda-ea1d-3f59-8d5c-dccf083c1279 | -11.2088 | -54.3258 | 2026-06-28 04:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 67.6 |
| 4ecee6ee-1657-3864-896b-1fc2fbc37ba4 | -4.3469 | -47.76398 | 2026-06-28 04:10:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| ea509ff6-6473-3c39-9852-c8ef92701222 | -3.50591 | -48.03581 | 2026-06-28 04:10:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b3ccfc1b-6b19-37d5-bcaf-abce3a1bd5ea | -3.516 | -48.03245 | 2026-06-28 04:10:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 813681a0-a2d2-3de8-8f7d-383176643001 | -3.50742 | -48.03534 | 2026-06-28 04:10:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6f480eab-15cc-3a15-bc12-b87e9210b09b | -4.28021 | -48.36204 | 2026-06-28 04:10:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| c14266bd-9ba4-3ff3-8e1a-79eb1e07d605 | -2.95146 | -39.92229 | 2026-06-28 04:10:00 | NOAA-20 | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 9d958dba-ed05-33df-9906-c4ee990627ba | -3.51056 | -48.0365 | 2026-06-28 04:10:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 96067d88-f1ca-3266-b7ce-6a63e09de704 | -3.97966 | -48.42381 | 2026-06-28 04:10:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 7f1a38ad-cad8-31da-941a-2390a9c57870 | -3.98085 | -48.42521 | 2026-06-28 04:10:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 72e43479-133d-34c9-bdd1-05e39cf8f897 | -4.28487 | -48.36293 | 2026-06-28 04:10:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fc4a1df2-8639-3a64-8950-024bee763182 | -6.98603 | -42.89107 | 2026-06-28 04:12:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 27f7b279-5eea-3dc3-a99c-441686237078 | -6.98326 | -42.88698 | 2026-06-28 04:12:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.1 |
| c02ec80b-93dc-3951-89a4-32c3ce255e38 | -8.18986 | -44.4247 | 2026-06-28 04:12:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d526b220-4268-303f-9f75-c479bd32d9f5 | -6.99659 | -45.00481 | 2026-06-28 04:12:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 150e542c-eb93-3e21-8fa9-35243aa4a743 | -7.54109 | -43.75301 | 2026-06-28 04:12:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| e9327d7c-909a-3357-ba8d-06995231d375 | -11.91747 | -43.40216 | 2026-06-28 04:12:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| aa167f2e-4255-3181-9cd6-6f70168cca45 | -9.46662 | -48.13854 | 2026-06-28 04:12:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 480fb3bb-c71c-3124-8130-7b649193600b | -12.35052 | -38.19222 | 2026-06-28 04:12:00 | NOAA-20 | POJUCA | BAHIA | Brasil | 2925204 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 2ec5ae58-b186-398d-b49b-e11ce564f3ce | -6.97599 | -42.88945 | 2026-06-28 04:12:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 11.1 |
| 9f9b78ef-0ee4-37ee-8635-9f947e091ace | -7.54049 | -43.75673 | 2026-06-28 04:12:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 4a97c4a6-d844-3ae8-9e17-3ac6df339537 | -6.97207 | -42.89247 | 2026-06-28 04:12:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 8a7acf13-18e6-376e-8686-c3599c6bf36e | -6.97656 | -42.88591 | 2026-06-28 04:12:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 11.1 |
| 5280c2da-6dc2-3756-bfdd-5029738af687 | -6.97877 | -42.89353 | 2026-06-28 04:12:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 9.7 |
| d56c22a7-06d4-344a-9a7e-7f4aff882721 | -10.78798 | -46.4852 | 2026-06-28 04:12:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 33a799c9-15f6-393f-846f-d95af9f8fe03 | -11.60694 | -43.11327 | 2026-06-28 04:12:00 | NOAA-20 | MORPARÁ | BAHIA | Brasil | 2921609 | 29 | 33 | nan | nan | nan | Caatinga | 5.7 |
| d88a5108-6205-3506-af74-458a06714b83 | -9.30137 | -41.09449 | 2026-06-28 04:12:00 | NOAA-20 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 2fce950a-9672-3cfe-a337-cb0258084e54 | -10.84598 | -49.13347 | 2026-06-28 04:12:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| afa16854-141d-3610-9a11-57a8d7821cf5 | -6.9782 | -42.89708 | 2026-06-28 04:12:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 9.7 |
| 35a05ebc-bd6e-3a1b-8eff-07c005f3e20a | -11.39955 | -43.2413 | 2026-06-28 04:12:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8e43080b-e844-3844-8ba0-1fd20819be07 | -6.98211 | -42.89407 | 2026-06-28 04:12:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 59ab268e-30d2-3bc4-994c-e7a984a13ba7 | -6.97542 | -42.893 | 2026-06-28 04:12:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 9.7 |
| 08a75283-eb65-3344-90d7-a0f5c1a8a9d6 | -11.03038 | -45.07668 | 2026-06-28 04:12:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a494e1e4-965b-3989-a380-219c21c57cdd | -11.60419 | -43.10922 | 2026-06-28 04:12:00 | NOAA-20 | MORPARÁ | BAHIA | Brasil | 2921609 | 29 | 33 | nan | nan | nan | Caatinga | 5.7 |
| ab96a2cc-e9b3-31b5-a5c6-0182117f45de | -6.9866 | -42.88752 | 2026-06-28 04:12:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 5daddfc5-c003-3f81-8ca0-826123ef84ef | -10.84237 | -49.12824 | 2026-06-28 04:12:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 02669239-7dfd-3d51-8bf4-db668f10a26a | -6.98546 | -42.89462 | 2026-06-28 04:12:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 7046be46-af12-3699-a9e6-e2e5f7ec6c10 | -6.97991 | -42.88644 | 2026-06-28 04:12:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 11.1 |
| 2673e48a-6d17-3bad-9d10-41f08c23dd82 | -6.97265 | -42.88892 | 2026-06-28 04:12:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 78473c38-bbb8-3e13-804d-bbf0594d8652 | -6.97934 | -42.88998 | 2026-06-28 04:12:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 11.1 |


[Clique aqui para ver as próximas entradas](README11.md)
