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

## Dados Diários - Página 88

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 46b7937b-31b2-3490-9713-487fc786a8cd | -17.9546 | -44.3882 | 2026-08-21 11:50:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 124.9 |
| aa6a0084-bb79-38d2-b2c6-a2948a941bde | -9.4071 | -60.417 | 2026-08-21 12:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 71.4 |
| 8ec2c3c2-7736-37c7-b3b1-c1ca0329cd69 | -13.2431 | -51.6295 | 2026-08-21 12:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 71.9 |
| 842004e3-7705-3245-9674-d493cda28b7f | -11.1747 | -54.0216 | 2026-08-21 12:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 76.6 |
| 1cf7f55d-c7ba-38d9-a5d6-73bdb4b145fb | -14.3343 | -51.8944 | 2026-08-21 12:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 110.9 |
| 96ff464b-67f4-3b2c-a50c-fce9d5f9b7fb | -11.1747 | -54.0216 | 2026-08-21 12:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 80.8 |
| 4abc1a0c-1f62-31a7-b500-dab3808a403e | -14.3343 | -51.8944 | 2026-08-21 12:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 92.4 |
| 3abf2d5b-b0e7-3944-85fd-d88964370226 | -9.4071 | -60.417 | 2026-08-21 12:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 74.7 |
| d4e3ed4e-0fbf-328b-a5b4-cf5b52f0fdad | -17.9546 | -44.3882 | 2026-08-21 12:10:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 101.2 |
| e5e41b0d-c41f-3ff0-81db-77f24a3dad3b | -22.8482 | -49.3487 | 2026-08-21 12:10:00 | GOES-19 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 135.8 |
| ab1c5e7f-4e43-37cc-87e7-5ed53617a656 | -6.8755 | -59.4364 | 2026-08-21 12:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 66.7 |
| 9f630894-ee93-330c-86f5-5513abc847c6 | -4.47049 | -55.39834 | 2026-08-21 12:12:00 | TERRA_M-T | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| e5c37dc8-8914-33b7-a9bc-dcbaf7c4aabf | -4.96207 | -45.14642 | 2026-08-21 12:12:00 | TERRA_M-T | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 28.0 |
| 276a1584-1c2f-3224-ae60-3195d3b0e9f1 | -14.34262 | -51.89017 | 2026-08-21 12:14:00 | TERRA_M-T | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 57.5 |
| b428ff9e-199a-30f3-a8ec-953dc7912882 | -14.72418 | -47.13366 | 2026-08-21 12:14:00 | TERRA_M-T | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 85.2 |
| 6ef2ef68-5dd3-336c-ac09-96b63b66ce53 | -8.07604 | -50.11279 | 2026-08-21 12:14:00 | TERRA_M-T | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| f5db3b74-99ef-3c85-9fa3-3a0e9426547d | -6.89921 | -55.70799 | 2026-08-21 12:14:00 | TERRA_M-T | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 1605c07e-6491-3dca-af34-6703da9924ed | -9.41018 | -60.41668 | 2026-08-21 12:14:00 | TERRA_M-T | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 77.5 |
| 2a3cc7fb-ea98-33c5-a255-218ea0e24e0f | -12.51491 | -54.75928 | 2026-08-21 12:14:00 | TERRA_M-T | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 53d61b98-21b6-34f1-94e2-2e098db100e6 | -8.07769 | -50.10015 | 2026-08-21 12:14:00 | TERRA_M-T | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 6229b730-d1d3-3198-b43f-c9cb502acbbe | -9.44983 | -51.61124 | 2026-08-21 12:14:00 | TERRA_M-T | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 01de506b-3571-3bcf-aeee-4fe0ebf8e429 | -5.67177 | -51.64632 | 2026-08-21 12:14:00 | TERRA_M-T | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 42.0 |
| c6a44f01-75f9-3d5e-a755-459134e3f1b1 | -11.18114 | -54.01934 | 2026-08-21 12:14:00 | TERRA_M-T | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 18.3 |
| 808c8907-6514-3d56-b285-b037eceaeea2 | -10.7667 | -50.30118 | 2026-08-21 12:14:00 | TERRA_M-T | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 35.7 |
| a0ee5319-c395-340e-bd34-d85b9325bbbe | -10.01099 | -53.94845 | 2026-08-21 12:14:00 | TERRA_M-T | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 22.3 |
| b7dd5819-3739-338c-a6d5-fde6a4ee299a | -6.90476 | -55.22206 | 2026-08-21 12:14:00 | TERRA_M-T | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 3dc57d15-e555-3bfe-a7bc-74f26d887994 | -6.75596 | -59.16062 | 2026-08-21 12:14:00 | TERRA_M-T | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 9f2a602e-0848-3854-ae1d-e64aa671cb6f | -13.26523 | -51.62631 | 2026-08-21 12:14:00 | TERRA_M-T | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 47.9 |
| fc10827c-198b-39a8-9272-4ae02e47002b | -8.08791 | -44.35481 | 2026-08-21 12:14:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 59.8 |
| b3f594b1-fd4c-3510-97eb-40eef482b462 | -6.87372 | -43.73471 | 2026-08-21 12:14:00 | TERRA_M-T | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 89.4 |
| 7fc2870e-06e6-32cb-abd3-cea2e368a718 | -8.16331 | -46.73679 | 2026-08-21 12:14:00 | TERRA_M-T | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 35.0 |
| b6cb00e0-b3ce-3138-9f32-4ed258c5e46b | -13.43687 | -51.79548 | 2026-08-21 12:14:00 | TERRA_M-T | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 25.3 |
| 818b99c3-aad0-30c9-9e50-6b1c848c1d66 | -6.89642 | -47.47319 | 2026-08-21 12:14:00 | TERRA_M-T | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 1fd5eaf1-3528-3c42-8416-04496e4f38f2 | -9.51768 | -58.36074 | 2026-08-21 12:14:00 | TERRA_M-T | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 18339e3a-d929-3e8a-abed-15088c3b5d83 | -9.42055 | -60.41221 | 2026-08-21 12:14:00 | TERRA_M-T | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 23.2 |
| 084b5aa9-6230-3913-a0cc-76ab00f315f3 | -14.24157 | -53.05091 | 2026-08-21 12:14:00 | TERRA_M-T | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 23d29aa5-43b7-33ef-b905-c24ac2ddd7d5 | -10.30884 | -50.37621 | 2026-08-21 12:14:00 | TERRA_M-T | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 15.7 |
| fb27394e-1c5e-38fc-89dd-d5751126731e | -10.52057 | -50.77655 | 2026-08-21 12:14:00 | TERRA_M-T | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 1f430ed3-940f-3180-8bb2-4722b38e289b | -8.46238 | -46.97719 | 2026-08-21 12:14:00 | TERRA_M-T | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 41.8 |
| 14047dd0-3a7c-3ab4-96d9-2d9bee44f511 | -13.25505 | -51.62511 | 2026-08-21 12:14:00 | TERRA_M-T | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 20.0 |
| 65df18e0-d5e9-3f0a-b843-d78babac3e67 | -8.5311 | -55.33149 | 2026-08-21 12:14:00 | TERRA_M-T | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 01c92c8d-0878-3b0d-9b2a-deb396a652de | -8.0914 | -51.66754 | 2026-08-21 12:14:00 | TERRA_M-T | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 8a0f0791-5593-382a-96e5-bab92407c823 | -8.58341 | -54.77686 | 2026-08-21 12:14:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| d798512e-9b1e-3f1a-8669-c46c186ad2be | -13.3788 | -54.38401 | 2026-08-21 12:14:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 16.8 |
| 1c523fc8-c97b-39ee-b87f-7a95f2516d58 | -9.33045 | -56.89991 | 2026-08-21 12:14:00 | TERRA_M-T | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 764b3c55-a99d-3228-9881-26edc09a639b | -6.24811 | -55.42233 | 2026-08-21 12:14:00 | TERRA_M-T | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| a1b26fc9-ebdd-3a74-bf7d-e03fd629124a | -11.5933 | -45.21189 | 2026-08-21 12:14:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 46.3 |
| 2324ec8a-3294-395f-9b4d-5da4218a8592 | -9.43735 | -48.24083 | 2026-08-21 12:14:00 | TERRA_M-T | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 31.9 |
| 5e1ad0c0-e513-3b62-831f-7a85b8a7f46b | -6.11661 | -53.07443 | 2026-08-21 12:14:00 | TERRA_M-T | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 091096f8-b9d7-3713-adf9-58f504556cac | -14.72377 | -47.12814 | 2026-08-21 12:14:00 | TERRA_M-T | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 65.5 |
| a385c6c9-f62f-3858-83a5-f8114110e9fc | -8.52974 | -55.34072 | 2026-08-21 12:14:00 | TERRA_M-T | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 007ec67d-dc15-35d9-a4d3-9bc03769e8cf | -11.18242 | -54.01028 | 2026-08-21 12:14:00 | TERRA_M-T | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 19.3 |
| 589c6280-f998-3fb2-bdad-90b75a25a091 | -12.78259 | -48.39566 | 2026-08-21 12:14:00 | TERRA_M-T | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 76020ce5-896d-3f7d-a5c3-3bbdb6c0e94d | -8.18515 | -54.97975 | 2026-08-21 12:14:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 8a7409ac-c70b-30c6-b140-c5d1f2a7909e | -11.17098 | -54.02712 | 2026-08-21 12:14:00 | TERRA_M-T | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 25.5 |
| 09f8b351-68ea-3d6a-b293-82a90b2fc753 | -14.32079 | -51.89959 | 2026-08-21 12:14:00 | TERRA_M-T | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 21.1 |
| 0acd8028-c675-39db-82f2-cc5db226d7bf | -14.10411 | -58.85563 | 2026-08-21 12:14:00 | TERRA_M-T | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 10.5 |
| e7864d53-2cfa-3a16-af60-1e3aef7558ae | -12.00057 | -53.42977 | 2026-08-21 12:14:00 | TERRA_M-T | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 12.4 |
| de7d0374-faef-3dfa-9b2c-d0d99261e464 | -10.81775 | -50.99072 | 2026-08-21 12:14:00 | TERRA_M-T | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 7e677bd4-93b3-32e0-b13c-7633447fe141 | -13.66121 | -51.7941 | 2026-08-21 12:14:00 | TERRA_M-T | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 37.3 |
| 819c823e-8cf5-35ba-a732-43256ad514ef | -6.26135 | -48.6428 | 2026-08-21 12:14:00 | TERRA_M-T | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 26.5 |
| 9d9495a8-6fa4-3891-b34c-1f9619684961 | -9.21236 | -59.66196 | 2026-08-21 12:14:00 | TERRA_M-T | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 17.8 |
| 8e5418ce-7f38-3dcd-ad47-a2f037ee5ea3 | -10.76314 | -50.32844 | 2026-08-21 12:14:00 | TERRA_M-T | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 73c44b79-388e-3a7c-a39d-fdc64faac912 | -8.44531 | -46.95858 | 2026-08-21 12:14:00 | TERRA_M-T | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 50.4 |
| b0782217-5e4e-3ba7-b1b1-f064d3591397 | -14.72069 | -47.15604 | 2026-08-21 12:14:00 | TERRA_M-T | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 29.1 |
| a9b41b07-03ba-355a-85b5-8cae1975c3d2 | -7.00725 | -48.02826 | 2026-08-21 12:14:00 | TERRA_M-T | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 17c4c399-b27d-3da4-93d1-abd238d8be39 | -14.341 | -51.89574 | 2026-08-21 12:14:00 | TERRA_M-T | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 65.1 |
| 45511c57-46a1-3aee-b4e3-838bd644f5fd | -11.37633 | -46.36497 | 2026-08-21 12:14:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 30.9 |
| 3840249f-3901-3e28-9102-651cb21e2788 | -6.31521 | -55.9206 | 2026-08-21 12:14:00 | TERRA_M-T | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| a1f84aad-59a6-3b9d-929f-ff5ca0847ae1 | -7.35213 | -45.80914 | 2026-08-21 12:14:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 28.2 |
| d3aee11d-8155-332b-ae5d-104143d79909 | -13.66276 | -51.78205 | 2026-08-21 12:14:00 | TERRA_M-T | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 29.4 |
| 59651e8c-7720-3ecd-bfa7-5ea84a57b5b1 | -8.08248 | -44.34739 | 2026-08-21 12:14:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 54.6 |
| 705a9740-590c-317b-ae11-b7d99ffbdb9c | -13.24491 | -51.6236 | 2026-08-21 12:14:00 | TERRA_M-T | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 32.3 |
| 3623a52a-4f32-3dd4-a8f2-944a9370a481 | -14.33249 | -51.88883 | 2026-08-21 12:14:00 | TERRA_M-T | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 100.8 |
| 0bb30bd4-e33d-30bf-a194-a3ba19bac74a | -13.24334 | -51.63568 | 2026-08-21 12:14:00 | TERRA_M-T | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 45.2 |
| 578142ab-3759-3d78-a734-a791ff78c7ea | -6.70004 | -58.9309 | 2026-08-21 12:14:00 | TERRA_M-T | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 16.2 |
| 857a725d-ae0e-396a-9ee4-502a0618c9b5 | -13.43582 | -51.80127 | 2026-08-21 12:14:00 | TERRA_M-T | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 14.8 |
| fc2f6153-9b88-35cb-9b8d-2a211febbbb7 | -9.25646 | -59.81175 | 2026-08-21 12:14:00 | TERRA_M-T | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 11.3 |
| fde264e5-f60f-392b-8162-12e19c3e336a | -13.39026 | -54.36695 | 2026-08-21 12:14:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 5943b824-535e-35ef-9ef0-9d8a3c2a8a12 | -6.8897 | -56.4344 | 2026-08-21 12:14:00 | TERRA_M-T | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| b1fd3baf-3fb4-3183-ae4f-6c2d00b48c57 | -6.66468 | -56.35049 | 2026-08-21 12:14:00 | TERRA_M-T | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 2224b6ef-4b84-3372-a14c-ffcf31c08de6 | -14.05991 | -58.87973 | 2026-08-21 12:14:00 | TERRA_M-T | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 0c0d507d-b1b7-34b5-b4fb-3c977640f074 | -15.10976 | -48.0506 | 2026-08-21 12:14:00 | TERRA_M-T | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 26.2 |
| a80cb2fe-33da-34c9-8ec8-065612f9eb40 | -5.7892 | -50.11892 | 2026-08-21 12:14:00 | TERRA_M-T | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 855dcea2-f781-3578-9d5e-5180193ec37f | -9.41366 | -60.55238 | 2026-08-21 12:14:00 | TERRA_M-T | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 20.5 |
| dfd41301-2e11-3dc4-b410-506cd0c14640 | -11.68566 | -54.56625 | 2026-08-21 12:14:00 | TERRA_M-T | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| abf4797d-f0f6-3438-8745-b119fd158cc4 | -8.47258 | -46.96178 | 2026-08-21 12:14:00 | TERRA_M-T | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 63.3 |
| f1b1c094-59e1-396e-8019-4d9ca47cda79 | -10.53098 | -50.77767 | 2026-08-21 12:14:00 | TERRA_M-T | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 8.8 |
| adf97f9b-46be-3831-b714-4d9a668e04af | -8.10739 | -50.03722 | 2026-08-21 12:14:00 | TERRA_M-T | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 7b3b3e37-d7c8-38f4-812f-2b590461e5e2 | -8.66075 | -54.62971 | 2026-08-21 12:14:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 818b7f80-e8fb-327d-a119-7aa8738c653f | -13.23475 | -51.62219 | 2026-08-21 12:14:00 | TERRA_M-T | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 4537e0aa-97f9-3a6b-8764-1db26137eae1 | -13.66977 | -51.8074 | 2026-08-21 12:14:00 | TERRA_M-T | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 12.8 |
| d27c1692-cca2-379f-a3a2-bb914867a7a8 | -12.74735 | -48.47444 | 2026-08-21 12:14:00 | TERRA_M-T | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 429b060b-d991-300c-bf0d-d3b4a40545b4 | -9.79898 | -46.64728 | 2026-08-21 12:14:00 | TERRA_M-T | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 36.3 |
| e12b7559-484b-3969-8d13-3e99b9bcae01 | -7.46283 | -46.15386 | 2026-08-21 12:14:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 46.6 |
| fbfb8ba7-483d-3769-99ca-829be89fbf4b | -11.37028 | -47.21683 | 2026-08-21 12:14:00 | TERRA_M-T | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 21.4 |
| 66d186df-0ffe-3bcd-b177-1255e34041ab | -13.38898 | -54.37613 | 2026-08-21 12:14:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 12.9 |
| c21d55f4-1437-3c8c-988f-e50110549d80 | -11.35723 | -46.00117 | 2026-08-21 12:14:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 37.4 |
| 31ef7776-49c4-3f3d-9f0a-11acad5dc6fd | -8.66718 | -54.58515 | 2026-08-21 12:14:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| b442a524-c0f8-3101-b3a0-90a01f01bcc4 | -6.382 | -54.94896 | 2026-08-21 12:14:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |


[Clique aqui para ver as próximas entradas](README89.md)
