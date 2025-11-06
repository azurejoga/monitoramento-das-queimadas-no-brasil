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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 403bd97f-c119-335e-ac3b-0576ab35dcf2 | -2.986 | -52.8146 | 2025-11-06 03:20:00 | GOES-19 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 65.5 |
| 26ebe3e3-76a9-3efb-878d-f1a67307f0b3 | -4.5932 | -43.3471 | 2025-11-06 03:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 106.2 |
| c3d52426-c16e-381a-95ca-2a2d383ae417 | -6.2757 | -43.6675 | 2025-11-06 03:30:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 78.2 |
| 7f8dc962-5f04-38fe-82e9-8a95d31c39fa | 0.4466 | -60.4873 | 2025-11-06 03:30:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 69.9 |
| be641489-8a95-3d5b-bedb-b31b31525103 | -4.5934 | -43.3239 | 2025-11-06 03:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 55.9 |
| f7d91784-5436-3033-ad06-c9f39746a5c1 | -3.9324 | -47.6962 | 2025-11-06 03:30:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 110.5 |
| 66940a3b-891e-3fe3-b0cb-7a9ae3e61477 | -4.58569 | -43.35057 | 2025-11-06 03:32:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2343f26d-a6fa-3ca0-a3b3-9843eb161b21 | -4.5974 | -43.35813 | 2025-11-06 03:32:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ebf29732-2a78-37ae-950a-cb8a4b10af94 | -4.85332 | -40.62781 | 2025-11-06 03:32:00 | NPP-375D | IPAPORANGA | CEARÁ | Brasil | 2305654 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| f3a14158-f2f7-3cae-8ce5-bdba1ab4161c | -4.5748 | -43.33833 | 2025-11-06 03:32:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ca0d339d-c997-3947-b902-ba13613833f4 | -4.60004 | -43.34281 | 2025-11-06 03:32:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| b451b37e-8755-3ad4-bbaf-bbca06ae3b87 | -4.85175 | -40.63151 | 2025-11-06 03:32:00 | NPP-375D | IPAPORANGA | CEARÁ | Brasil | 2305654 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| b32c7848-54cc-322c-afa9-3466a3a60ba9 | -3.89527 | -42.55107 | 2025-11-06 03:32:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 8.4 |
| 056c691e-695a-35db-870e-2e03cf075040 | -5.15043 | -41.2761 | 2025-11-06 03:32:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| ccc6d9ab-6c6a-3785-9c43-1d48b73cbe54 | -4.59826 | -43.35313 | 2025-11-06 03:32:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d00b86b0-e074-341d-afc6-1207bd520acd | -4.57729 | -43.34018 | 2025-11-06 03:32:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 4805abc7-5910-3a7e-8077-fec6151dc5fb | -4.59023 | -43.362 | 2025-11-06 03:32:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 03c87ae0-86e3-3ed8-bb56-70380e9c17e1 | -5.15417 | -41.25428 | 2025-11-06 03:32:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| d38eec37-7d47-35f7-a187-4ac2023667b9 | -3.33476 | -43.86635 | 2025-11-06 03:32:00 | NPP-375D | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| df1e4ae0-f313-3ff2-ac1e-f09adb573399 | -5.14925 | -41.25007 | 2025-11-06 03:32:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 8983358d-d7a2-3f9b-98e2-49e375e95e2a | -4.85232 | -40.62823 | 2025-11-06 03:32:00 | NPP-375D | IPAPORANGA | CEARÁ | Brasil | 2305654 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 0d72ca79-1992-3ea7-bb21-f31c32940b9a | -4.58361 | -43.34122 | 2025-11-06 03:32:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| fe1c3782-9401-3372-bb77-c01ec8f75b0a | -4.58626 | -43.36265 | 2025-11-06 03:32:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e8705a5d-6a09-37cb-8bf9-5ba1d52c061e | -4.58935 | -43.36708 | 2025-11-06 03:32:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0b0586f9-3323-3575-b4d5-e96c26ef6c14 | -3.43156 | -42.54555 | 2025-11-06 03:32:00 | NPP-375D | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| d3f227a4-47c3-38e6-8236-37b606bb3b2e | -4.78289 | -45.13621 | 2025-11-06 03:32:00 | NPP-375D | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 7a9d6ef9-be8a-3632-b62c-029e8953ef16 | -4.64886 | -45.6768 | 2025-11-06 03:32:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 956c968f-7e06-3119-9acc-f251bd4777b4 | -4.59286 | -43.34671 | 2025-11-06 03:32:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 605f7b67-6217-349d-b849-e27e63d2c612 | -4.59548 | -43.33153 | 2025-11-06 03:32:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 471b531e-02f5-3dc6-81e2-d33b216f8dfa | -4.78698 | -45.13917 | 2025-11-06 03:32:00 | NPP-375D | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 188bad10-1b23-32cb-93e6-e89ed30ab8ff | -3.3391 | -43.86078 | 2025-11-06 03:32:00 | NPP-375D | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e139ea41-b76a-3609-9db5-fac7ea74f1de | -4.27479 | -45.12056 | 2025-11-06 03:32:00 | NPP-375D | OLHO D'ÁGUA DAS CUNHÃS | MARANHÃO | Brasil | 2107407 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e2f76e04-42ca-3222-8c95-e6339e1ad862 | -5.15627 | -41.27667 | 2025-11-06 03:32:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| e2ebd881-913b-3f47-81a0-3d593e6aae48 | -4.58903 | -43.34731 | 2025-11-06 03:32:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 472d5e06-d197-3e00-9460-9fc69a07b93e | -4.82155 | -43.53236 | 2025-11-06 03:32:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4ddaad57-275d-35ab-93d2-a8997f4bd0b4 | -4.58391 | -43.36087 | 2025-11-06 03:32:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d0a9075a-437e-31ba-8670-48195a95be35 | -3.89687 | -42.54195 | 2025-11-06 03:32:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| b2f7ee09-83c3-3fa9-903f-558bbe8a0562 | -4.791 | -45.13115 | 2025-11-06 03:32:00 | NPP-375D | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 40a687c0-90c3-382e-89f6-e8ce8fb0103a | -4.58197 | -43.33447 | 2025-11-06 03:32:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 99ce7bb0-84d9-398f-808b-1b827fd982c8 | -3.90215 | -42.54752 | 2025-11-06 03:32:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 8.4 |
| e8a75ae3-03e5-3486-85f9-381234c972ae | -4.60434 | -43.33448 | 2025-11-06 03:32:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| c1deffdb-c3f0-377b-926e-86068d01c065 | -4.59198 | -43.35183 | 2025-11-06 03:32:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 33444614-9ca8-32b0-87ff-6664d8c46341 | -3.91569 | -43.15209 | 2025-11-06 03:32:00 | NPP-375D | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f731ae24-4dec-3a26-9806-e136bf1411e4 | -4.60253 | -43.34459 | 2025-11-06 03:32:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| a0d60e2d-c7de-3c60-a434-9341cda8dd56 | -5.97707 | -37.82902 | 2025-11-06 03:32:00 | NPP-375D | UMARIZAL | RIO GRANDE DO NORTE | Brasil | 2414506 | 24 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 1bcf1ce3-96e6-30ac-89de-b7727f0d8482 | -4.60179 | -43.33265 | 2025-11-06 03:32:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| d2cd5fdf-448a-3f2c-a07d-300319f848e9 | -4.96696 | -38.65203 | 2025-11-06 03:32:00 | NPP-375D | QUIXADÁ | CEARÁ | Brasil | 2311306 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| dc169c59-7767-3524-b455-577e2fade1b9 | -3.89607 | -42.54651 | 2025-11-06 03:32:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 8.4 |
| eaf42726-49c7-3312-aa20-da006e0024e1 | -4.59462 | -43.33653 | 2025-11-06 03:32:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| dea32547-a3c8-3117-b27b-32bf2ddb0758 | -4.59259 | -43.3637 | 2025-11-06 03:32:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3ec85bb4-6684-3f2f-b44c-e162ff92b705 | -3.33145 | -43.86539 | 2025-11-06 03:32:00 | NPP-375D | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 47749b5b-8870-3dd6-ac62-4e6f0b0045f9 | -5.15104 | -41.27257 | 2025-11-06 03:32:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 83a9dd6f-3e1a-3eef-8f10-88041a942ad4 | -3.33575 | -43.86053 | 2025-11-06 03:32:00 | NPP-375D | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 35c13034-785b-388f-b198-93980885546f | -4.5883 | -43.33551 | 2025-11-06 03:32:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 7d7e39e2-5bd8-395b-a525-ee0ed20ea3f7 | -4.58111 | -43.33947 | 2025-11-06 03:32:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 0c9bd807-0d32-3160-bea2-b0ffad1488fe | -5.97872 | -37.83032 | 2025-11-06 03:32:00 | NPP-375D | UMARIZAL | RIO GRANDE DO NORTE | Brasil | 2414506 | 24 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 5eb2cfc0-7e9c-3ad8-baf0-fbfd049279f9 | -4.59167 | -43.36881 | 2025-11-06 03:32:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0d29bf67-be00-3f6f-8d28-4debf5a4844b | -4.85277 | -40.63108 | 2025-11-06 03:32:00 | NPP-375D | IPAPORANGA | CEARÁ | Brasil | 2305654 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 8423b016-b837-3f6d-98e0-6d364aad471b | -4.58744 | -43.34048 | 2025-11-06 03:32:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| e0135dae-96fe-3ee2-8a5f-66b495bd0b38 | -5.1569 | -41.27312 | 2025-11-06 03:32:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 3f2d4b55-0580-3fec-8999-d37a4e74b8a8 | -3.89474 | -42.55067 | 2025-11-06 03:32:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| be759a79-0dc2-3dd4-8b3a-dc5f1ad79449 | -6.22776 | -37.42056 | 2025-11-06 03:32:00 | NPP-375D | SÃO JOSÉ DO BREJO DO CRUZ | PARAÍBA | Brasil | 2514651 | 25 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 9c01dc97-a197-3bbb-a6ff-e7d6d9b712b5 | -4.60344 | -43.33953 | 2025-11-06 03:32:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 22c62000-bd79-310f-a262-00f706e5f11e | -5.15166 | -41.26896 | 2025-11-06 03:32:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 18715f7f-b8b8-3df1-a437-de89c2b6ab1b | -3.13538 | -40.05691 | 2025-11-06 03:32:00 | NPP-375D | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| b294bdd5-2ffa-3583-800b-cb5ba5488016 | -5.4254 | -40.67108 | 2025-11-06 03:32:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| aa117dc0-b134-3288-981c-a42c09f808a2 | -5.14863 | -41.25368 | 2025-11-06 03:32:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 00b657a7-d516-3863-aaff-f9405de47fde | -4.78173 | -45.14268 | 2025-11-06 03:32:00 | NPP-375D | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 8bd7e5bf-0019-3b5a-b155-ab99f234c69c | -4.58451 | -43.33627 | 2025-11-06 03:32:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| cc1bde61-9eb6-3f7e-8504-9a495f57cd60 | -4.59083 | -43.33727 | 2025-11-06 03:32:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| d259dd50-8daa-3c9f-a479-539fafb8b2fa | -4.58303 | -43.36598 | 2025-11-06 03:32:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e1516686-cf35-37e7-8d90-ef2075ae1e4c | -5.15354 | -41.25794 | 2025-11-06 03:32:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| e4ad11d3-0787-3ae4-8c52-5c5963a0b92b | -4.59805 | -43.33332 | 2025-11-06 03:32:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 09d6c777-ecf2-3a73-9473-812da28e1432 | -4.59715 | -43.33834 | 2025-11-06 03:32:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| e7ede898-67b2-3a40-9e36-0347855ccfd6 | -4.85116 | -40.63483 | 2025-11-06 03:32:00 | NPP-375D | IPAPORANGA | CEARÁ | Brasil | 2305654 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| d5feaef3-d2db-382c-82d1-35e3b403a103 | -4.64179 | -45.67467 | 2025-11-06 03:32:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 7ae7b2ab-bffb-3c94-bfd3-dbd9e48922d7 | -4.85221 | -40.6344 | 2025-11-06 03:32:00 | NPP-375D | IPAPORANGA | CEARÁ | Brasil | 2305654 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 711bde1f-9495-321b-bc1c-eb36c65f52bf | -4.59374 | -43.34161 | 2025-11-06 03:32:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 55a37bac-49a3-3484-a5ef-45df12285515 | -6.22713 | -37.42431 | 2025-11-06 03:32:00 | NPP-375D | SÃO JOSÉ DO BREJO DO CRUZ | PARAÍBA | Brasil | 2514651 | 25 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 2c798b30-cfbd-3d21-8701-d22246284a6d | -4.59623 | -43.34344 | 2025-11-06 03:32:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 7d7212d0-9879-3418-9a7f-2c774db6476b | -3.33247 | -43.8596 | 2025-11-06 03:32:00 | NPP-375D | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 894609f4-fbf3-37f5-a053-d5336e510a66 | -4.59531 | -43.34856 | 2025-11-06 03:32:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| abbfef40-fb23-3762-aa31-7f745fcd929f | -3.43073 | -42.55027 | 2025-11-06 03:32:00 | NPP-375D | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| d36be275-6efd-3b5d-b7e5-1016ac8d5c27 | -4.58811 | -43.3524 | 2025-11-06 03:32:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2bbed4d0-ec48-3ce2-9a29-4ff12673d361 | -4.5911 | -43.35691 | 2025-11-06 03:32:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dccb2034-6ae5-3d71-bbd9-43e61ea3d2cb | -3.8955 | -42.5461 | 2025-11-06 03:32:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 3671b6f5-fadf-32d4-bf68-d9fadb456c86 | -4.78981 | -45.13784 | 2025-11-06 03:32:00 | NPP-375D | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| e1b6cde2-416e-3b27-b343-877618681b69 | -3.47945 | -43.67686 | 2025-11-06 03:32:00 | NPP-375D | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| abed1f2c-b586-36a1-9337-d851ce0bf0b3 | -3.90295 | -42.54295 | 2025-11-06 03:32:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| ca8cc29c-ab65-3be9-8121-794cbfa54cae | -3.90134 | -42.55212 | 2025-11-06 03:32:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 8.4 |
| 78998aef-b804-32a4-87ad-92594bf21fa0 | -4.59916 | -43.34794 | 2025-11-06 03:32:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 630f149d-f92e-309b-8325-154ec3fbba19 | -4.81834 | -37.75637 | 2025-11-06 03:32:00 | NPP-375D | JAGUARUANA | CEARÁ | Brasil | 2307007 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| a50c6575-bc9d-33aa-9a61-0f7cd3763ec4 | -4.58719 | -43.35751 | 2025-11-06 03:32:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4dd056e6-fa0d-3399-a71c-7ba0bead91ff | -4.59173 | -43.3323 | 2025-11-06 03:32:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 22beeb9d-6946-3775-a37b-b42dade738ec | -5.14988 | -41.2464 | 2025-11-06 03:32:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| ea7097c6-9161-3da5-8308-b2dc54ff1a91 | -3.47195 | -43.68134 | 2025-11-06 03:32:00 | NPP-375D | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8ac378dd-6531-3113-8706-513e0582d264 | -4.96641 | -38.65057 | 2025-11-06 03:32:00 | NPP-375D | QUIXADÁ | CEARÁ | Brasil | 2311306 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 8f97bcc2-2100-3ce6-ba61-e1d54123a64e | -5.33456 | -35.55251 | 2025-11-06 03:32:00 | NPP-375D | PUREZA | RIO GRANDE DO NORTE | Brasil | 2410405 | 24 | 33 | nan | nan | nan | Caatinga | 1.4 |
| ae6042d8-8d25-31e0-8931-02326893db00 | -5.15594 | -41.27693 | 2025-11-06 03:32:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 575fcf1b-b490-3265-85e4-6dc09acd26c6 | -4.60092 | -43.33771 | 2025-11-06 03:32:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |


[Clique aqui para ver as próximas entradas](README11.md)
