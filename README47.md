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

## Dados Diários - Página 47

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d2d68794-55ad-38e1-b5bf-216c0ee57b74 | 1.27921 | -51.23824 | 2024-10-28 04:55:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4e5afd1a-2074-3f1a-88b1-c7153aec925c | 1.11297 | -52.58677 | 2024-10-28 04:55:00 | NOAA-21 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 89104643-bb21-3bad-967e-9cae9ffc6f2b | 1.07565 | -52.21402 | 2024-10-28 04:55:00 | NOAA-21 | SERRA DO NAVIO | AMAPÁ | Brasil | 1600055 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b00f5d3c-b510-3054-9dbd-0c73eadcf3a0 | 1.00773 | -52.21752 | 2024-10-28 04:55:00 | NOAA-21 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a3c387eb-2197-31e8-b7fc-40d35e10e2d6 | 0.63729 | -51.87424 | 2024-10-28 04:55:00 | NOAA-21 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 0.5 |
| abdfb6bb-1ff9-3868-804a-48b5182804f4 | 0.54228 | -51.46461 | 2024-10-28 04:55:00 | NOAA-21 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 69ba180a-594c-3e99-89c9-0d02bbd3a4c7 | 0.04715 | -51.71403 | 2024-10-28 04:55:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5eb5fd68-0c96-3fc0-88c9-13627638fbf4 | -0.27728 | -51.81476 | 2024-10-28 04:55:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5101bb07-5cb4-356d-a55f-07f27140119f | -0.23335 | -52.95996 | 2024-10-28 04:55:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f8ad65f9-07b7-32fc-ad6e-5eef9a12205c | -0.21746 | -51.54691 | 2024-10-28 04:55:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3103e883-6ba3-3e9b-b18e-39c093e15cd4 | -0.21411 | -51.54639 | 2024-10-28 04:55:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 75403d8f-1b4f-3e7b-84fe-f4e1f13407ff | -0.10672 | -51.62307 | 2024-10-28 04:55:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.4 |
| bdef819d-618b-35c9-ad15-b2bcc6d46490 | -0.09894 | -51.62906 | 2024-10-28 04:55:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 83bca20a-2ccf-301b-816a-43768ab94c13 | 1.16858 | -52.80615 | 2024-10-28 04:55:00 | NOAA-21 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 982bd938-5191-3ccb-a962-45e6f51fe53c | 1.59678 | -55.64378 | 2024-10-28 04:55:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 90b71c1d-55b9-35b7-a07e-7cdc67482ec6 | -1.9763 | -52.0804 | 2024-10-28 04:55:17 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 20633866-7761-3f91-8f33-e4f293aa0fee | -2.0497 | -52.1611 | 2024-10-28 04:55:17 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 53.8 |
| a1cbe2f5-516c-3f93-9df7-88163a5a5d89 | -2.2662 | -53.7825 | 2024-10-28 04:55:18 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 72.5 |
| 514489ce-278f-3c54-9265-e05d421f52ea | -2.2846 | -53.7822 | 2024-10-28 04:55:19 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 38.3 |
| 0fc7d9b0-f10a-3566-8441-9e60f3f92abd | -2.4104 | -48.5479 | 2024-10-28 04:55:19 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 50.9 |
| b4ee548a-9f3f-31cb-90dd-ef9455c6c3c6 | -2.8699 | -49.2615 | 2024-10-28 04:55:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 73.4 |
| 9b6edae2-4621-371d-8c49-4e849d297c98 | -2.87 | -49.2402 | 2024-10-28 04:55:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 72.2 |
| 61bc0ea4-c284-301c-9e83-d9fde086d5e8 | -2.8884 | -49.2609 | 2024-10-28 04:55:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 116.7 |
| debb132c-f77a-3d87-9f77-438a0f2df8da | -2.8885 | -49.2397 | 2024-10-28 04:55:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 100.2 |
| b172cbaa-6985-3c22-bec4-433289a686cf | -3.0317 | -50.4176 | 2024-10-28 04:55:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 68.0 |
| 01cbddf0-f9d7-3288-ad83-b53f779d423c | -3.0317 | -50.3967 | 2024-10-28 04:55:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 31.8 |
| 3bfe5342-e2a0-39e5-81a4-a07eba3a59c5 | -3.0501 | -50.4171 | 2024-10-28 04:55:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 38.2 |
| 8e5d942a-a5c3-3311-a05b-81a03d42c2f4 | -3.497 | -45.7971 | 2024-10-28 04:55:25 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 82.3 |
| 00b44c2e-dbb8-3ff8-90f2-5aa25d430d55 | -3.5155 | -45.7964 | 2024-10-28 04:55:25 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 79.2 |
| d2911702-c410-38e8-9ccd-45a163ccd264 | -3.56152 | -41.4003 | 2024-10-28 04:57:00 | NOAA-21 | COCAL DOS ALVES | PIAUÍ | Brasil | 2202729 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 3ef3c508-1acd-3927-b305-f6a2fbb2b1e1 | -6.09072 | -41.87132 | 2024-10-28 04:57:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| fe6dd2dd-8da4-35ae-8a14-84a2de094ae9 | -6.09062 | -41.87351 | 2024-10-28 04:57:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 3583e59b-4185-313d-a470-6e680efd4eec | -6.08996 | -41.87683 | 2024-10-28 04:57:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 8.6 |
| c58fdbec-a858-34b4-839b-62ec646e9037 | -6.0899 | -41.87905 | 2024-10-28 04:57:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 02b860d1-45f0-31aa-9a38-8e2f39cbac6d | -7.01039 | -41.3004 | 2024-10-28 04:57:00 | NOAA-21 | SANTO ANTÔNIO DE LISBOA | PIAUÍ | Brasil | 2209401 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| f085634a-5552-3a4d-ba94-c25eb08f6fc0 | -4.95767 | -43.19921 | 2024-10-28 04:57:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ada9c7f6-37aa-3a6a-b5f6-f3b9822f02c7 | -4.95707 | -43.2034 | 2024-10-28 04:57:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 6ba396ff-8015-3774-80e6-75bfc62e9314 | -4.95631 | -43.19819 | 2024-10-28 04:57:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 761431bd-4600-3aa2-aa77-8721a0b93161 | -4.95573 | -43.2024 | 2024-10-28 04:57:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f1c44aec-2292-37e4-8c65-d64cad46c49b | -4.63782 | -43.11087 | 2024-10-28 04:57:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 8c61dc5d-50c2-3faf-82c7-c5f4d50b1bab | -4.63666 | -43.10904 | 2024-10-28 04:57:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 5532ba6e-2939-3636-b023-28a833d17c1e | -4.63607 | -43.11333 | 2024-10-28 04:57:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 2123de20-8cc9-3e2b-9c15-54e19877655a | -4.63193 | -43.11003 | 2024-10-28 04:57:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 155f15a9-9bbf-3fe5-a1c1-61c9897fb162 | -4.63131 | -43.11429 | 2024-10-28 04:57:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 5efe4ece-0f92-325e-baea-d019e3bd0ad9 | -4.48723 | -42.88563 | 2024-10-28 04:57:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 02c96f12-1f79-3159-8296-f7deb594a7e2 | -4.48658 | -42.89006 | 2024-10-28 04:57:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 480f9d8f-6de2-30de-a1eb-6a15c8678242 | -4.48373 | -42.89035 | 2024-10-28 04:57:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f25b2fed-63b3-3359-8cbe-9da20a954bee | -4.15571 | -43.70524 | 2024-10-28 04:57:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e25ab377-a869-39ad-9419-ec7f5ec9f18a | -3.66599 | -43.62667 | 2024-10-28 04:57:00 | NOAA-21 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a20f3cfd-26cd-3762-ac16-fda4e86eff24 | -7.8247 | -45.40305 | 2024-10-28 04:57:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e37c02fb-d035-3a0c-930f-6cb9dd1d87ab | -7.81984 | -45.399 | 2024-10-28 04:57:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 255ea24c-acfe-3c79-a10b-11748d7302a6 | -7.8194 | -45.40226 | 2024-10-28 04:57:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 851ce814-6376-32d5-b8c6-1e96313c422a | -7.42895 | -44.79373 | 2024-10-28 04:57:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 15c2ee5c-c391-3487-bba9-3ac7097920be | -7.86826 | -45.40078 | 2024-10-28 04:57:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 2ac184e6-48b7-3a63-acf0-ed9a8429074b | -7.86779 | -45.4042 | 2024-10-28 04:57:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 5d48ce40-19af-3b35-ace6-d6e94fbb472a | -7.86727 | -45.39968 | 2024-10-28 04:57:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 0dc0d580-b7bb-3b93-a94f-f7d433a798c8 | -7.86682 | -45.40312 | 2024-10-28 04:57:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 3ba45942-e6f2-33f2-956b-8d93ad67b1d1 | -5.26303 | -43.99376 | 2024-10-28 04:57:00 | NOAA-21 | SENADOR ALEXANDRE COSTA | MARANHÃO | Brasil | 2111748 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 36916129-8456-3136-8e34-7d2b46d8b856 | -9.43615 | -44.48543 | 2024-10-28 04:57:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 2662325e-2a86-3899-8a2a-e7a5952ab614 | -3.17714 | -50.38847 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 917c8504-0389-3dd7-96f0-5b610085bdaa | -7.00894 | -41.29661 | 2024-10-28 04:57:00 | NOAA-21 | SANTO ANTÔNIO DE LISBOA | PIAUÍ | Brasil | 2209401 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| dd5b913a-2054-3606-9803-132c8f805704 | -7.00815 | -41.30258 | 2024-10-28 04:57:00 | NOAA-21 | SANTO ANTÔNIO DE LISBOA | PIAUÍ | Brasil | 2209401 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 02b0070c-9047-3adc-8da1-abfe699fa2e3 | -6.67466 | -40.89564 | 2024-10-28 04:57:00 | NOAA-21 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| bb92250a-e438-36de-8bc4-f636778e6756 | -6.67457 | -40.89803 | 2024-10-28 04:57:00 | NOAA-21 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 2188077f-e949-3db9-b243-3bb9b710a06a | -8.86905 | -41.2734 | 2024-10-28 04:57:00 | NOAA-21 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 3244b16a-494f-30cd-a3a9-541efb52ad49 | -4.62603 | -43.10916 | 2024-10-28 04:57:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 4853815d-36cf-35bb-b017-567de146a949 | -4.54379 | -42.98091 | 2024-10-28 04:57:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 04780bdb-46eb-3860-9e0f-1d1ceb7a0a73 | -4.9616 | -43.20338 | 2024-10-28 04:57:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1829863f-4348-38df-b5c7-4b69b6feb122 | -7.32949 | -43.57329 | 2024-10-28 04:57:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 2f8f5641-6fad-3109-8c1e-9a73d429101c | -7.32887 | -43.57788 | 2024-10-28 04:57:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| cf0c850a-1e8b-384e-8b8c-b1560ce8741b | -6.62249 | -42.78083 | 2024-10-28 04:57:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| e2d67396-af8d-3dd9-8d23-f8c1477f6004 | -6.62181 | -42.78576 | 2024-10-28 04:57:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 8339d078-b610-3c3b-a5b1-b5d8206e6385 | -6.62114 | -42.7906 | 2024-10-28 04:57:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 02b1c169-0040-3521-ae69-ec310350babd | -6.59202 | -42.27836 | 2024-10-28 04:57:00 | NOAA-21 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| c74323f3-8349-3787-9dd0-7d9e131fdd34 | -6.59133 | -42.28339 | 2024-10-28 04:57:00 | NOAA-21 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 0da40458-df49-3a79-854e-d417ba3208dc | -4.98466 | -43.71093 | 2024-10-28 04:57:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 751c530a-baaf-3e65-bc44-2c5005c55293 | -4.98409 | -43.71483 | 2024-10-28 04:57:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 7647594e-0356-3675-8ee6-0463b9cf7fa5 | -4.98353 | -43.71873 | 2024-10-28 04:57:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| ac038d42-001d-3a1c-bb7a-e9a29b7e0551 | -4.98115 | -43.71127 | 2024-10-28 04:57:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| e09d8d9d-f8be-3cb0-9fdb-90d149faeabe | -4.98062 | -43.71519 | 2024-10-28 04:57:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 175039f6-75cc-3200-82b8-f39f996102ab | -4.98008 | -43.71914 | 2024-10-28 04:57:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| dc17e496-fc13-3f62-9cd7-721deab0c73a | -4.97898 | -43.70994 | 2024-10-28 04:57:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d688a262-6e40-39e5-ba13-9b7efd993493 | -4.74163 | -43.251 | 2024-10-28 04:57:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1b1ae4e3-5b56-322f-a1f3-d5b7a831794c | -4.74105 | -43.25526 | 2024-10-28 04:57:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d437a4f4-7e6d-38d3-8a54-4b2d699b0061 | -8.76603 | -44.71839 | 2024-10-28 04:57:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1de2b488-a8bb-3c4a-8ad5-7cb96c7bbd29 | -4.65657 | -44.66961 | 2024-10-28 04:57:00 | NOAA-21 | PEDREIRAS | MARANHÃO | Brasil | 2108207 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fbca4472-3372-3fff-aed6-77a8ad1c5879 | -4.65235 | -44.66988 | 2024-10-28 04:57:00 | NOAA-21 | PEDREIRAS | MARANHÃO | Brasil | 2108207 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8fff4bbd-19e8-3852-bf95-cc11c298c16e | -4.65126 | -44.66871 | 2024-10-28 04:57:00 | NOAA-21 | PEDREIRAS | MARANHÃO | Brasil | 2108207 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 73a1d5b6-8f38-3a09-834e-931d9adb6082 | -3.89172 | -44.17163 | 2024-10-28 04:57:00 | NOAA-21 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5598a09f-4fed-36f0-916d-8350d7f213d1 | -3.89121 | -44.17514 | 2024-10-28 04:57:00 | NOAA-21 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9da0e680-bdf2-323f-93ca-0c8f36e946e5 | -4.17151 | -44.10691 | 2024-10-28 04:57:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 3ed969c3-6687-3f03-9e10-037ad4cce3cf | -4.171 | -44.11039 | 2024-10-28 04:57:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 98584c57-9bb9-31a3-b29f-78e7e84b3edc | -5.0635 | -44.21867 | 2024-10-28 04:57:00 | NOAA-21 | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5e729bd2-b78f-309a-922e-6c28671f2618 | -5.05798 | -44.21792 | 2024-10-28 04:57:00 | NOAA-21 | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| a3e2f1df-6d7a-3189-9895-7bf8f1e02792 | -5.05746 | -44.2216 | 2024-10-28 04:57:00 | NOAA-21 | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| e6e4228c-2a3a-3789-8663-27462c610c87 | -5.05695 | -44.22527 | 2024-10-28 04:57:00 | NOAA-21 | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| d1dbaab3-8240-36c3-8176-47644dba9632 | -6.13318 | -44.30313 | 2024-10-28 04:57:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| eb90684e-ae04-3023-9bb8-75cfab649d4a | -6.12767 | -44.30192 | 2024-10-28 04:57:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 442b6081-fa5a-3455-8d47-e4706823905e | -5.84483 | -44.75912 | 2024-10-28 04:57:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8069daab-8851-31fc-a7e7-cefd8e92c64c | -5.84437 | -44.76249 | 2024-10-28 04:57:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README48.md)
