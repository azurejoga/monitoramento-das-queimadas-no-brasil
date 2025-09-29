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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cf5354bd-0627-3270-9e87-b061307f662e | -5.02378 | -42.53994 | 2025-09-29 03:45:00 | NPP-375D | ALTOS | PIAUÍ | Brasil | 2200400 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 8ebae0fb-0cba-31d9-a974-8e4a103f300b | -5.18523 | -43.76269 | 2025-09-29 03:45:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| cf31afd9-c8db-3dd3-a19d-221987c9e276 | -4.97435 | -44.50325 | 2025-09-29 03:45:00 | NPP-375D | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| ae162552-3090-3794-bd24-8d4285128164 | -3.83277 | -40.32685 | 2025-09-29 03:45:00 | NPP-375D | FORQUILHA | CEARÁ | Brasil | 2304350 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| b0581fe1-3357-309f-a84c-8bae42741a9f | -5.1906 | -43.76112 | 2025-09-29 03:45:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| b4444cdd-aa32-34fd-9682-c8acfd02341b | -5.71997 | -42.84254 | 2025-09-29 03:45:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 75d6b001-4487-34ee-99ae-e1e36daf55de | -5.73156 | -42.83351 | 2025-09-29 03:45:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 11.2 |
| a5644cdf-0a9b-398a-afee-952cad11a70e | -5.71617 | -42.86459 | 2025-09-29 03:45:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 7841ea3b-9c75-32f4-961d-667a1ba8c87c | -5.15277 | -46.08246 | 2025-09-29 03:45:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2ad51e31-7931-3d5a-98c7-ec99144867f8 | -5.16245 | -45.01567 | 2025-09-29 03:45:00 | NPP-375D | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 870ea6ad-9dcb-397a-8639-f22aefde6b53 | -5.09101 | -45.48711 | 2025-09-29 03:45:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 994de85d-68f9-3fac-a67b-f6dad73c7a1c | -5.08836 | -43.85364 | 2025-09-29 03:45:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b7541a3f-8f04-3097-a7f9-0ea97aceb2ad | -5.19005 | -43.76428 | 2025-09-29 03:45:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 21.0 |
| 95826def-6472-383f-8720-f34289c12ad1 | -5.1683 | -41.26048 | 2025-09-29 03:45:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 795a491c-1270-342a-8f5f-cf3a35976d9a | -5.72667 | -42.83278 | 2025-09-29 03:45:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 40521ab5-0c25-31a4-8bd6-00dfcec55d28 | -5.1536 | -46.07776 | 2025-09-29 03:45:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7b82a256-cac2-38ce-a4a2-1ad9961e6268 | -4.70645 | -41.98141 | 2025-09-29 03:45:00 | NPP-375D | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 19.5 |
| c0e760c9-61a2-3b24-971d-44e7c1a51ae9 | -5.74224 | -42.82977 | 2025-09-29 03:45:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 7.6 |
| e7f76426-ce9f-38d1-89eb-b82107d4ff81 | -4.39827 | -44.08252 | 2025-09-29 03:45:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 963b5bcc-21ee-36e6-82df-bbae998da7fa | -2.57577 | -48.40474 | 2025-09-29 03:45:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| cd2c6698-6bce-350e-8d34-7da9aa774a88 | -4.24691 | -46.94935 | 2025-09-29 03:45:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 8574ca46-0cbb-3044-a421-1e82e8c5a6e2 | -5.1957 | -43.76455 | 2025-09-29 03:45:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| f74b36ea-f81d-3b4b-9a5e-1e7d96403819 | -2.54964 | -45.16079 | 2025-09-29 03:45:00 | NPP-375D | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f96573ec-aaf7-384b-a871-252775669346 | -5.09306 | -43.85789 | 2025-09-29 03:45:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 676bba69-d698-3374-9a30-09e5003904ce | -5.24527 | -45.35731 | 2025-09-29 03:45:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 335928df-7d70-363e-9fdc-74dc714dfc5d | -2.5765 | -48.40265 | 2025-09-29 03:45:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| c12e64d7-5ec3-3f97-b427-d767ae008ffa | -2.87689 | -40.02763 | 2025-09-29 03:45:00 | NPP-375D | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 16.4 |
| c858f79d-873e-3ef7-be04-5270aa98b5cf | -2.58178 | -48.41339 | 2025-09-29 03:45:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| a603cba9-d96e-3427-aa2b-4a3f31835546 | -5.19045 | -43.76368 | 2025-09-29 03:45:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 045f1b18-1d24-3fe5-918d-f0ab2e97e901 | -4.2896 | -48.26831 | 2025-09-29 03:45:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e487a966-47f9-398a-9d49-7de0105c89e6 | -5.24006 | -45.3589 | 2025-09-29 03:45:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2ef41113-233b-30bb-af2e-3eac7c044fa8 | -5.17343 | -41.25692 | 2025-09-29 03:45:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 727fde85-3d3f-3d95-bc26-4fd1851af069 | -3.61292 | -42.76717 | 2025-09-29 03:45:00 | NPP-375D | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 76c5fcd2-74e3-38a0-9ea4-21afed07bd26 | -6.77368 | -34.98873 | 2025-09-29 03:45:00 | NPP-375D | MARCAÇÃO | PARAÍBA | Brasil | 2509057 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 9e44d5d6-ad35-3331-b6b5-5efd627e8fe3 | -4.54378 | -41.01436 | 2025-09-29 03:45:00 | NPP-375D | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 0d433c81-3f6e-3fed-9c8a-f22a154901eb | -4.40247 | -44.09044 | 2025-09-29 03:45:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 1e025d7a-c512-35c5-9298-8fa98881e6d7 | -5.02861 | -42.54081 | 2025-09-29 03:45:00 | NPP-375D | ALTOS | PIAUÍ | Brasil | 2200400 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 6dc426dd-b3de-3e4b-9c5a-033948d4f431 | -5.7389 | -42.67501 | 2025-09-29 03:45:00 | NPP-375D | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 3ecdf858-3035-3f72-bdaf-50837f3823e1 | -4.29661 | -48.26969 | 2025-09-29 03:45:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 687650ff-5d8d-37a1-a92f-b432a7a1c3dc | -4.28838 | -48.27525 | 2025-09-29 03:45:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 931bdbb0-d8d1-34c9-97d5-e82c0a877b5b | -6.22515 | -38.24519 | 2025-09-29 03:45:00 | NPP-375D | RAFAEL FERNANDES | RIO GRANDE DO NORTE | Brasil | 2410504 | 24 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 1d1e1955-ef23-3b57-8e0b-fc6bba94d4da | -5.17929 | -41.24887 | 2025-09-29 03:45:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| ffe06b3d-7f69-3763-8329-f56d023b2386 | -4.30596 | -48.09321 | 2025-09-29 03:45:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 720749a5-bbe1-37b1-b18c-ec8c35e8951f | -5.74148 | -42.86361 | 2025-09-29 03:45:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 8.4 |
| 14c10187-5e15-3440-b976-7eb307bb98d5 | -4.5748 | -38.92317 | 2025-09-29 03:45:00 | NPP-375D | ITAPIÚNA | CEARÁ | Brasil | 2306504 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| fb3c47f3-6232-34ac-9236-3bb6912ce399 | -4.40368 | -44.08348 | 2025-09-29 03:45:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| c6d421b9-25cc-3e21-ad07-4cfa96983dbd | -5.51107 | -42.20758 | 2025-09-29 03:45:00 | NPP-375D | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| a627b208-4234-3caa-93a8-c77df07bd511 | -4.97305 | -44.5106 | 2025-09-29 03:45:00 | NPP-375D | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e8a9b1bb-3782-3ce4-995c-757e118e3a61 | -5.38067 | -42.31111 | 2025-09-29 03:45:00 | NPP-375D | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 4770ce0e-702f-38ac-b790-403a5de4e8b5 | -3.09255 | -47.01857 | 2025-09-29 03:45:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| ba723d55-8c65-3aeb-8c8b-1bbb42dc2a2e | -5.13374 | -38.43364 | 2025-09-29 03:45:00 | NPP-375D | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| b429d5c6-10d5-3d14-9d8c-c2fd1b4b093c | -4.31227 | -48.08672 | 2025-09-29 03:45:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 1c855967-8d6b-36d5-b587-6de19b0ce6fd | -2.58377 | -48.40385 | 2025-09-29 03:45:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| febcff78-f933-32a8-bcfc-89679481cd67 | -4.31406 | -48.08801 | 2025-09-29 03:45:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 87e31934-26cb-3a39-9228-d28a0cc9e761 | -5.36451 | -42.84869 | 2025-09-29 03:45:00 | NPP-375D | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 012f13e4-a348-31b6-b741-9f88a6a6c0fd | -5.19529 | -43.76514 | 2025-09-29 03:45:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| c275ac2f-cb94-312f-bea1-498a93505d5b | -5.36681 | -42.84502 | 2025-09-29 03:45:00 | NPP-375D | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 8.4 |
| f2dededc-4b87-31f7-b738-118ec37ea0b3 | -5.70152 | -42.60539 | 2025-09-29 03:45:00 | NPP-375D | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| cbbdc93b-6cfb-32be-b5cc-224b4a8a25ca | -5.19116 | -43.75798 | 2025-09-29 03:45:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 176f08dc-9382-354e-b4f0-3afdeec5d1ef | -5.16811 | -45.01685 | 2025-09-29 03:45:00 | NPP-375D | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6ab1b1f7-6d63-3a3d-a479-ab76f0973f81 | -2.58248 | -48.41122 | 2025-09-29 03:45:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 20.6 |
| a667043b-3ce7-3085-a77c-6d1a9664d460 | -2.87752 | -40.02378 | 2025-09-29 03:45:00 | NPP-375D | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 16.4 |
| d3192a2d-338a-345e-8d4f-1627cf8bf758 | -4.40846 | -44.08813 | 2025-09-29 03:45:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 944d6eb8-cd00-3196-9e3d-a988b1baf057 | -5.13744 | -38.43423 | 2025-09-29 03:45:00 | NPP-375D | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| aa0d68a6-6e14-3f23-b1b7-16c8d9c80475 | -4.14425 | -40.01071 | 2025-09-29 03:45:00 | NPP-375D | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 2be9808e-3843-3cf7-89c0-0384f5698fc1 | -5.36542 | -42.84322 | 2025-09-29 03:45:00 | NPP-375D | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 75946d5c-1eb2-383b-8bf4-26a1fb28a7d6 | -2.57523 | -48.40989 | 2025-09-29 03:45:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 20.6 |
| 76d1b3d3-2f42-3264-850d-147edb32e75e | -4.97498 | -44.49968 | 2025-09-29 03:45:00 | NPP-375D | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| c6607c3b-cf4a-3998-85ed-0034d9ca67b6 | -5.70338 | -42.63095 | 2025-09-29 03:45:00 | NPP-375D | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| c5dddb6d-34fa-3808-b448-aff7f3ef487c | -5.7018 | -42.6319 | 2025-09-29 03:45:00 | NPP-375D | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 8f2fddc7-961d-33ff-9d5d-9e9d076c9963 | -5.19099 | -43.76051 | 2025-09-29 03:45:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 50e11b5f-aaf0-3ec0-b190-5992d37b2928 | -4.29367 | -48.26785 | 2025-09-29 03:45:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| bb87a234-9442-3961-82de-e6644098564d | -5.2459 | -45.35977 | 2025-09-29 03:45:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 1418a41d-5116-331d-9553-7b6421592355 | -5.68808 | -42.63362 | 2025-09-29 03:45:00 | NPP-375D | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 29081457-5c38-3cd1-a6c5-174282886ada | -5.17716 | -41.26182 | 2025-09-29 03:45:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 1d7ca825-287d-3ccb-bad9-ea631fef30da | -5.19623 | -43.76139 | 2025-09-29 03:45:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 78399021-8934-3b80-ba50-be9f6d1fe3b1 | -5.09366 | -43.85441 | 2025-09-29 03:45:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 22445991-9174-3cc0-9e90-a47321e7041e | -5.69462 | -42.62422 | 2025-09-29 03:45:00 | NPP-375D | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| fd8f50a6-4b0d-3e7d-8ad2-6ddcb848bac3 | -5.15572 | -35.63416 | 2025-09-29 03:45:00 | NPP-375D | TOUROS | RIO GRANDE DO NORTE | Brasil | 2414407 | 24 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 52692307-2005-368f-877e-88ddc4df25b4 | -5.71903 | -42.84801 | 2025-09-29 03:45:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 27.9 |
| 386cd1d1-7794-3112-b0a6-d192aa4337c8 | -5.21621 | -43.76894 | 2025-09-29 03:45:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 44bf07e0-978c-31a9-8492-38e2a92d83e0 | -4.1395 | -40.01376 | 2025-09-29 03:45:00 | NPP-375D | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| b6094162-4937-33eb-ac11-609651439ff1 | -5.70953 | -42.65337 | 2025-09-29 03:45:00 | NPP-375D | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 561518ec-f4f7-372f-81d0-e09ac86eaf8a | -3.10118 | -47.00817 | 2025-09-29 03:45:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 16.4 |
| 2d7c5130-c134-34b3-8ad5-4ffb35ec4947 | -3.09921 | -47.01967 | 2025-09-29 03:45:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 23.0 |
| 96d41b47-9f52-31e6-8b1c-371cc57e4e58 | -5.74314 | -42.8245 | 2025-09-29 03:45:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| c46b0192-d0fb-315a-ba82-7d30357e4f31 | -4.40308 | -44.08695 | 2025-09-29 03:45:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 30cfe40c-c1ce-3d24-953e-7fcfedc5a81a | -3.61794 | -42.76802 | 2025-09-29 03:45:00 | NPP-375D | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 624fd8cf-ea16-3947-bdf1-03da7d23d422 | -4.75482 | -38.47802 | 2025-09-29 03:45:00 | NPP-375D | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 7b964b0a-731b-322f-9b19-9e9352d59107 | -5.73403 | -42.67448 | 2025-09-29 03:45:00 | NPP-375D | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| e79a0709-175f-35a0-8e1c-5393d3721641 | -4.50652 | -40.72266 | 2025-09-29 03:45:00 | NPP-375D | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 3352b1bc-ddce-3396-b104-bec604aefe90 | -4.31108 | -48.09322 | 2025-09-29 03:45:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 6e5f58e2-e456-37a4-9c79-c2f44c58a542 | -2.58303 | -48.40598 | 2025-09-29 03:45:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| a613b418-8933-34f9-a5a7-1ada0465df25 | -4.71965 | -41.98877 | 2025-09-29 03:45:00 | NPP-375D | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| ab7e436d-62f1-3599-830f-17c415731c0e | -4.14012 | -40.01005 | 2025-09-29 03:45:00 | NPP-375D | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| b95ba2c0-1ee2-3f86-85d4-fe3dc9871643 | -2.57454 | -48.41196 | 2025-09-29 03:45:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| dbac7398-91f6-3007-8c64-3b1468e5eb03 | -4.71112 | -41.98224 | 2025-09-29 03:45:00 | NPP-375D | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 4decf19d-4d51-3e54-81ee-2753451d04b6 | -4.31291 | -48.09453 | 2025-09-29 03:45:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| d8970777-7b60-3941-8fd2-be39b00adeb2 | -5.72579 | -42.83791 | 2025-09-29 03:45:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 6.3 |
| e7d4daf3-ed1a-3046-bc90-f50feec65db0 | -4.39223 | -44.08513 | 2025-09-29 03:45:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README10.md)
