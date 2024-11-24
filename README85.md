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

## Dados Diários - Página 85

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 62e7be0a-c211-36f3-a4fa-fcecc47467ec | -3.51292 | -53.8158 | 2024-11-24 05:40:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 8857a886-aa33-3ad3-8f40-6b77577ad5b4 | -3.25241 | -54.22779 | 2024-11-24 05:40:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0afe4e0c-56f3-3771-a086-60a4691a3c76 | -3.7045 | -51.79917 | 2024-11-24 05:40:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fa2bcb2f-1c5d-33a6-bb55-728ba8cf8033 | -3.24785 | -54.21888 | 2024-11-24 05:40:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 90d5e605-c321-3fb5-89d8-93f3a711a19f | -3.52233 | -53.81448 | 2024-11-24 05:40:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e89fda89-3e18-34ba-9f3f-2e5ee50586de | -3.29653 | -53.85596 | 2024-11-24 05:40:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0458980a-ab32-3857-b976-13af1aacaebf | -8.92762 | -64.30514 | 2024-11-24 05:40:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cdc78235-6dca-3e5f-a545-6836a0fc6a4a | -4.1613 | -54.58212 | 2024-11-24 05:40:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 3dac7850-b39b-3a0a-bb36-c7d8fc6dc76d | -4.16186 | -54.57838 | 2024-11-24 05:40:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ad134440-c0f5-3369-bf11-3f5bd478dae4 | -4.05481 | -53.65202 | 2024-11-24 05:40:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 58765745-3b4b-372e-87c6-ac60dde52dc8 | -3.23966 | -54.23683 | 2024-11-24 05:40:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2cb1fc32-c08a-3e96-a861-d7661a44539c | -3.51231 | -53.82013 | 2024-11-24 05:40:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 6d5af37f-6b4f-3d0d-9112-03ee3efc5e47 | -3.18115 | -54.77272 | 2024-11-24 05:40:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3d18f903-03f8-3501-a8d3-da2d1ee492ae | -3.2414 | -54.22466 | 2024-11-24 05:40:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0aa167ff-5fad-383f-b0e6-005abe3b0cc6 | -3.24601 | -54.23371 | 2024-11-24 05:40:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3002e8db-a1e7-348d-a3a1-c7804c3f6940 | -3.24937 | -54.24784 | 2024-11-24 05:40:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b7a93d9d-ec93-3823-a1d9-b0752965f8c5 | -3.23964 | -54.23417 | 2024-11-24 05:40:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2f8c5b6b-db8d-36a6-a4e5-c056e90d22f4 | -3.50616 | -53.80033 | 2024-11-24 05:40:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8dec8a58-695d-304f-91a1-5df31e6ce90a | -3.24724 | -54.22289 | 2024-11-24 05:40:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 032cfde7-b161-36f4-b501-89ee697b80c8 | -3.25116 | -54.23604 | 2024-11-24 05:40:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ba4b18d5-44e2-3398-9051-a530d9c6374b | -4.15557 | -54.58139 | 2024-11-24 05:40:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1e5b8f78-6f6e-3e73-b636-ced13c999aca | -3.22511 | -53.93046 | 2024-11-24 05:40:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4ee6aa40-8bb3-3dd0-a9f7-c8b0a2b6a155 | -3.68046 | -54.58788 | 2024-11-24 05:40:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d0f0c74d-b390-3375-8e4c-fc8a83bc295d | -3.51891 | -53.81646 | 2024-11-24 05:40:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| c1aae108-3a0e-3452-bb76-9d01622908fc | -3.24663 | -54.22693 | 2024-11-24 05:40:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 348f1423-3ff5-3acd-b66c-10a69debd743 | -3.24024 | -54.23278 | 2024-11-24 05:40:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 71499a91-ca2b-37e2-85dd-e158d4cc4c10 | -3.25296 | -54.22641 | 2024-11-24 05:40:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8fe51f0d-1957-3aa6-b33c-3c7ba08e402c | -3.28469 | -53.85414 | 2024-11-24 05:40:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d3d7fe58-ccf6-3264-a466-da616294ffc1 | -3.51569 | -53.81814 | 2024-11-24 05:40:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| e267b701-63ee-3d2a-a154-fddfb3464105 | -3.2466 | -54.2296 | 2024-11-24 05:40:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d2016c1f-bfa0-3158-b853-fdf2d5029584 | -3.50488 | -53.80894 | 2024-11-24 05:40:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5354d663-2c91-3b83-a035-de97bd99bea6 | -3.25483 | -54.21182 | 2024-11-24 05:40:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9b71eb9a-d640-3221-b3a6-011a3288c7fa | -3.23903 | -54.23817 | 2024-11-24 05:40:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b808a883-f7a8-3655-a17d-f392e747f456 | -4.16244 | -54.57447 | 2024-11-24 05:40:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 833bf119-2fba-3c67-9c58-d064f8a70a42 | -3.25062 | -54.24268 | 2024-11-24 05:40:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c286cb55-e903-3c72-89bf-4510f6b2feb0 | -3.33726 | -53.33366 | 2024-11-24 05:40:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1359e6be-9dd7-3b0e-b80c-461807879c50 | -6.22217 | -55.65892 | 2024-11-24 05:40:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 35582f0c-55cc-3399-b7e5-4ec0ac752cd4 | -3.2448 | -54.23909 | 2024-11-24 05:40:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 89b1e439-ce89-3493-b6c1-e6a8a4d3fc04 | -3.2656 | -53.81947 | 2024-11-24 05:40:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 2cdb026f-bd3c-3087-8e9c-46bee569cebb | -3.2281 | -54.23232 | 2024-11-24 05:40:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f6167065-49ff-305b-aa57-09c9bfc4ff22 | -3.24082 | -54.22872 | 2024-11-24 05:40:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3e028bef-24d8-3fdf-8724-08593b718cd1 | -3.50968 | -53.81763 | 2024-11-24 05:40:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| ae2a1595-893f-32b1-ad22-8aa36551bf36 | -3.24833 | -54.21749 | 2024-11-24 05:40:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 48956ee5-5a20-3363-ae20-814546671ec3 | -3.25006 | -54.24659 | 2024-11-24 05:40:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e0a6de79-1b8e-35ca-871e-327d9417f8c4 | -3.51768 | -53.82511 | 2024-11-24 05:40:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4df372f7-ba02-3e12-8d27-946df13bfb55 | -3.22453 | -53.93441 | 2024-11-24 05:40:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 36aaebee-2fbb-338a-8452-a861b4a6ad28 | -3.18554 | -54.77275 | 2024-11-24 05:40:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e2f64e39-489c-3567-ba29-a19a2220e656 | -3.18169 | -54.76919 | 2024-11-24 05:40:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8b289529-baa9-3d25-aa73-a12eda65e4d8 | -3.23268 | -54.24113 | 2024-11-24 05:40:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bddd0ec7-cd3d-3173-a085-0ddf1e66b03b | -3.21923 | -53.92953 | 2024-11-24 05:40:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 6ad6ebf7-48f0-35ed-bf07-e4f5c309bb5e | -3.25354 | -54.22237 | 2024-11-24 05:40:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c2275844-a604-369c-ab14-fcd1e5bd3dc2 | -3.51953 | -53.81212 | 2024-11-24 05:40:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 37b24a3a-a1bf-3d65-8df7-90144f8ec3ae | -4.15819 | -54.57542 | 2024-11-24 05:40:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| df91e194-18dd-3368-8716-63662c3e0c41 | -4.16391 | -54.57631 | 2024-11-24 05:40:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 64829803-267f-31a2-8f48-af639ffb2fa5 | -3.24085 | -54.22607 | 2024-11-24 05:40:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 17966238-6153-3ddc-b624-b43568bfa769 | -3.22393 | -53.93851 | 2024-11-24 05:40:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5c369cd9-6ef6-369f-9031-ac063b693d6e | -4.16337 | -54.58016 | 2024-11-24 05:40:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e913f1ed-212b-3b8e-8941-8f80bb4fc484 | -3.18502 | -54.77629 | 2024-11-24 05:40:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 303a388e-d5e5-3e75-b2c2-1518890af3b0 | -3.24421 | -54.24294 | 2024-11-24 05:40:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 48c44303-7a7d-3191-a3c6-59108e1ee32d | -3.17884 | -54.32621 | 2024-11-24 05:40:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 16a02125-00f3-38d9-b7aa-046b43149c13 | -3.17996 | -54.77195 | 2024-11-24 05:40:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2a91175d-0f37-38e2-8a3a-2029c1985b23 | -3.28661 | -53.84127 | 2024-11-24 05:40:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9136061f-2a0d-3bee-9a37-63a4948c5fb5 | -3.50904 | -53.82191 | 2024-11-24 05:40:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| afaecd75-aa72-3b61-8bc3-05608f85731a | -3.67481 | -54.58683 | 2024-11-24 05:40:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3b3da40a-d5b1-31e4-aa7b-ddfe1238284a | -3.51634 | -53.81381 | 2024-11-24 05:40:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e514b48c-5d9c-3495-acad-147bd8e54082 | -3.28134 | -53.836 | 2024-11-24 05:40:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e757e4f3-d86e-31f4-8fee-75f7f4585be6 | -3.52168 | -53.81882 | 2024-11-24 05:40:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| d3121ded-6c13-3121-b266-1dfaffc0c096 | -3.23786 | -54.24592 | 2024-11-24 05:40:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d8196932-db20-3f59-b8c3-72fa696c64e2 | -3.24431 | -54.24553 | 2024-11-24 05:40:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dc7ca8d2-3768-3f6b-9e1b-b74158d86b9a | -3.24318 | -54.25338 | 2024-11-24 05:40:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 18edfdcc-7abb-3230-9748-542207f54103 | -3.25179 | -54.23191 | 2024-11-24 05:40:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 62d770fb-b3c4-3785-a5b8-6d2258dd56cb | -3.70534 | -51.79319 | 2024-11-24 05:40:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e6b28804-d6ea-3b6a-9d1d-0e63f9b492d4 | -3.7714 | -52.40682 | 2024-11-24 05:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 4c2f9066-12ec-3091-aa74-650a72dc1059 | -3.17431 | -54.3172 | 2024-11-24 05:40:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1df1d806-3f20-3120-b58e-43a335c3bcb0 | -3.82362 | -52.41145 | 2024-11-24 05:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| f915c9e3-c014-3520-8898-5e35d956630a | -3.51698 | -53.80952 | 2024-11-24 05:40:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cdb1f89e-eb4f-3e8b-84b9-35e7d26b3216 | -3.57793 | -54.51945 | 2024-11-24 05:40:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 68782e56-ec0b-3b9e-9e76-5428e2c13968 | -3.2275 | -54.23635 | 2024-11-24 05:40:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 61d7f1b3-de5b-3c24-af48-e5f6abd4a43b | -3.24542 | -54.23778 | 2024-11-24 05:40:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8fc10978-3a45-3c86-9903-cef9ec368ec7 | -3.52103 | -53.82312 | 2024-11-24 05:40:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 7a7431b5-f790-31be-b20d-2218b1ae56c8 | -3.25177 | -54.23466 | 2024-11-24 05:40:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5175ba32-e53e-3994-a794-696b90fc0b75 | -3.24776 | -54.22149 | 2024-11-24 05:40:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6a044e38-bd6e-352d-8238-960d71c0ecf1 | -3.25469 | -54.21442 | 2024-11-24 05:40:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 892ae7ff-1a13-32a0-a6f9-ba956ff7c501 | -3.25526 | -54.21043 | 2024-11-24 05:40:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dd6e6de6-3282-3f4f-abfa-631d21625cbb | -3.25118 | -54.23875 | 2024-11-24 05:40:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d1f7abad-8459-314f-b2e2-ba6b241af515 | -3.23845 | -54.24205 | 2024-11-24 05:40:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b4b6765f-6027-3376-ac51-67b5dac3eb27 | -3.51505 | -53.82245 | 2024-11-24 05:40:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 3b7bc7e9-0c88-3619-90fa-d0235b753846 | -3.51281 | -53.79664 | 2024-11-24 05:40:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a88b6ac4-874b-3d4d-99f2-a3836ecf117b | -3.50425 | -53.81317 | 2024-11-24 05:40:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a08a18f5-4623-3476-b3a3-961cf0e69076 | -3.23327 | -54.23726 | 2024-11-24 05:40:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2397318c-8e1c-30d9-8dc0-f9eada39fce7 | -3.25412 | -54.21838 | 2024-11-24 05:40:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4defe185-e13f-3e3c-83c5-4c9df7e0f5f6 | -3.23387 | -54.23325 | 2024-11-24 05:40:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 560c540c-b1db-3069-b906-4d1cf1ac0496 | -3.28996 | -53.85936 | 2024-11-24 05:40:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b17eedc5-e81d-3167-8eda-07ae8317b2f1 | -3.22692 | -54.24024 | 2024-11-24 05:40:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4de6c9ce-c0a8-3297-b7c5-2d3c910dada0 | -3.47892 | -51.99453 | 2024-11-24 05:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| d743c2ae-e7c2-34a4-87b2-6dc31f732647 | -3.51169 | -53.82447 | 2024-11-24 05:40:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 776e7121-ddb7-3fd6-86c2-0ccee55484bc | -3.26493 | -53.82401 | 2024-11-24 05:40:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 23c63c6c-af86-3481-8c4c-207d20eb3699 | -3.82364 | -52.41445 | 2024-11-24 05:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| dc19c850-495c-352a-bdf4-34c4031b0847 | -3.21864 | -53.93355 | 2024-11-24 05:40:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c6e6ac8a-5ccb-3ba0-a398-95241f417e22 | -4.15763 | -54.57939 | 2024-11-24 05:40:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |


[Clique aqui para ver as próximas entradas](README86.md)
