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

## Dados Diários - Página 156

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b87c9bc9-4b77-3ff8-81d3-4cd5d011b8fb | -7.06309 | -64.22378 | 2024-09-26 05:46:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3df3b7f1-4c6e-3e18-a3c2-bbc6ee60de04 | -7.0033 | -64.21124 | 2024-09-26 05:46:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3bc74c87-3218-39f0-80f9-4fecb13d4d69 | -6.93042 | -64.24063 | 2024-09-26 05:46:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d03fbf6f-f442-3f63-9e29-2eb8aa45a153 | -6.83419 | -64.30335 | 2024-09-26 05:46:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ebb97613-13e1-3dd4-8765-5cb4d66183ca | -6.82832 | -64.31844 | 2024-09-26 05:46:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 4bc4d69a-355b-3058-98a7-bcc8b26acc20 | -6.82482 | -64.31792 | 2024-09-26 05:46:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 113ad0f7-ece8-3021-8b16-dd56dd994b18 | -6.82132 | -64.31738 | 2024-09-26 05:46:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dafe735c-7a5a-3198-97ed-4fe2fbb37f63 | -6.72898 | -64.37553 | 2024-09-26 05:46:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 955d4b85-dde0-35d9-a034-dee71336c2fa | -6.7127 | -64.36511 | 2024-09-26 05:46:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 52e8bd87-2722-35f2-a715-3a8fe95aad44 | -6.71212 | -64.369 | 2024-09-26 05:46:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1a26e910-a113-3cbb-a640-bfcb8f2f2768 | -6.70863 | -64.36846 | 2024-09-26 05:46:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 80cc449d-338e-3763-9b96-2e7723112094 | -3.76224 | -69.47186 | 2024-09-26 05:46:00 | NOAA-20 | TABATINGA | AMAZONAS | Brasil | 1304062 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 98d782ac-ad50-3ff9-8996-0ce38124b98e | -3.7034 | -69.39753 | 2024-09-26 05:46:00 | NOAA-20 | SÃO PAULO DE OLIVENÇA | AMAZONAS | Brasil | 1303908 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1dcd4bda-ff31-3daf-a0fc-765a8e3dc5e1 | -3.70271 | -69.40173 | 2024-09-26 05:46:00 | NOAA-20 | SÃO PAULO DE OLIVENÇA | AMAZONAS | Brasil | 1303908 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0654fddd-d936-3f7b-96a0-7bd669823c49 | -3.70264 | -69.39895 | 2024-09-26 05:46:00 | NOAA-20 | SÃO PAULO DE OLIVENÇA | AMAZONAS | Brasil | 1303908 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 1d7faa8d-8fc2-3105-8580-26bf5dce6b37 | -3.60108 | -64.58946 | 2024-09-26 05:46:00 | NOAA-20 | TEFÉ | AMAZONAS | Brasil | 1304203 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 17c45ef8-e332-3d11-83db-44e8aa442883 | -3.57161 | -64.59255 | 2024-09-26 05:46:00 | NOAA-20 | TEFÉ | AMAZONAS | Brasil | 1304203 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e3b0f83c-3196-3a6f-b91c-0725a9f2f168 | -2.93654 | -65.19949 | 2024-09-26 05:46:00 | NOAA-20 | UARINI | AMAZONAS | Brasil | 1304260 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 473ab4bf-1beb-3387-a995-69bbdc0a26e2 | -8.42727 | -66.0883 | 2024-09-26 05:46:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 454d9184-c29b-3202-bf3f-0256c3c00b25 | -8.42672 | -66.09186 | 2024-09-26 05:46:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| de2591ea-d2cb-3c3a-a3fb-7eec6c0bee61 | -8.41 | -66.08925 | 2024-09-26 05:46:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1ec8f135-dcc5-356d-aa69-a092bd864ec5 | -8.40945 | -66.09282 | 2024-09-26 05:46:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 944cd35b-3fd5-3d37-a485-f67b2926ab0b | -8.4072 | -66.08518 | 2024-09-26 05:46:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 4a176496-1963-3447-aba2-ce816a50c4cd | -8.40665 | -66.08874 | 2024-09-26 05:46:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7bcf9ce9-ac27-3d8b-aa47-703b4888e6f5 | -8.4061 | -66.0923 | 2024-09-26 05:46:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e43e5f88-04cc-37c8-97cc-1b8543454058 | -8.4033 | -66.08822 | 2024-09-26 05:46:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3bd166bf-8e99-3eab-bb4d-67cd3f79493e | -8.40276 | -66.09178 | 2024-09-26 05:46:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b3812ee2-fcaf-35ee-a4d5-66cde7d112eb | -8.42393 | -66.08778 | 2024-09-26 05:46:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d85e58ca-27b4-38c6-bf70-a2f6666617fe | -8.42338 | -66.09133 | 2024-09-26 05:46:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9d8ef87f-6aa0-3160-aebe-2e39576690c6 | -8.41054 | -66.08569 | 2024-09-26 05:46:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| ebfce4f3-e40a-3996-b04b-d4b88ff3a785 | -4.8891 | -66.89124 | 2024-09-26 05:46:00 | NOAA-20 | CARAUARI | AMAZONAS | Brasil | 1301001 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| da1ec4d0-d0b2-3557-ae2c-6701270f588a | -4.85867 | -66.88964 | 2024-09-26 05:46:00 | NOAA-20 | CARAUARI | AMAZONAS | Brasil | 1301001 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 335d05ed-e508-3f6d-a8b5-7bc412dd67eb | -3.3936 | -53.725 | 2024-09-26 05:46:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0672d8ca-0fe6-3f65-b025-53115b3f8d7a | -3.38707 | -53.72385 | 2024-09-26 05:46:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 93d3b484-3efa-336e-8d90-4921d293c271 | -2.85572 | -53.32085 | 2024-09-26 05:46:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c85c0b80-f261-349c-9807-dcf328391070 | -8.71097 | -54.79821 | 2024-09-26 05:46:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b524acec-73a0-3149-b44a-0c351e69b39d | -8.71024 | -54.80394 | 2024-09-26 05:46:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e39e2f17-e09e-32be-8b78-b68ab0001f22 | -8.69867 | -54.78944 | 2024-09-26 05:46:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3bc3010e-58f9-35b7-ac3f-7ca1d563f3f7 | -8.69795 | -54.79521 | 2024-09-26 05:46:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 84dd4266-c086-36d5-b6e5-ab86ffb5d6b7 | -8.52666 | -54.58554 | 2024-09-26 05:46:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 86a92d29-e0b2-3a33-9390-cb5956cc770e | -8.52521 | -54.59706 | 2024-09-26 05:46:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f217fe4c-1b1e-32c1-ba7e-ce6edb7f39e0 | -8.52076 | -54.57867 | 2024-09-26 05:46:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d0b697d7-8e5c-3950-9924-06cbcf6935eb | -8.52003 | -54.5845 | 2024-09-26 05:46:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 276b9f1c-2472-3867-bc96-2285fb101d4a | -8.51487 | -54.5717 | 2024-09-26 05:46:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 86e0c6c3-92f5-3cb0-bd70-fb15d2bbbd87 | -9.17488 | -54.68113 | 2024-09-26 05:46:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 749a74d3-0591-39ce-b81e-febf179d3983 | -9.17253 | -54.67713 | 2024-09-26 05:46:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 62d1bdb7-f007-3a24-8139-88613a62534a | -9.17558 | -54.67558 | 2024-09-26 05:46:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| de11e96c-5fed-32fe-ba85-ba15766ad900 | -9.17319 | -54.67163 | 2024-09-26 05:46:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 727cc530-8ef2-3f4e-8571-2dbc7ccb2a73 | -8.92156 | -54.74897 | 2024-09-26 05:46:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 78135262-6306-32bd-9881-83cb2085e81e | -8.91501 | -54.74756 | 2024-09-26 05:46:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 328aca7d-2ca4-3761-92ba-b591ce48a31a | -8.70439 | -54.79728 | 2024-09-26 05:46:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0db657e7-3eac-3927-a452-461406ca855d | -8.52816 | -54.57373 | 2024-09-26 05:46:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 55d942e2-1595-32d1-9cf6-4f09c09e3cd4 | -8.5274 | -54.57969 | 2024-09-26 05:46:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 68dbeaca-e868-3449-b7fc-1f1118398900 | -9.46535 | -54.56097 | 2024-09-26 05:46:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2173cf5f-7eee-3167-8e29-0bebe78e92b5 | -9.46459 | -54.56728 | 2024-09-26 05:46:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 40d7260e-b086-3988-8ab7-57c71d50f411 | -3.3584 | -53.78183 | 2024-09-26 05:46:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 1e28ece5-8185-3043-90e8-b1ad8647d3ae | -3.35185 | -53.7809 | 2024-09-26 05:46:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| ad255894-14bc-3efb-8813-e252bd399949 | -3.3511 | -53.78602 | 2024-09-26 05:46:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 4805cbef-10b2-321c-b0de-78972a14a8f6 | -3.34457 | -53.78502 | 2024-09-26 05:46:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 47a70f36-b3b8-3e2c-8965-198929ffd3a3 | -2.95612 | -53.71868 | 2024-09-26 05:46:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c4ff991a-4faf-392c-9e0b-985a2ea4c048 | -2.95038 | -53.71218 | 2024-09-26 05:46:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 78226e4e-a5aa-3991-83f6-158e67619ff0 | -2.95036 | -53.71524 | 2024-09-26 05:46:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| eec3bcc0-cba2-30af-831e-ce6e2625d7da | -2.9496 | -53.71769 | 2024-09-26 05:46:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ab4dd93c-e106-35f3-8ee0-b24f8e5b29a4 | -7.37562 | -55.4935 | 2024-09-26 05:46:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| ca023193-adc1-36f4-ac30-776e80172e8f | -7.37498 | -55.49826 | 2024-09-26 05:46:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 5018b9f5-5bb4-3dc2-87e0-73d8fb48aade | -7.37471 | -55.49147 | 2024-09-26 05:46:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 02e81614-c2eb-3cc6-b5e4-313f013a4682 | -7.3741 | -55.49624 | 2024-09-26 05:46:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 8a4852c7-0f8b-33f8-beee-54d4167e8d5d | -7.37368 | -55.5079 | 2024-09-26 05:46:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 63684dcf-14ec-359b-9ac1-f2ba05db3342 | -7.37349 | -55.50101 | 2024-09-26 05:46:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 79bddd9f-7864-3d0a-a080-c821cea66341 | -7.37237 | -55.51763 | 2024-09-26 05:46:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 21.2 |
| df9568cb-b48b-38e7-84c2-9109381bd666 | -7.37173 | -55.52242 | 2024-09-26 05:46:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 5cad5b8d-3e41-3884-a852-1d7c40b54ee1 | -7.37109 | -55.52711 | 2024-09-26 05:46:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 314c69a3-5162-383d-a7cd-64c0377a6075 | -7.37101 | -55.52052 | 2024-09-26 05:46:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 69c69b3c-d8ec-306f-8cb0-d9297f346037 | -7.36746 | -55.5072 | 2024-09-26 05:46:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| eedf268b-9456-382d-997d-b78651865407 | -7.36678 | -55.51228 | 2024-09-26 05:46:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 21.2 |
| 89598072-cb76-3dd3-bfdc-f076aaf34a92 | -7.36611 | -55.51725 | 2024-09-26 05:46:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 21.2 |
| 9be43574-f555-3811-85e7-9f7bfc9b2aad | -7.36547 | -55.52205 | 2024-09-26 05:46:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 5f1fac2f-5618-3386-a488-f7cfe1e36b50 | -7.36259 | -55.49646 | 2024-09-26 05:46:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5926c94e-7beb-363e-8e86-d6ae7ba7c9c5 | -7.36122 | -55.50669 | 2024-09-26 05:46:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 710e9741-bcf0-3269-882c-cac324386a67 | -7.82049 | -54.73451 | 2024-09-26 05:46:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| ecc27f55-d15f-3a35-beaa-16026141323a | -7.8084 | -54.73243 | 2024-09-26 05:46:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 04fcea9a-c1eb-3e33-be0b-f69d555e3fb9 | -7.80677 | -54.73783 | 2024-09-26 05:46:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 79afec91-4ba9-3154-ab45-b960777fb3d8 | -7.80617 | -54.7426 | 2024-09-26 05:46:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8ac90ced-b305-3a1f-95c0-9d6d9b5f04bd | -7.80148 | -54.72694 | 2024-09-26 05:46:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3d2d35ea-c85a-38f7-b7e0-f7f8aeb54e2a | -7.79615 | -54.72433 | 2024-09-26 05:46:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 7eae4d36-a7c9-362e-862e-b0f67696dee9 | -7.79508 | -54.72488 | 2024-09-26 05:46:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| acbb2054-c31e-3832-8549-094d126fb059 | -7.61207 | -55.29045 | 2024-09-26 05:46:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 53e5d057-ed8b-333b-8ccd-6f5a53f8998a | -7.60837 | -55.29236 | 2024-09-26 05:46:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2ce734c9-4b74-359b-993e-269b7eca2ea2 | -7.60521 | -55.36404 | 2024-09-26 05:46:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a3fb59d4-9a5d-30d3-90cf-2f194d375d32 | -7.56663 | -55.16861 | 2024-09-26 05:46:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 69e7dbb1-a263-3b70-925e-6d779e4a22e8 | -7.56451 | -55.16659 | 2024-09-26 05:46:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 0169d52f-5791-3c63-8b34-034bb9957a06 | -7.56095 | -55.1625 | 2024-09-26 05:46:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 3d2f4def-6b63-3d32-beb9-719334eb0bd9 | -7.55885 | -55.16067 | 2024-09-26 05:46:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 4c2529b0-9490-3e2e-9b58-50b18e9de6b9 | -7.55314 | -55.15507 | 2024-09-26 05:46:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 4ea1ceda-b775-367e-87ad-479131a1b9c6 | -7.82154 | -54.73371 | 2024-09-26 05:46:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| f4892f12-a396-34ab-8cb5-b53fb32adcd6 | -7.82094 | -54.73825 | 2024-09-26 05:46:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 341f96dc-c799-30e5-b92f-113f89d7ebcd | -7.81991 | -54.73907 | 2024-09-26 05:46:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| b5eeb20d-cde1-3a7b-891e-e3ebfbd588d2 | -7.81497 | -54.73305 | 2024-09-26 05:46:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 2526cd14-dc08-3a13-a726-a0a09d3444ec | -7.81442 | -54.73719 | 2024-09-26 05:46:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 866db91d-3b21-37a1-a7b2-89aaeb066649 | -7.81394 | -54.7337 | 2024-09-26 05:46:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |


[Clique aqui para ver as próximas entradas](README157.md)
