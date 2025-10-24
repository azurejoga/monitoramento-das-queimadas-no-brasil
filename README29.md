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

## Dados Diários - Página 29

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9ad0eb32-1dec-3bc1-aab9-2b4e559bac29 | -12.82158 | -48.67314 | 2025-10-24 04:19:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b1d625bb-cfc3-3716-9dcd-299a821345a2 | -17.65824 | -46.66786 | 2025-10-24 04:19:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d6e94cc2-11b6-367f-88c5-257dc9f06a02 | -12.41645 | -54.36472 | 2025-10-24 04:19:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 62c454ce-569f-3385-bb2d-a5317198d9ee | -13.12485 | -47.25475 | 2025-10-24 04:19:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7bf541d3-c758-382f-881d-58cbc3e7cc04 | -7.29957 | -46.95518 | 2025-10-24 04:19:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7f507d69-44e3-35ee-a805-68e838baf276 | -13.24659 | -47.88642 | 2025-10-24 04:19:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5a810e65-a332-3b39-8185-1a03a6d02c7e | -6.7788 | -45.47217 | 2025-10-24 04:19:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d3cdd3b5-95c6-37df-84df-8192d6d6f496 | -12.76831 | -47.37839 | 2025-10-24 04:19:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b713daf8-7936-3552-8521-23769b9e13f2 | -12.8178 | -48.67241 | 2025-10-24 04:19:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8f1f020c-5c39-345b-9d9a-dfb2531e4b86 | -6.77916 | -45.49185 | 2025-10-24 04:19:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 98643daf-ba9a-30de-920d-c528ac7c2a5c | -16.64342 | -43.70923 | 2025-10-24 04:19:00 | NPP-375D | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 66b36270-29ad-3b38-b863-74b0d9dd13e9 | -18.45616 | -44.44378 | 2025-10-24 04:19:00 | NPP-375D | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 618bb830-cba8-30dc-b520-806a97bd3739 | -18.34559 | -51.69516 | 2025-10-24 04:19:00 | NPP-375D | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e2419a64-f3c6-34f6-b423-0260d3f9838b | -15.31877 | -47.85384 | 2025-10-24 04:19:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 28f26890-ea2d-30bf-b12f-d7efb3f20ec1 | -14.48208 | -47.92244 | 2025-10-24 04:19:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 3b6cb968-b81d-317a-8974-5e50c0101663 | -8.07037 | -47.13016 | 2025-10-24 04:19:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e7f51576-9ef1-3036-971d-902c2e57afac | -16.12548 | -54.00744 | 2025-10-24 04:19:00 | NPP-375D | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4b4c68a4-5c6b-3cd9-a21d-084f3816e017 | -15.18748 | -47.945 | 2025-10-24 04:19:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6ccd4704-6cee-3211-ac31-daf5737d2a18 | -17.66063 | -46.65316 | 2025-10-24 04:19:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b61418d2-cb61-32ba-8f0e-6405b5b324de | -7.1376 | -45.04816 | 2025-10-24 04:19:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 61028ba1-d39a-355d-8ba8-8df24e06fa54 | -18.91283 | -47.18016 | 2025-10-24 04:19:00 | NPP-375D | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 05e928ca-c0af-32c3-969f-26421f04c56c | -17.09945 | -46.18902 | 2025-10-24 04:19:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0e0cd459-464e-307f-8f3e-c956adc3a250 | -6.78351 | -45.46516 | 2025-10-24 04:19:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 93236e24-0145-3f45-9a57-cfb94bb8d011 | -7.37346 | -47.02506 | 2025-10-24 04:19:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6774318c-7fa3-38e6-9e21-60829580ea3b | -15.31524 | -47.85327 | 2025-10-24 04:19:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e5ca1316-b1b0-3bcf-86b9-dcedc97c7cf7 | -7.14162 | -45.04503 | 2025-10-24 04:19:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 64752c9c-392d-310a-99bc-d7f23642abc4 | -20.13267 | -41.79797 | 2025-10-24 04:19:00 | NPP-375D | DURANDÉ | MINAS GERAIS | Brasil | 3123528 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 8fbc5dcb-c63e-3e06-8150-9107fb865ccc | -6.78227 | -45.47276 | 2025-10-24 04:19:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 64ddf17d-0a5b-3a3c-b6ff-74599d983993 | -6.35456 | -47.06085 | 2025-10-24 04:19:00 | NPP-375D | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ba1f781f-f331-360a-917c-5795ed5ed295 | -7.12817 | -45.49638 | 2025-10-24 04:19:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4f39d513-77f9-3a2e-a0dd-17d983f0ba39 | -6.8081 | -45.44543 | 2025-10-24 04:19:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| aa802bdd-bf55-35a6-85f9-846c5d4b74e7 | -20.20779 | -45.8033 | 2025-10-24 04:19:00 | NPP-375D | IGUATAMA | MINAS GERAIS | Brasil | 3130309 | 31 | 33 | nan | nan | nan | Cerrado | 18.3 |
| a2b7db21-f13d-3862-a797-9f1e6a8dc285 | -6.77942 | -45.46837 | 2025-10-24 04:19:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 329b6689-480e-3dd6-99bc-65f70949dca6 | -8.11195 | -47.05049 | 2025-10-24 04:19:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c1cb80ed-2c27-3dfd-b2c1-2622e39a8929 | -14.7604 | -46.60357 | 2025-10-24 04:19:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cdc0f8be-1e5d-39b4-b0ea-f0d0630039f7 | -15.18804 | -47.0841 | 2025-10-24 04:19:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6743b669-1d9a-3fc2-885e-9310497c4c4e | -6.51342 | -48.49346 | 2025-10-24 04:19:00 | NPP-375D | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3c6cb943-86ea-30ac-b0be-fd6039e2d963 | -17.09553 | -46.19207 | 2025-10-24 04:19:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 466a4f62-035f-3cf4-9604-5ced6a080e5d | -7.82123 | -45.38108 | 2025-10-24 04:19:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1b794bd1-b0f8-33ce-92fc-71b12b7f3308 | -7.38747 | -46.53768 | 2025-10-24 04:19:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d6d502a0-2d97-391b-857d-0752c63dde8d | -17.71309 | -46.20034 | 2025-10-24 04:19:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d39c50a9-6b60-3441-8002-ec72b7250f14 | -13.36536 | -50.47062 | 2025-10-24 04:19:00 | NPP-375D | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a592f1ac-a999-3cf5-94a7-2fa1f015293b | -6.77978 | -45.488 | 2025-10-24 04:19:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 421f61ee-8bc9-3755-914e-8f0d3577feff | -18.76277 | -46.82178 | 2025-10-24 04:19:00 | NPP-375D | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a47bf6ec-dacc-3b8a-a8f3-9cb1020122ed | -14.4338 | -50.9592 | 2025-10-24 04:19:00 | NPP-375D | ARUANÃ | GOIÁS | Brasil | 5202502 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 39fbcf00-a45b-3365-875b-d949c2abc53b | -15.19101 | -47.9457 | 2025-10-24 04:19:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b7108399-2f1b-34a0-a1fb-9d038295ed64 | -17.40506 | -52.01842 | 2025-10-24 04:19:00 | NPP-375D | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 5504f20c-68b8-3257-b16d-5ca62b8662d3 | -12.8105 | -48.62983 | 2025-10-24 04:19:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5e46c89e-f0fc-3d1a-835f-9199a9794dac | -7.06066 | -43.1674 | 2025-10-24 04:19:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 4d9154c2-b1d9-3d11-abb2-e0882236c1de | -6.88536 | -43.61359 | 2025-10-24 04:19:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 94148f30-7d0c-3469-888c-c6de1dd2b473 | -14.15509 | -47.01223 | 2025-10-24 04:19:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fb9d59f1-a188-3ec3-aecd-3634ae087359 | -15.56632 | -45.93193 | 2025-10-24 04:19:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 338066c0-8fdd-3730-93c1-19ee096a9b34 | -13.88537 | -48.36953 | 2025-10-24 04:19:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 22db94b6-6bd1-3bc0-96d9-10fd19463483 | -7.83532 | -45.5919 | 2025-10-24 04:19:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| b2b71b03-8d5c-3f28-8146-3622148f5252 | -8.32665 | -46.24841 | 2025-10-24 04:19:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 5c197a72-c9a2-3d65-bafe-114e2e052ce9 | -12.81879 | -50.96106 | 2025-10-24 04:19:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 11c0ac24-9d1d-3d0d-97dc-c3e2cb2f88e4 | -6.28059 | -47.01593 | 2025-10-24 04:19:00 | NPP-375D | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f14b9f1a-de74-3c50-8f64-3fa097197874 | -15.13645 | -47.92345 | 2025-10-24 04:19:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bc4f7e0a-f059-3106-90b6-38511b33f6a9 | -6.75113 | -46.54878 | 2025-10-24 04:19:00 | NPP-375D | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3aabba5f-5fad-324c-8d7c-efc629287168 | -12.82186 | -48.63165 | 2025-10-24 04:19:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ef2f2a05-56bf-3e18-9e73-838ff0268ec7 | -6.79408 | -46.46866 | 2025-10-24 04:19:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2b5efbe9-6e5a-3612-8d01-9e6d07e600bb | -20.21056 | -45.80758 | 2025-10-24 04:19:00 | NPP-375D | IGUATAMA | MINAS GERAIS | Brasil | 3130309 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 6d732b37-89f9-3e29-927f-ea60909a6791 | -13.02463 | -48.57763 | 2025-10-24 04:19:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d76d3046-afa1-33a0-b4f6-8030e851720f | -13.30054 | -47.45754 | 2025-10-24 04:19:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e7418400-5265-377a-8b87-f244c694214c | -8.61515 | -44.81517 | 2025-10-24 04:19:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| efd66143-9680-38ee-8c98-2a13ca964b04 | -6.8097 | -45.45758 | 2025-10-24 04:19:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bc7fde6f-9d30-30b9-844a-4240b5f086e1 | -13.6431 | -49.45539 | 2025-10-24 04:19:00 | NPP-375D | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9f846596-4a8b-3eb2-89b9-dfe90c7bab0e | -6.80872 | -45.44164 | 2025-10-24 04:19:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0c1d361a-a05d-3104-833b-8f4cea06459d | -19.59198 | -43.74537 | 2025-10-24 04:19:00 | NPP-375D | TAQUARAÇU DE MINAS | MINAS GERAIS | Brasil | 3168309 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 66c3a4fc-8978-3848-ba8f-6bec17e67d36 | -6.93364 | -45.16354 | 2025-10-24 04:19:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1ca1b34e-f14c-3e3d-ab01-cf88ef27fb74 | -15.21029 | -47.95655 | 2025-10-24 04:19:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1ca85f37-bc5d-3c7f-9bc6-60e991a0b260 | -14.77234 | -49.29649 | 2025-10-24 04:19:00 | NPP-375D | HIDROLINA | GOIÁS | Brasil | 5209804 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d574fd87-df37-3567-8416-28ffc4e64877 | -16.48403 | -47.82237 | 2025-10-24 04:19:00 | NPP-375D | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 330c3779-5e76-3c28-9b73-1bc48c749a0d | -8.20588 | -46.98609 | 2025-10-24 04:19:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| cfcb5782-fc20-3440-b746-9ca4ce232414 | -12.8741 | -48.59528 | 2025-10-24 04:19:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 84b9cc58-60a5-3818-9ae0-c02236d98c32 | -13.04171 | -47.21308 | 2025-10-24 04:19:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 00731cd4-fab0-385b-a421-b407ddd35213 | -13.76211 | -48.34452 | 2025-10-24 04:19:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0ce19e49-c035-3b61-b40a-34863ff478ad | -8.56737 | -44.86676 | 2025-10-24 04:19:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d5dd288f-55f7-3167-88a1-fa4ba279ddc1 | -19.9852 | -44.22935 | 2025-10-24 04:19:00 | NPP-375D | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 54f168f7-fac6-3fe7-adaf-18bb0827d3a9 | -7.48876 | -42.57624 | 2025-10-24 04:19:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 6.9 |
| c841d62d-d163-3887-9148-76f616e1632d | -17.03628 | -51.49924 | 2025-10-24 04:19:00 | NPP-375D | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bbf485f7-54ca-3cb1-955b-e16d6ad3452b | -13.96734 | -50.30857 | 2025-10-24 04:19:00 | NPP-375D | MUNDO NOVO | GOIÁS | Brasil | 5214051 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c29bf278-d753-3a3a-9c32-72878baf426f | -17.2377 | -44.11244 | 2025-10-24 04:19:00 | NPP-375D | ENGENHEIRO NAVARRO | MINAS GERAIS | Brasil | 3123809 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 2a86dfc5-a274-3f4a-aa54-8ee9bebd8d1a | -13.7606 | -48.35326 | 2025-10-24 04:19:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2dead11c-d51e-3b81-be6a-3cb824acb6c4 | -8.16292 | -43.38473 | 2025-10-24 04:19:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| aa0dd007-b170-3110-aac6-e5c2fe0839ec | -13.91113 | -48.37365 | 2025-10-24 04:19:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b0135aa6-2649-3cf3-852b-4680a09a520d | -6.78627 | -45.42638 | 2025-10-24 04:19:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5a5271eb-8098-312e-96b1-070b10ecf5e1 | -15.83903 | -49.09204 | 2025-10-24 04:19:00 | NPP-375D | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ce67b1b9-2c93-3a89-9cc6-623ceef69ff3 | -6.92637 | -44.01392 | 2025-10-24 04:19:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 9894d456-3dc9-3a76-b5fb-6f9b262d7890 | -6.78974 | -45.42692 | 2025-10-24 04:19:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 45a84b5f-06e8-39dc-ad17-38481b91bf2e | -18.00075 | -51.22369 | 2025-10-24 04:19:00 | NPP-375D | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e6e474c2-df1b-342b-b0dd-61963b4b33c3 | -8.66573 | -44.77952 | 2025-10-24 04:19:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 217c65ec-6bea-36d9-a4b3-2aee2d6e6e51 | -7.54826 | -47.36568 | 2025-10-24 04:19:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f5ff8b47-0601-382a-8d6f-6318ab6fd445 | -14.73946 | -46.60369 | 2025-10-24 04:19:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6ca3728f-9d33-3ba7-9f69-e13a596a0728 | -12.67966 | -48.62377 | 2025-10-24 04:19:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b03cf256-5362-3460-9383-06b6ab40f7ee | -8.65221 | -44.7993 | 2025-10-24 04:19:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0422aa1b-70a0-3b22-997e-0e7177a22f13 | -8.41776 | -45.66586 | 2025-10-24 04:19:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2b85ae1d-54ae-3383-9eca-21240f19353f | -8.6112 | -44.81821 | 2025-10-24 04:19:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 02cced6c-5799-39c8-9e66-24d49be14bab | -12.81802 | -50.96535 | 2025-10-24 04:19:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 634286b2-6d10-34e7-a501-418d071d170a | -15.62707 | -48.54759 | 2025-10-24 04:19:00 | NPP-375D | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |


[Clique aqui para ver as próximas entradas](README30.md)
