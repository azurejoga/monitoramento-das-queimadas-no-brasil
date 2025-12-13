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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 33cdb3b3-3569-39d3-82fc-a45f2fb4223a | -3.1822 | -41.8448 | 2025-12-13 02:10:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 78.6 |
| c6245071-b122-369a-bc27-14c1c3122733 | -3.182 | -41.8687 | 2025-12-13 02:10:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 65.1 |
| 9fa05da6-b005-3394-ac20-99970271f7f6 | -3.2196 | -41.8431 | 2025-12-13 02:10:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 102.5 |
| 0842a43d-493e-3c7d-9564-39df27ef8d1f | -3.2009 | -41.844 | 2025-12-13 02:10:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 271.5 |
| c28ba6e7-5066-387f-b724-a7c22dbbc2e7 | -3.2194 | -41.867 | 2025-12-13 02:10:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 80.7 |
| 8c60fc41-beda-32f2-8645-d0822490288d | -2.4869 | -47.7909 | 2025-12-13 02:10:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 49.5 |
| 9bf6283e-46f6-3831-bf45-66447799eef8 | -2.487 | -47.7692 | 2025-12-13 02:10:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 80.2 |
| 15c1a958-b7a4-3647-a816-24f439508dda | -3.2007 | -41.8678 | 2025-12-13 02:10:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 205.0 |
| 7913d0d2-402f-34fe-9e52-5cdcf4251ae4 | -3.2196 | -41.8431 | 2025-12-13 02:20:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 109.2 |
| 8a916572-e708-3733-9e82-216660a32408 | -3.1822 | -41.8448 | 2025-12-13 02:20:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 71.3 |
| 030a5da5-7fdc-3714-988b-c5037d55a269 | -3.182 | -41.8687 | 2025-12-13 02:20:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 62.8 |
| d5a6ca53-0c62-308f-8538-01dbc69b1542 | -2.487 | -47.7692 | 2025-12-13 02:20:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 80.7 |
| 6a43f689-3a33-3954-b3dc-1fb8a53dbc06 | -3.2007 | -41.8678 | 2025-12-13 02:20:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 194.9 |
| 880062e2-8d33-37bd-a9bf-1b54a0eca3c7 | -3.2009 | -41.844 | 2025-12-13 02:20:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 241.0 |
| 7b2e08ca-8749-3df2-85b2-e6161f9dce22 | -2.2646 | -47.8617 | 2025-12-13 02:20:00 | GOES-19 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 39.7 |
| c013f609-5b9f-310e-8fed-f4528c059a68 | -2.4869 | -47.7909 | 2025-12-13 02:20:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 46.6 |
| 6f32145c-bdbf-33ba-b7d5-0359a360ca51 | -3.2194 | -41.867 | 2025-12-13 02:20:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 90.4 |
| d7d21df9-63b4-3260-82c6-a92b4b440c85 | -3.1822 | -41.8448 | 2025-12-13 02:30:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 63.9 |
| 47323e28-4c76-314d-b344-05ad81d1d932 | -8.0324 | -43.1022 | 2025-12-13 02:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 302.4 |
| f888b919-610f-3d50-a0a6-965ee7c47848 | -8.051 | -43.1237 | 2025-12-13 02:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 75.3 |
| dbca0197-27c5-3549-84f3-9ac0bfde109d | -8.0513 | -43.1001 | 2025-12-13 02:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 142.2 |
| e27e14d6-6d7e-31c3-8c18-15ccf3d22f88 | -8.0321 | -43.1257 | 2025-12-13 02:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 137.4 |
| 4f9128f9-9d37-3c98-b347-188fa56582c7 | -2.487 | -47.7692 | 2025-12-13 02:30:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 56.9 |
| 213290a3-dc14-3413-b402-06fa493085e8 | -3.2007 | -41.8678 | 2025-12-13 02:30:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 246.8 |
| 0aae4358-b23b-32e4-ab76-963243b41a53 | -3.182 | -41.8687 | 2025-12-13 02:30:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 63.7 |
| 5fdba0fd-783d-3956-94bd-7d63cfe8efcf | -3.2194 | -41.867 | 2025-12-13 02:30:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 80.8 |
| 01fa6a9d-e648-3fed-8e7a-01a2bfff2236 | -3.2196 | -41.8431 | 2025-12-13 02:30:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 83.9 |
| 0c919adf-ff9a-3d78-bcfc-aad58e9bbe7d | -8.0327 | -43.0786 | 2025-12-13 02:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 71.2 |
| d5deffd8-60b1-3c9e-8345-f996bbb27ebe | -3.2009 | -41.844 | 2025-12-13 02:30:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 264.5 |
| 05be6b9a-f928-36e5-9439-263646f488ae | -3.1822 | -41.8448 | 2025-12-13 02:40:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 89.1 |
| cd1af3ea-ea28-3d2e-a2a2-db148c5644f2 | -3.2194 | -41.867 | 2025-12-13 02:40:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 88.2 |
| 9cd5e4d1-ee1c-3adf-ab6d-fab364c1d0e6 | -3.2007 | -41.8678 | 2025-12-13 02:40:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 182.7 |
| 9bd8e3ef-aa37-38c4-8a13-9bf7698f8721 | -3.2196 | -41.8431 | 2025-12-13 02:40:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 124.8 |
| 845a3681-10f8-37be-9296-12d746e3150c | -3.182 | -41.8687 | 2025-12-13 02:40:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 69.0 |
| 520427cb-8898-3446-abc0-242321876bd7 | -3.2009 | -41.844 | 2025-12-13 02:40:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 265.1 |
| 29d225bb-78d6-398f-95e8-8d80040533bf | -3.1822 | -41.8448 | 2025-12-13 02:50:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 72.0 |
| 9a7212cf-aa99-3b70-86e5-7247ad7711d7 | -8.0327 | -43.0786 | 2025-12-13 02:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 51.3 |
| d66a4c04-35e7-3ef1-ace5-421731aea89e | -3.182 | -41.8687 | 2025-12-13 02:50:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 76.4 |
| 87abb94b-d765-3f0d-b266-0f24997c94f8 | -10.235 | -52.2263 | 2025-12-13 02:50:00 | GOES-19 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 20560e73-448e-3ba3-9b3a-2a9cebe5b3c2 | -8.0324 | -43.1022 | 2025-12-13 02:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 224.2 |
| 9eb592d1-dd32-39fc-94c4-e8915767db15 | -3.2194 | -41.867 | 2025-12-13 02:50:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 104.1 |
| 2046b1de-2ed2-3044-95ea-13bb79023168 | -3.2007 | -41.8678 | 2025-12-13 02:50:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 212.8 |
| 303a57f5-bad3-301c-968e-a82ab442fc25 | -8.0513 | -43.1001 | 2025-12-13 02:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 145.7 |
| cb56699a-5896-32e4-a378-3f990e083381 | -3.2196 | -41.8431 | 2025-12-13 02:50:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 105.6 |
| 01e32d0c-7b0d-3b05-a4c4-c63b02b32d39 | -8.0321 | -43.1257 | 2025-12-13 02:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 106.4 |
| c02b75c7-2526-3b05-8641-fda13720ebd3 | -3.2009 | -41.844 | 2025-12-13 02:50:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 206.1 |
| 019af77c-23e2-3f1e-997f-140943fd3ff5 | -8.051 | -43.1237 | 2025-12-13 02:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 79.3 |
| bfd2162f-5a20-37da-b8df-9f297c7741e9 | -8.0135 | -43.1042 | 2025-12-13 02:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 64.1 |
| b832f947-04ae-3fc6-bf60-12166b43e2e6 | -10.0042 | -36.4623 | 2025-12-13 03:00:00 | GOES-19 | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 245.0 |
| b95cd61d-82b1-370d-bb41-64b3429913dc | -8.0513 | -43.1001 | 2025-12-13 03:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 145.8 |
| b4fc2482-5ba8-349c-9941-b6a23bfcf977 | -8.0321 | -43.1257 | 2025-12-13 03:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 88.8 |
| f5fe074d-be90-3cf0-8ee7-36f9782af840 | -8.0135 | -43.1042 | 2025-12-13 03:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 61.0 |
| 2b2f52bc-1ae4-3fc5-b075-15e662b0c7cd | -2.8669 | -45.4406 | 2025-12-13 03:00:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 09906e5c-1f8c-33e7-bf21-534415399615 | -10.0047 | -36.4353 | 2025-12-13 03:00:00 | GOES-19 | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 59.9 |
| e65bddfe-d47b-3f10-9b22-20a53465345f | -3.2009 | -41.844 | 2025-12-13 03:00:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 215.4 |
| 6b5dcd6f-f678-3d42-b0fd-15cb1039e272 | -3.2194 | -41.867 | 2025-12-13 03:00:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 97.0 |
| 724368b4-22b9-371f-b7ac-83105d86060e | -3.182 | -41.8687 | 2025-12-13 03:00:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 75.9 |
| ee92b9a8-73fe-305b-aa8d-63c63253059a | -3.2007 | -41.8678 | 2025-12-13 03:00:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 203.3 |
| 4fea1bbb-3820-31d2-968d-a0aefaf13924 | -8.0324 | -43.1022 | 2025-12-13 03:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 217.0 |
| 209621f2-d0dc-31cd-bc1f-c2ece3538637 | -10.0037 | -36.4892 | 2025-12-13 03:00:00 | GOES-19 | SÃO SEBASTIÃO | ALAGOAS | Brasil | 2708808 | 27 | 33 | nan | nan | nan | Mata Atlântica | 111.4 |
| 92865e12-90f9-34a1-ac70-4e737f1f4386 | -3.1822 | -41.8448 | 2025-12-13 03:00:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 76.7 |
| 7118e9e5-da40-3e50-9263-1ae2d959cd4d | -10.0235 | -36.4589 | 2025-12-13 03:00:00 | GOES-19 | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 119.8 |
| aa1e57bf-a359-325a-ae73-13ec54018c8d | -2.8854 | -45.44 | 2025-12-13 03:00:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 43.5 |
| 468ffd97-b2e6-3701-8a40-71adf2f69c22 | -2.487 | -47.7692 | 2025-12-13 03:00:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 52.6 |
| ff32cca0-d426-38c6-b9fd-5d97c45d2325 | -8.051 | -43.1237 | 2025-12-13 03:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 68.1 |
| 6a35b61a-ecc0-3259-94b8-05f8dc178233 | -2.8668 | -45.4631 | 2025-12-13 03:00:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 46.9 |
| 124e2273-8421-3948-82ab-45877b46ee86 | -3.2196 | -41.8431 | 2025-12-13 03:00:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 102.8 |
| f72cadeb-711d-3a86-b673-7d857b4c7ace | -2.487 | -47.7692 | 2025-12-13 03:10:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 55.5 |
| a9cd89cc-13c9-3440-939e-5168e8674224 | -3.2196 | -41.8431 | 2025-12-13 03:10:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 89.6 |
| b54ac448-cd03-3141-81b8-4bb892e3f628 | -3.2194 | -41.867 | 2025-12-13 03:10:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 88.3 |
| 249b8902-2077-36f4-b539-4791b98bb693 | -3.2007 | -41.8678 | 2025-12-13 03:10:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 204.6 |
| 1f8ceab3-b16b-3834-a8db-3eabce5ecc5d | -3.182 | -41.8687 | 2025-12-13 03:10:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 81.0 |
| 41eaf2b1-6a37-3b45-a285-8eb8204a6a1d | -8.0324 | -43.1022 | 2025-12-13 03:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 108.6 |
| 502420c8-5a30-367c-aa98-ebafb9b5358e | -3.1822 | -41.8448 | 2025-12-13 03:10:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 74.7 |
| e9f46381-ee36-38a6-96b0-ca81dedc7050 | -8.051 | -43.1237 | 2025-12-13 03:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 49.2 |
| 26a2cef0-320b-3611-a1fe-24d6ea221845 | -8.0321 | -43.1257 | 2025-12-13 03:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 56.1 |
| 6f944e1f-2442-31b1-8b1c-473eda49db2e | -8.0513 | -43.1001 | 2025-12-13 03:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 82.2 |
| 513df362-df5c-359a-b11c-08a03a079ff7 | -3.2009 | -41.844 | 2025-12-13 03:10:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 193.4 |
| a66b8127-0850-3acb-a503-aecc8cbd2222 | -6.6635 | -37.27531 | 2025-12-13 03:10:00 | NOAA-21 | SÃO JOÃO DO SABUGI | RIO GRANDE DO NORTE | Brasil | 2412104 | 24 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 09ef70e6-4f6b-3b2b-9bfc-4f4d7872e0c1 | -6.66252 | -37.27274 | 2025-12-13 03:10:00 | NOAA-21 | SÃO JOÃO DO SABUGI | RIO GRANDE DO NORTE | Brasil | 2412104 | 24 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 1ecee337-ef45-3f90-8c3a-9051a427f4e1 | -7.14787 | -35.09154 | 2025-12-13 03:10:00 | NOAA-21 | CRUZ DO ESPÍRITO SANTO | PARAÍBA | Brasil | 2504900 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| e4f81102-c835-337f-97d5-bff045f44ecf | -6.65762 | -37.26804 | 2025-12-13 03:10:00 | NOAA-21 | SÃO JOÃO DO SABUGI | RIO GRANDE DO NORTE | Brasil | 2412104 | 24 | 33 | nan | nan | nan | Caatinga | 2.4 |
| b7a4e7a8-db94-34ac-aceb-a14cde638c57 | -6.65856 | -37.27064 | 2025-12-13 03:10:00 | NOAA-21 | SÃO JOÃO DO SABUGI | RIO GRANDE DO NORTE | Brasil | 2412104 | 24 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 11c144b3-8f70-35f2-8bc5-c428e243ad6f | -5.31744 | -38.00305 | 2025-12-13 03:10:00 | NOAA-21 | TABULEIRO DO NORTE | CEARÁ | Brasil | 2313104 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 02526b9b-eb16-32da-8df5-bd03211444da | -4.70653 | -37.77519 | 2025-12-13 03:10:00 | NOAA-21 | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 9.2 |
| 474be5a9-3700-3276-b760-ebc25eecf358 | -5.36531 | -35.54649 | 2025-12-13 03:10:00 | NOAA-21 | PUREZA | RIO GRANDE DO NORTE | Brasil | 2410405 | 24 | 33 | nan | nan | nan | Caatinga | 1.7 |
| c61b68d1-9453-3de6-ab77-b756402e057d | -6.66414 | -37.27163 | 2025-12-13 03:10:00 | NOAA-21 | SÃO JOÃO DO SABUGI | RIO GRANDE DO NORTE | Brasil | 2412104 | 24 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 7b9f394e-3e00-30f8-9133-9bf0a817dddd | -7.1483 | -35.08845 | 2025-12-13 03:10:00 | NOAA-21 | CRUZ DO ESPÍRITO SANTO | PARAÍBA | Brasil | 2504900 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 8fe1d09d-5170-33ec-bc20-23b3cbcca718 | -6.7831 | -39.63241 | 2025-12-13 03:12:00 | NOAA-21 | TARRAFAS | CEARÁ | Brasil | 2313252 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| ccf93ff7-eb16-3c96-8457-605ed96a3716 | -10.29476 | -37.8083 | 2025-12-13 03:12:00 | NOAA-21 | CORONEL JOÃO SÁ | BAHIA | Brasil | 2909208 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| b5257472-7889-3dae-af74-6bb90df54923 | -7.63378 | -34.85374 | 2025-12-13 03:12:00 | NOAA-21 | GOIANA | PERNAMBUCO | Brasil | 2606200 | 26 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 5f9dc000-02cb-35a1-9941-41bdff77f07b | -7.63846 | -34.85448 | 2025-12-13 03:12:00 | NOAA-21 | GOIANA | PERNAMBUCO | Brasil | 2606200 | 26 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 4bd86450-2a83-3d4d-87cc-f275318c7397 | -12.31454 | -37.92312 | 2025-12-13 03:12:00 | NOAA-21 | ENTRE RIOS | BAHIA | Brasil | 2910503 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| ce7700b7-655c-3d7a-9cde-46e90b51ef6b | -10.01153 | -36.46795 | 2025-12-13 03:12:00 | NOAA-21 | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 32.6 |
| 1735e9b4-e32f-32d8-8187-17c64edddfa7 | -10.01205 | -36.46508 | 2025-12-13 03:12:00 | NOAA-21 | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 18.7 |
| bf651a77-e9f1-3304-a93c-714f3e21c6e8 | -10.73347 | -36.94429 | 2025-12-13 03:12:00 | NOAA-21 | SANTO AMARO DAS BROTAS | SERGIPE | Brasil | 2806602 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| e9023a2a-4716-398a-8109-93ca00993fbe | -7.63291 | -34.85863 | 2025-12-13 03:12:00 | NOAA-21 | GOIANA | PERNAMBUCO | Brasil | 2606200 | 26 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| 08ddd6fb-60cc-39bc-8cdf-dc8040a80c78 | -7.63762 | -34.85925 | 2025-12-13 03:12:00 | NOAA-21 | GOIANA | PERNAMBUCO | Brasil | 2606200 | 26 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| a5aa8c64-42f4-391a-a6e3-6d39a8c87472 | -6.78304 | -39.62993 | 2025-12-13 03:12:00 | NOAA-21 | TARRAFAS | CEARÁ | Brasil | 2313252 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 6f0e9734-7e93-30f3-9297-b8212e492df2 | -10.01257 | -36.46221 | 2025-12-13 03:12:00 | NOAA-21 | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 18.7 |


[Clique aqui para ver as próximas entradas](README4.md)
