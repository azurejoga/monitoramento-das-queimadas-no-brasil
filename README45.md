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

## Dados Diários - Página 45

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9a2de836-322a-3082-b521-c66c81b8e0a2 | -0.3776 | -51.54879 | 2024-11-24 04:53:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5cff706d-9680-3b34-b468-27f9ddfccfd3 | -2.31209 | -53.60139 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9f258a27-ec95-3564-8e73-384547d7804a | -2.10538 | -50.13242 | 2024-11-24 04:53:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1ac7b528-34e8-3f9e-93b0-fcba3c3ac1b1 | -1.39046 | -51.13719 | 2024-11-24 04:53:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bd96c261-4cf3-3fce-8295-0bac4325ca34 | -3.09873 | -54.00307 | 2024-11-24 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 92217b26-0336-3476-bf73-d3a6d55eb1e5 | -3.3618 | -53.53926 | 2024-11-24 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bdf0ba0b-8a62-3f5e-8ba4-93295826d9ec | -1.86755 | -48.16764 | 2024-11-24 04:53:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 07b73505-cc24-35c7-8c23-ce053b9d5cdd | -2.18142 | -53.78677 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c78957ad-5ec7-3658-9f2c-73958304d403 | -2.07365 | -49.8636 | 2024-11-24 04:53:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b9a50fbc-99fd-32ea-a320-ecfa730169ff | -2.78034 | -52.86762 | 2024-11-24 04:53:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d6c574c2-6c74-38c5-b3d0-baa90628ae2d | -3.10232 | -53.73775 | 2024-11-24 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f85aa287-19d5-366d-94b1-44196d9dc189 | -2.33266 | -51.29087 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 298331f7-99f1-3cf0-a6d5-55e7600191f0 | -3.2908 | -53.85646 | 2024-11-24 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b74cf9e8-cae6-3636-9b21-b8b92418a0d8 | -3.68744 | -50.11174 | 2024-11-24 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c4d3d104-1c20-3e58-a93d-4ee07ade296d | -2.6895 | -46.27205 | 2024-11-24 04:53:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0b9fce28-15f5-3c9f-875a-21f631053263 | -1.36789 | -52.54661 | 2024-11-24 04:53:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f7087c7a-dcd6-37af-a950-86ca62747e51 | -2.57275 | -54.06743 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c4d9d81b-7cab-3555-a152-37f94289935d | -3.66795 | -51.73603 | 2024-11-24 04:53:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ceccabbf-e473-3cc0-b5fe-1f5f43f26cd6 | -3.10227 | -45.78544 | 2024-11-24 04:53:00 | NOAA-21 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| ac0437f0-aaa1-3dd8-b465-9b6f19bd3b5b | -1.2549 | -51.74594 | 2024-11-24 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f360313b-7a9e-3fa7-a5c0-8185c09acd57 | -2.58156 | -49.21931 | 2024-11-24 04:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b28c6e0e-a99c-32c9-8a02-02a41fcfb7e1 | -3.56705 | -51.64193 | 2024-11-24 04:53:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 579e4f64-1464-3c0c-8b93-b017a821f668 | -2.22156 | -50.38361 | 2024-11-24 04:53:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 10ca0c1f-2d27-387f-a1d3-ac0857023d5e | -1.42353 | -46.05366 | 2024-11-24 04:53:00 | NOAA-21 | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cf3d275d-df15-3b5b-9e82-c0812f5509aa | -3.25372 | -54.24413 | 2024-11-24 04:53:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f6d9bb57-7f09-336f-9275-d3de1fd88d7c | -2.39131 | -49.80376 | 2024-11-24 04:53:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4b03d354-d182-36ee-b191-aa7aa5feae09 | -2.24309 | -53.62048 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4e25e608-f220-381f-93ee-69376d45fbfe | -2.33428 | -51.28049 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| dc977778-6f99-3dd5-94e0-50eee353aee1 | -2.09598 | -48.88643 | 2024-11-24 04:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e7583ee4-a2c8-3a6c-b7f7-527faa30f793 | -2.84724 | -54.01778 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 90761f80-347f-3c08-9412-0b5ed6ed65b1 | -2.86287 | -53.96334 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ea01efe6-126a-379e-9ab2-4303454eff93 | -2.26718 | -50.46779 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8ecde2a1-2034-364e-a6ec-577c96f258e3 | -3.2043 | -52.57217 | 2024-11-24 04:53:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 21a8601f-8c66-3824-b34b-ebdfbf57a085 | -0.94698 | -51.64847 | 2024-11-24 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7db7738d-c345-3708-8735-69bc4756a95d | -1.44964 | -53.39388 | 2024-11-24 04:53:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3c9c80a2-639b-347a-8369-a0f2170491f2 | -2.05515 | -50.73361 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f63dd3f0-7e0c-308e-96bb-cc08fbd04235 | -3.63726 | -51.51797 | 2024-11-24 04:53:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| da9cf7db-242e-3bd0-b5c9-7db358c24792 | -1.4502 | -54.96793 | 2024-11-24 04:53:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 65fcf45f-fe6d-38e0-912b-ffcdb7f5937f | -0.28333 | -51.49906 | 2024-11-24 04:53:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e4df8c10-9039-32cc-8fc0-13adf8b63f34 | -3.54428 | -49.88206 | 2024-11-24 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9ada2a72-2306-3c52-86b5-e222989d9580 | -2.82045 | -54.00982 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0e3a3f1c-309c-39f7-89ee-676b0223d01b | -3.90836 | -50.59466 | 2024-11-24 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| aa68c8f9-390b-357e-a6ce-477f65242050 | -2.32368 | -53.86535 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 28dbea56-0e72-3883-a198-9ff9aeff0fc1 | -1.89003 | -53.3178 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ba9e17bd-089d-3584-823a-85c7c09c97a0 | -3.29458 | -49.90716 | 2024-11-24 04:53:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0a4329ee-cf01-3116-bc91-11737f0d91c8 | -1.60305 | -52.58714 | 2024-11-24 04:53:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 48afa12a-1d2d-3533-8ab7-bb1a85583607 | -2.77296 | -54.04392 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 83fb9512-533d-393e-983b-a42d819aa6b2 | -5.95379 | -48.05274 | 2024-11-24 04:53:00 | NOAA-21 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ab0c5b91-9e55-3bfb-9790-99a6daddd215 | -1.40389 | -54.47342 | 2024-11-24 04:53:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| dce86556-3fa8-3135-8e8d-94a404c9b1b7 | -2.04815 | -49.73421 | 2024-11-24 04:53:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ce310e73-1c87-3b97-be5b-164cff7d0768 | -3.10956 | -54.00093 | 2024-11-24 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 10769004-e8b3-38b4-991d-e1fcb30d669f | -3.03993 | -51.53197 | 2024-11-24 04:53:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8e6b22ac-1847-3e30-8a9f-338d1fa079a3 | -10.49825 | -51.75262 | 2024-11-24 04:53:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9054b5dd-d7b9-3720-b760-9b24b30483f5 | -2.82428 | -52.95654 | 2024-11-24 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 924a5d5f-3550-3256-8c20-4eaa6ffcc309 | -2.17095 | -50.90937 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7acd9f79-aa4c-39e6-b243-dff8edbddf6f | -3.75321 | -50.00592 | 2024-11-24 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5ed77c85-1bfe-3df5-8fab-4a8633a28f06 | -3.76095 | -49.93306 | 2024-11-24 04:53:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ec471d29-89a6-330c-a49d-0bc9777c8582 | -2.20899 | -48.90641 | 2024-11-24 04:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f8bef546-b023-3711-b50e-fbe5991cbc08 | -2.71128 | -46.27094 | 2024-11-24 04:53:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 89848d13-480a-3bf4-aeff-4b53abd6e1e6 | -3.25265 | -54.22865 | 2024-11-24 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| bd5d67e6-ddc6-349a-98ab-eb6c4dc0da3c | -3.54064 | -50.77547 | 2024-11-24 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| de4680a5-4c47-3349-b1d4-1fd3bd44caad | -0.25533 | -51.63512 | 2024-11-24 04:53:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.1 |
| fa376489-67ad-3662-b229-a60ed0189fa2 | -3.02322 | -54.0595 | 2024-11-24 04:53:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 460c0227-f83d-374c-9246-4e09730993a2 | -2.23918 | -46.4651 | 2024-11-24 04:53:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0c6df229-a405-3d32-a6d2-a63db7c33c3d | -2.78208 | -54.05294 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 73650fd3-3568-3704-9623-15e876386227 | -4.40834 | -49.66003 | 2024-11-24 04:53:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6216bd4f-fb8e-37ef-a102-c7f143bbbd23 | -2.31153 | -53.60502 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 73eb28be-ded4-334a-93e7-6addf3f6fcce | -3.29531 | -50.36031 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 2b83184e-7cb7-30d5-9d4a-90e5d9f31a2a | -1.14303 | -51.67887 | 2024-11-24 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0fd0baa1-a0aa-3b86-a254-46daa5125115 | -3.0471 | -54.3984 | 2024-11-24 04:53:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 77b83da8-154f-31ab-8a05-e8b331c2b44d | -1.34856 | -46.91597 | 2024-11-24 04:53:00 | NOAA-21 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6c7482f5-f378-3f35-aac4-ea4eb104f544 | -3.43084 | -49.9814 | 2024-11-24 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6946dbd2-5177-3410-8305-da704f008929 | -1.4282 | -52.39965 | 2024-11-24 04:53:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a0c7768b-d776-32d7-90f0-dd0ea1bb7e25 | -1.60885 | -54.4155 | 2024-11-24 04:53:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| c425b47a-29cf-30d4-8f0e-2b8aecef4520 | -3.23507 | -54.09639 | 2024-11-24 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a408dc41-5a9f-3814-9df7-ef82a397121b | -2.57649 | -51.88609 | 2024-11-24 04:53:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8770d308-aac9-3032-98b2-570ba537e1c9 | -3.29419 | -50.36763 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c6dbd89d-e74d-3847-ac7c-f07ba16d5d18 | -3.84259 | -46.63829 | 2024-11-24 04:53:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bc78c0b3-f14a-38a1-bb88-350b6b074619 | -1.12801 | -53.61006 | 2024-11-24 04:53:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bb928778-11cc-3155-94cc-c420947e791a | -1.60752 | -46.88091 | 2024-11-24 04:53:00 | NOAA-21 | SANTA LUZIA DO PARÁ | PARÁ | Brasil | 1506559 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| f8179786-ec5a-3744-a5d7-d82b7c8dbb59 | -2.1697 | -53.26588 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 372cfa90-a8f8-329d-ab99-c6ecd6c47263 | -1.06676 | -51.75131 | 2024-11-24 04:53:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1ba2abdf-1ad5-305e-bc35-59380d8c4973 | -1.78658 | -53.64344 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 28661863-6791-3f67-8469-a07bd9990375 | -2.0793 | -50.32138 | 2024-11-24 04:53:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1ec4de82-ad96-3a18-9293-95d33dc07307 | -1.49508 | -51.12134 | 2024-11-24 04:53:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0f0613a1-3c8e-32d6-be86-3e57af596733 | -2.75181 | -51.96246 | 2024-11-24 04:53:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 51be1ad7-312e-30da-bec4-4860c3d80db4 | -2.70157 | -46.27792 | 2024-11-24 04:53:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| b8ca5f23-ad52-3fe0-839a-6c662a402dcb | -3.09989 | -53.99567 | 2024-11-24 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9b2a3355-902d-3d0a-866c-10f0eb52f469 | -3.27551 | -48.75877 | 2024-11-24 04:53:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 63145598-4514-361f-b909-7236aed23d16 | -2.12506 | -51.24774 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 846f10ca-c130-3ab0-ae36-b79d63e73753 | -2.95047 | -51.42959 | 2024-11-24 04:53:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5efcb488-fc04-3071-b004-23f2c69fffde | -0.92387 | -51.64492 | 2024-11-24 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fde8b05b-734b-3801-92c8-fdc5b6aa34b1 | -3.79772 | -51.97485 | 2024-11-24 04:53:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f4ebb05d-3ad1-32ca-b561-29fde7526766 | -3.2479 | -50.11929 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8a5f4d43-4c64-3082-bb16-200a4076dfe8 | -2.20597 | -53.67394 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9fb3b640-fd21-3cd2-9f10-6cd3d12d7767 | -2.11779 | -50.57299 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d5226cdf-6328-372c-8fa3-83420c4122f2 | -11.51 | -48.12846 | 2024-11-24 04:53:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d556e391-82dc-3a02-940d-cc8904fce3a4 | -3.84395 | -44.05048 | 2024-11-24 04:53:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 9b3920ab-4670-35af-a96b-78d3d748886e | -3.27954 | -53.83982 | 2024-11-24 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 679fd9f1-8ba8-37dd-9027-db857ba56588 | -5.54858 | -45.32835 | 2024-11-24 04:53:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README46.md)
