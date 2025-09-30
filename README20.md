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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| aed7f5ae-42df-3dc6-8e83-a750b4ad9659 | -19.85624 | -43.81139 | 2025-09-30 03:30:00 | NPP-375D | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| b091d225-4031-3847-b91c-91a53267d29e | -19.85981 | -42.58758 | 2025-09-30 03:30:00 | NPP-375D | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| ca08eff3-f74a-3c0a-8df6-c5f1d15e296e | -16.42225 | -47.03981 | 2025-09-30 03:30:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7c027262-7563-3bd2-bb85-23074dcccdef | -19.85906 | -44.55035 | 2025-09-30 03:30:00 | NPP-375D | PARÁ DE MINAS | MINAS GERAIS | Brasil | 3147105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| f678f389-8e14-378f-a05e-da6c89624c5b | -21.04292 | -45.69303 | 2025-09-30 03:30:00 | NPP-375D | BOA ESPERANÇA | MINAS GERAIS | Brasil | 3107109 | 31 | 33 | nan | nan | nan | Cerrado | 6.4 |
| c32b97c6-7081-330c-bdd3-065ec72a1351 | -18.46686 | -40.56527 | 2025-09-30 03:30:00 | NPP-375D | ECOPORANGA | ESPÍRITO SANTO | Brasil | 3202108 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 8d8e49b5-2fca-3b5a-bb64-9496d59264d3 | -16.42369 | -47.0335 | 2025-09-30 03:30:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 33568b8c-33d7-3167-bf5e-d637e86e6179 | -19.84906 | -43.81812 | 2025-09-30 03:30:00 | NPP-375D | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.6 |
| d3c8989f-8880-3eb4-b04e-d0ea7b250e83 | -19.30705 | -43.81842 | 2025-09-30 03:30:00 | NPP-375D | BALDIM | MINAS GERAIS | Brasil | 3105004 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e9b3585b-0d39-3245-b048-798a9b257b47 | -15.859 | -46.23937 | 2025-09-30 03:30:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d789b166-41bd-39e3-91ae-f8d4a3bdc0c2 | -15.8514 | -46.24321 | 2025-09-30 03:30:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 51b7e678-1c70-3b33-b39c-4f180f2a5df3 | -21.21897 | -47.13469 | 2025-09-30 03:30:00 | NPP-375D | CÁSSIA DOS COQUEIROS | SÃO PAULO | Brasil | 3510906 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| eb5c5465-3ef2-3126-bd7f-9241839a2322 | -19.59975 | -45.89808 | 2025-09-30 03:30:00 | NPP-375D | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 84fa6dc7-d84f-39de-a7c9-d7b350e96863 | -20.60798 | -46.19072 | 2025-09-30 03:30:00 | NPP-375D | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e706ad25-57ca-39ef-ad1f-d2b31a611d96 | -16.41346 | -47.04597 | 2025-09-30 03:30:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e2cfa26e-d47c-314c-996e-9c262c919940 | -15.90455 | -46.22877 | 2025-09-30 03:30:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9a8b0e9d-18b3-38f3-8185-e3f2291bc49f | -17.38866 | -47.16001 | 2025-09-30 03:30:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 40953a70-b477-3569-b0db-87b54f761c8b | -19.86072 | -43.81726 | 2025-09-30 03:30:00 | NPP-375D | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 64e5b74d-2022-38a6-b863-494ce8499026 | -19.85916 | -42.59069 | 2025-09-30 03:30:00 | NPP-375D | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.5 |
| a2b25b8d-0558-3734-872a-4848ed38d01d | -18.47644 | -44.02049 | 2025-09-30 03:30:00 | NPP-375D | SANTO HIPÓLITO | MINAS GERAIS | Brasil | 3160603 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 3d8ae3f0-1435-31c7-b9a8-a4bd755e562f | -18.12375 | -42.19595 | 2025-09-30 03:30:00 | NPP-375D | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 964d97b2-10d6-3aca-b4e6-5f594afbb78b | -15.37361 | -47.07846 | 2025-09-30 03:30:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d2d2bf7e-4987-391e-9c3f-234b10a78fb9 | -21.04281 | -45.68571 | 2025-09-30 03:30:00 | NPP-375D | BOA ESPERANÇA | MINAS GERAIS | Brasil | 3107109 | 31 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 9fd32bf9-aa03-3107-9ed1-42cbb8e5aabd | -20.22877 | -41.34393 | 2025-09-30 03:30:00 | NPP-375D | BREJETUBA | ESPÍRITO SANTO | Brasil | 3201159 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 06685f9a-f44b-38cc-abf7-0f66846ef05c | -15.85774 | -46.24502 | 2025-09-30 03:30:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| cc2b92cb-53ce-3657-be79-e30bc40c2112 | -19.85538 | -43.81542 | 2025-09-30 03:30:00 | NPP-375D | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| 67a36c66-ed77-368f-8fb1-dc4df38f07d7 | -18.46723 | -40.56831 | 2025-09-30 03:30:00 | NPP-375D | ECOPORANGA | ESPÍRITO SANTO | Brasil | 3202108 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 00c4e317-6028-392f-a567-285eda9728cc | -15.67431 | -46.2634 | 2025-09-30 03:30:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 1aa687f4-cc2d-3c5f-a835-8f8582e5c893 | -21.73997 | -44.619 | 2025-09-30 03:30:00 | NPP-375D | MINDURI | MINAS GERAIS | Brasil | 3141900 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 3365396d-7dc9-35b0-8030-f20501e0942e | -17.719 | -46.6719 | 2025-09-30 03:30:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7c74b349-7a6c-3f64-97bd-fe7e41517ab7 | -16.42058 | -47.04713 | 2025-09-30 03:30:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8ec9ffab-b7db-3d57-883d-9ebc94a29cc7 | -15.85246 | -46.23859 | 2025-09-30 03:30:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9a92d9e4-a6e5-3d92-84e8-ad6930f83b4c | -21.1609 | -43.61617 | 2025-09-30 03:30:00 | NPP-375D | BARBACENA | MINAS GERAIS | Brasil | 3105608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 0b7cb3f2-1ee4-35e2-8fbd-b7ee72c3073b | -21.22529 | -47.1368 | 2025-09-30 03:30:00 | NPP-375D | CÁSSIA DOS COQUEIROS | SÃO PAULO | Brasil | 3510906 | 35 | 33 | nan | nan | nan | Cerrado | 4.2 |
| c1f5c23b-d04d-3235-9c4c-e6c1e57928c9 | -17.39597 | -47.13911 | 2025-09-30 03:30:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 35b378f5-5e7a-3fe2-9550-fade399b1301 | -17.39233 | -47.14447 | 2025-09-30 03:30:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 3b9ba75c-209c-33dd-9d9e-2c234fa789f2 | -19.59847 | -45.88908 | 2025-09-30 03:30:00 | NPP-375D | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 704fda2d-da4f-3e50-aabd-754a2f5ce5cb | -20.60914 | -46.07346 | 2025-09-30 03:30:00 | NPP-375D | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 8.5 |
| cedaff36-9f35-34af-9def-4e109b381259 | -19.85075 | -43.80692 | 2025-09-30 03:30:00 | NPP-375D | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 6cf1b7a6-a86e-3550-9543-62053aa39307 | -18.30539 | -42.89395 | 2025-09-30 03:30:00 | NPP-375D | RIO VERMELHO | MINAS GERAIS | Brasil | 3156007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| e071f685-99f6-3a4b-9cbd-2f6fc0174c52 | -20.04621 | -41.32521 | 2025-09-30 03:30:00 | NPP-375D | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 29ea90af-1a94-3845-930a-f17f0e939f9c | -15.62446 | -46.26329 | 2025-09-30 03:30:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| be2180f0-d630-3d12-b541-a4ee74d7d141 | -20.41875 | -43.35249 | 2025-09-30 03:30:00 | NPP-375D | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 19.3 |
| 629a3987-f4b5-3f9f-a89d-91305d34306f | -21.61835 | -44.06061 | 2025-09-30 03:30:00 | NPP-375D | SANTANA DO GARAMBÉU | MINAS GERAIS | Brasil | 3158706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 43ee1d97-feb9-39ea-91c5-c9021c233372 | -21.88858 | -45.75647 | 2025-09-30 03:30:00 | NPP-375D | TURVOLÂNDIA | MINAS GERAIS | Brasil | 3169802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 610eeb65-0ca5-31ac-9a50-cc0db65132be | -15.91724 | -46.20412 | 2025-09-30 03:30:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1dca574c-7e8a-3b39-a9a0-bbc6d3289b49 | -16.41063 | -47.04519 | 2025-09-30 03:30:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| b4df5b6d-8325-3eb1-9dc6-5d3623d0f169 | -15.68234 | -46.25954 | 2025-09-30 03:30:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7dda1953-4929-3098-930b-ad255bd0b171 | -15.87306 | -46.20817 | 2025-09-30 03:30:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7ee3ab30-2790-39bd-8302-57d3ff00d06c | -19.60078 | -45.89355 | 2025-09-30 03:30:00 | NPP-375D | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 851efff7-4b37-3f1c-a2a2-133c28a82e25 | -18.12298 | -42.19978 | 2025-09-30 03:30:00 | NPP-375D | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| fc75c2c9-0d89-3eea-837b-38fb401c2a6e | -20.95831 | -46.29561 | 2025-09-30 03:30:00 | NPP-375D | CARMO DO RIO CLARO | MINAS GERAIS | Brasil | 3114402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| bdb47e28-f2b6-3674-a5ff-e5829e5a6e48 | -17.71575 | -46.6498 | 2025-09-30 03:30:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 89796ec9-eec8-38fb-908c-dbc65d0a7995 | -18.53194 | -46.04987 | 2025-09-30 03:30:00 | NPP-375D | VARJÃO DE MINAS | MINAS GERAIS | Brasil | 3170750 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 156704c6-34ed-335b-a8df-4e6dab1c9239 | -19.60364 | -45.89497 | 2025-09-30 03:30:00 | NPP-375D | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3fc4fc48-4c56-3541-8530-f26de9152a95 | -20.32564 | -41.40304 | 2025-09-30 03:30:00 | NPP-375D | MUNIZ FREIRE | ESPÍRITO SANTO | Brasil | 3203700 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| d9583d15-44db-3e78-aa2a-66e7cd2ba7da | -21.31909 | -42.87837 | 2025-09-30 03:30:00 | NPP-375D | ASTOLFO DUTRA | MINAS GERAIS | Brasil | 3104601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 5dfc1fad-2140-3e0c-a1da-dbfb5f96b010 | -17.40983 | -47.13224 | 2025-09-30 03:30:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| ced42a8f-4552-35e4-94c2-36e629725d6a | -15.39011 | -47.07216 | 2025-09-30 03:30:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 296a4117-d3ba-3692-8421-e4f3a17d089f | -17.39261 | -47.15374 | 2025-09-30 03:30:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| afa0de14-5432-353e-a6bc-926622b20dce | -21.74089 | -44.61498 | 2025-09-30 03:30:00 | NPP-375D | MINDURI | MINAS GERAIS | Brasil | 3141900 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 9ca96b0e-b774-3bdd-931d-95aa3789a05a | -19.59636 | -43.82457 | 2025-09-30 03:30:00 | NPP-375D | LAGOA SANTA | MINAS GERAIS | Brasil | 3137601 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1e6b2bf0-9b96-3bdf-93e9-137fd30aa21e | -20.05918 | -41.33321 | 2025-09-30 03:30:00 | NPP-375D | BREJETUBA | ESPÍRITO SANTO | Brasil | 3201159 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| f5341bd7-db4d-33fb-ba10-444415842cce | -18.05806 | -43.65306 | 2025-09-30 03:30:00 | NPP-375D | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1341a184-8723-3cf8-a58f-018b95599828 | -20.61704 | -46.1952 | 2025-09-30 03:30:00 | NPP-375D | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 084a6cf0-6694-31af-a413-96f0428d6795 | -19.60106 | -43.8295 | 2025-09-30 03:30:00 | NPP-375D | LAGOA SANTA | MINAS GERAIS | Brasil | 3137601 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7bd4170f-dfa9-32e7-a6fb-54f11aab847a | -18.05513 | -43.65351 | 2025-09-30 03:30:00 | NPP-375D | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b98e0ec7-e7a9-34ae-9a47-5b47638df747 | -21.73664 | -44.61506 | 2025-09-30 03:30:00 | NPP-375D | MINDURI | MINAS GERAIS | Brasil | 3141900 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| a5ed07b3-4546-36cb-b02e-3e0f0e8383dd | -20.39225 | -43.68053 | 2025-09-30 03:30:00 | NPP-375D | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| e2f757d5-55c8-3e0f-96b9-3bce305f9957 | -21.40925 | -43.89464 | 2025-09-30 03:30:00 | NPP-375D | IBERTIOGA | MINAS GERAIS | Brasil | 3129400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 4ad86a5c-5553-3c7c-971a-fb5670365d11 | -18.47708 | -43.79926 | 2025-09-30 03:30:00 | NPP-375D | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c5cadf7e-734a-3621-ba48-67e2df21115c | -19.86046 | -42.58448 | 2025-09-30 03:30:00 | NPP-375D | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 1d5e978b-4f68-376c-94a2-388f148e551c | -19.69337 | -43.69173 | 2025-09-30 03:30:00 | NPP-375D | TAQUARAÇU DE MINAS | MINAS GERAIS | Brasil | 3168309 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 63490d51-826d-3b34-88de-5b8436bd825f | -17.71858 | -46.63741 | 2025-09-30 03:30:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 99999377-c00c-3a7b-ab70-515333b80152 | -17.71433 | -46.65604 | 2025-09-30 03:30:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 1538c9e8-8dc3-3447-9523-713ec17f5fc7 | -18.11795 | -42.19822 | 2025-09-30 03:30:00 | NPP-375D | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| a8fd3c3b-7ebc-3984-aa6f-ee5affa29d0d | -17.71653 | -46.65228 | 2025-09-30 03:30:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 33560223-9b41-3dbc-a34d-791568714f62 | -20.74087 | -47.14702 | 2025-09-30 03:30:00 | NPP-375D | SÃO TOMÁS DE AQUINO | MINAS GERAIS | Brasil | 3165107 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1aaec764-0f7c-3ba1-8d03-5b82ece8d34a | -19.85981 | -43.82151 | 2025-09-30 03:30:00 | NPP-375D | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| cb67413a-55e8-3de8-9a63-3377f5d25cb3 | -21.04168 | -45.69063 | 2025-09-30 03:30:00 | NPP-375D | BOA ESPERANÇA | MINAS GERAIS | Brasil | 3107109 | 31 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 5e3a9057-3b8a-39ce-a00a-bfcd2dec0944 | -19.60577 | -43.8344 | 2025-09-30 03:30:00 | NPP-375D | LAGOA SANTA | MINAS GERAIS | Brasil | 3137601 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9139fb8e-b66f-36f9-9ea1-88bd1fe9b3f5 | -19.30782 | -43.81483 | 2025-09-30 03:30:00 | NPP-375D | BALDIM | MINAS GERAIS | Brasil | 3105004 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5d4343f4-43e6-3550-95f2-558fa25fb44b | -19.85994 | -43.81728 | 2025-09-30 03:30:00 | NPP-375D | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| ec1dcc8c-0061-304b-94d6-d899feb16118 | -18.86047 | -41.13057 | 2025-09-30 03:30:00 | NPP-375D | MANTENÓPOLIS | ESPÍRITO SANTO | Brasil | 3203304 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| b2bdac2f-63cd-3689-9356-ba9496ca3f15 | -19.30859 | -43.81123 | 2025-09-30 03:30:00 | NPP-375D | BALDIM | MINAS GERAIS | Brasil | 3105004 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c57b462a-3c8d-361c-bab1-1dfe7f61d34d | -21.74214 | -44.61651 | 2025-09-30 03:30:00 | NPP-375D | MINDURI | MINAS GERAIS | Brasil | 3141900 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 0ee12ae5-2ae6-3289-841c-1e73703ec876 | -15.62642 | -46.25359 | 2025-09-30 03:30:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8e357207-47ec-3672-80bc-f7817ed4fab3 | -19.69422 | -43.68787 | 2025-09-30 03:30:00 | NPP-375D | TAQUARAÇU DE MINAS | MINAS GERAIS | Brasil | 3168309 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8f35666a-8bd7-3d46-b043-3a316dd4306f | -20.42605 | -46.16833 | 2025-09-30 03:30:00 | NPP-375D | PIUMHI | MINAS GERAIS | Brasil | 3151503 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 247d9d7b-e08c-3a62-addf-601ef18e209c | -16.42644 | -47.04079 | 2025-09-30 03:30:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dd72cc2f-fc37-3d2d-b2f1-037190a70952 | -18.8652 | -41.13152 | 2025-09-30 03:30:00 | NPP-375D | MANTENÓPOLIS | ESPÍRITO SANTO | Brasil | 3203304 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| f4385b8f-0393-398a-9d2f-2a487d382f25 | -19.86295 | -44.55989 | 2025-09-30 03:30:00 | NPP-375D | PARÁ DE MINAS | MINAS GERAIS | Brasil | 3147105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| 0f7a899c-e523-344f-bb84-dbc213984235 | -16.41953 | -47.01951 | 2025-09-30 03:30:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e9fff939-f176-3532-be8c-6052d9a4627a | -19.8491 | -43.81438 | 2025-09-30 03:30:00 | NPP-375D | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |
| 43eb73b8-a4d5-3adc-bba6-dc11e246b6c0 | -15.90568 | -46.22379 | 2025-09-30 03:30:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 771ebcb5-3fcd-384b-bc5c-4a063e9dee2f | -15.37194 | -47.08574 | 2025-09-30 03:30:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9da3398d-9546-3d21-820d-222702383406 | -20.42485 | -46.17341 | 2025-09-30 03:30:00 | NPP-375D | PIUMHI | MINAS GERAIS | Brasil | 3151503 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fcd48d46-957d-38eb-a57e-4a198cbb6076 | -20.61818 | -46.19041 | 2025-09-30 03:30:00 | NPP-375D | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1dc628bc-467a-3613-bfa9-e73995884c2c | -15.92919 | -46.21418 | 2025-09-30 03:30:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 742a19c7-958d-3421-8b72-4c69656acf78 | -18.48069 | -44.02849 | 2025-09-30 03:30:00 | NPP-375D | SANTO HIPÓLITO | MINAS GERAIS | Brasil | 3160603 | 31 | 33 | nan | nan | nan | Cerrado | 6.0 |


[Clique aqui para ver as próximas entradas](README21.md)
