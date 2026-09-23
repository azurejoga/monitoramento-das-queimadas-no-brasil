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

## Dados Diários - Página 61

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 94f57b2a-0b07-370c-b066-23d647b21ced | -13.45281 | -46.26028 | 2026-09-23 04:27:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b18f1ca8-d6fb-3361-87a1-fa5a82e09b4f | -9.54843 | -45.77102 | 2026-09-23 04:27:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| da2190f7-6d3a-357c-a0d0-406455dde8ed | -10.53963 | -57.44088 | 2026-09-23 04:27:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 32160f75-f949-3ebb-80c5-a8598b0b4493 | -11.1167 | -48.33149 | 2026-09-23 04:27:00 | NOAA-21 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| b2637c9d-46ef-37e6-9718-1dcb82602a7a | -7.61513 | -50.42012 | 2026-09-23 04:27:00 | NOAA-21 | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 7623db6a-627b-37f6-92eb-502f92f67228 | -9.71165 | -48.32869 | 2026-09-23 04:27:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 93c9fd1f-0f9e-315d-9572-391ff7cd575c | -6.10949 | -57.6739 | 2026-09-23 04:27:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 34a1fa1a-420e-38a9-9510-40e5b727c0a0 | -12.04901 | -50.35387 | 2026-09-23 04:27:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 13ee2dcf-40c9-3d3d-8276-1f40c3fc8868 | -11.88059 | -49.95683 | 2026-09-23 04:27:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 533213f6-99f0-333d-ac64-1e0d61cdc073 | -8.2606 | -45.4337 | 2026-09-23 04:27:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d12a4abf-cc8b-3621-b3ed-7d679e8b33ee | -13.5427 | -47.67596 | 2026-09-23 04:27:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a28ec3ee-a878-3932-824b-d98591a173a6 | -10.68972 | -48.72295 | 2026-09-23 04:27:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 351b103f-ddc5-35f2-9301-2450e2263f48 | -10.88339 | -54.09336 | 2026-09-23 04:27:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bc36453f-2d1c-33a1-9c09-824f144d5ca2 | -9.59934 | -43.94182 | 2026-09-23 04:27:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 26c40911-d4d6-39c2-9898-aad4677c637b | -7.6131 | -46.68108 | 2026-09-23 04:27:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 81122661-6c34-384a-b73d-9138935b33a5 | -14.61685 | -45.63655 | 2026-09-23 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 20.4 |
| dae0462e-21ce-3091-b374-eacbb4f9f439 | -6.10381 | -57.67511 | 2026-09-23 04:27:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 1bd24843-2e00-3ef2-b219-c87df9e5b348 | -13.71162 | -48.79131 | 2026-09-23 04:27:00 | NOAA-21 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f290a794-3f9c-3f91-83b0-0f8165555fe4 | -14.41107 | -42.10719 | 2026-09-23 04:27:00 | NOAA-21 | RIO DO ANTÔNIO | BAHIA | Brasil | 2926806 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 254382cc-6746-390a-96ce-dd2e05254530 | -11.12925 | -51.05626 | 2026-09-23 04:27:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b757d53e-bd7c-37b0-a044-db6f1e41ddda | -9.92635 | -48.47769 | 2026-09-23 04:27:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e5c1fa77-a34a-3e83-8c42-8c61fe906fed | -14.39858 | -47.25639 | 2026-09-23 04:27:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e6e8c07e-364f-37d4-a368-255687e47946 | -6.13129 | -52.76118 | 2026-09-23 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b35fb962-38fc-37b3-9f9b-40a9466ae093 | -10.87582 | -50.15181 | 2026-09-23 04:27:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 197c21fb-6a0c-3c4e-a38a-e30db40bfb53 | -8.73588 | -47.59321 | 2026-09-23 04:27:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 74ea0f24-9589-3fab-877b-29f9af8a8f07 | -12.45011 | -46.97795 | 2026-09-23 04:27:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0a2268db-2cce-3e4b-8254-4600fb7444db | -7.27865 | -45.54653 | 2026-09-23 04:27:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e859e259-5a0e-32fc-b0e9-92cb656b77a5 | -8.27923 | -54.76167 | 2026-09-23 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| e301643a-17c4-3463-8975-43f376cd4af6 | -10.3788 | -50.21659 | 2026-09-23 04:27:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 4caa438c-9701-31fa-b4ec-0f32bdcba73c | -10.36224 | -50.44999 | 2026-09-23 04:27:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d154aa0d-5f4c-3a7b-8207-8c0f49280f54 | -10.11408 | -46.09378 | 2026-09-23 04:27:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2f411653-e6df-39ef-a72d-f0a231ed1bef | -11.43763 | -47.39481 | 2026-09-23 04:27:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8080d7cf-11de-39f4-8ea2-5a5055eac44f | -12.41407 | -46.96858 | 2026-09-23 04:27:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 62e7f2ab-1cc0-3f12-8aaf-6725079c133d | -8.766 | -45.88897 | 2026-09-23 04:27:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5a877c56-0f32-3850-af12-a2ae2e2a7020 | -14.62921 | -45.62587 | 2026-09-23 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 5d000418-2027-3414-9b73-dd02a15f56d8 | -11.29693 | -44.03969 | 2026-09-23 04:27:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 758bd8a4-645e-3dde-89dd-e8d45aabc161 | -10.05466 | -48.84295 | 2026-09-23 04:27:00 | NOAA-21 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 57e463c0-1323-3a39-b321-e099fe0fbbd5 | -9.89287 | -48.47234 | 2026-09-23 04:27:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cb8b3a11-d3ad-35ab-9a1a-93dc186f1808 | -14.64109 | -45.64762 | 2026-09-23 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a5237435-e3ac-3ac6-9089-f2f01fb23f43 | -8.27826 | -54.76717 | 2026-09-23 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| c35cdfcc-be23-38ff-ba26-618a60af5b08 | -10.3074 | -50.51369 | 2026-09-23 04:27:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 3c81b346-896d-38a4-ae84-994e41b06b55 | -9.9965 | -39.1718 | 2026-09-23 04:27:00 | NOAA-21 | CANUDOS | BAHIA | Brasil | 2906824 | 29 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 50d6e1c7-aba3-3322-a3cc-fffae13b893b | -14.63053 | -45.64603 | 2026-09-23 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 22.4 |
| c0252ade-4b2e-3f07-877f-fa1fa730f69f | -8.55227 | -38.35605 | 2026-09-23 04:27:00 | NOAA-21 | FLORESTA | PERNAMBUCO | Brasil | 2605707 | 26 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 78adf9ed-a730-3b81-b8d8-b2b0f9489a06 | -11.12116 | -48.3249 | 2026-09-23 04:27:00 | NOAA-21 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 0aa99ee8-c1fd-33f7-aff5-6933ca2f7b5c | -12.12437 | -45.63226 | 2026-09-23 04:27:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 433b6484-7671-3230-bf18-fd33874ec58e | -11.28836 | -44.04735 | 2026-09-23 04:27:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3fa442a3-e192-367b-9d3a-a612468096a1 | -8.46931 | -48.69275 | 2026-09-23 04:27:00 | NOAA-21 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6d1ad4aa-f89a-387e-903e-745ee3fbae3c | -8.25593 | -54.77995 | 2026-09-23 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| dc0e16b3-f69a-38f2-ab26-e100fc127dfe | -7.4988 | -44.32317 | 2026-09-23 04:27:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5d9a8fd2-9c3c-3d60-91d1-76fb4aa8ae34 | -7.43911 | -49.84064 | 2026-09-23 04:27:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 30.6 |
| 80e5ddc5-b207-3c76-bd0e-8c2fb9688bed | -10.50978 | -44.85773 | 2026-09-23 04:27:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ccf1b401-56e0-3c1b-88fe-4a7cb036c3df | -14.63273 | -45.6264 | 2026-09-23 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 70cedf3f-0e59-3256-a234-fddfc4335957 | -11.3 | -51.36002 | 2026-09-23 04:27:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7d9288de-4b6d-3eda-98e5-7e011f649a26 | -11.35192 | -43.37482 | 2026-09-23 04:27:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 41a57a62-e8d5-3fb5-967c-17c1befa30a3 | -10.70489 | -48.7142 | 2026-09-23 04:27:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4b5c1c01-eedd-30e5-9b30-7cc37caedc88 | -6.67037 | -47.4425 | 2026-09-23 04:27:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 39593067-c4dc-3a9c-9e1e-9ff0a6d4a043 | -7.58544 | -57.66229 | 2026-09-23 04:27:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 90310514-9a96-3e7f-982f-1c9f2f0b40fa | -14.63521 | -45.63837 | 2026-09-23 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9463ddb3-aeb0-3809-a356-e65afd0033bf | -13.89847 | -42.76063 | 2026-09-23 04:27:00 | NOAA-21 | IGAPORÃ | BAHIA | Brasil | 2913408 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 3acc647a-c3d3-3e82-af31-b2296e737276 | -11.5243 | -45.35109 | 2026-09-23 04:27:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| aae7bc5b-9875-3d51-9875-3736f60c7dd9 | -8.08856 | -44.42797 | 2026-09-23 04:27:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 25c0d402-1553-3a9e-85e7-6a4f9e610f6c | -7.29202 | -45.41397 | 2026-09-23 04:27:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 78e584ea-c9a6-38e8-87fb-ab443eb76ce8 | -8.36695 | -45.60865 | 2026-09-23 04:27:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bc7502af-e05c-3d48-bdf7-d5ba5f6354af | -6.06794 | -57.80239 | 2026-09-23 04:27:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 828ceed6-ed24-36eb-ae8d-a49902fbc706 | -11.27735 | -44.0457 | 2026-09-23 04:27:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 034ad4cf-d43d-3ab3-b8e1-6fb26b33fc81 | -14.6639 | -45.58842 | 2026-09-23 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 8.2 |
| ef3c0900-2b07-36e0-8573-2676f646e40c | -12.80007 | -50.85899 | 2026-09-23 04:27:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 210cdf9f-9966-30e1-813b-333b1f2e3a6a | -6.52862 | -55.35408 | 2026-09-23 04:27:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b9dc3f02-0a7f-328a-a358-9f142fab2871 | -7.42921 | -49.85628 | 2026-09-23 04:27:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ba630262-8714-3ea6-b7ef-3513ee5ff760 | -11.68611 | -43.44499 | 2026-09-23 04:27:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a340fe4f-485d-316e-ae4c-6297a3fb2e5b | -7.65028 | -45.45092 | 2026-09-23 04:27:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8475c793-4e38-3775-8389-1d985b1a045d | -10.83052 | -48.48186 | 2026-09-23 04:27:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3452d76a-4227-322c-9bc5-e5df3710b7c1 | -14.27229 | -47.12878 | 2026-09-23 04:27:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a1f156df-1d83-3803-99d9-799699c7b392 | -10.45278 | -50.36203 | 2026-09-23 04:27:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 88ba5186-3071-3bd8-870e-3b22f735aa28 | -11.481 | -47.35494 | 2026-09-23 04:27:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f4d6c0ec-eb73-3cda-9108-c87d7df0c428 | -10.21554 | -44.15331 | 2026-09-23 04:27:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 834cc79f-f349-351c-b907-de23e7b9832e | -9.10951 | -51.55704 | 2026-09-23 04:27:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| f92b320d-b979-38b5-9bc5-d2501aa27425 | -8.83575 | -50.48501 | 2026-09-23 04:27:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f6005f80-4e91-3a8b-9e61-59d19a8af963 | -10.27333 | -49.97723 | 2026-09-23 04:27:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 47.8 |
| 39c44a6d-9d5f-3f6d-9554-97128302f32f | -9.86074 | -48.31249 | 2026-09-23 04:27:00 | NOAA-21 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 18668d9c-e2a9-3a5e-a0bd-318a60c7408f | -9.28126 | -45.9179 | 2026-09-23 04:27:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a54bdeed-c107-3c8b-a86a-2885a3f55c0d | -11.30591 | -51.3703 | 2026-09-23 04:27:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bc74e962-4443-37fe-a8c8-3ed2947bf5e9 | -6.45731 | -59.99241 | 2026-09-23 04:27:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 1f934921-e821-3108-8d67-1dc4fb7d0a5c | -7.42537 | -49.83431 | 2026-09-23 04:27:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 24e1e926-8a55-340b-9254-2d06fe61cf1b | -14.63695 | -45.62611 | 2026-09-23 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ce1674c3-5145-3e7f-b598-708e334c18ae | -6.12602 | -57.76075 | 2026-09-23 04:27:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| ecf8cfd5-a4a9-3449-8e1d-0b9cc7e72ebf | -12.78115 | -50.90665 | 2026-09-23 04:27:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| de7d29c4-9a7c-385c-b2e0-8d29c6ec6ee7 | -11.60046 | -46.80043 | 2026-09-23 04:27:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d99c15a1-db8f-3778-9b1b-a2aeba392bbc | -14.69917 | -45.59388 | 2026-09-23 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 2de22c3a-ab6c-3e8f-90d7-aa9cb961ae89 | -6.55495 | -56.03144 | 2026-09-23 04:27:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c513efe0-0d28-394c-b04c-5b9665b03f21 | -13.51363 | -46.90977 | 2026-09-23 04:27:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 77124770-60e0-3b4a-b0f6-a72134905578 | -10.51232 | -44.87317 | 2026-09-23 04:27:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f5974857-de0f-3bdf-8491-b1289a6a7e10 | -6.98811 | -52.85743 | 2026-09-23 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9829e891-09a2-3c9f-b963-52b42270df38 | -8.28312 | -54.76799 | 2026-09-23 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 57487ec5-4e5a-34b7-ae20-83360f7f171a | -8.30739 | -54.77223 | 2026-09-23 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 88bfe018-b20c-3bc4-aa23-3f216e92e3e9 | -11.1333 | -49.45199 | 2026-09-23 04:27:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 550b37ea-fb52-3470-ad7b-603c04b2f973 | -14.651 | -45.60318 | 2026-09-23 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 04a06f54-b552-327e-a244-0b1df03881a1 | -11.69213 | -43.45265 | 2026-09-23 04:27:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9573de2d-d5af-3c2c-9cc3-8fc337e2fac4 | -11.27797 | -44.04132 | 2026-09-23 04:27:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |


[Clique aqui para ver as próximas entradas](README62.md)
