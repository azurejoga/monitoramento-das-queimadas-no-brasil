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

## Dados Diários - Página 63

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 523c79fe-d1c8-3301-9a02-4f09ac9df540 | -3.66308 | -50.60846 | 2024-11-17 05:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cce8fc08-481a-3055-920f-fb381802e224 | -3.53331 | -50.25688 | 2024-11-17 05:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| af9f5f5f-8c1f-3a96-888f-5c4b3d907afa | -2.86508 | -46.71547 | 2024-11-17 05:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 28.7 |
| 874fd63c-5233-3172-91a7-dce52b1df21e | -1.56535 | -52.29232 | 2024-11-17 05:25:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 77e95ec6-558c-37f8-9fbc-f8f1079e935e | -3.17025 | -46.59959 | 2024-11-17 05:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c7574c80-3858-3a1e-b8c5-1d73f1262e31 | -1.1094 | -51.93596 | 2024-11-17 05:25:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bd80e73e-1746-34c5-9cb3-013f7676a621 | -3.17725 | -46.60063 | 2024-11-17 05:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 616fb4c8-fcd8-3a20-b557-2520189d2ba8 | -2.34349 | -54.82816 | 2024-11-17 05:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e2fec67e-7509-3601-86b3-b989adde8ed2 | -1.07992 | -53.64642 | 2024-11-17 05:25:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b4ac7ead-0129-3e99-8400-27cda3f4b54b | -1.22105 | -53.36535 | 2024-11-17 05:25:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5a9d24c2-a1f6-3ab1-a1f5-f5fda5469505 | -1.25234 | -52.02919 | 2024-11-17 05:25:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e4a6393f-002e-37e7-9fe9-52cd88c35479 | -3.10918 | -53.74705 | 2024-11-17 05:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f3a3e0db-a881-3acf-aef8-4ec135e3f4ff | -12.55269 | -57.76852 | 2024-11-17 05:25:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d17a5dcf-eb75-31b2-8a87-d77bcd243a1b | -2.81296 | -52.91882 | 2024-11-17 05:25:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 174bbd07-0f1e-3170-8aef-0bb362bdac6c | -2.99028 | -52.60165 | 2024-11-17 05:25:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5247c538-521b-3c60-8b91-011a6d4053b9 | -1.9686 | -48.38801 | 2024-11-17 05:25:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| f1b4ab50-d118-34d0-8e5c-d35127fffae8 | -1.20948 | -51.76581 | 2024-11-17 05:25:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a217a53f-3cb4-354f-9371-c5e80ee9a3b2 | -2.62151 | -54.15952 | 2024-11-17 05:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0408b076-cc99-3c03-bd9a-98a3bf5d539d | -10.94883 | -59.10428 | 2024-11-17 05:25:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bc11a877-5ff2-3b09-abb7-6049fcebb22b | -1.63001 | -53.28236 | 2024-11-17 05:25:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1944343a-a97a-30c9-a85d-8fe896d56ef3 | -1.36989 | -51.11206 | 2024-11-17 05:25:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f1952433-9e0b-3c4d-95d1-fe864f57c379 | -3.24277 | -53.51983 | 2024-11-17 05:25:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1525c251-72bb-3943-8933-19c2690d86b7 | -12.55669 | -57.82407 | 2024-11-17 05:25:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 33a26175-000a-31e9-9a99-dbec759bcade | -2.60001 | -47.55529 | 2024-11-17 05:25:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 75aea8fc-8dfa-398f-9e93-add25a6bceea | -12.87715 | -56.76623 | 2024-11-17 05:25:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 70fe2031-2696-367b-894e-52dc9ad04290 | -10.99797 | -59.09046 | 2024-11-17 05:25:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b74dc879-3d16-3bba-af83-c0bbf6c5134f | -1.52963 | -53.5612 | 2024-11-17 05:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a3eb81da-2c49-32cc-b923-4e3152f422a9 | -3.52897 | -50.25858 | 2024-11-17 05:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 176861ed-aa9e-346b-8dcc-684898e4011a | -2.34402 | -54.82464 | 2024-11-17 05:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d2c7ab86-7294-3c9b-b741-4ddd383e9bd6 | -10.95295 | -59.10077 | 2024-11-17 05:25:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b35349c3-27ee-31c6-bb34-d293fcacdfae | -3.58462 | -50.52868 | 2024-11-17 05:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 25f57135-d6aa-3ac5-94df-56905437b879 | -2.1605 | -50.70548 | 2024-11-17 05:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| baae41c8-fb3a-3769-a5b3-94cf11eab93a | -1.14516 | -51.69419 | 2024-11-17 05:25:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 0d0e98c0-2208-3338-be8b-43f08f6f64f6 | -2.60738 | -47.55086 | 2024-11-17 05:25:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6d627a9c-5fb3-3a38-b176-44660b036027 | -1.63494 | -52.66645 | 2024-11-17 05:25:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| aa8f5f91-ea0f-3459-9bdd-467d806596f8 | -1.32646 | -51.86781 | 2024-11-17 05:25:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 771555a2-1d25-31f9-8329-7b9f18a17354 | -2.62209 | -54.15555 | 2024-11-17 05:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 890daae5-ff09-37ae-b8db-5e434233a5dc | -2.34052 | -54.82049 | 2024-11-17 05:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 76419363-a6ff-3882-833f-e47c651891b1 | -2.15592 | -50.70953 | 2024-11-17 05:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e52aa373-9091-39e4-be6b-fcab74d2b2af | -3.25045 | -51.51947 | 2024-11-17 05:25:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1913b81f-dd95-3d2f-af1e-95a791469909 | -1.75057 | -50.47774 | 2024-11-17 05:25:00 | NOAA-21 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d8be8a56-04d9-3d19-9fbb-4c648feec643 | -17.5986 | -57.57419 | 2024-11-17 05:27:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 63d82dea-abcb-3aae-a076-9064c1ea0e9b | -15.56509 | -59.62019 | 2024-11-17 05:27:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 975f1622-82e8-3c09-bf09-0e8c6805d306 | -15.92089 | -59.80319 | 2024-11-17 05:27:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 160f63b2-ec12-3350-8470-5d2c6882c5d1 | -17.83172 | -54.54625 | 2024-11-17 05:27:00 | NOAA-21 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4abed077-49b2-3c8b-9c89-0ec66315d0f2 | -15.67423 | -59.72963 | 2024-11-17 05:27:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| de70febe-2ce4-3605-8f4e-388c7a6a8f65 | -15.67657 | -59.7275 | 2024-11-17 05:27:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 595fe217-255f-3921-8977-7ec1ac36ae33 | -13.91329 | -60.22387 | 2024-11-17 05:27:00 | NOAA-21 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7bfd0db7-076c-3c58-8e07-1ee394f8776f | -15.05141 | -58.23094 | 2024-11-17 05:27:00 | NOAA-21 | SALTO DO CÉU | MATO GROSSO | Brasil | 5107750 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 953b7383-2bc1-32d0-a293-016aad3bdefb | -15.92328 | -59.81229 | 2024-11-17 05:27:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ca53f60f-0fad-3e67-9d9a-a8c149fb6313 | -15.67175 | -59.73547 | 2024-11-17 05:27:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3cd787f7-a8c9-30eb-b04b-13950782417d | -15.67004 | -59.73335 | 2024-11-17 05:27:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1d24627e-22bd-3ba4-8962-dd018c8c2bcd | -19.49403 | -56.61481 | 2024-11-17 05:27:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.6 |
| 59dfa0b7-ab4b-340e-b200-537acceb27b4 | -14.88025 | -60.06367 | 2024-11-17 05:27:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5cd30908-ad35-3cc8-9e9b-5aa6b4215ece | -15.9173 | -59.80262 | 2024-11-17 05:27:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ce884b25-bd55-3af5-9c48-734f2f8798d6 | -15.67063 | -59.72908 | 2024-11-17 05:27:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 00fca693-5f80-368c-9bdc-59aabc3ea5b7 | -15.56448 | -59.62447 | 2024-11-17 05:27:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 8328811f-11af-3ccf-ada4-f1e0cd6d0e0c | -19.48946 | -56.6142 | 2024-11-17 05:27:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.6 |
| 3aaf8cc7-14f8-3502-a750-5e5005820763 | -13.91386 | -60.21998 | 2024-11-17 05:27:00 | NOAA-21 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 43974aa8-be61-3b47-89f2-d3be94d7afcf | -15.67363 | -59.73389 | 2024-11-17 05:27:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c705774e-8ee7-355f-8e3c-6515f6f9459f | -15.91491 | -59.81968 | 2024-11-17 05:27:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 95f65429-4f14-3698-b52d-b68fb2f27fd2 | -17.82694 | -54.54251 | 2024-11-17 05:27:00 | NOAA-21 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a2f9a580-9828-373a-b9d1-7a2004093b3a | -17.60377 | -57.56682 | 2024-11-17 05:27:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 52c9c19f-5940-3cd9-a8af-75136477d34f | -15.67782 | -59.73018 | 2024-11-17 05:27:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| aae5447f-8df6-39fb-8df9-8aded21ca747 | -17.82924 | -54.54401 | 2024-11-17 05:27:00 | NOAA-21 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 38de73d3-9d8c-36b7-8e39-9299ef1b38d0 | -17.60327 | -57.57081 | 2024-11-17 05:27:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 01ab04d9-44ba-3f27-a598-0ac728bd15ab | -17.82659 | -54.54565 | 2024-11-17 05:27:00 | NOAA-21 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1656a181-095a-3925-8d43-db0d87b7f3a7 | -17.60844 | -57.56342 | 2024-11-17 05:27:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| b206e642-ae50-3594-a356-5cd4ddd90199 | -14.87967 | -60.06771 | 2024-11-17 05:27:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b3a00993-6ac5-3357-90ef-9bd12a6c0a9e | -17.58779 | -57.59291 | 2024-11-17 05:27:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| e8eaf909-ca5e-35a1-8e09-ffd7430f4299 | -15.9155 | -59.81544 | 2024-11-17 05:27:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9cda875b-daad-30ec-a5ec-f0aa1b8ea05a | -17.59197 | -57.59349 | 2024-11-17 05:27:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 23a37cfb-4bb5-31e2-9d56-cf15aafaacae | -15.67236 | -59.73122 | 2024-11-17 05:27:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4a2c7b76-e59c-3f9e-b62f-d24c82f2c6e4 | -17.82891 | -54.54716 | 2024-11-17 05:27:00 | NOAA-21 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 62e4fb6a-0fed-358a-b5da-2a9ada868b00 | -15.92688 | -59.81285 | 2024-11-17 05:27:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 05ffdf95-e3bb-390e-88b9-a6b5422fe363 | -15.67596 | -59.73177 | 2024-11-17 05:27:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8aa5fe86-d9a1-3078-af53-9b1ad2fa5099 | -27.05846 | -52.623 | 2024-11-17 05:29:00 | NOAA-21 | CHAPECÓ | SANTA CATARINA | Brasil | 4204202 | 42 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 471fef8b-043b-3a2c-8f03-9954adabab24 | -4.5616 | -47.9925 | 2024-11-17 05:30:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 68.2 |
| 2df54ef9-cfe4-3c16-a5fd-92cb210d81ca | 0.6159 | -51.7676 | 2024-11-17 05:30:00 | GOES-16 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 6a8fd9b6-1b52-3b9f-b894-c8a53275fddc | -4.5614 | -48.0141 | 2024-11-17 05:30:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 73.9 |
| d88c3722-4fa3-3220-85a6-5cd69382523c | -2.5802 | -47.571 | 2024-11-17 05:30:00 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 13b44760-0b4e-3a3f-bbfd-372adcaaad01 | -2.6322 | -48.5634 | 2024-11-17 05:30:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 55.0 |
| a65853b4-f880-3332-abe3-44bc1fc6fb35 | -29.74734 | -51.94009 | 2024-11-17 05:31:00 | NOAA-21 | TAQUARI | RIO GRANDE DO SUL | Brasil | 4321303 | 43 | 33 | nan | nan | nan | Pampa | 2.5 |
| 5add02e5-62df-3b6c-adee-3bf90b9c352e | -2.8615 | -46.7086 | 2024-11-17 05:40:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 71.6 |
| 294102a8-ea8e-3b87-8aba-368bf8b23e4b | -2.6137 | -48.5639 | 2024-11-17 05:40:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 38.3 |
| 18def54f-851a-3040-88d0-143329d533e0 | -2.6322 | -48.5634 | 2024-11-17 05:40:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 56.9 |
| 854334fe-32d5-3795-a5e9-b07e1af41a3f | -4.5616 | -47.9925 | 2024-11-17 05:40:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 80.6 |
| c2602c27-5e14-37f1-bd1a-e7731cd8ef46 | -4.5614 | -48.0141 | 2024-11-17 05:40:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 81.2 |
| fa17a63e-f9bb-3a5d-a18a-1051448c16e0 | 0.6159 | -51.7676 | 2024-11-17 05:40:00 | GOES-16 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 53.4 |
| fe046dc7-24d9-37c9-83d0-70bb7e5ebac4 | -2.8614 | -46.7306 | 2024-11-17 05:40:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 65.6 |
| 429dc25e-940f-3262-8c31-caf444d83b15 | -2.32546 | -53.57165 | 2024-11-17 05:46:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 50d445d6-0bf1-3818-b3a4-e11d0827b53b | -3.48736 | -53.98905 | 2024-11-17 05:46:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 1cd9aa8c-bffa-3268-ad3a-a5f6b7010300 | -1.13583 | -51.68505 | 2024-11-17 05:46:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 28220a44-5d2a-3bbe-8a35-cf95fdeaf383 | 1.05404 | -60.59567 | 2024-11-17 05:46:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9ca39597-190a-3e70-926c-6eb984523460 | -3.02174 | -54.09674 | 2024-11-17 05:46:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 12dc0ac4-91f2-3602-98dc-e4cc01cc3217 | -3.02816 | -54.09771 | 2024-11-17 05:46:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 885d89d9-edb3-3e8e-becd-7d9c3a7d99de | 0.61606 | -51.778 | 2024-11-17 05:46:00 | NPP-375D | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 21.5 |
| fcd8a756-ad20-3c0a-a12a-8cb65ab81b98 | -2.41718 | -54.62447 | 2024-11-17 05:46:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b1781564-673d-3190-a3eb-dfe962243ca3 | -1.63881 | -52.66389 | 2024-11-17 05:46:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| ca9bf4a8-1f36-33ee-9799-95c9f062fea4 | -1.62801 | -53.29069 | 2024-11-17 05:46:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README64.md)
