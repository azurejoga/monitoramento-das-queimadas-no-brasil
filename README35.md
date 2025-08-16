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

## Dados Diários - Página 35

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ae745808-12f0-3b94-be01-cc91758f91af | -13.13613 | -57.16525 | 2025-08-16 04:12:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3f558ef5-9617-305a-b116-4adb27cdad4b | -14.53237 | -48.59274 | 2025-08-16 04:12:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7e2a1b3e-37eb-34f0-bd51-11e6fadc71cb | -19.12306 | -46.68164 | 2025-08-16 04:12:00 | NPP-375D | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 97b75256-8ac7-3f43-a122-588e8fc4df00 | -14.93721 | -54.71342 | 2025-08-16 04:12:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 8fc42449-4aa7-3e09-89e9-380fde80c535 | -21.55436 | -46.85123 | 2025-08-16 04:14:00 | NPP-375D | SÃO JOSÉ DO RIO PARDO | SÃO PAULO | Brasil | 3549706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| d701ad03-bedb-3a54-812a-d4e96d960448 | -22.53471 | -46.89151 | 2025-08-16 04:14:00 | NPP-375D | MOGI MIRIM | SÃO PAULO | Brasil | 3530805 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.7 |
| 97b9b7c8-b82c-361b-8019-5319cdb4ad18 | -24.91965 | -52.36452 | 2025-08-16 04:14:00 | NPP-375D | PALMITAL | PARANÁ | Brasil | 4117800 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 71161d44-9cbb-31d6-8ab9-6e4746f2627b | -19.66461 | -49.37685 | 2025-08-16 04:14:00 | NPP-375D | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ee23b441-2dcc-3a1e-9861-599627eb48f8 | -20.418 | -46.53605 | 2025-08-16 04:14:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0f719d05-7ba4-37a6-b162-5348e57e6c7b | -22.77999 | -50.19881 | 2025-08-16 04:14:00 | NPP-375D | PALMITAL | SÃO PAULO | Brasil | 3535309 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 7fcc820e-e3b4-3c0a-bb8a-1db41805e205 | -20.90454 | -49.45931 | 2025-08-16 04:14:00 | NPP-375D | BADY BASSITT | SÃO PAULO | Brasil | 3504602 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| db2e5e73-e192-3819-af34-522ee4a498b0 | -22.97765 | -48.8058 | 2025-08-16 04:14:00 | NPP-375D | AVARÉ | SÃO PAULO | Brasil | 3504503 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9a2d9300-5e66-3c82-b2cb-e6fe8174f11e | -20.08254 | -49.42225 | 2025-08-16 04:14:00 | NPP-375D | PAULO DE FARIA | SÃO PAULO | Brasil | 3536604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 67.7 |
| eeffe146-c4d3-3afb-9068-5a090fcf97e0 | -21.38497 | -45.74494 | 2025-08-16 04:14:00 | NPP-375D | CAMPOS GERAIS | MINAS GERAIS | Brasil | 3111606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 1243108e-f869-3316-9f60-e17e2fcb42f5 | -22.97227 | -46.72372 | 2025-08-16 04:14:00 | NPP-375D | ITATIBA | SÃO PAULO | Brasil | 3523404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 091bc165-d83d-3bda-a02e-9572a6fcda87 | -22.95926 | -46.69711 | 2025-08-16 04:14:00 | NPP-375D | BRAGANÇA PAULISTA | SÃO PAULO | Brasil | 3507605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 8d5e4752-d454-3e5f-aadb-be882d388f8e | -20.39802 | -46.49266 | 2025-08-16 04:14:00 | NPP-375D | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 002281cb-2b17-3968-b0d4-430dfcc0b882 | -22.53878 | -46.88822 | 2025-08-16 04:14:00 | NPP-375D | MOGI MIRIM | SÃO PAULO | Brasil | 3530805 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.7 |
| f752fafd-5074-31f2-81bc-74e03261310e | -20.66409 | -49.38704 | 2025-08-16 04:14:00 | NPP-375D | IPIGUÁ | SÃO PAULO | Brasil | 3521150 | 35 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 46a6d5d5-a3f9-3633-a4c3-e1cbc5cd3e51 | -20.08449 | -49.43371 | 2025-08-16 04:14:00 | NPP-375D | PAULO DE FARIA | SÃO PAULO | Brasil | 3536604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.3 |
| c16a1e7a-d0c0-321b-b0bf-c14c6b28ec10 | -21.52589 | -49.14306 | 2025-08-16 04:14:00 | NPP-375D | NOVO HORIZONTE | SÃO PAULO | Brasil | 3533502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| a0be415f-da88-32d8-ac2c-c01ece93179a | -22.86131 | -45.29419 | 2025-08-16 04:14:00 | NPP-375D | ROSEIRA | SÃO PAULO | Brasil | 3544301 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| d57fe28e-e55f-31a7-a882-fcd312988f6a | -20.07764 | -49.42678 | 2025-08-16 04:14:00 | NPP-375D | PAULO DE FARIA | SÃO PAULO | Brasil | 3536604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 2220cf43-838c-3ede-9a65-e639efd16f47 | -20.41733 | -46.54001 | 2025-08-16 04:14:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6c941511-5ec7-3403-994f-cead2302ec83 | -21.5162 | -45.45261 | 2025-08-16 04:14:00 | NPP-375D | VARGINHA | MINAS GERAIS | Brasil | 3170701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 1b3bd215-aecb-3d75-bee5-550c8ff7ba63 | -20.15761 | -47.2922 | 2025-08-16 04:14:00 | NPP-375D | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 684aa5ce-7bf9-3f2b-8b3a-0272d2292ad4 | -22.53539 | -46.88756 | 2025-08-16 04:14:00 | NPP-375D | MOGI MIRIM | SÃO PAULO | Brasil | 3530805 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.7 |
| 18b59601-2f8c-38bf-96f0-9ec9b2309e2b | -20.15443 | -48.92045 | 2025-08-16 04:14:00 | NPP-375D | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d8ab2fba-ddaa-33ff-861d-ca361c24091b | -21.38162 | -45.74432 | 2025-08-16 04:14:00 | NPP-375D | CAMPOS GERAIS | MINAS GERAIS | Brasil | 3111606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 59f12156-c714-333f-bb8a-cc7b144bba9c | -20.66315 | -49.39222 | 2025-08-16 04:14:00 | NPP-375D | IPIGUÁ | SÃO PAULO | Brasil | 3521150 | 35 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 0b4cc5e5-3317-3893-aede-4a333bbdc45c | -20.66702 | -49.39303 | 2025-08-16 04:14:00 | NPP-375D | IPIGUÁ | SÃO PAULO | Brasil | 3521150 | 35 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 22c65b03-3ece-38cd-a09c-3169051e5eb5 | -23.34216 | -46.60505 | 2025-08-16 04:14:00 | NPP-375D | MAIRIPORÃ | SÃO PAULO | Brasil | 3528502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| b533ca52-4271-34e9-95ac-c00a82095c00 | -20.16114 | -47.29277 | 2025-08-16 04:14:00 | NPP-375D | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d235100e-ab84-38cf-92fb-ddc24abcfe55 | -21.28564 | -45.95151 | 2025-08-16 04:14:00 | NPP-375D | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 6327f109-657e-3efd-b678-2bd9cc91f612 | -23.16 | -50.6269 | 2025-08-16 04:14:00 | NPP-375D | CORNÉLIO PROCÓPIO | PARANÁ | Brasil | 4106407 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 44e423ba-3e32-370f-bf0f-62b02fe5e252 | -24.24069 | -50.20963 | 2025-08-16 04:14:00 | NPP-375D | VENTANIA | PARANÁ | Brasil | 4128534 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| beb4af33-c042-3745-9675-1aaac063327d | -20.66804 | -49.38973 | 2025-08-16 04:14:00 | NPP-375D | IPIGUÁ | SÃO PAULO | Brasil | 3521150 | 35 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 26d0205a-81f0-3709-9818-a872f52b9c08 | -23.38846 | -47.22372 | 2025-08-16 04:14:00 | NPP-375D | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 53f230ec-efd9-3e9e-b6ef-681282cb50ee | -20.08645 | -49.42304 | 2025-08-16 04:14:00 | NPP-375D | PAULO DE FARIA | SÃO PAULO | Brasil | 3536604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 67.7 |
| c58655be-b5a7-3c45-9b46-532bf69b48c1 | -23.18046 | -46.75497 | 2025-08-16 04:14:00 | NPP-375D | CAMPO LIMPO PAULISTA | SÃO PAULO | Brasil | 3509601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 8f4c89ee-71f4-3319-9406-e5d84bd138ef | -20.08058 | -49.43288 | 2025-08-16 04:14:00 | NPP-375D | PAULO DE FARIA | SÃO PAULO | Brasil | 3536604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.3 |
| 82c959cd-6339-3e74-9520-85840f78eaa1 | -24.11478 | -49.84726 | 2025-08-16 04:14:00 | NPP-375D | ARAPOTI | PARANÁ | Brasil | 4101606 | 41 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 3496dc13-f15f-3d89-853d-befba767298d | -20.08547 | -49.42838 | 2025-08-16 04:14:00 | NPP-375D | PAULO DE FARIA | SÃO PAULO | Brasil | 3536604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 67.7 |
| 5aac4388-a05d-304d-93b9-7c01bd954376 | -23.54049 | -47.58434 | 2025-08-16 04:14:00 | NPP-375D | ARAÇOIABA DA SERRA | SÃO PAULO | Brasil | 3502903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| f56e354b-b3d3-3c50-96a7-bf00ac4d9cb6 | -20.3971 | -46.56138 | 2025-08-16 04:14:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0f2927cb-bedc-3956-ab98-10efdba82b26 | -22.53811 | -46.89218 | 2025-08-16 04:14:00 | NPP-375D | MOGI MIRIM | SÃO PAULO | Brasil | 3530805 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.7 |
| ac30c114-5536-3da9-91bc-0698fbbf30a9 | -22.95589 | -46.69646 | 2025-08-16 04:14:00 | NPP-375D | BRAGANÇA PAULISTA | SÃO PAULO | Brasil | 3507605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 97269810-8bc0-3644-90c4-a288b7d88d07 | -20.46262 | -46.20964 | 2025-08-16 04:14:00 | NPP-375D | PIUMHI | MINAS GERAIS | Brasil | 3151503 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f496a27e-e428-3dd4-b86b-e69e20837e02 | -23.34895 | -47.29015 | 2025-08-16 04:14:00 | NPP-375D | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 90f53f34-a39a-33e3-b400-e0b5533861eb | -20.39461 | -46.49199 | 2025-08-16 04:14:00 | NPP-375D | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 889c1b25-d7a5-3290-b3f8-f8aa37b2724e | -20.42072 | -46.5408 | 2025-08-16 04:14:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c1470e33-c7b1-3ebc-a32f-3e6b7cf75f97 | -22.53945 | -46.88428 | 2025-08-16 04:14:00 | NPP-375D | MOGI MIRIM | SÃO PAULO | Brasil | 3530805 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 9c1651af-58c5-3df5-adba-f04a7540b963 | -20.42138 | -46.53687 | 2025-08-16 04:14:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9f9bd71e-5182-3caf-9250-9deb68005913 | -22.98128 | -48.80655 | 2025-08-16 04:14:00 | NPP-375D | AVARÉ | SÃO PAULO | Brasil | 3504503 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| bb1efeef-0c51-3225-b095-4ff55bf2df49 | -24.91535 | -52.36366 | 2025-08-16 04:14:00 | NPP-375D | PALMITAL | PARANÁ | Brasil | 4117800 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 225c2b67-2c60-38cb-a01c-5384cc63ddba | -20.39396 | -46.49586 | 2025-08-16 04:14:00 | NPP-375D | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f155e58d-e006-37c7-b3e2-bcd9bff7b3a7 | -23.34553 | -46.60571 | 2025-08-16 04:14:00 | NPP-375D | MAIRIPORÃ | SÃO PAULO | Brasil | 3528502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 8ba75f93-dc86-3655-bbef-ffacdec08bf4 | -20.41038 | -46.498 | 2025-08-16 04:14:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 66ba5e56-d3c6-3935-8ca4-b6c3e5d97d24 | -20.41598 | -46.54794 | 2025-08-16 04:14:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a19e860a-474f-39d4-9258-cdaa70e1b128 | -20.66796 | -49.38785 | 2025-08-16 04:14:00 | NPP-375D | IPIGUÁ | SÃO PAULO | Brasil | 3521150 | 35 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 128dd8cb-5ca6-3059-b146-5e66007886b3 | -22.34671 | -47.31582 | 2025-08-16 04:14:00 | NPP-375D | ARARAS | SÃO PAULO | Brasil | 3503307 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 6e006651-fee4-33d4-8a64-1b54900d5cc4 | -20.41101 | -46.49918 | 2025-08-16 04:14:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 9113ecce-7e74-3cf2-a413-914deb24b170 | -23.35991 | -47.32952 | 2025-08-16 04:14:00 | NPP-375D | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| c7783474-4cb0-3158-a157-b88a7b94f88f | -20.08156 | -49.42757 | 2025-08-16 04:14:00 | NPP-375D | PAULO DE FARIA | SÃO PAULO | Brasil | 3536604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 67.7 |
| bce0ae26-c753-3794-b7ab-7f2cdbdbc378 | -22.77719 | -49.16075 | 2025-08-16 04:14:00 | NPP-375D | IARAS | SÃO PAULO | Brasil | 3519253 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f8e39414-fc75-39b4-9663-450996dd2fb8 | -20.41665 | -46.54399 | 2025-08-16 04:14:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e013a844-c05e-390e-8d5d-8302f03f8836 | -21.58138 | -47.00426 | 2025-08-16 04:14:00 | NPP-375D | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 31cd6761-f36c-339f-bc2c-559695f33ff7 | -20.66417 | -49.38892 | 2025-08-16 04:14:00 | NPP-375D | IPIGUÁ | SÃO PAULO | Brasil | 3521150 | 35 | 33 | nan | nan | nan | Cerrado | 18.5 |
| 4c8a8ce6-f7ee-3c36-afc7-0f9e7991dfdc | -22.99889 | -45.51107 | 2025-08-16 04:14:00 | NPP-375D | TAUBATÉ | SÃO PAULO | Brasil | 3554102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| c517fbe8-472f-3ac3-ab46-4fe61e693c61 | -22.5357 | -46.80285 | 2025-08-16 04:14:00 | NPP-375D | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 38b0278e-1320-3dd3-99f1-9945d736860e | -22.53744 | -46.89613 | 2025-08-16 04:14:00 | NPP-375D | MOGI MIRIM | SÃO PAULO | Brasil | 3530805 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 301ca52b-f43a-3408-b8d7-d511c4a6dcff | -23.34617 | -46.6018 | 2025-08-16 04:14:00 | NPP-375D | MAIRIPORÃ | SÃO PAULO | Brasil | 3528502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 206e6ac6-6d55-305f-8004-6dfa540b7cb8 | -23.14552 | -47.08692 | 2025-08-16 04:14:00 | NPP-375D | ITUPEVA | SÃO PAULO | Brasil | 3524006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| c3a0918d-0c73-3b6d-b485-5c81f31178a9 | -20.07862 | -49.42146 | 2025-08-16 04:14:00 | NPP-375D | PAULO DE FARIA | SÃO PAULO | Brasil | 3536604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 41ae8ce2-ff94-3a62-8189-2816608d5ccf | -21.06223 | -50.30386 | 2025-08-16 04:14:00 | NPP-375D | BURITAMA | SÃO PAULO | Brasil | 3508108 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 3f998a9d-fa40-346a-9173-d2a90b032f90 | -22.33884 | -46.89124 | 2025-08-16 04:14:00 | NPP-375D | MOGI GUAÇU | SÃO PAULO | Brasil | 3530706 | 35 | 33 | nan | nan | nan | Cerrado | 0.4 |
| c69f3236-2778-3a19-89e8-2c07d80d62de | -20.15154 | -48.91472 | 2025-08-16 04:14:00 | NPP-375D | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1f2aaceb-cee4-34f1-a3e2-0f2599d575eb | -21.06626 | -50.30482 | 2025-08-16 04:14:00 | NPP-375D | BURITAMA | SÃO PAULO | Brasil | 3508108 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| a0b2deb8-5d9d-3140-879a-c70fd7a8cd5b | -23.78662 | -51.88394 | 2025-08-16 04:14:00 | NPP-375D | BOM SUCESSO | PARANÁ | Brasil | 4103206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| b480114c-cf93-3f36-8dba-5bb3b5696b75 | -28.83958 | -51.7145 | 2025-08-16 04:17:00 | NPP-375D | FAGUNDES VARELA | RIO GRANDE DO SUL | Brasil | 4307864 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 7cbe1d72-5667-3e67-846a-f6a2d2d70e54 | -8.9708 | -61.7033 | 2025-08-16 04:20:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 74.8 |
| 87445410-f639-34ab-ac3b-147ff67ce121 | -8.9893 | -61.7024 | 2025-08-16 04:20:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 73.6 |
| 36f487f0-6797-32cc-9a05-3d13ebb3db9e | -9.4992 | -60.547 | 2025-08-16 04:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 36e0f018-d251-3896-b6f1-cd692ef997cb | -14.9632 | -54.7143 | 2025-08-16 04:20:00 | GOES-19 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 50.4 |
| 91aaf561-f1ba-38ac-be0e-dbf89db1c0bf | -6.6327 | -60.0033 | 2025-08-16 04:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 39.5 |
| a88d54b2-d7d6-3043-a341-114421cec50f | -14.9628 | -54.7351 | 2025-08-16 04:20:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 91.6 |
| b1f5f6a3-2c08-329b-9630-8a1c0de06185 | -7.9148 | -61.7478 | 2025-08-16 04:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 58.7 |
| e533c4ce-f711-3ee9-a66e-c8851682b7fd | -7.4983 | -63.8199 | 2025-08-16 04:20:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 43.5 |
| 15cdcc67-45ff-302e-969b-5d92f85b33a8 | -9.1708 | -59.6568 | 2025-08-16 04:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 58.2 |
| 8b4dea80-c5b0-3caa-84e1-5a268ebce98b | -7.9149 | -61.7288 | 2025-08-16 04:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 22516f80-9848-3a65-9b11-5150c6af1faf | -6.9486 | -59.549 | 2025-08-16 04:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 43.8 |
| e8688eea-9486-3988-93a0-0908002e4cc1 | -14.9435 | -54.7374 | 2025-08-16 04:20:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 82.1 |
| ddf688a7-83fc-3145-88f6-c61f592993d3 | -9.4994 | -60.5278 | 2025-08-16 04:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 50.9 |
| 533c485f-20c4-3bf8-8b39-e0c5c81e9903 | -14.9441 | -54.6959 | 2025-08-16 04:20:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 107.4 |
| be4d4f5a-dd8c-3f14-ab75-8cdfe27ae7ba | -9.1709 | -59.6374 | 2025-08-16 04:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 77.8 |
| d451ab36-8ae6-385c-8b8e-7848af20fa5b | -6.9487 | -59.5297 | 2025-08-16 04:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 45.2 |
| 0a3c0d18-cc08-3692-be39-8105497b134d | -14.9438 | -54.7166 | 2025-08-16 04:20:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 66.3 |
| 54cf3892-3f63-33d8-b3e1-c88de222130c | -8.9709 | -61.6842 | 2025-08-16 04:20:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 81.3 |
| da136a3a-1e63-31d4-99c5-ae837b15fc9c | -2.54079 | -47.72165 | 2025-08-16 04:29:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 24c3ecaa-60bd-39b6-b6db-eb64572a8d42 | -2.47617 | -47.20661 | 2025-08-16 04:29:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |


[Clique aqui para ver as próximas entradas](README36.md)
