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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cd103add-ed8d-359c-86f4-7ab33e42aad6 | -3.5819 | -47.3403 | 2024-11-09 03:40:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 118.9 |
| 1df4c473-a8c8-3e0a-828c-5206e6352fa1 | -2.2318 | -46.5508 | 2024-11-09 03:40:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 46.6 |
| 66187f12-a06b-3063-acbd-d7132d8cc2e0 | -2.2295 | -53.7832 | 2024-11-09 03:40:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 82.1 |
| 7c23f9e5-7ae0-3a9d-b12a-7c01d67f0827 | -11.0877 | -43.3456 | 2024-11-09 03:40:00 | GOES-16 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 233.6 |
| 9e959ad7-ef49-30e9-9ce4-581174ceae07 | -1.5164 | -52.1696 | 2024-11-09 03:40:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 5d108c65-ef47-37ee-b185-54ddad715e1a | -4.2058 | -48.5491 | 2024-11-09 03:40:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 52.7 |
| a74ebe9c-d989-33d6-91e4-ae84a3535a94 | -3.6003 | -47.3614 | 2024-11-09 03:40:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 148.7 |
| 289b7284-fda2-3779-a2d6-51c34607b0c4 | -11.0685 | -43.3485 | 2024-11-09 03:40:00 | GOES-16 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 82.7 |
| 81975355-9a9b-3187-9ced-d161eadec177 | -3.9854 | -48.1708 | 2024-11-09 03:40:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 112.5 |
| 9d317d3a-d63a-33ef-9c61-06e38d86526e | -4.2487 | -47.5511 | 2024-11-09 03:40:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 2f265673-2036-3589-b0d3-a41e68cbbcd7 | -1.5163 | -52.1901 | 2024-11-09 03:40:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 49.1 |
| 9b80b815-3a6c-375c-b392-7695dbc7dea6 | -2.2295 | -53.7631 | 2024-11-09 03:40:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 63.1 |
| e0045a2a-07be-3a35-aab2-db2cfb068761 | -4.2484 | -47.5947 | 2024-11-09 03:40:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 69.8 |
| 1c444856-696f-313a-bac6-22e6b53d9e9d | -4.15552 | -44.39849 | 2024-11-09 03:40:00 | NOAA-20 | ALTO ALEGRE DO MARANHÃO | MARANHÃO | Brasil | 2100436 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a83bd408-0a90-3e33-9f09-221b626b4b29 | -4.01779 | -46.18985 | 2024-11-09 03:40:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 510229e4-f7a8-31bf-964f-4f1d4c3e3122 | -3.96326 | -48.18406 | 2024-11-09 03:40:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 21cfe60f-ce22-3b4b-9960-d89f3266b6fe | -6.1682 | -43.58828 | 2024-11-09 03:40:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 98d72e41-c380-3951-9135-a5e22b43ee25 | -4.72974 | -43.25486 | 2024-11-09 03:40:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cf64dcf4-7ce9-33be-8cee-462ebd0559a1 | -4.21121 | -46.69719 | 2024-11-09 03:40:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3ddd662b-22a3-38aa-9482-28fc30f6911d | -3.58964 | -47.35074 | 2024-11-09 03:40:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 64.2 |
| 82db3ac8-2ca2-3b9f-bada-d9b5b357248b | -4.20609 | -45.86493 | 2024-11-09 03:40:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 10.0 |
| f3af81f8-2db8-3d38-a810-09e747e0e26d | -7.76603 | -35.39645 | 2024-11-09 03:40:00 | NOAA-20 | BUENOS AIRES | PERNAMBUCO | Brasil | 2602704 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| f1476c55-60b0-3fcf-a0bc-83b71e68cde6 | -6.75904 | -40.53825 | 2024-11-09 03:40:00 | NOAA-20 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 70d06746-ba1b-311a-9efe-61807c6829c3 | -6.21001 | -41.62457 | 2024-11-09 03:40:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 003e345d-1f48-31e8-812a-03318b5408b9 | -5.43872 | -43.25653 | 2024-11-09 03:40:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 67554ef7-cae3-368b-9a0a-d52b5f93046d | -4.94957 | -40.02707 | 2024-11-09 03:40:00 | NOAA-20 | MONSENHOR TABOSA | CEARÁ | Brasil | 2308609 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| b3479a42-cb12-3830-b1e7-3e80de4e499f | -5.47194 | -43.65242 | 2024-11-09 03:40:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 04720752-2520-35ef-99cf-3bf74c47e7de | -5.99672 | -46.09685 | 2024-11-09 03:40:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6ee724bf-9f94-3de4-8ed4-296ed74bff51 | -5.80665 | -44.48281 | 2024-11-09 03:40:00 | NOAA-20 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0f61a778-19f0-3a24-8a54-56e0581309f8 | -4.23357 | -47.56305 | 2024-11-09 03:40:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| c72d7cbd-33ad-3370-89ea-190df8588c87 | -6.54825 | -44.49543 | 2024-11-09 03:40:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 81236b6d-a6ea-3bd4-9938-4209bcc53285 | -2.4532 | -46.32039 | 2024-11-09 03:40:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a65194e7-1a6d-3761-8916-8a89821f9742 | -5.11479 | -37.5687 | 2024-11-09 03:40:00 | NOAA-20 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 33a282c3-9f0a-38be-a265-d97f791994da | -3.5963 | -47.35217 | 2024-11-09 03:40:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 64.2 |
| 74da28f8-3a42-341f-ad01-a4c9e35fb112 | -6.35725 | -40.49485 | 2024-11-09 03:40:00 | NOAA-20 | PARAMBU | CEARÁ | Brasil | 2310308 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| a54d2b02-e7c7-3f26-a507-bc3761567d8b | -6.18027 | -45.44942 | 2024-11-09 03:40:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 71be60ac-a185-3f7b-a504-38a1993194db | -3.96231 | -48.17873 | 2024-11-09 03:40:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 2cb64972-2312-30fa-bb00-8792b2a49d59 | -6.76312 | -40.53894 | 2024-11-09 03:40:00 | NOAA-20 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 0ce0e447-98ee-348a-97f4-bcec2c57275a | -6.21149 | -41.67003 | 2024-11-09 03:40:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 046b2171-2c3f-35fd-8c06-951ee30fd006 | -5.46936 | -43.65779 | 2024-11-09 03:40:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| b1df6dd1-ca3b-30c5-bdf8-aa103b602b11 | -2.97139 | -47.93185 | 2024-11-09 03:40:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 88fab9fb-4ef3-3652-b598-fc071472d3a4 | -3.9644 | -48.17743 | 2024-11-09 03:40:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 66674d77-9642-343e-9327-33bdf670ebc9 | -4.82682 | -47.32581 | 2024-11-09 03:40:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 74e7c3b6-4652-3391-a798-41bb2dfe0d07 | -3.54972 | -47.38105 | 2024-11-09 03:40:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| caa2807a-ba3d-389b-a858-7dcdf931a206 | -4.1224 | -43.59387 | 2024-11-09 03:40:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4f5f9bb3-4d83-331c-b747-1c2ab5da0dda | -3.95138 | -48.16922 | 2024-11-09 03:40:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 9c4962b1-1775-345f-a901-b9afaf69323b | -3.55894 | -43.57829 | 2024-11-09 03:40:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2401ea0f-283e-300c-b27e-9152947f9315 | -5.14131 | -46.21392 | 2024-11-09 03:40:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1d840be1-0728-3f84-a85f-2c75871ef381 | -2.63007 | -46.77128 | 2024-11-09 03:40:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 12fcf1a8-18b8-31d7-ba3b-aceb6b941616 | -6.1738 | -45.45258 | 2024-11-09 03:40:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 5b76cfb5-0985-3ff5-96de-7000acdc9a8e | -6.16306 | -43.5878 | 2024-11-09 03:40:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 65049d79-2a7c-3b74-aef5-36daaf2ff287 | -2.08837 | -46.34592 | 2024-11-09 03:40:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4a40fede-c6ad-38db-b88d-dda0ae6cb145 | -4.20494 | -46.69538 | 2024-11-09 03:40:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f240860e-73eb-3491-bad9-ac52e138fdc0 | -4.62402 | -46.54465 | 2024-11-09 03:40:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| ba5545c8-efad-3453-af91-56b19b488818 | -6.19655 | -43.42596 | 2024-11-09 03:40:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0dc90656-34b5-3e8a-9ddf-f8288c7b6800 | -3.5549 | -43.57736 | 2024-11-09 03:40:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| fc0638fb-fe46-35d1-9bd6-1beb18d0043a | -6.17453 | -45.44844 | 2024-11-09 03:40:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 8fbfd4db-6b28-32b0-873a-e94881392274 | -5.6487 | -42.72916 | 2024-11-09 03:40:00 | NOAA-20 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 55f4761c-bf49-3bb0-86fb-df21ca4780ae | -6.59027 | -39.60691 | 2024-11-09 03:40:00 | NOAA-20 | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 3eab5079-d0cb-3e71-8b17-00d91cba0de7 | -5.72771 | -42.00023 | 2024-11-09 03:40:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 033eeeb0-a41a-3169-b6fa-b3008f3429b9 | -6.98554 | -40.03903 | 2024-11-09 03:40:00 | NOAA-20 | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| edfee26a-6f51-3a04-9556-3418828f9c55 | -4.80597 | -44.93442 | 2024-11-09 03:40:00 | NOAA-20 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a819b287-7615-3052-884f-59a1e11592fd | -3.95842 | -48.17024 | 2024-11-09 03:40:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| b6112664-9b0a-33aa-8abc-1ccc2a778499 | -4.5085 | -45.68769 | 2024-11-09 03:40:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e752ba6a-6fff-3f23-9e41-36a67332e8b6 | -5.17005 | -45.28313 | 2024-11-09 03:40:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 92874a30-0179-352a-8512-fba9eed77996 | -5.73405 | -43.51005 | 2024-11-09 03:40:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 06bdccd4-e62c-3979-b063-757b63e26ccc | -2.17176 | -46.44669 | 2024-11-09 03:40:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a492cb7c-e1e2-3035-bcb8-70c52bb698e6 | -3.833 | -46.4898 | 2024-11-09 03:40:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 6cc455ff-a557-3c11-80f9-35d29853a0f8 | -2.45416 | -46.31474 | 2024-11-09 03:40:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 7706c31a-b6a2-3507-a7d4-9a529ffc198f | -6.90689 | -40.20199 | 2024-11-09 03:40:00 | NOAA-20 | CAMPOS SALES | CEARÁ | Brasil | 2302701 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 7b9bc2b3-d7fb-38f3-8c7b-19fd94729606 | -3.24674 | -46.47645 | 2024-11-09 03:40:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 45f93b42-0593-3f67-a075-0af2facae8cb | -6.18485 | -41.88373 | 2024-11-09 03:40:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| fb9dc373-47b5-354b-b05d-c8f07642d335 | -4.62491 | -46.53952 | 2024-11-09 03:40:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 48d96e09-2d3b-3c70-b0a7-16f8f69141e7 | -3.95635 | -48.17165 | 2024-11-09 03:40:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| cfedc689-15f7-330b-8b20-884b9868b590 | -6.30336 | -35.06198 | 2024-11-09 03:40:00 | NOAA-20 | VILA FLOR | RIO GRANDE DO NORTE | Brasil | 2415008 | 24 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| 8008d490-25e8-3b69-8419-50c8db27bfba | -5.59116 | -37.87001 | 2024-11-09 03:40:00 | NOAA-20 | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 5cbb5578-57a5-3251-b876-b82a9bb5c4cc | -5.83923 | -39.62949 | 2024-11-09 03:40:00 | NOAA-20 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 386ea878-5d6a-38cc-be97-ab5f8914eedc | -3.29101 | -46.4186 | 2024-11-09 03:40:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 12.1 |
| c28bf3ca-72e4-381e-8d2f-ab5ef39f3c3d | -4.60273 | -46.62977 | 2024-11-09 03:40:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8f0784f8-dd41-3a88-ab73-8e56c8c3ee18 | -3.96689 | -48.19357 | 2024-11-09 03:40:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 18.9 |
| 712a31aa-1ac7-3653-a356-1ce0ee610004 | -3.26581 | -46.32472 | 2024-11-09 03:40:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d8ae3030-49b2-3148-9c75-a2788e4294c4 | -2.42039 | -46.31335 | 2024-11-09 03:40:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 1e6ebbd3-ef48-32c3-8e2a-81c4cf64ed0a | -3.26036 | -46.31838 | 2024-11-09 03:40:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 87c16610-40a9-33ca-aab6-0375fc38f628 | -4.19844 | -45.87309 | 2024-11-09 03:40:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 375896d9-f920-3948-8f7b-3f45a8914c18 | -5.17287 | -44.00898 | 2024-11-09 03:40:00 | NOAA-20 | SENADOR ALEXANDRE COSTA | MARANHÃO | Brasil | 2111748 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dd4cd80f-6693-3d58-ac14-849404812e5f | -1.76222 | -45.61538 | 2024-11-09 03:40:00 | NOAA-20 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9a4467f4-5e20-3266-812d-dd469abfad98 | -5.16429 | -45.28203 | 2024-11-09 03:40:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b51b5203-6f06-3e13-9874-7a08a08f10d3 | -3.59174 | -42.84218 | 2024-11-09 03:40:00 | NOAA-20 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| de9232a9-4161-387d-b39c-16a0ea8622b2 | -6.24827 | -39.71012 | 2024-11-09 03:40:00 | NOAA-20 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 020e1d99-e284-3cca-862a-95c55d8169f5 | -4.61766 | -46.54395 | 2024-11-09 03:40:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 39fddf6f-4757-35d1-9ce7-9f25d1509ddc | -3.29068 | -43.54423 | 2024-11-09 03:40:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9645a537-0df5-3982-9b19-849c020e9099 | -6.20303 | -42.08335 | 2024-11-09 03:40:00 | NOAA-20 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 157ca15e-28e4-3bc1-9d75-2705a89fbc50 | -6.2314 | -47.28474 | 2024-11-09 03:40:00 | NOAA-20 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7c1e21c1-e7a6-3af1-bf21-d4bd8d5bd021 | -4.24294 | -47.58905 | 2024-11-09 03:40:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 21.8 |
| 60caa2e0-cd40-3307-9ecb-291895394be2 | -5.4422 | -43.26619 | 2024-11-09 03:40:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 1c00b16c-9da3-395e-b635-e2b1187d1c3a | -7.2405 | -38.9214 | 2024-11-09 03:40:00 | NOAA-20 | MILAGRES | CEARÁ | Brasil | 2308302 | 23 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 340a0daa-4184-3b44-88bd-475fdb146291 | -5.80603 | -44.48633 | 2024-11-09 03:40:00 | NOAA-20 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 749c60fd-08f3-3e20-a609-7c695007c356 | -4.83891 | -45.64011 | 2024-11-09 03:40:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d67e3756-5feb-3071-97c3-1e86d764fe0b | -5.44724 | -43.26694 | 2024-11-09 03:40:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 54a18a39-4b20-3a82-98fb-a9a13e3ab298 | -3.26128 | -46.31292 | 2024-11-09 03:40:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |


[Clique aqui para ver as próximas entradas](README19.md)
