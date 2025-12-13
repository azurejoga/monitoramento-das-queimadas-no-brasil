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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dacd3358-5873-3e79-a6cb-58b91368dfd0 | -2.66315 | -51.64118 | 2025-12-13 04:50:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 68408af1-5a09-3682-ac48-b05129f86f5e | -3.20801 | -41.8588 | 2025-12-13 04:50:00 | NOAA-21 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 30.5 |
| ed654fe8-6c8e-33ec-9a41-b1d48ea6a9fb | -2.42159 | -51.92302 | 2025-12-13 04:50:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a8c7b767-966e-30fa-a1a5-720e567cd7fb | -2.2547 | -53.75854 | 2025-12-13 04:50:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4f5d2dca-f8cf-33b9-9dce-2d4ff8585ed7 | -1.41762 | -52.5735 | 2025-12-13 04:50:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 539795b3-9c0e-3194-85c0-9364bf1876a9 | -2.49936 | -51.81551 | 2025-12-13 04:50:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ebae5ad5-6513-34ca-8f60-19855028361a | -2.53967 | -51.23345 | 2025-12-13 04:50:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 02e0f82f-28aa-3362-a363-521258e66aa3 | -2.48378 | -47.77185 | 2025-12-13 04:50:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 644cf76f-a911-392f-a448-e79030e48217 | -1.20111 | -51.82925 | 2025-12-13 04:50:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8d4307eb-0dfd-36d7-b47e-0ab6676048fe | -3.37567 | -45.48967 | 2025-12-13 04:50:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 5f9645ee-6b2f-3d49-85e3-33f4abdea504 | -2.48829 | -47.76779 | 2025-12-13 04:50:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 71a491fe-e600-30a6-bfba-d19beafc3d08 | -2.63513 | -46.94889 | 2025-12-13 04:50:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3663efa6-7bec-3692-9826-731f55e451db | -1.18364 | -52.09481 | 2025-12-13 04:50:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 64253458-548b-3e6e-97cd-770f4ac69513 | -2.4282 | -51.92405 | 2025-12-13 04:50:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| beefe077-62c5-340e-a754-c1c29e8bda9c | -2.4249 | -51.92353 | 2025-12-13 04:50:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f129d88a-b1fe-336d-a195-994c6ea47cc9 | -2.23822 | -46.51366 | 2025-12-13 04:50:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2ff8cfb2-32b9-34a9-bdd8-be019bae5523 | -3.68912 | -43.94228 | 2025-12-13 04:50:00 | NOAA-21 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 38d191f2-5d3d-3a42-889e-0a53df37500b | -2.44573 | -52.22265 | 2025-12-13 04:50:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 89bf7706-63e4-3e25-af32-d8285334c545 | -1.99071 | -52.06664 | 2025-12-13 04:50:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 353c32be-58dc-3fb3-b2a9-0a93f26804f7 | -1.84638 | -54.52832 | 2025-12-13 04:50:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 081d58f5-49c3-38f0-9615-d7ad9edd2abc | -2.69451 | -51.78671 | 2025-12-13 04:50:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6feaca6a-7a87-3557-b2d1-e26cd888f37e | -2.49491 | -51.80075 | 2025-12-13 04:50:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f087c780-c712-359b-98f3-2a7ce4ab729c | -1.20496 | -51.8299 | 2025-12-13 04:50:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c804e4e3-0d85-339c-9a12-6b4570fe085e | -1.47719 | -54.2004 | 2025-12-13 04:50:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 58eaecc6-5e4b-384f-a382-90b891025fa0 | -2.66796 | -46.89396 | 2025-12-13 04:50:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 136f44ab-d187-3086-92e0-dd4440b7537f | -2.15107 | -53.76986 | 2025-12-13 04:50:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c89e4374-f812-3dca-8167-3f728ec3d84c | -1.90643 | -54.23677 | 2025-12-13 04:50:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1d112029-7adb-396c-a834-0684bfae918f | -1.12102 | -47.73536 | 2025-12-13 04:50:00 | NOAA-21 | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5858d93d-4578-342c-87d9-4e8b43fda00e | -2.09447 | -53.4176 | 2025-12-13 04:50:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4779f588-378f-380d-ae15-2d62bd9e7b78 | -2.42069 | -46.15483 | 2025-12-13 04:50:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3a01a93a-44f1-35e0-9568-81ef6fc70168 | -2.78691 | -45.78429 | 2025-12-13 04:50:00 | NOAA-21 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6b02f17e-69d5-3334-80d1-049b411aef24 | -2.43804 | -46.26678 | 2025-12-13 04:50:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a58d9579-2b40-3c33-bd54-5be048a61d19 | -2.69505 | -51.78328 | 2025-12-13 04:50:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9a96408a-7f33-3b85-a108-15d79e30319c | -2.09896 | -53.43324 | 2025-12-13 04:50:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 9aa218d4-e78e-3a47-a555-2af212f568a4 | -2.42436 | -51.92697 | 2025-12-13 04:50:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ae0f5ba8-54be-3cc3-a896-57629e562913 | -2.656 | -51.64359 | 2025-12-13 04:50:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 11511950-4b79-3a22-a007-dc702a5caef7 | -2.44519 | -52.2261 | 2025-12-13 04:50:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 03b66dd0-3665-332e-9ed0-bb1d63bb74d7 | -5.07805 | -43.68024 | 2025-12-13 04:53:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c20da2ca-46ef-38fa-ace4-3ff2646beb48 | -4.4675 | -50.64002 | 2025-12-13 04:53:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ca0ff5a4-397c-32ce-809f-0472734664dc | -3.56684 | -47.18206 | 2025-12-13 04:53:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| add37d8f-a809-32db-bf03-bffad5f56948 | -3.80407 | -49.03536 | 2025-12-13 04:53:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| ccbd409a-fcd3-3fa0-989d-b808370ea076 | -3.67387 | -47.16356 | 2025-12-13 04:53:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c23ca664-3477-3a0f-a2ec-61b40509f4d9 | -5.06942 | -43.66646 | 2025-12-13 04:53:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0803de14-cdf6-3d16-ba9f-dd0530fba904 | -2.8114 | -52.38625 | 2025-12-13 04:53:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| be360391-ed83-3942-9ead-503f309c9af0 | -4.48603 | -55.80146 | 2025-12-13 04:53:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 66c1c77a-36b7-3a9e-90da-64efd60d3489 | -4.83083 | -49.53924 | 2025-12-13 04:53:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 315f8c4d-a3a0-3e30-b41c-21b861dbb20d | -3.81488 | -47.0526 | 2025-12-13 04:53:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a8dc295d-84d9-33ca-a3fe-3e2380f15c9e | -10.23808 | -52.22816 | 2025-12-13 04:53:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| facff40b-b4ec-3227-847e-6895fd121f15 | -2.88602 | -53.01248 | 2025-12-13 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a6044345-f97d-340b-8e35-0fc3f5f94bfa | -10.37497 | -45.05415 | 2025-12-13 04:53:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6443f35b-8724-3069-8b92-64d6252f7034 | -3.8189 | -47.05328 | 2025-12-13 04:53:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ef33727a-7eb7-3118-90ca-ba98d8c5a1e6 | -5.98757 | -44.59589 | 2025-12-13 04:53:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 137507b5-0857-3e3e-af0b-85969f5be6a0 | -2.81417 | -52.39021 | 2025-12-13 04:53:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 79776fe6-4db1-3885-a09b-396e3b4117a9 | -2.94844 | -52.55346 | 2025-12-13 04:53:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dea31f9b-c3da-3660-bc4a-048fa3e87a4a | -3.31289 | -54.76749 | 2025-12-13 04:53:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f987c0c8-a5a7-3f8d-9419-16dccf85d29a | -9.65471 | -56.86901 | 2025-12-13 04:53:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fd175459-7492-366a-8696-c9887b654223 | -3.15765 | -54.60564 | 2025-12-13 04:53:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4cdbc983-d464-3463-9490-c55826648336 | -2.88323 | -53.00847 | 2025-12-13 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d9174dc8-b837-3f24-a050-f7c6dbceb45e | -3.8154 | -47.0491 | 2025-12-13 04:53:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 97820688-9b82-3fea-b41c-0c67c906021b | -10.23863 | -52.22454 | 2025-12-13 04:53:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| f3c35a1f-4248-352d-939b-e65229631155 | -3.22544 | -54.77105 | 2025-12-13 04:53:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3aaa695d-1e88-34b7-8128-7c36947e88e0 | -2.77461 | -54.52753 | 2025-12-13 04:53:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 30322a6b-99e5-3196-931a-17268e7dfcb1 | -3.6978 | -53.75597 | 2025-12-13 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f5737f65-fe40-3445-8248-93096cd37466 | -2.81471 | -52.38676 | 2025-12-13 04:53:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 27b1e261-6863-3875-890d-ff66490156d3 | -2.95508 | -52.55447 | 2025-12-13 04:53:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 7e4291d0-baa7-3a74-86e4-edd052cbbd5b | -14.81779 | -59.94995 | 2025-12-13 04:53:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6ba44ade-0637-35bc-ab6f-a2ad156bce09 | -4.68933 | -43.24363 | 2025-12-13 04:53:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c40b96bd-a142-3d7e-9e6c-1d117be83a04 | -9.65836 | -56.8696 | 2025-12-13 04:53:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 866f2589-e1b2-3956-92b5-9fd53e1fc50c | -3.81137 | -47.04845 | 2025-12-13 04:53:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f8efa83c-729b-3bd4-a577-8afbd4cd13c8 | -2.94177 | -53.02835 | 2025-12-13 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8d6b4cdc-7825-3b8d-9c65-4daee069af2e | -3.19123 | -51.11131 | 2025-12-13 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| bf2b3421-26e6-35f5-bd1c-77289e415856 | -3.51943 | -52.18726 | 2025-12-13 04:53:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 66da800f-800c-3ea9-b5b2-c51fbf09c0c5 | -3.15711 | -54.6057 | 2025-12-13 04:53:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| eee500ca-265c-3904-9984-652ab2a9feb1 | -2.88937 | -53.013 | 2025-12-13 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 98c49a93-ddef-3cce-b9bf-abdb068f306d | -4.69463 | -43.24441 | 2025-12-13 04:53:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d7e002d5-9a9f-3583-8263-db0ff3a9e17a | -3.05028 | -53.00903 | 2025-12-13 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e466535f-28ca-37b6-8e7c-f306f3a07354 | -3.42778 | -52.92159 | 2025-12-13 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d646420a-33da-3905-b587-6f3377e4b1bd | -3.48806 | -52.36567 | 2025-12-13 04:53:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bd58e743-50ea-34e3-9830-c552a9b9cff3 | -3.23063 | -52.64056 | 2025-12-13 04:53:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0ddbea35-52d1-38d5-81d8-d1af3ed73d45 | -2.91372 | -52.38498 | 2025-12-13 04:53:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 45d28fd1-d0e3-3bb5-8748-15719acef45f | -3.15421 | -54.60119 | 2025-12-13 04:53:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| a8331bcb-7073-3414-bcdc-05efd02449cf | -5.03048 | -56.1941 | 2025-12-13 04:53:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| fdd8c3b8-3d14-3e3f-a8b6-b933d5112e1d | -2.99275 | -52.87796 | 2025-12-13 04:53:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| fa98786b-891d-31d3-b72c-479c6a3f4e77 | -10.24089 | -52.2323 | 2025-12-13 04:53:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 94adc2b7-8126-385a-924b-1c43258ba9de | -3.04972 | -53.01254 | 2025-12-13 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 37853515-cc16-3c13-b920-54b6ba11e51c | -2.97307 | -52.72093 | 2025-12-13 04:53:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 06980355-70c8-3de4-9f29-56c53010917d | -10.36987 | -45.05346 | 2025-12-13 04:53:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 88d4a0c8-f0c0-30b2-9bc5-3e5772b235c5 | -3.16429 | -51.30635 | 2025-12-13 04:53:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| b5289524-12ac-388d-b442-bd21655565b3 | -2.93843 | -53.02782 | 2025-12-13 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 84d485e9-f91f-35d2-8687-2963ea0e9b52 | -2.84082 | -54.24686 | 2025-12-13 04:53:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2e10e337-9e6c-3a6e-835b-ca7d4ae3e223 | -4.36775 | -55.77226 | 2025-12-13 04:53:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 40ef78b5-e901-36a6-a0f0-375200246b6c | -3.0701 | -52.83965 | 2025-12-13 04:53:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6c0489c7-9991-385c-b2f4-b93abe40fab4 | -2.99608 | -52.87848 | 2025-12-13 04:53:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 380334ca-aa44-372a-9e57-6b3d8bce076c | -2.93898 | -53.02429 | 2025-12-13 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| da9c7cc0-e053-3707-a287-fb7d3018c7c3 | -2.95176 | -52.55397 | 2025-12-13 04:53:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 14374d5d-5915-3071-bf20-e92a7105e64b | -14.81712 | -59.95366 | 2025-12-13 04:53:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| aa664e96-6c21-3286-b23e-73c3bcabb21e | -3.5189 | -52.1907 | 2025-12-13 04:53:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2c4519af-3b3c-3146-a1ed-81168114ca37 | -4.70742 | -55.98675 | 2025-12-13 04:53:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9cbd1279-92fc-3969-87af-98b1b33673c1 | -3.43699 | -54.60348 | 2025-12-13 04:53:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 29685bbf-5563-3d97-9f78-57e22558e20e | -3.7443 | -50.94241 | 2025-12-13 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README11.md)
