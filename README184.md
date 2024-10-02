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

## Dados Diários - Página 184

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9091106a-c2c2-3073-bad8-dc09169ba6e9 | -16.74144 | -57.47937 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 20e1d617-0d28-37fc-bffb-72ac2a0e99cc | -16.74109 | -57.48238 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 9fa9544f-ed1f-33a3-8ecc-57150016e923 | -16.73172 | -57.47509 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 06e69d9e-56e8-39c5-9684-dd0ea4347760 | -16.73137 | -57.4781 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 54aa5ece-6147-3dac-89a2-0c7c0d249c7e | -16.72824 | -57.50513 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 3d5a7342-791f-3161-b832-049b008fa23b | -16.72599 | -57.48048 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 1b26a950-94b3-38ed-9483-1a3ed47da0c8 | -16.72234 | -57.46781 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 003be4eb-5b60-34f8-b4e2-83d2bac9ec1e | -16.72199 | -57.47083 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 5c431957-c9c6-37be-8f91-6a4567490f24 | -16.72164 | -57.47383 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| eb24d8fa-9f81-330c-83ff-4eceddad485c | -16.71695 | -57.4702 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| d71847eb-9188-3ffc-b5d0-1a49ca177b07 | -16.7166 | -57.47321 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| f7bca28c-4877-3106-862b-ac94090fb5ef | -16.69646 | -57.47068 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 10.1 |
| 59c5c504-be66-3d74-9ffd-697309e9e141 | -16.69612 | -57.47369 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 10.1 |
| 9cbaf5d4-5044-39fa-9bfb-3ab18b8bb728 | -16.69578 | -57.47668 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.7 |
| b46488db-db8d-3163-bdde-1da43ac15410 | -16.69075 | -57.47606 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.7 |
| a021fcae-5f6c-3383-8bf9-c45e63df9fdd | -16.69041 | -57.47906 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.7 |
| 2e314fcc-8b65-37ff-943f-b5269c48f6bc | -16.67733 | -57.4591 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 01e84b74-2467-336f-9733-434242540ddd | -16.66777 | -57.46026 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 988d64dc-7575-3782-81d8-c01d86930cdd | -16.66741 | -57.46328 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 87eb912b-8332-377e-aa8d-1f5c5e0120c9 | -17.20557 | -57.37821 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 1de9639a-2edc-30ef-a3ed-fd4b9e13160a | -17.20083 | -57.37449 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 86019c2c-43ff-3ea1-b1e2-56af54f5606a | -17.20047 | -57.37759 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 437097e4-170e-30e4-be13-9849df1b73dc | -17.20011 | -57.38068 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| b3c5e974-4e6a-3b03-bbe6-9931ef10395e | -17.19572 | -57.37386 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.6 |
| c96497f7-46e1-3a91-a396-6b4ce21def22 | -17.19537 | -57.37696 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.6 |
| 5d80dc52-ec7d-3389-99d1-4c5410a1334f | -16.78921 | -57.36656 | 2024-10-02 05:36:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| e2a9230e-5bdb-32e4-a642-d4d6832e6fcf | -16.78887 | -57.36962 | 2024-10-02 05:36:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 6549a814-199d-3173-8a86-fe504ba07138 | -16.78565 | -57.36472 | 2024-10-02 05:36:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| f5bb40e2-1f54-33d5-9399-416e81d7f24a | -16.78528 | -57.36777 | 2024-10-02 05:36:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 627f0aef-0834-31bd-9296-c1427f5e8bf5 | -16.78493 | -57.37083 | 2024-10-02 05:36:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 946f012d-5607-3fc8-9d53-d193c3d356bb | -16.77949 | -57.37328 | 2024-10-02 05:36:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| c6193a67-1a18-3e45-aaa3-53bb5c996b71 | -16.77482 | -57.41294 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 2d321f74-761e-303e-8d9c-78e1692d6740 | -16.77446 | -57.41598 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| f0539ed6-d7eb-37ca-9e03-d005855b1432 | -16.77041 | -57.36284 | 2024-10-02 05:36:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 6e49d183-1625-32bf-ab1e-824e08d2ebb7 | -16.77006 | -57.3659 | 2024-10-02 05:36:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| f0c2fdd4-04c0-31a3-bc13-271277776440 | -16.7697 | -57.36896 | 2024-10-02 05:36:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| a7d58d1d-b416-3000-876f-b41e560b00a7 | -16.76941 | -57.41536 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 25d6ddff-5132-3f42-b7a3-2a99f7982dba | -16.76934 | -57.37202 | 2024-10-02 05:36:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 55f816ab-480d-3676-9741-6322eeb2c649 | -16.76905 | -57.4184 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 3c32b0b3-f80d-365f-bd20-4771371eceee | -16.76898 | -57.37508 | 2024-10-02 05:36:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 106105df-6fb8-374f-8ff2-b3c88785752c | -16.76869 | -57.42144 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 79b96d98-07a0-3ef3-9ff8-a9bccac6d69a | -16.76863 | -57.37814 | 2024-10-02 05:36:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| cd9cf4fc-290d-3c5b-ac4b-c9866fa4edf1 | -16.76834 | -57.42447 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| b89602f9-243f-393e-8336-cc5e99caba71 | -16.76827 | -57.38119 | 2024-10-02 05:36:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 32f4b7b2-2982-323d-ba12-65322999ac64 | -16.7672 | -57.39035 | 2024-10-02 05:36:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 9b7181e9-185f-33ae-b7ab-c4fb122c80e8 | -16.76391 | -57.37445 | 2024-10-02 05:36:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| d3f150f1-ce43-38c0-b820-b2fce1cd0a91 | -16.76355 | -57.37751 | 2024-10-02 05:36:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 0fe2e036-f5d5-3d7c-bd79-91b25865d50c | -16.76328 | -57.42382 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| ce5fb6a3-4cfc-3dae-a2ca-c5778311bcd0 | -16.7632 | -57.38056 | 2024-10-02 05:36:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| f7f1cd0d-ff30-3b34-8322-2dfaac4e1ba3 | -16.7467 | -57.43409 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 23afb3d1-ab87-3cb7-bc13-1602e8cc9d06 | -16.74292 | -57.37805 | 2024-10-02 05:36:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 6e76ee77-802b-337a-9e26-178284f8d40a | -16.74257 | -57.3811 | 2024-10-02 05:36:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 30d68265-7abe-3318-9c39-09f416f97595 | -16.74221 | -57.38416 | 2024-10-02 05:36:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 8d49243e-88a5-368d-9921-2e9745c0b5fe | -16.74165 | -57.43346 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 7c891e1c-0a89-3368-81e6-beedc0eb3818 | -16.7413 | -57.43648 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 1cc60c66-7f53-3e68-b40d-f7b010141dce | -16.73784 | -57.37742 | 2024-10-02 05:36:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 131b1098-4739-3bfb-8e5a-f21364616dd1 | -16.7366 | -57.43281 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| e3f84714-5450-32df-9fb3-efe0b0f3c453 | -16.73625 | -57.43583 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 7103e7fc-11c8-3b56-b3f1-6160a126c3a5 | -16.73155 | -57.43219 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| e36bac2a-a8b3-359a-bd7a-7d48b89eb868 | -16.7312 | -57.43521 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 4000717d-4114-349c-9584-5127a598d5c6 | -16.72719 | -57.4255 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 10.5 |
| 456d95aa-5b20-31ba-95f1-1ce259a96ac6 | -16.72685 | -57.42853 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 10.5 |
| 17ed58ec-9eb1-33ef-b5cb-85b7f170c809 | -16.7265 | -57.43156 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 97cfae57-00b7-31e9-80ff-4185536421c1 | -16.72615 | -57.43458 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| e61dffe5-d2b6-3f10-9b49-96e092463c71 | -16.72318 | -57.41576 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| bdbabf63-ce70-3cb3-bf8a-a43fc405a0ad | -16.72284 | -57.4188 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 6be1d079-fe58-3af8-a452-7cff7f83154c | -16.72249 | -57.42183 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 3b179a63-0209-3033-816d-34747b552503 | -16.72214 | -57.42486 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.2 |
| bc4a1ea7-e574-3cac-a653-7bc4ac507734 | -16.72179 | -57.42789 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.2 |
| 6e4d8d37-3d7a-35b1-9d14-c08303484c8e | -17.00509 | -57.96428 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| d0b4bf2a-e5a3-3f26-a999-8f4fd8efd676 | -16.99954 | -57.96928 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 3934988f-330e-386d-a5ee-551e32d608c1 | -16.91328 | -57.7064 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 11.3 |
| 80161fbd-8f1f-3b92-8fd5-f2cca9194726 | -16.9126 | -57.71225 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 11.3 |
| 6a8285c9-87a3-3916-8b6b-5344cdc13c9c | -16.90831 | -57.70578 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 11.3 |
| 54ff8189-6476-3ca1-b791-21d0e19e7a30 | -16.90763 | -57.71162 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 11.3 |
| 0bae8951-8cd4-39fd-a88f-92f17efdecdf | -16.90401 | -57.6993 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.3 |
| 8628cc8c-fc3a-34e5-b69a-f3079d85dda8 | -16.90334 | -57.70515 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 16.1 |
| dc05d3d1-fb41-38c6-bd61-ac79ac572988 | -16.90266 | -57.71099 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 16.1 |
| 47de06b1-4e30-3560-9922-dbc4553ea923 | -16.90132 | -57.72266 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 57d666f1-90b5-36c7-ba6e-46ee4987c02e | -16.90038 | -57.68695 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.5 |
| e2dc0971-49d0-32ba-8f74-19e7b8017ea1 | -16.89904 | -57.69868 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.3 |
| 4e960659-6c12-31c5-8b10-c85efe01f67a | -16.89837 | -57.70452 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 16.1 |
| 04e46796-a731-31fc-9438-111c1987e7fc | -16.8977 | -57.71036 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 16.1 |
| 431c4603-3ea0-3217-b21c-f8466b384ca5 | -16.89703 | -57.71618 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 8cac2938-b31c-3176-8520-c1554865b230 | -16.89636 | -57.72202 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 96d2e59e-afb7-389f-98f3-4eebfbd18053 | -16.8954 | -57.68632 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 32.8 |
| e036b7d7-5da4-3005-80c5-cf03c8fbc064 | -16.89473 | -57.69218 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 15.3 |
| 83731d35-44ec-32fd-96b5-87d9b72d1f5d | -16.89406 | -57.69805 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 15.3 |
| 5cdad099-3ed6-3387-a095-8edd6f34bc0f | -16.8934 | -57.7039 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.0 |
| 6879a534-4665-3d73-a5a9-fe9e95363950 | -16.89273 | -57.70973 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.0 |
| 10d19db9-7d4b-3f74-8c77-9168c368f91e | -16.89206 | -57.71557 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 8952b644-51cb-3137-a320-0dde866eb4f0 | -16.88976 | -57.69156 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 15.3 |
| 479d3bf2-1fab-3031-a53a-36db0608d8a4 | -16.88909 | -57.69741 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 15.3 |
| 5f64b0f6-8791-3aec-94db-de9823a4af36 | -16.88709 | -57.71495 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 1e36165e-fa43-30a3-984a-a1ac1aaf7051 | -16.88545 | -57.68507 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.6 |
| b26a424f-cdbe-3794-b0c1-87733366a695 | -16.88478 | -57.69093 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.9 |
| 07521b8f-2144-313d-846b-8243bd12b3f0 | -16.88412 | -57.69678 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.9 |
| 9d48c673-8056-3379-b93a-0e128be1b107 | -16.88047 | -57.68444 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.6 |
| 1c03662d-1d47-3d32-9dc5-bdbcde6f1069 | -16.87981 | -57.6903 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.9 |
| 76e65d4c-3982-36dd-a83a-51a3fc4220fe | -16.87932 | -57.68927 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.5 |


[Clique aqui para ver as próximas entradas](README185.md)
