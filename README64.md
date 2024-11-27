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

## Dados Diários - Página 64

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3415a4d5-8ee1-3047-820a-1d4cde5ecd51 | -2.87775 | -51.80022 | 2024-11-27 04:42:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e65706a8-0dc0-397b-a88c-bed4085d509e | -5.98475 | -45.35987 | 2024-11-27 04:42:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 13.7 |
| f826456a-f6e0-3d44-96ff-37a360d28212 | -2.46585 | -49.04682 | 2024-11-27 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 45711eb6-b60a-3d48-b02d-cc9159d2ce18 | -3.71644 | -47.12683 | 2024-11-27 04:42:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2d1e5f63-5fb3-3fdd-9997-4843d01267b7 | -4.31051 | -48.18191 | 2024-11-27 04:42:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4d29bafc-3292-398f-a64c-f14bb12e820d | -3.03157 | -54.01904 | 2024-11-27 04:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 58ca657d-073f-397d-9e8f-22d43f9509bc | -3.13079 | -51.01939 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ada0d588-65c5-366f-8949-9dfeb0a6409d | -5.03013 | -47.0174 | 2024-11-27 04:42:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2a7da988-967d-3dbe-8e96-996e9be697ac | -4.08831 | -48.21496 | 2024-11-27 04:42:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3400b60c-8a50-31ba-9a1c-8af2de6d2813 | -1.55193 | -51.27095 | 2024-11-27 04:42:00 | NOAA-20 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 19dc1c9a-dfd5-37a3-9854-50b95660ef76 | -1.7379 | -52.04433 | 2024-11-27 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 737841f1-1412-3197-a545-52aa9c17591e | -3.21784 | -50.91914 | 2024-11-27 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 85271fe8-01b8-3d72-bbdb-42be36dbc323 | -3.16518 | -48.43198 | 2024-11-27 04:42:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 20.8 |
| 9ad9594f-1939-3955-a222-71d4709d02b9 | -2.95046 | -53.71645 | 2024-11-27 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8a8e2151-7dbd-3349-b94d-ac59062b0e5a | -3.49634 | -53.81118 | 2024-11-27 04:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| cf2fca9d-b6fa-3673-a531-7f0bb53c3813 | -3.90107 | -50.11948 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 086205f3-a526-33a6-9ea9-e83a5e179b89 | -1.55841 | -52.78717 | 2024-11-27 04:42:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f79f9674-6156-3451-a795-dfebbbc4d7ff | -3.94064 | -46.71587 | 2024-11-27 04:42:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a8eba583-9e6b-35f8-8f57-b68337336153 | -4.06613 | -54.38218 | 2024-11-27 04:42:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 241e4fbb-7693-331f-88a2-f702e49dfacd | -1.64367 | -52.45069 | 2024-11-27 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 04103d61-07e2-3219-bc88-2b166267c019 | -3.2606 | -53.03485 | 2024-11-27 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a0497fd3-1fb5-3dac-b3a8-2a6226327118 | -3.99121 | -48.32417 | 2024-11-27 04:42:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 34b17ccb-7c89-321f-98a5-798cd5a3b790 | -3.32485 | -50.21931 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 70bcedcf-dbde-30c3-8057-aafdef8bc099 | -2.23468 | -53.62213 | 2024-11-27 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 178afa3a-85c6-32f0-84e1-5ae20e4dea39 | -2.57096 | -49.09208 | 2024-11-27 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e4457ea7-78e4-3f6f-9090-6396539c3e9a | -1.73183 | -52.78717 | 2024-11-27 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6aada3a2-2528-3819-92bc-368d894e849e | -1.28449 | -51.74285 | 2024-11-27 04:42:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9cf6e7d4-e1e8-3972-9998-3eafb598768a | -1.66855 | -52.45704 | 2024-11-27 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c2cef3aa-30a9-3109-a0ea-056a2a340221 | -3.5113 | -50.30865 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7c63e988-f6d4-3476-8876-d7abe9c46582 | -3.45209 | -50.29583 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 44606b5a-43c6-3265-ae0e-2bb53f841e46 | -3.87252 | -50.15031 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cfb8bf27-43c4-317e-9d3a-99fec886e488 | -3.95126 | -49.95073 | 2024-11-27 04:42:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0f539813-f9be-3514-87cc-b6a90b457c6f | -1.27276 | -52.1682 | 2024-11-27 04:42:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ce4e4433-5d1b-39e5-8bcb-ed83a7c0a87f | -3.4149 | -50.38155 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 64fa5c06-8e77-3c62-acc2-3ba26b84ba0e | -3.07385 | -49.50193 | 2024-11-27 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d0b94681-ff08-3a37-9d57-66e12340f10f | 0.33355 | -49.71627 | 2024-11-27 04:42:00 | NOAA-20 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a6b6a8b7-852a-3cbe-8b2c-5e6e3e7f1909 | -2.93612 | -54.79893 | 2024-11-27 04:42:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 29d01029-b8f8-350a-857d-2bec790c830f | -2.81655 | -54.12408 | 2024-11-27 04:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 57b14e2f-572f-341e-90a9-9baf607a07e0 | -3.98271 | -46.65234 | 2024-11-27 04:42:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 12e4a4b2-5fa4-3e94-ae5a-0313c4865918 | -3.50284 | -53.79443 | 2024-11-27 04:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7b6493e2-6939-3fa6-aaa5-0c6cd1b518d8 | -3.82047 | -50.632 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c7bb7e9b-d5e4-3b16-b332-82a174e84882 | -2.94656 | -54.08649 | 2024-11-27 04:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 9626738b-1840-3dc3-9b7b-8b7e46f6e025 | -3.24958 | -53.28985 | 2024-11-27 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7b5aea31-4375-37ab-9bc9-175627912a75 | -1.66338 | -52.25562 | 2024-11-27 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9eb52c76-2b45-376a-a4b8-3c71154fa0c7 | -3.59739 | -50.38543 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ae133eb0-3d1f-3013-b67d-22bc306ed9b4 | -4.24129 | -48.67651 | 2024-11-27 04:42:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 2b6a779e-53b9-3f4b-a1e1-df6c716d3693 | -3.81164 | -46.60286 | 2024-11-27 04:42:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 47806b66-d962-33d8-8dc2-a669f405fc01 | -4.30239 | -48.18856 | 2024-11-27 04:42:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a50a6ecc-567b-381b-97fa-9398c4bdb67e | -3.97725 | -48.07012 | 2024-11-27 04:42:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 26ec4e92-c65e-3612-b2ef-02a60cc273ee | 0.65413 | -50.82773 | 2024-11-27 04:42:00 | NOAA-20 | ITAUBAL | AMAPÁ | Brasil | 1600253 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c1e53a17-70c0-3424-afc9-7b94a97cdb23 | -4.73889 | -48.12619 | 2024-11-27 04:42:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 467b3db9-8c93-32ba-bbd8-84bbbfa0b3fa | -2.73749 | -54.10857 | 2024-11-27 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1fb1d93b-d6c4-3642-ad4b-7f8995b76370 | -3.25023 | -53.28573 | 2024-11-27 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7faf3c72-bfd3-3fce-aacb-a6e965d2168f | 0.97196 | -50.12551 | 2024-11-27 04:42:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8e6f9c24-07c3-3bde-96e5-62dab75144eb | -4.05112 | -46.84143 | 2024-11-27 04:42:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a0dbaf5b-438d-3133-8afe-221a51bce895 | -4.04268 | -54.454 | 2024-11-27 04:42:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1ed8ae35-a7c0-3e34-8cf7-b6ff4e0b6dfb | -1.28507 | -51.73916 | 2024-11-27 04:42:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ffec686a-57f0-3e57-a047-c3f9edff062b | -2.47629 | -50.36436 | 2024-11-27 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4d7045b2-5cb0-32ce-82bf-f87103043552 | -3.24038 | -53.6338 | 2024-11-27 04:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 7ea1aaf8-9682-3c10-bb76-6088b81d284e | -2.31588 | -50.65006 | 2024-11-27 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| aa153139-eb06-36f8-a037-c798e52c74df | -3.1426 | -48.53322 | 2024-11-27 04:42:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c36ffc11-d3b3-3cc9-b9bd-7464d302afed | -4.21859 | -48.66547 | 2024-11-27 04:42:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 22.5 |
| 27c37123-ed3d-3c1d-96cc-dda43f9d29bb | -1.23462 | -51.79203 | 2024-11-27 04:42:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4f926bb5-1ee6-3e5a-97cc-10480375a754 | -4.41824 | -48.303 | 2024-11-27 04:42:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a6c81fe5-233d-3d1f-b226-f1fa930d3306 | -1.10371 | -54.14943 | 2024-11-27 04:42:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 74d98314-27ff-3eb6-b488-20b8898adfce | -2.18113 | -53.77816 | 2024-11-27 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 25.0 |
| 297ef016-8b50-3100-a7b2-926822124e5f | -4.18887 | -50.68598 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 83c9324a-6f75-3c27-8933-a65d4f018665 | -4.21275 | -50.88074 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e8de88c5-6d34-3b1d-9170-eaa429e69165 | -3.28439 | -50.75587 | 2024-11-27 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e8ff02c4-419d-3a65-9370-d5c68ffb2a81 | -1.48514 | -52.53887 | 2024-11-27 04:42:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ec989d29-071b-3c16-a431-ee7d584a4373 | -2.25571 | -53.7517 | 2024-11-27 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 5ebb246e-c300-32e3-be33-a2f4e87b08f9 | -1.50898 | -47.27432 | 2024-11-27 04:42:00 | NOAA-20 | BONITO | PARÁ | Brasil | 1501600 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 75ae732f-b8ad-3ae8-96ca-497e5c4c1169 | -2.26797 | -51.2368 | 2024-11-27 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c8d05db8-dacf-3572-a6e1-f8105b63a1ca | -3.2916 | -50.53807 | 2024-11-27 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 45cd88e5-621e-3951-8f72-a7f273edd20b | -3.50137 | -50.50076 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bf5fff68-e7c7-3cf2-aefa-f75dfe0e5432 | -4.17838 | -49.41199 | 2024-11-27 04:42:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| bb23acab-6cf8-32c8-a3b1-7108a5efa926 | -2.02007 | -51.19066 | 2024-11-27 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 35b79d58-dc12-38a1-a58c-f6da1c888c5d | -1.70359 | -52.17064 | 2024-11-27 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bb02cc30-71be-3818-92e9-5f2811dba099 | -4.36917 | -48.50691 | 2024-11-27 04:42:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fe459e4a-6827-3d1a-a12c-990d985ce7cb | -2.78691 | -53.21299 | 2024-11-27 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7636b659-99b2-3271-9c60-4158d7972c13 | -3.10811 | -53.26468 | 2024-11-27 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 82b37ebe-771a-397f-9767-e2e7a7a5680c | -1.13705 | -48.35744 | 2024-11-27 04:42:00 | NOAA-20 | BELÉM | PARÁ | Brasil | 1501402 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f7da6b47-2c81-3ac6-a432-c787f74c1f81 | -3.80843 | -47.47191 | 2024-11-27 04:42:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2a411c27-2a10-32a6-a1c3-1b09f56211b4 | -2.21785 | -53.6165 | 2024-11-27 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 38525362-8391-3021-9880-93d258f06791 | -4.19217 | -50.68649 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cf0f412e-8b47-30fe-bcbf-a3846b6a8879 | -2.33721 | -52.18232 | 2024-11-27 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 045d74f4-0d11-3484-9608-4eb017ed92b3 | -2.92322 | -48.63677 | 2024-11-27 04:42:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ca1bc6a3-e328-3ad1-8f26-d4d3890c4b9e | -3.93236 | -46.64631 | 2024-11-27 04:42:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2a8c6c78-8d87-3fd8-9c5f-00b2255e49f1 | -3.17143 | -48.43669 | 2024-11-27 04:42:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 19.0 |
| c7d470fc-4ff8-31b4-bf01-5cc755782eda | -3.46902 | -50.2527 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 962c5382-dc3e-35cf-a958-db5f8305ae7a | -3.59841 | -50.35742 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| ca632909-6227-3e47-b9cf-7bde50befe3d | -4.28923 | -50.22257 | 2024-11-27 04:42:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c5cad252-016d-3d39-b48a-77ca39f77985 | -4.10961 | -46.80497 | 2024-11-27 04:42:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 14a42af4-f0b7-3ce3-b1bd-c94f1dd7a751 | -1.07568 | -53.37682 | 2024-11-27 04:42:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c01580b2-c769-3603-92c7-e52746e731b0 | -3.03486 | -48.50577 | 2024-11-27 04:42:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b9b8ce0e-dfae-3ae8-858f-ea41e7cf49ba | -2.62958 | -54.38842 | 2024-11-27 04:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 712fab53-7bcc-3d26-b7e2-c5ed64a7b5a0 | -3.27092 | -48.76402 | 2024-11-27 04:42:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9b820f61-fe4d-3431-94c0-36c69091440f | -3.87006 | -54.32367 | 2024-11-27 04:42:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5ecb6e3c-37df-3b84-8dad-5ee95c2763d6 | -5.22194 | -44.91249 | 2024-11-27 04:42:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e5d4a735-592d-3bbc-a837-d80316deea5a | -4.25663 | -48.66758 | 2024-11-27 04:42:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |


[Clique aqui para ver as próximas entradas](README65.md)
