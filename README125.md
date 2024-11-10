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

## Dados Diários - Página 125

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ed0e0bb5-e2ab-3471-9ae9-369e4cd81ed9 | -23.9095 | -54.0606 | 2024-11-10 10:40:00 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 175.0 |
| eaf46bc5-42bb-35e9-b357-5566d60ccd32 | -17.6266 | -57.5281 | 2024-11-10 10:40:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 126.0 |
| 3ab91c58-1290-3ac8-9b0f-66fd7ec0b79e | -23.9306 | -54.0564 | 2024-11-10 10:40:00 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 124.1 |
| c8716cf9-c645-3148-82ab-52e275658262 | -17.6069 | -57.5304 | 2024-11-10 10:40:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 235.2 |
| 512c3311-cee5-38c9-8820-02773c1f0ecf | -17.627 | -57.5075 | 2024-11-10 10:40:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 90.1 |
| 790ad071-c648-32cd-93db-a306a44b9bea | -17.6073 | -57.5099 | 2024-11-10 10:40:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 208.0 |
| 0c9b0764-1091-3754-8ee9-193cc30b5d09 | -1.5115 | -55.0142 | 2024-11-10 10:50:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 73.4 |
| 431c4cf2-74d1-3885-aaf3-d488c4f09dd4 | -17.6266 | -57.5281 | 2024-11-10 10:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 130.0 |
| f5669b08-cf56-3621-83a0-831724ca40c9 | -17.2933 | -57.4857 | 2024-11-10 10:50:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 88.6 |
| 18232aaa-d59b-3cab-8201-9173be9bdaf6 | -23.9089 | -54.083 | 2024-11-10 10:50:00 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 127.4 |
| cc35cc80-a845-3784-85e6-7c709746bf13 | -23.9095 | -54.0606 | 2024-11-10 10:50:00 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 183.8 |
| d24aa734-4c6d-3ef9-afff-b19b8b11da37 | -17.6073 | -57.5099 | 2024-11-10 10:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 169.6 |
| 0fd982b0-dc41-3348-995e-7855c6fe3ea0 | -1.5299 | -54.9941 | 2024-11-10 10:50:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 115.6 |
| 365a1439-2576-30c9-84b0-c19731649b68 | -17.627 | -57.5075 | 2024-11-10 10:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 113.3 |
| c60bded3-f008-3545-8d89-a2b53249e1a3 | -17.6069 | -57.5304 | 2024-11-10 10:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 179.0 |
| 8c6f486d-c88e-31b3-809b-19ff4499494b | -1.5116 | -54.9944 | 2024-11-10 10:50:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 136.5 |
| bfc46ee2-8dbc-3507-a94c-f5607927c01e | -23.9095 | -54.0606 | 2024-11-10 11:00:00 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 150.7 |
| 3c98bbcf-1875-3f69-a86b-76ede6b39394 | -17.6266 | -57.5281 | 2024-11-10 11:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 127.0 |
| df0ceb65-5d86-362d-a893-1475bac6fe28 | -1.5116 | -54.9944 | 2024-11-10 11:00:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 135.3 |
| da8aefe0-ff56-3a33-a55b-160b5fb89613 | -17.6073 | -57.5099 | 2024-11-10 11:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 179.5 |
| 114701b9-dc01-3726-8625-742faf1d7a7b | -23.9089 | -54.083 | 2024-11-10 11:00:00 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 93.3 |
| 46fea3f5-36d4-3f73-be6d-c33dda0179d8 | -1.5299 | -54.9941 | 2024-11-10 11:00:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 119.9 |
| b7012910-9e0a-3e6f-a67f-3bc161c219e5 | -17.627 | -57.5075 | 2024-11-10 11:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 117.9 |
| 8688cf7b-2b60-3c60-b053-75bbbd4846d7 | -17.2933 | -57.4857 | 2024-11-10 11:00:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 83.6 |
| 35688caf-e588-3357-962c-598a6d241ac5 | -6.13 | -42.57 | 2024-11-10 11:00:00 | MSG-03 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 500e0831-d124-3e55-a51a-d8e1805204b2 | -6.16 | -42.58 | 2024-11-10 11:00:00 | MSG-03 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| a69b6731-009a-349a-baa2-1b25f92e87c9 | -17.627 | -57.5075 | 2024-11-10 11:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 113.9 |
| 9f315f58-04cc-313c-b15f-dbe46cbcdf85 | -17.6266 | -57.5281 | 2024-11-10 11:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 146.3 |
| 0c688f08-18d9-3cac-b02e-d4418dad49da | -23.9095 | -54.0606 | 2024-11-10 11:10:00 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 149.8 |
| bb0568e0-8542-3a8b-a975-a7a1e4f0dcb8 | -17.2933 | -57.4857 | 2024-11-10 11:10:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 80.3 |
| 19796567-621e-39ce-80dc-1c6cf71eea42 | -23.9089 | -54.083 | 2024-11-10 11:10:00 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 102.8 |
| 32955a09-8030-3bfb-b2b4-7c7310c895a6 | -1.5299 | -54.9941 | 2024-11-10 11:10:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 102.4 |
| a921f14f-5708-3fb9-adf6-0e45f12c7d0b | -1.5116 | -54.9944 | 2024-11-10 11:10:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 139.5 |
| 8ec013b9-e1d5-33ea-8064-523c7ead9476 | -17.6073 | -57.5099 | 2024-11-10 11:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 212.5 |
| 3d93e456-0795-3c14-93b3-25f3d7becfd3 | -23.9089 | -54.083 | 2024-11-10 11:20:00 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 114.3 |
| a30c8b54-ffbb-349c-a607-20871e686911 | -17.2933 | -57.4857 | 2024-11-10 11:20:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 95.2 |
| b3a6afbc-4b80-3dd0-8ae5-9796970b203e | -1.5116 | -54.9944 | 2024-11-10 11:20:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 162.5 |
| 9bab10a1-c36b-3a7e-af44-41a062f96286 | -23.9095 | -54.0606 | 2024-11-10 11:20:00 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 177.0 |
| d151f079-269b-3c4e-83f9-8e25c0e8dad4 | -17.5872 | -57.5328 | 2024-11-10 11:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 87.5 |
| 82336714-b0dd-3baf-a132-0c67830d26d8 | -17.627 | -57.5075 | 2024-11-10 11:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 132.4 |
| ff45470c-ef07-3c52-8f1e-520d4687819d | -1.5299 | -54.9941 | 2024-11-10 11:20:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 114.4 |
| 279f913b-4987-362b-a852-7fd71d69ee13 | -17.6073 | -57.5099 | 2024-11-10 11:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 183.6 |
| 86318d98-3b5f-34ac-a0b7-c068a91ea5be | -17.6266 | -57.5281 | 2024-11-10 11:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 156.0 |
| ebf06471-369a-3f11-a92e-9f48d4f4a769 | -17.2933 | -57.4857 | 2024-11-10 11:30:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 85.6 |
| 4750a6bc-a40a-3f2a-87a8-fb7bcdebe8c3 | -1.5299 | -54.9941 | 2024-11-10 11:30:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 177.4 |
| 6355ddd4-a4bf-39ff-beef-0625c18b0b1d | -17.6266 | -57.5281 | 2024-11-10 11:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 154.5 |
| 240be62d-8c79-3c7f-a7f2-83359e254200 | -17.627 | -57.5075 | 2024-11-10 11:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 122.2 |
| 104e2e1b-c04a-3929-8f0a-85296d8d92fe | -1.5116 | -54.9944 | 2024-11-10 11:30:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 92.2 |
| 6def515f-cf60-3039-b1a8-44b47ca357ae | -23.9095 | -54.0606 | 2024-11-10 11:30:00 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 137.9 |
| ab3ce550-6ab2-3a48-ab1e-60dadec9c75c | -23.9089 | -54.083 | 2024-11-10 11:30:00 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 138.8 |
| 08ef6521-a648-30b4-a7c8-a028e8d52752 | -17.6073 | -57.5099 | 2024-11-10 11:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 211.7 |
| 16b433ca-6cd7-3bff-ab25-9ffaff0d3501 | -23.9095 | -54.0606 | 2024-11-10 11:40:00 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 120.6 |
| 0737d12d-4bf2-314b-9f1e-bc1a4fa120aa | -17.6266 | -57.5281 | 2024-11-10 11:40:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 215.9 |
| 53b4c30f-ee5f-3dcd-af0f-2077fc6eec3c | -17.627 | -57.5075 | 2024-11-10 11:40:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 183.9 |
| f0ef863b-3ef7-381b-b914-9dff3c9d8ac0 | -23.9089 | -54.083 | 2024-11-10 11:40:00 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 129.0 |
| eb03831b-1c00-3ba4-9749-79c31bfb6215 | -17.2933 | -57.4857 | 2024-11-10 11:40:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 95.6 |
| f786c4ef-1467-37e9-a0aa-35a92a4c656c | -1.5299 | -54.9941 | 2024-11-10 11:40:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 104.7 |
| 566781ad-489b-33ae-9310-64345b330cfe | -17.6073 | -57.5099 | 2024-11-10 11:40:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 233.0 |
| afef7017-69d4-3a0d-9283-e0e39d6c35ce | -1.5116 | -54.9944 | 2024-11-10 11:40:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 88.4 |
| 69971229-2d29-3ac1-ba22-fca9f23b3d3e | -17.627 | -57.5075 | 2024-11-10 11:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 155.6 |
| 92bf8f37-fd42-39a0-b8f8-e6c4bac3a3f0 | -1.5116 | -54.9944 | 2024-11-10 11:50:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 105.6 |
| 82483134-dec5-30be-b965-f99ad06e249f | -17.2933 | -57.4857 | 2024-11-10 11:50:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 89.2 |
| 2c2c06cb-bed7-3e8f-8cd1-675b29f281d4 | -1.5299 | -54.9941 | 2024-11-10 11:50:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 123.2 |
| 095215f6-017b-3b54-8c12-5d931bb5023d | -23.9095 | -54.0606 | 2024-11-10 11:50:00 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 114.8 |
| 2cf11778-c684-35fc-a447-172470486a5f | -23.9089 | -54.083 | 2024-11-10 11:50:00 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 105.8 |
| 149bd014-fd6f-3a25-86a8-aef0ec359ebc | -17.5872 | -57.5328 | 2024-11-10 11:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 73.0 |
| dace9988-954d-3b30-b95f-56a320c66a55 | -17.6073 | -57.5099 | 2024-11-10 11:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 239.6 |
| eac1e530-a208-31b7-b661-9f74027a0e8b | -1.5116 | -54.9944 | 2024-11-10 12:00:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 113.4 |
| 294cddcc-b8a6-3da8-aa52-66c57a110695 | -1.5299 | -54.9941 | 2024-11-10 12:00:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 140.4 |
| a9cb4296-a40f-3089-9c90-42edb72508ab | -1.476 | -54.3166 | 2024-11-10 12:00:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 118.1 |
| 5aa0d569-7b52-391b-8766-65dd9f8c8758 | -17.2933 | -57.4857 | 2024-11-10 12:00:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 114.2 |
| 54c92a30-90dc-35bf-ae9f-3982721c98a8 | -17.627 | -57.5075 | 2024-11-10 12:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 181.9 |
| 0fa152d9-fa80-350f-89ad-e9ea1e44b611 | -17.6073 | -57.5099 | 2024-11-10 12:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 226.2 |
| 78819672-dc76-3194-aa6a-817898ffa2a7 | -23.9095 | -54.0606 | 2024-11-10 12:00:00 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 214.9 |
| 87728abd-befb-3498-a0fc-ee8fe5dfbe76 | -23.9089 | -54.083 | 2024-11-10 12:00:00 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 177.8 |
| 4b7885ba-ff6c-3d29-963c-f9ac5e4d28b3 | -1.476 | -54.2965 | 2024-11-10 12:00:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 88.7 |
| 247106c1-4bd7-31b7-a81c-a98c1cee2225 | -17.5872 | -57.5328 | 2024-11-10 12:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 94.3 |
| a85592a1-a39d-301f-a386-680b0cd19fa2 | -6.13 | -42.62 | 2024-11-10 12:00:00 | MSG-03 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 1cbb00e2-bcb8-34cd-92a2-e275a66f4964 | -6.13 | -42.57 | 2024-11-10 12:00:00 | MSG-03 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| eba848da-686a-3d95-92e2-2eff5c5a10ee | -8.42 | -44.17 | 2024-11-10 12:00:00 | MSG-03 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 6e82c9db-c559-3b81-883a-cd2b5158ae00 | -6.16 | -42.58 | 2024-11-10 12:00:00 | MSG-03 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 8705b3bd-b8ab-31ed-b5dc-2181dc7b8118 | -8.39 | -44.12 | 2024-11-10 12:00:00 | MSG-03 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 9e85b087-b80c-3488-914e-f011cf52814a | -8.39 | -44.16 | 2024-11-10 12:00:00 | MSG-03 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| addda120-17b2-3f31-a2e0-b5a4be00df5e | -3.979 | -42.08009 | 2024-11-10 12:01:00 | TERRA_M-T | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 17.8 |
| d464946a-41b4-3ea5-9ccb-48d6a2aae55c | -3.98145 | -42.06411 | 2024-11-10 12:01:00 | TERRA_M-T | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 35.2 |
| 7af62463-3390-36f2-8f9c-c7601a75df9c | -3.57141 | -42.17884 | 2024-11-10 12:01:00 | TERRA_M-T | MORRO DO CHAPÉU DO PIAUÍ | PIAUÍ | Brasil | 2206670 | 22 | 33 | nan | nan | nan | Caatinga | 42.5 |
| 8a366aa4-582d-3378-9f7a-6e3fe2c96d04 | -3.4018 | -41.48791 | 2024-11-10 12:01:00 | TERRA_M-T | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 25.7 |
| bc1e81ee-0832-39e7-b526-9eaef6030b85 | -3.40083 | -41.49432 | 2024-11-10 12:01:00 | TERRA_M-T | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 27.9 |
| 96e54535-acb9-3c84-8b5e-1a0e4465eda3 | -3.52308 | -44.02464 | 2024-11-10 12:01:00 | TERRA_M-T | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 28.0 |
| 693d4e1d-408b-3919-b065-c93bce456cdb | -3.56539 | -42.17182 | 2024-11-10 12:01:00 | TERRA_M-T | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 47.6 |
| d690d09c-11aa-30a2-988b-d25cbaca64c9 | -4.12733 | -43.5868 | 2024-11-10 12:01:00 | TERRA_M-T | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 4272afaf-216a-3f26-a3c2-965108c3a377 | -6.11992 | -38.90264 | 2024-11-10 12:04:00 | TERRA_M-T | JAGUARIBE | CEARÁ | Brasil | 2306900 | 23 | 33 | nan | nan | nan | Caatinga | 55.0 |
| 4cadc079-9bcf-3070-acca-f86b4ace1998 | -8.38611 | -44.14647 | 2024-11-10 12:04:00 | TERRA_M-T | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 333.6 |
| c9d0ee70-8810-3b41-8fc0-fa88b21cfefb | -10.9086 | -40.20425 | 2024-11-10 12:04:00 | TERRA_M-T | PONTO NOVO | BAHIA | Brasil | 2925253 | 29 | 33 | nan | nan | nan | Caatinga | 10.3 |
| 92d950b7-9d9f-309e-b10a-24eae2bd690b | -8.80656 | -41.40018 | 2024-11-10 12:04:00 | TERRA_M-T | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 16.3 |
| 37785342-f2cd-3081-b841-1af92639cff7 | -9.12985 | -37.62031 | 2024-11-10 12:04:00 | TERRA_M-T | CANAPI | ALAGOAS | Brasil | 2701605 | 27 | 33 | nan | nan | nan | Caatinga | 8.6 |
| 2752da0e-9a17-3ef0-b201-6548237f5642 | -6.11851 | -38.91213 | 2024-11-10 12:04:00 | TERRA_M-T | ORÓS | CEARÁ | Brasil | 2309508 | 23 | 33 | nan | nan | nan | Caatinga | 9.0 |
| 8eae9a63-aeb5-373a-b310-56ce9804a020 | -5.56432 | -43.97064 | 2024-11-10 12:04:00 | TERRA_M-T | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 28.5 |
| b3f0d414-c09d-30d8-981d-42e140cc98ee | -8.63182 | -41.07051 | 2024-11-10 12:04:00 | TERRA_M-T | AFRÂNIO | PERNAMBUCO | Brasil | 2600203 | 26 | 33 | nan | nan | nan | Caatinga | 11.3 |
| a0ef2ce1-2c35-3b5c-b1a0-93e0c20dbf97 | -6.13687 | -42.56978 | 2024-11-10 12:04:00 | TERRA_M-T | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 71.3 |


[Clique aqui para ver as próximas entradas](README126.md)
