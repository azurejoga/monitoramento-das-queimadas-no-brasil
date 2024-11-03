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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b70ae750-b72a-3f98-858f-550bc5296b3c | -2.86587 | -49.33753 | 2024-11-03 03:53:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e2abb37e-cbf0-3a75-ae84-57f86872eafd | -2.84637 | -49.5426 | 2024-11-03 03:53:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7b83a808-5766-3b29-89a4-ed64429dba8d | -2.84526 | -49.54127 | 2024-11-03 03:53:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f036b1a5-2a68-314c-bc92-0beb76738519 | -2.84258 | -49.48835 | 2024-11-03 03:53:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 265689d3-efd6-37f4-82f2-dda6a9bd80ec | -2.84169 | -49.49353 | 2024-11-03 03:53:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 835f0589-e206-3b13-ab8c-770ed9932d44 | -2.84027 | -49.49205 | 2024-11-03 03:53:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 3921d473-e692-313a-874b-033bba9a52ac | -2.8192 | -49.1539 | 2024-11-03 03:53:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 32.8 |
| 19aa0c69-b43c-3e15-99b9-9752aa15fed8 | -2.81836 | -49.15882 | 2024-11-03 03:53:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 29.4 |
| 678fbd23-8128-31d5-8913-205a1d87fe7d | -2.71487 | -49.32918 | 2024-11-03 03:53:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 97edfdd2-ce0d-3d8a-b70c-40e3940b81f1 | -2.71401 | -49.3343 | 2024-11-03 03:53:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| ca35fc51-6aed-3ea8-8166-ec7fad0022c6 | -2.70855 | -49.32809 | 2024-11-03 03:53:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 63c98221-76a0-3afe-9ebd-78a668083d79 | -2.70768 | -49.33319 | 2024-11-03 03:53:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 4e68d2f2-9436-3049-8871-ed7fcc3765ea | -2.70653 | -49.30149 | 2024-11-03 03:53:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0e941089-ee3b-3a9f-9ec8-164d63eadf10 | -3.33307 | -50.27195 | 2024-11-03 03:53:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| cf25385c-3ac1-3ac6-a850-a5e5a74734db | -3.33205 | -50.27767 | 2024-11-03 03:53:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 522a9d03-4ed6-3cfa-9589-42a5bf89b18f | -3.32928 | -50.27051 | 2024-11-03 03:53:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 09a1b03f-b27e-3ade-8cf2-cedc75501f6e | -3.3283 | -50.27625 | 2024-11-03 03:53:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| ae1aa76d-2756-3b7a-b7a9-8c6fe37fa51b | -3.32731 | -50.28208 | 2024-11-03 03:53:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 41a9417a-9ba9-3df3-8195-6387f1fdeb4c | -3.32642 | -50.27087 | 2024-11-03 03:53:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 9fca19e0-7696-35d3-b661-baf08d9c3d4f | -3.3254 | -50.27663 | 2024-11-03 03:53:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| dfef458a-9928-3ccf-9793-71f1dc1a25b7 | -3.32438 | -50.28241 | 2024-11-03 03:53:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 3e46b5f1-3de6-3ef0-b888-6bd60ef2032f | -3.32164 | -50.27527 | 2024-11-03 03:53:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| fbaeffb8-d2ba-3e20-b780-38e3fffe455d | -3.32065 | -50.28105 | 2024-11-03 03:53:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| c2f1baf0-24b5-3487-93a2-25c2ca87cda7 | -3.29648 | -50.03339 | 2024-11-03 03:53:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 35b8e2d9-3054-3010-8fb1-38766f3c6ec7 | -3.29602 | -50.03027 | 2024-11-03 03:53:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| dd6524e4-006b-3447-8aae-44dead738f52 | -3.29505 | -50.0358 | 2024-11-03 03:53:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 97ecfab6-baae-31de-a7e9-400f0ca43ea5 | -3.29087 | -50.02671 | 2024-11-03 03:53:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 72bd2141-a05d-3710-8b49-f94ed510533a | -3.29045 | -50.02357 | 2024-11-03 03:53:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| dfdaf717-8059-3efc-b2d9-a29a96b52c1a | -3.28993 | -50.03231 | 2024-11-03 03:53:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 70f53958-905f-36ee-ad6b-b2f8a782f3ed | -3.26881 | -50.34361 | 2024-11-03 03:53:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1836d5e1-77a1-338b-803c-46ff138f50d7 | -3.26779 | -50.3495 | 2024-11-03 03:53:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 160ead36-403f-3ab2-9af6-3767a1ecc102 | -3.26214 | -50.34247 | 2024-11-03 03:53:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4938f93c-1995-31ff-817c-65fda4553a0f | -3.207 | -50.28183 | 2024-11-03 03:53:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 2a177b12-68a5-334b-ba69-13efb21f73d5 | -3.206 | -50.28769 | 2024-11-03 03:53:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 86ac73f4-ed34-3fed-b477-f374165fd6c3 | -3.205 | -50.29354 | 2024-11-03 03:53:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 4453034c-e87c-354d-aae5-3cce21f239f1 | -3.19935 | -50.28652 | 2024-11-03 03:53:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1d7b5f7e-6c7e-3b27-875a-e5fab12347bb | -3.19835 | -50.29239 | 2024-11-03 03:53:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| cf7140dc-d474-3f1a-9e0d-da4d1ef616c9 | -3.17793 | -50.58655 | 2024-11-03 03:53:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 68368b90-9022-3b9f-b7ec-de0e79215ac1 | -3.17639 | -50.58395 | 2024-11-03 03:53:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 0b626dbb-34b3-3259-925e-dd97464bb01c | -3.17534 | -50.59011 | 2024-11-03 03:53:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 71b93efb-1af0-3c9b-88cd-39e6404cccff | -3.06332 | -50.50087 | 2024-11-03 03:53:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9a73fd8a-cd58-3d93-815e-6da7f662a0b2 | -3.06228 | -50.50698 | 2024-11-03 03:53:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 87de8e0a-5763-38b5-aaf7-4ff6b829404d | -3.05659 | -50.4996 | 2024-11-03 03:53:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| b57db637-d7e5-32c4-9331-4823ae028aab | -3.05554 | -50.50571 | 2024-11-03 03:53:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 288e1afa-5e67-317e-b928-dd996929f521 | -3.0545 | -50.51186 | 2024-11-03 03:53:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| a9e57dee-8cdb-358c-82b7-481d30f64905 | -2.72643 | -49.85442 | 2024-11-03 03:53:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 795bee47-7b65-3996-8a6a-f1d497ab376b | -2.7255 | -49.85986 | 2024-11-03 03:53:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 6208277b-8a60-3d29-b883-1ee3fdf9b257 | -2.60459 | -49.82446 | 2024-11-03 03:53:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a6438f81-fe15-3360-b0ec-2468e3500146 | -2.59809 | -49.82318 | 2024-11-03 03:53:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9410fbf7-6ae3-3099-90e6-272556934db1 | -4.40803 | -49.67591 | 2024-11-03 03:53:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 840b33f5-e7f2-39f9-a3b2-6b24c7940de6 | -4.39597 | -49.76502 | 2024-11-03 03:53:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 15e6702e-a2e7-395a-8163-2f0677e662d4 | -4.39258 | -49.76233 | 2024-11-03 03:53:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 96a4a6f2-732c-3031-b80c-2c94149a54be | -4.39167 | -49.7674 | 2024-11-03 03:53:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b6fed85b-b7e8-33e0-8749-c2c11b11b257 | -4.3896 | -49.76411 | 2024-11-03 03:53:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 011bb638-ec98-33ee-924a-a036f58fd16d | -4.35905 | -50.63982 | 2024-11-03 03:53:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3812bf0c-db9b-3551-8fe0-9b93c38976c1 | -4.35547 | -50.63972 | 2024-11-03 03:53:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3abb7137-69d0-3f48-85ff-9da2962e4829 | -4.35237 | -50.63865 | 2024-11-03 03:53:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6fbb196f-2fb7-37c5-bb62-7b0f871fde78 | -4.34876 | -50.63874 | 2024-11-03 03:53:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9b0b9795-d1f0-3140-8607-cd86ca956bf2 | -3.62241 | -50.18821 | 2024-11-03 03:53:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| fce2cdfd-cc79-39bd-b6ba-3dfeecbb6c1c | -3.61587 | -50.18689 | 2024-11-03 03:53:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 33697a76-9184-3c70-8e16-1c1661b0c54f | -6.77934 | -37.54182 | 2024-11-03 03:53:00 | NOAA-20 | MALTA | PARAÍBA | Brasil | 2508802 | 25 | 33 | nan | nan | nan | Caatinga | 0.8 |
| f94bc10f-cc03-357a-97ec-aacdf9a3a1ea | -6.77879 | -37.54536 | 2024-11-03 03:53:00 | NOAA-20 | MALTA | PARAÍBA | Brasil | 2508802 | 25 | 33 | nan | nan | nan | Caatinga | 0.8 |
| e8299f20-d41a-374f-96c8-07652444e074 | -6.77825 | -37.54884 | 2024-11-03 03:53:00 | NOAA-20 | MALTA | PARAÍBA | Brasil | 2508802 | 25 | 33 | nan | nan | nan | Caatinga | 0.7 |
| d7d850f5-1cd2-3194-9a94-4c103b73791f | -6.353 | -35.14472 | 2024-11-03 03:53:00 | NOAA-20 | CANGUARETAMA | RIO GRANDE DO NORTE | Brasil | 2402204 | 24 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| fd27cbf1-ee7d-33ac-a812-e76704a22e9f | -7.70314 | -34.90911 | 2024-11-03 03:53:00 | NOAA-20 | ITAPISSUMA | PERNAMBUCO | Brasil | 2607752 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 47b33cd2-0fa2-313f-b061-a0fb86e155ac | -6.80514 | -34.97576 | 2024-11-03 03:53:00 | NOAA-20 | RIO TINTO | PARAÍBA | Brasil | 2512903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 139a569d-12a7-3610-b3cf-06cf246b8b51 | -6.80448 | -34.98007 | 2024-11-03 03:53:00 | NOAA-20 | RIO TINTO | PARAÍBA | Brasil | 2512903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 09f4c285-7cb4-3360-bad4-68d2009af6f9 | -6.80383 | -34.98439 | 2024-11-03 03:53:00 | NOAA-20 | RIO TINTO | PARAÍBA | Brasil | 2512903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| da88f221-66ac-3a6e-820c-9280a8b22fcf | -6.80082 | -34.97953 | 2024-11-03 03:53:00 | NOAA-20 | RIO TINTO | PARAÍBA | Brasil | 2512903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 08fee0da-aa55-3b4b-8fe4-170a13f0ec2c | -6.80016 | -34.98384 | 2024-11-03 03:53:00 | NOAA-20 | RIO TINTO | PARAÍBA | Brasil | 2512903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 23d4a2f4-8d43-35b0-92ad-0e8070fbd6a1 | -10.30407 | -36.3048 | 2024-11-03 03:53:00 | NOAA-20 | FELIZ DESERTO | ALAGOAS | Brasil | 2702702 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 697f6842-45b8-31d7-b105-2670416f7190 | -10.30129 | -36.30531 | 2024-11-03 03:53:00 | NOAA-20 | FELIZ DESERTO | ALAGOAS | Brasil | 2702702 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 4b2bbc35-0ef3-347b-a199-8c12565bc699 | -10.18851 | -36.31076 | 2024-11-03 03:53:00 | NOAA-20 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 0b8fd3fa-5bfe-3a23-b523-b575b6d87737 | -5.16979 | -36.55178 | 2024-11-03 03:53:00 | NOAA-20 | MACAU | RIO GRANDE DO NORTE | Brasil | 2407203 | 24 | 33 | nan | nan | nan | Caatinga | 0.9 |
| affb3f0c-6975-3dba-9d94-c9ad085c107b | -12.83928 | -38.27282 | 2024-11-03 03:53:00 | NOAA-20 | CAMAÇARI | BAHIA | Brasil | 2905701 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| c0264256-9994-3639-bbbc-e898a477db51 | -5.07083 | -37.71625 | 2024-11-03 03:53:00 | NOAA-20 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 0.7 |
| be2e6fe0-d468-383a-90f5-c3ddc6b97429 | -5.68931 | -38.03962 | 2024-11-03 03:53:00 | NOAA-20 | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 47f52dd6-fa50-36eb-b1c6-83194654e9f5 | -5.68877 | -38.04307 | 2024-11-03 03:53:00 | NOAA-20 | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 6ebe894c-cc3d-315e-9936-d342d9554c59 | -5.68601 | -38.0391 | 2024-11-03 03:53:00 | NOAA-20 | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 5842eef9-d2d3-32f6-ac14-1615b5a8ed03 | -5.68548 | -38.04253 | 2024-11-03 03:53:00 | NOAA-20 | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 1.5 |
| dcb01c21-2e84-30cf-91f0-df26acf0de8f | -6.90145 | -38.56366 | 2024-11-03 03:53:00 | NOAA-20 | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 1a109a92-f6cc-302b-86ca-d87635de847c | -6.89815 | -38.56314 | 2024-11-03 03:53:00 | NOAA-20 | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 10.9 |
| 8c584bb7-1559-35b4-a174-3d8a2e2a8300 | -6.86526 | -38.36335 | 2024-11-03 03:53:00 | NOAA-20 | MARIZÓPOLIS | PARAÍBA | Brasil | 2509156 | 25 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 12375420-b4ce-30ac-b175-9556fcca8bd4 | -6.86196 | -38.36283 | 2024-11-03 03:53:00 | NOAA-20 | MARIZÓPOLIS | PARAÍBA | Brasil | 2509156 | 25 | 33 | nan | nan | nan | Caatinga | 1.2 |
| d2eba82e-08f2-34f2-b4b2-d82b77ca57cb | -6.85613 | -38.46453 | 2024-11-03 03:53:00 | NOAA-20 | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 3.3 |
| c797298d-aa80-3091-82b1-e843fcb5dec1 | -6.85559 | -38.46799 | 2024-11-03 03:53:00 | NOAA-20 | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 3.3 |
| c337de0b-3ec4-3462-86aa-4478ef0894aa | -6.85283 | -38.46401 | 2024-11-03 03:53:00 | NOAA-20 | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 1.3 |
| a21ba643-07d1-3326-a174-5f2885a05a0c | -6.77601 | -37.54132 | 2024-11-03 03:53:00 | NOAA-20 | SÃO JOSÉ DE ESPINHARAS | PARAÍBA | Brasil | 2514404 | 25 | 33 | nan | nan | nan | Caatinga | 0.8 |
| aa9fe698-082a-3016-bd9d-e9635b0e74f2 | -6.77323 | -37.53725 | 2024-11-03 03:53:00 | NOAA-20 | SÃO JOSÉ DE ESPINHARAS | PARAÍBA | Brasil | 2514404 | 25 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 139c0e40-b07c-3e3a-9280-c9094a502229 | -6.77268 | -37.54081 | 2024-11-03 03:53:00 | NOAA-20 | SÃO JOSÉ DE ESPINHARAS | PARAÍBA | Brasil | 2514404 | 25 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 9351d862-97e0-3e56-8c9f-83e88c541fa2 | -6.76991 | -37.53672 | 2024-11-03 03:53:00 | NOAA-20 | SÃO JOSÉ DE ESPINHARAS | PARAÍBA | Brasil | 2514404 | 25 | 33 | nan | nan | nan | Caatinga | 1.0 |
| ab83cde4-e3a6-3197-bc96-3bbdea71e012 | -6.76936 | -37.5403 | 2024-11-03 03:53:00 | NOAA-20 | SÃO JOSÉ DE ESPINHARAS | PARAÍBA | Brasil | 2514404 | 25 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 95e07827-5714-33de-ba05-360429f34586 | -6.76603 | -37.53979 | 2024-11-03 03:53:00 | NOAA-20 | SÃO JOSÉ DE ESPINHARAS | PARAÍBA | Brasil | 2514404 | 25 | 33 | nan | nan | nan | Caatinga | 1.1 |
| e85a1ce4-87a5-3155-90cb-29da5b368012 | -6.7009 | -37.47944 | 2024-11-03 03:53:00 | NOAA-20 | SERRA NEGRA DO NORTE | RIO GRANDE DO NORTE | Brasil | 2413409 | 24 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 164a7f58-89f7-38de-a3fd-0ed79aeb4d5f | -6.69811 | -37.47544 | 2024-11-03 03:53:00 | NOAA-20 | SERRA NEGRA DO NORTE | RIO GRANDE DO NORTE | Brasil | 2413409 | 24 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 59e15660-0a91-3405-920a-7c0ed0754138 | -6.69757 | -37.47896 | 2024-11-03 03:53:00 | NOAA-20 | SERRA NEGRA DO NORTE | RIO GRANDE DO NORTE | Brasil | 2413409 | 24 | 33 | nan | nan | nan | Caatinga | 0.8 |
| c776f539-ee9a-3c58-a716-8e8639bb2cd0 | -11.81656 | -39.14939 | 2024-11-03 03:53:00 | NOAA-20 | CANDEAL | BAHIA | Brasil | 2906402 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| d7cd7e16-9be2-323b-a2a0-0d4ff49ede9d | -11.23926 | -39.40986 | 2024-11-03 03:53:00 | NOAA-20 | SANTALUZ | BAHIA | Brasil | 2928000 | 29 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 12dd5fcb-8c2a-3525-9bad-8f1303ac361d | -11.23595 | -39.40933 | 2024-11-03 03:53:00 | NOAA-20 | SANTALUZ | BAHIA | Brasil | 2928000 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 24735413-f598-3386-9831-814573e36d23 | -13.38067 | -40.04871 | 2024-11-03 03:53:00 | NOAA-20 | JAGUAQUARA | BAHIA | Brasil | 2917607 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |


[Clique aqui para ver as próximas entradas](README27.md)
