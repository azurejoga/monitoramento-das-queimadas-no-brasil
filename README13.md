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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 24575811-4355-303d-adcd-bfc6efa980bd | -4.2261 | -47.21352 | 2025-11-12 04:31:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| a6d3159f-6e88-3c9d-9c51-5850ba14fb94 | -2.83392 | -48.82846 | 2025-11-12 04:31:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8e35ce43-2f9f-390d-bcc5-9eb5b2d08756 | -4.95091 | -43.724 | 2025-11-12 04:31:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| f6d067fb-86cf-3286-b5b1-63deff2f2599 | -9.32972 | -47.83892 | 2025-11-12 04:31:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| b8413129-cd06-3fca-954e-99b02ffe5376 | -9.83529 | -44.98983 | 2025-11-12 04:31:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 3cf0a1a9-5779-3732-888b-28e40c63a77f | -4.09653 | -48.01666 | 2025-11-12 04:31:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| caba939c-8570-3f8a-91df-be1b9f63b0f4 | -5.01567 | -44.09013 | 2025-11-12 04:31:00 | NOAA-21 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6c6dce0f-3315-3349-9ff5-7c640b7cc808 | -3.96246 | -43.77569 | 2025-11-12 04:31:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f5eb7ae5-b3cf-377c-9c61-6754d3e13742 | -2.10246 | -53.36452 | 2025-11-12 04:31:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 188c240c-8d1d-3e69-b032-8aff64bd7a1c | -4.54854 | -50.26528 | 2025-11-12 04:31:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0a5dd11f-3b29-3d38-982c-e2d7321913ef | -3.75728 | -45.07964 | 2025-11-12 04:31:00 | NOAA-21 | PIO XII | MARANHÃO | Brasil | 2108702 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8744dad2-78d5-3513-82ef-5b2307bd0fd1 | -5.80058 | -40.80096 | 2025-11-12 04:31:00 | NOAA-21 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 603cbead-d15b-33cb-8882-df3b7e9db99b | -3.06364 | -51.51689 | 2025-11-12 04:31:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| aa51db53-612b-3ada-bc64-7be95971a428 | -3.49408 | -55.41751 | 2025-11-12 04:31:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1c27c550-135a-3418-ab7d-6ce2a1a614cf | -7.53263 | -41.5517 | 2025-11-12 04:31:00 | NOAA-21 | VERA MENDES | PIAUÍ | Brasil | 2211506 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| b92cd249-0ace-3f37-99fb-52fe619810da | -4.08547 | -48.04358 | 2025-11-12 04:31:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 04ad4c97-33e1-32ff-b7f5-03c90e49ff91 | -7.28119 | -41.5816 | 2025-11-12 04:31:00 | NOAA-21 | AROEIRAS DO ITAIM | PIAUÍ | Brasil | 2200954 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 706d8268-acba-3afc-99b4-0b73a02e01db | -4.93906 | -44.29284 | 2025-11-12 04:31:00 | NOAA-21 | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 44afaa8d-3144-3890-b001-b5bc3adf25aa | -3.08925 | -49.45165 | 2025-11-12 04:31:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 043836c6-55fc-3595-b9f9-79a84f56ca3a | -4.52039 | -44.97301 | 2025-11-12 04:31:00 | NOAA-21 | LAGO DO JUNCO | MARANHÃO | Brasil | 2105807 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 02f538e2-e020-3b74-9702-5d82f421e37b | -3.96311 | -43.77142 | 2025-11-12 04:31:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 916a2273-b365-3d3e-a829-3020848e810a | -5.62811 | -43.07981 | 2025-11-12 04:31:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 094c0c66-fb5d-3684-9d87-cdfdb74146ec | -6.22864 | -47.33183 | 2025-11-12 04:31:00 | NOAA-21 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d66b91bc-3fc2-322c-9bdf-afdd4d1e0fb4 | -4.10207 | -48.02467 | 2025-11-12 04:31:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 7dfeb032-388a-321f-b167-59cfa2cb05ff | -4.86962 | -49.58829 | 2025-11-12 04:31:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5e203f5c-a263-311b-a646-efc5b500b4f8 | -3.63951 | -50.58357 | 2025-11-12 04:31:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 6a684a8f-9a61-30fd-8561-246483d04a48 | -9.14561 | -50.01761 | 2025-11-12 04:31:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 30bee3bc-8d06-3f18-bc77-5c1aecd4dc69 | -2.19876 | -50.52054 | 2025-11-12 04:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6e1117af-022e-3c0c-88d5-5c6e5162c714 | -5.65595 | -46.70528 | 2025-11-12 04:31:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e98503a8-93cf-3171-8042-3312bb5fc0f4 | -4.24832 | -50.05484 | 2025-11-12 04:31:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| f78bf1dc-0c0f-3a02-8c02-2957912dd510 | -7.06691 | -43.58232 | 2025-11-12 04:31:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ff724b62-3900-3b8d-a3b8-4610cb151c8d | -3.1211 | -49.4764 | 2025-11-12 04:31:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5f552e59-92d1-33ce-b584-84f489055525 | -2.64333 | -49.19157 | 2025-11-12 04:31:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d78288b2-8b55-3bef-8601-aea3c25c03e3 | -5.60042 | -41.07412 | 2025-11-12 04:31:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 0ab10fc2-05a3-36a9-ae57-e3fa970b4cb8 | -4.00101 | -43.81654 | 2025-11-12 04:31:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ff337818-8599-3461-9185-d4b838e07e9e | -4.112 | -48.00479 | 2025-11-12 04:31:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f0781991-9b33-3e84-bb9f-49316a980554 | -2.63519 | -49.19814 | 2025-11-12 04:31:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 704b6007-2778-3cd6-876e-7bf3c8264aea | -4.51441 | -45.6277 | 2025-11-12 04:31:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7f9eb8a8-66e4-3062-9430-fc184b4131d0 | -4.9538 | -44.95774 | 2025-11-12 04:31:00 | NOAA-21 | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| eef303ea-e303-380b-a0b0-1f21b6248ed4 | -7.86039 | -45.22311 | 2025-11-12 04:31:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1817ab90-b9b4-311e-bc74-0f906df973ec | -3.81579 | -50.14651 | 2025-11-12 04:31:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9f453142-d508-3872-9cf0-8d42998af581 | -10.49714 | -44.93293 | 2025-11-12 04:31:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 01eb3d40-f489-345c-820f-2909faec15bb | -4.94264 | -44.29341 | 2025-11-12 04:31:00 | NOAA-21 | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e9e6afd5-1d2c-3b15-9b81-858e62944715 | -6.93272 | -43.49073 | 2025-11-12 04:31:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9632a99b-6a09-3fd0-bf2b-30a232f21516 | -9.89305 | -47.86728 | 2025-11-12 04:31:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8a125bc9-a7c5-30e5-83df-97858e9246e2 | -4.10649 | -48.0182 | 2025-11-12 04:31:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| fa64c544-b966-3f05-a834-e58e0630f284 | -4.11313 | -48.01923 | 2025-11-12 04:31:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 878c4958-b925-3bfe-87c9-5cdc6ca10d56 | -4.33794 | -50.81442 | 2025-11-12 04:31:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 63a2c1ac-c397-3dc8-bfc5-08e047083992 | -4.77779 | -46.44693 | 2025-11-12 04:31:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d5fa9b04-4761-30e0-b750-e85c9d245920 | -6.54525 | -43.0371 | 2025-11-12 04:31:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| df78575a-bd24-3ba1-b96e-882957cb6cc2 | -4.38867 | -47.24239 | 2025-11-12 04:31:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0f5102c7-342e-340d-9caa-1af1be1b2dff | -7.29717 | -45.06977 | 2025-11-12 04:31:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 571bc705-54e8-3f77-ae92-b4081fc19397 | -7.30888 | -45.28254 | 2025-11-12 04:31:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8d4b410f-fbd3-3a34-bded-7abd3d6f3d8e | -3.76996 | -48.92499 | 2025-11-12 04:31:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cc2677be-dff5-311c-90ec-b48fd3c1dcfb | -2.96159 | -44.5952 | 2025-11-12 04:31:00 | NOAA-21 | CAJAPIÓ | MARANHÃO | Brasil | 2102408 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 82580950-ea44-34dd-91a4-c46399c7a0c2 | -7.63366 | -40.88895 | 2025-11-12 04:31:00 | NOAA-21 | CARIDADE DO PIAUÍ | PIAUÍ | Brasil | 2202554 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| f92d69c8-c3a2-3de1-b26a-754290d2fba2 | -9.00728 | -44.82321 | 2025-11-12 04:31:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b25cc95f-a601-3e28-9500-9f85fc7a9552 | -4.78014 | -42.68336 | 2025-11-12 04:31:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c92bb518-d60c-3531-9eac-4f715803e934 | -7.78684 | -43.79194 | 2025-11-12 04:31:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| d35d16ec-cef1-3bc4-8346-1eabc6434d07 | -2.40206 | -49.39512 | 2025-11-12 04:31:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fafce3f8-d77e-36b9-8c85-1e49a1f8e8a3 | -4.09598 | -48.02013 | 2025-11-12 04:31:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1c58f47c-a345-395e-bb18-f57659f4a911 | -3.71547 | -45.82083 | 2025-11-12 04:31:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| d9c0e93f-732e-39ca-bb3c-03db51fba35b | -6.61295 | -42.07255 | 2025-11-12 04:31:00 | NOAA-21 | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 5add4935-f5b6-337c-930d-d142f20731a3 | -3.09274 | -49.45218 | 2025-11-12 04:31:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 21419977-eede-3bd1-a86f-c3fe2f0e4948 | -5.49096 | -39.17203 | 2025-11-12 04:31:00 | NOAA-21 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 5fc06911-4e7f-3b8a-bcba-f26d302acf30 | -4.11368 | -48.01574 | 2025-11-12 04:31:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 21697e26-a4a4-335b-b8f7-94e3bb42b962 | -4.1466 | -47.65551 | 2025-11-12 04:31:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d604573a-a503-37ca-836f-d4bf1ab4ed55 | -6.31627 | -43.81036 | 2025-11-12 04:31:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 20.5 |
| 9a662431-021f-348f-b5ef-07084f84b052 | -8.73775 | -48.31876 | 2025-11-12 04:31:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a2bd8e81-8723-34b3-a8ce-ec2c0ace34e5 | -5.75568 | -42.73351 | 2025-11-12 04:31:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 4c87e8c8-168f-3ada-a182-560e0c2b1a32 | -6.98702 | -41.28256 | 2025-11-12 04:31:00 | NOAA-21 | SANTO ANTÔNIO DE LISBOA | PIAUÍ | Brasil | 2209401 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| e1753265-8ba2-315d-b670-fd9248acaa90 | -3.9854 | -47.29502 | 2025-11-12 04:31:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 16.1 |
| 0c7c4e93-6566-3db8-bf58-4110507799ee | -4.50469 | -43.92875 | 2025-11-12 04:31:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 91909328-fdaa-3c73-ab14-1960418fa42e | -4.11036 | -48.01523 | 2025-11-12 04:31:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 9499fc37-7e5c-33d1-b680-44b704fc926f | -6.11149 | -41.54363 | 2025-11-12 04:31:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| ba00741f-1288-3255-a25f-ffd76acbc9d0 | -5.01788 | -48.36669 | 2025-11-12 04:31:00 | NOAA-21 | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 8498c210-a233-371f-8e4d-ecd47763a70a | -3.13139 | -45.24588 | 2025-11-12 04:31:00 | NOAA-21 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5796fb35-af8e-3e46-8588-6e58e5fa1d7f | -8.29498 | -45.95233 | 2025-11-12 04:31:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1eae401a-e418-314f-91b2-41ceac86687c | -9.67554 | -43.90711 | 2025-11-12 04:31:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 286f25f7-7fff-3c40-8a36-beac20f641ea | -3.11093 | -50.53328 | 2025-11-12 04:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| eba2126b-35eb-3b93-a04d-884bb5d0ee90 | -3.26193 | -50.03103 | 2025-11-12 04:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2ce75fd0-da1e-349e-a177-8e61e3efcf1c | -2.64261 | -49.21885 | 2025-11-12 04:31:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1878d11d-1879-329c-b13c-fab3437c0a99 | -4.35776 | -44.34838 | 2025-11-12 04:31:00 | NOAA-21 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a57f2d49-aed6-3af1-aad1-879fad927729 | -9.01094 | -44.82376 | 2025-11-12 04:31:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2d9d2c14-af56-3104-baeb-b1593682b442 | -5.8957 | -42.25586 | 2025-11-12 04:31:00 | NOAA-21 | SÃO MIGUEL DA BAIXA GRANDE | PIAUÍ | Brasil | 2210383 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 2e2d1ea8-f41c-31a3-894c-871164650fb5 | -2.79455 | -51.36177 | 2025-11-12 04:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 8d440ece-ce05-34d2-860b-7d0e4f62afe7 | -4.94045 | -44.29652 | 2025-11-12 04:31:00 | NOAA-21 | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 26a39ba6-6bb3-3ed3-b661-68b0eeaa27b0 | -3.88477 | -47.17737 | 2025-11-12 04:31:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 1e0a2d0d-88ec-3202-8f92-babe5f40b1ac | -4.95157 | -43.71957 | 2025-11-12 04:31:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| e6bb0d05-3024-386a-a6c1-e626fb08cc04 | -4.10923 | -48.0008 | 2025-11-12 04:31:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4e9fff2d-e43a-366d-95c1-2c05d3b316a1 | -5.10462 | -50.80384 | 2025-11-12 04:31:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 46480572-d0f7-3215-9f56-2d12e94f22b4 | -3.71157 | -45.82386 | 2025-11-12 04:31:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 835c6f89-5a10-3616-bc46-0b18e236f063 | -4.42641 | -50.18881 | 2025-11-12 04:31:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 62e14567-96ef-39ea-82c6-72993cdac4b5 | -4.95964 | -43.71631 | 2025-11-12 04:31:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f5548846-c054-3ad4-93c7-ca5598beb0d0 | -10.4965 | -44.93737 | 2025-11-12 04:31:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |
| ba8aee18-7f61-325c-80eb-d18ffca4c237 | -6.78335 | -42.84343 | 2025-11-12 04:31:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| b78267ba-d3ba-3e9d-ae0f-28aceb82c05a | -7.45384 | -44.75207 | 2025-11-12 04:31:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| f18039b9-21dd-31ad-b96d-6e5c94c26b0f | -2.83012 | -47.43719 | 2025-11-12 04:31:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c69be1fd-dbb9-375b-b2da-80c80f9e6b5a | -10.45551 | -44.96921 | 2025-11-12 04:31:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| c5cb8052-bada-3462-87c2-08560db82685 | -4.96267 | -43.72133 | 2025-11-12 04:31:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 20.4 |


[Clique aqui para ver as próximas entradas](README14.md)
