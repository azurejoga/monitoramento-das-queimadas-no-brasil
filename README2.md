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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0fe3257e-69e5-3b81-93c8-1f935428c573 | -20.28878 | -50.981 | 2025-03-05 03:46:00 | NPP-375D | SANTA FÉ DO SUL | SÃO PAULO | Brasil | 3546603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 33241765-cc59-300b-a646-61fd1ea2bd14 | -22.85598 | -42.97927 | 2025-03-05 03:46:00 | NPP-375D | SÃO GONÇALO | RIO DE JANEIRO | Brasil | 3304904 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| ce322d6f-ddc5-32ce-8b0a-41de5ef14192 | -21.91204 | -42.26204 | 2025-03-05 03:46:00 | NPP-375D | CANTAGALO | RIO DE JANEIRO | Brasil | 3301108 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| f7be79c0-f37d-3263-bda5-322c5210cf70 | -22.8784 | -42.58091 | 2025-03-05 03:46:00 | NPP-375D | SAQUAREMA | RIO DE JANEIRO | Brasil | 3305505 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 8fef5eea-3408-30ff-9ec3-2923bbd30ea4 | -21.17978 | -43.97995 | 2025-03-05 03:46:00 | NPP-375D | BARROSO | MINAS GERAIS | Brasil | 3105905 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| d3b83ee8-3a91-3ec8-8065-1ab5c58ef050 | -22.78601 | -43.75795 | 2025-03-05 03:46:00 | NPP-375D | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 2c765a9d-c8ac-3ec1-ada7-2eff33919bc4 | -22.77274 | -42.83696 | 2025-03-05 03:46:00 | NPP-375D | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 64879f64-b05c-3fb0-b89c-98da79828c31 | -21.6187 | -48.47683 | 2025-03-05 03:46:00 | NPP-375D | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bac2ea98-4f22-3299-8382-cca82761495d | -21.64793 | -46.42457 | 2025-03-05 03:46:00 | NPP-375D | BOTELHOS | MINAS GERAIS | Brasil | 3108404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 311809b1-e6e0-3110-b17f-a2824cd99225 | -22.79412 | -42.80268 | 2025-03-05 03:46:00 | NPP-375D | TANGUÁ | RIO DE JANEIRO | Brasil | 3305752 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 3ebc26a6-a86c-357b-938d-dfa5894cac0e | -22.67577 | -42.85814 | 2025-03-05 03:46:00 | NPP-375D | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 4e445122-fd3d-3108-9994-0b7015f27940 | -20.28381 | -50.97406 | 2025-03-05 03:46:00 | NPP-375D | SANTA FÉ DO SUL | SÃO PAULO | Brasil | 3546603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 1dfc8cf4-17f4-39ff-bfbb-457378cf6faa | -22.79208 | -42.80531 | 2025-03-05 03:46:00 | NPP-375D | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| cab77c84-8e89-38e6-b6a5-fc2cb6bb6a70 | -22.75305 | -43.26751 | 2025-03-05 03:46:00 | NPP-375D | DUQUE DE CAXIAS | RIO DE JANEIRO | Brasil | 3301702 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 0324a27c-b649-30e9-adcf-11da16fb50d8 | -21.0409 | -41.89531 | 2025-03-05 03:46:00 | NPP-375D | NATIVIDADE | RIO DE JANEIRO | Brasil | 3303104 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| b7d4c12e-19aa-3a7c-b267-7d1414c552e8 | -19.63736 | -47.16166 | 2025-03-05 03:46:00 | NPP-375D | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 15ca24a4-3302-30c2-ad65-7d5d53cd2858 | -22.67221 | -42.86433 | 2025-03-05 03:46:00 | NPP-375D | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| a071bc35-cd53-344c-850b-d448ac8da66d | -22.90005 | -43.7527 | 2025-03-05 03:46:00 | NPP-375D | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 0f6a9bad-7b94-31df-8550-a8c9ed1e0b39 | -22.67503 | -42.86981 | 2025-03-05 03:46:00 | NPP-375D | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| 59c9f1f9-5a55-3433-b338-c56c4a6779af | -22.68028 | -42.85425 | 2025-03-05 03:46:00 | NPP-375D | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 9e1a3daa-347f-32a2-9dd5-eff739094657 | -20.00525 | -45.40242 | 2025-03-05 03:46:00 | NPP-375D | SANTO ANTÔNIO DO MONTE | MINAS GERAIS | Brasil | 3160405 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7adce62c-8f9c-339b-9cbd-14007ba248a6 | -19.63291 | -47.15775 | 2025-03-05 03:46:00 | NPP-375D | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d24e9e10-e101-314f-9c11-f7013c969c3a | -22.67409 | -42.86752 | 2025-03-05 03:46:00 | NPP-375D | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 14.7 |
| 0ce1731f-bb31-3f0c-a5ae-b0e49df10db6 | -22.68217 | -42.85186 | 2025-03-05 03:46:00 | NPP-375D | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 69f0efd6-a8f4-331e-9150-5425361ec2dd | -22.68112 | -42.84956 | 2025-03-05 03:46:00 | NPP-375D | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| ae111874-4167-3d8b-aa64-a58192baa7d3 | -20.29003 | -50.97564 | 2025-03-05 03:46:00 | NPP-375D | SANTA FÉ DO SUL | SÃO PAULO | Brasil | 3546603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 388181b2-646a-3665-a53a-f800499c84ad | -20.28257 | -50.97938 | 2025-03-05 03:46:00 | NPP-375D | SANTA FÉ DO SUL | SÃO PAULO | Brasil | 3546603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| a7b68bb1-4fcd-3e4d-ad82-fd17feb8cbbc | -22.79328 | -42.80738 | 2025-03-05 03:46:00 | NPP-375D | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| c126fe78-a9f4-3b70-b271-92f51ee5982c | -22.68131 | -42.85654 | 2025-03-05 03:46:00 | NPP-375D | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 749910c5-b7f1-343d-9777-db17ef9e8a83 | -17.7926 | -48.99804 | 2025-03-05 03:46:00 | NPP-375D | MORRINHOS | GOIÁS | Brasil | 5213806 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ab096e51-17bd-3245-a26b-2495ec9ab3c6 | -22.67676 | -42.86044 | 2025-03-05 03:46:00 | NPP-375D | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 17.2 |
| a29b7f27-ed4b-37f1-8f37-bacd0c1b3c63 | -22.77558 | -42.8424 | 2025-03-05 03:46:00 | NPP-375D | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 5b0b8065-861d-3220-979a-d391cc76a0f0 | -22.87922 | -42.57639 | 2025-03-05 03:46:00 | NPP-375D | SAQUAREMA | RIO DE JANEIRO | Brasil | 3305505 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 299274b2-ace0-3b53-9842-3658295645ea | -19.71847 | -40.35442 | 2025-03-05 03:46:00 | NPP-375D | JOÃO NEIVA | ESPÍRITO SANTO | Brasil | 3203130 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 73ac303a-8ae5-33e5-9792-27c251400efa | -19.63228 | -47.16077 | 2025-03-05 03:46:00 | NPP-375D | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6885b618-a9c8-31fd-9793-683a0842976a | -21.91182 | -42.26381 | 2025-03-05 03:46:00 | NPP-375D | CANTAGALO | RIO DE JANEIRO | Brasil | 3301108 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| fc3bb99e-8bd0-3804-9b23-6a4fc69e7211 | -17.59512 | -43.19701 | 2025-03-05 03:46:00 | NPP-375D | CARBONITA | MINAS GERAIS | Brasil | 3113503 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 096488e8-b4b7-3573-9e26-cfeec6df0871 | -15.37934 | -43.72179 | 2025-03-05 03:46:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 210f2fbb-bbad-38ba-a34a-e40b30ab0e96 | -21.6525 | -46.42581 | 2025-03-05 03:46:00 | NPP-375D | BOTELHOS | MINAS GERAIS | Brasil | 3108404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| bdbee1c4-e93d-37ad-ae14-ff65d0658193 | -22.84348 | -43.5989 | 2025-03-05 03:46:00 | NPP-375D | NOVA IGUAÇU | RIO DE JANEIRO | Brasil | 3303500 | 33 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| 9ef285c4-86e9-3e5c-9c4e-4adfd4646701 | -19.63798 | -47.15865 | 2025-03-05 03:46:00 | NPP-375D | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 820848c7-1c8b-33f4-96d6-be7a7fbfb2e0 | -17.67785 | -42.74198 | 2025-03-05 03:46:00 | NPP-375D | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dc4d17bd-24b0-3918-b082-144e11b03e2f | -22.67493 | -42.86283 | 2025-03-05 03:46:00 | NPP-375D | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 14.7 |
| dc327389-d7db-3b03-b177-f2aad8213cfd | -17.79166 | -49.00235 | 2025-03-05 03:46:00 | NPP-375D | MORRINHOS | GOIÁS | Brasil | 5213806 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ce996b41-943b-37fe-bf25-e665ed7f6fbe | -20.00613 | -45.40454 | 2025-03-05 03:46:00 | NPP-375D | SANTO ANTÔNIO DO MONTE | MINAS GERAIS | Brasil | 3160405 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 455d7fe0-6f28-3a6c-965b-251440b580e0 | -22.6759 | -42.86512 | 2025-03-05 03:46:00 | NPP-375D | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 17.2 |
| 41fd8f99-3364-38bb-9654-6ed2fb5ba178 | -21.65046 | -46.42206 | 2025-03-05 03:46:00 | NPP-375D | BOTELHOS | MINAS GERAIS | Brasil | 3108404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 642bc64a-eb02-3ce5-8c86-d5ea684e9774 | -22.96198 | -42.90698 | 2025-03-05 03:46:00 | NPP-375D | MARICÁ | RIO DE JANEIRO | Brasil | 3302700 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| a8c26dbf-2b63-3d2d-aa0a-4679fd0497b1 | -22.67777 | -42.86832 | 2025-03-05 03:46:00 | NPP-375D | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 14.7 |
| 238c86fb-f17e-308a-ab23-5be411868f97 | -27.70714 | -50.62433 | 2025-03-05 03:49:00 | NPP-375D | SÃO JOSÉ DO CERRITO | SANTA CATARINA | Brasil | 4216800 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| ba7a029c-aa62-3c01-93a6-6f759480d5c0 | -25.11272 | -52.73111 | 2025-03-05 03:49:00 | NPP-375D | GUARANIAÇU | PARANÁ | Brasil | 4109302 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| ab481ec4-2efa-3e83-ac3b-0f30b99bda2d | -23.3375 | -46.77466 | 2025-03-05 03:49:00 | NPP-375D | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| e756b0b9-a9a2-3920-834c-bf0eb2e21f98 | -23.40677 | -46.55666 | 2025-03-05 03:49:00 | NPP-375D | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 04478558-e917-3f53-b110-1f4193b13619 | -25.11403 | -52.726 | 2025-03-05 03:49:00 | NPP-375D | GUARANIAÇU | PARANÁ | Brasil | 4109302 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 109d2f90-6414-376a-a84c-aa6f7fda201c | -23.33855 | -46.77315 | 2025-03-05 03:49:00 | NPP-375D | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 5718e82b-d6fc-3960-9532-9e61137ddfe4 | -23.20143 | -46.40478 | 2025-03-05 03:49:00 | NPP-375D | NAZARÉ PAULISTA | SÃO PAULO | Brasil | 3532405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| a6a43db5-9b67-3f7d-8ba0-7c4ce5825c4b | -25.11036 | -52.73062 | 2025-03-05 03:49:00 | NPP-375D | GUARANIAÇU | PARANÁ | Brasil | 4109302 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| b78633b1-82fc-3c41-8bd4-ad2dce985bb2 | -25.11166 | -52.72539 | 2025-03-05 03:49:00 | NPP-375D | GUARANIAÇU | PARANÁ | Brasil | 4109302 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 8172207d-a26a-3710-beae-5678c7a7cc1a | -23.02086 | -48.75637 | 2025-03-05 03:49:00 | NPP-375D | ITATINGA | SÃO PAULO | Brasil | 3523503 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 79e66196-9f6f-31e0-a4a6-6cdadc0c3088 | -30.49455 | -51.83086 | 2025-03-05 03:51:00 | NPP-375D | BARÃO DO TRIUNFO | RIO GRANDE DO SUL | Brasil | 4301750 | 43 | 33 | nan | nan | nan | Pampa | 3.7 |
| 3c63ca63-48b1-39b1-a3d5-959df045ac9c | -30.49132 | -51.83226 | 2025-03-05 03:51:00 | NPP-375D | BARÃO DO TRIUNFO | RIO GRANDE DO SUL | Brasil | 4301750 | 43 | 33 | nan | nan | nan | Pampa | 1.2 |
| 9514b310-460d-3638-babd-451611d1619e | -28.58693 | -49.44476 | 2025-03-05 03:51:00 | NPP-375D | SIDERÓPOLIS | SANTA CATARINA | Brasil | 4217600 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 47b25182-bbe5-3672-8a84-3b76da300c9a | -30.49659 | -51.83381 | 2025-03-05 03:51:00 | NPP-375D | BARÃO DO TRIUNFO | RIO GRANDE DO SUL | Brasil | 4301750 | 43 | 33 | nan | nan | nan | Pampa | 5.0 |
| 411b3f78-4803-3a6b-8aec-510ed76d0ce8 | -30.49364 | -51.83451 | 2025-03-05 03:51:00 | NPP-375D | BARÃO DO TRIUNFO | RIO GRANDE DO SUL | Brasil | 4301750 | 43 | 33 | nan | nan | nan | Pampa | 3.7 |
| dd7a8da0-02c1-36bb-b959-630983e9e509 | -5.24256 | -36.201 | 2025-03-05 04:04:00 | NOAA-20 | GALINHOS | RIO GRANDE DO NORTE | Brasil | 2404101 | 24 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 7a691f8c-b6cc-3d8d-acdd-042b1155fe62 | -5.24659 | -36.20161 | 2025-03-05 04:04:00 | NOAA-20 | GALINHOS | RIO GRANDE DO NORTE | Brasil | 2404101 | 24 | 33 | nan | nan | nan | Caatinga | 0.6 |
| ac3c6ca1-5a3f-3cfc-bce9-c2950e27efcc | -6.96985 | -41.00914 | 2025-03-05 04:06:00 | NOAA-20 | MONSENHOR HIPÓLITO | PIAUÍ | Brasil | 2206506 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| adde0542-7d83-318b-bf5a-fa0abb415304 | -7.24307 | -44.78646 | 2025-03-05 04:06:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c07eac7e-66f3-3c65-a336-bc4d206643ed | -11.95541 | -37.83171 | 2025-03-05 04:06:00 | NOAA-20 | ESPLANADA | BAHIA | Brasil | 2910602 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 71c488ad-b016-374f-8f8e-575e35c6e162 | -9.05837 | -36.82129 | 2025-03-05 04:06:00 | NOAA-20 | IATI | PERNAMBUCO | Brasil | 2606507 | 26 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 1f8739f7-b0ca-30de-8f40-e1b2ca0647ef | -9.33988 | -43.08496 | 2025-03-05 04:06:00 | NOAA-20 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 05044fcb-06c2-3d24-8a85-26f690c4d0c8 | -9.34321 | -43.0855 | 2025-03-05 04:06:00 | NOAA-20 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 48113774-7cf1-37ea-b479-4d8cb4eafd99 | -8.37079 | -43.97899 | 2025-03-05 04:06:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dbefb8c8-767f-3308-9a4a-0db51d301907 | -7.98954 | -43.23645 | 2025-03-05 04:06:00 | NOAA-20 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 1a29adbb-69a9-384f-8857-b01d12fb99e2 | -9.85696 | -37.99888 | 2025-03-05 04:06:00 | NOAA-20 | SANTA BRÍGIDA | BAHIA | Brasil | 2927606 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 0a696115-f40e-39b8-b15c-bb67b93819f7 | -7.74324 | -35.42703 | 2025-03-05 04:06:00 | NOAA-20 | LIMOEIRO | PERNAMBUCO | Brasil | 2608909 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 41729bf2-4001-3ea3-9f41-52869c1b7cfc | -7.24666 | -44.78704 | 2025-03-05 04:06:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d650e78e-f6f2-3d53-b24d-21ef8c76f373 | -6.95288 | -43.00468 | 2025-03-05 04:06:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| f566b548-e53a-3fb7-b3e1-0fae79f39b65 | -9.34378 | -43.08195 | 2025-03-05 04:06:00 | NOAA-20 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 17f7602b-173d-390a-a9a9-f7048d60fc3f | -7.24374 | -44.78233 | 2025-03-05 04:06:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1ed52265-be5c-3d99-822e-9ad1dc68256a | -6.15458 | -44.75008 | 2025-03-05 04:06:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| bd217b07-625c-3c89-bc4a-26e81547c6d6 | -9.08272 | -37.31061 | 2025-03-05 04:06:00 | NOAA-20 | ITAÍBA | PERNAMBUCO | Brasil | 2607505 | 26 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 3d5f2666-7f23-3219-8dde-1a60136b3c27 | -7.09469 | -44.38476 | 2025-03-05 04:06:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 84703c41-0399-3630-aff8-ac3cc613fae1 | -7.24598 | -44.79118 | 2025-03-05 04:06:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| aa31049a-7c5b-3190-b233-dd446770fbaf | -8.3714 | -43.97525 | 2025-03-05 04:06:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cad95eae-44e9-3d31-8772-d43eec5551b5 | -7.09821 | -44.3854 | 2025-03-05 04:06:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 236f4f02-8510-36dc-a329-1c640b2e7cb3 | -10.51821 | -40.32852 | 2025-03-05 04:06:00 | NOAA-20 | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| badd4f83-2b8c-3b5d-b60c-868d7c331c37 | -7.74329 | -35.42885 | 2025-03-05 04:06:00 | NOAA-20 | LIMOEIRO | PERNAMBUCO | Brasil | 2608909 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| e7292024-4145-39af-923d-6b5797aa9ccc | -9.36712 | -40.43965 | 2025-03-05 04:06:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 0de4ee99-9ec9-34af-aead-9b1703c2edce | -7.44514 | -39.888 | 2025-03-05 04:06:00 | NOAA-20 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 1.6 |
| cd543366-e4af-31bd-9033-e07c24132114 | -10.50819 | -42.405 | 2025-03-05 04:06:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| a4b6795f-efb5-3acc-b82e-de0c070301cc | -9.85494 | -37.99599 | 2025-03-05 04:06:00 | NOAA-20 | SANTA BRÍGIDA | BAHIA | Brasil | 2927606 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| e48fa2b8-23b0-3fab-b686-5a195555a274 | -9.71183 | -37.13238 | 2025-03-05 04:06:00 | NOAA-20 | BATALHA | ALAGOAS | Brasil | 2700706 | 27 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 59e499ff-0318-3b40-8429-ad62f4748653 | -10.69499 | -37.04863 | 2025-03-05 04:06:00 | NOAA-20 | ROSÁRIO DO CATETE | SERGIPE | Brasil | 2806107 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| d4fe288f-c290-3c9c-8a87-d825a416303c | -7.24015 | -44.78176 | 2025-03-05 04:06:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 68497f85-9999-38d6-88dd-a00006ac9550 | -7.25223 | -45.37132 | 2025-03-05 04:06:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| caaa685a-1ac6-3ebb-b8be-2ebd34659acf | -17.38665 | -42.65876 | 2025-03-05 04:08:00 | NOAA-20 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c221ef8e-b5ff-32f8-b03d-1693472ccaea | -15.32074 | -48.71956 | 2025-03-05 04:08:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2262bed6-8ed8-3348-b231-6472334c1fec | -12.0129 | -43.79464 | 2025-03-05 04:08:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e0851356-3abe-3490-881a-e30001c4a856 | -17.78074 | -42.80913 | 2025-03-05 04:08:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README3.md)
