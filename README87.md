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

## Dados Diários - Página 87

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3b8e498b-34ba-30b1-a033-edb83393f1ab | -10.9453 | -46.71212 | 2025-10-03 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 15.3 |
| f14ab92c-3085-3dbe-b170-bde681927bed | -9.38961 | -47.33757 | 2025-10-03 04:32:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| febaad77-f44d-3e95-95e4-feb7d7bef5d1 | -10.00493 | -48.26843 | 2025-10-03 04:32:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a6c9664d-3349-3c1a-a461-818473972a71 | -7.7489 | -46.26138 | 2025-10-03 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| cb49d3af-e5f6-3e22-ad19-a9e98bcee4be | -7.7478 | -42.58007 | 2025-10-03 04:32:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 1ee9fa2d-9a7b-3470-9cad-33034e8f8c20 | -11.85869 | -44.97333 | 2025-10-03 04:32:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e146cee7-2857-3d69-8c63-420de6f3012c | -11.90463 | -46.30633 | 2025-10-03 04:32:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bc1b6322-07f4-34e3-a72a-68a87f49289e | -8.88527 | -46.5875 | 2025-10-03 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a6e3d2b9-f258-32b3-ae93-78a78212dab2 | -11.59521 | -47.66561 | 2025-10-03 04:32:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 61a76733-1654-3e9c-a462-e0ba8a8d0294 | -6.48102 | -44.22171 | 2025-10-03 04:32:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 35b0ff0a-e85c-32e2-af41-e87711be9cbf | -7.75174 | -46.26561 | 2025-10-03 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 7895c3eb-ba10-37e9-ac35-9decf33f02d8 | -11.49029 | -45.00858 | 2025-10-03 04:32:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 31f00c66-661f-3267-bff3-0868339eb249 | -7.76825 | -46.27164 | 2025-10-03 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 97aa88cf-d115-32bb-a4d1-4bf779ec1d04 | -7.563 | -42.39859 | 2025-10-03 04:32:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| ca8fdbb1-2f87-35fe-95c0-7097886d262d | -7.71806 | -46.62197 | 2025-10-03 04:32:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0915a0e8-fae6-3747-aadd-c0eb2b198759 | -11.82577 | -45.04313 | 2025-10-03 04:32:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 095d5502-a0a6-3a7a-89ae-47cc00f66d21 | -9.76786 | -46.21775 | 2025-10-03 04:32:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a3fc3c85-94e9-395e-92f7-e10e017b29a0 | -7.48154 | -43.0377 | 2025-10-03 04:32:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 21dda1b3-7bfa-3f86-9a37-94b353af44e1 | -7.74636 | -42.57582 | 2025-10-03 04:32:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| e2c5cf56-d072-39aa-b42e-b72c90557d68 | -7.76538 | -46.26757 | 2025-10-03 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 43.1 |
| 47c81574-f761-32be-ae10-d85ee2f9730c | -10.9476 | -46.72025 | 2025-10-03 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 016dece8-35ca-3a48-bab2-b41ca0125afb | -6.65368 | -42.78714 | 2025-10-03 04:32:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 1d05835c-fafb-344e-aabe-4acd02e8931f | -10.9658 | -51.08797 | 2025-10-03 04:32:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 837c2b6c-7a1a-35e8-89ac-a0a7840db97b | -7.29354 | -46.01094 | 2025-10-03 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 09d57ac9-ebc0-3afe-9a4c-a1cad8f88da6 | -11.15786 | -47.18 | 2025-10-03 04:32:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fdc5d2f4-d8d3-3cc7-8456-9ce2ac90712a | -10.89261 | -46.71617 | 2025-10-03 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2375c056-e777-37d0-a9f2-5cbcc449d06b | -10.41262 | -54.41265 | 2025-10-03 04:32:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ff9d6ead-acfc-3b2f-8e95-603864fd1ce2 | -9.87981 | -47.80986 | 2025-10-03 04:32:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f76afb4d-eb09-39ac-85a6-9c1b4e95cf93 | -11.90877 | -46.30268 | 2025-10-03 04:32:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a50f9484-dde4-3a7a-b07e-0708d2477818 | -8.64542 | -47.71249 | 2025-10-03 04:32:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| bd3d17ee-ab10-30ad-9777-e8d74caaa5fd | -7.31006 | -42.87174 | 2025-10-03 04:32:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 22f963ea-3f9f-33cc-a860-5a0d5b7667f8 | -7.75627 | -46.25874 | 2025-10-03 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 24.5 |
| e5c5c720-b64a-3635-8fa9-8c6e0c611789 | -11.21411 | -41.59588 | 2025-10-03 04:32:00 | NOAA-20 | JOÃO DOURADO | BAHIA | Brasil | 2918357 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 2b23e1ef-1a82-3f89-9453-6fc7991ea4d5 | -10.00816 | -50.22733 | 2025-10-03 04:32:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| a7dfeaf6-7a31-3f57-8880-635d0816f958 | -11.14656 | -43.38547 | 2025-10-03 04:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 177981aa-3401-30dd-b3c2-19696a3d18ed | -11.83595 | -44.99803 | 2025-10-03 04:32:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 624731c7-8aaa-3301-945d-0aefb9bf38c8 | -6.68312 | -42.83875 | 2025-10-03 04:32:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 6568399d-9c3d-3fb9-bbe7-10409b850a87 | -11.50323 | -43.50764 | 2025-10-03 04:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c461613d-8715-3c1b-b510-5c1f263fb0f6 | -9.84155 | -48.27065 | 2025-10-03 04:32:00 | NOAA-20 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ae96b2b9-a81e-38db-8aca-91ce7e1ea08e | -7.46123 | -46.85692 | 2025-10-03 04:32:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bdfa8474-84ad-378e-8f2e-1465e524b0ee | -8.88214 | -49.79426 | 2025-10-03 04:32:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 083805da-9dd5-352f-bed4-f673188b59fe | -10.84368 | -47.2189 | 2025-10-03 04:32:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9703bb06-a71d-3696-bb8a-636fccbda6e7 | -11.49784 | -45.00935 | 2025-10-03 04:32:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 081039f6-8a1a-39a3-84af-ae6ad6cde638 | -10.94931 | -46.70882 | 2025-10-03 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 70c8e98e-6a7b-347a-b503-9ae9f44504c3 | -10.92872 | -46.72895 | 2025-10-03 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 4bf8bbc7-6d4c-32c5-9904-dd7030996da4 | -11.13623 | -43.39915 | 2025-10-03 04:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 4ff79d86-f9d3-367d-a713-5bf317611f2d | -11.59621 | -42.86963 | 2025-10-03 04:32:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 53c01e2c-1c55-30f9-9c18-702cd3229700 | -5.26626 | -42.64048 | 2025-10-03 04:32:00 | NOAA-20 | DEMERVAL LOBÃO | PIAUÍ | Brasil | 2203305 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f02b4267-0514-322c-be8b-24748b632e8d | -11.86746 | -44.99297 | 2025-10-03 04:32:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cdfe0271-a0ee-3c08-bc35-5fa2141c074a | -7.21055 | -46.88049 | 2025-10-03 04:32:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 38481653-540a-32b0-9de0-28099471dc70 | -11.59011 | -47.63153 | 2025-10-03 04:32:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0758996c-7699-3f49-88cd-d102f5e34ea3 | -11.86496 | -44.98343 | 2025-10-03 04:32:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8e86d305-013e-323c-941d-6be512612483 | -5.44931 | -44.8273 | 2025-10-03 04:32:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 44024618-4571-3a67-a2a7-2b1fa3b4c564 | -6.23512 | -44.24113 | 2025-10-03 04:32:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6f98b362-b50a-330b-8af7-24f4d1c74930 | -11.61973 | -47.98927 | 2025-10-03 04:32:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0b34aa77-23cd-3fdf-9dff-94ddf2b0e361 | -7.29707 | -44.19069 | 2025-10-03 04:32:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 6c43d64e-7f62-3d5b-83c1-25bb159ecbf3 | -11.78467 | -46.82824 | 2025-10-03 04:32:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cba0896a-012d-3fa2-8486-453c98e02550 | -11.91059 | -46.26598 | 2025-10-03 04:32:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 5f321d45-aff1-3be8-9d1e-d6760eeb21a9 | -11.08744 | -47.87669 | 2025-10-03 04:32:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 40d4b374-398f-3f9b-86a9-9b0b49f62c40 | -8.83228 | -44.80515 | 2025-10-03 04:32:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 0e31c8c4-4750-3400-b71a-1f7e7fa7a6fa | -9.94572 | -43.76764 | 2025-10-03 04:32:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 7307271c-10c7-3cab-bb66-0ae6462daa53 | -10.01729 | -48.49206 | 2025-10-03 04:32:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2e5154be-0747-3ba7-aa16-6c290c6554d6 | -11.01192 | -46.55018 | 2025-10-03 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 34a71878-08d8-360c-b227-6214b3eabdcb | -7.76237 | -42.61218 | 2025-10-03 04:32:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 22.7 |
| a9ba2a89-dfb8-3fbe-9473-1ea029cb94e4 | -11.13808 | -47.19582 | 2025-10-03 04:32:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5effdcc1-38dd-3f70-9f4c-d6f7a837b3ff | -6.96174 | -45.34222 | 2025-10-03 04:32:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 17ef10a4-0c9d-36ca-a568-3e322e83f813 | -10.9052 | -46.72589 | 2025-10-03 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0bebf8fb-14bb-3320-820e-436b91fe52b9 | -11.10288 | -47.82075 | 2025-10-03 04:32:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| aa959a7e-23ca-3a30-8c3c-930b0bd2f54d | -6.05635 | -44.63615 | 2025-10-03 04:32:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| f1fa9dfd-d870-3ffd-ad35-c08349c690ca | -8.75594 | -49.9234 | 2025-10-03 04:32:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 88094b37-ccc5-3405-b304-09b03f24fa64 | -6.05154 | -44.64376 | 2025-10-03 04:32:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e4b45e12-d59e-3910-b58f-9c4f9ca17aad | -7.26067 | -48.48165 | 2025-10-03 04:32:00 | NOAA-20 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e68f7bac-fddd-33fe-8143-873f565c04e1 | -10.82151 | -49.37606 | 2025-10-03 04:32:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f05f9a55-3454-327f-b125-795a57da815a | -11.32006 | -49.01745 | 2025-10-03 04:32:00 | NOAA-20 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 72c28262-02b7-3770-b76a-3b70e9171b3d | -7.89183 | -47.32125 | 2025-10-03 04:32:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b9ec6c20-c82f-3db5-a89a-9b0a6eecf10f | -8.75933 | -49.92396 | 2025-10-03 04:32:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5b15b87a-edbe-36ce-b2ad-8c4bc30b873a | -11.10681 | -47.83967 | 2025-10-03 04:32:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0731b1d9-39d8-3505-a6ff-445c5cbe98a3 | -7.81756 | -46.97026 | 2025-10-03 04:32:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5592c8f4-0ea3-3dcb-aa28-d2ca5d033f9a | -7.82035 | -46.97433 | 2025-10-03 04:32:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 68fa8bc6-34f7-39d6-92e7-e84bb783108c | -11.80193 | -47.93404 | 2025-10-03 04:32:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5e566857-3210-322e-8167-74c3fc3944c5 | -8.65913 | -39.43364 | 2025-10-03 04:32:00 | NOAA-20 | CURAÇÁ | BAHIA | Brasil | 2909901 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 2639f6cf-6494-39ca-bf36-fe9793caa464 | -10.00548 | -48.26492 | 2025-10-03 04:32:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d622b7cd-a884-3c4b-be2e-5d7d478661bd | -7.56508 | -42.63002 | 2025-10-03 04:32:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| baa4c451-5d9c-3d5c-be53-9a96b1af3e49 | -11.93625 | -47.87782 | 2025-10-03 04:32:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fcdfbfdf-3180-3e08-b473-cd93e7c86bd9 | -10.93842 | -46.71104 | 2025-10-03 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 907a49c1-23a3-3bc7-abff-518b148f403f | -10.10731 | -48.09103 | 2025-10-03 04:32:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d5686337-6bd4-3c6c-b688-d476929301ea | -8.62085 | -54.99108 | 2025-10-03 04:32:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fefba959-7959-3268-962a-3aae61951614 | -10.59148 | -48.70633 | 2025-10-03 04:32:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| e7140509-ff50-33c8-9092-b935411f3803 | -7.79936 | -46.02094 | 2025-10-03 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1da4ff1c-57f7-3da9-94a0-a9f233a5773f | -8.80333 | -46.6685 | 2025-10-03 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2ea14edb-a45c-3018-88b1-da6ebfb81063 | -7.76084 | -46.27448 | 2025-10-03 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 45.7 |
| ccb6d154-39ba-3c44-b1a8-f8100e4a089a | -11.87059 | -44.99797 | 2025-10-03 04:32:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5ee42dd3-797e-3b26-814b-c7db3b3aef2b | -10.95505 | -46.71749 | 2025-10-03 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 079f93c8-d070-396b-9f17-12a6e67e6c2f | -7.87075 | -47.30358 | 2025-10-03 04:32:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 314d420d-b83e-397c-8cec-1f252d25dcf3 | -11.88236 | -45.02334 | 2025-10-03 04:32:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 52ce6815-eef2-3195-ba5e-d368bb96d227 | -10.90349 | -46.71398 | 2025-10-03 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0e392e50-9723-301b-af41-1ba7cf52a0c0 | -5.56079 | -47.22263 | 2025-10-03 04:32:00 | NOAA-20 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e0cd2713-f696-3b32-9b88-71fcf5dfbb87 | -11.61499 | -45.05981 | 2025-10-03 04:32:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9008b7ed-37b0-332d-8196-8364b74eaedc | -11.82579 | -45.01567 | 2025-10-03 04:32:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6564a522-befa-340d-bb88-63133b98e6b2 | -4.48397 | -47.6745 | 2025-10-03 04:32:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README88.md)
