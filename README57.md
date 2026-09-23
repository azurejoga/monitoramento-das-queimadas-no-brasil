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

## Dados Diários - Página 57

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ce8156c0-5622-3c81-b2a9-49f2b8a7f22f | -8.79569 | -48.76033 | 2026-09-23 04:27:00 | NOAA-21 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 4.0 |
| ce3d9a44-1628-3a39-b08d-774b8b56b2b6 | -12.85986 | -50.86888 | 2026-09-23 04:27:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0ba81df1-9aeb-3473-b7d3-6a6644bb4139 | -11.47335 | -47.3825 | 2026-09-23 04:27:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 48984694-b73e-3d16-bbd1-d7b0e0b0ee79 | -12.71987 | -50.87909 | 2026-09-23 04:27:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| f7be8e02-b4ee-3f8b-a15a-df17a357bddd | -12.05035 | -50.34592 | 2026-09-23 04:27:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 31d2a970-3b0e-38e3-8408-9db7fdf7ecc5 | -13.86326 | -48.56533 | 2026-09-23 04:27:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5b221f25-71ff-3207-8641-997da93c0931 | -12.02765 | -50.06424 | 2026-09-23 04:27:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 32798a30-6408-31f8-9a64-da06138bf1db | -7.46304 | -45.49927 | 2026-09-23 04:27:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 76d94c46-334e-38d3-9925-ca7cac0c336d | -7.98595 | -47.4725 | 2026-09-23 04:27:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d98d7852-48c6-3fe0-8965-15cf61bec3cf | -8.25509 | -50.87166 | 2026-09-23 04:27:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b5bccb6e-4a16-34c6-8489-4e14b2e59a45 | -14.34706 | -43.76772 | 2026-09-23 04:27:00 | NOAA-21 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8686dca1-2ad6-3125-b4f8-9c84a38d9edd | -8.37301 | -45.59144 | 2026-09-23 04:27:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5b586293-48fa-305a-9851-20abc1e3bdbd | -8.34996 | -50.86209 | 2026-09-23 04:27:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8437d430-b1f2-383a-866c-063b9c07c81a | -6.66412 | -50.88099 | 2026-09-23 04:27:00 | NOAA-21 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 99695a80-9701-3fba-b360-c661c2135606 | -11.95567 | -50.07685 | 2026-09-23 04:27:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6f6ac0ab-aec6-366a-90b8-1a348c17b864 | -12.43353 | -46.99723 | 2026-09-23 04:27:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cec48bab-a093-3b69-8c82-dea6658fae40 | -8.86217 | -50.18833 | 2026-09-23 04:27:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 47cf704e-efa6-3150-ab43-050e170e231a | -10.70094 | -48.71732 | 2026-09-23 04:27:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e12b7976-3b29-33f8-af00-5478a87b8cba | -10.87814 | -54.0971 | 2026-09-23 04:27:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 19ea6e13-24ec-34c2-b381-06dcd4402e24 | -8.65944 | -50.11917 | 2026-09-23 04:27:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 592de19f-cd1c-37e5-8311-ba14f86e836f | -6.67116 | -55.05336 | 2026-09-23 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 28af121d-2374-372f-806e-30f9102667f5 | -11.78148 | -50.08364 | 2026-09-23 04:27:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3810f7aa-96cf-3d3d-a69f-525335499cb2 | -14.62823 | -45.66228 | 2026-09-23 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fb3d8b59-15ee-3a42-ab04-f61ce87406fa | -8.4699 | -48.68905 | 2026-09-23 04:27:00 | NOAA-21 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9c535d4e-4842-3407-934f-238d270051e6 | -10.25618 | -49.96657 | 2026-09-23 04:27:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 1d047726-db00-3fb7-beb8-43071546a204 | -6.04401 | -53.27452 | 2026-09-23 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 02ad7b55-df70-3370-883d-714f83ddff33 | -6.66987 | -58.5624 | 2026-09-23 04:27:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| e1aaa3b6-b97d-3c09-b765-767761b8b984 | -6.8126 | -47.87476 | 2026-09-23 04:27:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f85692fe-e9dd-3bba-8ca7-b72b9f43a33a | -11.46996 | -47.33881 | 2026-09-23 04:27:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| cad4e7cb-b7ec-3195-a956-70fb8f5c60dc | -10.10204 | -48.82815 | 2026-09-23 04:27:00 | NOAA-21 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| de25265a-82cd-384f-b4e6-cfe2e5f9266b | -11.87776 | -49.95239 | 2026-09-23 04:27:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 012cfe12-2e88-31ff-8bf0-8b16f1044ebf | -9.54789 | -45.77462 | 2026-09-23 04:27:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 78b49028-5605-34fc-adee-fa569a4c3e07 | -6.93011 | -46.56935 | 2026-09-23 04:27:00 | NOAA-21 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c74d7a91-021a-3316-98e3-2dabc9150ec2 | -14.63405 | -45.64655 | 2026-09-23 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e9e77d6b-5855-3e4b-a745-ba613752b802 | -10.61742 | -53.98561 | 2026-09-23 04:27:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0da8f0c1-c3ab-3b91-865a-fcf3ecea7aab | -9.72237 | -47.76641 | 2026-09-23 04:27:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d93601b2-61ac-38e5-a6f4-ef8dc54f8355 | -6.74295 | -55.306 | 2026-09-23 04:27:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bb79d7f3-44a2-3d7e-90c5-df44e0462df4 | -10.2995 | -50.51667 | 2026-09-23 04:27:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 103fa8d4-2024-3a5e-97be-7120f27f3866 | -11.12561 | -48.31832 | 2026-09-23 04:27:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b63afc14-9333-3b69-9d44-492e975d7e44 | -11.68542 | -43.44975 | 2026-09-23 04:27:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f6773a3f-a7af-344c-8f2c-b4afc631f5cc | -6.81596 | -47.87528 | 2026-09-23 04:27:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 07934044-37c9-366d-b99e-5236a96c3a11 | -12.06235 | -50.36022 | 2026-09-23 04:27:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 880314a4-3856-355c-84e1-e75a5682a525 | -12.74052 | -50.88689 | 2026-09-23 04:27:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 08867d4d-c799-394a-94c5-0693aac45a52 | -11.886 | -49.01238 | 2026-09-23 04:27:00 | NOAA-21 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 269b0df9-ae93-32e7-b3e7-878152f08a1d | -6.13092 | -51.69795 | 2026-09-23 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e36e7701-f766-35c8-81c6-46369834279c | -10.26982 | -49.97665 | 2026-09-23 04:27:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 47.8 |
| ed8d5b4f-e5c3-38ce-beeb-0f87caa1db8b | -11.52776 | -45.35162 | 2026-09-23 04:27:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7b2236f9-b5b7-3c77-a566-ba9ba453d68c | -8.45853 | -48.69482 | 2026-09-23 04:27:00 | NOAA-21 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 876d7e19-678e-33ce-b1ee-0c94fc6bef0c | -7.55734 | -48.68506 | 2026-09-23 04:27:00 | NOAA-21 | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7fad8bc1-91f2-31ae-8ab6-6c12f8bc29de | -7.31537 | -55.2192 | 2026-09-23 04:27:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dc427809-f8cc-397e-af2f-5ab603fba3a0 | -10.70999 | -48.70386 | 2026-09-23 04:27:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 59967893-b9a7-3b21-aef7-8e79252ebb4d | -8.48631 | -57.61009 | 2026-09-23 04:27:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2a5176ee-79d7-332c-9075-57ff8935ff4c | -7.54929 | -48.69144 | 2026-09-23 04:27:00 | NOAA-21 | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 17bbcf29-8326-393c-8188-35e7c876b97f | -6.26441 | -50.81092 | 2026-09-23 04:27:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e90a2942-cffb-39db-93fd-ef47dc158ce1 | -12.91406 | -50.91639 | 2026-09-23 04:27:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b1971a06-1216-3927-af7e-fb5bbc9ae729 | -9.58096 | -46.53662 | 2026-09-23 04:27:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6872ae3d-5985-3256-acf2-8d624370849a | -11.4777 | -47.35442 | 2026-09-23 04:27:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| d02b771d-054e-3898-9d81-773d89a69cf4 | -7.3299 | -55.59199 | 2026-09-23 04:27:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a52a1976-d6cf-322d-a185-845f4b16dca5 | -6.67428 | -58.57436 | 2026-09-23 04:27:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 9e2d41a6-10cb-3fe6-9ae6-c4fcfbcf38d5 | -9.94756 | -48.4738 | 2026-09-23 04:27:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| aa857d8d-7a93-38d6-bb3a-b04c81cbe065 | -8.6054 | -47.29697 | 2026-09-23 04:27:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d04385f3-7e8f-312d-b912-461636caa23a | -7.42067 | -49.86338 | 2026-09-23 04:27:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| acbca2e9-842f-3667-9fbf-64abd0ab1165 | -6.67273 | -55.07486 | 2026-09-23 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cf0316a9-2da3-35ac-baaf-72d8dfe71eab | -10.26598 | -50.24045 | 2026-09-23 04:27:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 56d93aad-21bc-324c-bed5-b77d5767d674 | -12.75753 | -50.87284 | 2026-09-23 04:27:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d6663983-3c5e-3b27-b024-89b55509ff4a | -6.67137 | -58.5647 | 2026-09-23 04:27:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| eb0b35f8-21d2-3c3b-a7db-c4b5ba65d10f | -7.65082 | -45.44734 | 2026-09-23 04:27:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9a0d647e-22c7-3e06-9687-13298edac053 | -12.73626 | -50.8904 | 2026-09-23 04:27:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9e88f3a9-4d83-3a0f-b592-d326eb931203 | -12.01899 | -47.8081 | 2026-09-23 04:27:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b4c85a6d-bab1-3de8-a68b-1b7c8325f305 | -6.68135 | -55.05508 | 2026-09-23 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c1393255-8079-38c6-9b2e-1f4fee95c47c | -12.06018 | -50.35167 | 2026-09-23 04:27:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2bf88189-fe91-3d90-b20b-52dfdffba71f | -8.7408 | -52.36315 | 2026-09-23 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ee183085-e724-353e-ae8f-90702384c563 | -11.4596 | -47.38393 | 2026-09-23 04:27:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 607a4f61-13bb-3407-994d-9b4363890f0e | -8.73567 | -54.97376 | 2026-09-23 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 216f1b35-f0db-3912-89d2-76e959e226fe | -12.46838 | -46.9699 | 2026-09-23 04:27:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a4fe62bf-e135-304d-bd6d-72d6489e6662 | -12.6977 | -47.00263 | 2026-09-23 04:27:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8d19411a-fb21-302a-ac6c-4f45bed25555 | -6.61541 | -59.9099 | 2026-09-23 04:27:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 3f4a4891-321a-33c5-9aad-2837d9e47948 | -14.65921 | -45.5961 | 2026-09-23 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 09ccbb2f-befa-36f1-ac19-d14a225f6d7a | -12.42459 | -46.96659 | 2026-09-23 04:27:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4d14f68e-e8c2-3e25-afef-09bc3a83bb72 | -7.55706 | -55.02118 | 2026-09-23 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9d523253-bbb8-3ba1-ad04-fcfd82e98444 | -5.89224 | -52.09304 | 2026-09-23 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a67352c8-89df-3d2c-9d03-9594a961d91a | -11.28987 | -44.01379 | 2026-09-23 04:27:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 29266a2f-9e48-3de0-818d-b65f2c1dabde | -12.74261 | -50.87452 | 2026-09-23 04:27:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 694774cd-314e-378e-a875-87c829546a09 | -8.49292 | -57.60701 | 2026-09-23 04:27:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 60276471-f138-3215-9e3b-1013714fb234 | -8.10979 | -45.82385 | 2026-09-23 04:27:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b7e7fe1a-28ef-3420-a38f-51631df252af | -12.05952 | -50.35564 | 2026-09-23 04:27:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e0549f7b-ce3f-33d1-9460-2fb1feeece04 | -14.62037 | -45.63709 | 2026-09-23 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 20.2 |
| 37d44a01-e810-3f70-8832-b8a65491290c | -8.78785 | -45.63266 | 2026-09-23 04:27:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6dffcb97-1559-393d-b073-48b1c9893834 | -6.89978 | -46.54693 | 2026-09-23 04:27:00 | NOAA-21 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 69bbb3ff-6203-3c7c-85d5-adddd3c05f42 | -6.66453 | -55.06149 | 2026-09-23 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 3b77d52d-f828-317e-b180-419d864ad725 | -6.6686 | -55.05713 | 2026-09-23 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 6cd19f7f-1f58-3758-8186-6b9788abf671 | -9.17345 | -51.47025 | 2026-09-23 04:27:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9d0f3337-9c70-33b3-b9de-a71842b80b8b | -11.12961 | -42.79448 | 2026-09-23 04:27:00 | NOAA-21 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 3.3 |
| c61cd3a0-32d5-3847-926b-acff93236e97 | -11.30446 | -51.35614 | 2026-09-23 04:27:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a9a3ac97-cd08-3d3b-a244-eff51c72db88 | -11.09063 | -48.34544 | 2026-09-23 04:27:00 | NOAA-21 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 8d50e486-09a7-361a-9be1-456bdf9247e1 | -11.40714 | -44.02682 | 2026-09-23 04:27:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9fd267a3-ed44-3c38-8c90-b34dc70c1823 | -10.32318 | -50.50773 | 2026-09-23 04:27:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9c6613b9-52cc-33f2-b7cc-76fa43b19e48 | -12.72041 | -50.88048 | 2026-09-23 04:27:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 8d6eb8d1-8c9f-3724-b7f1-9217d938cdad | -6.67878 | -55.05887 | 2026-09-23 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5de987be-32e2-3d79-87e4-3e0c1260ce99 | -8.36041 | -45.65167 | 2026-09-23 04:27:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |


[Clique aqui para ver as próximas entradas](README58.md)
