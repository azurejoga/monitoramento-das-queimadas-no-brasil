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
| afdcdb72-fd5f-356d-a0b1-d07d46afc422 | -19.16808 | -46.56164 | 2025-07-22 04:04:00 | NOAA-20 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8d147d9f-74eb-3fe1-987b-354b0bf89081 | -20.3058 | -46.6792 | 2025-07-22 04:04:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2e6368b2-400b-3cb5-af47-acff9132bb2e | -22.06571 | -47.14138 | 2025-07-22 04:04:00 | NOAA-20 | AGUAÍ | SÃO PAULO | Brasil | 3500303 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 92f0390c-452c-3712-990e-a3271be5d005 | -18.16781 | -39.64354 | 2025-07-22 04:04:00 | NOAA-20 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 1ca19a42-a16e-3ca7-b7b0-a0e8d5155c13 | -21.0554 | -41.83935 | 2025-07-22 04:04:00 | NOAA-20 | NATIVIDADE | RIO DE JANEIRO | Brasil | 3303104 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 4ba25cd6-ce0c-3309-aab3-b42281861ea3 | -21.49264 | -47.27528 | 2025-07-22 04:04:00 | NOAA-20 | TAMBAÚ | SÃO PAULO | Brasil | 3553302 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c1b2fb22-54e3-3a8b-89ab-1855a251e888 | -18.4171 | -44.18513 | 2025-07-22 04:04:00 | NOAA-20 | SANTO HIPÓLITO | MINAS GERAIS | Brasil | 3160603 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 751bbcda-0b1c-3797-8488-3375a2da8838 | -20.31092 | -46.67141 | 2025-07-22 04:04:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b7088d5c-67f8-3f44-b7e8-59949f0034f8 | -22.1567 | -47.37109 | 2025-07-22 04:04:00 | NOAA-20 | LEME | SÃO PAULO | Brasil | 3526704 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 9f809f30-dc0b-3ec0-bd62-8a921e24ecfd | -18.13235 | -44.27721 | 2025-07-22 04:04:00 | NOAA-20 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1e706858-b574-33fd-a3cb-94afd4ed1b85 | -18.19649 | -45.04508 | 2025-07-22 04:04:00 | NOAA-20 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a1c3a4a0-269b-3f15-8f07-6b748c1855ee | -18.19715 | -45.04118 | 2025-07-22 04:04:00 | NOAA-20 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 055b0b6a-7602-3073-8660-e4601992aa4c | -16.06995 | -43.64632 | 2025-07-22 04:04:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a144b424-7d9c-3dff-8dfd-5958f33f66de | -21.64994 | -44.2282 | 2025-07-22 04:04:00 | NOAA-20 | ANDRELÂNDIA | MINAS GERAIS | Brasil | 3102803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 0534957a-0f69-35ff-9dc1-13eb628f1bcf | -22.82763 | -46.14689 | 2025-07-22 04:04:00 | NOAA-20 | CAMANDUCAIA | MINAS GERAIS | Brasil | 3110509 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| 5bbaa875-1488-39d5-afc8-89a619cde14e | -17.86257 | -45.23232 | 2025-07-22 04:04:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 469f4891-30af-36ea-96a3-d66220a0af44 | -19.15719 | -46.55948 | 2025-07-22 04:04:00 | NOAA-20 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 39341a40-2b85-3f6c-98ca-fad3813913bf | -18.65946 | -55.72972 | 2025-07-22 04:04:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| c1d25c17-6391-3e33-b8cb-21fc462eb9c8 | -18.66136 | -55.72699 | 2025-07-22 04:04:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 072e75f2-f090-3392-a891-bce06fea6fd2 | -21.11198 | -48.64376 | 2025-07-22 04:04:00 | NOAA-20 | PIRANGI | SÃO PAULO | Brasil | 3539004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 242aa767-4027-322b-9618-e98f8b54d071 | -20.06443 | -41.40159 | 2025-07-22 04:04:00 | NOAA-20 | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.8 |
| 35b2a5bc-fe0e-39f5-8348-099f627f02e0 | -17.02326 | -47.19765 | 2025-07-22 04:04:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 66a143e6-e9d9-3b94-a7f0-229d898d594f | -19.16728 | -46.56612 | 2025-07-22 04:04:00 | NOAA-20 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d37f26f7-05a4-3ac7-9104-f3fa9be8f23a | -18.95618 | -45.73772 | 2025-07-22 04:04:00 | NOAA-20 | TIROS | MINAS GERAIS | Brasil | 3168903 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1e20fb80-ad6d-3d37-84d7-006f66f4ec31 | -18.61463 | -44.26578 | 2025-07-22 04:04:00 | NOAA-20 | INIMUTABA | MINAS GERAIS | Brasil | 3131109 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 34d6e72f-13ca-374a-b42c-5cc170cd6510 | -18.98839 | -45.78209 | 2025-07-22 04:04:00 | NOAA-20 | TIROS | MINAS GERAIS | Brasil | 3168903 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ba60768a-8fa3-31b0-8714-3f8a5aa87ffb | -16.30357 | -42.98169 | 2025-07-22 04:04:00 | NOAA-20 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6d2d1aa5-d993-3863-bca8-02e1ac6351b5 | -20.31009 | -46.676 | 2025-07-22 04:04:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d631dbfc-2b13-3ff1-8f0a-8a8e8f7f4092 | -22.1177 | -43.15396 | 2025-07-22 04:04:00 | NOAA-20 | TRÊS RIOS | RIO DE JANEIRO | Brasil | 3306008 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 3095467f-4124-36e9-ab38-27ed30421f6a | -20.35226 | -41.48756 | 2025-07-22 04:04:00 | NOAA-20 | IÚNA | ESPÍRITO SANTO | Brasil | 3203007 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| b12e58c5-ad43-3064-a6a0-c7a9dd7eea6f | -21.49358 | -47.2726 | 2025-07-22 04:04:00 | NOAA-20 | TAMBAÚ | SÃO PAULO | Brasil | 3553302 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d9b47957-57ee-3486-bfbe-cd7c6fe98cbe | -17.87052 | -45.54569 | 2025-07-22 04:04:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0d8a2c59-5f24-316f-b810-641461dbf169 | -17.59644 | -50.64698 | 2025-07-22 04:04:00 | NOAA-20 | SANTO ANTÔNIO DA BARRA | GOIÁS | Brasil | 5219712 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d2d0b48f-0ddb-3c00-98c5-224600c0dcaf | -19.83186 | -41.95189 | 2025-07-22 04:04:00 | NOAA-20 | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 01c5a42f-453a-3327-86ab-2d26de051eee | -18.98911 | -45.77789 | 2025-07-22 04:04:00 | NOAA-20 | TIROS | MINAS GERAIS | Brasil | 3168903 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3c2bddc4-3982-3789-b8f9-f10f9ee4e3ab | -17.02535 | -47.20844 | 2025-07-22 04:04:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 18fa7e28-33ef-3f3a-9d6a-0010da875583 | -20.71792 | -47.15083 | 2025-07-22 04:04:00 | NOAA-20 | SÃO TOMÁS DE AQUINO | MINAS GERAIS | Brasil | 3165107 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 75d0f6be-d7b6-371b-b6e5-e131679b17cb | -19.14579 | -45.45722 | 2025-07-22 04:04:00 | NOAA-20 | ABAETÉ | MINAS GERAIS | Brasil | 3100203 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 331ecdff-77ad-3849-bd99-50b175311cb9 | -18.62753 | -40.09185 | 2025-07-22 04:04:00 | NOAA-20 | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| d4590362-c00b-3fe5-bd00-0201538f67a1 | -20.35172 | -41.49129 | 2025-07-22 04:04:00 | NOAA-20 | IÚNA | ESPÍRITO SANTO | Brasil | 3203007 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 5c9691fd-0acd-3090-a68d-689d55234492 | -17.59412 | -43.19897 | 2025-07-22 04:04:00 | NOAA-20 | CARBONITA | MINAS GERAIS | Brasil | 3113503 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 692b4202-2aeb-3a37-b873-52c94926beae | -17.91386 | -47.76501 | 2025-07-22 04:04:00 | NOAA-20 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d0b19728-663b-3f70-9f63-0f650617c40b | -23.02879 | -47.18174 | 2025-07-22 04:04:00 | NOAA-20 | CAMPINAS | SÃO PAULO | Brasil | 3509502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| e841452d-2295-388e-bc28-25d1f6bba4b4 | -17.02148 | -47.20762 | 2025-07-22 04:04:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 130210bc-8843-334e-b1d5-587d3885ae1d | -22.12938 | -42.89839 | 2025-07-22 04:04:00 | NOAA-20 | SÃO JOSÉ DO VALE DO RIO PRETO | RIO DE JANEIRO | Brasil | 3305158 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 89c5ac21-6f52-333e-8d18-c53f57a71ba8 | -20.06385 | -41.40566 | 2025-07-22 04:04:00 | NOAA-20 | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.8 |
| db31d6f9-8d0c-333f-bff7-8833f0fb5acd | -17.91219 | -47.76592 | 2025-07-22 04:04:00 | NOAA-20 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cf032584-fca6-36e2-990d-1fa2bd233dbd | -18.64745 | -47.92609 | 2025-07-22 04:04:00 | NOAA-20 | CASCALHO RICO | MINAS GERAIS | Brasil | 3115003 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4db26c23-b8a0-313d-9c77-16595de59d03 | -17.57811 | -47.49996 | 2025-07-22 04:04:00 | NOAA-20 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4393d56d-69cf-34c8-b4e8-824eb15b3e27 | -16.6941 | -41.01688 | 2025-07-22 04:04:00 | NOAA-20 | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| f86cda36-2893-34da-8a2d-a8ea8db9a644 | -18.46605 | -40.5443 | 2025-07-22 04:04:00 | NOAA-20 | ECOPORANGA | ESPÍRITO SANTO | Brasil | 3202108 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 4b09a2cc-ede4-3d9d-9ff0-4d34624586f1 | -19.74834 | -44.84599 | 2025-07-22 04:04:00 | NOAA-20 | CONCEIÇÃO DO PARÁ | MINAS GERAIS | Brasil | 3117603 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a0455440-70c6-343e-b941-d0feaf07de05 | -21.01618 | -56.00597 | 2025-07-22 04:04:00 | NOAA-20 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c17d2903-527f-3fcb-ac48-3e91b1a2b254 | -18.95968 | -45.73841 | 2025-07-22 04:04:00 | NOAA-20 | TIROS | MINAS GERAIS | Brasil | 3168903 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| f97b973a-eb03-32e7-b7b7-c4aef74d03dc | -21.66264 | -46.93985 | 2025-07-22 04:04:00 | NOAA-20 | SÃO JOSÉ DO RIO PARDO | SÃO PAULO | Brasil | 3549706 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9f262b62-0a7f-31bd-a13c-b1cc74862c14 | -18.48192 | -40.34988 | 2025-07-22 04:04:00 | NOAA-20 | BOA ESPERANÇA | ESPÍRITO SANTO | Brasil | 3201001 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 474645ac-76f3-3b79-8ac6-478cf556d5d1 | -19.762 | -43.6459 | 2025-07-22 04:04:00 | NOAA-20 | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4c1ce9be-26b6-37c8-96d4-bf754c03ab85 | -18.12898 | -44.2766 | 2025-07-22 04:04:00 | NOAA-20 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1bc0e21d-35e9-32af-a29f-798c281ecb8c | -19.41279 | -44.95975 | 2025-07-22 04:04:00 | NOAA-20 | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ef664f90-9400-3d97-8706-7be026ffea15 | -19.50673 | -45.93511 | 2025-07-22 04:04:00 | NOAA-20 | SANTA ROSA DA SERRA | MINAS GERAIS | Brasil | 3159704 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a97dc8c0-17e5-349c-83fe-cf63f3bf1672 | -22.06694 | -47.13955 | 2025-07-22 04:04:00 | NOAA-20 | AGUAÍ | SÃO PAULO | Brasil | 3500303 | 35 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5c929ed3-a0a5-3d71-b1c9-f412e53b1250 | -20.35567 | -41.48808 | 2025-07-22 04:04:00 | NOAA-20 | IÚNA | ESPÍRITO SANTO | Brasil | 3203007 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 3e9c09a7-1666-34c0-a273-5f89c07b558d | -21.11292 | -48.39899 | 2025-07-22 04:04:00 | NOAA-20 | TAIÚVA | SÃO PAULO | Brasil | 3553203 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a0a4cde2-5bb9-3d08-9d64-80ebede7c244 | -19.16366 | -46.56538 | 2025-07-22 04:04:00 | NOAA-20 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d61c5cc5-f68e-3398-8f08-d6ce438762c3 | -21.05543 | -42.9569 | 2025-07-22 04:04:00 | NOAA-20 | UBÁ | MINAS GERAIS | Brasil | 3169901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 91e5f61d-0fe4-396e-adfe-cac0a5835a3c | -22.16033 | -47.37183 | 2025-07-22 04:04:00 | NOAA-20 | LEME | SÃO PAULO | Brasil | 3526704 | 35 | 33 | nan | nan | nan | Mata Atlântica | 14.4 |
| b5276c8b-c80f-3ad1-9fd7-afdd062533f7 | -20.16667 | -41.39469 | 2025-07-22 04:04:00 | NOAA-20 | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 75320645-4049-3019-bde1-228b03e2eb80 | -15.53526 | -47.99071 | 2025-07-22 04:04:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fee602ff-4931-3243-89a3-7f5da9ee3430 | -22.17865 | -42.46766 | 2025-07-22 04:04:00 | NOAA-20 | BOM JARDIM | RIO DE JANEIRO | Brasil | 3300506 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| ffd5e709-0c97-3728-87c1-25263f84ccac | -15.54016 | -47.98751 | 2025-07-22 04:04:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e5a364bc-fcc5-3bb9-9499-300d1ad3c117 | -18.66264 | -55.72152 | 2025-07-22 04:04:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| c4a39797-bcbf-3870-a9d4-c05f5b897b08 | -16.30747 | -42.97865 | 2025-07-22 04:04:00 | NOAA-20 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a407556a-a8af-3d55-b9b8-1f65b3bedd38 | -17.59566 | -50.64898 | 2025-07-22 04:04:00 | NOAA-20 | SANTO ANTÔNIO DA BARRA | GOIÁS | Brasil | 5219712 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2e548847-0972-307b-b88d-2d86f8818447 | -22.69866 | -43.34614 | 2025-07-22 04:04:00 | NOAA-20 | BELFORD ROXO | RIO DE JANEIRO | Brasil | 3300456 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 4657857e-e81a-3b20-ba29-04a456de4461 | -18.99614 | -45.77926 | 2025-07-22 04:04:00 | NOAA-20 | TIROS | MINAS GERAIS | Brasil | 3168903 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f1fb4717-84a2-35d3-834a-b47dce8c9199 | -18.8082 | -44.41231 | 2025-07-22 04:04:00 | NOAA-20 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b5a138cc-f753-37bf-bede-c951e33a76ef | -19.86407 | -48.96772 | 2025-07-22 04:04:00 | NOAA-20 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c66e60ba-145d-3099-afa4-1248b0943cab | -19.57992 | -40.54817 | 2025-07-22 04:04:00 | NOAA-20 | COLATINA | ESPÍRITO SANTO | Brasil | 3201506 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 5362e8e4-2c8f-3bfe-929d-5d1783a9c254 | -22.8242 | -46.14626 | 2025-07-22 04:04:00 | NOAA-20 | CAMANDUCAIA | MINAS GERAIS | Brasil | 3110509 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.4 |
| 42edd937-ad9e-3a9b-8b44-de63f54536df | -21.28492 | -56.20729 | 2025-07-22 04:04:00 | NOAA-20 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5d4a0207-bb24-3893-bb81-d050ded15f34 | -20.06503 | -41.39749 | 2025-07-22 04:04:00 | NOAA-20 | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| cf13c729-7041-32b8-be88-7aed46175941 | -16.46959 | -46.15424 | 2025-07-22 04:04:00 | NOAA-20 | BONFINÓPOLIS DE MINAS | MINAS GERAIS | Brasil | 3108206 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6232a90a-1925-3251-a077-74c822f402d4 | -18.05551 | -44.84216 | 2025-07-22 04:04:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3f051e5c-94b9-3bb7-854a-bdbb41727871 | -15.53948 | -47.99123 | 2025-07-22 04:04:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b99cc469-b1ce-3a96-8e0a-28e7d21dc9de | -19.16003 | -46.56465 | 2025-07-22 04:04:00 | NOAA-20 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c892cc46-b2b4-3ff7-b131-fd04211943f1 | -21.99089 | -41.46704 | 2025-07-22 04:04:00 | NOAA-20 | QUISSAMÃ | RIO DE JANEIRO | Brasil | 3304151 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 1e40f312-51ce-398f-b75b-76f371910ca8 | -23.17906 | -46.82187 | 2025-07-22 04:04:00 | NOAA-20 | JUNDIAÍ | SÃO PAULO | Brasil | 3525904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 855965bf-ae3f-3d3f-9214-d1615b1532ee | -21.66174 | -46.93708 | 2025-07-22 04:04:00 | NOAA-20 | SÃO JOSÉ DO RIO PARDO | SÃO PAULO | Brasil | 3549706 | 35 | 33 | nan | nan | nan | Cerrado | 3.8 |
| cf32c409-0d1b-32dd-bb63-1388e2cf9598 | -19.45579 | -45.30657 | 2025-07-22 04:04:00 | NOAA-20 | MARTINHO CAMPOS | MINAS GERAIS | Brasil | 3140506 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e1e34c3b-4582-3654-956d-c4c33bc549c0 | -21.21579 | -45.84596 | 2025-07-22 04:04:00 | NOAA-20 | CAMPOS GERAIS | MINAS GERAIS | Brasil | 3111606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| e534dd36-6ff4-33fb-b274-ef7449c0af18 | -22.32336 | -41.79759 | 2025-07-22 04:04:00 | NOAA-20 | MACAÉ | RIO DE JANEIRO | Brasil | 3302403 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 8fbb3c2e-2f99-371f-9568-bcd31a886a57 | -18.4797 | -40.34869 | 2025-07-22 04:04:00 | NOAA-20 | BOA ESPERANÇA | ESPÍRITO SANTO | Brasil | 3201001 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| eff6fd65-2a31-398e-a903-e51a41e8b5be | -15.53595 | -47.98697 | 2025-07-22 04:04:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 28c7393e-0022-3864-b829-57e44961ef1a | -18.61798 | -44.26638 | 2025-07-22 04:04:00 | NOAA-20 | INIMUTABA | MINAS GERAIS | Brasil | 3131109 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0825ae5a-2ff5-3ad5-9289-39e27898025a | -21.66343 | -46.93549 | 2025-07-22 04:04:00 | NOAA-20 | SÃO JOSÉ DO RIO PARDO | SÃO PAULO | Brasil | 3549706 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 111fb207-40aa-3e63-9267-cdfee3f3eb72 | -22.42844 | -48.56434 | 2025-07-22 04:04:00 | NOAA-20 | BARRA BONITA | SÃO PAULO | Brasil | 3505302 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| d8d296f7-475a-33c6-957c-1c3d8eb56ce9 | -21.65844 | -41.32452 | 2025-07-22 04:04:00 | NOAA-20 | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 54a436b3-6ba2-3adc-ad97-0cccfe9deaf8 | -20.06065 | -41.40154 | 2025-07-22 04:04:00 | NOAA-20 | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 3ed4f589-de84-3a32-b0e7-b0808676179f | -17.02237 | -47.20264 | 2025-07-22 04:04:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 442775c0-fe47-37c7-8191-f66bc52a68d4 | -18.62756 | -40.09406 | 2025-07-22 04:04:00 | NOAA-20 | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |


[Clique aqui para ver as próximas entradas](README12.md)
