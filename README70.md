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

## Dados Diários - Página 70

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8e84596f-74f6-3e0d-bb3f-ac072801d9de | -11.68059 | -50.98568 | 2026-09-22 04:49:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f8bba4c2-6d29-3ce9-8114-34d55d79a4b6 | -12.56714 | -45.98086 | 2026-09-22 04:49:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 104bf237-55cf-3d10-a8df-e169fabbfa3c | -15.98796 | -43.27837 | 2026-09-22 04:49:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 57c15db7-0f78-3e25-a880-d9aa91433fb5 | -10.60769 | -53.99819 | 2026-09-22 04:49:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8a841ac7-b525-3d93-9052-1201ee6f1cde | -13.19989 | -51.6078 | 2026-09-22 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a6322a73-92ff-3c2a-b79d-c54d4dbee0b9 | -11.1657 | -51.11378 | 2026-09-22 04:49:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 14.3 |
| e9e98650-c14c-3c3a-86cb-47fb9901158a | -14.67097 | -45.67549 | 2026-09-22 04:49:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 11.9 |
| a0d8f1ec-859e-3796-8c1f-12b3a87113cb | -10.61009 | -53.9833 | 2026-09-22 04:49:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 38.7 |
| 3b5a76f1-3722-3129-bdbc-3e86c9064848 | -12.30479 | -50.69906 | 2026-09-22 04:49:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c93cb43e-aebb-3850-a046-3dd1f3c6d11c | -12.39876 | -47.0644 | 2026-09-22 04:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ecc481cb-7257-3144-a93a-d67293720e51 | -11.01458 | -54.13333 | 2026-09-22 04:49:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e34c1bef-8804-3f0f-ad68-d2c596fdf4b1 | -11.96867 | -46.51737 | 2026-09-22 04:49:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 15bb54f6-1092-3b66-9cb1-4d93eee1a85c | -12.29573 | -50.71302 | 2026-09-22 04:49:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| adbfa5dc-1e4c-3a46-a9d7-9cb2eabffd89 | -14.38886 | -47.24967 | 2026-09-22 04:49:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8a899300-8b62-3585-bdea-b32333df818a | -11.47328 | -47.73758 | 2026-09-22 04:49:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 48674598-19d8-3942-9d47-d80331e14399 | -12.00816 | -51.47288 | 2026-09-22 04:49:00 | NOAA-21 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d413480e-628d-3594-a22a-0ad406add9e5 | -11.9594 | -46.51444 | 2026-09-22 04:49:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 54418afe-2371-36f1-83c6-728128979c99 | -9.56197 | -66.03245 | 2026-09-22 04:49:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.7 |
| a91cb9ae-c546-3c7a-bf2e-c30a2b97b2f0 | -9.18464 | -65.85458 | 2026-09-22 04:49:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 2ee5e550-3ee4-3efb-aca2-7588f5dff514 | -15.99205 | -43.27687 | 2026-09-22 04:49:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| b23b50be-ad9d-3c2e-919a-bfa00e38fda4 | -14.04569 | -52.0587 | 2026-09-22 04:49:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 6f614767-9179-3a0b-b810-9af48edcd034 | -12.29461 | -50.72052 | 2026-09-22 04:49:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8cf8910d-6536-398c-bd2b-438ef386fb20 | -13.93178 | -47.84822 | 2026-09-22 04:49:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ce6fa12d-9e21-38d2-8ce4-92a8b4b09b6d | -13.33112 | -51.28455 | 2026-09-22 04:49:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 25bf387e-3dea-33af-8f68-6d1164aa7b55 | -13.92765 | -48.5725 | 2026-09-22 04:49:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 75da8e09-812f-3966-bae8-c94f4e39f430 | -10.93424 | -58.33845 | 2026-09-22 04:49:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5d56855d-47cb-3931-93c9-af2934b03507 | -10.60149 | -53.99332 | 2026-09-22 04:49:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e83326ec-5f5c-3931-8f98-ed156f324462 | -14.75567 | -48.43412 | 2026-09-22 04:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f057f269-1b87-305a-bfcd-080054f68888 | -16.65985 | -49.2808 | 2026-09-22 04:49:00 | NOAA-21 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 37409eb0-b06e-3c94-8d14-3c54f2f39d50 | -10.91599 | -53.96098 | 2026-09-22 04:49:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| db53e97f-6dbd-3c8f-b9fc-fc4a861bad0a | -11.69914 | -50.99977 | 2026-09-22 04:49:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 6c393148-ed14-3306-b46c-a5f76acc0074 | -14.17851 | -47.87265 | 2026-09-22 04:49:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 636f4c8d-8893-3d38-a8fb-69907bdae487 | -13.72038 | -48.7844 | 2026-09-22 04:49:00 | NOAA-21 | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 08588773-0cf2-3766-886b-12b7ed27a5ec | -12.40651 | -47.06943 | 2026-09-22 04:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 13646791-d5e1-39ea-9d0d-125f83f138e7 | -12.96626 | -50.98952 | 2026-09-22 04:49:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dc09902d-dab8-30d2-a172-c5189547f6b0 | -11.50867 | -51.51523 | 2026-09-22 04:49:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1188a5fd-ccdc-37a4-bd0f-8ce109afb192 | -11.96012 | -46.51631 | 2026-09-22 04:49:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 3cd4498b-420e-3712-bb82-be5cd0377ba1 | -13.29887 | -51.76339 | 2026-09-22 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f5cff25c-6571-34a3-bb17-f51965fb490f | -11.35317 | -51.39947 | 2026-09-22 04:49:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 976c9a61-234f-329a-bad2-82a35f9dca26 | -10.86786 | -57.16739 | 2026-09-22 04:49:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ced4b69a-e1c5-399f-8a10-dff6d21dc285 | -12.5645 | -45.96665 | 2026-09-22 04:49:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 36.0 |
| b441bcd2-e5c7-3c77-8b41-511a03db00ba | -13.21988 | -46.92788 | 2026-09-22 04:49:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b1c47901-0618-3d41-be9a-fbad25ce1c0b | -10.60949 | -53.98701 | 2026-09-22 04:49:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 38.7 |
| 7aee4012-4569-3a55-b28e-3d492a1f79e0 | -10.87959 | -51.53922 | 2026-09-22 04:49:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c9220673-9e38-30ed-96de-83080867f0aa | -11.42985 | -47.35032 | 2026-09-22 04:49:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| d2f88e65-f479-335f-a7be-9123be08a144 | -11.75488 | -50.81338 | 2026-09-22 04:49:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 30fedeb7-0def-3ab4-aef5-dabb82a40afa | -14.11806 | -49.87223 | 2026-09-22 04:49:00 | NOAA-21 | UIRAPURU | GOIÁS | Brasil | 5221577 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cb92f886-d82c-3abc-9054-600c5ec7564f | -9.12574 | -65.87244 | 2026-09-22 04:49:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 901f17c4-3e84-39b5-8fea-fd5f770f9d44 | -9.28241 | -60.61813 | 2026-09-22 04:49:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bc77bfec-ac50-33ea-a102-eb0bb636519b | -13.28832 | -51.7654 | 2026-09-22 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b47eb043-14f2-342b-a168-92d1bff4b54d | -15.00416 | -51.39503 | 2026-09-22 04:49:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 65750621-cd5f-34c6-84cb-5141c7f7fefa | -11.44392 | -47.3369 | 2026-09-22 04:49:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 01f5d941-fa2c-3e08-a679-50ec7349cd14 | -10.59809 | -53.99276 | 2026-09-22 04:49:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e7d669ab-08fa-3aab-964e-c2b6c8d6bdc3 | -12.20005 | -47.03154 | 2026-09-22 04:49:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 417ffaa4-f61f-3c40-8ff9-9c4cfb89a491 | -10.92118 | -53.95044 | 2026-09-22 04:49:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 07136836-09b9-39ef-a277-fa02fabf58fd | -14.66483 | -45.66825 | 2026-09-22 04:49:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1e9750de-ca7f-3ab6-9699-ff5c114fab44 | -11.16625 | -51.11019 | 2026-09-22 04:49:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 5a5e21b1-1f80-3aa5-a8d1-ba9d7eab604b | -14.63541 | -45.6746 | 2026-09-22 04:49:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 42f7d4b2-2e23-324d-ab3e-c9ea5d7eec5f | -13.22307 | -46.93639 | 2026-09-22 04:49:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| aa615519-d153-3d91-a128-20155c3084e1 | -10.90123 | -53.96616 | 2026-09-22 04:49:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| bad59969-79a3-3139-9eaf-aaae5d7324b4 | -11.25604 | -54.13853 | 2026-09-22 04:49:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 63211d77-828b-3d45-9880-c0543e032716 | -10.87809 | -53.95856 | 2026-09-22 04:49:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d2ef905e-8da8-3c06-80bd-002f4234380b | -13.34179 | -51.28246 | 2026-09-22 04:49:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fec78848-28cf-39af-ad5b-5ddd474cca77 | -10.58568 | -53.98309 | 2026-09-22 04:49:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ad28cb07-dc84-37f4-83a3-cffe8b20ab29 | -13.33449 | -51.28508 | 2026-09-22 04:49:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 945f16bf-bc37-36be-8919-dd2b969a8325 | -13.34126 | -51.30877 | 2026-09-22 04:49:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 073bbc8f-31be-3854-afc5-9d2c609aed87 | -11.24324 | -54.10963 | 2026-09-22 04:49:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4bb9dab2-dbdd-3a8f-b9f3-a4c5f7765ecb | -11.96264 | -46.52283 | 2026-09-22 04:49:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b8a7db14-e49b-3769-b0be-2bdd828a094b | -11.50535 | -51.5147 | 2026-09-22 04:49:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 19443f5f-3b78-37b2-b71c-9eb380a83ab4 | -11.3262 | -54.05449 | 2026-09-22 04:49:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| afcb6136-7d9a-3752-ae84-2c4aea3e829f | -10.91778 | -53.94989 | 2026-09-22 04:49:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9cac6a5e-a18e-3f1b-bbef-aa369728d240 | -11.44892 | -47.33027 | 2026-09-22 04:49:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 536331f7-6310-3ec4-9393-22807a913833 | -15.26872 | -47.60131 | 2026-09-22 04:49:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f36f2d71-9b5f-3883-adb7-f848bdafaac0 | -11.89153 | -49.00179 | 2026-09-22 04:49:00 | NOAA-21 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1e2fdf4e-9c43-3c81-b201-4d882b4bceaa | -10.89663 | -53.97301 | 2026-09-22 04:49:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2c9c0dea-477a-38a1-8b78-43ad7cea4d67 | -10.90861 | -53.96356 | 2026-09-22 04:49:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| bd027fcc-df2f-3252-a59f-39a8bbd777a9 | -10.90402 | -53.9704 | 2026-09-22 04:49:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 069c46e0-7f25-3fd2-99e5-6a5071e3320e | -11.04717 | -54.15063 | 2026-09-22 04:49:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 440b0eec-c4e3-3c3b-9249-f74facc1c57a | -11.01738 | -54.13761 | 2026-09-22 04:49:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 22d98f38-c0b3-3efb-9299-8a6d1f6f0334 | -11.23984 | -54.10906 | 2026-09-22 04:49:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9a905789-c4c2-32a6-b3e5-5841d2eaffad | -10.59749 | -53.99647 | 2026-09-22 04:49:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2df1a9c8-ea09-3ca4-a730-69065d0b0535 | -13.2973 | -51.79634 | 2026-09-22 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 84cacd0d-0268-3e21-9db6-457650ef7396 | -10.41544 | -53.79587 | 2026-09-22 04:49:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 424b1bef-6276-3c7b-a354-cf1dff3552c4 | -15.44602 | -48.47585 | 2026-09-22 04:49:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c027d49d-2ef4-3868-85e7-83a623ce518f | -10.15645 | -58.76012 | 2026-09-22 04:49:00 | NOAA-21 | JURUENA | MATO GROSSO | Brasil | 5105176 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 086ae449-6bae-30ba-ab84-59760620f14c | -10.59968 | -54.00451 | 2026-09-22 04:49:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e1f570bc-beb7-3759-842a-3c502697b3c3 | -11.15341 | -51.1045 | 2026-09-22 04:49:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 37.0 |
| d08697ce-2ac7-3367-a0f9-0032c98c0689 | -10.90063 | -53.96986 | 2026-09-22 04:49:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9a7742b1-f991-3b87-b0eb-dc7bf4f6e8ac | -13.85635 | -51.85139 | 2026-09-22 04:49:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 967f2f19-c4c0-39d4-aad8-dff7e5519335 | -16.67539 | -41.85309 | 2026-09-22 04:49:00 | NOAA-21 | ITINGA | MINAS GERAIS | Brasil | 3134004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 2fb84582-5539-33e5-9ac9-1d326d73d8ea | -13.02636 | -50.60431 | 2026-09-22 04:49:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3824114e-28f0-32aa-a02a-b3c76e7d5669 | -11.70306 | -50.99665 | 2026-09-22 04:49:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 21.8 |
| 0345f6d6-67c5-382c-b72f-cb4241838b25 | -12.56124 | -45.95697 | 2026-09-22 04:49:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9810ffca-ffef-3967-b1e8-ef12466d50b5 | -13.33115 | -51.30717 | 2026-09-22 04:49:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| aee4c8cd-b89c-36d1-8d50-02cdc488e829 | -13.8569 | -51.84777 | 2026-09-22 04:49:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8246f94d-cdb2-3452-8807-1d7649d83993 | -11.32303 | -54.03114 | 2026-09-22 04:49:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 14a05ecc-46c0-3aad-a197-dc2e321baa35 | -11.4424 | -47.34814 | 2026-09-22 04:49:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ed8da8ca-fc96-3515-ab88-83460457fa22 | -10.60089 | -53.99705 | 2026-09-22 04:49:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 56b85fa8-9676-3cc5-9282-648cc70527fc | -10.42587 | -57.22596 | 2026-09-22 04:49:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6802f755-5b30-3507-bb3d-11df92677341 | -11.87199 | -46.84674 | 2026-09-22 04:49:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |


[Clique aqui para ver as próximas entradas](README71.md)
