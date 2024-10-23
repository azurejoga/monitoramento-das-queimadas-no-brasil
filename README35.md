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

## Dados Diários - Página 35

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 729a6007-688e-33dd-9341-1048eaf3435f | -4.12864 | -46.86218 | 2024-10-23 04:51:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4058f25e-b441-31e7-93a1-2f778fbddf07 | -4.07133 | -47.13538 | 2024-10-23 04:51:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0621183b-00c2-3bd7-b5d3-03b7a35013d4 | -3.98326 | -46.47184 | 2024-10-23 04:51:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b2c491cb-12d3-3501-831a-854e32e5d2c5 | -3.97905 | -46.47148 | 2024-10-23 04:51:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7893717c-3dca-3e49-b291-8bf65d236947 | -3.9618 | -46.38617 | 2024-10-23 04:51:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d124cf96-fba9-3520-96f3-44bade70db9c | -3.85116 | -46.4886 | 2024-10-23 04:51:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| de32eb67-cd8d-3d7d-91f6-be0b670d2f0a | -3.83045 | -46.931 | 2024-10-23 04:51:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 44ca4f3d-9ff8-31bd-8529-de24a420c221 | -3.8264 | -46.93047 | 2024-10-23 04:51:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9a08efb4-d3d0-3ade-81fa-222d242c38b3 | -3.82341 | -46.92298 | 2024-10-23 04:51:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0345f56a-e0cd-3466-b812-ac14427c5e46 | -3.81938 | -46.92232 | 2024-10-23 04:51:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3b89bd98-f076-3f8f-bfc9-fa5a69db6909 | -3.81536 | -46.92156 | 2024-10-23 04:51:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f36b0d5f-707c-3f75-a781-c03916559606 | -4.97592 | -46.73069 | 2024-10-23 04:51:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 492d72f3-a268-3935-833d-8e5823af3818 | -4.76729 | -46.61933 | 2024-10-23 04:51:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 6.4 |
| b9a32310-485c-3e20-8a20-8d7ef6256e67 | -4.76674 | -46.62313 | 2024-10-23 04:51:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 82eda344-9c40-356c-b713-a5be0091e1af | -4.76619 | -46.62692 | 2024-10-23 04:51:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ba8bca01-df5d-3e44-b175-f213ada8b036 | -4.76575 | -46.61969 | 2024-10-23 04:51:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 010bb0a0-2201-3087-bbaa-67ccb60a07a3 | -4.76518 | -46.62348 | 2024-10-23 04:51:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 1f96b6cc-93bc-3a3a-985b-195c5cdc9a1e | -4.7646 | -46.62725 | 2024-10-23 04:51:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 17d3136b-245f-303b-968e-964dbe363611 | -4.7631 | -46.61877 | 2024-10-23 04:51:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 847a3df6-aba9-373e-a094-72bde3ef1662 | -4.76255 | -46.62255 | 2024-10-23 04:51:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 4eab9477-110b-3e89-944d-ccd819011101 | -4.76201 | -46.62631 | 2024-10-23 04:51:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e5a4bce9-4929-3578-9214-752f9ee3ece3 | -4.76156 | -46.61914 | 2024-10-23 04:51:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 5.7 |
| f084ce06-373e-3daf-96a1-c8094d568948 | -4.76099 | -46.62291 | 2024-10-23 04:51:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 5.7 |
| bb15c316-2fe6-360b-adef-c4b4fc8958b7 | -4.76042 | -46.62666 | 2024-10-23 04:51:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 548dc45b-ce33-3c0b-abeb-7ee41f546611 | -4.75891 | -46.61818 | 2024-10-23 04:51:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 8945122f-038c-35e6-9f7e-a61eb4a10ab0 | -4.75782 | -46.62574 | 2024-10-23 04:51:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d7db577b-69d0-3864-b073-f8e373d41225 | -4.75738 | -46.61855 | 2024-10-23 04:51:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 22c820b9-6aa7-373d-bb71-624ac9efd5cd | -4.75623 | -46.6261 | 2024-10-23 04:51:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| d4bdb3b9-6289-3014-89c3-d1fd3a3f52a8 | -4.75319 | -46.61797 | 2024-10-23 04:51:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 49e75819-e29a-3b4e-884f-8dd59dd111e2 | -4.75262 | -46.62175 | 2024-10-23 04:51:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 828ad381-92a4-32d3-b23c-9ee9f4689431 | -4.75204 | -46.62557 | 2024-10-23 04:51:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 923d8d81-6406-3019-b007-544506a30715 | -4.749 | -46.61744 | 2024-10-23 04:51:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9ac24a85-b05b-317e-b9e2-d55cb3819342 | -4.74148 | -46.66718 | 2024-10-23 04:51:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 804ebb60-e436-397b-a645-1fadbd90efac | -4.74091 | -46.67094 | 2024-10-23 04:51:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a6a7643f-1aff-33b0-b4e6-0a0602973072 | -4.73729 | -46.66671 | 2024-10-23 04:51:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a794e333-5de6-3118-b2d3-7723e88d83a7 | -4.73672 | -46.67048 | 2024-10-23 04:51:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d07ae401-26a5-3735-a3c9-a1c20a8a651e | -4.73616 | -46.67418 | 2024-10-23 04:51:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 8ec32b7d-2a85-350f-b1ad-a3590b95f283 | -4.73199 | -46.67364 | 2024-10-23 04:51:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d3983774-1ab9-32c7-9d04-e118fb23b153 | -4.73142 | -46.67739 | 2024-10-23 04:51:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 7d13493f-35a7-3c61-9a1c-5da6c6a17573 | -4.63621 | -46.53433 | 2024-10-23 04:51:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6895de24-ae18-3041-aac5-689ba183a932 | -4.55371 | -46.65912 | 2024-10-23 04:51:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 4.4 |
| a6148a86-a08f-3f96-87f8-c0026175e749 | -4.54957 | -46.65844 | 2024-10-23 04:51:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 372d8ba6-7529-3a43-8bf5-d7ff25f233bb | -4.54903 | -46.6621 | 2024-10-23 04:51:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 500eb1e1-ee5e-3292-9eb4-b27ca2e31162 | -4.52816 | -46.72929 | 2024-10-23 04:51:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 402c7df9-ad52-3c9c-8baa-78087bf7f339 | -4.52761 | -46.73288 | 2024-10-23 04:51:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 30aa30f1-b678-314f-a751-b89788ce25b9 | -4.52707 | -46.73643 | 2024-10-23 04:51:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 496076fc-f2c4-358a-ac4c-ccd81ffb5908 | -4.52676 | -46.72797 | 2024-10-23 04:51:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5b28c170-6292-3695-940f-fe6a677c7228 | -4.52623 | -46.73162 | 2024-10-23 04:51:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| cc9e5b9b-c44c-343c-896a-076c8d347080 | -4.52571 | -46.7352 | 2024-10-23 04:51:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| be281432-95d9-3e12-839a-8940da98d0f0 | -4.52402 | -46.72869 | 2024-10-23 04:51:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7fec8b17-5df3-39ec-91b7-82839127b8c1 | -4.36729 | -46.7988 | 2024-10-23 04:51:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c5c80fe1-6f41-3589-bf45-2396c3ee38da | -4.3075 | -46.70028 | 2024-10-23 04:51:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 761eac11-876a-3d78-82f8-52e277881965 | -4.25967 | -46.53776 | 2024-10-23 04:51:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 7e5f19f7-afd4-3a93-be6b-39af9725c40e | -4.25551 | -46.53709 | 2024-10-23 04:51:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 18712d6c-d468-3607-b2a6-0e0082c1b191 | -4.17586 | -46.79842 | 2024-10-23 04:51:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 260fb844-fecf-3ce3-802a-58d21b52bff6 | -4.07037 | -46.21028 | 2024-10-23 04:51:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5bc40eac-1579-36f6-91ea-98c099f0f9ac | -4.06996 | -46.20868 | 2024-10-23 04:51:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ea82e61a-ab90-35c4-a720-4e39be0cb67a | -3.98382 | -46.46807 | 2024-10-23 04:51:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| da366c26-c3a7-39d2-a456-0219c138b7c2 | -3.97486 | -46.47091 | 2024-10-23 04:51:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 139a219f-29fe-3640-868a-54384efbe4a7 | -3.97323 | -46.39587 | 2024-10-23 04:51:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2c459489-40e9-363d-a32d-f1545cbacdd4 | -3.85646 | -46.48156 | 2024-10-23 04:51:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3a91e5c4-6981-312e-8650-ba5a242e7d85 | -3.85172 | -46.48483 | 2024-10-23 04:51:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 994d1fa9-3805-3035-9f17-820ad77085ba | -5.5136 | -46.48437 | 2024-10-23 04:51:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| aff56410-ecaf-3219-9665-c94b803caa5f | -5.50934 | -46.48372 | 2024-10-23 04:51:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e66efd5e-7d65-3f4a-b014-65d04a18d8f7 | -5.47331 | -47.14463 | 2024-10-23 04:51:00 | NOAA-21 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2dd6ee07-a30f-3c2b-bcf8-3d27d63b9850 | -5.41208 | -47.10958 | 2024-10-23 04:51:00 | NOAA-21 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 991c97b7-09d9-32e1-bca5-59607ac674bf | -5.37398 | -47.50084 | 2024-10-23 04:51:00 | NOAA-21 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9013f4f1-637a-3de9-a3be-ee041f4d5fcf | -5.21231 | -47.19103 | 2024-10-23 04:51:00 | NOAA-21 | SÃO FRANCISCO DO BREJÃO | MARANHÃO | Brasil | 2110856 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7de11e5c-2eb6-3eb0-b6a2-263aab8e52f6 | -6.51756 | -47.03891 | 2024-10-23 04:51:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a38929ba-fa59-3725-80a4-68669eec8f28 | -6.51339 | -47.03833 | 2024-10-23 04:51:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 35df39aa-690d-3b86-9d7e-1a5621eb6bb4 | -6.51283 | -47.0421 | 2024-10-23 04:51:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5219c1c0-2a87-3876-ba7c-12318724cefa | -7.68031 | -47.31025 | 2024-10-23 04:51:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 68b6c39f-ad3f-3aa9-9885-342213b6da6a | -7.67614 | -47.30962 | 2024-10-23 04:51:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c987d9a6-e555-3098-9fa1-50a7b7f30f88 | -7.50179 | -47.3574 | 2024-10-23 04:51:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0cb68555-91a7-3599-b3ba-4961b054a2ca | -6.95641 | -47.08435 | 2024-10-23 04:51:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 16a615e7-99b1-3972-be8d-89851b72d1b0 | -6.95585 | -47.08817 | 2024-10-23 04:51:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 360264f9-8338-3351-a01f-25b88a52770f | -6.92304 | -46.83878 | 2024-10-23 04:51:00 | NOAA-21 | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0d7b54e7-0b7a-31ba-9693-68a4bb3fed00 | -6.78326 | -47.1494 | 2024-10-23 04:51:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8ea8b3f6-2927-36fd-a391-a57e14137694 | -6.62911 | -47.35239 | 2024-10-23 04:51:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8939a64e-01f5-3359-9d20-19e170f5cb54 | -9.01013 | -48.72198 | 2024-10-23 04:51:00 | NOAA-21 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4cd19c94-6055-3c3d-bb22-e6bb3f8ed10b | -9.00944 | -48.72684 | 2024-10-23 04:51:00 | NOAA-21 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 35d31381-77b3-32fb-b9c2-22b6611d534d | -9.00832 | -48.72438 | 2024-10-23 04:51:00 | NOAA-21 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ed48a2de-979d-303f-bfdb-ce3930a740b8 | -9.0793 | -47.98877 | 2024-10-23 04:51:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2b693698-e86a-3da6-b67b-75b711a904c6 | -9.07878 | -47.9924 | 2024-10-23 04:51:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 08232f65-d15a-3e5b-ac59-e870050a57f1 | -9.6144 | -47.6059 | 2024-10-23 04:51:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 66c35fdd-d787-30a3-9d41-0be1ccbfff1f | -9.53969 | -47.82322 | 2024-10-23 04:51:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 2a4c4b8a-7c33-3051-8a8e-8f1a33740451 | -3.14158 | -48.74864 | 2024-10-23 04:51:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3d43d66b-f686-3d79-a57f-f4cd1ca3cbf1 | -3.14018 | -48.74743 | 2024-10-23 04:51:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4b6bb3c2-27d1-3f12-bc4c-bdbc3b225f84 | -3.1034 | -48.66233 | 2024-10-23 04:51:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b1378ada-06b9-39f7-a211-5ce2ce40ada1 | -3.10276 | -48.6665 | 2024-10-23 04:51:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 812d8d8d-a826-3760-bc6b-9ef649be581b | -3.00835 | -48.08988 | 2024-10-23 04:51:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bf1faecc-6ed1-35c8-bb5e-22e803ad01e4 | -2.99789 | -48.08375 | 2024-10-23 04:51:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9b6c5061-130e-3772-aa0b-aa21d30570ae | -2.96787 | -48.00616 | 2024-10-23 04:51:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 01e30676-98d2-38ac-a48b-102d2198c743 | -2.9239 | -48.95752 | 2024-10-23 04:51:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| ae2d973a-176a-3b35-8fb6-dda284472bad | -2.89496 | -48.28718 | 2024-10-23 04:51:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6d00d037-6abf-33ac-b185-8812bf47213c | -2.78838 | -48.08252 | 2024-10-23 04:51:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 368afc98-5cbe-3784-b7bf-2cc33b869db5 | -2.76775 | -48.65355 | 2024-10-23 04:51:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8fde2c4b-9132-3cea-ba00-df2effbf9ca8 | -2.74771 | -48.68837 | 2024-10-23 04:51:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 630a002a-110c-352d-96f4-ec23042ffec2 | -2.74412 | -48.68782 | 2024-10-23 04:51:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 09e76482-1990-3cbf-a7c8-2d3bfe0834bb | -2.73694 | -48.68671 | 2024-10-23 04:51:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |


[Clique aqui para ver as próximas entradas](README36.md)
