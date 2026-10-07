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

## Dados Diários - Página 81

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e7bf877e-c1ed-32df-8584-48dd4cc2fbf0 | -4.75514 | -45.76991 | 2026-10-07 05:04:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 111d9aba-6315-3168-8d21-9b17913da70d | -3.0594 | -54.25434 | 2026-10-07 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 82586138-8d7f-38e4-b80b-85b128a07068 | -3.28207 | -54.17754 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ebebf891-c905-3329-be21-80f0165d8bfa | -3.29062 | -54.06011 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| a886f82d-9116-3ae4-958c-1492a708311c | -3.87465 | -52.26095 | 2026-10-07 05:04:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6a002d87-3d33-3fb3-b5bf-639caedd7a9b | -4.96982 | -50.90455 | 2026-10-07 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c2dc325d-8042-35c5-baa7-94a752fa4f92 | -3.2742 | -54.18726 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 72907012-6684-3c43-81dc-859fd1ce8ff3 | -3.26887 | -54.0459 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 131d7ef0-6192-3edc-b26b-a5a44c1562d5 | -2.9324 | -54.13105 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3de9bbd3-14e0-3e41-9530-7bf2866a7a30 | -3.53629 | -49.47558 | 2026-10-07 05:04:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 12d7dc1c-aaf7-3d86-8fab-f09875f5538a | -2.10001 | -52.06325 | 2026-10-07 05:04:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5134e986-b3dc-34f6-a819-fb4638425ffb | -3.05169 | -54.39227 | 2026-10-07 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f24a1c5b-58d5-3585-9830-618b44fa3e24 | -3.10405 | -54.18597 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a41e5891-88b8-3e30-8cd2-1b7d426fc481 | -3.02445 | -54.17376 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8f6330b8-b5f1-3e2d-985d-0db3a0c09e85 | -3.52396 | -54.65793 | 2026-10-07 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 509857e5-0050-39eb-9a84-a14181d83e1d | -3.27555 | -54.04694 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 83dbdedf-015d-3c17-b876-0534cfd21f39 | -3.08484 | -54.244 | 2026-10-07 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1959ea28-aa2c-36ca-9ad4-3f6172966fca | -3.28229 | -54.06966 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 9a25b803-8c66-3edd-bfd0-b311802b99d3 | -3.58745 | -54.5575 | 2026-10-07 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3fd8ed0d-ce23-3261-b2b5-3cf98d45eac1 | -3.8646 | -55.98574 | 2026-10-07 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a26da947-9150-3b40-8f39-a37a95b02ab3 | -1.29268 | -54.56664 | 2026-10-07 05:04:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f45cbd83-6e40-3ed8-b92e-e4d3b8e698cb | -3.35665 | -59.50283 | 2026-10-07 05:04:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 047f0327-3eb8-30e4-884b-bea44a200fb9 | -6.2086 | -52.83763 | 2026-10-07 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6d2f4cd5-02df-3d92-946a-7e06588abefd | -3.53597 | -54.64901 | 2026-10-07 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c862cad7-8ea2-30fb-9ff9-3721ff07ceb6 | -2.95235 | -54.11254 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0d38788e-cf48-3350-a3e3-da5ca0559bb1 | -5.84084 | -53.57156 | 2026-10-07 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 259269f9-521e-3489-9c99-efaca614ffd6 | -3.00154 | -54.12352 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 8564ee01-d400-338e-bb3e-645c191e2077 | -3.05921 | -54.21139 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 88fd3869-fcfc-3db3-9884-d0c0b1384877 | -3.04881 | -54.14877 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| b882ab5c-fc5f-37b0-91f5-2fb32dced768 | -3.99499 | -56.26219 | 2026-10-07 05:04:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 6ef48fd1-4a96-3a81-a2f5-0a894634d857 | -3.10675 | -53.77682 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| a278508f-a831-3b04-b2fb-8f9f6576c560 | -4.1533 | -54.02444 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0b695fa1-ab9c-3371-b3aa-233efbfea1bb | -3.2142 | -53.87368 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 096019cd-9cbb-33fb-8790-61ef1170bcd6 | -3.01092 | -50.47089 | 2026-10-07 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 593416a3-2f78-32a7-b3f6-a0cf4a7a6679 | -3.05551 | -57.52213 | 2026-10-07 05:04:00 | NOAA-21 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3e603e65-876a-3307-8468-137048984391 | -3.08155 | -54.39689 | 2026-10-07 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 235c3029-d598-3bb2-a21a-7f22c9dd9b98 | -2.4923 | -56.12248 | 2026-10-07 05:04:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 63fc3c97-5f6d-37ae-93f5-c0c37114461a | -3.21028 | -53.87673 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ee84cf80-1bee-342c-8db8-b4cdf805656d | -1.25566 | -55.76123 | 2026-10-07 05:04:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2e72d5e0-41aa-36e1-91e3-78a6f3f8ad6c | -2.57852 | -56.15792 | 2026-10-07 05:04:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0e78ed67-cf8b-3097-9a7b-d5b5acbbed9d | -2.95239 | -54.1341 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c004eb30-0787-3f06-8f7d-57e6655e89f2 | -3.13316 | -53.70724 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c92028c1-7368-3d1a-82f0-5b4bd098c0e8 | -4.27105 | -54.86626 | 2026-10-07 05:04:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 020ac724-bcf9-3144-a60e-c4a8a591451f | -1.7154 | -55.43321 | 2026-10-07 05:04:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a5a1bf35-ec7f-3bf1-91d9-3a1bcf6baf23 | -4.16333 | -55.14257 | 2026-10-07 05:04:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| ce1559bb-e80f-37df-9f42-e3038a85da15 | -3.09549 | -53.73844 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c1c0c12f-ecab-3248-ad52-ccbd5efb7983 | -2.9727 | -54.1334 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 042d1959-d659-321b-8016-43fa2cc51102 | -3.50741 | -54.65538 | 2026-10-07 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e4323c25-bc9e-3be7-9ee0-cd4b83acf784 | -2.96827 | -56.62405 | 2026-10-07 05:04:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9f39e2ba-8558-3dee-8088-bfeb820d3173 | -3.50241 | -54.64397 | 2026-10-07 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f6ca5fb2-441d-3147-bcf5-1f53c2884af9 | -3.27665 | -54.03987 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 26.4 |
| ade4e2da-1255-332d-a6b3-cbf60b423bd4 | -3.02307 | -53.89541 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 387701f5-f090-38d9-87f8-a998a2a1841e | -3.73347 | -51.20954 | 2026-10-07 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 437b7e88-ec11-33ff-873f-2ad039af51e0 | -3.07936 | -54.25747 | 2026-10-07 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| fe60c348-4e00-381b-b835-f6eb62857bf5 | -3.39332 | -59.51828 | 2026-10-07 05:04:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 7210af15-05f7-32a9-80aa-dc3d53c7982b | -1.12115 | -54.11724 | 2026-10-07 05:04:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 785a72eb-2a0d-3353-9362-e14b18c0d0ff | -3.57087 | -54.55494 | 2026-10-07 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| abd2912e-6d7d-3169-9dbe-a472aa125c9a | -3.61244 | -54.59337 | 2026-10-07 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ad2ec2d4-ac41-3ca2-b560-1f46e78a306e | -4.91965 | -55.85642 | 2026-10-07 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| c208e3e3-c82f-3b36-a955-c02f400b1ebb | -2.99541 | -54.11898 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e49334f2-2b5b-3de2-84da-7a337cc1f073 | -3.05174 | -54.2174 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| af1647d9-c9e8-3ece-98be-0abd6a235c6e | -8.70273 | -45.19969 | 2026-10-07 05:04:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 7a060a98-ff9d-3c08-81fa-9e331464db2a | -3.05706 | -54.2254 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a09e5bd2-6858-3ce1-aa83-615ef2609b2d | -3.49023 | -57.78749 | 2026-10-07 05:04:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 79d917d9-3d4f-3a73-a7ad-fb79de8e8c27 | -3.09939 | -54.28202 | 2026-10-07 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 27067e07-be24-3af6-ab86-75bd068886e0 | -1.09876 | -54.12789 | 2026-10-07 05:04:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 15b0180d-7645-39bd-bf86-f171373d5962 | -4.15183 | -55.15133 | 2026-10-07 05:04:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6d7c77d0-573a-32ab-82f3-c5aa3a18d837 | -3.01269 | -54.13961 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 187a7a65-e0b3-3f5b-8fca-991f89b56af4 | -3.18709 | -50.55346 | 2026-10-07 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 35c4167b-60f7-30b5-a266-8958c8c84950 | -2.9431 | -54.19366 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 25996589-5809-3062-a4d1-69f1290fe43c | -3.08168 | -54.28645 | 2026-10-07 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 4245b24b-c632-3e50-86d2-a2ef68c2688b | -2.86863 | -54.14634 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 89a28eb6-fee7-3a95-8ac4-b88b27a0563f | -4.51618 | -42.89331 | 2026-10-07 05:04:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 3d371a88-ba7e-3a91-9120-4b56c3aa7d32 | -3.20199 | -53.95187 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cf540f06-b440-3f4b-ab8e-5b4fb0a902fd | -3.93105 | -54.57879 | 2026-10-07 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c9660934-cf78-3152-88e4-b4ee5291dc71 | -5.68493 | -53.48593 | 2026-10-07 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d23f2e20-980f-3861-baa7-677dc76627b4 | -3.59579 | -54.56944 | 2026-10-07 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 05a2cd50-f8f8-3fc7-bc37-54d62ccc3173 | -2.92964 | -53.92852 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 57b5e9d0-762c-3211-9ee4-e65a68fb60e8 | -5.01642 | -50.93999 | 2026-10-07 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 710d9938-176b-3123-9ef3-fc44795a1309 | -3.03879 | -53.92691 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 750576b8-5bed-3d06-93de-509820a65046 | -5.37484 | -55.88234 | 2026-10-07 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2850f503-8381-3d0c-8fad-c075a48b7a74 | -3.13065 | -54.36535 | 2026-10-07 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d7a7905d-8ff0-36dd-82fd-12a31d97f773 | -3.229 | -54.30228 | 2026-10-07 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 47e5e943-9230-3d9f-8525-793e09e5fd18 | -3.40584 | -59.58813 | 2026-10-07 05:04:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0fddfc5b-3ea5-3c9e-8731-19d8a12f1fd5 | -3.27326 | -54.01761 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 44d07b9f-3092-3055-aa8f-a29a707a306c | -3.10111 | -53.74664 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e6563cd8-874c-328c-87e2-b0f0dc8280f8 | -3.56029 | -59.49199 | 2026-10-07 05:04:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 60d9e1dd-1ceb-3c6c-8930-ea41e5e9f86e | -3.78858 | -59.37777 | 2026-10-07 05:04:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5b5180f8-a970-38d0-b62f-4ad842b82c83 | -2.9207 | -54.11848 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a58ff24d-073f-3b00-8ff7-0419646e966c | -5.58313 | -48.9531 | 2026-10-07 05:04:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1fa14369-93c5-3183-86a3-5b97ccf39c1e | -3.19273 | -50.5698 | 2026-10-07 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 5baa56ea-fe53-34b7-ba72-5ed897d4e954 | -3.11628 | -53.78197 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| ae010cbe-b071-399e-b87e-09cedf13b6b0 | -6.15345 | -51.7296 | 2026-10-07 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c6164b6e-3525-3ea6-aa07-c20e6071a506 | -2.00075 | -56.94982 | 2026-10-07 05:04:00 | NOAA-21 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 33bbca91-d7a4-3415-8719-7a80c07f9485 | -6.6647 | -55.44191 | 2026-10-07 05:04:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3ca28866-0437-3014-9f1c-9386200d6d07 | -1.4627 | -54.78635 | 2026-10-07 05:04:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e50676ae-901d-32c4-9ff8-5f53a52e2234 | -2.97082 | -54.07919 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ff95516c-e74f-322e-85a6-a1a855a19645 | -4.26389 | -54.86868 | 2026-10-07 05:04:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 810086a9-5811-326a-85c4-fe3b237727e1 | -5.37326 | -56.06537 | 2026-10-07 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 77fb3993-d0a8-3bd5-bb2f-d3feb5b92960 | -3.03088 | -53.88933 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README82.md)
