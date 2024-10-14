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

## Dados Diários - Página 110

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9b38c639-fc8c-35d7-a5c1-f210d41cf818 | -2.25525 | -53.48559 | 2024-10-14 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4c55d136-8cea-3e43-8aef-3e59292c2bd8 | -4.36733 | -53.66877 | 2024-10-14 05:08:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e0f09129-a6e2-38e3-b27e-e2c7f9002ae9 | -4.36371 | -53.66821 | 2024-10-14 05:08:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 651c3bf9-de7a-38cf-8e7f-6b5fc67497e1 | -4.17498 | -53.53117 | 2024-10-14 05:08:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 78f45c32-0abf-36c0-9647-b5ddf39f4952 | -4.17434 | -53.5354 | 2024-10-14 05:08:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 19e185b4-aed2-39a0-8278-a5cd42ff754b | -4.09893 | -53.72995 | 2024-10-14 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ee3c7fad-6109-3f70-914b-62f50992168f | -4.09829 | -53.73406 | 2024-10-14 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 805f3c71-b481-3b18-881e-966907b9136b | -3.96432 | -53.75686 | 2024-10-14 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0bc24643-1642-35a7-a3a2-fe37425d3b32 | -3.96074 | -53.75632 | 2024-10-14 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 75cf942b-b2f8-3060-8de2-6e4549f5ec94 | -3.67571 | -53.68338 | 2024-10-14 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 274c80f7-bfc8-3fd6-b9a7-36c3af28ef13 | -3.87079 | -52.29408 | 2024-10-14 05:08:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c3ed320c-970b-3866-b1b3-67fa7c637f47 | -3.86765 | -52.28858 | 2024-10-14 05:08:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ea1f0f39-62b8-3adf-a83d-d850ce3dab8c | -3.8669 | -52.29348 | 2024-10-14 05:08:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| fd951565-57c4-3651-b3e9-cc60f5da0086 | -5.99682 | -53.3504 | 2024-10-14 05:08:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d1efa33f-7b98-3283-b359-cc329befce56 | -5.99613 | -53.35496 | 2024-10-14 05:08:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c44aeea1-34b2-3a41-ab25-1b8b2fb72935 | -5.72035 | -53.69378 | 2024-10-14 05:08:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 41932c3e-f9f9-32ec-86e9-f77944075b44 | -2.0299 | -54.93571 | 2024-10-14 05:08:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 79e76166-f8e7-3c14-bb43-3a67ff116f4c | -1.69959 | -54.87432 | 2024-10-14 05:08:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8f695796-f27d-3626-88f6-d19f2704a32a | -1.69623 | -54.8738 | 2024-10-14 05:08:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e9e25a58-257c-33d4-bccb-448bd5327909 | -1.69381 | -53.81235 | 2024-10-14 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8707ace5-c747-35a8-81d2-0a1648f6882d | -1.69031 | -53.81184 | 2024-10-14 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a2410d07-8af4-3abc-a65f-6a3dfed90144 | -1.59946 | -53.35008 | 2024-10-14 05:08:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b1ed6489-aae6-3608-bbcd-03fd04617de6 | -1.59589 | -53.34953 | 2024-10-14 05:08:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2056ae78-6328-3367-9226-33f0387bb8fc | -1.54968 | -54.59749 | 2024-10-14 05:08:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8e7e7c85-4e11-3899-86c6-28fc25f870b2 | -1.5463 | -54.59695 | 2024-10-14 05:08:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c1eda97a-f5e8-3251-8116-9c97618b3c6d | -1.43397 | -54.48752 | 2024-10-14 05:08:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 70e5926b-dd41-3501-ad5c-1ef3b9bae502 | -1.43116 | -54.48322 | 2024-10-14 05:08:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 76e2a348-9381-3a81-b50c-7cd4e1bf0813 | -1.43059 | -54.48689 | 2024-10-14 05:08:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 49d1091c-d82f-3d37-8b82-3b6f2696bd05 | -1.42778 | -54.48262 | 2024-10-14 05:08:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0d4099d4-39c6-38f3-9639-910699801d25 | -1.42491 | -53.47333 | 2024-10-14 05:08:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fbfde5c3-f1b4-3ab7-9b62-7344190545f7 | -1.42199 | -53.46884 | 2024-10-14 05:08:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| dc59b845-5bf9-3f44-84d2-c8511a4975f5 | -1.42137 | -53.4728 | 2024-10-14 05:08:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 819b29fe-8f33-3890-91ab-5b84416af0fb | -1.23519 | -54.09937 | 2024-10-14 05:08:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7f429f7f-20b6-3ff6-b275-84aecb52d550 | -1.23282 | -54.1144 | 2024-10-14 05:08:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 96d253ed-bb66-3cca-b239-4106fae1c8a9 | -1.23222 | -54.11814 | 2024-10-14 05:08:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4b2fec3c-1a53-3622-932c-ec1cdab961ab | -1.21882 | -54.54036 | 2024-10-14 05:08:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c3e7258a-2e2a-3899-a229-e891c5a18d2f | -1.14646 | -54.10452 | 2024-10-14 05:08:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d8738343-12ed-3617-b779-ee16a8963508 | -3.66988 | -54.07188 | 2024-10-14 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 77419b3f-4aac-3ef2-ab86-510d6e177e4c | -3.66634 | -54.07148 | 2024-10-14 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 202d6b78-904a-3632-9d9d-690eea0edda1 | -3.62064 | -54.12975 | 2024-10-14 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| feac3b58-bd0c-3eb2-b7d5-70ea46781679 | -3.62004 | -54.1336 | 2024-10-14 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 85ef6377-c22c-39df-a9f8-ba6cbde8d587 | -3.61713 | -54.12922 | 2024-10-14 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| abc0072f-0ae4-3e95-b248-178bd29ae3bf | -3.61652 | -54.13308 | 2024-10-14 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e1b12975-9682-34aa-be3c-279a0a57dc04 | -3.58905 | -54.6669 | 2024-10-14 05:08:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 043daee2-fb6a-3133-a018-ca92844bac4f | -3.58561 | -54.66638 | 2024-10-14 05:08:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cb8a1291-a421-3336-8397-66af990a1e35 | -3.51588 | -54.66428 | 2024-10-14 05:08:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 88ed2d82-0e44-3d1c-b121-40f24a895d97 | -3.51245 | -54.66375 | 2024-10-14 05:08:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| fa7f33e0-b74e-392c-adb0-1af9eebbdacf | -3.48273 | -54.15735 | 2024-10-14 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f6572f56-bb11-3230-ad55-5f47f9d5c03f | -3.42898 | -54.18078 | 2024-10-14 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4495d415-b226-39c7-a53e-d55a9cf5a54c | -3.42607 | -54.1764 | 2024-10-14 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5c0b5606-61a3-3570-973f-1c6c0348b2b3 | -3.36583 | -54.56922 | 2024-10-14 05:08:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1820eec9-7e93-3639-bb68-168fdfe0c9d0 | -3.36239 | -54.5687 | 2024-10-14 05:08:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 958ba3ea-587e-3072-bc54-328ed71791be | -3.35433 | -54.71227 | 2024-10-14 05:08:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b225cf89-5880-3927-a17c-f40c5b9153ca | -3.29776 | -53.85689 | 2024-10-14 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bac269a4-dba4-36ad-b8bd-6509e2f20185 | -3.29483 | -53.85236 | 2024-10-14 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 073d72ac-7caa-3104-a6ec-050682e9ca31 | -3.27244 | -54.18199 | 2024-10-14 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cc1d43ab-ef5c-3df1-b75e-fd09dcc3a7f1 | -3.27088 | -54.14611 | 2024-10-14 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5ebbd8df-878b-3609-b55a-a49b69f80363 | -3.26895 | -54.18147 | 2024-10-14 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5f238389-e9e7-3560-b1fb-07408aaea992 | -3.26834 | -54.18534 | 2024-10-14 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 26a9b290-3638-317f-a6f9-a1e4cb3d88cf | -3.26545 | -54.18095 | 2024-10-14 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ecc4be3e-9ffd-3c45-af86-2f354a5ba412 | -3.25772 | -54.20766 | 2024-10-14 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 31ffb1b8-7bf5-3a82-a94d-a57cd835e3df | -3.25604 | -54.19551 | 2024-10-14 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f3861d67-5bf7-3391-a46c-219bbfc32b9c | -3.25544 | -54.19939 | 2024-10-14 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 41a30aeb-50d1-3165-9c67-2afa4d71c20f | -3.25484 | -54.20326 | 2024-10-14 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9f3e6295-ea88-3a9c-b477-b93d35196512 | -3.25315 | -54.19113 | 2024-10-14 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7a3bb994-af65-33e0-a46d-c5067b8644df | -3.25255 | -54.19499 | 2024-10-14 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 32456d23-81ce-3a14-a4aa-89f8ac9671db | -3.21632 | -54.85689 | 2024-10-14 05:08:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 575950af-2e90-3a1a-96e3-a63646625b11 | -3.21576 | -54.86054 | 2024-10-14 05:08:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b60d6be3-b416-33fc-9d7b-bd753e2a5c5c | -3.16591 | -54.77437 | 2024-10-14 05:08:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 25496ba5-8966-366a-8441-0e7a04755adc | -3.13623 | -53.68654 | 2024-10-14 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cb47597a-d417-39c7-a094-db8d4b766a7f | -3.12029 | -53.74202 | 2024-10-14 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8db280d3-41e8-3512-9793-487872c3953b | -3.11673 | -53.74148 | 2024-10-14 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ecec99be-f21b-3a52-b46e-f6e670b1b217 | -3.08634 | -54.24471 | 2024-10-14 05:08:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5d22fc4e-12a4-30c1-91a9-18f1b3a1f5a6 | -3.08345 | -54.24034 | 2024-10-14 05:08:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ed087455-e656-3188-8277-61c6a60f179e | -3.08287 | -54.24417 | 2024-10-14 05:08:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8d084a43-884b-3e07-bced-2a6ff3a8f81c | -3.07998 | -54.23981 | 2024-10-14 05:08:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 646af441-5b05-3944-a04b-bc976609799b | -3.07939 | -54.24364 | 2024-10-14 05:08:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3e4f2b5b-d1bf-369a-9920-2e1e72ec40e2 | -3.07881 | -54.24747 | 2024-10-14 05:08:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e45dca13-7d18-3742-849e-94d48b82730b | -3.0765 | -54.23927 | 2024-10-14 05:08:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 32fb6b6f-8522-31e1-bf17-88eb7592a2a1 | -3.07592 | -54.2431 | 2024-10-14 05:08:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ec39c619-4658-3de9-9dfa-2ee0014b5ef8 | -3.07533 | -54.24691 | 2024-10-14 05:08:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6b06e0d4-df95-36f2-b609-432e016e3b7b | -3.07303 | -54.23874 | 2024-10-14 05:08:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 08e97353-259a-3756-86dd-5a4343658501 | -3.07244 | -54.24255 | 2024-10-14 05:08:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6a4ad70c-9960-3336-947b-07cbc2bfb83d | -3.07186 | -54.24636 | 2024-10-14 05:08:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a6779795-4f13-3e73-bb2a-18845a5bf44f | -3.06619 | -53.88042 | 2024-10-14 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c38f8273-01f7-37be-bd05-43d1a8ccd5d5 | -3.06556 | -53.88449 | 2024-10-14 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b96884a8-39cd-3994-a636-0fb8c2b6938e | -3.06494 | -53.88853 | 2024-10-14 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7736106b-c8e7-3c39-8331-4f23c90faad5 | -2.99901 | -53.91538 | 2024-10-14 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| df4ac53b-03b0-366e-a897-03403561cfe5 | -2.99549 | -53.91484 | 2024-10-14 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 97e2c21e-8827-3aa5-b7a2-16003b5468cd | -2.9954 | -54.17701 | 2024-10-14 05:08:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 805acacb-acc6-3b53-a22f-f6744107d9d4 | -2.99113 | -54.90843 | 2024-10-14 05:08:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5edb2485-478f-3378-a476-ba1e031774ba | -2.99056 | -54.91207 | 2024-10-14 05:08:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e3c4cfe7-73ab-321b-954d-a2eb498fbfc4 | -2.97791 | -53.72502 | 2024-10-14 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b4f8a9be-54b2-388e-847d-0dd46797ca9d | -2.96393 | -54.65388 | 2024-10-14 05:08:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| f65584b5-5923-31e6-85d2-3e182f5c4279 | -2.96336 | -54.65757 | 2024-10-14 05:08:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| f7059279-4bf2-34e2-8553-18caba75f19e | -2.96052 | -54.65334 | 2024-10-14 05:08:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bb7809e6-e1c0-3e37-aa90-72d3142d46a6 | -2.87481 | -53.9696 | 2024-10-14 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9e566421-967a-369c-acc7-d92a2c7b9e85 | -2.83848 | -54.49052 | 2024-10-14 05:08:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 99ff39aa-ae13-39ba-93e1-922d237d407a | -2.82352 | -54.74531 | 2024-10-14 05:08:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| adf804dc-fd8e-380a-844a-978970756b06 | -2.81002 | -54.08687 | 2024-10-14 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README111.md)
