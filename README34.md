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

## Dados Diários - Página 34

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ca94debe-1631-348d-ac59-a3e59a84a7d9 | -8.76365 | -44.27453 | 2026-09-21 04:19:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 7.2 |
| d750596a-3775-3ee4-b2ec-b7214229e61b | -3.6651 | -40.55507 | 2026-09-21 04:19:00 | NOAA-20 | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 53e30294-025f-339f-817c-a767ae10ed1e | -8.41297 | -45.87009 | 2026-09-21 04:19:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| c400682e-9fa2-3d5b-a29a-605dccc026a1 | -8.76597 | -45.85759 | 2026-09-21 04:19:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 935256a0-f3f5-37ec-b27e-595e4f392f9e | -2.17182 | -48.32013 | 2026-09-21 04:19:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ef265f19-3a78-3507-b449-f7c84eaa1b6c | -8.7841 | -48.74679 | 2026-09-21 04:19:00 | NOAA-20 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f2fd0727-71ca-345e-b8a1-0e3d9e323264 | -7.38157 | -51.77476 | 2026-09-21 04:19:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d6a05fef-40ae-346f-b1a2-27767cf31135 | -5.19886 | -56.10369 | 2026-09-21 04:19:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| ba71cb9c-418f-3618-8ef3-7b0a9da86007 | -7.89105 | -44.84582 | 2026-09-21 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 628ce3fa-00b2-335a-ba2c-dfcf72dc0fe2 | -6.53859 | -44.9279 | 2026-09-21 04:19:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 117163ba-b2da-3f57-bbf3-ea888fd5d050 | -3.45102 | -50.61186 | 2026-09-21 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 73acc3d1-2242-3882-a1a5-5d4e01a2c77e | -9.44047 | -45.41772 | 2026-09-21 04:19:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9358073d-d17f-3ed3-adf3-5c53b9f1fa54 | -5.20458 | -56.11099 | 2026-09-21 04:19:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 1a2a9d32-fa6b-39a2-96e1-e509f29aaa5b | -6.88727 | -42.93185 | 2026-09-21 04:19:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 0247535a-a322-3342-ab20-895e0ac67efc | -6.46643 | -48.4451 | 2026-09-21 04:19:00 | NOAA-20 | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 037a1655-cd9b-3dc5-8498-ad8931fb359b | -6.47124 | -42.77025 | 2026-09-21 04:19:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| ef62b6a3-49f2-36ff-a8f2-262f1f292110 | -6.88675 | -41.71045 | 2026-09-21 04:19:00 | NOAA-20 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 9d8d1c2f-51bf-334b-8e51-4405a3ea62f2 | -3.06333 | -43.76121 | 2026-09-21 04:19:00 | NOAA-20 | MORROS | MARANHÃO | Brasil | 2107100 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 90624010-a0cf-3dd3-8be5-7dcfef2ae71f | -9.44785 | -45.38136 | 2026-09-21 04:19:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 78.7 |
| dfc26e0e-6b93-3f93-8054-b62cbd31a1cf | -9.27152 | -45.91997 | 2026-09-21 04:19:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ca688ec5-6d07-3879-80da-82a3f098cf86 | -5.21235 | -56.1129 | 2026-09-21 04:19:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 5d48cc49-81d2-3647-a096-f518a78508c0 | -9.24622 | -46.18031 | 2026-09-21 04:19:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 589f2af6-f913-3e1b-ae9c-37363c58a74d | -4.09136 | -52.12193 | 2026-09-21 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 598e6bd3-6239-37d1-83b2-8de9f5718f2d | -9.10686 | -44.70088 | 2026-09-21 04:19:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b84b3404-519a-3147-a358-de3c680539e4 | -8.78014 | -48.74596 | 2026-09-21 04:19:00 | NOAA-20 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 569fde8b-0f82-3142-bafe-ab59cc677eed | -7.32482 | -55.22324 | 2026-09-21 04:19:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 04ecd376-03b9-3606-a922-fa3397c13c71 | -5.8424 | -53.54237 | 2026-09-21 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2e417736-297f-3460-8cf8-0be09e419bb8 | -6.72731 | -55.07903 | 2026-09-21 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9fd56242-939f-340a-abbc-19ea5d3a782b | -8.41827 | -45.85939 | 2026-09-21 04:19:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 43a717ce-b0a6-3313-a255-47b754f0c7e1 | -2.99822 | -54.17368 | 2026-09-21 04:19:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 87782ea8-6790-34d2-9737-c0b90d72b72c | -7.42246 | -44.73407 | 2026-09-21 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f3979ec4-a401-3508-bc9c-8795bbc7229a | -7.45543 | -44.74294 | 2026-09-21 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a9223220-97d2-3aa3-9397-c1daadda9607 | -8.78881 | -48.74331 | 2026-09-21 04:19:00 | NOAA-20 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 45a1da86-1ea4-33d5-98b0-4140b2385a67 | -6.93312 | -38.22577 | 2026-09-21 04:19:00 | NOAA-20 | SÃO JOSÉ DA LAGOA TAPADA | PARAÍBA | Brasil | 2514206 | 25 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 1a413ccf-b570-3df4-821c-8f52ea019daa | -4.87583 | -55.88713 | 2026-09-21 04:19:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 5401fa89-7a6e-363a-9323-44bc5cf7ed5d | -4.11276 | -46.39225 | 2026-09-21 04:19:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 949f9d2a-ae28-3ddb-851b-215075d4c574 | -2.82068 | -46.7132 | 2026-09-21 04:19:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 074dab57-bf9e-39de-b462-28667d718c8d | -6.99775 | -43.37238 | 2026-09-21 04:19:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 7780487d-063a-3c30-9c49-9dc38342f6e1 | -9.53929 | -45.39285 | 2026-09-21 04:19:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5bfb1e96-4cf0-3fd6-a82f-b6a48d8e2fb6 | -6.99487 | -42.20351 | 2026-09-21 04:19:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 7cabc094-2800-3221-b65e-829ce95ef892 | -9.26917 | -46.19202 | 2026-09-21 04:19:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ef55630e-7dbb-3673-a162-cac7c7c2388f | -4.55974 | -55.75047 | 2026-09-21 04:19:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 74bfda41-9e91-3306-b9f0-70d72f42eb46 | -6.71904 | -55.08888 | 2026-09-21 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b31c8adb-4956-3da6-a9a3-cc5cfb0e50d2 | -2.61123 | -51.72217 | 2026-09-21 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 74f869a0-cb3c-34de-a4ef-d5a8814e08bd | -9.00424 | -44.34241 | 2026-09-21 04:19:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| be8990c0-8f36-3f09-b6b4-8f2aed677289 | -7.54629 | -45.4204 | 2026-09-21 04:19:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 43497b3b-a31d-3969-b330-0dcf95b8ed97 | -6.73605 | -55.10179 | 2026-09-21 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ed0d43c9-f695-367d-8a76-2bdf746a98f6 | -9.46727 | -45.41061 | 2026-09-21 04:19:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2f432191-9f51-37f5-80d3-ae332463a40e | -6.91319 | -42.91844 | 2026-09-21 04:19:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| ba8fe34d-8dc0-372a-8209-20893ab9cf18 | -6.97582 | -42.17135 | 2026-09-21 04:19:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 74fb2943-7ddd-32bb-aadd-4eb7d3fdf9f0 | -8.77355 | -44.29762 | 2026-09-21 04:19:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 307c9045-e45a-37e7-b2cd-b67956f493ad | -6.98705 | -42.20958 | 2026-09-21 04:19:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 2c78afef-f541-3bcb-8128-6c66916505b1 | -7.43791 | -44.78773 | 2026-09-21 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 43d1e1cf-6abb-38b5-b38c-335f9f649180 | -5.8165 | -53.52106 | 2026-09-21 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 99c0dbc3-a50a-3935-80b3-f66ee3130646 | -9.03584 | -48.14917 | 2026-09-21 04:19:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 4c046956-65fd-347e-957c-540dbb7940e7 | -7.41777 | -44.78451 | 2026-09-21 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.4 |
| b99cd4bf-70e9-3ffd-93aa-dc596e33824d | -7.02454 | -42.0799 | 2026-09-21 04:19:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| cf3168b1-2612-39be-a135-33a48f90f470 | -8.79675 | -48.74478 | 2026-09-21 04:19:00 | NOAA-20 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 9.1 |
| c674e2ba-9f03-32b8-9bd9-ca2e4023aab8 | -9.45478 | -45.42358 | 2026-09-21 04:19:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 674b6c1a-0233-3fbd-81b2-3475c637093e | -6.46987 | -48.44935 | 2026-09-21 04:19:00 | NOAA-20 | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 769e400e-faa5-3482-9010-d353a8aefb40 | -4.07121 | -52.13 | 2026-09-21 04:19:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bc9c4520-1a90-3b08-a091-24dab927f890 | -9.25941 | -46.18651 | 2026-09-21 04:19:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ed3214e0-69c7-3d4c-97d2-86f284f4a288 | -4.09077 | -52.12529 | 2026-09-21 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f760fff2-ac0f-3f64-8ccc-8df6678ab2d5 | -9.44505 | -45.44068 | 2026-09-21 04:19:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 672ca01c-be26-3243-b206-c321d4e3f5bb | -8.30438 | -45.99779 | 2026-09-21 04:19:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f926ca31-d126-3575-bfd1-27f91de79746 | -2.99601 | -54.16972 | 2026-09-21 04:19:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c1867d70-7dd5-3c75-aed1-7a3aefda90ed | -5.83375 | -53.52421 | 2026-09-21 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 519f5e7c-aa85-3fb0-aafe-f85f4af24f0a | -6.21392 | -53.57238 | 2026-09-21 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 78b4df1f-09a1-33ae-a02c-7c0d04b02260 | -8.36654 | -47.20645 | 2026-09-21 04:19:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d760566b-dbc3-35e4-aef8-a24f13964fc8 | -8.41703 | -45.86693 | 2026-09-21 04:19:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fd7cccb8-dda8-33fe-94ea-e659d785d54a | -3.33861 | -42.7743 | 2026-09-21 04:19:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 15bffd0f-698f-3fba-92c5-76ecc2765f3e | -7.31821 | -46.76898 | 2026-09-21 04:19:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1fc25434-f71b-374a-af42-968484d47c46 | -7.56165 | -57.68485 | 2026-09-21 04:19:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ee086fe4-8f3e-39f9-824d-aee1adf71907 | -6.28875 | -41.76867 | 2026-09-21 04:19:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| c60cdd8e-23d9-3d55-9327-dccce5fbf01d | -5.66376 | -42.63594 | 2026-09-21 04:19:00 | NOAA-20 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 4fa53b7e-729d-31b9-8c9e-829508a04b08 | -9.44106 | -45.41411 | 2026-09-21 04:19:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 30a7ebaf-2d2f-3fdc-8e2f-4447eb9ab9d1 | -6.04031 | -53.27759 | 2026-09-21 04:19:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 104540b5-5f0a-3b1f-8050-612283a64f46 | -5.82156 | -53.52596 | 2026-09-21 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c52a35f3-900e-34df-b77e-a8e46bd69853 | -6.77676 | -55.49934 | 2026-09-21 04:19:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3ead305a-3eeb-3674-a058-0c56012e79a3 | -9.4635 | -45.39137 | 2026-09-21 04:19:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 173.0 |
| 7dba3682-29dc-38c5-8037-22d4cbacade0 | -4.09676 | -52.12288 | 2026-09-21 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 17f04cab-be9b-3ca0-9a2d-5d0a7f274a9b | -7.87181 | -48.92385 | 2026-09-21 04:19:00 | NOAA-20 | BERNARDO SAYÃO | TOCANTINS | Brasil | 1703206 | 17 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1c0e0997-6dae-39cd-9de9-88c22317c56d | -9.47064 | -45.41116 | 2026-09-21 04:19:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2f6e32f7-ec32-30d9-a849-61d5636ec1ee | -8.36288 | -47.20583 | 2026-09-21 04:19:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 77d71e3e-de1f-3005-93c0-c76eb88f703c | -9.54207 | -45.39703 | 2026-09-21 04:19:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| dd744c1d-60b6-37b2-8434-d41ad2d9814c | -7.33196 | -55.21959 | 2026-09-21 04:19:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8a388fcc-cc7a-3037-ae50-4dbf8c1ce02d | -8.94336 | -49.05533 | 2026-09-21 04:19:00 | NOAA-20 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ba46b8f7-8c85-313f-a77f-6d80d903197f | -7.51592 | -46.22962 | 2026-09-21 04:19:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bb40b557-1adb-3552-a806-dd45225b54e9 | -9.27296 | -46.21225 | 2026-09-21 04:19:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 390fd72b-a787-3815-8b88-7639d3b38dfc | -9.26508 | -46.1953 | 2026-09-21 04:19:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e2ee898e-bb2c-3a18-8cb7-4b35e7b066e0 | -1.67358 | -54.93719 | 2026-09-21 04:19:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d7dc280d-d327-3e40-ba05-0cc34f16777f | -6.83895 | -41.02098 | 2026-09-21 04:19:00 | NOAA-20 | MONSENHOR HIPÓLITO | PIAUÍ | Brasil | 2206506 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| ee448552-d013-3165-9a63-6ea9b8644a21 | -6.31184 | -41.75377 | 2026-09-21 04:19:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| ca5560b1-c9c3-3770-bdc0-ef7ca180e473 | -8.79369 | -48.73881 | 2026-09-21 04:19:00 | NOAA-20 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 9.1 |
| d83a51b6-707b-3372-bd81-3c0248fc3ee9 | -7.02734 | -42.08405 | 2026-09-21 04:19:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 1e41109a-5fa7-357b-8573-b5ac97f83bef | -7.42506 | -44.78202 | 2026-09-21 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6c3c74c9-c7dd-3a38-8f58-f93a7817fbdc | -6.71996 | -55.08386 | 2026-09-21 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f9386e80-fc92-31f4-9b55-9bf70fd1dd31 | -7.41737 | -44.74427 | 2026-09-21 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 787ec92b-8cfb-33b3-a5f8-8cb59bfed5e9 | -5.82367 | -53.51415 | 2026-09-21 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ae56b352-e6c2-3d67-a299-65a538c03318 | -9.5749 | -45.43934 | 2026-09-21 04:19:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |


[Clique aqui para ver as próximas entradas](README35.md)
