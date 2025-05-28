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
| de9b4d2f-0f6a-336a-8630-6a67ecc28d2e | -9.4387 | -40.3419 | 2025-05-28 01:20:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 139.3 |
| 9e17b891-6f61-3bad-a22d-94844738e117 | -17.284 | -42.6479 | 2025-05-28 01:20:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 151.4 |
| 94edde43-3796-3a5b-b0b9-e5407e3875d8 | -11.8176 | -44.2938 | 2025-05-28 01:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 38.2 |
| d4cad1bb-f09a-3d29-8102-e724810aeff3 | -6.2038 | -43.3475 | 2025-05-28 01:30:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 49.4 |
| 576f2f6f-ef20-3c27-b0cd-aa873b81fe7b | -7.6762 | -46.0995 | 2025-05-28 01:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 90.7 |
| 39f645fd-7dea-3e3d-99cc-e1be17cb3a0c | -7.2025 | -43.1171 | 2025-05-28 01:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 87.2 |
| 157d2840-76ed-33e3-96e3-b3b51868f7b1 | -11.4062 | -44.82 | 2025-05-28 01:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 65.1 |
| a4e96b95-cd50-34ae-834b-d3cb64db58a8 | -17.284 | -42.6479 | 2025-05-28 01:30:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 156.7 |
| 97b7aadb-b565-3102-b732-b85b818361f7 | -10.2539 | -52.2246 | 2025-05-28 01:30:00 | GOES-19 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 57.2 |
| b8ea1f5e-bf70-3d61-886e-3cb420233f57 | -10.235 | -52.2263 | 2025-05-28 01:30:00 | GOES-19 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 4b4d8277-e12a-3907-a6e3-b55b9281a8a3 | -6.2226 | -43.3459 | 2025-05-28 01:30:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 59.8 |
| 95706f43-d429-3ac1-a988-3f199455e374 | -11.818 | -44.2703 | 2025-05-28 01:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 94.3 |
| 917a670c-ddec-3750-9e8f-2e417ad34086 | -17.284 | -42.6479 | 2025-05-28 01:40:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 118.3 |
| 0f49b44d-a2ab-3276-baac-e737f29aa3e8 | -11.818 | -44.2703 | 2025-05-28 01:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 88.2 |
| e11e64b2-c1f0-3ba0-b4d7-5de273dede1b | -7.6762 | -46.0995 | 2025-05-28 01:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 101.7 |
| e2cc4d3e-6059-32a8-882a-c11b1906944d | -10.235 | -52.2263 | 2025-05-28 01:40:00 | GOES-19 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 568ee0eb-741e-307f-995d-288720524c07 | -10.2539 | -52.2246 | 2025-05-28 01:40:00 | GOES-19 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 3bf06b5d-b417-3b07-94b8-57e3ce099e2f | -6.2226 | -43.3459 | 2025-05-28 01:40:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 63.4 |
| 23f11614-32d5-3591-9388-560e0f069c6a | -7.695 | -46.0978 | 2025-05-28 01:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 54.5 |
| 71aa3083-1c76-38b5-a5c4-b47d97d2c408 | -7.2025 | -43.1171 | 2025-05-28 01:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 69.9 |
| ed61dca0-b621-3e3b-b9cb-d4fbadb022fd | -7.695 | -46.0978 | 2025-05-28 01:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 51.5 |
| da771bb4-b330-30aa-a60d-353e157d6900 | -7.2025 | -43.1171 | 2025-05-28 01:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 63.6 |
| 73bed7aa-dfd6-3405-937f-5d44d2f52d51 | -17.284 | -42.6479 | 2025-05-28 01:50:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 108.8 |
| 234c4ff2-0fea-3a6e-9bcf-a834446048f9 | -7.6762 | -46.0995 | 2025-05-28 01:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 97.9 |
| 1894f5ce-eda9-39cb-82b5-f0486822ca49 | -11.818 | -44.2703 | 2025-05-28 01:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 91.8 |
| a4675ccf-f6d7-3221-b7c9-eb4d807bd810 | -6.2226 | -43.3459 | 2025-05-28 01:50:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 59.7 |
| bb7c756e-cbaa-3545-b6cb-a20ca697eec4 | -9.62508 | -67.2677 | 2025-05-28 01:56:00 | TERRA_M-M | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 6.4 |
| ee21f1d7-b1fa-3db4-99b8-cdb817c4a7a6 | -9.61625 | -67.26897 | 2025-05-28 01:56:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| d8720d63-def6-325c-a191-9965b615e8a6 | -7.2025 | -43.1171 | 2025-05-28 02:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 63.7 |
| 7964a371-76bd-3b20-b571-f6f702114f68 | -6.2226 | -43.3459 | 2025-05-28 02:00:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 63.8 |
| 5bf9954a-cd60-36c8-85c9-baa6bb18a976 | -7.6762 | -46.0995 | 2025-05-28 02:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 83.1 |
| 030849c1-a339-3eab-bbc2-6f508b239a41 | -17.284 | -42.6479 | 2025-05-28 02:00:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 134.0 |
| e7ce333c-d127-3891-a693-33bad1588289 | -10.235 | -52.2263 | 2025-05-28 02:00:00 | GOES-19 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 43289b64-404d-336b-aba7-47874d647308 | -11.818 | -44.2703 | 2025-05-28 02:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 115.1 |
| c8ff3f27-25f2-325e-a069-11141e0d81c3 | -17.284 | -42.6479 | 2025-05-28 02:10:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 119.6 |
| 167d772f-21f6-3bd4-a52c-1d9cc1f52415 | -10.235 | -52.2263 | 2025-05-28 02:10:00 | GOES-19 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 65.5 |
| c642cac9-6b93-3406-9122-99624d04fa0a | -7.6762 | -46.0995 | 2025-05-28 02:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 104.8 |
| 8ce73e1b-b787-3eab-8ed9-e9708dbfb976 | -6.2038 | -43.3475 | 2025-05-28 02:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 59.2 |
| ec7c3303-edbb-3f22-8eb7-97a19ff412c2 | -7.2025 | -43.1171 | 2025-05-28 02:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 62.4 |
| 6936734c-0fcb-3800-942a-1a144636c34e | -11.818 | -44.2703 | 2025-05-28 02:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 67.1 |
| 8da6550c-8e1d-384f-b578-d92b8d6aedb4 | -11.818 | -44.2703 | 2025-05-28 02:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 60.6 |
| 2eb488a0-990f-390f-89d1-c26cd66be708 | -7.6762 | -46.0995 | 2025-05-28 02:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 91.6 |
| dcfece93-55e4-3e31-8fc1-60378438209f | -17.284 | -42.6479 | 2025-05-28 02:20:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 87.6 |
| e319cea2-7159-32d8-819f-09e5387c09eb | -6.2226 | -43.3459 | 2025-05-28 02:20:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 56.4 |
| 1f387928-3ba9-35cd-aea0-f0858f232964 | -17.284 | -42.6479 | 2025-05-28 02:30:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 83.1 |
| 9331051d-1560-3d74-8c3a-44c2989dac08 | -7.6762 | -46.0995 | 2025-05-28 02:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 79.3 |
| 7b1c9b8c-00fe-31ff-9fdb-da7d2a3b069a | -6.2226 | -43.3459 | 2025-05-28 02:30:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 61.5 |
| ceaa092d-bb5a-3ad1-b2b4-5584272df454 | -11.818 | -44.2703 | 2025-05-28 02:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 118.8 |
| 930fc24e-eb1e-33bc-b77e-f9be3766ac88 | -17.284 | -42.6479 | 2025-05-28 02:40:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 83.8 |
| c34dff9a-2e5f-3d7a-8b52-1c5bea7156cc | -11.818 | -44.2703 | 2025-05-28 02:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 94.1 |
| 9832a288-74cc-388f-9684-38fa96195655 | -6.2038 | -43.3475 | 2025-05-28 02:40:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 58.8 |
| 32867816-078a-36e5-a9e6-99a454511a83 | -7.6762 | -46.0995 | 2025-05-28 02:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 86.5 |
| 62fca2f2-e3c4-3e18-adee-76837ddc4d1a | -11.818 | -44.2703 | 2025-05-28 02:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 106.4 |
| 4921a7b1-a40b-3599-9875-af7ab6491bbe | -17.284 | -42.6479 | 2025-05-28 02:50:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 78.8 |
| cc34044a-1463-3bc4-ac92-d3da6aee797f | -7.6762 | -46.0995 | 2025-05-28 02:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 83.5 |
| 6984dda7-b6b7-3289-bc1f-e4561b0d1930 | -17.284 | -42.6479 | 2025-05-28 03:00:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 81.0 |
| 2e5c19ee-9218-35a1-a1ed-5f63f39ba252 | -7.6762 | -46.0995 | 2025-05-28 03:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 83.1 |
| 5cf8644a-1d91-3799-9bad-8855120997a2 | -11.818 | -44.2703 | 2025-05-28 03:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 90.1 |
| 4972a985-46b4-30bb-88a7-432bb5985612 | -17.284 | -42.6479 | 2025-05-28 03:10:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 66.2 |
| cd8ee6c6-cb09-363c-ba77-bef8223dc631 | -6.2038 | -43.3475 | 2025-05-28 03:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 53.9 |
| 6113dfd2-41a0-30e0-b0ab-69b90653e6e5 | -7.6762 | -46.0995 | 2025-05-28 03:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 106.9 |
| e1f0dd97-b3be-3732-8e38-0f2c85289df8 | -11.818 | -44.2703 | 2025-05-28 03:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 84.8 |
| 49f2efcd-4c8c-3896-a5a5-61fd7eb52506 | -11.818 | -44.2703 | 2025-05-28 03:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 77.2 |
| 869fd5f8-f846-3638-a94f-d213d0dab225 | -7.6762 | -46.0995 | 2025-05-28 03:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 103.1 |
| 9ecad6aa-9e35-3bcd-9d75-09374d00563e | -6.2038 | -43.3475 | 2025-05-28 03:20:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 51.9 |
| 6de93247-3913-33c8-a8d1-603c6842b1af | -11.818 | -44.2703 | 2025-05-28 03:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 93.0 |
| eb930d0e-b4ed-3d34-b4b5-ac4a5f74ceeb | -7.6762 | -46.0995 | 2025-05-28 03:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 95.4 |
| fd19827e-61b5-384a-bf5f-3ae13b14b6aa | -7.6762 | -46.0995 | 2025-05-28 03:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 117.7 |
| ec5cad12-559d-323d-8b6c-56032bf23d39 | -11.818 | -44.2703 | 2025-05-28 03:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 78.4 |
| ef31c54b-92a6-3526-b0c8-acbc1e80c184 | -3.13003 | -40.98962 | 2025-05-28 03:40:00 | NOAA-21 | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 6dc0dbb6-d1a1-3cf4-9c17-e292094d9d1a | -6.5078 | -43.64083 | 2025-05-28 03:42:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 452ee43f-b5e0-3ef2-8d6e-82b0cedb194c | -5.77149 | -43.48978 | 2025-05-28 03:42:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e03f0d4c-bd31-3da3-a05d-e4c94e30a451 | -9.18229 | -40.31284 | 2025-05-28 03:42:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 0d4769fd-6a3f-3dea-8203-e62d6b66fe5f | -5.76184 | -43.48537 | 2025-05-28 03:42:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f4bfc4a4-0703-3a0f-aeaa-fadf11e6d50b | -7.60559 | -46.64789 | 2025-05-28 03:42:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0c2dd974-9f8c-39bc-b7cc-7d4eb19fe216 | -7.08155 | -46.05402 | 2025-05-28 03:42:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 2d71181b-ceb9-30f7-a782-92ba22886949 | -6.61478 | -48.02259 | 2025-05-28 03:42:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9a1ea78c-e41d-3991-a835-ac881507f823 | -7.21269 | -43.11404 | 2025-05-28 03:42:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| d0e4214e-eea5-3753-97b5-293082f107a2 | -6.12574 | -43.94823 | 2025-05-28 03:42:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ab7e6aa0-f784-3ddc-a800-4274dc416071 | -5.6462 | -43.59096 | 2025-05-28 03:42:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| afa67822-5c57-36dc-b8df-86c7ae21c7b5 | -6.21788 | -43.34806 | 2025-05-28 03:42:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 17.5 |
| da693d0d-d578-3eef-a954-35890a1e3c27 | -7.22231 | -43.11562 | 2025-05-28 03:42:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 5614eadd-8ff4-39ed-b123-b2e1b7fdfe3b | -6.1195 | -43.9535 | 2025-05-28 03:42:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 887d9440-3558-37d1-9c2e-949cff541138 | -7.68485 | -46.09734 | 2025-05-28 03:42:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 22.8 |
| f2e1e345-8e18-3dbd-a9f7-4a296acd5ab0 | -7.62583 | -45.76054 | 2025-05-28 03:42:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| c0b63413-af1d-3a02-a04b-b4d612b3500f | -7.99811 | -46.15332 | 2025-05-28 03:42:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ab0ec5cc-84b4-3a97-9b1e-394f46aa6baf | -7.96009 | -45.93883 | 2025-05-28 03:42:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c419e759-e5d1-3a2c-a180-115cf1c705b7 | -7.20788 | -43.11326 | 2025-05-28 03:42:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 472576eb-23ad-34c5-a8ab-4d1e1b477046 | -6.63348 | -43.21435 | 2025-05-28 03:42:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 3d33dba7-fc0e-3600-9cea-f8d518039abb | -6.32631 | -43.37621 | 2025-05-28 03:42:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 58a4022e-5e14-31ba-9ace-0ea139da4356 | -7.67248 | -46.09944 | 2025-05-28 03:42:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 26.3 |
| 2592b31a-405b-314e-8ce8-186c64ea1579 | -7.68476 | -46.09674 | 2025-05-28 03:42:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 24.5 |
| 7a1355db-fee3-3c1f-819c-7dc6b3fb9813 | -7.67397 | -46.09121 | 2025-05-28 03:42:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 13.5 |
| b474bb5a-9713-31d3-9899-3a3bdfd98b2c | -6.12055 | -43.94742 | 2025-05-28 03:42:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f3d8c3f4-885f-36f0-bf92-bb31afaab123 | -6.33177 | -43.37414 | 2025-05-28 03:42:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2995f175-6b6b-3924-b248-474a4a87ac75 | -6.31685 | -43.37176 | 2025-05-28 03:42:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0b8ccda3-e094-3c1a-852a-56486dae720c | -6.32183 | -43.37252 | 2025-05-28 03:42:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 32ee3827-7886-3d45-9391-63cb6e7a95e2 | -7.19345 | -43.11081 | 2025-05-28 03:42:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 10.4 |
| 1c9ec43c-fa1e-35c7-83ad-51b25b064b3f | -5.78464 | -43.61663 | 2025-05-28 03:42:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4796ebdf-7f4b-30df-b72b-466e0e66830c | -5.76235 | -43.4824 | 2025-05-28 03:42:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README4.md)
