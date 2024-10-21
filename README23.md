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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5c964a14-51a8-3e5f-bf45-f111950282e9 | 1.00856 | -51.1541 | 2024-10-21 04:10:00 | NPP-375D | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b6657187-5258-3930-a627-6b7ed334cfc9 | 1.00638 | -51.15966 | 2024-10-21 04:10:00 | NPP-375D | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5a7a8b3c-0919-3272-9ff9-4d513792f5b9 | 1.00582 | -51.15596 | 2024-10-21 04:10:00 | NPP-375D | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| baeae4fc-b00a-3abe-81fa-39854d0e0777 | 1.00352 | -51.15868 | 2024-10-21 04:10:00 | NPP-375D | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fa833827-4b90-3434-8f45-84b6024a5921 | 0.3968 | -50.95116 | 2024-10-21 04:10:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| acca0352-60b4-3704-b070-d5380fbfae12 | 0.39625 | -50.94763 | 2024-10-21 04:10:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dd9db458-c3db-3a5e-9cf4-b5b9913a0811 | 0.3957 | -50.94409 | 2024-10-21 04:10:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9b3e38ea-59aa-3b79-bf19-78a23b22509a | 0.39514 | -50.94053 | 2024-10-21 04:10:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a7e3c2f3-a49c-3c96-86de-c193560eb758 | -5.07624 | -42.56522 | 2024-10-21 04:12:00 | NPP-375D | ALTOS | PIAUÍ | Brasil | 2200400 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 44c22d21-df6a-3581-9217-9b7d916dc638 | -5.0516 | -37.99554 | 2024-10-21 04:12:00 | NPP-375D | QUIXERÉ | CEARÁ | Brasil | 2311504 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 626c7d93-26f1-3c2e-8cd5-f0750a0e940a | -3.09336 | -54.18408 | 2024-10-21 04:12:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 37.9 |
| fc5135ef-156b-3b6a-aefa-80c7942e9513 | -6.85769 | -40.7453 | 2024-10-21 04:12:00 | NPP-375D | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| b60977fa-52f0-3621-98f6-f55bc7b74f6e | -6.8542 | -40.74478 | 2024-10-21 04:12:00 | NPP-375D | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 50bcb6e0-1029-33e6-922f-d437cebf4d36 | -6.43599 | -42.114 | 2024-10-21 04:12:00 | NPP-375D | BARRA D'ALCÂNTARA | PIAUÍ | Brasil | 2201176 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| e17217b1-620e-3b92-86bd-a970f608215a | -5.98622 | -43.52974 | 2024-10-21 04:12:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ed4752d2-a186-3996-ac69-97136f9fa044 | -5.9239 | -38.35804 | 2024-10-21 04:12:00 | NPP-375D | ERERÊ | CEARÁ | Brasil | 2304277 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| bc7460c8-184a-3e9d-963f-89a3af64f19a | -5.91753 | -42.95626 | 2024-10-21 04:12:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| c528fee5-becc-3888-8ab4-322555fc28a0 | -5.87754 | -40.16666 | 2024-10-21 04:12:00 | NPP-375D | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| b3350dc9-987a-32fd-b3a8-635ad1c28e55 | -5.874 | -40.16611 | 2024-10-21 04:12:00 | NPP-375D | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| e54de9b6-725e-3314-b2b7-786731c17d24 | -5.66485 | -42.78805 | 2024-10-21 04:12:00 | NPP-375D | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 66e12436-6ff3-3c87-a983-68ee586e362b | -5.3854 | -42.8885 | 2024-10-21 04:12:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 9bfe58be-7591-3c61-ada6-8714ce2bdc8b | -5.38153 | -42.89144 | 2024-10-21 04:12:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 2fb72667-7bbb-3249-9f78-43ab277114fa | -5.32624 | -35.48164 | 2024-10-21 04:12:00 | NPP-375D | TOUROS | RIO GRANDE DO NORTE | Brasil | 2414407 | 24 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| f216bac9-b728-3b85-85d5-9e3c4e229311 | -5.3229 | -43.32658 | 2024-10-21 04:12:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7c809623-2a69-3ce7-82ee-e0cd48ff8366 | -5.32235 | -43.33006 | 2024-10-21 04:12:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a4a3072a-7bf1-3885-ac24-7564b637a5b9 | -5.31958 | -43.32605 | 2024-10-21 04:12:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c93dcfc9-79c7-31f7-a7cb-5629d6434df3 | -5.31902 | -43.32954 | 2024-10-21 04:12:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 48b76832-7048-39bb-b351-3c4bef24dcbb | -5.21981 | -43.41199 | 2024-10-21 04:12:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5af9afc8-a5d7-3dbc-b9e5-a1f84da8373d | -5.16584 | -42.87389 | 2024-10-21 04:12:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1fd65e08-6d48-3ebd-9694-6e67db82cef8 | -5.03552 | -40.90788 | 2024-10-21 04:12:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 4.1 |
| cbb5bc3c-9160-31bd-8519-e4665ad01cdd | -4.99107 | -39.25504 | 2024-10-21 04:12:00 | NPP-375D | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 00515b3d-8d14-332c-a389-dc60d03ce8ae | -4.54346 | -43.5575 | 2024-10-21 04:12:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| f1f614db-1fa8-3331-84a5-3d1306b265eb | -4.5429 | -43.56103 | 2024-10-21 04:12:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 2f90e82e-a0d8-3292-80d4-f0a8dbfc62ee | -4.54177 | -43.56808 | 2024-10-21 04:12:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c637f87a-36ff-3bce-ab54-2fc3917286fe | -4.5401 | -43.55698 | 2024-10-21 04:12:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| c907bc33-4e38-3dae-85ba-aa26d98cf884 | -4.53954 | -43.5605 | 2024-10-21 04:12:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 92fa067f-f00f-396d-8a8d-188d35903d88 | -4.53842 | -43.56756 | 2024-10-21 04:12:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a96badfb-5111-33b4-84a3-8ccbaaba788d | -4.53786 | -43.57108 | 2024-10-21 04:12:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| b9218b15-a19d-303c-89bc-e19d8a48a6d2 | -4.3421 | -42.56329 | 2024-10-21 04:12:00 | NPP-375D | MIGUEL ALVES | PIAUÍ | Brasil | 2206209 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| d979307e-47e8-3ee6-9ce0-7a93c6beab1f | -4.33932 | -42.55931 | 2024-10-21 04:12:00 | NPP-375D | MIGUEL ALVES | PIAUÍ | Brasil | 2206209 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 0c397505-391d-3cc2-aea4-7c4b59601d2d | -4.33878 | -42.56277 | 2024-10-21 04:12:00 | NPP-375D | MIGUEL ALVES | PIAUÍ | Brasil | 2206209 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| e750b142-51da-398f-b87b-905e63838b92 | -4.30536 | -43.58479 | 2024-10-21 04:12:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 585da982-7575-3e0b-81d1-379f421031a2 | -4.25737 | -43.72667 | 2024-10-21 04:12:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 203fed3d-1e06-349a-a823-084dee1347fc | -4.25625 | -43.7338 | 2024-10-21 04:12:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a1ad7d93-caa9-369e-aa62-62c1ec44b244 | -4.25401 | -43.72614 | 2024-10-21 04:12:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0e2d8218-42cf-3fb4-bc6d-d996122f8c52 | -4.25345 | -43.7297 | 2024-10-21 04:12:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bfaa715a-0027-3a54-b2a6-00ada0c2f724 | -4.25288 | -43.73327 | 2024-10-21 04:12:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a529247b-b546-302c-ba2b-7965ba35884c | -4.25232 | -43.73684 | 2024-10-21 04:12:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1ddb29f5-b3ac-364c-8533-241a65467965 | -4.2512 | -43.72206 | 2024-10-21 04:12:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a883deb9-68fc-37bb-8753-d7123616cfb6 | -4.25064 | -43.7256 | 2024-10-21 04:12:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6aec9688-4b6e-3fae-8a58-bc18cd80014e | -4.25008 | -43.72915 | 2024-10-21 04:12:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4b5a75e2-564d-39ce-8158-d9e146bf9c0c | -4.24952 | -43.73272 | 2024-10-21 04:12:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e2d3e19c-1ba5-303d-bf0a-0196b4d46fed | -4.24895 | -43.73629 | 2024-10-21 04:12:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cbd9010a-df16-3190-b044-ad9b132bd850 | -4.2484 | -43.71796 | 2024-10-21 04:12:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 97e7dad3-26c0-3c7f-b25b-3e77edf8975a | -4.24784 | -43.72152 | 2024-10-21 04:12:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a228de23-7e60-3b84-af99-e97cf6d26ce3 | -4.24727 | -43.72506 | 2024-10-21 04:12:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 17a060c6-91ce-33f8-8f44-60980ff7a898 | -4.24672 | -43.7286 | 2024-10-21 04:12:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 69b4ae08-3938-3151-8871-7c30e461e047 | -4.24615 | -43.73217 | 2024-10-21 04:12:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| feb8f876-06b8-3fad-88db-16b83fc242ee | -4.24559 | -43.73575 | 2024-10-21 04:12:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b003cb10-2c8a-3e5e-9b36-7ee1807dc2b2 | -4.24502 | -43.73932 | 2024-10-21 04:12:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c79a00b9-026c-3814-9cc7-d48cf2d58cc5 | -4.24391 | -43.72453 | 2024-10-21 04:12:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1cd8408a-4a2b-3488-a9bb-b51821214a8a | -4.24335 | -43.72807 | 2024-10-21 04:12:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 561adbe9-c2cf-363d-b01b-139f4c2f7442 | -4.24278 | -43.73163 | 2024-10-21 04:12:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2078b053-d7d2-399c-a669-cbcd369dd8fb | -4.24222 | -43.73521 | 2024-10-21 04:12:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2228b526-114a-32d0-87c5-bd14573296d0 | -4.24166 | -43.73878 | 2024-10-21 04:12:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4c4eeb36-a0f7-3894-897c-b59bf8ebaf93 | -4.23998 | -43.72754 | 2024-10-21 04:12:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 8e22b8c7-035d-3d8f-9123-e722c5194186 | -4.23942 | -43.7311 | 2024-10-21 04:12:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 12.4 |
| ea52d93c-3a7b-3fdd-8e50-dd82a3e97e38 | -4.23885 | -43.73467 | 2024-10-21 04:12:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c4b7b6d9-327a-3675-bc5c-f69507ea4853 | -4.23829 | -43.73823 | 2024-10-21 04:12:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 197978ce-4ad5-3b61-baf2-69374e346bb7 | -4.23661 | -43.72701 | 2024-10-21 04:12:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 9f381dba-6b91-3462-b955-e355007bfde5 | -4.23605 | -43.73057 | 2024-10-21 04:12:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 40f28f04-2ea3-34fb-9419-98a8d8daf0c5 | -4.23549 | -43.73413 | 2024-10-21 04:12:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 136c1747-d7df-344b-9f18-8350565d2bd3 | -4.23492 | -43.73769 | 2024-10-21 04:12:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 84e48841-6043-3724-b6eb-b8cdf74345bc | -4.23268 | -43.73003 | 2024-10-21 04:12:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| edb3b1bd-7a09-35a4-8aa5-b3bf4fe75d2f | -4.23212 | -43.73359 | 2024-10-21 04:12:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9c6083cc-d80c-3d74-8148-de53e33fc3ae | -4.17368 | -43.24405 | 2024-10-21 04:12:00 | NPP-375D | AFONSO CUNHA | MARANHÃO | Brasil | 2100105 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d70d2bac-922c-3079-9760-5dbc0b6315dd | -4.1709 | -43.24002 | 2024-10-21 04:12:00 | NPP-375D | AFONSO CUNHA | MARANHÃO | Brasil | 2100105 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 05b3e3fd-1ab8-35cd-bacc-86056e96551b | -4.05263 | -43.21761 | 2024-10-21 04:12:00 | NPP-375D | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c0dddede-5cb6-3196-b54e-1a08490d2434 | -3.94947 | -43.22663 | 2024-10-21 04:12:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a2213c2f-bd6c-3e35-ba75-8033b877d05e | -3.87357 | -42.13995 | 2024-10-21 04:12:00 | NPP-375D | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 8cd7fc67-e8e9-3901-b212-9bf8a947a602 | -3.63743 | -43.12392 | 2024-10-21 04:12:00 | NPP-375D | MATA ROMA | MARANHÃO | Brasil | 2106409 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 783019ec-bd66-3142-a618-7a8db68cf07b | -3.63688 | -43.12741 | 2024-10-21 04:12:00 | NPP-375D | MATA ROMA | MARANHÃO | Brasil | 2106409 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 0a9f7de7-790a-35cb-ba25-a7b4d29a02ee | -3.35121 | -42.77261 | 2024-10-21 04:12:00 | NPP-375D | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 119826c1-e766-34f7-be5f-7f5f5c28b06d | -3.16301 | -40.20577 | 2024-10-21 04:12:00 | NPP-375D | MARCO | CEARÁ | Brasil | 2307809 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| a01c095c-873a-35b1-98ac-f2e4b4e84a61 | -3.16243 | -40.20951 | 2024-10-21 04:12:00 | NPP-375D | MARCO | CEARÁ | Brasil | 2307809 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| ab1b943a-8e8d-3653-8c76-f7f0c397ab6b | -7.18553 | -44.9677 | 2024-10-21 04:12:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 48276908-969e-316a-9d0e-c5ba8f329c1a | -7.1827 | -44.96346 | 2024-10-21 04:12:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9f0cd169-491a-32e1-8ffd-aa41f84234db | -7.18211 | -44.96716 | 2024-10-21 04:12:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f96eed35-37cb-3774-a0fe-828e32d9cca2 | -7.06961 | -44.71201 | 2024-10-21 04:12:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 449208ec-4c19-3059-b269-a11e7cf86bed | -6.80159 | -46.47029 | 2024-10-21 04:12:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| edcb4e3e-6173-3da3-9609-2b34bbff0169 | -6.80088 | -46.4746 | 2024-10-21 04:12:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4457e284-731b-3784-971e-36a0e1493fa4 | -6.79721 | -46.474 | 2024-10-21 04:12:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4a203952-04a3-3a42-a084-f8acc04120f4 | -6.76803 | -46.67466 | 2024-10-21 04:12:00 | NPP-375D | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c638738b-1d32-3e60-930b-ffcd0211cccc | -6.35164 | -46.34568 | 2024-10-21 04:12:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ead7142f-4212-3e8b-bdc1-43f37a0c755f | -6.29183 | -49.31236 | 2024-10-21 04:12:00 | NPP-375D | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3ece09ee-274f-3b83-be8b-5c3925d90a98 | -6.29109 | -49.3167 | 2024-10-21 04:12:00 | NPP-375D | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| adfeb8db-bbfe-325c-b72a-b80fd1babb59 | -6.19921 | -50.87626 | 2024-10-21 04:12:00 | NPP-375D | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ff721842-b346-3576-bd56-e608ba68cbe1 | -6.19829 | -50.88168 | 2024-10-21 04:12:00 | NPP-375D | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b53ff49e-fec3-3b9d-a089-e3b6fad48012 | -6.1943 | -50.8754 | 2024-10-21 04:12:00 | NPP-375D | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 76a6b0b4-8441-3a8e-be9f-3504cef3859d | -6.14349 | -46.90036 | 2024-10-21 04:12:00 | NPP-375D | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |


[Clique aqui para ver as próximas entradas](README24.md)
