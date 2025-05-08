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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 87ea9a78-9d80-353f-804a-6ee840b2b57d | -10.6689 | -44.3904 | 2025-05-08 12:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 78.0 |
| f5557075-bc2c-30fb-80f2-67489665582a | -6.6211 | -44.7668 | 2025-05-08 12:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 72.0 |
| 59173a6a-3ee2-34c2-b0b3-a565fb6acd0a | -6.9801 | -42.809 | 2025-05-08 12:50:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 105.5 |
| 77d05159-02b0-3d81-b789-ca14317a651d | -6.9613 | -42.8108 | 2025-05-08 12:50:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 145.4 |
| cb6d425d-da43-3967-9ecb-53a394b6a631 | -10.6689 | -44.3904 | 2025-05-08 13:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 80.9 |
| e3d0df1f-129a-33c1-b3fb-6926c2a474c7 | -6.9613 | -42.8108 | 2025-05-08 13:00:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 110.3 |
| 3806440e-322a-3c4f-a9c8-8db9839c8d10 | -6.9801 | -42.809 | 2025-05-08 13:00:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 121.4 |
| 9ed7f87f-fb02-3367-ba86-c977c4ad5112 | -18.4279 | -54.7129 | 2025-05-08 13:00:00 | GOES-19 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 88.8 |
| a10682af-267d-3456-baca-93e2d76446f3 | -10.6689 | -44.3904 | 2025-05-08 13:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 80.6 |
| 1b9ce157-c2ef-3759-bd84-a728cf2191c4 | -6.9613 | -42.8108 | 2025-05-08 13:10:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 95.5 |
| 1121ae05-4c82-31f0-b04f-0fe6b10b4696 | -18.4279 | -54.7129 | 2025-05-08 13:10:00 | GOES-19 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 87.5 |
| f45c2e73-7c06-389f-aa1c-e3fd673b6717 | -18.4283 | -54.6916 | 2025-05-08 13:10:00 | GOES-19 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 94.2 |
| 59017849-d68b-3b37-b133-87fdd6f26f57 | -6.9801 | -42.809 | 2025-05-08 13:10:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 138.4 |
| 778abbba-d89b-37a0-beca-ac102bf193c5 | -18.408 | -54.7158 | 2025-05-08 13:20:00 | GOES-19 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 66.4 |
| 4f7aae58-2329-3a4f-bb56-cdae141470f2 | -18.4279 | -54.7129 | 2025-05-08 13:20:00 | GOES-19 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 74.0 |
| 4bd353c0-ea9c-330f-a941-51998293c32f | -18.4283 | -54.6916 | 2025-05-08 13:20:00 | GOES-19 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 79.8 |
| f2ef2fd0-cbc7-39cb-a9ec-dd99d4a3ce95 | -10.9733 | -44.441 | 2025-05-08 13:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 109.6 |
| 39b8db0e-3421-360c-8711-9f2eded8a900 | -6.9613 | -42.8108 | 2025-05-08 13:20:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 97.2 |
| 5acc71b6-c5c7-337a-9717-cc64a9936bbe | -10.6689 | -44.3904 | 2025-05-08 13:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 75.7 |
| 54d026e4-f307-389c-946a-af283e1882be | -18.4084 | -54.6946 | 2025-05-08 13:20:00 | GOES-19 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 70.8 |
| fee4bc64-aeec-3e61-85aa-bb9856864493 | -6.9801 | -42.809 | 2025-05-08 13:20:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 117.3 |
| 24441be7-ed00-30d3-9f42-70071c16c11e | -18.4283 | -54.6916 | 2025-05-08 13:30:00 | GOES-19 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 88.9 |
| bc53de77-848b-3bf3-aef9-b3ab1ae07244 | -6.6211 | -44.7668 | 2025-05-08 13:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 67.5 |
| 665873c0-1061-38ca-99d3-06506b61d992 | -10.9736 | -44.4177 | 2025-05-08 13:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 102.8 |
| a326810e-2a39-3acc-a440-1c0489b7356a | -6.9613 | -42.8108 | 2025-05-08 13:30:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 92.3 |
| 39dcaea7-c8de-3fc4-b839-926ed9737406 | -18.408 | -54.7158 | 2025-05-08 13:30:00 | GOES-19 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 76.5 |
| 12c24270-8f28-3a4f-8e41-9fd7a06f99ed | -18.4279 | -54.7129 | 2025-05-08 13:30:00 | GOES-19 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 99.6 |
| 3eb3b5d7-c2cc-3640-9f41-3cbe4883ba09 | -18.4084 | -54.6946 | 2025-05-08 13:30:00 | GOES-19 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 68.5 |
| 580b5e47-d6e6-3625-98c1-95ad926c6320 | -10.9733 | -44.441 | 2025-05-08 13:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 160.5 |
| 7f86b727-0d8b-30be-a066-1bf51e65ad00 | -6.9801 | -42.809 | 2025-05-08 13:30:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 110.4 |
| 1456fc08-0334-3830-943e-8b5b78738660 | -10.6689 | -44.3904 | 2025-05-08 13:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 71.3 |
| 56fb4609-f26f-375c-ba34-1d04b8cfbeea | -18.408 | -54.7158 | 2025-05-08 13:40:00 | GOES-19 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 91.1 |
| 9d2ef8a6-93ad-30e7-b09a-f0bf243366e3 | -10.9736 | -44.4177 | 2025-05-08 13:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 105.9 |
| d9e66325-16ea-3b49-86a9-184cad310664 | -18.4084 | -54.6946 | 2025-05-08 13:40:00 | GOES-19 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 80.3 |
| 8aa14a61-b539-3b6f-b255-4102f668ed4b | -18.4283 | -54.6916 | 2025-05-08 13:40:00 | GOES-19 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 86.7 |
| a086c762-0731-31a2-b5a7-6593c67e3668 | -18.4279 | -54.7129 | 2025-05-08 13:40:00 | GOES-19 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 97.9 |
| e58211c1-aa79-387b-9f35-4eda68c65196 | -6.9613 | -42.8108 | 2025-05-08 13:40:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 95.0 |
| 1d8d5992-ec04-3bbb-8e31-94156939bafd | -10.6689 | -44.3904 | 2025-05-08 13:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 76.4 |
| d6bb51e1-a81a-375b-bc8c-052893da07b7 | -10.9733 | -44.441 | 2025-05-08 13:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 193.4 |
| 2ddad878-787f-30fd-95c5-65320738e2ec | -6.9801 | -42.809 | 2025-05-08 13:40:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 101.5 |
| 63204b0c-46d0-3bfb-a14e-f7469192cbfd | -6.9613 | -42.8108 | 2025-05-08 13:50:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 107.6 |
| 881bb800-d000-343f-95c3-203de9bb877b | -18.4084 | -54.6946 | 2025-05-08 13:50:00 | GOES-19 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 94.7 |
| 1db956e0-4ca4-3d51-8f9b-d14d8f7f6b1b | -10.9541 | -44.4437 | 2025-05-08 13:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 73.4 |
| b7c9011d-591f-39a7-8a26-613ef8ab6a90 | -18.4279 | -54.7129 | 2025-05-08 13:50:00 | GOES-19 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 63.0 |
| 49a83238-eb45-3d45-a67e-b421c18b7231 | -6.9801 | -42.809 | 2025-05-08 13:50:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 95.0 |
| b107830a-4ff4-379e-b2a1-af3de63bd729 | -18.408 | -54.7158 | 2025-05-08 13:50:00 | GOES-19 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 86.5 |
| 81c68be6-807c-3dc8-9484-689c15cd62cd | -10.9733 | -44.441 | 2025-05-08 13:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 222.7 |
| d0ad6bab-30fc-37bf-b70f-3d75c0cd285b | -18.4283 | -54.6916 | 2025-05-08 13:50:00 | GOES-19 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 67.4 |
| 9fdacceb-7d79-37c7-bd26-1c99db3edf39 | -10.6689 | -44.3904 | 2025-05-08 13:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 80.4 |
| 938c6175-1026-3006-b702-1d3d6095e122 | -10.9736 | -44.4177 | 2025-05-08 13:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 92.9 |
| 5018863c-e1ef-3144-bf97-07095e4ffe0a | -12.8355 | -47.4117 | 2025-05-08 13:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 68.4 |
| bc325cb8-aad1-375f-b57e-0abc97d3adad | -13.0335 | -45.0794 | 2025-05-08 14:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 101.7 |
| fac1ccc8-a2c2-3f9a-b7d2-0f76772e52dc | -18.4279 | -54.7129 | 2025-05-08 14:00:00 | GOES-19 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 87.5 |
| 96487b56-ed35-3bbd-939b-5c2c02db2861 | -10.9736 | -44.4177 | 2025-05-08 14:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 125.8 |
| 56334cf5-7a1c-3d51-bf05-0f5c2b84e90e | -12.6339 | -54.0642 | 2025-05-08 14:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 59.6 |
| d9c5c6dd-ca53-31f6-a752-f077c5dda0ca | -6.9613 | -42.8108 | 2025-05-08 14:00:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 90.5 |
| ca51ba65-f922-381f-9041-59b20f0746a8 | -10.6689 | -44.3904 | 2025-05-08 14:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 92.8 |
| db190a40-7dba-3d61-b7d7-605d7e96a8c2 | -6.9801 | -42.809 | 2025-05-08 14:00:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 108.4 |
| 2ad6c2e9-7225-300c-a1d4-1d9b5726b644 | -6.6211 | -44.7668 | 2025-05-08 14:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 134.9 |
| b2c408f3-840a-33bb-9c40-93efadc335db | -10.9733 | -44.441 | 2025-05-08 14:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 263.1 |
| e6c4a98b-64b9-3001-aa18-800831a5b8c5 | -18.4283 | -54.6916 | 2025-05-08 14:00:00 | GOES-19 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 92.3 |
| 1444a296-e294-39ce-ab52-781d1437fd96 | -12.653 | -54.0622 | 2025-05-08 14:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 69.1 |
| 2ef67e70-a433-3f44-ac68-cab0313f8089 | -10.6689 | -44.3904 | 2025-05-08 14:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 89.2 |
| 596e4039-be8a-3ed1-a659-b32bc6235cdf | -13.0335 | -45.0794 | 2025-05-08 14:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 126.9 |
| e6a749cf-e4cd-36f3-a8fe-d46cc74a5e5f | -18.408 | -54.7158 | 2025-05-08 14:10:00 | GOES-19 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 74.4 |
| 5a67ee9b-f82b-3e19-a0e0-760a55fdefaf | -10.9733 | -44.441 | 2025-05-08 14:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 267.2 |
| 95967bbc-244e-30a4-96c6-b0295581df89 | -18.4084 | -54.6946 | 2025-05-08 14:10:00 | GOES-19 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 85.0 |
| 4f2fa95c-3d0c-3f8d-a42c-9f7689162021 | -12.836 | -47.3893 | 2025-05-08 14:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 60.7 |
| cf3a9c2c-0259-3aea-9e72-4c54281da94b | -10.9541 | -44.4437 | 2025-05-08 14:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 104.6 |
| 0925b2db-8461-3498-936f-9f2c7f47da5b | -18.4283 | -54.6916 | 2025-05-08 14:10:00 | GOES-19 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 62.7 |
| 2bea3b13-626b-3b9a-b33e-ac32d343eaa1 | -12.6339 | -54.0642 | 2025-05-08 14:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 91.6 |
| ada93824-4617-3aaf-87c3-326e298d322e | -6.9801 | -42.809 | 2025-05-08 14:10:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 85.6 |
| 5bb8adc2-5eed-33ff-98fd-7f9a3d212281 | -12.8355 | -47.4117 | 2025-05-08 14:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 89.6 |
| 92b62050-a2ee-3620-8956-cd357b4ad9a8 | -10.9736 | -44.4177 | 2025-05-08 14:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 94.5 |
| bb199cda-7fcf-37b9-9c22-75f662f98364 | -12.8355 | -47.4117 | 2025-05-08 14:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 67.0 |
| b7eec1f8-4976-3f93-9131-e6412aaf58a4 | -18.408 | -54.7158 | 2025-05-08 14:20:00 | GOES-19 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 67.7 |
| 91cda469-796b-3510-bfa7-ff22d7583e65 | -6.9613 | -42.8108 | 2025-05-08 14:20:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 92.7 |
| 4ac013fc-b162-3754-bc27-0eb79d99ba57 | -12.6339 | -54.0642 | 2025-05-08 14:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 81.5 |
| 917a9102-3347-3581-8ace-2003c446bc1a | -10.5817 | -46.279 | 2025-05-08 14:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 61.0 |
| 4aeed822-5ed8-321e-9fa6-f6453a8063a1 | -10.6689 | -44.3904 | 2025-05-08 14:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 85.6 |
| 1e1ae7d9-1b96-3538-a323-127e3d6d5b29 | -18.4084 | -54.6946 | 2025-05-08 14:20:00 | GOES-19 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 64.7 |
| f3d4aecf-ea9f-3dea-ba09-da604d8c69e0 | -12.653 | -54.0622 | 2025-05-08 14:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 70.9 |
| dc949ce3-fca6-3947-9884-d83dba27a085 | -10.9733 | -44.441 | 2025-05-08 14:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 286.6 |
| bcf93ea4-9bb2-3496-b596-838c3c1eec07 | -10.9736 | -44.4177 | 2025-05-08 14:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 135.2 |
| 07653857-7b89-384e-a808-a1713a7c68c1 | -10.6693 | -44.3671 | 2025-05-08 14:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 67.1 |
| 8f351b5e-13ec-3125-b14a-7be3937814b0 | -18.4283 | -54.6916 | 2025-05-08 14:20:00 | GOES-19 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 88.2 |
| ce1250a8-dd87-3223-b785-f661add50fa0 | -13.0335 | -45.0794 | 2025-05-08 14:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 104.6 |
| 2b41ac0b-bff1-388b-acb8-d5b30faac69c | -12.836 | -47.3893 | 2025-05-08 14:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 63.0 |
| d49278e5-b617-3b56-a63a-71c53665ec07 | -6.9801 | -42.809 | 2025-05-08 14:20:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 93.4 |
| 83c4bd36-a152-3265-889a-8be9650d190b | -18.408 | -54.7158 | 2025-05-08 14:30:00 | GOES-19 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 71.4 |
| 499b1205-5cc7-3474-94e9-a183a4ccd161 | -10.9541 | -44.4437 | 2025-05-08 14:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 80.5 |
| 02a0594f-dea3-3b21-8f57-89f47995dc31 | -10.9736 | -44.4177 | 2025-05-08 14:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 110.7 |
| 05237d8d-83b8-394b-85c4-f1c3e70a288e | -13.3752 | -54.2538 | 2025-05-08 14:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 55.4 |
| 116f40b3-800e-399c-ba1e-b7f4ef3926ec | -6.9613 | -42.8108 | 2025-05-08 14:30:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 95.4 |
| 63196ee5-c910-33f3-ad4c-8719586807d0 | -10.6689 | -44.3904 | 2025-05-08 14:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 83.1 |
| b2016be7-f8c5-3539-abe9-aa7fa11552ba | -12.653 | -54.0622 | 2025-05-08 14:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 62.5 |
| f683c630-95da-3ca4-a5db-79b6a2c93f4c | -18.4283 | -54.6916 | 2025-05-08 14:30:00 | GOES-19 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 85.7 |
| 9616f515-b271-36f8-a970-dc33cf3ca5c8 | -12.8355 | -47.4117 | 2025-05-08 14:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 69.0 |
| 21b25580-0ad8-38c6-a62d-619b3a146032 | -12.6339 | -54.0642 | 2025-05-08 14:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 79.9 |
| cda239a9-94ab-367e-8c0a-274cfc41539a | -10.9733 | -44.441 | 2025-05-08 14:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 245.3 |


[Clique aqui para ver as próximas entradas](README8.md)
