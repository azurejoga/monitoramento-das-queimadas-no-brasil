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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5dd47358-ed22-3ccd-979f-853c63019ead | -8.51213 | -48.50562 | 2026-09-18 00:01:00 | TERRA_M-M | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| eb9e2114-9e9a-306b-b191-337acdacb866 | -7.65351 | -45.83735 | 2026-09-18 00:01:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 16808105-7359-3447-8a74-69135f3958bc | -3.96018 | -49.4427 | 2026-09-18 00:01:00 | TERRA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 7cdf0b7f-4829-3a60-bad4-e2d9ae693570 | -5.73726 | -44.39399 | 2026-09-18 00:01:00 | TERRA_M-M | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 23.4 |
| 8969a9ab-b81e-3f86-8f64-2f04f40bee52 | -5.5044 | -45.52623 | 2026-09-18 00:01:00 | TERRA_M-M | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 9dd746f6-7165-39d1-9061-2027365a9049 | -10.91165 | -53.9901 | 2026-09-18 00:01:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 8.1 |
| db7e136b-8461-3889-9a25-4f76f5c68969 | -11.52465 | -46.86152 | 2026-09-18 00:01:00 | TERRA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| a03c4ac8-5377-391a-abf5-ae8338f2c02c | -9.60142 | -45.85458 | 2026-09-18 00:01:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| d30377cf-e1bd-3625-8f76-d5d5dcb9076d | -4.42512 | -46.293 | 2026-09-18 00:01:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 37eac30d-cee5-35f5-a1de-31d6a0849d77 | -10.55012 | -44.85877 | 2026-09-18 00:01:00 | TERRA_M-M | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 0e981e54-3e7f-3438-967f-873fb02b7e35 | -7.01948 | -44.65132 | 2026-09-18 00:01:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 192010ac-ae47-323b-8c13-3384c073ee44 | -10.99669 | -49.74159 | 2026-09-18 00:01:00 | TERRA_M-M | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 14.1 |
| e0bb1c20-1b0f-35c5-bbec-c68d458ea5a7 | -9.2779 | -50.3187 | 2026-09-18 00:01:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| e81a6aa1-14db-3729-abec-19493cd077fa | -9.55507 | -45.41158 | 2026-09-18 00:01:00 | TERRA_M-M | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 10.0 |
| e4d4503a-7585-3d1c-9103-4ae052f679b6 | -9.10202 | -45.73143 | 2026-09-18 00:01:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 36c7b2ee-c00f-3006-b799-c525e483dbe3 | -11.39404 | -47.29699 | 2026-09-18 00:01:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 46e0c87a-be72-3bd2-ba24-09ac7f11b3e8 | -9.28684 | -50.31746 | 2026-09-18 00:01:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 6c44b832-d14a-3830-bd34-bd0624a772bb | -10.33143 | -45.31745 | 2026-09-18 00:01:00 | TERRA_M-M | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 20.2 |
| d19c16a1-7b32-37a4-bbfc-13df640ed270 | -10.03002 | -45.56989 | 2026-09-18 00:01:00 | TERRA_M-M | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 5d3e9efd-3e9d-32c9-b049-1e84f4b2eab9 | -8.45132 | -45.83643 | 2026-09-18 00:01:00 | TERRA_M-M | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 16.4 |
| aff56342-0f95-3cff-8d68-67d15530ee02 | -6.29979 | -41.79264 | 2026-09-18 00:01:00 | TERRA_M-M | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 26.2 |
| 615fff45-dce6-36b4-8e15-afbc130d1ae6 | -10.83908 | -44.94167 | 2026-09-18 00:01:00 | TERRA_M-M | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 9.1 |
| f30a0aac-8a7b-3dc5-87c8-b099d4ae5482 | -10.63221 | -50.2545 | 2026-09-18 00:01:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| d1257c03-8337-3747-ad29-6eaa745205e9 | -10.98422 | -48.30553 | 2026-09-18 00:01:00 | TERRA_M-M | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 731058bd-1f68-3249-83ae-0d8021c694c9 | -5.74195 | -52.2407 | 2026-09-18 00:01:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 33.5 |
| 227e51b8-abcf-32dc-a215-da26858d73b5 | -8.45313 | -45.84866 | 2026-09-18 00:01:00 | TERRA_M-M | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 82282f13-4eea-35ef-b2c8-c48614cb534c | -10.63346 | -50.26383 | 2026-09-18 00:01:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 95d5613f-2e44-3410-a8fe-bf8031c6088d | -11.06251 | -48.2849 | 2026-09-18 00:01:00 | TERRA_M-M | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 0d8efe25-4be9-3a99-90cd-f63245cd1a7c | -5.74967 | -57.60652 | 2026-09-18 00:01:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 34.4 |
| be15c24c-38b4-33d2-87ba-28ffd3230b62 | -10.80765 | -50.18932 | 2026-09-18 00:01:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| ad691f58-e335-3783-abed-f54be84b26a6 | -9.84217 | -48.38623 | 2026-09-18 00:01:00 | TERRA_M-M | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 7cb009b5-ddea-3644-83eb-619336db26ce | -11.05491 | -48.29511 | 2026-09-18 00:01:00 | TERRA_M-M | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 95602f34-a40e-3d24-88ec-717c06ded10c | -6.11551 | -44.02014 | 2026-09-18 00:01:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 3f378a24-84ff-3be4-a15a-1281f093b450 | -4.55149 | -42.96023 | 2026-09-18 00:01:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 32.6 |
| d5d711fa-6c5a-3696-a316-6886de205e97 | -5.86819 | -51.94798 | 2026-09-18 00:01:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 20f6e8c3-7c17-360a-902d-6b72d66c9a36 | -5.90451 | -53.55005 | 2026-09-18 00:01:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| d580b4fb-405c-35db-836a-aa079a7cdf90 | -9.60962 | -45.35203 | 2026-09-18 00:01:00 | TERRA_M-M | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 7cf6be51-1dfa-3c5a-b1b7-eb8285dc8b0e | -11.31645 | -46.76453 | 2026-09-18 00:01:00 | TERRA_M-M | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 11.0 |
| fc406e0a-3f24-3243-9491-b604511d9572 | -7.8162 | -44.90673 | 2026-09-18 00:01:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 8541cf37-c962-3ba5-9f4e-7364ec32a775 | -9.1136 | -48.98462 | 2026-09-18 00:01:00 | TERRA_M-M | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 62fdaea0-cf2e-3fd7-af10-af8c9f0bbe05 | -9.71418 | -54.83372 | 2026-09-18 00:01:00 | TERRA_M-M | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 39.7 |
| b7a06804-4fe3-3b1d-b167-c70d5f3f1912 | -5.87804 | -53.57209 | 2026-09-18 00:01:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| e91f2a33-e8ce-3d10-a11e-ec0bebc1152c | -7.80367 | -44.88771 | 2026-09-18 00:01:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 2b91bded-40b6-3980-8edc-9c742eb82eb2 | -5.73258 | -52.24212 | 2026-09-18 00:01:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 16.2 |
| 9d0c9749-501e-310d-a0ec-c5fc5ffcf39c | -6.6677 | -50.90451 | 2026-09-18 00:01:00 | TERRA_M-M | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 16.1 |
| 05eca08c-9c9e-37bf-b968-a8244201ad4f | -5.74664 | -57.58165 | 2026-09-18 00:01:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 6675834a-1041-3fd3-b3f1-3fc526b0302f | -7.672 | -46.10772 | 2026-09-18 00:01:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 19.6 |
| a01297c1-9a18-384c-b541-15dae2f32053 | -6.03449 | -51.81427 | 2026-09-18 00:01:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 1223d871-eca8-3eaf-bce6-55c292429f5b | -6.02015 | -51.77679 | 2026-09-18 00:01:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 41114d78-5511-3f91-ac0f-873c6c8db54f | -11.02201 | -54.1482 | 2026-09-18 00:01:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 727fb00b-0355-3701-aa92-89e5e612b367 | -7.53566 | -46.64421 | 2026-09-18 00:01:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 259bdb0f-07f5-3478-91f5-000f85e84de9 | -5.75997 | -45.08364 | 2026-09-18 00:01:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 33.5 |
| 9475b028-85a6-3b23-acc3-9aee1c9ba394 | -9.76038 | -45.05202 | 2026-09-18 00:01:00 | TERRA_M-M | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 9.0 |
| c84df284-6a0a-3878-a459-3794cb9d983e | -8.51087 | -48.49656 | 2026-09-18 00:01:00 | TERRA_M-M | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 29.5 |
| e242f6b0-5814-3a03-907f-c5543354ca61 | -5.6083 | -44.2662 | 2026-09-18 00:01:00 | TERRA_M-M | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 62141afe-e9c2-302e-9ac6-182436637271 | -6.52176 | -49.89902 | 2026-09-18 00:01:00 | TERRA_M-M | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 7a114225-3235-3e4a-8798-48cf789aa080 | -7.81696 | -44.9005 | 2026-09-18 00:01:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 398da7d1-06e4-38f1-8af5-01fd57de4c49 | -10.03199 | -45.57538 | 2026-09-18 00:01:00 | TERRA_M-M | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 17998504-4b53-3ef4-b2df-c9401d4d643d | -5.3324 | -45.14684 | 2026-09-18 00:01:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 59.9 |
| a16e0410-bbe2-396b-860b-4d7b77db6833 | -9.61998 | -45.35044 | 2026-09-18 00:01:00 | TERRA_M-M | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 8.4 |
| b762bb7c-2d75-3b85-8043-b8350f610f0c | -11.82104 | -48.82867 | 2026-09-18 00:01:00 | TERRA_M-M | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| b942760c-78a8-38bf-aa5e-73e6d40ae766 | -10.40018 | -48.67985 | 2026-09-18 00:01:00 | TERRA_M-M | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 20.6 |
| 89ea4665-21d7-3654-adfe-faa9be8175bb | -6.52055 | -49.89022 | 2026-09-18 00:01:00 | TERRA_M-M | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 70.1 |
| e7cc6ef1-62f4-3a5b-a14e-4cae89008ddb | -4.57502 | -42.97361 | 2026-09-18 00:01:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 768.0 |
| 658a4d71-fc47-37dd-9f6a-58ef688ffee2 | -9.54714 | -45.48242 | 2026-09-18 00:01:00 | TERRA_M-M | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 9.2 |
| ce6ad69f-a37e-3545-9706-1f886cf1b9d2 | -5.75089 | -45.10019 | 2026-09-18 00:01:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 211.4 |
| 1b47b99c-7e2b-337c-8042-bb01579dab46 | -8.44354 | -45.71296 | 2026-09-18 00:01:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 17.7 |
| b63a6728-e558-32bd-beda-50660706f220 | -11.13072 | -47.71447 | 2026-09-18 00:01:00 | TERRA_M-M | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 14.9 |
| e6fb82a0-61e1-3706-9ead-29a9d7e358ce | -10.63594 | -50.28251 | 2026-09-18 00:01:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 8901f0ae-4db2-3f8e-8463-e257e24c2584 | -11.27268 | -54.12114 | 2026-09-18 00:01:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 14.3 |
| efcdbc00-9f65-3441-b553-3ca7aeffd519 | -9.95483 | -45.67926 | 2026-09-18 00:01:00 | TERRA_M-M | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 14.9 |
| dae10879-32a8-3bac-92a7-6dc0f2267a0c | -9.79196 | -46.10479 | 2026-09-18 00:01:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 52.1 |
| 51d2aac2-fc49-3935-b506-6f2ef48db4fa | -4.57145 | -42.95052 | 2026-09-18 00:01:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1880.5 |
| 01c841c8-6913-303f-bf55-b4fcac181ad2 | -9.7053 | -54.81071 | 2026-09-18 00:01:00 | TERRA_M-M | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 16.0 |
| f40b6dd2-145a-36fc-88ed-d91d64f4e369 | -6.71152 | -46.40442 | 2026-09-18 00:01:00 | TERRA_M-M | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 8053e0eb-fd52-3701-887f-beb6ee996f1a | -4.58228 | -42.97884 | 2026-09-18 00:01:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 97.2 |
| 9d1ba24b-f47b-3e6b-a6c9-a2030ddf0512 | -6.65999 | -50.9149 | 2026-09-18 00:01:00 | TERRA_M-M | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 7526fdbe-4964-356a-8651-ef96986353fd | -6.4344 | -46.12573 | 2026-09-18 00:01:00 | TERRA_M-M | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| e2caee76-8c2d-3c07-b7e8-d09537f7c69d | -5.59005 | -48.1082 | 2026-09-18 00:01:00 | TERRA_M-M | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 7.4 |
| d3ac9957-5248-366f-9334-dd251cecf25e | -9.09185 | -45.73294 | 2026-09-18 00:01:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 1ae396bc-aa4e-3d1a-94c9-06c09c58b656 | -6.94865 | -43.12121 | 2026-09-18 00:01:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 30.9 |
| 42f3ddaf-1764-3f32-8b62-c66e319235d4 | -10.409 | -48.67857 | 2026-09-18 00:01:00 | TERRA_M-M | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| a0de7a9e-de97-3d71-be85-b01a13155748 | -9.74024 | -49.98558 | 2026-09-18 00:01:00 | TERRA_M-M | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| f39c4971-8906-322e-98dd-9a3ee244156d | -9.78218 | -46.10646 | 2026-09-18 00:01:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 34.5 |
| a08bb637-a76e-3625-bfaa-143b5e9435e4 | -5.61251 | -44.25972 | 2026-09-18 00:01:00 | TERRA_M-M | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 15.6 |
| cf168129-b094-3810-8ed4-77477e49fd36 | -4.57893 | -42.95586 | 2026-09-18 00:01:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 797.2 |
| 0385a283-66b7-3da8-857b-1adfc5ec6322 | -6.93568 | -43.12323 | 2026-09-18 00:01:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 24.6 |
| ac5a7d8e-2dda-3dee-8cb9-32406fdf644c | -10.40513 | -47.34687 | 2026-09-18 00:01:00 | TERRA_M-M | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| ad4b1717-65fa-35bd-b531-1e3beccaac61 | -10.94808 | -54.09797 | 2026-09-18 00:01:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 2b48a1de-f45d-3cb0-8d43-22ef8abe6648 | -10.84102 | -44.95468 | 2026-09-18 00:01:00 | TERRA_M-M | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 13.1 |
| e08fa2e3-8ae1-3706-89b4-b09e2287068f | -11.27085 | -54.1315 | 2026-09-18 00:01:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 6c73e812-319c-3bdc-a21f-65b0fed17b84 | -9.84133 | -49.17525 | 2026-09-18 00:01:00 | TERRA_M-M | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 867f8f0d-9c21-3495-950e-24ec47293184 | -6.61844 | -44.21682 | 2026-09-18 00:01:00 | TERRA_M-M | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 19.2 |
| 12d3ca6d-2fea-3873-84e4-59081d56c487 | -7.93265 | -44.83231 | 2026-09-18 00:01:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 19.0 |
| 97fc9c0c-3750-30f5-82bc-31e485e965a3 | -7.01467 | -50.81285 | 2026-09-18 00:01:00 | TERRA_M-M | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 1988a312-83e0-3250-a059-0b2a754cc8fb | -8.926 | -50.91919 | 2026-09-18 00:01:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 37a1d270-e0d2-35f2-a628-e7e3a4ae6f12 | -5.87642 | -53.56009 | 2026-09-18 00:01:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| aa404072-7263-3c7b-b9c4-bdc6542317ef | -8.94208 | -51.46284 | 2026-09-18 00:01:00 | TERRA_M-M | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 35.5 |
| a7308a71-1161-396d-b703-aab1c2ed7d9b | -9.94476 | -45.33887 | 2026-09-18 00:01:00 | TERRA_M-M | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 52.3 |
| e3a290c3-9de7-303b-ba72-ef621c47ec23 | -6.66121 | -50.92398 | 2026-09-18 00:01:00 | TERRA_M-M | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |


[Clique aqui para ver as próximas entradas](README4.md)
