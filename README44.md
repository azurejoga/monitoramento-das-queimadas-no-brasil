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

## Dados Diários - Página 44

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bc33e8d6-dc38-3a62-b8ef-4a2391b28020 | -16.44916 | -42.4189 | 2026-09-02 04:59:00 | NPP-375D | RUBELITA | MINAS GERAIS | Brasil | 3156502 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a9ac4585-9dda-36e3-b90f-dbd8fac28183 | -16.82001 | -43.91603 | 2026-09-02 04:59:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 33c72b4c-4151-327c-8053-6f915e5c2ccd | -14.50457 | -59.84316 | 2026-09-02 04:59:00 | NPP-375D | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7d19275d-1fda-3505-b362-d973c5029849 | -14.99391 | -47.97881 | 2026-09-02 04:59:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0e5bcf5e-d455-3f07-8fde-824fc980414e | -14.96365 | -48.1135 | 2026-09-02 04:59:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 1a4038d9-77c7-3739-a5ce-573241338f37 | -17.0919 | -56.85558 | 2026-09-02 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 2a333af9-08dc-3df3-9086-a241c85b6a82 | -15.34357 | -47.04341 | 2026-09-02 04:59:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| d6c3a0ff-ad45-3421-b6f5-2d279b32d7f4 | -15.60278 | -46.58038 | 2026-09-02 04:59:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 6455fd7c-bd4b-3dd1-8472-1951d51b7142 | -15.36617 | -47.68943 | 2026-09-02 04:59:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c284ffd2-1ff5-35d8-b0d1-bb0596432f0e | -15.68011 | -45.89732 | 2026-09-02 04:59:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0c376e2e-88b5-3209-b6b2-77262c91872d | -14.96662 | -48.11194 | 2026-09-02 04:59:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1db575cb-8492-3ea4-9a48-365c77bdd9c3 | -15.66201 | -47.26358 | 2026-09-02 04:59:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ac8a8ccc-9fc0-316a-9862-83a1c06bf29d | -16.72816 | -47.08636 | 2026-09-02 04:59:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 656b4d2e-5628-3f35-836b-89977e88a214 | -15.33974 | -47.03901 | 2026-09-02 04:59:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 44ba88e8-800d-3165-8469-67b4bd43455f | -15.66256 | -47.25946 | 2026-09-02 04:59:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6cd40823-c503-35cc-b10e-ad17c034e1ef | -15.36187 | -47.03799 | 2026-09-02 04:59:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 20dfb477-9f74-36a3-a8d9-5fc5eef06cbf | -16.16572 | -46.6759 | 2026-09-02 04:59:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ba7527d6-0aba-3cbb-b80f-9dfa7ab530e3 | -14.98661 | -48.03357 | 2026-09-02 04:59:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4cbe617c-a45b-3248-9a93-508caf9655fe | -15.64497 | -46.81527 | 2026-09-02 04:59:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b79aa6f1-35c4-3f88-99cf-ca885ee7fdfc | -17.08467 | -56.85421 | 2026-09-02 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 70f78c01-d6c0-3101-a714-70e6242d4c8e | -15.35705 | -47.04126 | 2026-09-02 04:59:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 42f886b2-a1a5-3b80-aaae-bcd0f94cfdd9 | -15.67795 | -45.89333 | 2026-09-02 04:59:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| f9289a33-d379-307d-ad69-b0a43bde42e8 | -15.17752 | -46.22688 | 2026-09-02 04:59:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7d7e5f15-e4cd-3417-ad99-4df9a03af36a | -16.15555 | -46.64812 | 2026-09-02 04:59:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 5ccd55a1-6bb6-330b-96e9-80d39c760277 | -15.35656 | -47.04499 | 2026-09-02 04:59:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e57037cc-6756-3c34-889f-fd90510c2c3b | -14.96733 | -48.10683 | 2026-09-02 04:59:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| e019f8b8-10d5-31e9-af81-5dddc4781327 | -15.17812 | -46.22216 | 2026-09-02 04:59:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 79031db3-f7f9-3860-aea4-45a7f5bbdf31 | -16.73366 | -47.0782 | 2026-09-02 04:59:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3326840a-dd91-336a-ad02-508ad6e86109 | -14.96833 | -48.10907 | 2026-09-02 04:59:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| b9c6aab4-5c89-39bc-8802-e811b30d14ed | -15.37176 | -47.67901 | 2026-09-02 04:59:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 435fd422-7d37-3276-8019-d5bec1555e94 | -16.14712 | -46.64257 | 2026-09-02 04:59:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c7b0598f-549f-35e3-8320-7547128df053 | -15.64922 | -45.91529 | 2026-09-02 04:59:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 55357068-e653-3226-a24a-8426bf692dbb | -16.22709 | -43.63815 | 2026-09-02 04:59:00 | NPP-375D | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d3b7feec-f7cf-324c-99d8-b2db2df394db | -17.67922 | -40.13705 | 2026-09-02 04:59:00 | NPP-375D | IBIRAPUÃ | BAHIA | Brasil | 2912806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| 6217893f-088d-3297-a126-802c0ce4dfef | -15.66652 | -45.94859 | 2026-09-02 04:59:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ce2225e0-c603-353f-ae55-e63885abb9a0 | -14.53257 | -51.96915 | 2026-09-02 04:59:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 380f9008-ae6e-31a4-b361-89482ea9dd1e | -14.96263 | -48.11125 | 2026-09-02 04:59:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| cccb25de-7be2-3322-8dbd-b2090b8c40dc | -15.17288 | -46.22686 | 2026-09-02 04:59:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7ca93ee1-646b-35b2-9d18-f7238c280f3b | -17.08543 | -56.84988 | 2026-09-02 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 1e15e6b0-7c03-32ae-a991-b6faed382403 | -16.14767 | -46.63816 | 2026-09-02 04:59:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f80c8aa1-ccb9-320d-9e38-f48e8bf62c7a | -15.17873 | -46.2175 | 2026-09-02 04:59:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f5049edb-d203-3f59-b3f3-e917f81fd7e5 | -15.3662 | -47.03855 | 2026-09-02 04:59:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 38e936d5-454b-3da4-83e9-ab548a959fbc | -15.64929 | -46.81647 | 2026-09-02 04:59:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2956bd65-06c2-3690-a901-6f0e947a3905 | -11.89103 | -63.18715 | 2026-09-02 04:59:00 | NPP-375D | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c0741c27-6acf-3381-ba7b-640396637ac7 | -16.73091 | -47.06447 | 2026-09-02 04:59:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3d2bd2d3-c701-3bed-b503-234120782ccc | -11.89189 | -63.18286 | 2026-09-02 04:59:00 | NPP-375D | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d73070d1-bdd9-37b5-b9e2-94a7471c0ebe | -14.69448 | -53.60227 | 2026-09-02 04:59:00 | NPP-375D | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 19da5be3-79a0-362a-a630-d2bf99f77d65 | -15.67855 | -45.88838 | 2026-09-02 04:59:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8ed6c881-c62b-37b9-a7bf-e69c9c492eae | -14.98614 | -48.03702 | 2026-09-02 04:59:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 35f3e64f-cb81-3146-a0d8-1359c3f85c85 | -15.3759 | -47.67962 | 2026-09-02 04:59:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c3b06c1f-623a-3d15-aecf-9410ff059574 | -15.34406 | -47.03964 | 2026-09-02 04:59:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 0ac88e6e-ec06-3b76-afc9-f8615cc5c05d | -17.67229 | -40.1365 | 2026-09-02 04:59:00 | NPP-375D | IBIRAPUÃ | BAHIA | Brasil | 2912806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 3fa4920f-5b53-366a-82be-24a5be7fea49 | -17.67172 | -40.14296 | 2026-09-02 04:59:00 | NPP-375D | IBIRAPUÃ | BAHIA | Brasil | 2912806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 504cf05a-afd4-3c12-845f-7c36f91cb4c0 | -13.97495 | -58.68359 | 2026-09-02 04:59:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c1e29617-a964-3f28-9772-5dcaaea70e60 | -14.9659 | -48.11706 | 2026-09-02 04:59:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a067a062-dfca-3231-9ebe-2a22588003d1 | -15.16233 | -47.28922 | 2026-09-02 04:59:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 95c5d882-16a5-3f68-a6b0-bc9a87432041 | -14.50006 | -59.84234 | 2026-09-02 04:59:00 | NPP-375D | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 958f7dad-248f-3942-8b8c-c5cf87d289ad | -16.14318 | -46.63756 | 2026-09-02 04:59:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 334a218e-0807-3914-9645-c3827702a57d | -17.08182 | -56.84921 | 2026-09-02 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 65c62e08-c7b6-363d-b138-e642688a46f8 | -15.36138 | -47.04175 | 2026-09-02 04:59:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 471c5167-8017-35af-b510-f2e11adf50d5 | -14.53593 | -51.9697 | 2026-09-02 04:59:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| df2fb8cf-db71-355a-a7a4-1093fba66caf | -14.50098 | -59.83747 | 2026-09-02 04:59:00 | NPP-375D | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 803dbb60-cf13-3d2e-ab1d-d3f959806fda | -13.55717 | -59.74949 | 2026-09-02 04:59:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 963bb9f1-b787-3b5f-b86f-ab3ff9c8f632 | -16.81462 | -43.91496 | 2026-09-02 04:59:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f53a075e-eeaa-3415-9d7f-69d19262af4b | -13.46761 | -57.03352 | 2026-09-02 04:59:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 435fd98a-8e82-3780-a099-3d7a98e4ef1f | -13.97916 | -58.6844 | 2026-09-02 04:59:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 08265197-d0af-3768-9225-66d619e4ea39 | -16.14657 | -46.64695 | 2026-09-02 04:59:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f29aff2d-0ee9-3c67-a809-67b6aa3523c2 | -15.34838 | -47.04021 | 2026-09-02 04:59:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| bc4df955-60dd-346f-8728-edd8535cddf4 | -16.73421 | -47.0738 | 2026-09-02 04:59:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5ffa6fcb-f109-34ad-9fc4-7774af410053 | -17.08619 | -56.84556 | 2026-09-02 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 89e9edaa-2dc7-33f0-a932-2232dd19f093 | -15.60335 | -46.57579 | 2026-09-02 04:59:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b05e88c9-169e-3e4f-88a2-bf77f4cc4026 | -15.35223 | -47.04448 | 2026-09-02 04:59:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 491431fb-81ba-30bf-9210-0da500a91ccb | -16.74854 | -47.03104 | 2026-09-02 04:59:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 9.1 |
| ef12cf43-da7e-37d8-b383-668a3ff193cc | -15.68414 | -45.90298 | 2026-09-02 04:59:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ee3321e8-0a5e-3bc7-83e8-ad56c6e248d8 | -16.2275 | -43.63449 | 2026-09-02 04:59:00 | NPP-375D | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c1c05e0a-8d82-3a28-93fa-97b3455a1507 | -16.15161 | -46.64318 | 2026-09-02 04:59:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 93d6a6e8-4a2d-3a9f-9c75-715bc01fa0f7 | -14.96696 | -48.11931 | 2026-09-02 04:59:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c51b9314-c241-3045-bfa5-34bd0bac3459 | -15.66359 | -45.95181 | 2026-09-02 04:59:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| eb331519-6c6f-3725-9006-9ef2f7d725f8 | -17.12562 | -55.93135 | 2026-09-02 04:59:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| a18a6b4b-cbca-3bd5-8faa-d8fd17a0701c | -16.73256 | -47.08697 | 2026-09-02 04:59:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6bf0fd96-59c5-3cbc-8dea-09fbde96b707 | -15.67606 | -45.89169 | 2026-09-02 04:59:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7e236234-6f71-385b-8ffe-229a941f1622 | -15.33924 | -47.04285 | 2026-09-02 04:59:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 26e7437f-91cc-3269-893f-59834b1a0e7d | -14.96434 | -48.10836 | 2026-09-02 04:59:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| ccf3defc-ec59-31b7-b120-346f8321f0ab | -15.17616 | -59.77892 | 2026-09-02 04:59:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 482aa997-af24-3631-9989-6154a3b848c1 | -15.64987 | -45.91019 | 2026-09-02 04:59:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a592891d-40f6-306c-bd8f-49e102fdaed4 | -8.4671 | -54.7035 | 2026-09-02 05:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 198.2 |
| 93dccacd-5d78-3a8a-96ed-01b5e704fae3 | -8.4485 | -54.7048 | 2026-09-02 05:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 75.2 |
| e0a8b422-3155-3054-8de4-84150b53261c | -8.4858 | -54.7023 | 2026-09-02 05:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 152.5 |
| c42cec80-a95a-36db-ba95-6c8634ba7626 | -8.4856 | -54.7225 | 2026-09-02 05:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 136.8 |
| 12f7ac90-2525-3a40-8457-8130e9ea83e8 | -3.2486 | -47.2438 | 2026-09-02 05:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 46.6 |
| bffb85d6-0529-378a-9ea2-fa48489c4aec | -8.4669 | -54.7237 | 2026-09-02 05:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 209.8 |
| ca613d89-2b81-3cd6-b901-a7c4f3a1e4b5 | -21.89627 | -55.37058 | 2026-09-02 05:01:00 | NPP-375D | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| aecd795d-1902-369a-ad93-a32d866a8d8c | -8.4485 | -54.7048 | 2026-09-02 05:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 86.3 |
| 16b615be-5646-30b5-b734-87bef6dab1f3 | -8.4671 | -54.7035 | 2026-09-02 05:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 292.7 |
| f60ee133-82e1-35ee-9fc4-1d5bef9c17d7 | -8.4858 | -54.7023 | 2026-09-02 05:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 172.6 |
| 056e3580-f212-387f-a337-fb723458154a | -8.4669 | -54.7237 | 2026-09-02 05:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 212.2 |
| 840d18f9-38d6-3e33-8dfb-6ea5f6458ead | -8.4483 | -54.725 | 2026-09-02 05:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 65.2 |
| c65ebc2a-4d7c-3b7a-8ccd-fb84c666b309 | -8.4856 | -54.7225 | 2026-09-02 05:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 120.6 |
| 5f0886cb-42f5-3600-8631-7226008bd9e2 | 3.28846 | -60.62477 | 2026-09-02 05:14:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2843c013-ac0d-3687-a463-34979214ca7e | 2.70231 | -60.09885 | 2026-09-02 05:14:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README45.md)
