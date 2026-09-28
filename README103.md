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

## Dados Diários - Página 103

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0e61dea1-3e71-356b-b6eb-4b3516ac988d | -14.83403 | -51.84633 | 2026-09-28 16:24:00 | NOAA-20 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| f7d24959-d3f4-389c-9ac3-e8a6d95b87f0 | -12.89595 | -47.13898 | 2026-09-28 16:24:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| ca31d012-819d-3292-8eb8-9d1eeed8dfc1 | -13.69638 | -48.81844 | 2026-09-28 16:24:00 | NOAA-20 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 3b74fd32-6070-3895-8469-70b7f8ce0b34 | -15.08648 | -54.62183 | 2026-09-28 16:24:00 | NOAA-20 | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 1b5ff0c9-9475-3d86-805b-6d023165a575 | -11.71247 | -44.52357 | 2026-09-28 16:24:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 34.0 |
| 2a759378-3856-3394-adfc-228396c1ab3b | -11.38811 | -43.43024 | 2026-09-28 16:24:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 2e7d4556-7722-3589-bd6b-495e94302d3f | -11.26355 | -43.53383 | 2026-09-28 16:24:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 21.1 |
| 53b74974-cec6-3c26-b30f-95a1b3d9e75e | -15.10273 | -54.71945 | 2026-09-28 16:24:00 | NOAA-20 | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 23.5 |
| 24758e38-a937-3d1b-b4d9-ab514c94f1ac | -15.26905 | -47.62512 | 2026-09-28 16:24:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 8a2c8738-daab-3f00-8e58-bd0b27fd623e | -12.75617 | -47.3468 | 2026-09-28 16:24:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 7e3c217b-0f79-31c9-af81-d8336b05d40e | -11.8694 | -47.08821 | 2026-09-28 16:24:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 21.3 |
| 096dbf78-2117-3418-93cb-2d78539d8710 | -12.73389 | -47.27831 | 2026-09-28 16:24:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 7fafe899-ff46-320b-9c5a-147d9aef0600 | -14.32755 | -44.8182 | 2026-09-28 16:24:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 1301f775-6a34-3d7d-baff-4f624be264fa | -11.35599 | -43.40084 | 2026-09-28 16:24:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 35.4 |
| e9a53fa6-1c6d-3613-96c7-d9dc9da0ff4d | -13.0794 | -47.41627 | 2026-09-28 16:24:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| aa18ad66-dbb2-32f3-92b8-1cc6cd4ba9bf | -12.69779 | -47.33378 | 2026-09-28 16:24:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 20.4 |
| 03e58611-6bf8-34cd-a82d-8de27ef798b7 | -15.71157 | -41.89006 | 2026-09-28 16:24:00 | NOAA-20 | BERIZAL | MINAS GERAIS | Brasil | 3106655 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| de64a077-356b-3a76-ae80-a83c620cf251 | -14.33066 | -44.81311 | 2026-09-28 16:24:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 12.1 |
| d2796ac0-cd2d-3661-bf99-3adf1afdf161 | -12.70767 | -40.55439 | 2026-09-28 16:24:00 | NOAA-20 | BOA VISTA DO TUPIM | BAHIA | Brasil | 2903805 | 29 | 33 | nan | nan | nan | Caatinga | 10.7 |
| a50b3f66-a79e-3506-a72c-50e91afcf1f8 | -12.16686 | -50.4155 | 2026-09-28 16:24:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 5f0b3f4c-595d-36b4-9b0a-786fe582c899 | -13.92354 | -47.8552 | 2026-09-28 16:24:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 6836a428-cc6f-3f78-b5a8-acbf79dd2562 | -12.14513 | -50.36914 | 2026-09-28 16:24:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| f114efc7-ebed-368f-b967-3b4a65a706ce | -14.51072 | -52.48544 | 2026-09-28 16:24:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 545e6e14-b7c1-36af-8bc3-65dca19236af | -16.35262 | -42.5775 | 2026-09-28 16:24:00 | NOAA-20 | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 17.8 |
| ed341907-50a7-3c95-828b-04744866c565 | -15.68495 | -47.59319 | 2026-09-28 16:24:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 27.0 |
| 1efc6a69-a957-3af7-8a1e-598d1481fbbb | -11.87507 | -47.09914 | 2026-09-28 16:24:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 21.1 |
| 623c7141-3dde-3d07-8093-c7143445c5d6 | -12.14313 | -50.35311 | 2026-09-28 16:24:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 19bef971-6dac-33e4-be30-737a26f01683 | -13.36149 | -43.34728 | 2026-09-28 16:24:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 12.1 |
| 10de6476-c197-3a53-b869-40017b5a22d0 | -15.03903 | -49.59387 | 2026-09-28 16:24:00 | NOAA-20 | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 5c838b1d-3afa-3065-bab1-ed0367bc9779 | -12.75521 | -47.35183 | 2026-09-28 16:24:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 19.7 |
| 7c1b33ca-181d-3d1d-9b4d-1688db6bcdab | -15.03351 | -49.59131 | 2026-09-28 16:24:00 | NOAA-20 | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 9db436d2-1e24-3286-b3c9-88400e1d1123 | -11.62252 | -46.78632 | 2026-09-28 16:24:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 984f68cf-d093-33b6-87b7-24402772b29b | -13.45469 | -48.58901 | 2026-09-28 16:24:00 | NOAA-20 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 7.7 |
| e3d2a6ed-3a58-32e1-989f-5703904e634d | -15.47546 | -46.13491 | 2026-09-28 16:24:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 8ed7900e-caaf-3310-b4f2-bfe7e93ab3ee | -12.64828 | -39.83682 | 2026-09-28 16:24:00 | NOAA-20 | IAÇU | BAHIA | Brasil | 2911907 | 29 | 33 | nan | nan | nan | Caatinga | 93.9 |
| 9cc6bc47-4897-3d7c-b92d-0125ac0266cf | -15.65411 | -52.686 | 2026-09-28 16:24:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 0265db23-0ada-3f4d-b2d6-d0e3584d723e | -11.54033 | -47.37025 | 2026-09-28 16:24:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| c8e8cf55-5802-3aa5-b2df-e2e8633d2155 | -11.90229 | -47.01756 | 2026-09-28 16:24:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 20.8 |
| aa9fd53b-846c-3095-a3e5-7c083692b8ba | -13.96996 | -54.01151 | 2026-09-28 16:24:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 13.2 |
| fc0732e2-7e79-3960-8ad1-f252c976fd83 | -11.12369 | -42.17516 | 2026-09-28 16:24:00 | NOAA-20 | CENTRAL | BAHIA | Brasil | 2907608 | 29 | 33 | nan | nan | nan | Caatinga | 7.3 |
| b069b41a-ecce-3934-9b27-3389fd017aba | -15.18657 | -46.17091 | 2026-09-28 16:24:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 66c799ad-28f5-341b-8ca0-90d7e2e18056 | -15.4102 | -47.8972 | 2026-09-28 16:24:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 42538533-4b6a-34dc-be0a-d0459a63428c | -12.75212 | -47.29349 | 2026-09-28 16:24:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 74d4aa08-663e-33ea-aa91-932a79b0b32b | -14.32628 | -44.80901 | 2026-09-28 16:24:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 19cbc62d-8e90-31fe-bc18-61a2f1211366 | -11.71069 | -44.53646 | 2026-09-28 16:24:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 19.0 |
| b72ae593-a50a-314c-b14c-52025d2468bf | -16.516 | -42.45072 | 2026-09-28 16:24:00 | NOAA-20 | VIRGEM DA LAPA | MINAS GERAIS | Brasil | 3171600 | 31 | 33 | nan | nan | nan | Cerrado | 20.0 |
| 41c2456d-2014-33a2-956c-0c609a39497f | -13.30796 | -47.26637 | 2026-09-28 16:24:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 39ef48ca-2e75-33da-95be-3d5ba177fed9 | -11.45096 | -44.93584 | 2026-09-28 16:24:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| bd07d15b-7685-31e6-ab3f-13c377ecc8c4 | -15.21103 | -46.17452 | 2026-09-28 16:24:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 7f1d686d-d147-31c0-82b7-213a5798b962 | -12.07539 | -48.54769 | 2026-09-28 16:24:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 424.5 |
| c47bbef4-fe6c-3f39-9c03-0bca249f316d | -11.21469 | -44.77409 | 2026-09-28 16:24:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 20.9 |
| 8f284270-2b44-3539-8c42-2747c8cb0ecd | -15.67161 | -50.22068 | 2026-09-28 16:24:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 4b55ec90-4aa4-39cc-82bd-6fcad18196d7 | -14.55507 | -40.75753 | 2026-09-28 16:24:00 | NOAA-20 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| c7364194-7bb1-3da9-bdca-c682c502d1f6 | -11.90386 | -49.9858 | 2026-09-28 16:24:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 4e1a7f6b-b2f2-39e0-adde-ac687f94b82e | -11.45255 | -44.91523 | 2026-09-28 16:24:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 25.9 |
| 13f52eff-cc36-384d-943a-e455e9b21e6d | -12.75377 | -47.29686 | 2026-09-28 16:24:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 3b4a4220-a607-3896-97c7-58f450cbe07d | -13.44438 | -48.62262 | 2026-09-28 16:24:00 | NOAA-20 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 10.0 |
| c5d5c3cb-b4bf-31a9-8864-a0bb47acdda6 | -11.85943 | -47.10918 | 2026-09-28 16:24:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 27f8102d-7184-39c0-ba0b-2cf71d9ed608 | -12.39679 | -50.24017 | 2026-09-28 16:24:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 3c089c07-7ff8-3ebb-8268-8bcca566ea7f | -11.90424 | -49.9888 | 2026-09-28 16:24:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 13.3 |
| c1ecea27-2aac-3736-9c05-3e7f4bdc513b | -11.38593 | -43.41537 | 2026-09-28 16:24:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 9.7 |
| be91b203-192d-38e3-8cd7-c0d7ae610508 | -12.74416 | -50.67956 | 2026-09-28 16:24:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 38e1ab36-61bc-36f4-a6cf-c49200219f78 | -14.39194 | -40.47072 | 2026-09-28 16:24:00 | NOAA-20 | BOM JESUS DA SERRA | BAHIA | Brasil | 2903953 | 29 | 33 | nan | nan | nan | Caatinga | 13.7 |
| 23a5ef61-300b-382f-8a61-d7e85eac4c19 | -12.75528 | -47.31823 | 2026-09-28 16:24:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| a2df501a-9664-3354-beec-60e626002fe9 | -12.83324 | -40.97018 | 2026-09-28 16:24:00 | NOAA-20 | BOA VISTA DO TUPIM | BAHIA | Brasil | 2903805 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| c45b3eb4-ce00-351e-938a-5b97ab442584 | -15.1889 | -46.13175 | 2026-09-28 16:24:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 13.8 |
| a97a6834-a491-3d23-86eb-50f60dbd7dd9 | -12.65206 | -47.24926 | 2026-09-28 16:24:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 7f7a0b4d-b4ba-36b9-b22d-1892fffa3bca | -11.41821 | -44.96616 | 2026-09-28 16:24:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| bd6f8412-eaeb-3746-9253-46bbb76ec7c6 | -14.53935 | -48.31182 | 2026-09-28 16:24:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 0d7c3aec-4a3e-304f-85e9-d8da38f28d5c | -14.52847 | -41.1623 | 2026-09-28 16:24:00 | NOAA-20 | CARAÍBAS | BAHIA | Brasil | 2906899 | 29 | 33 | nan | nan | nan | Caatinga | 60.2 |
| a110f6a7-8a37-3d87-9cc1-438aa35b1cd4 | -15.0469 | -48.56899 | 2026-09-28 16:24:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 9bd9d09a-7b77-3dbb-8ad9-368fb8190978 | -15.19591 | -46.1541 | 2026-09-28 16:24:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7cbc0124-f3d6-33bc-9299-e5b232d10e1b | -15.18098 | -46.16806 | 2026-09-28 16:24:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 58877f8b-e103-3caa-9af1-34d178167b63 | -15.07203 | -54.59569 | 2026-09-28 16:24:00 | NOAA-20 | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 114.1 |
| 7463d940-94e2-35ed-bfef-b00597e8f65b | -12.1073 | -45.22414 | 2026-09-28 16:24:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 9b931342-f613-3c24-bdad-d48972af7198 | -11.39551 | -45.40713 | 2026-09-28 16:24:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.9 |
| c82cc447-3d95-3815-b4b5-58fe0e5c02da | -13.49027 | -48.60579 | 2026-09-28 16:24:00 | NOAA-20 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 1b5bcb52-e9d9-3fe3-9118-b68b404f3e9e | -12.31897 | -46.41312 | 2026-09-28 16:24:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 9382a22c-ef9e-321d-9105-6251b43765cb | -13.87948 | -41.4685 | 2026-09-28 16:24:00 | NOAA-20 | ITUAÇU | BAHIA | Brasil | 2917201 | 29 | 33 | nan | nan | nan | Caatinga | 6.8 |
| decd98b3-2437-3b3f-88fa-75226f810725 | -15.93699 | -42.33575 | 2026-09-28 16:24:00 | NOAA-20 | SALINAS | MINAS GERAIS | Brasil | 3157005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 28.5 |
| 9f50b296-0bc7-3cf0-8ccc-172eb0f06451 | -16.9301 | -41.69305 | 2026-09-28 16:24:00 | NOAA-20 | ARAÇUAÍ | MINAS GERAIS | Brasil | 3103405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| 537c30b7-6a36-3d64-9354-5559f7c5c2c9 | -13.71688 | -48.82667 | 2026-09-28 16:24:00 | NOAA-20 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 9a5cfaeb-824a-3328-b99e-9efc7c93a694 | -15.68591 | -47.59095 | 2026-09-28 16:24:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 16.5 |
| e73c0fe3-820a-3384-87d8-320877dea4ee | -11.86259 | -47.10091 | 2026-09-28 16:24:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| c5ce17a1-6120-323c-9146-8f546035f4bf | -15.99067 | -48.41342 | 2026-09-28 16:24:00 | NOAA-20 | ALEXÂNIA | GOIÁS | Brasil | 5200308 | 52 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 95fd868b-97aa-3354-920a-25443ad36aaf | -17.26201 | -48.28416 | 2026-09-28 16:24:00 | NOAA-20 | PIRES DO RIO | GOIÁS | Brasil | 5217401 | 52 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 65ff9436-db76-38cd-b5ef-bc3c75b17af4 | -12.86489 | -44.80769 | 2026-09-28 16:24:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 8.7 |
| e2ee9397-4d4c-31fe-879d-a72d31d4cd92 | -11.37285 | -43.42111 | 2026-09-28 16:24:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 94643598-87cb-3e93-8f1f-58915aa62b86 | -13.47609 | -48.60746 | 2026-09-28 16:24:00 | NOAA-20 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 9.8 |
| c349a951-f589-3998-9017-821e3ddc900c | -11.90127 | -47.00993 | 2026-09-28 16:24:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 10.7 |
| e9fd2dc1-9ea0-3bd9-8c59-d90bc1df5569 | -16.90636 | -42.10174 | 2026-09-28 16:24:00 | NOAA-20 | ARAÇUAÍ | MINAS GERAIS | Brasil | 3103405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| ab81efd9-0f2b-3503-b728-eba2e5cf05a5 | -12.06859 | -46.47131 | 2026-09-28 16:24:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| ab46d801-14f5-3333-bc3d-18659a6a1d88 | -15.1626 | -46.14754 | 2026-09-28 16:24:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 5fecc96f-8de4-33a5-8091-4d6529b947a9 | -11.71103 | -43.46243 | 2026-09-28 16:24:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 31.0 |
| 7533036c-daf3-3a92-885b-a4cb39c4d238 | -13.56869 | -49.08361 | 2026-09-28 16:24:00 | NOAA-20 | MUTUNÓPOLIS | GOIÁS | Brasil | 5214101 | 52 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 452de434-2f14-3553-a2dd-67a81a3d16fd | -12.87711 | -44.81489 | 2026-09-28 16:24:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 41.5 |
| 759888b8-8573-3b52-8454-aa009632cddc | -11.22192 | -44.79854 | 2026-09-28 16:24:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 38.8 |
| b50f1cc1-8ea6-38d0-b32a-3ab8bbeef724 | -16.62973 | -48.47081 | 2026-09-28 16:24:00 | NOAA-20 | SILVÂNIA | GOIÁS | Brasil | 5220603 | 52 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 04ce243c-b9a0-36e0-890a-16250dfd2a50 | -14.3188 | -44.81 | 2026-09-28 16:24:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 47.9 |
| c3907579-f05a-3375-bbb4-252a688bc8b6 | -12.78704 | -54.02261 | 2026-09-28 16:24:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 128.0 |


[Clique aqui para ver as próximas entradas](README104.md)
