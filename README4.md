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
| 0f1fe0a9-bc6e-3697-aaba-92f57a3543c7 | -6.57003 | -43.6675 | 2025-09-02 00:11:00 | TERRA_M-M | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 2709ea3c-25a8-3825-96b3-547521fbd594 | -6.31748 | -43.51383 | 2025-09-02 00:11:00 | TERRA_M-M | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 80781fcb-8ae0-3420-ae7d-cc81d7067a88 | -6.27336 | -43.52007 | 2025-09-02 00:11:00 | TERRA_M-M | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 86b2a24c-2b50-3a36-b0d4-3a8a05df059a | -5.69027 | -45.95599 | 2025-09-02 00:11:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 29.3 |
| cb770e3c-3e88-348d-94fd-b90082438e88 | -6.77932 | -52.83958 | 2025-09-02 00:11:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 31.2 |
| 5c605e15-c8d2-326f-9f65-d411bba7cd50 | -6.42414 | -43.88204 | 2025-09-02 00:11:00 | TERRA_M-M | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 6f19c6a5-0c0d-3c04-890d-b1ad33d0b2ad | -10.06233 | -48.13521 | 2025-09-02 00:11:00 | TERRA_M-M | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 67.3 |
| fdbfd33f-52d2-3027-a917-51336c2c0085 | -4.29892 | -46.26503 | 2025-09-02 00:11:00 | TERRA_M-M | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 9.6 |
| ed642564-fab7-3b6a-bbf6-766e237dd7ac | -5.68328 | -45.90317 | 2025-09-02 00:11:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| baf3eddd-98cc-3203-bc36-e6a64b55a31a | -6.89195 | -45.85455 | 2025-09-02 00:11:00 | TERRA_M-M | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 46.1 |
| 2b9750b0-a114-3ef6-bf65-f7b6805fed18 | -8.70828 | -50.44014 | 2025-09-02 00:11:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 126.3 |
| 9ab4d029-5d5f-3052-a5a2-c04855cfae6d | -7.86761 | -47.97298 | 2025-09-02 00:11:00 | TERRA_M-M | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 30258b07-1b12-35a9-9240-dd705c1b35d1 | -6.98077 | -44.32014 | 2025-09-02 00:11:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| e837872b-5a1a-3205-812d-47318c99a944 | -6.45281 | -43.69616 | 2025-09-02 00:11:00 | TERRA_M-M | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| e90bdfd9-861c-30a7-adfd-6f1b94efcf73 | -7.19571 | -43.26557 | 2025-09-02 00:11:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 797fadac-a1b2-3ed4-bdbb-4cca71b4e55d | -6.81862 | -43.33445 | 2025-09-02 00:11:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 475b6646-6220-375c-9d34-5a7448e3d2f5 | -6.80119 | -52.83192 | 2025-09-02 00:11:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 151.9 |
| c7dc184a-180a-3ef7-b2ef-5e071b051ba5 | -6.25667 | -42.60656 | 2025-09-02 00:11:00 | TERRA_M-M | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 8.2 |
| 6370e932-528c-3202-b2a5-eac9e8c22ffd | -5.69989 | -45.95467 | 2025-09-02 00:11:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 49.1 |
| 27f120e1-8a6e-3edc-b59d-1211e9f1ef54 | -9.1133 | -46.05667 | 2025-09-02 00:11:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 31.8 |
| 496bf2a2-714f-36fb-9a70-c6c01591153e | -4.22198 | -47.2079 | 2025-09-02 00:11:00 | TERRA_M-M | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 20.7 |
| 87f413e7-c29e-35bc-8015-8e68f7af8347 | -9.17256 | -45.24475 | 2025-09-02 00:11:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 397647ce-7bd4-3a86-bcbe-b9836528bdc6 | -7.87627 | -47.96566 | 2025-09-02 00:11:00 | TERRA_M-M | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 71.8 |
| e2d49c9a-b119-3571-a6dc-6b0fa0ab35d2 | -5.17007 | -37.98871 | 2025-09-02 00:11:00 | TERRA_M-M | LIMOEIRO DO NORTE | CEARÁ | Brasil | 2307601 | 23 | 33 | nan | nan | nan | Caatinga | 20.1 |
| 7e6d32c9-b2ed-392c-bf76-76d58fcd8ea3 | -6.03266 | -43.77983 | 2025-09-02 00:11:00 | TERRA_M-M | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| d2b44ebb-045f-30a7-929f-d1dd6d401428 | -6.03144 | -43.77095 | 2025-09-02 00:11:00 | TERRA_M-M | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 50eb05c9-7c45-37bc-84f7-12c42eb0afb4 | -3.78277 | -47.56914 | 2025-09-02 00:11:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 482805ce-d269-3829-a0e0-b583a9d8e959 | -7.55463 | -45.70052 | 2025-09-02 00:11:00 | TERRA_M-M | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| b4f55d8c-0759-33ca-8982-1a340dac65d3 | -7.69063 | -40.44957 | 2025-09-02 00:11:00 | TERRA_M-M | ARARIPINA | PERNAMBUCO | Brasil | 2601102 | 26 | 33 | nan | nan | nan | Caatinga | 15.3 |
| 6ad17573-5d77-34e5-bde5-db4563c3b536 | -7.61461 | -44.03859 | 2025-09-02 00:11:00 | TERRA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 10.1 |
| c8e07bcc-a029-3eba-a620-08d801f45a24 | -6.25916 | -42.62433 | 2025-09-02 00:11:00 | TERRA_M-M | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 11.2 |
| f8d1ecd1-105e-3999-999c-cc376116ec97 | -9.44788 | -48.86622 | 2025-09-02 00:11:00 | TERRA_M-M | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 19.7 |
| 486b3d7d-7898-3376-8b34-1bc2b12476b0 | -7.70175 | -50.27613 | 2025-09-02 00:11:00 | TERRA_M-M | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 50.8 |
| 99ed58c9-d925-37a9-b3aa-c90d042f84d0 | -6.39944 | -43.50499 | 2025-09-02 00:11:00 | TERRA_M-M | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 618166bf-9eba-3718-ac51-cc5d5f474bd8 | -5.91894 | -44.98074 | 2025-09-02 00:11:00 | TERRA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 5d5c9c11-5981-3824-b503-5bcd16353b97 | -9.74753 | -48.9678 | 2025-09-02 00:11:00 | TERRA_M-M | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 35.5 |
| 459ce2ee-1423-35c3-b0cb-2a87f8c6adb8 | -6.22241 | -43.36224 | 2025-09-02 00:11:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 34.3 |
| ba44d6e6-cc2d-3d6b-8781-cdc8d572db40 | -6.72376 | -42.26307 | 2025-09-02 00:11:00 | TERRA_M-M | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 10.5 |
| cdaf76e7-a31e-30e7-a4d6-9d4bdf3b0254 | -6.82234 | -45.25972 | 2025-09-02 00:11:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 59c68f2b-aaac-3bc0-a3eb-e849edd859e2 | -5.66648 | -43.66621 | 2025-09-02 00:11:00 | TERRA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 7fcfde66-5e18-3e24-a986-4f1d87ef4844 | -6.89413 | -44.22557 | 2025-09-02 00:11:00 | TERRA_M-M | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| aa0fa520-bea6-34eb-a2bb-9f75d31ce99a | -10.05234 | -48.15392 | 2025-09-02 00:11:00 | TERRA_M-M | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 38.1 |
| ca710865-52f8-31cb-87ae-372a01d934f0 | -6.77999 | -52.79701 | 2025-09-02 00:11:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 47.2 |
| b732f3d6-cc02-3707-a465-36813089add3 | -6.82289 | -52.82264 | 2025-09-02 00:11:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 107.8 |
| b752bbee-2792-3cab-a81f-65ac983cf0f5 | -8.00799 | -44.08458 | 2025-09-02 00:11:00 | TERRA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 96a1721d-6a79-3292-931a-959f66952786 | -7.37686 | -47.04049 | 2025-09-02 00:11:00 | TERRA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 6ba4ac04-0163-3810-8c27-51bac0b6944e | -6.27826 | -44.50403 | 2025-09-02 00:11:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 5c9de4a3-333b-344a-b7a8-1f6ff3dcf506 | -7.48864 | -45.35429 | 2025-09-02 00:11:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 25.9 |
| c645a56f-22bf-3f28-9197-10e3695c2c8e | -5.78511 | -42.59572 | 2025-09-02 00:11:00 | TERRA_M-M | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 45.7 |
| 00c6757d-7238-3ba6-be6c-5b64fd226a76 | -6.33758 | -43.52905 | 2025-09-02 00:11:00 | TERRA_M-M | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| ca45cb52-6b22-3053-91f8-85a33e8d0611 | -7.99318 | -44.04562 | 2025-09-02 00:11:00 | TERRA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 61320682-3724-3001-baa1-8471ad083132 | -6.85626 | -52.81813 | 2025-09-02 00:11:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 100.8 |
| e68f9adc-ca15-31bb-b8b2-d7891b6743e7 | -6.29557 | -43.6161 | 2025-09-02 00:11:00 | TERRA_M-M | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 95b59302-0d27-3914-9d2d-3f2f82e3bd1b | -9.12196 | -46.04376 | 2025-09-02 00:11:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 22.0 |
| f7c9a15f-0ceb-3ba4-8e3a-8a0fd8a55627 | -4.48112 | -48.12609 | 2025-09-02 00:11:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 22.8 |
| 3497a749-8982-3990-85af-a9c779fbfcd6 | -9.83698 | -48.63092 | 2025-09-02 00:11:00 | TERRA_M-M | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 22.9 |
| 4fc248f5-674b-397f-bb03-17a089223ba0 | -6.79662 | -52.79474 | 2025-09-02 00:11:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 84.8 |
| 4463af27-29dd-311e-83b8-e3735ba7db3e | -9.17118 | -45.23401 | 2025-09-02 00:11:00 | TERRA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 0058a0e1-500f-36d0-82cd-88948c34f384 | -6.98327 | -44.33854 | 2025-09-02 00:11:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 6e80425a-775b-3e6c-902b-66f88426624a | -8.85658 | -50.57933 | 2025-09-02 00:11:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 33.6 |
| d310f2cf-14d2-3d6e-846f-647060faeac3 | -4.17433 | -46.09645 | 2025-09-02 00:11:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 5.3 |
| b34d68cc-f017-39ab-8546-c73da3bea8ba | -7.92007 | -46.44823 | 2025-09-02 00:11:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 63.7 |
| ac986ee0-78e3-3c0a-b171-3fb0badf2a61 | -5.69849 | -45.9441 | 2025-09-02 00:11:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 0b96362f-d02f-3f4b-bb4c-a9b925094510 | -6.86381 | -45.16657 | 2025-09-02 00:11:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| c2124121-e25d-3b0e-9cfe-387f5de1236f | -9.16824 | -45.24086 | 2025-09-02 00:11:00 | TERRA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 42f2351e-0ee9-3b36-9c7b-b54c2dcc482d | -5.78403 | -43.85138 | 2025-09-02 00:11:00 | TERRA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 9ec8f0e0-4c86-3d4b-8416-9e1df32d105b | -6.25792 | -42.61546 | 2025-09-02 00:11:00 | TERRA_M-M | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 12.1 |
| f95bf3cf-ee6a-3f27-bfdb-da23694e00fc | -3.22028 | -46.83455 | 2025-09-02 00:11:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 183b86e3-1f49-3a7e-8632-d0736200ab48 | -5.73707 | -45.54342 | 2025-09-02 00:11:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 452bb5e5-0fa1-3d56-aaf5-689c81366526 | -6.27819 | -43.29451 | 2025-09-02 00:11:00 | TERRA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 4cc49aaa-8b52-3a79-98fd-a16ace97f3f4 | -6.89053 | -45.84383 | 2025-09-02 00:11:00 | TERRA_M-M | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 17.3 |
| f8666ebf-9168-3ead-a47c-002f581f1645 | -6.88082 | -45.84512 | 2025-09-02 00:11:00 | TERRA_M-M | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 13.9 |
| d304e428-44a9-36ef-9bdf-851b0c71fae2 | -7.31574 | -44.27723 | 2025-09-02 00:11:00 | TERRA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 645f1f48-eb6f-3780-9fc0-5e77678df593 | -3.22956 | -47.12102 | 2025-09-02 00:11:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 8c3b8cf4-75f4-3d4d-b106-47161e5c4c96 | -8.71934 | -50.44528 | 2025-09-02 00:11:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 646c94a6-4f4b-3603-861f-a152448836ea | -6.22363 | -43.37106 | 2025-09-02 00:11:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 21.0 |
| c42a3240-5982-3b97-80a0-b3625177087e | -6.27437 | -42.60405 | 2025-09-02 00:11:00 | TERRA_M-M | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 6415b824-3362-3b64-aa4c-5a159b38416d | -6.26324 | -43.52741 | 2025-09-02 00:11:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| a343004e-4c02-3f13-8a3e-ef47520d4026 | -8.70191 | -50.42167 | 2025-09-02 00:11:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 46.1 |
| 03eee867-e83e-3365-abde-7b3ab3ca7dcd | -6.33358 | -42.56243 | 2025-09-02 00:11:00 | TERRA_M-M | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 9.0 |
| d18eaabb-e26c-3412-ae77-f127631fb965 | -9.47915 | -47.60156 | 2025-09-02 00:11:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 15.0 |
| b184f0cb-ddb2-33e3-b26e-bbf841144feb | -7.11338 | -44.756 | 2025-09-02 00:11:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 49354c48-1b58-359a-81a7-e27bec304adf | -3.97571 | -43.24314 | 2025-09-02 00:11:00 | TERRA_M-M | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| be446364-4118-3130-8d7d-4e979b820d8f | -4.47919 | -48.11187 | 2025-09-02 00:11:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 44.0 |
| 82ba3141-ed07-37fb-96d4-d915a256b709 | -5.47583 | -44.02782 | 2025-09-02 00:11:00 | TERRA_M-M | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 6fb2c7cb-2ad4-38c0-ae22-bf28f11af6c0 | -7.06464 | -45.99656 | 2025-09-02 00:11:00 | TERRA_M-M | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| fd904ce2-a4b1-3168-bba8-95e67e7ad607 | -6.27176 | -44.52372 | 2025-09-02 00:11:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 60e0ae8a-9329-3291-92bf-7e905900d27d | -6.22713 | -41.80961 | 2025-09-02 00:11:00 | TERRA_M-M | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 6.9 |
| bc49b176-a511-345d-bef9-84e55b936fe6 | -8.81053 | -47.83186 | 2025-09-02 00:11:00 | TERRA_M-M | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 27.9 |
| 53358ba9-09ca-329e-8d9c-37ca190e5319 | -5.91085 | -46.62125 | 2025-09-02 00:11:00 | TERRA_M-M | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 4359e80d-229c-3023-abe1-4aa29b2ed1b0 | -8.72558 | -50.46397 | 2025-09-02 00:11:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 26.5 |
| b872e862-0ba7-3c0a-a123-8b533227995f | -6.81786 | -52.82954 | 2025-09-02 00:11:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 103.0 |
| 46b158f1-9188-3005-ae7f-ba8955fc1534 | -4.61798 | -47.42076 | 2025-09-02 00:11:00 | TERRA_M-M | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 4d473359-b574-3727-8b87-abd9e4a658b5 | -6.29434 | -43.60721 | 2025-09-02 00:11:00 | TERRA_M-M | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 0542b942-9b80-3882-b51f-85185bcc6518 | -5.78525 | -43.86027 | 2025-09-02 00:11:00 | TERRA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 31c00a79-d243-3465-b21f-37e286277d99 | -7.663 | -42.71173 | 2025-09-02 00:11:00 | TERRA_M-M | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 44c926d0-3a46-384f-8cc9-4c03bc9b6562 | -6.26552 | -42.60531 | 2025-09-02 00:11:00 | TERRA_M-M | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 62f1def5-8087-3eaf-b1ee-a8f3aeb38e6e | -6.19475 | -43.35718 | 2025-09-02 00:11:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| e6b8ada7-0226-383c-b322-8d9254785b9f | -5.38591 | -46.28524 | 2025-09-02 00:11:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 8e61bd42-2ecd-39ee-977d-1f5102794078 | -6.18085 | -44.19136 | 2025-09-02 00:11:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |


[Clique aqui para ver as próximas entradas](README5.md)
