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
| 6ad2a047-f97c-3bc1-a80e-3b3eeb3797c6 | -27.53173 | -50.83677 | 2025-12-05 01:06:00 | TERRA_M-M | SÃO JOSÉ DO CERRITO | SANTA CATARINA | Brasil | 4216800 | 42 | 33 | nan | nan | nan | Mata Atlântica | 10.2 |
| 0a40cbf3-34a3-3488-ba49-96957a5d6a10 | -23.62575 | -51.66901 | 2025-12-05 01:06:00 | TERRA_M-M | JANDAIA DO SUL | PARANÁ | Brasil | 4112108 | 41 | 33 | nan | nan | nan | Mata Atlântica | 13.0 |
| e653b9f5-8516-383a-80eb-6dc73a21addf | -21.36921 | -48.53771 | 2025-12-05 01:06:00 | TERRA_M-M | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 46.0 |
| 6eaed2d0-978d-3266-b871-0c8819481779 | -27.53428 | -50.85143 | 2025-12-05 01:06:00 | TERRA_M-M | SÃO JOSÉ DO CERRITO | SANTA CATARINA | Brasil | 4216800 | 42 | 33 | nan | nan | nan | Mata Atlântica | 8.7 |
| 18dbf329-d9d1-384a-92c4-04e91ee9c621 | -20.9247 | -56.38343 | 2025-12-05 01:09:00 | TERRA_M-M | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 12.9 |
| f69dc9cf-f39e-37b4-aa7b-08cb412095c8 | -21.35167 | -56.8627 | 2025-12-05 01:09:00 | TERRA_M-M | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 4629e2b1-7f35-36d5-928d-47f27ad6683a | -21.62665 | -56.13861 | 2025-12-05 01:09:00 | TERRA_M-M | JARDIM | MATO GROSSO DO SUL | Brasil | 5005004 | 50 | 33 | nan | nan | nan | Cerrado | 27.7 |
| 2e8e8a1d-0690-3e16-b262-7d7d19c7fa1a | -19.97858 | -57.44997 | 2025-12-05 01:09:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.4 |
| ee42c905-c660-35c0-9ada-bc8375f3df70 | -21.62526 | -56.12895 | 2025-12-05 01:09:00 | TERRA_M-M | JARDIM | MATO GROSSO DO SUL | Brasil | 5005004 | 50 | 33 | nan | nan | nan | Cerrado | 48.8 |
| 2adc4985-eede-3d92-aee9-a0b5fb7839d9 | -20.92333 | -56.37387 | 2025-12-05 01:09:00 | TERRA_M-M | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 90248f08-17a6-3d0d-8ec3-a61da3e23c91 | -19.97987 | -57.45935 | 2025-12-05 01:09:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 18.8 |
| fcff3f7a-bc47-31a3-a698-c5d296e52ff7 | -20.91578 | -56.38492 | 2025-12-05 01:09:00 | TERRA_M-M | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 24.1 |
| 0505d837-ddaa-3c1e-8567-ed499184bfa5 | -20.00544 | -55.76439 | 2025-12-05 01:09:00 | TERRA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 6.3 |
| 3ab403b9-a690-3000-a05c-82b9ecfb4b7f | -20.91441 | -56.37534 | 2025-12-05 01:09:00 | TERRA_M-M | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 10.9 |
| f3315c30-2dac-3d9b-8ef7-3ca64b4c213b | -6.6249 | -40.877 | 2025-12-05 01:10:00 | GOES-19 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 76.0 |
| fe849088-df10-3c8c-8480-fdb5b64e07cf | -6.0192 | -41.1278 | 2025-12-05 01:10:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 95.7 |
| 8d4776fb-36a5-3073-aff7-f20ee3d2a165 | -6.6627 | -40.8733 | 2025-12-05 01:10:00 | GOES-19 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 90.6 |
| f3773bda-3ef9-360c-83df-b2f43583545d | -5.1753 | -43.0756 | 2025-12-05 01:10:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 67.7 |
| 3ce29c2c-900a-32d5-a24b-6096c85a3fc6 | -6.019 | -41.1521 | 2025-12-05 01:10:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 91.3 |
| 0f71a621-0d08-3268-b8d8-aa19420e0afb | -6.6441 | -40.8507 | 2025-12-05 01:10:00 | GOES-19 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 146.3 |
| 4913ae7b-b9d8-3469-9227-8a9891c59dc8 | -6.6438 | -40.8751 | 2025-12-05 01:10:00 | GOES-19 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 195.3 |
| 9489f240-a29b-35c7-a2e6-01f734f9ca9c | -2.9049 | -45.2368 | 2025-12-05 01:10:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 83.0 |
| e235b185-f58c-3612-bf29-bd2ab010ca38 | -3.6223 | -43.3074 | 2025-12-05 01:10:00 | GOES-19 | MATA ROMA | MARANHÃO | Brasil | 2106409 | 21 | 33 | nan | nan | nan | Cerrado | 63.9 |
| 7801fa95-e6be-3e0c-b290-023c5ede089c | -6.0002 | -41.1538 | 2025-12-05 01:10:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 89.3 |
| 9f6028d2-4f72-3c90-83e0-b0a7184436ba | -6.0004 | -41.1295 | 2025-12-05 01:10:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 97.6 |
| fcbd7fa4-870e-3fe8-8ba8-d120fdeb6249 | -3.641 | -43.3065 | 2025-12-05 01:10:00 | GOES-19 | MATA ROMA | MARANHÃO | Brasil | 2106409 | 21 | 33 | nan | nan | nan | Cerrado | 75.0 |
| dd932abb-9908-3617-b653-a1b717a973ee | -5.194 | -43.0743 | 2025-12-05 01:10:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 64.0 |
| 340cd54a-4beb-3223-b7cb-2732e7f964fa | 1.95696 | -55.73954 | 2025-12-05 01:13:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 39.3 |
| 8b930e8d-1e8b-36aa-8a77-49b43dd38a7b | 1.95699 | -55.74601 | 2025-12-05 01:13:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 17.1 |
| f4513120-0382-3c76-b628-8bd3138d58b7 | 1.9597 | -55.72007 | 2025-12-05 01:13:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 22.1 |
| 41c9384c-44e6-3bcb-aacd-84b1f6d996d8 | -1.79055 | -54.01015 | 2025-12-05 01:13:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 28.1 |
| 3d76905d-703c-30de-998a-bd72a9c2ad84 | 1.95957 | -55.72652 | 2025-12-05 01:13:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 42.3 |
| e8526082-df6f-3f74-b82a-1eb520eb7d92 | -5.1751 | -43.099 | 2025-12-05 01:20:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 114.2 |
| 8cd69932-9259-3d59-a024-210b639c1d8d | -5.194 | -43.0743 | 2025-12-05 01:20:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 107.7 |
| d36edc7f-faa1-3c1c-9b08-66e6fc82e6e4 | -6.0004 | -41.1295 | 2025-12-05 01:20:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 80.6 |
| 2aacd86b-2565-3f35-bee2-590ef29eb5f7 | -6.6438 | -40.8751 | 2025-12-05 01:20:00 | GOES-19 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 147.8 |
| 6e641790-7981-395b-a90e-6c970225e36d | -6.0002 | -41.1538 | 2025-12-05 01:20:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 83.1 |
| e2401987-d1f9-3e6b-995b-2d5afeececd5 | -6.6627 | -40.8733 | 2025-12-05 01:20:00 | GOES-19 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 101.3 |
| 87d63544-ae7e-3289-bb9f-eb339b6c1f5e | -6.663 | -40.8488 | 2025-12-05 01:20:00 | GOES-19 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 82.0 |
| 8eb0ee1d-3bee-3ba0-ad9e-bf2be4e3eec6 | -5.1938 | -43.0977 | 2025-12-05 01:20:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 86.7 |
| 6891f551-dde7-3973-8e22-ec20e97909b8 | -5.1753 | -43.0756 | 2025-12-05 01:20:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 148.8 |
| 551b9756-4008-3609-9368-6200305f2570 | -6.0192 | -41.1278 | 2025-12-05 01:20:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 81.3 |
| 06b6c3f8-4bf4-30c1-8d31-25ba30dd8bcd | -2.9049 | -45.2368 | 2025-12-05 01:20:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 75.7 |
| 4ca74e7a-a95a-3b21-8854-02baadb93c9c | -6.6441 | -40.8507 | 2025-12-05 01:20:00 | GOES-19 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 113.4 |
| b206eaaa-e280-3948-a111-60a75059ca15 | -6.019 | -41.1521 | 2025-12-05 01:20:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 86.1 |
| ef82c39b-6e9b-3459-b830-ddf8d2c5e2d4 | -5.1751 | -43.099 | 2025-12-05 01:30:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 123.8 |
| 2f88e401-08b1-3e43-810c-33e6d5a83637 | -6.019 | -41.1521 | 2025-12-05 01:30:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 81.2 |
| aebb1bac-82f8-396e-979c-dabc56731d75 | -5.1753 | -43.0756 | 2025-12-05 01:30:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 153.1 |
| 5c11ed15-5551-3126-8172-8236f83036c4 | -3.4901 | -43.592 | 2025-12-05 01:30:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 57.9 |
| 4817f2e2-538a-39fe-b830-549e1fe96f4f | -5.194 | -43.0743 | 2025-12-05 01:30:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 113.4 |
| 5f47be0b-de95-3444-85ba-2623e44f9856 | -6.0002 | -41.1538 | 2025-12-05 01:30:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 80.7 |
| 89f66003-20c7-307f-848e-fa57080d83d0 | -5.1938 | -43.0977 | 2025-12-05 01:30:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 93.1 |
| 0fa651fb-dfab-3ad0-a1ca-a1e58e95d3ee | -2.9049 | -45.2368 | 2025-12-05 01:30:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 77.8 |
| 8700f473-ca2c-3484-88a7-48b770961fd5 | -6.6441 | -40.8507 | 2025-12-05 01:30:00 | GOES-19 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 88.7 |
| 46055984-1381-3c4c-9016-d7cd5e76c245 | -6.6438 | -40.8751 | 2025-12-05 01:30:00 | GOES-19 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 79.3 |
| fcadf5c8-a790-3525-8d18-d4857af4f2dc | -2.9049 | -45.2368 | 2025-12-05 01:40:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 78.4 |
| ae585496-3f73-3c5c-8084-05ec51a87ec0 | -5.194 | -43.0743 | 2025-12-05 01:40:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 87.2 |
| 0d8e27f4-914a-3d79-a6a2-863833cfb265 | -5.1753 | -43.0756 | 2025-12-05 01:40:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 144.6 |
| ee4476a9-2daa-33ce-9593-359c281e2209 | -5.1938 | -43.0977 | 2025-12-05 01:40:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 67.8 |
| d904e5e6-25ec-309f-895b-1d60d62cb43c | -3.4715 | -43.5929 | 2025-12-05 01:40:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 55.7 |
| fed4246e-46c2-38e8-846b-a44caee2c3da | -5.1751 | -43.099 | 2025-12-05 01:40:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 103.7 |
| 20123480-e39f-368d-8ccd-86264b3b710f | -5.1751 | -43.099 | 2025-12-05 01:50:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 77.3 |
| ba986bc4-e8dd-34da-9cf6-e3766645fe2b | -5.194 | -43.0743 | 2025-12-05 01:50:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 81.0 |
| c501f9f3-abd1-3e71-9408-8cab9d297194 | -3.4901 | -43.592 | 2025-12-05 01:50:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 52.3 |
| 3ccb68d2-375d-34e8-a295-5e68354fd629 | -5.1753 | -43.0756 | 2025-12-05 01:50:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 107.9 |
| ab4fa1fa-dab2-3718-bb13-27bcc186ddb5 | -2.9049 | -45.2368 | 2025-12-05 01:50:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 80.1 |
| 85d0e87e-89fa-308a-8150-fc39e8de9b75 | -2.9049 | -45.2368 | 2025-12-05 02:00:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 88.7 |
| 35968cab-ec6b-34ff-a97e-31a2767c94eb | -5.1751 | -43.099 | 2025-12-05 02:00:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 72.1 |
| 695ace42-f9cf-3e2f-acb0-a7266c87577f | -5.1753 | -43.0756 | 2025-12-05 02:00:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 89.1 |
| 83be4b53-4e90-39a8-a041-793f4e5f94ad | -5.194 | -43.0743 | 2025-12-05 02:00:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 63.0 |
| 982ecfb0-4702-343b-8bce-4f9e95abbddc | -3.4901 | -43.592 | 2025-12-05 02:00:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 63.9 |
| da38586f-ac8b-36e5-96b1-2d8582aa1cb8 | -6.0002 | -41.1538 | 2025-12-05 02:00:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 68.3 |
| eaaca539-1429-319a-8bed-ea3f6081752e | -3.4715 | -43.5929 | 2025-12-05 02:00:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 67.5 |
| af4eefbc-6619-3e75-a6ac-f188d5e50ee7 | -6.019 | -41.1521 | 2025-12-05 02:00:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 61.4 |
| 78f92743-3f6b-39a3-bd8d-62db2281dbcd | -6.0002 | -41.1538 | 2025-12-05 02:10:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 76.7 |
| bb683b49-1724-3d41-9a4d-b2e1dd7902c8 | -2.9049 | -45.2368 | 2025-12-05 02:10:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 136.5 |
| 83e75ae9-c32b-3f7c-903b-fac85dd405dc | -5.1751 | -43.099 | 2025-12-05 02:10:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 95.3 |
| 3d48f499-05ea-32ee-8284-2472928a6e1b | -5.194 | -43.0743 | 2025-12-05 02:10:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 69.9 |
| 33a6b1b3-bd90-3c86-9c87-4e1ce9403d1b | -2.9048 | -45.2594 | 2025-12-05 02:10:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 73de13f9-9d36-37f1-bd32-3100e09be7b8 | -2.8863 | -45.2375 | 2025-12-05 02:10:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 70.3 |
| df645e36-9752-3e4a-a7df-c682f918380f | -5.1753 | -43.0756 | 2025-12-05 02:10:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 129.8 |
| 946888e2-e377-3078-b37e-4de275dbdb3b | -5.3609 | -43.2727 | 2025-12-05 02:20:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 75.1 |
| ff842a3c-1456-370e-8225-675c2e63f501 | -5.1753 | -43.0756 | 2025-12-05 02:20:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 111.1 |
| 545524b3-eb29-3cf4-b472-459c1aa4e364 | -2.9049 | -45.2368 | 2025-12-05 02:20:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 185.1 |
| 4c3140fe-bec6-38cd-8be1-91dfa0eb9348 | -5.3422 | -43.2741 | 2025-12-05 02:20:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 66.9 |
| 4709577e-c5d3-3b93-b9a8-bac879c0b75a | -2.9048 | -45.2594 | 2025-12-05 02:20:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 80.4 |
| 675cf26f-aa33-36d0-b62e-b78858fd555d | -5.194 | -43.0743 | 2025-12-05 02:20:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 72.5 |
| a42e8ead-c53d-3800-b1c5-2f6a395f82c0 | -6.0002 | -41.1538 | 2025-12-05 02:20:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 87.0 |
| 955c1e88-c367-3b3f-b853-fb1135da6fa6 | -9.9879 | -36.3038 | 2025-12-05 02:20:00 | GOES-19 | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 72.0 |
| 91e5f7e6-d5ee-306f-b127-8a8db798f23a | -2.905 | -45.2143 | 2025-12-05 02:20:00 | GOES-19 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 4b4ce321-a405-316d-861c-81b55945b511 | -6.019 | -41.1521 | 2025-12-05 02:20:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 79.1 |
| cec29594-d7dc-347c-9661-2fee14ecd2b2 | -5.1938 | -43.0977 | 2025-12-05 02:20:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 60.7 |
| ba36ded2-be8d-3e1b-8a9c-51a09e9fac15 | -6.0004 | -41.1295 | 2025-12-05 02:20:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 78.5 |
| cc549b35-bbf8-32df-9644-20c9cc47489a | -5.1751 | -43.099 | 2025-12-05 02:20:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 82.7 |
| b00bd9bb-e0ed-3673-9b5e-5d47bd584e15 | -2.8863 | -45.2375 | 2025-12-05 02:20:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 67.7 |
| f1e29dfd-a6a6-3bd9-ad90-e094a0d90819 | -2.905 | -45.2143 | 2025-12-05 02:30:00 | GOES-19 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 0740e37c-5b81-3422-8cf9-c3395a38822a | -5.1753 | -43.0756 | 2025-12-05 02:30:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 94.3 |
| cf18f50e-f6ca-36e7-84dc-e15ad31e49b1 | -2.9049 | -45.2368 | 2025-12-05 02:30:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 170.6 |
| fb600859-1996-34b9-8ff6-9b70a4e0cfbd | -2.9048 | -45.2594 | 2025-12-05 02:30:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 66ea745f-3f30-3888-b05d-6a814be98f4f | -6.0002 | -41.1538 | 2025-12-05 02:30:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 69.0 |


[Clique aqui para ver as próximas entradas](README4.md)
