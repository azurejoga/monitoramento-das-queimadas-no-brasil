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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| db1d7304-8ea0-345c-b9d0-c3503a5a0b60 | -10.1796 | -49.489399 | 2025-08-13 00:12:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c2e5cd2d-c6b2-3784-b071-35009a77976f | -7.458 | -59.816601 | 2025-08-13 00:12:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b89024f4-767e-3dd9-8a53-926d0152a024 | -7.0537 | -44.345299 | 2025-08-13 00:12:00 | METOP-B | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e3b07de5-166a-3dc7-9c03-2d03cbd69b8b | -11.0064 | -45.204102 | 2025-08-13 00:12:00 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 409abc19-cf2d-36a4-ac50-bf34913811f6 | -10.8962 | -50.536999 | 2025-08-13 00:12:00 | METOP-B | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0c1115e1-680c-3197-8e27-70acef61c6a2 | -6.279 | -53.604801 | 2025-08-13 00:12:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d62d34ae-22da-3fcb-ab80-e330d667a187 | -6.9282 | -59.0835 | 2025-08-13 00:12:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1b0ac61c-931e-32e9-8f16-0d32ba3a44e0 | -7.1328 | -60.042999 | 2025-08-13 00:12:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1a8c126e-6b12-3285-8b0a-05b26eae1f47 | -4.6234 | -47.410099 | 2025-08-13 00:12:00 | METOP-B | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 8faaeca3-6c7e-3c57-995c-7e3b78f915e3 | -16.600201 | -47.021599 | 2025-08-13 00:12:00 | METOP-B | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| e90bb28d-6f15-39ab-b7b3-88345aa4b28e | -11.9819 | -45.140499 | 2025-08-13 00:12:00 | METOP-B | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 6d52b7f5-1d5e-3d74-8c57-a649b30ecfa4 | -12.4282 | -48.681599 | 2025-08-13 00:12:00 | METOP-B | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d531f56b-7962-3986-bbef-dea02ac01cd1 | -12.5502 | -47.025299 | 2025-08-13 00:12:00 | METOP-B | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 307b93fc-e4e6-37a1-a09a-b1c803266990 | -12.5234 | -46.9506 | 2025-08-13 00:12:00 | METOP-B | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 63c13989-29a5-3067-ad6d-5bfaa3358802 | -6.8979 | -59.033798 | 2025-08-13 00:12:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 36e7f5e2-28c9-300d-b927-3ce26b212af1 | -9.7124 | -49.465698 | 2025-08-13 00:12:00 | METOP-B | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6e92469b-6044-395b-9624-f42548303c64 | -12.0889 | -45.746201 | 2025-08-13 00:12:00 | METOP-B | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d6fe5c1a-8d07-3c29-8cdc-e5f81d9645d3 | -15.7389 | -49.469898 | 2025-08-13 00:12:00 | METOP-B | JARAGUÁ | GOIÁS | Brasil | 5211800 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 76a078a6-a282-367a-9120-4dc0ab60fd11 | -12.5249 | -46.9576 | 2025-08-13 00:12:00 | METOP-B | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a9bfc1fc-3065-3b4f-bc4b-857895495cf4 | -15.5552 | -43.141499 | 2025-08-13 00:12:00 | METOP-B | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | nan |
| 272ef84f-1f22-3209-bc5f-ccf430e8f564 | -12.5574 | -46.964802 | 2025-08-13 00:12:00 | METOP-B | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5138e097-2a0c-375e-a2ff-0490de698786 | -12.1479 | -48.003899 | 2025-08-13 00:12:00 | METOP-B | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| de1bbaae-feb4-3a3d-927d-d5d211b556c8 | -6.9034 | -59.060501 | 2025-08-13 00:12:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1a6136ca-9d14-3dde-8652-d8342d48a156 | -12.5363 | -46.962299 | 2025-08-13 00:12:00 | METOP-B | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3a528eee-92fc-37d0-81f7-602900ccd3e6 | -9.3556 | -40.684299 | 2025-08-13 00:12:00 | METOP-B | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | nan |
| 5aa3ab85-2e73-3cdb-80c2-66d95dfd4359 | -12.5409 | -46.983299 | 2025-08-13 00:12:00 | METOP-B | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4b5989d3-2b09-3e07-b2d5-8ca3278e00e9 | -12.5487 | -47.018299 | 2025-08-13 00:12:00 | METOP-B | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| eff6b757-fdd0-3ae4-8b6a-514d4ca07099 | -13.4325 | -44.493599 | 2025-08-13 00:12:00 | METOP-B | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 80af7c52-b50f-3915-bd9f-47a12c4a2532 | -13.119 | -46.851398 | 2025-08-13 00:12:00 | METOP-B | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 30f92569-ad9c-365d-b7cf-9c95e300b7b1 | -6.8592 | -59.0415 | 2025-08-13 00:12:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| dfbbd21a-aa20-3bea-9329-43151ea72ffc | -10.974 | -49.555901 | 2025-08-13 00:12:00 | METOP-B | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e767d4a0-836d-3e3e-a827-958d16b6acfb | -6.9227 | -59.056599 | 2025-08-13 00:12:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 76841d95-23ba-34be-bc6c-664c87e39f06 | -10.349 | -50.806499 | 2025-08-13 00:12:00 | METOP-B | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 5b9c5e47-b8e0-32d1-8202-d350fee7b97f | -6.1161 | -44.701599 | 2025-08-13 00:12:00 | METOP-B | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 661b8e06-d798-3d69-b402-a3ea4c7d0460 | -12.3294 | -46.035599 | 2025-08-13 00:12:00 | METOP-B | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| dfb1dd52-ff72-3366-b45e-a584f1cb90e0 | -7.1168 | -60.013401 | 2025-08-13 00:12:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c7a2a664-2e9f-3b29-abd6-8a0f614f30cf | -13.4307 | -44.485901 | 2025-08-13 00:12:00 | METOP-B | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 58f21352-7d28-342b-929c-c44d7d4eebe8 | -8.9778 | -40.614101 | 2025-08-13 00:12:00 | METOP-B | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | nan |
| 9fd8772c-840a-308e-8266-3c6e9c2f6da5 | -15.5474 | -43.152302 | 2025-08-13 00:12:00 | METOP-B | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | nan |
| 4a808d5e-6efd-330c-b4bb-1a0cd4152de3 | -18.5287 | -46.049 | 2025-08-13 00:12:00 | METOP-B | VARJÃO DE MINAS | MINAS GERAIS | Brasil | 3170750 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| ef20dc7e-7843-3414-b47d-39ec0fb10394 | -12.5662 | -47.050999 | 2025-08-13 00:12:00 | METOP-B | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 076f5616-686f-36fb-b96b-a7b56f983822 | -22.389 | -45.459999 | 2025-08-13 00:12:00 | METOP-B | ITAJUBÁ | MINAS GERAIS | Brasil | 3132404 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 30e85c23-6092-300a-834a-ad3ceba8b1fa | -12.5425 | -46.990299 | 2025-08-13 00:12:00 | METOP-B | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8ec3dff7-eb08-3cb5-ba1c-0d801981108d | -18.6117 | -43.902699 | 2025-08-13 00:12:00 | METOP-B | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| e234b197-8daf-3352-b8f7-2eec34d38546 | -12.1479 | -44.919601 | 2025-08-13 00:12:00 | METOP-B | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c3df3d96-ab3e-3eab-9024-1c44e7de8de3 | -18.6231 | -43.907799 | 2025-08-13 00:12:00 | METOP-B | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| a4c61079-709d-31fe-9a8b-ffebcbb0eb75 | -7.0883 | -59.9217 | 2025-08-13 00:12:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ce1d5243-398f-351d-b1ad-5e1c2cf4193e | -12.5347 | -46.955299 | 2025-08-13 00:12:00 | METOP-B | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8001fa44-4870-346f-9867-7fc24c13d2be | -7.8744 | -47.252399 | 2025-08-13 00:12:00 | METOP-B | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 526a937a-1a8c-34b5-957f-3b256beb90a8 | -5.4417 | -43.573799 | 2025-08-13 00:12:00 | METOP-B | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 65506cb0-0a0c-3862-8202-c70eaefc6161 | -12.3228 | -46.052101 | 2025-08-13 00:12:00 | METOP-B | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 0f8f0467-a590-37a6-83ee-a76f5e1eaae4 | -22.3792 | -45.462399 | 2025-08-13 00:12:00 | METOP-B | ITAJUBÁ | MINAS GERAIS | Brasil | 3132404 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| beb196a4-4270-3b0b-a1d7-a13400e1ea65 | -10.2458 | -50.226398 | 2025-08-13 00:12:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7a43e2bd-5fab-38e5-aad9-d965cd2e9d18 | -11.9934 | -45.145599 | 2025-08-13 00:12:00 | METOP-B | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| bb69b7d1-4484-3f72-bbba-da0fe60891b6 | -8.3821 | -49.3494 | 2025-08-13 00:12:00 | METOP-B | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4f2e8ee8-64a6-38f3-b62a-2e624ec0bb0b | -5.7375 | -51.673 | 2025-08-13 00:12:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8a935697-37e9-3baa-b8d3-9697b3355059 | -10.2424 | -50.210201 | 2025-08-13 00:12:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d991aa37-bf98-38cb-9402-1fed46e1454f | -16.975 | -48.415298 | 2025-08-13 00:12:00 | METOP-B | ORIZONA | GOIÁS | Brasil | 5215306 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| d40497a2-cc3b-3727-aa50-5077c2156f69 | -4.2189 | -49.780499 | 2025-08-13 00:12:00 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e800a7f8-067e-3a72-92d0-31c814efbf2c | -4.9519 | -47.587101 | 2025-08-13 00:12:00 | METOP-B | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 1a9a85b6-46fc-38ce-8c01-e24fee90823d | -21.140301 | -49.0886 | 2025-08-13 00:12:00 | METOP-B | ELISIÁRIO | SÃO PAULO | Brasil | 3514924 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 2634db03-d4ff-312e-97ae-f42962c17064 | -9.8547 | -44.682899 | 2025-08-13 00:12:00 | METOP-B | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 744c62e6-0ecf-3081-8bc8-35ce8ce8d0f2 | -10.7042 | -48.8307 | 2025-08-13 00:12:00 | METOP-B | OLIVEIRA DE FÁTIMA | TOCANTINS | Brasil | 1715507 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 715f7809-f818-3e8d-910e-aaa923c8f448 | -9.9925 | -47.8372 | 2025-08-13 00:12:00 | METOP-B | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2bdaaf33-edf1-311c-808f-4bf8ee7d997d | -6.8992 | -59.089298 | 2025-08-13 00:12:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 064764e8-b98c-356e-8904-7249a7ec2ce9 | -9.2016 | -59.575401 | 2025-08-13 00:12:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ca4f8258-dbde-397d-939b-45a1cf3bb1f7 | -7.1232 | -60.044899 | 2025-08-13 00:12:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 24c45428-3ffa-3a43-9456-446014ded4da | -6.3105 | -51.383499 | 2025-08-13 00:12:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 90433386-6e47-3a2d-9b0e-9b849479ed44 | -10.0816 | -50.321201 | 2025-08-13 00:12:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| bf4e5333-8b96-371b-9c85-0bd7d9a5c56e | -7.1136 | -60.046799 | 2025-08-13 00:12:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c0e9e376-e73c-33dd-9fc2-7838f8b77766 | -4.2272 | -47.207699 | 2025-08-13 00:12:00 | METOP-B | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d1ff84b3-b075-3190-99aa-6c1bd4de9f91 | -12.559 | -46.971802 | 2025-08-13 00:12:00 | METOP-B | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ce9dae02-9019-3190-ab8f-a9a542c4dde5 | -22.390499 | -45.467499 | 2025-08-13 00:12:00 | METOP-B | ITAJUBÁ | MINAS GERAIS | Brasil | 3132404 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 20a0e278-e3d4-3b44-bfd3-f9986b582398 | -21.138399 | -49.0788 | 2025-08-13 00:12:00 | METOP-B | ELISIÁRIO | SÃO PAULO | Brasil | 3514924 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| ecaec133-6b0b-3740-b5d3-2329c38b96ac | -16.9172 | -48.136398 | 2025-08-13 00:12:00 | METOP-B | ORIZONA | GOIÁS | Brasil | 5215306 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| c8435502-9207-3f35-97fb-bdb2b7af029a | -11.9083 | -52.511101 | 2025-08-13 00:12:00 | METOP-B | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1ba89753-8a6f-391e-8f01-e65e5c355ce4 | -7.0946 | -59.952702 | 2025-08-13 00:12:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3550d17a-cd5b-3e6e-85e2-27d12a30bded | -12.544 | -46.997299 | 2025-08-13 00:12:00 | METOP-B | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1904067d-7259-3a5c-a62d-7f602fd14bd2 | -5.4393 | -43.563499 | 2025-08-13 00:12:00 | METOP-B | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c518e32b-8a83-3ba0-9d2c-b11c2528b4f2 | -16.318199 | -52.894798 | 2025-08-13 00:12:00 | METOP-B | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| ca3a3b80-ecbf-327c-a8bd-73957aff3cde | -12.3114 | -46.047298 | 2025-08-13 00:12:00 | METOP-B | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 06baf993-d693-330a-921b-7074e84a3cc4 | -4.2158 | -47.202702 | 2025-08-13 00:12:00 | METOP-B | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 9492f4c5-eea6-3373-915a-19fc00651d56 | -4.2174 | -49.773499 | 2025-08-13 00:12:00 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 628e27e2-c7f2-3afa-8f1d-372d2af6bd56 | -9.714 | -49.473202 | 2025-08-13 00:12:00 | METOP-B | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| bd346087-0604-30a5-b917-96d287e99411 | -10.9625 | -49.550301 | 2025-08-13 00:12:00 | METOP-B | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 24301372-78fb-3443-b73d-d0dcf25dd813 | -6.5409 | -44.002499 | 2025-08-13 00:12:00 | METOP-B | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 33ea3cac-6564-3768-bcc6-85095b3c64a8 | -12.3196 | -46.037899 | 2025-08-13 00:12:00 | METOP-B | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b218c282-04a2-31a0-84af-e557070e8db3 | -12.528 | -46.9715 | 2025-08-13 00:12:00 | METOP-B | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e8f8c11e-895b-3052-8803-6a4f6eb14df1 | -19.086901 | -48.137402 | 2025-08-13 00:12:00 | METOP-B | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| cf1bdb50-c302-36ed-90fe-b213a3c86f1b | -16.740999 | -47.5877 | 2025-08-13 00:12:00 | METOP-B | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 4092ba10-2952-350b-b6d8-2c2a7ba5bd85 | -11.7632 | -48.172298 | 2025-08-13 00:12:00 | METOP-B | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b022c4a7-8f83-37d0-a1cb-400162884c88 | -12.5445 | -46.953098 | 2025-08-13 00:12:00 | METOP-B | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e48ea942-a9df-311b-9c5c-0c580d388c21 | -12.313 | -46.054401 | 2025-08-13 00:12:00 | METOP-B | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e0ce0db4-fcc7-349b-accc-68607f73eb46 | -18.052999 | -47.933498 | 2025-08-13 00:12:00 | METOP-B | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 26a7fa67-a3ea-3660-a7c0-94f88d3dbbf8 | -6.9185 | -59.0854 | 2025-08-13 00:12:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 23aa5be5-0b89-3489-9b2b-02aeaa2f460d | -12.6895 | -46.956799 | 2025-08-13 00:12:00 | METOP-B | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b187c394-cbe5-3748-a7c8-13ade7ccdc98 | -8.6276 | -50.002701 | 2025-08-13 00:12:00 | METOP-B | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d95eae93-6883-3caf-9f40-1125b4c85342 | -14.1116 | -44.306 | 2025-08-13 00:12:00 | METOP-B | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 3eba232f-bd53-376a-b0d1-80277d046f6d | -12.5786 | -46.9673 | 2025-08-13 00:12:00 | METOP-B | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 79cc96cd-6450-331d-bf49-331442c01a1c | -16.7425 | -47.595299 | 2025-08-13 00:12:00 | METOP-B | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README5.md)
