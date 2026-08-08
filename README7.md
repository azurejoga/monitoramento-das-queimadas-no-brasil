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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8e5b4ae6-5f43-32eb-ae21-d608439428fd | -14.92985 | -48.25344 | 2026-08-08 03:51:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 7ec50cac-b7cb-3c47-8152-da20188bc76c | -18.38871 | -50.68974 | 2026-08-08 03:51:00 | NOAA-21 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 37.8 |
| 632286c0-bacb-3b36-bab5-fe906e28355e | -15.16602 | -52.75019 | 2026-08-08 03:51:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| ab60fc87-422d-35de-b9f5-e2f49ca91e78 | -15.67237 | -48.26447 | 2026-08-08 03:51:00 | NOAA-21 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3f771a12-9e48-330f-8511-a249ab4e82d1 | -13.95474 | -41.87307 | 2026-08-08 03:51:00 | NOAA-21 | LIVRAMENTO DE NOSSA SENHORA | BAHIA | Brasil | 2919504 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| b8ced4e1-d3eb-3789-8587-c81505777a91 | -19.96546 | -40.60779 | 2026-08-08 03:51:00 | NOAA-21 | SANTA MARIA DE JETIBÁ | ESPÍRITO SANTO | Brasil | 3204559 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 647cae58-fbb9-3eec-8dcb-6d88bd11853d | -14.27797 | -45.28859 | 2026-08-08 03:51:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e53d7432-712d-3bf4-8281-df404c6dd163 | -14.42149 | -45.658 | 2026-08-08 03:51:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f25d6d68-d30c-3aff-948a-e4d7b6e95bc4 | -20.24115 | -46.90556 | 2026-08-08 03:51:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 699cebed-efe0-3790-b03e-037c01efc553 | -17.84047 | -44.49416 | 2026-08-08 03:51:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ac77aaf8-7ee3-323f-9a33-bc40a480bd3a | -15.15944 | -52.74735 | 2026-08-08 03:51:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 430c91e4-096f-38e6-b937-943cc9622dcc | -17.88793 | -50.51896 | 2026-08-08 03:51:00 | NOAA-21 | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 884600af-3598-38d0-9f0f-186019f2d224 | -18.36939 | -50.69528 | 2026-08-08 03:51:00 | NOAA-21 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3a2d6747-6cef-33d6-8d5a-e2bcd92481b2 | -14.93949 | -48.26038 | 2026-08-08 03:51:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 83d20d27-21a9-3bfb-af20-6f1892720e85 | -20.54773 | -41.3201 | 2026-08-08 03:51:00 | NOAA-21 | CASTELO | ESPÍRITO SANTO | Brasil | 3201407 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| fae85e8b-42af-3867-ba62-67bbc755dc1b | -20.23677 | -46.90457 | 2026-08-08 03:51:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4f2984a8-5e0b-33e6-b645-28effbd2124d | -15.16107 | -52.74012 | 2026-08-08 03:51:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 497a1659-6d12-37a0-9902-666f80baf7c9 | -14.92514 | -48.24942 | 2026-08-08 03:51:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 22dffa13-ddb2-347d-8902-b8d9fc5230b2 | -18.3495 | -50.73107 | 2026-08-08 03:51:00 | NOAA-21 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 1c342a1c-67d6-3d2e-bb54-2edee00c8ba8 | -18.36183 | -50.70221 | 2026-08-08 03:51:00 | NOAA-21 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 6245ae54-ea6f-3282-af18-aca36ef9bdde | -20.44423 | -43.70533 | 2026-08-08 03:51:00 | NOAA-21 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 96f15639-70de-3191-b7ab-7c13f458190b | -17.88458 | -43.77634 | 2026-08-08 03:51:00 | NOAA-21 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 45b17664-f5d2-3759-ad65-a34b5ab2663d | -15.39748 | -44.22534 | 2026-08-08 03:51:00 | NOAA-21 | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 8a025e9d-d343-3e71-a847-e429a856ef2e | -17.3041 | -42.66357 | 2026-08-08 03:51:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 1134d95d-ed5e-3748-bf5a-32d579140e23 | -18.36003 | -50.7105 | 2026-08-08 03:51:00 | NOAA-21 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 17.0 |
| fa8f979d-96b1-3ca9-9ca5-72fc44a5a74c | -20.05989 | -40.88654 | 2026-08-08 03:51:00 | NOAA-21 | SANTA MARIA DE JETIBÁ | ESPÍRITO SANTO | Brasil | 3204559 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| fb51e92b-c956-3462-9661-3386e465a272 | -20.17499 | -43.69558 | 2026-08-08 03:51:00 | NOAA-21 | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 894289c6-366a-34f1-948e-5caa9903cca3 | -18.21664 | -44.35982 | 2026-08-08 03:51:00 | NOAA-21 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 4c7d3929-23eb-3e2a-be78-05d90f21f1ec | -20.36573 | -41.16342 | 2026-08-08 03:51:00 | NOAA-21 | VENDA NOVA DO IMIGRANTE | ESPÍRITO SANTO | Brasil | 3205069 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 7660a3d5-28fc-3188-a502-af3ae5bdd574 | -18.35723 | -50.72341 | 2026-08-08 03:51:00 | NOAA-21 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 28.2 |
| 84fabf21-dab5-31f6-aafa-90b774cf1ff0 | -20.27325 | -41.78881 | 2026-08-08 03:51:00 | NOAA-21 | MARTINS SOARES | MINAS GERAIS | Brasil | 3140530 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| a313266d-9826-35f2-8482-c1e2b9b9dd32 | -20.19052 | -40.28138 | 2026-08-08 03:51:00 | NOAA-21 | SERRA | ESPÍRITO SANTO | Brasil | 3205002 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| a51e47cc-7137-3731-abd0-3875a50028a5 | -14.41898 | -45.6647 | 2026-08-08 03:51:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 0b147bf3-e48d-3eaf-9444-9a68fe42d3ec | -20.04914 | -44.05559 | 2026-08-08 03:51:00 | NOAA-21 | IBIRITÉ | MINAS GERAIS | Brasil | 3129806 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 5a2cd514-85e5-3b07-9dc4-cf90b1eaf409 | -14.27439 | -45.2833 | 2026-08-08 03:51:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 18a94342-8b52-3772-9dff-bf3fce7a9ec9 | -19.74764 | -43.90274 | 2026-08-08 03:51:00 | NOAA-21 | SANTA LUZIA | MINAS GERAIS | Brasil | 3157807 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 787403e1-90f1-3ea7-963e-0e36caf184ef | -14.90132 | -47.74468 | 2026-08-08 03:51:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b4ae0be6-f1f3-3ef7-9eba-54d1f7797ec8 | -20.54714 | -41.32372 | 2026-08-08 03:51:00 | NOAA-21 | CASTELO | ESPÍRITO SANTO | Brasil | 3201407 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| e1f298af-ca33-3a21-8b8d-3f0dd2322768 | -18.35241 | -50.71766 | 2026-08-08 03:51:00 | NOAA-21 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 22c07b83-026b-3ad4-bc99-06637e1dcfab | -19.95595 | -40.17262 | 2026-08-08 03:51:00 | NOAA-21 | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| d78df478-705a-3f11-9aaa-2b11e95fce04 | -18.35335 | -50.71333 | 2026-08-08 03:51:00 | NOAA-21 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| eeceb91d-8a1e-3407-8834-d6fa7f249895 | -15.70986 | -42.18618 | 2026-08-08 03:51:00 | NOAA-21 | INDAIABIRA | MINAS GERAIS | Brasil | 3130655 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 20a04988-ebc0-3466-9793-600e93e38e23 | -19.643 | -46.206 | 2026-08-08 03:51:00 | NOAA-21 | CAMPOS ALTOS | MINAS GERAIS | Brasil | 3111507 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| dcec0c93-d412-38bf-9124-b6cdb6798787 | -14.27356 | -45.28773 | 2026-08-08 03:51:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 826df2ff-e137-3b3d-b462-37e4857f053e | -18.3951 | -50.6883 | 2026-08-08 03:51:00 | NOAA-21 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 42.1 |
| 8a41ac43-097a-3eb7-8e37-05bc5c58937b | -14.42511 | -45.66356 | 2026-08-08 03:51:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 0c93390a-1f4f-3dea-a827-326b61c0e954 | -18.39265 | -50.69927 | 2026-08-08 03:51:00 | NOAA-21 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 23.4 |
| 10b609e8-849a-3971-8802-b37c116f1033 | -18.72381 | -39.76957 | 2026-08-08 03:51:00 | NOAA-21 | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 4e692498-f043-390b-ae22-0be4fb7924e1 | -14.93809 | -48.26736 | 2026-08-08 03:51:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 7d229e0a-adcb-30cd-a72f-05eee0a26aaf | -20.24208 | -46.90081 | 2026-08-08 03:51:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a9cba845-3324-3584-bcc1-d23b83b5f505 | -16.6883 | -51.3458 | 2026-08-08 03:51:00 | NOAA-21 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 34c58eee-55cc-3015-a804-02d3eee086b2 | -15.94025 | -48.31166 | 2026-08-08 03:51:00 | NOAA-21 | SANTO ANTÔNIO DO DESCOBERTO | GOIÁS | Brasil | 5219753 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 3ace2ad1-20ad-3914-9e02-33bdaba1cd52 | -18.3685 | -50.69939 | 2026-08-08 03:51:00 | NOAA-21 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 72be5ff3-6ee4-3ffa-a22f-1d4dd30b6471 | -18.38935 | -50.6869 | 2026-08-08 03:51:00 | NOAA-21 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 42.1 |
| d590fb54-560e-3506-b599-8f419fa2d2a6 | -19.74682 | -40.05351 | 2026-08-08 03:51:00 | NOAA-21 | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 7ff6f648-0509-307f-a569-5615e55f8847 | -14.41608 | -45.6618 | 2026-08-08 03:51:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| d771754b-2aae-300a-891b-fa5e79994dd4 | -19.93846 | -41.38617 | 2026-08-08 03:51:00 | NOAA-21 | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| f9b15099-2d72-3854-a41f-263fb56deb7d | -14.41971 | -45.66735 | 2026-08-08 03:51:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 145086a7-ae98-3ea7-b1ec-c67a68187862 | -14.93285 | -48.26597 | 2026-08-08 03:51:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 85319a21-a9af-33f9-afe7-f5efe6544463 | -18.35628 | -50.72776 | 2026-08-08 03:51:00 | NOAA-21 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 28.2 |
| 64e37f4a-7a12-3ab6-9919-fded191642ad | -20.84916 | -42.23525 | 2026-08-08 03:51:00 | NOAA-21 | VIEIRAS | MINAS GERAIS | Brasil | 3171402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 78b2fd93-786f-3016-a514-8f41c9c34a86 | -18.39539 | -50.68697 | 2026-08-08 03:51:00 | NOAA-21 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 37.8 |
| 089a4b79-d5da-3d19-a5b2-e07a65cb946d | -20.27451 | -41.7812 | 2026-08-08 03:51:00 | NOAA-21 | MARTINS SOARES | MINAS GERAIS | Brasil | 3140530 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 8b2c5502-2080-3eb3-81b1-41f7303a78ad | -18.35817 | -50.71908 | 2026-08-08 03:51:00 | NOAA-21 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 29.1 |
| 413e4caa-9f20-3207-ac91-aa38c2618fc6 | -19.92154 | -40.2837 | 2026-08-08 03:51:00 | NOAA-21 | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 9d4154ab-48bd-3a94-b34b-1db57c0c0f1e | -19.74871 | -43.9055 | 2026-08-08 03:51:00 | NOAA-21 | SANTA LUZIA | MINAS GERAIS | Brasil | 3157807 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 86992db7-9d82-30e7-9ae2-a02779390ea5 | -16.87722 | -43.21526 | 2026-08-08 03:51:00 | NOAA-21 | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 23007628-50a4-3502-a074-18a08e2033ff | -16.4002 | -49.93788 | 2026-08-08 03:51:00 | NOAA-21 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3fb05fed-9d61-3d7b-a4d6-e0ea0b4f1a28 | -14.42069 | -45.65532 | 2026-08-08 03:51:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 1fd2f271-ead8-344e-a597-ed07faa535fd | -17.30486 | -42.65918 | 2026-08-08 03:51:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 24.2 |
| c2080c6a-238b-38c3-a368-b48aea416a77 | -18.39424 | -50.69233 | 2026-08-08 03:51:00 | NOAA-21 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 42.1 |
| fc1c51fe-a64e-3215-b917-01418a1e8250 | -16.68731 | -51.35033 | 2026-08-08 03:51:00 | NOAA-21 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| a298e001-fea4-3576-9fcb-872a5d9ed1e9 | -19.36421 | -40.68466 | 2026-08-08 03:51:00 | NOAA-21 | COLATINA | ESPÍRITO SANTO | Brasil | 3201506 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 9d4eb561-0a2f-35bc-b85e-da8e508b18d2 | -14.92836 | -48.26087 | 2026-08-08 03:51:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 8.4 |
| d1ed1692-9882-386a-bd03-b8ba24fae8f9 | -14.93047 | -48.25033 | 2026-08-08 03:51:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 25429266-0147-3832-a52a-1424ecc089ea | -18.38847 | -50.69099 | 2026-08-08 03:51:00 | NOAA-21 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 42.1 |
| 5becb901-3503-3aff-8da7-bc2a850dc9c9 | -14.26936 | -45.31007 | 2026-08-08 03:51:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b0468ee3-5b48-30f2-8560-960c28ff7d4f | -14.93684 | -48.24606 | 2026-08-08 03:51:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e6ecf246-8929-3981-9275-1d248be450a6 | -14.93561 | -48.25221 | 2026-08-08 03:51:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 1df28378-1ebf-3ed6-b268-078a4c5089a3 | -20.17577 | -43.69118 | 2026-08-08 03:51:00 | NOAA-21 | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 965073dc-049d-341c-88f9-88bdce763924 | -14.2788 | -45.28417 | 2026-08-08 03:51:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 010f0172-d9cc-3fad-ab6c-9f232db52bfe | -20.39187 | -42.10979 | 2026-08-08 03:51:00 | NOAA-21 | LUISBURGO | MINAS GERAIS | Brasil | 3138674 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| cb6f8087-81e9-355a-9057-9732eca01628 | -20.04778 | -44.05767 | 2026-08-08 03:51:00 | NOAA-21 | IBIRITÉ | MINAS GERAIS | Brasil | 3129806 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 3b6e1319-bb2c-3f2c-86fd-a3392740b77a | -18.36094 | -50.70633 | 2026-08-08 03:51:00 | NOAA-21 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 5a831d45-3130-3af1-8930-6a31760bb4da | -18.39606 | -50.68383 | 2026-08-08 03:51:00 | NOAA-21 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 3c8c2216-990c-3716-b447-7786caa653e7 | -15.71061 | -42.18186 | 2026-08-08 03:51:00 | NOAA-21 | INDAIABIRA | MINAS GERAIS | Brasil | 3130655 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 547b298c-2ab4-330c-a049-699c7083ab98 | -14.41519 | -45.6665 | 2026-08-08 03:51:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 740eaa18-4e16-33d1-a876-1557607b77ef | -16.44903 | -43.14733 | 2026-08-08 03:51:00 | NOAA-21 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cddbac0e-5d04-3228-8e00-6cccce774df3 | -15.70626 | -42.1856 | 2026-08-08 03:51:00 | NOAA-21 | INDAIABIRA | MINAS GERAIS | Brasil | 3130655 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 02784d1f-fd7e-3351-9dbf-6d870ae25499 | -13.65042 | -50.29826 | 2026-08-08 03:51:00 | NOAA-21 | MUNDO NOVO | GOIÁS | Brasil | 5214051 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| fa7c63e3-5e39-3784-8c56-fa397c0f5501 | -18.51044 | -48.34137 | 2026-08-08 03:51:00 | NOAA-21 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d1075f96-c565-33a1-aa17-a310c1c76a97 | -15.15359 | -52.74261 | 2026-08-08 03:51:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 2274c6a5-2ff2-3c65-bd61-4475b3f9f480 | -18.37145 | -39.95549 | 2026-08-08 03:51:00 | NOAA-21 | PINHEIROS | ESPÍRITO SANTO | Brasil | 3204104 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 7834ff6a-536f-3fdc-9745-5bd76c1b47e0 | -14.92445 | -48.25288 | 2026-08-08 03:51:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 9bfe3101-2101-3f68-9108-bf06ad28d123 | -14.4206 | -45.66267 | 2026-08-08 03:51:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 211978b4-f19a-398c-95fc-51626f4e5bbe | -15.16052 | -52.74391 | 2026-08-08 03:51:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| b3d02ede-0812-3f7d-9b92-a188d800f8d6 | -17.74668 | -42.39245 | 2026-08-08 03:51:00 | NOAA-21 | CAPELINHA | MINAS GERAIS | Brasil | 3112307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 0b0cb527-bb8c-33a4-b12c-1de3ddf46ab2 | -20.74106 | -41.09704 | 2026-08-08 03:51:00 | NOAA-21 | CACHOEIRO DE ITAPEMIRIM | ESPÍRITO SANTO | Brasil | 3201209 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| fd4c948f-3cac-3c51-b1f2-417d83fc9c19 | -15.15406 | -52.73917 | 2026-08-08 03:51:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| de1fede2-6688-3f94-933d-75b0b4e6753d | -15.79115 | -43.23508 | 2026-08-08 03:51:00 | NOAA-21 | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |


[Clique aqui para ver as próximas entradas](README8.md)
