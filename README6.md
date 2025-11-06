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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 001ad6ff-5d3e-3d40-b293-6e71ba86028f | -4.6121 | -43.3227 | 2025-11-06 00:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 267.7 |
| 156f6037-f08d-3f61-956f-9578c8077358 | -3.9324 | -47.6962 | 2025-11-06 00:20:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 94.7 |
| e6f1cc5d-a5c0-3136-a7dd-8f84680d4038 | -4.5747 | -43.325 | 2025-11-06 00:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 142.1 |
| 440835af-5556-3e49-b151-6561e9e2e927 | -3.3758 | -44.0582 | 2025-11-06 00:20:00 | GOES-19 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 83.9 |
| f82dfeca-2066-300e-a840-0bc4f7e7c057 | -4.4632 | -43.2386 | 2025-11-06 00:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 143.5 |
| 91cf429f-4e0a-398e-9f06-e7a9be801056 | -3.3757 | -44.0812 | 2025-11-06 00:20:00 | GOES-19 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 65.1 |
| 0c4adc88-8390-3c1c-9785-8cd7a731100d | -2.986 | -52.835 | 2025-11-06 00:20:00 | GOES-19 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 70.9 |
| 0261af61-8b7c-365e-9ec1-b67edc9be0d7 | -3.7937 | -49.4211 | 2025-11-06 00:20:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 89.7 |
| 544acb45-4006-3791-aef4-ba88bacc864a | -3.7752 | -49.4219 | 2025-11-06 00:20:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 82.1 |
| 9b2d0915-d01f-32a2-8b97-708d429e45c3 | -4.029 | -47.0143 | 2025-11-06 00:20:00 | GOES-19 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 76.2 |
| 733dfcb9-eb51-3cd7-a504-b3fd0dac9414 | -4.7857 | -45.1249 | 2025-11-06 00:20:00 | GOES-19 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 90.5 |
| 920a8ca4-0998-3576-ad4c-54539c85c01c | 0.4466 | -60.4873 | 2025-11-06 00:20:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 114.0 |
| 233728ff-2aa5-3a2e-a89b-cfb4102965d9 | -4.7855 | -45.1475 | 2025-11-06 00:20:00 | GOES-19 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 82.4 |
| 93daa348-d58c-3d6d-b017-4e5cc23befb0 | -2.986 | -52.8146 | 2025-11-06 00:20:00 | GOES-19 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 87.7 |
| f608c88a-6826-3168-8d6d-8396d14a4147 | -5.1531 | -41.271 | 2025-11-06 00:20:00 | GOES-19 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 137.3 |
| 57fcd6e8-79cb-34c0-83fc-e62a7f5e6621 | -5.1533 | -41.2468 | 2025-11-06 00:20:00 | GOES-19 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 118.5 |
| 522db9c3-0cf5-3048-a8f3-d361a27b8670 | -3.9139 | -47.697 | 2025-11-06 00:20:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 75.9 |
| da92c037-3aeb-34e9-8a6f-7972be729e63 | 0.4283 | -60.4874 | 2025-11-06 00:20:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 91.8 |
| edc4ae54-f28a-330b-a77d-f252679d1ea2 | -4.4633 | -43.2152 | 2025-11-06 00:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 114.9 |
| d3015ea6-6753-316c-9950-36b070d08516 | -3.3944 | -44.0574 | 2025-11-06 00:20:00 | GOES-19 | PRESIDENTE VARGAS | MARANHÃO | Brasil | 2109304 | 21 | 33 | nan | nan | nan | Cerrado | 158.3 |
| 95884406-e713-3fdd-83c4-edbc2225c5a9 | -7.9228 | -44.3251 | 2025-11-06 00:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 83.6 |
| e60c4d7e-dc24-3d40-8ff0-25ac434810c6 | -4.1161 | -48.0136 | 2025-11-06 00:20:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 101.2 |
| 7b3b2025-f21a-34e5-b256-54097cbd6fc5 | -4.5932 | -43.3471 | 2025-11-06 00:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 466.8 |
| 1a7fae08-a139-3f25-a499-e3c0b4022884 | -4.5745 | -43.3483 | 2025-11-06 00:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 134.7 |
| 37c32efa-fbd3-306a-8631-bdc35ba8131f | -4.0476 | -47.0134 | 2025-11-06 00:20:00 | GOES-19 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 83.6 |
| 8904cd4c-97ee-30d9-b352-7aa9b282ffc9 | -3.4231 | -54.0172 | 2025-11-06 00:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 82.6 |
| 6221968f-f35e-3ac0-9ae5-1729557ddae7 | -4.593 | -43.3704 | 2025-11-06 00:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 64.5 |
| 6165e1f5-c377-3d4f-8ae7-7356d06ad298 | -3.4711 | -43.6623 | 2025-11-06 00:20:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 483.3 |
| 3721206b-34b3-386c-a642-940930a9ee28 | -3.4525 | -43.6631 | 2025-11-06 00:20:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 43.7 |
| 67b64139-e4b3-33af-b748-c62a00420365 | -3.3943 | -44.0804 | 2025-11-06 00:20:00 | GOES-19 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 110.9 |
| 6c70dcbc-973a-3837-8fe5-bdbb9e1e7309 | -3.471 | -43.6854 | 2025-11-06 00:20:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 86.0 |
| cd161fcd-8b08-3923-9fa9-9d9ae316f3eb | -3.4898 | -43.6614 | 2025-11-06 00:20:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 155.1 |
| b053f6c1-2a2e-3ce4-94d4-955c9edac26a | -4.6119 | -43.346 | 2025-11-06 00:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 262.4 |
| e2992a7e-a7c0-3267-bbea-1ec64c28a665 | -4.72 | -46.5162 | 2025-11-06 00:20:00 | GOES-19 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 124.8 |
| d92a0842-608e-39a2-8637-d1a5184c720d | -4.5934 | -43.3239 | 2025-11-06 00:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 489.8 |
| 2321d883-7c96-37d7-9874-3f95cd4fc226 | -3.9071 | -42.5436 | 2025-11-06 00:20:00 | GOES-19 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 59.2 |
| ddb430a1-a236-3e7f-af71-d1a1aff85e8e | -4.0477 | -46.9915 | 2025-11-06 00:20:00 | GOES-19 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 170.7 |
| 5149aee2-8099-3f08-9703-5a4bf60d33c9 | -5.7589 | -40.81 | 2025-11-06 00:20:00 | GOES-19 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 71.2 |
| b3e1e174-7d02-3b2a-8e36-d75330767b34 | -4.0292 | -46.9923 | 2025-11-06 00:20:00 | GOES-19 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 151.6 |
| 112d0041-2240-31b0-9a55-c7ffb073972f | -4.4632 | -43.2386 | 2025-11-06 00:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 125.2 |
| 77561e85-ea29-3e91-9d20-c4248ed5cf28 | -3.3944 | -44.0574 | 2025-11-06 00:30:00 | GOES-19 | PRESIDENTE VARGAS | MARANHÃO | Brasil | 2109304 | 21 | 33 | nan | nan | nan | Cerrado | 53.3 |
| b9224ea7-bd41-3058-9f90-eb67a4436f19 | -7.5062 | -44.5273 | 2025-11-06 00:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 381.1 |
| ad1e38ef-015b-3b4d-b55f-cb5ec202b1a4 | -3.4231 | -54.0172 | 2025-11-06 00:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 78.4 |
| fbe7abe6-a04d-3230-ad8c-04634fd4cb06 | -4.0292 | -46.9923 | 2025-11-06 00:30:00 | GOES-19 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 195.4 |
| 9cd9c210-e5fd-313b-86bb-b07616007162 | -4.5745 | -43.3483 | 2025-11-06 00:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 129.7 |
| 8f637a0a-eb68-337f-a4a2-a6143a2d8bc4 | -4.7014 | -46.5173 | 2025-11-06 00:30:00 | GOES-19 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 120.6 |
| 6ed657aa-e32c-3853-8ffd-d03057a0f57a | 0.4283 | -60.4874 | 2025-11-06 00:30:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 82.6 |
| b1bdc5bc-4448-380d-bcb4-826674affd75 | -5.1531 | -41.271 | 2025-11-06 00:30:00 | GOES-19 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 120.2 |
| 5b7bb068-961e-395d-add6-47a4b462e155 | -4.1161 | -48.0136 | 2025-11-06 00:30:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 104.2 |
| f9471853-c928-3d3c-a4db-c6b7246f6082 | -4.5934 | -43.3239 | 2025-11-06 00:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 398.5 |
| e1b24397-4b85-3d32-a4fc-4a194fa4f751 | -2.986 | -52.8146 | 2025-11-06 00:30:00 | GOES-19 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 79.3 |
| f3398a10-e6e9-3482-a014-92b7557304da | -4.5932 | -43.3471 | 2025-11-06 00:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 464.9 |
| 4ef6860e-1d7a-3bbd-9ac4-a81fd631b554 | -4.4633 | -43.2152 | 2025-11-06 00:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 137.3 |
| 6857e662-1865-39f8-9e27-38aa4e15cec0 | -3.9324 | -47.6962 | 2025-11-06 00:30:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 88.5 |
| 38d330c9-fe2d-3b59-b3e6-110c46ce0c35 | -3.4712 | -43.6392 | 2025-11-06 00:30:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 206.6 |
| e3a5c55f-69c5-350e-8756-b82d9dbfaed7 | -4.0476 | -47.0134 | 2025-11-06 00:30:00 | GOES-19 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 88.5 |
| 0bc8d7eb-9971-36fc-a342-a0288fd936d9 | -7.4874 | -44.5291 | 2025-11-06 00:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 195.1 |
| 1612c7a8-8258-3c0f-9cb3-5d91448fcb26 | -4.6121 | -43.3227 | 2025-11-06 00:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 232.0 |
| f588c8b0-2a24-356b-bb58-8b40aee244e3 | -4.7857 | -45.1249 | 2025-11-06 00:30:00 | GOES-19 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 101.5 |
| 1e0ca0b7-a390-3b99-9f26-6ff949436890 | -5.1533 | -41.2468 | 2025-11-06 00:30:00 | GOES-19 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 93.0 |
| 3c19c62c-15fc-3055-bed4-3d1d7a77af63 | -4.7198 | -46.5384 | 2025-11-06 00:30:00 | GOES-19 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 85.6 |
| 0395e674-8ea6-30be-af24-abf275f9f646 | -7.5065 | -44.5043 | 2025-11-06 00:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 108.4 |
| 31ec7283-28c9-319d-ab51-988514657dc9 | -4.5747 | -43.325 | 2025-11-06 00:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 117.5 |
| a1338c36-9684-36ca-99c2-20fb2f7c1249 | -3.4898 | -43.6614 | 2025-11-06 00:30:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 129.3 |
| 479dd478-0e20-3ed1-b8bc-4ba195ddad84 | -7.4871 | -44.5521 | 2025-11-06 00:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 102.1 |
| 89783b7f-c179-379c-802e-8a138e9d5d58 | -4.6119 | -43.346 | 2025-11-06 00:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 274.9 |
| 6554143d-3947-3e57-a340-194785a59f7e | -7.506 | -44.5503 | 2025-11-06 00:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 150.2 |
| 2a487b55-ab82-3ef4-ba2b-be731b437072 | -3.4899 | -43.6383 | 2025-11-06 00:30:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 79.7 |
| bd6fbe43-4c5a-3248-88ce-f3a26fa11385 | -3.4711 | -43.6623 | 2025-11-06 00:30:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 377.8 |
| d3df920f-9ede-3a60-9a91-ff41d58d431f | -4.7012 | -46.5394 | 2025-11-06 00:30:00 | GOES-19 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 95.4 |
| 9db0bff7-1bab-309b-8124-f93ca4fff829 | 0.4466 | -60.4873 | 2025-11-06 00:30:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 101.1 |
| c30a20ff-6436-345f-8eb4-47e4b114579f | -5.7589 | -40.81 | 2025-11-06 00:30:00 | GOES-19 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 73.9 |
| 1bb388a4-ef3a-31f5-a37b-91004d3788a2 | -4.72 | -46.5162 | 2025-11-06 00:30:00 | GOES-19 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 94.5 |
| 5b43ca56-1347-32ad-87c0-a03660c7d3c3 | -4.0477 | -46.9915 | 2025-11-06 00:30:00 | GOES-19 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 259.4 |
| ae65a8da-f215-3c06-b99f-0c7cdcf3e15f | -4.7198 | -46.5384 | 2025-11-06 00:40:00 | GOES-19 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 147.8 |
| 7ad758ab-c15a-3ba9-9180-e3669fe4f48e | -3.4525 | -43.6631 | 2025-11-06 00:40:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 51.9 |
| 47da0511-5630-382e-846b-21a30e77167c | -7.9228 | -44.3251 | 2025-11-06 00:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 67.4 |
| a40df7ba-bea7-39be-a8b5-fe62ef23a5f2 | -3.4712 | -43.6392 | 2025-11-06 00:40:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 184.7 |
| d37f5d6a-0265-3c0b-aa45-6bc0a38888b9 | -4.0476 | -47.0134 | 2025-11-06 00:40:00 | GOES-19 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 97.2 |
| 5b67dbfa-72fb-3c53-a3a1-cec3bc0b30d4 | -4.4633 | -43.2152 | 2025-11-06 00:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 93.3 |
| 2a14ac3d-8c29-370b-96ad-5b6686de8fe8 | -3.4898 | -43.6614 | 2025-11-06 00:40:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 148.0 |
| 001e4358-b14c-3466-a952-ca626c9edca3 | -3.9324 | -47.6962 | 2025-11-06 00:40:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 94.1 |
| 49feca37-ba8a-354b-8a72-781af6ec0829 | -4.4632 | -43.2386 | 2025-11-06 00:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 99.0 |
| a659d32e-656b-33b1-92ae-863a4623364a | -4.7012 | -46.5394 | 2025-11-06 00:40:00 | GOES-19 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 113.6 |
| af364645-6f95-3f5e-ad77-1ecd5c0d157b | -4.7855 | -45.1475 | 2025-11-06 00:40:00 | GOES-19 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 75.5 |
| 42bf2e9b-8526-3dcc-b9bd-d729012723db | -5.1533 | -41.2468 | 2025-11-06 00:40:00 | GOES-19 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 86.9 |
| 45b11503-cbbe-36ac-ad59-a0d2dee973e8 | -2.986 | -52.8146 | 2025-11-06 00:40:00 | GOES-19 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 80.3 |
| 144b9034-5bdd-3679-b67c-e0e30b686286 | -4.5932 | -43.3471 | 2025-11-06 00:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 694.5 |
| a87faae5-5a6c-3b86-ace1-21e531d75714 | -2.986 | -52.835 | 2025-11-06 00:40:00 | GOES-19 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 74.7 |
| 9e20287f-17ae-3e60-ab5e-8edfc7057843 | 0.4283 | -60.4874 | 2025-11-06 00:40:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 78.6 |
| 4b43ed05-fcfb-34b9-8663-93259f01ce17 | -3.4711 | -43.6623 | 2025-11-06 00:40:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 247.9 |
| 3f7f102b-e247-3692-83be-99aae2bdf700 | -4.0976 | -48.0144 | 2025-11-06 00:40:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 85.4 |
| d90cc0a7-545c-3231-908c-dd2315ed0701 | -5.1531 | -41.271 | 2025-11-06 00:40:00 | GOES-19 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 87.1 |
| e20dae13-efa8-31ba-aa0b-4548be1edcb0 | -4.5747 | -43.325 | 2025-11-06 00:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 85.3 |
| cab34f40-3509-3297-8181-ecbefc8aa3ef | -4.0477 | -46.9915 | 2025-11-06 00:40:00 | GOES-19 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 291.8 |
| 8158d1f0-0f16-3c57-b6d5-764d0707d02a | -4.7857 | -45.1249 | 2025-11-06 00:40:00 | GOES-19 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 92.5 |
| 674fee04-2345-3676-ae59-389e6f107d4d | 0.4466 | -60.4873 | 2025-11-06 00:40:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 124.5 |
| 2927c1e8-5c71-3114-96a6-3265503eb5ae | -4.1161 | -48.0136 | 2025-11-06 00:40:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 76.7 |
| cde460bf-cc12-36fc-a900-1a9875bd4bba | -4.0292 | -46.9923 | 2025-11-06 00:40:00 | GOES-19 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 166.9 |
| a0bd6fb1-c9a0-370d-8386-1798f83875b1 | -4.5745 | -43.3483 | 2025-11-06 00:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 77.2 |


[Clique aqui para ver as próximas entradas](README7.md)
