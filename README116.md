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

## Dados Diários - Página 116

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 24ef15f8-4edd-3ec8-b0c3-dc019b4ce05a | -15.18165 | -48.07459 | 2024-10-05 04:40:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f131041d-b3d8-35c4-b632-836fd802c393 | -15.17969 | -48.06859 | 2024-10-05 04:40:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 019e7955-ce6a-39b6-8b02-cd58da63ab0f | -15.17863 | -48.06986 | 2024-10-05 04:40:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d9834c70-ee85-3716-b388-e81ace667fd6 | -15.17851 | -48.0771 | 2024-10-05 04:40:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 01de0e85-ff68-31b4-b6fa-6ee05e05024d | -15.17627 | -48.06059 | 2024-10-05 04:40:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f1afc3f4-05c5-3884-88d9-3e01ede44414 | -15.17564 | -48.06497 | 2024-10-05 04:40:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9f098323-79f8-3522-bff1-dd2d6304d176 | -15.17264 | -48.0601 | 2024-10-05 04:40:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8ede0d61-6602-3bc6-8980-8688adef03e3 | -15.16901 | -48.05955 | 2024-10-05 04:40:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 782609ca-ab6c-3920-b7e0-a5ae21bca67b | -15.16839 | -48.06388 | 2024-10-05 04:40:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 694d157b-a1a2-3397-8762-c25451d445dd | -15.14844 | -48.07385 | 2024-10-05 04:40:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4a298fec-029d-32fb-886e-e31409c5aca8 | -15.63745 | -47.17085 | 2024-10-05 04:40:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cec4b969-f263-3559-a940-20092516f3f5 | -15.62531 | -47.17409 | 2024-10-05 04:40:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b48f5ffb-e0fc-318e-968d-02923d353786 | -15.4334 | -47.42526 | 2024-10-05 04:40:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 710c960e-11e6-3ea5-a6c9-b0828cef8afd | -15.43152 | -47.68366 | 2024-10-05 04:40:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 49ca02bb-5919-3ac8-abcd-47e0ce3b39ca | -15.43032 | -47.41973 | 2024-10-05 04:40:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 63343891-6cbe-3f69-9d31-a80b06c62166 | -15.42845 | -47.67857 | 2024-10-05 04:40:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ae3f8d49-7c88-35ad-a558-52f6cb62bd5e | -15.4278 | -47.68317 | 2024-10-05 04:40:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ea5c67a4-f9f3-3eaa-8788-0e51b9e70289 | -15.42473 | -47.67809 | 2024-10-05 04:40:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 533cb603-af98-3273-a72e-3df8e4552a53 | -15.42392 | -47.71056 | 2024-10-05 04:40:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 23edafab-660c-3c19-8b8c-a2dc488ba6e9 | -15.42022 | -47.70998 | 2024-10-05 04:40:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 51a59f50-db48-3e65-aa35-bc38a9d2e8d7 | -15.40539 | -47.40544 | 2024-10-05 04:40:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 09152135-3bcd-3a6e-a592-128c92bbb248 | -15.40485 | -47.68483 | 2024-10-05 04:40:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 39c09f46-9a04-3cb1-bd54-5b58c621dc78 | -15.39723 | -47.40895 | 2024-10-05 04:40:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 18d5ffdf-791c-3285-a848-0837883fad0e | -15.39655 | -47.41395 | 2024-10-05 04:40:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4536bcd1-b822-3b24-b8e9-f7765513f20b | -15.3959 | -47.41874 | 2024-10-05 04:40:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 388fbab8-2207-3d1a-9298-72a3c05af3e8 | -15.39282 | -47.41311 | 2024-10-05 04:40:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8daa4bf8-4def-39d8-9da2-1068ffaf294c | -15.39217 | -47.41787 | 2024-10-05 04:40:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a4ff4e4b-403e-3e67-8f9d-eea9402c21ce | -15.27708 | -47.49899 | 2024-10-05 04:40:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 16fcdbbf-ff30-3218-9be8-764f8ba30d8f | -15.27334 | -47.49846 | 2024-10-05 04:40:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| aa98da96-0e56-30a5-ae5a-4f55cf94633b | -15.26959 | -47.49798 | 2024-10-05 04:40:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b309e3f1-fbd4-3490-83ea-b8b9ead42b9e | -15.25832 | -47.49665 | 2024-10-05 04:40:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c58bf7f2-69da-3605-a9a2-8016db3a6da8 | -15.25074 | -47.48747 | 2024-10-05 04:40:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e8a638ad-fa72-39cc-9540-f7da25522701 | -15.24627 | -47.49204 | 2024-10-05 04:40:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b61fcbfa-a662-38d4-b16b-fa758a686417 | -15.22697 | -47.49353 | 2024-10-05 04:40:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| def059c4-1956-3e18-816f-0330dfb91104 | -15.22255 | -47.49785 | 2024-10-05 04:40:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e5c55e4a-a794-348c-a0f8-80d9e09b9def | -15.21885 | -47.49702 | 2024-10-05 04:40:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fe76187b-24ba-3c65-b10b-c83cb5845b7f | -19.14816 | -48.22575 | 2024-10-05 04:40:00 | NOAA-20 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3716e217-f23c-3801-9900-25391d88a8a0 | -19.14042 | -48.95288 | 2024-10-05 04:40:00 | NOAA-20 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5d06ffb0-4555-37b0-b98a-f56850f76b63 | -19.13753 | -48.21918 | 2024-10-05 04:40:00 | NOAA-20 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 64cb90ec-6b14-34ad-9580-e9a31651de8f | -19.09036 | -48.22703 | 2024-10-05 04:40:00 | NOAA-20 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a03e83e5-d7c7-374b-88ca-b48e6890f3c4 | -19.08973 | -48.23176 | 2024-10-05 04:40:00 | NOAA-20 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9fc3d358-ae68-3755-a9df-7e235ed73984 | -19.0891 | -48.23649 | 2024-10-05 04:40:00 | NOAA-20 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e82a517f-4cb1-3d48-b987-e26067989ee5 | -19.08156 | -48.23545 | 2024-10-05 04:40:00 | NOAA-20 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c0b7cf01-1f77-37e1-9668-a99b69d94030 | -19.08092 | -48.24021 | 2024-10-05 04:40:00 | NOAA-20 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 25b1d95d-a7e2-3e0a-849b-4fbbfbb8db52 | -18.79033 | -48.44359 | 2024-10-05 04:40:00 | NOAA-20 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 83b5c179-a6db-36f3-9e65-14d4cd004e2c | -20.92647 | -49.01784 | 2024-10-05 04:40:00 | NOAA-20 | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 257598af-008d-3503-b047-b13f41eae9da | -20.93016 | -49.0184 | 2024-10-05 04:40:00 | NOAA-20 | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 074699f2-0282-3516-a4ec-65ad4a8fc2af | -20.92708 | -49.01325 | 2024-10-05 04:40:00 | NOAA-20 | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 2fa192cd-3620-32bd-b633-6742e10db3b0 | -20.92954 | -49.023 | 2024-10-05 04:40:00 | NOAA-20 | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| df7e9972-3e09-38d3-a98d-06e2f97e7c62 | -20.92893 | -49.0276 | 2024-10-05 04:40:00 | NOAA-20 | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 20d343cb-8f4c-3d6a-b2ab-24d4cd5ff5e5 | -21.14033 | -48.44952 | 2024-10-05 04:40:00 | NOAA-20 | TAIÚVA | SÃO PAULO | Brasil | 3553203 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6ca9bbe5-1833-37fd-9511-5923b9316900 | -16.0845 | -50.44977 | 2024-10-05 04:40:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 30dddb1c-d8b6-3346-b66c-0f1f612a82a3 | -14.82511 | -48.81001 | 2024-10-05 04:40:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8c5a720f-309b-34b9-bde4-b5aa089101a9 | -14.82454 | -48.8139 | 2024-10-05 04:40:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5161f60f-46d5-3efb-a95b-b8aa79116634 | -14.82399 | -48.8177 | 2024-10-05 04:40:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 880c3015-4546-3614-9d5e-f5f0e865ef58 | -14.82343 | -48.82149 | 2024-10-05 04:40:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 938e1548-4b45-389a-a266-146f3e2f70d1 | -14.82161 | -48.80952 | 2024-10-05 04:40:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fd2e6fcd-2fa2-3c82-aec5-b49780e0e9e2 | -14.82105 | -48.81339 | 2024-10-05 04:40:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 81a02153-2d1b-3cd6-8d4b-e4564393ff17 | -14.81995 | -48.8209 | 2024-10-05 04:40:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4227acaa-47f0-3e1b-be0e-42eea6034a42 | -14.81757 | -48.81281 | 2024-10-05 04:40:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| aa6b0b55-66f6-37d2-b7c9-05442ca10239 | -14.81409 | -48.8122 | 2024-10-05 04:40:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2aed290b-f6c4-34db-8072-913f3c482398 | -14.81005 | -48.81538 | 2024-10-05 04:40:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8a8df92c-5570-3620-b9b6-ccac296db45d | -14.80714 | -48.81088 | 2024-10-05 04:40:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f73399a6-08c1-35b2-8055-b52fd1e802c0 | -14.80658 | -48.81475 | 2024-10-05 04:40:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f033ae83-aa28-3ccb-bf44-b89a476b612a | -14.80367 | -48.81022 | 2024-10-05 04:40:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 943b3783-6955-36f2-9a78-2196aca6b8d9 | -14.8031 | -48.81411 | 2024-10-05 04:40:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 5d512505-c818-37b4-9c9d-9307b8df7edb | -14.79906 | -48.81734 | 2024-10-05 04:40:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| ac02dd65-8268-3ddf-8fed-34a9ae12c52c | -14.689 | -48.78106 | 2024-10-05 04:40:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 8d81761b-6f09-3059-b422-de0b033561b1 | -14.68608 | -48.77659 | 2024-10-05 04:40:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 81f0f008-2108-3456-bd71-72c3958730fd | -14.68552 | -48.78046 | 2024-10-05 04:40:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7b17db1d-9847-3eb4-8814-c6a5643a3ce3 | -14.6826 | -48.77601 | 2024-10-05 04:40:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 466e0350-4413-3e4a-b555-43eadcda9f27 | -14.67911 | -48.77542 | 2024-10-05 04:40:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1ebc10bc-8ed2-33ea-b993-dfd39e14cde8 | -14.67563 | -48.7748 | 2024-10-05 04:40:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 610e2c88-e82f-394c-8efe-c88e31ae3645 | -14.67091 | -48.75809 | 2024-10-05 04:40:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 5516c21f-b1bb-38d9-be95-5ebe3f43e732 | -14.67035 | -48.76195 | 2024-10-05 04:40:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| afed48e8-22a7-3363-b1b1-d9ef0b99082e | -14.66744 | -48.7574 | 2024-10-05 04:40:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a9a1ed90-4beb-38fd-bc62-5180a13f5c04 | -14.66687 | -48.7613 | 2024-10-05 04:40:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 574b2d8c-3fe0-3c1f-bfc7-accc8d480876 | -14.66631 | -48.76519 | 2024-10-05 04:40:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d484b2c7-bd03-3510-823a-96221594666b | -14.6634 | -48.76064 | 2024-10-05 04:40:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 27e0bc21-fc34-3094-920a-18582ccacc2d | -14.65991 | -48.76003 | 2024-10-05 04:40:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 58c4be0e-9340-3c7a-856d-3c8cb4cef01c | -14.58103 | -48.82687 | 2024-10-05 04:40:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 0481d83c-4a2b-33c6-b7ac-43dc3c1a7c15 | -14.58046 | -48.8308 | 2024-10-05 04:40:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 6d2f40da-2bc5-331c-b0d3-b5e8bbd6659e | -14.57754 | -48.82635 | 2024-10-05 04:40:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c10dba4f-519b-3b50-a9d5-7e07b15e9ee7 | -14.57697 | -48.83027 | 2024-10-05 04:40:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ca16c0ac-8972-32d4-af4d-f5091b462bbc | -14.57523 | -48.81787 | 2024-10-05 04:40:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 50518c9c-353a-3640-b0a0-1097596f2c85 | -14.57464 | -48.82188 | 2024-10-05 04:40:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b70b792a-2dc6-3861-a227-603fa93f7164 | -14.57406 | -48.82581 | 2024-10-05 04:40:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b0d8e415-a6d9-3722-a4c1-160e93b89569 | -14.57349 | -48.82973 | 2024-10-05 04:40:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c1f88547-7b3b-386e-9ecd-b8a4b61a7376 | -14.57174 | -48.81734 | 2024-10-05 04:40:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| e047ef69-4b54-308f-ade4-5cf9472eae83 | -14.56825 | -48.81689 | 2024-10-05 04:40:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| a463437e-1a4b-376d-82fb-3d1e9129ece8 | -14.56651 | -48.80437 | 2024-10-05 04:40:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 644b98ef-cc52-398d-8572-310ac6c7db84 | -14.56475 | -48.81649 | 2024-10-05 04:40:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 3d3c90b4-bb45-3ba3-849a-889a56a2b018 | -14.56301 | -48.80393 | 2024-10-05 04:40:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 894e90c5-840a-385c-933b-d91819bfe779 | -14.56242 | -48.80801 | 2024-10-05 04:40:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6a794535-5816-37c6-b32a-d329ecc1e294 | -14.56183 | -48.81205 | 2024-10-05 04:40:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 8278af86-1095-3877-8907-923e8c525a4e | -14.56126 | -48.816 | 2024-10-05 04:40:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| b38faded-629b-38e5-8106-a4cf3be6875c | -14.5601 | -48.79943 | 2024-10-05 04:40:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 0fad66b8-0749-3ab8-b9d9-21926e673a1b | -14.55952 | -48.80346 | 2024-10-05 04:40:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 7852804d-1d2b-3e37-9dd1-bd21a2a2ff3b | -14.55661 | -48.79899 | 2024-10-05 04:40:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 8438f4cc-2eda-3529-aaa3-12def879f612 | -14.55602 | -48.803 | 2024-10-05 04:40:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 9.5 |


[Clique aqui para ver as próximas entradas](README117.md)
