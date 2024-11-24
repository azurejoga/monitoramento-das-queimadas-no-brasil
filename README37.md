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

## Dados Diários - Página 37

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c6e00305-403a-39b4-a7c5-72dcac8919f9 | -4.19445 | -50.69044 | 2024-11-24 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 7f8ee1bb-ac15-3c4e-bd61-4ee1ac6060f2 | -3.02299 | -51.44436 | 2024-11-24 04:53:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c3bc1402-b198-3c7a-acff-483cd332fd38 | -3.25491 | -54.23663 | 2024-11-24 04:53:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bb026bdf-b9a0-3c27-a3ca-395c09185e69 | -3.43761 | -51.20544 | 2024-11-24 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 56470c5f-eacc-3f2b-a6ba-fa87d2d4b0b3 | -2.3228 | -51.31061 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 822ec365-c309-31a9-9f35-8dc06c97d5a5 | -2.7758 | -54.04817 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 384bcefb-1798-3875-940b-3e264932b2ce | -1.30879 | -51.74721 | 2024-11-24 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f8896864-e0a7-3d6a-94b4-5b30b8c39a46 | -2.37333 | -50.32907 | 2024-11-24 04:53:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fdff4bea-b16f-3a69-8b34-8e957e48ac52 | -2.84861 | -53.96492 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f53659ed-083b-3e40-bf31-813dd27d8096 | -6.3625 | -47.91142 | 2024-11-24 04:53:00 | NOAA-21 | ANGICO | TOCANTINS | Brasil | 1701051 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ef934ba7-6581-38b6-92b6-2e0dac943742 | -2.38389 | -49.89848 | 2024-11-24 04:53:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 309b1a71-a11d-3f12-8e19-b706acebf8d5 | -0.02153 | -50.86326 | 2024-11-24 04:53:00 | NOAA-21 | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 22c991dc-c496-3679-af17-57e2a4ed84cf | -0.81857 | -51.60004 | 2024-11-24 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 55e89c07-6086-3ec6-8b96-de1fa389b942 | -2.18014 | -54.46932 | 2024-11-24 04:53:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 570bf15a-52d5-3370-9568-a05d05743377 | -2.08414 | -45.54716 | 2024-11-24 04:53:00 | NOAA-21 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c541e31e-e5bf-3239-bb7c-06680b0a32ff | -1.22223 | -53.68085 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| bfa2898b-2593-3233-8286-6cb933fa818f | -2.59962 | -46.26413 | 2024-11-24 04:53:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 65a4a338-2c72-31b4-995d-d0afe647c7e3 | -3.22176 | -53.93541 | 2024-11-24 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 606f3334-04f9-3d73-95d2-b18b393a199d | -3.24646 | -53.28097 | 2024-11-24 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 97a0aefc-1ff5-3676-b192-822bf44d3b04 | -4.35792 | -45.87841 | 2024-11-24 04:53:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b105655a-544c-32dd-a443-d369d52309ba | -1.94076 | -49.52078 | 2024-11-24 04:53:00 | NOAA-21 | LIMOEIRO DO AJURU | PARÁ | Brasil | 1504000 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4b70b25e-9ecd-35b1-a17a-2cba664f2ea5 | -1.46579 | -51.1133 | 2024-11-24 04:53:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2799cb0c-42e2-3a5b-920c-e1cdacc20810 | -10.1049 | -49.58812 | 2024-11-24 04:53:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9878b2a9-9bac-38f7-a2bc-10134d2db905 | -2.60648 | -49.48068 | 2024-11-24 04:53:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0604aa47-4201-3970-8fdb-f623dc9779b7 | -3.48583 | -49.91604 | 2024-11-24 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 96913266-1175-3d5a-969d-51b6abaab65b | -2.24193 | -50.47491 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 368027f7-72cf-3836-ba1d-1bab0abc01d8 | -3.72042 | -51.31031 | 2024-11-24 04:53:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 4bd33835-62e2-3b92-b07e-2eae05aa3378 | -2.3665 | -49.83137 | 2024-11-24 04:53:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 710568bc-d75e-3853-a9b6-8032412575db | -2.38157 | -49.84453 | 2024-11-24 04:53:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4ab9242a-b55e-3635-a608-89e874717bbe | -3.91849 | -50.57386 | 2024-11-24 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ac8f5645-13be-30d6-ab50-bf9caa7fada3 | -1.42612 | -51.12843 | 2024-11-24 04:53:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fe227e53-0fa3-38be-b4c5-e25b04e59dbd | -2.44105 | -46.14008 | 2024-11-24 04:53:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 846fd0ff-fa1a-37d3-88b5-82425c6e385b | -3.17524 | -46.55104 | 2024-11-24 04:53:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 682b7df4-2508-308f-8b70-767eec5accca | -3.10077 | -53.87943 | 2024-11-24 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c50f11da-fee8-3d78-b53b-0450e96e3bbc | -2.69794 | -46.27335 | 2024-11-24 04:53:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1c9e96c3-c40b-3589-8a20-d7b834a45df2 | -3.89382 | -52.31763 | 2024-11-24 04:53:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 43395787-5523-37bf-9df3-88156f680592 | -4.1952 | -45.36245 | 2024-11-24 04:53:00 | NOAA-21 | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a8c916c4-efc4-3687-b917-ebb6240e23c2 | -3.84851 | -44.05439 | 2024-11-24 04:53:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 92040aa4-f737-3a27-b1d3-77a573bd94aa | -1.06408 | -53.18664 | 2024-11-24 04:53:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 469ba998-84a8-394a-88c5-d89311df8bf4 | -3.0434 | -54.02093 | 2024-11-24 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8f5b4d7d-2933-37e8-807b-8b505c85e9ea | -2.53868 | -53.99331 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 31745a99-f2c8-30e0-850c-20035ee73cfc | -2.53857 | -54.01625 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 519876ef-34df-36b4-93c3-89f2adbb8dc4 | -1.95471 | -46.43782 | 2024-11-24 04:53:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 7c6d3aea-84d7-3538-88ee-aebefadca800 | -3.86577 | -44.18428 | 2024-11-24 04:53:00 | NOAA-21 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 293cc3f3-ac80-3b77-8880-c455b90f4911 | -3.2124 | -53.84025 | 2024-11-24 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 961e479c-6d58-3b84-a486-ba4d3bcd82e8 | -3.6718 | -51.7331 | 2024-11-24 04:53:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2ba9a408-abda-34d1-a372-0bf17907abb1 | -3.51269 | -54.73711 | 2024-11-24 04:53:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 083b55d0-494f-37e1-9fb6-22d8869a2783 | -2.06692 | -50.3121 | 2024-11-24 04:53:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f912575a-f87d-3c54-a228-16119a37c77a | -3.23268 | -53.39124 | 2024-11-24 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c4904ae0-ab89-38a1-8436-494b22fdb69a | -1.98914 | -49.54306 | 2024-11-24 04:53:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c888bc37-f0f6-35e7-ab35-c41fe3f322ac | -2.70821 | -46.26241 | 2024-11-24 04:53:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1a9d461f-9ff1-3d09-ba46-2d760ba090e6 | -2.82552 | -54.022 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9c6f8cbe-bb15-36f8-b48b-4f16020f7c71 | -4.51703 | -45.72143 | 2024-11-24 04:53:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7595c750-3cae-3132-88e8-43d5f0dc296a | -2.54701 | -54.05201 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 46ad32bd-9bf9-3f4c-a291-3ade9c717223 | -2.54043 | -53.98217 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 95b24c0d-3eae-36e9-9fb3-c8bfe57f6587 | -3.84439 | -44.04752 | 2024-11-24 04:53:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 87ca525b-c93e-3e56-a2d9-17e232c913f3 | -2.07636 | -50.75129 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| aa574d28-2a18-3786-b422-f410b4f2dd3f | -4.96885 | -50.04971 | 2024-11-24 04:53:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8044efa3-a7de-39b5-9271-f916d35abc8f | -2.54555 | -53.99428 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2c8158f9-8d5b-32a2-a427-44bd85c91247 | -0.11618 | -51.65157 | 2024-11-24 04:53:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.3 |
| d943d136-b17b-3716-aad9-f5c5aadee8e6 | -3.26128 | -52.94634 | 2024-11-24 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bc7e208e-8fe6-3e96-894e-b44fa1034170 | -2.6687 | -46.15195 | 2024-11-24 04:53:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4185d7ab-88a5-30e8-9fcd-b92b3910f716 | -1.64037 | -53.87874 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 085c5524-4058-39ce-a1af-37816944a7ae | -1.24231 | -53.39481 | 2024-11-24 04:53:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d3f2344a-a843-3c82-a662-e4751c38e216 | -1.89726 | -53.00945 | 2024-11-24 04:53:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 041b28d4-e0d9-34f3-9366-4113c1b33915 | -3.56794 | -51.11048 | 2024-11-24 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f400fcff-332c-3397-89f6-1d9f14cf7763 | -3.04329 | -49.44402 | 2024-11-24 04:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 17dfc85b-dd88-33f9-a73d-c96f05c755db | -3.50345 | -50.46669 | 2024-11-24 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 14010c7a-72b9-337e-9fbe-e4c6aa12dbbc | -3.18219 | -54.32161 | 2024-11-24 04:53:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b4051a3e-9f9e-3fe7-98e9-5c49ac64b393 | -3.95409 | -45.99152 | 2024-11-24 04:53:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c969f5b4-af21-32f4-9ebe-37e90d1db5d0 | -2.82095 | -52.95601 | 2024-11-24 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d06db475-f96e-3a47-8dfd-221d4725d326 | -1.21528 | -51.73986 | 2024-11-24 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d7de2293-727e-3e70-aafa-b28410bc7a85 | -1.48029 | -51.15091 | 2024-11-24 04:53:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 6c98e477-cb36-36bb-9ec9-dddebc51d8f7 | -2.73702 | -46.09611 | 2024-11-24 04:53:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d091eebd-53de-3d09-9e0e-139e56cea90a | -2.28663 | -53.63092 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f431601b-ccd7-3b34-bb06-960539e81586 | -3.22373 | -53.38258 | 2024-11-24 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 55baf585-0074-3392-92a5-e2268022804d | -2.58033 | -51.88316 | 2024-11-24 04:53:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| bd5f128c-6353-315f-a9be-64c33501a755 | -2.44278 | -49.08522 | 2024-11-24 04:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| abce4754-9fbd-3a66-a679-e27fec8576e1 | -1.47197 | -51.13902 | 2024-11-24 04:53:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a7cafb47-cf1d-36da-840d-271532b6037a | -2.53213 | -47.31971 | 2024-11-24 04:53:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 25d24908-4595-3f42-a57d-fc0ac2c3ad34 | -1.0393 | -52.99256 | 2024-11-24 04:53:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6a7a8b51-c1f2-3db4-ad74-e3b655156fb6 | -0.99707 | -51.78624 | 2024-11-24 04:53:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bd857742-6704-3db7-8dea-8772dd254527 | -2.87091 | -50.40465 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 031b9dfc-ac7f-3041-90b6-46b2afc4de8b | -4.11601 | -54.23174 | 2024-11-24 04:53:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5c2a65e4-2f2c-3cbd-909c-89eee099e60f | -3.25325 | -54.22491 | 2024-11-24 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 17ad953e-5537-394d-b531-0a3a8a20325a | -2.55959 | -54.06159 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 311554fe-bcab-383f-9677-ddc22b7cd2ca | -3.25699 | -53.27528 | 2024-11-24 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7241c8fd-3927-3433-b844-85751892154f | -2.38631 | -50.33477 | 2024-11-24 04:53:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 17a443ea-9024-344b-8391-71f4073a246a | -3.23988 | -45.54892 | 2024-11-24 04:53:00 | NOAA-21 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c0c59a79-4b3b-344e-8cbf-20de9bbc153e | -2.97013 | -53.8854 | 2024-11-24 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 51f98d83-ecf0-3701-ba5c-852e1cc4d1bb | -3.89552 | -52.19826 | 2024-11-24 04:53:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cd170261-0a63-335f-adfc-d3d10230d04b | -4.08925 | -54.75724 | 2024-11-24 04:53:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 01df044b-f503-33bf-9fa4-c95908de2c15 | -1.50054 | -49.46304 | 2024-11-24 04:53:00 | NOAA-21 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| eb9be9a4-d8c7-39a3-9160-b732431d290d | -1.46846 | -46.04466 | 2024-11-24 04:53:00 | NOAA-21 | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d8e78afc-a931-3529-aeaf-b0bf02c42338 | -1.34921 | -46.91177 | 2024-11-24 04:53:00 | NOAA-21 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a8eb418e-4f78-38f1-ad33-837a6d00aa0d | -2.86228 | -53.96703 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 4c60860b-fd3d-324e-bd84-60c8c561cd73 | -1.7939 | -53.66336 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f0945fde-0f20-3e1b-80d0-b9480bd670a2 | -10.09975 | -49.5969 | 2024-11-24 04:53:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7ed7cced-827a-351c-a751-9d80ec161979 | -3.94801 | -52.25211 | 2024-11-24 04:53:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f3c3ee68-3abe-30fc-a6ba-a58b4a3e2220 | -4.02215 | -53.77795 | 2024-11-24 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README38.md)
