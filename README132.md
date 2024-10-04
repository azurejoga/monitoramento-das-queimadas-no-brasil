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

## Dados Diários - Página 132

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d9b7ef7d-d57d-33ad-98c8-87bc99345b21 | -19.85457 | -42.3693 | 2024-10-04 04:36:00 | NPP-375D | BOM JESUS DO GALHO | MINAS GERAIS | Brasil | 3107802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.9 |
| 0d33b945-4548-33ee-99a1-dfef1ea7d4da | -19.85398 | -42.3747 | 2024-10-04 04:36:00 | NPP-375D | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.7 |
| fa4fbf0f-ccd5-3d6f-b097-945c4eb8f43b | -19.85342 | -42.37968 | 2024-10-04 04:36:00 | NPP-375D | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.7 |
| c44c6fb0-e400-3a75-ba25-25a06733ff05 | -19.85027 | -42.36221 | 2024-10-04 04:36:00 | NPP-375D | BOM JESUS DO GALHO | MINAS GERAIS | Brasil | 3107802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.9 |
| 3f8d3bfd-4576-3d62-8b41-49e36ea0bb64 | -19.84956 | -42.36863 | 2024-10-04 04:36:00 | NPP-375D | BOM JESUS DO GALHO | MINAS GERAIS | Brasil | 3107802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.9 |
| 7cefbd93-4a6e-3989-a010-c578c3a84c43 | -19.84894 | -42.37425 | 2024-10-04 04:36:00 | NPP-375D | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.7 |
| 9ed52b64-5df2-30f4-a2ba-94c120a73f99 | -19.84837 | -42.37943 | 2024-10-04 04:36:00 | NPP-375D | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.7 |
| 03fa241a-823b-3049-9263-4eb64f7050c5 | -19.84592 | -42.35553 | 2024-10-04 04:36:00 | NPP-375D | BOM JESUS DO GALHO | MINAS GERAIS | Brasil | 3107802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 58e67062-b54b-341c-a601-4beff2517768 | -19.84523 | -42.36178 | 2024-10-04 04:36:00 | NPP-375D | BOM JESUS DO GALHO | MINAS GERAIS | Brasil | 3107802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 68.6 |
| 162f8a6d-97a1-34db-bb62-c15641e11532 | -19.84454 | -42.36805 | 2024-10-04 04:36:00 | NPP-375D | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 68.6 |
| a02ea4f2-8786-31b6-adff-47f9e21f96b7 | -19.84391 | -42.37373 | 2024-10-04 04:36:00 | NPP-375D | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 29.6 |
| bfc6e7f9-6f75-3667-9205-b8cfb9a9a56f | -19.84335 | -42.37884 | 2024-10-04 04:36:00 | NPP-375D | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 29.6 |
| 496cff1e-d19a-3e9b-9a48-5363012d7c56 | -19.84016 | -42.36164 | 2024-10-04 04:36:00 | NPP-375D | BOM JESUS DO GALHO | MINAS GERAIS | Brasil | 3107802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 68.6 |
| 8721169b-0078-3d7a-a8d7-51f6323b5e31 | -19.83947 | -42.36784 | 2024-10-04 04:36:00 | NPP-375D | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 68.6 |
| 94c6a6ac-710a-3de3-a4e1-c59d21710b8d | -19.83888 | -42.37328 | 2024-10-04 04:36:00 | NPP-375D | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 29.6 |
| 4dae47c8-d9f5-340c-862d-bd2420cbc34a | -20.10318 | -43.42427 | 2024-10-04 04:36:00 | NPP-375D | CATAS ALTAS | MINAS GERAIS | Brasil | 3115359 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 024121c5-43e0-3a8f-a079-d6954685ece2 | -20.28765 | -43.50677 | 2024-10-04 04:36:00 | NPP-375D | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| b2f137fd-9334-3ece-829c-1fd9c2a0574f | -20.28684 | -43.51416 | 2024-10-04 04:36:00 | NPP-375D | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 3b484009-c9c3-3352-a1b3-9141d89ff5bf | -20.28481 | -43.51172 | 2024-10-04 04:36:00 | NPP-375D | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| fe35a083-f1fc-31c6-ae34-cc58f8b2f043 | -20.28223 | -43.51297 | 2024-10-04 04:36:00 | NPP-375D | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| b6903d7f-cac8-37ca-847a-72a9372bc147 | -20.28023 | -43.5103 | 2024-10-04 04:36:00 | NPP-375D | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| f2d59603-96dd-3c0e-a99b-c06553286636 | -20.27765 | -43.51146 | 2024-10-04 04:36:00 | NPP-375D | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 0ca51767-c000-3a16-b620-6cd9de9d61ce | -20.27565 | -43.50883 | 2024-10-04 04:36:00 | NPP-375D | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| d530f4bc-638b-3937-aa5f-6a427d8d2274 | -20.27307 | -43.50989 | 2024-10-04 04:36:00 | NPP-375D | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 61790e1f-68a0-3f15-9464-30254d556cf3 | -20.27093 | -43.52962 | 2024-10-04 04:36:00 | NPP-375D | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| c0709e98-48bd-3b65-b99b-54e9d5673df7 | -20.27026 | -43.51437 | 2024-10-04 04:36:00 | NPP-375D | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 5ea6efb4-3b41-3f66-8629-b02563e1fe7c | -20.26869 | -43.52772 | 2024-10-04 04:36:00 | NPP-375D | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 2bf4f8e0-0bba-3dce-bc1c-1bebee6f5c11 | -20.26812 | -43.53263 | 2024-10-04 04:36:00 | NPP-375D | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| d588c3f2-015e-32e6-b7db-6823e860c9cd | -20.26491 | -43.51954 | 2024-10-04 04:36:00 | NPP-375D | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 08c3f3f2-144f-3c8d-9a40-b81d4a098ee7 | -20.26414 | -43.52613 | 2024-10-04 04:36:00 | NPP-375D | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| c2713f37-e403-3aa1-8ace-e0422b8237c3 | -20.08598 | -43.43204 | 2024-10-04 04:36:00 | NPP-375D | CATAS ALTAS | MINAS GERAIS | Brasil | 3115359 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| a0ab4054-449c-3cc0-84ba-414e5deefa56 | -20.08245 | -43.43956 | 2024-10-04 04:36:00 | NPP-375D | CATAS ALTAS | MINAS GERAIS | Brasil | 3115359 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 6207a67f-ec24-3f40-978e-db0891495212 | -20.08064 | -43.4369 | 2024-10-04 04:36:00 | NPP-375D | CATAS ALTAS | MINAS GERAIS | Brasil | 3115359 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| e2fee7fe-6c6c-3fb9-b512-4adaad36fc3b | -20.07991 | -43.44305 | 2024-10-04 04:36:00 | NPP-375D | CATAS ALTAS | MINAS GERAIS | Brasil | 3115359 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 6b4e0156-678a-3724-b52c-f13708d56e27 | -20.52098 | -42.87967 | 2024-10-04 04:36:00 | NPP-375D | PONTE NOVA | MINAS GERAIS | Brasil | 3152105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| e2624b94-2263-3748-af89-78e01d4445c2 | -20.46347 | -43.17868 | 2024-10-04 04:36:00 | NPP-375D | DIOGO DE VASCONCELOS | MINAS GERAIS | Brasil | 3121704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| c95996c3-539e-3583-88cd-11d2c3479475 | -20.46285 | -43.18427 | 2024-10-04 04:36:00 | NPP-375D | DIOGO DE VASCONCELOS | MINAS GERAIS | Brasil | 3121704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| e96d7a47-cce1-3997-8162-caf279c947d1 | -20.26505 | -43.18238 | 2024-10-04 04:36:00 | NPP-375D | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 474dc2fb-6768-3874-a881-52836a5a0a93 | -20.26442 | -43.18806 | 2024-10-04 04:36:00 | NPP-375D | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 4adc7672-c657-3e34-af95-74482339d574 | -20.25066 | -43.18103 | 2024-10-04 04:36:00 | NPP-375D | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| be8b4d1a-228c-3c57-9de1-4b9a68041804 | -20.24528 | -43.18583 | 2024-10-04 04:36:00 | NPP-375D | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 8ca91a56-248d-3738-9f2c-2948060cb401 | -20.2447 | -43.19103 | 2024-10-04 04:36:00 | NPP-375D | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| a9ad0bfe-773a-3f0a-aee0-4a5b9263e007 | -20.2405 | -43.18517 | 2024-10-04 04:36:00 | NPP-375D | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 436095d5-be1f-3ef7-9f52-7383431f5c16 | -20.0985 | -43.42352 | 2024-10-04 04:36:00 | NPP-375D | CATAS ALTAS | MINAS GERAIS | Brasil | 3115359 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| d06846a0-660c-3d31-9746-ed1fad2b2eeb | -20.08323 | -43.43242 | 2024-10-04 04:36:00 | NPP-375D | CATAS ALTAS | MINAS GERAIS | Brasil | 3115359 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 7ccb3291-7568-3acd-b6f1-4dedb432986d | -19.88144 | -43.11274 | 2024-10-04 04:36:00 | NPP-375D | RIO PIRACICABA | MINAS GERAIS | Brasil | 3155702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 1b852df3-9270-3bfe-9a41-a67ddd1ba04e | -19.8763 | -43.15732 | 2024-10-04 04:36:00 | NPP-375D | JOÃO MONLEVADE | MINAS GERAIS | Brasil | 3136207 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 87b01eca-c061-32b7-b67f-e213032f50b7 | -19.70327 | -42.93959 | 2024-10-04 04:36:00 | NPP-375D | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| cc17f8cf-ec85-3328-8edd-ec6ab0243d5b | -19.70222 | -42.94861 | 2024-10-04 04:36:00 | NPP-375D | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 2e291213-3e1b-3877-9f96-f829ea07a5b2 | -19.70221 | -42.94014 | 2024-10-04 04:36:00 | NPP-375D | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| a6835546-8050-34b7-abb8-ecff4fc54ffe | -19.70173 | -42.94451 | 2024-10-04 04:36:00 | NPP-375D | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 8784356b-c3a6-3c79-a204-d95196f8bfb8 | -19.70121 | -42.9493 | 2024-10-04 04:36:00 | NPP-375D | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| c9f846b3-7d97-3025-8d38-301396ee2cf8 | -19.69846 | -42.93881 | 2024-10-04 04:36:00 | NPP-375D | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 1388cf75-266e-3abb-b055-c482d18c29b6 | -19.69794 | -42.94332 | 2024-10-04 04:36:00 | NPP-375D | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| bf7fca3b-b2cc-3e0e-811d-fdad3d660c3a | -19.6974 | -42.94799 | 2024-10-04 04:36:00 | NPP-375D | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 78388d80-887e-3e56-a0f0-8aec00bab2cf | -19.6974 | -42.93937 | 2024-10-04 04:36:00 | NPP-375D | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| abbecb2c-d6c6-3bd9-ba90-6a7cf0cfb0d8 | -19.69691 | -42.9439 | 2024-10-04 04:36:00 | NPP-375D | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 1cca984b-aff2-30ac-8248-8e3d3913c2d3 | -19.69425 | -42.93293 | 2024-10-04 04:36:00 | NPP-375D | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| d4ed0ba7-778d-381a-a3cb-a3454dfb5ee0 | -19.69368 | -42.93784 | 2024-10-04 04:36:00 | NPP-375D | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 20ab0b4c-71ad-35c6-873a-2f5ccbf36f5c | -19.68953 | -42.93142 | 2024-10-04 04:36:00 | NPP-375D | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| edcb9ef5-ecc4-3c7b-aba5-c2df2acba3dc | -19.68478 | -42.93018 | 2024-10-04 04:36:00 | NPP-375D | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| ff4a6fab-aaf0-328e-aa28-41d77ab2a619 | -20.2114 | -44.74783 | 2024-10-04 04:36:00 | NPP-375D | CARMO DO CAJURU | MINAS GERAIS | Brasil | 3114204 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a39c4bbe-ef86-3cc9-84ad-c00fe6ee2806 | -19.87483 | -44.40259 | 2024-10-04 04:36:00 | NPP-375D | FLORESTAL | MINAS GERAIS | Brasil | 3126000 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8d322fb0-505d-3890-ae68-8e660e294c31 | -19.80547 | -43.64326 | 2024-10-04 04:36:00 | NPP-375D | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| cc29ff45-13ba-35fd-a469-c7e1287243cf | -19.80086 | -43.64273 | 2024-10-04 04:36:00 | NPP-375D | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| de0de7d8-ef14-3ea4-9662-4a5d43683132 | -19.77893 | -43.90701 | 2024-10-04 04:36:00 | NPP-375D | SANTA LUZIA | MINAS GERAIS | Brasil | 3157807 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3ecc7a81-caff-39be-95ff-a8caff13a652 | -20.62649 | -45.16238 | 2024-10-04 04:36:00 | NPP-375D | CAMACHO | MINAS GERAIS | Brasil | 3110400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 906e4712-a8fd-3567-9845-41b756015d46 | -20.62596 | -45.16163 | 2024-10-04 04:36:00 | NPP-375D | CAMACHO | MINAS GERAIS | Brasil | 3110400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 365beefb-b10a-3e53-9d65-a845f89cb6e7 | -20.57917 | -44.57517 | 2024-10-04 04:36:00 | NPP-375D | PASSA TEMPO | MINAS GERAIS | Brasil | 3147709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| d4b84e20-4439-3f34-834e-e44f2228ca20 | -20.52245 | -44.89394 | 2024-10-04 04:36:00 | NPP-375D | CARMO DA MATA | MINAS GERAIS | Brasil | 3114006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 762d4923-effd-3750-9839-d72f9da10b85 | -20.52191 | -44.8983 | 2024-10-04 04:36:00 | NPP-375D | CARMO DA MATA | MINAS GERAIS | Brasil | 3114006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 74d407b0-a5a3-3bc3-a858-6a81aec81757 | -20.52137 | -44.90271 | 2024-10-04 04:36:00 | NPP-375D | CARMO DA MATA | MINAS GERAIS | Brasil | 3114006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| a29c8f0a-7957-3b77-898c-201fd8919a27 | -20.51763 | -44.89768 | 2024-10-04 04:36:00 | NPP-375D | CARMO DA MATA | MINAS GERAIS | Brasil | 3114006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| d67caa39-d920-3c49-9d38-093669676f33 | -20.51709 | -44.90213 | 2024-10-04 04:36:00 | NPP-375D | CARMO DA MATA | MINAS GERAIS | Brasil | 3114006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| d9bbb8ba-e206-38da-9210-50b8a8fc0c5e | -20.51655 | -44.90652 | 2024-10-04 04:36:00 | NPP-375D | CARMO DA MATA | MINAS GERAIS | Brasil | 3114006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 92ddf0f8-a2db-34e1-9fda-4eeb465481d1 | -20.42623 | -43.76144 | 2024-10-04 04:36:00 | NPP-375D | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 7221ded8-c048-3d45-93ca-715687b36384 | -20.42458 | -43.77569 | 2024-10-04 04:36:00 | NPP-375D | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 17415418-7389-3dcd-9d2d-93ca8c367d16 | -20.42161 | -43.76094 | 2024-10-04 04:36:00 | NPP-375D | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| ba6c6915-9b23-3245-9fd7-2dc510fadb58 | -20.42 | -43.77485 | 2024-10-04 04:36:00 | NPP-375D | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 750dcefe-083d-317e-b2f0-49552d7655d5 | -20.41541 | -43.77414 | 2024-10-04 04:36:00 | NPP-375D | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 96c37ce6-a46e-3996-8468-1812cb98e69f | -20.33994 | -43.86457 | 2024-10-04 04:36:00 | NPP-375D | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 8797f588-4f54-3c6c-9245-eed4efedcd3c | -20.27481 | -44.10865 | 2024-10-04 04:36:00 | NPP-375D | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 1aea2e1a-bb5d-3ff6-aea9-ba78381b408a | -20.15521 | -43.55004 | 2024-10-04 04:36:00 | NPP-375D | SANTA BÁRBARA | MINAS GERAIS | Brasil | 3157203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| ef2ad29d-c2f6-3d0e-b402-38d382d6137a | -20.1417 | -43.861 | 2024-10-04 04:36:00 | NPP-375D | NOVA LIMA | MINAS GERAIS | Brasil | 3144805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 3f418c3c-1185-366a-a55c-03cb98db51b9 | -20.14119 | -43.86239 | 2024-10-04 04:36:00 | NPP-375D | NOVA LIMA | MINAS GERAIS | Brasil | 3144805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| b13ec55c-b1e4-3fa6-97a3-84c2857abe5f | -20.14112 | -43.86584 | 2024-10-04 04:36:00 | NPP-375D | NOVA LIMA | MINAS GERAIS | Brasil | 3144805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| a6f86f12-ea51-39a1-9628-2e18ac1c83e2 | -20.13718 | -43.86012 | 2024-10-04 04:36:00 | NPP-375D | NOVA LIMA | MINAS GERAIS | Brasil | 3144805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 79d9dc8a-91b9-3288-902c-3858a04b254b | -20.13717 | -43.85693 | 2024-10-04 04:36:00 | NPP-375D | NOVA LIMA | MINAS GERAIS | Brasil | 3144805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| f8946218-6525-3e5f-94c2-c92a954912f6 | -20.13667 | -43.86143 | 2024-10-04 04:36:00 | NPP-375D | NOVA LIMA | MINAS GERAIS | Brasil | 3144805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| cfb6d695-0af0-3cd2-8233-3ea24d93f0aa | -20.1332 | -43.85469 | 2024-10-04 04:36:00 | NPP-375D | NOVA LIMA | MINAS GERAIS | Brasil | 3144805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 54a9b66c-face-3431-afb7-f9cae93e1020 | -20.13317 | -43.85128 | 2024-10-04 04:36:00 | NPP-375D | RIO ACIMA | MINAS GERAIS | Brasil | 3154804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| cf322c35-8d7b-31b1-aac8-8dc2cb1132f5 | -20.13264 | -43.85601 | 2024-10-04 04:36:00 | NPP-375D | NOVA LIMA | MINAS GERAIS | Brasil | 3144805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 03a8f8f5-6088-3469-9f88-b4c96feb2c45 | -20.1307 | -43.51663 | 2024-10-04 04:36:00 | NPP-375D | SANTA BÁRBARA | MINAS GERAIS | Brasil | 3157203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 0429065d-5f77-3d51-9c6c-39ae1fd66465 | -20.1302 | -43.52099 | 2024-10-04 04:36:00 | NPP-375D | SANTA BÁRBARA | MINAS GERAIS | Brasil | 3157203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 395d6a8c-1a6f-3784-8670-91e184e85530 | -20.12968 | -43.52547 | 2024-10-04 04:36:00 | NPP-375D | SANTA BÁRBARA | MINAS GERAIS | Brasil | 3157203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| caa868e0-d01c-35b6-8402-30f1d0f1e1c0 | -20.12915 | -43.5301 | 2024-10-04 04:36:00 | NPP-375D | SANTA BÁRBARA | MINAS GERAIS | Brasil | 3157203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| a48bd7c8-06fd-3d7b-8cfd-896d423ff0cf | -20.12608 | -43.51565 | 2024-10-04 04:36:00 | NPP-375D | SANTA BÁRBARA | MINAS GERAIS | Brasil | 3157203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 32f1fa38-aa2f-3483-8b66-420a35a51d65 | -20.12556 | -43.52011 | 2024-10-04 04:36:00 | NPP-375D | SANTA BÁRBARA | MINAS GERAIS | Brasil | 3157203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| fbe67a2b-e0e3-3e29-a0de-dc72685d9dd5 | -20.12503 | -43.52475 | 2024-10-04 04:36:00 | NPP-375D | SANTA BÁRBARA | MINAS GERAIS | Brasil | 3157203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| b5b76ed6-434e-3334-80f3-29fdd8506f65 | -20.11628 | -43.51852 | 2024-10-04 04:36:00 | NPP-375D | SANTA BÁRBARA | MINAS GERAIS | Brasil | 3157203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |


[Clique aqui para ver as próximas entradas](README133.md)
