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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f4fd70ba-e0a1-343e-8a13-066443dcc6e6 | -12.7949 | -44.4661 | 2026-06-19 14:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 185.1 |
| fc634433-032a-3da2-86b9-47dccc1f30c7 | -10.2432 | -47.3491 | 2026-06-19 14:30:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 55.7 |
| bfdc6457-1aa3-3cfd-9e82-5d499ea410b0 | -12.7944 | -44.4895 | 2026-06-19 14:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 863.1 |
| c8091004-0d74-3d21-a600-277890019e94 | -10.543 | -46.329 | 2026-06-19 14:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 73.0 |
| d7dfbc4d-fb62-3af3-b121-a2d13df93819 | -12.7939 | -44.513 | 2026-06-19 14:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 136.3 |
| 44695738-2f79-302a-8774-7b724249ba31 | -10.562 | -46.3266 | 2026-06-19 14:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 82.2 |
| 929c763c-2474-36e7-ac88-d74dbdb556e3 | -12.7939 | -44.513 | 2026-06-19 14:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 158.3 |
| 3cbd44e2-b1b3-3666-ba7c-a4d9e1edab0d | -10.562 | -46.3266 | 2026-06-19 14:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 77.3 |
| 645b93c7-f85c-3fc9-a295-5505a118c7a6 | -8.9072 | -46.9621 | 2026-06-19 14:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 83.2 |
| a7247499-9300-3eb0-a641-017213f52474 | -12.7944 | -44.4895 | 2026-06-19 14:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 998.8 |
| 64f6fed6-3145-36f3-8139-5219cbc58f19 | -12.7746 | -44.5162 | 2026-06-19 14:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 96.3 |
| f99dbd4b-23be-3c1d-bf97-2e8b1a785f0e | -12.7949 | -44.4661 | 2026-06-19 14:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 222.6 |
| 0ebf3d52-28cc-393c-9219-93156c69aa10 | -12.7944 | -44.4895 | 2026-06-19 14:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 579.5 |
| 68c50325-4085-33ea-be4c-0a6ebc110372 | -10.2622 | -47.3469 | 2026-06-19 14:50:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 67.7 |
| 12ec9b3e-cf94-3f86-b268-9a6d1c5c6dbb | -12.7939 | -44.513 | 2026-06-19 14:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 153.8 |
| 6c4f91b1-c311-32c5-9b69-8e3bf5ac205e | -12.7746 | -44.5162 | 2026-06-19 14:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 119.3 |
| a608a86a-50c4-3aec-8639-3ea9faca6de9 | -12.7949 | -44.4661 | 2026-06-19 14:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 213.9 |
| 58695262-2b7f-3900-9f23-bf1e19614d45 | -13.9412 | -53.5667 | 2026-06-19 14:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 63.9 |
| d9723453-296a-344e-848d-a430f7e04b66 | -12.7939 | -44.513 | 2026-06-19 15:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 113.7 |
| 8e14c396-3d61-3dff-8157-7b70455af3aa | -12.7949 | -44.4661 | 2026-06-19 15:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 174.0 |
| 47646839-476b-32cc-82d1-32961571621d | -12.7944 | -44.4895 | 2026-06-19 15:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 465.6 |
| 6873fb9a-ea3b-3300-9a9c-2115e613ba05 | -10.2432 | -47.3491 | 2026-06-19 15:00:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 59.6 |
| 8f5753da-1a87-3d4e-90c5-94759514439f | -8.9072 | -46.9621 | 2026-06-19 15:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 82.7 |
| 61308e6c-b799-3389-9c99-d8e6b6226b49 | -12.7949 | -44.4661 | 2026-06-19 15:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 133.9 |
| 66f26350-2ecb-328d-91bb-b2ef68db0664 | -12.7939 | -44.513 | 2026-06-19 15:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 115.3 |
| d501b4fe-bf19-3bbb-bb46-77b1bc34e6aa | -10.2622 | -47.3469 | 2026-06-19 15:10:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 66.8 |
| 0045952d-9594-31df-b1a0-c0fbe2230610 | -8.9072 | -46.9621 | 2026-06-19 15:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 84.2 |
| 176675a2-ec72-3b78-b5d8-73a8a7cb2f28 | -12.7944 | -44.4895 | 2026-06-19 15:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 376.9 |
| 0631f360-c10c-39b7-8447-9ce1c68b7a20 | -10.562 | -46.3266 | 2026-06-19 15:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 86.7 |
| 5e417e4f-7aa6-3a35-ac21-bd5ad84d00e5 | -9.1674 | -47.2458 | 2026-06-19 15:10:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 65.9 |
| ef7df6e2-506c-3203-a6c0-230beea66b9e | -12.7944 | -44.4895 | 2026-06-19 15:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 308.9 |
| d6d368c3-45e1-3003-a00b-a4f69834975e | -12.7949 | -44.4661 | 2026-06-19 15:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 120.8 |
| 7d34230a-6eca-3284-b2a4-2cd3aaa9984e | -10.2432 | -47.3491 | 2026-06-19 15:20:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 60.1 |
| a74d7ff2-d73e-3441-b54d-86124ce9c4d3 | -12.7939 | -44.513 | 2026-06-19 15:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 94.9 |
| 45cc375b-b3ec-3277-a123-0e42ab7485f7 | -12.7949 | -44.4661 | 2026-06-19 15:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 101.5 |
| d648595b-9513-3b3c-85af-46ed131a9a93 | -10.2432 | -47.3491 | 2026-06-19 15:30:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 59.7 |
| 2882f6f7-2f9d-3841-ae6f-3175d89e6adf | -9.1674 | -47.2458 | 2026-06-19 15:30:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 64.9 |
| c87eaf05-9aff-325d-8c11-9c0dfdb5bc69 | -13.9412 | -53.5667 | 2026-06-19 15:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 63.6 |
| c1d48351-16b9-3dd1-b8bf-5cbeab8dafde | -10.2432 | -47.3491 | 2026-06-19 15:40:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 61.8 |
| 254a43cd-92cc-3b2b-9b0e-bbd424f63aff | -12.7939 | -44.513 | 2026-06-19 15:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 82.4 |
| 58d154d3-cd58-3514-9ec3-0c404a55811c | -13.9412 | -53.5667 | 2026-06-19 15:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 64.5 |
| 3818987b-2835-36d1-a307-e7069d230052 | -9.1674 | -47.2458 | 2026-06-19 15:40:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 57.1 |
| 0c04e34c-790c-3a59-a4a3-cd9e5b270e7b | -13.9412 | -53.5667 | 2026-06-19 15:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 61.0 |
| 4304a99a-c6d4-33c5-840e-57375a4de055 | -12.7939 | -44.513 | 2026-06-19 15:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 74.9 |
| 821cd959-1a72-344d-a2b9-a844379b4bf7 | -10.2432 | -47.3491 | 2026-06-19 15:50:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 61.6 |
| 4959609d-abef-30b8-a224-0523332e2098 | -8.9075 | -46.9399 | 2026-06-19 15:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 89.5 |
| cea7c68d-e28b-3ee1-a264-cea9d790830f | -9.5734 | -47.9309 | 2026-06-19 16:00:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 51.4 |
| 0d03781d-7385-316a-ac7d-57b4658afbdd | -8.9072 | -46.9621 | 2026-06-19 16:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 7645da5c-78bd-3304-ac7a-751d9fb75f8f | -10.2432 | -47.3491 | 2026-06-19 16:20:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 78.2 |
| c5645562-e426-3a95-b47c-b3b6b4b3b353 | -8.9075 | -46.9399 | 2026-06-19 16:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 68.3 |
| 4ef20565-a42f-31aa-9fbb-deb34daddb0f | -12.7939 | -44.513 | 2026-06-19 16:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 119.0 |
| 2a46a15b-b53c-3854-a5a7-eecb0f73da45 | -12.7751 | -44.4927 | 2026-06-19 16:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 541.4 |
| f37bb110-71cc-3414-91c1-db6d4da07bde | -9.5734 | -47.9309 | 2026-06-19 16:30:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 67.4 |
| bed561e0-5eed-3fb5-b9bc-62d8691deb51 | -8.9261 | -46.9602 | 2026-06-19 16:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 80.3 |
| 0790dcf7-60a2-3d4c-9f79-c81a9b2cdc1e | -8.9263 | -46.9379 | 2026-06-19 16:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 80.3 |
| 352a51c9-5fdf-3930-aa42-9a678d67411d | -12.7944 | -44.4895 | 2026-06-19 16:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 779.2 |
| 84bc89e0-c825-3819-a3eb-536e820355e1 | -10.2432 | -47.3491 | 2026-06-19 16:40:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 76.2 |
| fdc075f6-0c52-3682-83ea-7890c801f835 | -12.7751 | -44.4927 | 2026-06-19 16:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 762.1 |
| 5a9b4f5c-675c-3fa9-9a18-bbb0e5d80504 | -12.7939 | -44.513 | 2026-06-19 16:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 89.3 |


