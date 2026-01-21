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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6086f0db-e075-365a-9cac-ee34d6d76492 | -2.70925 | -45.56575 | 2026-01-21 04:21:00 | NOAA-21 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 92c6e77b-a2d4-3f31-a86c-ddc5d44ce01f | -3.5542 | -48.85539 | 2026-01-21 04:21:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0409c810-3fa4-35ba-bafa-0995135d63a1 | -4.69078 | -38.16272 | 2026-01-21 04:21:00 | NOAA-21 | RUSSAS | CEARÁ | Brasil | 2311801 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 8177b4d3-81ff-378a-acad-8fb292d2f102 | -6.44952 | -37.99705 | 2026-01-21 04:21:00 | NOAA-21 | BOM SUCESSO | PARAÍBA | Brasil | 2502300 | 25 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 16d41367-2509-3c87-99f6-834d4cc3eac2 | -3.15987 | -48.13719 | 2026-01-21 04:21:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b9bf1085-c00e-3438-8200-df5db2213a1c | -3.89388 | -38.64702 | 2026-01-21 04:21:00 | NOAA-21 | MARANGUAPE | CEARÁ | Brasil | 2307700 | 23 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 29733104-7b47-30ef-8be0-f84679c82f05 | -3.48443 | -47.68737 | 2026-01-21 04:21:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3b69b701-6a1c-330a-9c3c-4646d8cb82f6 | -3.55341 | -48.86034 | 2026-01-21 04:21:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 762a8d81-b1e4-38cb-b5c4-430cd22bd3e2 | -2.46811 | -48.11856 | 2026-01-21 04:21:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 67ebb9ce-91e7-3c88-843d-6724734d9e9d | -2.42097 | -47.23199 | 2026-01-21 04:21:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d73ad36e-cf3f-3c2d-a2e7-d18e46ac4749 | -1.76828 | -47.13713 | 2026-01-21 04:21:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 70e65ba3-8ea1-3944-be26-79884163e7f5 | -2.666 | -45.56656 | 2026-01-21 04:21:00 | NOAA-21 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| bbc2ea6f-2a61-33c6-9b3b-aafe8d228c16 | -2.01788 | -46.92711 | 2026-01-21 04:21:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1339f402-3f9d-328c-9599-7cbb1a535226 | -4.74654 | -48.12133 | 2026-01-21 04:21:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 20c48401-16ed-3d04-a1eb-b25c682cc87a | -2.6078 | -47.35057 | 2026-01-21 04:21:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 364f951a-0e2d-3999-953b-f96298d843c7 | -1.50542 | -47.32878 | 2026-01-21 04:21:00 | NOAA-21 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4ead12af-4b50-3ead-baf0-420f90777b39 | -2.51018 | -47.26177 | 2026-01-21 04:21:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7f78d2e0-0bcb-3d3f-95c2-b6fc4ee4f46f | -2.50901 | -47.26295 | 2026-01-21 04:21:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f4e92a6e-d5b9-3cf1-9b04-e7ab5f90023f | -2.66994 | -45.56348 | 2026-01-21 04:21:00 | NOAA-21 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fb41ec76-59ef-3fb6-8856-133e14d99ddc | -4.1017 | -47.29938 | 2026-01-21 04:21:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3f4cc0ed-28e3-391e-84a6-e2470fd89387 | -2.42436 | -49.03074 | 2026-01-21 04:21:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5f96d191-815c-3dc5-8767-a383c60ca55f | -3.06234 | -54.59305 | 2026-01-21 04:21:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b6e9f5cb-1278-38dc-819d-06b65a78c57a | -3.5538 | -48.85744 | 2026-01-21 04:21:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d67d0db7-e141-33b9-830a-5e624634a2fe | -3.06231 | -54.59162 | 2026-01-21 04:21:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 52834a9f-88cf-3700-8127-cda9403d53b1 | -4.10105 | -47.30343 | 2026-01-21 04:21:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c4c20f30-49ba-357b-9791-bc9b506b5019 | -1.52413 | -46.69552 | 2026-01-21 04:21:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1a46aef3-ee75-3fab-8292-ba0e7aa00abe | -2.60832 | -47.35009 | 2026-01-21 04:21:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e22dc3b4-c548-3773-b00f-c37631295ad6 | -2.74045 | -47.39109 | 2026-01-21 04:21:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 46a6b4df-8962-365e-937a-7d15f38b89a1 | -2.60847 | -47.34628 | 2026-01-21 04:21:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 632a408f-b686-35e8-b7f3-fceee8932192 | -3.15384 | -48.15042 | 2026-01-21 04:21:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f4942201-ab18-3ef0-a2f4-9ac111fd6330 | -2.42794 | -47.14308 | 2026-01-21 04:21:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c3435699-754a-30cd-8c17-fb524e930535 | -3.89807 | -38.64768 | 2026-01-21 04:21:00 | NOAA-21 | MARANGUAPE | CEARÁ | Brasil | 2307700 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 52aace98-3e86-32a5-bb27-76e96d72fcfa | -3.15459 | -48.14581 | 2026-01-21 04:21:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 972961b5-695f-3590-8f98-e3fc675d31b6 | -3.55298 | -48.86239 | 2026-01-21 04:21:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 538be9b2-918f-3c75-babe-58fed71c7aa5 | -18.93897 | -53.39358 | 2026-01-21 04:23:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 69cd6e0f-5dce-3f8d-a04f-257a5ac0663d | -18.82401 | -51.61695 | 2026-01-21 04:23:00 | NOAA-21 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a01f46c3-51af-32bf-920c-3457b7daf8bf | -10.24777 | -36.52225 | 2026-01-21 04:23:00 | NOAA-21 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 8a01217a-70cb-3617-bb12-f8e967af68d0 | -15.97382 | -56.27667 | 2026-01-21 04:23:00 | NOAA-21 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 0b6f8f41-3677-3880-95e7-d77872e4f1de | -15.97317 | -56.27992 | 2026-01-21 04:23:00 | NOAA-21 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 1e3c1c08-5637-30b4-8b47-51eb46510518 | -18.93416 | -53.3966 | 2026-01-21 04:23:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 73886694-4e46-3cee-aabc-c9ec0e9cc335 | -10.2531 | -36.52298 | 2026-01-21 04:23:00 | NOAA-21 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| d0a23ce3-4796-3da7-8686-796ddf536a53 | -18.93345 | -53.40036 | 2026-01-21 04:23:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 11a34630-e3f5-3ff2-9ace-ad4f11671e42 | -15.97448 | -56.27344 | 2026-01-21 04:23:00 | NOAA-21 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 801a881f-cf38-3de3-8887-cac5a45dd139 | -18.82032 | -51.61625 | 2026-01-21 04:23:00 | NOAA-21 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 012ddf79-81ab-3195-85e0-972a27c49cdb | -18.81744 | -51.61095 | 2026-01-21 04:23:00 | NOAA-21 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fc26d02c-211b-3ff4-ad94-4e9f68a00d28 | -19.21278 | -53.43763 | 2026-01-21 04:25:00 | NOAA-21 | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1bb31f34-5baf-334c-a417-99629eeb14d2 | -20.34103 | -57.89541 | 2026-01-21 04:25:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| ef1a6144-43eb-334e-9da1-3092558d186a | -19.39318 | -57.26959 | 2026-01-21 04:25:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 2ff056a1-69cd-3a3d-ac96-a1bdea1f6543 | -19.6674 | -56.95151 | 2026-01-21 04:25:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 46474d56-dcfb-317d-8695-99a63cceb6cb | -20.72002 | -48.7837 | 2026-01-21 04:25:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| b80259f8-7fb8-3380-9ed9-a4b76ddf9f77 | -21.57571 | -47.14663 | 2026-01-21 04:25:00 | NOAA-21 | TAMBAÚ | SÃO PAULO | Brasil | 3553302 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 8e7eaa61-d975-3047-a9e9-d5b218d92c1d | -22.0189 | -56.34484 | 2026-01-21 04:25:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 317c0fb7-7179-3a0c-a600-e54786ac0691 | -19.42689 | -57.2117 | 2026-01-21 04:25:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.7 |
| 477c6d4d-45cb-37de-9075-d34b64bfbea7 | -19.42588 | -57.29461 | 2026-01-21 04:25:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| fb298209-cce0-358c-94dd-c563e35e81bf | -19.41795 | -57.30674 | 2026-01-21 04:25:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 6f647c90-f5d5-3273-95c0-2574029c0e47 | -19.65602 | -56.95542 | 2026-01-21 04:25:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| e9e445d6-d3f4-3dc6-90bc-e776a7700687 | -19.66805 | -56.94839 | 2026-01-21 04:25:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 70805596-14da-30d2-a3f9-cfb228acd6c3 | -21.26172 | -50.29931 | 2026-01-21 04:25:00 | NOAA-21 | BIRIGUI | SÃO PAULO | Brasil | 3506508 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 2c9c7cd3-ff58-3ab4-ac5c-0fabeaa7962b | -19.44624 | -57.22881 | 2026-01-21 04:25:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 10db0e24-35d1-305d-990e-7aa8969ed3a7 | -19.43717 | -57.21408 | 2026-01-21 04:25:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| f4cbe773-3bdf-31f6-92da-c1d889c92977 | -20.3192 | -57.89386 | 2026-01-21 04:25:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 683602f4-c62b-3dd8-a5f8-d51b2bb62d8c | -19.4425 | -57.22106 | 2026-01-21 04:25:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 3ac8e3f8-a051-36c4-b398-86e6534919b9 | -23.80743 | -48.86369 | 2026-01-21 04:25:00 | NOAA-21 | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 0ae783e3-8f46-38c5-994c-47c714832dc4 | -20.72829 | -55.15943 | 2026-01-21 04:25:00 | NOAA-21 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 83c0f0b5-b89b-3952-9981-f8736f4092af | -23.60758 | -48.26347 | 2026-01-21 04:25:00 | NOAA-21 | ITAPETININGA | SÃO PAULO | Brasil | 3522307 | 35 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 860d930b-a7be-3a8c-9e2e-eaa57c1dbf5e | -20.99628 | -48.84433 | 2026-01-21 04:25:00 | NOAA-21 | EMBAÚBA | SÃO PAULO | Brasil | 3514957 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 1b9fd9db-659c-303d-a9ab-4284d93acc0a | -19.43565 | -57.27824 | 2026-01-21 04:25:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 34cf8f0f-7790-3189-962a-8476d6620a5d | -19.43649 | -57.21737 | 2026-01-21 04:25:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 94254348-cad7-3f15-94eb-b279915dfbfd | -26.00391 | -52.44038 | 2026-01-21 04:25:00 | NOAA-21 | CORONEL VIVIDA | PARANÁ | Brasil | 4106506 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 02b42be4-eb44-30bf-8179-35507bca0018 | -23.60484 | -48.25909 | 2026-01-21 04:25:00 | NOAA-21 | ITAPETININGA | SÃO PAULO | Brasil | 3522307 | 35 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 769c119d-7e43-3506-bbcb-a1a05d3c671e | -19.41933 | -57.30008 | 2026-01-21 04:25:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 27bf07ae-93f9-32fb-a3f4-c16a0120cda5 | -19.44435 | -57.26289 | 2026-01-21 04:25:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 169f7691-87c9-322f-89d3-025457b1c31c | -23.60426 | -48.26286 | 2026-01-21 04:25:00 | NOAA-21 | ITAPETININGA | SÃO PAULO | Brasil | 3522307 | 35 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 9dbc25b8-549f-31c5-a4a4-469bb347452b | -20.32447 | -57.89511 | 2026-01-21 04:25:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| f62a86f7-0f2c-33fe-b1fa-9cb03cbf3fb1 | -19.43423 | -57.28486 | 2026-01-21 04:25:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 38dacb3d-b2bf-3eb6-8a78-8b5a7b9dd50d | -19.43806 | -57.21661 | 2026-01-21 04:25:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| e1960e50-62d2-353a-ab3f-e5ab05528f68 | -19.44164 | -57.21857 | 2026-01-21 04:25:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 486012ae-3f74-3885-bdf9-e3937e1df48c | -19.44474 | -57.22963 | 2026-01-21 04:25:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 43094072-cedf-3fd9-954f-40f6586f02e9 | -23.60094 | -48.26226 | 2026-01-21 04:25:00 | NOAA-21 | ITAPETININGA | SÃO PAULO | Brasil | 3522307 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 285ff2ca-d7e7-3945-8ba9-96edbff1143d | -19.2118 | -53.43802 | 2026-01-21 04:25:00 | NOAA-21 | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f7e877f7-a473-357b-827b-0be76fdf8abc | -22.73113 | -49.34194 | 2026-01-21 04:25:00 | NOAA-21 | AGUDOS | SÃO PAULO | Brasil | 3500709 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 43df9a48-097b-3b08-b8b1-6dd84cfd7663 | -20.7298 | -55.15712 | 2026-01-21 04:25:00 | NOAA-21 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 861ca4b2-e899-3b1f-99f5-e51aa69954cd | -23.80413 | -48.86308 | 2026-01-21 04:25:00 | NOAA-21 | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 7c664359-7d48-3517-8a5a-0e118e3e605f | -20.71942 | -48.7874 | 2026-01-21 04:25:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 11ec05e2-bef3-36bb-b95d-043720355d6e | -19.44223 | -57.27282 | 2026-01-21 04:25:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 4253375d-bc0d-39a2-8d76-bc2c98d00508 | -19.44554 | -57.23209 | 2026-01-21 04:25:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| e214611c-5440-30da-972d-f4e074c4e4c0 | -19.66171 | -56.95347 | 2026-01-21 04:25:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| bc572361-cbe1-3d39-a43e-08f40ac5037c | -19.44152 | -57.27613 | 2026-01-21 04:25:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 03d3b979-befe-32f5-a652-fa02ea5ca138 | -19.43636 | -57.27493 | 2026-01-21 04:25:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| fe8e72f9-bb9b-3ae3-850c-ea4115db7855 | -22.84028 | -51.05716 | 2026-01-21 04:25:00 | NOAA-21 | PRIMEIRO DE MAIO | PARANÁ | Brasil | 4120507 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 311e97ac-2e6d-3ae6-858e-d10eb541a261 | -19.4338 | -57.28253 | 2026-01-21 04:25:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 1c61f08e-d611-3846-914f-9db861f7b24c | -20.84436 | -51.73781 | 2026-01-21 04:25:00 | NOAA-21 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 28ae86b1-9f73-3918-a1e5-257c125bfc69 | -19.21511 | -53.44285 | 2026-01-21 04:25:00 | NOAA-21 | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4d2777d6-9ae6-35f4-8ca0-218a93374de2 | -19.42693 | -57.29361 | 2026-01-21 04:25:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 5fc33ddf-03be-39b0-b44e-1532b7f98244 | -19.38661 | -57.27505 | 2026-01-21 04:25:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 9857b5d4-5916-3495-87b8-92804d4446da | -22.88416 | -47.26366 | 2026-01-21 04:25:00 | NOAA-21 | SUMARÉ | SÃO PAULO | Brasil | 3552403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 739008b0-dc90-3773-b4e9-de7818ada372 | -19.41962 | -57.30238 | 2026-01-21 04:25:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| cf62500e-7d82-303d-bd38-af7adecad858 | -19.42657 | -57.29129 | 2026-01-21 04:25:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| e490becc-284d-33e5-8a90-679dd4253b92 | -19.6697 | -56.89003 | 2026-01-21 04:25:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 4e6ae08d-23cc-3ea3-b0f4-d0e15b47f4c2 | -20.36283 | -57.89699 | 2026-01-21 04:25:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |


[Clique aqui para ver as próximas entradas](README3.md)
