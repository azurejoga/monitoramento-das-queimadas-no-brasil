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

## Dados Diários - Página 31

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c536ff72-361d-375d-8350-2acd10408ab5 | -2.09093 | -46.32739 | 2024-11-22 04:36:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cacad8bd-53fb-3ed9-9e49-35d215196ad9 | -3.20594 | -54.25666 | 2024-11-22 04:36:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 31e4c8a9-25ea-31d5-ad88-8cfb65c2ff85 | -1.61978 | -52.59411 | 2024-11-22 04:36:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 26ba13f4-e120-3506-9b76-7349b46fbe50 | -3.82885 | -52.25805 | 2024-11-22 04:36:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 19fba19d-84a3-3e8a-b691-cc44afb73973 | -1.74438 | -46.30201 | 2024-11-22 04:36:00 | NOAA-20 | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0555a70e-ecf5-3dd3-9fe1-b2e7cd2fa981 | -3.80653 | -51.26556 | 2024-11-22 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 668f64c5-35dc-360c-8935-2151fe9c9100 | -4.6392 | -49.54219 | 2024-11-22 04:36:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1fd119d8-7dc6-3d77-bacc-547357b61b4d | -1.72584 | -52.38758 | 2024-11-22 04:36:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1cf79ff6-a8bc-378a-bede-e6eae88b4e93 | -1.7432 | -52.37617 | 2024-11-22 04:36:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| ceb5160b-fed9-3ee2-814b-5564d30001ce | -3.66408 | -51.56915 | 2024-11-22 04:36:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b3b4dac0-2aec-3774-bc38-ba3b86fa3ffd | -4.34238 | -45.53103 | 2024-11-22 04:36:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ad247c2f-4659-3f51-8628-f881161bacde | -2.15128 | -53.78765 | 2024-11-22 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 29c5c0ab-4342-3f32-912c-7e6b97c154a7 | -1.65288 | -52.67009 | 2024-11-22 04:36:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| ccd74027-8687-380b-8d71-7e2415d4da35 | -1.77654 | -53.60523 | 2024-11-22 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b92536ff-22f1-3549-8dc2-32255da38bf1 | -1.76368 | -50.85761 | 2024-11-22 04:36:00 | NOAA-20 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 86ae6268-f968-32d0-af81-e6e7ddb80c0e | -4.30225 | -50.14855 | 2024-11-22 04:36:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7616daf7-9d29-3208-accd-f4507638236e | -3.08222 | -45.96574 | 2024-11-22 04:36:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 19e1d75e-2484-382d-95a5-b3f53b6b41f0 | -3.40472 | -54.02735 | 2024-11-22 04:36:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 06a39484-6341-369b-9800-4fd54222bfe7 | -4.55725 | -48.52974 | 2024-11-22 04:36:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 264dd1bb-d562-356b-9a5d-14e4833251d4 | -3.5176 | -53.79379 | 2024-11-22 04:36:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 158c59d3-51f8-3721-873d-1132e16a616c | -2.70669 | -46.24065 | 2024-11-22 04:36:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b265f76a-ed41-3aac-a78d-879e6caaca54 | -3.31112 | -45.49709 | 2024-11-22 04:36:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8ed45836-6348-3bdc-8bb6-00213d888433 | -1.15502 | -53.66789 | 2024-11-22 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 74553e7c-41de-33ce-8531-5fa456f0adc0 | -3.33676 | -53.33947 | 2024-11-22 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| e2ac883f-aea4-3262-9c7e-6f94995e0f8a | -3.10083 | -53.74145 | 2024-11-22 04:36:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 87fe43cb-5100-3732-9e5c-74a9ee6e2595 | -1.13143 | -48.77555 | 2024-11-22 04:36:00 | NOAA-20 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 55aa7b2d-b291-30ca-ad46-4c6b25daf50d | -2.25633 | -48.70857 | 2024-11-22 04:36:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b9690dca-bdff-3126-aae4-db80435f6602 | -4.25528 | -48.70178 | 2024-11-22 04:36:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fb3e0ff5-1b80-3f97-82cf-9dd13a80ec73 | -3.18822 | -51.3071 | 2024-11-22 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f96bb372-7774-3c02-96e5-0bf63e320101 | -4.40647 | -44.12656 | 2024-11-22 04:36:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e3b13849-698b-36eb-83d4-5249f53f3990 | -2.69676 | -46.07372 | 2024-11-22 04:36:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7f05bb95-573e-3ec8-9843-a10bc5dddb69 | -3.83182 | -52.26292 | 2024-11-22 04:36:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| c7e5e69c-e6be-38c7-84f4-a6973b621c6a | -3.40791 | -54.66603 | 2024-11-22 04:36:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a9282845-813e-31b1-8ae2-df629ea4acee | -3.10505 | -54.29152 | 2024-11-22 04:36:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6ba3a99a-e155-3975-94b1-f39563b35ab2 | -1.11174 | -51.75893 | 2024-11-22 04:36:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 88d683d0-9181-3d6c-932f-55bac8aeeee0 | -1.79115 | -48.44941 | 2024-11-22 04:36:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cf85c37b-60de-325d-9e7f-3149f743f317 | -3.51187 | -53.80376 | 2024-11-22 04:36:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3d81497e-55db-3291-8872-c1f205dc4fa5 | -5.09438 | -45.941 | 2024-11-22 04:36:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3f97002c-cccd-3136-91f8-7f980d46cae9 | -2.71013 | -54.1395 | 2024-11-22 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| a2a35b74-93f6-3218-bb3b-892abcb7d657 | -2.65492 | -48.78864 | 2024-11-22 04:36:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 723b6352-4e83-34d5-bc2b-6fc4cdeb22f9 | -3.07011 | -53.29776 | 2024-11-22 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4e3a2f38-d4da-334c-a609-199622148ac4 | -0.86659 | -51.89011 | 2024-11-22 04:36:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 66d8fd47-a635-3149-bced-d8f2155ba6ef | -2.61101 | -48.24672 | 2024-11-22 04:36:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0752c44b-fab8-351c-87cd-14a36aa6cb3f | -2.19414 | -53.65193 | 2024-11-22 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ef5b98b7-67d0-3f3d-8cc8-3c6d1c54b854 | -0.89275 | -51.72322 | 2024-11-22 04:36:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e486ccbf-3a8f-3590-901b-f7f7a87a46b0 | -3.76234 | -52.13498 | 2024-11-22 04:36:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 260a743b-d4e1-337f-a76d-21d05835b30e | -4.8388 | -48.64152 | 2024-11-22 04:36:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f57c28e0-bd1d-30bc-9f14-2784dc646b68 | -2.7346 | -54.38667 | 2024-11-22 04:36:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6fe5042e-ea97-3b45-80fa-f9db3724b2b6 | -2.50418 | -54.15178 | 2024-11-22 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 8b963aaf-d34c-3d07-8d19-d6c4e05f719e | -3.21969 | -54.25106 | 2024-11-22 04:36:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 814eae78-c715-37cd-bb22-3a9d42646a14 | -2.03633 | -49.64982 | 2024-11-22 04:36:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 52952acb-9eb3-37cc-8825-f19c157f81d5 | -2.21873 | -50.46384 | 2024-11-22 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 69304d69-ac7a-3500-a712-e40b0775035c | -1.09604 | -53.16614 | 2024-11-22 04:36:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f8724a30-23ed-3b44-85dd-8da3a2b23314 | -2.1549 | -50.46957 | 2024-11-22 04:36:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7a435a89-b335-3e4c-85f6-081067368a45 | -3.23355 | -54.25308 | 2024-11-22 04:36:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| e92b50e4-6cd6-3ba2-b6a1-7351237e516d | -1.72624 | -52.70641 | 2024-11-22 04:36:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| d661475e-4d40-3e65-801a-7cf1823d8235 | -2.44017 | -46.53564 | 2024-11-22 04:36:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 92d76b1b-b563-3e55-bff2-7cee672617fd | -2.65147 | -46.24073 | 2024-11-22 04:36:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bcb1c3c9-fdcc-30eb-967e-96924f8df55b | -3.53406 | -52.78809 | 2024-11-22 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1d4aff4a-5282-3f7c-ba44-f65b8f9c2148 | -1.15147 | -53.66339 | 2024-11-22 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 61bab057-6530-391e-bd79-f2aa4219ec79 | -1.79169 | -48.44598 | 2024-11-22 04:36:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a0e1ddb1-e8c9-3d34-8ba1-b5a9503bf6cf | -1.19364 | -51.97704 | 2024-11-22 04:36:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 95b899cd-12e1-32d9-b93c-7763e5dad8b8 | -3.31673 | -52.86287 | 2024-11-22 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 27c90495-c17b-3b2b-9fd7-4614f9a87f4f | -3.10383 | -53.75225 | 2024-11-22 04:36:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2b62fd57-13e8-369f-be2a-60cf2a5f10d0 | -2.67107 | -46.16148 | 2024-11-22 04:36:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 86cfefb5-7c05-362e-9dda-b3d580f532ae | -2.2195 | -46.39946 | 2024-11-22 04:36:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 59e5259e-5068-39a9-b586-216fbae67e47 | -2.32119 | -48.57808 | 2024-11-22 04:36:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 21008763-1c9b-3c60-99b6-436a7534b9a3 | -3.42638 | -54.60725 | 2024-11-22 04:36:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eecd26ab-295e-3cb5-bfa9-3c62d5c77497 | -3.32008 | -54.08909 | 2024-11-22 04:36:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e9814913-cf6d-36b7-8960-ff0deb87753e | -3.58371 | -51.43883 | 2024-11-22 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 693f30d4-fd27-3116-99f4-1f7e4ee3b7cc | -2.75083 | -54.12636 | 2024-11-22 04:36:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ccc7c0d0-9cda-35c3-8b06-854d1272e13b | -1.84948 | -53.6958 | 2024-11-22 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c5fadf1d-1f90-330f-bc34-4221b7d72afe | -0.8088 | -51.78381 | 2024-11-22 04:36:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 87fb0234-8dd3-3795-954d-89e075a30d93 | -2.52304 | -46.40684 | 2024-11-22 04:36:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a9badbcd-2e5b-384a-9085-bee55dff0480 | -3.23002 | -54.24852 | 2024-11-22 04:36:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 1f5e71e7-8ae7-3d35-b37a-41045c603216 | -2.60764 | -48.22506 | 2024-11-22 04:36:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3fb6cd31-a737-3b68-8c6e-85b67aa18baa | -4.99628 | -50.50647 | 2024-11-22 04:36:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2af07efe-b785-30ab-b51d-a366ebf5d7dc | -2.20113 | -53.6605 | 2024-11-22 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4bfab9e0-9f62-39a6-9d9d-c5519b23d2d4 | -2.91903 | -46.83766 | 2024-11-22 04:36:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c4d45cbe-fce8-394b-937d-38fbc307254a | -2.70606 | -46.08308 | 2024-11-22 04:36:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 47a3af2e-5376-3329-8bd0-f7e45dccbe22 | -4.55671 | -48.53318 | 2024-11-22 04:36:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4c0ae29a-13d4-3a91-944c-7da81e955ef8 | -4.36155 | -50.39587 | 2024-11-22 04:36:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| add18029-2951-3ec2-b263-f491d132be48 | -2.2718 | -49.08513 | 2024-11-22 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 072ec338-3177-3e1d-a4d0-4d79e7d64ca5 | -3.49981 | -53.80152 | 2024-11-22 04:36:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d28f64e7-e048-394b-b309-6f55bf0eac9b | -2.69975 | -46.23958 | 2024-11-22 04:36:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1d32193d-80f0-3f1c-83af-4fb02b54a4e6 | -3.53336 | -51.10107 | 2024-11-22 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 6dd8bfb7-a703-3c64-b5eb-8c3ac7c443ae | -6.38679 | -47.15474 | 2024-11-22 04:36:00 | NOAA-20 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 26cf104d-a0c2-363e-96e3-536197bbd3aa | -2.92244 | -46.83815 | 2024-11-22 04:36:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 996b3f13-969f-3d9d-b170-9735e3da50df | -2.4204 | -54.59787 | 2024-11-22 04:36:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 699914a7-e2b4-3e79-9474-eca879108d21 | -3.23902 | -54.24592 | 2024-11-22 04:36:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| e7c09de3-d69b-3a51-98b5-511340cd2f08 | -2.30669 | -53.60051 | 2024-11-22 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| cbce8a68-f361-3469-92e9-23d263e9326a | -2.39692 | -46.06928 | 2024-11-22 04:36:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1f2efa19-6c8a-3c30-b3d9-7ac9f4de7039 | -4.2426 | -49.08393 | 2024-11-22 04:36:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4b7ab569-2e20-3800-9610-d00642ed64cf | -2.53512 | -46.37408 | 2024-11-22 04:36:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 17d86215-34ba-3d2c-87d5-a546d5201998 | -2.89402 | -53.0478 | 2024-11-22 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ec90c33e-431b-3401-bb16-e00f6dfa0166 | -3.36929 | -53.06356 | 2024-11-22 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d9f0d4a0-e2f7-337f-afeb-10e7f66182e0 | -4.72179 | -44.43133 | 2024-11-22 04:36:00 | NOAA-20 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 92f0e4ee-84e0-3f9f-8eea-8ba19b5df420 | -2.72113 | -46.1013 | 2024-11-22 04:36:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0c9bcd73-76ff-3a62-bf7e-157946923af4 | -1.6167 | -52.58874 | 2024-11-22 04:36:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 56aaafac-e1ac-3f21-ad00-d63ef69b65be | -2.69377 | -46.84459 | 2024-11-22 04:36:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README32.md)
