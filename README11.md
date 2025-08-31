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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e43d3260-5f26-3d1e-b599-d8c14d405d2a | -10.9512 | -50.8509 | 2025-08-31 02:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 107.2 |
| 972cdb3e-8095-3f3e-901a-17916a9f6c01 | -9.0799 | -65.4349 | 2025-08-31 02:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 52.6 |
| 9796f464-1799-37f4-86fa-81a5c8633479 | -18.6715 | -49.102 | 2025-08-31 02:10:00 | GOES-19 | CENTRALINA | MINAS GERAIS | Brasil | 3115805 | 31 | 33 | nan | nan | nan | Cerrado | 52.2 |
| 1b40a021-273e-3b9d-a41e-07b186857a81 | -9.5913 | -40.3448 | 2025-08-31 02:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 155.0 |
| 20311929-1d5b-3a0e-8f14-a2aaa1e8e0c1 | -8.6539 | -61.9457 | 2025-08-31 02:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 87.4 |
| 04638816-077c-39d0-9677-a7d0d5b36578 | -6.7093 | -51.4165 | 2025-08-31 02:10:00 | GOES-19 | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 75.4 |
| c88ec41a-f71f-38f4-b41e-daaa249ff43d | -8.744 | -62.379 | 2025-08-31 02:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 74.8 |
| e3247dac-27d0-3608-87ae-62c600166765 | -7.0951 | -44.3128 | 2025-08-31 02:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 80.5 |
| 7c034093-d102-399b-9259-e7b0e97e9757 | -8.6538 | -61.9647 | 2025-08-31 02:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 139.1 |
| 396d4cc0-7f5e-3dfb-81d1-46dc8c97fc39 | -10.9515 | -50.8296 | 2025-08-31 02:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 93.6 |
| a783dd49-897d-36f7-bdd6-ca288daf679e | -11.3696 | -43.6341 | 2025-08-31 02:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 50.9 |
| f01b0e6f-874d-346a-b931-dbcf10863a17 | -14.5452 | -51.9729 | 2025-08-31 02:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 68.6 |
| 34cbae66-050b-3c3e-a5d4-f9ca8369b14d | -10.7567 | -59.8175 | 2025-08-31 02:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 67.6 |
| 2553ede2-3486-34ef-a86e-e3b576c51a03 | -8.6353 | -61.9655 | 2025-08-31 02:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 51.4 |
| a9ecf205-ebc6-35ba-8adb-c0071c97e2bf | -9.4433 | -60.5499 | 2025-08-31 02:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 51.2 |
| e41367bd-de9c-3a9d-9bdc-3eb27eafb962 | -7.1139 | -44.3111 | 2025-08-31 02:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 82.1 |
| 983ba1bf-7aae-393d-afde-61c9130ddd38 | -9.0614 | -65.4355 | 2025-08-31 02:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 296227a8-567d-3820-ac4e-70e36c4ab313 | -18.672 | -49.0793 | 2025-08-31 02:10:00 | GOES-19 | CENTRALINA | MINAS GERAIS | Brasil | 3115805 | 31 | 33 | nan | nan | nan | Cerrado | 67.7 |
| b46a1d03-3c1e-33de-b927-65d0d41fdb49 | -9.4432 | -60.5692 | 2025-08-31 02:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 122.2 |
| 38c317c0-9698-3819-83f0-67fd23bec377 | -11.3701 | -43.6104 | 2025-08-31 02:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 47.7 |
| 8c65e943-4a80-37b8-b002-377bb8e28077 | -16.2221 | -52.6778 | 2025-08-31 02:10:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 78.9 |
| abc7944b-214b-3ba4-b63e-78f0e3e1cf7f | -11.3504 | -43.637 | 2025-08-31 02:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 128.7 |
| 64a7cbb9-0841-396a-b614-75e229d55263 | -11.9143 | -46.3953 | 2025-08-31 02:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 67.7 |
| ed0646f0-e37e-3ef2-80cc-ca369a6b47ce | -11.4232 | -63.2634 | 2025-08-31 02:10:00 | GOES-19 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 62.5 |
| 0530c074-69fe-3d9a-bc2b-ed79f2492886 | -9.4618 | -60.5682 | 2025-08-31 02:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 62c5c47a-b5ed-3651-b846-3c0574ea3d38 | -9.4431 | -60.5884 | 2025-08-31 02:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 75.1 |
| e31c73e8-d44e-31da-8ce3-883cae5347e8 | -11.3312 | -43.6399 | 2025-08-31 02:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 41.0 |
| 7896f740-746c-3052-b1fa-450334f96f73 | -12.0976 | -44.717 | 2025-08-31 02:10:00 | GOES-19 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 67.0 |
| f4f57d24-b54c-3761-afbc-bee195c65765 | -3.5995 | -47.5142 | 2025-08-31 02:10:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 44f35fcc-0a9f-34d3-8308-12186c331e73 | -8.7439 | -62.3979 | 2025-08-31 02:10:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 135.5 |
| 19a14299-fb10-34b5-ab5d-0f2709747879 | -13.3636 | -46.95 | 2025-08-31 02:10:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 96.5 |
| 041951bf-1da8-360d-85c0-b7390bd62f8f | -12.6298 | -48.1979 | 2025-08-31 02:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 35.1 |
| 502f8a24-97d4-3afc-aa43-22c7ef804bdd | -9.0613 | -65.4542 | 2025-08-31 02:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 48.8 |
| 24002866-c8b1-3a09-8e65-f9bf54d85f0e | -11.4045 | -63.2453 | 2025-08-31 02:10:00 | GOES-19 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 87.3 |
| 57ce725e-6649-33d1-b244-d3d416e1b106 | -16.2225 | -52.6565 | 2025-08-31 02:10:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 64.6 |
| 5408fd6d-be6c-313d-a329-678c78cd55f4 | -11.4233 | -63.2444 | 2025-08-31 02:10:00 | GOES-19 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 78.7 |
| a25e795d-a83a-3d41-aff8-e08e3b34a6de | -10.3126 | -59.2023 | 2025-08-31 02:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 62.7 |
| baf1ea19-54d8-3c81-9002-52ae46b3347b | -9.5908 | -40.3696 | 2025-08-31 02:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 67.6 |
| e4837a33-791a-35be-99eb-516b8fd188ed | -11.3509 | -43.6133 | 2025-08-31 02:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 105.2 |
| 776ceeb5-9a37-339f-9cc4-958bb4cb0c84 | -10.9702 | -50.8489 | 2025-08-31 02:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 97.0 |
| 3325ae73-8f6d-37ff-bd27-ad3f9eb88a05 | -11.4044 | -63.2644 | 2025-08-31 02:10:00 | GOES-19 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 66.4 |
| 72c59f79-f555-37ce-b720-56c1e210b258 | -10.3313 | -59.2011 | 2025-08-31 02:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 59.3 |
| d807ba9d-5519-3813-9d50-9328528e739d | -6.7093 | -51.4165 | 2025-08-31 02:20:00 | GOES-19 | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 72.0 |
| 89085f4b-c67d-3e28-ab35-dab5637cc348 | -10.3126 | -59.2023 | 2025-08-31 02:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 3c043647-5016-3c32-95fd-8629aa6065f7 | -8.7439 | -62.3979 | 2025-08-31 02:20:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 101.5 |
| e8f5dca2-7a3e-3231-95b2-a1e1ac0ad4b0 | -6.1665 | -43.3273 | 2025-08-31 02:20:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 83.0 |
| ba7fb839-8089-3821-87c5-ceb3b0c37fa2 | -14.5456 | -51.9516 | 2025-08-31 02:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 53.3 |
| 6c60ac32-6954-328e-9ed7-21c6362c8720 | -3.5995 | -47.5142 | 2025-08-31 02:20:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 43.1 |
| 046b9a9b-cb22-3eae-a911-24c60fb29968 | -8.744 | -62.379 | 2025-08-31 02:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 69.2 |
| 3c12b7fa-b613-3eb4-89f8-c5e2b26db4c9 | -9.68 | -47.0353 | 2025-08-31 02:20:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 89.6 |
| 177ecf94-fad6-33b4-a77c-d581a7f7feda | -12.0976 | -44.717 | 2025-08-31 02:20:00 | GOES-19 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 59.2 |
| 28dc5072-98fd-3c93-b29d-aeab6b25fd40 | -18.672 | -49.0793 | 2025-08-31 02:20:00 | GOES-19 | CENTRALINA | MINAS GERAIS | Brasil | 3115805 | 31 | 33 | nan | nan | nan | Cerrado | 56.0 |
| cc8f7136-2ae1-3a2d-b8a4-37b42368adf6 | -8.6538 | -61.9647 | 2025-08-31 02:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 1caa57bf-941b-35e8-944a-ca78ad3a8c06 | -9.4618 | -60.5682 | 2025-08-31 02:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 48.7 |
| cb983a48-1973-3082-a8ca-5fcf836b03ef | -9.4432 | -60.5692 | 2025-08-31 02:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 104.3 |
| 7eff9075-51fc-30eb-bb4a-dc2c32fb35c8 | -16.2217 | -52.6992 | 2025-08-31 02:20:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 48.4 |
| a62726ca-aa0a-324a-8362-9c7cc16f7f6e | -10.9512 | -50.8509 | 2025-08-31 02:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 68.6 |
| 2387871c-981d-316f-9f93-887ef1576e0e | -10.3313 | -59.2011 | 2025-08-31 02:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 4cbc63bf-699a-34c5-bd6f-ddff8c4c0534 | -11.3509 | -43.6133 | 2025-08-31 02:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 114.8 |
| d3e12350-e081-3179-b81a-7d09cfd4b10d | -11.3701 | -43.6104 | 2025-08-31 02:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 52.3 |
| 2ddf8569-936b-30d5-85f1-b57e8ae3622f | -13.3636 | -46.95 | 2025-08-31 02:20:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 92.3 |
| 9860cab3-f99f-3eb5-9691-3b4f55641b3d | -7.0951 | -44.3128 | 2025-08-31 02:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 66.5 |
| e074211f-e8b9-3dd5-8940-14ef29bf19bd | -16.2221 | -52.6778 | 2025-08-31 02:20:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 77cf282b-ebd3-3eaa-b96c-cb1d12071f48 | -11.3504 | -43.637 | 2025-08-31 02:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 118.5 |
| f399dd3a-fe42-3bf2-8635-d88f9dbd6aa8 | -9.6989 | -47.0332 | 2025-08-31 02:20:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 110.5 |
| 0871a7d5-5c4b-30d3-b670-526a6726fd18 | -11.3696 | -43.6341 | 2025-08-31 02:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 41.8 |
| 116501ae-23c7-334b-9aa0-add54ed61c30 | -10.6128 | -44.3284 | 2025-08-31 02:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 60.0 |
| c7e00ff9-e2d1-3c74-9fe8-1ef910dbf8e8 | -10.9699 | -50.8702 | 2025-08-31 02:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 66.6 |
| 7c4b2026-6c6a-3ba7-ac76-c61aed8a96de | -11.3112 | -43.69 | 2025-08-31 02:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 32.0 |
| d86b8958-bab9-31e7-a7d6-d2c78ed8506d | -9.4431 | -60.5884 | 2025-08-31 02:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 62.1 |
| 89b201fe-399d-3d3f-bb2f-a69a6d0a19dd | -10.9702 | -50.8489 | 2025-08-31 02:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 103.0 |
| f48423ed-6165-3142-9cc7-b616aeeabae2 | -14.5448 | -51.9943 | 2025-08-31 02:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 63.9 |
| 6cf241f3-17bd-3d19-9fde-7baa5b92904b | -6.1853 | -43.3257 | 2025-08-31 02:20:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 76.3 |
| ab8d642b-2370-3a03-a684-6bbe9bcdd44d | -14.5452 | -51.9729 | 2025-08-31 02:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 124.5 |
| 32cb7114-ce19-3cb8-aa65-93ff3af3407f | -10.7567 | -59.8175 | 2025-08-31 02:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 57.4 |
| f6bb2e0c-5bf3-3f95-8eee-6ea28ceb834b | -9.6797 | -47.0576 | 2025-08-31 02:20:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 85.5 |
| 76adf8e6-31d8-30ae-bc59-31116d7ebe89 | -9.6986 | -47.0555 | 2025-08-31 02:20:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 102.3 |
| 7a95fb06-dde5-3e2d-9777-2d26b5a7982a | -11.8181 | -46.4314 | 2025-08-31 02:20:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 88.3 |
| 5ac52004-4266-3cf8-bc07-03cdd82baa1c | -16.2225 | -52.6565 | 2025-08-31 02:20:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 48.2 |
| 0096724c-d179-3294-937f-294342a956e5 | -11.8177 | -46.4541 | 2025-08-31 02:20:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 87.6 |
| 9ab3fbac-258a-3b70-8264-8cfbcf08fe99 | -7.1139 | -44.3111 | 2025-08-31 02:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 72.0 |
| 77523120-0bf6-3a05-bbfd-1d42ef607878 | -11.3112 | -43.69 | 2025-08-31 02:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 92.8 |
| fcff6a41-fd3c-3a20-b5a9-7250e87be9f2 | -8.7439 | -62.3979 | 2025-08-31 02:30:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 69.0 |
| 5b749b97-9596-35b5-bc09-7aacc3fe747a | -3.5995 | -47.5142 | 2025-08-31 02:30:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 38.9 |
| caa4b992-f4bb-341b-af0b-155d3f88b892 | -11.3504 | -43.637 | 2025-08-31 02:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 99.4 |
| 8b949975-b8db-3415-be2e-cd29c40aa944 | -10.7567 | -59.8175 | 2025-08-31 02:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 52.1 |
| 3f157432-ec02-303d-b2bd-9fc2ed54f931 | -8.6539 | -61.9457 | 2025-08-31 02:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 79d467be-fc27-3012-8017-19bff3c2200f | -16.2217 | -52.6992 | 2025-08-31 02:30:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 77.1 |
| 37e46898-19d8-3faf-aaae-ae0d91872ed2 | -11.3312 | -43.6399 | 2025-08-31 02:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 42.9 |
| c2cb8268-22ae-36d0-876c-62db24e84e81 | -9.5908 | -40.3696 | 2025-08-31 02:30:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 68.3 |
| 587805fb-2dab-371e-bb69-84a95bc60900 | -8.6538 | -61.9647 | 2025-08-31 02:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 93.8 |
| 60363e01-6689-30ec-836d-2b379e18eee6 | -6.7093 | -51.4165 | 2025-08-31 02:30:00 | GOES-19 | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 71.0 |
| f5c936cd-be62-3c32-8288-d383e69a2f3b | -11.3509 | -43.6133 | 2025-08-31 02:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 107.6 |
| e31fd617-b25d-3e8c-a17d-788f45719547 | -18.672 | -49.0793 | 2025-08-31 02:30:00 | GOES-19 | CENTRALINA | MINAS GERAIS | Brasil | 3115805 | 31 | 33 | nan | nan | nan | Cerrado | 50.8 |
| c96106d8-928f-3863-8508-0f10b7c28f01 | -10.3313 | -59.2011 | 2025-08-31 02:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 58.8 |
| b12776a4-d47c-3f4a-94a6-7e81fd427fee | -12.0976 | -44.717 | 2025-08-31 02:30:00 | GOES-19 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 58.5 |
| d5331e8b-18fa-3d1c-899e-b2abe52fada2 | -6.1853 | -43.3257 | 2025-08-31 02:30:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 70.0 |
| 5a3abdc9-df66-37ec-ae36-16f37aab7ace | -10.6128 | -44.3284 | 2025-08-31 02:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 61.0 |
| d0f663f3-dbd3-38ba-8b8c-9087e8292f5f | -13.3636 | -46.95 | 2025-08-31 02:30:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 93.1 |
| 45d181fc-383d-3336-86c6-fc75936cee30 | -11.8181 | -46.4314 | 2025-08-31 02:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 79.5 |


[Clique aqui para ver as próximas entradas](README12.md)
