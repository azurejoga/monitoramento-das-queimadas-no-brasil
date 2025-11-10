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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7ad2ab6e-2b99-39c6-97f6-ab59966b1ddc | -2.66431 | -54.76628 | 2025-11-10 05:08:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cc4fa666-e593-3809-a573-6c1c8bb52cde | -3.25755 | -50.07323 | 2025-11-10 05:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ba32cb84-d407-3fee-b457-4038284b648b | -2.63776 | -49.21781 | 2025-11-10 05:08:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c2e2b712-a9c0-3126-8fb2-25beeedf8059 | -3.10265 | -50.32302 | 2025-11-10 05:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 12cb58b0-b1a3-3edb-9cac-c628c662e58f | -3.40251 | -50.45689 | 2025-11-10 05:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 67403537-9aff-3ad3-90c7-92812cb0ec9c | -1.63373 | -53.68592 | 2025-11-10 05:08:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 53753cd3-ca5a-3e8a-8da6-f500cf4768e3 | -1.22724 | -52.64071 | 2025-11-10 05:08:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3f130b21-d61d-3b5a-b187-74268101e448 | -3.24141 | -52.79653 | 2025-11-10 05:08:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0e9f58df-0bba-3aff-bf01-9e30e4a97c7d | -3.22791 | -48.78693 | 2025-11-10 05:08:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| e65e3cc9-64bc-31c7-b5b9-8468a79a9e9e | -3.85439 | -50.18084 | 2025-11-10 05:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 023fe508-c521-3ec2-9845-a1a27ba16a84 | -2.7426 | -51.82765 | 2025-11-10 05:08:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6a4214ff-0c62-3e3d-99d5-18ad1f49b64b | -2.26947 | -47.84388 | 2025-11-10 05:08:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4842dd06-6edd-3872-9e3b-025ee6d01326 | -2.94851 | -53.28836 | 2025-11-10 05:08:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 014c8e56-fd7a-35e8-b434-74e94c9405c4 | -2.115 | -48.18328 | 2025-11-10 05:08:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3ee125e4-305a-3834-9f82-cf5efde0cace | -2.70832 | -47.39452 | 2025-11-10 05:08:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 089e8f86-594f-3259-9198-4f504ff7928f | -1.76402 | -55.02588 | 2025-11-10 05:08:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8df4c16b-ac01-3a0f-bd31-4db1c239ae56 | -3.28398 | -51.12229 | 2025-11-10 05:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cc68fcd0-549b-32ea-8e56-427aa4e89f70 | -2.19547 | -51.36565 | 2025-11-10 05:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 90458bc1-c5c8-39b5-bdb3-f45861589dd4 | -3.40377 | -50.44863 | 2025-11-10 05:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 47774598-d4ac-313d-b6b8-5884c9dcd3ce | -2.9746 | -49.82392 | 2025-11-10 05:08:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0cc1aa58-59e0-34ff-84f5-45ead9c321c0 | -2.96732 | -47.89911 | 2025-11-10 05:08:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 24b13e3a-22b6-3178-b6be-15e1ce4cbcf3 | -2.60297 | -49.22742 | 2025-11-10 05:08:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 8f53dfda-8dab-3973-96b9-356e3af9507d | -1.79704 | -54.85725 | 2025-11-10 05:08:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8557da81-717e-39b8-b983-8be537daee00 | -2.5694 | -50.63778 | 2025-11-10 05:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 778b6595-a72a-39be-a9cf-26bb011f4e60 | -3.69456 | -50.19352 | 2025-11-10 05:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 5a988577-e644-3ed1-bdc0-a7584dc0e60e | -3.12099 | -50.14454 | 2025-11-10 05:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 543403e6-fa8e-3829-9687-4b1e2fcdd1d6 | -3.46355 | -50.02584 | 2025-11-10 05:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 3f4ae9e5-9adb-3c27-8887-0f5d917e3829 | -2.97245 | -47.89989 | 2025-11-10 05:08:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 29eee019-656b-37a3-bcd6-58ca2f1c856b | -2.43982 | -49.3427 | 2025-11-10 05:08:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a8c3e9cb-8915-398b-95c5-661e7242fe86 | -3.1038 | -50.19848 | 2025-11-10 05:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fbed038f-4c29-3a0f-b5a4-d5ec0e5ad466 | -2.19774 | -48.24844 | 2025-11-10 05:08:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b673936f-a40c-368a-bcf0-b12583f042e3 | -3.1515 | -54.98849 | 2025-11-10 05:08:00 | NOAA-21 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6aa8dcb7-8692-39d1-af26-7504c1bdbda0 | -3.1429 | -50.27226 | 2025-11-10 05:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0cd3eb24-2339-30b8-ac22-be547c994c29 | -2.93581 | -51.05215 | 2025-11-10 05:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 805c5f1c-d0eb-3481-9f2f-6403ef494b83 | -3.34163 | -50.20716 | 2025-11-10 05:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| af2a2804-0775-3a92-90bc-4c2c08706a56 | -1.60778 | -55.06983 | 2025-11-10 05:08:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 62beb84d-54ae-3c4f-b2d5-114842b87798 | -2.97395 | -49.8284 | 2025-11-10 05:08:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4aa7d590-ab73-3a11-a66e-b5f5c7fc92a3 | -3.33436 | -49.92279 | 2025-11-10 05:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a356839e-3826-3745-87f2-61b57cb23394 | -3.30849 | -50.15643 | 2025-11-10 05:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 81549c79-dcca-3f9d-aadb-547267c4a910 | -2.64316 | -49.21371 | 2025-11-10 05:08:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 7ec932d1-eb20-3e67-a5a6-6704b4a9a67a | -1.76348 | -55.0294 | 2025-11-10 05:08:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3c39faf4-5948-3bf8-857c-ffa25dd56afe | -3.45021 | -50.47623 | 2025-11-10 05:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 4c0f1664-c256-304d-aa8e-e4f94d968969 | -2.99599 | -48.05698 | 2025-11-10 05:08:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6b137bfa-bcc0-3039-a11e-e2b150c30397 | -1.77016 | -55.03043 | 2025-11-10 05:08:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e5594635-34d7-31c2-91da-239d51c4caa3 | -3.10329 | -50.31885 | 2025-11-10 05:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8b5294e9-b2c9-3144-b3b4-9b8ecf48c407 | -3.30785 | -50.1607 | 2025-11-10 05:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5cdc3cd1-f7c4-333f-9f55-4a6c386fc72a | -2.04843 | -48.6498 | 2025-11-10 05:08:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d9ba8aaa-527a-3efe-a9e0-5785bfbb3dda | -3.47833 | -49.92836 | 2025-11-10 05:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| a5199d76-5b1e-3085-ad1a-5fb43ba308d2 | -2.99748 | -49.59759 | 2025-11-10 05:08:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f0b425eb-1a07-3f58-bd76-7803a9ce01a5 | -3.23096 | -54.61735 | 2025-11-10 05:08:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c8e626b8-17b9-38e4-bdd0-d4cc9d4fcaa5 | -2.18784 | -48.247 | 2025-11-10 05:08:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ae97e876-e628-33a4-bb2e-daa10c3119a7 | -3.33002 | -53.24807 | 2025-11-10 05:08:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5f631c86-9289-3f88-a8e6-f8794c0cb4b7 | -2.56881 | -50.64168 | 2025-11-10 05:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c80beacc-de90-33c9-bd96-6336ce5a4b8a | -3.03669 | -49.49486 | 2025-11-10 05:08:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 30b69129-f08e-3bea-b3ed-10db336fee67 | -2.44053 | -49.33797 | 2025-11-10 05:08:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e396934b-4567-3137-a1a8-b6cb7154147a | -2.94492 | -53.28779 | 2025-11-10 05:08:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 21e27e4d-4a55-3fb8-8c04-ed499bc60d68 | -3.25787 | -50.07572 | 2025-11-10 05:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 838c7563-9a37-3e94-a492-a3114d2c92f0 | -1.75082 | -54.20208 | 2025-11-10 05:08:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 040e535b-79a4-32e4-9cfb-2ca17e6213bf | -2.26901 | -47.84687 | 2025-11-10 05:08:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 434122a1-c84c-38df-9177-285dbc3211a0 | -2.99292 | -49.59691 | 2025-11-10 05:08:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 916fa554-8c33-3a93-9870-ec09669cba2d | -3.31226 | -50.16135 | 2025-11-10 05:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2ed5bce6-5e2f-31f8-8182-4f0dcf85649d | -1.23904 | -53.79255 | 2025-11-10 05:08:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b59f55f6-3ffd-362f-89dc-f88f34058b3d | -3.42389 | -52.9245 | 2025-11-10 05:08:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 531d52b3-7d79-32a3-b5d5-bd406dbd6651 | -3.41491 | -50.25775 | 2025-11-10 05:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 324a2a8e-c8bc-30a9-bbdc-95241ee23708 | -1.64676 | -52.02082 | 2025-11-10 05:08:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e2ba6a94-0427-36ea-b101-960ebe3edea0 | -3.69584 | -50.18482 | 2025-11-10 05:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 979a2fd1-a00e-3e74-be83-e184253c6e9a | 1.25896 | -51.27136 | 2025-11-10 05:08:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d3779279-6ee4-378b-8ee0-024118b6ea56 | -3.40745 | -50.45353 | 2025-11-10 05:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 817ee753-530a-34cf-acec-9e5558ca32a2 | -2.95211 | -53.28894 | 2025-11-10 05:08:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cb02a66f-b16d-380f-aa07-1cfe9e72a1a2 | -2.44513 | -49.33866 | 2025-11-10 05:08:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 5a01e182-518a-3236-ada6-c5890286daf0 | -3.08328 | -52.92235 | 2025-11-10 05:08:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 161ee629-f23c-37bb-9bd8-1b7ac3ac2778 | 1.26842 | -51.19023 | 2025-11-10 05:08:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b67493ef-d95a-39c9-af76-2300da015ed3 | -2.87026 | -54.10799 | 2025-11-10 05:08:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 90d63fc0-d1fe-3d21-9589-3acfba49df9f | -4.1943 | -50.6281 | 2025-11-10 05:10:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 5ea97d65-c4b7-31b3-8219-702135f61cd2 | -3.73193 | -52.65927 | 2025-11-10 05:10:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f4a4bfd0-6a39-32b3-9830-7a4959647ce0 | -4.91991 | -46.73188 | 2025-11-10 05:10:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bedb6d89-4e31-3b62-a3c0-ecc83ada9e6b | -4.20144 | -50.63379 | 2025-11-10 05:10:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 28d6b225-884f-35c4-95d7-f4a7fc1cd8c8 | -3.04913 | -58.73126 | 2025-11-10 05:10:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 01bc1354-2950-30e1-a860-4b330a097620 | -4.27021 | -59.65043 | 2025-11-10 05:10:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cb8162ea-8721-365f-aa6c-e9af6d051e29 | -4.27416 | -50.50417 | 2025-11-10 05:10:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9a05db0a-fc8d-383e-93ac-2479ec6bfb4e | -3.80396 | -51.09511 | 2025-11-10 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a6d2e5e1-5384-3703-8aec-3449063a1b10 | -5.12547 | -44.73273 | 2025-11-10 05:10:00 | NOAA-21 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| bf5a9c61-b8c3-3245-8bb3-d68ab3f2e7b4 | -7.89227 | -48.39555 | 2025-11-10 05:10:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 310c8baa-3a8c-32c9-9f3f-c4b1849556aa | -3.85709 | -51.4091 | 2025-11-10 05:10:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d59cf9a7-c941-3463-8ccf-89969262decf | -9.13352 | -50.08984 | 2025-11-10 05:10:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 09e26b4a-bb65-3d61-9e6a-ae85384dcc23 | -7.87396 | -48.41042 | 2025-11-10 05:10:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b4fea17c-bf0b-3f19-a439-c6ce1a31d3d9 | -7.88739 | -48.39153 | 2025-11-10 05:10:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| d6e15efc-135d-30b4-9bad-821405b30079 | -4.29061 | -60.96078 | 2025-11-10 05:10:00 | NOAA-21 | BERURI | AMAZONAS | Brasil | 1300631 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2c4950a8-3699-37c8-bffb-b979f642cb8b | -4.2998 | -60.95257 | 2025-11-10 05:10:00 | NOAA-21 | BERURI | AMAZONAS | Brasil | 1300631 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 613c6e32-22f0-3090-9b0a-7e77b18cf798 | -4.29138 | -60.95607 | 2025-11-10 05:10:00 | NOAA-21 | BERURI | AMAZONAS | Brasil | 1300631 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ea09326b-7b92-3939-b7b6-a9c577f6a9fc | -9.12868 | -50.08916 | 2025-11-10 05:10:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 7269e7d2-be34-398d-bc89-fe33c57152fd | -4.20266 | -50.62557 | 2025-11-10 05:10:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 6ceb63b3-0f3b-3d60-a9e9-883a62928143 | -3.70339 | -54.66944 | 2025-11-10 05:10:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 52fceea0-ee35-3162-bea3-e678d53dd56e | -2.94464 | -57.78048 | 2025-11-10 05:10:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 47169e1d-0b2b-39b2-b7f2-34554736bd17 | -7.89274 | -48.39217 | 2025-11-10 05:10:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ce2a1f4e-063a-3ee1-a2cc-a6dbaca24a28 | -7.9335 | -55.01213 | 2025-11-10 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 30aade4a-bb94-3903-8482-92dceb4a5d9c | -3.92167 | -59.12424 | 2025-11-10 05:10:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 406f16ca-8932-3571-b412-1659c8f626b0 | -4.58467 | -46.66953 | 2025-11-10 05:10:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 687f4e7f-5401-3e2b-acef-550d8e9d4d96 | -3.22931 | -58.89977 | 2025-11-10 05:10:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bc377165-4ddd-3129-b0bb-2829716b3e62 | -3.84169 | -52.10368 | 2025-11-10 05:10:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README17.md)
