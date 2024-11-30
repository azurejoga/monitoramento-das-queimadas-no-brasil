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

## Dados Diários - Página 124

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d9edfd5a-0a27-33b4-aad9-24470383d10d | 1.91107 | -55.70664 | 2024-11-30 05:27:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 69075ce6-da2c-3c54-ae7f-f002df0ae298 | -2.5474 | -55.22784 | 2024-11-30 05:27:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 9e1ae0ad-b51c-3ddd-99ea-afbc6e927e5d | -2.90141 | -54.15546 | 2024-11-30 05:27:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9cf80578-398a-353e-9deb-8869acff1ad8 | -1.61586 | -53.88258 | 2024-11-30 05:27:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a9c73b51-a55b-33ad-9475-63688b43e9fd | -3.25084 | -53.62292 | 2024-11-30 05:27:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 8d022aaf-df7e-31e6-9f14-531b26fd6262 | -1.46644 | -54.50747 | 2024-11-30 05:27:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 81a57ec7-46a8-37ad-9aab-6c5cb5f26ca5 | -3.33513 | -53.2232 | 2024-11-30 05:27:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8c7c5ee2-c581-384b-ab03-ab3f3eea2f74 | -2.98377 | -53.28191 | 2024-11-30 05:27:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 26ec838a-2f97-3ee9-ae74-733fc57ab89d | -1.08782 | -51.88817 | 2024-11-30 05:27:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0e1ea5a4-e559-300b-a7e1-3f37b148c43c | -2.74806 | -51.66582 | 2024-11-30 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fea6af94-e13c-318a-b403-29b38077e600 | -3.3031 | -51.10701 | 2024-11-30 05:27:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1f9097af-43d8-3770-a94f-b6627ef5f868 | -1.50916 | -52.56857 | 2024-11-30 05:27:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 570b94cf-1600-39a4-8b52-a97534a76a2a | -1.85262 | -55.61434 | 2024-11-30 05:27:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| c8a017bb-ddd2-3aee-a944-5b4c2fa6dc68 | -3.25504 | -53.8588 | 2024-11-30 05:27:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| fafe7f3e-e89b-3c79-bd67-a7f2d63b811e | -1.8877 | -48.65508 | 2024-11-30 05:27:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0d453bbc-fc3c-386a-b004-3d0d232a6e6c | -2.65886 | -48.78379 | 2024-11-30 05:27:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4182a327-c544-3493-be6b-f5d3104ec287 | -1.58115 | -53.8393 | 2024-11-30 05:27:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 34832b8e-646e-316e-aebd-1a6c597242aa | -3.24883 | -50.62001 | 2024-11-30 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7d6080f5-bb88-34e9-ba22-a53fc7bca44e | -1.59866 | -52.29681 | 2024-11-30 05:27:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 326819b5-fb87-38a6-9300-f4c81a710c2b | -3.16308 | -53.24179 | 2024-11-30 05:27:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 8e631db6-97c4-3638-b392-95bfc558798c | -3.02651 | -51.53682 | 2024-11-30 05:27:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 809d8af0-44f8-317f-be81-91eb1599c512 | -3.2263 | -54.17614 | 2024-11-30 05:27:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 1fa08459-3d68-3fa7-b472-7f56bb2f8060 | -1.34853 | -54.6284 | 2024-11-30 05:27:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 5cdaa3e3-3132-3d39-8a94-deb5b0117a8d | -0.99964 | -51.72881 | 2024-11-30 05:27:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 39df0f47-c458-377d-932a-20f399da7339 | -2.5155 | -48.46624 | 2024-11-30 05:27:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 6d79f7cb-5526-3c5a-a539-85fe14b984af | -0.95862 | -51.6557 | 2024-11-30 05:27:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 68cf717e-aacc-323f-85cd-bd0167ed09ff | -3.5376 | -50.17962 | 2024-11-30 05:27:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a32672b1-1a91-3564-b747-2ced8ad321a1 | -1.15634 | -53.55167 | 2024-11-30 05:27:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| b68c5d03-cd68-3b3d-81fd-692ff812966e | -1.64749 | -52.40339 | 2024-11-30 05:27:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e34d789f-93ae-3be8-b0a6-58c5571c802a | -3.49533 | -51.56918 | 2024-11-30 05:27:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 21f7833f-c228-3d04-9681-9580f84de390 | -2.61634 | -60.02339 | 2024-11-30 05:27:00 | NOAA-20 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a51b2a43-f833-33a6-ba95-9b80941ffa8c | -1.69333 | -55.01609 | 2024-11-30 05:27:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 10eaa278-1b4c-3360-b2d0-f8eb36155077 | 1.20194 | -55.94687 | 2024-11-30 05:27:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 380e3fc0-cc8a-37ac-9577-97e28cfcc64c | 0.97848 | -50.25235 | 2024-11-30 05:27:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b4d22b87-45c3-33f5-8936-c2260c280421 | -3.32 | -54.17562 | 2024-11-30 05:27:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| ecd4be3c-7f36-3fc9-b381-006871cba6e7 | -3.22163 | -54.17551 | 2024-11-30 05:27:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| af0fbcdd-46d9-366d-81f9-8177822a8256 | -0.14321 | -60.86653 | 2024-11-30 05:27:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 95df36d5-11ab-3c87-9c93-576828bb5ac6 | -1.71754 | -52.77942 | 2024-11-30 05:27:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8b9d51b0-93e8-3a68-a15a-33ea1bbbd15d | -1.30462 | -55.74566 | 2024-11-30 05:27:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c4cf8a88-8542-37ac-b23b-55814b097001 | -3.10643 | -53.10897 | 2024-11-30 05:27:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0aa1907f-c99b-3bf6-ad14-7939dc28c94f | -1.59494 | -52.28671 | 2024-11-30 05:27:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 71b96b9b-5bc8-3a7f-b336-98fad98f01ea | -3.49916 | -53.79803 | 2024-11-30 05:27:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 17565876-2fcc-39da-84ff-be9163d90e92 | 1.21901 | -55.92932 | 2024-11-30 05:27:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4d7b4409-01c5-33b3-9d99-c48b2c69743d | -2.0004 | -52.09701 | 2024-11-30 05:27:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3746bd6d-464b-328c-8975-8f138abf8f0a | -1.65263 | -52.40417 | 2024-11-30 05:27:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9d2251b0-bd60-3219-a28b-b9b03a746547 | -2.51868 | -48.46461 | 2024-11-30 05:27:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 8cef2763-7939-3b29-84a8-658200dd3249 | -2.76674 | -55.3401 | 2024-11-30 05:27:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 50adc45b-1541-3336-a1b6-fed8b9490118 | -3.8418 | -59.57836 | 2024-11-30 05:27:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7d740900-7aa6-300a-80bd-ab9b0695739a | 0.97844 | -50.26338 | 2024-11-30 05:27:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 893f61be-2892-3924-b2c9-50567b5c4903 | -3.42602 | -50.42939 | 2024-11-30 05:27:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 78160759-7ce3-3a3f-8a1d-c677e133cd4d | 0.94041 | -50.74111 | 2024-11-30 05:27:00 | NOAA-20 | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3a5394d9-38de-31cd-a482-cd6cf6eafe82 | -3.25892 | -53.6353 | 2024-11-30 05:27:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 647ba6f0-f7e4-3165-b613-6083d38ffecb | 0.98229 | -50.25069 | 2024-11-30 05:27:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2603bb9c-fb5c-3060-a992-8afb970e30a2 | -3.96203 | -50.19196 | 2024-11-30 05:27:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 6d34c2da-6bf5-361f-836c-ce941709792f | -0.99585 | -51.71807 | 2024-11-30 05:27:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3f1cc21d-748a-3db7-b250-1d58bc604422 | -3.46293 | -53.87606 | 2024-11-30 05:27:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9551a885-eb0d-31b6-aab3-8ad010af4682 | -1.57856 | -53.84647 | 2024-11-30 05:27:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ae074d71-2b8f-3185-920f-7dda557aaaad | 1.28508 | -55.9128 | 2024-11-30 05:27:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| fc4f8395-2bb2-3f3d-81de-a03746c96df0 | -1.30478 | -52.86818 | 2024-11-30 05:27:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f15e9ae1-2f27-3e43-b703-ca5add464c0d | -1.07894 | -53.63359 | 2024-11-30 05:27:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 96101e56-6b47-3f9b-85b8-983e44ae2411 | -3.22556 | -54.18105 | 2024-11-30 05:27:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 83cd8a8d-4726-3551-8054-e258d7d31fe2 | -1.62819 | -53.86419 | 2024-11-30 05:27:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 0d42e054-927a-3d9a-8c85-8b68334a5dd2 | -1.79033 | -52.73885 | 2024-11-30 05:27:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f7f4c1f6-9ba3-312b-9afd-bf4a66ee4019 | -3.39104 | -50.31968 | 2024-11-30 05:27:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2c684ac1-4771-3d58-804b-2f5a50c90bf7 | -2.82956 | -54.09506 | 2024-11-30 05:27:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e6c55905-3c8e-316d-ba26-0620dabc53e3 | -1.70603 | -52.44736 | 2024-11-30 05:27:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 3f1267c1-9530-3c06-8790-707c4c6e6671 | -3.25251 | -53.6452 | 2024-11-30 05:27:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b7f4e55a-4612-30b9-ae3b-8f8fb6ae517f | -3.74555 | -54.68148 | 2024-11-30 05:27:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| b001711d-34d9-32f3-a8e8-5f2ed14b3439 | -1.60383 | -52.29759 | 2024-11-30 05:27:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6a2abe61-a68a-362d-9e7b-572c2331e6f1 | -1.00118 | -51.71891 | 2024-11-30 05:27:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 174fe8bb-0b54-33a9-bd25-ee6718ff4491 | -3.44342 | -54.07076 | 2024-11-30 05:27:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0ba0405a-c9d9-34bb-aecd-0b475daa488a | 1.97179 | -60.92092 | 2024-11-30 05:27:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2e51e223-0722-352c-a033-09bd3c1174a3 | -3.65144 | -50.21578 | 2024-11-30 05:27:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| a882fff0-1dd3-3d72-9fba-0f542543be3a | -3.42003 | -50.16824 | 2024-11-30 05:27:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a572c7e8-2d6f-3489-a10a-f1ed8f55568e | -1.48818 | -52.32748 | 2024-11-30 05:27:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 181ee221-0a64-30e6-817d-651fbde7801b | -3.4217 | -53.89077 | 2024-11-30 05:27:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 624be72a-8430-34e4-a204-39eb4a9981c3 | -1.68708 | -52.45301 | 2024-11-30 05:27:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3623d100-accd-3f4b-a5bc-4ef04446b417 | -3.59628 | -49.99084 | 2024-11-30 05:27:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 21.8 |
| 72ce351d-8485-3328-9937-e9734739425d | -3.51042 | -53.78864 | 2024-11-30 05:27:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 45182647-6462-3073-84e9-e81bf287bc94 | -0.24578 | -53.76206 | 2024-11-30 05:27:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 4268a3a6-0be9-36e9-9970-bd7ca0fb7a8d | -2.97008 | -53.29483 | 2024-11-30 05:27:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bd8c054b-6e24-3cf7-8531-26e141c166c7 | -3.72817 | -54.23179 | 2024-11-30 05:27:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| de5636c3-db37-35d7-be4b-2e6c0c9dacf8 | -1.30055 | -55.74505 | 2024-11-30 05:27:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b0f4257c-d7c0-3389-af8b-7fb19de3a77f | -0.88832 | -51.72002 | 2024-11-30 05:27:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b794f552-3017-3828-b2ed-0f668d491858 | -2.76829 | -52.90847 | 2024-11-30 05:27:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e5668a28-313d-3404-a692-cc9cfc0476c5 | -3.73742 | -51.83516 | 2024-11-30 05:27:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6641bb42-e9a6-3065-90c3-daf3773aa9f3 | -3.37413 | -50.82441 | 2024-11-30 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| a3d3c575-2abd-35e8-a212-a3e03b0a62ba | -1.34862 | -54.97665 | 2024-11-30 05:27:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 53381cd6-7e17-3efe-8767-94ce4364345a | -1.21285 | -51.73883 | 2024-11-30 05:27:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b93e5e32-db83-3498-85d5-e77243421724 | -3.10636 | -53.80754 | 2024-11-30 05:27:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 47bf68e1-56e2-31b7-9cfe-36333cde7d48 | -1.07078 | -53.63933 | 2024-11-30 05:27:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 4b269873-54c0-3f7c-8153-1a96551b3946 | -3.34947 | -50.51496 | 2024-11-30 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6d1c1e32-dda9-3949-96de-1875b6d464b4 | -2.37768 | -47.8881 | 2024-11-30 05:27:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ee62eda8-a350-3851-924c-e57c92c93f49 | -3.54373 | -50.18046 | 2024-11-30 05:27:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1e812569-270d-36fb-a08f-92702a75d23e | -3.53691 | -50.18417 | 2024-11-30 05:27:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d0a10f3a-a9d2-31ac-ada1-13642da2e8d6 | 1.18181 | -55.96977 | 2024-11-30 05:27:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6bd5148c-8573-3d87-8fdc-6c6c6093251d | -3.59174 | -50.37245 | 2024-11-30 05:27:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| b113e6f6-1c98-3809-bd4a-b0cd53220de0 | -2.73449 | -54.13748 | 2024-11-30 05:27:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 339d4fda-8014-3a87-8ee9-5712c28c0fa7 | -2.19434 | -50.58309 | 2024-11-30 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3f1d8c17-f554-31d1-9e92-c861d81e59c7 | -2.95355 | -60.01678 | 2024-11-30 05:27:00 | NOAA-20 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |


[Clique aqui para ver as próximas entradas](README125.md)
