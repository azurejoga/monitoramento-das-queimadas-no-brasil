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

## Dados Diários - Página 52

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0fadac24-f9db-3a6b-b17e-69eebcd3702f | -1.89472 | -53.01316 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7ad38b66-c914-3bb8-8302-02e5e75e8bc8 | -3.41646 | -50.24437 | 2024-11-29 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5b65b8d5-40c4-3d2f-891b-50da6554111c | -1.9397 | -52.96366 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f3d730a5-1954-3a96-8fe3-99ce6cf33bd7 | 1.22511 | -55.94258 | 2024-11-29 04:57:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b4fc6a3f-44e4-3a3e-8534-be742ba1e9e6 | -0.61983 | -51.74677 | 2024-11-29 04:57:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e9d1b670-23f5-3f34-bed6-2e64a135388b | -1.66371 | -52.50936 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fe79824b-8cd0-3ac0-ab54-724797e0f68f | 1.44233 | -50.70691 | 2024-11-29 04:57:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| da3ee570-dc90-3e4f-aa18-3daecbc2cc9a | -1.28726 | -53.37543 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3fb6b33e-9ac0-3d94-80f7-8039584b965f | -3.2642 | -54.11106 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bddf43fb-3e45-3aa7-9513-9a64b59c038c | -2.85889 | -51.84315 | 2024-11-29 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 09d88d3f-5675-3b6f-98a4-464e15ddfbeb | -3.3913 | -50.11097 | 2024-11-29 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7f6bea67-b4b6-35ef-9797-0af27240a431 | -2.59414 | -53.98123 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3375bf9f-877d-3981-b41d-64e53803ca64 | -3.89954 | -49.81966 | 2024-11-29 04:57:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| c060f04d-4549-325f-ab82-2448b6ed937c | -3.46417 | -54.20274 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fc2756b4-516b-320f-a17a-97af4aea40da | -3.07803 | -50.96531 | 2024-11-29 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a4d32735-eb9b-3ec5-bfaf-1f37769d50ba | -1.86257 | -52.27852 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 9e317fdf-6b37-3c64-919a-55596804a4d6 | -2.83507 | -54.11444 | 2024-11-29 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4fbc0544-fee6-369b-9096-7cdcb697853d | -1.09372 | -53.39401 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 17.3 |
| 31b0b1bc-7b56-3011-9603-f796b624af1d | -1.36617 | -51.97012 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8b070a2b-e5c7-3c0b-aa6d-9c8f16e855cb | -1.60535 | -55.37927 | 2024-11-29 04:57:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8e1ad7f6-493d-3ed2-b0c5-6fefc51a81d5 | -1.25591 | -51.63419 | 2024-11-29 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 57c55e98-345d-3a65-a8a7-b997e0619c1f | -1.14412 | -51.67588 | 2024-11-29 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ebaeade4-4cd9-38bb-9c83-2610bbe3e383 | -2.93775 | -53.8943 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7e39612f-0ecb-3bbd-b71c-2bb14986571a | -2.85526 | -46.82577 | 2024-11-29 04:57:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b0366711-68e5-3cd8-b3e7-3d123251def7 | -1.59994 | -55.43578 | 2024-11-29 04:57:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7ab487ab-cf0b-3ec4-900f-2f4922b7c0fa | -4.40996 | -50.82656 | 2024-11-29 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a8c0b2a7-5dfd-374e-a658-e4e786186a78 | -1.88944 | -52.93829 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| aa80b36d-d5f7-3441-b3aa-b06aaf1d06fc | -1.16094 | -53.55195 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 24b6a3e4-bca2-3606-aa39-b286107cc430 | -2.03379 | -53.4958 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 93a4674b-ccb9-392e-9268-2984e7ea58ce | -1.44688 | -55.20349 | 2024-11-29 04:57:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8d75f4a8-7d4a-3059-8ddc-e1efa9dfc6d6 | -1.92308 | -51.1304 | 2024-11-29 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 914672ae-447d-3472-90b5-c6a8362fc91a | -3.26595 | -50.09766 | 2024-11-29 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 89537d08-6b07-3942-b5b7-522b8d123618 | -2.63215 | -51.76751 | 2024-11-29 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 310f9c71-4bca-3e0e-ac4c-58e7e9e756af | -2.97848 | -53.89354 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6f8aa27b-0757-3288-98e0-821fda1ee2ed | -1.31733 | -52.81005 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b93fa3a5-e2fb-368f-9da4-8c56fc234e03 | -2.97678 | -53.88272 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9529abaa-3652-30f3-ad33-b99af819bb99 | 1.6772 | -50.66023 | 2024-11-29 04:57:00 | NOAA-21 | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| af83ff31-1ec7-362e-882a-aea20791556e | -2.80884 | -54.02221 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8a09dbbc-c90d-3ae1-920f-dcfe77be6ee6 | -1.29409 | -51.36676 | 2024-11-29 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2858c772-2dd7-3f0e-b560-ffda51a161e6 | -3.0921 | -53.29546 | 2024-11-29 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 54b551f0-9c8e-3e03-a454-da24deba004a | -1.10332 | -53.59587 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 882fae0f-711b-3f88-b310-d359f4a7fd25 | -3.53341 | -52.15742 | 2024-11-29 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 346d3a72-7f9a-30bf-9bcd-1aff7c330c00 | -1.34945 | -51.98938 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ec89fb6f-ef2f-322a-925a-403a8534c4a3 | -4.31284 | -48.20683 | 2024-11-29 04:57:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e7e17d86-cf8b-370b-865f-ff6272f86a1a | -1.14415 | -53.61616 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3343e52b-2696-32ec-b08f-a48091106996 | -2.25459 | -50.42654 | 2024-11-29 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 63976b63-81e8-352e-83ce-aa575625a736 | -2.57761 | -53.97868 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e9d1cfbb-0e36-35f9-b477-25a25d1e06d7 | -4.17435 | -48.62053 | 2024-11-29 04:57:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 869873f0-5950-3b51-af4c-200eee74105c | -1.12291 | -51.9 | 2024-11-29 04:57:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d8ab96eb-61d4-3dd5-b3af-8b3e08ed6b2f | -2.78732 | -51.71553 | 2024-11-29 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| db368a58-bc66-382d-a40a-b154b3a254d8 | -3.77537 | -51.81389 | 2024-11-29 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 51159dcc-9bb8-34cf-a7e3-22d96f886906 | -2.8405 | -46.79992 | 2024-11-29 04:57:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 915d850f-8133-30e0-807f-b81a6a6565ed | -3.97221 | -47.2388 | 2024-11-29 04:57:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0bc76090-916f-3d91-bc5c-c1c8b2aea7da | -1.14085 | -48.34168 | 2024-11-29 04:57:00 | NOAA-21 | BELÉM | PARÁ | Brasil | 1501402 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9c0a21ad-64a8-308e-888f-afcc57cd6287 | -3.29494 | -53.67595 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e785265c-ec56-3034-9326-aa3c6ad94322 | -1.36557 | -55.18375 | 2024-11-29 04:57:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 49e4e52c-1f3c-3404-927c-e451983ef3db | -2.52602 | -54.13305 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2a8851a5-6126-3a4e-9af5-f71a71ce147b | -1.14826 | -53.54649 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2b5260e2-68d9-3058-a707-f6563262d208 | -1.6667 | -52.73073 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 00fa2449-eb1e-3de8-91e5-6ffeede1ae29 | -3.53658 | -50.19376 | 2024-11-29 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8f062e63-32db-3449-828b-c96da6cffdc9 | -2.2951 | -50.68612 | 2024-11-29 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c0218bd7-bb6f-31f1-95ca-b223fb60f51f | 0.98131 | -50.12492 | 2024-11-29 04:57:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 13.0 |
| d35694bc-a6ff-369f-83e2-657e44a4c320 | -1.35575 | -52.93634 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 40d05303-d5a0-3db0-be40-a1f5ead67118 | -2.84215 | -54.09082 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c746f989-49fb-32dc-bd42-3c1721829e64 | -1.69232 | -52.43518 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 9ef614e7-d3b5-3ca7-a3ce-9ae177656e98 | -1.36336 | -51.96604 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b8034ec2-f867-3e52-8a41-fbf1867ec5fe | -3.28717 | -53.66068 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 856c399f-c26c-35c7-87af-3ebb770a8c3e | -2.53177 | -47.32835 | 2024-11-29 04:57:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 27f82f3d-1466-339d-935a-58ebdc40dd06 | 0.97716 | -50.12513 | 2024-11-29 04:57:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 247cf1b5-b97b-3fb2-bf98-0b65450c610c | -2.44475 | -50.51784 | 2024-11-29 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0df3904f-f0fb-39db-9780-488d42ca75bc | -1.10716 | -53.59295 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e4ba333a-dae5-37e3-96ff-6f998772d239 | -1.12153 | -53.2158 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 14fa998c-98b1-3fa1-bfc0-6e75bb3a9a55 | -3.66917 | -54.28403 | 2024-11-29 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8a509968-2f95-36cd-b6f3-2866d4d9efd5 | -1.6287 | -53.86863 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 04e0a9f5-f45e-340e-941b-cb081bee9e6a | -3.1151 | -54.47747 | 2024-11-29 04:57:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 5b15aa1a-20a0-3eba-83d0-705ffd38d7f4 | -3.04022 | -54.08628 | 2024-11-29 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4474d2e5-a060-3962-bdd4-f3d0bed8097b | -2.79845 | -54.04528 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 84d4ee89-db18-3b61-9441-37db36b91e38 | -1.70164 | -52.63679 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 9610bf08-d06d-3b5e-a775-ecbb4f94251f | -1.06941 | -51.75641 | 2024-11-29 04:57:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1aeccf07-bb9d-37e4-8f9b-624073a8c42b | -0.04523 | -51.5449 | 2024-11-29 04:57:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5129cc9b-ebd7-3779-88a8-52b3ee3a52ba | -3.49931 | -50.29032 | 2024-11-29 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4e7f27a0-9c77-31a6-9e6a-e4184f96f10d | -1.37581 | -53.6351 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e424f89f-7383-3376-9148-5b4c3f86ab08 | -1.59216 | -52.24772 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 97efeb32-3f0b-35cd-bc60-9f85d8c16d8e | -4.07396 | -47.02669 | 2024-11-29 04:57:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 71dc3c2d-39fa-3f8d-ac8f-3c9d513e8bca | -3.2678 | -53.7632 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8736c92f-0964-3073-b7f9-4523df3fecd1 | -2.63051 | -53.98685 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3f921a6b-b953-31a5-832f-8bf7ad46e5eb | -2.8283 | -54.07104 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cad4edfd-6bae-39f5-a310-c08dd7a8b581 | -1.58888 | -52.26879 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 657bf1f6-7a56-392f-a747-047c7b2be753 | -2.36666 | -56.11376 | 2024-11-29 04:57:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e45adfde-bda1-3a2d-8c1e-bb521fcd30c1 | -2.85456 | -46.83042 | 2024-11-29 04:57:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| afd8e4ee-36de-3c45-92d6-e5488862da44 | -3.39056 | -54.28317 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6fb4a084-9422-3e77-b14e-706939e6b703 | -2.69842 | -51.99717 | 2024-11-29 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6f117e4d-c069-366d-a0a3-c4d55e1ec939 | -1.36281 | -51.9696 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b80241f6-fde8-3cd5-ac0c-3f0be3edcd77 | -1.55983 | -55.266 | 2024-11-29 04:57:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7a0e7d19-9eeb-3bf1-b797-42cb6fcf3710 | -1.98166 | -49.51224 | 2024-11-29 04:57:00 | NOAA-21 | LIMOEIRO DO AJURU | PARÁ | Brasil | 1504000 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fc48400e-b971-32f3-a63b-eeca6b72fb51 | -2.04052 | -54.6904 | 2024-11-29 04:57:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bcbbdc1b-999e-33d0-a572-b1a3da457bf4 | -3.0953 | -54.12715 | 2024-11-29 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3acdde60-2226-3683-8d68-6300fae0af63 | 1.43813 | -55.89066 | 2024-11-29 04:57:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 997334d0-50f3-3229-b0ea-e2de351276f5 | -3.11619 | -54.4705 | 2024-11-29 04:57:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6d8d843f-7e79-3233-b4bf-468ff76f8005 | 0.62769 | -50.57308 | 2024-11-29 04:57:00 | NOAA-21 | ITAUBAL | AMAPÁ | Brasil | 1600253 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |


[Clique aqui para ver as próximas entradas](README53.md)
