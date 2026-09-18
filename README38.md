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

## Dados Diários - Página 38

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1ed02887-476c-354f-bbd6-7e1f442c1892 | -4.36127 | -47.77775 | 2026-09-18 04:19:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| e5a0ef34-916f-3b7c-bfd4-61cfb6ee0f93 | -5.88618 | -52.08875 | 2026-09-18 04:19:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bd5fbca7-b24e-35db-adf2-b88d238a206d | -5.58432 | -48.10275 | 2026-09-18 04:19:00 | NOAA-21 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bf954868-354d-387a-be13-9945288db8a0 | -7.10775 | -41.81756 | 2026-09-18 04:19:00 | NOAA-21 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 4f1adaae-a713-3cbc-bd00-a5b3a0015c1a | -6.29977 | -41.79438 | 2026-09-18 04:19:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 1865d7ad-d2cc-3b68-8dbb-affe46bdfce6 | -3.37438 | -50.46586 | 2026-09-18 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c2aa39fb-f7b4-3e55-8d5a-df4af80d7691 | -7.0529 | -42.05832 | 2026-09-18 04:19:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 55e5bd99-8814-3caf-87bd-2a06d0c9dacf | -2.96599 | -52.1454 | 2026-09-18 04:19:00 | NOAA-21 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 97b1fee3-8a7f-3f2e-b88b-734b188de7ea | -4.57082 | -42.95361 | 2026-09-18 04:19:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 18.0 |
| b20ecb90-6f3c-3d71-8c65-d88e674fda93 | -5.77838 | -47.2915 | 2026-09-18 04:19:00 | NOAA-21 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0724ac4f-4a64-36a7-b450-8b9a06ac5b22 | -6.93254 | -46.15432 | 2026-09-18 04:19:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 80809cbe-0a0c-34c8-9221-a01e2bf9ab0a | -3.49558 | -43.31409 | 2026-09-18 04:19:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 26da6345-6fa1-3ced-bf5d-10b5033c15b9 | -2.8954 | -54.18764 | 2026-09-18 04:19:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 520dcbc7-415e-35bd-9dee-a49de13993ca | -7.09734 | -43.58846 | 2026-09-18 04:19:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3a5c36db-b3e5-34fe-9e05-ef4fe3a92d79 | -7.00854 | -43.63774 | 2026-09-18 04:19:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d95000d0-e550-3e24-9611-a5bce7532138 | -2.61083 | -54.75198 | 2026-09-18 04:19:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 33.5 |
| b73b1b45-38d5-345a-8124-913345c7a4c1 | -3.37418 | -50.43987 | 2026-09-18 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d7e12671-f779-3324-8585-8984281629b3 | -4.57701 | -42.95826 | 2026-09-18 04:19:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| e69d1648-447f-3215-8ecf-d89d400a06f7 | -7.79283 | -44.87813 | 2026-09-18 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| dc610087-2176-3b69-bb21-3ea7eb78912a | -1.1505 | -54.16806 | 2026-09-18 04:19:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 392f5831-33c8-3e5f-8fc7-1849096362d7 | -7.65965 | -45.8377 | 2026-09-18 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 500ee62c-7152-3a5a-877b-e211fde49903 | -7.8039 | -44.89404 | 2026-09-18 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 91dde1b3-f509-3839-8130-24d31a9c3007 | -4.55396 | -42.95104 | 2026-09-18 04:19:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7a62a58a-94c5-326c-bf43-316459d85b3c | -6.52395 | -49.8888 | 2026-09-18 04:19:00 | NOAA-21 | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 8823b83f-559e-3f52-9609-7d7a96bfb3e4 | -3.26952 | -54.26378 | 2026-09-18 04:19:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bd2c8498-716c-34ee-aa87-4e545f51b2ba | -5.20048 | -42.75509 | 2026-09-18 04:19:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2c81aa59-30b6-39e7-830e-45887205cdb1 | -3.38016 | -50.45807 | 2026-09-18 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 566583b3-ee70-3e5b-8334-00876d735969 | -2.83381 | -50.48375 | 2026-09-18 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8fe198b3-d833-3516-bd1b-d64b537510de | -4.56573 | -42.94177 | 2026-09-18 04:19:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 13a1464c-7447-35f1-879b-94e8cb3b04df | -6.96771 | -42.57256 | 2026-09-18 04:19:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 400f7170-09c1-395e-9304-c40176eba4cc | -2.82785 | -50.46479 | 2026-09-18 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7d5d4ae8-62d6-3699-b276-6f13fe4c9774 | -7.14466 | -42.14618 | 2026-09-18 04:19:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 3cb5938e-36fd-3418-a821-1a6330b1d4c6 | -5.32188 | -45.17069 | 2026-09-18 04:19:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9549df7d-2a3f-31c4-a89a-44a587023a8e | -2.82341 | -49.24234 | 2026-09-18 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 63d17db7-627b-36e9-a9a7-dcbbd9142e3c | -7.00028 | -42.16623 | 2026-09-18 04:19:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| a550357e-3719-396d-b582-88b7fe02096f | -2.29391 | -47.87875 | 2026-09-18 04:19:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0cd8742d-6d9b-3df8-b06e-e14915fbe564 | -5.14918 | -37.72263 | 2026-09-18 04:19:00 | NOAA-21 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.0 |
| f2281459-4966-3724-8247-c7bd34255fb6 | -7.63699 | -45.85207 | 2026-09-18 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c28aefa7-1509-3dd3-a713-ecc0028f0d9e | -4.98514 | -37.39677 | 2026-09-18 04:19:00 | NOAA-21 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 15.7 |
| 15e1701e-e3e8-3121-ba5d-0a9af1968916 | -7.14968 | -42.08886 | 2026-09-18 04:19:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 675f73ec-b821-30b6-ae17-d57426049813 | -6.44151 | -44.95134 | 2026-09-18 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| dcb67bbc-2304-3dd2-819e-4faf5bab06e9 | -3.3275 | -42.86347 | 2026-09-18 04:19:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b5175999-db4d-3071-b3ff-4a58158ea0cd | -7.80774 | -44.8911 | 2026-09-18 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 840ce40e-a21c-340d-b3a3-15b53e952c07 | -6.65135 | -51.48862 | 2026-09-18 04:19:00 | NOAA-21 | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e98b346c-ea6f-380d-8f54-b87308e2ee5c | -6.93589 | -46.15485 | 2026-09-18 04:19:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ff4383da-bd36-3440-b673-17e890af07ae | -2.8257 | -50.47787 | 2026-09-18 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 32274503-5be2-3e19-b336-3e7bdbae71fa | -7.52462 | -44.94212 | 2026-09-18 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| aff7aba3-267b-3774-96bb-3b7ab5f18046 | -4.55843 | -42.94434 | 2026-09-18 04:19:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 5686eedc-2a40-37d2-a541-4d77287e8ce2 | -7.58179 | -46.35286 | 2026-09-18 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0b69e3af-abba-3095-8ce5-983df5f22638 | -7.80443 | -44.89058 | 2026-09-18 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 29c0030d-dc5a-3349-aa21-0b2e1571fa9f | -7.45911 | -46.84107 | 2026-09-18 04:19:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6c9de7c7-a920-3de7-b7f8-26f2df2226d1 | -6.94162 | -43.11374 | 2026-09-18 04:19:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5f3b59a7-2e60-3e14-95a4-a925d178f6e7 | -2.822 | -50.47279 | 2026-09-18 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 39.6 |
| 2059e84f-40a0-3467-a811-d3252ff4b8de | -5.33285 | -45.14404 | 2026-09-18 04:19:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| df7a9611-fbe4-3682-8eea-7915e10caf63 | -7.19498 | -41.8126 | 2026-09-18 04:19:00 | NOAA-21 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| d4b5368e-d24e-3eea-a968-f37a7c9ca484 | -2.05282 | -52.1679 | 2026-09-18 04:19:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 838c2049-e37b-33e5-86d0-6a65ae08fb33 | -4.58713 | -42.9598 | 2026-09-18 04:19:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| e5b8d92c-ad91-3c2b-814d-d7deacc85be7 | -7.04687 | -42.07406 | 2026-09-18 04:19:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| fd39c3cc-82ac-3d66-a657-4478a913043d | -4.49487 | -45.9085 | 2026-09-18 04:19:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 67c0830e-2d61-3e14-9ea7-c1286f5657a7 | -6.58844 | -46.7291 | 2026-09-18 04:19:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d8fecfa0-5909-356c-b9b6-2b6e9b3198c5 | -7.80612 | -44.90148 | 2026-09-18 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5725899e-2f2e-36c3-852c-03811be5fc91 | -6.66254 | -43.63236 | 2026-09-18 04:19:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| aec46584-4c6d-3159-95dd-acf9612ad173 | -3.4106 | -39.2837 | 2026-09-18 04:19:00 | NOAA-21 | TRAIRI | CEARÁ | Brasil | 2313500 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| a8666536-464b-3a8d-b4d2-f542d1744a08 | -4.37307 | -55.42574 | 2026-09-18 04:19:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7d236048-df48-327d-b8bd-dd2b36594c94 | -2.37908 | -48.22329 | 2026-09-18 04:19:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0e813671-dfc6-32d0-a60a-dcdd3fe19fe5 | -0.78057 | -47.55528 | 2026-09-18 04:19:00 | NOAA-21 | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 82ce91a6-968b-3661-a755-579c01ad882b | -7.09736 | -41.83736 | 2026-09-18 04:19:00 | NOAA-21 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 87964d59-ba64-3b54-b115-14c78fd40c1e | -7.60876 | -46.62951 | 2026-09-18 04:19:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a0a45c98-66db-3bef-a481-feb375b9d20c | -4.17183 | -54.41065 | 2026-09-18 04:19:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 47299b52-c2d4-3d3e-b4d9-f8d44853508b | -3.91992 | -55.744 | 2026-09-18 04:19:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e871f8b3-9bb6-34f2-a43a-687b094a5f61 | -6.96423 | -42.57205 | 2026-09-18 04:19:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 7076fcb6-638b-3d19-96ad-a7e789bb7b35 | -6.30756 | -41.79139 | 2026-09-18 04:19:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 806c0341-927c-3fe7-b2d5-12ea26e4e415 | -3.63552 | -44.57543 | 2026-09-18 04:19:00 | NOAA-21 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3704be15-369a-32f1-87e1-3931b95684cb | -5.87494 | -53.56208 | 2026-09-18 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8163e947-47b4-38e9-af8a-12cec97579eb | -2.63291 | -48.42812 | 2026-09-18 04:19:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 72909925-9db4-3989-98e5-9ff3324ae373 | -3.04206 | -51.36922 | 2026-09-18 04:19:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 510b29ba-ba96-3ee8-805a-3f8fa083928e | -7.12116 | -42.08456 | 2026-09-18 04:19:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 0e82371f-926a-34f0-953a-5a7bde7214e4 | -5.75481 | -45.10077 | 2026-09-18 04:19:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 3e0e7211-af62-376f-9c17-aaf3368db77f | -7.60597 | -46.62535 | 2026-09-18 04:19:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9206fcb1-5a79-3e2a-8c2d-e5e052eb130f | -4.49544 | -45.90491 | 2026-09-18 04:19:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9521bae1-4123-3c2f-b986-49ef9cb87fe1 | -7.00909 | -43.63416 | 2026-09-18 04:19:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 8.5 |
| acf27dcc-1337-3f94-b10e-deba03ac3fea | -3.33988 | -53.26383 | 2026-09-18 04:19:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 555c337c-942b-3622-82aa-dbf3a28e91df | -3.35829 | -50.45452 | 2026-09-18 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 8b0c3c56-43fd-39b0-924d-df305bfc1449 | -7.4309 | -44.25092 | 2026-09-18 04:19:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a3cf83c2-25c9-3836-93b4-5e73f2359b2d | -7.80005 | -44.89698 | 2026-09-18 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 09f1bc83-608c-3668-a15b-dabd45b72a63 | -6.37945 | -42.79804 | 2026-09-18 04:19:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 57ab5376-15df-3441-84f9-2738d3c1ea02 | -5.77135 | -45.10333 | 2026-09-18 04:19:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c0c8d515-eb90-3ec1-9bfe-d90ea12c253a | -1.38797 | -49.36915 | 2026-09-18 04:19:00 | NOAA-21 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 14ed4b1c-4481-35a6-a360-96cb2cb1c509 | -2.81686 | -50.4765 | 2026-09-18 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| d3fdf63f-e526-310d-a687-fadf70c73ea6 | -6.27043 | -51.74901 | 2026-09-18 04:19:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bfb538a3-defa-3b3f-ba59-88ffc407a3e2 | -4.56407 | -42.95258 | 2026-09-18 04:19:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 91258bed-4493-35f2-b8d3-e50cb136e5f7 | -6.292 | -41.79738 | 2026-09-18 04:19:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 60482861-f050-30b1-804f-d6ab7110a820 | -4.87882 | -56.0731 | 2026-09-18 04:19:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 4994aef6-dea2-3ca2-bc12-0feb27587261 | -5.19056 | -49.33371 | 2026-09-18 04:19:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7e468bfd-859b-300e-95af-db0d7d5d7aa5 | -3.4986 | -51.25354 | 2026-09-18 04:19:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 74872a17-16b7-3e18-bea7-1a949b552ee5 | -7.07432 | -43.5812 | 2026-09-18 04:19:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f47c6969-76c4-3f0a-bd81-af21d40d88d9 | -5.8744 | -53.56517 | 2026-09-18 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 418895d5-52b4-38ca-a332-18fb6fce6e0e | -6.28841 | -41.79683 | 2026-09-18 04:19:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 48154a6c-8e03-3e38-94e7-1cc2044e3437 | -7.6401 | -44.81178 | 2026-09-18 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 26ad74c4-a74b-3e98-9248-f8ed756aad29 | -4.51794 | -56.078 | 2026-09-18 04:19:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |


[Clique aqui para ver as próximas entradas](README39.md)
