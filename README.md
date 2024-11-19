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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 76b475b5-8ee8-3ea1-8517-76ae38acee02 | -3.3452 | -50.4917 | 2024-11-19 00:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 46a86931-df61-334b-a225-2e5051e4bf47 | -4.8609 | -50.536 | 2024-11-19 00:00:00 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 64.7 |
| c7763d1f-0b0d-3c43-ab24-e1bc05a95da7 | -1.7003 | -52.1465 | 2024-11-19 00:00:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 75.1 |
| 8156e76d-e1a2-3bd0-9b91-cda8208c72f7 | -3.3677 | -54.0991 | 2024-11-19 00:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 57.1 |
| e35cd081-0d6e-3391-8978-9b480a9e5f0f | -4.0997 | -51.0493 | 2024-11-19 00:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 61.1 |
| b1d7fb7e-a254-37da-a962-018f3fdfe87c | -2.9788 | -45.3467 | 2024-11-19 00:00:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 260cce97-b762-322d-afa7-1ea4d62f0439 | -2.7659 | -52.6163 | 2024-11-19 00:00:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 104.5 |
| 9c6b68e8-07dd-3500-9d65-7e78382a90e8 | -5.979 | -45.3395 | 2024-11-19 00:00:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 93.1 |
| ac99481d-ee5b-3899-bbca-183c45c8b84e | -22.3365 | -52.0415 | 2024-11-19 00:00:00 | GOES-16 | MIRANTE DO PARANAPANEMA | SÃO PAULO | Brasil | 3530201 | 35 | 33 | nan | nan | nan | Mata Atlântica | 111.0 |
| 0f13d1cd-addf-30b4-a992-4c808d011daa | -2.6946 | -51.8802 | 2024-11-19 00:00:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 68.8 |
| 4593c188-2f14-378e-b98b-652aab51d52d | -3.0713 | -45.4332 | 2024-11-19 00:00:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 42.4 |
| 24cf7bc1-cfc1-3b76-a8fc-2859b290163d | -3.5126 | -50.2133 | 2024-11-19 00:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 69.1 |
| cdcf83f4-f45b-34b9-ba5d-be83f992466f | -1.9353 | -46.5138 | 2024-11-19 00:00:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 153254fd-e789-37fc-bfca-1d082cc4c6f8 | -2.5011 | -49.0375 | 2024-11-19 00:00:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 98.2 |
| 56e007b2-6a10-3778-8dcd-6853623c28d9 | -2.9789 | -45.3242 | 2024-11-19 00:00:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 66.0 |
| d3816b5a-07da-37ba-adbd-e96c3c6930e0 | -5.9975 | -45.3607 | 2024-11-19 00:00:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 94.7 |
| 9fc860dd-bf3a-390c-87e2-d1a73e462ffc | -22.3168 | -49.7526 | 2024-11-19 00:00:00 | GOES-16 | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 100.2 |
| 10353fa1-b065-35ea-9e1a-e5fe3d6ef5da | -2.9974 | -45.3235 | 2024-11-19 00:00:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 64.4 |
| 7a07d3dd-82c8-30dc-85e5-05829128bcf4 | -9.2543 | -45.0074 | 2024-11-19 00:00:00 | GOES-16 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 134.7 |
| bdbad34b-cff6-37b5-8c5e-9cb18334f359 | -5.9786 | -45.3847 | 2024-11-19 00:00:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 78.4 |
| c6950cf3-bc74-30ce-91e8-da07d4aaeb4c | -3.5437 | -51.5258 | 2024-11-19 00:00:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 73.0 |
| 7b5fb4b7-bb69-3204-8ffa-afa3254c3d40 | -2.766 | -52.5959 | 2024-11-19 00:00:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 191.7 |
| 6bb2c01d-3479-35e4-87cc-93b1fc4bef03 | -9.2546 | -44.9845 | 2024-11-19 00:00:00 | GOES-16 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 94.5 |
| f5dc633c-ff97-3c05-991e-3d9c2b27805c | -3.6063 | -54.2129 | 2024-11-19 00:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 14f748d1-061f-329f-8eed-fca16b029986 | -9.2733 | -45.0052 | 2024-11-19 00:00:00 | GOES-16 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 82.6 |
| 17ba2795-7c6c-396b-91c6-484163d4df70 | -6.0659 | -44.0316 | 2024-11-19 00:00:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 89.6 |
| dea45475-8dc7-34e0-8ec3-b49ef093c370 | -2.4827 | -49.038 | 2024-11-19 00:00:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 79.1 |
| 16d7274b-c70c-3eed-8144-ae4747730942 | -2.5012 | -49.0162 | 2024-11-19 00:00:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 96.3 |
| 56123c02-855f-364e-bea4-242b81169977 | -3.3267 | -50.4923 | 2024-11-19 00:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 72.8 |
| bbcb9419-2a36-3d6e-bd1d-b4c385770c2a | -2.7844 | -52.5954 | 2024-11-19 00:00:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 90.5 |
| 58b04792-bfaa-3ba5-abfb-10573e9fe7ee | -4.1182 | -51.0486 | 2024-11-19 00:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 61.5 |
| b2fca841-846c-3df7-a7a3-d27adda934e5 | -3.4847 | -48.2558 | 2024-11-19 00:00:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 83.3 |
| 53e88304-9fc3-3b2b-9488-d4f566efbbbc | -2.4827 | -49.0167 | 2024-11-19 00:00:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 87.5 |
| ac2a03d9-a6ea-3583-b553-bbb587dbdc5e | -3.6247 | -54.2124 | 2024-11-19 00:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 55.5 |
| e6643a3f-0a91-3bb6-8039-434d0d64b8da | -2.9973 | -45.346 | 2024-11-19 00:00:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 5b68e212-d97a-3bee-9cd2-3f5acd30390c | -3.5125 | -50.2343 | 2024-11-19 00:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 83.0 |
| 133115cc-de94-3394-9fef-1c57f1cd07a1 | -5.9788 | -45.3621 | 2024-11-19 00:00:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 240.4 |
| 1446d060-86b4-36f0-8ae2-0e3ecba9b986 | -5.97 | -45.35 | 2024-11-19 00:00:00 | MSG-03 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 55435491-ae10-376c-89ec-4cff3bf31013 | -3.5125 | -50.2343 | 2024-11-19 00:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 83.6 |
| 1e6df5c2-cfde-376d-87ea-403cce088211 | -6.0659 | -44.0316 | 2024-11-19 00:10:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 88.4 |
| b520407e-fd8b-3e26-8200-b27df7fab92d | -13.2452 | -56.7965 | 2024-11-19 00:10:00 | GOES-16 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 106.3 |
| ce582dd4-75a0-3d5b-bd59-fa21b09bd750 | -3.6247 | -54.2124 | 2024-11-19 00:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 50.9 |
| ef3b2b79-cd8b-3417-b446-fd8346ccba3e | -3.3677 | -54.0991 | 2024-11-19 00:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 56.9 |
| 29663a39-79ed-3935-83d1-f7aa091d262d | -9.2543 | -45.0074 | 2024-11-19 00:10:00 | GOES-16 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 120.4 |
| 5186e9af-f3db-3a9a-b0d6-9947b064f4a7 | -3.3452 | -50.4917 | 2024-11-19 00:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 56.1 |
| bdd311e2-40f8-3f31-8d4b-7d48555ad81e | -1.7003 | -52.1465 | 2024-11-19 00:10:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 67.9 |
| ffdcbd1f-6880-3e46-b5b3-c921d43dc532 | -2.766 | -52.5959 | 2024-11-19 00:10:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 172.2 |
| 23dd64a8-852c-3fff-92ac-177ad464800b | -9.2733 | -45.0052 | 2024-11-19 00:10:00 | GOES-16 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 78.3 |
| 93411da6-9836-344f-9848-fb39d29861e5 | -5.9786 | -45.3847 | 2024-11-19 00:10:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 70.8 |
| 58db00ac-9f49-383c-9e69-c814129ddb03 | -3.5126 | -50.2133 | 2024-11-19 00:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 20de1911-8c7d-38e6-b546-6e55ee8cde36 | -2.4827 | -49.0167 | 2024-11-19 00:10:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 69.7 |
| ac034e68-45a3-3b3c-beaa-1306fdc71a11 | -2.5011 | -49.0375 | 2024-11-19 00:10:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 89.1 |
| f8433060-7862-3b21-acec-c93819b8ac3c | -2.5012 | -49.0162 | 2024-11-19 00:10:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 100.5 |
| 532722dd-2512-3d61-9328-ceec35324447 | -3.6063 | -54.2129 | 2024-11-19 00:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 75f29ad7-0683-3e64-b205-f4e2df87defc | -2.7844 | -52.5954 | 2024-11-19 00:10:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 84.5 |
| 5a77868a-5551-3a7a-9a1c-c6f89ffd5bc9 | -13.264 | -56.8149 | 2024-11-19 00:10:00 | GOES-16 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 271.7 |
| 14822cd0-79e5-3f21-b8ce-e1319a0eec33 | -22.3365 | -52.0415 | 2024-11-19 00:10:00 | GOES-16 | MIRANTE DO PARANAPANEMA | SÃO PAULO | Brasil | 3530201 | 35 | 33 | nan | nan | nan | Mata Atlântica | 105.2 |
| 85b743bb-965d-3030-8cee-ce63f65f46e4 | -5.9788 | -45.3621 | 2024-11-19 00:10:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 213.6 |
| 3fd860cc-d999-3d81-8e68-7988cba8cfa0 | -2.7659 | -52.6163 | 2024-11-19 00:10:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 109.3 |
| 902a9bff-4187-3c3d-90ac-61b6242c62a0 | -4.8609 | -50.536 | 2024-11-19 00:10:00 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 56.1 |
| e42ab34e-59b2-3e71-a596-46f27ef96a85 | -3.4847 | -48.2558 | 2024-11-19 00:10:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 80.3 |
| 954eca62-5bcd-3ec4-8b8b-c76f851f165a | -3.3267 | -50.4923 | 2024-11-19 00:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 65.7 |
| faa51a3c-859e-3b63-b69c-fb0c99bb710c | -9.2546 | -44.9845 | 2024-11-19 00:10:00 | GOES-16 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 93.7 |
| 1b5dd92a-e950-3ea3-b1cf-835523e6f95d | -13.2643 | -56.7947 | 2024-11-19 00:10:00 | GOES-16 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 164.6 |
| fd269ba8-9131-3a96-a32b-92f6b752bdca | -2.4827 | -49.038 | 2024-11-19 00:10:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 68.7 |
| a1793ba6-b2a8-31c3-ae45-d1aba524e565 | -3.9946 | -49.9215 | 2024-11-19 00:10:00 | GOES-16 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 47.6 |
| b6c487fb-4f5b-3c32-8f6a-76a3ed0fccd8 | -4.1182 | -51.0486 | 2024-11-19 00:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 56.2 |
| cc0995e9-87ae-38e7-b358-ec09bf1e9f18 | -13.2834 | -56.7929 | 2024-11-19 00:10:00 | GOES-16 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 66.2 |
| 8ef836f3-3316-314a-8b1c-0e8d41fc252f | -5.979 | -45.3395 | 2024-11-19 00:10:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 100.5 |
| 8e3ef415-3fd6-372a-ad39-1a0371181d3c | -13.2831 | -56.8131 | 2024-11-19 00:10:00 | GOES-16 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 84.4 |
| 30fb42b5-1695-3031-a804-e3b8c4210d59 | -5.9975 | -45.3607 | 2024-11-19 00:10:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 89.7 |
| 27e7eef7-5f70-35c7-8e0f-c43f8a653153 | -2.9974 | -45.3235 | 2024-11-19 00:10:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 321b8599-c845-3ade-916a-6d212163ff71 | -1.9353 | -46.5138 | 2024-11-19 00:10:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 54.9 |
| c94de475-5d9c-335b-a830-76e5bf12ffb4 | -8.6876 | -47.976 | 2024-11-19 00:10:00 | GOES-16 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 60.8 |
| 769c9fee-02d6-3141-b3f4-ca8c9015630f | -3.5437 | -51.5258 | 2024-11-19 00:10:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 68.1 |
| 724c6660-c664-3f85-9a76-85384d883fe7 | -13.245 | -56.8167 | 2024-11-19 00:10:00 | GOES-16 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 177.3 |
| bd2ce935-0817-3f76-bd14-05a4eb875c6e | -3.3677 | -54.0991 | 2024-11-19 00:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 96b4036c-5454-3528-8173-88cb73700e5a | -5.9975 | -45.3607 | 2024-11-19 00:20:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 86.1 |
| 6e33a6c8-dd2e-3316-9743-62c805b9bd1f | -9.2543 | -45.0074 | 2024-11-19 00:20:00 | GOES-16 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 116.9 |
| 2b5a7a56-7ecb-3da1-8504-69389dd64de7 | -2.7659 | -52.6163 | 2024-11-19 00:20:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 102.3 |
| d4fc9f1f-5d81-30c2-9014-131e2baa8a97 | -3.5126 | -50.2133 | 2024-11-19 00:20:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 5878c1b2-2bba-3c6f-b9c2-0271ac732528 | -5.9786 | -45.3847 | 2024-11-19 00:20:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 72.4 |
| 6c257fd2-0cbb-3c75-98ea-fbeab2a28f6a | -3.5125 | -50.2343 | 2024-11-19 00:20:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 81.0 |
| cad088c9-e856-3032-bb4e-21261c29fb05 | -2.5011 | -49.0375 | 2024-11-19 00:20:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 86.8 |
| f4d9a110-1ff9-3a4b-9002-135b8353ff7d | -1.7003 | -52.1465 | 2024-11-19 00:20:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 65.0 |
| a8f8cacc-32ef-3da9-ba36-e18e4f324a31 | -5.9788 | -45.3621 | 2024-11-19 00:20:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 213.5 |
| 46aac5fc-3964-3d48-87f9-35ebb39c9827 | -4.0997 | -51.0493 | 2024-11-19 00:20:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 56.2 |
| d35eca8c-9be6-3700-97af-4bf3e5b178b5 | -9.2546 | -44.9845 | 2024-11-19 00:20:00 | GOES-16 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 82.4 |
| b62bd5eb-1e50-3213-a4d4-35e93c075ad7 | -2.5012 | -49.0162 | 2024-11-19 00:20:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 83.6 |
| a9deac0c-5ae7-3345-b3e4-f79152a13c94 | -3.6063 | -54.2129 | 2024-11-19 00:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 52.9 |
| 252f845d-d3e5-39bb-b9f3-9a26f77d5440 | -3.3267 | -50.4923 | 2024-11-19 00:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 47b2d91f-1ab4-3e75-a296-cf4b9e00f87e | -22.3365 | -52.0415 | 2024-11-19 00:20:00 | GOES-16 | MIRANTE DO PARANAPANEMA | SÃO PAULO | Brasil | 3530201 | 35 | 33 | nan | nan | nan | Mata Atlântica | 81.1 |
| 00dff4f8-c2c6-3b5f-b522-a9769c92a164 | -2.4827 | -49.0167 | 2024-11-19 00:20:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 64.3 |
| c8b40b54-6d0d-34ab-9f82-ec8a0c29882f | -2.9983 | -45.1433 | 2024-11-19 00:20:00 | GOES-16 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 58.0 |
| d77e5566-dcf9-31a1-a13c-c76574d06950 | -4.8609 | -50.536 | 2024-11-19 00:20:00 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 52.9 |
| 95785ed6-173e-3a36-980a-c1a641d3a416 | -6.0659 | -44.0316 | 2024-11-19 00:20:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 8a06b17f-01cc-3254-b543-e8ebf9903e3f | -5.979 | -45.3395 | 2024-11-19 00:20:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 82.1 |
| 133d25bc-2236-31f0-955c-c30f622cb0cb | -2.7844 | -52.5954 | 2024-11-19 00:20:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 82.8 |
| b3983c75-8509-3f7d-8f2f-053df6e13302 | -3.9946 | -49.9215 | 2024-11-19 00:20:00 | GOES-16 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 46.3 |
| 4817ba43-13c8-3a20-9748-4ae8625112f4 | -9.2733 | -45.0052 | 2024-11-19 00:20:00 | GOES-16 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 72.2 |


[Clique aqui para ver as próximas entradas](README2.md)
