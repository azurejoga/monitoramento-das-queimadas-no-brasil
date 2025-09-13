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

## Dados Diários - Página 35

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f4a3723f-f923-3fce-896e-022b9d528dbc | -13.12799 | -47.13297 | 2025-09-13 03:47:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5a8a672e-6463-364a-9e7a-d0ecbba54c21 | -17.2869 | -47.2523 | 2025-09-13 03:47:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e5bacd0c-fa9a-3757-af30-70e752c77b59 | -14.1894 | -46.28228 | 2025-09-13 03:47:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 2f7a4ccf-a5be-3150-b6fc-7673a5264714 | -11.15951 | -45.24078 | 2025-09-13 03:47:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c311591b-f285-394e-b551-5fed671ddb32 | -20.08897 | -46.94129 | 2025-09-13 03:47:00 | NPP-375D | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 64ba58ee-6258-353b-9a3a-c72a8cdfd065 | -18.96777 | -48.60325 | 2025-09-13 03:47:00 | NPP-375D | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a7e7b8ac-d0eb-39fb-b1b1-0d4c80c8dedf | -10.90254 | -45.58023 | 2025-09-13 03:47:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5bba5e52-46da-3fb7-b7af-b7cf4211ee7c | -11.59518 | -50.61491 | 2025-09-13 03:47:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| db934a15-0b49-3b6c-ac3f-c9eaf4d7309d | -17.28761 | -46.09606 | 2025-09-13 03:47:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a4962618-5c96-3476-9f6a-a7f434b19f6b | -14.27346 | -45.03633 | 2025-09-13 03:47:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 54c0dff2-c56f-3958-92a2-db2e010f834b | -11.06833 | -40.80428 | 2025-09-13 03:47:00 | NPP-375D | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 8f0479ba-2115-32f2-8e0f-54ee508ce3e0 | -10.77144 | -50.54113 | 2025-09-13 03:47:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 607e56f7-f213-3059-bc59-ec95c570d832 | -16.64882 | -49.75911 | 2025-09-13 03:47:00 | NPP-375D | NAZÁRIO | GOIÁS | Brasil | 5214408 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 52298aec-a4a6-33fa-9368-1cdafa08ec7a | -11.43053 | -45.60708 | 2025-09-13 03:47:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 8dcaa92f-ffbc-3418-88d8-f961b76a8584 | -16.36558 | -51.54471 | 2025-09-13 03:47:00 | NPP-375D | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3742b8d9-d24c-3c2a-9e2c-540a4d6e31ef | -11.71869 | -46.57933 | 2025-09-13 03:47:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 75ee7424-7a4c-3e47-ac14-850688dc3a9d | -9.84855 | -43.14362 | 2025-09-13 03:47:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 9c025488-21eb-3b67-a7bd-52cbfb512383 | -14.2883 | -46.08187 | 2025-09-13 03:47:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 5f4283c5-1e3b-3d3c-bef8-055bf1e8b3ba | -14.2045 | -46.26154 | 2025-09-13 03:47:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9b3321ef-0e47-3310-82f6-de1b4a4a7e63 | -12.10454 | -47.59233 | 2025-09-13 03:47:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| c42240a3-0000-3d23-9442-aee81a762d9f | -10.74719 | -50.51255 | 2025-09-13 03:47:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 20.2 |
| cc16d9f9-c926-3ee9-a2cd-8758359185c2 | -7.55763 | -42.64576 | 2025-09-13 03:47:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 6dda0c35-d92d-3be4-8e38-0d05eedd080c | -17.13952 | -48.51221 | 2025-09-13 03:47:00 | NPP-375D | PIRES DO RIO | GOIÁS | Brasil | 5217401 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 1825aa13-a0fe-3ef7-b6c0-dad84b4b11d8 | -7.41427 | -44.3552 | 2025-09-13 03:47:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 72691d56-aed6-3cb3-8816-b6ea872dbdb9 | -20.06728 | -43.69738 | 2025-09-13 03:47:00 | NPP-375D | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| bea00d01-ad1a-37b7-8e7a-bff5a2a08d85 | -17.54579 | -44.55344 | 2025-09-13 03:47:00 | NPP-375D | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 6a59077f-e93e-31ed-907b-7e0ebdda9b28 | -14.22939 | -46.29311 | 2025-09-13 03:47:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| e8dee76f-bc4f-3bb6-ac50-76ce67a0ef29 | -13.28697 | -43.77864 | 2025-09-13 03:47:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 87e5cdca-d811-39c1-be05-63e2c0b75b10 | -7.43187 | -44.40903 | 2025-09-13 03:47:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7c96c87e-4cc9-3396-8e3b-b564cc59b4d0 | -8.95104 | -44.45448 | 2025-09-13 03:47:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 180216be-85af-32a4-82a2-89a81a5ce06f | -12.84298 | -47.94608 | 2025-09-13 03:47:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 081b7c7c-c9c6-3580-abc4-a3a662f65aef | -8.32415 | -38.09391 | 2025-09-13 03:47:00 | NPP-375D | BETÂNIA | PERNAMBUCO | Brasil | 2601805 | 26 | 33 | nan | nan | nan | Caatinga | 0.9 |
| cfd3c756-bc8f-3a23-b8ba-ada61f0e0ab7 | -20.59812 | -44.90578 | 2025-09-13 03:47:00 | NPP-375D | CARMO DA MATA | MINAS GERAIS | Brasil | 3114006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 1c71e6c9-ba1c-3e05-845f-6591a37c0d50 | -11.86223 | -46.76333 | 2025-09-13 03:47:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| dbe62ac2-2376-30f8-97ac-45408199b666 | -14.21808 | -46.30474 | 2025-09-13 03:47:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a46460d1-4237-3e81-a062-1500408539bf | -16.33819 | -51.53667 | 2025-09-13 03:47:00 | NPP-375D | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 6d133ba2-171c-3133-a37e-b0e5057132ae | -12.1026 | -44.89613 | 2025-09-13 03:47:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8fe2fea7-53dc-382f-ba12-3af072f9e23d | -10.33211 | -48.82102 | 2025-09-13 03:47:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| d6973f00-0473-3de6-8d38-4c8d269ede32 | -11.72914 | -46.61578 | 2025-09-13 03:47:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 1fa03e7d-9ffd-3861-8004-98982fdcba9c | -9.13647 | -40.2417 | 2025-09-13 03:47:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| cea7939b-4344-390b-82db-01cb8a78decb | -14.41482 | -46.40227 | 2025-09-13 03:47:00 | NPP-375D | BURITINÓPOLIS | GOIÁS | Brasil | 5203962 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| edb3563d-24fc-36c5-8159-3ebf23bbfea9 | -12.82196 | -47.95667 | 2025-09-13 03:47:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 2e70da4f-cb08-3e5f-9381-55ed2a1daf5a | -14.18864 | -46.28616 | 2025-09-13 03:47:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 8b91f8b5-1bbb-3fa4-a35e-ffcc8564534f | -12.94843 | -47.98549 | 2025-09-13 03:47:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 8918e080-2e78-305e-a633-14b31ca6abfb | -17.42631 | -49.23549 | 2025-09-13 03:47:00 | NPP-375D | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4d39b557-31d2-3ac0-adb0-fb4c450ef477 | -7.94898 | -46.90606 | 2025-09-13 03:47:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 536fd096-3b4e-39f2-86db-89c93e5bdfea | -19.63711 | -43.73914 | 2025-09-13 03:47:00 | NPP-375D | TAQUARAÇU DE MINAS | MINAS GERAIS | Brasil | 3168309 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a9ee26f2-2f28-3ddb-8a31-0eb921ebe9e9 | -9.85036 | -43.14681 | 2025-09-13 03:47:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 9e6b6ef6-dace-33b7-8d54-f3bb3a9e9207 | -14.20115 | -46.25064 | 2025-09-13 03:47:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 25.2 |
| c2210bdb-cd12-3d46-af0c-4b0a8ede4f91 | -13.08238 | -48.26152 | 2025-09-13 03:47:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| fcaf6d5a-0615-303e-b3d6-5d0c57b5ad34 | -10.10259 | -45.501 | 2025-09-13 03:47:00 | NPP-375D | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 825d9f5c-27eb-3863-ade4-ec9b2d585fa6 | -13.77232 | -46.29172 | 2025-09-13 03:47:00 | NPP-375D | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 085d0498-b190-3bcd-824c-46ff9c236255 | -18.1509 | -49.19092 | 2025-09-13 03:47:00 | NPP-375D | BURITI ALEGRE | GOIÁS | Brasil | 5203906 | 52 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 754e7abf-292a-3071-8d4a-60ac8917b1a3 | -12.57006 | -45.67559 | 2025-09-13 03:47:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 43715e6f-ecb4-3041-b862-e7b189648af6 | -12.8982 | -47.95221 | 2025-09-13 03:47:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fe804a37-cbc1-3367-b54c-8f13daa474cc | -11.48363 | -43.70716 | 2025-09-13 03:47:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 32b8eab4-290a-3dfc-930d-7f9df189cf04 | -17.91551 | -44.45771 | 2025-09-13 03:47:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| d361de16-9671-3e2c-863f-e5a4b229610a | -17.28069 | -47.24097 | 2025-09-13 03:47:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 98cea7e6-a606-3df4-83e6-3067e027b59d | -12.93301 | -47.99935 | 2025-09-13 03:47:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f1e1a537-9e4b-36eb-bf84-c71cdd41c844 | -18.70419 | -43.39158 | 2025-09-13 03:47:00 | NPP-375D | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| aafe6655-7b5e-3fa8-9fc0-0a2cf5d716ad | -14.16307 | -46.16613 | 2025-09-13 03:47:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| f475267e-c5d2-3833-8416-c6b3bbc1a291 | -12.12827 | -44.83804 | 2025-09-13 03:47:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 2c3994ed-9830-30a7-ae1a-5a6157aa28c9 | -17.23762 | -50.23055 | 2025-09-13 03:47:00 | NPP-375D | JANDAIA | GOIÁS | Brasil | 5211701 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b4aa5b81-ea7b-3022-9b29-829b46e520e9 | -14.22199 | -46.30238 | 2025-09-13 03:47:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 50.8 |
| 42e69c96-f0e4-3855-887c-d10d71feac36 | -11.42111 | -50.74681 | 2025-09-13 03:47:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 422a2321-5ffe-352f-9651-5461dda05257 | -17.32112 | -46.65901 | 2025-09-13 03:47:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| ac57cf00-7c57-30b2-b8be-f9ffb2b03f83 | -11.42749 | -45.6232 | 2025-09-13 03:47:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 38f2391a-6140-33f3-aafd-e448de4b85c8 | -14.22018 | -46.28412 | 2025-09-13 03:47:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 40.9 |
| 712387cc-b005-37c0-9df8-094bcb12c417 | -11.70533 | -46.55793 | 2025-09-13 03:47:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 31be4db5-0f0a-37c4-908c-f42ad56d0a9d | -11.83645 | -50.57729 | 2025-09-13 03:47:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 58.3 |
| 249d0106-05d6-3f70-8ae0-5cd66ed34e63 | -14.28573 | -46.06755 | 2025-09-13 03:47:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 578a57fd-939d-3ea9-b747-342a3d45e9a4 | -14.18612 | -46.271 | 2025-09-13 03:47:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 24.4 |
| e4d3c9d1-d2c7-3336-9121-0c2257c36655 | -14.17807 | -46.28385 | 2025-09-13 03:47:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 60.9 |
| 386e93b1-0e32-355b-ba9a-81d17f8c645e | -8.0715 | -44.53067 | 2025-09-13 03:47:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8ee12a33-a22e-3f1f-b3a8-194f257f7402 | -9.97036 | -50.30354 | 2025-09-13 03:47:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 4c235ead-3732-357b-af3a-b9f07593a909 | -18.15924 | -49.19421 | 2025-09-13 03:47:00 | NPP-375D | BURITI ALEGRE | GOIÁS | Brasil | 5203906 | 52 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| 59911537-c7c4-35dd-99e5-ce7f8bcebe03 | -11.86633 | -50.5767 | 2025-09-13 03:47:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 16.5 |
| b79a8bd8-f7b0-312b-9e47-63157abd95b9 | -13.00335 | -44.11888 | 2025-09-13 03:47:00 | NPP-375D | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b864dee4-819d-3c2a-946c-c0107f16f0f9 | -11.85103 | -50.59144 | 2025-09-13 03:47:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 28.0 |
| 1b97a8d8-1a48-361e-9d74-6f9f1906c6f7 | -11.83944 | -50.56304 | 2025-09-13 03:47:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 35.2 |
| f831d0fa-8ee5-3061-82f9-f9e1ba0d3430 | -12.10976 | -44.85775 | 2025-09-13 03:47:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 70eaa653-1c91-358b-a962-82d49c62b5f6 | -10.77572 | -50.52643 | 2025-09-13 03:47:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| bbb219f9-bdc4-30a4-bae7-6537d462da1d | -11.56907 | -50.58644 | 2025-09-13 03:47:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| b9a38547-c46d-3c17-868c-a79a2516a1bb | -8.24271 | -44.35575 | 2025-09-13 03:47:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c8a4b3b4-854e-3b0f-b604-c3b49d07cfac | -14.28897 | -46.07851 | 2025-09-13 03:47:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 11ba2bba-85d6-3261-8af6-b375a4cb5348 | -14.19535 | -46.28008 | 2025-09-13 03:47:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 1c85c116-578c-35f7-8e3d-658fb10fc7d9 | -7.32528 | -44.60334 | 2025-09-13 03:47:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2d926e37-67f5-3998-ab27-0b682c0f2912 | -16.33487 | -51.55089 | 2025-09-13 03:47:00 | NPP-375D | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| a96d332d-a390-34be-bf6b-457a8c9900be | -10.24739 | -48.6413 | 2025-09-13 03:47:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 7b78ccae-c447-3026-b1b8-31ec7585b0bf | -11.43488 | -45.62592 | 2025-09-13 03:47:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e0726dde-409e-35cc-8340-62bb760c6228 | -13.08848 | -48.26287 | 2025-09-13 03:47:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 36acfe75-7476-3c7a-97ec-f95f09130f18 | -16.5545 | -49.22701 | 2025-09-13 03:47:00 | NPP-375D | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| f92c4ecf-b911-3084-9700-05137aa2df80 | -13.90378 | -48.29504 | 2025-09-13 03:47:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 7230330c-e39f-33fe-9389-284b69b566ae | -11.85626 | -50.58932 | 2025-09-13 03:47:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 7ddb27eb-07b8-32a3-9ac2-363fbc747a8c | -13.91168 | -48.28884 | 2025-09-13 03:47:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 0929add4-c934-36cf-935d-26868d61674d | -16.53131 | -51.75298 | 2025-09-13 03:47:00 | NPP-375D | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 77210ab7-d133-334d-af4b-c06b754aad13 | -11.43708 | -43.55668 | 2025-09-13 03:47:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2f9ec0aa-0fc0-391b-b2f1-41e72f1598f3 | -16.64219 | -49.79536 | 2025-09-13 03:47:00 | NPP-375D | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| cdcb2f95-36b3-368a-91ef-2d20ab2ecbd9 | -10.33077 | -48.82767 | 2025-09-13 03:47:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 457067fe-780a-3334-8ee2-b8763376ec7b | -13.40381 | -46.80499 | 2025-09-13 03:47:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |


[Clique aqui para ver as próximas entradas](README36.md)
