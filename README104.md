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

## Dados Diários - Página 104

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 94ea3738-e270-3c77-8cf9-4316e7777668 | -19.19903 | -46.83208 | 2026-09-19 11:30:00 | TERRA_M-M | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 365de289-1b71-3371-843c-63a58784dbbd | -14.79765 | -48.57647 | 2026-09-19 11:30:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 4c932405-3838-3ab1-bff7-6a619bba2928 | -19.42323 | -45.74849 | 2026-09-19 11:30:00 | TERRA_M-M | SERRA DA SAUDADE | MINAS GERAIS | Brasil | 3166600 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 790c7683-215d-3157-bdb8-703c00b692e9 | -12.5952 | -49.1046 | 2026-09-19 11:40:00 | GOES-19 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 132.1 |
| 4c0399cf-69e0-372e-bb1f-707f423eb7e9 | -11.7823 | -49.8152 | 2026-09-19 11:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 211.3 |
| 3fab7efb-7f67-301b-a610-1eb922030490 | -9.9702 | -46.578 | 2026-09-19 11:40:00 | GOES-19 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 210.2 |
| 46333aed-1a24-3658-918c-8e2431b65f31 | -10.567 | -51.3137 | 2026-09-19 11:40:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 120.3 |
| 94322586-75c8-35a4-85a4-36d290d7bdfd | -12.7085 | -45.96 | 2026-09-19 11:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 105.8 |
| 752b6d2e-ba10-38a1-980c-2f1857bedf37 | -8.7731 | -48.6868 | 2026-09-19 11:40:00 | GOES-19 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 82.8 |
| 26346171-37db-3dce-83ed-7695a0106387 | -9.9699 | -46.6004 | 2026-09-19 11:40:00 | GOES-19 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 71.0 |
| cafed354-d193-34f0-b017-544d33b95b07 | -8.7919 | -48.6851 | 2026-09-19 11:40:00 | GOES-19 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 89.3 |
| 7689241e-f200-3c05-a538-c8fc1e68babf | -7.7656 | -44.8688 | 2026-09-19 11:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 122.6 |
| 08535b35-bedc-3b33-864a-c37a2bad085a | -12.7085 | -45.96 | 2026-09-19 11:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 118.7 |
| b27fdfe4-dba6-337a-b85a-d09e22d7259b | -11.3177 | -51.7429 | 2026-09-19 11:50:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 97.6 |
| 02cd5fff-af71-3f40-81e8-ceeb1c331e3a | -11.949 | -50.1186 | 2026-09-19 11:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 134.7 |
| c8b29a22-eff4-31e8-abd0-99bad950926c | -9.2414 | -45.9411 | 2026-09-19 11:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 118.4 |
| 38557c45-5a86-3d54-9dae-18f617849023 | -11.9109 | -50.1232 | 2026-09-19 11:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 67.8 |
| e04c02e0-4b63-3185-b147-ae242d959b6d | -10.7994 | -50.8881 | 2026-09-19 11:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 72.9 |
| 00b5a8ea-ff71-3a93-be97-ba6cf5bb7f85 | -11.318 | -51.7218 | 2026-09-19 11:50:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 95.2 |
| f568fe01-4eef-34e2-b6c4-78a9b8ffbf53 | -10.567 | -51.3137 | 2026-09-19 11:50:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 148.2 |
| 85d2627e-2b3c-35f0-9260-789361b4695c | -11.9487 | -50.1402 | 2026-09-19 11:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 69.8 |
| 8cc63e68-a7f3-308b-a59e-a5ddbbaae89d | -11.7823 | -49.8152 | 2026-09-19 11:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 181.9 |
| bfef165f-1a58-34a3-b9f1-3dcce574ff91 | -11.9112 | -50.1016 | 2026-09-19 11:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 86.0 |
| 2309628d-f4e6-33e1-a4d8-e51c5950f67a | -12.5952 | -49.1046 | 2026-09-19 11:50:00 | GOES-19 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 103.7 |
| 3eada254-2938-36fa-908c-7c6b09988f36 | -8.7731 | -48.6868 | 2026-09-19 11:50:00 | GOES-19 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 89.5 |
| 9c12935d-eb70-3fa2-a710-d32130c372bd | -12.1339 | -46.9734 | 2026-09-19 11:50:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 78.5 |
| da54a5ff-9eaf-3d3b-9195-15f850baee76 | -10.567 | -51.3137 | 2026-09-19 12:00:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 99.8 |
| 4c4c0d66-d4d6-3431-9237-d89cd04dc1e6 | -12.6892 | -45.9629 | 2026-09-19 12:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 124.4 |
| 5a1ebc25-ccec-30cb-a745-fe896b9d7784 | -12.5952 | -49.1046 | 2026-09-19 12:00:00 | GOES-19 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 100.8 |
| 63b10288-071c-3c7a-b014-828036e6cd45 | -8.7731 | -48.6868 | 2026-09-19 12:00:00 | GOES-19 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 142.0 |
| f09894dd-3b6d-32c6-a36d-1f51427f6641 | -12.7085 | -45.96 | 2026-09-19 12:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 159.4 |
| f795daab-b72e-3a93-b990-48f5e2ed5016 | -11.2987 | -51.7449 | 2026-09-19 12:00:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 81.2 |
| ba9f5bf1-aa71-3ad9-8301-e7ba26209f05 | -11.0062 | -48.3407 | 2026-09-19 12:00:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 76.3 |
| 02f6e7da-444e-3cfe-8695-d104b6b1e513 | -10.8469 | -50.1795 | 2026-09-19 12:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 75.1 |
| 916a5f17-2531-3f26-9d04-2c43d2161e9d | -12.1339 | -46.9734 | 2026-09-19 12:00:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 76.2 |
| dd064455-3e99-36df-bb98-454ab7aea069 | -11.949 | -50.1186 | 2026-09-19 12:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 130.6 |
| 14cf2024-5fd5-3c55-b50c-e13e3b112709 | -11.0065 | -48.3187 | 2026-09-19 12:00:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 66.1 |
| 7e8620d4-0003-3bb2-bcc7-2eb72caac4b1 | -11.083 | -48.2875 | 2026-09-19 12:00:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 80.8 |
| 0fd9bf20-e405-39da-84c1-0220da3e68db | -8.7919 | -48.6851 | 2026-09-19 12:00:00 | GOES-19 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 150.4 |
| 03c6057d-bf8d-3342-968b-597dbd7e73a3 | -12.1531 | -46.9707 | 2026-09-19 12:00:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 74.8 |
| 044b6c5d-e8fa-30ba-b067-d9686ab8fcfa | -11.0608 | -49.7909 | 2026-09-19 12:00:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 69.2 |
| 0d5ef479-1a25-3210-9b85-84de4c43a3ef | -11.9109 | -50.1232 | 2026-09-19 12:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 79.9 |
| 929ac93c-7e59-36a4-ab1a-28ee35cb28d4 | -13.0173 | -46.9352 | 2026-09-19 12:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 68.0 |
| f2f71e55-fa06-38b1-8201-180b6d971c3b | -11.9487 | -50.1402 | 2026-09-19 12:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 76.2 |
| 33ab11f8-f445-30de-b1e3-1b039341136b | -11.9112 | -50.1016 | 2026-09-19 12:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 106.7 |
| d01d4d3a-9812-3c73-9acb-36ed676dbda2 | -10.8469 | -50.1795 | 2026-09-19 12:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 94.0 |
| 9a66a463-fbc2-35df-96c2-7f92d3360691 | -12.1535 | -46.9482 | 2026-09-19 12:10:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 75.8 |
| a9b46e5e-324a-384a-a98d-247853e08e35 | -9.6205 | -45.8755 | 2026-09-19 12:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 79.0 |
| b5b71a7c-7f7c-3ddf-bd5a-bc69223d9c43 | -11.3177 | -51.7429 | 2026-09-19 12:10:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 107ddaca-30f3-3a86-a926-e984cd998c5f | -12.0076 | -50.0254 | 2026-09-19 12:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 67.7 |
| 74f375b3-8b0e-308a-8780-615b3bda4021 | -10.567 | -51.3137 | 2026-09-19 12:10:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 79.0 |
| b39e0cc0-3d8c-350d-a6bb-9651bd458ff5 | -12.5952 | -49.1046 | 2026-09-19 12:10:00 | GOES-19 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 97.0 |
| 401909e1-ef36-39e4-b8a3-a64fe9447247 | -13.0173 | -46.9352 | 2026-09-19 12:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 64.8 |
| f63dfcb7-65b4-363c-8108-89383820e9e9 | -9.2377 | -46.2119 | 2026-09-19 12:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 78.7 |
| aa4d01d7-7527-3a1f-ad9c-8c9fe62fb55a | -11.0065 | -48.3187 | 2026-09-19 12:10:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 159.9 |
| eb9897b3-1441-38d6-aabb-069dc4a73aed | -12.6892 | -45.9629 | 2026-09-19 12:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 94.5 |
| 6c24728c-d8f1-37ea-8d21-129b6ead8fa3 | -11.2987 | -51.7449 | 2026-09-19 12:10:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 76.3 |
| 74fdd5fe-255b-350a-8e7a-5b545fe90c04 | -11.0062 | -48.3407 | 2026-09-19 12:10:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 155.4 |
| a94d7649-a55e-3d8d-8687-b38d408d736a | -11.318 | -51.7218 | 2026-09-19 12:10:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 77.6 |
| 12105848-b9b3-36e2-9a21-0a2a94d8130d | -9.2567 | -46.2098 | 2026-09-19 12:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 92.8 |
| 46ed30ff-bd2c-36f2-9c91-31d3fa8ca673 | -9.6016 | -45.8777 | 2026-09-19 12:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 95.2 |
| 6167aaec-2631-30eb-a43b-37b69feed233 | -11.949 | -50.1186 | 2026-09-19 12:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 110.1 |
| c895d5ba-0a09-34bb-b758-7998e833aab9 | -11.9109 | -50.1232 | 2026-09-19 12:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 88.7 |
| 7a4280b5-61f3-3210-a94c-a09ea36f3af5 | -11.9112 | -50.1016 | 2026-09-19 12:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 118.8 |
| 2a2b72b7-7645-3037-a967-bf98d4c8abf1 | -11.8746 | -47.6125 | 2026-09-19 12:10:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 84.7 |
| 79e21e67-1f8f-3167-8d11-03e7797e3546 | -11.8742 | -47.6348 | 2026-09-19 12:10:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 72.3 |
| b30e97b3-186f-367b-8633-3ec8649d86a7 | -12.5032 | -50.0508 | 2026-09-19 12:10:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 128.1 |
| bdc4e3df-9ccf-31c9-80d2-66abd92079b8 | -12.1339 | -46.9734 | 2026-09-19 12:10:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 107.1 |
| e33e5a33-6334-3e9e-ad7a-b986dbb63d97 | -7.8598 | -44.8595 | 2026-09-19 12:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 99.7 |
| dd581fc2-92a4-3e00-9326-0005b842bb34 | -8.7731 | -48.6868 | 2026-09-19 12:10:00 | GOES-19 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 95.8 |
| 523d074f-d427-369b-b716-33e03005bb47 | -12.7085 | -45.96 | 2026-09-19 12:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 173.3 |
| 38e6f553-b24b-35f4-b4a5-4f4b5e46d2e4 | -10.8279 | -50.1815 | 2026-09-19 12:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 88.5 |
| 9d439812-19e7-3331-a5f3-2d2022c9ce8b | -9.3815 | -45.381 | 2026-09-19 12:10:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 126.3 |
| c9ff71a0-28a4-3d76-aaf6-6747a0577d96 | -11.083 | -48.2875 | 2026-09-19 12:10:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 72.2 |
| d508eed1-6aa6-39e6-86c8-792880fb82e9 | -11.9487 | -50.1402 | 2026-09-19 12:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 83.4 |
| 4139d62c-844c-3da5-b5b8-f9881c8d1f25 | -12.4841 | -50.0532 | 2026-09-19 12:10:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 76.5 |
| 2755004c-e454-3409-9d50-b684051a9ba2 | -14.667 | -46.6461 | 2026-09-19 12:10:00 | GOES-19 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 72.2 |
| 65722d7a-cb8a-3c08-bb96-58b51190c03d | -12.1531 | -46.9707 | 2026-09-19 12:10:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 95.5 |
| 53e4f90d-d14d-3c6d-ae99-1078d34329c2 | -8.7919 | -48.6851 | 2026-09-19 12:10:00 | GOES-19 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 107.8 |
| b08002ca-3e95-3ec9-be41-0a55fb6db4e9 | -10.8279 | -50.1815 | 2026-09-19 12:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 125.7 |
| 73c632bd-aee9-35f9-805c-a9b30eac9baa | -9.7501 | -46.0863 | 2026-09-19 12:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 68.3 |
| 0674086d-d90b-3d0f-a5f7-f10dcfa4aad6 | -12.1531 | -46.9707 | 2026-09-19 12:20:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 99.8 |
| 0ff766e1-5b8b-372f-9332-8d648cc405f4 | -11.8746 | -47.6125 | 2026-09-19 12:20:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 76.2 |
| 6ba92ff6-23f1-30b0-81de-c870d393bde2 | -7.6354 | -44.7442 | 2026-09-19 12:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 128.9 |
| 737c9664-d4c5-3e74-8214-b510e31fa379 | -10.8469 | -50.1795 | 2026-09-19 12:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 169.6 |
| 85e45aa9-293c-3b44-8ccb-2efa3343206b | -11.8742 | -47.6348 | 2026-09-19 12:20:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 64.5 |
| 86796d03-efc5-3c53-905c-5bfaabefd0cd | -10.567 | -51.3137 | 2026-09-19 12:20:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 74.8 |
| f890be50-1aba-375d-a0b6-546cd9292842 | -12.5032 | -50.0508 | 2026-09-19 12:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 158.0 |
| f21cf90f-2369-3a90-b657-16392b79eee6 | -11.0065 | -48.3187 | 2026-09-19 12:20:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 96.1 |
| ff6f987a-47df-3c9f-8537-f1ab921475b0 | -12.7085 | -45.96 | 2026-09-19 12:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 273.0 |
| 9c147e74-bcc8-38c4-b738-e040bcbff5e8 | -11.9112 | -50.1016 | 2026-09-19 12:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 165.9 |
| 663e7db5-505d-30bc-9621-d15a7f1fa09e | -10.8282 | -50.1601 | 2026-09-19 12:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 93.9 |
| 2615488f-9448-31c5-aeb5-a272e7314434 | -11.9487 | -50.1402 | 2026-09-19 12:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 106.9 |
| 24323585-40fe-3dc8-86a1-fcd1412ef119 | -14.667 | -46.6461 | 2026-09-19 12:20:00 | GOES-19 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 88.9 |
| 46085617-0e38-3a52-b8d5-a14a2fe19680 | -11.0062 | -48.3407 | 2026-09-19 12:20:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 117.5 |
| 475e508e-cbd8-34ec-9756-1d0532888b98 | -8.7919 | -48.6851 | 2026-09-19 12:20:00 | GOES-19 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 91.0 |
| 39cbcaad-9d12-3625-b7d6-81bfe915fc21 | -9.3815 | -45.381 | 2026-09-19 12:20:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 100.4 |
| 657d76f8-1143-35ad-8b64-46b6e7b4791f | -11.0608 | -49.7909 | 2026-09-19 12:20:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 101.2 |
| 6a94dd41-d803-3258-94f9-a766eff15c55 | -12.1535 | -46.9482 | 2026-09-19 12:20:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 81.1 |
| 30bf0d09-20fa-3fdf-99d4-f3f575a2f30c | -11.9109 | -50.1232 | 2026-09-19 12:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 116.2 |


[Clique aqui para ver as próximas entradas](README105.md)
