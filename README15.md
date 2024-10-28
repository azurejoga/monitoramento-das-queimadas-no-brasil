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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e7d7c760-cc32-3e68-a1d0-9d549b13c1be | -1.9012 | -52.327599 | 2024-10-28 00:50:27 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7e2f296f-b54c-32e8-b377-90dd0d32f009 | 2.3577 | -50.752102 | 2024-10-28 00:51:04 | METOP-C | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 7885ba45-3ee1-3d81-9555-b0760ffd15fb | 3.4465 | -51.268299 | 2024-10-28 00:51:24 | METOP-C | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 4a3f10aa-2fd1-353c-b7fe-f52ae30e6397 | 3.59 | -51.271702 | 2024-10-28 00:51:26 | METOP-C | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 5cd47a03-9d2e-3d4a-bc4c-238e1562bf67 | 3.5885 | -51.2785 | 2024-10-28 00:51:26 | METOP-C | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| b481b251-d414-3319-861c-43f276b284b6 | 3.58847 | -51.27964 | 2024-10-28 00:52:00 | TERRA_M-M | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 22.7 |
| 5c5ac050-bfc2-3ce9-a6af-c083f1d6190e | 0.08149 | -49.87389 | 2024-10-28 00:52:00 | TERRA_M-M | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 01fbfd7e-069f-378a-9316-06d47b7a61a5 | -3.56752 | -54.67388 | 2024-10-28 00:52:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 16.8 |
| f81828ab-6504-3b8b-b652-7315dc6450d2 | -3.42858 | -54.58938 | 2024-10-28 00:52:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 25.1 |
| c13a0760-c684-3873-bb73-1c07369ab447 | -3.42289 | -54.58483 | 2024-10-28 00:52:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 19.6 |
| 16f0f47f-8ddf-3631-8ed3-9053c320e08d | -3.41654 | -54.50181 | 2024-10-28 00:52:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 28.0 |
| b9c3357d-634d-3ba0-837e-6f7b91ec77e0 | -3.41361 | -54.48047 | 2024-10-28 00:52:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 8c0987ee-3b36-3713-8ea4-3981f6133599 | -3.41158 | -54.49737 | 2024-10-28 00:52:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 946ff102-5ae3-32f2-9e8a-26400f4f5f3c | -3.1659 | -53.91794 | 2024-10-28 00:52:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 33.2 |
| b24b67a8-1d95-3236-92e6-60b2e1b4bad7 | -3.16579 | -53.91235 | 2024-10-28 00:52:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 28.0 |
| 86770f42-b41d-3726-89a9-91a9bc402d1c | -3.15318 | -53.91985 | 2024-10-28 00:52:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 21.3 |
| c46cd788-d9a7-32cc-9b20-7f197989d88f | -3.15308 | -53.91433 | 2024-10-28 00:52:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 20.8 |
| e5ceb316-596f-3185-b321-18e3d169b2f2 | -3.12419 | -54.27665 | 2024-10-28 00:52:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 17.0 |
| 325b6485-6e77-3465-930e-69577e862413 | -3.11106 | -54.29318 | 2024-10-28 00:52:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 56884f9a-5c93-371f-a82e-99fe054fb1c1 | -3.11106 | -54.27838 | 2024-10-28 00:52:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 31.0 |
| 2f8c2328-d5a2-305e-b7e4-c7fad766705e | -3.10835 | -54.27235 | 2024-10-28 00:52:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 2d95a923-f274-3d4a-ad17-e65a024dd9d0 | -3.08386 | -54.17752 | 2024-10-28 00:52:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 30b78ee4-d2a7-3235-9d03-92f8824a270a | -3.07085 | -54.17927 | 2024-10-28 00:52:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 34e857b8-a59a-33b6-b9de-b31686edb16e | -3.03492 | -51.4649 | 2024-10-28 00:52:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 15.6 |
| fe2575e2-9bcb-3ba3-9d0e-471e3d1deafa | -2.95677 | -54.68498 | 2024-10-28 00:52:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 17.0 |
| 093156e5-eb0c-3636-8e2f-280e827adc99 | -2.88815 | -49.49906 | 2024-10-28 00:52:00 | TERRA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 309d9be0-7cd1-3d4f-9405-26ee4a7a0c39 | -2.8853 | -51.83247 | 2024-10-28 00:52:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 19.0 |
| d62c5c2b-72a1-30dd-8bde-0709c60deb2a | -2.87825 | -51.82758 | 2024-10-28 00:52:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| d1a126ee-6e66-3236-83a6-c57e7885db59 | -2.87224 | -51.31047 | 2024-10-28 00:52:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 0c5095f1-7241-3d10-b704-6e5fa1e6f2a4 | -2.86433 | -49.25965 | 2024-10-28 00:52:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 73.4 |
| 35b43a68-44de-30e5-b259-886863007dd5 | -2.86417 | -53.33572 | 2024-10-28 00:52:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 74.5 |
| f9d36763-c969-3309-a5a2-f96924f22c6a | -2.8631 | -49.45355 | 2024-10-28 00:52:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| c0794940-8abc-35ed-929b-e8562631b6fe | -2.86303 | -49.25024 | 2024-10-28 00:52:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 75a2690e-f585-3127-a684-116d98c178f3 | -2.86172 | -49.24082 | 2024-10-28 00:52:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 26.5 |
| 8d5f1e05-86b4-38ad-bc12-bb03ae289ab5 | -2.85521 | -49.26093 | 2024-10-28 00:52:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| e6ec0b63-71bc-36e1-b3b2-187b7ecbf208 | -2.85391 | -49.25154 | 2024-10-28 00:52:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 36.0 |
| b8fb6c6f-2668-3e14-8e85-88e488469153 | -2.8526 | -49.24212 | 2024-10-28 00:52:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 15.9 |
| 1a58185c-4cb7-3362-851f-33f5504f853e | -2.85206 | -53.33723 | 2024-10-28 00:52:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 24.7 |
| 9e80dc62-57b2-3941-98d1-f865bdae2554 | -2.84972 | -53.32 | 2024-10-28 00:52:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 42fa0915-b864-3e99-95e0-de86dd1d94b7 | -2.84478 | -49.25279 | 2024-10-28 00:52:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 23.9 |
| 88ed864f-423f-3fff-848a-e83337ec0fd7 | -2.84349 | -49.24339 | 2024-10-28 00:52:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 43.3 |
| c471ab0c-3ac2-3249-bc38-29eac3cfb877 | -2.83878 | -51.81161 | 2024-10-28 00:52:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| d9ce24fe-31f4-3c20-9229-13b4dcc6d7c7 | -2.83566 | -49.25406 | 2024-10-28 00:52:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 49f8a016-9f88-3ec2-a864-ef851647a5b7 | -2.83437 | -49.24466 | 2024-10-28 00:52:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 08efd3b6-b233-37e4-963b-d3e64ddae7c2 | -2.83036 | -49.35121 | 2024-10-28 00:52:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 21.6 |
| a7088793-fc00-3314-8997-cdd033f67d02 | -2.82768 | -49.40007 | 2024-10-28 00:52:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| dbf79c9f-eb72-3c60-b0ae-3107c57e5627 | -2.82525 | -49.24593 | 2024-10-28 00:52:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 34.7 |
| 940fbdda-63af-3fe4-8f35-5cb01444c268 | -2.82396 | -49.23653 | 2024-10-28 00:52:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 33.4 |
| 7a2fc29f-d420-3ad6-9952-c5e6f855dd87 | -2.81485 | -49.2378 | 2024-10-28 00:52:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 26.6 |
| 83774ed7-bcf6-3dbc-b8ce-215d50b360d5 | -2.81356 | -49.2284 | 2024-10-28 00:52:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 64.6 |
| a21e2edd-a9e6-3329-b4f5-f6b038974545 | -2.80672 | -51.81607 | 2024-10-28 00:52:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 932a7d6d-0e69-3d60-b470-e16b189b357c | -2.80573 | -49.23908 | 2024-10-28 00:52:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| b5140699-f7e0-373e-b704-5855242d5fd8 | -2.80495 | -51.80296 | 2024-10-28 00:52:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 39.8 |
| ee5a458e-6f7b-32bf-a737-7b05dbf61e55 | -2.80445 | -49.22969 | 2024-10-28 00:52:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 8e76e5cf-1ab9-3cee-8d84-5bdba67c255b | -2.79427 | -51.80445 | 2024-10-28 00:52:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 21.3 |
| f83b289e-0acb-31a4-a5ab-a7e612374004 | -2.78188 | -52.90837 | 2024-10-28 00:52:00 | TERRA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| dcd4a4c7-2531-360e-b645-171c4b873c46 | -2.77733 | -48.69883 | 2024-10-28 00:52:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 4c78f8ab-c87d-39db-b019-3d1d65b7c75c | -2.77608 | -48.68979 | 2024-10-28 00:52:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 20fdecbc-89f6-32d4-a847-9a29fb207cb6 | -2.75074 | -54.03717 | 2024-10-28 00:52:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 8d180146-feda-32d4-b8e4-2541e92b30ee | -2.70746 | -49.05957 | 2024-10-28 00:52:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 1a9634bf-6407-3e33-8806-f4fdc3070292 | -2.70739 | -49.32249 | 2024-10-28 00:52:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 49.5 |
| 6ae59863-e406-338b-bfb3-84335aa7cd1e | -2.70619 | -49.05033 | 2024-10-28 00:52:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 90ca8a6c-0a40-34d7-b899-7a460eac0dca | -2.70607 | -49.31304 | 2024-10-28 00:52:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 172.1 |
| 2931346b-a0af-3526-8707-ece8993dfb0d | -2.70325 | -48.63275 | 2024-10-28 00:52:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 781b78da-33e8-3301-bd75-3fdff668e2c4 | -2.69825 | -49.32376 | 2024-10-28 00:52:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| f179323c-d5dc-39c6-8ead-0b9b7c884b05 | -2.69715 | -49.05161 | 2024-10-28 00:52:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| ec99ee31-fcec-3d5d-84e8-5593414849b7 | -2.69693 | -49.31431 | 2024-10-28 00:52:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 1434e8ad-637e-316a-a530-1c318ae00e6b | -2.68664 | -48.64426 | 2024-10-28 00:52:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 908ab9cc-7b87-3e6e-b3c1-93ad125f5b74 | -2.64409 | -54.30863 | 2024-10-28 00:52:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 7dfdbc59-ebbb-3e61-a113-8e17e92cfcc5 | -2.64127 | -54.28818 | 2024-10-28 00:52:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 18.8 |
| 95275101-33f9-30d8-bad9-df7f52d5d82c | -2.63851 | -48.55945 | 2024-10-28 00:52:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 38408f5b-b590-3a9d-a1a0-6d684ebb9b71 | -2.63441 | -49.2655 | 2024-10-28 00:52:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 57989ec7-3db2-3889-a422-b4faf3734d88 | -2.61259 | -48.37208 | 2024-10-28 00:52:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 82110a5b-d38b-3cba-b8fe-707010e8075d | -2.59934 | -48.2113 | 2024-10-28 00:52:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 681e9939-f4aa-3223-8829-9a88e41f2e58 | -2.5891 | -49.20191 | 2024-10-28 00:52:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| a9aee656-5622-3841-8487-77b8d4287ab1 | -2.5878 | -49.19259 | 2024-10-28 00:52:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| beeb6a07-b7a6-37d7-a6f3-ac7de50d115f | -2.58314 | -48.15953 | 2024-10-28 00:52:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 06bbe595-3b01-3ca7-a91a-38b7751be987 | -2.58191 | -48.1507 | 2024-10-28 00:52:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 8f2e49b2-cd61-3b46-a78d-adea55dbcc07 | -2.56572 | -49.23374 | 2024-10-28 00:52:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| da13e702-5234-3770-9578-1eeaa873a275 | -2.56464 | -54.01507 | 2024-10-28 00:52:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 30.4 |
| f2cec6b7-d7c3-34fc-a670-58f15eeff46c | -2.55148 | -49.19769 | 2024-10-28 00:52:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 01a8e952-e253-3772-b812-df6bfa271f48 | -2.54994 | -47.32384 | 2024-10-28 00:52:00 | TERRA_M-M | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 06b21add-d060-3ed8-9acb-ac7a2c75d749 | -2.5487 | -47.31502 | 2024-10-28 00:52:00 | TERRA_M-M | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| f8caae12-3e39-325b-8cc4-8cfd2c6881d4 | -2.54603 | -47.36037 | 2024-10-28 00:52:00 | TERRA_M-M | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 3fb8b1b0-2c10-383b-997f-53cd5bab30fc | -2.53725 | -47.37687 | 2024-10-28 00:52:00 | TERRA_M-M | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| bd33e202-2e5e-3dfa-a767-3fbcd76d5f5c | -2.53602 | -47.36806 | 2024-10-28 00:52:00 | TERRA_M-M | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| d5c3d27d-bdf5-3c8e-85fa-56bdcfb9e7e9 | -2.52939 | -47.44984 | 2024-10-28 00:52:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| d726467b-f1c5-3092-93e9-8a54ea6cc8c4 | -2.52841 | -47.37812 | 2024-10-28 00:52:00 | TERRA_M-M | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 66f81fea-e9bd-329f-be75-930d8084e763 | -2.52816 | -47.44104 | 2024-10-28 00:52:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 29.3 |
| 6dfccd89-1355-348f-a9da-6b0ffc43a8e2 | -2.52718 | -47.36931 | 2024-10-28 00:52:00 | TERRA_M-M | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 7685af35-1953-3f59-8fed-e249bcb4a71c | -2.52284 | -48.12893 | 2024-10-28 00:52:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 3a7bc07b-7191-37ea-8910-96b0db87927e | -2.52055 | -47.4511 | 2024-10-28 00:52:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 29.7 |
| a44ba61b-ebc9-359c-a73a-ebe5e4073f7d | -2.51932 | -47.4423 | 2024-10-28 00:52:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 92.0 |
| fca8626d-c3c3-31f6-abd8-43c8628743a6 | -2.50604 | -49.13416 | 2024-10-28 00:52:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 7d637cd8-0834-3264-901f-7898246262cf | -2.49657 | -48.06973 | 2024-10-28 00:52:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 3454cc38-ee62-315d-b8b9-fc45ab8c3243 | -2.49535 | -48.06092 | 2024-10-28 00:52:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 29.2 |
| 804c3b8a-ee86-36b9-a56a-83f8472bc3be | -2.49413 | -48.05212 | 2024-10-28 00:52:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| e5071049-aac8-3fe7-92fe-51b85412a7c8 | -2.49025 | -48.49231 | 2024-10-28 00:52:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| c6f357b6-1697-3209-ac0c-f22ab22f827d | -2.47501 | -49.11019 | 2024-10-28 00:52:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 21d1f58f-85b3-3be2-a2fd-2921b08ce4fd | -2.4686 | -49.06405 | 2024-10-28 00:52:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |


[Clique aqui para ver as próximas entradas](README16.md)
