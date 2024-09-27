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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fdd0c2ed-a77a-3c98-889e-bfb213da5d53 | -10.5556 | -51.089699 | 2024-09-27 00:34:38 | METOP-B | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 851f4bfb-64a5-3bdf-b3fd-a312ec01650f | -10.4676 | -50.7248 | 2024-09-27 00:34:38 | METOP-B | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 2441fd74-994b-3b41-8fe4-0ef507558c33 | -10.4694 | -50.7332 | 2024-09-27 00:34:38 | METOP-B | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 1cb18ea8-eafd-338b-9b05-43ba22c8d920 | -10.473 | -50.749901 | 2024-09-27 00:34:38 | METOP-B | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| ae6b55c6-6d89-3dbb-afc2-1bcb76fdc7ca | -10.4748 | -50.758301 | 2024-09-27 00:34:38 | METOP-B | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| ce5b778e-38d9-3248-95be-51213325c573 | -10.4873 | -50.8172 | 2024-09-27 00:34:38 | METOP-B | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 284c27bb-2140-3018-8343-f3bc95f4da09 | -10.4891 | -50.8256 | 2024-09-27 00:34:38 | METOP-B | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 304dc0f1-fdd8-397d-b856-e6b8e53fc400 | -10.5458 | -51.091801 | 2024-09-27 00:34:38 | METOP-B | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 523d1c0b-3127-38bf-bd71-2d2599c701d3 | -10.4614 | -50.743599 | 2024-09-27 00:34:38 | METOP-B | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| d6b25ec1-2a4c-3c27-bcfc-75ca551226ab | -10.4632 | -50.751999 | 2024-09-27 00:34:38 | METOP-B | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 54cf10f4-31e6-3a34-b9fa-218a73f6d400 | -10.465 | -50.760399 | 2024-09-27 00:34:38 | METOP-B | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| c7e8476a-8cef-3b64-b06e-3f301e137d39 | -10.4757 | -50.810799 | 2024-09-27 00:34:38 | METOP-B | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 60959184-f3a4-3262-a3ff-131000a73a7c | -10.536 | -51.093899 | 2024-09-27 00:34:38 | METOP-B | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f78893af-08d2-38bb-b734-063b14749dc7 | -10.5378 | -51.102699 | 2024-09-27 00:34:38 | METOP-B | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| db8d1e06-2237-395d-bb9b-6638dea88d68 | -10.4552 | -50.7626 | 2024-09-27 00:34:38 | METOP-B | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| d684f618-4221-335c-8400-96fe8835a06e | -10.457 | -50.770901 | 2024-09-27 00:34:38 | METOP-B | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 2634a005-3bed-3589-b136-5e85452376f1 | -10.4588 | -50.779301 | 2024-09-27 00:34:38 | METOP-B | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 78a0d05e-9311-335f-872a-8b3e94145ea9 | -10.4606 | -50.787701 | 2024-09-27 00:34:38 | METOP-B | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 7d654381-58db-3013-bc9e-57e3676123ee | -10.4624 | -50.796101 | 2024-09-27 00:34:38 | METOP-B | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e22ff285-7a4c-3ca5-bb49-96291eabd561 | -10.4641 | -50.8046 | 2024-09-27 00:34:38 | METOP-B | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 98b4706a-67fc-35e7-ae5b-31507b013859 | -10.5299 | -51.113499 | 2024-09-27 00:34:38 | METOP-B | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e8c0a5de-e2d1-3bda-bbdf-cebbc22fb536 | -8.2966 | -41.4188 | 2024-09-27 00:34:39 | METOP-B | QUEIMADA NOVA | PIAUÍ | Brasil | 2208650 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| e572173f-3ebf-3b9b-9cec-a93955313f68 | -8.2869 | -41.4212 | 2024-09-27 00:34:39 | METOP-B | SÃO FRANCISCO DE ASSIS DO PIAUÍ | PIAUÍ | Brasil | 2209658 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| e03ab45f-c0d9-36e2-9a6a-a9e1380b14ab | -8.2901 | -41.434601 | 2024-09-27 00:34:39 | METOP-B | QUEIMADA NOVA | PIAUÍ | Brasil | 2208650 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 8d62aa1a-cc6f-3e9e-9f7d-9d313ab8d982 | -10.5219 | -51.124298 | 2024-09-27 00:34:39 | METOP-B | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a3398470-669b-343f-9a21-1cfa8bb5aee8 | -11.1378 | -54.1497 | 2024-09-27 00:34:39 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| fb6976a7-a2d4-3c4c-8c46-45e08bda94c7 | -11.1406 | -54.163399 | 2024-09-27 00:34:39 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| dade77fc-7899-37ee-8e63-a3429b6e6cc0 | -10.5042 | -51.137299 | 2024-09-27 00:34:39 | METOP-B | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 01a6c99b-be32-37c6-b8fb-78bc9974e01c | -11.1281 | -54.1516 | 2024-09-27 00:34:39 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d54bb9a8-7b85-3aad-9b2b-90b880fd481c | -11.1309 | -54.165298 | 2024-09-27 00:34:39 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 65afd9e8-5f73-3d9b-b842-d0121cb8c309 | -10.4963 | -51.148201 | 2024-09-27 00:34:39 | METOP-B | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| edfa1195-8076-37ee-8c25-afde7fbad81c | -10.4865 | -51.150299 | 2024-09-27 00:34:39 | METOP-B | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4254ed61-da92-3ed6-aeed-5301a07acef8 | -10.4884 | -51.1591 | 2024-09-27 00:34:39 | METOP-B | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a411c8a6-d502-3192-b33c-1748412e5dd6 | -10.4804 | -51.169998 | 2024-09-27 00:34:39 | METOP-B | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 318054be-13c5-398f-8f14-657b4732611c | -10.4823 | -51.178799 | 2024-09-27 00:34:39 | METOP-B | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 392bf718-3338-3054-b0b2-5cd8ed174d4f | -10.4842 | -51.187599 | 2024-09-27 00:34:39 | METOP-B | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| dd5c557b-6325-3a75-9bca-b8db29839ac6 | -10.486 | -51.1964 | 2024-09-27 00:34:39 | METOP-B | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e8c3d61e-7f23-3e73-9628-03286789febf | -10.4879 | -51.2052 | 2024-09-27 00:34:39 | METOP-B | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 10706b4c-1931-3561-98c1-375836dc47f8 | -10.4898 | -51.214001 | 2024-09-27 00:34:39 | METOP-B | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b36af267-df7e-32e8-8943-adb817d980c8 | -10.4917 | -51.2229 | 2024-09-27 00:34:39 | METOP-B | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 62905a17-844f-34b4-b86f-39884a3afc65 | -11.0109 | -53.923901 | 2024-09-27 00:34:40 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e77379c1-399e-3f0c-b004-7807e957a776 | -10.1552 | -49.987701 | 2024-09-27 00:34:41 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a5d585ac-5008-3e2d-8051-a6914b1d17ec | -10.1454 | -49.989899 | 2024-09-27 00:34:41 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5e791238-ec68-38a4-b58b-40e5202b2032 | -10.1471 | -49.997601 | 2024-09-27 00:34:41 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| faf7c1ad-42f2-3ba2-84f9-cdede8d51671 | -10.1356 | -49.992001 | 2024-09-27 00:34:41 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b0ae6ef0-5216-3ddf-ab21-76bd56a09149 | -10.1373 | -49.999802 | 2024-09-27 00:34:41 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 36481c6f-a56a-3a7c-ada9-6ff6b9b3ab7f | -10.139 | -50.0075 | 2024-09-27 00:34:41 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 870f8ee9-e810-3949-a110-59279e4cce27 | -10.1258 | -49.994202 | 2024-09-27 00:34:41 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7d5385ee-a09d-34a9-80db-2463c3c38012 | -10.1275 | -50.0019 | 2024-09-27 00:34:41 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2399b819-fed0-36af-8e5f-c3a448fa14b2 | -10.116 | -49.9963 | 2024-09-27 00:34:41 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e9834e18-a140-3c21-b641-f8e2ea91e6ae | -10.0776 | -50.150902 | 2024-09-27 00:34:42 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d66304cb-adb1-3a0a-b907-e830a6801c0c | -10.0793 | -50.158699 | 2024-09-27 00:34:42 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7d9398a0-040f-3519-89af-55ab16505f32 | -10.9287 | -54.220798 | 2024-09-27 00:34:42 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 70aa5311-a185-3c18-8d78-259132a361fb | -10.9314 | -54.2346 | 2024-09-27 00:34:42 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8042ec14-b11a-317c-9db5-9b6024fc67ea | -10.9342 | -54.248402 | 2024-09-27 00:34:42 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0220c3b6-b76f-3f3c-83de-7575370e4627 | -10.8172 | -53.721298 | 2024-09-27 00:34:43 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0a4591b0-5da1-38f3-b557-79e396fb25e9 | -10.919 | -54.222801 | 2024-09-27 00:34:43 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e469c8ee-5aa2-35e3-afa2-f6df3a0290c5 | -10.9217 | -54.236599 | 2024-09-27 00:34:43 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 335f6d73-5efe-3958-a5c4-5867c5ecad95 | -10.9245 | -54.250401 | 2024-09-27 00:34:43 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 25a5b58b-1ce5-329f-b480-27b2cfa4361a | -10.0609 | -50.597 | 2024-09-27 00:34:44 | METOP-B | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a4d9fdd8-8fff-3896-96d7-060eaa616a89 | -9.8975 | -50.125 | 2024-09-27 00:34:45 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5994056f-f5d2-3c51-8623-06be9b37ca4c | -7.7806 | -41.075901 | 2024-09-27 00:34:46 | METOP-B | JACOBINA DO PIAUÍ | PIAUÍ | Brasil | 2205151 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 864a1ce2-3a1b-3e2a-9b9e-9847e986957a | -9.8748 | -50.162498 | 2024-09-27 00:34:46 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c53c7900-f3de-3811-9e63-b732021181a2 | -8.0621 | -42.884899 | 2024-09-27 00:34:48 | METOP-B | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| d84d01c9-55af-3422-9f67-fa7c44fe28d5 | -10.6175 | -54.591702 | 2024-09-27 00:34:49 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0a65d20e-0adb-3b01-bbe3-c25b9f839c06 | -10.4228 | -53.6847 | 2024-09-27 00:34:49 | METOP-B | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f2d91a9b-05d1-3772-9d1d-06df7a7bd5c4 | -10.4106 | -53.674301 | 2024-09-27 00:34:49 | METOP-B | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c4e6a525-60b3-384f-a904-64bf91c6cf88 | -10.4131 | -53.686699 | 2024-09-27 00:34:49 | METOP-B | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 17c2d2ee-032d-3c37-a73f-4aba8294b9d3 | -10.3838 | -53.692799 | 2024-09-27 00:34:50 | METOP-B | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 69bf59ec-74fb-3db4-ae07-db9284fac5b3 | -9.6097 | -50.1231 | 2024-09-27 00:34:50 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c2cc5a51-129b-3915-a7be-5c02cc916bb0 | -9.6114 | -50.130798 | 2024-09-27 00:34:50 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3aa114d2-1f2c-3dad-8ded-28f812b314b8 | -9.613 | -50.1385 | 2024-09-27 00:34:50 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 95705b05-d646-3617-af64-0c269c5eacb3 | -10.3771 | -53.759201 | 2024-09-27 00:34:50 | METOP-B | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 92013d81-aa76-3c54-8b4f-4920964ad799 | -8.9241 | -47.0783 | 2024-09-27 00:34:50 | METOP-B | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 858d6b05-0902-3fce-b94a-f327f6b8e9fc | -9.5982 | -50.1175 | 2024-09-27 00:34:50 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0d4a4bf7-f5ed-3f9e-8aa6-442589565995 | -9.5999 | -50.125301 | 2024-09-27 00:34:50 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2ee4cdb4-e260-39de-97b5-f1a9600b8a17 | -9.6015 | -50.132999 | 2024-09-27 00:34:50 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4f180c50-87ce-3337-8ab4-20ddc34865d9 | -9.6032 | -50.140701 | 2024-09-27 00:34:50 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5ebc5531-6de2-3901-af39-e9693b7fec50 | -9.6049 | -50.148399 | 2024-09-27 00:34:50 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7f91605f-ce07-3e3d-8067-687f34c3172d | -10.3647 | -53.748699 | 2024-09-27 00:34:50 | METOP-B | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8584509c-197e-37b8-b60a-077421f6e3a1 | -10.3673 | -53.761299 | 2024-09-27 00:34:50 | METOP-B | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| eac379ce-acd1-3f27-bf66-a6dc99a87e68 | -10.3698 | -53.773899 | 2024-09-27 00:34:50 | METOP-B | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 718a2422-7ca3-397d-8be4-3bae2092e870 | -10.3724 | -53.786499 | 2024-09-27 00:34:50 | METOP-B | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 74191caa-f97b-3581-9bbc-02fca86a416c | -9.5884 | -50.119598 | 2024-09-27 00:34:50 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d69119b3-b57f-3093-bbe9-f263e551349d | -9.5901 | -50.127399 | 2024-09-27 00:34:50 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bcae181f-152f-3fa2-bb49-c313111a0068 | -9.5917 | -50.135101 | 2024-09-27 00:34:50 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7e5b0a31-815f-38d2-940a-b4c0c55dc361 | -10.3575 | -53.763302 | 2024-09-27 00:34:50 | METOP-B | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| bb9de807-d1ec-343e-9f50-ee7fbc438414 | -10.3601 | -53.775902 | 2024-09-27 00:34:50 | METOP-B | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 53568f91-dca4-3a0f-9388-0132cc62ca9b | -9.5652 | -50.060398 | 2024-09-27 00:34:50 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4a3864b7-312b-335f-8322-23e1d097746c | -9.5786 | -50.121799 | 2024-09-27 00:34:50 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4171f982-d834-3d92-99e4-a8311ee079ff | -9.5803 | -50.129601 | 2024-09-27 00:34:50 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b8bec4c6-bb1e-3e73-85f0-0a3b11d5faa0 | -7.8606 | -42.688801 | 2024-09-27 00:34:51 | METOP-B | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 20f064cd-2a21-3250-af93-4e15f0d1bfad | -9.5609 | -50.182301 | 2024-09-27 00:34:51 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8e0de269-fd69-37b0-a54b-3556bad3bf22 | -9.5495 | -50.176701 | 2024-09-27 00:34:51 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 373287b3-4928-335e-b570-6f873ffc47de | -9.5511 | -50.184399 | 2024-09-27 00:34:51 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| eb9122e2-bf57-3de1-83b1-01d8cd54b8f9 | -9.5528 | -50.192101 | 2024-09-27 00:34:51 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 63990500-85a1-3b19-81f1-beb4d4607ac8 | -9.5545 | -50.199902 | 2024-09-27 00:34:51 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cb41c4ab-25e0-3049-a6be-fcd0045f8411 | -9.5429 | -50.194199 | 2024-09-27 00:34:51 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a65b63e3-eb50-359d-856b-3ff372099df7 | -9.5331 | -50.1964 | 2024-09-27 00:34:51 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6c327242-2417-3985-8452-f1e3a5b8b442 | -9.4032 | -50.0238 | 2024-09-27 00:34:53 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README12.md)
