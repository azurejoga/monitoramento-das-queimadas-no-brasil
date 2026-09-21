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

## Dados Diários - Página 152

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2df2fd02-aefb-3fd0-848e-1ed601c060db | -9.88243 | -48.4235 | 2026-09-21 16:01:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 54.4 |
| b20e449f-58c6-3772-8794-e009b2a4fe66 | -9.26469 | -48.21691 | 2026-09-21 16:01:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| d18e42d8-b88c-3ac9-a539-cd057696f210 | -11.08361 | -49.73746 | 2026-09-21 16:01:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 24.2 |
| 5d80617b-0362-37be-bfb6-6ba948821368 | -9.62258 | -45.81435 | 2026-09-21 16:01:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 16.5 |
| d61280af-50ba-3ce5-9b30-6e897d3dcea0 | -9.82365 | -48.45929 | 2026-09-21 16:01:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 14.2 |
| e5223d56-04b8-3241-997b-c99bd5cd54d4 | -9.51053 | -45.81525 | 2026-09-21 16:01:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2e6323b6-841c-363d-b470-f2037474acd6 | -10.72341 | -50.7841 | 2026-09-21 16:01:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 172.6 |
| fdc2d0ef-e358-3ac4-8595-28180c1a10dd | -8.77974 | -44.26096 | 2026-09-21 16:01:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 34.9 |
| 699b1d98-8532-3abe-a34d-e0d142f802fd | -11.34055 | -43.37527 | 2026-09-21 16:01:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 31.7 |
| da060044-5fc7-3be1-a3f4-3f6345eb9dc5 | -10.95125 | -50.62061 | 2026-09-21 16:01:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 22.3 |
| 3a900cdf-9e12-34a2-bbca-f313b3af5984 | -11.42629 | -47.3218 | 2026-09-21 16:01:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| a4bc4e20-d911-3e0a-95b7-4df622a05094 | -14.36141 | -43.77024 | 2026-09-21 16:01:00 | NOAA-21 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| eaba9385-df02-36bc-8ec6-0ecf8158b72a | -14.00227 | -42.13671 | 2026-09-21 16:01:00 | NOAA-21 | LAGOA REAL | BAHIA | Brasil | 2918753 | 29 | 33 | nan | nan | nan | Caatinga | 53.3 |
| 6617d937-34fa-3cd4-9c48-083a6de08d63 | -11.15277 | -42.82487 | 2026-09-21 16:01:00 | NOAA-21 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 10.3 |
| a8729e1c-84a1-3cb0-807a-19fed9f44acf | -8.78032 | -44.2653 | 2026-09-21 16:01:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 109.9 |
| fb4766fe-2c3f-3909-9b97-ae2b8819fdca | -10.06834 | -45.87 | 2026-09-21 16:01:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 9c995bf6-8e83-3e53-b2da-6d08f976df85 | -8.69681 | -45.44333 | 2026-09-21 16:01:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 29.6 |
| 4010f91b-98eb-3fb4-884d-48a91a823119 | -8.76145 | -45.85843 | 2026-09-21 16:01:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 8621f96e-7f7c-3d25-bd30-60b7ed05cd42 | -10.86527 | -48.07216 | 2026-09-21 16:01:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 506bf9c4-0531-3a85-87d0-1293749776b3 | -11.26843 | -43.40683 | 2026-09-21 16:01:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 18.1 |
| d0aa73d5-6785-3cee-9d82-2532ca65e06f | -10.12124 | -48.4376 | 2026-09-21 16:01:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 200f0f93-5997-3dfe-b619-ccff8067505c | -9.88188 | -48.41898 | 2026-09-21 16:01:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 29.0 |
| 7d15253f-8e08-338f-8d92-daf756fba493 | -11.95729 | -46.50794 | 2026-09-21 16:01:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 398a5279-0442-321e-9a71-a4a1eaba2c3d | -12.44213 | -47.07666 | 2026-09-21 16:01:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 7e31a581-78dd-3e3c-aa96-58fe4a782301 | -9.73127 | -48.15967 | 2026-09-21 16:01:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 68ebf336-a693-3166-b2dc-a5a4295deb2a | -9.15695 | -50.01089 | 2026-09-21 16:01:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| a4096ec1-4a16-361a-ab53-056fc1918fec | -11.64944 | -50.21586 | 2026-09-21 16:01:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 16.6 |
| c9be2ea1-aeac-3915-8108-9861a158590a | -12.77772 | -47.11386 | 2026-09-21 16:01:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| c1ef8629-5ab1-39ad-aee1-06747aba8f93 | -10.55848 | -46.54546 | 2026-09-21 16:01:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| dea7a678-ebc4-34e0-ae65-82f7aa7c489f | -9.77758 | -48.33688 | 2026-09-21 16:01:00 | NOAA-21 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 901ac8d8-6721-3cd3-90fa-add65937250d | -11.81115 | -50.02431 | 2026-09-21 16:01:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 7268f7dc-2f52-336b-99d0-40f840031bca | -8.73263 | -45.45019 | 2026-09-21 16:01:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 20656047-5fba-35a5-b2a6-4237fb3245f7 | -11.37685 | -46.76608 | 2026-09-21 16:01:00 | NOAA-21 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| bb034a31-6fa8-3f75-9a0d-73fe3bac70c2 | -7.93553 | -38.91158 | 2026-09-21 16:01:00 | NOAA-21 | VERDEJANTE | PERNAMBUCO | Brasil | 2616100 | 26 | 33 | nan | nan | nan | Caatinga | 8.6 |
| 6a3b17f7-63dd-36a5-82bd-6b8ad85b26ee | -11.42098 | -47.32647 | 2026-09-21 16:01:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 19.1 |
| eefbea15-9227-3a8a-8de2-1ee1ac9ddeda | -13.91276 | -45.48972 | 2026-09-21 16:01:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| e6e6289d-ee8c-3e55-a86a-941bb480a097 | -9.20812 | -46.22171 | 2026-09-21 16:01:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 38.0 |
| 1db46275-b981-3707-a2a5-33561c70e215 | -9.54836 | -46.53141 | 2026-09-21 16:01:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 4be9adb2-6a71-313e-b407-bdcf41a4ef5f | -10.34183 | -50.20285 | 2026-09-21 16:01:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 62d5bcf0-80c0-3f3b-bd3e-fabf0ad1ba5b | -10.97709 | -50.59734 | 2026-09-21 16:01:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 24.9 |
| 584d55b7-81a3-3d01-979b-f8390bc9b32b | -12.41613 | -47.05465 | 2026-09-21 16:01:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 52c2c54e-c885-3e80-956f-88e454b17baf | -11.42146 | -47.33054 | 2026-09-21 16:01:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 3db088a9-3910-3cb5-a4fd-ce4b1e2f843d | -11.07984 | -49.74128 | 2026-09-21 16:01:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 84123b7a-d68e-34ad-be22-beccd159b1aa | -10.95828 | -50.61991 | 2026-09-21 16:01:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 21.6 |
| e0980570-3e92-3da2-9c8e-2d4075213239 | -12.42287 | -47.06218 | 2026-09-21 16:01:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 3940a115-66b2-3e9e-bafa-5bcf1a9407f7 | -11.95773 | -46.51165 | 2026-09-21 16:01:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 42a9ef6d-5889-300f-bda5-6c6df1a53170 | -12.31042 | -50.67689 | 2026-09-21 16:01:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 7a883f9c-6eed-3e63-965a-9df1fce01b51 | -12.40458 | -47.00684 | 2026-09-21 16:01:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| af6a7a0a-7a6d-3f96-ac44-9dae869a1de3 | -13.89006 | -45.47901 | 2026-09-21 16:01:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| fb6530a4-b7bc-30b2-b423-99a738d3867f | -11.80191 | -49.81076 | 2026-09-21 16:01:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 23.0 |
| f2e075bd-379b-3ac3-b4e8-b902106a9f8c | -9.35734 | -46.37878 | 2026-09-21 16:01:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| d53da57b-ab7b-3a7a-a8ce-c15d18a54026 | -10.16638 | -45.55554 | 2026-09-21 16:01:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 11.1 |
| edef4a40-1c4d-37bc-962f-3e5dfadc3eeb | -10.07417 | -50.24707 | 2026-09-21 16:01:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 52.7 |
| 7007c628-a54d-3498-a8d5-1907fb5d832d | -8.84763 | -45.93166 | 2026-09-21 16:01:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 48a45931-03eb-34e0-ab64-d13278b28e5d | -9.02733 | -48.14798 | 2026-09-21 16:01:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 12.8 |
| ef271b7b-5693-3a34-a33c-b6bc5473b6d5 | -12.04692 | -50.07213 | 2026-09-21 16:01:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 30.2 |
| 1ff191bb-c967-3a0c-94d4-ccab97636101 | -11.92457 | -49.80467 | 2026-09-21 16:01:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 597c899a-75e1-360c-914f-29ca5e10c32a | -9.17671 | -50.02281 | 2026-09-21 16:01:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 517a645f-fca9-3beb-bb8d-a775244a21a2 | -10.82002 | -50.14146 | 2026-09-21 16:01:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 23.9 |
| 22dcebf0-d260-3329-9442-0d084a9bc0f3 | -10.86546 | -50.16071 | 2026-09-21 16:01:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 34.8 |
| 54bc725f-ce11-3baf-991b-b0d2e78128aa | -12.06071 | -50.07076 | 2026-09-21 16:01:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 18.7 |
| d9c44996-6303-365c-ac44-4d0add62ca13 | -11.64236 | -50.21564 | 2026-09-21 16:01:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 5ddba432-b3ed-3207-bce2-88eb89e8adde | -8.75843 | -44.28555 | 2026-09-21 16:01:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 23.4 |
| 319153dd-3389-3daf-89d8-320275e9564f | -9.87413 | -48.40604 | 2026-09-21 16:01:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 51.7 |
| 6ec7fe33-a28e-3baa-b824-065768868920 | -7.81211 | -38.83626 | 2026-09-21 16:01:00 | NOAA-21 | SÃO JOSÉ DO BELMONTE | PERNAMBUCO | Brasil | 2613503 | 26 | 33 | nan | nan | nan | Caatinga | 3.6 |
| ad68daa8-631a-3a24-82d6-9065fe625a18 | -9.7662 | -46.06006 | 2026-09-21 16:01:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 081c22bf-57d2-3ac4-b01b-3deb211649ab | -10.26117 | -45.50029 | 2026-09-21 16:01:00 | NOAA-21 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 23.2 |
| c4506247-e806-33c5-8539-8feff49f5563 | -9.876 | -48.4718 | 2026-09-21 16:01:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 20.4 |
| bdd2208d-a3a2-3441-8bb5-714e09191ec1 | -14.33874 | -44.79556 | 2026-09-21 16:01:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5b37776f-b5fa-3782-8680-dfa1b1116b77 | -9.8116 | -46.08445 | 2026-09-21 16:01:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 14.0 |
| d02b9f1a-30b4-3abb-b151-992bda1316c0 | -12.42532 | -47.01939 | 2026-09-21 16:01:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 0067a2aa-0cbd-334c-9cf9-85c9482516dd | -12.28046 | -50.15573 | 2026-09-21 16:01:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 18b428f3-a6ea-39db-846f-f4635a68c067 | -7.82143 | -38.85295 | 2026-09-21 16:01:00 | NOAA-21 | SÃO JOSÉ DO BELMONTE | PERNAMBUCO | Brasil | 2613503 | 26 | 33 | nan | nan | nan | Caatinga | 18.2 |
| 58f0849b-7ede-39d3-bbab-8718ba48689f | -11.01091 | -49.73045 | 2026-09-21 16:01:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 15.8 |
| cb71f42a-718f-3ead-8a6c-3412b2bdc768 | -11.93392 | -46.50379 | 2026-09-21 16:01:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 7b4528a1-0fc8-3d7e-87e8-88ae39301101 | -10.27482 | -50.23646 | 2026-09-21 16:01:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 10265945-0e81-3678-ae85-173582e1c221 | -10.09997 | -45.83135 | 2026-09-21 16:01:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6affb500-1b34-3773-b115-e3362e2b615a | -11.45868 | -47.63745 | 2026-09-21 16:01:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6de41fd4-1dbf-3e10-a000-4dfd6b6a5fbd | -11.62629 | -50.19753 | 2026-09-21 16:01:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 30d9f042-b2a6-3f36-8743-c56a384e71bb | -8.77044 | -44.29485 | 2026-09-21 16:01:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 52.2 |
| 054222e2-cf4d-3c67-9890-4b23d9c9f69b | -11.33066 | -43.40327 | 2026-09-21 16:01:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 46a3be4d-a802-30fb-a5cb-8a1fbafc0b5f | -9.97638 | -50.25489 | 2026-09-21 16:01:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 24.0 |
| b0f5a0ed-e5e6-3649-bf70-6d0911766139 | -9.97536 | -50.26158 | 2026-09-21 16:01:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 19.9 |
| 799cc384-caf7-3e60-9b41-8eb4c034fab6 | -11.44055 | -45.38456 | 2026-09-21 16:01:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 08826321-1222-3001-b43f-7a57b46bae4a | -10.77316 | -46.15765 | 2026-09-21 16:01:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 0c5687e6-a239-3c53-a219-cf9fc37a746e | -12.82622 | -44.2062 | 2026-09-21 16:01:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 10.2 |
| d92ccd5f-862b-348f-abf4-c2ca55294acc | -10.75827 | -46.34316 | 2026-09-21 16:01:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 25f5160a-83e3-3f3f-9144-0a5998c644a6 | -9.42044 | -35.9701 | 2026-09-21 16:01:00 | NOAA-21 | ATALAIA | ALAGOAS | Brasil | 2700409 | 27 | 33 | nan | nan | nan | Mata Atlântica | 8.2 |
| 70d05de9-d31f-360b-a0f7-a76af6f20a4d | -9.61422 | -43.92399 | 2026-09-21 16:01:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 75.1 |
| db2975a3-a008-3bcc-b1b0-3128cf15bcaa | -12.28741 | -50.15505 | 2026-09-21 16:01:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 4f687a6f-7630-32fb-9321-65011082744c | -11.7837 | -46.82855 | 2026-09-21 16:01:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bcc63a02-9a39-3356-9e87-46ac16f8c5af | -10.07778 | -50.27818 | 2026-09-21 16:01:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 14.6 |
| c0ba25e7-ea0e-3bde-8ab9-513d66297ed7 | -12.07121 | -50.03488 | 2026-09-21 16:01:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| a3c550e6-cf0d-30e4-872b-7a4c2a95fee6 | -12.38694 | -47.00502 | 2026-09-21 16:01:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 97a89242-3d09-3ea8-9832-792540af6980 | -11.80678 | -49.81427 | 2026-09-21 16:01:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 15.9 |
| dd977255-6ef6-3d0f-804e-9a9ae3839be8 | -11.44093 | -45.38756 | 2026-09-21 16:01:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 2f24a9fd-ac95-36d5-b1a7-6ea9fbf72992 | -9.2708 | -46.20676 | 2026-09-21 16:01:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 254fe43d-c5a0-3bee-9e79-249918f45010 | -10.75989 | -46.33833 | 2026-09-21 16:01:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 0289cfe6-4bbd-3194-87b2-943b33add41c | -12.7776 | -47.10884 | 2026-09-21 16:01:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 17cb798b-0819-3b59-92a6-089d68953941 | -8.15152 | -35.87568 | 2026-09-21 16:01:00 | NOAA-21 | RIACHO DAS ALMAS | PERNAMBUCO | Brasil | 2611705 | 26 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |


[Clique aqui para ver as próximas entradas](README153.md)
