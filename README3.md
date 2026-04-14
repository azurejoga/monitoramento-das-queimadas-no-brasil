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
| d00dbd7f-eeef-3630-b2f0-16b6b5790a02 | -21.19258 | -48.61097 | 2026-04-14 04:00:00 | NPP-375D | VISTA ALEGRE DO ALTO | SÃO PAULO | Brasil | 3556909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 93c5c1a7-a905-3358-bf36-d6c5a152f805 | -23.02178 | -48.44923 | 2026-04-14 04:00:00 | NPP-375D | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 77289836-c693-32e2-9890-0df4c38f1586 | -20.11693 | -46.75106 | 2026-04-14 04:00:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 373c2472-5c14-3b05-91ca-98e330287540 | -20.11567 | -46.75298 | 2026-04-14 04:00:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2d3d4477-b68d-3957-ac5a-1329d0aa24f4 | -21.33207 | -47.06794 | 2026-04-14 04:00:00 | NPP-375D | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ab49b289-953c-36c2-8987-9f411737a315 | -21.34 | -47.05081 | 2026-04-14 04:00:00 | NPP-375D | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9fc53c3d-904c-36ef-b1a3-e7c74606f83c | -21.33296 | -47.06342 | 2026-04-14 04:00:00 | NPP-375D | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d66274a4-b64d-33dd-acb2-5801f44076f2 | -18.70544 | -46.48885 | 2026-04-14 04:00:00 | NPP-375D | LAGOA FORMOSA | MINAS GERAIS | Brasil | 3137502 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f9b4b7dd-fc3a-35ed-b1fe-1603f0c238cc | -23.67698 | -47.59086 | 2026-04-14 04:02:00 | NPP-375D | SALTO DE PIRAPORA | SÃO PAULO | Brasil | 3545308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| c36305bd-aa04-373b-96fb-4f03235ebf38 | -27.45565 | -48.4533 | 2026-04-14 04:02:00 | NPP-375D | FLORIANÓPOLIS | SANTA CATARINA | Brasil | 4205407 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| ec3f18f7-4913-3527-835e-cd8d647c0f1d | -23.58329 | -46.82293 | 2026-04-14 04:02:00 | NPP-375D | CARAPICUÍBA | SÃO PAULO | Brasil | 3510609 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| bde2e95b-059e-35ad-8888-60eb531c2158 | -23.67789 | -47.5864 | 2026-04-14 04:02:00 | NPP-375D | SALTO DE PIRAPORA | SÃO PAULO | Brasil | 3545308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| b8a3516a-3bd7-3a54-a60c-829f137e17be | 2.9463 | -60.179 | 2026-04-14 04:10:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 419a875d-1a4d-3f77-b71d-0a9ac9239e82 | 2.9281 | -60.1793 | 2026-04-14 04:10:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 063da023-47bc-3f61-a569-0a94e759f67b | -14.40104 | -44.58472 | 2026-04-14 04:17:00 | NOAA-20 | MONTALVÂNIA | MINAS GERAIS | Brasil | 3142700 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 189e96a1-784d-35d0-b39e-20d5a43dd1a0 | -14.40049 | -44.58828 | 2026-04-14 04:17:00 | NOAA-20 | MONTALVÂNIA | MINAS GERAIS | Brasil | 3142700 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bc7a5dee-22a5-3739-b125-beecef326f50 | -5.34689 | -45.11758 | 2026-04-14 04:17:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dab5d131-2162-372b-8b96-6ed8d06a8e05 | -16.33191 | -43.89129 | 2026-04-14 04:17:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8cf1cba7-28fd-358f-82b3-a8078da61c11 | -15.42603 | -43.02286 | 2026-04-14 04:17:00 | NOAA-20 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 0.9 |
| a1bf66d6-c3e2-3dfd-a79c-475ab39e433d | -14.55692 | -42.32815 | 2026-04-14 04:17:00 | NOAA-20 | CACULÉ | BAHIA | Brasil | 2905008 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| f4fe7396-9cc3-3a0d-b77b-92e01dd45f02 | -7.01551 | -45.42531 | 2026-04-14 04:17:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1d147dfe-0c11-34fd-8def-9bc0fe2c936c | -9.45426 | -47.82295 | 2026-04-14 04:17:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 61275286-59d4-341f-9ac7-714f9f89c158 | -9.79896 | -37.47353 | 2026-04-14 04:17:00 | NOAA-20 | PORTO DA FOLHA | SERGIPE | Brasil | 2805604 | 28 | 33 | nan | nan | nan | Caatinga | 0.8 |
| b95d0d3d-eb3b-3b2d-831e-87bf2fff4158 | -9.34787 | -40.5257 | 2026-04-14 04:17:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 0.4 |
| a94ce2ff-2e65-3aaa-8b12-e8e37762c6c6 | -9.4505 | -47.82227 | 2026-04-14 04:17:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 0d1a9d78-661f-3abd-b946-907bcb46d6c9 | -9.80338 | -37.47416 | 2026-04-14 04:17:00 | NOAA-20 | PORTO DA FOLHA | SERGIPE | Brasil | 2805604 | 28 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 956f429c-3724-39a6-bee7-22dcfb011fd1 | -14.40324 | -44.59239 | 2026-04-14 04:17:00 | NOAA-20 | MONTALVÂNIA | MINAS GERAIS | Brasil | 3142700 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 57ffc4d6-3b9b-3fff-8595-4ac9903ace7d | -9.03525 | -45.0839 | 2026-04-14 04:17:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3b2b7c6a-dead-38a6-8e69-00bfc845ad5e | -9.34876 | -40.52353 | 2026-04-14 04:17:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 0.9 |
| a7a7ba79-99e6-35b1-88a5-f7273d7eee0a | -13.58623 | -43.77912 | 2026-04-14 04:17:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 076de537-5543-3864-8af8-d9cab4228a40 | -8.46678 | -44.62537 | 2026-04-14 04:17:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a9c44ecf-2131-3ad5-a3f2-33db0ef043ac | -14.4038 | -44.58883 | 2026-04-14 04:17:00 | NOAA-20 | MONTALVÂNIA | MINAS GERAIS | Brasil | 3142700 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3d814bf3-509c-3498-871e-78f75ccf5c05 | -22.83389 | -48.64401 | 2026-04-14 04:19:00 | NOAA-20 | PRATÂNIA | SÃO PAULO | Brasil | 3541059 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 78cedfbc-00d3-364e-a626-105ad7fbf7f3 | -22.87527 | -48.65106 | 2026-04-14 04:19:00 | NOAA-20 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2c0a17b8-1ba4-3a64-8e33-e65edaa74efb | -22.83454 | -48.64011 | 2026-04-14 04:19:00 | NOAA-20 | PRATÂNIA | SÃO PAULO | Brasil | 3541059 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f99a975f-3a64-3ec0-a926-e4185f94c260 | -11.13732 | -46.77552 | 2026-04-14 04:19:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 22271df2-d2c2-33f3-af63-3fbc4540db71 | -16.55297 | -49.91006 | 2026-04-14 04:19:00 | NOAA-20 | NAZÁRIO | GOIÁS | Brasil | 5214408 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e934cfb5-9496-34fd-a1c1-c19364344a9b | -20.11647 | -46.75437 | 2026-04-14 04:19:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d8e49e91-8d83-3999-9dd4-4d494d4ce542 | -23.6765 | -47.58601 | 2026-04-14 04:19:00 | NOAA-20 | SALTO DE PIRAPORA | SÃO PAULO | Brasil | 3545308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 59fc037d-7ed6-3c60-80cb-8c3c5fd1e755 | -19.6055 | -40.07276 | 2026-04-14 04:19:00 | NOAA-20 | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 16a2666a-5b3b-31b9-8760-ecd892d1a58c | -21.71184 | -57.04179 | 2026-04-14 04:19:00 | NOAA-20 | CARACOL | MATO GROSSO DO SUL | Brasil | 5002803 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 68621ac5-34f1-3aca-b88b-f312a268e97f | -20.15078 | -46.75293 | 2026-04-14 04:19:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cf071be3-0489-3ca0-9df7-7d0ddbdc784e | -11.70634 | -44.74453 | 2026-04-14 04:19:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4d3d2680-4890-3291-9ce3-2b73971e2d37 | -20.12524 | -46.76345 | 2026-04-14 04:19:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e75c863c-0869-3526-acee-8ead3f8457b1 | -23.50203 | -47.57335 | 2026-04-14 04:19:00 | NOAA-20 | ARAÇOIABA DA SERRA | SÃO PAULO | Brasil | 3502903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 653ed557-2474-3e9c-9e68-110a8d0cf633 | -23.02545 | -48.44758 | 2026-04-14 04:19:00 | NOAA-20 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 918a405c-cb77-33fc-9626-872ba023134f | -11.03477 | -49.53207 | 2026-04-14 04:19:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7cd01170-66ec-303b-87c5-b936a504cb24 | -11.03841 | -49.5318 | 2026-04-14 04:19:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fae88fa6-fb70-3864-9db5-b1e97a76998e | -21.47115 | -56.29836 | 2026-04-14 04:19:00 | NOAA-20 | JARDIM | MATO GROSSO DO SUL | Brasil | 5005004 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 792b1a54-866f-34e4-b1e1-9260bc857f7b | -11.7069 | -44.74101 | 2026-04-14 04:19:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 741c772b-0ef5-3e27-a4d6-1478b20d382f | -11.03775 | -49.53548 | 2026-04-14 04:19:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 76b52b9c-148c-3cf4-8cf0-6401b334911d | -23.02145 | -48.45077 | 2026-04-14 04:19:00 | NOAA-20 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5d2d95fa-11e6-3e20-87a9-708cf9ec9421 | -20.14747 | -46.75232 | 2026-04-14 04:19:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ed7b3fe9-b65e-3827-ba10-5925c6bc6f1a | -11.70302 | -44.74398 | 2026-04-14 04:19:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e361c643-754a-3eaa-b482-d63e7ecf5886 | -11.13666 | -46.77946 | 2026-04-14 04:19:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 824f67e6-d3e6-377d-ab33-53d8f81825a6 | -23.39345 | -47.48774 | 2026-04-14 04:19:00 | NOAA-20 | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| f253b4ca-552c-390c-9501-c50c463e5ded | -23.55987 | -47.51066 | 2026-04-14 04:19:00 | NOAA-20 | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| bc0ba4d7-7a4d-3997-9913-e8b41992504f | -20.14806 | -46.74865 | 2026-04-14 04:19:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| adb40ed6-d822-3bdc-b46b-9d1dd8c12a8a | -21.19218 | -48.60863 | 2026-04-14 04:19:00 | NOAA-20 | VISTA ALEGRE DO ALTO | SÃO PAULO | Brasil | 3556909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| d406a503-5ef8-39cf-bb80-ff84d292c1a2 | -21.47062 | -56.30081 | 2026-04-14 04:19:00 | NOAA-20 | JARDIM | MATO GROSSO DO SUL | Brasil | 5005004 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 81a2c18d-3fe4-3a50-be79-db1603f691f8 | -21.1956 | -48.60927 | 2026-04-14 04:19:00 | NOAA-20 | VISTA ALEGRE DO ALTO | SÃO PAULO | Brasil | 3556909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| d7945617-5b0a-38af-b879-47c783f85cd0 | -22.88334 | -48.64462 | 2026-04-14 04:19:00 | NOAA-20 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 84830c95-96b0-35ea-a381-7e7c7e9ace04 | -19.60602 | -40.06854 | 2026-04-14 04:19:00 | NOAA-20 | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 133d43ee-8591-3f12-bb41-be0ce72bf759 | -22.87996 | -48.64393 | 2026-04-14 04:19:00 | NOAA-20 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 2.8 |
| dfb3f7c0-b407-376f-ad2c-523fb8cf7654 | -23.5831 | -46.82262 | 2026-04-14 04:19:00 | NOAA-20 | CARAPICUÍBA | SÃO PAULO | Brasil | 3510609 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 830df963-6320-3861-8335-5cc7402a630f | -22.87256 | -48.64649 | 2026-04-14 04:19:00 | NOAA-20 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8d934dbf-ddff-3f96-98a1-f880d178d86d | -21.71096 | -57.04577 | 2026-04-14 04:19:00 | NOAA-20 | CARACOL | MATO GROSSO DO SUL | Brasil | 5002803 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c947757b-f071-36ce-951d-e42cbca2455f | -22.8719 | -48.65039 | 2026-04-14 04:19:00 | NOAA-20 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1d213f58-e87f-3532-9e6b-1ca6843b8195 | -18.70497 | -46.48893 | 2026-04-14 04:19:00 | NOAA-20 | LAGOA FORMOSA | MINAS GERAIS | Brasil | 3137502 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4383a9bc-1a19-3958-8d0c-f4b8db6d8ce6 | -11.03885 | -49.5328 | 2026-04-14 04:19:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a0b0d488-0623-3f1e-85d7-6981f836f5d0 | -11.70578 | -44.74805 | 2026-04-14 04:19:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b7969a4c-23c5-3526-8259-12a3c83cdec1 | -29.74084 | -51.2653 | 2026-04-14 04:21:00 | NOAA-20 | PORTÃO | RIO GRANDE DO SUL | Brasil | 4314803 | 43 | 33 | nan | nan | nan | Pampa | 0.5 |
| 1992f8ae-264e-354e-9d62-2e24cadc1894 | -25.24002 | -49.36064 | 2026-04-14 04:21:00 | NOAA-20 | ITAPERUÇU | PARANÁ | Brasil | 4111258 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 0e7f5904-8ed0-34f6-be33-4174be34d0aa | 2.9463 | -60.179 | 2026-04-14 04:40:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 46.1 |
| 4b21e444-411e-3090-9499-bc37e599b789 | 2.5842 | -60.338 | 2026-04-14 05:01:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6f9185ab-1abc-31bc-8544-dcac83dcd9f4 | 4.3231 | -59.74441 | 2026-04-14 05:01:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 97c37e1d-2ca7-3e04-bfa9-02f2bf589f8c | 2.94404 | -60.17873 | 2026-04-14 05:01:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e72db501-2141-3170-b7e5-fd6b0e8700cb | 4.32241 | -59.73974 | 2026-04-14 05:01:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bab71d13-9eb8-3d9e-bdf5-4cfd9ee07850 | 2.94024 | -60.18386 | 2026-04-14 05:01:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4c72db29-1324-30b4-8289-4f31c073d83f | 2.93955 | -60.17936 | 2026-04-14 05:01:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2ab67be8-4352-32d8-9177-dd8734ba80ba | 2.58488 | -60.34253 | 2026-04-14 05:01:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 94ac885e-ecce-33de-a719-512080f94418 | 2.93506 | -60.18005 | 2026-04-14 05:01:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f9de46ed-ede0-3ac6-a24f-d10f06510d12 | 2.57901 | -60.33415 | 2026-04-14 05:01:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| be615462-f660-331b-ab6c-13e3b0c586b8 | 1.7319 | -60.35773 | 2026-04-14 05:04:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c26dbe7b-5f3f-30d2-98a9-dd480dafa5ee | 1.7414 | -60.63334 | 2026-04-14 05:04:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 585b4791-dcac-32ee-a13c-cb1877ad7c2b | 1.73685 | -60.63403 | 2026-04-14 05:04:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 85cc5268-b30f-360b-833d-d8bd767603b9 | 1.7407 | -60.63575 | 2026-04-14 05:04:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c0416737-6eae-35df-90df-6acc9dc8cf7a | 1.73639 | -60.35725 | 2026-04-14 05:04:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2345cb58-8841-3c22-92fe-1d2c36c60543 | 1.74087 | -60.35666 | 2026-04-14 05:04:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 63353c59-ffb0-3a6c-bea6-b490bed27542 | -5.28525 | -56.01739 | 2026-04-14 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 90736538-8103-3ffe-9251-1c6903fc6f21 | 1.73542 | -60.63183 | 2026-04-14 05:04:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d941a884-0168-3632-baf5-bf38a77396b5 | 2.19937 | -60.80798 | 2026-04-14 05:04:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3feb2632-6c93-3002-acfa-f6f6865c8419 | 1.7357 | -60.35276 | 2026-04-14 05:04:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.1 |
| d7767e11-b15e-3d09-b9f9-644807e24a2f | 1.73504 | -60.34844 | 2026-04-14 05:04:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.1 |
| ccf7b6a9-c99f-3b14-aa13-604bb3171b46 | 1.73997 | -60.63115 | 2026-04-14 05:04:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cb5b267d-d5c4-3b90-9537-bed591cf43f1 | 1.74209 | -60.63795 | 2026-04-14 05:04:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f81419bf-f626-33f1-a03d-c353fe161d10 | -9.45205 | -47.82539 | 2026-04-14 05:06:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8ef6a77d-b9b9-3024-8187-e0076d3e873c | -9.45282 | -47.81942 | 2026-04-14 05:06:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0f1d926b-a551-34e0-8f77-b51ff870dddc | -11.84099 | -55.02091 | 2026-04-14 05:06:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a0a4d4ad-07e4-3314-8cb5-c3dac3a7e89a | -11.13602 | -46.78326 | 2026-04-14 05:06:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |


[Clique aqui para ver as próximas entradas](README4.md)
