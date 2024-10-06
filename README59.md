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

## Dados Diários - Página 59

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f62bbace-8234-3ee6-a873-f2a271fae79a | -20.4407 | -49.94316 | 2024-10-06 03:57:00 | NPP-375D | VOTUPORANGA | SÃO PAULO | Brasil | 3557105 | 35 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 5eff30f2-d955-3290-a091-a43cfc609168 | -20.44043 | -49.94986 | 2024-10-06 03:57:00 | NPP-375D | VOTUPORANGA | SÃO PAULO | Brasil | 3557105 | 35 | 33 | nan | nan | nan | Cerrado | 7.0 |
| e507b261-c624-3c57-89bd-1f277833c0ae | -19.38472 | -44.32281 | 2024-10-06 03:57:00 | NPP-375D | CAETANÓPOLIS | MINAS GERAIS | Brasil | 3109907 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0724968a-2801-36ef-93ba-7414ed3d664e | -19.29389 | -43.78038 | 2024-10-06 03:57:00 | NPP-375D | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8391aaac-3247-346c-b1a7-558bdaf0eea8 | -19.29038 | -43.77976 | 2024-10-06 03:57:00 | NPP-375D | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e9497f50-3375-3757-a5f2-9286118af9ed | -19.63017 | -44.1176 | 2024-10-06 03:57:00 | NPP-375D | PEDRO LEOPOLDO | MINAS GERAIS | Brasil | 3149309 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1fe501f5-8bc2-30a2-bbcd-d9276653b596 | -19.62736 | -44.11275 | 2024-10-06 03:57:00 | NPP-375D | PEDRO LEOPOLDO | MINAS GERAIS | Brasil | 3149309 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f016f64b-0615-3783-9328-92a3bfbc5db1 | -17.00017 | -55.08625 | 2024-10-06 03:57:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 16.6 |
| 0bdd0b5e-b8fe-33d5-b316-31f0d1b3b2c2 | -20.43953 | -49.94891 | 2024-10-06 03:57:00 | NPP-375D | VOTUPORANGA | SÃO PAULO | Brasil | 3557105 | 35 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 66c8998d-8714-3e4a-9740-ad541c85f0a8 | -20.43675 | -49.94308 | 2024-10-06 03:57:00 | NPP-375D | VOTUPORANGA | SÃO PAULO | Brasil | 3557105 | 35 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 73a0a59f-08ba-3e30-a9c9-35a5075e3552 | -20.43554 | -49.9488 | 2024-10-06 03:57:00 | NPP-375D | VOTUPORANGA | SÃO PAULO | Brasil | 3557105 | 35 | 33 | nan | nan | nan | Cerrado | 7.0 |
| d03d43e6-3bd9-3ae7-8406-192e09461c0b | -19.29782 | -46.22176 | 2024-10-06 03:57:00 | NPP-375D | RIO PARANAÍBA | MINAS GERAIS | Brasil | 3155504 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 499e2566-decb-3ad5-8aef-1b0b3806240e | -19.61291 | -46.25912 | 2024-10-06 03:57:00 | NPP-375D | CAMPOS ALTOS | MINAS GERAIS | Brasil | 3111507 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 513bc232-8f51-3a24-bd06-08c8733e1f47 | -23.08291 | -48.43373 | 2024-10-06 03:57:00 | NPP-375D | PARDINHO | SÃO PAULO | Brasil | 3536109 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 97296947-fe40-3dea-95cf-5a2e331a227d | -22.84536 | -47.37339 | 2024-10-06 03:57:00 | NPP-375D | SANTA BÁRBARA D'OESTE | SÃO PAULO | Brasil | 3545803 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| c4ccb687-0461-35ce-b5e1-a1071506e3cc | -22.8414 | -47.37241 | 2024-10-06 03:57:00 | NPP-375D | SANTA BÁRBARA D'OESTE | SÃO PAULO | Brasil | 3545803 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| d095690e-04cd-3da0-beb3-02ac171b7c2a | -20.34758 | -40.36213 | 2024-10-06 03:57:00 | NPP-375D | CARIACICA | ESPÍRITO SANTO | Brasil | 3201308 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 94ccf491-2bed-379f-a540-b2de9696403a | -20.266 | -40.391 | 2024-10-06 03:57:00 | NPP-375D | CARIACICA | ESPÍRITO SANTO | Brasil | 3201308 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 1490505c-139f-3d4f-808a-f757152eb285 | -19.56404 | -40.49392 | 2024-10-06 03:57:00 | NPP-375D | COLATINA | ESPÍRITO SANTO | Brasil | 3201506 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 3e6c7a6b-e484-3d06-8241-c893a3c63e0e | -19.56348 | -40.49763 | 2024-10-06 03:57:00 | NPP-375D | COLATINA | ESPÍRITO SANTO | Brasil | 3201506 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| f585adc9-22cc-3d67-bcc7-69b5e9badae7 | -19.5607 | -40.49335 | 2024-10-06 03:57:00 | NPP-375D | COLATINA | ESPÍRITO SANTO | Brasil | 3201506 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| d14ceb64-af1e-3d9f-b3e9-43cb6f8f5ae8 | -19.33454 | -40.8688 | 2024-10-06 03:57:00 | NPP-375D | BAIXO GUANDU | ESPÍRITO SANTO | Brasil | 3200805 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 8fd82fc4-643d-3059-a68f-8957d019b083 | -22.30385 | -41.8804 | 2024-10-06 03:57:00 | NPP-375D | MACAÉ | RIO DE JANEIRO | Brasil | 3302403 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| aa82c591-e197-31b4-aa0f-201984b264cd | -21.96365 | -41.51725 | 2024-10-06 03:57:00 | NPP-375D | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 5cfcdd91-8074-3ef0-8359-f25c3d7b6e97 | -21.96032 | -41.51666 | 2024-10-06 03:57:00 | NPP-375D | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| c5dddb76-2262-362a-aec0-f297fcc65dfe | -21.95974 | -41.5204 | 2024-10-06 03:57:00 | NPP-375D | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 6546ea67-1568-3073-a9c6-becc9c35fabf | -21.95854 | -41.51704 | 2024-10-06 03:57:00 | NPP-375D | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| a0b9707f-ae64-3edb-9d8a-7a26f39f2374 | -21.93215 | -41.55458 | 2024-10-06 03:57:00 | NPP-375D | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| d6672750-aa05-37da-810f-9081fe54e43b | -21.90017 | -42.16154 | 2024-10-06 03:57:00 | NPP-375D | SÃO SEBASTIÃO DO ALTO | RIO DE JANEIRO | Brasil | 3305307 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 948cdc6e-d0c7-38a2-866d-13c9bd7d6b81 | -21.89684 | -42.16095 | 2024-10-06 03:57:00 | NPP-375D | SÃO SEBASTIÃO DO ALTO | RIO DE JANEIRO | Brasil | 3305307 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| e416a891-4312-30cd-9923-d341d7cd12fc | -19.03291 | -44.51561 | 2024-10-06 03:57:00 | NPP-375D | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 543c59d2-d832-38e9-b634-1d890a02ff4e | -18.7539 | -44.18521 | 2024-10-06 03:57:00 | NPP-375D | INIMUTABA | MINAS GERAIS | Brasil | 3131109 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 19d38786-0372-3378-816d-c839a0414945 | -18.56453 | -43.83608 | 2024-10-06 03:57:00 | NPP-375D | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c3129b32-c3a6-36ea-8e6b-10b26c29466e | -19.87994 | -44.40694 | 2024-10-06 03:57:00 | NPP-375D | FLORESTAL | MINAS GERAIS | Brasil | 3126000 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 218e27fb-cd75-3932-b516-d7564b477faf | -19.87636 | -44.40628 | 2024-10-06 03:57:00 | NPP-375D | FLORESTAL | MINAS GERAIS | Brasil | 3126000 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f6cf7c81-1092-356f-b9be-3ed9e09072e1 | -19.85659 | -44.06392 | 2024-10-06 03:57:00 | NPP-375D | CONTAGEM | MINAS GERAIS | Brasil | 3118601 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 54182391-1573-3033-afc8-1c25f7ec4380 | -19.85307 | -44.06322 | 2024-10-06 03:57:00 | NPP-375D | CONTAGEM | MINAS GERAIS | Brasil | 3118601 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 86553abe-16c5-3373-a90c-40d472b3f623 | -19.8147 | -43.84536 | 2024-10-06 03:57:00 | NPP-375D | SANTA LUZIA | MINAS GERAIS | Brasil | 3157807 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1fc3a8b2-f92a-3aac-9156-7c5d43503f11 | -19.81121 | -43.84476 | 2024-10-06 03:57:00 | NPP-375D | SANTA LUZIA | MINAS GERAIS | Brasil | 3157807 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cf54354f-39a9-3866-b1bd-a62b5b976490 | -19.81051 | -43.84885 | 2024-10-06 03:57:00 | NPP-375D | SANTA LUZIA | MINAS GERAIS | Brasil | 3157807 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d6d3a56c-3f31-3736-a0fa-8249df467ea8 | -19.77127 | -44.2598 | 2024-10-06 03:57:00 | NPP-375D | ESMERALDAS | MINAS GERAIS | Brasil | 3124104 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 74871487-c70b-35df-b54d-c8ae35836021 | -19.63088 | -44.11348 | 2024-10-06 03:57:00 | NPP-375D | PEDRO LEOPOLDO | MINAS GERAIS | Brasil | 3149309 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6e5a4aa3-aa69-37d8-8335-830360cfc0a8 | -20.05186 | -44.06407 | 2024-10-06 03:57:00 | NPP-375D | IBIRITÉ | MINAS GERAIS | Brasil | 3129806 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| a1f2039c-ca79-30d6-9b86-a4e46e9027f6 | -20.05113 | -44.06826 | 2024-10-06 03:57:00 | NPP-375D | IBIRITÉ | MINAS GERAIS | Brasil | 3129806 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 97b45962-4b8a-3415-b705-2d586b532c6b | -20.04761 | -44.06762 | 2024-10-06 03:57:00 | NPP-375D | IBIRITÉ | MINAS GERAIS | Brasil | 3129806 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| c9ea3be7-8c39-3618-b69b-ebc47f862592 | -20.00812 | -44.48313 | 2024-10-06 03:57:00 | NPP-375D | MATEUS LEME | MINAS GERAIS | Brasil | 3140704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| a2e0fc30-1dd5-3ed9-8487-8322959fbfd3 | -19.91917 | -44.52078 | 2024-10-06 03:57:00 | NPP-375D | FLORESTAL | MINAS GERAIS | Brasil | 3126000 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| 7540847c-bd9e-38c3-beef-998160587140 | -19.9184 | -44.52519 | 2024-10-06 03:57:00 | NPP-375D | PARÁ DE MINAS | MINAS GERAIS | Brasil | 3147105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| 3692e7b4-f81d-3b78-a760-09d1626d33ed | -19.91558 | -44.52009 | 2024-10-06 03:57:00 | NPP-375D | FLORESTAL | MINAS GERAIS | Brasil | 3126000 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| 83f78882-a79e-31f6-ab29-2a24e950ede3 | -19.91274 | -44.51512 | 2024-10-06 03:57:00 | NPP-375D | FLORESTAL | MINAS GERAIS | Brasil | 3126000 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 0889e4a6-a818-306f-951a-ce9cd104bc51 | -19.91199 | -44.51942 | 2024-10-06 03:57:00 | NPP-375D | FLORESTAL | MINAS GERAIS | Brasil | 3126000 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| e95e32fa-81c6-3865-811d-713931353123 | -19.91123 | -44.52383 | 2024-10-06 03:57:00 | NPP-375D | FLORESTAL | MINAS GERAIS | Brasil | 3126000 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 023aacac-3ccd-3c17-b7aa-c5dc67c8d7a6 | -21.67122 | -43.99082 | 2024-10-06 03:57:00 | NPP-375D | LIMA DUARTE | MINAS GERAIS | Brasil | 3138609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 9453e8ef-0714-3fba-958c-a49877d3ffd5 | -21.67053 | -43.99485 | 2024-10-06 03:57:00 | NPP-375D | LIMA DUARTE | MINAS GERAIS | Brasil | 3138609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 78269170-d861-30a6-9448-05b0f50bd0b3 | -21.66709 | -43.99415 | 2024-10-06 03:57:00 | NPP-375D | LIMA DUARTE | MINAS GERAIS | Brasil | 3138609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 9b48f6fc-4a37-318c-9eb8-927830e59934 | -18.08554 | -45.61374 | 2024-10-06 03:57:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 41f5a46a-d922-3db8-8c5d-b2e74f9be2d2 | -20.76522 | -46.28905 | 2024-10-06 03:57:00 | NPP-375D | SÃO JOSÉ DA BARRA | MINAS GERAIS | Brasil | 3162948 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7a18b1ae-df9f-37ac-96b7-5d999135de0f | -20.74829 | -45.5992 | 2024-10-06 03:57:00 | NPP-375D | CRISTAIS | MINAS GERAIS | Brasil | 3120201 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5d125090-4cf1-37f7-84cc-8ab3502c5d37 | -20.62137 | -45.82603 | 2024-10-06 03:57:00 | NPP-375D | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 5c89e1ff-fc7e-3af1-92a4-7c268c977ffb | -20.577 | -45.82013 | 2024-10-06 03:57:00 | NPP-375D | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 67f9cd7a-1541-37fd-82ad-07d4de4dc2a1 | -20.57505 | -45.82156 | 2024-10-06 03:57:00 | NPP-375D | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3890c10f-e49a-356f-98a1-70f720f7f91f | -20.31242 | -45.58549 | 2024-10-06 03:57:00 | NPP-375D | ARCOS | MINAS GERAIS | Brasil | 3104205 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 64eb1234-c527-3c87-bc58-137c9d821a4b | -20.02526 | -45.65089 | 2024-10-06 03:57:00 | NPP-375D | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 247960cb-b165-3a51-aa15-7fcc0f91a749 | -20.02437 | -45.65583 | 2024-10-06 03:57:00 | NPP-375D | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 2502b9f9-9228-3904-9796-eb435901d370 | -19.94989 | -45.1153 | 2024-10-06 03:57:00 | NPP-375D | PERDIGÃO | MINAS GERAIS | Brasil | 3149705 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8b58df52-e174-3074-ba2c-bd5ba43eb276 | -19.94862 | -45.11265 | 2024-10-06 03:57:00 | NPP-375D | PERDIGÃO | MINAS GERAIS | Brasil | 3149705 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 29cc6b88-aa52-3400-bfaf-e62a5f7ce370 | -19.83361 | -46.44919 | 2024-10-06 03:57:00 | NPP-375D | PRATINHA | MINAS GERAIS | Brasil | 3153004 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 4678a46f-8d9a-3e22-85a8-07077e5f3aa3 | -19.83072 | -46.44271 | 2024-10-06 03:57:00 | NPP-375D | PRATINHA | MINAS GERAIS | Brasil | 3153004 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ef192a68-7cd9-3dc0-a6fa-1f05244e652b | -19.82968 | -46.44821 | 2024-10-06 03:57:00 | NPP-375D | PRATINHA | MINAS GERAIS | Brasil | 3153004 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 10e8644c-0061-337c-afa4-6ea144794f9d | -19.82677 | -46.4418 | 2024-10-06 03:57:00 | NPP-375D | PRATINHA | MINAS GERAIS | Brasil | 3153004 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bbdc7f0e-c2ab-35ca-8617-e8a9cb3ace1f | -21.08301 | -45.72019 | 2024-10-06 03:57:00 | NPP-375D | BOA ESPERANÇA | MINAS GERAIS | Brasil | 3107109 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8f67941b-b3c4-3fd9-8b43-786d432e2dc2 | -21.08214 | -45.72498 | 2024-10-06 03:57:00 | NPP-375D | BOA ESPERANÇA | MINAS GERAIS | Brasil | 3107109 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| b6eb3328-1dae-3375-b06f-8bfd0b73236b | -21.78284 | -46.18366 | 2024-10-06 03:57:00 | NPP-375D | CAMPESTRE | MINAS GERAIS | Brasil | 3111002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 21.5 |
| 03df203d-d559-3f4b-a144-ca8161aed0ed | -21.78193 | -46.18861 | 2024-10-06 03:57:00 | NPP-375D | CAMPESTRE | MINAS GERAIS | Brasil | 3111002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 21.5 |
| 0cf4389b-bc7f-36db-9a63-ed55076ae155 | -20.98262 | -46.07414 | 2024-10-06 03:57:00 | NPP-375D | CARMO DO RIO CLARO | MINAS GERAIS | Brasil | 3114402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 77b2fdf4-01b2-308d-bd16-a903b24d13bc | -22.75752 | -47.01031 | 2024-10-06 03:57:00 | NPP-375D | CAMPINAS | SÃO PAULO | Brasil | 3509502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| c8831651-8a8c-37d4-b05a-3a06a80b5ae8 | -22.7562 | -47.01139 | 2024-10-06 03:57:00 | NPP-375D | CAMPINAS | SÃO PAULO | Brasil | 3509502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 4e0f9cd7-5054-3fc2-a018-00c69d24f2dd | -22.73591 | -47.03908 | 2024-10-06 03:57:00 | NPP-375D | CAMPINAS | SÃO PAULO | Brasil | 3509502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| c72355e2-0b69-3d47-aec7-85a8895e8517 | -17.63418 | -46.9818 | 2024-10-06 03:57:00 | NPP-375D | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0efa43f2-e5f7-3f34-8714-4f809e455848 | -17.63225 | -46.9684 | 2024-10-06 03:57:00 | NPP-375D | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1aad3eda-f3a1-3ac3-9870-03c4266c77dd | -17.63151 | -46.97239 | 2024-10-06 03:57:00 | NPP-375D | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ee3c690c-697f-36c6-879d-260c98f258ec | -17.62998 | -46.98054 | 2024-10-06 03:57:00 | NPP-375D | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 52706583-d794-3d37-ab36-ebe526180ecd | -19.0709 | -47.00629 | 2024-10-06 03:57:00 | NPP-375D | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 5a316dbc-bfdf-3b71-aee8-5763e4a96509 | -19.07013 | -47.01031 | 2024-10-06 03:57:00 | NPP-375D | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 2950aae6-93e9-334e-a362-702f937c63f2 | -19.06677 | -47.0053 | 2024-10-06 03:57:00 | NPP-375D | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6d830014-f230-333d-be1b-cbce45aa718a | -18.99443 | -46.9745 | 2024-10-06 03:57:00 | NPP-375D | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f2e64c38-09e4-383f-b4bd-41407fe50d97 | -18.88038 | -46.63046 | 2024-10-06 03:57:00 | NPP-375D | CRUZEIRO DA FORTALEZA | MINAS GERAIS | Brasil | 3120706 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1e18d766-1674-3a35-b6a5-1f56c3eeb317 | -18.59926 | -46.38902 | 2024-10-06 03:57:00 | NPP-375D | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4a281908-78d6-3ed8-b527-42f427152a87 | -18.59522 | -46.38823 | 2024-10-06 03:57:00 | NPP-375D | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 489ac1bd-b848-3189-899a-30ade0ab6995 | -18.45728 | -46.66328 | 2024-10-06 03:57:00 | NPP-375D | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f468b464-dca1-32c0-9b04-08a780738d97 | -18.45386 | -46.65866 | 2024-10-06 03:57:00 | NPP-375D | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dc154f15-949f-32ec-8600-06b024a17515 | -18.44972 | -46.65797 | 2024-10-06 03:57:00 | NPP-375D | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6712e2d9-b8cb-31d7-b7ac-0c768666ff19 | -18.44903 | -46.66167 | 2024-10-06 03:57:00 | NPP-375D | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0df236e4-3621-3d53-81e8-052ac916ad6e | -18.44417 | -46.66484 | 2024-10-06 03:57:00 | NPP-375D | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e51c7c78-fd92-3226-83da-226b366869a3 | -18.44345 | -46.66876 | 2024-10-06 03:57:00 | NPP-375D | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4c4739d3-17b8-3ad7-a019-68ee04b176f2 | -18.78915 | -47.47734 | 2024-10-06 03:57:00 | NPP-375D | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bb3d5adb-0b12-3c5d-92d9-a3246ef45d31 | -18.47488 | -47.3941 | 2024-10-06 03:57:00 | NPP-375D | ABADIA DOS DOURADOS | MINAS GERAIS | Brasil | 3100104 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7eba090c-43c9-32cd-b107-7638d875f2fa | -18.30963 | -47.56969 | 2024-10-06 03:57:00 | NPP-375D | ABADIA DOS DOURADOS | MINAS GERAIS | Brasil | 3100104 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 418d9d5c-66b8-360b-8b9f-69b97683695d | -18.30555 | -47.57136 | 2024-10-06 03:57:00 | NPP-375D | ABADIA DOS DOURADOS | MINAS GERAIS | Brasil | 3100104 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c6a36d2d-a130-3572-b30a-bb1a03ebea9b | -18.30437 | -47.57335 | 2024-10-06 03:57:00 | NPP-375D | ABADIA DOS DOURADOS | MINAS GERAIS | Brasil | 3100104 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |


[Clique aqui para ver as próximas entradas](README60.md)
