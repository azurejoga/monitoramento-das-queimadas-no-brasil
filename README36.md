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

## Dados Diários - Página 36

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9825ff36-2356-34a9-97f6-9915b7060fa2 | -2.90746 | -48.29856 | 2025-08-19 04:51:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 76f1ce9e-b0bb-3c4c-a258-a4c0bf03e69b | -4.59208 | -43.3181 | 2025-08-19 04:51:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ea69a056-98aa-3e1d-9f35-0a2e361d4245 | -5.54829 | -49.07297 | 2025-08-19 04:51:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 545a3734-6ed9-3a78-b212-450c7aefee4e | -6.95289 | -43.59936 | 2025-08-19 04:51:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fccf9c7b-0fb4-3164-a407-3c7d4d7963ee | -4.02311 | -48.06309 | 2025-08-19 04:51:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a2af26d0-78ab-3c01-b79d-c1d68c28da80 | -4.60363 | -43.31002 | 2025-08-19 04:51:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| bb95d97e-9519-3e4a-976f-0a68f595d4b8 | -5.64758 | -43.40744 | 2025-08-19 04:51:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8add5649-0584-3746-8dd6-6dac9fa0a966 | -3.66446 | -50.95244 | 2025-08-19 04:51:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 31e4d24e-f17d-3447-8970-2312ca8eca70 | -5.65736 | -43.40491 | 2025-08-19 04:51:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9d77abd1-d02b-39ba-b795-818a55050750 | -6.74483 | -41.53396 | 2025-08-19 04:51:00 | NPP-375D | SÃO JOSÉ DO PIAUÍ | PIAUÍ | Brasil | 2210201 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 05a0c470-8a1b-3fb6-ab37-d69645af6164 | -2.98582 | -49.30622 | 2025-08-19 04:51:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2da20d26-de8f-3d2d-9480-9b21a381d3a1 | -5.87227 | -48.11544 | 2025-08-19 04:51:00 | NPP-375D | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 061bee08-3cd3-3ea3-94b9-b4f5747a2ceb | -2.90368 | -48.24973 | 2025-08-19 04:51:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9fa0d228-ed5b-3c8f-b49f-031c82152c38 | -6.95472 | -43.58626 | 2025-08-19 04:51:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cc6e45c9-4224-32dc-a7a3-af6a08fe7b97 | -5.97433 | -44.11539 | 2025-08-19 04:51:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8eb95d21-6cd6-3c97-a7c5-16bc077e6a8b | -5.78418 | -43.60519 | 2025-08-19 04:51:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ac9259fd-f0ed-3aa4-ab7f-d4d15b762fe9 | -4.96018 | -47.59823 | 2025-08-19 04:51:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d9025338-be67-3508-af97-af9bd14ba753 | -6.9321 | -43.59312 | 2025-08-19 04:51:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 3b6ba731-b760-3809-ac75-3e028a4bb945 | -6.68115 | -43.67189 | 2025-08-19 04:51:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 85d73fc5-61b8-30ac-919b-472dded1e8e7 | -6.45645 | -44.56408 | 2025-08-19 04:51:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 96b81c79-fba4-3c23-9c75-9b3b2da4c65f | -5.87469 | -48.12549 | 2025-08-19 04:51:00 | NPP-375D | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 480b705a-1c41-3db5-b2f4-23233a752811 | -6.06605 | -44.12317 | 2025-08-19 04:51:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8a66f95c-5ade-31b0-a281-6da69df9491e | -5.64241 | -43.39628 | 2025-08-19 04:51:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bee35b26-7c83-3406-bde3-2b3aa0336b72 | -6.92726 | -43.58901 | 2025-08-19 04:51:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 65f349c3-40d8-3ecd-bd48-4ddffb381e56 | -6.93517 | -43.6101 | 2025-08-19 04:51:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 47243b1f-fb83-357f-9ad8-0d65874359ff | -5.79037 | -43.88873 | 2025-08-19 04:51:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 08405ea1-73f5-3719-8e47-1847fc7377b2 | -6.9268 | -43.59234 | 2025-08-19 04:51:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 1b8515b6-1520-309d-bd42-2b764d1c89d2 | -3.9928 | -42.52215 | 2025-08-19 04:51:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 2d168440-b4cf-3b28-9382-dd2a20106427 | -6.5116 | -45.49978 | 2025-08-19 04:51:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| df76aabf-b05e-3343-b39d-daa414628f5f | -6.54768 | -43.01075 | 2025-08-19 04:51:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 59e16aa0-5f61-3bf9-a535-59fc2b3b9f16 | -6.87631 | -45.20969 | 2025-08-19 04:51:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| eda9ea34-e4ec-35f1-9bb7-b86faa961c51 | -4.43247 | -47.75679 | 2025-08-19 04:51:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 65ef0f7d-a698-3dcb-97a0-d7e047936b47 | -5.55252 | -49.07269 | 2025-08-19 04:51:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b18a5da2-e713-366c-bc31-ab60cfe948a2 | -6.9391 | -43.62069 | 2025-08-19 04:51:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 875af4ca-a2cf-3e63-9cc0-7d10cea0c0c7 | -4.59228 | -43.31474 | 2025-08-19 04:51:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6e576879-0bc1-305c-85cb-7636ba07eb99 | -6.67646 | -43.67456 | 2025-08-19 04:51:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9245ad1f-eb30-3742-b282-cf71c0a0ad1c | -4.91317 | -43.24118 | 2025-08-19 04:51:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e5e2763e-2d3c-3fe8-b158-74ccd863b918 | -5.78847 | -43.6124 | 2025-08-19 04:51:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 3b2f1eec-3d42-3d03-9efa-cede91c77421 | -2.84685 | -48.7864 | 2025-08-19 04:51:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2af40d39-dedc-3897-b50c-ba04554c5190 | -5.87611 | -48.11606 | 2025-08-19 04:51:00 | NPP-375D | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 1b7d0103-9619-353d-90f8-202bcf6b0f43 | -3.98239 | -42.51699 | 2025-08-19 04:51:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| f8301720-5aa4-3abf-9942-610191aa9eeb | -5.9806 | -44.10745 | 2025-08-19 04:51:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f17b2ce0-2b78-3455-81ee-8b312f2c6635 | -5.87853 | -48.12612 | 2025-08-19 04:51:00 | NPP-375D | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 07e3f45f-ce18-3854-be43-36ae183ba1bd | -5.98183 | -44.09864 | 2025-08-19 04:51:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 38a96bac-8b1f-3e8e-9413-d848946694ad | -3.24771 | -43.26596 | 2025-08-19 04:51:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 299a3482-d87d-3b49-8f44-762352306216 | -5.78801 | -43.61558 | 2025-08-19 04:51:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 15.3 |
| c1ab162f-b94c-3843-bcb9-1c4eca4167b2 | -4.30943 | -48.10504 | 2025-08-19 04:51:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e0bac08e-dff6-336a-90cb-aafd26d2db4e | -6.9453 | -43.61504 | 2025-08-19 04:51:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ddd2b16e-f12a-3c64-941d-922024f87cfc | -6.95426 | -43.58957 | 2025-08-19 04:51:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 53b3f06b-b1be-35ef-acf8-ac1f9140493b | -7.00919 | -44.27738 | 2025-08-19 04:51:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c59f236a-1947-345a-9e35-53d347b6e734 | -3.4855 | -48.43991 | 2025-08-19 04:51:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d280e9f3-3b80-3066-a2cf-164d9bd8fe7d | -4.00122 | -43.26518 | 2025-08-19 04:51:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5d766b28-317e-3e4f-9e6e-ad5110bc8f91 | -3.05881 | -52.48018 | 2025-08-19 04:51:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 816eca32-de51-3fc6-a691-73df8a9b82ad | -4.15819 | -50.22607 | 2025-08-19 04:51:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 30291d6f-e203-3f7a-9331-34d2a05c04f0 | -5.57208 | -44.08332 | 2025-08-19 04:51:00 | NPP-375D | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 20622200-130b-3d9b-b909-f075538c73a9 | -3.03803 | -49.43505 | 2025-08-19 04:51:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3f58c36b-1470-3339-9112-78e8b6b17df7 | -4.59303 | -43.31181 | 2025-08-19 04:51:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9cbd4f35-2291-3912-8fda-a968e4487ddb | -4.91749 | -43.24833 | 2025-08-19 04:51:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e5c0a8e7-41eb-3482-895f-cb765a570e6c | -4.14941 | -46.45218 | 2025-08-19 04:51:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 58e2eed9-e42b-3a93-bee6-9b953c8f2ebe | -6.93956 | -43.61741 | 2025-08-19 04:51:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9efe4b64-c2cc-3169-b439-d7e922d65115 | -6.75002 | -41.53802 | 2025-08-19 04:51:00 | NPP-375D | SÃO JOSÉ DO PIAUÍ | PIAUÍ | Brasil | 2210201 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 491b55b8-0e3a-3ac3-8fc6-03ad452e8cea | -6.55244 | -43.9875 | 2025-08-19 04:51:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| c2507689-da35-337b-976a-a11cbb2172b9 | -4.91786 | -43.24174 | 2025-08-19 04:51:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 5b962549-ced5-348a-bcd6-9ad464409ba1 | -6.95105 | -43.61256 | 2025-08-19 04:51:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 27cc7301-01dd-3f99-8df8-4f2fc15e6307 | -4.82039 | -48.52431 | 2025-08-19 04:51:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e5d86208-baad-3c67-8f2c-51dc758238f3 | -5.65428 | -43.38846 | 2025-08-19 04:51:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8f0305ef-5aff-3996-864d-aba533984bab | -6.61426 | -43.88512 | 2025-08-19 04:51:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| cf4224a7-1d03-386a-a949-7c9df3527438 | -3.97198 | -42.51175 | 2025-08-19 04:51:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 2ab04106-486d-3828-81dd-b5877bbc94b7 | -6.94438 | -43.62159 | 2025-08-19 04:51:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6e1b0398-d5e0-3a99-8597-be18f7b314ba | -6.95911 | -43.59365 | 2025-08-19 04:51:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 3271ac59-4846-3b72-9488-204b95ca0a98 | -5.64371 | -43.39717 | 2025-08-19 04:51:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5334f4c2-f276-353b-99ef-9f90bbb48baf | -5.66093 | -43.37949 | 2025-08-19 04:51:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 739c0119-2bab-367d-8d24-f7546a335f7b | -4.14882 | -46.45612 | 2025-08-19 04:51:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ba7ecbd5-512b-3e6e-abd5-6763f304d55e | -5.97732 | -44.13087 | 2025-08-19 04:51:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e95db167-23c2-3675-9649-673e236c236c | -6.74363 | -41.54305 | 2025-08-19 04:51:00 | NPP-375D | SÃO JOSÉ DO PIAUÍ | PIAUÍ | Brasil | 2210201 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 443e1be7-55a8-3d2d-b458-db8fddf9d184 | -6.5176 | -45.4911 | 2025-08-19 04:51:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f1b437d0-9a81-34ea-b1c9-c64de1e4ae24 | -5.99205 | -44.13593 | 2025-08-19 04:51:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b49bbf90-da11-3745-8a80-02a41eb0a9c7 | -4.02242 | -48.06762 | 2025-08-19 04:51:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 876273be-7799-3393-92ad-81ce040d6f76 | -4.14463 | -46.45556 | 2025-08-19 04:51:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3557878c-fc2d-3ca9-8f90-1170ff019fb5 | -5.98156 | -44.13734 | 2025-08-19 04:51:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4b42f45c-e3b8-3e07-8c0e-f76cca83a161 | -6.95957 | -43.59035 | 2025-08-19 04:51:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 59085122-7c22-3ddd-a74c-295f97635d9c | -6.06451 | -44.1263 | 2025-08-19 04:51:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 05aa3986-cb2b-36d7-a593-7fbb92a2432a | -4.54514 | -46.68646 | 2025-08-19 04:51:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 5f35e77c-6373-39af-8d21-7bd96144be09 | -6.74334 | -41.54166 | 2025-08-19 04:51:00 | NPP-375D | SÃO JOSÉ DO PIAUÍ | PIAUÍ | Brasil | 2210201 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 0f24b974-3c61-35ca-b57d-02ddab4ad2a9 | -3.2515 | -43.27576 | 2025-08-19 04:51:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1795b68e-83fc-3bf5-bcd0-8ff2b65b255f | -5.87541 | -48.12075 | 2025-08-19 04:51:00 | NPP-375D | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e421ba3f-8a1c-3d98-924e-bb742e633b74 | -5.55257 | -49.06934 | 2025-08-19 04:51:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9a999aa2-a7e1-36e0-a470-a470f20ed7f9 | -5.65038 | -43.38847 | 2025-08-19 04:51:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e4017c84-01f1-35da-aaaa-5ce39ce72a75 | -6.676 | -43.67773 | 2025-08-19 04:51:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d8b91a52-b7e0-36ee-b1a5-b2d3da9b1edb | -3.48042 | -47.68379 | 2025-08-19 04:51:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2c482bd6-3cfe-337d-94f7-3061932f4935 | -6.9582 | -43.60012 | 2025-08-19 04:51:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 625ac40b-96a6-3146-aebe-dbf8182fac7e | -3.48115 | -47.67909 | 2025-08-19 04:51:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 38d4db6a-27e3-32d8-8b7b-f52991cb09a4 | -5.65565 | -43.37864 | 2025-08-19 04:51:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 556bc3b5-8ae2-31cb-a708-9f4f12ff78d6 | -5.98018 | -44.11044 | 2025-08-19 04:51:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 49616176-fa2d-38c6-af83-f0ebce17b8f9 | -3.98849 | -47.88651 | 2025-08-19 04:51:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 84ac9bdc-1653-3770-8206-d2440c28f343 | -3.98467 | -47.88599 | 2025-08-19 04:51:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 37ca42a8-f91c-3a32-b1be-ad3c7e2ff848 | -3.82739 | -47.75043 | 2025-08-19 04:51:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6df81d0b-b5ba-393a-95f8-6d3b7e8892d5 | -5.98102 | -44.10447 | 2025-08-19 04:51:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6d5266f5-4e42-367e-8af6-2e7f8a46688e | -3.46895 | -47.68194 | 2025-08-19 04:51:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 40d2f788-df22-3f3b-a2a0-9f1212b2ea84 | -5.65182 | -43.37866 | 2025-08-19 04:51:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README37.md)
