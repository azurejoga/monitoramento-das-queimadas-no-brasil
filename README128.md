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

## Dados Diários - Página 128

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 35d9decb-2981-3873-9575-199f9f1bfd95 | -3.3867 | -59.5223 | 2026-09-22 13:20:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 119.4 |
| 26d7a660-e8bb-3117-b5ea-57c60be047a4 | -9.9058 | -48.4867 | 2026-09-22 13:20:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 118.1 |
| 0ecc00b4-803b-34ed-894f-3de42c675aef | -7.4765 | -45.4872 | 2026-09-22 13:20:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 78.2 |
| 35590cfd-8c58-31e0-b1db-839070506926 | -10.6097 | -53.9697 | 2026-09-22 13:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 77.7 |
| 204a6c27-fdaf-3dc1-ae5d-e329fda2e6a9 | -11.3416 | -51.3817 | 2026-09-22 13:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 100.5 |
| d3481e33-e26f-32d2-9676-a53b6a522e4e | -3.405 | -59.522 | 2026-09-22 13:20:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 136.3 |
| c6ce6818-130d-311c-8b45-3f915e3ddb98 | -11.7079 | -50.9811 | 2026-09-22 13:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 94.9 |
| 7387e9bc-57e1-34a6-8f9a-46d603d36145 | -9.152 | -50.0066 | 2026-09-22 13:20:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 113.8 |
| 522128c4-7bd2-34bb-85cd-56465d87ad03 | -13.4335 | -46.326 | 2026-09-22 13:20:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 131.2 |
| e4a75d75-194e-3aa1-9c2b-105224dbabfc | -6.3619 | -55.8433 | 2026-09-22 13:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 55.9 |
| 6411b9fc-d0e3-33ce-92a4-684922c5086e | -12.6796 | -50.974 | 2026-09-22 13:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 183.2 |
| 9023c137-777c-303a-a66f-6970935ec805 | -11.0052 | -53.996 | 2026-09-22 13:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 202.8 |
| 4ef49edc-d5e9-36c5-8107-c1935a280b02 | -9.2762 | -46.1627 | 2026-09-22 13:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 236.8 |
| 1a52d407-e13f-3c2e-88d2-08e789272df7 | -12.1027 | -50.0355 | 2026-09-22 13:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 113.9 |
| b86a1e5d-f658-3a8c-9f44-be3ea5f4616c | -7.0164 | -44.6413 | 2026-09-22 13:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 113.7 |
| 0ac06521-0437-3b1b-ba7f-68b595301b98 | -11.4113 | -46.7798 | 2026-09-22 13:20:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 212.6 |
| ca9acbdf-08bd-3c46-9dd1-5b47620c6476 | -8.3764 | -47.2802 | 2026-09-22 13:20:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 57.9 |
| 2eeb81dd-8d17-30dc-9abf-c509b73f3ea9 | -12.3484 | -50.1779 | 2026-09-22 13:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 90.3 |
| ba0f0fae-0b53-3c65-947b-e697f8b6f770 | -8.7706 | -45.8567 | 2026-09-22 13:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 74.2 |
| 08eb6683-4633-3b61-bc59-b6289e485590 | -11.024 | -53.9943 | 2026-09-22 13:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 86.8 |
| 70ab7c06-4cec-36ce-a5a3-0870dcb4ec23 | -6.9225 | -42.9088 | 2026-09-22 13:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 130.1 |
| 51b6a3f3-46ac-3ee2-b85e-c9158d99c478 | -11.4213 | -47.338 | 2026-09-22 13:20:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 89.4 |
| bf44ba38-df85-3595-a3bf-7eea4ed423bd | -6.384 | -55.285 | 2026-09-22 13:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 93.9 |
| 4373977d-f81f-35a6-ac88-2213dd48572a | -6.9228 | -42.8852 | 2026-09-22 13:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 113.6 |
| fffc700f-5484-3aef-add7-617d9f7a5c2d | -6.9416 | -42.8834 | 2026-09-22 13:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 225.7 |
| c58e967c-feb9-3a55-a64f-0141a761d5ab | -3.4599 | -59.54 | 2026-09-22 13:20:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 97c9a98c-b054-37e7-b75a-96bfdd10871e | -10.5908 | -53.9713 | 2026-09-22 13:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 9401c313-b929-3aef-96cd-ede865b074d5 | -6.6146 | -59.9272 | 2026-09-22 13:20:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 169.2 |
| 16f7f9f5-762d-33a5-bb89-71611d32a32f | -12.1458 | -47.3974 | 2026-09-22 13:20:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 140.0 |
| 71256bbc-ddfe-3170-bffb-98950f940cce | -9.9061 | -48.4649 | 2026-09-22 13:20:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 103.5 |
| 8c1b6834-6ccf-33f0-8d91-d37246148c07 | -10.4536 | -51.325 | 2026-09-22 13:20:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 104.2 |
| 43c9b03e-cfa1-3040-8a80-e64e9e5e4229 | -8.6169 | -54.6328 | 2026-09-22 13:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 86.1 |
| 010467ff-fd97-3458-a4f3-9d21f3627e63 | -13.8536 | -51.8504 | 2026-09-22 13:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 109.0 |
| 430b0e5b-26ff-37e1-854a-a3f4114abe64 | -9.5833 | -45.8345 | 2026-09-22 13:20:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 85.8 |
| 41ff20bd-7437-3261-95ec-10741d75f850 | -11.6793 | -43.4684 | 2026-09-22 13:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 114.9 |
| ddb89d61-a1ef-3693-b56b-ebf5d433e7db | -3.6946 | -60.5835 | 2026-09-22 13:20:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 91.4 |
| a1d5430c-abf7-33f5-bbf3-002061e2d778 | -7.0352 | -44.6396 | 2026-09-22 13:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 111.1 |
| 85d4ac8e-27cd-36ca-92d5-7d5ca216571f | -7.547 | -42.6817 | 2026-09-22 13:20:00 | GOES-19 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 119.5 |
| 90da2aac-521d-3f6f-8524-e738df95dec8 | -7.0349 | -44.6625 | 2026-09-22 13:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 188.6 |
| bb634b6f-71fd-3128-b371-6db160a17335 | -6.7989 | -43.9008 | 2026-09-22 13:20:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 97.4 |
| ba86628b-8571-33ad-8f56-4df91142c836 | -6.7354 | -55.3074 | 2026-09-22 13:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 60.6 |
| b530ee94-87e5-3baf-8756-4cf624cc4b82 | -6.9414 | -42.907 | 2026-09-22 13:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 268.3 |
| 5665b418-995f-3489-a6d4-bd7f968cf1eb | -3.7856 | -60.7335 | 2026-09-22 13:20:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 80.0 |
| 0706fe2c-64aa-373e-80c7-d7bdacf83b5a | -6.6148 | -59.908 | 2026-09-22 13:20:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 85.0 |
| 5f911064-e065-3283-94ab-8e8c7c1ee170 | 4.94451 | -60.22657 | 2026-09-22 13:21:00 | TERRA_M-T | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 38.8 |
| 153b787a-5fca-3139-a7eb-6c51c2f4efe7 | 4.93511 | -60.22039 | 2026-09-22 13:21:00 | TERRA_M-T | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 36.7 |
| bc18e993-243e-3d05-b464-5f7abd772fda | -10.24992 | -68.74535 | 2026-09-22 13:25:00 | TERRA_M-T | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 9.2 |
| e981071b-4b9f-392f-8041-b4e68f4d640c | -8.60824 | -62.49881 | 2026-09-22 13:25:00 | TERRA_M-T | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 60.4 |
| fc99ec46-8c13-334b-adff-ae566ad36389 | -6.4301 | -59.9916 | 2026-09-22 13:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 54.4 |
| 33d00eb5-f733-32c8-bad5-f9db95e42db9 | -7.5889 | -57.6757 | 2026-09-22 13:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 364ea9e2-504b-3b06-a4bb-da8a4d0dd4c1 | -10.5748 | -46.7296 | 2026-09-22 13:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 255.9 |
| 76ed540c-7a94-3d18-b1de-963d6b4dfaa9 | -8.7916 | -44.2778 | 2026-09-22 13:30:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 134.7 |
| d647ed34-ce47-385c-a113-d8e7661343d6 | -3.405 | -59.522 | 2026-09-22 13:30:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 129.2 |
| 57123043-dc2f-375c-810e-036e479db0e0 | -7.5945 | -43.4296 | 2026-09-22 13:30:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 110.7 |
| 332b0b96-7e1f-36dd-b01d-8face9a24683 | -12.6799 | -50.9526 | 2026-09-22 13:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 178.5 |
| 3def0e31-1169-3109-be50-24b06a633105 | -6.4485 | -59.9909 | 2026-09-22 13:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 1c5fec52-7388-35bf-a623-0c8d4e3f1f4c | -11.024 | -53.9943 | 2026-09-22 13:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 130.4 |
| 9963d474-a138-36c2-ab5e-4aa6960be578 | -10.5752 | -46.7072 | 2026-09-22 13:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 79.3 |
| 2bc4f70a-38e7-33ae-a651-c9649a011de2 | -9.8869 | -48.4887 | 2026-09-22 13:30:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 67.7 |
| 082faf22-2eab-3db9-8925-df3f441ffd68 | -11.3226 | -51.3838 | 2026-09-22 13:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 82.1 |
| 774e8bd8-202a-3f32-a553-9a426c29837f | -3.4781 | -59.5396 | 2026-09-22 13:30:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 72.2 |
| 912d6224-5f95-3221-8147-6d6dd068f7cc | -10.6875 | -50.7722 | 2026-09-22 13:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 84.8 |
| f65697cc-91ab-3dac-9f79-bd005e00338a | -11.156 | -51.1051 | 2026-09-22 13:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 133.8 |
| 7b974a76-945b-3894-ad27-6297d53fa31e | -11.1563 | -51.0839 | 2026-09-22 13:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 209.6 |
| 9a336d51-1946-35dc-9465-ceacfa161ec7 | -11.3232 | -51.3414 | 2026-09-22 13:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 81.9 |
| 719cad52-8065-3b1d-b725-cc0c7bdcf4ed | -3.4598 | -59.5591 | 2026-09-22 13:30:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 7c674546-8831-30e9-81af-9781fd7307b1 | -9.6111 | -43.9243 | 2026-09-22 13:30:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 81.8 |
| 4b6e45f8-e958-3c84-9b7d-0e0ada1367fb | -6.0925 | -57.6847 | 2026-09-22 13:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 1d823c7d-6720-37bd-a1aa-455cc0bfcafd | -10.2635 | -49.984 | 2026-09-22 13:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 100.0 |
| f6a736cf-5281-33d6-935a-5362a211b061 | -6.9416 | -42.8834 | 2026-09-22 13:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 277.4 |
| 5abc9ac9-f828-34e1-93c6-b0fa7064847b | -7.146 | -48.4352 | 2026-09-22 13:30:00 | GOES-19 | CARMOLÂNDIA | TOCANTINS | Brasil | 1703883 | 17 | 33 | nan | nan | nan | Cerrado | 174.6 |
| a31975b4-e6cd-3966-8c9c-38a798b33eef | -11.3416 | -51.3817 | 2026-09-22 13:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 128.1 |
| 46572e55-45ba-3748-918d-59c512d22989 | -10.5745 | -46.7521 | 2026-09-22 13:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 73.0 |
| ff33a361-dd9b-3010-b8cf-f2f1eaa427f9 | -7.0349 | -44.6625 | 2026-09-22 13:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 172.7 |
| 6ac30064-dd7d-3e18-8c1d-674d84084e1b | -12.9276 | -51.0076 | 2026-09-22 13:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 99.9 |
| b42a0864-13da-337c-bdd6-067697549b30 | -9.257 | -46.1873 | 2026-09-22 13:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 81.6 |
| 5c96c463-4d7c-34ad-a90c-7a7536f35c96 | -14.6878 | -45.6762 | 2026-09-22 13:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 198.8 |
| 0d180ee6-8bb6-3c7c-ac69-addfed2ddba5 | -9.9064 | -48.443 | 2026-09-22 13:30:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 73.4 |
| 6564be51-50d5-376a-b567-d0629c442209 | -9.8872 | -48.4669 | 2026-09-22 13:30:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 73.7 |
| cb181529-849c-3796-8a20-b779a59cfbb9 | -12.3484 | -50.1779 | 2026-09-22 13:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 94.5 |
| b4a66a6f-fca9-3385-be28-c8e5d4d533bd | -10.6097 | -53.9697 | 2026-09-22 13:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 116.0 |
| b88241ff-e3aa-308a-ba4d-d6e4702d2185 | -10.5908 | -53.9713 | 2026-09-22 13:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 110.1 |
| b7cdb16e-d4b2-3160-a7b6-87a49eeb4777 | -11.3229 | -51.3626 | 2026-09-22 13:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 116.3 |
| e5756da4-e952-3612-835b-8e9335701213 | -11.3606 | -51.3797 | 2026-09-22 13:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 123.7 |
| 2dd6f358-2954-38fa-8843-32729bed82f9 | -14.6018 | -52.0506 | 2026-09-22 13:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 89.2 |
| d5490308-e4fb-3205-9e7b-066e508708d0 | -9.6108 | -43.9477 | 2026-09-22 13:30:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 102.8 |
| f31877b3-3d08-3e84-8326-379f97ca02f9 | -3.4599 | -59.54 | 2026-09-22 13:30:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 5ace9ec1-4d2a-3e70-bd2e-dd43ce8382b0 | -11.4213 | -47.338 | 2026-09-22 13:30:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 85.7 |
| ad938a38-0a34-3409-b1d1-ebcc1ad4d805 | -6.3619 | -55.8433 | 2026-09-22 13:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 54.6 |
| b75c8c35-725e-3f98-bba0-64da8ad2defd | -9.788 | -46.0819 | 2026-09-22 13:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 69.4 |
| 6cdee987-c05d-3cd9-af8a-eb3cc0b3704a | -3.3367 | -57.8673 | 2026-09-22 13:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 60.0 |
| d3144bff-8f1d-366d-9258-83f2aa5164ad | -12.4208 | -47.0002 | 2026-09-22 13:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 118.4 |
| 53c1a954-cfdd-3612-85d7-5b74e725dc23 | -9.2383 | -46.1668 | 2026-09-22 13:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 72.5 |
| b2144176-edc4-3d8d-8c7c-2288dee0f4ac | -10.5906 | -53.9918 | 2026-09-22 13:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 78.4 |
| a5d00e21-f511-32a0-8a63-1fb235530013 | -6.9414 | -42.907 | 2026-09-22 13:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 385.5 |
| b84fec22-b1e8-3c7e-af59-2fc2afa642bf | -10.4539 | -51.3038 | 2026-09-22 13:30:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 84.7 |
| 5ebd9eb1-9f3e-3fc9-ab23-7cfad45be029 | -10.4536 | -51.325 | 2026-09-22 13:30:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 128.1 |
| ef63954d-1af1-35cb-ad3f-d2983215e470 | -12.1458 | -47.3974 | 2026-09-22 13:30:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 99.1 |
| 70f92bd3-c482-36f0-b510-a548d20c2b90 | -7.0164 | -44.6413 | 2026-09-22 13:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 147.5 |
| 487337ff-b69b-3e1a-a899-d46b293bd0ea | -3.6764 | -60.5649 | 2026-09-22 13:30:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 65.4 |


[Clique aqui para ver as próximas entradas](README129.md)
