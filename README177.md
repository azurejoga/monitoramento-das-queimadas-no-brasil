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

## Dados Diários - Página 177

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8613fc19-2c7d-3598-901d-a10afd01d2b6 | -10.18785 | -69.11832 | 2024-10-03 05:16:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 52df5e1c-7d7b-327d-bd93-1e583cc8f35a | -10.18722 | -69.12176 | 2024-10-03 05:16:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5997e7e2-79be-31fc-b05e-059f18d9379b | -10.16653 | -69.36157 | 2024-10-03 05:16:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6715ef10-ae5f-3feb-afb8-de86179de8be | -10.16586 | -69.36507 | 2024-10-03 05:16:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 937e0b8a-0ec1-372a-ac89-37e8f992cff3 | -10.16553 | -69.36077 | 2024-10-03 05:16:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2ee4df83-6db9-38ba-8073-9eac076b926b | -10.16489 | -69.36428 | 2024-10-03 05:16:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f3243bbf-352b-3535-bac4-f07c5f0d4180 | -9.70982 | -69.06572 | 2024-10-03 05:16:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a77c4190-3093-3e95-8fa9-7d4647e9d041 | -9.70916 | -69.06921 | 2024-10-03 05:16:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e204d777-9df2-3f32-9d3d-ef80a218b6bd | -9.70444 | -69.0647 | 2024-10-03 05:16:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 252013e6-85b5-305c-9e35-2ab416527cd1 | -9.70379 | -69.0682 | 2024-10-03 05:16:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 782df327-ee05-3046-a721-7c1a222cb5a6 | -9.6694 | -69.06193 | 2024-10-03 05:16:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 71a79496-e098-318a-bdbf-6f0e02151c44 | -9.66877 | -69.06538 | 2024-10-03 05:16:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 032ee4ff-4662-3c3f-b70c-e9602d7190f8 | -9.66403 | -69.06083 | 2024-10-03 05:16:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0a21428e-5ca1-367b-bee6-cc78ceb85378 | -9.66341 | -69.06424 | 2024-10-03 05:16:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3bb8aab7-064a-3d4c-93a7-65458176ebd6 | -7.56709 | -70.11273 | 2024-10-03 05:16:00 | NOAA-20 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5def0c75-68dc-370e-9936-d6635e7f5cab | -9.19899 | -71.80207 | 2024-10-03 05:16:00 | NOAA-20 | JORDÃO | ACRE | Brasil | 1200328 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 92addfc4-303d-382c-9184-8014d0e87256 | -8.87089 | -70.8485 | 2024-10-03 05:16:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0c58ffd4-e9b3-3433-a7b8-03647eac0a5f | -8.86997 | -70.8534 | 2024-10-03 05:16:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 35ae1679-dcc1-3a06-b7ca-5505c7b48a5a | -8.7449 | -71.01366 | 2024-10-03 05:16:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 650956b9-5100-3e6f-a45d-dcaeec777664 | -8.7387 | -71.0126 | 2024-10-03 05:16:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| daec9b66-8cfd-35e8-a6c1-e9c983c834b4 | -8.4686 | -70.37099 | 2024-10-03 05:16:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2768dc63-5e6b-3d3c-b07e-3c4b6b6c0f71 | -8.4667 | -70.36691 | 2024-10-03 05:16:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7be74421-7710-36ea-9c93-97ec90228b30 | -7.9278 | -71.47309 | 2024-10-03 05:16:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5a8895f6-d123-3600-b292-ee0f415db1c2 | -7.92676 | -71.47868 | 2024-10-03 05:16:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6004fdd0-daa1-33c2-9426-91ab9612d155 | -7.42787 | -72.7324 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| cc5a4657-77e9-3354-ba3b-26773fe272f3 | -7.42091 | -72.73096 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 349be2e8-9a42-3c78-993c-9c12e4de7f84 | -7.2154 | -72.31774 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f91d1169-84d7-3d8e-947f-07907207f88f | -8.46588 | -70.37136 | 2024-10-03 05:16:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 58af4c60-4fb2-38e9-ba8b-9c8df35fe8e1 | -8.46349 | -70.36537 | 2024-10-03 05:16:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9ca130d5-e42d-3fe3-b525-2ac77cae5303 | -8.33654 | -70.25641 | 2024-10-03 05:16:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a4c90cfd-0f54-3367-bb46-1c2470de078a | -8.22138 | -70.80605 | 2024-10-03 05:16:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 190f49d1-5ad9-3c2d-8c9b-49fbb8492c14 | -8.22045 | -70.81099 | 2024-10-03 05:16:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9b3522b5-6190-33cd-a7e5-e84369331f8f | -8.12657 | -70.49898 | 2024-10-03 05:16:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| aca726e3-159a-3949-b555-b740b166de56 | -8.12051 | -70.49789 | 2024-10-03 05:16:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cff56d0e-035f-3fd1-bae6-4de3930a4934 | -7.96356 | -71.3518 | 2024-10-03 05:16:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b6975d67-3112-3379-be1d-cd53637e2abf | -7.96259 | -71.35706 | 2024-10-03 05:16:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1aad5255-759a-3e1f-8238-a0b14a1f80ef | -21.38284 | -47.63304 | 2024-10-03 05:18:00 | NOAA-20 | SÃO SIMÃO | SÃO PAULO | Brasil | 3550902 | 35 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 7ad69de2-b297-3700-b0b0-018e62103b6a | -17.11779 | -47.13847 | 2024-10-03 05:18:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 3c232fac-bdf6-369e-8dce-9eebdcf7f590 | -17.12112 | -47.13765 | 2024-10-03 05:18:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 76cff932-c16b-368b-93ce-f870db71665a | -17.11839 | -47.13187 | 2024-10-03 05:18:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 5.1 |
| ad506595-0301-3b09-a870-baa8e3f360a3 | -17.11444 | -47.13137 | 2024-10-03 05:18:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 5.4 |
| b0d7aff2-f766-3144-a890-aa065b46fa65 | -17.11392 | -47.13757 | 2024-10-03 05:18:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 5.4 |
| af843254-9621-31c3-8ba3-0ede2f2a96e9 | -17.11115 | -47.13227 | 2024-10-03 05:18:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 2f1e68f6-d229-3dcd-aff5-0270fc52bd65 | -17.11059 | -47.13847 | 2024-10-03 05:18:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 8.2 |
| b79be619-467e-30b4-9002-85b04b99a56d | -17.10723 | -47.13147 | 2024-10-03 05:18:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ae1f104b-2a78-3445-ae13-c2da49d3245b | -21.38945 | -47.64179 | 2024-10-03 05:18:00 | NOAA-20 | SÃO SIMÃO | SÃO PAULO | Brasil | 3550902 | 35 | 33 | nan | nan | nan | Cerrado | 5.8 |
| d1f5bb70-bf31-323a-a7fc-c600b453c105 | -21.38888 | -47.64945 | 2024-10-03 05:18:00 | NOAA-20 | SÃO SIMÃO | SÃO PAULO | Brasil | 3550902 | 35 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 671fddca-e5dd-3f0e-aa3b-d887ece4e89c | -21.29618 | -47.62617 | 2024-10-03 05:18:00 | NOAA-20 | SERRA AZUL | SÃO PAULO | Brasil | 3551405 | 35 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 8be7a7b6-fea3-3de8-9943-c44fe9917b04 | -21.28845 | -47.63294 | 2024-10-03 05:18:00 | NOAA-20 | SERRA AZUL | SÃO PAULO | Brasil | 3551405 | 35 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 058bab20-f0ba-3912-8cae-1a160b43b7a3 | -15.72105 | -48.38313 | 2024-10-03 05:18:00 | NOAA-20 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0d4f37af-9894-36f8-b180-c9a94d81f2c8 | -15.71402 | -48.38714 | 2024-10-03 05:18:00 | NOAA-20 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| da40a859-1693-3c76-a52b-a8f6f9db10f6 | -19.09757 | -48.05511 | 2024-10-03 05:18:00 | NOAA-20 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a9382906-8e80-3e16-b851-e5f127d30d58 | -19.09067 | -48.05422 | 2024-10-03 05:18:00 | NOAA-20 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 12b391d1-249b-3fdb-8759-8d33afb90237 | -19.08375 | -48.05374 | 2024-10-03 05:18:00 | NOAA-20 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| efe91f38-df54-3b5e-a2d1-ce126e0cef15 | -16.10506 | -50.26962 | 2024-10-03 05:18:00 | NOAA-20 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 989e8d2c-893c-33c4-b1ba-2abd1f67a8e1 | -16.10458 | -50.27398 | 2024-10-03 05:18:00 | NOAA-20 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7adbaa73-aa0e-3449-b650-35db55355625 | -16.10433 | -50.26871 | 2024-10-03 05:18:00 | NOAA-20 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0b0373d0-0a9e-3ecb-ba34-529cb0f3436d | -16.1041 | -50.27828 | 2024-10-03 05:18:00 | NOAA-20 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2bf8d4ba-b0b8-3980-a5ef-f387056bb1b0 | -16.10387 | -50.27308 | 2024-10-03 05:18:00 | NOAA-20 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 24a3bdae-ec00-3bac-93d0-40df4c0c3542 | -16.10343 | -50.27736 | 2024-10-03 05:18:00 | NOAA-20 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| eeeefa9a-adea-39af-b3ad-c7a50cc107e8 | -16.10299 | -50.28164 | 2024-10-03 05:18:00 | NOAA-20 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| bfa36e83-43d6-3d63-8994-21cfb77cac88 | -16.09946 | -50.26659 | 2024-10-03 05:18:00 | NOAA-20 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bdf1954c-7e96-3a9b-85e7-b69a936b07fc | -16.09896 | -50.27106 | 2024-10-03 05:18:00 | NOAA-20 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dc437a4c-436b-34fb-933b-45ef0a922a29 | -16.09871 | -50.26572 | 2024-10-03 05:18:00 | NOAA-20 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5d56e7c5-e2d2-322e-844e-d9c426a05547 | -16.09824 | -50.27024 | 2024-10-03 05:18:00 | NOAA-20 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6afc362e-95ff-3ada-8bd6-64084a211cec | -16.09804 | -50.27935 | 2024-10-03 05:18:00 | NOAA-20 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 35e9c279-9891-3593-99e8-62428a348c5d | -16.09738 | -50.2785 | 2024-10-03 05:18:00 | NOAA-20 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8159de41-10b1-31e9-804a-9a7e4c7fbf7f | -16.09351 | -50.26667 | 2024-10-03 05:18:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0868f4a1-f652-3469-94b7-b2aa0b34127f | -16.09282 | -50.26527 | 2024-10-03 05:18:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| fe7c741b-f109-345a-a4cf-4e1f8a888a25 | -16.09153 | -50.27777 | 2024-10-03 05:18:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| dd0ab220-56a2-337b-ad29-89e9c7399d38 | -16.09107 | -50.28218 | 2024-10-03 05:18:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 37b87da7-4471-3df0-8442-22b8bc3f4575 | -16.08641 | -50.27727 | 2024-10-03 05:18:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d57c7e20-ce49-3806-83e6-1285ee4350e7 | -16.0859 | -50.28195 | 2024-10-03 05:18:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 60c05c04-25d5-351a-99d4-20e8fb8cc8e9 | -15.90473 | -50.16601 | 2024-10-03 05:18:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3bd727b5-739b-32e5-ab05-05fc7edbcec5 | -15.90335 | -50.16701 | 2024-10-03 05:18:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f8b9d5c4-0867-3912-beb6-c103a0196ba3 | -15.89836 | -50.16972 | 2024-10-03 05:18:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3bce101e-7b59-35c1-a740-250b2316bf9a | -15.8974 | -50.16697 | 2024-10-03 05:18:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 169033f5-6d79-3919-a68a-2bf739f1f438 | -15.897 | -50.17077 | 2024-10-03 05:18:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3dd8949b-5778-315d-8bee-503f6442c07f | -15.89372 | -50.15776 | 2024-10-03 05:18:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6989531c-785b-39b8-b0f0-2e116304d41f | -15.89328 | -50.16168 | 2024-10-03 05:18:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e8b18e21-1b2e-3c59-a67c-97970756b06c | -15.89285 | -50.16557 | 2024-10-03 05:18:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a53ce7a1-8480-3531-a355-9dc7c820cbc0 | -15.89242 | -50.16947 | 2024-10-03 05:18:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8ad6b435-388b-3fb9-8e60-c5fcf27ac0b7 | -15.89231 | -50.15852 | 2024-10-03 05:18:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 357ac9fe-ad8f-3f73-aea4-2c287cd832da | -15.8919 | -50.16251 | 2024-10-03 05:18:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4ef38fc1-b4d7-3e67-ba44-5940250fb0c3 | -15.89149 | -50.16649 | 2024-10-03 05:18:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 26df120f-445f-3317-9248-efe61fffabad | -16.08748 | -50.37386 | 2024-10-03 05:18:00 | NOAA-20 | BURITI DE GOIÁS | GOIÁS | Brasil | 5203939 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ad2c752d-315b-372d-8a09-872ef6ffb836 | -17.84089 | -50.81264 | 2024-10-03 05:18:00 | NOAA-20 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ffe02048-9c95-3b12-a287-e152ede81406 | -16.11593 | -50.43895 | 2024-10-03 05:18:00 | NOAA-20 | BURITI DE GOIÁS | GOIÁS | Brasil | 5203939 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a8684db1-75ea-36c9-a9c3-5cb5bfeb7cd3 | -16.10996 | -50.43988 | 2024-10-03 05:18:00 | NOAA-20 | BURITI DE GOIÁS | GOIÁS | Brasil | 5203939 | 52 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 7a6242e9-8ff2-3b42-91b1-863805329bde | -16.10405 | -50.44017 | 2024-10-03 05:18:00 | NOAA-20 | BURITI DE GOIÁS | GOIÁS | Brasil | 5203939 | 52 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 20c75eae-7d51-3b59-896e-5dab08737c65 | -16.10369 | -50.44365 | 2024-10-03 05:18:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 49794488-7e4e-3f03-adce-4c3e78879772 | -16.09916 | -50.3749 | 2024-10-03 05:18:00 | NOAA-20 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 061ef336-4252-31ee-a528-9d5f50b6b5fd | -16.09872 | -50.43505 | 2024-10-03 05:18:00 | NOAA-20 | BURITI DE GOIÁS | GOIÁS | Brasil | 5203939 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 816c9a37-2d5a-303f-b40f-018c97234e3a | -16.0983 | -50.43903 | 2024-10-03 05:18:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 350cdbb6-02d1-3fa1-9abd-853ae0ee3c59 | -16.09796 | -50.44223 | 2024-10-03 05:18:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 311b4d66-a94b-39e3-93c4-3bde43cb5061 | -16.09332 | -50.37437 | 2024-10-03 05:18:00 | NOAA-20 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c5277248-0f2b-3608-9e6c-ba0b2883f5a9 | -16.0933 | -50.37523 | 2024-10-03 05:18:00 | NOAA-20 | BURITI DE GOIÁS | GOIÁS | Brasil | 5203939 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6c22e587-8ffa-34cb-97f3-e841446fbc8b | -16.08784 | -50.42682 | 2024-10-03 05:18:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e1fea0c1-0cdd-39b7-84c7-f79990a3a1b1 | -16.08746 | -50.42747 | 2024-10-03 05:18:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c029097e-1eea-3404-9c2c-1401c2b4df0f | -16.08745 | -50.37481 | 2024-10-03 05:18:00 | NOAA-20 | BURITI DE GOIÁS | GOIÁS | Brasil | 5203939 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README178.md)
