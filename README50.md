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

## Dados Diários - Página 50

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5e7e61e5-4b2d-3dd8-9f1b-d994f50fe4fe | -10.92098 | -45.59937 | 2025-09-15 04:51:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 627ea222-b3d1-37ec-a65e-68225c3f09f3 | -11.79676 | -50.49939 | 2025-09-15 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a3a06f57-eafc-3e2f-a6ad-1e863826c0cc | -14.1493 | -46.2487 | 2025-09-15 04:51:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 18612918-2ca6-3433-9cc8-5635d0e709ef | -8.45007 | -64.14589 | 2025-09-15 04:51:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 45120ad2-24dc-384f-a972-6f6cf4b3f516 | -14.503 | -47.33729 | 2025-09-15 04:51:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b59eb184-13a7-39aa-abb8-893cd5c75141 | -12.98413 | -47.96983 | 2025-09-15 04:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 18.5 |
| 2cb7e8e0-91cc-3d54-8493-f880ed2b71e7 | -11.31967 | -51.13376 | 2025-09-15 04:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 603a7181-8bce-3f1b-a9b8-2aa3d8d334de | -13.75861 | -48.77517 | 2025-09-15 04:51:00 | NPP-375D | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 76738814-b922-36fe-8c2d-addeff0ec442 | -15.90429 | -49.97445 | 2025-09-15 04:51:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 58f317a0-42de-3c9b-902a-fadd27e52b6f | -10.93791 | -45.50626 | 2025-09-15 04:51:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b8e0829f-c906-3b0a-a8fb-bb842bff11d4 | -14.39861 | -48.3573 | 2025-09-15 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 43cd907c-7a6f-3745-9d47-8adea5a0dbcf | -11.67073 | -46.49754 | 2025-09-15 04:51:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 84fd3f92-82a1-36ea-a82b-eb6906620e84 | -10.91682 | -45.56247 | 2025-09-15 04:51:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c7404f8a-ae2e-3adc-8a79-d2fb44bac382 | -13.92967 | -44.80031 | 2025-09-15 04:51:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3b48e6b8-3622-31a0-8527-0466b18a8122 | -11.43202 | -43.53374 | 2025-09-15 04:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fbb20e9b-dadd-3b33-82b7-3323c74ebab8 | -14.80011 | -51.60604 | 2025-09-15 04:51:00 | NPP-375D | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ef3b9835-d7a7-38a9-ac96-0f43fa9593d5 | -17.14048 | -48.52261 | 2025-09-15 04:51:00 | NPP-375D | PIRES DO RIO | GOIÁS | Brasil | 5217401 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 80348151-5e0a-3986-a887-ed8e2796f341 | -12.00591 | -47.76367 | 2025-09-15 04:51:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9141677c-bf8c-334c-8f64-b043252bfd62 | -12.4321 | -46.88615 | 2025-09-15 04:51:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 030dfd49-0462-30f7-8cde-66e9758e783a | -14.47277 | -55.96524 | 2025-09-15 04:51:00 | NPP-375D | NOBRES | MATO GROSSO | Brasil | 5105903 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| aabc11c3-0a2a-3567-8259-3064881e5cb3 | -14.28372 | -46.12384 | 2025-09-15 04:51:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 14fa6d9f-0c28-3734-9696-a02eed78d7f1 | -15.90976 | -49.96188 | 2025-09-15 04:51:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 129b5c9f-ded0-3230-8c86-5c7b0301063d | -11.87712 | -50.54186 | 2025-09-15 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f2b4a5ca-2a71-30d7-b1cc-eae6e97fcf99 | -11.83246 | -50.44276 | 2025-09-15 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 5bfd311b-2e94-3d19-865c-de2d8b03d598 | -14.51421 | -47.34844 | 2025-09-15 04:51:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2070edce-d9f4-34d3-92ea-cd64b30c7066 | -15.09896 | -52.47842 | 2025-09-15 04:51:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 31919d13-c8b1-3572-ad71-9ce2af110560 | -11.07716 | -49.71319 | 2025-09-15 04:51:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3605c851-bbe2-3d30-aa6b-e5c21b017bb1 | -14.59318 | -46.59507 | 2025-09-15 04:51:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 987a1541-2fbe-38a5-89ca-7a93c256cc0b | -18.02021 | -46.95335 | 2025-09-15 04:51:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| baa2d697-1d18-327d-85f9-3d3e4d582166 | -12.002 | -47.76311 | 2025-09-15 04:51:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 8fe5f8a9-a73e-30d6-b9be-b4c9337b4ed4 | -15.70989 | -53.07262 | 2025-09-15 04:51:00 | NPP-375D | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ff634e5a-5019-3189-821b-59ed8037cee5 | -16.67526 | -49.77769 | 2025-09-15 04:51:00 | NPP-375D | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 9.2 |
| be0f7f77-d8ad-3a8b-ba1c-46d235d04827 | -11.08057 | -49.71657 | 2025-09-15 04:51:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0f2e8fa6-fd90-3d01-8965-b5c771acb5bd | -11.43677 | -43.5376 | 2025-09-15 04:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5217bebf-e23b-3d7f-a7ee-523fc971ca45 | -11.07768 | -49.73326 | 2025-09-15 04:51:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 859d080f-de5e-3120-a634-93fa1743eecc | -11.33577 | -43.49168 | 2025-09-15 04:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0d6993db-d9d4-379c-a467-ff6001ff82a4 | -11.79848 | -50.4421 | 2025-09-15 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| eb548310-caf3-3aae-9985-d4c86928026b | -10.76361 | -50.64402 | 2025-09-15 04:51:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| bedea7ff-96d7-3a37-a921-35b9a9d10ed9 | -12.0032 | -46.66791 | 2025-09-15 04:51:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| c39baefc-4d5a-35ac-9338-0442ce7d566a | -17.83441 | -50.42112 | 2025-09-15 04:51:00 | NPP-375D | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 066d923c-d073-3f33-b670-cf8fe624cbdd | -13.88413 | -48.13286 | 2025-09-15 04:51:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 7333948c-0e1f-3745-9a78-9c36bc9386d8 | -11.28447 | -50.79526 | 2025-09-15 04:51:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7104d250-a0e2-3c94-b009-e5b848944939 | -17.34042 | -42.63726 | 2025-09-15 04:51:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c6fec2f0-92a4-31c8-89dc-370e599e8e9b | -11.80648 | -50.43566 | 2025-09-15 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 7072df44-1127-3814-8c3c-221978246685 | -12.97172 | -47.97292 | 2025-09-15 04:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| a80538a8-dd90-3c2f-a0a4-bd7d19b31a34 | -17.73129 | -47.94881 | 2025-09-15 04:51:00 | NPP-375D | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8860cbed-99d1-3c80-8098-d0543d928f8a | -14.83059 | -51.63367 | 2025-09-15 04:51:00 | NPP-375D | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 7af8f876-6414-337f-abdd-68f3c7b868e9 | -13.87703 | -48.30131 | 2025-09-15 04:51:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a0d5b7cb-d47c-33d0-bbb3-692651d77b1b | -10.76022 | -50.64349 | 2025-09-15 04:51:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cced4816-dec6-3f23-9eeb-b6f768ba971a | -12.96048 | -47.99658 | 2025-09-15 04:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 368ad65f-127e-3e46-ac95-25483551ec1a | -13.89872 | -48.31768 | 2025-09-15 04:51:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 290afe72-fd6d-3a08-9ecc-c5061f058acb | -11.36275 | -47.35443 | 2025-09-15 04:51:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0d34a974-eca8-3166-bc33-dadf0566b42b | -17.16162 | -53.23228 | 2025-09-15 04:51:00 | NPP-375D | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 824fb165-1a9b-325e-b5ee-1cd6767b8124 | -16.65432 | -49.7655 | 2025-09-15 04:51:00 | NPP-375D | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 523d81a7-b568-308c-a639-2e497beed92e | -10.7591 | -50.65079 | 2025-09-15 04:51:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d8d4fc54-9e83-3871-9bd7-ba030a477f33 | -12.64924 | -47.9427 | 2025-09-15 04:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 1a9d4264-edbf-31fb-8492-38be2d252b5a | -11.07826 | -49.73221 | 2025-09-15 04:51:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b485dad4-e90f-328a-acdd-92e62c355a4a | -14.8097 | -51.61138 | 2025-09-15 04:51:00 | NPP-375D | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 641d7af8-05f6-3f02-ac8d-cdda0e832b00 | -14.50596 | -47.34679 | 2025-09-15 04:51:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 49f8b6d6-d980-3288-a9b0-23f1dee094df | -15.90551 | -49.96572 | 2025-09-15 04:51:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7ee294a5-be45-3357-8f35-57696b158aaa | -17.14495 | -53.89032 | 2025-09-15 04:51:00 | NPP-375D | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1d8aff6c-fb59-3f12-b1f5-3b90afcf2f9f | -16.4892 | -55.10146 | 2025-09-15 04:51:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| de58737f-48a7-321a-a5da-f5e7fb8503ff | -11.86856 | -50.52903 | 2025-09-15 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6d101e65-6ff9-3dd8-8696-78c7f16a0498 | -10.93522 | -45.49221 | 2025-09-15 04:51:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 20b42397-13de-3071-9954-9e20e1dfb8d7 | -8.45492 | -64.14225 | 2025-09-15 04:51:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 24341f9f-50eb-3f90-a1d0-0ef09a3e5d99 | -11.72363 | -46.48903 | 2025-09-15 04:51:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| cbf27078-e689-30dc-9c4a-c4c4f290f349 | -11.3124 | -51.13629 | 2025-09-15 04:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e795957c-922a-325a-aa5c-f61ce803e55d | -11.15799 | -57.18638 | 2025-09-15 04:51:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 47682b50-72d8-33cd-9aa5-60a16e69a7bd | -15.18207 | -56.68382 | 2025-09-15 04:51:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 61565c20-6d0f-3421-87e0-3f6de0b80dd9 | -12.00184 | -47.75964 | 2025-09-15 04:51:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| c7e4f46f-9697-355b-a9fc-eab864977488 | -14.81817 | -51.6241 | 2025-09-15 04:51:00 | NPP-375D | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 67d9a8ee-2a97-3ad4-add2-a1e5dffb6dfa | -11.07359 | -49.73662 | 2025-09-15 04:51:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e320910a-6d37-3af9-823f-4fe3e770e258 | -15.79721 | -52.22353 | 2025-09-15 04:51:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 627d25f5-472c-30f9-b0d4-ccc338748d17 | -13.87684 | -48.13447 | 2025-09-15 04:51:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7704fb4d-24ec-3d81-b448-8dbbebb502ad | -11.16133 | -57.19006 | 2025-09-15 04:51:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 409e495a-2a22-3226-a603-0dddbb936f65 | -11.1251 | -45.31776 | 2025-09-15 04:51:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b25ba11d-f746-3fe0-b62a-bdab741860c0 | -14.49683 | -47.3201 | 2025-09-15 04:51:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c05ddb99-18e7-3d03-b5c7-ded8b29a204d | -11.48067 | -43.60289 | 2025-09-15 04:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2347e447-d77c-32db-a0cd-c4c370106bf6 | -13.00438 | -47.96788 | 2025-09-15 04:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b50b7838-45ca-3abb-a2f3-107ac71697a4 | -16.48732 | -55.11285 | 2025-09-15 04:51:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 672fb2fa-a791-3a83-8950-e6fd2a382e6d | -12.09497 | -44.86411 | 2025-09-15 04:51:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1d3b98a7-f2d7-3ae6-8beb-eb61cecadce3 | -13.19029 | -47.27835 | 2025-09-15 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 96a5268d-22fe-3a7f-ab3d-a0751c3d50ea | -11.08875 | -49.73384 | 2025-09-15 04:51:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 057ffdcc-a17c-38b9-a81f-fc4bd5ebd30b | -13.89159 | -48.31194 | 2025-09-15 04:51:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 4b6504c6-6cf4-37f4-9e14-245859d96709 | -11.08583 | -49.72939 | 2025-09-15 04:51:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 09febf42-55f6-3372-bb07-c0e419f5cfe6 | -17.33948 | -42.64597 | 2025-09-15 04:51:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 134c3e2b-9b30-3243-9da6-e9ecd0da270e | -12.171 | -44.10064 | 2025-09-15 04:51:00 | NPP-375D | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 15.6 |
| d0dccda6-7149-35ef-b68a-edbd8e56e12c | -15.8061 | -53.46439 | 2025-09-15 04:51:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0e9eb5a8-991e-34d9-9b2b-f1e29d7d0989 | -15.89583 | -49.9819 | 2025-09-15 04:51:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0b40d2e5-5736-3689-a4f0-2463d15e7fee | -15.89821 | -49.99136 | 2025-09-15 04:51:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 9b8c644d-e8fd-3895-8ef0-56d2a8a5e534 | -17.339 | -42.65044 | 2025-09-15 04:51:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a5f84888-515e-3bce-978b-7287ddc02420 | -14.83397 | -51.63422 | 2025-09-15 04:51:00 | NPP-375D | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 157871d3-c3e0-322d-a2ba-66ef3ce28978 | -16.41257 | -49.07681 | 2025-09-15 04:51:00 | NPP-375D | TEREZÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5221197 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0982356b-7525-3306-90d7-cdead9b12ce8 | -13.00119 | -47.96214 | 2025-09-15 04:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e2d94bc8-750c-34af-b485-0013dc843d5c | -16.28633 | -45.6874 | 2025-09-15 04:51:00 | NPP-375D | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e33aff46-573e-3174-96de-23961c741f80 | -12.86088 | -62.12839 | 2025-09-15 04:51:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6d80c7bd-7a21-35f3-972f-c764e03068fb | -11.85541 | -50.50014 | 2025-09-15 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| fa91eced-d6a2-37ba-9027-aa6c39725f71 | -13.87361 | -48.12902 | 2025-09-15 04:51:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 212c2f23-2015-3686-a4ca-d7db445facc6 | -12.95238 | -48.25364 | 2025-09-15 04:51:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8c35eeb8-6fac-3d60-a16f-3198d9d8812d | -10.98143 | -55.3143 | 2025-09-15 04:51:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README51.md)
