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

## Dados Diários - Página 55

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 305bb340-608f-3e2f-9587-aad07f1245ab | -10.97818 | -48.32283 | 2026-09-15 05:18:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 3e7eb6d8-d591-372a-a39a-1b4be6855f8c | -6.09679 | -57.68629 | 2026-09-15 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 9e9d57f3-5129-3d2d-ab3a-c0630629537c | -7.3241 | -59.57264 | 2026-09-15 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 68f425e8-08c9-36ea-8ef1-495081a02946 | -10.80322 | -46.21577 | 2026-09-15 05:18:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 0a80106e-939a-3480-89a6-85004b95be94 | -6.27908 | -59.92296 | 2026-09-15 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 90247709-72dd-3655-a488-09b637c1b6b9 | -6.1108 | -57.6847 | 2026-09-15 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1da2fe3f-62c6-39dc-9d08-298912b6e9d3 | -7.25116 | -46.15739 | 2026-09-15 05:18:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| c8e5b43a-65af-34cf-a64f-39144380fcd6 | -10.89021 | -51.56385 | 2026-09-15 05:18:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0987628e-6622-3742-998c-9b59ee62df6b | -6.70157 | -51.17347 | 2026-09-15 05:18:00 | NOAA-21 | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0fa6f551-cda9-3b61-9177-a1ed8642a9d7 | -6.15959 | -55.70239 | 2026-09-15 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2d13a6cf-6b52-3849-8812-9df60fdaec2c | -9.69557 | -58.16866 | 2026-09-15 05:18:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0241e917-3697-32fe-82db-58aabedc4b64 | -6.56972 | -58.95721 | 2026-09-15 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| da0bfb9b-d6f8-3b47-8de0-581e4f2f474e | -6.8364 | -55.5538 | 2026-09-15 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 53.8 |
| 249c1a0c-edca-33ca-adde-a6868b96a76d | -8.0842 | -61.80192 | 2026-09-15 05:18:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 53c2b609-942f-3ea6-9f6a-463cc581ad52 | -9.10098 | -65.55635 | 2026-09-15 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c234da5b-5cd4-30ce-b333-7d1c228ae449 | -8.81911 | -62.48971 | 2026-09-15 05:18:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dbc7f7e6-ef23-3f5f-9130-11b227c45ce9 | -10.90602 | -51.54405 | 2026-09-15 05:18:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 521108d8-8a9f-361f-b899-1417e68bfdc4 | -10.59999 | -57.32057 | 2026-09-15 05:18:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f3538514-0409-3c89-ad6e-91a62b4bb34f | -10.65895 | -54.14826 | 2026-09-15 05:18:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 19eb5eb1-f425-355a-8db0-b33e4866cc6f | -9.35844 | -50.15787 | 2026-09-15 05:18:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 030aba6b-5c0f-3fa9-be19-90485f96fc87 | -9.64332 | -63.50748 | 2026-09-15 05:18:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ab28213b-e085-3efe-a63b-ab543e9413ac | -7.61421 | -47.29642 | 2026-09-15 05:18:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6f175047-8d1f-3cb0-a86c-b84a0a6beb73 | -5.13012 | -55.95315 | 2026-09-15 05:18:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 327dbcde-239b-317c-9327-b3e152c62df9 | -6.68962 | -58.6895 | 2026-09-15 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 3ed0e51e-106e-3391-a790-0d430e024aed | -5.12424 | -55.94382 | 2026-09-15 05:18:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0870e541-cdbe-3d2a-b958-d5b8f1edbb18 | -10.80494 | -46.2009 | 2026-09-15 05:18:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 80e8a0ee-b57d-350e-b006-fd74e4f61ecf | -9.25748 | -60.28078 | 2026-09-15 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 28e130aa-502f-31a1-a55a-0dfdd4d21702 | -10.67549 | -54.15465 | 2026-09-15 05:18:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6665b845-57ac-314b-b087-71b744a9f73d | -6.10957 | -57.8639 | 2026-09-15 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5159b1b8-75aa-3795-957a-31b1cd18dcc4 | -6.16134 | -55.71562 | 2026-09-15 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 708d3fb3-429c-3b42-b0ac-9d9816f7c9e6 | -6.76012 | -56.3321 | 2026-09-15 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e02d93c7-7211-3dd6-bef9-516355865279 | -6.72089 | -48.12169 | 2026-09-15 05:18:00 | NOAA-21 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5f469221-5be7-3133-b67a-1aa344d7a5f1 | -5.4554 | -60.22671 | 2026-09-15 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6eebbb8e-e11c-3f09-b29f-a2f320fd7eed | -9.35872 | -50.11126 | 2026-09-15 05:18:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 59a94849-5114-3f15-993b-99a6b89c6508 | -6.10638 | -57.71336 | 2026-09-15 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0e1acef3-ee4b-334b-a498-07e0163af02d | -5.78038 | -56.3676 | 2026-09-15 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7a5b7ff9-76ee-3a61-a640-c7c5faf5aa4b | -7.77734 | -49.47939 | 2026-09-15 05:18:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| fed63299-fdea-3f3d-b9ae-f6ce698104d5 | -8.5455 | -54.69675 | 2026-09-15 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6263b2fe-bf3a-33b9-9ce5-f78ab571df4b | -8.12197 | -54.80368 | 2026-09-15 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 69d892b2-5fba-3b89-9b8d-814cd3a214c7 | -9.07114 | -61.00803 | 2026-09-15 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9fb9e532-e6cc-30ae-9c2a-958735e18446 | -8.08481 | -61.7981 | 2026-09-15 05:18:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5f58e7ad-935b-3dea-92f1-34876245021e | -6.13349 | -57.70694 | 2026-09-15 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 577b6d36-8a1e-3368-b042-0aaa1398feb8 | -6.13579 | -59.8825 | 2026-09-15 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d172c2fe-b00e-3f3f-9d9f-70b396307005 | -10.98109 | -48.32364 | 2026-09-15 05:18:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 6ebb5ddb-a8fe-3ca4-91cd-9b7669ad6d63 | -7.24182 | -46.176 | 2026-09-15 05:18:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a1320b3d-f34f-3f7a-9b22-f70ae7900bf4 | -5.9284 | -53.54252 | 2026-09-15 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4a70cbb8-d073-33e4-9260-0994efe40133 | -7.23023 | -46.15061 | 2026-09-15 05:18:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 202a3e70-a95e-3579-ad57-821770990472 | -9.68625 | -63.4272 | 2026-09-15 05:18:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 03098d98-9d05-3ae2-82f7-dc74e4a033f1 | -6.15585 | -57.6957 | 2026-09-15 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 7ea15d94-3827-330b-9f66-4967f583aaeb | -8.50385 | -50.14866 | 2026-09-15 05:18:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 46c47341-52d7-3abb-81d4-e31c329d770c | -5.16754 | -59.76513 | 2026-09-15 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6ec97815-5585-3b91-a8b3-dbd1358ef5d9 | -8.79281 | -45.90516 | 2026-09-15 05:18:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c7565bef-d9fa-37d5-994b-87f006bb8b32 | -9.41207 | -62.70293 | 2026-09-15 05:18:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 7e2c011f-6c89-33df-ac4e-cc97ee32cb57 | -10.03235 | -52.10273 | 2026-09-15 05:18:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 38b4ce98-58bb-3dd5-85ee-84ad1b5cbe60 | -9.74432 | -62.36326 | 2026-09-15 05:18:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 5458187a-a25c-3b4e-823d-290ecdaba502 | -10.67122 | -54.15404 | 2026-09-15 05:18:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 86788121-b7b5-31c6-b76b-3457c240dc01 | -9.69501 | -58.17234 | 2026-09-15 05:18:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4c6abe5a-d971-3ca3-9f56-c9e8dc201a18 | -6.08714 | -57.85997 | 2026-09-15 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fce4029e-acd7-3b1b-b8b0-9761975f1dcd | -6.37263 | -55.25727 | 2026-09-15 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d3838ab4-7d9e-3e01-98e8-474c965f5661 | -10.69463 | -54.17393 | 2026-09-15 05:18:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 70219db4-c84c-340e-836b-c3d53ec3db3c | -5.81666 | -52.10411 | 2026-09-15 05:18:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| d283f696-2efb-30ab-931b-caf3593d61e0 | -9.35929 | -50.10615 | 2026-09-15 05:18:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| d116005a-43cb-3fca-bdee-4859ef5653f4 | -9.36526 | -50.10325 | 2026-09-15 05:18:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| cc61f286-480e-335b-9485-2e9a0e7564ee | -8.50929 | -50.14939 | 2026-09-15 05:18:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 7da186dc-de2c-3b6b-bb92-76314496bda5 | -6.07991 | -57.86246 | 2026-09-15 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6cfec36e-26ba-3aa9-b21e-b40d0e85c4a6 | -6.01516 | -59.93478 | 2026-09-15 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 7.5 |
| c2b67e9c-59d7-39d1-921a-6a6861283e17 | -6.68577 | -58.69245 | 2026-09-15 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c3ba2687-d0ad-339c-ab7f-9065942477ba | -8.80429 | -50.4896 | 2026-09-15 05:18:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 68dfde08-d24e-3dc7-bdbb-b8c141cdb74d | -7.34113 | -55.17802 | 2026-09-15 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6fa433f7-cb31-309e-80bb-3af5906ce1cc | -6.68138 | -58.69888 | 2026-09-15 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fb2b42d0-4dd8-36cd-b781-dcd2c05383e5 | -6.83945 | -55.55879 | 2026-09-15 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 10f7d184-258c-3281-85ad-850d9e1f8205 | -7.46966 | -46.15363 | 2026-09-15 05:18:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 238feae9-8c08-30ad-bf65-51e3e1c0cafe | -5.12008 | -55.94727 | 2026-09-15 05:18:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6f078875-7643-3330-81ff-3d13abaf4b1d | -10.90091 | -51.54333 | 2026-09-15 05:18:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8b15c7be-d550-348a-a6c7-7ea45f2fa68c | -9.49403 | -56.75349 | 2026-09-15 05:18:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6a8aec3f-7ede-3f2c-9da7-2492cd042903 | -5.81533 | -53.80505 | 2026-09-15 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3a2d084d-3cd4-3849-a6ae-e3b83a2e5a8c | -8.79851 | -50.49224 | 2026-09-15 05:18:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3939b90d-1e87-304e-abb9-428161f0d45b | -8.40941 | -54.72278 | 2026-09-15 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a2565a3c-b5ac-35bc-8794-1d8289ccdc78 | -9.3652 | -50.10471 | 2026-09-15 05:18:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a65b40dd-9365-3689-bfb6-b802ea6a7cef | -8.50977 | -50.14587 | 2026-09-15 05:18:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| bf97a7a6-12d1-35e0-84f6-58cadc8dd7bd | -5.07871 | -56.24599 | 2026-09-15 05:18:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 99318eba-3cd4-3156-b3c3-a8d7621d994a | -7.23625 | -46.15792 | 2026-09-15 05:18:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d7122459-2626-3771-8cd9-cba590e86e6a | -8.81491 | -62.49316 | 2026-09-15 05:18:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4dd7dba1-5b9e-38a4-8254-79aebfb4adf9 | -10.03307 | -52.09732 | 2026-09-15 05:18:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8f1ffc73-2a10-36f7-ae0b-2cb4cfd0da37 | -6.11528 | -57.67804 | 2026-09-15 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| ed164709-e466-3586-850f-84a63a7459e2 | -8.35918 | -47.58662 | 2026-09-15 05:18:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b87c6dfd-b3da-3fa8-99e3-3588b0b426bc | -9.69168 | -54.34385 | 2026-09-15 05:18:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| a4d16036-b779-3d2e-8a7f-d62625ab0ccc | -6.84315 | -55.55935 | 2026-09-15 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2249b8d7-c894-383a-b6a2-426e63dc2a99 | -6.28524 | -56.04312 | 2026-09-15 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b0999a74-9d02-343b-8446-97a588948ef5 | -6.00641 | -52.18707 | 2026-09-15 05:18:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2206adb6-344c-337a-9d27-ec12a3b3928a | -9.50711 | -64.71182 | 2026-09-15 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2bf6ecdf-80c2-3680-ae85-299b704f7f2c | -7.88067 | -61.40501 | 2026-09-15 05:18:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 684d652d-bf9e-33e7-afe2-101b1c730bc7 | -10.25543 | -57.7011 | 2026-09-15 05:18:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 798cc50d-032b-360f-bf80-1224b3350eab | -8.7936 | -45.8987 | 2026-09-15 05:18:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c0b8e23b-1d39-3c4a-bc79-4132fad33659 | -11.26573 | -54.13022 | 2026-09-15 05:18:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9da2dc0b-5a4e-3df5-9baa-17655207f80d | -6.72245 | -48.12212 | 2026-09-15 05:18:00 | NOAA-21 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 4cf00d44-990b-396e-a37b-0b888a1da8c9 | -7.09981 | -47.48468 | 2026-09-15 05:18:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e5395076-c4da-329d-89bc-dffb69115ae7 | -6.01793 | -59.9388 | 2026-09-15 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 022ae476-2c33-3b78-a845-4d05768f50d6 | -9.85326 | -65.18247 | 2026-09-15 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 22460e59-53ac-32c5-bfc5-423653a07afb | -10.65829 | -50.5838 | 2026-09-15 05:18:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |


[Clique aqui para ver as próximas entradas](README56.md)
