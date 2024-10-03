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

## Dados Diários - Página 143

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 185691d1-0e56-32e9-8af3-3a5250ff94a2 | -19.27257 | -43.77518 | 2024-10-03 04:53:00 | NPP-375D | BALDIM | MINAS GERAIS | Brasil | 3105004 | 31 | 33 | nan | nan | nan | Cerrado | 6.0 |
| eca77f4a-c5fd-3319-baae-c2f7d6288e74 | -19.26758 | -43.76878 | 2024-10-03 04:53:00 | NPP-375D | BALDIM | MINAS GERAIS | Brasil | 3105004 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 491ba4d9-edac-30dd-8f68-5700c59ef77f | -19.26711 | -43.77373 | 2024-10-03 04:53:00 | NPP-375D | BALDIM | MINAS GERAIS | Brasil | 3105004 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ad01ff37-b690-32bd-9c22-13f9f982e048 | -19.26685 | -43.76951 | 2024-10-03 04:53:00 | NPP-375D | BALDIM | MINAS GERAIS | Brasil | 3105004 | 31 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 3ed84b93-5125-3020-9a4f-88ad08355af6 | -19.26639 | -43.77456 | 2024-10-03 04:53:00 | NPP-375D | BALDIM | MINAS GERAIS | Brasil | 3105004 | 31 | 33 | nan | nan | nan | Cerrado | 6.0 |
| c9be04c7-87ee-3ae4-b203-98f6ce305eaa | -19.26614 | -43.78381 | 2024-10-03 04:53:00 | NPP-375D | BALDIM | MINAS GERAIS | Brasil | 3105004 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 09167841-764a-34be-a15d-0978485485ce | -19.26593 | -43.77974 | 2024-10-03 04:53:00 | NPP-375D | BALDIM | MINAS GERAIS | Brasil | 3105004 | 31 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 6c22ace2-7aca-3712-b9d7-f9e36d783dd0 | -19.24704 | -43.38034 | 2024-10-03 04:53:00 | NPP-375D | MORRO DO PILAR | MINAS GERAIS | Brasil | 3143708 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 68fc18aa-ae7a-33e6-8817-f3d772f0ef3a | -19.24069 | -43.38005 | 2024-10-03 04:53:00 | NPP-375D | MORRO DO PILAR | MINAS GERAIS | Brasil | 3143708 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4fc8de31-23c9-3387-b697-add661b60e54 | -19.24029 | -43.3845 | 2024-10-03 04:53:00 | NPP-375D | MORRO DO PILAR | MINAS GERAIS | Brasil | 3143708 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cfea0b2e-ec62-3d40-8ff7-8b32a493ed12 | -18.60315 | -43.93028 | 2024-10-03 04:53:00 | NPP-375D | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 45bb06b7-5cd7-3575-b550-384368a244ab | -18.6027 | -43.93497 | 2024-10-03 04:53:00 | NPP-375D | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f272a2ec-c498-3b5b-b5c0-1e4b985313c5 | -18.59749 | -43.92553 | 2024-10-03 04:53:00 | NPP-375D | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e82b6cec-dcef-375a-b5c5-b3b6d827acfc | -18.59703 | -43.93015 | 2024-10-03 04:53:00 | NPP-375D | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 10516504-2823-3bf0-ba17-7cf7233c36c5 | -18.59659 | -43.93465 | 2024-10-03 04:53:00 | NPP-375D | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c89833ac-9981-37a2-994b-5c5c8baf98f7 | -18.76733 | -43.38742 | 2024-10-03 04:53:00 | NPP-375D | ALVORADA DE MINAS | MINAS GERAIS | Brasil | 3102407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 15c145dd-30f1-3b1e-af40-8b7e68bd627d | -18.76427 | -43.38194 | 2024-10-03 04:53:00 | NPP-375D | ALVORADA DE MINAS | MINAS GERAIS | Brasil | 3102407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| a15a3875-df63-327a-b97c-97b02459484d | -18.76379 | -43.38731 | 2024-10-03 04:53:00 | NPP-375D | ALVORADA DE MINAS | MINAS GERAIS | Brasil | 3102407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| f5955755-c1e6-3340-88c9-1e2068f87d24 | -18.76109 | -43.38626 | 2024-10-03 04:53:00 | NPP-375D | ALVORADA DE MINAS | MINAS GERAIS | Brasil | 3102407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 912f6e7f-a9bd-339b-b910-a7bbb9d9a348 | -18.31174 | -43.23379 | 2024-10-03 04:53:00 | NPP-375D | SERRA AZUL DE MINAS | MINAS GERAIS | Brasil | 3166501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| 699be001-0078-329e-827e-552d63e82941 | -19.7576 | -44.26096 | 2024-10-03 04:53:00 | NPP-375D | ESMERALDAS | MINAS GERAIS | Brasil | 3124104 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7aff5579-4283-3516-a823-d71d3ef94ac2 | -19.753 | -44.2567 | 2024-10-03 04:53:00 | NPP-375D | ESMERALDAS | MINAS GERAIS | Brasil | 3124104 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8a0cd3df-8889-3b71-aae6-b873a0396123 | -19.75254 | -44.26175 | 2024-10-03 04:53:00 | NPP-375D | ESMERALDAS | MINAS GERAIS | Brasil | 3124104 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a2cb6123-3206-35a7-ba8d-59c43589b565 | -19.75155 | -44.26056 | 2024-10-03 04:53:00 | NPP-375D | ESMERALDAS | MINAS GERAIS | Brasil | 3124104 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 937f593d-bcc4-36a8-a272-1663bffad5ed | -19.74654 | -44.26086 | 2024-10-03 04:53:00 | NPP-375D | ESMERALDAS | MINAS GERAIS | Brasil | 3124104 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 13472793-1e3a-379f-aef4-3589e2ff62cb | -19.74613 | -44.26537 | 2024-10-03 04:53:00 | NPP-375D | ESMERALDAS | MINAS GERAIS | Brasil | 3124104 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b4ab5dce-6ee5-33ca-bbe5-a339339f2d42 | -19.74553 | -44.25982 | 2024-10-03 04:53:00 | NPP-375D | ESMERALDAS | MINAS GERAIS | Brasil | 3124104 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1f0396a6-44f6-3bdd-a694-93a9d6fc1899 | -19.74511 | -44.26427 | 2024-10-03 04:53:00 | NPP-375D | ESMERALDAS | MINAS GERAIS | Brasil | 3124104 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 99ca926e-b3d2-342f-8e2a-1be9dd9bfdeb | -19.74093 | -44.25556 | 2024-10-03 04:53:00 | NPP-375D | ESMERALDAS | MINAS GERAIS | Brasil | 3124104 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4a1ef8fd-9043-3462-82ba-5d68fc01292c | -19.74054 | -44.25994 | 2024-10-03 04:53:00 | NPP-375D | ESMERALDAS | MINAS GERAIS | Brasil | 3124104 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ef5cfba0-9de1-34e5-a914-4d276c321231 | -19.7404 | -44.24996 | 2024-10-03 04:53:00 | NPP-375D | ESMERALDAS | MINAS GERAIS | Brasil | 3124104 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1cb82278-1aa9-3054-951e-89913e155ed3 | -19.74014 | -44.26439 | 2024-10-03 04:53:00 | NPP-375D | ESMERALDAS | MINAS GERAIS | Brasil | 3124104 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 4a504524-516d-3c2e-a164-5e8f00d68560 | -19.73996 | -44.25449 | 2024-10-03 04:53:00 | NPP-375D | ESMERALDAS | MINAS GERAIS | Brasil | 3124104 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2abbf278-6458-34ba-a017-72b54f7bb73d | -19.73911 | -44.26333 | 2024-10-03 04:53:00 | NPP-375D | ESMERALDAS | MINAS GERAIS | Brasil | 3124104 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| aef1d810-8835-32b5-8bdf-eef355be5ad5 | -19.7353 | -44.25046 | 2024-10-03 04:53:00 | NPP-375D | ESMERALDAS | MINAS GERAIS | Brasil | 3124104 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 18f825db-9feb-35e6-8ca5-713949eb319f | -19.73434 | -44.24959 | 2024-10-03 04:53:00 | NPP-375D | ESMERALDAS | MINAS GERAIS | Brasil | 3124104 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5d4250c6-7ec2-3a1f-8e53-8aa3d3b81ef5 | -19.5254 | -44.25244 | 2024-10-03 04:53:00 | NPP-375D | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 28e48df9-ace9-35b8-9025-8f13e4e7e1bc | -20.01824 | -44.50923 | 2024-10-03 04:53:00 | NPP-375D | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| db34b714-acef-36ef-bc0a-5aa9ba04ea65 | -20.01777 | -44.51408 | 2024-10-03 04:53:00 | NPP-375D | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 1bcc19a2-b044-31bd-bb5a-fdbf01774432 | -20.01315 | -44.49956 | 2024-10-03 04:53:00 | NPP-375D | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 8015b0bf-eefb-3a9e-bf4b-76f8042cfcf8 | -20.01268 | -44.50443 | 2024-10-03 04:53:00 | NPP-375D | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 166f3655-6c5f-3966-b5ac-7e5d037ae8ea | -20.01222 | -44.50932 | 2024-10-03 04:53:00 | NPP-375D | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 99255908-82f0-3ff1-b4a5-fcfbdb297f31 | -20.01175 | -44.51425 | 2024-10-03 04:53:00 | NPP-375D | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| e07341f7-4cb7-3853-829e-a7a680a87e52 | -19.81568 | -43.8331 | 2024-10-03 04:53:00 | NPP-375D | SANTA LUZIA | MINAS GERAIS | Brasil | 3157807 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2e75f47d-6292-3c4d-b62f-4c9572d47018 | -19.81137 | -43.83198 | 2024-10-03 04:53:00 | NPP-375D | SANTA LUZIA | MINAS GERAIS | Brasil | 3157807 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 88a41c25-e5ab-3be8-b2c1-b85c58105a45 | -19.81092 | -43.8367 | 2024-10-03 04:53:00 | NPP-375D | SANTA LUZIA | MINAS GERAIS | Brasil | 3157807 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f3cffc24-daad-3fca-8eca-15dd8d1ed351 | -19.8095 | -43.83236 | 2024-10-03 04:53:00 | NPP-375D | SANTA LUZIA | MINAS GERAIS | Brasil | 3157807 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b6283437-8359-3669-867a-01b8551c45d6 | -19.80908 | -43.8371 | 2024-10-03 04:53:00 | NPP-375D | SANTA LUZIA | MINAS GERAIS | Brasil | 3157807 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9855e739-5aad-3fd8-b1b1-01c971bbd0db | -20.14758 | -43.85199 | 2024-10-03 04:53:00 | NPP-375D | RIO ACIMA | MINAS GERAIS | Brasil | 3154804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 35cd6f6e-7eb7-370d-b260-e7207b688fc8 | -20.1409 | -43.85672 | 2024-10-03 04:53:00 | NPP-375D | NOVA LIMA | MINAS GERAIS | Brasil | 3144805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 6f10d037-cec5-31fa-8e21-dc461dd91ca0 | -22.118 | -45.09016 | 2024-10-03 04:53:00 | NPP-375D | CARMO DE MINAS | MINAS GERAIS | Brasil | 3114105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 1f2b8cab-8448-32c0-92d4-c52e083825a8 | -22.1176 | -45.09484 | 2024-10-03 04:53:00 | NPP-375D | CARMO DE MINAS | MINAS GERAIS | Brasil | 3114105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 2d74e878-1b1e-3012-8ff6-460d40001171 | -21.45745 | -44.58482 | 2024-10-03 04:53:00 | NPP-375D | CARRANCAS | MINAS GERAIS | Brasil | 3114600 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 1c99162b-6183-3505-8113-cadac252aff4 | -21.4571 | -44.58874 | 2024-10-03 04:53:00 | NPP-375D | CARRANCAS | MINAS GERAIS | Brasil | 3114600 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.7 |
| 0886c99c-7ebb-359b-bf4e-037ba3d91076 | -21.45674 | -44.5928 | 2024-10-03 04:53:00 | NPP-375D | CARRANCAS | MINAS GERAIS | Brasil | 3114600 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.7 |
| 9fd5bdcb-0179-372e-ae4f-54e6ae99be0d | -21.45637 | -44.59694 | 2024-10-03 04:53:00 | NPP-375D | CARRANCAS | MINAS GERAIS | Brasil | 3114600 | 31 | 33 | nan | nan | nan | Mata Atlântica | 14.7 |
| 30f73830-c70f-38bc-bc0a-65c102f3ba23 | -21.45598 | -44.60132 | 2024-10-03 04:53:00 | NPP-375D | CARRANCAS | MINAS GERAIS | Brasil | 3114600 | 31 | 33 | nan | nan | nan | Mata Atlântica | 14.7 |
| 167c778e-aeea-3fae-9f0b-d38f02853cee | -21.45279 | -44.56882 | 2024-10-03 04:53:00 | NPP-375D | CARRANCAS | MINAS GERAIS | Brasil | 3114600 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 7f2a2ad3-a2c1-342d-8feb-1f5333dfe328 | -21.4523 | -44.5743 | 2024-10-03 04:53:00 | NPP-375D | CARRANCAS | MINAS GERAIS | Brasil | 3114600 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 81a896b1-b697-3ff0-b013-ef6c73d2d386 | -21.45188 | -44.57914 | 2024-10-03 04:53:00 | NPP-375D | CARRANCAS | MINAS GERAIS | Brasil | 3114600 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| f9d0d00a-6ebc-3441-bd83-72b5e89298b0 | -21.45151 | -44.58321 | 2024-10-03 04:53:00 | NPP-375D | CARRANCAS | MINAS GERAIS | Brasil | 3114600 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| 0c56363a-70e2-3af5-bc67-2e02ad0164e2 | -21.45117 | -44.58711 | 2024-10-03 04:53:00 | NPP-375D | CARRANCAS | MINAS GERAIS | Brasil | 3114600 | 31 | 33 | nan | nan | nan | Mata Atlântica | 15.2 |
| e5298093-d5f6-38fa-90a9-06c980a3b106 | -21.45081 | -44.5912 | 2024-10-03 04:53:00 | NPP-375D | CARRANCAS | MINAS GERAIS | Brasil | 3114600 | 31 | 33 | nan | nan | nan | Mata Atlântica | 15.2 |
| ee310140-6c2d-3b47-b008-fdfa9a80ee2f | -21.45044 | -44.5954 | 2024-10-03 04:53:00 | NPP-375D | CARRANCAS | MINAS GERAIS | Brasil | 3114600 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.3 |
| 4be8703b-4296-35a3-818a-9e356ca9f352 | -21.45005 | -44.59976 | 2024-10-03 04:53:00 | NPP-375D | CARRANCAS | MINAS GERAIS | Brasil | 3114600 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.3 |
| c7870056-8d58-3b8f-a805-2fd0db25123c | -21.446 | -44.57685 | 2024-10-03 04:53:00 | NPP-375D | CARRANCAS | MINAS GERAIS | Brasil | 3114600 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| 8e47d4a0-8233-30b2-a63c-0a2b850003a1 | -21.44558 | -44.58163 | 2024-10-03 04:53:00 | NPP-375D | CARRANCAS | MINAS GERAIS | Brasil | 3114600 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| faf62fca-f057-3866-9d00-dea2fe9a4303 | -21.4452 | -44.58601 | 2024-10-03 04:53:00 | NPP-375D | CARRANCAS | MINAS GERAIS | Brasil | 3114600 | 31 | 33 | nan | nan | nan | Mata Atlântica | 15.2 |
| b04003f7-4364-35f8-a859-2a2e43aa75f6 | -22.31433 | -44.06384 | 2024-10-03 04:53:00 | NPP-375D | VALENÇA | RIO DE JANEIRO | Brasil | 3306107 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 21aeb051-4419-3a72-b75c-85f366cd962f | -22.31395 | -44.06864 | 2024-10-03 04:53:00 | NPP-375D | VALENÇA | RIO DE JANEIRO | Brasil | 3306107 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| ab2f0222-892b-34f5-8eff-f711dee6261d | -22.30584 | -44.05459 | 2024-10-03 04:53:00 | NPP-375D | VALENÇA | RIO DE JANEIRO | Brasil | 3306107 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| b7c7cfe6-d5e6-364c-bc51-dbd61ba1d0c9 | -22.30544 | -44.05912 | 2024-10-03 04:53:00 | NPP-375D | VALENÇA | RIO DE JANEIRO | Brasil | 3306107 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| e7931469-ab40-324b-9637-7f08411b7a5d | -22.29846 | -44.06688 | 2024-10-03 04:53:00 | NPP-375D | VALENÇA | RIO DE JANEIRO | Brasil | 3306107 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 47c4f844-42d1-3c9a-89d2-554116ae35aa | -22.29798 | -44.07243 | 2024-10-03 04:53:00 | NPP-375D | VALENÇA | RIO DE JANEIRO | Brasil | 3306107 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| cb237d2c-f996-3188-9b87-e17c1f46ff3b | -16.64521 | -44.36328 | 2024-10-03 04:53:00 | NPP-375D | CORAÇÃO DE JESUS | MINAS GERAIS | Brasil | 3118809 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1c01f2f8-5ca8-3f42-a38e-e7d4404f3c22 | -16.64477 | -44.36737 | 2024-10-03 04:53:00 | NPP-375D | CORAÇÃO DE JESUS | MINAS GERAIS | Brasil | 3118809 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 326c0c50-4496-36fa-a55f-e6eb296b4fd0 | -16.91404 | -45.31701 | 2024-10-03 04:53:00 | NPP-375D | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c4ec4526-73b3-3cdf-ba61-4745ffd31778 | -16.90821 | -45.31975 | 2024-10-03 04:53:00 | NPP-375D | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4b157933-f637-3523-ba42-59e9b1c569fc | -16.90397 | -45.30844 | 2024-10-03 04:53:00 | NPP-375D | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| caddfad1-91fc-31b5-be65-a89d4ab423fd | -19.05874 | -45.55962 | 2024-10-03 04:53:00 | NPP-375D | ABAETÉ | MINAS GERAIS | Brasil | 3100203 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9502a99a-51cf-34ef-8ab8-3c52abbfc621 | -20.76887 | -46.29283 | 2024-10-03 04:53:00 | NPP-375D | SÃO JOSÉ DA BARRA | MINAS GERAIS | Brasil | 3162948 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6f208063-afa1-3aca-995c-fa5d1903f941 | -20.76851 | -46.29643 | 2024-10-03 04:53:00 | NPP-375D | SÃO JOSÉ DA BARRA | MINAS GERAIS | Brasil | 3162948 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3444f460-9ba1-3f2d-8588-8c54afbd17ef | -20.76814 | -46.30002 | 2024-10-03 04:53:00 | NPP-375D | SÃO JOSÉ DA BARRA | MINAS GERAIS | Brasil | 3162948 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d72eacd6-c842-30f3-b77e-ba44450486da | -20.76778 | -46.3036 | 2024-10-03 04:53:00 | NPP-375D | SÃO JOSÉ DA BARRA | MINAS GERAIS | Brasil | 3162948 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e53a15d5-755d-36ee-a189-e0f6f0680342 | -20.76743 | -46.30707 | 2024-10-03 04:53:00 | NPP-375D | SÃO JOSÉ DA BARRA | MINAS GERAIS | Brasil | 3162948 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bac9c17f-f01e-325c-9cbf-8a546d6dec0e | -19.72311 | -45.07866 | 2024-10-03 04:53:00 | NPP-375D | LEANDRO FERREIRA | MINAS GERAIS | Brasil | 3138302 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 41d8ab38-38be-3b89-91ac-2b37d9accd78 | -19.71775 | -45.07425 | 2024-10-03 04:53:00 | NPP-375D | LEANDRO FERREIRA | MINAS GERAIS | Brasil | 3138302 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| aac2e438-f754-3207-888f-3b2099ba24f6 | -20.80723 | -45.29679 | 2024-10-03 04:53:00 | NPP-375D | CANDEIAS | MINAS GERAIS | Brasil | 3112000 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 8b473e21-8ae1-3cf6-a83f-9111cf900002 | -21.37573 | -46.45739 | 2024-10-03 04:53:00 | NPP-375D | MUZAMBINHO | MINAS GERAIS | Brasil | 3144102 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 6c79b64f-1ada-3c92-b9a0-55c09d34492d | -21.37039 | -46.4567 | 2024-10-03 04:53:00 | NPP-375D | MUZAMBINHO | MINAS GERAIS | Brasil | 3144102 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 920ac113-202d-3533-8000-4085ee3c76fb | -17.60228 | -46.95774 | 2024-10-03 04:53:00 | NPP-375D | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 9d11d80a-a18f-3ef8-8132-ae460b7527ee | -17.60158 | -46.96384 | 2024-10-03 04:53:00 | NPP-375D | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| ea8c542b-247e-335e-908c-746db6eb2981 | -17.59668 | -46.96304 | 2024-10-03 04:53:00 | NPP-375D | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b93abfe7-aa6d-3d8a-84d7-7753af9cdb20 | -17.414 | -46.31475 | 2024-10-03 04:53:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f5065311-7483-3280-bd3b-9b7fe7289059 | -17.41364 | -46.31789 | 2024-10-03 04:53:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e45960bc-057c-3d7f-b9f0-92a59bff67f4 | -17.12452 | -47.13066 | 2024-10-03 04:53:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 5.7 |
| eb6bb882-1ef7-31a9-a78e-bdac23db4006 | -17.12386 | -47.13605 | 2024-10-03 04:53:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 367622f4-e6f0-3a13-a6e0-d5b0ff721c83 | -17.1224 | -47.13119 | 2024-10-03 04:53:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 4c203fc0-12cc-3cd5-8f34-eec039b1ad02 | -17.12179 | -47.13653 | 2024-10-03 04:53:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 11.6 |
| f9e6d1db-d0c1-32e6-84b8-6e037de7fddf | -17.11963 | -47.13043 | 2024-10-03 04:53:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 5.7 |


[Clique aqui para ver as próximas entradas](README144.md)
