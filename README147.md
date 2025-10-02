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

## Dados Diários - Página 147

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0f333d28-f844-358d-b999-32132755f36e | -6.95523 | -52.55396 | 2025-10-02 12:36:00 | TERRA_M-T | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| ea189501-f808-33cb-af27-ddc2a5db2a22 | -8.68579 | -47.69801 | 2025-10-02 12:36:00 | TERRA_M-T | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 30.7 |
| 01fa6687-9d59-3eb5-a021-e833a53a898f | -9.90927 | -47.71423 | 2025-10-02 12:36:00 | TERRA_M-T | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 31.0 |
| 7b3e76de-b16d-3de3-8445-24a639085158 | -9.34077 | -45.73373 | 2025-10-02 12:36:00 | TERRA_M-T | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 73.6 |
| 42e89405-1f5a-3a00-86d9-5f182f0ddf0d | -4.37719 | -43.01772 | 2025-10-02 12:36:00 | TERRA_M-T | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 31.9 |
| a569c6e7-1a5c-32d2-baa0-5ddce02a3aee | -10.11449 | -50.28344 | 2025-10-02 12:36:00 | TERRA_M-T | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 36.3 |
| c0d5779f-1edb-3dc3-b1bc-dc5cbab2327c | -9.42704 | -46.30601 | 2025-10-02 12:36:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 24.8 |
| 09dd375b-7ddd-3cb8-aca2-bdd25ab67390 | -6.7229 | -44.14977 | 2025-10-02 12:36:00 | TERRA_M-T | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 51.9 |
| e750569b-3970-3b25-85a1-06b36ccd5983 | -6.77639 | -45.59116 | 2025-10-02 12:36:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 46.0 |
| 3b81b4a0-6450-3904-890f-051e10cb5144 | -5.99571 | -44.57985 | 2025-10-02 12:36:00 | TERRA_M-T | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 45.0 |
| 5d914db5-85df-3049-b366-20d3b6fbe229 | -5.79587 | -43.07891 | 2025-10-02 12:36:00 | TERRA_M-T | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 43.0 |
| 2338095a-2a84-384f-9058-f6aa5215e4e1 | -10.21343 | -48.2121 | 2025-10-02 12:36:00 | TERRA_M-T | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 30.9 |
| c8f33ff8-41dc-3084-a7c6-b8d5ad911aa0 | -10.21195 | -48.2051 | 2025-10-02 12:36:00 | TERRA_M-T | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 78.9 |
| a3048d36-6e6c-3da7-9791-63169855d556 | -7.46054 | -46.46509 | 2025-10-02 12:36:00 | TERRA_M-T | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 19.9 |
| ae1d1192-45c2-38ce-abe1-7eddc943dacf | -6.78879 | -45.59787 | 2025-10-02 12:36:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 29.3 |
| aa6dd019-a650-304a-a019-08b369eb8c9f | -8.62231 | -54.98779 | 2025-10-02 12:36:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| dde3a38d-890e-369f-ba38-6050bf58cbc8 | -8.14801 | -50.24789 | 2025-10-02 12:36:00 | TERRA_M-T | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| c3a5012b-dfec-312d-83d6-e1c266adf529 | -10.82453 | -46.61587 | 2025-10-02 12:36:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 57.1 |
| 0ac5be72-29d1-3f84-b126-23baac2cda0d | -9.80155 | -47.84089 | 2025-10-02 12:36:00 | TERRA_M-T | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 6a1e4d00-724e-3bde-b832-5877ed4da1ed | -5.34261 | -43.77139 | 2025-10-02 12:36:00 | TERRA_M-T | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 409.7 |
| 276189e3-1d1e-3128-b8bb-5e114bf5d474 | -6.77451 | -45.30036 | 2025-10-02 12:36:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 59.6 |
| 8d198907-f403-3736-9c46-dbe51b6fff49 | -6.35248 | -49.32373 | 2025-10-02 12:36:00 | TERRA_M-T | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 19.7 |
| 1b87b4f1-50f3-3e67-ad93-26d770bfaa83 | -5.75846 | -43.49057 | 2025-10-02 12:36:00 | TERRA_M-T | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 41.2 |
| d1e3c14f-d413-3395-af61-14f40abe11a1 | -9.07616 | -46.71142 | 2025-10-02 12:36:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 76.2 |
| 5126f9c6-fd72-3e45-b8cd-cbfecfdd76be | -10.21529 | -48.19717 | 2025-10-02 12:36:00 | TERRA_M-T | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 62.2 |
| e01e06f5-f48d-3631-a887-9285507f2607 | -8.21425 | -47.00847 | 2025-10-02 12:36:00 | TERRA_M-T | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 31.6 |
| d0e81c77-5ada-3e23-a7c0-3656e2bffe1d | -9.33048 | -45.93789 | 2025-10-02 12:36:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 46.3 |
| 8e8d5a59-aace-3bd6-9d56-43c7f7254946 | -9.81583 | -48.25757 | 2025-10-02 12:36:00 | TERRA_M-T | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 50.8 |
| a4a18daf-54e0-3401-b5bf-b1127dc977bd | -9.83399 | -48.28712 | 2025-10-02 12:36:00 | TERRA_M-T | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 23.2 |
| 878bb7a4-0e11-3487-875f-f25c36bb629a | -9.64807 | -48.2222 | 2025-10-02 12:36:00 | TERRA_M-T | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 91b067b2-c414-373a-aa8a-f48e58bca470 | -6.78927 | -45.59237 | 2025-10-02 12:36:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 34.8 |
| 0d47b50c-2702-3e7a-b56c-41be83b59f84 | -6.72074 | -44.14265 | 2025-10-02 12:36:00 | TERRA_M-T | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 42.4 |
| 5709802e-0cdd-3bd6-93ee-0aa42b029414 | -6.23681 | -45.32143 | 2025-10-02 12:36:00 | TERRA_M-T | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 354.6 |
| 8afbbaf5-93df-3b98-a676-113a37438aec | -7.81294 | -47.63159 | 2025-10-02 12:36:00 | TERRA_M-T | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 18.2 |
| ef8c4200-7eb3-3255-a996-0ba710151ec4 | -9.8852 | -46.92056 | 2025-10-02 12:36:00 | TERRA_M-T | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 51.7 |
| d4ece79a-3ab1-372f-a154-a50484c8fa51 | -8.51924 | -47.82495 | 2025-10-02 12:36:00 | TERRA_M-T | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 25.1 |
| 3b8911e6-0f0e-38a3-8a22-7981c2f843aa | -8.62076 | -54.97076 | 2025-10-02 12:36:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 44a45769-ebdb-3ddd-980f-14d88491b3fc | -8.52784 | -47.23508 | 2025-10-02 12:36:00 | TERRA_M-T | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 19.8 |
| f096885b-6fbb-321d-bc08-c893dd7559a1 | -7.81188 | -47.62569 | 2025-10-02 12:36:00 | TERRA_M-T | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 120663a9-6816-3875-b725-f3736eb09e46 | -10.22298 | -48.20607 | 2025-10-02 12:36:00 | TERRA_M-T | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 66.3 |
| e9171aed-bb85-32c6-844f-665723cdab03 | -8.36189 | -48.6753 | 2025-10-02 12:36:00 | TERRA_M-T | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 9.6 |
| ad828f0d-b97d-3985-8c49-2fa0c695c419 | -3.48603 | -48.95689 | 2025-10-02 12:36:00 | TERRA_M-T | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 381bb9e1-a2d0-30f0-bb5b-021400d82218 | -9.00177 | -51.39122 | 2025-10-02 12:36:00 | TERRA_M-T | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 6acc91e5-dd3c-3508-91cb-ecf0efafaf6c | -10.01537 | -50.26415 | 2025-10-02 12:36:00 | TERRA_M-T | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 17.9 |
| ff3604c4-ed1f-3c34-b782-5e775704b183 | -9.05457 | -46.64876 | 2025-10-02 12:36:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 42.1 |
| 761c98b6-d1b2-3cdb-9e84-3057c3430a53 | -7.9016 | -47.29897 | 2025-10-02 12:36:00 | TERRA_M-T | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 18.8 |
| 8e136612-4abc-360c-8b59-20e3817dc1cf | -8.51731 | -47.24319 | 2025-10-02 12:36:00 | TERRA_M-T | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 37.9 |
| cb0fab64-c67a-3913-83bc-f9b1b4291667 | -9.00891 | -46.71432 | 2025-10-02 12:36:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 20.5 |
| 9553f947-1504-35d4-a20a-03967198d52d | -7.88819 | -47.31329 | 2025-10-02 12:36:00 | TERRA_M-T | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 50.1 |
| 837301f9-e7ee-30e7-b767-9904fba41b66 | -8.21637 | -46.99213 | 2025-10-02 12:36:00 | TERRA_M-T | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 23.6 |
| 723d11db-b352-3ded-98e2-04a3b1632cdf | -9.64986 | -48.20868 | 2025-10-02 12:36:00 | TERRA_M-T | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 2017a097-f6e1-37bb-8732-c5c60ebda544 | -9.8376 | -48.26004 | 2025-10-02 12:36:00 | TERRA_M-T | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 55.3 |
| 1163d872-195b-3bc4-aed7-2ba93707ae85 | -9.34171 | -45.94522 | 2025-10-02 12:36:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 36.2 |
| 3e9f8625-ec3c-39f3-916c-617e058ccc98 | -9.45492 | -47.95551 | 2025-10-02 12:36:00 | TERRA_M-T | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 3ecf0531-9da7-3b3f-b1db-a50369cd8c58 | -8.62393 | -54.97725 | 2025-10-02 12:36:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| c93577a1-38f8-3697-87f9-f68da2e2f34b | -8.6192 | -54.98131 | 2025-10-02 12:36:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| ec92e78c-ee8e-3ea8-9a60-6fb255e9d6d3 | -9.44386 | -47.95411 | 2025-10-02 12:36:00 | TERRA_M-T | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 7b89a718-42d5-3d72-ac08-a3191d910b76 | -9.33363 | -45.70533 | 2025-10-02 12:36:00 | TERRA_M-T | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 54.6 |
| 504c7723-64ba-35ca-abda-4d85a3bbdbeb | -2.92327 | -48.31223 | 2025-10-02 12:36:00 | TERRA_M-T | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 26.6 |
| c50cebc8-c5b3-3a21-86ce-0463543db131 | -9.92212 | -47.70958 | 2025-10-02 12:36:00 | TERRA_M-T | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 14.4 |
| c004fa9f-aefa-3a3c-a696-81dd45fc3842 | -9.34407 | -45.72892 | 2025-10-02 12:36:00 | TERRA_M-T | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 34.1 |
| 0ad35644-2f8c-304c-aece-77ac7fe50f5a | -8.14664 | -50.25777 | 2025-10-02 12:36:00 | TERRA_M-T | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 39b9c58a-d2e0-3548-bdcc-292364d4e19f | -8.51734 | -47.83907 | 2025-10-02 12:36:00 | TERRA_M-T | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 9ba21f3a-8b47-374c-a14f-d837de0f30d7 | -9.3433 | -45.71269 | 2025-10-02 12:36:00 | TERRA_M-T | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 133.3 |
| 3f3e0fab-b9f2-3d42-a3ba-e17485f9cdb0 | -10.22267 | -48.22724 | 2025-10-02 12:36:00 | TERRA_M-T | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 9e9b3721-3bb3-3579-be16-06855704ccc5 | -7.75502 | -46.21315 | 2025-10-02 12:36:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 22.9 |
| 420aea1d-769d-3c9f-85cd-788d7f80abd8 | -10.80176 | -44.2431 | 2025-10-02 12:36:00 | TERRA_M-T | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 62.7 |
| 631f4fc5-fd57-3c36-8ca4-f04a667fc541 | -8.55787 | -44.66247 | 2025-10-02 12:36:00 | TERRA_M-T | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 60.7 |
| ced770a5-d44a-336d-8981-80895fd5a7a7 | -10.19446 | -45.388 | 2025-10-02 12:36:00 | TERRA_M-T | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 25.6 |
| 92b7bd3e-2954-329d-b21c-ef12552bf371 | -10.30139 | -48.24186 | 2025-10-02 12:36:00 | TERRA_M-T | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 20.9 |
| 4e15a1eb-dbf6-36ec-aaf7-ebdd4b50cbfd | -8.72259 | -47.14343 | 2025-10-02 12:36:00 | TERRA_M-T | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 9daf7a4e-3a79-372f-b2e2-a6576517ce11 | -9.92488 | -43.73546 | 2025-10-02 12:36:00 | TERRA_M-T | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 300.8 |
| c61d60fe-c2e1-30b9-b2c8-95950c9c31d4 | -4.28969 | -44.93077 | 2025-10-02 12:36:00 | TERRA_M-T | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Amazônia | 19.7 |
| 94ede028-3694-342b-a6f9-81a7b6794067 | -6.7913 | -45.57779 | 2025-10-02 12:36:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 30.5 |
| 133da731-52e6-35c8-ad39-daaf79de12bc | -8.20252 | -47.00729 | 2025-10-02 12:36:00 | TERRA_M-T | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 36.6 |
| a60f1799-99af-39d4-9d21-240e5664cbe1 | -9.41297 | -47.56706 | 2025-10-02 12:36:00 | TERRA_M-T | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 221.9 |
| 8a7f7c1f-0bb9-3f65-8ec7-b1a061c8329c | -9.45453 | -47.60361 | 2025-10-02 12:36:00 | TERRA_M-T | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 7218989e-206c-37e3-b8fd-78a67a43abbf | -8.90448 | -46.62291 | 2025-10-02 12:36:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 34.9 |
| 98b3bebc-08d4-362a-a2b5-8abec237fd9b | -9.34675 | -45.70792 | 2025-10-02 12:36:00 | TERRA_M-T | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 47.6 |
| 3ff63721-67a9-3a72-ac96-c39461130eb3 | -7.74014 | -46.23135 | 2025-10-02 12:36:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 27.8 |
| 2bcf3abb-613f-35c8-b5c5-9d1d8398511d | -9.8357 | -48.27422 | 2025-10-02 12:36:00 | TERRA_M-T | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 17.3 |
| d1809fe8-9f44-314a-93cd-025fae86ecd0 | -7.78918 | -42.50898 | 2025-10-02 12:36:00 | TERRA_M-T | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 172.8 |
| 450ef6e6-89ed-363e-9d95-b8eda2904923 | -15.31926 | -45.05544 | 2025-10-02 12:38:00 | TERRA_M-T | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 39.0 |
| 912ba38e-aa79-3928-9c89-4fd90e72a631 | -15.31139 | -46.29118 | 2025-10-02 12:38:00 | TERRA_M-T | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 60.0 |
| 7936e09c-ebd2-3bd4-ba86-5bc13b0dedc3 | -11.05807 | -46.61888 | 2025-10-02 12:38:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 63.1 |
| 55834e9a-8610-3f61-9e8d-d717b67389b3 | -16.18418 | -45.16642 | 2025-10-02 12:38:00 | TERRA_M-T | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 37.5 |
| 3e7379af-72fd-3bb5-8433-72d882e7ab6b | -13.08864 | -47.08235 | 2025-10-02 12:38:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 14.5 |
| ab975146-360c-3d93-8dd2-79b88cc94c3c | -13.31391 | -47.582 | 2025-10-02 12:38:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 28.6 |
| 55843634-8f8a-3924-aed6-e33a36f15ab5 | -14.31162 | -45.98164 | 2025-10-02 12:38:00 | TERRA_M-T | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 47.2 |
| d183f238-db38-3bfb-944b-ae5afe48ef1d | -14.37525 | -45.97066 | 2025-10-02 12:38:00 | TERRA_M-T | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 70.7 |
| 3e1cf99d-c889-3e48-bfac-6dfaa4cf6f40 | -15.02291 | -55.27763 | 2025-10-02 12:38:00 | TERRA_M-T | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 3217ac6a-2448-39a4-aef7-185f719168b9 | -13.04984 | -49.15047 | 2025-10-02 12:38:00 | TERRA_M-T | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 7f80fc7c-28e2-3581-a8dc-52ca58307a10 | -13.96577 | -48.12704 | 2025-10-02 12:38:00 | TERRA_M-T | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 27.7 |
| d1e463c5-80ed-3878-a757-c2953ae2808b | -15.35578 | -47.07841 | 2025-10-02 12:38:00 | TERRA_M-T | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 24.6 |
| f3694443-86ec-3113-a2a2-3a919dc35251 | -14.4894 | -48.42596 | 2025-10-02 12:38:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 23.4 |
| f92b74e9-04da-3456-8de5-ce781a6c7712 | -12.28939 | -45.38196 | 2025-10-02 12:38:00 | TERRA_M-T | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 47.8 |
| 39be2565-dd9c-3859-aa7d-f0d87141cf30 | -14.20026 | -46.15895 | 2025-10-02 12:38:00 | TERRA_M-T | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 233.1 |
| b0c21cf6-c1c4-3ec6-8828-06fc71b4a3b8 | -13.18057 | -47.82213 | 2025-10-02 12:38:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 65.3 |
| 04592174-5738-368c-b596-636a5b5f3ba5 | -13.39907 | -47.78243 | 2025-10-02 12:38:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 19.6 |
| d718afbb-9411-337e-94b2-c911e2e3a77a | -13.75036 | -48.00269 | 2025-10-02 12:38:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 22.4 |


[Clique aqui para ver as próximas entradas](README148.md)
