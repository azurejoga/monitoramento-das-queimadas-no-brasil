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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fc9877a4-54a8-34ea-b707-e30b87353fce | -6.9605 | -42.8816 | 2025-06-27 02:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 348.3 |
| 864caa9c-6d30-39cc-ad7a-c71c384fd217 | -11.559 | -52.117 | 2025-06-27 02:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 146.5 |
| 1517f168-f3be-3a0e-83eb-011ce76a0f24 | -6.9793 | -42.8798 | 2025-06-27 02:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 142.0 |
| 5518fb23-f1de-35cf-a92c-65b61bdbf9a0 | -6.9416 | -42.8834 | 2025-06-27 02:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 65.2 |
| 9ea05e1b-f266-3b0c-8751-94432cebfe02 | -11.0644 | -55.3757 | 2025-06-27 02:00:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 72.9 |
| 397d2acf-2fab-3ede-8e46-883d2410c42a | -8.6097 | -51.5731 | 2025-06-27 02:00:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 122.9 |
| f9235212-80d4-36af-9c5a-0b39286210a9 | -11.5969 | -52.113 | 2025-06-27 02:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 110.6 |
| 27c936b4-bbf8-3d5b-9b55-39c755fd4f99 | -6.1789 | -48.0929 | 2025-06-27 02:00:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 144.8 |
| 0b374cc4-cff0-3215-bf3f-c3d5274e9cee | -6.1791 | -48.0712 | 2025-06-27 02:00:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 85.9 |
| f3dace2b-6cd9-39c3-8b37-fa80b09b0d54 | -7.2219 | -43.0682 | 2025-06-27 02:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 78.0 |
| 2d35d492-27ae-34f9-b8d4-7ae2c53484a7 | -11.5779 | -52.115 | 2025-06-27 02:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 535.9 |
| 449656c5-ec7f-3e86-934c-29d785c2197c | -6.9602 | -42.9052 | 2025-06-27 02:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 293.9 |
| 2a230032-4017-32d9-b74b-00dad507982c | -8.6282 | -51.5925 | 2025-06-27 02:00:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 46.0 |
| fd4244d9-2c7f-35e0-aab1-c118b624fd9a | -7.2031 | -43.0701 | 2025-06-27 02:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 73.9 |
| 8f12121a-feaf-3e26-9d87-2b981bd3bb02 | -10.71143 | -59.14719 | 2025-06-27 02:00:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 20.3 |
| 21bc3de1-79f0-3c24-8b38-cad585814700 | -11.5779 | -52.115 | 2025-06-27 02:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 503.4 |
| c21963c8-7692-3cfa-9cbe-48759684a970 | -6.1791 | -48.0712 | 2025-06-27 02:10:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 72.5 |
| 65757d81-af1d-32b6-9141-c7d24be5774c | -11.5776 | -52.136 | 2025-06-27 02:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 112.6 |
| d710a0f2-b1d6-303f-bc91-4bfbd8a7bbec | -8.6097 | -51.5731 | 2025-06-27 02:10:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 105.3 |
| 52de34b9-cc45-3851-8cf6-ca620df83b24 | -6.9793 | -42.8798 | 2025-06-27 02:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 133.4 |
| 1a1c7e52-4ec0-39be-b577-fc7ace6c63e2 | -11.5592 | -52.096 | 2025-06-27 02:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 45.4 |
| 6075150a-c885-3cc6-9fd5-cec8412c6248 | -8.6282 | -51.5925 | 2025-06-27 02:10:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 46.3 |
| 4d36b1c2-8ef3-30ed-868f-a06e9af795b0 | -11.5782 | -52.094 | 2025-06-27 02:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 121.2 |
| 264068e3-4eb9-3f1d-b922-bf7f7dbea67e | -11.0644 | -55.3757 | 2025-06-27 02:10:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 70.4 |
| fe80a146-df5a-32f6-bbf8-60c9dc03dbaf | -11.559 | -52.117 | 2025-06-27 02:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 156.0 |
| 3bb00109-1dfe-36ac-ac03-a7e8e26c9f82 | -6.9602 | -42.9052 | 2025-06-27 02:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 301.2 |
| 0b060c2a-d69d-33b8-91c5-cd3a4076d18f | -6.9416 | -42.8834 | 2025-06-27 02:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 72.0 |
| 8e531cc6-f9da-306c-ac2c-dbb8ea164b3f | -8.6284 | -51.5716 | 2025-06-27 02:10:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 82.7 |
| 7605bc9e-ce9e-3dfb-8ec6-bb3e1a00142d | -6.9414 | -42.907 | 2025-06-27 02:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 69.2 |
| b85998cc-9138-3db8-9669-148dd53ea438 | -6.9605 | -42.8816 | 2025-06-27 02:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 326.5 |
| d0ae1dbc-d82a-3c2b-8b52-7a53987c9e7c | -6.1789 | -48.0929 | 2025-06-27 02:10:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 132.4 |
| dd9a0f47-15a6-3b6e-aff2-7164550f7fec | -8.6094 | -51.594 | 2025-06-27 02:10:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 65.9 |
| 20137568-8fd4-3221-972c-99346a0f818a | -6.9791 | -42.9034 | 2025-06-27 02:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 130.7 |
| 37b52214-b7a7-3f4a-8b66-467b6649a594 | -11.5969 | -52.113 | 2025-06-27 02:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 106.7 |
| 7290e511-8720-3b9c-b9f2-bec1e781d5db | -7.2219 | -43.0682 | 2025-06-27 02:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 67.5 |
| d08b3da6-017d-3a13-825a-82d4d3e86608 | -7.2031 | -43.0701 | 2025-06-27 02:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 75.7 |
| 3b0cad4d-a687-3b06-931f-e2af396b5ff0 | -6.9791 | -42.9034 | 2025-06-27 02:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 147.4 |
| f3615da2-a644-3b88-845a-663266402b75 | -11.5969 | -52.113 | 2025-06-27 02:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 103.2 |
| 341ca12e-908d-38b5-a773-e7ee2ed5b236 | -8.6097 | -51.5731 | 2025-06-27 02:20:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 86.6 |
| f7c5fba6-d34d-33f5-b334-301047fc08cd | -6.1789 | -48.0929 | 2025-06-27 02:20:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 122.8 |
| 9ea7d0af-2fc2-380b-a3ce-881d82702fcb | -6.1791 | -48.0712 | 2025-06-27 02:20:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 68.4 |
| 068451dd-5206-39d5-ad09-ee092465652b | -6.9793 | -42.8798 | 2025-06-27 02:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 126.9 |
| d2653d8e-d888-394c-9617-902ba579178b | -8.6094 | -51.594 | 2025-06-27 02:20:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 54.5 |
| f00b3af1-272d-3019-ba09-6caef846ad16 | -7.2219 | -43.0682 | 2025-06-27 02:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 69.4 |
| fdc070c5-0fb5-3678-ac74-2d039ea3f55b | -7.2031 | -43.0701 | 2025-06-27 02:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 66.4 |
| 7669d534-6681-3e42-b7f5-670928739338 | -8.6284 | -51.5716 | 2025-06-27 02:20:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 63673832-1f8e-342c-b8c7-9905fa4ea643 | -6.9602 | -42.9052 | 2025-06-27 02:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 328.9 |
| adaf5652-b699-358f-986d-72e415f6c061 | -11.5782 | -52.094 | 2025-06-27 02:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 122.5 |
| b1e4c42a-03b0-3f9b-9c23-9db0f73ee078 | -11.0644 | -55.3757 | 2025-06-27 02:20:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 66.8 |
| 06180dbc-42de-3c3a-879b-e2a3e6714792 | -6.9605 | -42.8816 | 2025-06-27 02:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 298.0 |
| 5ea1860f-67c8-3b88-a372-c4898356d44a | -11.5776 | -52.136 | 2025-06-27 02:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 102.6 |
| ab63865d-92ac-39c7-889c-c3d09821f608 | -11.5779 | -52.115 | 2025-06-27 02:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 506.4 |
| 3aa429fb-87fd-3987-88fa-d199c047d868 | -11.559 | -52.117 | 2025-06-27 02:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 137.2 |
| 3fab664c-7867-3179-9e40-0582f75d14dd | -11.5969 | -52.113 | 2025-06-27 02:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 102.6 |
| d8d8952e-2760-37b4-856c-2c487014ad8b | -6.9602 | -42.9052 | 2025-06-27 02:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 314.0 |
| 1b6e245a-bd55-30f4-9f1e-5165a922e9af | -6.1791 | -48.0712 | 2025-06-27 02:30:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 72.6 |
| 64a6b42a-4844-3227-9330-a90dc9dd00d3 | -6.9793 | -42.8798 | 2025-06-27 02:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 136.9 |
| 8fb269dc-ee39-3bf7-8dcf-f7b8fa1cc268 | -8.6097 | -51.5731 | 2025-06-27 02:30:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 81.1 |
| a8c6dc69-f00a-39a1-8a0f-7d81513dcce9 | -7.2219 | -43.0682 | 2025-06-27 02:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 64.1 |
| ff2b8cf9-1c16-3bcc-8db3-b4bc17b52d03 | -6.9791 | -42.9034 | 2025-06-27 02:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 139.1 |
| 92320d3b-12bf-3058-bfc7-82e2385faaaa | -6.9605 | -42.8816 | 2025-06-27 02:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 343.5 |
| cf653601-5c5d-3160-8e42-4a65a1a91ed8 | -11.5782 | -52.094 | 2025-06-27 02:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 147.5 |
| 3bd74d38-a418-3cf5-9c70-2aa5542df2ed | -11.559 | -52.117 | 2025-06-27 02:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 121.5 |
| 1ba27c98-721e-3d55-956f-60cc163a4974 | -6.1789 | -48.0929 | 2025-06-27 02:30:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 91.1 |
| bd047e84-f1dd-350b-ba04-a50e8321f97d | -11.5776 | -52.136 | 2025-06-27 02:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 112.5 |
| ff554010-df77-336b-937e-5dd9705626c4 | -11.0644 | -55.3757 | 2025-06-27 02:30:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 58.8 |
| a829c464-c80d-3d35-be8a-b866e6b2950d | -11.5592 | -52.096 | 2025-06-27 02:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 47.2 |
| bc5c6f02-f2b9-3f67-98e2-14debd747afb | -11.5779 | -52.115 | 2025-06-27 02:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 428.1 |
| 80703164-08ec-34ef-83a6-fff74103558d | -8.6284 | -51.5716 | 2025-06-27 02:30:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 56.1 |
| ffe88b1c-912a-3f9d-abbb-990e8d7a1d48 | -6.9602 | -42.9052 | 2025-06-27 02:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 323.8 |
| b1fd579c-706f-3c08-a04b-b67e18da65af | -6.9416 | -42.8834 | 2025-06-27 02:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 63.1 |
| 66331bbf-3515-3f36-ad00-212f0924cfe8 | -7.2031 | -43.0701 | 2025-06-27 02:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 69.5 |
| 7a3a74be-d72d-38c4-8a99-c33b351a91d7 | -11.5776 | -52.136 | 2025-06-27 02:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 103.8 |
| b418477d-928f-3c89-8b15-ad7799af7334 | -11.5782 | -52.094 | 2025-06-27 02:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 175.6 |
| 73b3c1ca-cfff-3899-92c4-ff9eb04cc42f | -8.6097 | -51.5731 | 2025-06-27 02:40:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 56.7 |
| 70cdcc86-a870-31f3-a7ba-0a7fb24d66d5 | -6.9605 | -42.8816 | 2025-06-27 02:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 285.2 |
| ce5c5446-493e-3987-8e73-964318de5234 | -11.559 | -52.117 | 2025-06-27 02:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 85.5 |
| 7dba996b-62ba-36ad-bc5e-b0ad97aadc5d | -8.6284 | -51.5716 | 2025-06-27 02:40:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 54.4 |
| 561836ee-63f0-3ff9-aa92-3dfdfe03dd52 | -11.5969 | -52.113 | 2025-06-27 02:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 76.4 |
| e42f9cfd-3539-3bbe-91d8-09976f2f9b0c | -6.1789 | -48.0929 | 2025-06-27 02:40:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 94.8 |
| f28b825d-67f0-31b1-8194-5407c7943de6 | -6.9791 | -42.9034 | 2025-06-27 02:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 165.0 |
| 9697f70e-380f-386c-afbf-e7c680cbc23c | -11.5779 | -52.115 | 2025-06-27 02:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 466.9 |
| a3fd6389-12f1-381f-85b0-d5ae46d25e3e | -6.9414 | -42.907 | 2025-06-27 02:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 72.6 |
| a49bdb86-b39c-3ea6-b4df-8faf7598b75f | -6.1791 | -48.0712 | 2025-06-27 02:40:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 55.8 |
| 3da81496-4bef-3eb0-9c21-0e2387b121da | -6.9793 | -42.8798 | 2025-06-27 02:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 142.4 |
| 6767f3ac-87cc-3dbd-8830-1617a57b91e0 | -11.0644 | -55.3757 | 2025-06-27 02:40:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 50.9 |
| 3d0b9b2c-0822-30af-874d-acecaf9730cd | -11.0644 | -55.3757 | 2025-06-27 03:00:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 56.0 |
| fda2db1f-9aec-30b1-9895-096dcdb2dfb6 | -6.9793 | -42.8798 | 2025-06-27 03:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 141.1 |
| 5eda5510-cadb-3c11-a5b7-985431dc52e9 | -11.559 | -52.117 | 2025-06-27 03:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 161.2 |
| bd06833a-87be-36a1-b731-eb0b8cbbaba4 | -11.5779 | -52.115 | 2025-06-27 03:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 365.6 |
| 9a0fee15-6323-35dd-8835-0ad19c523954 | -6.1789 | -48.0929 | 2025-06-27 03:00:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 70.0 |
| 6874b347-3028-3f78-8ee2-f27ebf583b3c | -6.9791 | -42.9034 | 2025-06-27 03:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 138.6 |
| 36e29d5c-8887-3e76-be7f-829e4ecfe01f | -6.9414 | -42.907 | 2025-06-27 03:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 68.1 |
| e20a2499-b955-390d-9903-63106e0cfd2c | -6.9416 | -42.8834 | 2025-06-27 03:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 71.0 |
| d5570335-08f9-3a4d-9c58-0bd57c9fbfbf | -8.6097 | -51.5731 | 2025-06-27 03:00:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 78b89c7a-5d2d-3bcb-8f82-7f9ebb5688b8 | -6.9602 | -42.9052 | 2025-06-27 03:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 360.9 |
| 2266c7cf-5bb6-3c77-aba4-b964f31d7bd4 | -6.9605 | -42.8816 | 2025-06-27 03:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 393.9 |
| 98240f08-5a1d-3997-b97c-c3b66b902d7d | -11.5782 | -52.094 | 2025-06-27 03:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 99.6 |
| bd22f6b7-20a5-32f3-8174-e9d7d024d3ab | -11.5969 | -52.113 | 2025-06-27 03:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 95.0 |
| 60ed0cf8-ba66-3ee5-bd16-8aedaae8cece | -6.1791 | -48.0712 | 2025-06-27 03:00:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 47.7 |


[Clique aqui para ver as próximas entradas](README7.md)
