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

## Dados Diários - Página 99

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2c5c0be9-ef5f-3d9c-af4c-b3ce4f20580a | -12.84243 | -53.49139 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 391.9 |
| 0f12f68a-37b2-3c62-b4ba-680ddc912125 | -12.84027 | -53.47182 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 32.2 |
| 8631881d-e341-3c3c-9b48-c6a76434ee8c | -12.83967 | -53.47655 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 6aab6750-e947-3814-8aa4-bd1bd898495b | -12.83908 | -53.48128 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 421c0154-4967-3ca7-98b9-f39cdcb2f4ba | -12.83898 | -53.47403 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 52401d63-fd24-31cb-beca-4b0db8f7a608 | -12.83835 | -53.47875 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 80.7 |
| 675655f5-4d90-3bec-ad6b-300d4d03e2e2 | -12.83645 | -53.4929 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 194.8 |
| 3ea289b6-370c-364e-b972-91d1866566f9 | -12.83572 | -53.47115 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| accd17d9-1707-3484-93b0-3199e0f51f49 | -12.83512 | -53.47588 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 559f4680-021c-33ae-91fa-04786c93f344 | -12.83453 | -53.48061 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 9bbe63c6-fdb8-37c9-ad61-e2c00619385a | -12.83443 | -53.47337 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| add182ab-666f-30a0-9e98-fd29191662c0 | -12.83393 | -53.48535 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 33.3 |
| 1a87a706-2d6f-36cd-a6bf-1c1c640fc297 | -12.8338 | -53.47808 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 80.7 |
| 41c348c5-2045-317d-abbb-c7908f771dfd | -12.83333 | -53.49007 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 33.3 |
| 9005199d-4d0f-3238-bb57-bba4f3617537 | -12.83317 | -53.4828 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 80.7 |
| 0054aeec-de3f-3834-94da-9416f1619c30 | -12.83254 | -53.48753 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 194.8 |
| 808c7b0d-b64c-3d06-9c78-0e9291cc5a44 | -12.8319 | -53.49225 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 194.8 |
| 26b771cd-af44-328d-93ac-5ab810c0db23 | -12.83117 | -53.47047 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 633acf9d-fc95-318a-a751-2364c2349d64 | -12.83057 | -53.4752 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 8fa3121f-b3dc-36a6-a2ed-4f75acf260b4 | -12.82998 | -53.47993 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 8.8 |
| c2c97261-0b34-394b-a82b-30b52fd1cb4d | -12.82938 | -53.48467 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 33.3 |
| d869c30c-0acc-3173-93d8-dacefe8df989 | -12.82925 | -53.47741 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 96fdaf32-a02c-3e31-a3f6-ccf2c0fc1f8a | -12.82879 | -53.48941 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 33.3 |
| 11dad908-c69d-37c7-9966-a0c93c85c000 | -12.82862 | -53.48214 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| eb3a9d3f-df18-3d83-a502-890823bba954 | -12.82799 | -53.48687 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 65269a54-dcb4-3e58-aed1-2e5205d4ec8a | -12.82736 | -53.49159 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c29b34dd-480e-300e-a3dd-1880b9e52ef3 | -12.82603 | -53.47453 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9183a9b0-7259-3699-92b0-4c29bac24c3f | -12.82543 | -53.47926 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 478470f5-b7bc-3c32-97f9-daaff4c85b29 | -12.82484 | -53.484 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5e52cf7e-f99b-3016-8640-bea14d1c4d95 | -12.82471 | -53.47675 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 87f8411a-aa7e-30b7-8ce5-27b7716ddc82 | -12.82424 | -53.48874 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| bff3f4a4-9a44-3f38-9a1b-a2f03a330e3c | -12.82408 | -53.48148 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5a15a2ea-e895-38ba-948a-4bd51ca21345 | -12.82365 | -53.49346 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| df459c01-6926-3bd4-84e7-ca6979dbaf61 | -12.82345 | -53.4862 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a8ec7000-1de8-39f7-84ae-ec216273fc45 | -12.82282 | -53.49092 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 708d866b-871a-3089-9b51-6e8e90adafb0 | -12.8189 | -53.48553 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4af37a33-0f66-3b67-9424-d3d411b661d2 | -12.62564 | -53.14168 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c6d08fe9-7562-3cce-8661-2291cd0f0b82 | -12.51968 | -53.2384 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 01040b3f-cc5c-3e28-b461-1fcd576ef0d5 | -12.51903 | -53.24335 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 089ff3e2-aa3b-3986-b0b6-f14dc3164440 | -12.47837 | -53.15844 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c1609074-34d3-3cb2-9af5-f147f9a0ba84 | -12.47775 | -53.16331 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 504863a9-7951-3c15-a3d5-413abc44f5f3 | -12.46912 | -53.15714 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 92d5231a-5735-367e-ae65-7d98bfe7af7a | -12.46638 | -53.14164 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 2bcfc198-fbf3-3f94-9400-fd8948b4837b | -12.46574 | -53.14666 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 062902ad-366e-3630-81bc-cbffc70d4b1e | -12.46511 | -53.15158 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| bee148b1-f064-3286-82ec-5c75f9aeedec | -12.46175 | -53.14095 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 130baf9f-4435-3aad-a189-5230bcfe5116 | -12.46111 | -53.14598 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 02b16fc7-5481-30ac-8faa-3a0ff9254055 | -12.46048 | -53.15091 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 77428a8f-1cc3-3cf0-9adf-8c063dbabd5b | -12.45712 | -53.14022 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 6f8c852b-1e04-3916-8837-7c8d1a7ecf25 | -12.45649 | -53.14524 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a6ac3dae-4ee3-3043-b350-f7ba592906b2 | -12.45586 | -53.15022 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| a0fe6eae-f604-3bab-b2ae-756692ac0dc7 | -12.45288 | -53.14357 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 54d33dda-dd91-38ec-86d3-e5d812f313c7 | -12.45186 | -53.14452 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e42c6ef9-b30e-3a61-8d20-77edd69882cc | -12.44825 | -53.14288 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 593443be-21e8-33ee-abe8-e24aa7f0c551 | -12.44724 | -53.14382 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c4a280a7-a7b0-38d3-8c15-3f148b94b2b9 | -12.43798 | -53.14244 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| dbf7a9f8-dc8e-3700-82ef-34efa648ceb4 | -12.43437 | -53.14085 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1e71e0d5-2f90-30a8-930a-21e7b26da0da | -12.43335 | -53.14176 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5f1fede6-9ec9-3bb9-8f1b-ecc25639cec1 | -12.42909 | -53.1451 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| efeda106-2009-3a90-8d79-c258380f7d93 | -12.42382 | -53.14935 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 6d479133-a346-3cfb-8588-f5e140c9d662 | -12.42317 | -53.15427 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 8375fb46-8418-355d-abc5-9b257e3fe31a | -12.42251 | -53.15925 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| a67db031-68c2-3db2-801b-c940faf00c6b | -12.41919 | -53.14868 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 8fd9b397-5051-3f6f-92bb-3abc7be3c9e0 | -12.41855 | -53.15359 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 275df8d5-f59f-3ea1-98e9-8a127f366bac | -12.41789 | -53.15854 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| cc0e5f9b-2afd-340a-86b3-67c5171bf488 | -12.41724 | -53.16351 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| f6298973-200e-3b89-9ff4-28bc6e7c99de | -12.41392 | -53.15293 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| b2364913-4b8d-3602-a385-a0152d85bc1c | -12.41327 | -53.15785 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 31.4 |
| b31ef6a5-229e-3397-b90b-8ba7c95861a9 | -12.41263 | -53.16278 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 31.4 |
| 480153bf-2265-335a-88df-3edc9e02a921 | -12.41197 | -53.16775 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 8fd1afd2-4e6e-3e22-86c1-762223fd0cb7 | -12.4093 | -53.15228 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 37ebb464-1104-344b-a6dd-8e512d9f629f | -12.40865 | -53.15718 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 31.4 |
| 0bb83245-e5ea-369a-a46e-7f5b9598000c | -12.40801 | -53.16209 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 31.4 |
| 91560d32-7a51-3a9b-b527-f0d4c8d1543f | -12.40736 | -53.16701 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 10.2 |
| efcf84ef-1138-3988-a305-d2677f1f1027 | -12.9987 | -53.47152 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ae4ab5c7-ee87-32bf-83a4-d6960ca644c4 | -12.99413 | -53.47095 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 08d67732-0d69-3048-81c5-dcc9052988c2 | -12.99167 | -53.48996 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b436e1df-0e50-352f-8587-aa6499d75b96 | -12.98956 | -53.47032 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1b93dbf8-fecf-3bed-8280-e6dcae11fec0 | -12.98711 | -53.48932 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 5f292c72-cac7-3973-9221-abee82d464b1 | -12.97984 | -53.47367 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 49e0eb1d-907a-3f0d-bebe-d089e0e70ba8 | -12.97922 | -53.47845 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b7c61ce0-874b-3a22-9170-d60a165850ce | -12.97465 | -53.47786 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a729d6d5-4764-3b1e-89a4-82d85f520ad1 | -12.97404 | -53.48267 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5e4e9647-1db2-32df-bf76-837fea0cafda | -12.97342 | -53.48747 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 33ff27d9-47a3-378c-9957-2f2b0e63caf5 | -12.89555 | -53.47476 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| de14b108-ff7f-3c45-b255-be19bcbb3fc5 | -12.89493 | -53.47951 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 122dd2be-4544-328a-be8b-d4a684aa3f40 | -12.89431 | -53.48426 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0735e275-9bb6-302b-9fdc-ea87cfdae081 | -12.891 | -53.47405 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 991e98db-63d0-3b8c-b9fb-a595e0aa0e4c | -12.89038 | -53.47881 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5bc48d59-3559-3e5c-b97a-ee79d5671f10 | -12.88977 | -53.48357 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 624834e0-0760-31f5-ae02-093fb4083210 | -12.88915 | -53.48833 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 16b59bc7-c30e-3f35-b66b-f3e4d24fd478 | -12.88583 | -53.47815 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 575ab6ac-05cd-325c-a999-3b68916271a3 | -12.88521 | -53.48293 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b58bee21-a222-3c1f-bcb8-e6e4b1f3be91 | -12.88459 | -53.48769 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 64492275-726f-30f2-9df5-4a23d6101b1c | -12.88189 | -53.47275 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 644b4409-6a73-3b9e-bdc7-8e7b4e9cbaf6 | -12.88127 | -53.47754 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0b5b8e0b-5fcd-3f28-91cb-1a9bb9ce4eb9 | -12.88066 | -53.48232 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 12.1 |
| bfaf2bb9-d590-3106-b295-fb044b753eda | -12.88004 | -53.48708 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 6d4e3fd6-5974-3c33-ad68-173b08523574 | -12.87943 | -53.49181 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| f989e658-1a8e-3503-a230-8c73d9d30f21 | -12.87733 | -53.47215 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README100.md)
