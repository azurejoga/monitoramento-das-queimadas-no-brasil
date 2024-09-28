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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8e077803-7562-300b-b89b-98ec1be8d58e | -12.7361 | -43.469101 | 2024-09-28 00:12:48 | METOP-B | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 7b312120-51d5-3282-84e1-0d162d7238f6 | -12.9965 | -44.7379 | 2024-09-28 00:12:48 | METOP-B | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c117abf3-c990-32f8-9a46-49501a7d7ab4 | -12.9983 | -44.746201 | 2024-09-28 00:12:48 | METOP-B | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ce253419-d49d-31a5-b0b4-793582212cf6 | -12.9867 | -44.740002 | 2024-09-28 00:12:49 | METOP-B | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 490896cd-2077-3487-b4e2-7574cc66b7ab | -12.9885 | -44.748299 | 2024-09-28 00:12:49 | METOP-B | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b4c0d9f4-c084-3762-a739-49917a06d594 | -13.271 | -46.307899 | 2024-09-28 00:12:49 | METOP-B | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| fcfe14de-2d20-34cd-a3e4-1df2d2c0c0c7 | -13.2772 | -46.3382 | 2024-09-28 00:12:49 | METOP-B | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| fd39f74d-773d-3be4-89dc-5a820ecdaa86 | -13.269 | -46.297798 | 2024-09-28 00:12:49 | METOP-B | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f7c4843e-74a5-302f-96d8-bd316a5f04e4 | -13.2731 | -46.318001 | 2024-09-28 00:12:49 | METOP-B | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 272db135-aee9-3aa1-b1a0-b8e66d9f63ea | -13.2752 | -46.328098 | 2024-09-28 00:12:49 | METOP-B | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 5d9c5c59-4512-3411-a594-4ca83aa89cc7 | -13.2592 | -46.299801 | 2024-09-28 00:12:49 | METOP-B | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 025fbb50-c964-31a0-91c2-e056fba44b1a | -13.2612 | -46.309898 | 2024-09-28 00:12:49 | METOP-B | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| db4fa5f6-3d55-3b69-b98d-6ccbc47f1a3f | -13.2633 | -46.32 | 2024-09-28 00:12:49 | METOP-B | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 3b6d4e3c-8d99-31cb-b284-aa8beec243b7 | -13.2654 | -46.330101 | 2024-09-28 00:12:49 | METOP-B | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 95323cc5-6b6f-30e0-a1bc-61c4f93d3589 | -13.2556 | -46.332199 | 2024-09-28 00:12:50 | METOP-B | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| e4360add-7ed4-39fd-b0c2-7ae0b40ce351 | -13.2514 | -46.312 | 2024-09-28 00:12:50 | METOP-B | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 5de5b2d3-6b34-3053-bca1-44bd3f36fb66 | -13.2535 | -46.322102 | 2024-09-28 00:12:50 | METOP-B | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 30914b65-eb63-37a0-a9ce-42925c4d21d0 | -13.2494 | -46.301899 | 2024-09-28 00:12:50 | METOP-B | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ba37b1f0-2f34-37c2-8e0c-f23f47ae4eab | -13.2576 | -46.3423 | 2024-09-28 00:12:50 | METOP-B | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 06791bd4-f5b5-3275-872b-b41c1374bf41 | -13.2417 | -46.313999 | 2024-09-28 00:12:50 | METOP-B | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 8fbae895-7056-3cbe-a996-bf59fac8090f | -13.2438 | -46.3241 | 2024-09-28 00:12:50 | METOP-B | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 2588045d-cf42-30d4-88d9-b8dd5a756730 | -13.2459 | -46.334202 | 2024-09-28 00:12:50 | METOP-B | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 11369249-26c7-3d78-a75c-592b80b5600d | -13.4585 | -48.5714 | 2024-09-28 00:12:54 | METOP-B | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| de7121b4-9f9d-3f11-8f45-8257a1cc3e63 | -12.7384 | -45.558102 | 2024-09-28 00:12:55 | METOP-B | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 044e897c-58b9-3114-add3-c057f99e7e9f | -13.1704 | -48.498501 | 2024-09-28 00:12:58 | METOP-B | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| c05aef07-aa26-3fac-b339-070e3bd52c37 | -11.8287 | -42.796398 | 2024-09-28 00:13:01 | METOP-B | BROTAS DE MACAÚBAS | BAHIA | Brasil | 2904506 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| e57af97b-e7cc-3397-bb7d-38ca3b7f5ada | -12.2275 | -45.4636 | 2024-09-28 00:13:03 | METOP-B | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 669eec4e-a166-3b03-b18d-8dc9d3ab37b2 | -12.0151 | -44.942101 | 2024-09-28 00:13:05 | METOP-B | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| dff2d01f-aa1b-35c1-b051-00558475aa31 | -11.9563 | -44.954899 | 2024-09-28 00:13:06 | METOP-B | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 5dbf264b-e265-3f87-8902-1fc4490ba2eb | -11.9581 | -44.9631 | 2024-09-28 00:13:06 | METOP-B | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| fa219ec9-3fcd-31c5-b7de-2298b3e680b4 | -12.5132 | -47.950699 | 2024-09-28 00:13:07 | METOP-B | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| bab3fa9f-2842-3027-a15d-4414141c69d5 | -12.4888 | -48.592999 | 2024-09-28 00:13:10 | METOP-B | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 15962e2b-7bf3-3e0c-9d29-737a8ff357f6 | -11.2122 | -43.314301 | 2024-09-28 00:13:12 | METOP-B | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 5f40af3a-50aa-3f99-9e0d-46c037436bd9 | -11.2138 | -43.3214 | 2024-09-28 00:13:12 | METOP-B | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| d224ea88-9990-3b90-98ef-54d8fb390a5e | -12.1686 | -47.956902 | 2024-09-28 00:13:13 | METOP-B | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 672cbed0-7cd9-3ce6-884c-5cc28e698146 | -12.1711 | -47.9692 | 2024-09-28 00:13:13 | METOP-B | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6118891c-7ef0-31f3-b783-564fcfaaa991 | -12.5275 | -50.609501 | 2024-09-28 00:13:15 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 088d3f7c-2984-3765-80ae-aedc701ec372 | -12.3752 | -50.446899 | 2024-09-28 00:13:17 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 477c78c2-6466-39cf-9bd3-ec3ca2f14e72 | -12.3585 | -50.412399 | 2024-09-28 00:13:18 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| eec1124f-0d19-3e4b-80b1-01b79f048b3b | -12.362 | -50.430599 | 2024-09-28 00:13:18 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e1e394d9-2087-38db-a55c-3879b4fb54b5 | -12.3655 | -50.448799 | 2024-09-28 00:13:18 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e4bab72f-ba85-3cab-83a8-bc5fefbbde2d | -12.369 | -50.467098 | 2024-09-28 00:13:18 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c45ca95f-07d4-3c42-8bb0-7bd473bdaad6 | -12.3488 | -50.414299 | 2024-09-28 00:13:18 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 171782ee-2dfc-32ec-b0f7-0a552fb0c538 | -12.3523 | -50.432499 | 2024-09-28 00:13:18 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5d3d826e-00b3-3c90-a500-18d44acb6847 | -12.3558 | -50.450699 | 2024-09-28 00:13:18 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 890defcb-1efd-3c4a-8621-13a0deedd8fb | -12.3593 | -50.468899 | 2024-09-28 00:13:18 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 24b3c30d-84d2-3232-81f7-a2a9ef55dda2 | -12.3914 | -50.635899 | 2024-09-28 00:13:18 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a592be4a-06f1-39f3-969d-e5c0ec1f6c14 | -12.395 | -50.654701 | 2024-09-28 00:13:18 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 51e3f3cc-a95a-3b9d-a860-89d2a5cf2517 | -11.7814 | -47.6036 | 2024-09-28 00:13:18 | METOP-B | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e9645e0d-33c4-37c4-81c8-c7559477ec65 | -11.7838 | -47.615101 | 2024-09-28 00:13:18 | METOP-B | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| cd752c2d-9b54-3e8c-a3ba-f7aca36be975 | -12.339 | -50.416199 | 2024-09-28 00:13:18 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c039b99a-2721-3ff3-8a6f-f350b84e869d | -12.3425 | -50.434399 | 2024-09-28 00:13:18 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a6876567-1f6d-3c68-83fc-84b7d4e1d65b | -12.3816 | -50.637798 | 2024-09-28 00:13:18 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 901e27a6-736a-3802-8e83-946c9acfc9db | -12.3852 | -50.656601 | 2024-09-28 00:13:18 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 894b7f4e-bdfe-3cff-a249-b1936c1d905b | -11.7716 | -47.605598 | 2024-09-28 00:13:18 | METOP-B | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ebd759ef-aca5-3a77-833c-9df7564fe1f6 | -11.774 | -47.6171 | 2024-09-28 00:13:18 | METOP-B | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6d526293-81cf-3fa4-9daf-2d4271b1abca | -12.3258 | -50.400002 | 2024-09-28 00:13:18 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 524b907d-2f09-3481-8ebb-4eb74d441413 | -12.3293 | -50.418098 | 2024-09-28 00:13:18 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 01f60c03-8068-3d37-b442-b789dde66149 | -10.9889 | -44.412601 | 2024-09-28 00:13:20 | METOP-B | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| dfb07c1b-2b1e-32a5-b3bf-2b778b346921 | -10.9905 | -44.4202 | 2024-09-28 00:13:20 | METOP-B | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 7d5f71cc-c1c5-3c46-af26-7c04fe83c7b6 | -10.9922 | -44.427799 | 2024-09-28 00:13:20 | METOP-B | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d6a3ba65-01ca-3a2f-825f-ee9e7d0a5d1b | -11.2083 | -45.5825 | 2024-09-28 00:13:20 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 291a3d31-c154-3210-a492-e89dafc477c9 | -11.3483 | -46.247601 | 2024-09-28 00:13:20 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 0bfac096-8b13-325a-9678-e24017dda124 | -11.3502 | -46.256901 | 2024-09-28 00:13:20 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 930cf2a3-72ed-3b56-8dd6-7233ab5fc8d1 | -11.2837 | -46.1348 | 2024-09-28 00:13:21 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d1e69131-b2a1-3b2b-a39f-8f55d3b89785 | -11.2818 | -46.125599 | 2024-09-28 00:13:21 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 98a80fe2-498c-31c4-92f2-bee06e0f5774 | -11.3208 | -46.214298 | 2024-09-28 00:13:21 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b888c808-f89b-35c2-99ec-2d9a3043f176 | -11.3228 | -46.223598 | 2024-09-28 00:13:21 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 6c84352c-cebb-3d2c-8417-33417dc3d12c | -11.3306 | -46.261101 | 2024-09-28 00:13:21 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 7e08104e-1688-3924-af83-7da8db1514af | -11.1128 | -45.567101 | 2024-09-28 00:13:22 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 9d03ed9f-d7e2-3566-824d-d08539884559 | -11.1146 | -45.575699 | 2024-09-28 00:13:22 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e0379da6-a07b-33f2-a70f-73efca71b11c | -11.7097 | -48.405102 | 2024-09-28 00:13:22 | METOP-B | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d5c8b043-0ae3-31c5-a008-fd9a0cf1471e | -10.8646 | -44.788502 | 2024-09-28 00:13:23 | METOP-B | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a53b4a84-5445-3610-a7c6-041520ee42f0 | -10.8531 | -44.782799 | 2024-09-28 00:13:23 | METOP-B | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a2ae97a6-e263-3c6f-9285-5059c3a9c4bc | -10.8548 | -44.7906 | 2024-09-28 00:13:23 | METOP-B | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 37942197-fc32-311c-97b6-80070b3c6161 | -11.0466 | -45.689602 | 2024-09-28 00:13:23 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d1dd5271-3f4f-3889-9ae8-0dd96b2c948f | -11.0485 | -45.698299 | 2024-09-28 00:13:23 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 30b187b4-b353-3cb1-845a-8932c0e477f5 | -11.0271 | -45.693802 | 2024-09-28 00:13:24 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 287a507e-3761-3fd4-a04b-83fdd6447a7e | -11.0289 | -45.702499 | 2024-09-28 00:13:24 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a5a0d6f7-28de-3daf-a21b-827437c0eede | -11.0387 | -45.700401 | 2024-09-28 00:13:24 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 69a234e8-49f1-3ca0-976d-11ff8f8f357a | -11.0405 | -45.709099 | 2024-09-28 00:13:24 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| fbb5fe48-dce2-329d-ada5-fec2a45139c3 | -11.0173 | -45.695999 | 2024-09-28 00:13:24 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 1ad9dbd2-339b-3c7f-a066-e36013ec47ec | -11.0191 | -45.7047 | 2024-09-28 00:13:24 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| db8a6ea2-27f2-3d3b-a6f0-cbfc0fae9199 | -11.0725 | -46.1031 | 2024-09-28 00:13:24 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| bc8a967b-8e75-32a5-9cf6-8f3e02428c7a | -11.1056 | -46.163101 | 2024-09-28 00:13:24 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 2d0f6c8c-7927-38a0-82e0-f8a6a2ef0a8b | -11.2729 | -47.113201 | 2024-09-28 00:13:25 | METOP-B | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9d5036d8-6b69-3026-8ccb-55cfd9ffe0fa | -10.864 | -45.504799 | 2024-09-28 00:13:26 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ab8ee634-ea78-3ae2-a342-ae8357102a13 | -10.8596 | -45.532299 | 2024-09-28 00:13:26 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 405674e7-cb99-3ff4-b52b-6c5b95ad6ba8 | -10.8614 | -45.540798 | 2024-09-28 00:13:26 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 51823f73-80de-37a2-982a-d55436632660 | -10.8498 | -45.5345 | 2024-09-28 00:13:26 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 5f73745a-3e89-3f31-8ea6-f20967317cc4 | -10.8534 | -45.551399 | 2024-09-28 00:13:26 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 514b13af-c81f-3c23-98ff-32b1cfb44b30 | -10.8756 | -45.5112 | 2024-09-28 00:13:26 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 659a0015-cb76-35dc-8872-1cf71d1d0152 | -10.8658 | -45.513302 | 2024-09-28 00:13:26 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 6733a2b6-d810-3bd6-a596-f55627469875 | -10.8676 | -45.521702 | 2024-09-28 00:13:26 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 13a5cf9d-6a86-3520-86f5-8df526956bae | -10.8516 | -45.5429 | 2024-09-28 00:13:26 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 017f717e-897b-3bef-9ce2-098a697719d9 | -11.696 | -50.02 | 2024-09-28 00:13:27 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c625503a-623c-3f4c-b0a6-8472b1010a8c | -10.2774 | -43.552502 | 2024-09-28 00:13:28 | METOP-B | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d8471d3d-845f-35b8-b2b5-52b591808350 | -10.279 | -43.559601 | 2024-09-28 00:13:28 | METOP-B | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 0b39b420-85bb-3501-a424-4640eca59481 | -10.2805 | -43.566799 | 2024-09-28 00:13:28 | METOP-B | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| deff36d0-698b-3d34-a88a-ebf55b37623e | -10.8382 | -46.0112 | 2024-09-28 00:13:28 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README5.md)
