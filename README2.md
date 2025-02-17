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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ec47ddf2-280a-33eb-b8f2-d8b3e46b1aa5 | -17.55445 | -46.5447 | 2025-02-17 04:08:00 | NOAA-20 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f9af283f-a11d-3667-9eb5-afbcc0857cd3 | -18.51962 | -39.93095 | 2025-02-17 04:08:00 | NOAA-20 | CONCEIÇÃO DA BARRA | ESPÍRITO SANTO | Brasil | 3201605 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| ec9f00de-fd54-368e-815c-1bc60ba4c1dd | -21.12159 | -47.81522 | 2025-02-17 04:10:00 | NOAA-20 | RIBEIRÃO PRETO | SÃO PAULO | Brasil | 3543402 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a3ef1d35-0696-3bc3-9708-a80519720945 | -21.19605 | -44.93711 | 2025-02-17 04:10:00 | NOAA-20 | IJACI | MINAS GERAIS | Brasil | 3130408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| e7e03944-4d7b-398f-8d9e-8466c9419e3f | -22.7871 | -43.75737 | 2025-02-17 04:10:00 | NOAA-20 | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 8b6cbdff-92ec-368d-9705-30822029c912 | -21.30137 | -48.63029 | 2025-02-17 04:10:00 | NOAA-20 | CÂNDIDO RODRIGUES | SÃO PAULO | Brasil | 3510104 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 6f4febdd-0b2c-3028-8ffc-31132c2dbbcf | -22.85766 | -43.87305 | 2025-02-17 04:10:00 | NOAA-20 | ITAGUAÍ | RIO DE JANEIRO | Brasil | 3302007 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| d448213d-04d3-3618-a82f-07a87f19b9fd | -20.32093 | -41.68707 | 2025-02-17 04:10:00 | NOAA-20 | IRUPI | ESPÍRITO SANTO | Brasil | 3202652 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 450fc9b7-a08f-3d49-b05e-24c68a811066 | -22.90569 | -43.52219 | 2025-02-17 04:10:00 | NOAA-20 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| f6a4455c-8f15-335a-a0e8-f808b537368c | -20.37946 | -45.41355 | 2025-02-17 04:10:00 | NOAA-20 | FORMIGA | MINAS GERAIS | Brasil | 3126109 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 8ad94f9f-4a47-318e-8eaa-0b9d1ac534c0 | -21.30217 | -48.6258 | 2025-02-17 04:10:00 | NOAA-20 | CÂNDIDO RODRIGUES | SÃO PAULO | Brasil | 3510104 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 691d7f94-886a-3d09-bc38-a51ec5cff9b9 | -20.76237 | -46.76946 | 2025-02-17 04:10:00 | NOAA-20 | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| ddf69cd3-cbd8-303e-afda-b594555b9857 | -20.31736 | -41.68645 | 2025-02-17 04:10:00 | NOAA-20 | IRUPI | ESPÍRITO SANTO | Brasil | 3202652 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 16a4831d-e9e5-3d03-b8a0-579d0e9c160e | -23.40397 | -46.55578 | 2025-02-17 04:10:00 | NOAA-20 | GUARULHOS | SÃO PAULO | Brasil | 3518800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 625ddd4c-bf80-3a0e-8f45-92156068646f | -22.67686 | -42.85447 | 2025-02-17 04:10:00 | NOAA-20 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 91eb4f9c-8775-39d0-a7fc-bd071406624c | -20.33615 | -46.7758 | 2025-02-17 04:10:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a895b15b-267e-3984-ab70-843271be75a8 | -23.98187 | -48.91642 | 2025-02-17 04:10:00 | NOAA-20 | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4c8b4d8d-05c9-367e-9774-8b46696ca81e | -22.67627 | -42.85862 | 2025-02-17 04:10:00 | NOAA-20 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| d88a90ad-4903-3df2-ad02-7b8ec1b3b1bd | -19.74117 | -40.11776 | 2025-02-17 04:10:00 | NOAA-20 | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| c6d3dc95-ab73-3b88-b3ec-e57b17e5a2a5 | -23.98543 | -48.91717 | 2025-02-17 04:10:00 | NOAA-20 | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8658de55-e8bf-399d-9a14-d17ee3c820bb | -20.32152 | -41.68275 | 2025-02-17 04:10:00 | NOAA-20 | IBATIBA | ESPÍRITO SANTO | Brasil | 3202454 | 32 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| 762e73ea-395b-3c35-8700-2e2a7352d2fe | -22.85768 | -42.97954 | 2025-02-17 04:10:00 | NOAA-20 | SÃO GONÇALO | RIO DE JANEIRO | Brasil | 3304904 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| c9021627-a345-3776-bee1-c4b89ebe17ee | -20.41805 | -43.5519 | 2025-02-17 04:10:00 | NOAA-20 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| 0e5a14ff-6f0e-3b29-9e7f-8217d20ce273 | -21.18009 | -43.98157 | 2025-02-17 04:10:00 | NOAA-20 | BARROSO | MINAS GERAIS | Brasil | 3105905 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| ee14445e-be76-3747-b91f-309748d0b6e7 | -20.34021 | -46.77258 | 2025-02-17 04:10:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0f37e3b1-15f3-3a6c-8c92-380f4b088f08 | -22.54025 | -48.81457 | 2025-02-17 04:10:00 | NOAA-20 | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9b2b58bf-f18f-3cf5-9f15-b6272a4dd562 | -20.31138 | -45.58403 | 2025-02-17 04:10:00 | NOAA-20 | ARCOS | MINAS GERAIS | Brasil | 3104205 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6dbabfac-0919-3d3b-9622-0cffa09377c1 | -23.33745 | -46.77162 | 2025-02-17 04:10:00 | NOAA-20 | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| acf025e0-f428-3016-8e75-60a48f6699a6 | -22.90626 | -43.51823 | 2025-02-17 04:10:00 | NOAA-20 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 36b7d175-d789-350e-b3f5-ae1059b28621 | -25.1923 | -49.32764 | 2025-02-17 04:10:00 | NOAA-20 | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 4fc8f73e-7be0-3e43-bba9-c9734ce0369a | -20.98133 | -43.03396 | 2025-02-17 04:10:00 | NOAA-20 | DIVINÉSIA | MINAS GERAIS | Brasil | 3121902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| c0ab47da-479c-3422-9c30-c4398e427931 | -22.90283 | -43.51778 | 2025-02-17 04:10:00 | NOAA-20 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 16e41eae-1777-3641-a1dc-363136d93b61 | -20.89964 | -43.81968 | 2025-02-17 04:10:00 | NOAA-20 | CARANDAÍ | MINAS GERAIS | Brasil | 3113206 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| ab316319-e241-3a1f-a775-c46497fd9a32 | -20.98475 | -43.03453 | 2025-02-17 04:10:00 | NOAA-20 | DIVINÉSIA | MINAS GERAIS | Brasil | 3121902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| f13dfcb0-e45f-327e-88e3-1694dea46a2e | -23.70903 | -46.89717 | 2025-02-17 04:10:00 | NOAA-20 | ITAPECERICA DA SERRA | SÃO PAULO | Brasil | 3522208 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| c743228a-1379-39f3-aa4c-00502a638e0f | -8.12603 | -43.1432 | 2025-02-17 04:57:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 474d4217-8e16-3421-8aaf-8f75a114bd3f | -9.12891 | -61.469 | 2025-02-17 04:57:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 24d15d08-6b49-31f1-89eb-6f7c1be30c1e | -9.12522 | -61.46383 | 2025-02-17 04:57:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bce38f47-9308-301e-8597-bc850f9bb9f0 | -8.12726 | -43.13328 | 2025-02-17 04:57:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 4b88281e-1bbe-3511-84e5-fbfcac38b405 | -8.12664 | -43.13829 | 2025-02-17 04:57:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 9c04ca07-1220-3d64-8ba2-5ae92afd364d | -9.12968 | -61.46457 | 2025-02-17 04:57:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ff619c02-17e6-3cbc-8913-d9ea8162eb70 | -12.32199 | -52.48424 | 2025-02-17 04:59:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 73e2d578-547e-376d-94a8-a6d53f94f5e4 | -17.55681 | -46.54361 | 2025-02-17 04:59:00 | NOAA-21 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 10e9d75d-a268-306e-991b-3f1e22947406 | -16.2881 | -46.2718 | 2025-02-17 04:59:00 | NOAA-21 | URUANA DE MINAS | MINAS GERAIS | Brasil | 3170479 | 31 | 33 | nan | nan | nan | Cerrado | 7.3 |
| b2268927-f91d-3b5d-98d8-1879018ed505 | -15.56084 | -59.44908 | 2025-02-17 04:59:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8ca4a94a-e5ba-3069-bae9-5b767a06129a | -25.19333 | -49.32722 | 2025-02-17 05:01:00 | NOAA-21 | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 90d3ee8d-4be1-3b68-a7d2-1f170398607f | -25.1988 | -49.32434 | 2025-02-17 05:01:00 | NOAA-21 | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 6b0ea973-241f-301c-8abf-8164116a22f6 | -21.30487 | -48.63003 | 2025-02-17 05:01:00 | NOAA-21 | CÂNDIDO RODRIGUES | SÃO PAULO | Brasil | 3510104 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 18349626-80a1-3893-85be-f5580da4589e | -24.24454 | -50.73795 | 2025-02-17 05:01:00 | NOAA-21 | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 779401cc-5357-330c-ae6e-632a739adeb3 | -21.30521 | -48.62671 | 2025-02-17 05:01:00 | NOAA-21 | CÂNDIDO RODRIGUES | SÃO PAULO | Brasil | 3510104 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 91f31921-ab3c-3b69-ae1f-2e156c8a8517 | -19.022 | -57.62224 | 2025-02-17 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 63166444-5fa5-38a2-9b9f-cb46ed97cd26 | -9.12968 | -61.46607 | 2025-02-17 05:22:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 3f771ce8-0a14-3539-85da-ef204673b934 | -9.91963 | -59.91208 | 2025-02-17 05:22:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 8363c08c-7501-35c2-9ea7-1714d4b1f5a1 | -9.12636 | -61.46553 | 2025-02-17 05:22:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| a115799b-f036-3ea9-aca3-618053cf2227 | 2.91533 | -60.42461 | 2025-02-17 05:22:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| da4b8449-baa5-307a-ad70-5fda05fb45e9 | 2.91591 | -60.4283 | 2025-02-17 05:22:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6003e312-2a55-3053-ae3a-43fd0092e847 | -9.12639 | -61.46669 | 2025-02-17 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 01da1814-631e-3844-9cca-cf7e45044fd8 | -13.99852 | -53.94281 | 2025-02-17 06:03:00 | AQUA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 9040d20c-f7ca-3ea1-a493-5dd071dfc11a | -7.11189 | -39.44877 | 2025-02-17 12:14:00 | TERRA_M-T | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | 6.3 |
| dbcaa81f-1a88-3558-848a-1cc149d2e4c7 | -7.3612 | -40.57984 | 2025-02-17 12:14:00 | TERRA_M-T | CALDEIRÃO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2202091 | 22 | 33 | nan | nan | nan | Caatinga | 8.1 |
| d3eaf462-5560-39bc-99dc-84797c14ef88 | -9.21964 | -40.00503 | 2025-02-17 12:14:00 | TERRA_M-T | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 23.0 |
| ac3cd8e1-8a55-34e1-8331-54a1b8fe1f61 | -18.13827 | -42.04026 | 2025-02-17 12:16:00 | TERRA_M-T | FRANCISCÓPOLIS | MINAS GERAIS | Brasil | 3126752 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| 9896eb41-d8ef-3981-8a93-3771fcf5399c | -11.58774 | -44.87012 | 2025-02-17 12:16:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 3295bb8f-fde6-3d29-9e2e-9a321797ca5b | -13.30178 | -39.87475 | 2025-02-17 12:16:00 | TERRA_M-T | SANTA INÊS | BAHIA | Brasil | 2927903 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |
| a99c074e-48a9-3e6d-a87a-84413963856f | -11.92005 | -43.11979 | 2025-02-17 12:16:00 | TERRA_M-T | MORPARÁ | BAHIA | Brasil | 2921609 | 29 | 33 | nan | nan | nan | Caatinga | 8.2 |
| 2769c6b9-e3ca-3baf-af86-c61e87ea7199 | -18.13685 | -42.05087 | 2025-02-17 12:16:00 | TERRA_M-T | FRANCISCÓPOLIS | MINAS GERAIS | Brasil | 3126752 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.1 |
| bb340d17-0118-3c53-88fc-f5cebbd61cb6 | -15.05058 | -45.16485 | 2025-02-17 12:16:00 | TERRA_M-T | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 9.8 |
| f3fcb3d0-bfbb-3b94-b367-5457b2cdcbd0 | -18.79784 | -40.0353 | 2025-02-17 12:16:00 | TERRA_M-T | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 11.2 |
| 55598234-4387-3fe0-9a8c-79403f3a305e | -14.30694 | -43.18787 | 2025-02-17 12:16:00 | TERRA_M-T | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Caatinga | 7.2 |
| 133470dd-6041-367f-8a0d-fa2b40ab7400 | -16.34534 | -45.0218 | 2025-02-17 12:16:00 | TERRA_M-T | ICARAÍ DE MINAS | MINAS GERAIS | Brasil | 3130051 | 31 | 33 | nan | nan | nan | Cerrado | 10.5 |
| e38f27bc-54f8-360b-ab72-0cb9ba2f4bd1 | -13.30031 | -39.88616 | 2025-02-17 12:16:00 | TERRA_M-T | SANTA INÊS | BAHIA | Brasil | 2927903 | 29 | 33 | nan | nan | nan | Mata Atlântica | 14.3 |
| 0d52f0f1-a1ac-3bfe-a2d1-e5837af223c9 | -11.58923 | -44.8603 | 2025-02-17 12:16:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 38.6 |
| dffc7112-ca94-3dc2-87b7-6a40ab250a7e | -14.69429 | -44.14711 | 2025-02-17 12:16:00 | TERRA_M-T | MANGA | MINAS GERAIS | Brasil | 3139300 | 31 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 94f55307-0f16-3512-b369-d4ffdc4dd564 | -21.2461 | -41.74419 | 2025-02-17 12:18:00 | TERRA_M-T | ITAPERUNA | RIO DE JANEIRO | Brasil | 3302205 | 33 | 33 | nan | nan | nan | Mata Atlântica | 11.9 |
| 0f356081-d271-3073-88f8-07c678f3718e | -20.79017 | -45.27519 | 2025-02-17 12:18:00 | TERRA_M-T | CANDEIAS | MINAS GERAIS | Brasil | 3112000 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| 9800d9f2-7176-3a40-8deb-d2fedb45c47d | -22.15447 | -43.40726 | 2025-02-17 12:18:00 | TERRA_M-T | PARAÍBA DO SUL | RIO DE JANEIRO | Brasil | 3303708 | 33 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 7e452f48-f612-3220-9870-b80fd788dc94 | -20.64132 | -43.98744 | 2025-02-17 12:18:00 | TERRA_M-T | SÃO BRÁS DO SUAÇUÍ | MINAS GERAIS | Brasil | 3160900 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| d3853edd-118d-33bf-849b-a8ec83f09ba7 | -20.41684 | -43.54794 | 2025-02-17 12:18:00 | TERRA_M-T | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| 05b323d2-a431-380c-8ce7-d65e7ed53ea1 | -14.4704 | -45.8306 | 2025-02-17 14:20:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 88.3 |


