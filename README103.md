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
| 6d67aae2-612a-35d6-a381-6abe5298be8b | -9.55635 | -54.59144 | 2025-10-01 04:51:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 062bfe0b-2721-3bad-a503-8198a0e79b26 | -15.54096 | -42.66476 | 2025-10-01 04:51:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| a4e1f359-06e0-34c3-abda-2788e6136120 | -12.77715 | -46.91251 | 2025-10-01 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 249e1bcd-4cf9-3dba-bd32-2bf533bd1fc0 | -12.86895 | -46.7725 | 2025-10-01 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9a3eee98-7fa0-3b3d-b0f6-1560d2a29670 | -14.89705 | -47.21226 | 2025-10-01 04:51:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 32bb7d83-5325-378a-ad25-190f7e0410ed | -10.3843 | -52.0356 | 2025-10-01 04:51:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 522e5949-f08a-3c81-8da6-2ff17d29885a | -13.98157 | -44.87422 | 2025-10-01 04:51:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bc7df79f-b6b3-32d5-ab9c-b73aeadb447c | -11.48536 | -54.60303 | 2025-10-01 04:51:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b468ee3f-77bc-3ca0-b166-5b3cdb43e2f3 | -13.27828 | -47.22663 | 2025-10-01 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cf61e5a3-8aec-3fda-a5e2-ef3e310135a7 | -15.73205 | -48.89084 | 2025-10-01 04:51:00 | NPP-375D | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2abb2ace-81fc-3cad-9b19-53d474ccb9e2 | -10.92791 | -54.33235 | 2025-10-01 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f5202c9f-c2aa-3a09-aa96-80cc044e9ac6 | -11.61963 | -52.24159 | 2025-10-01 04:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 13ec936f-8fd5-3400-94cc-d44ebd0d4823 | -12.92349 | -54.73119 | 2025-10-01 04:51:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 230990b5-1b04-3628-81cc-549989a74192 | -13.21677 | -47.33761 | 2025-10-01 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 12bfc0cb-b5fe-3138-a4d0-1936a3a40127 | -10.91056 | -46.56705 | 2025-10-01 04:51:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e226578f-953e-37ea-8cc2-0fd7ee55314c | -14.65656 | -48.13985 | 2025-10-01 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| af6138db-211c-310f-947c-8fe2a3bad815 | -15.2614 | -49.25642 | 2025-10-01 04:51:00 | NPP-375D | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0a38f336-b539-3dcc-87f7-5ce57401553a | -9.8547 | -44.60039 | 2025-10-01 04:51:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5c640309-d0e9-32a5-b0c0-27048dd2aed0 | -11.17004 | -54.11616 | 2025-10-01 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 09bfb9ab-e10e-30b8-ad56-a9a6ac9ed76a | -15.24022 | -48.73923 | 2025-10-01 04:51:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 9c3a3067-c83d-3ff6-86c3-265b2de109f9 | -11.8428 | -48.05445 | 2025-10-01 04:51:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 27b65af3-2510-33c5-8cc6-0ca4c1ee0b5e | -14.58827 | -48.29659 | 2025-10-01 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| deaf9ccc-e8a1-3e40-9ab9-021547a7b512 | -13.91584 | -48.08873 | 2025-10-01 04:51:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f0f744f3-3765-3452-8ba8-aa28dbfbe0e8 | -13.78033 | -47.98217 | 2025-10-01 04:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9fc8ff18-566f-346d-8bde-77c539605ceb | -14.66412 | -48.12814 | 2025-10-01 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c4aafa59-bdcb-388f-8904-e36f1477fa6b | -15.17762 | -46.41764 | 2025-10-01 04:51:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 812014f9-3727-362b-8606-2f61e3a93743 | -14.18465 | -46.11277 | 2025-10-01 04:51:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3b75bca4-1779-321c-af2c-a47a89a626c4 | -15.53688 | -45.219 | 2025-10-01 04:51:00 | NPP-375D | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 64f9898b-eff8-3411-bf8e-6485dadfb0cf | -9.13987 | -51.60634 | 2025-10-01 04:51:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4d4e8dde-7160-3326-b0f1-495550ab2531 | -8.61633 | -50.3998 | 2025-10-01 04:51:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b99a5ebd-d946-3dee-9cac-ea9efc7d551e | -12.15897 | -47.76463 | 2025-10-01 04:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2f3d9e7d-c95c-39e8-b629-facfd81bc590 | -13.33783 | -47.33109 | 2025-10-01 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8d6355af-abf1-3f44-aab5-022484afa237 | -12.70069 | -48.55972 | 2025-10-01 04:51:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 7632534a-d247-3e81-9f92-cda3c18f2b6d | -14.54675 | -48.21727 | 2025-10-01 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 864eca9d-501e-38f3-9589-d3f0cf5bebdf | -10.01847 | -50.2415 | 2025-10-01 04:51:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 885a63aa-d9c7-3ad7-8ad4-7ee73f4c524b | -10.21968 | -43.03516 | 2025-10-01 04:51:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| b1e0d790-b9be-384c-927c-159a9701d522 | -14.0212 | -53.88917 | 2025-10-01 04:51:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f9039282-6d71-3489-ba77-8787c8ec09de | -13.77678 | -48.32504 | 2025-10-01 04:51:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 91b8c93d-22b4-3970-9e8f-11747419e84b | -15.14394 | -48.3968 | 2025-10-01 04:51:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ca085b13-23ab-34c6-bc52-7052ba41b527 | -15.49272 | -45.91823 | 2025-10-01 04:51:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 49a72bcf-3b06-3d14-9aeb-e9f5b91cf480 | -15.31708 | -46.41042 | 2025-10-01 04:51:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d4697473-18f5-3eae-bd73-a57eb9682f4d | -16.11707 | -48.40584 | 2025-10-01 04:51:00 | NPP-375D | ALEXÂNIA | GOIÁS | Brasil | 5200308 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 206b8348-f53b-3216-87a7-b71c48686524 | -12.87541 | -44.60296 | 2025-10-01 04:51:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1d37f507-5e24-3f5f-b4c8-fc01dcefbd27 | -12.87371 | -46.76923 | 2025-10-01 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 85f27dcb-d4f8-3272-973a-b5b677f047f1 | -11.84142 | -44.99572 | 2025-10-01 04:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 9149bb39-9968-33bd-b5c1-2af2deef467b | -14.95596 | -47.50988 | 2025-10-01 04:51:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f9ad3c74-5174-392b-8f71-daa2668ff632 | -9.92839 | -43.68064 | 2025-10-01 04:51:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 531b258e-fad5-3dd8-a00a-e890e5cde8da | -15.44419 | -43.64322 | 2025-10-01 04:51:00 | NPP-375D | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 51efe2a2-16fc-3626-9080-d13657e0d79a | -15.27035 | -51.48 | 2025-10-01 04:51:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bac5beac-9e0e-3b98-9a5b-c0a5aec5821c | -11.61907 | -52.24512 | 2025-10-01 04:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 30aeda5f-b605-3983-8466-4bd32c2d035e | -14.54327 | -48.24327 | 2025-10-01 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7e03d695-372d-35b3-8db6-e6551dcd754f | -15.32261 | -47.36636 | 2025-10-01 04:51:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 0e759724-5323-34fc-9660-629e2f2c81cb | -14.39482 | -46.22027 | 2025-10-01 04:51:00 | NPP-375D | BURITINÓPOLIS | GOIÁS | Brasil | 5203962 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 30415ee7-a384-3438-a312-f55cb1e4470f | -14.6619 | -48.13017 | 2025-10-01 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 777bdd63-6a01-37df-8c16-33f3e1f86d3c | -10.90657 | -46.53534 | 2025-10-01 04:51:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| a4b0aa42-f968-3529-9485-c473cec10f85 | -14.54722 | -48.24381 | 2025-10-01 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e7706ad0-1d97-334c-a3d2-6881e47c95af | -10.24102 | -52.69895 | 2025-10-01 04:51:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7af45fc7-15bb-3447-b0e0-9b88b104b0a4 | -11.8252 | -44.97333 | 2025-10-01 04:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cd90a06a-83fb-39b9-81ff-b80ad1352fba | -15.28659 | -52.89736 | 2025-10-01 04:51:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2412d074-578c-3454-a637-e16b66e5f50e | -15.77724 | -50.15763 | 2025-10-01 04:51:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| f5d5a934-ea15-378a-b134-d564d166a7a6 | -11.67651 | -44.2878 | 2025-10-01 04:51:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 26ca3985-260c-3064-8d85-50d8779a09f5 | -13.53707 | -47.25767 | 2025-10-01 04:51:00 | NPP-375D | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d5b14f4f-2f48-3c1b-af25-9f85fb59cbb5 | -10.05832 | -50.23203 | 2025-10-01 04:51:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 03dc8c7e-8195-3869-af47-13eab0214b2b | -13.32035 | -47.33629 | 2025-10-01 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 21.2 |
| 76f444aa-f394-38fb-8129-f357259350aa | -16.40912 | -47.05862 | 2025-10-01 04:51:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 66c5e133-ec44-32d9-a142-6c20d18c85f8 | -14.35525 | -47.13189 | 2025-10-01 04:51:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6bced3ff-048d-3ef1-a9d0-2f22a20b0ae0 | -16.01325 | -50.87536 | 2025-10-01 04:51:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 023443b9-458d-337b-8086-87bbe3767519 | -8.22382 | -55.20031 | 2025-10-01 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 54f4e4d3-4c8b-3e94-9812-b5421a26addf | -14.19499 | -46.10412 | 2025-10-01 04:51:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 587cb3a9-38de-3dfc-81f9-8bfc811eef99 | -12.77666 | -46.88515 | 2025-10-01 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 80775a2a-d5c8-35b4-aa8e-e45dbe1f5ad5 | -11.58168 | -47.65397 | 2025-10-01 04:51:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9dd7c7d0-4c79-3d93-8aa7-5efaaede101d | -13.98377 | -45.05164 | 2025-10-01 04:51:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 453652a8-0170-3557-b5c7-5e3f253219a0 | -12.01479 | -46.61787 | 2025-10-01 04:51:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1f97a677-2532-313d-b784-17eb91acfe93 | -14.71556 | -48.27109 | 2025-10-01 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 05216d72-231d-3faf-8387-e4bc0d2a2ed2 | -14.67463 | -45.297 | 2025-10-01 04:51:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| f36df6f3-cc21-3321-83d0-5401235dedb4 | -15.36067 | -46.10897 | 2025-10-01 04:51:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ef9c12c5-6362-3cfd-807e-0cefb2971037 | -11.4895 | -54.5997 | 2025-10-01 04:51:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 48ff2d90-8153-3a51-95fa-eabcd2ca56ff | -16.28422 | -47.84188 | 2025-10-01 04:51:00 | NPP-375D | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d00af777-1758-3107-9512-1cae27257189 | -14.92208 | -47.81775 | 2025-10-01 04:51:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 26e5feef-7e7c-3a52-9952-0e0e599d624b | -9.58372 | -54.59481 | 2025-10-01 04:51:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ed72354b-b8bc-3a18-bd60-5fbdd585acb2 | -12.85379 | -46.94672 | 2025-10-01 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 71f72556-527b-36f4-8796-069af429e39e | -14.53011 | -48.371 | 2025-10-01 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1e2f38ac-4a58-3c10-8241-76e677b1e51e | -13.37232 | -47.32438 | 2025-10-01 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5c1b2a92-beab-3d44-89a7-01e1285a056d | -10.83622 | -45.38228 | 2025-10-01 04:51:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 9d46a143-d107-3905-9508-caf3d7dd237c | -10.63112 | -48.59423 | 2025-10-01 04:51:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| fe6a09f5-f59d-3301-a4ec-f4eca08effa6 | -13.22996 | -48.44017 | 2025-10-01 04:51:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 62e27aa6-672a-39cc-b64d-e19e5719a68e | -14.75218 | -45.77348 | 2025-10-01 04:51:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4c23d0ac-b495-31b7-91de-be4b2f03b335 | -14.66988 | -48.13121 | 2025-10-01 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 207a07ef-adee-362a-9234-b55f5d42a38c | -15.2485 | -49.72721 | 2025-10-01 04:51:00 | NPP-375D | CERES | GOIÁS | Brasil | 5205406 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 82a8946e-32cc-3e3d-aebd-7859002c6038 | -12.84916 | -46.94941 | 2025-10-01 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 99158425-cab6-3c2a-81cf-b2f0b77f0e34 | -13.29032 | -50.65631 | 2025-10-01 04:51:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8d7216a4-1255-3d70-9ff4-ff67c20a8216 | -12.15249 | -51.4239 | 2025-10-01 04:51:00 | NPP-375D | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a3b6d1e6-399d-3ce0-84be-b84f6b161ddc | -15.15999 | -49.10255 | 2025-10-01 04:51:00 | NPP-375D | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 1484913f-99e2-3ad0-b662-916d209605da | -14.9108 | -47.20602 | 2025-10-01 04:51:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8149498e-1181-353e-88ef-47dfdbc48ff3 | -15.23571 | -48.74337 | 2025-10-01 04:51:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 18b3b1fc-e0e0-38ba-ae37-f8b42fb6a45f | -12.84337 | -46.8661 | 2025-10-01 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b6a8c83f-3c13-3298-8d19-d13cd21ffe5b | -10.7536 | -45.36923 | 2025-10-01 04:51:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d8a092a8-653c-349e-96e7-b6911d0f786d | -9.94561 | -43.58809 | 2025-10-01 04:51:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1aff493a-b5c1-3a14-89a2-a462a52ba925 | -14.35466 | -47.1363 | 2025-10-01 04:51:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 381a340a-e189-3a36-b16d-5bc8b3731d7f | -15.94336 | -46.23924 | 2025-10-01 04:51:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README104.md)
