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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 85caf23d-f163-3a4c-9cf1-4198ce987d88 | -5.77766 | -43.61329 | 2025-06-10 03:23:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| f3ecd335-5bc8-35e9-a87f-d6416d898266 | -5.21728 | -43.30973 | 2025-06-10 03:23:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 21.7 |
| 89007335-bb1d-3242-a9df-7c252795dee4 | -5.65207 | -43.60383 | 2025-06-10 03:23:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 44e9af39-c19e-3ddc-bf49-1ffe7529a383 | -6.21976 | -43.3264 | 2025-06-10 03:23:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bc81a3d5-54d3-32f1-82ba-bbc463c46d90 | -5.21038 | -43.3088 | 2025-06-10 03:23:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 21.7 |
| def31419-5719-39eb-a125-b6dda2a310be | -5.78218 | -43.62773 | 2025-06-10 03:23:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0a119849-cf4d-33fb-924f-8bf200b829b4 | -2.52248 | -43.25486 | 2025-06-10 03:23:00 | NPP-375D | SANTO AMARO DO MARANHÃO | MARANHÃO | Brasil | 2110278 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 408f80e1-6e9c-360b-8bbf-488ddc5598fb | -6.20517 | -43.32975 | 2025-06-10 03:23:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7d3560da-0caa-3916-be22-cd618f43f2fb | -5.77746 | -43.6106 | 2025-06-10 03:23:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c6f3245b-8627-38a6-a858-d14820b5fac2 | -5.77627 | -43.61694 | 2025-06-10 03:23:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 744022dd-0243-3f76-9e2c-3f4523e6fe49 | -5.77527 | -43.62643 | 2025-06-10 03:23:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.3 |
| f69278c0-47ca-31d9-9f4a-8dcf92573d2f | -7.00667 | -44.62362 | 2025-06-10 03:25:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9b07a3ce-da25-361a-9198-32ccc39bacc6 | -9.5897 | -40.33928 | 2025-06-10 03:25:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 7b1bed2a-0cf8-32c0-810f-25855fde3974 | -9.5844 | -40.33825 | 2025-06-10 03:25:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 5d8f6627-456a-3fc9-a8bd-bd7fc6083408 | -9.595 | -40.34031 | 2025-06-10 03:25:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 233b9f1f-176f-3126-b75e-1258efc418ac | -7.56967 | -37.81417 | 2025-06-10 03:25:00 | NPP-375D | JURU | PARAÍBA | Brasil | 2508000 | 25 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 570f1ef2-612b-31fe-8767-ad809e476b47 | -7.73877 | -44.18093 | 2025-06-10 03:25:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4b53f7d4-74aa-3ad3-a88e-21811b3a26dd | -7.73996 | -44.17478 | 2025-06-10 03:25:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4b3a7aad-ec1a-353c-948e-35d13afac5e1 | -13.65617 | -41.62447 | 2025-06-10 03:25:00 | NPP-375D | RIO DE CONTAS | BAHIA | Brasil | 2926707 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| e6e6b035-23f6-3a31-88df-2866eb5c663a | -13.65679 | -41.6213 | 2025-06-10 03:25:00 | NPP-375D | RIO DE CONTAS | BAHIA | Brasil | 2926707 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| e5e1209f-2ee6-39af-8b6b-69b68dcad888 | -7.01399 | -44.62416 | 2025-06-10 03:25:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 049b5a5c-7ab9-3768-9dda-ab1157f3c564 | -6.21064 | -44.51476 | 2025-06-10 03:25:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7af52b8b-f839-3627-8700-c7fbdfb4a081 | -6.49306 | -42.85259 | 2025-06-10 03:25:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 1f7d8aa5-bf8c-366b-933d-0ea9b7af06b5 | -7.01531 | -44.61708 | 2025-06-10 03:25:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| dc5aaf22-0cfa-36ac-9c30-167e8165a2ee | -7.00934 | -44.61779 | 2025-06-10 03:25:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3ced008f-7d46-3bf8-8037-ab4f76741090 | -7.00796 | -44.62494 | 2025-06-10 03:25:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 5e5fae77-20e7-341f-818a-bdc9091c6fd0 | -6.21211 | -44.50694 | 2025-06-10 03:25:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b9363562-4dda-3753-ade9-20418eac4f12 | -7.01661 | -44.61864 | 2025-06-10 03:25:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3b4a9ea2-59d8-346f-aaa9-3f2924d3073c | -15.45144 | -40.93686 | 2025-06-10 03:28:00 | NPP-375D | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 35e1e2d8-18e1-37bc-86f2-52ba256463e2 | -14.21321 | -45.49873 | 2025-06-10 03:28:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4b818602-4695-3efb-a977-6f81c1357357 | -14.4986 | -43.80529 | 2025-06-10 03:28:00 | NPP-375D | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 395955db-08e2-3dac-aae7-1bf3ff7b1fe5 | -14.19236 | -45.48634 | 2025-06-10 03:28:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a0172519-c60a-3133-a3eb-75aa2504e9e4 | -18.8211 | -46.43629 | 2025-06-10 03:28:00 | NPP-375D | LAGOA FORMOSA | MINAS GERAIS | Brasil | 3137502 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5d908819-75cd-3dc6-8ca8-0f47ecf7aa39 | -14.2012 | -45.48952 | 2025-06-10 03:28:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e08802a2-daf2-3d84-adc9-a058e42e44ee | -14.20251 | -45.48353 | 2025-06-10 03:28:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bf80a7bf-b183-3cd5-83fb-39aab9293f60 | -14.21453 | -45.49269 | 2025-06-10 03:28:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0a707f66-2d96-3f28-8823-f33bd5ba08c9 | -14.20918 | -45.48507 | 2025-06-10 03:28:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dbd6b2fa-9f03-392b-bcf1-f3b100089e91 | -14.21585 | -45.48658 | 2025-06-10 03:28:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 874b8732-0c59-325d-abd8-49e6f9573b08 | -14.19323 | -45.4939 | 2025-06-10 03:28:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 168437a5-0d76-3fc7-b798-564906418dd4 | -18.81911 | -46.43507 | 2025-06-10 03:28:00 | NPP-375D | LAGOA FORMOSA | MINAS GERAIS | Brasil | 3137502 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 90598817-bd95-3794-9927-f5ab436d0180 | -14.19108 | -45.49237 | 2025-06-10 03:28:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 564ff3c5-b330-3dcd-9385-a7372a92c965 | -18.81455 | -46.43504 | 2025-06-10 03:28:00 | NPP-375D | LAGOA FORMOSA | MINAS GERAIS | Brasil | 3137502 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 61dbabe5-c588-3f3a-94a6-0b14c323a5e3 | -14.50366 | -43.81132 | 2025-06-10 03:28:00 | NPP-375D | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0d1fb72e-bbb1-3c7c-b9bb-ab9d2494f07b | -14.20786 | -45.49111 | 2025-06-10 03:28:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c3ff2998-a503-3902-80b8-b8121dcccb4e | -18.81327 | -46.44067 | 2025-06-10 03:28:00 | NPP-375D | LAGOA FORMOSA | MINAS GERAIS | Brasil | 3137502 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9eebee57-d41b-3a9f-91fb-48e050d38459 | -18.81779 | -46.44068 | 2025-06-10 03:28:00 | NPP-375D | LAGOA FORMOSA | MINAS GERAIS | Brasil | 3137502 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 83be3705-4bd8-356a-8bad-b9c56463b7a3 | -15.77837 | -39.35734 | 2025-06-10 03:28:00 | NPP-375D | MASCOTE | BAHIA | Brasil | 2920908 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| c479baf1-90eb-32b0-9130-17f015ca2b20 | -14.23589 | -45.49109 | 2025-06-10 03:28:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e91b0017-ebb8-39eb-9774-791e942ce6a7 | -14.50463 | -43.80662 | 2025-06-10 03:28:00 | NPP-375D | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 64f7fc1f-90cb-3118-ab50-6595d9e88ddc | -14.19455 | -45.48788 | 2025-06-10 03:28:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ae998238-1a75-3ac5-964f-43ae58d8a7bf | -5.2106 | -43.33 | 2025-06-10 03:40:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 68.1 |
| 2613f1e1-8d1a-3339-833b-3462a91c810c | -5.2108 | -43.3067 | 2025-06-10 03:40:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 141.1 |
| 73cd97d6-5db3-3344-9f31-d855380239c8 | -5.1921 | -43.308 | 2025-06-10 03:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 71.8 |
| 01a3be0e-3295-3fb1-9381-fb5b081566bc | -13.24492 | -40.12467 | 2025-06-10 03:47:00 | NOAA-20 | IRAJUBA | BAHIA | Brasil | 2914208 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| c30077e0-0c14-33b0-ae03-4dac430d318b | -5.64513 | -43.60143 | 2025-06-10 03:47:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 47c259d6-e0f1-3706-add0-fe2c4821041e | -6.33126 | -43.74413 | 2025-06-10 03:47:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b55121a9-ce86-324e-95f0-6e6d3d4a604f | -11.56861 | -47.44093 | 2025-06-10 03:47:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7f69852e-1214-3084-8dca-4a1587583ef9 | -2.51926 | -43.25271 | 2025-06-10 03:47:00 | NOAA-20 | SANTO AMARO DO MARANHÃO | MARANHÃO | Brasil | 2110278 | 21 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 628c9479-1915-3f40-bd4c-8433aba10a76 | -6.33604 | -43.74705 | 2025-06-10 03:47:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1b0ba4a1-e50f-3fc5-b341-5be6d62c37f6 | -6.19454 | -43.32566 | 2025-06-10 03:47:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| aa4d2ae4-908b-3f13-b1c3-fcb0527f5a18 | -13.14023 | -44.0793 | 2025-06-10 03:47:00 | NOAA-20 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 98f813ec-ec42-3107-a380-0c1556e3f885 | -12.06351 | -43.89818 | 2025-06-10 03:47:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 67a6ee9d-170a-322d-8352-792d34d3ba5b | -10.20865 | -46.93459 | 2025-06-10 03:47:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 68e2f7de-0fe0-3249-827a-254e5486d42c | -8.96031 | -47.97268 | 2025-06-10 03:47:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| bf25ac88-1ec1-30fa-be0c-d6b4273f0b5f | -5.91765 | -45.52675 | 2025-06-10 03:47:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| cbc38167-85ec-3e8a-885c-79e88d54eae7 | -5.91301 | -45.52253 | 2025-06-10 03:47:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 94fe3acd-f3e1-3a1a-ba67-8e6309ccafe8 | -6.19828 | -43.33087 | 2025-06-10 03:47:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 19.0 |
| adf59f37-27a4-321f-8486-afe3ebf16401 | -6.19652 | -43.32784 | 2025-06-10 03:47:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 12.9 |
| a4a30071-fde1-3ca8-8a99-936ffb0d410f | -5.81483 | -46.48609 | 2025-06-10 03:47:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 641a5a07-9282-3a95-a6cc-e1fd6e7a39cb | -10.51807 | -40.33098 | 2025-06-10 03:47:00 | NOAA-20 | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 3e69c7bd-0244-3af1-a6cb-9479d9b87ea2 | -6.19903 | -43.32636 | 2025-06-10 03:47:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 321752f4-1511-30c4-9ed9-504708e50936 | -6.34373 | -43.36964 | 2025-06-10 03:47:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5db27168-cdec-3fb4-a8f6-d4ab289a6dd0 | -10.65491 | -44.48236 | 2025-06-10 03:47:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0a6a3d40-2649-319a-b82f-b6ef05fa5195 | -12.06357 | -43.89943 | 2025-06-10 03:47:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b7901721-88a7-3064-80c7-05b3152795c6 | -13.13952 | -44.08315 | 2025-06-10 03:47:00 | NOAA-20 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7c118381-dce4-3808-b934-c8c5692bdcaf | -6.75505 | -44.98832 | 2025-06-10 03:47:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6158e6a3-3e68-3fa8-86c3-3ac5952c30c6 | -9.20777 | -48.86776 | 2025-06-10 03:47:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f1988476-eb74-340d-8f34-a52c120b20cd | -9.39031 | -48.43082 | 2025-06-10 03:47:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e3882e08-d1db-330b-9d39-08e26e984107 | -6.21971 | -43.32707 | 2025-06-10 03:47:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9be7ee2b-4c14-32df-af22-94c7b7f2ab52 | -13.65369 | -41.62049 | 2025-06-10 03:47:00 | NOAA-20 | RIO DE CONTAS | BAHIA | Brasil | 2926707 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 56c5eeae-cc6c-3235-9acf-379e58a12b39 | -6.21108 | -44.5107 | 2025-06-10 03:47:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b98c4320-073f-3d5e-aa75-01aa1e657893 | -12.42058 | -47.80419 | 2025-06-10 03:47:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8b57f9bd-73d6-34c3-b458-96b0f5524fc8 | -3.58508 | -49.4433 | 2025-06-10 03:47:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ff0d2f9a-94ff-32f8-ab3a-96ab03e9cb64 | -8.96111 | -47.96842 | 2025-06-10 03:47:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 50a3a42d-4a59-3e38-b2c2-111b42262df4 | -12.20724 | -49.62347 | 2025-06-10 03:47:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| eaf3d776-103a-3fa6-9c42-e27c5dcc347c | -11.89651 | -47.45239 | 2025-06-10 03:47:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a123aece-6462-37e9-b00b-2490e5e40bbf | -13.65442 | -41.62368 | 2025-06-10 03:47:00 | NOAA-20 | RIO DE CONTAS | BAHIA | Brasil | 2926707 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| ba4e6f6f-2fa3-3f9c-abb0-cdc42477a0ff | -5.91768 | -45.5265 | 2025-06-10 03:47:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6edcffa0-1a5f-3a0b-9af8-832ce7431f38 | -5.77752 | -43.62717 | 2025-06-10 03:47:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a5cf029d-eee8-39e8-98b5-9bde33de37d8 | -6.83412 | -44.63111 | 2025-06-10 03:47:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5a552800-dd38-3df5-a25b-a6d4331af0d1 | -9.38743 | -48.42926 | 2025-06-10 03:47:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d4e5b32b-a5bc-33f4-87f0-ed3cf3c941ff | -10.24357 | -46.89581 | 2025-06-10 03:47:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5e925b57-53da-368c-9231-6da63b9d766d | -10.21532 | -46.92853 | 2025-06-10 03:47:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bff9d99b-8f58-354c-b889-5f7f11ee639a | -12.68914 | -45.06129 | 2025-06-10 03:47:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f4606f81-ea01-3894-ae20-502bd45058cc | -13.24771 | -40.12902 | 2025-06-10 03:47:00 | NOAA-20 | IRAJUBA | BAHIA | Brasil | 2914208 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 3c5e91ce-26a1-3a15-b656-72f801d5ff70 | -5.77536 | -43.61197 | 2025-06-10 03:47:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f7970075-3de7-3493-94ee-b08920e12969 | -10.22601 | -46.93037 | 2025-06-10 03:47:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c95815b1-44c7-3bf8-ba9d-a421a46a732f | -5.77292 | -43.62635 | 2025-06-10 03:47:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6b6d687f-246b-3954-9923-203de3a1c31f | -12.22968 | -44.19069 | 2025-06-10 03:47:00 | NOAA-20 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 932a9f16-3004-3bae-babd-98961f4b4532 | -9.39251 | -48.43487 | 2025-06-10 03:47:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |


[Clique aqui para ver as próximas entradas](README5.md)
