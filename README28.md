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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 501dfb55-4ed7-314a-a51c-cf8a8cc7d577 | -3.03572 | -50.97567 | 2025-11-29 05:03:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5327a8b9-c013-35db-af7c-c3ecfaba63f5 | -2.35568 | -48.07488 | 2025-11-29 05:03:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d44593b6-8b7d-3cf5-aaa4-b4d96ec6666f | -2.78623 | -47.4342 | 2025-11-29 05:03:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 3f4378de-34f6-356c-a673-b226b8e41072 | -2.53688 | -45.39062 | 2025-11-29 05:03:00 | NOAA-20 | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 79d9a233-34db-3cf4-9cd1-c90f0ed50892 | -3.32491 | -53.51128 | 2025-11-29 05:03:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8ed6f20c-868e-3f70-8cef-c605a62be46c | -3.04429 | -53.04019 | 2025-11-29 05:03:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0369cffe-bf63-3a09-a1cb-5f50d6547c45 | -2.17218 | -48.41896 | 2025-11-29 05:03:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 79feac90-4fff-36fc-8482-86ca7dca8d21 | -3.47427 | -51.36863 | 2025-11-29 05:03:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b4b86a44-9975-392e-b648-9b45fb1b0032 | -1.84469 | -55.34597 | 2025-11-29 05:03:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 88dcf914-926c-307b-8d98-dab816495de3 | -3.11168 | -50.35983 | 2025-11-29 05:03:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f5297768-3d26-39f2-a924-75f0266b421e | -2.64895 | -48.02552 | 2025-11-29 05:03:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d31bbca8-2d0e-3e1f-95b5-bcd8d1d3a011 | -2.78299 | -47.42306 | 2025-11-29 05:03:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| c344e527-c4ca-3ac5-8971-142ac9393125 | -2.63552 | -48.54083 | 2025-11-29 05:03:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 30552211-46f1-3280-a4f4-0f3f91d23c3c | -3.5385 | -54.16858 | 2025-11-29 05:03:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b3964fc0-54c3-319c-9c07-8debdb036da2 | -2.96364 | -50.98838 | 2025-11-29 05:03:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 11bd8141-f395-38ef-a790-2bd46ff95fb5 | -3.2222 | -50.3184 | 2025-11-29 05:03:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0f5aeeff-da68-338f-8c42-15b00b25ca5b | -2.29501 | -53.9114 | 2025-11-29 05:03:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 28486cb5-8e3d-3272-9cd6-0761dbe02403 | -2.79183 | -47.42974 | 2025-11-29 05:03:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5f70cc10-3ad2-3ad6-bc7d-87839d634dc9 | -2.64293 | -48.03434 | 2025-11-29 05:03:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a8328f76-f2f9-3a8d-924b-a98104200b15 | -2.9622 | -50.99784 | 2025-11-29 05:03:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 42bb9e26-3bda-3c70-b065-61389efb114c | -3.4238 | -52.63195 | 2025-11-29 05:03:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8c128021-1dd8-31c4-8737-764be322fc6f | -1.32766 | -53.16996 | 2025-11-29 05:03:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 48fd027c-fc3a-3be7-ae16-00a5d3d7bf8a | -2.94664 | -54.28409 | 2025-11-29 05:03:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 051c0220-7f7a-3662-8278-207c3eadea42 | -4.116 | -51.101 | 2025-11-29 05:03:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| eb1e1f66-c714-3a2e-9bad-d87895aafd10 | -2.63484 | -48.5452 | 2025-11-29 05:03:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7cc212ef-0e83-3e04-a87f-815f5703934a | -3.4306 | -52.07018 | 2025-11-29 05:03:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f58507f1-b4cf-37e9-8b32-572682aaa8b4 | -2.99927 | -45.42836 | 2025-11-29 05:03:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 67049c09-4f74-3c3e-9d46-41d90929887d | -3.3227 | -53.32072 | 2025-11-29 05:03:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 613a5138-8adf-328f-8fd4-69234d48b7bb | -2.23363 | -53.6744 | 2025-11-29 05:03:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ff502dee-3b61-32da-9212-a382627f1d85 | -2.22558 | -47.51495 | 2025-11-29 05:03:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 3ed37eba-14c9-372b-8136-5632e2ae0424 | -1.28336 | -53.17772 | 2025-11-29 05:03:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4cdc5196-190c-3b78-8743-d82053674f75 | -2.9389 | -51.42412 | 2025-11-29 05:03:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d5f04abe-8b36-3d7f-b485-d7564993572a | -2.64002 | -48.02689 | 2025-11-29 05:03:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 40d7fe01-b363-3069-aa3e-6c2d2fe18d3e | -4.63908 | -49.36178 | 2025-11-29 05:03:00 | NOAA-20 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6b9f8c27-00b4-3e85-a396-63f504fc3153 | -1.25977 | -54.6797 | 2025-11-29 05:03:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9d385b65-e16d-3bf2-81bd-7a88e03cc7e5 | -3.59863 | -50.42231 | 2025-11-29 05:03:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 4fe8ea7d-01ff-3924-b85d-210c5a105dd7 | -1.90854 | -55.28536 | 2025-11-29 05:03:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f752aa7d-7534-30bc-99b0-13bfb8266e4c | -2.58353 | -48.40174 | 2025-11-29 05:03:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4302d4d0-efe2-3aca-a892-43c33a778a3c | -3.26859 | -51.4691 | 2025-11-29 05:03:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c65aabcc-8e89-3ab9-8a18-71072f4ca1ba | -3.5735 | -50.41138 | 2025-11-29 05:03:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 7b396762-ffaa-390b-bd1e-8abb575815cb | -3.3368 | -50.25153 | 2025-11-29 05:03:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 75e8424d-7e07-3ac5-97dd-eec4ec45bf95 | -2.93431 | -53.2732 | 2025-11-29 05:03:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ad5c7018-f095-3ae9-be98-51bbf88e6ade | -3.33151 | -42.50625 | 2025-11-29 05:03:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9ec4a460-8b31-3b60-bf39-c4bfa188a5e1 | -2.63973 | -48.02415 | 2025-11-29 05:03:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4d0908cc-c86b-3bef-b0e0-4e26bc5faeca | -3.22618 | -50.319 | 2025-11-29 05:03:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 388c7cfd-3045-374f-b4d6-e456a053b0e6 | -4.63109 | -43.98796 | 2025-11-29 05:03:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5b3b909d-6ea1-31d4-8d0c-5aa406103e4e | -1.28673 | -53.17826 | 2025-11-29 05:03:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 59b1654a-0bd8-3899-b03b-44c589458e3a | -2.91288 | -53.07374 | 2025-11-29 05:03:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7279d532-6a1a-371a-9132-cde51c8fc6fd | -2.64966 | -48.02078 | 2025-11-29 05:03:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ddc5dc6f-d82f-3261-b166-cf5a6e564f4f | -3.57487 | -50.29783 | 2025-11-29 05:03:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 73732921-b566-30a7-8102-6e7def53a036 | -3.22671 | -50.31557 | 2025-11-29 05:03:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 601d4d65-11ce-32c3-9d9b-0378ceb9dd63 | -2.71418 | -53.1793 | 2025-11-29 05:03:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e8419c50-485a-34e6-9c00-02e797807e22 | -2.32094 | -48.15003 | 2025-11-29 05:03:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 63a927c4-8c7e-3181-be3e-89213658fb83 | -2.78379 | -47.4178 | 2025-11-29 05:03:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0ba3ea34-b9df-3bee-8127-ecf782e800f8 | -4.11733 | -44.90545 | 2025-11-29 05:03:00 | NOAA-20 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 58927969-5abc-3425-8a52-ce8636d7c5fd | -2.64434 | -48.02483 | 2025-11-29 05:03:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 70786308-628d-3d52-97aa-bfadc0cee7fe | -2.84066 | -51.81744 | 2025-11-29 05:03:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 94ef314a-be18-38c9-91a5-412bc38d357d | -2.55198 | -46.00271 | 2025-11-29 05:03:00 | NOAA-20 | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 680498f8-93fc-3a97-886f-d462344cc589 | -2.71362 | -53.18298 | 2025-11-29 05:03:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| add5726a-da1d-3506-9b4e-c25fa0078ab9 | -3.86194 | -54.05985 | 2025-11-29 05:03:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d58ced07-f944-3284-9ddb-9e6a0fd44985 | -4.62602 | -43.98919 | 2025-11-29 05:03:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| efec06d9-c01c-354a-9cf1-45efbdd4b234 | -2.93091 | -53.27265 | 2025-11-29 05:03:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bfb49ec6-9f51-3ca1-9dff-73111755b7d8 | -3.32131 | -52.99258 | 2025-11-29 05:03:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 60dd141f-7cc0-3201-8f23-0c340158eb1b | -3.47497 | -51.36412 | 2025-11-29 05:03:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e4a0df1b-b014-3b36-8d8d-b0e57ff5d33e | -1.68641 | -53.6551 | 2025-11-29 05:03:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d30fa2d3-1169-39e1-8ea3-0eb7390d6d5e | -4.63846 | -49.36592 | 2025-11-29 05:03:00 | NOAA-20 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c8fbf501-2d9d-3527-b2af-9de3600cfb08 | -1.85105 | -55.11035 | 2025-11-29 05:03:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9d406db7-3578-3ad5-afa9-2013bc418596 | -1.6892 | -53.65914 | 2025-11-29 05:03:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6dd5af1e-5546-357a-a7a2-86bca8c281a2 | -2.92467 | -53.26793 | 2025-11-29 05:03:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| be515480-4082-3029-8dcb-82a0e0dff5d2 | -1.37519 | -52.50963 | 2025-11-29 05:03:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 24ffc4a4-d508-3c82-b151-56022f2c2fc3 | -6.59984 | -43.69307 | 2025-11-29 05:03:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ba9a3ccb-2bde-39d1-ba1a-4d2a6bd75b51 | -3.06423 | -49.52146 | 2025-11-29 05:03:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0f2297b4-c6b0-3a9f-a91c-8e4f734747d3 | -1.40167 | -54.47032 | 2025-11-29 05:03:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 217a23ba-dc40-3a47-b102-392f62a98283 | -2.78781 | -47.42376 | 2025-11-29 05:03:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 654e35c1-a74a-39c8-a5ae-61bff37e3fb5 | -3.25932 | -52.57516 | 2025-11-29 05:03:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f806a1c0-1682-36fa-85d0-ece7aa026677 | -3.38407 | -51.49796 | 2025-11-29 05:03:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f659ec17-8ba4-3f1e-9300-ad321949cc28 | -5.93814 | -45.39718 | 2025-11-29 05:03:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fca0fdc7-4dd3-3d9e-ad3a-b0da491e2e87 | -3.67855 | -52.53072 | 2025-11-29 05:03:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2f8cc86d-9a08-34d8-af56-a77ae544eb66 | -1.40989 | -55.38738 | 2025-11-29 05:03:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8dc1e24d-d90d-3547-a733-1308badbf777 | -2.17152 | -48.42334 | 2025-11-29 05:03:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d8e72c68-cdbe-3775-b65b-08422a9f30de | -2.63107 | -48.54017 | 2025-11-29 05:03:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 483b8eb1-4093-3678-a803-83a868427634 | -2.4722 | -50.24019 | 2025-11-29 05:03:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 833d51a7-9db8-3c18-9cc0-f745fc4e86e8 | -3.75098 | -55.99014 | 2025-11-29 05:03:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c36200b0-874d-3470-bbc6-cf5fa2bc547b | -2.85844 | -50.28148 | 2025-11-29 05:03:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9ac32ba5-4a10-3651-8e67-39f39206e345 | -3.03684 | -53.04286 | 2025-11-29 05:03:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3b9a38d6-3e12-33c9-97a6-445347e819d6 | -3.47293 | -52.98824 | 2025-11-29 05:03:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 559fb514-9287-3324-8785-f0f0af417a8a | -3.0334 | -53.04232 | 2025-11-29 05:03:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 14fc211d-7c6c-37c0-9106-93bf301ca8a5 | -2.91406 | -53.06625 | 2025-11-29 05:03:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 56f2426c-eb3f-34d4-85c2-d5a71af52d44 | -1.51372 | -52.78645 | 2025-11-29 05:03:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| afbc3382-6ac5-39c1-a32e-1cc5a516da55 | -5.9439 | -45.39826 | 2025-11-29 05:03:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6e81c8b2-bf74-3364-a926-2a4b18d00550 | -4.74282 | -44.43444 | 2025-11-29 05:03:00 | NOAA-20 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6348c67c-97af-3b15-a457-52f628d94e71 | -3.04027 | -53.04339 | 2025-11-29 05:03:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 12a11225-c773-3590-bce9-d8d6fa6d7978 | -1.91094 | -54.40915 | 2025-11-29 05:03:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 6c2596f1-a784-368f-8c22-6756e3cf2c6f | -3.5322 | -51.24281 | 2025-11-29 05:03:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1ff1dda6-6aba-344e-82f0-8a5e42653342 | -2.721 | -53.1804 | 2025-11-29 05:03:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9f618c85-bc59-3349-9c50-6285c00099a8 | -3.22565 | -50.32242 | 2025-11-29 05:03:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0ccb48b0-3860-31ff-96b5-9501fcaa0d86 | -2.22636 | -47.50988 | 2025-11-29 05:03:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 20e33bd3-c2c5-37bc-a8a2-25cf6ce03f5b | -2.75171 | -49.32723 | 2025-11-29 05:03:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4d6bee36-cc89-38ff-a1c5-2365b43cc4d4 | -2.29952 | -47.9819 | 2025-11-29 05:03:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6e058ad7-acb6-3179-a07b-1f61359ab637 | -2.8949 | -49.46645 | 2025-11-29 05:03:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |


[Clique aqui para ver as próximas entradas](README29.md)
