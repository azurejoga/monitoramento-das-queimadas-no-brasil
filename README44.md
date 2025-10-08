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

## Dados Diários - Página 44

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e474f808-4ec6-3f24-bca6-21e2d1d8ae94 | -12.25282 | -47.87165 | 2025-10-08 04:17:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| ed53f2b3-7074-326f-a3d3-7302137ac0ba | -12.41656 | -45.62549 | 2025-10-08 04:17:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 8ad69af9-6168-3fef-b26c-0809d23f3bb0 | -7.67477 | -42.58438 | 2025-10-08 04:17:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 6ffb3b51-f925-3285-8b7d-a6ed5a6adfd1 | -9.13661 | -50.05972 | 2025-10-08 04:17:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f0e4a793-2ac1-31f9-b928-f8cd5e6e2027 | -7.79166 | -42.60645 | 2025-10-08 04:17:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 29c094c3-183e-3813-8097-734ea95c835d | -11.16827 | -54.90215 | 2025-10-08 04:17:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e5459417-072b-3fe2-901c-125decd0e839 | -4.62565 | -47.41673 | 2025-10-08 04:17:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fc6961ad-9e0c-309b-8f2b-6512e02f2d68 | -10.41873 | -48.09494 | 2025-10-08 04:17:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 954c3c4d-c6be-336f-a3bf-d87fc6b2a24c | -6.45403 | -44.5829 | 2025-10-08 04:17:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e83a127a-d481-32b9-9702-fac092e47a68 | -5.98183 | -44.91433 | 2025-10-08 04:17:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 69a5edcb-963f-3e17-be0a-8c8f286e319f | -4.47745 | -49.71592 | 2025-10-08 04:17:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 412cf3c0-0ecb-30cf-a1c2-6eaea2824787 | -3.28807 | -42.62373 | 2025-10-08 04:17:00 | NPP-375D | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2cd10cbe-1e26-3b6f-a54c-aa83e0a7b399 | -12.3964 | -51.12975 | 2025-10-08 04:17:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e9bf2161-21ab-30cd-b6fa-22b85fd0707d | -0.90435 | -47.55104 | 2025-10-08 04:17:00 | NPP-375D | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| bdf46262-8842-318c-aa44-bd24e9fef133 | -7.0267 | -42.87109 | 2025-10-08 04:17:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 6b962b89-cd9f-3e57-9eb6-ec27e45abd57 | -4.91854 | -45.08883 | 2025-10-08 04:17:00 | NPP-375D | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f4c2c915-c565-3b6c-89dd-8f03b4580ce6 | -4.13251 | -47.65335 | 2025-10-08 04:17:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 53f867c4-55d3-3f57-854b-893fe32e96c0 | -13.37075 | -47.25421 | 2025-10-08 04:17:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 18e92491-22bc-3b38-b798-2d86f903490d | -13.02983 | -47.8985 | 2025-10-08 04:17:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3b9d5e29-73be-3838-a652-bbb73c147106 | -11.16009 | -54.88266 | 2025-10-08 04:17:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 5b9d5ef2-5cc1-3a26-aaeb-e076e02850c8 | -11.79707 | -45.04598 | 2025-10-08 04:17:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8c8a8860-cf1f-321e-84e3-478bc954977a | -5.80923 | -44.04845 | 2025-10-08 04:17:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2504f5ba-274f-3ad8-b534-badfaaf98a0e | -6.69928 | -42.8693 | 2025-10-08 04:17:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 6ada1541-5985-3641-b967-9f6572c7db2e | -11.11696 | -54.04232 | 2025-10-08 04:17:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 45d839c3-b32c-3aa7-8469-78658a0414e2 | -11.71384 | -50.98453 | 2025-10-08 04:17:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 1f96f3cc-3e3e-3f8e-bbae-ab617b3caf75 | -7.53176 | -42.71729 | 2025-10-08 04:17:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 67ca90f1-d1b9-367f-b14d-78c3a375adc1 | -10.23734 | -52.70277 | 2025-10-08 04:17:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4608a517-820e-36fd-9e9d-ec0fc4b276c1 | -12.24636 | -47.87135 | 2025-10-08 04:17:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 078b671d-2e88-37ef-ac29-612b4f5f8ed1 | -10.60978 | -44.34502 | 2025-10-08 04:17:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c342bd58-5573-3ce0-8f5d-c2809425ba3a | -4.62285 | -47.41856 | 2025-10-08 04:17:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 022477c6-112c-3823-96a9-056f54a18d1c | -7.78388 | -42.40126 | 2025-10-08 04:17:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 6f43dfd8-2930-393d-9b19-1a91ddf3c4b8 | -10.66424 | -44.1522 | 2025-10-08 04:17:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6b6ff58e-7ee8-3e40-afc9-e972909121de | -11.18411 | -54.88329 | 2025-10-08 04:17:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| d0ac91da-b7d2-3d90-bd20-30655af76ffc | -5.74234 | -44.51166 | 2025-10-08 04:17:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4771e651-55a6-339c-a2c0-0ed4b920d3f5 | -4.91043 | -48.02305 | 2025-10-08 04:17:00 | NPP-375D | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 924e76d2-64cc-3c17-a226-e6f8cff88aa3 | -3.69127 | -49.55066 | 2025-10-08 04:17:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| cdc9434a-dc4e-3553-b772-9b3e04d8d523 | -13.30543 | -47.7713 | 2025-10-08 04:17:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fe00a165-95bb-37ec-8041-0a2c46341d43 | -13.03695 | -47.92233 | 2025-10-08 04:17:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4acda562-c8d5-34dd-b86b-c0afcf9a254f | -6.40747 | -44.72063 | 2025-10-08 04:17:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 64af9f21-d310-3981-ba89-8132b40c8db8 | -7.05541 | -37.69244 | 2025-10-08 04:17:00 | NPP-375D | EMAS | PARAÍBA | Brasil | 2505907 | 25 | 33 | nan | nan | nan | Caatinga | 1.2 |
| ebaed5cf-767a-3bce-9a4f-db19b4699f12 | -7.4381 | -43.13954 | 2025-10-08 04:17:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 4a9cbd7a-cd0b-30b0-8d82-b7aa8268c06e | -10.35785 | -50.28443 | 2025-10-08 04:17:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6205290f-a4d7-3c1c-8e8f-3c899f090975 | -11.74503 | -50.93979 | 2025-10-08 04:17:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 38.9 |
| 24b5942c-a39f-333d-b45e-9c08178aed4e | -11.73128 | -50.96476 | 2025-10-08 04:17:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9c96a20c-49e9-324d-9f3c-c5afafd8012d | -7.51451 | -42.71819 | 2025-10-08 04:17:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| ab7ee6d7-2009-3ed2-b4c3-497b10ed9230 | -11.07388 | -48.36193 | 2025-10-08 04:17:00 | NPP-375D | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 82492cfe-1dc7-3d86-9074-6fee9079cf67 | -10.22767 | -52.69763 | 2025-10-08 04:17:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0b6334a6-42c5-3c4e-9f69-fcc70818d1c1 | -3.44414 | -45.59197 | 2025-10-08 04:17:00 | NPP-375D | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 338735bb-34f9-3586-891a-533e2d4e5574 | -13.25677 | -46.46873 | 2025-10-08 04:17:00 | NPP-375D | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d6f4bd55-0fcc-34b9-b183-e10780d20fd4 | -7.71649 | -42.38388 | 2025-10-08 04:17:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 399d8851-6a1a-31f6-b2eb-11216b7f1281 | -6.56806 | -44.15032 | 2025-10-08 04:17:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8a268d1d-1a3b-307e-ae7d-ee514cf3d1d6 | -13.37004 | -47.25842 | 2025-10-08 04:17:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 30dc3de4-c408-3ab3-b877-c2679ca8cd04 | -11.45623 | -43.49252 | 2025-10-08 04:17:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cc5b97fc-89cc-33e4-8cfc-9560c252634f | -10.39432 | -50.23037 | 2025-10-08 04:17:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 042ea176-180e-36c1-9760-38564bb5ac91 | -5.7519 | -44.60651 | 2025-10-08 04:17:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e4e5bc3b-09ab-3520-96e9-50882235a42c | -13.37135 | -47.2292 | 2025-10-08 04:17:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f3a15c03-09cf-3145-96ef-cee22836d9da | -4.0483 | -42.52019 | 2025-10-08 04:17:00 | NPP-375D | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 52f97190-ef9b-3728-b2af-e759f248dad1 | -11.1657 | -54.86032 | 2025-10-08 04:17:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1ae442e8-07db-31c8-8563-f80ed17906ba | -11.73696 | -50.93369 | 2025-10-08 04:17:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 25.1 |
| f704de05-4bff-3f1c-8a21-673c93ee5006 | -7.01731 | -42.88748 | 2025-10-08 04:17:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 24.6 |
| 9c09879f-1b94-327a-964c-26ece6881578 | -13.07811 | -47.29682 | 2025-10-08 04:17:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 4671fd95-3700-3d2c-817e-07384d2421a6 | -11.78947 | -45.13609 | 2025-10-08 04:17:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 05ba0baa-cc7f-3b85-970a-3aaaa9ce6c8d | -4.69903 | -44.96998 | 2025-10-08 04:17:00 | NPP-375D | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1f2ae9e0-1aad-3c24-b2fd-2914d66c766f | -2.43822 | -48.43289 | 2025-10-08 04:17:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4c7df14f-9b61-3e54-8c96-9bff1396db90 | -13.26995 | -48.04686 | 2025-10-08 04:17:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1cf9b6a8-1b18-3538-bd78-9099db5a463d | -5.70891 | -45.68668 | 2025-10-08 04:17:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2916fd6a-eefc-3ebd-8400-37d8dda0b0bb | -3.13838 | -50.44517 | 2025-10-08 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 20c855a3-dccc-3122-957f-ee5998f692cb | -11.1435 | -54.88166 | 2025-10-08 04:17:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6c3ed0af-6b77-363f-ad39-c8a67b16c31a | -11.16257 | -54.87028 | 2025-10-08 04:17:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| d39097c4-0633-3f80-a774-3ff7b6365d23 | -5.168 | -46.22929 | 2025-10-08 04:17:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bc5135b1-2404-329c-bf4f-74acb3a1914e | -4.74627 | -43.66648 | 2025-10-08 04:17:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5801c07d-e3c1-39a1-b0ca-b7bb9f220548 | -5.77803 | -46.15295 | 2025-10-08 04:17:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 601ccd6c-0661-3003-8440-fa09a6d194e7 | -10.46983 | -49.38573 | 2025-10-08 04:17:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c4bd0430-e643-3a67-aeb9-7a134a7dbcb8 | -11.94116 | -46.41846 | 2025-10-08 04:17:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cb2ee022-7893-3814-8fd2-d84811ab6910 | -9.66928 | -49.95032 | 2025-10-08 04:17:00 | NPP-375D | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a5aa705c-7e4c-3451-a775-25b8c82e6f55 | -12.40162 | -45.15587 | 2025-10-08 04:17:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bb609b15-a614-33e1-a6e5-fe5e8f52e638 | -4.40785 | -49.77121 | 2025-10-08 04:17:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6f5cb5e0-f9b3-38dd-8432-b51ab2e5ed1e | -12.24487 | -47.87412 | 2025-10-08 04:17:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 6c59b568-f6f5-38eb-a799-b64b69498a8f | -11.69391 | -46.34599 | 2025-10-08 04:17:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c4faf0d6-cbde-30e0-85bb-562d94d7a7b6 | -11.99178 | -46.77164 | 2025-10-08 04:17:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 6b6de9da-db48-3dc4-890a-7181e2b140d6 | -11.69261 | -50.96352 | 2025-10-08 04:17:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d9f1d840-f47d-3609-a3aa-d4d13180727b | -10.46587 | -47.8177 | 2025-10-08 04:17:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 11c265d0-cdfc-32d4-8c60-3fae5647ef6a | -13.06577 | -47.88473 | 2025-10-08 04:17:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d85d169c-7e2f-316f-96b7-bdc3a9900263 | -12.2444 | -43.77895 | 2025-10-08 04:17:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 728c1a2b-e1e3-34a5-a42c-ce0d26330e4c | -12.23682 | -47.86091 | 2025-10-08 04:17:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 82f370a8-1430-3250-9a98-8a99072e719c | -11.79259 | -45.05251 | 2025-10-08 04:17:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8dba16c4-326e-301e-8d1a-66cc67cde0b5 | -12.38589 | -51.13696 | 2025-10-08 04:17:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2976b3ea-bac3-3e53-b3ce-0cd12448ad0d | -5.97548 | -45.49015 | 2025-10-08 04:17:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 58d66b54-18c1-3b49-b36d-f116990b8fe5 | -13.06821 | -47.93624 | 2025-10-08 04:17:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ccb225f3-6175-3897-9448-dda60211da26 | -6.99564 | -42.87334 | 2025-10-08 04:17:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 163b9994-507b-3a02-b77b-79676cd534c4 | -5.77633 | -45.74294 | 2025-10-08 04:17:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bd5792a3-9cb9-32f1-9f89-ce6f18ed46a4 | -12.9321 | -46.8498 | 2025-10-08 04:17:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f381f111-bc25-3d61-8bab-f93ee8d33b05 | -4.95179 | -45.59267 | 2025-10-08 04:17:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cddcc616-c5f5-3267-b81c-481a0e686d21 | -11.4983 | -44.96763 | 2025-10-08 04:17:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7192b207-5310-3157-8907-4a85bde2f726 | -2.48041 | -48.3669 | 2025-10-08 04:17:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2afe7b75-9aa9-3756-ac4b-f66d678f93b7 | -5.86355 | -44.30156 | 2025-10-08 04:17:00 | NPP-375D | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 527b2b00-f2d8-3378-aa8c-2e70e2e00ebd | -11.14686 | -47.74575 | 2025-10-08 04:17:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8310396d-2618-32fd-886f-23b6e848b68d | -7.47463 | -43.10247 | 2025-10-08 04:17:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| a48ba464-0dd4-30d5-859f-9440240650d9 | -11.77277 | -45.13327 | 2025-10-08 04:17:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2441b14e-46e3-3588-9272-27d0989b00b9 | -11.33507 | -56.20204 | 2025-10-08 04:17:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README45.md)
