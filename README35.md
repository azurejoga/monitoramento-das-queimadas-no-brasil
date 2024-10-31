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

## Dados Diários - Página 35

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 33f35bfb-67bd-3673-b3ba-10aa0ceb1bf9 | -7.54658 | -45.5329 | 2024-10-31 04:49:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 45af1f86-bf0e-393d-a2cb-a86cd6beb1da | -7.54258 | -45.52716 | 2024-10-31 04:49:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 408cc380-4536-3675-80a6-ae71d52aa239 | -7.43587 | -45.65591 | 2024-10-31 04:49:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4a883a02-9011-3069-8321-946fbd4ebc45 | -7.35129 | -46.24707 | 2024-10-31 04:49:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9a7ef062-a003-3501-bcec-abf782982397 | -7.23814 | -45.53382 | 2024-10-31 04:49:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| e18376ea-a688-3525-a407-57326ef70f64 | -7.23743 | -45.53883 | 2024-10-31 04:49:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 398b3215-b71a-3c42-aa64-404da4fbc301 | -7.23385 | -46.72402 | 2024-10-31 04:49:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1584bf39-c24e-3d08-8c71-2d5ac084973c | -7.18271 | -46.32387 | 2024-10-31 04:49:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 70037b8f-0265-3d20-bc3a-800c77d2914e | -7.18208 | -46.32836 | 2024-10-31 04:49:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ee903bdd-d4ca-366f-87a5-d55ba5c4eea4 | -7.18147 | -46.33275 | 2024-10-31 04:49:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3aad138b-6a9d-3a8a-9fee-9a5d3d8187fd | -7.17767 | -46.3275 | 2024-10-31 04:49:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2c652b21-f914-3810-bbb8-e2112731ba66 | -7.17706 | -46.33187 | 2024-10-31 04:49:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b31c34b1-e582-3dd1-b91f-fa681e428194 | -7.00031 | -45.28445 | 2024-10-31 04:49:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4806ccfc-5b53-3651-b363-3234fa6a5b02 | -6.78426 | -45.4983 | 2024-10-31 04:49:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e33b5ea2-1b8e-3025-8687-685ae069554d | -6.78357 | -45.50319 | 2024-10-31 04:49:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fffaa838-8a34-3cb6-a927-85b30b3eb4ac | -6.72513 | -46.35377 | 2024-10-31 04:49:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 40bd40a8-2476-3a41-a6b5-be06bb9aafab | -6.52839 | -45.94516 | 2024-10-31 04:49:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e1635da1-f54d-3a92-8533-2db7721defd9 | -6.52387 | -45.94456 | 2024-10-31 04:49:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2a6f62bc-cb98-35bf-8686-fa1317c0b96a | -7.90744 | -46.6901 | 2024-10-31 04:49:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 145ff46d-76ed-38bf-a0bc-7d3e77891f8c | -7.90305 | -46.68952 | 2024-10-31 04:49:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| dd902ded-afa8-3c4b-9fdd-25a9a27f9865 | -7.90245 | -46.6938 | 2024-10-31 04:49:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 8c25d5d4-5eae-3397-81cd-9041de3ef337 | -7.86825 | -46.87328 | 2024-10-31 04:49:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e1daa344-10ea-34eb-804e-9faea1115849 | -7.85846 | -46.8802 | 2024-10-31 04:49:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6438c9cd-7312-36a4-b4aa-ed2530b0f7e2 | -7.85413 | -46.8796 | 2024-10-31 04:49:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 125b3340-a07c-3a3e-a47a-a89b8b7d0808 | -4.79739 | -46.47592 | 2024-10-31 04:49:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 9a976f3e-6498-3ae0-b715-826bb8dce03d | -4.76893 | -46.40796 | 2024-10-31 04:49:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6e9ab4c9-0224-3980-a704-3f7e625ab80d | -4.76833 | -46.4119 | 2024-10-31 04:49:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eee88c7c-cde2-350a-be0d-59acb0c46327 | -4.76772 | -46.41126 | 2024-10-31 04:49:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| abc0f15b-8f04-3f78-9143-17a3c98ed747 | -4.50083 | -47.10381 | 2024-10-31 04:49:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 42dfe029-e253-3b63-9c8a-178bdb53b7c6 | -4.49934 | -46.47504 | 2024-10-31 04:49:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9e7809be-d6f9-3045-823f-8a0f68b67e67 | -4.49514 | -46.47426 | 2024-10-31 04:49:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3709a3d5-9167-3638-9289-172d46b92c10 | -4.46841 | -46.45057 | 2024-10-31 04:49:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b01597fc-c59f-3bc3-b46b-76e450f5dfeb | -4.21518 | -46.4391 | 2024-10-31 04:49:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ceecbb30-f6ad-31fb-88ee-4ebd3631854d | -4.2146 | -46.44294 | 2024-10-31 04:49:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3c5e756b-a4db-35de-8018-532726ef4da6 | -4.19424 | -46.70106 | 2024-10-31 04:49:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.7 |
| afa657ba-00b6-3c67-8ae7-bcbf0eb41c39 | -4.19206 | -46.70129 | 2024-10-31 04:49:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1950b3c6-789f-3f19-9db9-a0e984c22580 | -4.13192 | -47.12504 | 2024-10-31 04:49:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 939542d9-f579-3c2f-a1ac-deadf4efdf3b | -4.12839 | -47.12106 | 2024-10-31 04:49:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2e3bda0a-e4e7-35a9-ad64-cc0de8220161 | -4.10129 | -46.59914 | 2024-10-31 04:49:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a2a1aab2-2f09-31ec-bbbf-64255b02eea8 | -4.0995 | -46.59909 | 2024-10-31 04:49:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 39d4f37c-b70f-3960-954f-1626cc9e3913 | -4.09712 | -46.5986 | 2024-10-31 04:49:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d5d90a5c-9e61-3516-bb88-6948a651581b | -4.0513 | -46.93936 | 2024-10-31 04:49:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4f1c5c83-a7a8-38e4-9994-0e819aca597d | -3.90389 | -46.44316 | 2024-10-31 04:49:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b4ab4acf-c171-3919-8640-06e169348ec3 | -3.90289 | -46.4433 | 2024-10-31 04:49:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 78a31f57-b690-317a-a04c-7bdc883a5c0c | -3.88636 | -46.21111 | 2024-10-31 04:49:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 09a90235-b2c2-311b-bc00-c58779c41fb0 | -5.39573 | -47.15501 | 2024-10-31 04:49:00 | NOAA-20 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 08f5bb6f-0e08-3bd6-ac35-1a30d01c0839 | -5.39109 | -47.15801 | 2024-10-31 04:49:00 | NOAA-20 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a1292baa-9306-3a49-8845-26e25073aa02 | -7.67034 | -47.32894 | 2024-10-31 04:49:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b2dc41c6-25a0-362f-a232-6b007c3b531b | -7.66724 | -47.32064 | 2024-10-31 04:49:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| ddff8279-781b-33d3-8ae4-40efcdedf189 | -7.66616 | -47.32832 | 2024-10-31 04:49:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5b08123b-bb9f-38fb-abbb-8bed87c74730 | -7.66575 | -47.32173 | 2024-10-31 04:49:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| cb5deeea-3612-3093-a517-248d66ea6d96 | -7.66562 | -47.33217 | 2024-10-31 04:49:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 44bb8f87-154a-303e-9b05-681d37fa8c36 | -7.66462 | -47.3294 | 2024-10-31 04:49:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5cffb540-03d1-3fd7-8e26-570b694e6364 | -7.66405 | -47.33325 | 2024-10-31 04:49:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1e6758dd-a3df-3e58-a916-ad1e8271ef10 | -7.66144 | -47.33157 | 2024-10-31 04:49:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 74703760-500e-3bde-acdf-34c273621dc0 | -7.58815 | -47.11699 | 2024-10-31 04:49:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5453d46f-5ce1-367c-b089-ed86ada7efdd | -7.588 | -47.11594 | 2024-10-31 04:49:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1c42da4a-561d-3acd-8c5d-28e1882f5e30 | -7.58392 | -47.11636 | 2024-10-31 04:49:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c6ed07cb-32e6-345d-82b9-45b6f63ae0e7 | -7.58376 | -47.11531 | 2024-10-31 04:49:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| dc2483cb-2481-30af-b61b-99b7adb5858d | -7.42016 | -47.11333 | 2024-10-31 04:49:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f131dd68-5392-3f23-be22-ed454a09d4bd | -7.15638 | -48.32128 | 2024-10-31 04:49:00 | NOAA-20 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b97f4d2e-652c-382e-b967-7fd2e99bafd2 | -7.15564 | -48.32624 | 2024-10-31 04:49:00 | NOAA-20 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ac05245b-a297-3c7a-86cc-650fc2ce828f | -6.69146 | -47.22102 | 2024-10-31 04:49:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fdd9578d-4f98-3787-aabe-c057b991e198 | -3.4863 | -48.2355 | 2024-10-31 04:49:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4578049f-5823-3b92-a404-4f08274a3756 | -3.44723 | -49.09597 | 2024-10-31 04:49:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 14fbd668-7b6d-391a-bd28-b46c1ea06a28 | -4.92788 | -49.15322 | 2024-10-31 04:49:00 | NOAA-20 | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3fb008f1-6435-3c56-a911-963f25524a7b | -4.89685 | -48.63938 | 2024-10-31 04:49:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e9541abc-6fbd-3da5-a5b6-4cebff88bf2b | -4.87042 | -48.57384 | 2024-10-31 04:49:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| eea90c0d-bf8d-3530-8fe2-d669df27d101 | -4.85829 | -49.30812 | 2024-10-31 04:49:00 | NOAA-20 | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4b7224ff-01f6-31c3-866f-f27fa71d4a7a | -5.52429 | -49.48843 | 2024-10-31 04:49:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| dc1bfae8-3563-301d-940c-523549f51bc1 | -5.52072 | -49.48787 | 2024-10-31 04:49:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c0755894-66ce-3893-af3e-b9a659b66e8f | -5.52011 | -49.49195 | 2024-10-31 04:49:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4917871d-8bfa-3a36-a7ea-c3307882b76b | -5.47157 | -49.0433 | 2024-10-31 04:49:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1a6f866b-f196-39fa-a04c-ac9276f8d0b5 | -4.97118 | -49.37379 | 2024-10-31 04:49:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| aca6cf56-77c2-33ea-809a-3e56733bbbd9 | -4.96761 | -49.37325 | 2024-10-31 04:49:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 25e1ed22-49f5-3201-9bd4-0fcde1b8ba8f | -6.99701 | -48.638 | 2024-10-31 04:49:00 | NOAA-20 | MURICILÂNDIA | TOCANTINS | Brasil | 1713957 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0fafbd26-e069-3841-991d-e1e65bcd8b1f | -2.88902 | -49.24305 | 2024-10-31 04:49:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 78378ab9-240e-3b5d-b731-c5452e1edddc | -2.88842 | -49.24696 | 2024-10-31 04:49:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7be8f48c-0aa4-30b3-8deb-3850bdbe8571 | -2.87849 | -49.24145 | 2024-10-31 04:49:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f991a9f0-54b9-3620-83c3-3d2037d94ee9 | -2.87498 | -49.24091 | 2024-10-31 04:49:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e39f86d5-e630-3a56-a6b1-721b5bd50589 | -2.87308 | -49.39172 | 2024-10-31 04:49:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d78e735f-001a-31b2-ad5e-a077cd41e55a | -2.86505 | -49.23538 | 2024-10-31 04:49:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a126a6df-cca3-3e1f-879e-6de2469284b2 | -2.86094 | -49.23875 | 2024-10-31 04:49:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4c5cb96b-a516-371e-bf15-85bc902a2a0e | -2.85743 | -49.37747 | 2024-10-31 04:49:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 15e5ff35-005b-3be7-b741-24db1667b349 | -2.85505 | -49.39287 | 2024-10-31 04:49:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 279ce671-4eca-3f66-a433-57ec8d0cdcba | -2.85156 | -49.39233 | 2024-10-31 04:49:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| adf4d684-5225-345d-a5a4-e83bcbe790eb | -2.84003 | -49.69435 | 2024-10-31 04:49:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9bbd6633-18e3-3f07-a335-61efe8fbf170 | -2.83517 | -49.24279 | 2024-10-31 04:49:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 00f614a6-7b73-3ed2-8999-7ba1c4ad8461 | -2.83509 | -49.26679 | 2024-10-31 04:49:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 30dfbc68-ebc6-3e2d-8e6b-7cb5e9209057 | -2.83345 | -49.23051 | 2024-10-31 04:49:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b773c889-c2b6-32a1-a79f-a1cd38cb3ace | -2.83285 | -49.23442 | 2024-10-31 04:49:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f865639a-e3f8-375b-a755-6461bc7a5bad | -2.83166 | -49.24226 | 2024-10-31 04:49:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 89fbeaf9-f997-3247-b890-7b470a7ae33f | -2.82994 | -49.22997 | 2024-10-31 04:49:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 56e51efe-af29-3f07-b936-d2599e0dae05 | -2.82963 | -49.22645 | 2024-10-31 04:49:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d628565d-1ec8-3bdf-afd1-b947e8e803fa | -2.82902 | -49.23035 | 2024-10-31 04:49:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| aeb4ce6c-d8e5-36ca-b05d-9d9b031b2f11 | -2.82702 | -49.22552 | 2024-10-31 04:49:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6960aad1-0d50-36ad-afb8-2c907521d33e | -2.82643 | -49.22944 | 2024-10-31 04:49:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 68802d29-2b38-3139-a51d-de850e2edf03 | -2.82612 | -49.2259 | 2024-10-31 04:49:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 665fa34b-8e1c-3160-8c58-36326de01da7 | -2.82551 | -49.22982 | 2024-10-31 04:49:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| f376e349-9615-3028-85f1-f0d24d2cce1b | -2.822 | -49.22929 | 2024-10-31 04:49:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README36.md)
