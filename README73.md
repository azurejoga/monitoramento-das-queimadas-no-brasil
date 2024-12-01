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

## Dados Diários - Página 73

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c7bee5f3-61aa-31a1-a12c-8d15fdd72a65 | 0.98465 | -50.24325 | 2024-12-01 05:05:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 3.8 |
| c0d67306-595b-3ac3-8f57-24c457bd7361 | 1.15587 | -56.00623 | 2024-12-01 05:05:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4d37f986-cf13-34ac-8dcb-cca3d3a8214a | 0.98935 | -50.2463 | 2024-12-01 05:05:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 21be63fc-aec1-3e79-8b60-cd4e0e1338b6 | -1.10951 | -52.30531 | 2024-12-01 05:05:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 9f9623fd-35ed-30df-a687-d5d669a5225f | 0.98314 | -50.12486 | 2024-12-01 05:05:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 34522bb4-286e-3190-b9f5-efe48594f12d | -1.15046 | -53.54763 | 2024-12-01 05:05:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cc61c097-d290-3b58-96f1-d6c72e20ec40 | -1.00975 | -51.73196 | 2024-12-01 05:05:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 4b99fc23-e635-339d-bd41-21bd25b91b25 | -1.2341 | -51.8096 | 2024-12-01 05:05:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b98cc5a4-7943-3848-b80b-da792d0c35ed | -1.06959 | -53.63011 | 2024-12-01 05:05:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8e380bf5-a08c-31c0-b135-02832f91f77a | -1.1455 | -53.66998 | 2024-12-01 05:05:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 66a438ed-2ba0-3562-8920-c02baf30fee4 | -1.10353 | -53.59567 | 2024-12-01 05:05:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1ba6b809-c2b5-3f66-bc3c-20c10b5264fb | -1.11831 | -51.92269 | 2024-12-01 05:05:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a8b13297-906e-35b9-b2fc-cbce95d02010 | -0.57849 | -51.69085 | 2024-12-01 05:05:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 05f7dc97-6755-3074-bea4-87c154756d4f | -1.05135 | -53.2087 | 2024-12-01 05:05:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 2a06a05f-2adb-3323-a66f-280cbea1867e | -1.10015 | -53.38309 | 2024-12-01 05:05:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 634f500a-57c7-39ca-bb6a-45fdbef46dbf | -0.94989 | -51.65874 | 2024-12-01 05:05:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 91fc00da-83af-3df8-b270-cafa645c8c7d | -1.32536 | -51.74223 | 2024-12-01 05:05:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| dc8015e0-0fcf-3701-80e8-822d02a53617 | -1.15322 | -51.69378 | 2024-12-01 05:05:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0f496924-8988-3f77-ba0e-121a959ea27e | -1.13792 | -53.67274 | 2024-12-01 05:05:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fa0999e8-739f-3e2e-a9fe-3164d1ddf9a2 | 0.99808 | -50.27522 | 2024-12-01 05:05:00 | NOAA-20 | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 948aaf3c-f76a-32d4-b6a9-b7f62265f90f | -1.06359 | -53.38575 | 2024-12-01 05:05:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2a3fba7d-dcc6-36fe-a2d2-2c75db83d235 | -1.30675 | -51.73438 | 2024-12-01 05:05:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| bdcc90f9-31b0-3223-ac84-d1ce0cebd4c4 | -1.19073 | -51.75882 | 2024-12-01 05:05:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 028bcd9f-e3cc-336c-8b71-dbfaf964b441 | -1.14672 | -51.67616 | 2024-12-01 05:05:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4c34affb-0c00-30ae-8053-bcc59596c766 | -0.81943 | -51.61409 | 2024-12-01 05:05:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3d58a6d9-2c9e-3630-a4cf-ab3dccbb77f8 | -1.07024 | -53.22762 | 2024-12-01 05:05:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| fd60e9f4-a9aa-33b4-a6a1-54ecc7926294 | -1.27556 | -52.70387 | 2024-12-01 05:05:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b5da8891-173a-374f-aaa6-d6171bf94ff1 | -0.84747 | -48.52589 | 2024-12-01 05:05:00 | NOAA-20 | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b40536f7-323c-368e-93f3-f6f2650e7ed6 | -1.09989 | -53.38655 | 2024-12-01 05:05:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 0aab947d-a8a4-320f-8bc6-d7aab6b4a4fa | -1.14758 | -53.54314 | 2024-12-01 05:05:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 727cb048-0513-3109-9257-2f8e9eb94317 | -1.08414 | -53.39292 | 2024-12-01 05:05:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 55849691-2341-321e-8b14-c5e5e1ee8c27 | -1.08992 | -53.63728 | 2024-12-01 05:05:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 728062a3-291c-3e43-8bc0-6f243a5fca7f | 0.64767 | -60.53249 | 2024-12-01 05:05:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 358af90f-972d-3097-8c72-9103e022f704 | -1.23562 | -51.80003 | 2024-12-01 05:05:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 89797360-be65-370e-82f7-4d5961c8cf0b | -1.10231 | -53.60351 | 2024-12-01 05:05:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 42c94740-1b9d-389c-8d28-628c6064ced0 | -0.01123 | -51.16476 | 2024-12-01 05:05:00 | NOAA-20 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 7.4 |
| a2f6df44-c7bb-3a08-b060-d0f24bc2358f | -1.14453 | -51.67257 | 2024-12-01 05:05:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c4d58997-fd86-3508-8d8e-bc8079bdc21b | 1.17989 | -56.00651 | 2024-12-01 05:05:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9052c322-2e8e-3a15-a9b0-2e22d9846e80 | 1.15851 | -55.97814 | 2024-12-01 05:05:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8130a6c8-e082-3a28-a159-75ce88ccf33c | -2.28988 | -45.60547 | 2024-12-01 05:05:00 | NOAA-20 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 13.9 |
| e5464156-c0b9-3bd6-a442-6940c7f1d152 | 0.93966 | -50.75134 | 2024-12-01 05:05:00 | NOAA-20 | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 85b65ecd-a82a-32e4-989a-26991c141c49 | -1.10848 | -53.1466 | 2024-12-01 05:05:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4d1eb389-bc1b-3d3d-a83d-18d65ef53f5a | -0.9546 | -52.99113 | 2024-12-01 05:05:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0ba9f36b-0cab-36a3-a2d4-4f367a495699 | -1.24613 | -51.79404 | 2024-12-01 05:05:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d67b7e3a-9c66-3a4b-97a6-2d7fbdf7d2b0 | -1.18077 | -51.77207 | 2024-12-01 05:05:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 14099f96-4c04-3586-a6a3-9c22bb269030 | -1.08581 | -53.64071 | 2024-12-01 05:05:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 559c99f1-9804-3fa9-8a83-4bd549999771 | -1.07884 | -53.6396 | 2024-12-01 05:05:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1cfd8fac-f3da-3b42-84a1-708d16f3b359 | 0.98928 | -50.27282 | 2024-12-01 05:05:00 | NOAA-20 | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 000a3256-60f6-368c-813b-302c231a1164 | -1.70157 | -46.15245 | 2024-12-01 05:05:00 | NOAA-20 | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 947b42d3-b3fd-32fc-aaab-f6f983d0da59 | 0.93911 | -50.74787 | 2024-12-01 05:05:00 | NOAA-20 | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 95c89183-1064-371f-affc-339cd797a92e | 0.9431 | -50.74724 | 2024-12-01 05:05:00 | NOAA-20 | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 79a4f383-6e93-38e6-b2b5-7a352d09d88d | -1.25032 | -51.74054 | 2024-12-01 05:05:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ea5fffcb-24bc-3b3d-bea6-1821ceddf186 | -1.08766 | -53.39346 | 2024-12-01 05:05:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e50489ba-6381-3319-84ef-4830d12fbf89 | 0.98325 | -50.07057 | 2024-12-01 05:05:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fb2674fc-c9db-378e-9ad1-fcc3f505cb20 | -1.25604 | -51.78084 | 2024-12-01 05:05:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d1dc1b65-5a1b-3a40-9c24-bc56c0046292 | 2.73399 | -60.39455 | 2024-12-01 05:05:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 42c8ba6a-536c-3396-b083-7a938b4e3961 | -0.24753 | -55.91677 | 2024-12-01 05:05:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4f583e62-d64f-30ab-80ac-b8f17d7c7593 | -1.1715 | -53.41389 | 2024-12-01 05:05:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fdd5049a-5d3b-30df-8bf5-1a7e5cce5809 | -0.74726 | -51.94673 | 2024-12-01 05:05:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3a2d1303-fa46-3baf-ae19-7f1f2f991069 | 1.53261 | -55.70109 | 2024-12-01 05:05:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3278a897-a330-3da8-bb41-8e29f57d8449 | -1.26119 | -51.74716 | 2024-12-01 05:05:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e2a2a88e-bdef-302f-86c7-bfe04d2a58c4 | -0.9615 | -51.66054 | 2024-12-01 05:05:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c24f355f-3589-37ec-afb6-752afed7b8d8 | 0.35019 | -51.08656 | 2024-12-01 05:05:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a0753192-0a0e-39fe-ac46-feb6b3f5e71b | 0.64821 | -60.5359 | 2024-12-01 05:05:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 86a9db87-9f98-3957-b701-d03438470b3c | -0.59387 | -51.69319 | 2024-12-01 05:05:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 691a9936-77e7-379f-950c-18cb71be49f0 | -1.29976 | -51.72834 | 2024-12-01 05:05:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9c65689d-237c-322a-8ab5-5c59a080cad0 | 2.12441 | -55.87587 | 2024-12-01 05:05:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 486d2be0-d335-3c23-8e35-39509a6bfeb7 | -1.19995 | -52.56533 | 2024-12-01 05:05:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 052c6a3d-4e31-3f9f-9148-6ba29d5ba329 | -1.06312 | -53.22661 | 2024-12-01 05:05:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 828129f4-9800-32f8-b3d8-8febc13be742 | 3.27338 | -60.08329 | 2024-12-01 05:05:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5a175a24-d6ec-366e-bcb1-9bb6d8fba146 | 0.78293 | -60.117 | 2024-12-01 05:05:00 | NOAA-20 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 07804a08-090a-3114-ace1-8a4c6e9cc0b6 | -1.30751 | -51.72953 | 2024-12-01 05:05:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 19223310-7330-3b42-ad55-ac55786d459c | 1.18725 | -55.94551 | 2024-12-01 05:05:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 070298dc-4455-341a-a43d-db8ab2f8d92c | -1.17792 | -53.41894 | 2024-12-01 05:05:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 61637f12-7c28-366e-8f15-e16c92c3699e | -1.28123 | -52.69162 | 2024-12-01 05:05:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| d1d7abc1-1168-3e74-9e9b-f35bccf5fcf2 | 3.27391 | -60.08677 | 2024-12-01 05:05:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 563f04f8-d816-35b3-af85-bcc99d06eee2 | -1.09943 | -53.59904 | 2024-12-01 05:05:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6aba427e-7a77-3811-a9ef-704f043d77cb | -0.58308 | -51.68672 | 2024-12-01 05:05:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c869ba83-75a4-328e-9876-7c50a4313d83 | -0.24645 | -51.60769 | 2024-12-01 05:05:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 41e067a7-2c34-3843-8e85-6bfb167ae208 | -0.94527 | -51.66298 | 2024-12-01 05:05:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| af16d0b3-dcc8-3575-abe8-1317f58e7660 | -1.13655 | -53.70407 | 2024-12-01 05:05:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 01cf2fb7-880b-3775-9559-cbe624c8885a | -0.81786 | -51.59895 | 2024-12-01 05:05:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 411eee35-9837-3a5c-a3c4-efdc90717d5c | -1.27128 | -52.70728 | 2024-12-01 05:05:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b4218258-f4de-37a9-b016-c0e2a374019a | -0.96494 | -51.71524 | 2024-12-01 05:05:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c32aefa8-0009-3495-b963-bf2622968d09 | 1.17895 | -55.95736 | 2024-12-01 05:05:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e2782040-1472-35ae-81ae-9ead45deb706 | 2.12387 | -55.87243 | 2024-12-01 05:05:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4ce92671-445f-3cda-993e-83be64de93d2 | -1.25917 | -51.78624 | 2024-12-01 05:05:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 54284cea-9484-35ee-8de8-25cfe5e1d39c | -1.03599 | -51.74089 | 2024-12-01 05:05:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2fe3c412-b23c-3cf6-8fa1-aeee7be95ea9 | 0.93403 | -50.7416 | 2024-12-01 05:05:00 | NOAA-20 | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 15ad3015-f829-37d0-bf00-8946e7be7a5a | -0.72258 | -51.70248 | 2024-12-01 05:05:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 771cb230-ef19-3c1f-a354-239c6e996228 | -1.23947 | -51.80062 | 2024-12-01 05:05:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2ab20274-cfa9-3f71-911a-f19e7f69c515 | -1.08643 | -53.63675 | 2024-12-01 05:05:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a5706da4-fdd8-3e0c-b3b1-2f071bf282f0 | -1.16492 | -53.56973 | 2024-12-01 05:05:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1cb31aa2-521d-35c3-bc96-defc45685bf8 | 1.24947 | -50.68095 | 2024-12-01 05:05:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 344daa45-4672-3f7f-853b-8a0f2ca209e9 | -1.32333 | -51.97348 | 2024-12-01 05:05:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ae4be572-29ca-311e-bfb8-7ef2cac439ea | -1.31837 | -51.73619 | 2024-12-01 05:05:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b85c8bb8-7cca-3e60-8688-cb82296761f2 | 1.16404 | -55.97023 | 2024-12-01 05:05:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8741a9aa-d5dc-3a71-b953-a8c31b2c119c | -0.60465 | -51.69971 | 2024-12-01 05:05:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 7.1 |
| c443243e-3535-3ca6-a69f-8464c8148772 | 1.15682 | -55.98897 | 2024-12-01 05:05:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e70d7580-3c5a-3430-9c01-29d389a9c654 | 0.97483 | -50.12619 | 2024-12-01 05:05:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README74.md)
