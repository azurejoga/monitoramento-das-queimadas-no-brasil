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

## Dados Diários - Página 125

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6f41e45f-5f1b-3ee8-9da1-235eb260536c | -16.87997 | -57.70074 | 2024-10-02 04:51:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| c82b39fb-5533-3178-bf05-8e5eaaf48d96 | -16.87996 | -57.69902 | 2024-10-02 04:51:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 2c3e8e73-1727-3453-ba93-6f0aad0e701f | -16.87909 | -57.70384 | 2024-10-02 04:51:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| bd482d3d-80d5-3a6e-b34d-3d8ba30dae69 | -16.87872 | -57.68556 | 2024-10-02 04:51:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.1 |
| 05eb54e7-eecf-31fe-9508-e269942b2382 | -16.87793 | -57.68869 | 2024-10-02 04:51:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 10.0 |
| 8026a457-66c3-3428-8756-0da32bd4da7a | -16.87788 | -57.69037 | 2024-10-02 04:51:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.1 |
| 61b3dc55-dc2f-3c3f-8c1b-3f1a289ea518 | -16.87706 | -57.69349 | 2024-10-02 04:51:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 82140a68-3296-3f66-9213-3b2c6d46a79c | -16.87703 | -57.69519 | 2024-10-02 04:51:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 9669def4-01f5-304d-be64-48b4dfd9f129 | -19.10917 | -57.49821 | 2024-10-02 04:51:00 | NOAA-21 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 8496b388-256f-3c93-bdee-fc33ef7b404d | -16.87619 | -57.70002 | 2024-10-02 04:51:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| c22059d7-5459-3d8f-9f71-a9bfe341e613 | -16.87618 | -57.6983 | 2024-10-02 04:51:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 4f251078-b908-34c1-bdc5-a64e7410a502 | -16.87531 | -57.70311 | 2024-10-02 04:51:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| eb6ea0f9-131a-3283-a5ee-8b3de28edf71 | -16.87494 | -57.68483 | 2024-10-02 04:51:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 9dba6d51-2fb5-36d3-985c-3b516c950b6a | -16.87325 | -57.69447 | 2024-10-02 04:51:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 0b1a8320-2e6c-35a2-bc80-66d53f8503c4 | -16.8724 | -57.6993 | 2024-10-02 04:51:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 347e856b-0692-379a-82f0-480e732a290d | -16.87116 | -57.68412 | 2024-10-02 04:51:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 9d627e9d-3942-3842-b62f-b51318bb2ca6 | -19.10826 | -57.50323 | 2024-10-02 04:51:00 | NOAA-21 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 3.4 |
| f609fb1e-d135-3c40-91a6-c5942e1fab1f | -17.13756 | -56.73483 | 2024-10-02 04:51:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 5de38f3f-bf7d-3273-b083-0bcee0dadec4 | -17.13683 | -56.73912 | 2024-10-02 04:51:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 494d9276-aff9-34ef-8e48-b09e1f689f36 | -17.13324 | -56.73845 | 2024-10-02 04:51:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 15.2 |
| 6081ad32-75b9-388c-abec-449a319b5f67 | -17.1325 | -56.74274 | 2024-10-02 04:51:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 15.2 |
| 83560f4f-896f-35fa-be89-c8fe27a47c0d | -17.12965 | -56.73778 | 2024-10-02 04:51:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 15.2 |
| 8b09fd57-cf5a-35b7-81a8-028bb2ae080e | -17.12891 | -56.74207 | 2024-10-02 04:51:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 15.2 |
| f4a9cb62-53cb-3667-b7b1-8c6d30088c00 | -17.11097 | -56.73873 | 2024-10-02 04:51:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| cd1211ab-6de4-33aa-9de9-5a36d11df4dc | -17.10949 | -56.74732 | 2024-10-02 04:51:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 52b8d6a9-9062-38c9-b595-a5bb540a36fd | -17.10874 | -56.75163 | 2024-10-02 04:51:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| aaf19fa4-7c8a-366c-9246-7c52ed212194 | -17.10799 | -56.75593 | 2024-10-02 04:51:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 6198257f-ac20-32a4-b71e-fee4be757a4b | -17.10738 | -56.73805 | 2024-10-02 04:51:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| c064529a-e563-3a12-9883-648295094554 | -17.10725 | -56.76024 | 2024-10-02 04:51:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 25.7 |
| 4aa33e00-2514-39bd-8922-831ed56435ea | -17.10664 | -56.74235 | 2024-10-02 04:51:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 13fb467e-f327-3da1-addd-e45def0c27d8 | -17.1065 | -56.76455 | 2024-10-02 04:51:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 25.7 |
| f782d319-e28e-3642-8332-a20b83519e93 | -17.10589 | -56.74665 | 2024-10-02 04:51:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 14c399c0-4459-398e-9f7f-e8e2332e1cb0 | -17.10515 | -56.75096 | 2024-10-02 04:51:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 6db53f12-0295-37a6-8682-e8f99169c442 | -17.1044 | -56.75526 | 2024-10-02 04:51:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 64e392e3-6a81-3579-ab67-9d0fff4f38a5 | -17.10365 | -56.75957 | 2024-10-02 04:51:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 25.7 |
| 30d25ead-9628-3b9c-8677-9b329b8f4a1e | -17.10291 | -56.76389 | 2024-10-02 04:51:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 25.7 |
| 66178189-c282-3a16-bb9a-dbe41b608e97 | -17.1023 | -56.74598 | 2024-10-02 04:51:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 8b7db9b9-dfa0-3727-b4c5-d7177c9f7eb8 | -17.10216 | -56.7682 | 2024-10-02 04:51:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| e1a6b466-ecc8-3394-8e6b-129a6ab894d6 | -17.10156 | -56.75029 | 2024-10-02 04:51:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 34df2972-85a9-382e-8d9f-c4baf9df2cae | -17.10081 | -56.7546 | 2024-10-02 04:51:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 7d4fe13c-292f-365b-81d8-4a61fc6f8694 | -17.10006 | -56.75891 | 2024-10-02 04:51:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 75.2 |
| ca41ab04-3153-3a2a-b324-a413327fd7f1 | -17.09932 | -56.76322 | 2024-10-02 04:51:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 75.2 |
| a2134432-ccb8-3a0e-8fae-df2261a3fbf6 | -17.09871 | -56.74532 | 2024-10-02 04:51:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| c78a0161-e936-3d22-a728-76717964db6b | -17.09857 | -56.76753 | 2024-10-02 04:51:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 20.8 |
| 8ba62d6d-bf4e-329a-b98e-6ef215e8ef48 | -17.09797 | -56.74962 | 2024-10-02 04:51:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| dc8b87c8-2911-3e05-a6ce-258858e772e7 | -17.09722 | -56.75393 | 2024-10-02 04:51:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| f8eb5bac-853c-3b64-b337-147197609495 | -17.09647 | -56.75824 | 2024-10-02 04:51:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 75.2 |
| 6dfdbcc6-63f2-3514-9470-fb9a77b7096c | -17.09572 | -56.76255 | 2024-10-02 04:51:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 75.2 |
| 1ea119a5-defb-33c8-a448-38bf7850b19f | -17.09497 | -56.76686 | 2024-10-02 04:51:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 20.8 |
| 0cc4297f-5639-3e97-9d0f-6bf5aad7cd25 | -17.09438 | -56.74895 | 2024-10-02 04:51:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| ae168b0c-dd07-3625-af39-8f8d91f34bff | -17.09363 | -56.75326 | 2024-10-02 04:51:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 62fa22df-cb5b-3983-8e11-6464b4d113b8 | -17.09288 | -56.75756 | 2024-10-02 04:51:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 14.3 |
| d7db5541-6e6f-3104-9c31-bb4c891b9b2b | -17.09213 | -56.76188 | 2024-10-02 04:51:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 14.3 |
| b32adaff-e3a1-3dfa-97be-1be75ebab5ad | -17.09138 | -56.76619 | 2024-10-02 04:51:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 35.1 |
| 2f533c4c-9520-3d0c-8e02-2ca0b092672f | -17.08928 | -56.7569 | 2024-10-02 04:51:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 14.3 |
| 7330f3a4-8aba-3c4b-9ee2-42babf2d31a3 | -17.08853 | -56.76121 | 2024-10-02 04:51:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 14.3 |
| 7f74423f-2bef-3484-8e47-627088e71d2b | -17.08779 | -56.76552 | 2024-10-02 04:51:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 35.1 |
| 7f52a71a-f8d5-3ef2-9af8-dbfdd8df7e41 | -17.08569 | -56.75623 | 2024-10-02 04:51:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.8 |
| 8f745fd3-26de-34c5-b76b-183bf22d4f92 | -17.08494 | -56.76054 | 2024-10-02 04:51:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.8 |
| 1c3697bc-6313-3051-9277-f40314e079ac | -17.08419 | -56.76485 | 2024-10-02 04:51:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.7 |
| 63432723-5c39-3ffb-9d90-aa2662e66a99 | -17.08135 | -56.75986 | 2024-10-02 04:51:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.8 |
| fe822e56-c0e8-3e45-a8dc-a193e1680e35 | -17.0806 | -56.76417 | 2024-10-02 04:51:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.7 |
| 75669d4b-433e-39eb-8870-47ddbc639ab6 | -17.07985 | -56.76848 | 2024-10-02 04:51:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.7 |
| 86ab70ca-5181-392d-ac20-2d64fbc34ab9 | -17.07625 | -56.76781 | 2024-10-02 04:51:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.4 |
| ffc65b39-b47a-3790-9e0c-75bf6f6fa788 | -17.0719 | -56.77147 | 2024-10-02 04:51:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| d6f0af2d-9813-34f6-8a75-001e29267df2 | -17.0683 | -56.77081 | 2024-10-02 04:51:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.6 |
| d5540e3b-bc40-34ea-a53a-fd59c2d56f16 | -17.06471 | -56.77014 | 2024-10-02 04:51:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.6 |
| 555ce93d-1316-3323-8f17-9d2f842c40ea | -17.06395 | -56.77446 | 2024-10-02 04:51:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.6 |
| 63065aa8-ca8f-3e00-bad9-7d0166a53573 | -17.06111 | -56.76947 | 2024-10-02 04:51:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.7 |
| 6d0e6777-8bd0-34d1-b502-b7f9524d52fe | -17.06035 | -56.77379 | 2024-10-02 04:51:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.7 |
| 3f1569b7-b780-3995-bb01-a9bf0ea42701 | -17.05751 | -56.76881 | 2024-10-02 04:51:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.7 |
| 52c72a75-62b0-3271-bd55-3b4fc42ae4e0 | -17.05467 | -56.76382 | 2024-10-02 04:51:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.5 |
| db928a1d-09d9-36f1-9064-bd850da90ecf | -17.05392 | -56.76814 | 2024-10-02 04:51:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 11.2 |
| 795368ed-d9d6-31fa-9b14-6def5832f8b2 | -17.05108 | -56.76315 | 2024-10-02 04:51:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.5 |
| 15e348f3-4a7c-370f-bc58-8fe105d2211e | -17.05017 | -56.75934 | 2024-10-02 04:51:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.4 |
| 08141a7d-a63f-34af-a44d-3c7401c9cce8 | -17.04943 | -56.76366 | 2024-10-02 04:51:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.4 |
| 05710a11-808f-312b-b1da-cf2a61c3e579 | -17.049 | -56.75387 | 2024-10-02 04:51:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.1 |
| d0fb984a-8753-3760-b88a-85d86f06b29c | -17.04887 | -56.72353 | 2024-10-02 04:51:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| ccc5fe28-16e8-363f-a269-5f61802e7da6 | -17.04825 | -56.75818 | 2024-10-02 04:51:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.2 |
| 4e00963b-29a5-3f82-9cbf-52a881f2b765 | -17.04805 | -56.75005 | 2024-10-02 04:51:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| b3ae4100-a7d0-3539-b0c2-225b83fcf2f9 | -17.04769 | -56.74028 | 2024-10-02 04:51:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| d865b0b9-d2d0-3f1b-9141-70e9a94571df | -17.04749 | -56.76248 | 2024-10-02 04:51:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.2 |
| 681201ef-d7b4-3c90-bef2-e9ea20020726 | -17.04731 | -56.75436 | 2024-10-02 04:51:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 9bd7c3eb-8313-35e4-adf3-3fb23dada430 | -17.04693 | -56.74459 | 2024-10-02 04:51:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 528fa18b-01a6-344d-b5c1-b534f11fe350 | -17.04658 | -56.75867 | 2024-10-02 04:51:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.4 |
| c788518f-75b0-32a2-835d-f5f76e919439 | -17.04617 | -56.7489 | 2024-10-02 04:51:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.1 |
| 451799ce-2fc4-3bad-8e01-eb1e47015f41 | -17.04593 | -56.74075 | 2024-10-02 04:51:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| c135e129-bf4a-33a6-8a44-f0eb01f53e38 | -17.04541 | -56.75321 | 2024-10-02 04:51:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.1 |
| 7b842e6b-04d7-39c5-af9d-f6741285d409 | -17.04528 | -56.72286 | 2024-10-02 04:51:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 6a768942-d158-3148-83c8-87e9e3c1540f | -17.04519 | -56.74506 | 2024-10-02 04:51:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| 9f0af748-b777-3fa2-91fa-fe70ba3c6dae | -17.04465 | -56.75751 | 2024-10-02 04:51:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.2 |
| 200e8dd6-7d7b-348d-9e12-b0fa4a9c3927 | -17.04445 | -56.74937 | 2024-10-02 04:51:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 59a1f928-40f6-3b7e-9928-ee6fffa3c10f | -17.04372 | -56.75369 | 2024-10-02 04:51:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| a7a813bd-f801-3712-af05-e7848621e2f0 | -17.04307 | -56.73577 | 2024-10-02 04:51:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 8c7d905d-e604-3cb5-a4f8-0f024c494031 | -17.04234 | -56.74008 | 2024-10-02 04:51:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| 8324add3-6f12-3d2e-8f18-86ae821a35eb | -17.04169 | -56.72219 | 2024-10-02 04:51:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 75aba5dd-1d4d-3ba1-8424-08045507ef49 | -17.04095 | -56.72649 | 2024-10-02 04:51:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| b0a0baf4-befa-31bb-a000-d4c21bf2cfe7 | -17.04022 | -56.7308 | 2024-10-02 04:51:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 7a8859c8-700b-393c-8911-20e2d3d67268 | -17.05382 | -58.03111 | 2024-10-02 04:51:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| e92c24c4-d322-32ab-9c7c-0b158f8d0158 | -17.03438 | -58.04079 | 2024-10-02 04:51:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |


[Clique aqui para ver as próximas entradas](README126.md)
