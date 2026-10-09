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

## Dados Diários - Página 228

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d15acf78-c43d-3824-a112-ad7f5489643c | -2.26052 | -48.05624 | 2026-10-09 06:57:00 | AQUA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 73161cca-305a-30e7-ae71-a69966c184db | -2.4986 | -56.07213 | 2026-10-09 06:57:00 | AQUA_M-M | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 44.7 |
| 8c648429-9dad-38b3-88d7-f7361a403543 | -4.14894 | -48.5508 | 2026-10-09 06:57:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0779bd9f-01a8-3728-a3dc-d2226aedfdec | -7.08296 | -52.67788 | 2026-10-09 06:57:00 | AQUA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 643ce3fd-e12b-379e-8667-ffe552c3c69d | -4.27913 | -49.09035 | 2026-10-09 06:57:00 | AQUA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| ee7987a3-c2cd-39a9-a43f-7ee13e7a64ed | -3.10113 | -53.78112 | 2026-10-09 06:57:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 16.7 |
| 583e9017-743b-3e0b-857d-2ae33c7ec0b0 | -3.19064 | -50.58182 | 2026-10-09 06:57:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 5c558a7f-e82d-3018-8d28-b5bdd75ae743 | -6.1469 | -47.91798 | 2026-10-09 06:57:00 | AQUA_M-M | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 2a3dd812-4eef-3319-a7fa-d55b8f0b190b | -4.82391 | -45.83145 | 2026-10-09 06:57:00 | AQUA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 1df4ba87-07ed-3328-8631-b541d8351260 | -2.49265 | -56.06614 | 2026-10-09 06:57:00 | AQUA_M-M | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 62.4 |
| 4891c4d7-f1df-3f5d-819d-7e33ec18a16f | -1.10396 | -54.17105 | 2026-10-09 06:57:00 | AQUA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 24.0 |
| ebbc50ec-e00d-36f4-9b4f-95684ccff8d8 | -6.96277 | -45.27361 | 2026-10-09 06:57:00 | AQUA_M-M | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 740f177e-f6f1-3cdd-a63e-3f1c85658c53 | -3.20249 | -53.86798 | 2026-10-09 06:57:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 3601c603-d8e4-33d5-9735-a21e24582f30 | -3.10713 | -54.16968 | 2026-10-09 06:57:00 | AQUA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| cbb7127b-552f-3462-8b4f-95819f9c49c9 | -5.711 | -53.48742 | 2026-10-09 06:57:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 19.7 |
| df7b8d33-9b39-375c-8a81-1ffc59dc1f26 | -8.2245 | -46.40875 | 2026-10-09 06:57:00 | AQUA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 39.4 |
| 26bba6ce-0e63-3b0a-98f5-0c3f40050375 | -3.35595 | -50.40827 | 2026-10-09 06:57:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| d831040f-eaeb-313a-9e18-d84790b0ad3b | -7.18545 | -52.61895 | 2026-10-09 06:57:00 | AQUA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 5e1bcefe-88d1-3069-88d8-821a6fe6f523 | -3.20577 | -50.54476 | 2026-10-09 06:57:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 508cf64b-9ceb-33c0-9a2b-409b6bbc4ec6 | -5.70241 | -53.47271 | 2026-10-09 06:57:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 18.2 |
| 69b48347-41fd-365a-92d9-98a53130458e | -2.80839 | -58.28789 | 2026-10-09 06:57:00 | AQUA_M-M | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 110.9 |
| b3e831e3-50b2-3081-a746-d62a0fae76ba | -3.565 | -54.68813 | 2026-10-09 06:57:00 | AQUA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 55.9 |
| 30cb9d5e-5c27-3b16-8c4a-cc985ba49c85 | -5.87417 | -53.51979 | 2026-10-09 06:57:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 18.2 |
| 9610f92b-8e78-39c6-853a-84eaa2337a02 | -1.49418 | -54.548 | 2026-10-09 06:57:00 | AQUA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 22.8 |
| 396ab702-25ee-3b50-8ba8-6dcced97c7ef | -5.88089 | -53.51235 | 2026-10-09 06:57:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| e286a911-54ed-37e9-9c2f-ec846a6a0d8b | -6.8852 | -45.89625 | 2026-10-09 06:57:00 | AQUA_M-M | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 7bd5f224-0a1c-352e-8ae0-ba1345079390 | -3.92703 | -56.0285 | 2026-10-09 06:57:00 | AQUA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 21.9 |
| 940e8fa0-019c-3a39-bbe3-91cccd821a39 | -5.44003 | -43.4531 | 2026-10-09 06:57:00 | AQUA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 48fe4452-f80c-32f1-ab11-f634480ac362 | -3.20429 | -50.55434 | 2026-10-09 06:57:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 3e70f882-9049-3991-8757-8ce54d5bf9db | -6.13034 | -53.05836 | 2026-10-09 06:57:00 | AQUA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 7b8fffd4-d614-31d0-9f68-ba247fdbb8e3 | -3.3458 | -50.47454 | 2026-10-09 06:57:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| ae607a4f-6264-3ef7-884a-c10ef3b72947 | -4.73837 | -55.65094 | 2026-10-09 06:57:00 | AQUA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 31.5 |
| d0ec48ff-3f11-39b4-b8d8-56f1e00a99cc | -2.99782 | -53.92185 | 2026-10-09 06:57:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 18.2 |
| 88587db3-1116-37f5-8e45-7c51ca1aa471 | -2.74068 | -54.11577 | 2026-10-09 06:57:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 19.3 |
| 0b746968-9fad-3ed4-b585-9e8a25c5c7a6 | -3.89827 | -55.90047 | 2026-10-09 06:57:00 | AQUA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 18.5 |
| 3f892a44-5e07-3705-9810-5bb022974ec2 | -7.50609 | -45.76313 | 2026-10-09 06:57:00 | AQUA_M-M | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 12.9 |
| bb1bc10b-07fc-3371-8ff7-bd3e2992057c | -3.12157 | -54.15515 | 2026-10-09 06:57:00 | AQUA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 21.7 |
| 77b69dc0-81c2-38d6-8a0a-ab12fba5ece6 | -4.29647 | -48.60513 | 2026-10-09 06:57:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 1a904101-3c81-3e5c-a4f7-17cb3a6b8ac3 | -6.93523 | -43.65634 | 2026-10-09 06:57:00 | AQUA_M-M | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 1df2a805-cce0-3442-aa60-9b12c8f7f9f5 | -6.46666 | -46.02993 | 2026-10-09 06:57:00 | AQUA_M-M | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| ed2da85d-d981-3ff7-bef7-91837fa8607c | -2.74323 | -54.0989 | 2026-10-09 06:57:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 18.9 |
| f259c5a2-ca93-332a-8273-0399fcb4036f | -1.1515 | -54.22079 | 2026-10-09 06:57:00 | AQUA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 8d734ec0-6522-3b8a-b30d-e8bf26d0fed6 | -6.45828 | -46.01691 | 2026-10-09 06:57:00 | AQUA_M-M | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 40139a95-a99a-32c3-b744-72fb729109bd | -3.80608 | -49.94402 | 2026-10-09 06:57:00 | AQUA_M-M | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| c43d81f0-7c3c-3440-995b-0bd0f74ad1d5 | -3.11897 | -54.17158 | 2026-10-09 06:57:00 | AQUA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 76.6 |
| ab9db8e2-f103-3063-b5b1-8dc8b86c1b4c | -7.18369 | -52.63016 | 2026-10-09 06:57:00 | AQUA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 31dfa503-69bd-3bf3-9060-f7d5a66e6dee | -3.24692 | -54.02766 | 2026-10-09 06:57:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 26.1 |
| 6dea09b8-e525-3a8a-ad66-2bc9dc1792b4 | -6.88349 | -45.90824 | 2026-10-09 06:57:00 | AQUA_M-M | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 31.9 |
| 654587ae-f8ee-32df-8a95-6d85e588ff5e | -5.93165 | -51.82334 | 2026-10-09 06:57:00 | AQUA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 128fb267-448b-3545-b6c4-a5273058c6dc | -6.88693 | -45.88418 | 2026-10-09 06:57:00 | AQUA_M-M | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 920abd6a-8d1e-31aa-a860-671156f6b4dd | -5.43461 | -43.44166 | 2026-10-09 06:57:00 | AQUA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 28.7 |
| 6f41158b-9a8c-3bbc-9ee8-f4b850b6021e | -4.62196 | -49.21053 | 2026-10-09 06:57:00 | AQUA_M-M | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 1bdb2edb-0b36-3cf4-ba8f-34f02afaa5f2 | -3.80746 | -49.93497 | 2026-10-09 06:57:00 | AQUA_M-M | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 6d8deaca-014e-328b-a21e-38b04b5e7939 | -8.27771 | -45.73846 | 2026-10-09 06:57:00 | AQUA_M-M | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 427.9 |
| 6719d0f7-c78f-3159-9b9c-d2bae0b33d0f | -2.50259 | -56.04769 | 2026-10-09 06:57:00 | AQUA_M-M | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 39.6 |
| 6d24446d-5034-37fd-a50f-b9a4d4b46b23 | -3.69612 | -47.68113 | 2026-10-09 06:57:00 | AQUA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| bec381aa-25bc-39b4-aca3-b58e7a90f530 | -8.22284 | -46.42025 | 2026-10-09 06:57:00 | AQUA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| a60e89f8-b6aa-35da-b89d-f4ee3d651765 | -3.02566 | -54.18436 | 2026-10-09 06:57:00 | AQUA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 7e621fa5-44d4-32a3-be36-9f68828f5738 | -8.22616 | -46.39719 | 2026-10-09 06:57:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 34.4 |
| 571a242e-2943-380d-8300-44c56716cd1c | -6.72883 | -48.11189 | 2026-10-09 06:57:00 | AQUA_M-M | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 9d3eba35-3f7d-35ee-9409-699fda8c0a49 | -3.28699 | -54.00051 | 2026-10-09 06:57:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 16.6 |
| f1a6c8c3-a4bf-3070-bacb-b0e9434f4fad | -8.22119 | -46.4317 | 2026-10-09 06:57:00 | AQUA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 34.4 |
| a1f98ad0-70a8-39dc-aa7a-de50506592c5 | -8.2796 | -45.72488 | 2026-10-09 06:57:00 | AQUA_M-M | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 20.7 |
| 1bbae3e4-1684-3528-b933-d441f10fa8e2 | -3.45943 | -50.58535 | 2026-10-09 06:57:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 19.1 |
| c22f12a3-abec-31ae-8853-3f75e5c853fe | -3.34541 | -50.41634 | 2026-10-09 06:57:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 09e245f4-de18-3139-bdb6-106d6c00555e | -5.87862 | -53.52628 | 2026-10-09 06:57:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 339c9532-d125-3c3f-8dbb-8e3fce91ea81 | -3.11265 | -53.78262 | 2026-10-09 06:57:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 24.4 |
| 7526e7c2-8314-374c-9714-0b7ab72b035a | -3.19513 | -50.55297 | 2026-10-09 06:57:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 9c268d0d-f204-331f-bc5d-e77bb6b00484 | -4.63309 | -50.94699 | 2026-10-09 06:57:00 | AQUA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 188c4093-3d3e-3407-810e-5cfd19a54262 | -3.56295 | -54.68071 | 2026-10-09 06:57:00 | AQUA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 37.9 |
| dc4a913c-c56a-3313-bfcd-13f0ebf77700 | -7.57603 | -45.64345 | 2026-10-09 06:57:00 | AQUA_M-M | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| a9ba9723-5a97-38e9-8870-086ca9fcf9ad | -3.17242 | -50.58301 | 2026-10-09 06:57:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 00233d98-07b5-3f9b-b907-1d3634421f49 | -3.00682 | -51.00628 | 2026-10-09 06:57:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 17.9 |
| 0a921989-4e9f-3af5-8184-9f3e5ac55987 | -2.73632 | -54.1048 | 2026-10-09 06:57:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 19.1 |
| ac89b6de-d78d-366e-a4a3-c06fae82d03a | -3.00033 | -53.9057 | 2026-10-09 06:57:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 31.6 |
| 840fc59d-d057-3f40-b239-5536a7f381c2 | -2.73362 | -54.12165 | 2026-10-09 06:57:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 2a2b7694-7612-3411-a530-e9f3d8591d2e | -3.20067 | -50.82258 | 2026-10-09 06:57:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 633a5d70-a216-36ed-b8cb-67eadbc5ca16 | -5.95866 | -55.36529 | 2026-10-09 06:57:00 | AQUA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 2d562620-3e2a-372f-beb4-5e689e97f1b4 | -7.08119 | -52.68918 | 2026-10-09 06:57:00 | AQUA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| e6c312ae-87f8-3113-b656-37651b0e9b38 | -6.46831 | -46.01829 | 2026-10-09 06:57:00 | AQUA_M-M | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 22.3 |
| 8e909731-521a-3278-8a8b-1a6e70b04a04 | -5.93002 | -51.83386 | 2026-10-09 06:57:00 | AQUA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 64f7930f-554f-3604-b747-624c26af5a7e | -6.89712 | -45.88557 | 2026-10-09 06:57:00 | AQUA_M-M | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 71bb9ec6-569e-35ad-84d5-5f689cd989e7 | -3.29889 | -53.69692 | 2026-10-09 06:57:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 7f50436b-b38d-3cb8-a376-8c9e8c9f927d | -6.87966 | -45.02753 | 2026-10-09 06:57:00 | AQUA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 44887e60-38a9-33c3-b027-c1fe08915882 | -4.7479 | -55.67447 | 2026-10-09 06:57:00 | AQUA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 93.4 |
| 11df5c07-2b06-3db0-92be-cb1e5cd3eb6e | -3.16394 | -50.45444 | 2026-10-09 06:57:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| d3ca2ebc-cb8f-37fc-ba27-876b34a4c71e | -2.87792 | -54.18394 | 2026-10-09 06:57:00 | AQUA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 318496df-ca54-33f3-8efe-193b2380dfb3 | -2.74818 | -54.10663 | 2026-10-09 06:57:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 22.6 |
| 09d1f0f6-5dc6-3fb8-bfe2-9470e429ac23 | -3.31023 | -53.69879 | 2026-10-09 06:57:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 0b6f9d7d-2e8a-33c1-abb8-97dea9ffab2e | -3.90179 | -55.87823 | 2026-10-09 06:57:00 | AQUA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 15.9 |
| 59fb92bd-8d54-3ff2-a59f-3dc2f0a379e7 | -3.00284 | -53.88964 | 2026-10-09 06:57:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| bc065e3f-2a3d-39a2-b888-2d0abd4aeb7a | -5.09696 | -46.2112 | 2026-10-09 06:57:00 | AQUA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 9.3 |
| d4dee0fa-3439-3bc0-93cb-77bf47bb1c3b | -3.18742 | -50.54591 | 2026-10-09 06:57:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 18ffbe77-b969-39c4-a807-e27a2d65a0b6 | -3.55273 | -54.6863 | 2026-10-09 06:57:00 | AQUA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 25.5 |
| 816c9cf2-ad8c-32d2-96d6-3af562f426ba | -3.42861 | -54.54465 | 2026-10-09 06:57:00 | AQUA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 91509e83-5a14-3d61-abc2-a774aebe566d | -6.87328 | -45.90714 | 2026-10-09 06:57:00 | AQUA_M-M | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 21.7 |
| e31f0226-27a9-39f0-be2d-c5d3d69c8a31 | -8.72649 | -45.15239 | 2026-10-09 06:59:00 | AQUA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 24.2 |
| 88f41a07-bad1-3c80-a6fc-e1a645b4fb29 | -8.1794 | -54.7165 | 2026-10-09 06:59:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 16.6 |
| 9cd4ef23-2d0b-38eb-897b-52e2cb473e64 | -10.3123 | -46.256 | 2026-10-09 06:59:00 | AQUA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 7a689dc7-525e-3d7d-aba6-7820a59dbbbe | -8.96866 | -45.91008 | 2026-10-09 06:59:00 | AQUA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 11.3 |


[Clique aqui para ver as próximas entradas](README229.md)
