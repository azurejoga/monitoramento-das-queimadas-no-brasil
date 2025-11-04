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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f2ebdec6-e8b7-3c93-bd25-03cf2de082c0 | -5.36468 | -44.74648 | 2025-11-04 00:34:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 94b83e8c-4653-3e07-a305-a1472fa0b6c3 | -5.4253 | -50.04881 | 2025-11-04 00:34:00 | TERRA_M-M | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 8f0d1be1-0235-3a74-9e6b-a5cd81295a94 | -3.69963 | -49.56666 | 2025-11-04 00:34:00 | TERRA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 27.1 |
| 2bc6039e-2e5b-3638-b5b2-15274d98c61f | -3.90697 | -44.40687 | 2025-11-04 00:34:00 | TERRA_M-M | SÃO MATEUS DO MARANHÃO | MARANHÃO | Brasil | 2111508 | 21 | 33 | nan | nan | nan | Cerrado | 21.3 |
| 76f1038f-21ff-3458-9ea2-934b74579f99 | -4.48764 | -45.88422 | 2025-11-04 00:34:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 8.8 |
| d26330a6-233c-3ce0-bca4-1b9494463d8b | -7.54661 | -45.85097 | 2025-11-04 00:34:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| dd05b22b-512a-3e0a-bc27-183c486c3aa6 | -5.83614 | -44.66127 | 2025-11-04 00:34:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 24.3 |
| 0bfa3222-8fae-340a-863d-c8b226be517d | -4.02584 | -45.47484 | 2025-11-04 00:34:00 | TERRA_M-M | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 45.5 |
| 60467f8f-25a9-39e8-956e-843518c3cf0b | -3.77681 | -52.32852 | 2025-11-04 00:34:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 24.4 |
| 93f55e6a-6d3b-3842-8e04-abcc49616ca5 | -3.908 | -44.40016 | 2025-11-04 00:34:00 | TERRA_M-M | SÃO MATEUS DO MARANHÃO | MARANHÃO | Brasil | 2111508 | 21 | 33 | nan | nan | nan | Cerrado | 29.1 |
| 805b123e-c8c0-3925-bf44-84e98524095e | -4.92069 | -47.33625 | 2025-11-04 00:34:00 | TERRA_M-M | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 614a8672-5016-3797-84d4-1ac5ec7055ac | -2.99075 | -44.966 | 2025-11-04 00:34:00 | TERRA_M-M | OLINDA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2107456 | 21 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 9eca31c6-f7a3-3283-a8d5-cc51ffdd14e0 | -5.89679 | -42.92597 | 2025-11-04 00:34:00 | TERRA_M-M | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 28.1 |
| 19bc7410-b10d-35a7-be7f-3ade71c88c58 | -3.59018 | -50.16912 | 2025-11-04 00:34:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c636c58e-ead2-379e-9bb1-ab8cd8dca200 | -3.50329 | -50.46606 | 2025-11-04 00:34:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| eeb16d61-d60c-36bb-af5e-eb9039f2d622 | -3.55251 | -49.43535 | 2025-11-04 00:34:00 | TERRA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 18.3 |
| f9472504-1d8c-3eef-94cf-2973fcb8172a | -6.60788 | -43.60662 | 2025-11-04 00:34:00 | TERRA_M-M | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 17.8 |
| a8b773a0-161c-3aaf-b6d8-0e3558901a2a | -3.41342 | -44.43279 | 2025-11-04 00:34:00 | TERRA_M-M | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 39.7 |
| 35c3052e-46bf-37c0-889a-8e1d6393de8e | -4.3822 | -46.27911 | 2025-11-04 00:34:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 9f3e11fd-4f70-3f4e-863a-99bb4b36d72f | -4.86971 | -47.55214 | 2025-11-04 00:34:00 | TERRA_M-M | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 16.0 |
| 36f6e8bb-2187-3635-9546-f9a985fbd867 | -4.03507 | -45.45749 | 2025-11-04 00:34:00 | TERRA_M-M | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 11.9 |
| f9434dbb-a9af-39ba-b792-569fa9ff933d | -5.28304 | -48.44178 | 2025-11-04 00:34:00 | TERRA_M-M | ESPERANTINA | TOCANTINS | Brasil | 1707405 | 17 | 33 | nan | nan | nan | Amazônia | 16.4 |
| 065d566d-7e85-3795-b9ff-10ca58d64bd8 | -3.19574 | -44.37844 | 2025-11-04 00:34:00 | TERRA_M-M | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 19.5 |
| 03bd44de-a8ae-37f6-8d5c-544f5265cf13 | -5.6216 | -45.98845 | 2025-11-04 00:34:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 29.7 |
| ff82523b-5ae4-3377-a280-8a17d8bed591 | -3.98407 | -47.08737 | 2025-11-04 00:34:00 | TERRA_M-M | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 36.4 |
| 9d262daf-c95b-315e-b23f-b4f3e547f765 | -6.42286 | -43.0889 | 2025-11-04 00:34:00 | TERRA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 22.2 |
| ca0c59b6-bb38-31f7-a0ef-d56ba3bb778f | -4.4315 | -49.85343 | 2025-11-04 00:34:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 067de79e-042b-3b8e-aaba-c485f958c81c | -3.48609 | -50.01789 | 2025-11-04 00:34:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| fb2df545-95ad-3445-8b01-1a9b34941f08 | -5.76455 | -49.24243 | 2025-11-04 00:34:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| a89b8b13-8065-36a8-a979-3a377f01832b | -4.9653 | -44.90503 | 2025-11-04 00:34:00 | TERRA_M-M | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 38.6 |
| 47bfc891-0876-39ee-86da-cf059b61783f | -4.01198 | -45.29914 | 2025-11-04 00:34:00 | TERRA_M-M | SATUBINHA | MARANHÃO | Brasil | 2111722 | 21 | 33 | nan | nan | nan | Amazônia | 11.1 |
| a8d69167-2700-3fc6-8634-dce56aa952e5 | -4.88882 | -45.86629 | 2025-11-04 00:34:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 23.7 |
| d4bf76f2-d2a9-353e-895a-1a7cf452eacc | -5.89318 | -42.90314 | 2025-11-04 00:34:00 | TERRA_M-M | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 23.5 |
| 5e397f36-1559-3d8f-b197-96f6a1224bd1 | -3.85044 | -49.98735 | 2025-11-04 00:34:00 | TERRA_M-M | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 7539584e-89a2-35f1-9d4e-4ae2b0e70c46 | -5.88686 | -42.91071 | 2025-11-04 00:34:00 | TERRA_M-M | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 22.8 |
| 0aab483b-5708-3408-9600-c74420b3a67f | -5.90055 | -42.9085 | 2025-11-04 00:34:00 | TERRA_M-M | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 16.1 |
| 392d9f05-1a77-3321-870e-356d675daa59 | -3.53624 | -49.45327 | 2025-11-04 00:34:00 | TERRA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 8242fa73-4d1e-38df-a321-cf5d175fe6af | -6.84919 | -46.30815 | 2025-11-04 00:34:00 | TERRA_M-M | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 11.7 |
| f0210cf6-a2bb-39a0-ac6a-718838d12621 | -4.38553 | -46.27204 | 2025-11-04 00:34:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 659dcf59-2178-3231-88d3-64b83e38b73e | -5.06867 | -45.91237 | 2025-11-04 00:34:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 26.9 |
| 5ea5a1b7-4176-3f95-b681-7e78d66c14ec | -5.24489 | -44.22797 | 2025-11-04 00:34:00 | TERRA_M-M | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 6a412120-d308-307a-b78c-ed14ee438d8a | -4.60905 | -45.76583 | 2025-11-04 00:34:00 | TERRA_M-M | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 2d1fa182-b1f5-3df3-93c4-d8894d45ede8 | -3.57302 | -50.64449 | 2025-11-04 00:34:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 46.0 |
| 9943c5b7-8211-3fdd-bc22-51de9110612b | -5.76329 | -49.23338 | 2025-11-04 00:34:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| cdd480cf-b834-378f-8b37-a0be71afda0b | -4.95349 | -44.90712 | 2025-11-04 00:34:00 | TERRA_M-M | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 62.1 |
| 1ec6ebd0-ca85-3044-9b76-51e786a28001 | -2.87658 | -45.32323 | 2025-11-04 00:34:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 13.0 |
| b12bad2b-bb02-3c6a-af0c-b7b84039c5bb | -3.50207 | -50.45727 | 2025-11-04 00:34:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 094c16d6-d553-34b4-a9be-f1d3e0446402 | -4.95096 | -44.8901 | 2025-11-04 00:34:00 | TERRA_M-M | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 10.7 |
| a17901f0-b2c1-3bdd-ac7a-617ae58b484f | -3.92605 | -47.68944 | 2025-11-04 00:34:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 75.3 |
| 9630e5e9-1a34-3f15-ba27-9d7ee58c30d2 | -4.47804 | -43.24349 | 2025-11-04 00:34:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 24.2 |
| 78db0b15-d333-3f3e-a1a1-b684a1de46fa | -4.1861 | -45.78363 | 2025-11-04 00:34:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 45.9 |
| 3ece8927-b0c7-32af-bd87-e69eff344756 | -5.61957 | -45.97503 | 2025-11-04 00:34:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 277.8 |
| 5bd554a8-7070-3113-9828-d18531ea9443 | -4.43275 | -49.86232 | 2025-11-04 00:34:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b4ac2bff-9672-34b0-9d5d-100f3e7ed165 | -3.92757 | -47.70031 | 2025-11-04 00:34:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 97.0 |
| 0d23d5fb-fc49-3f44-8f49-2799bf6eabed | -4.62528 | -49.46627 | 2025-11-04 00:34:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 5ade262b-c01f-3a88-8dca-8f72a4e2b002 | -4.67131 | -50.72204 | 2025-11-04 00:34:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 0c8457d5-8ac5-3958-93f9-fec704e2ec4c | -4.62653 | -49.4753 | 2025-11-04 00:34:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| ab71da33-b26c-3a8d-8d48-ced11582a8a5 | -3.91628 | -47.69086 | 2025-11-04 00:34:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 210.0 |
| ae20c2a8-8d51-34c1-bac8-0a3f7261c458 | -3.50451 | -50.47485 | 2025-11-04 00:34:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 48200ce4-fa15-3e24-ad38-b5bd6f9703ad | -5.06672 | -45.91922 | 2025-11-04 00:34:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 16.8 |
| e069b746-6b95-34bf-a403-2bab3861e750 | -5.2886 | -44.60657 | 2025-11-04 00:34:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 11.2 |
| a44c03ae-bb9e-3ceb-bbff-199ce3f41002 | -7.85262 | -44.21487 | 2025-11-04 00:34:00 | TERRA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 5222cb41-eee7-372d-83ae-ec537e9d996d | -2.87411 | -45.30648 | 2025-11-04 00:34:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 143.8 |
| 62fa17fa-3cc9-3c80-94a5-7c60b07497c0 | -4.183 | -49.98826 | 2025-11-04 00:34:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 2937abf7-9ad9-3a1c-82c0-a5655a84a7ee | -5.00121 | -50.7838 | 2025-11-04 00:34:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 95e059d7-6eb4-33d2-88bd-cbc45a3da9ef | -5.26088 | -48.48436 | 2025-11-04 00:34:00 | TERRA_M-M | ESPERANTINA | TOCANTINS | Brasil | 1707405 | 17 | 33 | nan | nan | nan | Amazônia | 45.0 |
| d6be497d-791d-3eec-9dfe-9a2b228c6fa9 | -4.02355 | -45.45926 | 2025-11-04 00:34:00 | TERRA_M-M | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 83.9 |
| 1cec4af0-549e-3cfc-8d4f-3ff9eb26466b | -6.41943 | -43.06673 | 2025-11-04 00:34:00 | TERRA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 132.8 |
| c14e1c34-acff-3578-ab71-8bbe02a41a28 | -5.61445 | -45.96843 | 2025-11-04 00:34:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 127.0 |
| 499d63af-bb94-3edf-b145-7fcde67da53d | -5.2595 | -48.47472 | 2025-11-04 00:34:00 | TERRA_M-M | ESPERANTINA | TOCANTINS | Brasil | 1707405 | 17 | 33 | nan | nan | nan | Amazônia | 19.2 |
| f7d0ef73-b3eb-3b67-a328-605ae474b7f9 | -6.18484 | -46.73714 | 2025-11-04 00:34:00 | TERRA_M-M | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 8075773d-4ba4-3be1-9a6e-4225d9c6094c | -4.87945 | -47.55077 | 2025-11-04 00:34:00 | TERRA_M-M | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 17.3 |
| d62e74f2-1bbd-3b56-9b6d-5b86a8df6b9e | -4.60697 | -45.75174 | 2025-11-04 00:34:00 | TERRA_M-M | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 31.9 |
| b15ab379-f810-320e-a68f-d1cfe9f640e1 | -4.1882 | -45.79818 | 2025-11-04 00:34:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 11.6 |
| c13a3ef4-75cc-3b53-b997-75743ff0ed55 | -6.01455 | -51.52062 | 2025-11-04 00:34:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| d9f6532f-f84a-31fa-ae91-8b3fbefd2f3b | -4.91222 | -45.08814 | 2025-11-04 00:34:00 | TERRA_M-M | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 37103f41-2906-37c8-b41f-ac124de44b97 | -4.1973 | -45.78198 | 2025-11-04 00:34:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 3ec1d6cf-dfd2-30f7-9a6e-541b4e1b7405 | -4.95056 | -48.56387 | 2025-11-04 00:34:00 | TERRA_M-M | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 87f8fc0b-79ef-3f48-a090-52327ca6240f | -4.91908 | -47.32519 | 2025-11-04 00:34:00 | TERRA_M-M | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 32.8 |
| 9fb1391a-099f-3c7c-a8e7-98f0e98f712b | -5.48839 | -47.08998 | 2025-11-04 00:34:00 | TERRA_M-M | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 36abb41f-db98-30bc-ab69-83eb1c511dfc | -3.49132 | -50.31509 | 2025-11-04 00:34:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| bf19a0de-bba8-3b59-8b10-c35fe326823a | -3.49697 | -50.16112 | 2025-11-04 00:34:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 3d8d24f4-9c78-37f9-8004-5565d7419534 | -3.89806 | -49.99274 | 2025-11-04 00:34:00 | TERRA_M-M | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| d2621c8a-8eba-3dd6-bb7c-e60027092854 | -4.47446 | -43.22041 | 2025-11-04 00:34:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 21.8 |
| ac083571-18a2-36d3-929d-f0b9cf2bc485 | -6.84745 | -46.29617 | 2025-11-04 00:34:00 | TERRA_M-M | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 40.7 |
| 94c50cba-a826-3c00-a0cf-9cbd625c8f84 | -4.03734 | -45.4731 | 2025-11-04 00:34:00 | TERRA_M-M | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 4587e407-0d8c-351f-80a5-c279008ff278 | -4.11044 | -45.50313 | 2025-11-04 00:34:00 | TERRA_M-M | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 56.5 |
| f0509c0f-698d-3048-aaa5-eb74778a0ad1 | -3.98237 | -47.07551 | 2025-11-04 00:34:00 | TERRA_M-M | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 18.8 |
| d418bfc6-b010-3454-9443-1a647a93b7df | -3.49799 | -45.63708 | 2025-11-04 00:34:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 22.6 |
| 5ae974eb-dc3b-3c57-b2ec-11b59e14097d | -5.61639 | -45.9819 | 2025-11-04 00:34:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 168.7 |
| 3822953b-4b01-375d-933f-ac71d1de0b67 | -6.40602 | -43.06879 | 2025-11-04 00:34:00 | TERRA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 117.5 |
| a4c26952-6c0a-3b96-b623-877f85cd04c5 | -4.02869 | -51.01402 | 2025-11-04 00:34:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 8469c40a-7bd3-3eeb-868a-785ef26892a8 | -4.01984 | -51.01529 | 2025-11-04 00:34:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| e31d6d2c-8cbd-386a-98f4-4bbd15154cb1 | -5.42652 | -50.05763 | 2025-11-04 00:34:00 | TERRA_M-M | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 1d2e94d2-683e-3e30-8442-ebf0e8d61791 | -6.61092 | -43.62654 | 2025-11-04 00:34:00 | TERRA_M-M | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 21.1 |
| 8983c6c5-e4db-3b30-9906-1ae5a87aaace | -4.87411 | -49.00496 | 2025-11-04 00:34:00 | TERRA_M-M | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 403706cf-ac38-3358-920c-b64cd19af8fd | -3.60589 | -50.62195 | 2025-11-04 00:34:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| ad4ca141-cb9e-3b74-a5fa-cfbc4870c29f | -4.66247 | -50.72328 | 2025-11-04 00:34:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 9802fe08-b738-3060-9046-2fb79925fea9 | -3.57181 | -50.6357 | 2025-11-04 00:34:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a3b2edcf-c969-31f4-925d-1b40c8d2d3a7 | -3.54351 | -49.43664 | 2025-11-04 00:34:00 | TERRA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 16.6 |


[Clique aqui para ver as próximas entradas](README3.md)
