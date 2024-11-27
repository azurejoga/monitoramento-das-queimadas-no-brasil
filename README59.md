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

## Dados Diários - Página 59

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 398c8d8f-78b0-371f-bc79-c50731a8b6a3 | -1.9325 | -48.65412 | 2024-11-27 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bd77785e-aa4f-3839-adf4-0f8db02d3b04 | -2.89334 | -51.38526 | 2024-11-27 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| abdc39dc-70a8-33e4-b4a0-d771b4cee939 | -3.9372 | -48.15461 | 2024-11-27 04:42:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1dbde5e6-8b8d-3898-bd8b-bfe49a3d95eb | -4.31186 | -48.08025 | 2024-11-27 04:42:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| bb9954b2-9644-3046-8624-29bbba6e492b | -3.508 | -50.30814 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b3df9083-e4b8-38ef-b3ab-33176d6da962 | -3.50018 | -50.46534 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 80b34066-c2f0-3be9-b6d3-93a6731dc1c5 | -2.27242 | -47.90782 | 2024-11-27 04:42:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3b4992be-43a8-37d4-8777-10c50da92f6e | -4.47671 | -48.10895 | 2024-11-27 04:42:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 35fc103d-5387-320d-b99f-54e81b39c107 | -1.31017 | -51.73552 | 2024-11-27 04:42:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 40a0b97b-f1bc-3494-be93-aaca2330dad8 | -2.98128 | -53.89453 | 2024-11-27 04:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| f4d60627-3097-3adc-acc0-670a2ed2bf7d | -4.05307 | -48.32943 | 2024-11-27 04:42:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 469105cd-fbaf-3867-a017-bf072a55b099 | -1.75929 | -53.62796 | 2024-11-27 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 87c645e0-ba03-3b5f-ab80-8c7fe15ccc14 | -3.24177 | -50.1429 | 2024-11-27 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| cbfd1502-7d6d-34bf-9d31-830e7c8b7eba | -4.09487 | -51.11008 | 2024-11-27 04:42:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a0c3ee2a-88b4-3612-9e44-3a2a4af63fef | -3.08187 | -47.81726 | 2024-11-27 04:42:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2fd6d606-b8f0-35f3-8a45-ba4be9a6e39f | -4.05245 | -46.6949 | 2024-11-27 04:42:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2e1f54a9-f274-31a8-b2fd-0bd8f14edd04 | -2.70097 | -51.9869 | 2024-11-27 04:42:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ddcad0d1-2adb-368f-b60e-5fdbd644ec68 | -2.02276 | -52.41549 | 2024-11-27 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2efffc2e-c099-3c85-be8c-5c118a2cc5d5 | -3.04448 | -48.51099 | 2024-11-27 04:42:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 22.0 |
| a7310993-5e40-3d07-bd0d-6ce3f276a4db | -4.04104 | -48.31591 | 2024-11-27 04:42:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| afd26a11-f651-3342-a881-d0a29bf599f2 | -3.84413 | -51.38565 | 2024-11-27 04:42:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 85266d47-5b92-3f01-86b0-4885c63cc740 | -2.72388 | -48.63271 | 2024-11-27 04:42:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e8cdda2c-1d6a-3a6e-88cb-2aabfcc59235 | -3.97086 | -48.08872 | 2024-11-27 04:42:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1db43739-d39f-35cd-ae04-d8ff8139ad89 | -2.96041 | -51.06377 | 2024-11-27 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1fdea7ae-9783-3432-9767-8f2c861db5a3 | -2.80478 | -52.91755 | 2024-11-27 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 716d8435-51f0-3c2f-b94f-529b36792e9c | -3.17828 | -50.22061 | 2024-11-27 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 167194a4-a82d-31c9-9a4d-64e7b00aa014 | -1.58463 | -52.23532 | 2024-11-27 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 550e0030-2d50-3578-b12b-d20753cd3cd9 | -3.19631 | -48.58986 | 2024-11-27 04:42:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f62bcead-1288-37a8-b644-a43568093f04 | -3.89971 | -47.7463 | 2024-11-27 04:42:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c3f9b913-d568-37bb-8318-35fe0c9b3362 | -3.97834 | -49.97263 | 2024-11-27 04:42:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dfa68e78-2a8d-3f41-b45d-ce941a105ff6 | -4.54194 | -46.61079 | 2024-11-27 04:42:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1bc8ef3b-db0d-329c-846a-766c1810ce02 | -2.53208 | -47.32611 | 2024-11-27 04:42:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 7fa35016-27d4-31a1-a5be-8cbd67791f5a | -3.31116 | -50.24181 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 40a85877-546a-335b-ae2a-3eb5813ceb4d | -2.15171 | -50.61345 | 2024-11-27 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 56bb87db-9b8b-34fb-92f9-979d1857a590 | -3.04679 | -53.72156 | 2024-11-27 04:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| fb5681eb-e27a-350d-bc44-b7840b4029aa | -2.78003 | -52.86855 | 2024-11-27 04:42:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 63e22142-c12e-346f-b00c-a0057a586563 | -2.94408 | -51.53434 | 2024-11-27 04:42:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 92adcb14-b175-32f0-8c41-b7c25cf4359a | -5.58775 | -43.15393 | 2024-11-27 04:42:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 95e9b275-bbd8-338c-ba34-3ce360928cab | -4.26764 | -42.43661 | 2024-11-27 04:42:00 | NOAA-20 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| b86d9b9a-6fb1-34ca-b200-e2fe4a79f098 | -1.65726 | -52.41536 | 2024-11-27 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8a9a4be8-8a3d-3a32-8c06-11eee6f15e1e | -5.98002 | -45.36306 | 2024-11-27 04:42:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4bc32c57-08a4-31e1-9467-f930ed634ec2 | -4.49604 | -46.60598 | 2024-11-27 04:42:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ab605769-a4cf-3b1b-a466-36a74a18e292 | 0.94838 | -50.73534 | 2024-11-27 04:42:00 | NOAA-20 | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 16ee388a-9b78-30c2-8609-929a8c4795bf | -5.8978 | -43.41054 | 2024-11-27 04:42:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 88451981-d5c5-3a23-b4ca-b86c6c1071cc | -2.54278 | -53.99284 | 2024-11-27 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 99afdbaf-8cdd-3351-b456-232ed2420c7f | -1.123 | -48.33697 | 2024-11-27 04:42:00 | NOAA-20 | BELÉM | PARÁ | Brasil | 1501402 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 91eee463-322a-34c1-b8b1-ae12048efb00 | -3.59787 | -50.36086 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 4a8936f9-f3e1-3934-aab8-b8dd49aeb6ac | -4.94725 | -45.88202 | 2024-11-27 04:42:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 939f4205-cbfc-3197-8cee-e3f934c2ab10 | -3.15157 | -50.58666 | 2024-11-27 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 432ef1e3-0ae4-3cb5-a65a-fd3849af02b6 | -1.50352 | -52.03993 | 2024-11-27 04:42:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2b26eab9-32a1-3e60-9c62-3ecbe341d4a9 | -4.41306 | -49.36136 | 2024-11-27 04:42:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ca1bc489-d1e9-3a91-9e35-7b3d1de91c4c | -3.10159 | -53.25946 | 2024-11-27 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 345d426c-f92a-3bee-a418-2cafbea6a0df | -3.35999 | -50.18958 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ae8fe868-3a25-3c76-b056-1349c5bc2418 | -3.53083 | -50.3997 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f6cd0546-8c5d-3a6e-9eff-c9427a1ef95c | -3.46848 | -50.25613 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 15b24b5a-3740-3805-9d75-6e024daa0d0b | -3.28264 | -41.7739 | 2024-11-27 04:42:00 | NOAA-20 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| a02365ac-89c7-36a1-b2f1-9ef0d4a17fec | -3.98303 | -48.07883 | 2024-11-27 04:42:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2ea0668e-5ce0-3a0d-b230-28532c3a774b | -3.58963 | -51.53336 | 2024-11-27 04:42:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 709f699a-c660-33c6-b3b1-cb92894bf89a | -1.66014 | -52.4198 | 2024-11-27 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 21e14bb3-a3bd-3ba9-9bd2-03fc85ad8a88 | -4.01451 | -46.98764 | 2024-11-27 04:42:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2495771f-f65c-3b9a-9ce7-0cb90e2603d9 | -5.52303 | -47.58611 | 2024-11-27 04:42:00 | NOAA-20 | SÃO MIGUEL DO TOCANTINS | TOCANTINS | Brasil | 1720200 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 60ec3521-cbaf-3fda-8000-a4eeeb575edc | -1.2033 | -51.74607 | 2024-11-27 04:42:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7c85bd7d-b247-3f46-8891-24acbb7b765d | -3.28064 | -50.56457 | 2024-11-27 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ce452330-00ab-3931-b3ed-ca47b8baa7b4 | -3.9385 | -47.98643 | 2024-11-27 04:42:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5091d4c9-3931-3d0c-8ab4-bda115b7b07d | -2.26406 | -51.23981 | 2024-11-27 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| afa6a8dd-0cdd-3965-9343-a5f337e06738 | -1.71168 | -52.47984 | 2024-11-27 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| adbf44ac-69ed-3718-98eb-8de4ecae282b | -3.17881 | -48.43407 | 2024-11-27 04:42:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 40c071f1-020f-36f6-a177-7ab6c49c696d | -3.8439 | -49.89832 | 2024-11-27 04:42:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8235db7a-fe1d-3b42-9150-b445e69a694a | -3.72391 | -50.18663 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 57ed3ea6-ec32-3949-ae2e-d7120119bdef | -3.96098 | -46.89626 | 2024-11-27 04:42:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b3d125a2-de81-37ee-b647-706975d7ddae | -1.26931 | -52.2346 | 2024-11-27 04:42:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7149c57e-b4e4-3ea0-8da3-54b5cd694d94 | -2.88118 | -51.58304 | 2024-11-27 04:42:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 54c62c8c-d45d-37f4-8a02-a25f597b0e5e | -3.246 | -53.28928 | 2024-11-27 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 33ed707a-7ce9-38e1-88d2-3855feea969f | -1.87885 | -48.54359 | 2024-11-27 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 912b0062-a51b-3847-b98a-669d1db040f1 | -4.47642 | -46.6585 | 2024-11-27 04:42:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 55671433-4c58-3c46-8662-094e66a61a0f | -2.8895 | -45.25589 | 2024-11-27 04:42:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cb0a80d5-df4f-360d-8cc1-b3961b508099 | -3.1105 | -51.25614 | 2024-11-27 04:42:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c8aa1c13-d676-3f5e-a43b-5d6dcd08175e | -3.34581 | -50.75519 | 2024-11-27 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e393a0a9-11c0-384f-93b4-644c50ac080e | -3.74139 | -51.8387 | 2024-11-27 04:42:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a927a772-119e-3c00-91c6-abd1b74ecd56 | -3.78291 | -50.13598 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| da5a2101-9804-38a6-859f-028f66b07d74 | -5.98834 | -45.36427 | 2024-11-27 04:42:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 8ab24255-fbcb-3b90-bfd2-9823c8d1f9ee | -0.0283 | -49.64291 | 2024-11-27 04:42:00 | NOAA-20 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0e755bbf-af78-32fa-9865-4ad5616cd298 | -3.55117 | -50.20572 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9f3ef754-c6eb-3cd4-9a3b-496650dab1c2 | -3.13161 | -50.25909 | 2024-11-27 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5da3da2d-44e4-3afa-aa1d-19e2ed522c69 | -2.60037 | -53.96944 | 2024-11-27 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| a360688d-5ecc-3541-8a65-b1fcd360faf4 | -3.08681 | -54.12985 | 2024-11-27 04:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 942cc434-cd55-32d2-a2aa-1a478e05c4f0 | -3.84802 | -51.38266 | 2024-11-27 04:42:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| df58aeb5-8195-3837-82e7-01cc4a675d49 | -1.0587 | -52.41915 | 2024-11-27 04:42:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1874ea72-1ed3-3fd3-9ba9-e220f661d0e4 | -3.49687 | -50.46483 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f2a870c8-2df8-30d2-b07d-f47c7b2e0602 | -3.593 | -50.39179 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 92a2c56f-cbee-3f74-b7c0-b02bd07a4e2f | -5.90255 | -43.41122 | 2024-11-27 04:42:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e264ee30-225b-311d-9855-c8ad710afcc7 | -4.27542 | -48.614 | 2024-11-27 04:42:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| b1ed8938-580c-340d-9091-6c3ab1d36e67 | -3.78622 | -50.1365 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d2ebf1e0-2c92-36af-b291-aa9c757fb262 | -1.63271 | -52.72699 | 2024-11-27 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 13541641-aae9-339e-8ad8-4587ca945178 | -4.01442 | -46.98592 | 2024-11-27 04:42:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9e2a3a40-2ffe-361f-9ce2-162c1a1f3d37 | -2.79527 | -53.02248 | 2024-11-27 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 13914987-ae67-3b15-9de6-ab8bd3109767 | -2.18685 | -52.13267 | 2024-11-27 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 32965f1c-fed0-31fa-8077-517a25863bcf | -3.93997 | -46.72022 | 2024-11-27 04:42:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fced43d6-f555-3b19-ab07-be421b028910 | -4.26859 | -42.43652 | 2024-11-27 04:42:00 | NOAA-20 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 6db942e9-1487-318c-9b9f-20a6d449d89d | -3.52939 | -52.15566 | 2024-11-27 04:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |


[Clique aqui para ver as próximas entradas](README60.md)
