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

## Dados Diários - Página 90

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4a1ac85c-855f-3ec9-8a6a-9e41770dd8f2 | -10.12099 | -50.24225 | 2026-09-24 11:25:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 196.1 |
| fcf6d328-4fae-33a0-b5b7-8a95d3c4bd7c | -8.80465 | -47.78375 | 2026-09-24 11:25:00 | TERRA_M-M | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 22.3 |
| 9bc32ebd-b94a-321e-a710-330caaca759e | -9.53768 | -45.35752 | 2026-09-24 11:25:00 | TERRA_M-M | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 22.5 |
| e36ff5fa-eb5a-376a-b1e6-57d580dc47ed | -8.76546 | -45.64477 | 2026-09-24 11:25:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 44de5067-599f-35ba-a4ae-a5100364de43 | -8.78622 | -45.83841 | 2026-09-24 11:25:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 4ec69214-5212-3ddc-96dd-82233461a404 | -10.07097 | -50.21109 | 2026-09-24 11:25:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 25.1 |
| f0351620-6d17-3c5c-bb3c-ff9712b1ba4e | -10.09778 | -50.21551 | 2026-09-24 11:25:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 98.6 |
| bdb2121c-effc-3145-b762-1ea1332330b1 | -10.12459 | -50.21995 | 2026-09-24 11:25:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 83.6 |
| 4a6b7ba4-8524-3411-b494-3c141701e766 | -10.44361 | -45.10955 | 2026-09-24 11:25:00 | TERRA_M-M | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 14.2 |
| edd03af5-ce66-39da-8d1f-49b4fbfae589 | -8.5861 | -47.24981 | 2026-09-24 11:25:00 | TERRA_M-M | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 12.1 |
| b10d4f86-50bb-3636-b133-c7a54b04d4bd | -9.54712 | -45.35881 | 2026-09-24 11:25:00 | TERRA_M-M | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| e5c3ebb4-a1c4-316b-866c-9fb52ecceea6 | -7.93099 | -44.86337 | 2026-09-24 11:25:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 46.6 |
| 81245c8b-a34e-31af-aa7b-835ba2ea60bf | -7.28304 | -45.5495 | 2026-09-24 11:25:00 | TERRA_M-M | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 136.9 |
| 5977bf27-a306-3d2f-8964-4c3dfb67d180 | -8.7638 | -45.65575 | 2026-09-24 11:25:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 6.4 |
| ec368257-3d04-3a4d-873a-cc44ba076cb9 | -10.10143 | -50.19329 | 2026-09-24 11:25:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 213.9 |
| e3bcc0c4-6664-37ed-9578-43a8acc7e737 | -8.3049 | -44.15148 | 2026-09-24 11:25:00 | TERRA_M-M | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 52090c74-123a-3e6d-8789-f19e7455d5b9 | -10.11546 | -50.24818 | 2026-09-24 11:25:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 112.1 |
| 50a55e4c-7947-3868-939d-6bb841b90c65 | -10.10505 | -50.17117 | 2026-09-24 11:25:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 146.1 |
| 02cd80c9-2db4-32c7-964e-de2908b51054 | -7.28471 | -45.53849 | 2026-09-24 11:25:00 | TERRA_M-M | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 974d9b70-60f4-37fd-a768-c5ccecc90a80 | -9.53611 | -45.36792 | 2026-09-24 11:25:00 | TERRA_M-M | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 6a2bd835-440d-3f66-84e3-c2868f99df66 | -7.672 | -45.48513 | 2026-09-24 11:25:00 | TERRA_M-M | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 37e88d64-f6d9-3fcf-9d14-8f36c76b9169 | -8.37124 | -47.30457 | 2026-09-24 11:25:00 | TERRA_M-M | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 8836d94c-1fec-3110-8c58-129bce157b4f | -7.99551 | -44.94455 | 2026-09-24 11:25:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 1decb717-7a4e-30ea-9ec1-ebb97ad63331 | -10.57272 | -39.34992 | 2026-09-24 11:25:00 | TERRA_M-M | MONTE SANTO | BAHIA | Brasil | 2921500 | 29 | 33 | nan | nan | nan | Caatinga | 9.1 |
| 39aea061-1e04-3fae-ba35-57ca43b76a0f | -10.06498 | -50.16457 | 2026-09-24 11:25:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 78.0 |
| 82ecc20d-681c-3b48-83d5-e45cfed08c26 | -9.25987 | -46.23723 | 2026-09-24 11:25:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 0001ddfe-5c3e-3aca-8838-9ca3bed23ffd | -10.93068 | -43.85888 | 2026-09-24 11:25:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 7c837d89-3562-319c-b59b-7687e012b662 | -10.10756 | -50.24002 | 2026-09-24 11:25:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 54.6 |
| 14bb9b98-4362-3eb4-9543-84af05643e89 | -9.2581 | -46.24898 | 2026-09-24 11:25:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| bbd05f6c-ba5d-3e3b-a1e8-09553c1ac073 | -9.044 | -45.01994 | 2026-09-24 11:25:00 | TERRA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 1a4f41ba-7e5d-32da-a8fa-eea138f30b10 | -10.06634 | -50.18148 | 2026-09-24 11:25:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 664.4 |
| 3209ea33-23dc-38ea-8a7e-49f965d60284 | -9.06081 | -45.7857 | 2026-09-24 11:25:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 10.5 |
| a72a80ef-2144-3ad8-8e20-ed8251320dad | -10.0628 | -50.20371 | 2026-09-24 11:25:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 144.1 |
| e07d6641-81bf-39eb-b257-f6c7db6f4b7e | -9.26814 | -46.25014 | 2026-09-24 11:25:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 75993641-4917-3f7c-8b05-78aa13dc85d7 | -7.94037 | -44.86458 | 2026-09-24 11:25:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 13.5 |
| fc79c867-d086-3a26-956b-4c44f5bb8af4 | -9.24094 | -42.7753 | 2026-09-24 11:25:00 | TERRA_M-M | SÃO RAIMUNDO NONATO | PIAUÍ | Brasil | 2210607 | 22 | 33 | nan | nan | nan | Caatinga | 9.1 |
| 88f83d7c-8096-3e57-a12b-70b250915ec3 | -10.06128 | -50.18671 | 2026-09-24 11:25:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 480.0 |
| d91926be-d7b5-3c70-86ca-a9a717881c9c | -8.94586 | -45.67278 | 2026-09-24 11:25:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 14.1 |
| dc1c7f52-634a-3b7b-879e-807c49e601b7 | -10.08883 | -46.04829 | 2026-09-24 11:25:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 12.1 |
| c113516d-80aa-33e5-b436-0bea76484e20 | -14.17397 | -43.43604 | 2026-09-24 11:28:00 | TERRA_M-M | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Cerrado | 29.8 |
| 5f3674f6-b21d-3d06-b456-6d785ecb7ce2 | -11.66833 | -43.48578 | 2026-09-24 11:28:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 68f5af6e-52eb-32bc-ac89-ab656908e4f6 | -11.65071 | -43.48325 | 2026-09-24 11:28:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 24.3 |
| 1dc8fb5a-ea3b-3f6d-b250-b16329f918a4 | -11.9861 | -39.48005 | 2026-09-24 11:28:00 | TERRA_M-M | RIACHÃO DO JACUÍPE | BAHIA | Brasil | 2926301 | 29 | 33 | nan | nan | nan | Mata Atlântica | 8.8 |
| 4aeff59f-2dae-337d-8d0c-726591bdf038 | -11.63381 | -50.61261 | 2026-09-24 11:28:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 21.1 |
| 53589630-9a45-3efd-b0b3-9649b51518f6 | -11.64944 | -43.49218 | 2026-09-24 11:28:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 40.8 |
| 908a2c52-f4cf-35df-a832-2059a0aa2d2f | -14.75401 | -45.60821 | 2026-09-24 11:28:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 23.1 |
| 32ffaa30-6a4e-3cdc-a102-661c01f082bb | -18.72485 | -47.07381 | 2026-09-24 11:28:00 | TERRA_M-M | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 25.7 |
| 49e485a9-6f70-37ce-9637-7a0eeca60974 | -14.18282 | -43.43731 | 2026-09-24 11:28:00 | TERRA_M-M | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Cerrado | 207.7 |
| 793e4601-0aa0-36ff-97b5-99b2c1b31ddc | -11.21961 | -51.38938 | 2026-09-24 11:28:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 62.9 |
| 6b409872-225c-333c-be44-10d2b5c40c34 | -17.24669 | -48.12062 | 2026-09-24 11:28:00 | TERRA_M-M | ORIZONA | GOIÁS | Brasil | 5215306 | 52 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 06894884-85ec-3340-ae30-1338046c7d70 | -11.22399 | -51.36316 | 2026-09-24 11:28:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 147.0 |
| c3ca1da0-ec3f-3a8a-8688-75f554fdd8a3 | -18.00491 | -44.63305 | 2026-09-24 11:28:00 | TERRA_M-M | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 57.0 |
| 5eee2175-d940-3658-884e-b1881ea89b06 | -13.93304 | -41.43352 | 2026-09-24 11:28:00 | TERRA_M-M | ITUAÇU | BAHIA | Brasil | 2917201 | 29 | 33 | nan | nan | nan | Caatinga | 6.0 |
| eda85d4b-9e12-39ae-aceb-45edc9002686 | -11.79991 | -50.96307 | 2026-09-24 11:28:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 22.0 |
| d2e27b7d-608d-30e1-8df1-f68cb4898de0 | -14.75545 | -45.59862 | 2026-09-24 11:28:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 1cb16534-b63d-32b7-a0f7-4de9acaa3102 | -11.22596 | -51.37059 | 2026-09-24 11:28:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 111.7 |
| 363b6609-4121-3c49-b4cb-394a487baf18 | -12.54971 | -44.78343 | 2026-09-24 11:28:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 7.9 |
| b9e0a6d8-7c0b-3771-bdc4-1557952441c5 | -13.45521 | -46.25166 | 2026-09-24 11:28:00 | TERRA_M-M | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 2bdd30cf-4f3a-3cf3-b245-38799d2c7f4a | -18.01504 | -44.62514 | 2026-09-24 11:28:00 | TERRA_M-M | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 18.8 |
| 42387648-cd3d-39f7-8b01-b87d8297ac7c | -13.61958 | -40.64445 | 2026-09-24 11:28:00 | TERRA_M-M | MARACÁS | BAHIA | Brasil | 2920502 | 29 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 5d9f21b4-f586-3712-99da-5af7778c3cc8 | -14.63576 | -41.53524 | 2026-09-24 11:28:00 | TERRA_M-M | MAETINGA | BAHIA | Brasil | 2919959 | 29 | 33 | nan | nan | nan | Caatinga | 6.4 |
| c9f9d169-e680-3016-8c71-b77a8cda6898 | -11.62038 | -50.61034 | 2026-09-24 11:28:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 83faf693-19d4-3561-bcef-9ef6732498c1 | -12.534 | -42.17384 | 2026-09-24 11:28:00 | TERRA_M-M | IBITIARA | BAHIA | Brasil | 2913002 | 29 | 33 | nan | nan | nan | Caatinga | 6.8 |
| ccd5c0d9-6e20-3d4c-861d-6b50649f2aab | -11.65825 | -43.49345 | 2026-09-24 11:28:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 46.0 |
| 75dd3f16-5762-3b62-9869-2c3c27677361 | -12.76912 | -42.20526 | 2026-09-24 11:28:00 | TERRA_M-M | NOVO HORIZONTE | BAHIA | Brasil | 2923035 | 29 | 33 | nan | nan | nan | Caatinga | 11.3 |
| 3ecd1445-8b93-3b8a-9a13-caa7da1e5379 | -13.46303 | -46.26362 | 2026-09-24 11:28:00 | TERRA_M-M | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 4681b55a-2d6e-3a19-bf57-d19e2b8c1c16 | -17.24863 | -48.10852 | 2026-09-24 11:28:00 | TERRA_M-M | ORIZONA | GOIÁS | Brasil | 5215306 | 52 | 33 | nan | nan | nan | Cerrado | 16.3 |
| a4777feb-5d07-386f-a893-1fb52b4423fd | -15.51201 | -48.42501 | 2026-09-24 11:28:00 | TERRA_M-M | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 654b4d78-4d82-37e7-8d2a-3f53a0a40115 | -13.18442 | -42.46754 | 2026-09-24 11:28:00 | TERRA_M-M | BOTUPORÃ | BAHIA | Brasil | 2904209 | 29 | 33 | nan | nan | nan | Caatinga | 10.9 |
| 6710d0bb-016b-3368-ae39-3e73d34dc913 | -17.99739 | -44.62249 | 2026-09-24 11:28:00 | TERRA_M-M | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 24.2 |
| ed346c3b-7ccf-331b-a28c-da1b7caa207c | -11.66706 | -43.49471 | 2026-09-24 11:28:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 47.2 |
| 4087fb30-2c60-31e9-9961-dfb2024dba8f | -11.2116 | -51.36813 | 2026-09-24 11:28:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 209.0 |
| 736bba83-6320-37d3-87cb-a1f54742fd23 | -18.01373 | -44.63437 | 2026-09-24 11:28:00 | TERRA_M-M | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 31.2 |
| 3aedaa01-c8bb-3b2d-bc7c-384f7bc95f60 | -13.88541 | -45.4903 | 2026-09-24 11:28:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 25.5 |
| 91c3e884-9bc8-35f6-802c-52205e3d020f | -17.12802 | -44.77288 | 2026-09-24 11:28:00 | TERRA_M-M | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| f3b4846b-b814-38aa-9dc0-f5745a686c8e | -11.44579 | -44.19914 | 2026-09-24 11:28:00 | TERRA_M-M | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 16.1 |
| f1abb6a2-c922-394b-8c01-64e92af034e8 | -14.18154 | -43.44641 | 2026-09-24 11:28:00 | TERRA_M-M | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Cerrado | 108.5 |
| 15cffbad-ff75-34c8-8350-41efa106a01d | -14.75113 | -45.62734 | 2026-09-24 11:28:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 080f0d1d-0cba-3f8e-9a48-a9d813082c98 | -11.61216 | -50.60286 | 2026-09-24 11:28:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 44.0 |
| 22094c14-7feb-300a-8f22-0a505cbb979b | -14.7812 | -41.37984 | 2026-09-24 11:28:00 | TERRA_M-M | CARAÍBAS | BAHIA | Brasil | 2906899 | 29 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 705bf491-724e-39f5-b4c2-93d3904ad0d9 | -11.23399 | -51.39187 | 2026-09-24 11:28:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 55.6 |
| 173295e6-3b49-3a1e-88de-6379706ee209 | -11.92772 | -50.7525 | 2026-09-24 11:28:00 | TERRA_M-M | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 28.6 |
| 726e7940-3897-35f9-baca-b349caa3f75e | -14.71143 | -45.5854 | 2026-09-24 11:28:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 8ad7faf9-827b-360b-a027-3e04336bafcc | -11.79586 | -50.98687 | 2026-09-24 11:28:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 49.5 |
| c38f8da2-ad39-33c1-9c8c-8c45799684ac | -12.53268 | -42.18335 | 2026-09-24 11:28:00 | TERRA_M-M | IBITIARA | BAHIA | Brasil | 2913002 | 29 | 33 | nan | nan | nan | Caatinga | 8.8 |
| 7e693507-9463-3349-9035-b7f8dcd34b99 | -11.62558 | -50.60515 | 2026-09-24 11:28:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 62.0 |
| bc4bf259-dd30-35f0-8fe7-dbb571dd50d5 | -13.46464 | -46.25315 | 2026-09-24 11:28:00 | TERRA_M-M | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 24.6 |
| a8ba519e-08ac-3340-a187-8f5c07d87a91 | -14.70764 | -48.74976 | 2026-09-24 11:28:00 | TERRA_M-M | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 0a6752cb-9797-3267-8461-a326d37bf950 | -17.7672 | -46.6302 | 2026-09-24 11:28:00 | TERRA_M-M | LAGAMAR | MINAS GERAIS | Brasil | 3137106 | 31 | 33 | nan | nan | nan | Cerrado | 15.3 |
| b1a76500-c87b-36e0-962c-3b7dc7ba4e9f | -11.69732 | -43.47171 | 2026-09-24 11:28:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 3254d353-106d-3266-beb3-464b9f72727a | -14.1841 | -43.42821 | 2026-09-24 11:28:00 | TERRA_M-M | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 31fa7026-e3a9-36d5-8b4f-bbe68dc75d49 | -13.35111 | -40.97179 | 2026-09-24 11:28:00 | TERRA_M-M | IRAMAIA | BAHIA | Brasil | 2914307 | 29 | 33 | nan | nan | nan | Caatinga | 15.6 |
| 721f7356-6c2e-31cd-b04a-1b6687afc9d0 | -14.17664 | -41.30957 | 2026-09-24 11:28:00 | TERRA_M-M | TANHAÇU | BAHIA | Brasil | 2931004 | 29 | 33 | nan | nan | nan | Caatinga | 5.9 |
| aea6785b-192c-36d0-96dc-d76d28920c52 | -14.70591 | -48.74411 | 2026-09-24 11:28:00 | TERRA_M-M | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 407a2867-2900-3aeb-b572-b30b419e4151 | -18.0036 | -44.64227 | 2026-09-24 11:28:00 | TERRA_M-M | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 48.2 |
| 42fc23f4-8ba5-3263-8e75-bb9afbec9650 | -14.75257 | -45.61777 | 2026-09-24 11:28:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 88c2371d-917f-3789-b68e-53efc402ffc7 | -11.44446 | -44.20821 | 2026-09-24 11:28:00 | TERRA_M-M | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 11.2 |
| fac0c38b-0388-308c-9faa-5de7de11a71b | -9.2604 | -47.3467 | 2026-09-24 11:30:00 | GOES-19 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 91.1 |
| 79193e72-6647-309b-b12f-b970570bd2b6 | -9.2415 | -47.3487 | 2026-09-24 11:30:00 | GOES-19 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 94.0 |
| 2b16b9c2-dcbe-3a30-b739-fdeb5e34d373 | -19.18724 | -47.35944 | 2026-09-24 11:30:00 | TERRA_M-M | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 9.1 |


[Clique aqui para ver as próximas entradas](README91.md)
