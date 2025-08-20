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

## Dados Diários - Página 39

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c83694bc-9fa7-3f3b-b928-75878e13cd55 | -22.26769 | -48.50217 | 2025-08-20 04:38:00 | NPP-375D | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 8235e5e5-eec0-3340-b4c0-674049c68e8e | -15.05595 | -54.83742 | 2025-08-20 04:38:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b299d566-fe46-37a7-abbc-7b707d93a3b6 | -15.01681 | -54.82382 | 2025-08-20 04:38:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 14ea6d73-5ff7-312b-9cdd-78c8435391b0 | -18.6781 | -46.98278 | 2025-08-20 04:38:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 701d8c3d-6d17-3f97-b357-7bcf26705040 | -15.02705 | -54.83619 | 2025-08-20 04:38:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a407c29a-c37f-381d-a296-c312928e3cc4 | -16.74188 | -50.0459 | 2025-08-20 04:38:00 | NPP-375D | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d92b603c-4e59-3c44-98f7-4f02c9ddc10a | -21.87278 | -48.20838 | 2025-08-20 04:38:00 | NPP-375D | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c02c6f7c-b605-3ba8-a5da-e32e7732b8c1 | -17.558 | -44.47903 | 2025-08-20 04:38:00 | NPP-375D | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ae9b5818-b01f-3bdf-81bc-358ec96494c7 | -21.89577 | -48.18391 | 2025-08-20 04:38:00 | NPP-375D | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9de4d3e4-7da8-3527-b241-10c2c1a54dbb | -19.83547 | -47.33022 | 2025-08-20 04:38:00 | NPP-375D | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7cc0bc02-bf79-303f-8275-c67c2a507ee7 | -22.36992 | -51.51467 | 2025-08-20 04:38:00 | NPP-375D | NARANDIBA | SÃO PAULO | Brasil | 3532207 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 75a6d3fc-57a1-3c70-8c38-694dac36c818 | -18.31213 | -48.86389 | 2025-08-20 04:38:00 | NPP-375D | CORUMBAÍBA | GOIÁS | Brasil | 5205901 | 52 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| ac53329f-240f-3eb5-968c-e2010d84a963 | -14.78218 | -59.6706 | 2025-08-20 04:38:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 313a1edb-967a-34fa-b170-d91788f7f79b | -21.12741 | -47.03775 | 2025-08-20 04:38:00 | NPP-375D | ITAMOGI | MINAS GERAIS | Brasil | 3132909 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 10c6bdac-c7ef-3711-b82b-28a8b1864c91 | -16.31025 | -50.18002 | 2025-08-20 04:38:00 | NPP-375D | ADELÂNDIA | GOIÁS | Brasil | 5200159 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ce4e8b71-0aea-3507-9ac0-cfebab1667f3 | -20.47703 | -53.67596 | 2025-08-20 04:38:00 | NPP-375D | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 36f1efee-740d-35c6-ac50-c83569a988d1 | -18.86319 | -48.93112 | 2025-08-20 04:38:00 | NPP-375D | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0e01bc82-729b-307a-875e-7f9a16d0358c | -20.44269 | -41.58538 | 2025-08-20 04:38:00 | NPP-375D | IÚNA | ESPÍRITO SANTO | Brasil | 3203007 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 5f5352bb-65ab-3bf7-a235-7b3de9a951ea | -19.88837 | -49.84771 | 2025-08-20 04:38:00 | NPP-375D | SÃO FRANCISCO DE SALES | MINAS GERAIS | Brasil | 3161304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| a67a0912-e7a4-30b5-9bd8-fdf683de08e1 | -19.44939 | -47.19355 | 2025-08-20 04:38:00 | NPP-375D | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 8d9b5cf7-7650-33fb-87d0-2a4f26cfcb3c | -20.34387 | -51.70596 | 2025-08-20 04:38:00 | NPP-375D | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 6.5 |
| c55925b8-b6b4-36b4-91ca-a3bf24935e10 | -20.33659 | -51.70845 | 2025-08-20 04:38:00 | NPP-375D | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 25fa5e07-f57e-33d7-b0d9-fe918c8fccac | -19.45565 | -45.30807 | 2025-08-20 04:38:00 | NPP-375D | MARTINHO CAMPOS | MINAS GERAIS | Brasil | 3140506 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 53077d88-5c5f-3e75-b52e-331545eb2d77 | -16.33076 | -50.17982 | 2025-08-20 04:38:00 | NPP-375D | ADELÂNDIA | GOIÁS | Brasil | 5200159 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c48662ec-fac6-3d66-ab11-9ff053359a39 | -17.67688 | -50.48132 | 2025-08-20 04:38:00 | NPP-375D | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d2c21989-2825-36f8-b7de-72c5a890a34a | -17.05432 | -48.30511 | 2025-08-20 04:38:00 | NPP-375D | ORIZONA | GOIÁS | Brasil | 5215306 | 52 | 33 | nan | nan | nan | Cerrado | 0.2 |
| 2e1305c0-f5a0-37a3-be8d-0c32a2bb3d79 | -15.02363 | -54.8321 | 2025-08-20 04:38:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 45f3fc69-5d85-3b72-aaee-6b38949b874b | -23.38832 | -47.25463 | 2025-08-20 04:38:00 | NPP-375D | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 9e9a1bac-e14c-3665-b4cf-c8520fc12967 | -14.78027 | -59.6726 | 2025-08-20 04:38:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 90c5f266-5e9b-3a47-8593-fa6d8ee651d0 | -19.45307 | -47.19409 | 2025-08-20 04:38:00 | NPP-375D | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 06032795-3339-387a-9f89-cefc12e59cc7 | -20.34053 | -51.70535 | 2025-08-20 04:38:00 | NPP-375D | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 5ca7efb0-bcf7-30dc-993d-dc9394cb8e4a | -21.90975 | -47.23935 | 2025-08-20 04:38:00 | NPP-375D | SANTA CRUZ DAS PALMEIRAS | SÃO PAULO | Brasil | 3546306 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| e4210dd0-149f-371a-9791-186f1e66a535 | -21.9038 | -47.23189 | 2025-08-20 04:38:00 | NPP-375D | SANTA CRUZ DAS PALMEIRAS | SÃO PAULO | Brasil | 3546306 | 35 | 33 | nan | nan | nan | Mata Atlântica | 19.3 |
| 8b56bf04-1a7b-3001-a681-67aecb1c0770 | -19.45369 | -47.18951 | 2025-08-20 04:38:00 | NPP-375D | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 16579e50-68f7-31e0-88e9-01627490f630 | -16.79434 | -50.09504 | 2025-08-20 04:38:00 | NPP-375D | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 22260bad-6ad6-3805-b1cd-6d57b9df82b0 | -19.87665 | -49.8342 | 2025-08-20 04:38:00 | NPP-375D | SÃO FRANCISCO DE SALES | MINAS GERAIS | Brasil | 3161304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| e55411bd-bbd1-3ae6-ace4-497e94551200 | -15.0492 | -54.82867 | 2025-08-20 04:38:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9b107ee5-dcc3-3854-9625-b879c55294dd | -19.72993 | -48.97447 | 2025-08-20 04:38:00 | NPP-375D | COMENDADOR GOMES | MINAS GERAIS | Brasil | 3116902 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 2e964e37-26e4-379a-b466-55b472220d65 | -21.13121 | -47.03822 | 2025-08-20 04:38:00 | NPP-375D | ITAMOGI | MINAS GERAIS | Brasil | 3132909 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 85e9f95b-f1c4-3bb5-a4c5-e82f8e291307 | -15.85931 | -50.89984 | 2025-08-20 04:38:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 88f3feea-c64a-3b97-b476-88e4156fdcfa | -17.6763 | -50.48494 | 2025-08-20 04:38:00 | NPP-375D | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4ff486bc-237a-38e7-a567-ca98396252ce | -22.3695 | -50.40588 | 2025-08-20 04:38:00 | NPP-375D | LUTÉCIA | SÃO PAULO | Brasil | 3527900 | 35 | 33 | nan | nan | nan | Cerrado | 6.9 |
| a4b1b970-5924-3d1c-8978-9c1fbbd9497a | -20.33933 | -51.71279 | 2025-08-20 04:38:00 | NPP-375D | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 14.3 |
| b4469001-9270-3d15-899c-e4c0e6fa1e93 | -14.99466 | -54.8312 | 2025-08-20 04:38:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 52b7dba6-52a0-3dff-9818-d987b9789661 | -15.00537 | -54.81806 | 2025-08-20 04:38:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 85613099-9826-3ac8-a31f-52db736495b4 | -22.55443 | -49.77314 | 2025-08-20 04:38:00 | NPP-375D | SÃO PEDRO DO TURVO | SÃO PAULO | Brasil | 3550506 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 372aea3b-a247-3358-8f08-c04e18b99a8a | -15.64894 | -52.69217 | 2025-08-20 04:38:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ec8df7f7-ffdf-3adc-b7c7-b6127edf8328 | -21.90785 | -47.25405 | 2025-08-20 04:38:00 | NPP-375D | SANTA CRUZ DAS PALMEIRAS | SÃO PAULO | Brasil | 3546306 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| ec902607-3918-3454-96d3-8119a673cfd9 | -17.55704 | -44.48665 | 2025-08-20 04:38:00 | NPP-375D | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e4690074-7ca2-3874-8a90-28c6ccfbb83a | -19.8582 | -49.81956 | 2025-08-20 04:38:00 | NPP-375D | SÃO FRANCISCO DE SALES | MINAS GERAIS | Brasil | 3161304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.8 |
| a86ffce8-a44a-3318-aa8e-6643d469e8f2 | -21.8969 | -47.22585 | 2025-08-20 04:38:00 | NPP-375D | SANTA CRUZ DAS PALMEIRAS | SÃO PAULO | Brasil | 3546306 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| a3f4b719-15d3-377c-97b6-3a341eeb1eda | -15.87573 | -50.65975 | 2025-08-20 04:38:00 | NPP-375D | ITAPIRAPUÃ | GOIÁS | Brasil | 5211008 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| fe016d17-3173-3c52-a1c7-84538e178ca5 | -19.85536 | -49.8383 | 2025-08-20 04:38:00 | NPP-375D | SÃO FRANCISCO DE SALES | MINAS GERAIS | Brasil | 3161304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 55f293e4-6209-327e-a912-0fd01a935c2d | -18.67504 | -46.97774 | 2025-08-20 04:38:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8ed38b49-466d-39fc-8c1b-4de2081f7e83 | -21.89757 | -47.22089 | 2025-08-20 04:38:00 | NPP-375D | SANTA CRUZ DAS PALMEIRAS | SÃO PAULO | Brasil | 3546306 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 1d2bff70-e602-31bc-9ab6-0ec1365bd99b | -19.54972 | -47.75134 | 2025-08-20 04:38:00 | NPP-375D | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5b300c91-92d3-37fc-bc38-0c11fa13e4d2 | -17.67298 | -50.48436 | 2025-08-20 04:38:00 | NPP-375D | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 580d1e9f-359c-33bb-872e-c8bc85d54d97 | -19.88001 | -49.83476 | 2025-08-20 04:38:00 | NPP-375D | SÃO FRANCISCO DE SALES | MINAS GERAIS | Brasil | 3161304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 322a36fc-69e1-33ea-9440-a4e2c2bd73b6 | -17.26826 | -44.88938 | 2025-08-20 04:38:00 | NPP-375D | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 992966c4-fedc-3d27-93bc-f9e154dea4b5 | -18.77312 | -48.05801 | 2025-08-20 04:38:00 | NPP-375D | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| bbc2442b-f2a4-31ed-999d-074dbbc11f04 | -15.02085 | -54.82447 | 2025-08-20 04:38:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 75399132-75c5-38cb-a846-5fbee07acfde | -20.33719 | -51.70473 | 2025-08-20 04:38:00 | NPP-375D | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 13f3a232-5f9d-3c6c-9e59-87c61fe4e475 | -18.61472 | -49.19465 | 2025-08-20 04:38:00 | NPP-375D | CENTRALINA | MINAS GERAIS | Brasil | 3115805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 967839e5-9877-371d-b2a7-c6cc53a30eda | -19.87944 | -49.83851 | 2025-08-20 04:38:00 | NPP-375D | SÃO FRANCISCO DE SALES | MINAS GERAIS | Brasil | 3161304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 2ceaa525-67d5-3997-949b-e9c49196cd14 | -21.90001 | -47.23136 | 2025-08-20 04:38:00 | NPP-375D | SANTA CRUZ DAS PALMEIRAS | SÃO PAULO | Brasil | 3546306 | 35 | 33 | nan | nan | nan | Mata Atlântica | 19.3 |
| 18a57149-8cc9-326d-a360-29bc7c9d34b5 | -16.31357 | -50.18059 | 2025-08-20 04:38:00 | NPP-375D | ADELÂNDIA | GOIÁS | Brasil | 5200159 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f8ce91e0-10c8-34bb-b3db-c6f062743476 | -19.88165 | -49.84658 | 2025-08-20 04:38:00 | NPP-375D | SÃO FRANCISCO DE SALES | MINAS GERAIS | Brasil | 3161304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 2d9b9f90-0989-3e12-837b-df44f1fdb12c | -16.1839 | -48.86171 | 2025-08-20 04:38:00 | NPP-375D | ABADIÂNIA | GOIÁS | Brasil | 5200100 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6939b8ab-6440-3bc6-89fd-93a508f0e48e | -16.71616 | -48.42585 | 2025-08-20 04:38:00 | NPP-375D | VIANÓPOLIS | GOIÁS | Brasil | 5222005 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 547908ad-c89b-36e2-b765-a35905042bc4 | -19.88952 | -49.8402 | 2025-08-20 04:38:00 | NPP-375D | SÃO FRANCISCO DE SALES | MINAS GERAIS | Brasil | 3161304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| 72027746-3ec5-3839-8183-9845e4320975 | -15.87298 | -50.65553 | 2025-08-20 04:38:00 | NPP-375D | ITAPIRAPUÃ | GOIÁS | Brasil | 5211008 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b389aa0b-b848-361b-8a97-964c97eca39f | -16.30968 | -50.18362 | 2025-08-20 04:38:00 | NPP-375D | ADELÂNDIA | GOIÁS | Brasil | 5200159 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9df96ba8-0af2-35b5-b50f-dc80f28728a2 | -19.87107 | -49.82558 | 2025-08-20 04:38:00 | NPP-375D | SÃO FRANCISCO DE SALES | MINAS GERAIS | Brasil | 3161304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 1fc18a9c-ea26-393a-809f-cfccca223c75 | -15.90354 | -50.83991 | 2025-08-20 04:38:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0561742b-0486-3daf-8ff8-7ca7091e238e | -23.39215 | -47.25529 | 2025-08-20 04:38:00 | NPP-375D | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| fce4c368-1eed-32f2-a47a-9f74818fb77e | -19.83914 | -47.33081 | 2025-08-20 04:38:00 | NPP-375D | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| aefb1d46-9de9-3bb1-a3f4-cfac85aeb822 | -18.52522 | -45.11394 | 2025-08-20 04:38:00 | NPP-375D | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1c59da78-568a-380e-836b-2a949def8175 | -20.50394 | -46.37141 | 2025-08-20 04:38:00 | NPP-375D | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dbdd969c-b85d-357b-b66c-c6ab5f1cfe63 | -20.09137 | -47.5981 | 2025-08-20 04:38:00 | NPP-375D | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6a6c5ce2-d185-3b99-9fbf-9f0d3c7b8a7d | -22.37228 | -50.41027 | 2025-08-20 04:38:00 | NPP-375D | LUTÉCIA | SÃO PAULO | Brasil | 3527900 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c3a76bbc-acb6-3e23-80bb-7e4d82e486e6 | -19.72936 | -48.97838 | 2025-08-20 04:38:00 | NPP-375D | COMENDADOR GOMES | MINAS GERAIS | Brasil | 3116902 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| cc3002ee-a1ba-3c4f-8e06-0e5ac4e4f959 | -22.55785 | -49.77373 | 2025-08-20 04:38:00 | NPP-375D | SÃO PEDRO DO TURVO | SÃO PAULO | Brasil | 3550506 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 26fc3a39-e644-32ba-8e23-f84bed404962 | -20.095 | -47.59865 | 2025-08-20 04:38:00 | NPP-375D | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 74fc81db-f729-3768-b10c-3dfc0c5100db | -20.43706 | -41.58806 | 2025-08-20 04:38:00 | NPP-375D | IÚNA | ESPÍRITO SANTO | Brasil | 3203007 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 670714d5-8239-3316-b531-012b7abb30b5 | -15.0566 | -54.83376 | 2025-08-20 04:38:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 34594c55-4f99-3283-9244-31f7ac9ba32e | -14.78139 | -59.67456 | 2025-08-20 04:38:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 6f5e0569-e45d-32a2-a5fd-4b68b0875b9c | -22.36892 | -50.40968 | 2025-08-20 04:38:00 | NPP-375D | LUTÉCIA | SÃO PAULO | Brasil | 3527900 | 35 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 02a7e05d-163d-3ffc-bba2-6a12e6dd8bfd | -16.34521 | -50.1749 | 2025-08-20 04:38:00 | NPP-375D | ADELÂNDIA | GOIÁS | Brasil | 5200159 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b8747f9d-2d47-3ba9-81b7-6c8e3a30850b | -15.00002 | -54.82462 | 2025-08-20 04:38:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 43529ff7-3250-35ac-951c-732e9e00a6df | -20.47003 | -45.07967 | 2025-08-20 04:38:00 | NPP-375D | ITAPECERICA | MINAS GERAIS | Brasil | 3133501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 32a91abb-afa8-3ed9-84cb-6be05ad0d3b7 | -20.50322 | -46.37678 | 2025-08-20 04:38:00 | NPP-375D | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6a15a072-f188-3ae9-8ac9-dd87c0c0eab4 | -16.01116 | -51.75818 | 2025-08-20 04:38:00 | NPP-375D | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dce8fd34-ed56-3e29-9ff7-b6a51f229642 | -21.89157 | -48.18777 | 2025-08-20 04:38:00 | NPP-375D | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f98189a6-8405-3270-8a8e-925053f5b061 | -23.49405 | -46.16106 | 2025-08-20 04:38:00 | NPP-375D | MOGI DAS CRUZES | SÃO PAULO | Brasil | 3530607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 99c63629-0160-3122-9574-577efbe5dd22 | -21.90825 | -47.22748 | 2025-08-20 04:38:00 | NPP-375D | SANTA CRUZ DAS PALMEIRAS | SÃO PAULO | Brasil | 3546306 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| eda39421-fda5-39ac-be31-b2ed0d5132a0 | -14.98523 | -54.81445 | 2025-08-20 04:38:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e24d7e9e-8c47-31ae-93f0-527e4072d583 | -23.19014 | -45.0073 | 2025-08-20 04:38:00 | NPP-375D | CUNHA | SÃO PAULO | Brasil | 3513603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 67caf0cf-7153-3cdd-b563-6ca4be46ec80 | -19.86492 | -49.82068 | 2025-08-20 04:38:00 | NPP-375D | SÃO FRANCISCO DE SALES | MINAS GERAIS | Brasil | 3161304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| cc0a0ed6-d350-38df-8ebb-3944eed7934a | -17.6402 | -52.20174 | 2025-08-20 04:38:00 | NPP-375D | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 658a662e-1f74-3dad-aa80-52b95a5ad75d | -15.87673 | -50.67487 | 2025-08-20 04:38:00 | NPP-375D | ITAPIRAPUÃ | GOIÁS | Brasil | 5211008 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README40.md)
