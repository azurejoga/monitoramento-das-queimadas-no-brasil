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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 063c48c2-0118-356a-956d-8e2510fc26b4 | -6.49021 | -56.22282 | 2025-07-30 00:48:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 16.1 |
| 7d14de23-f9e8-3611-8a26-b3214a6b81d5 | -6.67005 | -49.80523 | 2025-07-30 00:48:00 | TERRA_M-M | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| f33cc712-b9ce-3a74-babe-681d18407135 | -9.2262 | -48.60089 | 2025-07-30 00:48:00 | TERRA_M-M | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 11.9 |
| fb2ef38d-bdf8-3099-91ef-920892f261b6 | -4.89778 | -44.95744 | 2025-07-30 00:48:00 | TERRA_M-M | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 32.7 |
| 32f85bd8-ab0c-3d6d-b574-81b3ee5e10ad | -6.53251 | -56.19645 | 2025-07-30 00:48:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 27.8 |
| ba58b773-df00-3a72-8e5a-c58b36104868 | -8.68052 | -51.20697 | 2025-07-30 00:48:00 | TERRA_M-M | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 891b9a6b-6a2e-3585-a064-0cd1e5c98dd7 | -9.15461 | -49.84541 | 2025-07-30 00:48:00 | TERRA_M-M | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 35.6 |
| 5d9ecbf8-421c-34f5-8aba-a4cfa84ddd2d | -7.03684 | -55.50432 | 2025-07-30 00:48:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 39f1d62e-89ae-362e-b3b7-8d04e24b4f9b | -9.45813 | -57.85624 | 2025-07-30 00:48:00 | TERRA_M-M | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 20.6 |
| 688856a3-7eae-38c7-9bc1-012df9feffb9 | -6.38985 | -53.36283 | 2025-07-30 00:48:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 6ff5f3e6-55f1-3d53-85b3-6fbdee762c6d | -8.50932 | -43.30418 | 2025-07-30 00:48:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 38.1 |
| 3db6690a-6b56-3e01-9f57-17d4bd97b85e | -8.33263 | -54.76025 | 2025-07-30 00:48:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 50ff99d4-3d16-37f7-a9e5-d225f5e81474 | -8.02897 | -47.68125 | 2025-07-30 00:48:00 | TERRA_M-M | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| f36cbd40-e02e-3415-af07-07f09d9c80a2 | -10.52777 | -42.55453 | 2025-07-30 00:48:00 | TERRA_M-M | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 23.5 |
| 56f102a9-0601-3d51-bb42-d0489e0e48da | -6.49752 | -56.19165 | 2025-07-30 00:48:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 25.2 |
| 0da3d226-6694-3178-bb04-1ab9b57020f1 | -9.04798 | -45.07271 | 2025-07-30 00:48:00 | TERRA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 44.3 |
| 4754f153-9ecf-36d5-be4e-18ab6c7451bc | -9.02473 | -47.97974 | 2025-07-30 00:48:00 | TERRA_M-M | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 81147bb4-3b73-3055-b718-6806c540c6cf | -7.73498 | -51.09485 | 2025-07-30 00:48:00 | TERRA_M-M | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| d89fd911-0dfd-356f-8f95-97d9345ebb55 | -11.3468 | -51.24746 | 2025-07-30 00:48:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 7.8 |
| e2516282-572e-375f-af36-28f6381d56c1 | -6.49869 | -56.2009 | 2025-07-30 00:48:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 41.3 |
| 9abe3777-ab30-30c2-bf5a-bd76bccbb1e7 | -10.61275 | -45.23014 | 2025-07-30 00:48:00 | TERRA_M-M | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 32.0 |
| b53700c9-2f01-3318-922d-62c907eb794f | -9.26311 | -50.22744 | 2025-07-30 00:48:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 17.7 |
| 9b52f997-18ac-3fe1-ba8f-5264fb1cb9de | -4.65398 | -43.14937 | 2025-07-30 00:48:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 47.4 |
| 855c6be4-29fa-369f-b0f2-cfb4f322adb8 | -9.16486 | -49.85322 | 2025-07-30 00:48:00 | TERRA_M-M | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| e7c4c3a4-f8d9-32ae-9408-0127c06c6406 | -6.52314 | -56.21281 | 2025-07-30 00:48:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 59.4 |
| c3bfd519-3a12-38ad-b136-4344d9f5bc79 | -11.45951 | -45.11887 | 2025-07-30 00:48:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 121.5 |
| 09afa8bb-c3ef-376b-94e6-ed52d0ae4b04 | -6.51186 | -56.21433 | 2025-07-30 00:48:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 33.9 |
| 976d6b92-2cb5-304a-a126-303568a78392 | -9.63157 | -48.54988 | 2025-07-30 00:48:00 | TERRA_M-M | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 32.8 |
| f6a8d16c-90bd-3653-95bd-4602e3ba2b94 | -4.37759 | -49.03431 | 2025-07-30 00:48:00 | TERRA_M-M | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 49.7 |
| 3dbdcb14-62d5-3ded-a5d6-88d19ca1f570 | -6.89452 | -45.24955 | 2025-07-30 00:48:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 25.2 |
| b7bf86ab-4721-3862-9a4d-a4b3c8a7bd63 | -11.32592 | -48.92197 | 2025-07-30 00:48:00 | TERRA_M-M | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 33.2 |
| 2d9d90be-f948-3889-ab77-7ac9a5cbbd6f | -6.56635 | -56.1921 | 2025-07-30 00:48:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 22.8 |
| fdcbde2a-b045-3840-8683-12a2b7ba5876 | -11.45704 | -45.10301 | 2025-07-30 00:48:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 55910087-ac7a-339b-8a9b-5ef33d8e8178 | -8.39504 | -48.98447 | 2025-07-30 00:48:00 | TERRA_M-M | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 77c9ebba-a9f1-36e2-942d-55e7619b49cb | -6.5108 | -56.20506 | 2025-07-30 00:48:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 48.1 |
| 6cbc39c6-7e2e-3b81-961b-db3c0ca647b5 | -10.51622 | -44.89263 | 2025-07-30 00:48:00 | TERRA_M-M | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 1e37f15e-f430-39cd-9beb-e85c83f8a812 | -10.70042 | -48.86457 | 2025-07-30 00:48:00 | TERRA_M-M | OLIVEIRA DE FÁTIMA | TOCANTINS | Brasil | 1715507 | 17 | 33 | nan | nan | nan | Cerrado | 21.3 |
| 81b0889a-b411-301f-b52d-20531c4f6c7f | -4.65297 | -43.12436 | 2025-07-30 00:48:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 141.8 |
| bce2e84e-cc72-3436-85e0-73408cfb19c5 | -8.95984 | -46.73721 | 2025-07-30 00:48:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 23.4 |
| 9037fd3d-58cb-302e-9c86-84374aad32ae | -7.94819 | -44.08574 | 2025-07-30 00:48:00 | TERRA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 30.4 |
| 338e0326-48bb-3ca5-9f05-4b16f3f1df8c | -3.513 | -43.25098 | 2025-07-30 00:48:00 | TERRA_M-M | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 29.6 |
| 065238ab-9b57-352c-a714-39c159c0fde2 | -6.89917 | -45.26088 | 2025-07-30 00:48:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 27.7 |
| 068f5209-df6a-35f6-9fb9-59eb8b2d4f14 | -8.95591 | -46.74438 | 2025-07-30 00:48:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 31.2 |
| 01dee966-260b-3767-8929-d83e93d55b23 | -9.74692 | -48.57817 | 2025-07-30 00:48:00 | TERRA_M-M | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 19.2 |
| 31c1ca81-af72-32ad-abc5-fbf127c6e637 | -8.95394 | -46.73101 | 2025-07-30 00:48:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 0b252c77-3b96-3bbc-9c7d-6f013f49a48a | -9.73757 | -48.57963 | 2025-07-30 00:48:00 | TERRA_M-M | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 3c90791a-e809-3b6e-b3ad-413c8f064efa | -8.96189 | -46.75048 | 2025-07-30 00:48:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 5fad77b2-508a-3b14-b7aa-a1cedd03f119 | -8.32471 | -54.75437 | 2025-07-30 00:48:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 4bb00192-e899-32c9-8caf-82bfb64edb1f | -11.46747 | -45.11086 | 2025-07-30 00:48:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 258.7 |
| d8602188-1b75-3552-9cee-25614af42043 | -8.51301 | -43.29761 | 2025-07-30 00:48:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 28.8 |
| 0bae1961-462a-373c-97fb-e62ea6a74997 | -7.84901 | -46.72665 | 2025-07-30 00:48:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 2df5a415-3c4b-345a-985a-9a1f20321cba | -6.45422 | -53.36773 | 2025-07-30 00:48:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 1f731558-5ddb-32bd-9f72-230c85d8b381 | -9.17913 | -48.84893 | 2025-07-30 00:48:00 | TERRA_M-M | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 16.3 |
| c1ddefe2-16cb-37a4-b353-a477c2aa8097 | -7.86188 | -46.73871 | 2025-07-30 00:48:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 34.8 |
| 759f8773-5030-3ef0-9bce-db57beffec27 | -7.63213 | -56.72951 | 2025-07-30 00:48:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 17.1 |
| 6de885d6-e04d-3f8a-aa07-fc0b86195344 | -6.45289 | -53.35789 | 2025-07-30 00:48:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| a1754874-43e3-3f76-8299-1a8dd665a2f5 | -6.50879 | -56.19023 | 2025-07-30 00:48:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 31.7 |
| 21230647-5dd4-346b-b7f8-bfd05f5ed298 | -10.70958 | -48.8632 | 2025-07-30 00:48:00 | TERRA_M-M | OLIVEIRA DE FÁTIMA | TOCANTINS | Brasil | 1715507 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 3e50f50c-cb7f-30db-9c3b-8c3a0c4ee8c0 | -9.40136 | -45.49723 | 2025-07-30 00:48:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 17.7 |
| ae9e3ea7-f967-3180-9385-443cfc4038ec | -9.26437 | -50.23644 | 2025-07-30 00:48:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 8fa5427b-c24b-3493-bf87-f895ee81fd6c | -9.22889 | -50.04818 | 2025-07-30 00:48:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| a4e5573e-1ce2-3fa9-8144-941ea299e3be | -8.51324 | -43.32903 | 2025-07-30 00:48:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 40.5 |
| da61f0ac-b4a0-38c8-b9e9-b8b032588e6b | -11.3273 | -48.93147 | 2025-07-30 00:48:00 | TERRA_M-M | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 71f1c05f-141f-30ba-bc37-bd97cb20f9f3 | -7.85547 | -46.74736 | 2025-07-30 00:48:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| bcb29996-3941-3598-9898-544518d30c1c | -10.61527 | -45.24615 | 2025-07-30 00:48:00 | TERRA_M-M | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 140.1 |
| 8db9a9c3-44cc-35c1-bb6b-286c82263ab5 | -8.88921 | -47.34165 | 2025-07-30 00:48:00 | TERRA_M-M | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 10.7 |
| f4c6577b-b932-3be0-a09f-0accaaa00419 | -7.85986 | -46.7249 | 2025-07-30 00:48:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 7c588fbc-fe92-330a-b679-cb01ac8feb81 | -6.40777 | -53.37413 | 2025-07-30 00:48:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| b6e80937-2551-349d-bd94-41981bf8cc99 | -11.46855 | -45.1008 | 2025-07-30 00:48:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 27.3 |
| e1d82672-4a05-3673-8981-1b0de6bd46f8 | -7.38405 | -48.1685 | 2025-07-30 00:48:00 | TERRA_M-M | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| f325ce8a-91bf-3ca1-aa0f-4a6b6cff6592 | -6.50997 | -56.19947 | 2025-07-30 00:48:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 76.8 |
| d65e3742-aa38-3d91-93d9-540967e27f9b | -7.85103 | -46.74043 | 2025-07-30 00:48:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 28.8 |
| 1dfc174d-f3ff-3d3e-be76-4c462c36dc8c | -9.6301 | -48.53977 | 2025-07-30 00:48:00 | TERRA_M-M | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 19921e0b-5bf4-3ef4-ad88-fdf911ae9c34 | -10.62689 | -45.24436 | 2025-07-30 00:48:00 | TERRA_M-M | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 63.4 |
| b7a2b71c-36fa-30d4-96e7-0242ce32798a | -6.49951 | -56.20647 | 2025-07-30 00:48:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 48.5 |
| a5e8c64e-9fc6-362a-acb0-04660c969eaf | -8.3351 | -54.75308 | 2025-07-30 00:48:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 7c4c5aeb-bf95-3902-9f4a-2fd9d620b200 | -8.01887 | -47.68279 | 2025-07-30 00:48:00 | TERRA_M-M | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 42.4 |
| 47e64384-688e-3b2d-92a3-9fdf24eb05d0 | -6.55507 | -56.19357 | 2025-07-30 00:48:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 19.4 |
| 1ce6f603-696e-360b-8420-1aec0e981390 | -11.47101 | -45.11671 | 2025-07-30 00:48:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 212.4 |
| 16d33b4f-364a-3960-951e-451dfc2e2846 | -10.28322 | -46.93282 | 2025-07-30 00:48:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 78ee4fdf-329b-3706-be2e-ab7c1fc1e7c9 | -11.5307 | -44.267 | 2025-07-30 00:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 59.7 |
| 5baa032b-6b4d-3538-89a0-475507e4af6e | -11.4776 | -45.1099 | 2025-07-30 00:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 139.7 |
| afe4a248-14e4-354e-8981-cfd90b200947 | -11.5503 | -44.2407 | 2025-07-30 00:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 57.2 |
| 45c2e277-9e4a-3670-9ab3-d38a6f72bc4a | -10.6169 | -45.2512 | 2025-07-30 00:50:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 79.4 |
| 75acaca7-7767-3ff3-85e4-e0d1919a20bb | -15.7174 | -41.9272 | 2025-07-30 00:50:00 | GOES-19 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 47.0 |
| e0cc4c6b-da72-3720-8813-749522c05299 | -9.4387 | -40.3419 | 2025-07-30 00:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 64.9 |
| 21254cd9-875e-3b5c-a8cd-63e3a527c1b9 | -10.6172 | -45.2282 | 2025-07-30 00:50:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 84.3 |
| 3dc58cc3-0b99-34c7-8e77-18398b20fabc | -17.4945 | -46.7321 | 2025-07-30 00:50:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 62.8 |
| 0e5806da-78f5-3f9a-a9d0-322ac497392b | -11.4584 | -45.1126 | 2025-07-30 00:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 133.8 |
| 520ca4a7-9063-32b5-b99b-d674b755ac3e | -2.8923 | -48.2546 | 2025-07-30 00:50:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 8b152254-2cc0-3c70-be7b-0bf8ca81bae8 | -4.6509 | -43.1337 | 2025-07-30 00:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 91.9 |
| 05394752-5f4e-3d0b-9aa1-b7705a188b10 | -2.9108 | -48.254 | 2025-07-30 00:50:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 84.9 |
| 40c7d5cf-9972-3f83-bae7-0eaf4cfcf250 | -4.6511 | -43.1104 | 2025-07-30 00:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 93.9 |
| ca562603-07ab-3b9c-9723-327b682fdd3c | -3.57983 | -52.54599 | 2025-07-30 00:50:00 | TERRA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 182768ce-fdfb-34fe-923b-85faa0720c32 | -2.90702 | -48.2545 | 2025-07-30 00:50:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 117.0 |
| b65a5522-c948-345a-a612-713ce4967813 | -3.17929 | -48.80871 | 2025-07-30 00:50:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 5151e8b2-3be8-3174-b7ff-c8edccb42532 | -2.91495 | -48.67963 | 2025-07-30 00:50:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| c168b78a-a6fb-35de-bf3f-ba87178d929e | -2.81031 | -48.66413 | 2025-07-30 00:50:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| b7b6f65e-413d-3eb0-b139-c33546234f73 | -2.91752 | -48.25304 | 2025-07-30 00:50:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 01a259b3-c56b-3d64-873b-b4563427bcac | -2.91574 | -48.24031 | 2025-07-30 00:50:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |


[Clique aqui para ver as próximas entradas](README8.md)
