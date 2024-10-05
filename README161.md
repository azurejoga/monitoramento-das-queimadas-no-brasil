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

## Dados Diários - Página 161

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e8031ce0-0e1c-34bb-a2c4-9595943bbcb5 | -17.0865 | -56.782 | 2024-10-05 12:38:00 | TERRA_M-T | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 76.5 |
| 34f697a8-40f3-378e-a93f-36b46ff9facb | -17.0403 | -56.79951 | 2024-10-05 12:38:00 | TERRA_M-T | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 213.1 |
| 21345efd-7a8c-3115-a81c-9d61d79b5509 | -17.02454 | -56.79626 | 2024-10-05 12:38:00 | TERRA_M-T | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 338.0 |
| 9cbdeb12-2971-3045-8796-6b49c967e40e | -17.01568 | -56.78868 | 2024-10-05 12:38:00 | TERRA_M-T | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 269.2 |
| 12f60682-95d8-3b67-8e0b-5bb9c264913a | -17.00879 | -56.79299 | 2024-10-05 12:38:00 | TERRA_M-T | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 350.2 |
| ddbac227-9111-3f94-8575-889425c6001b | -16.99993 | -56.78537 | 2024-10-05 12:38:00 | TERRA_M-T | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 232.3 |
| 52ed3f5c-e39a-3b25-a374-fdd0529e0cad | -16.99303 | -56.7897 | 2024-10-05 12:38:00 | TERRA_M-T | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 139.2 |
| f96b7dd6-42ed-32f7-97cf-522d570320e0 | -16.98418 | -56.78206 | 2024-10-05 12:38:00 | TERRA_M-T | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 135.8 |
| 33c26d30-75a0-36fb-b405-08caefca3e25 | -16.98379 | -56.75333 | 2024-10-05 12:38:00 | TERRA_M-T | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 122.2 |
| 694bc8e9-1410-35ba-82cb-acdf6350af4f | -16.97727 | -56.78647 | 2024-10-05 12:38:00 | TERRA_M-T | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 185.8 |
| 3cf0d2e7-589c-387b-9ed9-062096cd4a57 | -16.97474 | -56.74563 | 2024-10-05 12:38:00 | TERRA_M-T | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 76.3 |
| db0c5dd4-1a83-3699-8580-53d8357b628b | -16.96843 | -56.77878 | 2024-10-05 12:38:00 | TERRA_M-T | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 194.7 |
| 7ef394ff-c787-3185-89ec-2512a4a7a4c2 | -15.13754 | -47.07433 | 2024-10-05 12:38:00 | TERRA_M-T | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 30.8 |
| 85e66830-3ab2-3e27-b89d-a174c02f74de | -15.1362 | -47.08347 | 2024-10-05 12:38:00 | TERRA_M-T | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 66.4 |
| c40bbb49-1039-302b-a3ca-b7891ad0d70b | -14.77278 | -48.04273 | 2024-10-05 12:38:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 022ebeac-ab16-3acb-a9c1-bf4e281dad68 | -14.77136 | -48.05225 | 2024-10-05 12:38:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 410dc1af-bccb-3736-93c8-fb04b10ff5a2 | -14.38626 | -47.10727 | 2024-10-05 12:38:00 | TERRA_M-T | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 7.3 |
| a8ba9552-b051-35a4-911e-6bee2caaa6b8 | -14.38492 | -47.1164 | 2024-10-05 12:38:00 | TERRA_M-T | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 12.0 |
| faeae7bc-bd63-3fc2-af7b-ce3fcada4818 | -14.02974 | -47.27177 | 2024-10-05 12:38:00 | TERRA_M-T | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 5c42c7c9-b7ae-3bb5-8aba-90e2895decfd | -16.48166 | -47.52298 | 2024-10-05 12:38:00 | TERRA_M-T | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 19.0 |
| d4401a61-7d15-364d-90b2-5b2a8978402f | -16.24156 | -48.02461 | 2024-10-05 12:38:00 | TERRA_M-T | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 2264842a-fd3b-33b4-856b-706ca00ebab0 | -15.83576 | -47.96473 | 2024-10-05 12:38:00 | TERRA_M-T | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 5.5 |
| eef9bfaa-1ac0-3bbd-9d28-80b354c1cc2e | -15.6657 | -47.18218 | 2024-10-05 12:38:00 | TERRA_M-T | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 6e84e7a3-3747-3dae-95d2-13a193b7094f | -15.4366 | -47.42561 | 2024-10-05 12:38:00 | TERRA_M-T | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 42fcc88b-f792-3ba0-9269-e22d9b0dee8e | -15.42734 | -47.41816 | 2024-10-05 12:38:00 | TERRA_M-T | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 9859705a-9206-3a95-8846-3af80b0bc762 | -15.42231 | -47.70698 | 2024-10-05 12:38:00 | TERRA_M-T | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 37.8 |
| a7882bac-b2f8-3f41-b780-8f8d56257a9e | -15.42094 | -47.71627 | 2024-10-05 12:38:00 | TERRA_M-T | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 13.2 |
| b89cd8f1-13d4-354f-a572-3448973b0560 | -15.39172 | -47.41287 | 2024-10-05 12:38:00 | TERRA_M-T | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 27.5 |
| 8ceba2a3-43b1-369b-a881-1cda7ec3e80d | -15.25199 | -47.48871 | 2024-10-05 12:38:00 | TERRA_M-T | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 13aee027-3e49-3174-bec4-a3fb5f072499 | -15.22234 | -47.49699 | 2024-10-05 12:38:00 | TERRA_M-T | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 2f51efea-4912-32be-a339-a30734ba94ba | -15.19258 | -48.07183 | 2024-10-05 12:38:00 | TERRA_M-T | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 25.8 |
| 84d21175-80bf-3493-a65e-9ebb861d6fd6 | -15.18356 | -48.07035 | 2024-10-05 12:38:00 | TERRA_M-T | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 4c08e523-d131-38ff-aba9-d3e9ed7f653c | -15.17597 | -48.05944 | 2024-10-05 12:38:00 | TERRA_M-T | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 32.5 |
| a74581e3-487f-3071-bdf1-4f22a60e76f6 | -15.16694 | -48.05804 | 2024-10-05 12:38:00 | TERRA_M-T | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 29.9 |
| 34732769-e45d-3258-b3bf-74b4958186d5 | -15.1655 | -48.06752 | 2024-10-05 12:38:00 | TERRA_M-T | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 6444474a-53f7-3402-b7f0-59ad37195cd7 | -18.51291 | -48.25085 | 2024-10-05 12:38:00 | TERRA_M-T | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 9.9 |
| ae1e2603-ab5f-31c2-87d7-6483907fe493 | -18.51153 | -48.26022 | 2024-10-05 12:38:00 | TERRA_M-T | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 14.5 |
| a6bf7c52-afc9-3d6d-bba5-919474145052 | -14.5564 | -48.80484 | 2024-10-05 12:38:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 17.5 |
| e46819e8-be45-36c5-849d-e16cd957f238 | -13.28581 | -49.33529 | 2024-10-05 12:38:00 | TERRA_M-T | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 1fd3839e-b638-37da-b6d3-f9636c045f21 | -14.82214 | -48.81394 | 2024-10-05 12:38:00 | TERRA_M-T | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 50800988-817a-391b-a110-0208369f5333 | -14.82052 | -48.82455 | 2024-10-05 12:38:00 | TERRA_M-T | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 18.5 |
| f11bbf1f-f4f0-3acb-962a-72b6130d80d2 | -14.57849 | -48.82544 | 2024-10-05 12:38:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 23.9 |
| 6639a7c5-6f0e-337d-9083-126d1e94cb8d | -14.57361 | -49.29428 | 2024-10-05 12:38:00 | TERRA_M-T | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 17.3 |
| ce19cc1d-66d5-35b9-ae70-b7c1f3e616af | -14.5735 | -48.81822 | 2024-10-05 12:38:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 20.1 |
| 80932ba8-ba38-3ff3-8ed6-6c50031f2bc2 | -14.57199 | -49.30479 | 2024-10-05 12:38:00 | TERRA_M-T | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 26.8 |
| aafe9c7c-b655-3d3b-87e4-da7329b49374 | -14.57196 | -48.82837 | 2024-10-05 12:38:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 28.7 |
| 32f8e787-251b-31a6-b8b1-655b02b308a8 | -14.56241 | -49.30326 | 2024-10-05 12:38:00 | TERRA_M-T | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 92c8b4f0-aad7-35a5-bdd3-c97545acffc8 | -16.17269 | -49.25726 | 2024-10-05 12:38:00 | TERRA_M-T | PETROLINA DE GOIÁS | GOIÁS | Brasil | 5216809 | 52 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 932c9340-2559-363a-80a4-336d43bbce1e | -16.17109 | -49.26747 | 2024-10-05 12:38:00 | TERRA_M-T | PETROLINA DE GOIÁS | GOIÁS | Brasil | 5216809 | 52 | 33 | nan | nan | nan | Cerrado | 22.5 |
| 21dceb25-cc30-33c4-8d72-c5b4bb27992c | -16.16642 | -49.26041 | 2024-10-05 12:38:00 | TERRA_M-T | PETROLINA DE GOIÁS | GOIÁS | Brasil | 5216809 | 52 | 33 | nan | nan | nan | Cerrado | 9.1 |
| c6f4c159-f067-3544-8aba-6f89d9cde67b | -16.08714 | -50.2388 | 2024-10-05 12:38:00 | TERRA_M-T | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 10.4 |
| b1ee3df7-6274-3e92-9c53-a84d1513b518 | -17.8109 | -49.90144 | 2024-10-05 12:38:00 | TERRA_M-T | GOIATUBA | GOIÁS | Brasil | 5209101 | 52 | 33 | nan | nan | nan | Cerrado | 68.5 |
| 15c92378-63bd-3ed0-b54e-5c90a1e31fba | -17.80923 | -49.91216 | 2024-10-05 12:38:00 | TERRA_M-T | GOIATUBA | GOIÁS | Brasil | 5209101 | 52 | 33 | nan | nan | nan | Cerrado | 91.5 |
| 029f93e1-b126-3b5c-8691-98af1c9307e6 | -12.78618 | -50.55751 | 2024-10-05 12:38:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 26.3 |
| 2e7b437d-42fd-3469-8c5d-c6041eb4dc5d | -15.63544 | -40.77605 | 2024-10-05 12:38:00 | TERRA_M-T | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 24.4 |
| 0027e1f1-bc1a-35f5-bd69-ecdc587cb9de | -15.2617 | -40.5257 | 2024-10-05 12:38:00 | TERRA_M-T | ITAMBÉ | BAHIA | Brasil | 2915809 | 29 | 33 | nan | nan | nan | Mata Atlântica | 17.4 |
| 62ad4701-e00b-311f-ab78-67a1dc518671 | -14.78916 | -41.2868 | 2024-10-05 12:38:00 | TERRA_M-T | CARAÍBAS | BAHIA | Brasil | 2906899 | 29 | 33 | nan | nan | nan | Caatinga | 17.4 |
| d677d13e-a81f-3a7c-9e4e-bf67cf5059e0 | -14.7859 | -41.275 | 2024-10-05 12:38:00 | TERRA_M-T | CARAÍBAS | BAHIA | Brasil | 2906899 | 29 | 33 | nan | nan | nan | Caatinga | 16.4 |
| 33becc4b-42f9-3092-9a44-a1d20cf25e63 | -14.78391 | -41.29206 | 2024-10-05 12:38:00 | TERRA_M-T | CARAÍBAS | BAHIA | Brasil | 2906899 | 29 | 33 | nan | nan | nan | Caatinga | 22.1 |
| d019cace-7016-3b7c-bd24-5079b0531238 | -14.49935 | -40.9184 | 2024-10-05 12:38:00 | TERRA_M-T | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 30.8 |
| 241330de-ce18-34e4-9167-53e1ea1f4e39 | -14.46049 | -40.68659 | 2024-10-05 12:38:00 | TERRA_M-T | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 28.9 |
| a630929c-2091-34df-87e8-1b271710d1b1 | -13.78232 | -41.83447 | 2024-10-05 12:38:00 | TERRA_M-T | DOM BASÍLIO | BAHIA | Brasil | 2910107 | 29 | 33 | nan | nan | nan | Caatinga | 32.5 |
| f4a26f22-3570-3a55-a752-ec4f85c83c78 | -16.37307 | -41.75051 | 2024-10-05 12:38:00 | TERRA_M-T | COMERCINHO | MINAS GERAIS | Brasil | 3117009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 19.8 |
| 127dc685-b1ad-3c8f-80ef-24e611835baf | -16.36557 | -41.74384 | 2024-10-05 12:38:00 | TERRA_M-T | COMERCINHO | MINAS GERAIS | Brasil | 3117009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.7 |
| 520b6cf3-3840-3404-9bb3-d43e95d2283f | -15.7545 | -41.1039 | 2024-10-05 12:38:00 | TERRA_M-T | DIVISÓPOLIS | MINAS GERAIS | Brasil | 3122454 | 31 | 33 | nan | nan | nan | Mata Atlântica | 40.1 |
| 1493a17d-217d-367e-a0e7-9f955422f844 | -16.81584 | -41.89494 | 2024-10-05 12:38:00 | TERRA_M-T | ARAÇUAÍ | MINAS GERAIS | Brasil | 3103405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 25.9 |
| 52e7b9a0-689d-3520-82b3-5e4d413d1264 | -13.28541 | -42.34459 | 2024-10-05 12:38:00 | TERRA_M-T | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 18.2 |
| 8ae2d6dd-22fd-3681-ad3c-64cf2e93a568 | -13.28142 | -42.33755 | 2024-10-05 12:38:00 | TERRA_M-T | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 18.3 |
| c5d04fec-9bc8-3588-842b-7e1f85ad9589 | -13.27965 | -42.35101 | 2024-10-05 12:38:00 | TERRA_M-T | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 13.5 |
| bd3d1968-4ac7-3377-b828-3b0b29f61fb6 | -13.27476 | -42.34325 | 2024-10-05 12:38:00 | TERRA_M-T | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 12.7 |
| ca4f26c1-5edf-3531-a41d-4d9099a835d0 | -14.20856 | -42.17002 | 2024-10-05 12:38:00 | TERRA_M-T | RIO DO ANTÔNIO | BAHIA | Brasil | 2926806 | 29 | 33 | nan | nan | nan | Caatinga | 17.9 |
| 57ed2e76-7600-349b-a2b4-bbd5672b2b17 | -15.78024 | -43.87321 | 2024-10-05 12:38:00 | TERRA_M-T | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Caatinga | 9.6 |
| 87cf3374-0419-3f24-abb3-eaeb51c54967 | -16.24721 | -43.08274 | 2024-10-05 12:38:00 | TERRA_M-T | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 11.8 |
| a93649ff-cc46-3576-8457-93934a79dc21 | -16.01147 | -43.25003 | 2024-10-05 12:38:00 | TERRA_M-T | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 22.5 |
| 857aa237-521c-3c22-8662-e446f6da5792 | -17.74192 | -43.82883 | 2024-10-05 12:38:00 | TERRA_M-T | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 13.3 |
| aa55236e-d01a-3bcd-9d9f-3a617dd0e7ed | -19.45614 | -44.12125 | 2024-10-05 12:38:00 | TERRA_M-T | PRUDENTE DE MORAIS | MINAS GERAIS | Brasil | 3153608 | 31 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 7d7dddb6-e4d2-3409-8909-b9cc68fea587 | -18.49884 | -44.28149 | 2024-10-05 12:38:00 | TERRA_M-T | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 9.8 |
| f63c6a40-7225-3271-9f48-f1bae9fd8fd0 | -18.18476 | -43.86761 | 2024-10-05 12:38:00 | TERRA_M-T | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 305dc706-5009-32d4-be8d-dfc838c5bcfe | -13.01596 | -44.76052 | 2024-10-05 12:38:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 4ae143bc-61b3-3c68-86a3-1746fafb9526 | -14.48882 | -44.95704 | 2024-10-05 12:38:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 6d7ba506-15f3-3547-a79e-8e591414fa7f | -14.48745 | -44.96693 | 2024-10-05 12:38:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 138d5600-e8c3-35f8-80d7-7d0e71086731 | -14.4796 | -44.95575 | 2024-10-05 12:38:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 2316572d-7c26-3e0e-aa9e-3df816c9cfc2 | -14.47823 | -44.9656 | 2024-10-05 12:38:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 28.7 |
| 5212b121-9c12-3f96-9ed2-eb4f7558dfd3 | -14.33109 | -44.69889 | 2024-10-05 12:38:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 20.0 |
| bedd30ce-3a79-3af3-a9b0-776e53764d1d | -14.3297 | -44.70898 | 2024-10-05 12:38:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 14.2 |
| cde4034d-81e1-3a35-aa9d-03b78aa42dba | -14.06856 | -45.13139 | 2024-10-05 12:38:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 35.6 |
| 367d9b56-358d-31a7-a8cf-06f73e692568 | -14.06054 | -45.18915 | 2024-10-05 12:38:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 72.6 |
| 114b436d-5005-3a39-b316-7378ef2a81dc | -14.05811 | -45.13968 | 2024-10-05 12:38:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 40.8 |
| bc28e29a-f93a-3b66-8eb2-69b188523bdc | -14.05677 | -45.14933 | 2024-10-05 12:38:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 24.2 |
| 9f1f36dd-dc9e-3218-be36-bf5ea07b047f | -14.05143 | -45.18781 | 2024-10-05 12:38:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 26.7 |
| 387baf0b-8ac4-35f8-8b66-539143b53a45 | -14.0134 | -45.06798 | 2024-10-05 12:38:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 8020bade-2f04-3201-8886-280119e818f4 | -13.95939 | -44.05617 | 2024-10-05 12:38:00 | TERRA_M-T | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 10.1 |
| a0f95d27-79ca-3529-8f29-5a193e966718 | -15.9932 | -45.44207 | 2024-10-05 12:38:00 | TERRA_M-T | URUCUIA | MINAS GERAIS | Brasil | 3170529 | 31 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 1c910e5d-1308-34ba-944f-2538154c54ff | -17.43279 | -44.94058 | 2024-10-05 12:38:00 | TERRA_M-T | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 24.8 |
| 02b981e6-90bb-3bfa-89d1-e68048741710 | -17.42244 | -45.1291 | 2024-10-05 12:38:00 | TERRA_M-T | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 31.1 |
| c8d37627-eb4d-3701-b01a-a7257d31386e | -19.29951 | -46.21132 | 2024-10-05 12:38:00 | TERRA_M-T | RIO PARANAÍBA | MINAS GERAIS | Brasil | 3155504 | 31 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 059fd8bc-806e-3a01-a538-e6a630e9dfbb | -19.29818 | -46.22121 | 2024-10-05 12:38:00 | TERRA_M-T | RIO PARANAÍBA | MINAS GERAIS | Brasil | 3155504 | 31 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 909f728c-8257-3aee-a0cc-cefdede54740 | -18.9936 | -46.30276 | 2024-10-05 12:38:00 | TERRA_M-T | CARMO DO PARANAÍBA | MINAS GERAIS | Brasil | 3114303 | 31 | 33 | nan | nan | nan | Cerrado | 7.4 |
| a4e81da9-cf99-3e31-8163-a2db598622d0 | -18.98449 | -46.30141 | 2024-10-05 12:38:00 | TERRA_M-T | CARMO DO PARANAÍBA | MINAS GERAIS | Brasil | 3114303 | 31 | 33 | nan | nan | nan | Cerrado | 21.5 |
| 17b6f705-6b57-3baa-b63b-8b70a4fa821b | -18.3477 | -45.07181 | 2024-10-05 12:38:00 | TERRA_M-T | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 7.4 |


[Clique aqui para ver as próximas entradas](README162.md)
