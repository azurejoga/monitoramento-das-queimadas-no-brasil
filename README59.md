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

## Dados Diários - Página 59

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a092b73e-13f9-30d7-99a4-3ef7ff68bb69 | -14.43967 | -46.35093 | 2025-10-01 04:21:00 | NOAA-21 | BURITINÓPOLIS | GOIÁS | Brasil | 5203962 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e449ae39-c706-3c1d-b758-8f96a60766ba | -17.57676 | -45.38736 | 2025-10-01 04:21:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| aa9c0d54-dae7-3224-80bf-b891fffe8066 | -15.69162 | -46.25908 | 2025-10-01 04:21:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a370ea96-1fd1-33a6-9a54-4c93d37cab2f | -14.66998 | -48.13114 | 2025-10-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9b1595a6-aff2-3c7f-93c3-4ddaa41cfda7 | -15.04874 | -48.06679 | 2025-10-01 04:21:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ded574fe-61b2-3431-ac3e-3596988a0b90 | -11.1982 | -47.19945 | 2025-10-01 04:21:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 5bc7d3e6-eecc-3c1e-acab-6e175f97b164 | -12.82939 | -46.87474 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 327c870e-cd10-33e7-a0a3-1e69edcd7182 | -10.47825 | -55.62014 | 2025-10-01 04:21:00 | NOAA-21 | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c258b50e-2612-3139-b013-c78e1b40b8b8 | -10.6425 | -48.52824 | 2025-10-01 04:21:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 00c56001-7564-3561-b973-283f76248556 | -15.27207 | -49.27224 | 2025-10-01 04:21:00 | NOAA-21 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8af18688-0f71-3947-8689-96103ba13c31 | -10.7791 | -45.36934 | 2025-10-01 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 683f1004-1748-3e7f-b07e-7be54bfa66ea | -13.80303 | -47.87548 | 2025-10-01 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2f846f96-890f-379d-ab52-01d159a3c867 | -10.9054 | -46.53649 | 2025-10-01 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 6de1dc48-5c7e-3ba5-9764-20832b5188b6 | -14.61333 | -48.21282 | 2025-10-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c23fe01e-4b01-3ca3-8574-7b1f6e9c8edb | -10.60396 | -49.63876 | 2025-10-01 04:21:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| c783b55b-cf20-35e0-9154-85fe80c01c5f | -15.92965 | -48.1381 | 2025-10-01 04:21:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 34ddd292-9a58-374a-b14c-872998e718a1 | -11.45776 | -45.04862 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 11ad2800-6c88-39ed-927a-1e4e5079242a | -11.99768 | -46.5817 | 2025-10-01 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4bf5111e-9bea-331d-b0c1-82dfc28c2ed2 | -12.96373 | -48.43114 | 2025-10-01 04:21:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 79415a32-cc3d-3a50-8dbb-3771d58827a5 | -13.92474 | -48.08512 | 2025-10-01 04:21:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b43c5b21-b866-3ed4-9acd-786fcfb0c513 | -10.7758 | -45.36882 | 2025-10-01 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 14ca5811-c056-3826-8a8e-9d07b703dd63 | -17.4108 | -47.14695 | 2025-10-01 04:21:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 85b28852-2ef1-3de5-afc4-02f2e718dbe1 | -14.94547 | -45.55528 | 2025-10-01 04:21:00 | NOAA-21 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4db4878e-0cfd-3d21-8dec-36205c7b4dd3 | -11.75956 | -46.85861 | 2025-10-01 04:21:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| be286a95-5d24-3cdd-922c-be6459bad8b3 | -13.71557 | -54.72187 | 2025-10-01 04:21:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 12.0 |
| a2bad1b8-75f5-30be-938d-c970159bd959 | -12.83989 | -46.87278 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2fc2e0d2-29c2-3513-a3d7-807328537a56 | -13.55526 | -47.27621 | 2025-10-01 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| ecfea4fa-3564-34ba-adfa-7dcd40656f30 | -14.34872 | -45.90625 | 2025-10-01 04:21:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 4bc91da0-491c-3d84-83cb-b00a6f77270f | -14.7758 | -45.80254 | 2025-10-01 04:21:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| db1d5695-fb79-3b46-98cf-d8b4779150eb | -13.53431 | -47.25808 | 2025-10-01 04:21:00 | NOAA-21 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 75a77405-6abf-3176-aa8d-9566468a12fa | -18.33675 | -41.80718 | 2025-10-01 04:21:00 | NOAA-21 | CAMPANÁRIO | MINAS GERAIS | Brasil | 3110806 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 0045b149-18b9-3784-b99f-b3c99ebda360 | -11.86644 | -48.0272 | 2025-10-01 04:21:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4aacdcec-22c5-357c-b680-d8fbbe5ec604 | -11.99696 | -46.65035 | 2025-10-01 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 00c5019c-2328-3e10-98ad-93ea351d761b | -17.38827 | -47.13943 | 2025-10-01 04:21:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ad89ec1f-ca0c-3eab-a53b-bf4602105742 | -15.13208 | -46.44955 | 2025-10-01 04:21:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 895a0710-bc3b-3cb6-81a5-5706e9ec9a9c | -14.60873 | -48.21984 | 2025-10-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 19e65ea4-fe83-391c-8abd-ccce6c726760 | -12.98345 | -48.4188 | 2025-10-01 04:21:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f0ef42df-5252-37a7-8634-6c0b99245880 | -9.92709 | -46.8439 | 2025-10-01 04:21:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ac0079aa-c1a3-33fd-9729-f754184f4c92 | -14.70056 | -48.26166 | 2025-10-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| acf513c9-3e55-392b-bcbe-c97de7955929 | -11.07485 | -47.81513 | 2025-10-01 04:21:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3fd9a0a9-050d-3912-b709-9140dcca8931 | -13.68362 | -47.85509 | 2025-10-01 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f2fadd11-8dd4-3852-b9c3-1c911a3e5cb3 | -15.30031 | -47.8588 | 2025-10-01 04:21:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 72ceaa92-d257-3bce-86b5-4e1ce81f4fca | -12.22131 | -40.98824 | 2025-10-01 04:21:00 | NOAA-21 | RUY BARBOSA | BAHIA | Brasil | 2927200 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| ffdb3ad6-afd6-342f-93f6-341c2b94b147 | -15.50419 | -48.55256 | 2025-10-01 04:21:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 89454e46-ddea-3b2b-a955-5297d0a49c30 | -15.31027 | -46.41667 | 2025-10-01 04:21:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4c477611-7a9d-38e3-87c2-49cdde8fc820 | -14.71344 | -48.26768 | 2025-10-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 596e7ea1-58c5-38f7-97b9-fbc64fd4fc0e | -10.83521 | -45.38186 | 2025-10-01 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c62fbd58-bb74-31be-bb9e-46d8bd10b0d5 | -11.67192 | -44.28277 | 2025-10-01 04:21:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e2908eed-b296-3466-ad5f-5fba4c718795 | -10.83138 | -45.3812 | 2025-10-01 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 63f919f4-8179-3bf4-9e71-84cee1240df2 | -14.05079 | -47.98122 | 2025-10-01 04:21:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 6ea4311b-9bc1-373a-8e0e-feaa27b274c7 | -14.68117 | -48.23188 | 2025-10-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d1c893c7-1297-385f-93e3-425595f0953d | -13.21791 | -47.34177 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| d75d4f5d-d2e3-33f4-b1a4-55f8d849ef9b | -11.68019 | -45.32637 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b02ec31f-0ff0-3f98-827a-5ff68e9f7918 | -14.72016 | -48.16243 | 2025-10-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6dd81025-85a1-3336-afe0-6196ab9aa1ba | -14.7015 | -48.12849 | 2025-10-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 9766c5e9-14fa-3b53-9e70-6c1655b54183 | -10.75875 | -45.36971 | 2025-10-01 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1703fc28-e824-3eb4-bb2f-5fdea8e6f3e8 | -13.36424 | -48.09435 | 2025-10-01 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3921b886-11a3-30c9-aa82-d5ac3eeb75d7 | -12.86948 | -46.94316 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 115bd67c-faad-376c-a5fa-7189f6e7e3cb | -11.43476 | -43.5008 | 2025-10-01 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 374d46e6-336c-3e27-b1bb-9e7c3777ce84 | -11.83687 | -48.05728 | 2025-10-01 04:21:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 21.1 |
| f43b71bb-fb5c-3d69-aebd-152d904c44a0 | -15.32719 | -47.37233 | 2025-10-01 04:21:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 70f1e626-f58c-373d-af2e-601d2ee1c2f5 | -11.84703 | -45.01527 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 53a2dd28-0ebc-3863-9191-f2f96b676444 | -15.93287 | -43.30729 | 2025-10-01 04:21:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 563124a0-e856-3a34-9847-1769d76f83b7 | -18.4234 | -39.79748 | 2025-10-01 04:21:00 | NOAA-21 | CONCEIÇÃO DA BARRA | ESPÍRITO SANTO | Brasil | 3201605 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 4b9c1439-0988-3d12-a415-c96e39e41fe9 | -15.77417 | -43.70014 | 2025-10-01 04:21:00 | NOAA-21 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| da4403b3-670d-3be1-944e-a9eeb85f45d7 | -11.08329 | -47.82798 | 2025-10-01 04:21:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 5c162bda-8313-339e-86cc-b31420b8e0f8 | -14.50708 | -48.47931 | 2025-10-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| dea31bed-0793-3063-91b1-f80c8da076b2 | -10.17493 | -44.89995 | 2025-10-01 04:21:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f43871e9-300b-3b42-8636-fa310f636db7 | -14.79702 | -42.82819 | 2025-10-01 04:21:00 | NOAA-21 | URANDI | BAHIA | Brasil | 2932606 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| b0960f87-d776-35ed-8e44-10caf8147970 | -11.82029 | -44.96729 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 40c5c2b9-a99c-32a3-9a5a-d547533be0e8 | -11.82362 | -44.96782 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e518c366-da56-35a2-bccc-fcd6973ef71c | -12.24435 | -47.80102 | 2025-10-01 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| db782ded-b990-39a2-9797-10b6a5c3aa9d | -11.76458 | -46.84849 | 2025-10-01 04:21:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 12.2 |
| a292e751-b52a-3c7a-aa36-63cdf83b0258 | -15.27486 | -49.27692 | 2025-10-01 04:21:00 | NOAA-21 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 98e2e399-7955-3183-a150-edf6ac71a581 | -12.01742 | -46.62833 | 2025-10-01 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 736a1415-9592-365e-aa6a-a051571e496c | -14.57089 | -45.02673 | 2025-10-01 04:21:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 09307ca8-9639-373a-9849-4470f56a8f93 | -13.94015 | -48.11812 | 2025-10-01 04:21:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 54c4f7aa-e9bd-32e6-85a8-48fe0726668b | -15.14034 | -46.41815 | 2025-10-01 04:21:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 91c4901f-9934-3f41-9ec9-7adbc675db75 | -14.3548 | -45.91088 | 2025-10-01 04:21:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| aa569554-9d35-324b-b8fa-d2b4a5fa4efb | -16.91955 | -49.78814 | 2025-10-01 04:21:00 | NOAA-21 | CEZARINA | GOIÁS | Brasil | 5205455 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 22ea88da-8940-305d-ac4b-3297d04d89f8 | -12.77123 | -46.87612 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 814462d5-604b-3874-9860-7edfcb73546a | -13.32806 | -47.33465 | 2025-10-01 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 61cb902b-cffd-35d2-926f-f14707df6520 | -13.03001 | -48.674 | 2025-10-01 04:21:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5f2c7600-5b9a-38c8-9f76-37c3d734b1ff | -11.81237 | -44.90733 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 650d5b5b-8253-3689-9d67-1dba37235e2e | -12.78194 | -46.87418 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 51a299a3-dd63-34c8-8f2a-53a6293ba73d | -11.56806 | -50.18894 | 2025-10-01 04:21:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 029a78ac-cc78-383c-968e-cfd2901d82f8 | -11.68663 | -44.30017 | 2025-10-01 04:21:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 790aa1d6-dc43-37d5-aab4-5993cad35079 | -15.25002 | -49.72669 | 2025-10-01 04:21:00 | NOAA-21 | CERES | GOIÁS | Brasil | 5205406 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bd4a2123-8bc7-3ec5-908f-a63e0deb69ce | -14.89461 | -48.11185 | 2025-10-01 04:21:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| d0885a19-ec1e-3f01-8118-359099dde127 | -15.2783 | -49.27771 | 2025-10-01 04:21:00 | NOAA-21 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8e0008e9-9ffe-3f10-afc0-89a89836b785 | -13.2805 | -47.22706 | 2025-10-01 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 77b4165f-c23f-3ce1-9654-1d7caa4a3bd7 | -15.23378 | -48.74268 | 2025-10-01 04:21:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 989045a2-225c-326f-b2fc-f7154410b058 | -9.58645 | -54.58814 | 2025-10-01 04:21:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d8104ec6-6e74-3f2a-9ec1-557ed6f36799 | -15.8398 | -46.24673 | 2025-10-01 04:21:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8b1e7834-1f61-390b-9e1b-dd10a79f2962 | -13.37709 | -47.32441 | 2025-10-01 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3e07ca33-a7b9-394c-b0ee-79425e9f9158 | -11.85089 | -45.0123 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 37a3de84-15e7-3e08-9740-a54296b02f36 | -16.02633 | -50.9003 | 2025-10-01 04:21:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 1dc3731f-be51-31c3-ae10-47ac17d4dbb1 | -13.06479 | -47.08532 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0027289a-8f59-315f-90c0-9309a10250a5 | -15.34244 | -56.63807 | 2025-10-01 04:21:00 | NOAA-21 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b223c2c1-c0e8-32fc-b6b7-ac16aa83be62 | -11.20335 | -47.75893 | 2025-10-01 04:21:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |


[Clique aqui para ver as próximas entradas](README60.md)
