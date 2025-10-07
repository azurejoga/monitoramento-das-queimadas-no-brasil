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

## Dados Diários - Página 112

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ea0a292c-856f-3b7c-b3b1-a04616074ea2 | -12.891 | -54.7577 | 2025-10-07 12:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 99.6 |
| 5e975200-7239-34c0-8796-fd83de61123b | -11.8029 | -45.1087 | 2025-10-07 12:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 84.1 |
| a88d9ec6-ff82-32c4-af96-5168741b637e | -10.2502 | -44.3771 | 2025-10-07 12:10:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 109.1 |
| 5fa7ed51-12b8-39e3-aeef-80f0431ec770 | -8.501 | -46.3117 | 2025-10-07 12:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 90.3 |
| 27372df6-692e-314d-8721-56f8a54f98c5 | -18.0187 | -44.9725 | 2025-10-07 12:10:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 77.0 |
| 1097c349-d36c-3d96-9e56-33e23a91c25e | -14.2949 | -45.8613 | 2025-10-07 12:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 33bc961a-300b-3ffa-99d5-5087dacd37fb | -15.3737 | -47.3201 | 2025-10-07 12:10:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 73.0 |
| 86c59c8f-7734-3c65-a093-e380395b3297 | -13.0939 | -47.9992 | 2025-10-07 12:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 68.0 |
| 95984e58-1524-329c-9a21-2562e635100a | -14.7585 | -46.0104 | 2025-10-07 12:10:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 154.7 |
| 2bbcb88f-1051-391d-9358-ae99a92d8bf0 | -10.4054 | -45.3931 | 2025-10-07 12:10:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 94.6 |
| e05d1b8f-a9e2-344c-9a30-7dffad40ecdc | -14.7389 | -46.0138 | 2025-10-07 12:10:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 124.9 |
| a95aa4a1-d4c0-3ff5-a506-708bdc4cc48b | -13.3241 | -48.0324 | 2025-10-07 12:10:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 62.3 |
| 9f30a7bf-44c9-3770-9294-f28e6233bb58 | -12.7637 | -50.4921 | 2025-10-07 12:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 82.4 |
| c7edd84a-0999-38ea-b4da-b3e6c0d852c2 | -10.4108 | -50.2683 | 2025-10-07 12:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 126.9 |
| 522a74aa-cb3c-3180-ab94-4e4969372971 | -12.8913 | -54.7372 | 2025-10-07 12:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 134.1 |
| a30ec7f1-7952-36ea-9103-81da3e08bbfd | -11.6855 | -46.3593 | 2025-10-07 12:10:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 75.8 |
| b7f33f01-9c68-358d-9046-e12de310aee4 | -15.3742 | -47.2973 | 2025-10-07 12:10:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 88.5 |
| 4a34d221-37d6-38fb-8e25-34dbc36d0e56 | -14.7384 | -46.037 | 2025-10-07 12:10:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 108.1 |
| c13750fa-9c25-3b8d-86fb-351b0cb8a0a3 | -11.6859 | -46.3366 | 2025-10-07 12:10:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 101.8 |
| 664887b2-44ed-3d84-b0aa-460076f02479 | -14.9224 | -51.4292 | 2025-10-07 12:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 74.7 |
| b04b7fae-0d8d-31e1-973f-2f7f8aa07dec | -12.6159 | -44.7519 | 2025-10-07 12:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 145.4 |
| 32a70b52-1a3d-3667-80b9-105348d539a5 | -10.7278 | -46.6658 | 2025-10-07 12:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 83.3 |
| b10e7f4b-aab9-35b4-9e00-423f2aa50889 | -11.8447 | -44.9176 | 2025-10-07 12:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 94.1 |
| f7ac9561-a826-3fbc-b852-5078327eda7f | -13.3241 | -48.0324 | 2025-10-07 12:20:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 83.2 |
| 3d9c6d68-0605-3991-922b-d0f57be62a6b | -10.8919 | -47.1153 | 2025-10-07 12:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 136.7 |
| 5a62fc96-5eea-303e-bd7e-9c1c2c675e40 | -12.891 | -54.7577 | 2025-10-07 12:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 124.3 |
| a0ec7a89-1f9a-3b24-a536-d183f5f7d9c3 | -14.5057 | -46.9242 | 2025-10-07 12:20:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 64.0 |
| 6262240d-ed30-3d01-a8a2-dae1d882df47 | -15.3742 | -47.2973 | 2025-10-07 12:20:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 66.8 |
| 0882275a-152d-3f20-9d1d-f9b7128765ff | -14.777 | -46.0532 | 2025-10-07 12:20:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 66.8 |
| aa5d4eba-1843-3c50-96b9-22c0d8d0688c | -14.2949 | -45.8613 | 2025-10-07 12:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 155.6 |
| 267d42fa-8feb-3dae-9fcb-6dae84adce4d | -14.758 | -46.0335 | 2025-10-07 12:20:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 143.3 |
| b6699301-2dac-3486-b011-f79f4952b53a | -14.7585 | -46.0104 | 2025-10-07 12:20:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 111.0 |
| 365580b8-c4d6-3498-804a-118524c3b1ae | -10.2502 | -44.3771 | 2025-10-07 12:20:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 145.0 |
| eb198f22-a38d-38d6-928f-16cbabb7e943 | -10.2693 | -44.3745 | 2025-10-07 12:20:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 106.5 |
| 2f45e768-dd1a-3af4-bd6e-0ece3a4e6bb8 | -16.2946 | -50.965 | 2025-10-07 12:20:00 | GOES-19 | JAUPACI | GOIÁS | Brasil | 5212006 | 52 | 33 | nan | nan | nan | Cerrado | 81.1 |
| 038815b5-451d-30ae-8f23-f97926685d26 | -10.4108 | -50.2683 | 2025-10-07 12:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 147.0 |
| c02f1387-03b5-3826-ba6b-74d555fb4af4 | -12.9103 | -54.7352 | 2025-10-07 12:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 110.8 |
| 8c771da5-6e22-3a39-a8b7-698f5295ae14 | -15.3737 | -47.3201 | 2025-10-07 12:20:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 59.9 |
| 7ad727bb-988e-3c15-85c1-85cc8c1a55ae | -8.5007 | -46.3342 | 2025-10-07 12:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 75.6 |
| 422c62cf-aaff-3bb7-b988-3f59c1d0b240 | -11.6859 | -46.3366 | 2025-10-07 12:20:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 117.0 |
| 0220692e-3eac-3652-9962-72c540087a0f | -18.9846 | -47.8282 | 2025-10-07 12:20:00 | GOES-19 | INDIANÓPOLIS | MINAS GERAIS | Brasil | 3130705 | 31 | 33 | nan | nan | nan | Cerrado | 83.9 |
| 9fb371c0-7e16-39fa-8aec-4783ea779131 | -11.6855 | -46.3593 | 2025-10-07 12:20:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 141.9 |
| 7ab4be29-6ff6-3acd-bffa-f2c5f0e808b8 | -12.8913 | -54.7372 | 2025-10-07 12:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 220.1 |
| 74efff83-4f67-35de-9870-8e7ff745593d | -12.6159 | -44.7519 | 2025-10-07 12:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 105.6 |
| 14c2bf91-faf1-37e5-9ee5-e0bdf79184ec | -10.4058 | -45.3702 | 2025-10-07 12:20:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 126.8 |
| 314d1a86-7b64-3237-a15f-904cd861a7f4 | -13.0939 | -47.9992 | 2025-10-07 12:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 84.2 |
| c44528f3-8c98-3b13-bd62-e205ba8da762 | -14.2953 | -45.8382 | 2025-10-07 12:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 287.6 |
| 9e9e2784-9604-37cf-8342-4bc022d9ee4f | -8.5395 | -46.2406 | 2025-10-07 12:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 97.5 |
| 24a35015-d6f7-3a89-b566-efaf0895eb3d | -14.7775 | -46.03 | 2025-10-07 12:20:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 69.0 |
| 42dee335-5dc6-3e15-a520-34db020bf9c1 | -14.7384 | -46.037 | 2025-10-07 12:20:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 112.2 |
| e95df39d-bdd4-3031-a80d-ba40b1944778 | -10.456 | -48.3607 | 2025-10-07 12:20:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 154.5 |
| 16710976-7b27-371d-8023-5033c88e86a1 | -10.9109 | -47.1129 | 2025-10-07 12:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 84.3 |
| 5cd7010f-2f2f-36de-a39f-d48b0293ca6a | -10.4054 | -45.3931 | 2025-10-07 12:20:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 101.1 |
| a8eb3af7-a63d-35bf-87f3-953cd74c6f97 | -13.3237 | -48.0547 | 2025-10-07 12:20:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 67.0 |
| 25ddbef9-3ca7-3933-b37c-bb48047c125a | -8.4824 | -46.2912 | 2025-10-07 12:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 90.8 |
| e9083591-371c-3b41-aff2-209f1fdb28d0 | -8.501 | -46.3117 | 2025-10-07 12:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 108.2 |
| 06a2aea3-7fb7-3d3e-b0c5-59703a879e58 | -16.2942 | -50.9868 | 2025-10-07 12:20:00 | GOES-19 | ISRAELÂNDIA | GOIÁS | Brasil | 5210307 | 52 | 33 | nan | nan | nan | Cerrado | 78.4 |
| 10b24bf3-8297-3cf4-800b-fac8992700f1 | -14.7389 | -46.0138 | 2025-10-07 12:20:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 106.4 |
| 3bc18246-ae0b-324c-91ab-a4a3b1b693b9 | -8.4821 | -46.3136 | 2025-10-07 12:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 88.6 |
| 3afcec23-135a-3b9b-861e-26d4a89782ac | -14.9224 | -51.4292 | 2025-10-07 12:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 79.6 |
| efa7739d-2616-350d-b403-5075cde9a664 | -13.3044 | -48.0575 | 2025-10-07 12:20:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 76.2 |
| 7f25ae5a-659b-3030-83a5-9519f95ad952 | -12.7637 | -50.4921 | 2025-10-07 12:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 77.4 |
| 04600f38-c079-396d-a850-d2cdeea069d4 | -11.8221 | -45.1059 | 2025-10-07 12:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 96.2 |
| 277b4012-219c-3aa6-81e3-67e9ea6b4685 | -10.2506 | -44.3538 | 2025-10-07 12:20:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 107.7 |
| cce80b8b-4e87-36b7-9cea-93be0bb49ad9 | -18.0187 | -44.9725 | 2025-10-07 12:20:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 89.4 |
| ad236495-11c2-3da3-9bf6-69d396a070d7 | -14.8645 | -51.4158 | 2025-10-07 12:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 79.1 |
| a1c20843-04ea-3404-97bf-adce2159daee | -10.4245 | -45.3907 | 2025-10-07 12:20:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 308.7 |
| 8c23dec2-acb5-32f3-b3e2-652df6b30161 | -11.0262 | -50.9067 | 2025-10-07 12:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 83.1 |
| 17295bd3-96a7-3232-b943-476c1b8ec837 | -10.4108 | -50.2683 | 2025-10-07 12:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 95.4 |
| 2b69f8df-9a73-3525-97e2-f66522e329b0 | -12.9101 | -54.7558 | 2025-10-07 12:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 64.4 |
| 07988ec4-e50a-3af9-807d-04bf3cb3c654 | -14.8645 | -51.4158 | 2025-10-07 12:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 86.0 |
| 9307c15d-5271-3f84-ac7f-abc9cd1d1116 | -12.891 | -54.7577 | 2025-10-07 12:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 169.7 |
| ec235563-192e-327e-99bb-c82baf142570 | -10.2502 | -44.3771 | 2025-10-07 12:30:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 136.6 |
| 3f1729da-3ae1-362a-a4d7-9cf7dd636cac | -13.0939 | -47.9992 | 2025-10-07 12:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 62.8 |
| ce51d043-7b27-3eb9-b623-eb7ac46b2522 | -14.8839 | -51.4131 | 2025-10-07 12:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 69.6 |
| b1a764a2-00c2-33ae-b318-9c8ba8612255 | -14.7585 | -46.0104 | 2025-10-07 12:30:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 111.2 |
| fc5bc15d-77e9-3b87-8a5e-f8c873d1920a | -15.3742 | -47.2973 | 2025-10-07 12:30:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 80.3 |
| 50f1283a-bbe5-3611-8510-eccfc6b0934a | -10.1379 | -45.4954 | 2025-10-07 12:30:00 | GOES-19 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 150.8 |
| 5eed973b-0c55-3daa-bab3-3a710bda477a | -14.758 | -46.0335 | 2025-10-07 12:30:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 109.5 |
| 4723052b-9bd6-331c-a475-d2e08ab0a8b3 | -12.9103 | -54.7352 | 2025-10-07 12:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 99.1 |
| 259e9a6d-ad31-3550-b9da-5005a24dcc0a | -10.4058 | -45.3702 | 2025-10-07 12:30:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 142.2 |
| e28aef98-2e98-341e-b3f4-7ea80e21e904 | -8.8717 | -46.7878 | 2025-10-07 12:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 80.9 |
| 308e2df7-c087-359c-b897-555079d4f2ad | -11.8447 | -44.9176 | 2025-10-07 12:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 84.9 |
| 65df0cd2-d93d-33d1-826b-a44c333fdd4d | -8.5395 | -46.2406 | 2025-10-07 12:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 136.0 |
| f8b21651-2932-3964-9197-ad10dc57801f | -9.6804 | -45.6645 | 2025-10-07 12:30:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 90.7 |
| 779c6284-cacc-3ebf-9ac4-86120e656c90 | -10.4245 | -45.3907 | 2025-10-07 12:30:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 217.7 |
| 623929f4-1a5b-3624-bb71-4f55ee346866 | -16.2942 | -50.9868 | 2025-10-07 12:30:00 | GOES-19 | ISRAELÂNDIA | GOIÁS | Brasil | 5210307 | 52 | 33 | nan | nan | nan | Cerrado | 83.0 |
| 4b73461d-0020-37c8-b2ce-71853c17bcf8 | -12.9426 | -46.8109 | 2025-10-07 12:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 66.9 |
| 2f4e628b-644a-3e76-85c0-2c983559e12f | -8.501 | -46.3117 | 2025-10-07 12:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 102.1 |
| 72bca491-400b-3686-8284-385cf7013df6 | -8.8714 | -46.8101 | 2025-10-07 12:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 115.3 |
| 6719dc29-fb49-336e-bb4c-7fe0ff006ef0 | -14.3148 | -45.8348 | 2025-10-07 12:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 74.7 |
| 773d4b14-32a6-3003-b37b-bf54be0b1b77 | -8.5584 | -46.2387 | 2025-10-07 12:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 81.0 |
| 10579d33-1067-3e15-9c90-d67eb68167ab | -8.4824 | -46.2912 | 2025-10-07 12:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 80.1 |
| 72f507df-0061-3fc3-8b7d-641f6084ab8a | -13.3241 | -48.0324 | 2025-10-07 12:30:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 79.6 |
| 96c8ed18-b53b-347e-8d97-e3e89c55743c | -10.456 | -48.3607 | 2025-10-07 12:30:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 226.8 |
| 1fa0632f-b7cc-3aac-8d80-8332c6e88e88 | -10.4557 | -48.3827 | 2025-10-07 12:30:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 92.6 |
| 5c46955d-6269-3463-b93d-5dba3d0b4eb5 | -10.4746 | -48.3805 | 2025-10-07 12:30:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 110.1 |
| 79439f0b-455a-31f6-bfce-93285cef9583 | -10.4054 | -45.3931 | 2025-10-07 12:30:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 113.7 |
| 42e1160e-db18-350e-a966-713cda22c356 | -11.8221 | -45.1059 | 2025-10-07 12:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 79.8 |
| 9511d67c-99c1-37fe-aed6-c522977dd1a4 | -10.2506 | -44.3538 | 2025-10-07 12:30:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 102.1 |


[Clique aqui para ver as próximas entradas](README113.md)
