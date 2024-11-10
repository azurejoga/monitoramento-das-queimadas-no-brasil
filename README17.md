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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5ce62d2e-c118-3167-86a3-00c8cfd5d2b6 | -4.8655 | -46.9938 | 2024-11-10 01:40:00 | GOES-16 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 89ebd70d-bd01-3ecf-b1b2-cfd32c43e76c | -3.1423 | -50.4352 | 2024-11-10 01:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 80.4 |
| 9c6b75ef-c737-31d8-b724-d834f0ab0782 | -3.2243 | -53.0727 | 2024-11-10 01:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 116.2 |
| 57d9a7a8-7f6c-373a-be7a-71705817edb9 | -8.3778 | -44.1386 | 2024-11-10 01:50:00 | GOES-16 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 76.7 |
| 73216518-08a2-3f4b-9abc-e99eefe4d616 | -3.6004 | -47.3395 | 2024-11-10 01:50:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 132.6 |
| 637064f2-ef29-3ee1-b8f8-329bf9089eca | -8.3964 | -44.1597 | 2024-11-10 01:50:00 | GOES-16 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 1f919dde-9d34-30a2-a58b-b3736aebb07b | -3.9671 | -48.1283 | 2024-11-10 01:50:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 64.3 |
| ff732f14-f0d9-380c-afad-2c14f9dbfaa3 | -2.0768 | -48.8342 | 2024-11-10 01:50:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 48.4 |
| 7e1ded93-71c0-314a-bae6-5c2088daba0e | -1.5163 | -52.1901 | 2024-11-10 01:50:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 52.2 |
| f8519bfa-bf08-3354-8cd5-f13efe658e45 | -17.627 | -57.5075 | 2024-11-10 01:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 318.0 |
| 876d7661-0c74-3622-bcf6-6f9888bd12a6 | -2.7772 | -49.3492 | 2024-11-10 01:50:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 101.8 |
| 3c375c0d-72ce-39e3-b9fa-cb54afffdf3e | -3.6003 | -47.3614 | 2024-11-10 01:50:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 82.7 |
| 6ab30890-c21a-319a-af9e-0bbc92ca59b0 | -8.4156 | -44.1344 | 2024-11-10 01:50:00 | GOES-16 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 84.2 |
| b50a6bae-b83e-3c11-b0ea-9c449942db24 | -2.0954 | -48.8125 | 2024-11-10 01:50:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 91.2 |
| b814e139-0ae4-3b9a-8601-fc7d1fd3e20e | -2.7586 | -49.371 | 2024-11-10 01:50:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 46.1 |
| 19a34b91-9264-3efa-ad31-e9531a8ae18f | -3.9483 | -48.1724 | 2024-11-10 01:50:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 112.3 |
| 250054a0-28b8-3dbb-8e96-5d46f64843bd | -3.2243 | -53.0727 | 2024-11-10 01:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 71.8 |
| 7402a1e1-ece4-38b8-8553-4510b5b653c8 | -3.5064 | -44.0294 | 2024-11-10 01:50:00 | GOES-16 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 71.5 |
| 588df813-cb57-3fa4-aa9d-8259e96fb274 | -3.4198 | -50.3005 | 2024-11-10 01:50:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 49.1 |
| ae281ed8-cac8-3598-90fc-a974794a9399 | -3.2428 | -53.0519 | 2024-11-10 01:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 33.1 |
| 9b786ed0-33bf-3731-b1f2-a02d34e4197d | -3.4383 | -50.2999 | 2024-11-10 01:50:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 71.3 |
| 8262f526-aeef-335a-9440-c221763e54d2 | -3.9485 | -48.1508 | 2024-11-10 01:50:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 106.2 |
| 9fad8e17-7709-347b-95e4-deb3aa351acc | -17.6069 | -57.5304 | 2024-11-10 01:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 433.4 |
| 97007492-343a-35a5-a935-209434956d68 | -1.5347 | -52.2104 | 2024-11-10 01:50:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 174.7 |
| 3cd529f7-ee0d-3f79-9f6f-8c1d73ad2c22 | -2.4367 | -51.948 | 2024-11-10 01:50:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 56.0 |
| b6a7f9b0-2923-3252-b971-f89c24677667 | -3.525 | -44.0286 | 2024-11-10 01:50:00 | GOES-16 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 58.9 |
| a4d9b3a1-2644-3be9-90ce-f89dc28306a0 | -4.8657 | -46.9718 | 2024-11-10 01:50:00 | GOES-16 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 58dd867d-f1b3-34ff-bb2e-b9ff002d6ae0 | -3.5819 | -47.3403 | 2024-11-10 01:50:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 65.7 |
| f633316e-63df-3c7c-8f33-afeb9fcab225 | -3.9668 | -48.1932 | 2024-11-10 01:50:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 81.1 |
| bd15e83e-5107-3531-894f-785ed4ee4c00 | -3.9669 | -48.1716 | 2024-11-10 01:50:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 150.0 |
| 87b210a5-3e13-38bf-a610-1fdb51675a49 | -3.1422 | -50.4562 | 2024-11-10 01:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 176.4 |
| 2f00ce28-2884-33b2-b931-16f76f1cecec | -2.0953 | -48.8338 | 2024-11-10 01:50:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 169.5 |
| 19807b4b-10ac-3d39-9e4a-077065e75f26 | -3.9486 | -48.1291 | 2024-11-10 01:50:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 49.1 |
| 6d607f97-0546-3075-89aa-ac52842f246a | -3.1238 | -50.4568 | 2024-11-10 01:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 150.6 |
| 548bc6cc-fa42-3192-bfd2-4864eb9dab2d | 2.8552 | -60.0853 | 2024-11-10 01:50:00 | GOES-16 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 26.8 |
| ba9d137a-aae4-3ba2-a615-a5010d53d6a3 | -2.931 | -52.7753 | 2024-11-10 01:50:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 106.1 |
| 7b13b7bb-7adc-3776-acf9-67d8b7888268 | -3.1239 | -50.4358 | 2024-11-10 01:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 272.4 |
| 2f4f7f7f-bea7-37b3-b828-2a1b5398be83 | -17.6273 | -57.487 | 2024-11-10 01:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 67.4 |
| 6c589b30-b2c8-309c-ab33-41175012ab7a | -8.3967 | -44.1365 | 2024-11-10 01:50:00 | GOES-16 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 112.5 |
| 15e64a8f-7f58-3c5f-8fe0-f31161890d82 | -2.2095 | -47.733 | 2024-11-10 01:50:00 | GOES-16 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 66.8 |
| a6160bd7-482f-32ff-b9eb-3a8bc9106af4 | -17.2933 | -57.4857 | 2024-11-10 01:50:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 155.1 |
| 317db9eb-0028-3cb5-9550-4711945ae6ad | -3.1423 | -50.4352 | 2024-11-10 01:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 255.5 |
| 30f1b4e8-70a7-39ca-b10b-a4c10088af8a | -3.8413 | -44.1283 | 2024-11-10 01:50:00 | GOES-16 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 57.7 |
| 0d97b019-a3eb-3b87-9a08-b0f07da6b31f | -2.7587 | -49.3497 | 2024-11-10 01:50:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 91.4 |
| 62957d4b-5a13-3b7f-bf6d-2c0f9f83697b | -17.6073 | -57.5099 | 2024-11-10 01:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 364.0 |
| eed28e68-293c-360b-a480-d8beed2c4680 | -2.9494 | -52.7748 | 2024-11-10 01:50:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 56.0 |
| fbabe95e-929c-389f-a725-fc7be4584824 | -2.2076 | -48.3596 | 2024-11-10 01:50:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 58.5 |
| f98d85ea-8563-3543-80a4-56a03d64c592 | -17.313 | -57.4834 | 2024-11-10 01:50:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 82.0 |
| 1f1bed4d-32a9-320e-b168-0b5024ec0828 | -3.2244 | -53.0524 | 2024-11-10 01:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 74.0 |
| 4e9c6570-20df-3bd8-b181-0588d8efb231 | -1.5347 | -52.1899 | 2024-11-10 01:50:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 76.5 |
| 99453c4d-b936-330a-8345-5cbd21698dc7 | -17.293 | -57.5062 | 2024-11-10 01:50:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 111.5 |
| 54ae9213-7e3c-3881-aae1-6e512a996346 | -1.5163 | -52.2106 | 2024-11-10 01:50:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 69.4 |
| 839bacf8-9f57-3495-b663-c9cd927e5b5c | -3.1095 | -49.4241 | 2024-11-10 01:50:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 75aa34eb-7249-3538-9602-10e37b555ae5 | -17.6066 | -57.551 | 2024-11-10 01:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 70.9 |
| 484d1370-11ab-3f4f-9b36-a9e8f07a5bcd | -2.8857 | -45.3726 | 2024-11-10 01:50:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 99.9 |
| abb87462-2411-39cb-a723-3d3aeb23e262 | -2.4183 | -51.9484 | 2024-11-10 01:50:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 49.2 |
| 05854acc-855f-3477-a797-fc0ec07300bf | -17.6266 | -57.5281 | 2024-11-10 01:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 389.3 |
| 7136ad66-e7b7-35b9-81b3-973969ec6978 | -2.8802 | -51.4835 | 2024-11-10 01:50:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 52.4 |
| 4f6f336a-50ee-3831-a9f7-13ea97418b62 | -3.4198 | -50.3005 | 2024-11-10 02:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 50.7 |
| 394ed654-ae62-3bec-92d8-1c84a2ad6885 | -2.9356 | -51.4613 | 2024-11-10 02:00:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 41.4 |
| a6b04e62-750d-3e57-b668-00370e74873e | -17.2933 | -57.4857 | 2024-11-10 02:00:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 176.8 |
| 18cd65ad-2690-3bad-88b5-68b97357eca0 | -2.8857 | -45.3726 | 2024-11-10 02:00:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 95.4 |
| 12ede6f1-9718-392e-801e-82482b9a6692 | -17.6069 | -57.5304 | 2024-11-10 02:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 414.3 |
| 2ea6b87b-1773-3cd5-b2c3-3040ad4be166 | -8.4156 | -44.1344 | 2024-11-10 02:00:00 | GOES-16 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 100.0 |
| 5991a654-def1-330d-9da2-e58835e3700f | -2.7586 | -49.371 | 2024-11-10 02:00:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 49.4 |
| 243a3835-5538-3a57-9540-d61143090699 | -2.2095 | -47.733 | 2024-11-10 02:00:00 | GOES-16 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 68.5 |
| f7694462-fc0a-3558-bb00-d5f7a2106c1e | -8.3964 | -44.1597 | 2024-11-10 02:00:00 | GOES-16 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 72.4 |
| aebeed10-3636-3ab9-a390-f96a54d99cbc | -3.1096 | -49.4029 | 2024-11-10 02:00:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 52.8 |
| e0e8015e-00e7-372b-a95c-d548db29b4fb | -3.6003 | -47.3614 | 2024-11-10 02:00:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 84.0 |
| aa981c43-cb58-32ec-89e8-8959e6f098f8 | -2.418 | -46.3024 | 2024-11-10 02:00:00 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 51.7 |
| d4b483a4-becc-3ff5-9406-2f86056521e1 | -1.5347 | -52.2104 | 2024-11-10 02:00:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 150.9 |
| 977d3207-5dbd-30fe-8c26-132fe38bc995 | -1.5163 | -52.2106 | 2024-11-10 02:00:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 59.7 |
| bc0f9b0e-e399-3913-8b98-e4b5106f2c5f | -17.313 | -57.4834 | 2024-11-10 02:00:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 77.5 |
| 1326120e-1dc4-3427-b4ae-18b16639933c | -8.3778 | -44.1386 | 2024-11-10 02:00:00 | GOES-16 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 100.7 |
| ec66ebc0-2630-3747-8e13-1a361b220827 | -2.0954 | -48.8125 | 2024-11-10 02:00:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 94.8 |
| f6c88544-1665-326d-93ca-0e926e9b7fbc | -8.3967 | -44.1365 | 2024-11-10 02:00:00 | GOES-16 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 136.3 |
| 19bc8f26-112d-39bd-81ce-206cec9b322e | -2.9355 | -51.482 | 2024-11-10 02:00:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 82.5 |
| ebe9388a-321d-3059-b9ec-c219b5929134 | -3.6004 | -47.3395 | 2024-11-10 02:00:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 116.5 |
| a12f1444-4e71-3679-9f73-726ea6132dac | -3.1095 | -49.4241 | 2024-11-10 02:00:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 60.5 |
| b7f6683f-46d7-3cd4-bf51-10425a8a02c3 | -3.525 | -44.0286 | 2024-11-10 02:00:00 | GOES-16 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 68.0 |
| e0bbfd01-67f3-3fe2-a8bf-4482307919da | -17.6073 | -57.5099 | 2024-11-10 02:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 342.5 |
| c4428ca2-31f2-3032-930c-9168aa2795e9 | -3.1423 | -50.4352 | 2024-11-10 02:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 41.2 |
| 43d39400-28c5-34eb-9226-0fe608ca7746 | -2.2076 | -48.3596 | 2024-11-10 02:00:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 55.4 |
| ba070ad9-38bc-349d-93d2-49a6c689a798 | -3.5064 | -44.0294 | 2024-11-10 02:00:00 | GOES-16 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 73.9 |
| 3029b497-fc26-3d46-890c-846901422b52 | -1.5347 | -52.1899 | 2024-11-10 02:00:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 166898d4-523c-348e-823e-25802f74cede | -17.6066 | -57.551 | 2024-11-10 02:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 79.7 |
| b6ab7fba-f8bb-301f-b4bb-2fd62553e52b | -3.5819 | -47.3403 | 2024-11-10 02:00:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 0a9701e8-9779-3f00-9da7-00675d142d60 | -2.0953 | -48.8338 | 2024-11-10 02:00:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 131.3 |
| 26eb51a0-ac02-375a-b053-454ed40ad0b4 | -3.1239 | -50.4358 | 2024-11-10 02:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 54.4 |
| a5f6745f-b735-37e6-89a5-3a966b0fecae | -17.627 | -57.5075 | 2024-11-10 02:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 329.6 |
| b7fb9f8e-2c9d-355e-99e1-16fa3049d840 | -2.7772 | -49.3492 | 2024-11-10 02:00:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 89.3 |
| 735b93ea-23a2-384a-bf56-19dcf8dd9d06 | -2.7771 | -49.3704 | 2024-11-10 02:00:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 45.5 |
| b7921182-95c3-3c4a-b70c-2fbc85fe401a | -2.8802 | -51.4835 | 2024-11-10 02:00:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 54.4 |
| dad64959-a78c-3347-9384-d78e5578096d | -17.6273 | -57.487 | 2024-11-10 02:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 69.1 |
| a048c173-87d4-3450-80e2-e53635924796 | -2.4366 | -51.9685 | 2024-11-10 02:00:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 51.5 |
| 95992e0b-3f1d-3ec2-9073-d6e758419694 | -2.7587 | -49.3497 | 2024-11-10 02:00:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 74.6 |
| d02b89ed-6576-3806-8229-689a699262f5 | -17.6266 | -57.5281 | 2024-11-10 02:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 349.0 |
| 8e961471-41af-38fb-9db1-7ed11eb195dc | -2.4367 | -51.948 | 2024-11-10 02:00:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 52.6 |
| ee7958b5-15fc-3521-81f0-6e90ee2e4ffb | -2.9171 | -51.4825 | 2024-11-10 02:00:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 80.0 |
| 581ead94-0d57-3542-b60e-13e56a6b2a5f | -3.4383 | -50.2999 | 2024-11-10 02:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 81.3 |


[Clique aqui para ver as próximas entradas](README18.md)
