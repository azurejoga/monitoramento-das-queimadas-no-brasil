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

## Dados Diários - Página 38

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c8a6981f-2922-3f1a-9a0e-1043329ab270 | -20.93855 | -45.79223 | 2025-09-11 04:00:00 | NOAA-21 | ILICÍNEA | MINAS GERAIS | Brasil | 3130507 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cf85eaa9-3a44-3903-8d0d-550444399a29 | -22.59307 | -51.88914 | 2025-09-11 04:00:00 | NOAA-21 | SANDOVALINA | SÃO PAULO | Brasil | 3545506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.6 |
| 84df834c-3498-3fea-9589-d3fc36f42664 | -23.75417 | -51.79028 | 2025-09-11 04:00:00 | NOAA-21 | BOM SUCESSO | PARANÁ | Brasil | 4103206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| 4ca80be6-0694-327d-abe6-7add7b5fc578 | -21.12384 | -47.73025 | 2025-09-11 04:00:00 | NOAA-21 | RIBEIRÃO PRETO | SÃO PAULO | Brasil | 3543402 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ba60c41f-315c-382b-acf0-5b457568c71d | -23.63914 | -51.67238 | 2025-09-11 04:00:00 | NOAA-21 | JANDAIA DO SUL | PARANÁ | Brasil | 4112108 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| c1447b01-0208-3a5b-8bd2-0d3271eccf5b | -23.308 | -47.34356 | 2025-09-11 04:00:00 | NOAA-21 | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 8d1b1e21-f457-3baf-9669-030b86ea2336 | -22.87735 | -48.53413 | 2025-09-11 04:00:00 | NOAA-21 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3d13a56d-e776-3b78-828c-258fd1b05c16 | -21.52592 | -43.88293 | 2025-09-11 04:00:00 | NOAA-21 | SANTA RITA DE IBITIPOCA | MINAS GERAIS | Brasil | 3159407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| e36a9924-b351-3b41-9152-8080552df0ba | -20.89223 | -48.45988 | 2025-09-11 04:00:00 | NOAA-21 | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 25453dd2-e6f4-3737-9826-ebba84f1c55f | -22.82703 | -46.43039 | 2025-09-11 04:00:00 | NOAA-21 | VARGEM | SÃO PAULO | Brasil | 3556354 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 7fc506e5-d821-3e35-8611-8b3b8edcf1cf | -21.52865 | -43.8875 | 2025-09-11 04:00:00 | NOAA-21 | SANTA RITA DE IBITIPOCA | MINAS GERAIS | Brasil | 3159407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| c4e227fc-d05f-3465-a51f-ee47f46258c8 | -22.5629 | -46.04254 | 2025-09-11 04:00:00 | NOAA-21 | CAMBUÍ | MINAS GERAIS | Brasil | 3110608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 05bc5781-c4cd-3dae-88b5-e8c749e2b3c8 | -22.79636 | -47.80935 | 2025-09-11 04:00:00 | NOAA-21 | PIRACICABA | SÃO PAULO | Brasil | 3538709 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f8007682-4948-3956-b946-d28e14de4de0 | -20.91649 | -49.46912 | 2025-09-11 04:00:00 | NOAA-21 | BADY BASSITT | SÃO PAULO | Brasil | 3504602 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.1 |
| 6aba8f7c-ed0f-3575-ae18-f8d6274566ea | -23.34455 | -47.21497 | 2025-09-11 04:00:00 | NOAA-21 | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| 9b1f08c0-de75-34c8-8ea5-fe719cbe730c | -21.45723 | -45.14108 | 2025-09-11 04:00:00 | NOAA-21 | CARMO DA CACHOEIRA | MINAS GERAIS | Brasil | 3113909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| a761c499-6ef4-35f2-a363-16cab345725a | -23.33239 | -47.32104 | 2025-09-11 04:00:00 | NOAA-21 | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| e1c81462-0c26-34f3-af21-e2ce61f35b6a | -22.59461 | -51.88228 | 2025-09-11 04:00:00 | NOAA-21 | SANDOVALINA | SÃO PAULO | Brasil | 3545506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 15.2 |
| 736a08ea-11a5-3739-b5fc-a492029ea3e1 | -21.43644 | -48.91567 | 2025-09-11 04:00:00 | NOAA-21 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 3206e16d-e6e1-317a-be6c-0ecfe2cdadd0 | -22.59319 | -51.88468 | 2025-09-11 04:00:00 | NOAA-21 | SANDOVALINA | SÃO PAULO | Brasil | 3545506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.1 |
| 33277d20-37cd-32c9-9992-be6c2efe3311 | -23.34554 | -47.20974 | 2025-09-11 04:00:00 | NOAA-21 | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| 365f5af0-5b18-3dad-8794-cee56ae60414 | -24.1992 | -51.76159 | 2025-09-11 04:00:00 | NOAA-21 | JARDIM ALEGRE | PARANÁ | Brasil | 4112504 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| ad8b2f24-3f05-36b0-9fd8-68ce002bea5a | -22.66513 | -53.12658 | 2025-09-11 04:00:00 | NOAA-21 | SÃO PEDRO DO PARANÁ | PARANÁ | Brasil | 4125902 | 41 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| 22ace940-8fc6-3b6a-a3a8-f9490be2d966 | -22.59893 | -51.8872 | 2025-09-11 04:00:00 | NOAA-21 | SANDOVALINA | SÃO PAULO | Brasil | 3545506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.6 |
| 96bea1c7-27ce-3ed9-adb8-e901bc35e6da | -21.52527 | -43.88683 | 2025-09-11 04:00:00 | NOAA-21 | SANTA RITA DE IBITIPOCA | MINAS GERAIS | Brasil | 3159407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| c73b6c36-b17d-3fab-a0d7-2ca481ac114d | -22.59608 | -51.89642 | 2025-09-11 04:00:00 | NOAA-21 | SANDOVALINA | SÃO PAULO | Brasil | 3545506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.7 |
| 37dfd36e-a9b1-3dce-9523-5aaf44b34a6c | -23.47588 | -46.20605 | 2025-09-11 04:00:00 | NOAA-21 | MOGI DAS CRUZES | SÃO PAULO | Brasil | 3530607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 20790b74-8945-39bf-87cc-0e850543dd3c | -24.19422 | -51.76053 | 2025-09-11 04:00:00 | NOAA-21 | JARDIM ALEGRE | PARANÁ | Brasil | 4112504 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| e1168fc1-23fc-3792-8691-9b250efe83af | -21.30037 | -45.95517 | 2025-09-11 04:00:00 | NOAA-21 | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 2fffe3b7-0a79-3456-8cee-70205df11802 | -23.41969 | -46.14026 | 2025-09-11 04:00:00 | NOAA-21 | GUARAREMA | SÃO PAULO | Brasil | 3518305 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 613ccfff-6770-35a1-be50-ca9d27946b88 | -20.8914 | -48.46418 | 2025-09-11 04:00:00 | NOAA-21 | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Cerrado | 5.9 |
| d10971d4-26a6-3152-ad91-591a4a1a5a65 | -23.4722 | -46.20555 | 2025-09-11 04:00:00 | NOAA-21 | MOGI DAS CRUZES | SÃO PAULO | Brasil | 3530607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 2c910cd0-a0cb-31cc-9537-bc982d64b31f | -23.33435 | -47.31074 | 2025-09-11 04:00:00 | NOAA-21 | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| dc55c34b-63a3-33d3-bd61-4609d8efcaa9 | -21.64681 | -45.53643 | 2025-09-11 04:00:00 | NOAA-21 | ELÓI MENDES | MINAS GERAIS | Brasil | 3123601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 91ad2fbb-0e15-3c8d-8605-d1083cdab479 | -22.52664 | -45.08636 | 2025-09-11 04:00:00 | NOAA-21 | CRUZEIRO | SÃO PAULO | Brasil | 3513405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| e1259885-19f4-3eca-878f-467375ebe1d6 | -22.84212 | -47.46645 | 2025-09-11 04:00:00 | NOAA-21 | SANTA BÁRBARA D'OESTE | SÃO PAULO | Brasil | 3545803 | 35 | 33 | nan | nan | nan | Mata Atlântica | 13.2 |
| 94d9d264-8c7a-3310-93ad-c3af9c88986c | -22.59394 | -51.88123 | 2025-09-11 04:00:00 | NOAA-21 | SANDOVALINA | SÃO PAULO | Brasil | 3545506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| 6e9708c2-881f-3748-81fd-5ce10363b005 | -21.5028 | -45.50037 | 2025-09-11 04:00:00 | NOAA-21 | TRÊS PONTAS | MINAS GERAIS | Brasil | 3169406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| dbeced24-2403-3ec0-bc29-1f91f00d381b | -24.47591 | -50.81039 | 2025-09-11 04:00:00 | NOAA-21 | RESERVA | PARANÁ | Brasil | 4121703 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 4639576a-79a9-3e47-bd40-88592ccf0b47 | -24.19852 | -51.76468 | 2025-09-11 04:00:00 | NOAA-21 | JARDIM ALEGRE | PARANÁ | Brasil | 4112504 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| af345694-0dce-31e2-a5b7-610ea5444022 | -23.23139 | -46.69361 | 2025-09-11 04:00:00 | NOAA-21 | ATIBAIA | SÃO PAULO | Brasil | 3504107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| fec7c04d-aa6b-3165-a78d-5cf0099c79ed | -22.16321 | -47.6855 | 2025-09-11 04:00:00 | NOAA-21 | ANALÂNDIA | SÃO PAULO | Brasil | 3502002 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 08cea50a-54aa-3224-a4c5-12b6c39f986b | -20.48351 | -49.73028 | 2025-09-11 04:00:00 | NOAA-21 | COSMORAMA | SÃO PAULO | Brasil | 3512902 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6566c4ad-b71c-3035-8796-cd9721b5b171 | -23.23231 | -46.68868 | 2025-09-11 04:00:00 | NOAA-21 | ATIBAIA | SÃO PAULO | Brasil | 3504107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 4816921c-fbaf-3676-b255-533a55c3d7d4 | -22.66879 | -53.12876 | 2025-09-11 04:00:00 | NOAA-21 | SÃO PEDRO DO PARANÁ | PARANÁ | Brasil | 4125902 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| e5e77d7c-36a0-313d-adc3-93de1d1fd0aa | -22.83827 | -47.46943 | 2025-09-11 04:00:00 | NOAA-21 | SANTA BÁRBARA D'OESTE | SÃO PAULO | Brasil | 3545803 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.5 |
| 797779d8-3df6-3b6a-a479-1673d2a735d3 | -23.77354 | -49.05039 | 2025-09-11 04:00:00 | NOAA-21 | ITABERÁ | SÃO PAULO | Brasil | 3521705 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1963c087-2ad4-32e9-94d0-917970332d9e | -22.84028 | -47.45863 | 2025-09-11 04:00:00 | NOAA-21 | SANTA BÁRBARA D'OESTE | SÃO PAULO | Brasil | 3545803 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 13d1ff0a-fb24-3671-98dd-9fc9ec59f284 | -21.44044 | -45.34117 | 2025-09-11 04:00:00 | NOAA-21 | TRÊS PONTAS | MINAS GERAIS | Brasil | 3169406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| f262961c-7f80-3088-a22a-e6180be7b3cf | -21.91766 | -47.90938 | 2025-09-11 04:00:00 | NOAA-21 | SÃO CARLOS | SÃO PAULO | Brasil | 3548906 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 34841484-7a81-376a-bc2f-21adc3be7936 | -20.93487 | -45.79144 | 2025-09-11 04:00:00 | NOAA-21 | ILICÍNEA | MINAS GERAIS | Brasil | 3130507 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d8cfad67-edf5-398c-a98e-0989dbf83448 | -23.59842 | -46.96997 | 2025-09-11 04:00:00 | NOAA-21 | ITAPEVI | SÃO PAULO | Brasil | 3522505 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 4334f1af-4456-3833-8f52-19b4cb4cd509 | -21.10843 | -45.07247 | 2025-09-11 04:00:00 | NOAA-21 | RIBEIRÃO VERMELHO | MINAS GERAIS | Brasil | 3154705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| b5a204be-2d30-30a8-8321-e76b55196fff | -22.58587 | -51.89346 | 2025-09-11 04:00:00 | NOAA-21 | SANDOVALINA | SÃO PAULO | Brasil | 3545506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 3fdf4697-8f1d-352e-8799-ceb75a8723dd | -22.59078 | -51.89939 | 2025-09-11 04:00:00 | NOAA-21 | SANDOVALINA | SÃO PAULO | Brasil | 3545506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 20.9 |
| ebefb9aa-4c96-344c-8ff4-c20e0fdff83f | -22.59155 | -51.89598 | 2025-09-11 04:00:00 | NOAA-21 | SANDOVALINA | SÃO PAULO | Brasil | 3545506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.2 |
| db4f35f8-8ddf-39b7-9e46-37334372e6ef | -21.43904 | -43.85511 | 2025-09-11 04:00:00 | NOAA-21 | IBERTIOGA | MINAS GERAIS | Brasil | 3129400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 5fc638c2-90ae-39f7-939b-4251e161c0bd | -23.5976 | -46.9722 | 2025-09-11 04:00:00 | NOAA-21 | ITAPEVI | SÃO PAULO | Brasil | 3522505 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 4a550cbf-cae6-363c-8302-f05848b5b319 | -22.59023 | -51.89842 | 2025-09-11 04:00:00 | NOAA-21 | SANDOVALINA | SÃO PAULO | Brasil | 3545506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 13.8 |
| d826f90d-dd2d-341b-9393-c75f300a52cd | -22.79237 | -47.80847 | 2025-09-11 04:00:00 | NOAA-21 | PIRACICABA | SÃO PAULO | Brasil | 3538709 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0986d721-3b4c-3a3f-b82d-3d7b829f115d | -22.92877 | -48.38343 | 2025-09-11 04:00:00 | NOAA-21 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 21.2 |
| eee4dfab-2503-38fb-924a-b9ff87399290 | -24.51745 | -49.79359 | 2025-09-11 04:00:00 | NOAA-21 | PIRAÍ DO SUL | PARANÁ | Brasil | 4119400 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 8f65bbe8-849f-38db-adcd-d1660db69805 | -22.32059 | -48.82551 | 2025-09-11 04:00:00 | NOAA-21 | PEDERNEIRAS | SÃO PAULO | Brasil | 3536703 | 35 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 809ebdeb-d456-3a8c-a36a-a871a4b9de30 | -24.5218 | -49.79467 | 2025-09-11 04:00:00 | NOAA-21 | PIRAÍ DO SUL | PARANÁ | Brasil | 4119400 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| fcd03fa4-f6f1-3d2a-b451-6c51628f3748 | -21.29668 | -45.95436 | 2025-09-11 04:00:00 | NOAA-21 | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| e20b7823-0ad7-341a-a847-c9e59dd64400 | -22.59903 | -51.88274 | 2025-09-11 04:00:00 | NOAA-21 | SANDOVALINA | SÃO PAULO | Brasil | 3545506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| 2bd86d02-eb40-3c2e-887d-05beee5dd63e | -21.77415 | -50.83808 | 2025-09-11 04:00:00 | NOAA-21 | PARAPUÃ | SÃO PAULO | Brasil | 3536000 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| 965aa64d-c420-3478-b6d7-168f01445712 | -21.0008 | -46.05408 | 2025-09-11 04:00:00 | NOAA-21 | CARMO DO RIO CLARO | MINAS GERAIS | Brasil | 3114402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 07e2d874-a0f8-380f-bfdd-a86371f2274e | -23.74844 | -51.79238 | 2025-09-11 04:00:00 | NOAA-21 | BOM SUCESSO | PARANÁ | Brasil | 4103206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 21.4 |
| 7d7b9860-d617-326b-a548-180aa54dcdb1 | -22.82043 | -47.03946 | 2025-09-11 04:00:00 | NOAA-21 | CAMPINAS | SÃO PAULO | Brasil | 3509502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| f686ee6e-f33c-3dc5-808b-f4564107c4d4 | -22.69992 | -46.82047 | 2025-09-11 04:00:00 | NOAA-21 | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 3128cb14-27c4-3fa3-b891-f3123d5d9ef6 | -22.27042 | -44.88325 | 2025-09-11 04:00:00 | NOAA-21 | ITANHANDU | MINAS GERAIS | Brasil | 3133105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 47b72e11-239a-3aad-857f-f77964e844a0 | -23.63842 | -51.67559 | 2025-09-11 04:00:00 | NOAA-21 | JANDAIA DO SUL | PARANÁ | Brasil | 4112108 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| d870391d-0687-32c1-8071-aa9a018f7aea | -22.83927 | -47.46403 | 2025-09-11 04:00:00 | NOAA-21 | SANTA BÁRBARA D'OESTE | SÃO PAULO | Brasil | 3545803 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 2c45cb46-1a46-3fdc-a254-7b1cd9f12861 | -23.33337 | -47.31589 | 2025-09-11 04:00:00 | NOAA-21 | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 74dff166-87d2-329a-8291-23753b915149 | -21.84229 | -48.08909 | 2025-09-11 04:00:00 | NOAA-21 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ad9c2ad3-5ee4-3ea7-8fa7-c16a98c451e0 | -22.34438 | -41.78438 | 2025-09-11 04:00:00 | NOAA-21 | MACAÉ | RIO DE JANEIRO | Brasil | 3302403 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 429d3def-7622-39bd-85b5-463bbcb26e55 | -23.25379 | -45.97517 | 2025-09-11 04:00:00 | NOAA-21 | JACAREÍ | SÃO PAULO | Brasil | 3524402 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 36e901a2-fb0c-3669-8762-fe29607caea0 | -23.74771 | -51.7957 | 2025-09-11 04:00:00 | NOAA-21 | BOM SUCESSO | PARANÁ | Brasil | 4103206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 14.3 |
| 6715ada2-99dc-3d56-a819-2a5518fb9ce5 | -23.3552 | -47.20085 | 2025-09-11 04:00:00 | NOAA-21 | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| c6929981-f212-37b7-91a3-da70140ba2da | -23.63437 | -51.67203 | 2025-09-11 04:00:00 | NOAA-21 | JANDAIA DO SUL | PARANÁ | Brasil | 4112108 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 85f8bf64-a834-3446-86ab-c0f4097b27ad | -22.58663 | -51.88998 | 2025-09-11 04:00:00 | NOAA-21 | SANDOVALINA | SÃO PAULO | Brasil | 3545506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 4e5f02d3-b4ac-31d7-8cc7-8fdc4092c996 | -21.91359 | -47.90842 | 2025-09-11 04:00:00 | NOAA-21 | SÃO CARLOS | SÃO PAULO | Brasil | 3548906 | 35 | 33 | nan | nan | nan | Cerrado | 5.1 |
| f4432d5c-78d6-31d6-a1da-d1c3a47e652c | -22.84119 | -47.47562 | 2025-09-11 04:00:00 | NOAA-21 | SANTA BÁRBARA D'OESTE | SÃO PAULO | Brasil | 3545803 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.1 |
| 0461e88d-6330-31c4-893e-db31e38ac55d | -22.79313 | -47.80452 | 2025-09-11 04:00:00 | NOAA-21 | PIRACICABA | SÃO PAULO | Brasil | 3538709 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2cbb8832-6536-3f16-a54d-017aea5ef522 | -20.89092 | -48.30536 | 2025-09-11 04:00:00 | NOAA-21 | VIRADOURO | SÃO PAULO | Brasil | 3556800 | 35 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2461f885-d7f2-3399-8e68-c06070574079 | -23.38836 | -46.85827 | 2025-09-11 04:00:00 | NOAA-21 | CAJAMAR | SÃO PAULO | Brasil | 3509205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 00cc16a5-3420-3f4b-b071-698bf109bf75 | -22.59742 | -51.89399 | 2025-09-11 04:00:00 | NOAA-21 | SANDOVALINA | SÃO PAULO | Brasil | 3545506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.2 |
| 5d44fa44-54ed-3158-8912-c19c9ab9eb28 | -23.36957 | -47.20921 | 2025-09-11 04:00:00 | NOAA-21 | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| b904f5f6-e455-3dff-ab24-236ed2cf9d7d | -22.84108 | -47.47182 | 2025-09-11 04:00:00 | NOAA-21 | SANTA BÁRBARA D'OESTE | SÃO PAULO | Brasil | 3545803 | 35 | 33 | nan | nan | nan | Mata Atlântica | 13.2 |
| 666d0d6a-1b2d-3609-8aaa-2279ee97111b | -21.06559 | -46.15023 | 2025-09-11 04:00:00 | NOAA-21 | CONCEIÇÃO DA APARECIDA | MINAS GERAIS | Brasil | 3117108 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 303fc3eb-0304-3dfc-a30d-f3841505e363 | -22.79288 | -45.62078 | 2025-09-11 04:00:00 | NOAA-21 | CAMPOS DO JORDÃO | SÃO PAULO | Brasil | 3509700 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| c7f91a24-852a-37e5-bd15-266894497994 | -22.58513 | -51.89692 | 2025-09-11 04:00:00 | NOAA-21 | SANDOVALINA | SÃO PAULO | Brasil | 3545506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| cfd219ae-72ff-3844-9fe8-a772af12790a | -23.75345 | -51.79355 | 2025-09-11 04:00:00 | NOAA-21 | BOM SUCESSO | PARANÁ | Brasil | 4103206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| 30966747-71f0-308b-a1cc-af6829b14187 | -22.58949 | -51.90185 | 2025-09-11 04:00:00 | NOAA-21 | SANDOVALINA | SÃO PAULO | Brasil | 3545506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 13.8 |
| 89826c18-0115-38c7-a051-d7cf7f6a3886 | -23.76934 | -49.04928 | 2025-09-11 04:00:00 | NOAA-21 | ITABERÁ | SÃO PAULO | Brasil | 3521705 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4f533427-db13-33d5-ad41-67cf83446019 | -22.52363 | -49.08853 | 2025-09-11 04:00:00 | NOAA-21 | AGUDOS | SÃO PAULO | Brasil | 3500709 | 35 | 33 | nan | nan | nan | Cerrado | 4.1 |
| b07c466d-ecc9-3b20-a292-8d508479c3ae | -22.59245 | -51.88811 | 2025-09-11 04:00:00 | NOAA-21 | SANDOVALINA | SÃO PAULO | Brasil | 3545506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.1 |
| a716bf23-4a87-3a8d-9b4f-64e26208b985 | -22.53012 | -45.08714 | 2025-09-11 04:00:00 | NOAA-21 | CRUZEIRO | SÃO PAULO | Brasil | 3513405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 842d26b8-0f83-33ac-b91f-ff26d77fa054 | -24.47316 | -50.81185 | 2025-09-11 04:00:00 | NOAA-21 | RESERVA | PARANÁ | Brasil | 4121703 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |


[Clique aqui para ver as próximas entradas](README39.md)
