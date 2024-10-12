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

## Dados Diários - Página 67

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| de576577-b785-391f-9a16-2a3499c7145e | -5.06424 | -46.07037 | 2024-10-12 04:57:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| d254bb33-ab75-3679-8781-00e0b26b6aff | -5.06347 | -46.07577 | 2024-10-12 04:57:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 8.9 |
| f012748a-ec9e-3ede-9c96-4cfad76b1b63 | -7.51988 | -46.59004 | 2024-10-12 04:57:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0c69aff4-95df-3914-a038-0efdf7bdabc3 | -6.77342 | -46.07562 | 2024-10-12 04:57:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a4b8ebc3-e5ef-3414-a265-486c54408295 | -6.77304 | -46.07845 | 2024-10-12 04:57:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8dffc227-b52a-3650-80d4-205027b9bd68 | -6.4838 | -46.05967 | 2024-10-12 04:57:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f566706a-44da-3bff-ac31-d567312c4b42 | -9.31488 | -45.90628 | 2024-10-12 04:57:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 95874dcf-3138-386a-816b-2fe6281b3ebf | -9.31443 | -45.90968 | 2024-10-12 04:57:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| dc38e244-c9de-314c-8fda-94b750e87a64 | -8.92148 | -47.0554 | 2024-10-12 04:57:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fd660e77-44ff-31b4-80c7-cbab378ddc3d | -2.7414 | -46.78251 | 2024-10-12 04:57:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b7c0bb2a-dd96-35d0-90cf-fed020f7697a | -3.31392 | -47.01518 | 2024-10-12 04:57:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fc9b1b0f-e004-35f3-93e3-eab075ed3278 | -3.31013 | -47.01012 | 2024-10-12 04:57:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ca151b2d-e256-3f22-adcd-91bdbb4e4cb3 | -3.30948 | -47.01451 | 2024-10-12 04:57:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 32df4a8f-34f9-3248-bcea-a9b016e3759d | -3.21784 | -46.77959 | 2024-10-12 04:57:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7d85deac-91b6-3957-b2fc-82a2af9dfd7c | -3.21718 | -46.78411 | 2024-10-12 04:57:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0096d716-8119-31c3-834f-9899f3d64abe | -3.21548 | -46.7811 | 2024-10-12 04:57:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 0925b264-21bc-3728-97f9-d7565455f009 | -3.21478 | -46.78561 | 2024-10-12 04:57:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| aac0cba0-31f0-3d67-837e-828da36318ed | -3.21334 | -46.77887 | 2024-10-12 04:57:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 01e8c8fe-dea9-369e-8531-9e297849006e | -3.21268 | -46.78339 | 2024-10-12 04:57:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 52bb4ccd-a7c0-32e7-a4c0-ee7377a4b9ca | -2.31762 | -46.05066 | 2024-10-12 04:57:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d78e0d16-7b1e-3420-a7e3-67c58b71cff5 | -2.61207 | -47.34183 | 2024-10-12 04:57:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 95f940f7-bd3f-38db-9d79-a2ed4f2dac4c | -2.61147 | -47.34588 | 2024-10-12 04:57:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3a08394d-60a9-3e9b-94ba-3692793090a3 | -2.60717 | -47.34521 | 2024-10-12 04:57:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 2e9988ef-bd96-3103-adc1-78e31f2c34c1 | -4.1055 | -46.80502 | 2024-10-12 04:57:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| efe18e6a-2060-3fe2-9815-c5124bad3c07 | -4.91387 | -47.64969 | 2024-10-12 04:57:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6ea53f11-d015-3c79-a69f-37534a81edc8 | -4.9125 | -47.6515 | 2024-10-12 04:57:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3dd775e4-58b4-3cdb-b6c6-787dd81dc6c9 | -4.85798 | -46.85638 | 2024-10-12 04:57:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1cfd0246-3536-396e-b70a-76b773fa544f | -4.61791 | -47.36293 | 2024-10-12 04:57:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 24ff74db-59dc-3bf5-b2dd-2d73c0050bda | -4.61727 | -47.36719 | 2024-10-12 04:57:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b7471641-095a-3b14-988a-415b116de537 | -4.58428 | -47.09559 | 2024-10-12 04:57:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 27.5 |
| b4e408a4-02bc-3a36-a769-d5f30187c799 | -4.58362 | -47.10016 | 2024-10-12 04:57:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 27.5 |
| fa8bf4c8-c88c-3c1b-9bcc-67c3c939c73c | -4.5791 | -47.09962 | 2024-10-12 04:57:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f0a6acd8-5c87-30cc-9fd0-d613cc5b4d10 | -4.47577 | -47.73573 | 2024-10-12 04:57:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c9c31f36-e838-38a3-9cab-024925c92eab | -4.47415 | -47.7338 | 2024-10-12 04:57:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 66bb3258-ccc0-3c7e-8e29-2da6cd3c4d92 | -4.47147 | -47.73508 | 2024-10-12 04:57:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fe7c6523-7f74-34e3-8636-58ec909d5f68 | -3.94377 | -46.43612 | 2024-10-12 04:57:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 10.2 |
| c9eb1f88-48c4-3855-bb19-da451fd4b0b8 | -3.94305 | -46.44106 | 2024-10-12 04:57:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 03e786e3-824d-309c-8079-c1008a40051f | -3.93982 | -46.4305 | 2024-10-12 04:57:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 574a4b8d-0c19-37eb-af78-15bd40900535 | -3.9391 | -46.43541 | 2024-10-12 04:57:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 6af58070-ae11-361a-9ae9-12514269b68e | -3.93838 | -46.44033 | 2024-10-12 04:57:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 9.4 |
| c339141e-35d5-34de-b909-6d20870bfaa5 | -3.93516 | -46.42973 | 2024-10-12 04:57:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 2cf3bc4e-c674-3a8c-bf45-e9d5496543b7 | -3.93444 | -46.43465 | 2024-10-12 04:57:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 070f1804-7816-352b-b295-0c9ab9c6995c | -3.93372 | -46.43958 | 2024-10-12 04:57:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 9.4 |
| c31fea36-39c8-380f-a800-b4974de12e61 | -5.64863 | -47.92224 | 2024-10-12 04:57:00 | NOAA-21 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b0211933-67c9-3c35-8def-c74c370a2644 | -5.64804 | -47.92635 | 2024-10-12 04:57:00 | NOAA-21 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d44de6b0-2b6e-3f4a-86a0-cd5e20f27777 | -5.52317 | -47.69652 | 2024-10-12 04:57:00 | NOAA-21 | SÃO MIGUEL DO TOCANTINS | TOCANTINS | Brasil | 1720200 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e4190fc1-89fa-3d60-aedd-67c4583834be | -5.52254 | -47.70079 | 2024-10-12 04:57:00 | NOAA-21 | SÃO MIGUEL DO TOCANTINS | TOCANTINS | Brasil | 1720200 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 716cf180-4c85-3ef9-9f7a-6156ca65c274 | -5.19513 | -47.8411 | 2024-10-12 04:57:00 | NOAA-21 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 437e747c-9afd-3d8f-967f-8168ae23008b | -5.12044 | -47.49646 | 2024-10-12 04:57:00 | NOAA-21 | SÃO FRANCISCO DO BREJÃO | MARANHÃO | Brasil | 2110856 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0541e166-24b3-3004-973d-4a8b94075fb0 | -5.08603 | -47.18445 | 2024-10-12 04:57:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4bc9309e-9418-3ada-8951-ca01357037e9 | -5.0838 | -47.18207 | 2024-10-12 04:57:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 5945da40-f4bb-3367-aed0-125d9db399ca | -5.08223 | -47.17902 | 2024-10-12 04:57:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7b2e9bb1-0bf9-32cd-8f96-e6d6fb31ece7 | -5.08152 | -47.1838 | 2024-10-12 04:57:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4ab59584-83a9-385f-8fbe-75a36271e3f8 | -6.44802 | -47.54652 | 2024-10-12 04:57:00 | NOAA-21 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d7855ca1-dd70-3743-b537-524a12ebfc2d | -6.44538 | -47.54881 | 2024-10-12 04:57:00 | NOAA-21 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 003844f0-627f-339c-938c-565dd3bddac3 | -6.44291 | -47.55022 | 2024-10-12 04:57:00 | NOAA-21 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1f5edea4-fff2-3271-b604-0705e5685f34 | -6.12354 | -47.87078 | 2024-10-12 04:57:00 | NOAA-21 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 44383ac1-8184-3406-b2c4-c151993764af | -6.11917 | -47.87017 | 2024-10-12 04:57:00 | NOAA-21 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 63d5cd97-5cb8-3eee-b3cd-70ebcf906dfe | -6.11856 | -47.87439 | 2024-10-12 04:57:00 | NOAA-21 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 493201ab-01d6-345f-b09c-3fd78faaac62 | -7.43552 | -47.35389 | 2024-10-12 04:57:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 730a58fe-fb28-381c-85ab-d383ddef43d5 | -7.10741 | -48.32638 | 2024-10-12 04:57:00 | NOAA-21 | CARMOLÂNDIA | TOCANTINS | Brasil | 1703883 | 17 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 228c318e-0249-3300-bbd4-da69bb0858c1 | -6.51247 | -47.82521 | 2024-10-12 04:57:00 | NOAA-21 | SANTA TEREZINHA DO TOCANTINS | TOCANTINS | Brasil | 1720002 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 68c9ea87-f1a1-3cde-8fc2-199af043bb05 | -6.51213 | -47.82775 | 2024-10-12 04:57:00 | NOAA-21 | SANTA TEREZINHA DO TOCANTINS | TOCANTINS | Brasil | 1720002 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 22446dd8-5f4d-3167-b499-d032df4a6a1c | -6.51186 | -47.82961 | 2024-10-12 04:57:00 | NOAA-21 | SANTA TEREZINHA DO TOCANTINS | TOCANTINS | Brasil | 1720002 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 4827fcc2-1713-32d9-ae4e-05511be677c4 | -8.91245 | -47.91529 | 2024-10-12 04:57:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4a72f52b-770a-31e5-b83a-6956a0916c9f | -8.88342 | -47.82073 | 2024-10-12 04:57:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1f688f72-aad8-3b5c-b205-2e95cda3e226 | -8.883 | -47.81958 | 2024-10-12 04:57:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| cb75b256-eed1-3e9f-9b2a-f51c508e42a1 | -8.87885 | -47.82004 | 2024-10-12 04:57:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1129d082-3394-38e1-9ef8-79d89a6b24da | -8.8497 | -47.95683 | 2024-10-12 04:57:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| faf9267d-85fe-35c3-90cd-f3af165ce08a | -8.73796 | -47.18199 | 2024-10-12 04:57:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3b276da3-8b75-3877-9e43-94f23c793470 | -8.7332 | -47.18126 | 2024-10-12 04:57:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 37fd0c9f-40eb-336e-b995-ef5f43f532b0 | -7.93395 | -47.9766 | 2024-10-12 04:57:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c559a8fe-ff36-3e5a-bd9f-8a906d7397ba | -7.93332 | -47.98107 | 2024-10-12 04:57:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 69fa1ef7-3be4-338c-953b-b7989f37b14d | -2.00202 | -47.25566 | 2024-10-12 04:57:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a429b9f0-a69b-3440-8850-833fa5b23b47 | -2.0014 | -47.25969 | 2024-10-12 04:57:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cc9255d0-bdfb-3135-818d-59d262fb4d4e | -1.62172 | -48.02565 | 2024-10-12 04:57:00 | NOAA-21 | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f2aa5f94-e3f1-3fd7-a8b1-b2fe33b404e3 | -1.61768 | -48.02503 | 2024-10-12 04:57:00 | NOAA-21 | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7cd7343b-7576-3ac7-9d31-924b2f133a74 | -3.45998 | -47.66341 | 2024-10-12 04:57:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| e8c4fc31-516b-3c3b-88c7-e5638c9ada52 | -2.95914 | -47.91485 | 2024-10-12 04:57:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 103e3512-eb51-3669-880f-d371e97f3534 | -2.82265 | -48.45701 | 2024-10-12 04:57:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9de1f221-ce43-3493-827e-30a7bf664077 | -2.81919 | -48.45292 | 2024-10-12 04:57:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bbb906be-9599-3695-be72-9e5febac11b3 | -2.81866 | -48.45639 | 2024-10-12 04:57:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f1c833cf-7945-3937-bbe5-a3000fa6eea7 | -2.80211 | -48.6918 | 2024-10-12 04:57:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 57085cce-d9e1-305d-847a-6e772f1e7ec3 | -2.79221 | -48.57541 | 2024-10-12 04:57:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fbf64046-eb0d-378a-8728-e6955536a627 | -2.78718 | -48.0918 | 2024-10-12 04:57:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 60d852fd-37a1-3689-8311-95519a7314d8 | -2.78662 | -48.09544 | 2024-10-12 04:57:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d2ff25cc-065b-33b1-9c13-4e4149f865c7 | -3.07174 | -48.02768 | 2024-10-12 04:57:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8b208f3b-7304-3ca8-9eaf-70978da52a46 | -3.05866 | -47.48323 | 2024-10-12 04:57:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| df06b7f1-32c4-3bca-bf0e-415422e2067e | -2.69528 | -48.63106 | 2024-10-12 04:57:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1dd20491-cfa8-3da6-994c-3a5179cdabd9 | -2.63739 | -48.1167 | 2024-10-12 04:57:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 686bab46-aad5-38c9-9d0b-30b09678ff49 | -2.63342 | -48.47774 | 2024-10-12 04:57:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6f15f55f-368e-344f-912c-21b2327b1aeb | -2.63239 | -48.48462 | 2024-10-12 04:57:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 892d4fdc-2bd1-3415-ad58-74282280a08c | -2.62943 | -48.47712 | 2024-10-12 04:57:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f4c24b15-2488-3826-a4b0-16306b78a076 | -2.62841 | -48.48399 | 2024-10-12 04:57:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e1a54276-ceed-32a3-99be-d4820acf0ebb | -2.62814 | -47.98436 | 2024-10-12 04:57:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f1d0b3f5-a65f-39bb-9726-c0c2aac0fc79 | -2.62611 | -48.48304 | 2024-10-12 04:57:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 40e16061-a41a-3a42-9e5e-08954ca0ab4f | -2.62403 | -47.98371 | 2024-10-12 04:57:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b3bf8021-67fb-3a87-bf51-5cae926bf977 | -2.48019 | -48.05258 | 2024-10-12 04:57:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3070e7a8-3560-37f0-92cb-009c73d1be9d | -2.46252 | -47.84294 | 2024-10-12 04:57:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d85befdd-7c6f-3848-81ed-8f74274f042c | -2.45838 | -47.84232 | 2024-10-12 04:57:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README68.md)
