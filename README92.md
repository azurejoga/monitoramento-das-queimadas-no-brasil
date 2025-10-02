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

## Dados Diários - Página 92

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 74fd1746-63c0-3e1d-ad17-5b57f6d6d3e6 | -13.86598 | -47.95435 | 2025-10-02 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| daf0b3f6-f7c3-3343-8acf-635a7b68c324 | -12.2548 | -47.79347 | 2025-10-02 04:32:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 14f91e76-53a8-38af-aebc-6a00e7594175 | -14.21402 | -46.09304 | 2025-10-02 04:32:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 291e861e-9ac1-32f5-bc4a-67b390752fcf | -18.37931 | -45.12189 | 2025-10-02 04:32:00 | NPP-375D | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a33331c7-4709-33dc-b12f-c1dd6b54452a | -14.69402 | -49.62105 | 2025-10-02 04:32:00 | NPP-375D | PILAR DE GOIÁS | GOIÁS | Brasil | 5216908 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e361c567-8ffa-3dc2-a66e-b111b5b284db | -13.16834 | -47.83671 | 2025-10-02 04:32:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bf11dbf2-7610-328d-9d79-95291bc19739 | -12.69125 | -48.55425 | 2025-10-02 04:32:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0110cb46-a832-34c7-b18d-daee1b81e4c4 | -11.87508 | -51.22634 | 2025-10-02 04:32:00 | NPP-375D | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 23d306d7-c9ac-3aac-a28d-d228906b56a8 | -14.86465 | -48.39661 | 2025-10-02 04:32:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0a70e52d-35d8-37b4-86ff-bef1cebc478a | -13.01107 | -45.20996 | 2025-10-02 04:32:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 108795cd-a88d-37fd-83d1-74cf7dc80777 | -15.83607 | -46.2425 | 2025-10-02 04:32:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a4968377-3249-3a26-8cd8-41e4fb13cfea | -19.95386 | -43.66712 | 2025-10-02 04:32:00 | NPP-375D | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 1e6e238f-5e35-38b5-8dfe-0b6f8fc428b0 | -14.58666 | -48.3181 | 2025-10-02 04:32:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9279f601-8d7a-3c47-89e7-b7362677776c | -14.22384 | -46.09822 | 2025-10-02 04:32:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4af040c3-bf30-3c0b-bfd1-a6dab56f7214 | -15.1994 | -48.1662 | 2025-10-02 04:32:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 61f28471-fcf6-3abb-bf35-84b1b0a58526 | -14.41842 | -46.09933 | 2025-10-02 04:32:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fb39f4b1-ef89-3648-b01e-df0cbe2a710c | -15.25795 | -49.28657 | 2025-10-02 04:32:00 | NPP-375D | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fb8b6562-50a8-38d5-9109-42d5ca317855 | -13.80755 | -47.5135 | 2025-10-02 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 98dc7c40-381d-38f6-b6d4-14d6f312f4fe | -13.80643 | -47.54259 | 2025-10-02 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 10f44ecf-2c14-33c4-b3b9-591645a2f089 | -13.61943 | -47.2891 | 2025-10-02 04:32:00 | NPP-375D | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8b71ccb8-705f-3ac1-850f-fec42920454f | -13.20842 | -48.50028 | 2025-10-02 04:32:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2458689e-d836-303f-9cb5-8dc83d7310c0 | -13.86675 | -43.60122 | 2025-10-02 04:32:00 | NPP-375D | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e14c01e4-f068-315c-a5fb-7ec46b9c922e | -14.43262 | -46.3517 | 2025-10-02 04:32:00 | NPP-375D | BURITINÓPOLIS | GOIÁS | Brasil | 5203962 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e08ad385-1c90-314e-a841-e2e1736f74f1 | -18.42828 | -46.53254 | 2025-10-02 04:32:00 | NPP-375D | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 40d627c5-65fd-3f06-bbce-f9ecda4a6bec | -15.3257 | -46.29394 | 2025-10-02 04:32:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c68ac1df-a21d-3345-87e6-84bdbe1ae3bb | -14.40691 | -46.10538 | 2025-10-02 04:32:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 363ae516-ae32-3f6c-b261-be5d67a28fc3 | -15.31831 | -46.39156 | 2025-10-02 04:32:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1f91b1b4-8297-32dd-bae5-0e795c363086 | -17.68298 | -44.43663 | 2025-10-02 04:32:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4db139e0-239f-3a2e-b5ea-198d694bfe0f | -14.79992 | -46.96652 | 2025-10-02 04:32:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| eaad6afb-1fea-3e1f-87e3-630bb697ed52 | -13.18888 | -47.83644 | 2025-10-02 04:32:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 192b7407-8290-320e-b522-0575073d63f7 | -14.42302 | -46.1394 | 2025-10-02 04:32:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ef281793-683e-3241-b13c-69b878e9615a | -14.37316 | -45.96644 | 2025-10-02 04:32:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4aaf4cc8-b725-3920-8ded-e91ac78326a0 | -13.57246 | -47.58944 | 2025-10-02 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 83bebec0-3074-3da3-8616-5c20795eeb7c | -15.75384 | -43.68408 | 2025-10-02 04:32:00 | NPP-375D | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b8750e55-8a96-332e-bf27-62d9a3eee998 | -12.14968 | -46.67339 | 2025-10-02 04:32:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f0e27e3d-2901-3138-9afb-7befe48f5b34 | -19.2503 | -47.25169 | 2025-10-02 04:32:00 | NPP-375D | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8c1d1df2-48d0-3cd8-8e46-52542f2ba9f1 | -15.83208 | -42.62666 | 2025-10-02 04:32:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 5d3d4383-cca5-34d2-ae59-f940d2fd16b6 | -14.31419 | -46.00481 | 2025-10-02 04:32:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 4f78be5e-c06b-3a74-92f4-8957161ced99 | -13.64936 | -47.30867 | 2025-10-02 04:32:00 | NPP-375D | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a53039c6-d7f8-33ec-b0df-4b3a8e38c135 | -14.70897 | -48.20625 | 2025-10-02 04:32:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 6bd3db15-5fde-3c7d-8951-0416164d5c6d | -13.63985 | -47.65493 | 2025-10-02 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a6e9eea7-d932-30a5-b6a4-fa884ce0af8c | -14.91641 | -47.81488 | 2025-10-02 04:32:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d6c70d9b-2c58-32fb-a784-6645c18dbf91 | -14.5864 | -46.72042 | 2025-10-02 04:32:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 51e88e41-d0cf-37e1-9fb4-1089265a8edd | -14.87217 | -48.29195 | 2025-10-02 04:32:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5789e846-9332-3738-9b15-c4388779944b | -18.87728 | -46.38166 | 2025-10-02 04:32:00 | NPP-375D | LAGOA FORMOSA | MINAS GERAIS | Brasil | 3137502 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a5d14f16-bdac-3041-9818-133a47d77e33 | -12.36532 | -45.78427 | 2025-10-02 04:32:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 45ed104d-1f22-3007-8f45-14095439b35a | -14.29968 | -45.95918 | 2025-10-02 04:32:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 21501eee-1fc4-378e-86c5-71ff28099061 | -12.95404 | -46.43073 | 2025-10-02 04:32:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 141339ef-5198-3e43-8632-f928f601e917 | -14.69387 | -48.25869 | 2025-10-02 04:32:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 596f121f-9d7d-3a47-99f4-3c3e9b6f3477 | -13.31292 | -47.82078 | 2025-10-02 04:32:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| fb5459b1-fdff-3216-a111-1332d15b6fc5 | -13.79431 | -48.04876 | 2025-10-02 04:32:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e348b626-e8f8-38d8-ad0f-ad108c8c1b92 | -13.57038 | -47.27394 | 2025-10-02 04:32:00 | NPP-375D | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0d58e837-a1b5-3330-9c63-bfc2c74d43bf | -12.68739 | -47.56224 | 2025-10-02 04:32:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7cc86571-3a40-39a2-b158-c0811883d869 | -13.91571 | -48.07212 | 2025-10-02 04:32:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b0313075-0f9c-382d-b88e-cb44a8c97943 | -15.75924 | -43.67422 | 2025-10-02 04:32:00 | NPP-375D | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 814f5280-6b7d-36c3-a98f-b3586792158f | -14.35986 | -45.9604 | 2025-10-02 04:32:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1f7092dc-5bdb-36bf-9838-1743360866f0 | -13.0152 | -45.20646 | 2025-10-02 04:32:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5ea33e58-5456-3772-9bc7-5d85df2bc985 | -12.8362 | -46.86263 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7d77651f-7122-3a09-b6fd-4d56e6513944 | -13.74498 | -48.69171 | 2025-10-02 04:32:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b6a58cad-0478-3cfc-a125-a6129e2259c4 | -13.95646 | -48.11145 | 2025-10-02 04:32:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f2900ea9-281b-391c-990b-77fc8788785c | -15.56147 | -48.18154 | 2025-10-02 04:32:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 62b58d54-3705-3b2d-928b-22a12b1d2a34 | -12.47919 | -47.27074 | 2025-10-02 04:32:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b9af58b7-91b5-3230-b7f8-924f73009242 | -15.46143 | -45.88303 | 2025-10-02 04:32:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ca589c23-fd5c-3a82-9ec7-60a9ab11007f | -13.31149 | -47.5912 | 2025-10-02 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a743e864-706d-3292-b1c7-e38af71b8974 | -13.32701 | -47.22819 | 2025-10-02 04:32:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2d7c0173-840c-3f3a-a780-ba29c3d5c87a | -13.78164 | -47.9992 | 2025-10-02 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 663881ed-0255-3a54-a4e9-15512adc9177 | -12.86765 | -47.01474 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3e42b466-931e-3d26-ac74-60b6e8432325 | -17.67818 | -43.83027 | 2025-10-02 04:32:00 | NPP-375D | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d076794b-1f26-3b2a-b7e2-a02a354f6199 | -17.70203 | -46.88589 | 2025-10-02 04:32:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c4268cc8-214d-3f49-b1fa-86cbbac6c355 | -13.30312 | -46.99552 | 2025-10-02 04:32:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f84ecc8b-c2a0-3314-ba05-07e80e0d52cc | -12.81752 | -47.05062 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8410da4c-dd46-338f-b05c-02e48c88989c | -11.46655 | -51.51336 | 2025-10-02 04:32:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dec86eb4-5a53-3998-9cf2-14eeef4eb9e2 | -11.78925 | -48.44643 | 2025-10-02 04:32:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b1b6e204-363a-3bfe-95a5-a84ee1822192 | -17.17807 | -47.02032 | 2025-10-02 04:32:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4cd9c979-8302-3869-abaa-4b28696a711b | -15.18854 | -46.41887 | 2025-10-02 04:32:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 2d11b4c5-005c-3567-bc6a-d3b578fae1d3 | -14.79373 | -42.82673 | 2025-10-02 04:32:00 | NPP-375D | URANDI | BAHIA | Brasil | 2932606 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 189a29e8-1c28-373c-99e2-5c3dcc88ccdf | -19.89804 | -44.93795 | 2025-10-02 04:32:00 | NPP-375D | NOVA SERRANA | MINAS GERAIS | Brasil | 3145208 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3162166b-87cc-3656-8b48-45b59b27777c | -13.85933 | -47.95325 | 2025-10-02 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 9c67b1d2-9634-3fde-82e0-564fedd1f9fd | -13.46898 | -47.25432 | 2025-10-02 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a0007ea1-4f52-3b96-b5d8-bee8e36335b6 | -13.28698 | -47.25428 | 2025-10-02 04:32:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 0ff896be-3297-3daf-bafe-a6760872d034 | -15.26048 | -48.01054 | 2025-10-02 04:32:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 69429262-10ed-3348-91ad-dda549a0551f | -12.83844 | -46.87046 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9ff4582d-6904-3250-bcc8-ad8170b225bb | -11.93956 | -47.88328 | 2025-10-02 04:32:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8f62046c-a443-38c5-b178-cd6eaf341785 | -13.15113 | -47.83752 | 2025-10-02 04:32:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3d2e9b67-4176-3272-a786-a16d754f63b7 | -14.35666 | -47.12936 | 2025-10-02 04:32:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 21fc9939-c76f-3df0-b2c7-6f8bcc81edfa | -15.31588 | -46.28856 | 2025-10-02 04:32:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 5f40b80d-8157-380d-a869-b9bb86030c57 | -13.75552 | -48.01313 | 2025-10-02 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e9d92f19-aa74-3153-a8e4-461a555934b7 | -15.28163 | -46.40119 | 2025-10-02 04:32:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 324363d5-f853-3e6f-85d6-367710804696 | -15.25224 | -49.3006 | 2025-10-02 04:32:00 | NPP-375D | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 7316c63f-b9fd-3ff3-ac3c-5ee40f0cf463 | -16.03231 | -50.86376 | 2025-10-02 04:32:00 | NPP-375D | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 7c1fa820-c4e4-3285-a363-23083930e416 | -14.43092 | -46.36311 | 2025-10-02 04:32:00 | NPP-375D | BURITINÓPOLIS | GOIÁS | Brasil | 5203962 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 24cb6cce-60d9-3d8f-90cd-1a1e60013577 | -15.1724 | -49.0825 | 2025-10-02 04:32:00 | NPP-375D | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 89842fd6-6aee-3249-abbd-ce150ee6c9a5 | -15.93681 | -46.21716 | 2025-10-02 04:32:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e87fa239-03b6-3388-b042-cae68221cf58 | -13.75054 | -48.00136 | 2025-10-02 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 64afd929-86b9-3a10-88f2-e215e8f6780c | -12.25974 | -47.8269 | 2025-10-02 04:32:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3d02b905-64a9-39bb-9649-2ea3ecc7a0c3 | -14.89934 | -48.30706 | 2025-10-02 04:32:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4a5a7395-edc5-35ba-adfa-7cb5ab0e9951 | -12.68835 | -48.5722 | 2025-10-02 04:32:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| cc88b4e4-fa85-3445-b72f-62473b5db129 | -13.61552 | -47.29216 | 2025-10-02 04:32:00 | NPP-375D | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d6620b61-f7e5-35f2-bdaa-fed02a25a51e | -12.51014 | -46.84096 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bc3d1d24-51d6-38e5-b33f-8d386df2729f | -16.04802 | -51.02695 | 2025-10-02 04:32:00 | NPP-375D | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |


[Clique aqui para ver as próximas entradas](README93.md)
