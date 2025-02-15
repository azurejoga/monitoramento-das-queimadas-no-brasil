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
| 1092e557-41db-3cfb-b07c-f283370fbabd | -12.29492 | -40.11992 | 2025-02-15 03:55:00 | NOAA-21 | IPIRÁ | BAHIA | Brasil | 2914000 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 0ebafe8b-a18d-3966-9b11-b32fe8071fc3 | -8.33838 | -37.58595 | 2025-02-15 03:55:00 | NOAA-21 | SERTÂNIA | PERNAMBUCO | Brasil | 2614105 | 26 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 84217d1f-7706-3e7c-9b11-ed080c9f8ecb | -10.29698 | -36.77221 | 2025-02-15 03:55:00 | NOAA-21 | NEÓPOLIS | SERGIPE | Brasil | 2804409 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 66f8f5c2-9397-3d56-9290-49b04e1a636f | -10.60925 | -45.10165 | 2025-02-15 03:55:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 4f3c894e-0969-38e5-bc7f-9d182724fcf3 | -14.13592 | -41.69317 | 2025-02-15 03:55:00 | NOAA-21 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| af592af7-fe97-3c2c-ab98-56752180155f | -10.2964 | -36.77609 | 2025-02-15 03:55:00 | NOAA-21 | NEÓPOLIS | SERGIPE | Brasil | 2804409 | 28 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| 9c0d7dee-acd9-3764-b091-ab79c5c0476f | -11.88907 | -37.76989 | 2025-02-15 03:55:00 | NOAA-21 | ESPLANADA | BAHIA | Brasil | 2910602 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| d45c3bad-412f-3e24-9410-efe8e62cf1bd | -19.82707 | -40.10387 | 2025-02-15 03:57:00 | NOAA-21 | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 4dfa576c-8dbf-372c-a924-c004f6aabeca | -16.68946 | -43.00855 | 2025-02-15 03:57:00 | NOAA-21 | BOTUMIRIM | MINAS GERAIS | Brasil | 3108503 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ff62a3c5-65a2-35ff-9009-2bb31c7ab33f | -20.43667 | -42.95686 | 2025-02-15 03:57:00 | NOAA-21 | PONTE NOVA | MINAS GERAIS | Brasil | 3152105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| c46d0937-54db-3666-acf9-7693eef8e8a7 | -20.33977 | -45.7617 | 2025-02-15 03:57:00 | NOAA-21 | PAINS | MINAS GERAIS | Brasil | 3146503 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4e8ad2d2-118e-3b86-b8cc-fee8d0bfc03b | -16.99321 | -42.8321 | 2025-02-15 03:57:00 | NOAA-21 | BOTUMIRIM | MINAS GERAIS | Brasil | 3108503 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bac330d0-5074-3ee7-8863-17f3bff92ba8 | -15.5568 | -46.28312 | 2025-02-15 03:57:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dba9f3d5-4290-3dad-8612-3cb92d17ae21 | -20.33603 | -45.76094 | 2025-02-15 03:57:00 | NOAA-21 | PAINS | MINAS GERAIS | Brasil | 3146503 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 396a2637-990e-3af2-82f0-abe1260d103c | -18.04478 | -43.23349 | 2025-02-15 03:57:00 | NOAA-21 | FELÍCIO DOS SANTOS | MINAS GERAIS | Brasil | 3125408 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8f42eb77-efc1-3273-ac3f-3fa4669d3a05 | -15.46848 | -42.14508 | 2025-02-15 03:57:00 | NOAA-21 | INDAIABIRA | MINAS GERAIS | Brasil | 3130655 | 31 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 7582c851-f6cc-3cc1-9fe3-f337a237167e | -22.6994 | -42.28504 | 2025-02-15 03:57:00 | NOAA-21 | ARARUAMA | RIO DE JANEIRO | Brasil | 3300209 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 4d176005-e59e-3771-a2c7-c4d87c1e4f00 | -20.31227 | -45.5857 | 2025-02-15 03:57:00 | NOAA-21 | ARCOS | MINAS GERAIS | Brasil | 3104205 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bcc164b5-35f2-354a-8db3-4c1f945f496b | -18.9056 | -45.04069 | 2025-02-15 03:57:00 | NOAA-21 | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 266d4849-8b3c-3996-ad37-ea93ccbe34ae | -19.74848 | -40.11076 | 2025-02-15 03:57:00 | NOAA-21 | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| df29912d-76fa-3ab4-ae05-b7d13ffaa118 | -19.74792 | -40.11452 | 2025-02-15 03:57:00 | NOAA-21 | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 07d6b831-753c-3063-8dcf-ee0046b7e5bb | -17.37884 | -42.48311 | 2025-02-15 03:57:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 70640da1-24ba-3307-847c-bf18c8a89497 | -21.62638 | -43.46797 | 2025-02-15 03:57:00 | NOAA-21 | JUIZ DE FORA | MINAS GERAIS | Brasil | 3136702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 0f26c033-7b8c-3255-93d7-b68aa6811736 | -14.47137 | -45.82188 | 2025-02-15 03:57:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 96eddd6e-b4c1-3e56-a274-edaaff1bb886 | -19.82763 | -40.1001 | 2025-02-15 03:57:00 | NOAA-21 | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| e1e06714-f0aa-3d59-a56d-358db23ef1ad | -14.2164 | -47.02036 | 2025-02-15 03:57:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6476e86a-481d-37b0-bf37-61fe3b93ad75 | -19.99599 | -46.5092 | 2025-02-15 03:57:00 | NOAA-21 | MEDEIROS | MINAS GERAIS | Brasil | 3141306 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a53096fc-70a1-3362-829a-6e00702a6292 | -21.06822 | -43.8794 | 2025-02-15 03:57:00 | NOAA-21 | CARANDAÍ | MINAS GERAIS | Brasil | 3113206 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| f666f6e3-739c-39fe-93ca-1fa0e0e4385d | -22.69609 | -42.28444 | 2025-02-15 03:57:00 | NOAA-21 | ARARUAMA | RIO DE JANEIRO | Brasil | 3300209 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| ead0c353-996d-310a-b93f-723302cd78a2 | -19.2074 | -40.09624 | 2025-02-15 03:57:00 | NOAA-21 | SOORETAMA | ESPÍRITO SANTO | Brasil | 3205010 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 17cabe9d-98bc-34d0-9671-50ea55987310 | -20.79428 | -41.1273 | 2025-02-15 03:57:00 | NOAA-21 | CACHOEIRO DE ITAPEMIRIM | ESPÍRITO SANTO | Brasil | 3201209 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| e8f6c389-d584-3ea3-9b2f-8ee96484edce | -20.52705 | -42.16396 | 2025-02-15 03:57:00 | NOAA-21 | DIVINO | MINAS GERAIS | Brasil | 3122009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 6f428aaf-d810-368c-a47c-cfcc18a2333d | -15.56942 | -47.856 | 2025-02-15 03:57:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2f491681-81f8-3133-ab6f-1150932d829b | -22.69882 | -42.28877 | 2025-02-15 03:57:00 | NOAA-21 | ARARUAMA | RIO DE JANEIRO | Brasil | 3300209 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| b2a65664-70e8-3689-a598-380e470500e6 | -25.20777 | -50.58206 | 2025-02-15 03:59:00 | NOAA-21 | IMBITUVA | PARANÁ | Brasil | 4110102 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| fea2967e-ef2f-3626-8388-e49b6d803eb2 | -23.40435 | -46.55537 | 2025-02-15 03:59:00 | NOAA-21 | GUARULHOS | SÃO PAULO | Brasil | 3518800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| e553e12e-2281-3bf9-8ab0-760b1a24f0ab | -23.40807 | -46.55626 | 2025-02-15 03:59:00 | NOAA-21 | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 9c702f47-c21c-3f84-a8c2-18f30d73d317 | -22.80618 | -41.97053 | 2025-02-15 03:59:00 | NOAA-21 | ARMAÇÃO DOS BÚZIOS | RIO DE JANEIRO | Brasil | 3300233 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 737fb6ee-d9bb-3518-a2af-2ae932f4022e | -20.99672 | -51.79277 | 2025-02-15 03:59:00 | NOAA-21 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| a81fca78-6732-3212-8913-cafeaae7c826 | -22.78517 | -43.75661 | 2025-02-15 03:59:00 | NOAA-21 | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| e2246222-dbdf-3ba7-b185-25021e54855d | -22.67705 | -42.8532 | 2025-02-15 03:59:00 | NOAA-21 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 74647640-ceb6-374b-920b-90d7852dc170 | -22.81545 | -47.15676 | 2025-02-15 03:59:00 | NOAA-21 | CAMPINAS | SÃO PAULO | Brasil | 3509502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 6054b054-9d8e-30d8-b005-0187c8ab9468 | -24.22564 | -50.90898 | 2025-02-15 03:59:00 | NOAA-21 | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 961a5726-d417-3caa-a6ba-147a58686bbe | -22.67644 | -42.85695 | 2025-02-15 03:59:00 | NOAA-21 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 97003f3b-975d-3e86-842c-300cbc218092 | -22.79006 | -41.9868 | 2025-02-15 03:59:00 | NOAA-21 | ARMAÇÃO DOS BÚZIOS | RIO DE JANEIRO | Brasil | 3300233 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| db1e7877-266a-321e-b950-4ceae787968e | -7.38555 | -42.78873 | 2025-02-15 04:21:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| dfc6166a-52f5-30f1-8ff3-15adde29261c | -7.38207 | -42.7882 | 2025-02-15 04:21:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 199aa8cd-73fd-305d-95b8-4868cc514c00 | -8.13411 | -43.1414 | 2025-02-15 04:21:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| b2d852f2-a3ec-34a1-964f-e679b7b45311 | -3.23809 | -42.07642 | 2025-02-15 04:21:00 | NPP-375D | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2d681739-868e-39b9-a83a-cd299da666f1 | -8.13066 | -43.14088 | 2025-02-15 04:21:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| d97d83f6-fe31-3876-a000-ff952036d64e | -5.45804 | -36.90506 | 2025-02-15 04:21:00 | NPP-375D | AÇU | RIO GRANDE DO NORTE | Brasil | 2400208 | 24 | 33 | nan | nan | nan | Caatinga | 1.8 |
| f1703239-5a43-388c-b91d-f18763229cb9 | -7.28268 | -39.72792 | 2025-02-15 04:21:00 | NPP-375D | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 1b8d82f0-e220-3f83-862a-f2fc7123840b | -7.28453 | -39.72893 | 2025-02-15 04:21:00 | NPP-375D | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 1b7f280b-3249-353e-aa30-9b19fba7f0d7 | -7.28399 | -39.73257 | 2025-02-15 04:21:00 | NPP-375D | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 3364edf0-9c66-3f5f-9eb9-4fb15ac9b599 | -7.28217 | -39.73156 | 2025-02-15 04:21:00 | NPP-375D | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 0cc53d6d-e681-3f47-a548-1f867f5ff660 | -8.87889 | -38.13779 | 2025-02-15 04:21:00 | NPP-375D | TACARATU | PERNAMBUCO | Brasil | 2614808 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| a9d78f9d-af6c-39eb-aa65-31760cea91da | -19.82422 | -40.10132 | 2025-02-15 04:23:00 | NPP-375D | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 90c2c41d-9a1e-3bef-ba30-eb45c0f1a197 | -15.03068 | -43.38106 | 2025-02-15 04:23:00 | NPP-375D | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 8.3 |
| 53842ccc-a394-332d-845f-39641661f8b4 | -10.61289 | -45.10181 | 2025-02-15 04:23:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| f186fa93-6614-3e22-a348-6f91e5b74a23 | -20.33608 | -45.76159 | 2025-02-15 04:23:00 | NPP-375D | PAINS | MINAS GERAIS | Brasil | 3146503 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d565dd20-53a2-303c-ad30-dceeb3c733f7 | -12.33859 | -52.48191 | 2025-02-15 04:23:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 060945ba-df98-3c3b-bca2-af907111b881 | -12.26274 | -43.42995 | 2025-02-15 04:23:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 971737c3-62af-332b-a320-74016a3cc574 | -15.55517 | -46.28231 | 2025-02-15 04:23:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 419a8d53-7e84-32c3-8ed5-aec45309a79f | -11.56086 | -44.8548 | 2025-02-15 04:23:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 7a4fa8a2-ae9c-3882-bfcb-9a1dffe16fe7 | -9.98543 | -48.08408 | 2025-02-15 04:23:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 33e09115-19b6-3123-9f1c-8630f3b3ddf6 | -22.67448 | -42.85272 | 2025-02-15 04:23:00 | NPP-375D | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| b658c6f3-f87b-34f2-94fe-ad7caa3e80b9 | -20.31063 | -45.58401 | 2025-02-15 04:23:00 | NPP-375D | ARCOS | MINAS GERAIS | Brasil | 3104205 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 73ace79d-dfce-3f52-83fe-19368f685ea1 | -12.35135 | -47.99264 | 2025-02-15 04:23:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 41c78918-8865-3f94-9191-420e0e963c01 | -11.69079 | -43.9104 | 2025-02-15 04:23:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b8252aa2-88b1-327a-b11e-c88d89d34f63 | -11.69368 | -43.91478 | 2025-02-15 04:23:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ee2012f9-c0f0-3d4f-ba7c-0750934c99d4 | -9.90916 | -38.10618 | 2025-02-15 04:23:00 | NPP-375D | PEDRO ALEXANDRE | BAHIA | Brasil | 2924207 | 29 | 33 | nan | nan | nan | Caatinga | 6.6 |
| a348311e-1ae4-35e1-bccd-6be03733f92f | -11.6954 | -43.92681 | 2025-02-15 04:23:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f125680e-2b69-3185-8153-e2d161869ff2 | -10.61234 | -45.10534 | 2025-02-15 04:23:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 11.3 |
| bba02b65-f9fa-3482-afab-bf429ea8e7b9 | -20.41755 | -43.55186 | 2025-02-15 04:23:00 | NPP-375D | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 2c2f41a8-95e7-353c-8ecb-3a0dbc95d076 | -12.8531 | -38.25033 | 2025-02-15 04:23:00 | NPP-375D | CAMAÇARI | BAHIA | Brasil | 2905701 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 88d6eadf-30ec-337c-adfb-05f00668e406 | -9.98479 | -48.08799 | 2025-02-15 04:23:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 653fd1ce-44a8-37da-a101-e6ec37c03c5a | -18.90469 | -45.0404 | 2025-02-15 04:23:00 | NPP-375D | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 455eb1b0-dd78-36cc-a44b-62fb8f051d9a | -12.34295 | -52.48274 | 2025-02-15 04:23:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 64992b6d-b499-32e7-ad0d-2fb0161008d8 | -11.69022 | -43.91424 | 2025-02-15 04:23:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5223ce2c-8201-3f45-a980-95bd8a091bb0 | -19.99484 | -46.50454 | 2025-02-15 04:23:00 | NPP-375D | MEDEIROS | MINAS GERAIS | Brasil | 3141306 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d63398fd-57cf-38e4-b964-4edc1231e1d3 | -14.17486 | -44.36772 | 2025-02-15 04:23:00 | NPP-375D | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0a055bce-2e00-3f86-bccf-04e52df0b5ac | -10.54445 | -45.22107 | 2025-02-15 04:23:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.4 |
| b662ea12-fae6-39d1-8d19-a94db44116bf | -14.17834 | -44.36824 | 2025-02-15 04:23:00 | NPP-375D | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 81bb59b0-9086-3e72-81ea-35e9d3db593d | -12.84743 | -38.24911 | 2025-02-15 04:23:00 | NPP-375D | CAMAÇARI | BAHIA | Brasil | 2905701 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 6b30d754-d66e-31d0-bb4d-d8ac4651629e | -12.33936 | -52.47765 | 2025-02-15 04:23:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 85dad3f0-552a-3c04-bcdc-96678c918c8e | -11.57747 | -47.63862 | 2025-02-15 04:23:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a12ea12e-eaa5-338e-93a0-29fed16d840c | -12.85239 | -38.25604 | 2025-02-15 04:23:00 | NPP-375D | CAMAÇARI | BAHIA | Brasil | 2905701 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 6c86f6d7-b36d-33d4-932a-03a3d59cf1a1 | -12.84886 | -38.24401 | 2025-02-15 04:23:00 | NPP-375D | CAMAÇARI | BAHIA | Brasil | 2905701 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 6c69a347-c82b-36e9-b616-6c68a01439ff | -12.34371 | -52.47848 | 2025-02-15 04:23:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 809c5194-2ea9-3f6d-bb30-f2fcc9329f14 | -11.69425 | -43.91094 | 2025-02-15 04:23:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7b000eb7-3ff5-3b42-8e85-7c2b0da6f7c6 | -13.48528 | -44.01847 | 2025-02-15 04:23:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4ce5a386-c6fe-30e8-a7c3-6232840bf631 | -15.03131 | -43.37665 | 2025-02-15 04:23:00 | NPP-375D | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 8.3 |
| f47c8f79-3379-36b6-95e6-853efb0f6bd4 | -18.90535 | -45.03777 | 2025-02-15 04:23:00 | NPP-375D | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7e76d492-b29c-38dc-9f46-506d88909499 | -11.57687 | -47.64235 | 2025-02-15 04:23:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 137383b4-9c4a-32c1-86ca-48ff5c749886 | -13.48179 | -44.01786 | 2025-02-15 04:23:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 434dd60a-8774-3ff3-8aa6-7100f9f65210 | -11.66152 | -44.83767 | 2025-02-15 04:23:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e7dbb583-a94c-3875-886d-915dbb5603e6 | -12.85163 | -38.25542 | 2025-02-15 04:23:00 | NPP-375D | CAMAÇARI | BAHIA | Brasil | 2905701 | 29 | 33 | nan | nan | nan | Mata Atlântica | 8.0 |
| af301897-4d62-30d3-8f3e-9d537340f9e6 | -12.33347 | -52.48534 | 2025-02-15 04:23:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1a725da7-5807-3998-b48c-ae0a93d911d3 | -10.60955 | -45.10128 | 2025-02-15 04:23:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 96bfca84-7de1-3bdc-8ba3-be2bb0f94b2e | -10.60566 | -45.10429 | 2025-02-15 04:23:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README4.md)
