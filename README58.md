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

## Dados Diários - Página 58

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4fa3786b-eafd-3e8a-9b1f-97acd08c023f | -3.72442 | -49.80407 | 2024-11-30 04:40:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c8a7efd8-ace2-3774-984a-9ad2d44c79d3 | -3.95264 | -49.95414 | 2024-11-30 04:40:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e26e6a2f-88be-30ac-8ad8-03c4bb99865f | -4.01661 | -46.99535 | 2024-11-30 04:40:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 3a5e325f-59f2-3557-a259-b4335b4e7faf | -2.64191 | -46.24517 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b949bd61-25cb-3113-9167-b512914a4d41 | -3.2165 | -54.17295 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| d6c9651a-2f34-3871-8927-1db5ba59264a | -1.69349 | -52.46709 | 2024-11-30 04:40:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 82c408ab-537c-3385-84a8-75e3599e7a0e | -2.21118 | -48.38551 | 2024-11-30 04:40:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| a9753f12-ab99-37ce-847d-0d3c544be27c | -4.95177 | -50.86552 | 2024-11-30 04:40:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bd65259e-ef29-3a31-9145-bec06cc13fa1 | -3.20219 | -46.56433 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0eab3c35-f4d1-35f3-947a-767ffdb76dc2 | -3.28895 | -50.52056 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ee12f423-34cd-3da4-a397-b903d15f3054 | -3.01405 | -49.53987 | 2024-11-30 04:40:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d1e2df80-a6d6-3748-ab0e-c6030e528456 | -2.80692 | -48.62299 | 2024-11-30 04:40:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6cfc7840-59d2-38dc-8448-f784bf4b82e7 | -3.83491 | -46.54888 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e1db323c-5301-3e12-890f-31a87a558f8e | -3.25293 | -53.62624 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 23.9 |
| 9e4c2e30-cbea-3f24-809f-db82b1208be8 | -2.64599 | -46.125 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 5.3 |
| b74dfc3d-c436-3cff-8920-52e421e3eff1 | -3.10622 | -50.3638 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 5457b077-deef-3c02-9bc4-8c826d485593 | -0.82511 | -51.85995 | 2024-11-30 04:40:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 7.3 |
| d0223946-d40e-36ea-bbc7-1b6fb614ab74 | -5.40893 | -45.98025 | 2024-11-30 04:40:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| eeafe662-136f-3dab-b6e0-80ea01b7dcea | -3.25589 | -48.88718 | 2024-11-30 04:40:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9766ba59-8869-33b1-9c0b-4d652bc8d1fe | -3.09556 | -50.34383 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 95b245b2-5b83-3450-b213-f846561e72c6 | -4.02064 | -46.99212 | 2024-11-30 04:40:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 995e9e4f-b6bf-30cb-8301-4c3b8a8fda6f | -2.57738 | -46.19173 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7ce3047d-c5b4-391e-87f6-a5f091963385 | -5.05886 | -46.3983 | 2024-11-30 04:40:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| caa8418c-7a39-315b-be4c-810aa8a200ca | -2.9908 | -53.35736 | 2024-11-30 04:40:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4cd970f1-c730-3f3e-aef3-990750693136 | -3.19116 | -46.5666 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9a12df27-2f89-3df1-bd75-7dcff9213b08 | -3.94844 | -46.72881 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9048bbf8-f5d8-3881-856a-2157572bc516 | -4.06945 | -46.695 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f7920007-8108-3623-88b3-5ee13f4c2b7a | -6.91014 | -43.55178 | 2024-11-30 04:40:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 50.6 |
| b5e9bcac-750d-3961-9b7d-a4e5b57b8fdf | -2.91684 | -48.59476 | 2024-11-30 04:40:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 94ad3c20-c5a9-3110-a219-c244d7bc8bba | -3.20176 | -50.27264 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 85b4fbf9-6c2d-363d-90ae-8ceb8f840668 | -5.12671 | -45.15674 | 2024-11-30 04:40:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3aa61e77-10ce-3590-aa76-9f0474f16298 | -3.38511 | -50.33793 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cb3755ec-41cf-3ec4-ac71-0a52fd0f786a | -3.99167 | -48.94239 | 2024-11-30 04:40:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 2fe1057c-caf4-3948-848b-364a1f1ec118 | -1.43908 | -55.25203 | 2024-11-30 04:40:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 92edda28-1ae6-3e77-9449-41f542b9fc23 | -2.48388 | -48.83955 | 2024-11-30 04:40:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 67920b10-bdf2-35ab-9571-aef5bff7f2fa | -3.74303 | -54.67535 | 2024-11-30 04:40:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d83c2f31-3e9a-324c-88be-8d6569f12b56 | -1.82911 | -46.30329 | 2024-11-30 04:40:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 051b8bbe-876b-33b5-9ed9-1afab58b1090 | -3.41036 | -49.81161 | 2024-11-30 04:40:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0a4a794b-5405-3eee-ad1a-ed13a2dd6391 | -3.31818 | -46.65583 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6cb282f5-c176-3e3a-ac36-1bef221f88e3 | -4.69137 | -42.3721 | 2024-11-30 04:40:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| c68139f3-6f6d-3a77-9696-222be4af16a5 | -5.07731 | -44.98691 | 2024-11-30 04:40:00 | NOAA-21 | SÃO ROBERTO | MARANHÃO | Brasil | 2111672 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 5eefdb90-a12e-301b-867c-43c64a1e93fd | -6.53807 | -55.05582 | 2024-11-30 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e1870836-e8d1-3bb4-a2a3-d31ade787b32 | -1.80282 | -50.90879 | 2024-11-30 04:40:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0f06e42d-67e3-36a7-84e7-7adf1181ddb2 | -2.60751 | -46.58269 | 2024-11-30 04:40:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 05921d8b-6e97-330f-86ba-93505d7e332c | -1.34098 | -54.9875 | 2024-11-30 04:40:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 010d6228-ca8f-3f9c-81b0-79faf5addbb1 | -4.11439 | -49.07423 | 2024-11-30 04:40:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| af003ca4-7dfc-3894-b5ca-7f2cb25e029d | -3.57858 | -52.29709 | 2024-11-30 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f1eb69df-e6e4-3dcb-b3d8-69dcba9840e2 | -3.70222 | -45.68254 | 2024-11-30 04:40:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8e9f5f6e-9769-3d6e-98d8-a84d1df2fdc8 | -3.06982 | -53.91569 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 98aec8e2-00fb-31e0-bf0c-64771ee573da | -2.46835 | -46.54992 | 2024-11-30 04:40:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bb969da9-8089-3b07-8d54-c0456b5614cd | -2.35864 | -46.87429 | 2024-11-30 04:40:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c79bf44a-36a6-3921-9e2f-e974eb98bec7 | -2.75351 | -48.61828 | 2024-11-30 04:40:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7985a0bb-75e5-3ccb-a0b7-6ca3ffc49225 | -2.80828 | -53.05182 | 2024-11-30 04:40:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| a96a3126-3c73-34a6-a7de-86a9fdf22a26 | -2.94718 | -49.44451 | 2024-11-30 04:40:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d2528941-1187-3453-b445-356b46561d74 | -1.21953 | -51.73581 | 2024-11-30 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fcd21219-2c95-366e-a61c-43afca7e62f4 | -3.02311 | -47.80033 | 2024-11-30 04:40:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1ebf6fc3-a898-303f-b03d-f64b93a806c7 | -2.81945 | -51.29377 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c7b1ada3-bf58-3623-ad89-48cdd02172fa | -5.04901 | -44.63561 | 2024-11-30 04:40:00 | NOAA-21 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 723c376d-9c74-37bd-b8fc-9988910a04f5 | -2.67115 | -46.55276 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9c6c74b6-a3b3-3d57-b1f5-0de3b9603d46 | -2.31642 | -50.65459 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c0dd1653-2ebe-31bc-bac1-6f6143886881 | -4.65435 | -46.37065 | 2024-11-30 04:40:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4da624d7-7a7c-3b21-b0d7-b41aa88a5c0c | -2.22736 | -46.38994 | 2024-11-30 04:40:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7b0ca3f7-d4ca-33e4-b5a1-00338ab8fc16 | -3.95512 | -46.91728 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 20264ebf-faf7-3b79-b564-ccca9bf223c6 | -3.35574 | -49.09615 | 2024-11-30 04:40:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d1a72493-1c54-37bf-b244-47c9debe7d0d | -3.08615 | -49.20846 | 2024-11-30 04:40:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 73b6040c-9a35-3592-8a3e-c668671829a1 | -3.32542 | -50.2226 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4a78c6d8-28d8-3aff-b364-431759e1f5e1 | -3.8749 | -46.6627 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 67d72ce0-fd47-3a6a-bf8c-176ff5fea6c4 | -1.15269 | -51.70539 | 2024-11-30 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 0728d6b0-3fbd-3f04-97a8-5e7a6caae798 | -5.07193 | -46.10468 | 2024-11-30 04:40:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f3799461-4acf-3a63-8903-b01dca2f8561 | -2.88928 | -50.42547 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e14181e8-c440-38fb-954c-547716b50971 | -6.07979 | -48.04042 | 2024-11-30 04:40:00 | NOAA-21 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bdb1d7a2-ee5d-326f-b988-8fd850fce24b | -2.25705 | -51.25204 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b258254c-916f-366d-b769-05873d6421ff | -2.51418 | -46.32165 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bd834713-a32a-3cd0-a22c-b127c8c6b706 | -3.76138 | -50.17545 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 798edd4d-5100-3e75-b621-4e5c79772138 | -1.60336 | -52.29922 | 2024-11-30 04:40:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fa564f8d-2824-33a6-a6d7-73b73a3f5c86 | -2.71756 | -46.13074 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c24fb785-1447-3acb-8a0f-b2591ca04f32 | -4.0756 | -43.23235 | 2024-11-30 04:40:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2cfbd4cc-953f-3f46-b251-8660c2aac031 | -2.87079 | -46.82946 | 2024-11-30 04:40:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a5e31ed1-bc10-3e6a-bc92-5ffda6c59cb9 | -2.2411 | -50.48483 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e8ae487b-516d-317e-aaae-2ab811d23d64 | -2.60125 | -47.03109 | 2024-11-30 04:40:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2639295c-d569-3f55-bf0a-305d917502a5 | -3.17364 | -46.29749 | 2024-11-30 04:40:00 | NOAA-21 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| edeeefd7-700d-3d35-9b17-733497063f11 | -2.57967 | -46.20013 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f1e42b60-2eee-3602-a8b9-4d5b2a0a8c86 | -1.60404 | -52.29481 | 2024-11-30 04:40:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ea5a98d3-b718-30ab-9c6a-82f78ea7d9aa | -3.0223 | -49.53051 | 2024-11-30 04:40:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 727d3a36-85f1-3f28-a219-6c54a9d2f272 | -3.27384 | -50.44092 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3dd281f3-5b7a-356e-be73-136664084ba9 | -2.82518 | -52.96873 | 2024-11-30 04:40:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 6e174bb1-08ba-3e4b-ae48-a3abcdb4a62f | -3.06256 | -53.68197 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 140267d9-3176-3d25-8227-c644f7602e17 | -6.8234 | -46.77471 | 2024-11-30 04:40:00 | NOAA-21 | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| afdd470e-68ab-3c88-b71d-bcb2e3572642 | -3.25329 | -50.615 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 31bf3453-fff2-311c-92a2-c5a6ed41db0d | -2.985 | -48.72504 | 2024-11-30 04:40:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 419cd680-0047-3f2a-9a70-3c72d80ee8f7 | -2.6102 | -54.20829 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e169626f-3c09-3ae5-a064-b9a1a3dc982e | -1.04751 | -51.7541 | 2024-11-30 04:40:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 5a215d55-9444-3edf-b845-40a5a5ac946f | -3.30166 | -51.06413 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7b600d01-1751-383e-99a2-083321a641b5 | -2.44185 | -46.51474 | 2024-11-30 04:40:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5e520320-7470-31a6-a04d-a21f810c8c84 | -1.48617 | -47.51659 | 2024-11-30 04:40:00 | NOAA-21 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ecafcbb8-33d8-301c-94b9-d65f18eb78f2 | -3.2543 | -53.86419 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6a335daf-3683-3d4c-a2f9-7886c3c0d241 | -3.81935 | -46.5957 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f345d6d0-d906-306c-b69b-712e925559d2 | -2.62609 | -54.21468 | 2024-11-30 04:40:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 266a8560-acbd-3bda-8789-bf25f2177fc9 | -3.76956 | -46.68694 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3cff7abd-823a-3440-a5e3-c29032cd6440 | -4.02005 | -46.99593 | 2024-11-30 04:40:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 4.4 |


[Clique aqui para ver as próximas entradas](README59.md)
