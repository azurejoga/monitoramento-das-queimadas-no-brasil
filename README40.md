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

## Dados Diários - Página 40

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ef181c3f-bcf0-3c19-9fe8-c299210ac805 | -3.07388 | -50.36812 | 2024-10-17 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| d4302669-b302-3b27-a559-8383d5194293 | -3.07354 | -50.37147 | 2024-10-17 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| b2504210-2d90-3e20-934f-b3cd8f956ec3 | -3.07314 | -50.37313 | 2024-10-17 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| a42b3e43-4eab-3167-b0a7-caf1b0ca0ade | -3.07277 | -50.37646 | 2024-10-17 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| e334018b-0948-32a1-b092-ea0d45310d95 | -3.0724 | -50.37814 | 2024-10-17 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| a65c1586-107e-35fa-b22d-2c53c2e1931e | -3.07039 | -50.36584 | 2024-10-17 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 9a3e693f-a18b-3a48-9621-b9080cffb66a | -3.06962 | -50.37086 | 2024-10-17 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| f4a80113-9ec2-38f5-a14e-1c31f1c82dc3 | -3.06792 | -50.48927 | 2024-10-17 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 0a4797dc-4ec4-36e4-8e52-3f6023edf0c0 | -3.06753 | -50.48737 | 2024-10-17 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| c5d5fbc1-308f-38df-9b91-747d89ce0148 | -3.06718 | -50.49419 | 2024-10-17 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 366a59d8-0415-3360-83c8-85aad034d195 | -3.06676 | -50.49228 | 2024-10-17 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 242ab27e-00a2-3380-9c4f-d932c3aa3745 | -3.02955 | -50.52669 | 2024-10-17 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bdd62e6a-1bcf-3342-b492-9fdab9dc8f4b | -4.19488 | -49.39588 | 2024-10-17 05:04:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7dc7283b-cfb2-3cc6-b4ed-1f383ffd328c | -4.19427 | -49.39989 | 2024-10-17 05:04:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 33a2c51d-fe44-3e7d-8af0-b75d618d0f2c | -3.92277 | -49.36056 | 2024-10-17 05:04:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b62c36de-9b03-323d-bc19-1b68631805a7 | -4.95796 | -49.9357 | 2024-10-17 05:04:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7381a5bf-a63b-35e5-90f7-3bc0d28b7cda | -4.95381 | -49.93509 | 2024-10-17 05:04:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8f27f19c-c9d1-3d81-8b5c-5ced48d27841 | -4.60013 | -49.52108 | 2024-10-17 05:04:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a7c69a71-0c30-3f40-98e0-37e27593889f | -4.4883 | -50.1505 | 2024-10-17 05:04:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7b22634b-ab42-393c-8a01-90bef1fece8b | -4.15327 | -50.21733 | 2024-10-17 05:04:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f98075c3-ec16-3ab3-9de6-be342c4c0136 | -4.14924 | -50.21672 | 2024-10-17 05:04:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9b1b0809-e662-318c-80bf-763f072dda5b | -4.10012 | -50.75735 | 2024-10-17 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 68d11fc0-0538-398c-ad07-76a36434be1e | -4.0994 | -50.76227 | 2024-10-17 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 131d7277-a0a8-3f2c-9678-c51c35db8a5f | -4.09876 | -50.76035 | 2024-10-17 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 9ef3da1f-e048-30d5-91eb-be0e935287e1 | -4.09802 | -50.76522 | 2024-10-17 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fbdc8413-842c-38bb-9d20-1917b3486ea6 | -4.09714 | -50.15064 | 2024-10-17 05:04:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 6db65730-f911-39d4-9d0f-5a273363f58b | -4.09488 | -50.75975 | 2024-10-17 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| dc5f99df-a77b-3bb3-9154-02eb31159f01 | -4.03727 | -50.37462 | 2024-10-17 05:04:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e37eded6-7e7e-3b34-a82c-2cf79aa9e0af | -4.03674 | -50.37805 | 2024-10-17 05:04:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 36d6bb21-ea0b-3e3c-b441-ceba0d161e37 | -3.98969 | -50.71174 | 2024-10-17 05:04:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d456fe61-6d8c-33f3-9e51-f5ef01f10679 | -3.9819 | -50.71053 | 2024-10-17 05:04:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 94bebe1a-4923-3100-96ff-5be65dd7aedc | -3.89371 | -50.0037 | 2024-10-17 05:04:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b7725a27-c6c9-3658-8314-f4de888a0956 | -3.89315 | -50.00731 | 2024-10-17 05:04:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 48675c74-4768-3f40-a873-0d714b35ca06 | -3.88964 | -50.00309 | 2024-10-17 05:04:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7d91d8f9-8580-335e-8dde-4ebeab43ef4b | -3.88908 | -50.00671 | 2024-10-17 05:04:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 73be63ae-629d-3879-a4b5-cd6c09c6875b | -3.86797 | -49.98122 | 2024-10-17 05:04:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 633c24cd-75b2-3954-b7a6-2c14922b9158 | -3.86389 | -49.98063 | 2024-10-17 05:04:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 57f294f9-52f9-3ed9-ab93-795e44f18281 | -3.6527 | -50.19926 | 2024-10-17 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b1a013d2-d3a4-3322-b05e-251ba20bffcb | -3.65142 | -50.19522 | 2024-10-17 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 7ba58c75-d3d1-3c27-9247-3e64c3eb51cd | -3.65088 | -50.19873 | 2024-10-17 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| eb617926-e5ef-38cb-96fd-418b8d356bb8 | -3.64921 | -50.19511 | 2024-10-17 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 72a6a628-39fd-3c1f-8c58-761a35512d6e | -3.6487 | -50.19864 | 2024-10-17 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 4c42c31d-fbd5-3489-92d6-3320895a17ef | -3.64741 | -50.1946 | 2024-10-17 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 1a52b133-fa6a-3a30-81e4-7d1517a2adc1 | -3.63635 | -49.83061 | 2024-10-17 05:04:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1a082381-97dd-384f-9685-2f37f93893de | -5.32669 | -50.84791 | 2024-10-17 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2cfef268-a9f9-3b21-8ab1-fac58fa29169 | -4.99616 | -50.88436 | 2024-10-17 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f6d178f9-9dd3-3a09-b63a-49edf48653a6 | -4.99225 | -50.88372 | 2024-10-17 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5e83143e-a5c2-30f8-8fba-302ae2c9b269 | -4.98835 | -50.88307 | 2024-10-17 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c1905d8b-8a86-30c9-8fd4-de84a128952f | -0.07272 | -51.29667 | 2024-10-17 05:04:00 | NOAA-21 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c193212d-a172-3ef6-aa69-ad299b2a82e5 | -0.07208 | -51.30077 | 2024-10-17 05:04:00 | NOAA-21 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 787025c7-3791-33d5-8e65-d6fc69e46569 | -0.06914 | -51.29611 | 2024-10-17 05:04:00 | NOAA-21 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 54556845-0180-34fd-baca-da8d1c67fa88 | -2.15435 | -50.897 | 2024-10-17 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fc5efe94-e956-3a50-90ad-5632b15d794d | -2.12239 | -50.80042 | 2024-10-17 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9298a2b8-9993-345d-a2ef-487ba74262b3 | -2.90168 | -51.81779 | 2024-10-17 05:04:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8472f611-d34d-385b-941c-c14134b095ab | -2.89608 | -51.68454 | 2024-10-17 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 19216922-3e51-3f19-98b8-d5d7c4803e16 | -2.89544 | -51.68874 | 2024-10-17 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 29960a7e-aca4-30bb-9793-ef21d3847aea | -2.89245 | -51.68398 | 2024-10-17 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 2fe75ed8-6135-33bf-9cad-ec27a7e811c3 | -2.89182 | -51.68819 | 2024-10-17 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 0d949a7d-4077-31e5-9a14-94ccd2444ab7 | -2.88819 | -51.68763 | 2024-10-17 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 4ab774e8-9ae5-3648-9c85-5754ddf3ab6f | -2.88755 | -51.69183 | 2024-10-17 05:04:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b686391f-dcc3-36e6-a473-f3487a652114 | -2.8852 | -51.68284 | 2024-10-17 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 66b64b74-b1ff-3848-a5f0-6d2976df4859 | -2.88473 | -51.68006 | 2024-10-17 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 07780408-0b9b-3dfb-b22c-beb52543665c | -2.88456 | -51.68706 | 2024-10-17 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 01c5157f-3a47-387d-bc37-2b72cecf5a1b | -2.88407 | -51.68427 | 2024-10-17 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 71f5bcfc-f656-33f6-9f3c-7a17ae267d5b | -2.88393 | -51.69127 | 2024-10-17 05:04:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| eaa5f637-2db7-31c6-be5c-1186dbacbc51 | -2.88341 | -51.68848 | 2024-10-17 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 240fa2d7-6cd8-351f-ab4b-fa9cb46a6ba7 | -2.88157 | -51.68228 | 2024-10-17 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2057903f-1c61-31d4-acf0-2c88a9c34667 | -2.87351 | -51.65676 | 2024-10-17 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2fbb5b1a-ecc8-3a20-814e-bdc900713cff | -2.86987 | -51.65621 | 2024-10-17 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 75118573-e829-3d4d-8fc8-194e9505c66c | -2.86428 | -51.66828 | 2024-10-17 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 667cf7b4-27b7-3d3e-811d-e1a55aec9ae6 | -2.86362 | -51.67249 | 2024-10-17 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fbc51b03-7fc6-3efe-9ad1-b1b02c7927bc | -2.86203 | -51.3917 | 2024-10-17 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bc31ace7-f2c9-3d8e-ac90-5d8b07df768d | -2.82426 | -51.34799 | 2024-10-17 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d84007bc-4ec9-3b76-b62e-4df1aecf89c4 | -2.82372 | -51.34563 | 2024-10-17 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5ee94734-670f-36d1-bedd-5caad42f5224 | -2.82262 | -51.33432 | 2024-10-17 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 187e3e05-c845-36db-92dc-5b87205af255 | -2.82194 | -51.33869 | 2024-10-17 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 95ac1bb7-c6c5-3f5e-aeb5-9ebd6d4dd8a1 | -2.82134 | -51.33629 | 2024-10-17 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5b8a5764-dc63-3556-9ff6-44e2e7bd7e7e | -2.82125 | -51.34307 | 2024-10-17 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d392c5b0-33b9-3d84-831a-9ac37fdeb42b | -2.82068 | -51.34068 | 2024-10-17 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 708d56ff-d281-39fe-ba52-e9a0e4e09e15 | -2.82057 | -51.34743 | 2024-10-17 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a1bc0335-8fc7-3144-91fe-df053265d8ad | -2.82002 | -51.34506 | 2024-10-17 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f34d7577-ce97-33a7-8db2-6e079d617f5a | -2.81756 | -51.3425 | 2024-10-17 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b8b275e3-13c6-3136-892e-2066b9324c86 | -2.80369 | -51.60254 | 2024-10-17 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3b8661ec-16b1-387e-a506-3420339cdd86 | -2.70271 | -51.7223 | 2024-10-17 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7ab6620d-56c2-31db-81ff-bef3f450e679 | -2.69909 | -51.72174 | 2024-10-17 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e1d42cdd-df43-3830-bee3-c7f0c5c75462 | -2.65099 | -51.73656 | 2024-10-17 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 688ecbb3-fd12-3b5b-a6e6-918bc97ae8ab | -2.59343 | -51.91707 | 2024-10-17 05:04:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5e720b60-13b7-381a-a6ef-fd76d115da13 | -2.58566 | -51.92001 | 2024-10-17 05:04:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dd9b5f67-7738-3b2b-82d0-e7cf996881c4 | -2.58146 | -51.9235 | 2024-10-17 05:04:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 40b83e2c-85fe-3ae8-9ff0-e09d45202569 | -2.26616 | -51.24855 | 2024-10-17 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f9690700-931e-347a-87a4-14f6e45ce60a | -3.67425 | -51.0219 | 2024-10-17 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c5a2a8f1-bd5f-3c37-afdd-960ebc358ea9 | -3.67355 | -51.02657 | 2024-10-17 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 82773d79-5533-34bd-adc0-03677876068e | -3.67284 | -51.03124 | 2024-10-17 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1218c784-398b-3aae-9f7f-eb0819958ee4 | -3.67044 | -51.02135 | 2024-10-17 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 349724c9-ead6-35b5-a86c-7b27958b3f93 | -3.66974 | -51.02599 | 2024-10-17 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d455c5f0-d013-31eb-a143-3bdb1aa09c74 | -3.60282 | -51.00872 | 2024-10-17 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| aaa6543d-41e3-3b39-9978-c08c57a95e6e | -3.59902 | -51.00811 | 2024-10-17 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1ce02d63-90e0-3509-a2a1-7a3ddd7c2923 | -3.5983 | -51.01279 | 2024-10-17 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ad9a9609-1d5a-3a74-b18e-a3dd2639dff2 | -3.51024 | -51.10818 | 2024-10-17 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 19.1 |
| 206c9592-b41d-3d56-b8c5-10460ac26078 | -3.50956 | -51.11006 | 2024-10-17 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 16.3 |


[Clique aqui para ver as próximas entradas](README41.md)
