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
| d562c52d-4d96-3c2f-aedf-ccadd87c57f3 | -10.9353 | -56.8522 | 2025-06-14 02:40:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 46.5 |
| a72f7944-eefb-3c9e-b87d-79f44ee3c6d0 | -10.9355 | -56.8322 | 2025-06-14 02:50:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 2dcd4e0b-ab53-3dac-aba2-6db598032aee | -14.2121 | -57.4098 | 2025-06-14 02:50:00 | GOES-19 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 51.3 |
| c74e6ac0-a267-3389-b5f8-dddeb37c4cfe | -6.9605 | -42.8816 | 2025-06-14 02:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 62.8 |
| c7eb30ba-8a06-3ba4-a3d7-2fa5bf1368b9 | -6.9416 | -42.8834 | 2025-06-14 02:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 78.7 |
| 4ff23ce4-4c0c-302a-bff9-99bbb260e347 | -13.887 | -54.6106 | 2025-06-14 02:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 62.1 |
| c7211dfe-d95c-36dc-85e1-d4b981e1ab98 | -10.9353 | -56.8522 | 2025-06-14 02:50:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 51.1 |
| 0318bd04-b10b-3e15-a521-6186a8882cfc | -13.9062 | -54.6084 | 2025-06-14 02:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 63.7 |
| dae0096b-402c-35ee-a119-05e51b61962a | -16.1967 | -46.4589 | 2025-06-14 02:50:00 | GOES-19 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 62.6 |
| 598a591a-59d4-3dc7-806d-ba87e3b2789b | -6.9414 | -42.907 | 2025-06-14 02:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 62.5 |
| 64a2c279-0948-35b2-aa9a-2eee198f05cb | -6.9416 | -42.8834 | 2025-06-14 03:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 81.0 |
| 0e941221-509f-30ad-8e55-eb93c745f288 | -13.887 | -54.6106 | 2025-06-14 03:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 55.3 |
| 20091a5c-c730-3630-9018-6ce7c215832b | -13.9062 | -54.6084 | 2025-06-14 03:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 77.7 |
| fa0dba0e-9f20-3035-b86d-c9f08c033a33 | -10.9355 | -56.8322 | 2025-06-14 03:00:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 68.0 |
| 576600a1-98f2-39c8-9507-78573b5327ca | -16.1967 | -46.4589 | 2025-06-14 03:00:00 | GOES-19 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 66.9 |
| a5f87cb8-3728-3231-b0a0-06addafee084 | -14.2121 | -57.4098 | 2025-06-14 03:00:00 | GOES-19 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 50.3 |
| f00c214f-da94-3e78-b931-558dc5487c01 | -6.9414 | -42.907 | 2025-06-14 03:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 68.1 |
| d89a3d1a-506d-3a01-8403-87d7de65bf21 | -10.9353 | -56.8522 | 2025-06-14 03:00:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 47.3 |
| 1259384e-a29f-36a4-a12e-f000457ebf6b | -6.9605 | -42.8816 | 2025-06-14 03:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 70.7 |
| 96a75141-c185-3846-8242-60a286ac95ba | -6.9416 | -42.8834 | 2025-06-14 03:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 74.4 |
| 42f4e2bc-f440-38f4-89ea-1bcd8283ded7 | -6.9605 | -42.8816 | 2025-06-14 03:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 75.4 |
| 17281711-b405-3645-b5a8-826b45948846 | -14.2121 | -57.4098 | 2025-06-14 03:10:00 | GOES-19 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 56.3 |
| 5c2fb8ed-7f64-3a97-b0d8-2fbbedb01869 | -13.9062 | -54.6084 | 2025-06-14 03:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 91.0 |
| a93c59d6-93fd-3ed3-9c8f-60e6f83932c4 | -10.9355 | -56.8322 | 2025-06-14 03:10:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 65.4 |
| ac3e67f8-870b-30b0-bf09-3adbbaa1e0b3 | -6.9602 | -42.9052 | 2025-06-14 03:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 62.3 |
| d5f6872b-5ba1-35d8-87e2-be9717dbe490 | -10.9353 | -56.8522 | 2025-06-14 03:10:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 45.8 |
| 664303e5-c4b1-3efb-acc4-099ed4611cde | -16.1967 | -46.4589 | 2025-06-14 03:10:00 | GOES-19 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 53.4 |
| ecd2081a-6a14-376e-b0c1-e7dada3b490b | -6.9414 | -42.907 | 2025-06-14 03:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 62.7 |
| 95f06a54-ea8b-361f-8351-2b01949c6ff3 | -14.2121 | -57.4098 | 2025-06-14 03:20:00 | GOES-19 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 7e9e8498-bd5c-36e0-bc09-10702f56919f | -16.1967 | -46.4589 | 2025-06-14 03:20:00 | GOES-19 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 48.3 |
| 7bba1939-5c6c-3eca-af58-c911bfb2929a | -10.9353 | -56.8522 | 2025-06-14 03:20:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 44.2 |
| 542d1d90-8d94-3ff7-9fd5-066e17380002 | -13.887 | -54.6106 | 2025-06-14 03:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 46.8 |
| 167b54d9-a5a8-3af5-87b0-e5684521d207 | -6.9414 | -42.907 | 2025-06-14 03:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 66.3 |
| e469ab68-2e68-3d28-a45d-39594b0a4ae9 | -10.9355 | -56.8322 | 2025-06-14 03:20:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 61.3 |
| c24686e3-5a19-3918-a5b3-0a84b71e87c6 | -13.9062 | -54.6084 | 2025-06-14 03:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 73.5 |
| 81fb5425-e00c-3bf5-8190-95e9c28b402b | -6.9605 | -42.8816 | 2025-06-14 03:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 69.1 |
| ac82380d-705d-38c1-b03d-73df3e4cb4d8 | -6.9416 | -42.8834 | 2025-06-14 03:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 83.5 |
| 4403c1df-15e0-3ae6-9dde-9eec88f05fd0 | -5.12107 | -37.78885 | 2025-06-14 03:21:00 | NOAA-21 | QUIXERÉ | CEARÁ | Brasil | 2311504 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| e5c7f85a-134f-3f88-80b2-f150dbe2d1ae | -5.91384 | -43.46203 | 2025-06-14 03:23:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| f44341a7-7ab5-36ca-b8e5-7a72e6161ef0 | -7.22077 | -43.10809 | 2025-06-14 03:23:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 8.2 |
| 61518e48-437c-3670-96d2-5eb6949724c8 | -6.60178 | -43.89561 | 2025-06-14 03:23:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 46a31829-ec7d-316f-8844-4b1f95dc9b02 | -7.2273 | -43.10912 | 2025-06-14 03:23:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| a4c63e0a-7220-34fb-9341-ab7b331973e5 | -6.6005 | -43.90345 | 2025-06-14 03:23:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 5d9438b2-1aae-32cc-ad91-efa1d59fa27a | -7.18535 | -39.29604 | 2025-06-14 03:23:00 | NOAA-21 | JUAZEIRO DO NORTE | CEARÁ | Brasil | 2307304 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 0597dd27-483b-3294-9e1d-26a69eb01933 | -7.23583 | -43.09942 | 2025-06-14 03:23:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| db2d3f95-95cd-3d8d-9b9e-57e36a702051 | -7.07425 | -43.55703 | 2025-06-14 03:23:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 0c7337b7-3b8f-3a01-afd6-6277c7c06526 | -7.23482 | -43.10482 | 2025-06-14 03:23:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 9a991198-a24c-37ff-ba10-56a7ad6b7573 | -6.21489 | -43.33081 | 2025-06-14 03:23:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 12.9 |
| b820ec43-1040-3a72-bdf5-80c4f777f812 | -6.60974 | -43.89226 | 2025-06-14 03:23:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| c42d65ea-051a-3352-8083-b5c856a61576 | -6.21377 | -43.33687 | 2025-06-14 03:23:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| d647c367-e51f-32ea-8f90-2c1516994939 | -5.9056 | -43.45739 | 2025-06-14 03:23:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 41035463-cfe8-313e-9f77-295495efbc0e | -10.65017 | -44.48175 | 2025-06-14 03:23:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| ccd53674-8011-3091-9ba2-1c5dcc83acbb | -7.2319 | -43.58316 | 2025-06-14 03:23:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| ff38be60-f802-3c17-a381-1fd9123b46ed | -10.65832 | -44.49174 | 2025-06-14 03:23:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 7568debf-4f63-348b-ba32-e746ca9436d1 | -10.65166 | -44.49042 | 2025-06-14 03:23:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| f8488da1-8e3e-3305-92a8-708a7b38b725 | -5.77419 | -43.47742 | 2025-06-14 03:23:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 088d6aa2-29a8-348a-8321-3939ad732c0e | -7.22965 | -43.59504 | 2025-06-14 03:23:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 84c68c16-9ef6-33a0-aea4-b89a1b99c4db | -5.89885 | -43.45606 | 2025-06-14 03:23:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a1434c59-9330-324a-a16a-ae4e448114b6 | -10.65563 | -44.48887 | 2025-06-14 03:23:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 38e06595-26f2-360a-ab91-109641d29b8d | -7.18959 | -43.5513 | 2025-06-14 03:23:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| fa87bbc9-b6df-330a-b566-c6329de59b4c | -7.21321 | -43.11255 | 2025-06-14 03:23:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 8.2 |
| 0f2d08ed-5f04-331a-bf97-4895b2d9b372 | -6.68824 | -43.96752 | 2025-06-14 03:23:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 40a6b7f5-4e3c-32a7-83ab-34ec1bf8401d | -10.65442 | -44.49474 | 2025-06-14 03:23:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 7ebb9221-6592-3fc5-9be7-04e63a5b584b | -10.64229 | -44.48636 | 2025-06-14 03:23:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 165a7b79-eb82-3675-b4ec-ef5d4c91afe0 | -6.60291 | -43.89082 | 2025-06-14 03:23:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 15.8 |
| a99c1182-fb0e-36df-a78d-cde1d3903ce0 | -6.95247 | -42.89187 | 2025-06-14 03:23:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 39.8 |
| dd449a8a-892e-3af3-b917-9cfbb4f2524d | -7.07124 | -43.55528 | 2025-06-14 03:23:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3de9e9f4-d046-3316-99aa-3cee0d54ee4e | -8.07824 | -43.11561 | 2025-06-14 03:23:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 28.6 |
| 9135b64b-dba7-375c-9394-d8036ac281ba | -8.07184 | -43.11437 | 2025-06-14 03:23:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 28.6 |
| 6d6fd3e2-b540-3b5f-9daf-a302cb733c3b | -6.68703 | -43.97388 | 2025-06-14 03:23:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 85566fc5-7fa2-3281-a176-cb1dc93134e6 | -7.21426 | -43.107 | 2025-06-14 03:23:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 8.2 |
| 1a89cf1f-f84d-3306-b3f2-fabd8ef2f16b | -7.22296 | -43.59387 | 2025-06-14 03:23:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0865af37-c65f-3fa6-8867-f3bf75e99ee5 | -7.22833 | -43.1036 | 2025-06-14 03:23:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| e777b05c-1308-30d8-af39-b22f209fe7b4 | -6.95041 | -42.90301 | 2025-06-14 03:23:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 47.8 |
| 697769ae-0a7b-3248-ac63-43af77067697 | -6.60172 | -43.89704 | 2025-06-14 03:23:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 41ed1fbc-9500-39b8-b968-e13b6e1ec871 | -5.91123 | -43.46494 | 2025-06-14 03:23:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| b92cf9b5-84ff-3431-96b4-463fbbc0a1c2 | -5.90151 | -43.45321 | 2025-06-14 03:23:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 097377ab-0ae7-3ed7-8136-1cc505773532 | -10.65284 | -44.48453 | 2025-06-14 03:23:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| fdaccb3f-528d-3356-a76a-22884a29cd2c | -6.60857 | -43.89729 | 2025-06-14 03:23:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 2c08172e-ec50-3bbf-b1f4-b2aa001feaa1 | -7.2413 | -43.10611 | 2025-06-14 03:23:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 277dbc8c-17ca-3856-a102-ab37687b23ba | -6.60738 | -43.90379 | 2025-06-14 03:23:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 6a6b3705-8ac5-324b-949e-54e85e22bca5 | -7.18174 | -43.55623 | 2025-06-14 03:23:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 24e3850e-2f2f-30bf-9a64-975bfc620601 | -10.64897 | -44.48759 | 2025-06-14 03:23:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 603c38d2-7430-3a84-9775-3f90fbd4fe54 | -8.07284 | -43.10907 | 2025-06-14 03:23:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 12.7 |
| 40fef1fd-1bd7-337f-94f7-d31a1c7a8aea | -6.60291 | -43.88942 | 2025-06-14 03:23:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 328433cb-5c41-3e0f-81ea-ec7dcbcac0e8 | -6.60976 | -43.89079 | 2025-06-14 03:23:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| e49b9341-b23e-36e6-b6f1-729494933e50 | -7.07792 | -43.55655 | 2025-06-14 03:23:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a1fc13cc-96a2-312c-bb37-00afd7660045 | -5.91916 | -43.45971 | 2025-06-14 03:23:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f1f69391-ff4e-3b70-bb0d-71630583ed93 | -6.68702 | -43.9736 | 2025-06-14 03:23:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 4ab82a2d-b7ef-3edd-81c3-3b159f864874 | -6.54992 | -42.3926 | 2025-06-14 03:23:00 | NOAA-21 | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 07fd05ec-e8fc-38a5-a32a-d8fad8ccdfbe | -7.2403 | -43.11153 | 2025-06-14 03:23:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 20f2241e-5a08-3a3c-a375-527ed731c3b9 | -5.90675 | -43.45105 | 2025-06-14 03:23:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 569fff9e-5555-3aad-85fa-a617ce3578f6 | -5.91235 | -43.45874 | 2025-06-14 03:23:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 692a41f4-c0fe-31f3-8771-3ade37df2c53 | -7.22409 | -43.58788 | 2025-06-14 03:23:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d14b7af0-1252-328a-992a-a8b70977f914 | -6.95145 | -42.8974 | 2025-06-14 03:23:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 47.8 |
| 20aaf2c0-bcb2-3799-a516-4e5552fe43ad | -6.60851 | -43.89874 | 2025-06-14 03:23:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 495aa9d2-891a-3bd5-840c-04d6eed49a69 | -7.23079 | -43.58903 | 2025-06-14 03:23:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 876e0116-269c-3179-8160-1ad992e913f8 | -10.65049 | -44.49631 | 2025-06-14 03:23:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 3400600d-1e26-35b2-bad0-791a0cd2d735 | -6.95347 | -42.88643 | 2025-06-14 03:23:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 39.8 |
| 3f3a89be-083e-36dd-89ef-d010e9664b8c | -7.47793 | -37.41468 | 2025-06-14 03:23:00 | NOAA-21 | SANTA TEREZINHA | PERNAMBUCO | Brasil | 2612802 | 26 | 33 | nan | nan | nan | Caatinga | 1.2 |


[Clique aqui para ver as próximas entradas](README8.md)
