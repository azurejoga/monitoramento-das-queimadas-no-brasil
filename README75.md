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

## Dados Diários - Página 75

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b218ef83-11ec-3387-ae85-012b83346620 | -20.41298 | -48.81973 | 2024-10-08 04:38:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 22.1 |
| 713a4b4a-42fa-3886-8c6b-803cec4abf76 | -20.41241 | -48.82374 | 2024-10-08 04:38:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 22.1 |
| 84b495db-93ad-3e36-9d68-718fd7132c50 | -20.41183 | -48.82775 | 2024-10-08 04:38:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b3a19279-b1a8-3bf9-9fa7-34a05ecb9d24 | -20.41068 | -48.81115 | 2024-10-08 04:38:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 5.0 |
| c400f3da-4fc9-3bd0-b3ee-fcc2dbb1f41d | -20.41011 | -48.81516 | 2024-10-08 04:38:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 5.0 |
| b2ceca62-593c-3ba4-91a2-4b3816eec817 | -20.40953 | -48.81917 | 2024-10-08 04:38:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 21.2 |
| 716e3cb2-95a9-3019-91a4-eb183bafbc81 | -20.40895 | -48.82318 | 2024-10-08 04:38:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 21.2 |
| 4a2fd27f-9c33-30eb-b302-6b5612def967 | -20.40837 | -48.82719 | 2024-10-08 04:38:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 244.0 |
| bd417b10-6309-3820-946c-a3d797c5438f | -20.40781 | -48.80656 | 2024-10-08 04:38:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 66f2bd21-6c52-3b89-9e8b-3339b787a05a | -20.40723 | -48.81057 | 2024-10-08 04:38:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 7931ac46-3195-3b94-85ad-827d7f5effc6 | -20.40665 | -48.81459 | 2024-10-08 04:38:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 4f3d99a4-802a-3090-9655-e35e474b4d3c | -20.40607 | -48.81861 | 2024-10-08 04:38:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 21.2 |
| 46438071-8ecb-31c4-8601-d0227a92a995 | -20.40549 | -48.82264 | 2024-10-08 04:38:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 21.2 |
| 2aa19159-2908-331a-b233-259c5bd0cdb6 | -20.40492 | -48.82664 | 2024-10-08 04:38:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 244.0 |
| 3b886e85-e950-3ef1-b1bd-a6b1c3ff2517 | -20.40435 | -48.80599 | 2024-10-08 04:38:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 31ac391a-7dac-360a-b3e9-ca43a3cdb83d | -20.40377 | -48.81 | 2024-10-08 04:38:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 72fb39fe-80d4-31f6-804c-212935d6f308 | -20.4032 | -48.81402 | 2024-10-08 04:38:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 11583649-7ca9-3bc6-b9f7-fe6b6285f343 | -20.4032 | -48.78934 | 2024-10-08 04:38:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 21e5f4f7-d261-3078-a587-398efcd659e3 | -20.40263 | -48.79335 | 2024-10-08 04:38:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 85c5e511-b0a1-31d3-b425-b078a7ea0c8c | -20.40262 | -48.81805 | 2024-10-08 04:38:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 7.9 |
| c39e2fce-b3dc-3095-9c70-c76e168cd255 | -20.40204 | -48.82207 | 2024-10-08 04:38:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 7.9 |
| df7c0bae-8ed9-38c5-a5f6-c62f43b580c7 | -20.40146 | -48.82609 | 2024-10-08 04:38:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 7.2 |
| b5e64bfc-65b9-306f-a136-c0e4cd1f9770 | -20.40089 | -48.80542 | 2024-10-08 04:38:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e4af841a-34ab-31b0-99b6-88fcd05dc659 | -20.40088 | -48.8301 | 2024-10-08 04:38:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 7.2 |
| e958749b-3a06-3d4f-ab93-f0f2638e2eb6 | -20.40032 | -48.80943 | 2024-10-08 04:38:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8927a7db-57f1-3c47-a173-62f2699eed1a | -20.39974 | -48.81344 | 2024-10-08 04:38:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8b98b3bb-e6a5-3012-b7d4-414582203720 | -20.39916 | -48.81747 | 2024-10-08 04:38:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 74639e27-daaf-3a2a-b418-106fe866586f | -20.39859 | -48.8215 | 2024-10-08 04:38:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 7.9 |
| f1e68256-5b78-305e-ae77-d08b10502a96 | -20.39859 | -48.79681 | 2024-10-08 04:38:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b5841f86-0752-3d46-adff-2faf9d79ce45 | -20.39802 | -48.80084 | 2024-10-08 04:38:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f6c76895-c309-339e-9cd2-4c29d8bc52c9 | -20.39801 | -48.82553 | 2024-10-08 04:38:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 149ab8b5-94f2-365e-8ea7-1586705ffdbd | -20.39744 | -48.80486 | 2024-10-08 04:38:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 624644b9-14ff-3807-abe8-b0214b8e535c | -20.39743 | -48.82956 | 2024-10-08 04:38:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 571db01e-fc52-38a8-b1da-b69a8bc667c0 | -20.39686 | -48.80886 | 2024-10-08 04:38:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 5.2 |
| ce3b5c7d-0b15-3e4f-a322-22d982f96711 | -20.39571 | -48.81689 | 2024-10-08 04:38:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 19.2 |
| 67124814-7640-32e0-97b7-6dabe6c9a298 | -20.39571 | -48.79224 | 2024-10-08 04:38:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 482985f4-f364-314d-ab19-dc6613943efa | -20.39513 | -48.82093 | 2024-10-08 04:38:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 19.2 |
| d5779cbe-de30-3afa-a692-d2392e269767 | -20.39513 | -48.79625 | 2024-10-08 04:38:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7f3a4bbc-a3f2-3f6d-a0d6-59b7f064267e | -20.39456 | -48.80026 | 2024-10-08 04:38:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6097452c-a8fb-3859-90dd-12960dd8558a | -20.39455 | -48.82496 | 2024-10-08 04:38:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 23.4 |
| 3e6b1355-978d-3a57-89ff-c67c2946c740 | -20.39398 | -48.80428 | 2024-10-08 04:38:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4f977f55-1569-3cc2-b139-4ae521cf7121 | -20.39397 | -48.82898 | 2024-10-08 04:38:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 23.4 |
| aca3a7e7-bfa7-3ce6-92e7-f5162986452d | -20.39226 | -48.81632 | 2024-10-08 04:38:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 19.2 |
| 052acf1f-b802-38b3-b104-1569b23bf249 | -20.39168 | -48.82034 | 2024-10-08 04:38:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 19.2 |
| c589df60-fb63-3630-a6fc-e58eb9bc20b8 | -20.3911 | -48.82437 | 2024-10-08 04:38:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 23.4 |
| addbff5b-6f2b-34b5-b302-59fc1a858dae | -20.39053 | -48.82839 | 2024-10-08 04:38:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 23.4 |
| 64d51984-1d22-300c-aa2c-1779fb7b9ee2 | -20.38995 | -48.80771 | 2024-10-08 04:38:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8c404f9a-79d5-3b46-a37f-e1e5a1dfc6a6 | -20.38881 | -48.81574 | 2024-10-08 04:38:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 13053f90-7440-3343-a7bb-efc0c0022e55 | -20.38823 | -48.81976 | 2024-10-08 04:38:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 588a0ebc-3f34-340e-ac95-c7c7cd215fd9 | -20.38765 | -48.82378 | 2024-10-08 04:38:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cd354b76-2535-359b-acf9-61b6b449300d | -20.38708 | -48.8278 | 2024-10-08 04:38:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7298fbd7-f3c2-31ae-8038-73c49b850b6b | -20.3865 | -48.80714 | 2024-10-08 04:38:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 28d99cb2-735b-37c9-ab58-06d0f5a38aec | -20.45123 | -48.81618 | 2024-10-08 04:38:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 315c663d-6353-39cd-b69b-b9f3b2509ec6 | -20.41125 | -48.83178 | 2024-10-08 04:38:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 36880f4d-28fa-300f-94e8-e2b5af7f45fb | -20.41067 | -48.83581 | 2024-10-08 04:38:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1ee1d719-e940-39d3-9a63-bc03f142cc53 | -20.41009 | -48.83983 | 2024-10-08 04:38:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b3b1921c-1ca5-314d-87eb-c6bc6d8799aa | -20.40951 | -48.84384 | 2024-10-08 04:38:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 3.8 |
| eec66115-8846-3459-a387-2c7dd7773591 | -20.40779 | -48.83121 | 2024-10-08 04:38:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 244.0 |
| 80223b38-f5d0-3af5-ae94-bcf977bbf016 | -20.40722 | -48.83523 | 2024-10-08 04:38:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 159.1 |
| 8fc79f12-cc09-3d40-a9b7-0cbd8d9a6646 | -20.40664 | -48.83924 | 2024-10-08 04:38:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 159.1 |
| b88c89b2-2cd6-3686-8579-6a565729fe97 | -20.40606 | -48.84325 | 2024-10-08 04:38:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 04bf2956-d2da-38c5-8a57-68038be66c0b | -20.40548 | -48.84727 | 2024-10-08 04:38:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 15107ffb-0550-3c80-b1dd-8ce079bb7267 | -20.4049 | -48.85129 | 2024-10-08 04:38:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| dd2bd9b4-c578-37d9-9f5e-2169a123d89c | -20.40318 | -48.83867 | 2024-10-08 04:38:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 159.1 |
| 2b4d8d9e-e10c-3b31-aa7e-a7a2adc675f6 | -20.40261 | -48.84267 | 2024-10-08 04:38:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 7613d8f7-e6d1-3926-8e66-4c8b8812ffc2 | -20.40203 | -48.84668 | 2024-10-08 04:38:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 4.6 |
| a0809955-6dce-3706-951b-4ab50da96c20 | -20.40145 | -48.8507 | 2024-10-08 04:38:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a889f6be-6062-350b-a813-ad5e6bacfcb6 | -20.40087 | -48.85471 | 2024-10-08 04:38:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 05197e29-aa49-3908-8eaa-fb1920babf11 | -20.40031 | -48.83411 | 2024-10-08 04:38:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 260.8 |
| a33c220e-3ec4-3f8f-83cf-aa6903b9a041 | -20.39858 | -48.84611 | 2024-10-08 04:38:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 610.6 |
| f480bb74-d0a4-3c58-9c22-d06b8d14e7d3 | -20.398 | -48.85012 | 2024-10-08 04:38:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 97.6 |
| cd8d36bb-9bb5-3aeb-9f05-25538c026a2a | -20.39743 | -48.85413 | 2024-10-08 04:38:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 97.6 |
| 37940f21-d895-3c7f-922c-c0d646f178af | -20.39685 | -48.83356 | 2024-10-08 04:38:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 260.8 |
| f0804ceb-1254-37bb-9336-9ddf5c82a0f3 | -20.39628 | -48.83757 | 2024-10-08 04:38:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 260.8 |
| f20f925a-fd0a-3815-8050-855a94f6c51b | -20.3957 | -48.84155 | 2024-10-08 04:38:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 610.6 |
| 32560c00-9f98-36d6-b539-c06a7dfa17da | -20.39456 | -48.84955 | 2024-10-08 04:38:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 97.6 |
| 44d91a74-9d8d-383e-921e-77039af5e6e5 | -20.3934 | -48.83299 | 2024-10-08 04:38:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 7d85de0a-578b-3220-a555-f975b26c13b8 | -20.39283 | -48.83699 | 2024-10-08 04:38:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 83cac4b0-f58d-30d4-9f66-c6a2f57766aa | -20.39225 | -48.84098 | 2024-10-08 04:38:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 7.1 |
| fbf178a2-0213-368a-81c7-add01f9bb81d | -20.39168 | -48.84497 | 2024-10-08 04:38:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 7.1 |
| a1778128-3ac2-3832-bde3-1a89b8cac387 | -20.3911 | -48.84898 | 2024-10-08 04:38:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 12.0 |
| ede4d4e4-832b-35b8-b6fc-7d3a73916b6d | -20.38995 | -48.8324 | 2024-10-08 04:38:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 1c59d0ae-5063-3ce7-a4e7-f94565f0494f | -20.38938 | -48.83641 | 2024-10-08 04:38:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 2ed06c32-bb14-37d7-b6d6-bc78c3d40124 | -20.3888 | -48.84041 | 2024-10-08 04:38:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 7.1 |
| a92aa5c5-f708-35ad-9857-42ea59686c01 | -20.38823 | -48.84441 | 2024-10-08 04:38:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 4f711da9-7266-31bc-8bce-f0c5c0b6e5cc | -20.38765 | -48.84842 | 2024-10-08 04:38:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 12.0 |
| d6482e7d-bb10-34dd-a8a5-cd97137f5b32 | -20.38707 | -48.85245 | 2024-10-08 04:38:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 68efc1d3-0249-3b3b-9885-9b1635402a4a | -20.3865 | -48.83182 | 2024-10-08 04:38:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 3.9 |
| d306ef9a-ec42-392d-93e0-5616d8edd6d5 | -20.38592 | -48.83583 | 2024-10-08 04:38:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 3.9 |
| f44cdeae-4673-3cb6-86db-30c6f0f0d262 | -22.29716 | -49.11764 | 2024-10-08 04:38:00 | NOAA-21 | BAURU | SÃO PAULO | Brasil | 3506003 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4b79439f-56f4-31bb-ab90-8844311d8bac | -21.37951 | -48.63249 | 2024-10-08 04:38:00 | NOAA-21 | CÂNDIDO RODRIGUES | SÃO PAULO | Brasil | 3510104 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 822b5f9a-a952-3ba4-acbb-88f0a4b7eb6d | -22.28877 | -50.00203 | 2024-10-08 04:38:00 | NOAA-21 | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 9c55d9ba-3a70-375b-81f3-95530c5add31 | -22.28819 | -50.00594 | 2024-10-08 04:38:00 | NOAA-21 | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 83a4a703-bb66-3286-b700-4e7b3cf8d2dd | -22.19954 | -49.9643 | 2024-10-08 04:38:00 | NOAA-21 | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 3b199cea-2c2f-37db-a10a-608332b88717 | -22.18827 | -49.97031 | 2024-10-08 04:38:00 | NOAA-21 | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| f2dde5a6-230e-36c0-8c5a-ddcb7fac78f5 | -22.5941 | -49.21713 | 2024-10-08 04:38:00 | NOAA-21 | AGUDOS | SÃO PAULO | Brasil | 3500709 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f99e3976-d16e-3b00-b0ce-f82c873e3ab9 | -22.59352 | -49.22122 | 2024-10-08 04:38:00 | NOAA-21 | AGUDOS | SÃO PAULO | Brasil | 3500709 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5fcdbdc8-3331-3c20-97fc-322d87a78c52 | -22.58948 | -49.22474 | 2024-10-08 04:38:00 | NOAA-21 | AGUDOS | SÃO PAULO | Brasil | 3500709 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3aade313-e903-3adf-bb50-c7d2ca3b7676 | -22.58369 | -49.21534 | 2024-10-08 04:38:00 | NOAA-21 | AGUDOS | SÃO PAULO | Brasil | 3500709 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 78c9bcea-b647-3905-8dea-5d0c06356a6b | -22.58312 | -49.21943 | 2024-10-08 04:38:00 | NOAA-21 | AGUDOS | SÃO PAULO | Brasil | 3500709 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README76.md)
