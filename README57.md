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

## Dados Diários - Página 57

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5c5b36f6-692a-339e-9493-2b71e76cd12e | -12.14903 | -48.97145 | 2026-09-12 11:49:00 | TERRA_M-M | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 4e29b4cc-265e-370c-a711-e7ba55e41b33 | -10.48027 | -48.6412 | 2026-09-12 11:49:00 | TERRA_M-M | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 25ac90a5-6336-34b7-80e0-b1fdc7bcbc0c | -12.14035 | -48.95461 | 2026-09-12 11:49:00 | TERRA_M-M | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 31.1 |
| de65a4a8-fd6d-3358-8d8f-3931ea836735 | -10.50655 | -51.30413 | 2026-09-12 11:49:00 | TERRA_M-M | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 13.1 |
| cc6ba618-f7d4-3322-8796-e2d43e3bba13 | -8.8026 | -46.93944 | 2026-09-12 11:49:00 | TERRA_M-M | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 85241e79-1e50-33ab-8603-942cff299ace | -14.11653 | -47.52854 | 2026-09-12 11:49:00 | TERRA_M-M | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 32.4 |
| e7fe2a88-bb24-3ab2-adfc-9ae78e8af1b5 | -8.46192 | -47.52554 | 2026-09-12 11:49:00 | TERRA_M-M | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 93c29f35-5fa6-37b1-af27-73ae64ff7d48 | -10.95703 | -48.33937 | 2026-09-12 11:49:00 | TERRA_M-M | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 241.1 |
| a19a9eeb-9771-391d-8952-5647b2f20236 | -16.14886 | -43.62964 | 2026-09-12 11:49:00 | TERRA_M-M | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 25.4 |
| d929651e-639a-3fd3-adff-046ef6b39e31 | -10.49696 | -51.36879 | 2026-09-12 11:49:00 | TERRA_M-M | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| e69f1cd4-faae-3bef-bfe9-8e9e0835517f | -13.33312 | -51.62882 | 2026-09-12 11:49:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 975f186a-fda8-30d7-b0e9-308f6ab46f5f | -8.64618 | -47.39813 | 2026-09-12 11:49:00 | TERRA_M-M | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| b0263e20-aebb-33ea-b854-e6fb391876e6 | -8.46064 | -47.53453 | 2026-09-12 11:49:00 | TERRA_M-M | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 11.0 |
| be5ae5b4-6004-3655-b46a-9d9e9ee0bc03 | -13.287 | -43.55618 | 2026-09-12 11:49:00 | TERRA_M-M | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 03b76028-fed7-3182-aac4-b4cfbed4f3f5 | -10.50951 | -51.31098 | 2026-09-12 11:49:00 | TERRA_M-M | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 11.4 |
| e1d0a608-3e01-3b9f-b522-2930b8f8eeaa | -10.55068 | -45.21199 | 2026-09-12 11:49:00 | TERRA_M-M | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 19fc7d3a-1b06-3424-a4de-e3d5d61e4cf2 | -10.41317 | -43.28763 | 2026-09-12 11:49:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 12.4 |
| 5b65c652-d3c0-37c4-8e35-0cee742c1597 | -11.38041 | -46.80751 | 2026-09-12 11:49:00 | TERRA_M-M | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 431.2 |
| de47f5a8-826f-3f7f-847b-3eebbc711a45 | -13.38012 | -48.00521 | 2026-09-12 11:49:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 78618207-4439-39d9-81fc-e8e20615c6c3 | -17.76525 | -45.38335 | 2026-09-12 11:49:00 | TERRA_M-M | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 8df49155-1b3a-3813-bced-b300a4d96048 | -11.375 | -46.84743 | 2026-09-12 11:49:00 | TERRA_M-M | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 21.6 |
| fa9a8e68-0bcf-3bc9-914f-925db223ab2a | -16.58841 | -53.05159 | 2026-09-12 11:49:00 | TERRA_M-M | PONTE BRANCA | MATO GROSSO | Brasil | 5106703 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| f306746f-2b9d-3edc-b6a3-6d8698d1a332 | -12.13906 | -48.96358 | 2026-09-12 11:49:00 | TERRA_M-M | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 23.3 |
| 8f91517e-e09b-3971-81da-40d6ce517834 | -16.31979 | -49.52366 | 2026-09-12 11:49:00 | TERRA_M-M | INHUMAS | GOIÁS | Brasil | 5210000 | 52 | 33 | nan | nan | nan | Cerrado | 19.7 |
| f288b5be-496b-37c4-8aec-9b76698d5222 | -13.36985 | -48.01306 | 2026-09-12 11:49:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 66491a6b-8d13-33e5-8f33-7a2d8d8e61d0 | -10.3358 | -48.0281 | 2026-09-12 11:49:00 | TERRA_M-M | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 50.1 |
| ed970bd6-4bfa-37b4-8e80-aa438c5dde3f | -13.32832 | -51.65999 | 2026-09-12 11:49:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 43d22dea-cc0b-3a43-86ae-d42adfca4cff | -13.45865 | -48.50204 | 2026-09-12 11:49:00 | TERRA_M-M | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 0c5dbc27-7fd2-3713-9b43-adde0becfcc2 | -13.48663 | -48.49663 | 2026-09-12 11:49:00 | TERRA_M-M | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 174ea5ef-66f5-3101-bc6d-651be1a45f74 | -12.44695 | -49.59018 | 2026-09-12 11:49:00 | TERRA_M-M | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| de7739c5-79f0-3505-b438-3dfe68bd82b7 | -10.89863 | -47.83023 | 2026-09-12 11:49:00 | TERRA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 7bc7c7d4-95bc-3e17-9a24-71867dcd6c3e | -13.27646 | -43.64297 | 2026-09-12 11:49:00 | TERRA_M-M | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 44.8 |
| cb89f28b-a933-3d54-92d3-4d3d885b3365 | -12.6457 | -51.41954 | 2026-09-12 11:49:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 75.6 |
| a3cc3751-5003-33ea-b7b8-0f9b6fae8bee | -13.56098 | -47.69329 | 2026-09-12 11:49:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 8.0 |
| a3eca61f-ea66-38f9-b52b-ff0700f96948 | -12.71896 | -43.17165 | 2026-09-12 11:49:00 | TERRA_M-M | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 19.6 |
| a114ef3d-02d6-3f08-98a9-64d504e43213 | -8.50803 | -50.14708 | 2026-09-12 11:49:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 0948ba31-e068-3f71-a9ac-367edb98f774 | -8.81681 | -46.9037 | 2026-09-12 11:49:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 88db229f-18e1-3c8a-886f-84f3e5d95f54 | -13.36016 | -41.67407 | 2026-09-12 11:49:00 | TERRA_M-M | JUSSIAPE | BAHIA | Brasil | 2918605 | 29 | 33 | nan | nan | nan | Caatinga | 21.7 |
| 67b2aba3-ac3e-3518-a197-3b2b7c11caf8 | -8.44415 | -47.52311 | 2026-09-12 11:49:00 | TERRA_M-M | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| b5d394c6-4f8f-3a66-8adf-ff55c5e3f69d | -11.36974 | -46.81636 | 2026-09-12 11:49:00 | TERRA_M-M | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 101.2 |
| 8028c929-fe70-373a-8b81-fbe066897b30 | -8.80129 | -46.94876 | 2026-09-12 11:49:00 | TERRA_M-M | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 4c7af3f1-ff8b-33c3-81c0-2254b89c371c | -10.31567 | -46.44541 | 2026-09-12 11:49:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 36.6 |
| d741a509-61f2-3218-970c-f904b30f4ed4 | -9.67624 | -46.01691 | 2026-09-12 11:49:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 25c30048-6667-3dc4-ab67-348e96919556 | -12.09189 | -47.26502 | 2026-09-12 11:49:00 | TERRA_M-M | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 9d64e68f-bc4a-3e1c-97e1-c0e0ea8d5513 | -11.80477 | -46.38728 | 2026-09-12 11:49:00 | TERRA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 19c71ff3-6e81-3c4b-8082-09847603f49e | -7.57902 | -50.54942 | 2026-09-12 11:49:00 | TERRA_M-M | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 71b61544-8a39-3e52-9c86-9f6bad281b28 | -13.3237 | -51.62737 | 2026-09-12 11:49:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 21.9 |
| a5c7f881-afef-3cc8-ba15-8f6c0ba225b0 | -16.02617 | -47.90196 | 2026-09-12 11:49:00 | TERRA_M-M | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 76a8e32e-521a-3d0b-af56-3b76ff7a8c15 | -10.50502 | -51.31441 | 2026-09-12 11:49:00 | TERRA_M-M | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 9.1 |
| f7967b47-56ea-35b8-aef7-893056076ed8 | -10.63564 | -46.11765 | 2026-09-12 11:49:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 786ab41b-52d0-369e-b32e-aa45b89f0469 | -8.81164 | -46.94066 | 2026-09-12 11:49:00 | TERRA_M-M | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 20.6 |
| 745820b1-95e3-3276-8f87-30798ba5dcfc | -11.38177 | -46.79747 | 2026-09-12 11:49:00 | TERRA_M-M | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 20.7 |
| 988cb755-59ae-3903-89d1-f8b1dc614bc4 | -13.93356 | -43.80047 | 2026-09-12 11:49:00 | TERRA_M-M | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 23.1 |
| 02c12621-446d-39db-902a-870690e18d4a | -13.62302 | -47.91276 | 2026-09-12 11:49:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 9b798c02-60cf-3bb2-ae48-ec58f630545e | -8.81034 | -46.94998 | 2026-09-12 11:49:00 | TERRA_M-M | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 345e01e4-5d69-3cc3-90d4-a1ade5a0a1b3 | -11.37635 | -46.83751 | 2026-09-12 11:49:00 | TERRA_M-M | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 25.2 |
| 982f8cb2-77cb-39a7-a41d-19a5724b5246 | -15.14478 | -47.61568 | 2026-09-12 11:49:00 | TERRA_M-M | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 8.4 |
| eba5f09e-0d97-3d0c-b468-f55db40e554d | -11.37245 | -46.79624 | 2026-09-12 11:49:00 | TERRA_M-M | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 81.1 |
| a18d2abc-ba17-3139-ae87-3757ea2490fa | -13.37885 | -48.01442 | 2026-09-12 11:49:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 38.3 |
| f401dade-007c-3486-b874-dbbc2be77f2b | -11.3536 | -46.8099 | 2026-09-12 11:50:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 86.9 |
| bda44c52-34fa-3eb7-9647-767135063e96 | -11.3727 | -46.8074 | 2026-09-12 11:50:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 423.3 |
| 24fd0ab8-3ba6-3a9e-869c-a83ca0791a6b | -11.3731 | -46.7849 | 2026-09-12 11:50:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 141d48a5-97e0-343a-b2aa-f0a539495380 | -12.6535 | -51.4246 | 2026-09-12 11:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 75.4 |
| a907105d-dcc6-3512-8119-7c57f32b4271 | -11.3723 | -46.8299 | 2026-09-12 11:50:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 253.3 |
| d4cdcd7f-83f7-3a14-9cbb-587b7edb8f01 | -19.15286 | -46.81743 | 2026-09-12 11:51:00 | TERRA_M-M | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 39.4 |
| 51ae2e9b-1dd8-3260-9ca7-0b02eff688aa | -19.59999 | -52.62327 | 2026-09-12 11:51:00 | TERRA_M-M | ÁGUA CLARA | MATO GROSSO DO SUL | Brasil | 5000203 | 50 | 33 | nan | nan | nan | Cerrado | 4.4 |
| b9b0c1e5-89c3-3665-991e-2c807900e17e | -19.1454 | -46.81057 | 2026-09-12 11:51:00 | TERRA_M-M | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 37.3 |
| 9fef047f-b908-3f5c-aa7f-f692d1be173d | -19.08686 | -44.36931 | 2026-09-12 11:51:00 | TERRA_M-M | CORDISBURGO | MINAS GERAIS | Brasil | 3118908 | 31 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 0bbffcae-f6c3-3296-bdcf-8fe3fd325631 | -20.463 | -44.78003 | 2026-09-12 11:51:00 | TERRA_M-M | CLÁUDIO | MINAS GERAIS | Brasil | 3116605 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.8 |
| d2c2751c-7b92-33b2-888f-aa7fd65e4f01 | -19.74346 | -46.46322 | 2026-09-12 11:51:00 | TERRA_M-M | PRATINHA | MINAS GERAIS | Brasil | 3153004 | 31 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 5c8fb4b7-23ec-3ca1-b95a-c54d95f3d3dc | -19.1438 | -46.82336 | 2026-09-12 11:51:00 | TERRA_M-M | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 618d5987-b9ec-350d-a6ad-aef1bd69f582 | -18.93948 | -46.82476 | 2026-09-12 11:51:00 | TERRA_M-M | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 9.5 |
| dea335c6-737c-35d6-88b6-117cb5f28274 | -19.73881 | -46.45666 | 2026-09-12 11:51:00 | TERRA_M-M | PRATINHA | MINAS GERAIS | Brasil | 3153004 | 31 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 3c1fb5bd-6f78-381b-8739-3a9b3443a296 | -11.3731 | -46.7849 | 2026-09-12 12:00:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 65.1 |
| f24a0663-d646-3afc-8e01-2481f90eeb75 | -11.372 | -46.8524 | 2026-09-12 12:00:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 70.5 |
| 98af13c6-a8bd-3606-a83b-af0bd31f2432 | -13.3192 | -51.6626 | 2026-09-12 12:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 75.1 |
| d220aa99-cf1b-325f-a3ca-0b05984e1a2e | -11.3723 | -46.8299 | 2026-09-12 12:00:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 269.6 |
| 67a14b87-d181-30cd-a061-0fea82818800 | -11.3727 | -46.8074 | 2026-09-12 12:00:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 335.5 |
| da2c904c-d0d1-350e-896b-25ee95b3245b | -11.3727 | -46.8074 | 2026-09-12 12:10:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 270.5 |
| d6f87e5f-3168-3a5c-bca6-9b9e638fc7c2 | -10.3472 | -48.022 | 2026-09-12 12:10:00 | GOES-19 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 69.3 |
| 83950214-c535-3e14-b913-e58090806377 | -11.372 | -46.8524 | 2026-09-12 12:10:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 73.3 |
| 921b639d-d1ca-3b03-b74a-a02bac65a452 | -11.3723 | -46.8299 | 2026-09-12 12:10:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 347.2 |
| 4d874300-36fb-3cc3-9003-d97aded349d6 | -11.3536 | -46.8099 | 2026-09-12 12:10:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 126.8 |
| 98e812ca-e157-3d24-a7e4-770f16184d03 | -13.3192 | -51.6626 | 2026-09-12 12:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 110.8 |
| 2a22f441-e898-37a2-bd51-347f75af4715 | -13.3192 | -51.6626 | 2026-09-12 12:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 126.1 |
| 2d8d7465-f618-3a1a-99c1-c3c2d55a2df2 | -8.5415 | -54.7187 | 2026-09-12 12:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 100.5 |
| 2bf98b35-6898-368b-ae71-181e5a0ade76 | -13.3384 | -51.6602 | 2026-09-12 12:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 78.8 |
| 790e093c-5e2d-3462-87dd-43db7afb9660 | -7.2147 | -43.7001 | 2026-09-12 12:20:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 78.8 |
| 8b8f63cd-982e-377b-bcc0-c15fe509aef4 | -11.3723 | -46.8299 | 2026-09-12 12:20:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 137.8 |
| 255d9bad-57e9-3568-b7d6-d9512fc8bc90 | -11.3727 | -46.8074 | 2026-09-12 12:20:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 118.6 |
| a007960d-4ad6-335a-bd8c-cc288b4583d6 | -10.2933 | -45.2702 | 2026-09-12 12:20:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 68.7 |
| eaa4f592-e095-32aa-9a4a-60797a173ee2 | -12.1388 | -48.9672 | 2026-09-12 12:20:00 | GOES-19 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 72.3 |
| 8fc1ea0f-803e-3669-8fc5-1c9fa87c0970 | -8.002 | -44.0163 | 2026-09-12 12:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 102.8 |
| 1196c782-d2c6-34f2-b634-654bb65e66ff | -10.5664 | -51.356 | 2026-09-12 12:20:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 96.9 |
| 58618c45-0a38-3e5b-b161-4fb93ea14333 | -10.2933 | -45.2702 | 2026-09-12 12:30:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 78.7 |
| 254c9e0f-d17b-3dc4-b1c6-bebddfcf6ca2 | -8.002 | -44.0163 | 2026-09-12 12:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 109.6 |
| 7f43e90f-4525-3667-9c6d-cee7c905605e | -10.5664 | -51.356 | 2026-09-12 12:30:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 92.2 |
| 6355c198-6c7a-3447-bfab-a39cdcf3e22d | -2.9579 | -50.3988 | 2026-09-12 12:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 177.9 |
| d911bca8-5b24-34cf-99c1-1772bd7ceb1b | -12.1388 | -48.9672 | 2026-09-12 12:30:00 | GOES-19 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 93.5 |
| d2bbec38-1833-33fa-8735-6a5fd515cb8a | -11.3731 | -46.7849 | 2026-09-12 12:30:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 63.0 |


[Clique aqui para ver as próximas entradas](README58.md)
