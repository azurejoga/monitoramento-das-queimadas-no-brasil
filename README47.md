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

## Dados Diários - Página 47

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 76016bb6-fdb1-3948-b235-3e8fe033d025 | -2.2482 | -53.6619 | 2024-11-11 06:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 50.7 |
| 198f06ae-6f15-31b8-861f-6df39392ef05 | -2.2481 | -53.6821 | 2024-11-11 06:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 43.8 |
| 17ebee2a-70d8-3b74-9b3c-a2ff45ed2a6a | -16.00525 | -59.30839 | 2024-11-11 06:01:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0e7b4fb3-11df-32c2-a56c-5a3d2f6ad867 | -16.00413 | -59.31952 | 2024-11-11 06:01:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| de5de2c3-41b2-37c9-b39e-c0f2b32c5935 | -16.00111 | -59.34951 | 2024-11-11 06:01:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 25.2 |
| f10089ba-a2b1-3d2e-9579-c9ce283df2be | -16.00538 | -59.34932 | 2024-11-11 06:01:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 18.0 |
| 03b47baa-318f-3dde-acce-7fdb490320c9 | -15.97016 | -59.32272 | 2024-11-11 06:01:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 785ac353-ef77-35a1-8c29-57b436c84696 | -15.99687 | -59.36839 | 2024-11-11 06:01:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d4c7b458-09c6-3d16-ab54-e907b4fcceba | -16.00596 | -59.34318 | 2024-11-11 06:01:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 18.0 |
| ee5931e4-dfd0-3b38-92ca-5db3bcc01701 | -15.99929 | -59.34262 | 2024-11-11 06:01:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 40.7 |
| d4c19ab6-f395-3be8-96fd-61e336075970 | -16.01134 | -59.31475 | 2024-11-11 06:01:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9881bdfb-db74-35f4-8f3d-1912ec98ef93 | -15.99989 | -59.33619 | 2024-11-11 06:01:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 19.9 |
| 38192fdc-515b-36be-a37c-fc2087e24ea0 | -16.00816 | -59.31984 | 2024-11-11 06:01:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| d6ba77b3-665d-370c-9280-146a03f2ca62 | -16.00716 | -59.35622 | 2024-11-11 06:01:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 29.8 |
| c6646d8c-ceee-3c7c-a23e-bb9ed73daf7d | -15.99258 | -59.34249 | 2024-11-11 06:01:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 40.7 |
| 490b1844-0887-3b0d-96f0-95c10558dd08 | -16.00416 | -59.36226 | 2024-11-11 06:01:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 24.6 |
| 9ec624b9-d49a-3364-8e71-020fd5a828ba | -15.99863 | -59.3072 | 2024-11-11 06:01:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 43ac70ce-ba9d-38b4-b562-2cffd270f314 | -15.9769 | -59.32254 | 2024-11-11 06:01:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b9d2803a-3613-3eae-bed1-ecbddb3b0da4 | -16.00045 | -59.35611 | 2024-11-11 06:01:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 25.2 |
| 79d66de1-42d8-3121-ba67-ccaae4e6f382 | -15.9998 | -59.36255 | 2024-11-11 06:01:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| c564dd85-c1e0-398d-998d-c4d7ecc9dbdf | -16.00177 | -59.34305 | 2024-11-11 06:01:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 22.6 |
| 7c643220-73d2-3756-b357-f35eae39f056 | -15.99438 | -59.34967 | 2024-11-11 06:01:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 25.2 |
| a323bf8a-3880-3996-af84-e9d4b5b392a7 | -16.01201 | -59.35026 | 2024-11-11 06:01:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 18.0 |
| a449781c-2bef-38aa-83fb-90354ab301a4 | -16.01076 | -59.32059 | 2024-11-11 06:01:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 236c5998-4fc3-3717-92bc-83ef3458e190 | -16.0024 | -59.33677 | 2024-11-11 06:01:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 22.6 |
| 2f77c665-23ba-3a7b-8699-4ea052285509 | -15.99804 | -59.35593 | 2024-11-11 06:01:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 11.1 |
| bf24505d-c6cf-3c7b-9d71-c8bf67c9d482 | -15.9695 | -59.32943 | 2024-11-11 06:01:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| eb7a5a9e-9a2d-358d-92b8-b918c299c325 | -16.00841 | -59.34385 | 2024-11-11 06:01:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 33.1 |
| 168a71f4-0fdb-334d-b661-7815ce797853 | -16.00651 | -59.36259 | 2024-11-11 06:01:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 8ef19dc5-dda5-3612-a21e-ed0469f72dc4 | -15.99506 | -59.34283 | 2024-11-11 06:01:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 22.6 |
| 8d999c67-3093-31fb-aceb-82bf315b0628 | -15.99372 | -59.35624 | 2024-11-11 06:01:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 25.2 |
| 3ab16a11-fb9d-3756-8e2a-5ee4d5f84e23 | -16.00478 | -59.35571 | 2024-11-11 06:01:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 24.6 |
| 539d6b18-6b99-3224-b419-e1b8e675fc42 | -15.96283 | -59.32887 | 2024-11-11 06:01:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1f7d609a-eb7a-3d3e-b028-630d84af4183 | -15.99867 | -59.34925 | 2024-11-11 06:01:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 40.7 |
| fcad1e4c-610b-384a-a29a-9be4f98c38e2 | -15.98833 | -59.34297 | 2024-11-11 06:01:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 7d95fe7b-85a9-35b1-9a30-4a14a953ffdf | -16.00779 | -59.34993 | 2024-11-11 06:01:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 29.8 |
| bfb8c7cc-e55d-327b-a8da-964d5cf98118 | -16.00472 | -59.31363 | 2024-11-11 06:01:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 75130b07-9844-345a-85fe-dc6f66e46d51 | -16.00257 | -59.30769 | 2024-11-11 06:01:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 540bdbfd-3daa-3785-9460-c788f30919e1 | -16.00871 | -59.31398 | 2024-11-11 06:01:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3b82b80d-54b1-32b6-9dd5-85cd0b245147 | -15.99745 | -59.36229 | 2024-11-11 06:01:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 11.1 |
| f894760d-6a9c-37a5-b20c-d54fba5eb9c2 | -15.99194 | -59.34935 | 2024-11-11 06:01:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 40.7 |
| 0d335ce0-7b08-3604-9c26-43193353c570 | -15.99574 | -59.33611 | 2024-11-11 06:01:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 22.6 |
| 266efe1f-ab25-3ed9-a7f2-c67893fb9250 | -15.99918 | -59.36871 | 2024-11-11 06:01:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 67546f0b-c339-33d6-9264-ce8e657159ba | -15.98766 | -59.34965 | 2024-11-11 06:01:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| e8116f2e-b2cb-3826-850f-aaf820ab52ce | -16.01258 | -59.34429 | 2024-11-11 06:01:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 18.0 |
| fbe142ad-18d9-32b2-97fe-94e1a405d673 | -2.2298 | -53.6623 | 2024-11-11 06:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 73.6 |
| 3958e63d-e15e-3ae4-9d6e-31710ecccb5f | -2.7587 | -49.3497 | 2024-11-11 06:10:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 68.9 |
| a07faaa6-3651-3634-abc8-9f98e1e3aeda | -2.2297 | -53.6824 | 2024-11-11 06:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 69.3 |
| 8dfe2cda-3615-333b-8a5e-1b3f5132da4f | -2.248 | -53.7426 | 2024-11-11 06:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 62.4 |
| f200b1a1-c72c-3e3a-ac81-48f61b3ab760 | -2.2482 | -53.6619 | 2024-11-11 06:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 48.1 |
| c87f5912-c5c3-3f09-bca0-74e447463ab2 | -3.1458 | -54.4859 | 2024-11-11 06:10:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 50.6 |
| 5f5b36cb-0499-3ee4-8bba-717d26ff4d8a | -3.1458 | -54.4859 | 2024-11-11 06:20:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 49.1 |
| 4b1325ac-bc6b-3c48-9b38-e335bcf6d7e9 | -2.2298 | -53.6623 | 2024-11-11 06:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 72.2 |
| 04ba6db4-a9c0-3fe3-a9b1-fd67578344ac | -2.248 | -53.7426 | 2024-11-11 06:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 56.8 |
| a9bb8105-8639-39ee-be9f-c7516189a234 | -2.7587 | -49.3497 | 2024-11-11 06:20:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 69.2 |
| 8b1a6158-3e24-3831-b6d1-34b465477bb1 | -2.2482 | -53.6619 | 2024-11-11 06:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 46.6 |
| be76507e-0988-3d12-9f28-143a758abed9 | -2.2297 | -53.6824 | 2024-11-11 06:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 6e8b8fbd-09c2-3c2f-bd35-021e35672a60 | -2.2298 | -53.6623 | 2024-11-11 06:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 6b0f5264-fc86-3b3f-8ccd-b314d51a52d9 | -2.248 | -53.7426 | 2024-11-11 06:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 46.4 |
| 7d797784-e572-39e6-8a53-f762ae4d102a | -2.2297 | -53.6824 | 2024-11-11 06:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 0426f51f-0c37-3734-be92-a237fca66dda | -2.7587 | -49.3497 | 2024-11-11 06:30:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 80.6 |
| 41f4daf0-8950-360d-bf73-fd814a38f475 | -4.1284 | -49.1307 | 2024-11-11 06:30:00 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 68.8 |
| 68c7ab05-7878-3333-bf41-66365f5732d3 | -4.1468 | -49.1513 | 2024-11-11 06:30:00 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 83.4 |
| d62ff79a-d136-31a5-b8cc-594b735ec6b7 | -4.1283 | -49.1521 | 2024-11-11 06:30:00 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 8f38daf1-5917-3e4c-9336-be44b76653fa | -4.1469 | -49.1299 | 2024-11-11 06:30:00 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 73.4 |
| b73c797a-cec5-39db-be29-41a796083384 | -2.248 | -53.7426 | 2024-11-11 06:40:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 48.0 |
| 4ee4b6c1-9525-3094-b7b7-923f873653c3 | -2.2298 | -53.6623 | 2024-11-11 06:40:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 67.9 |
| 620c2b83-aa33-306b-a622-d4b851faf761 | -4.1283 | -49.1521 | 2024-11-11 06:40:00 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 696cb157-f67b-340c-90f9-e4f8f2eaa710 | -4.1284 | -49.1307 | 2024-11-11 06:40:00 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 6b5d8e57-7cb7-3da2-8a21-12e33fcb3e76 | -2.2297 | -53.6824 | 2024-11-11 06:40:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 53.1 |
| d3344c2a-7384-3c70-982f-6e30c3b5aacf | -4.1468 | -49.1513 | 2024-11-11 06:40:00 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 69.6 |
| afaf473b-2f1b-3ae3-be08-d1cc1027353c | -2.7587 | -49.3497 | 2024-11-11 06:40:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 88.3 |
| bbe0aa82-9011-370d-802a-f6f6bb9098a5 | -2.2663 | -53.7422 | 2024-11-11 06:40:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 44.6 |
| 4948530b-b17a-3dce-8073-23f10bebd752 | -2.2298 | -53.6623 | 2024-11-11 06:50:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 079b795d-4667-3750-aa3f-06a3515bf55f | -2.2297 | -53.6824 | 2024-11-11 06:50:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 59.0 |
| fc8217cb-954b-3ebd-beae-6bf7b381824f | -2.7587 | -49.3497 | 2024-11-11 06:50:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 88.3 |
| 5e17ef19-17a7-3aea-89ab-5675a39e0bf3 | -2.248 | -53.7426 | 2024-11-11 06:50:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 50.6 |
| 9084b122-8707-394b-965a-f5f23d12f862 | -2.7587 | -49.3497 | 2024-11-11 07:00:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 83.4 |
| a8f4ae33-97d0-3aca-a879-5bf4a27bda43 | -2.248 | -53.7426 | 2024-11-11 07:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 48.3 |
| eee867d0-ea05-395e-8467-da2eff0674cf | -2.2297 | -53.6824 | 2024-11-11 07:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 54.7 |
| 3cd28d0c-b855-34b3-8be1-7d60ea5cb019 | -2.2298 | -53.6623 | 2024-11-11 07:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 89e605fb-173e-3fea-bad0-cba5ee3d0a8c | -2.7587 | -49.3497 | 2024-11-11 07:10:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 82.3 |
| 87e878c4-433e-38f1-9d0d-4883cb95859c | -2.248 | -53.7426 | 2024-11-11 07:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 47.8 |
| 1ef9f729-aa41-37d2-a010-a4a74e80becc | -2.2298 | -53.6623 | 2024-11-11 07:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 654e44be-8aa1-36fe-85f7-633c16fc4635 | -3.0903 | -45.3426 | 2024-11-11 07:10:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 70.7 |
| 5b70d5d0-688d-3453-80d0-32ee2fb807cc | -2.2297 | -53.6824 | 2024-11-11 07:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 723d2a6d-ed71-392f-a74f-acb2d1ef964a | -3.0717 | -45.3433 | 2024-11-11 07:10:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 73.4 |
| 747e1a9a-b741-354a-9b88-10196c7db47a | -2.2482 | -53.6619 | 2024-11-11 07:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 45.0 |
| e035852d-6977-3b0b-b945-75a6e82161be | -2.2298 | -53.6623 | 2024-11-11 07:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 581fc529-4753-39d0-8398-4d8934b6ed9f | -2.7587 | -49.3497 | 2024-11-11 07:20:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 70.6 |
| 0d88466d-8a53-3cdb-b95e-6d5cccc8fd9f | -2.248 | -53.7426 | 2024-11-11 07:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 50.7 |
| 2ef28788-3055-31d5-af9e-66c6e1ab4a51 | -2.2297 | -53.6824 | 2024-11-11 07:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 3598c0f5-98ef-3f19-ba37-25138aad2829 | -2.248 | -53.7426 | 2024-11-11 07:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 47.0 |
| 2b2e1e0d-332f-309b-bc01-d8c586a02c9e | -2.2297 | -53.6824 | 2024-11-11 07:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 48.3 |
| 1b699721-b546-3a6c-ad1d-7ac62e3c0509 | -2.2298 | -53.6623 | 2024-11-11 07:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 52.4 |
| 9125e7bd-3a2b-35f5-bc4c-463a95b1644c | -2.2298 | -53.6623 | 2024-11-11 07:40:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 51.5 |
| 51f6d288-fc0a-395f-a4da-1942b8ec9fd4 | -17.5872 | -57.5328 | 2024-11-11 07:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 82.6 |
| d69e4290-b540-35c2-9044-e1e3c6fecfd3 | -17.2933 | -57.4857 | 2024-11-11 07:50:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 86.0 |
| 2e08e95b-cbed-310d-b3d6-d13ef4fcefe4 | -17.6073 | -57.5099 | 2024-11-11 07:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 83.0 |
| 8f0c466a-899d-39ac-b156-91d13e5a1bf0 | -17.6463 | -57.5257 | 2024-11-11 07:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 80.6 |


[Clique aqui para ver as próximas entradas](README48.md)
