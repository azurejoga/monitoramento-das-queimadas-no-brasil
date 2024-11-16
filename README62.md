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

## Dados Diários - Página 62

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 73589613-372e-34b0-aeb1-37bf53a09466 | -16.9577 | -57.6473 | 2024-11-16 12:30:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 93.6 |
| 44ff13e4-83dd-3974-acbe-2e92121296ed | -16.0466 | -60.119 | 2024-11-16 12:30:00 | GOES-16 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 203.8 |
| f6a9528f-a434-359a-8fa0-1f1049e44174 | -17.5869 | -57.5533 | 2024-11-16 12:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 88.5 |
| d74946bc-0491-3085-bf08-b8237827ac93 | -3.4787 | -42.3058 | 2024-11-16 12:30:00 | GOES-16 | LUZILÂNDIA | PIAUÍ | Brasil | 2205805 | 22 | 33 | nan | nan | nan | Cerrado | 169.1 |
| c7949955-1f94-36de-8f50-5ddbcc068e73 | -19.5426 | -56.908 | 2024-11-16 12:30:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 98.3 |
| 154c4efa-e983-3ab1-bc75-a9f9ac5705de | -17.6066 | -57.551 | 2024-11-16 12:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 106.2 |
| 59ed8519-00d2-3b09-a208-b24d7da6ccd4 | -17.6263 | -57.5486 | 2024-11-16 12:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 92.1 |
| d0ba82ea-2dee-3b19-b670-345dd7a1b284 | -17.5865 | -57.5739 | 2024-11-16 12:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 244.3 |
| d821c797-5123-39af-8027-a6610afab193 | -17.2547 | -57.4493 | 2024-11-16 12:30:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 101.3 |
| 30d7a1ce-faf8-3efe-9238-f01c9ed285c0 | -17.235 | -57.4516 | 2024-11-16 12:30:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 104.3 |
| 65755785-b276-34ed-be17-f2223fda50cd | -3.8348 | -42.1455 | 2024-11-16 12:40:00 | GOES-16 | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 449.7 |
| d9f44ff2-f84a-3abd-8f2b-b6e387d815f0 | -17.2547 | -57.4493 | 2024-11-16 12:40:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 101.3 |
| 7caadfe6-66fb-3644-b2ac-a0dd20ed5618 | -3.6537 | -44.3436 | 2024-11-16 12:40:00 | GOES-16 | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 76.1 |
| 92721bef-f308-326b-81c3-38ec30ab8061 | -17.5869 | -57.5533 | 2024-11-16 12:40:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 91.0 |
| 5a7c1f24-ca49-3933-bf0f-44b93683610c | -17.5865 | -57.5739 | 2024-11-16 12:40:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 365.5 |
| e0785f2d-006f-372d-a090-08c3c93cd8a3 | -17.6263 | -57.5486 | 2024-11-16 12:40:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 97.1 |
| b22fae84-685c-34f9-8fc5-3116f7b898d5 | -16.0466 | -60.119 | 2024-11-16 12:40:00 | GOES-16 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 145.2 |
| 26b07b0b-bc1c-3e0e-b337-bb54ca1a03b3 | -16.9384 | -57.6291 | 2024-11-16 12:40:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 141.3 |
| 00f1e21f-803a-3d12-99c2-6df446ea743d | -17.5862 | -57.5944 | 2024-11-16 12:40:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 246.7 |
| 824ebb87-d04b-3a7c-aad2-5caeea582be0 | -19.5426 | -56.908 | 2024-11-16 12:40:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 129.1 |
| 09b80984-727a-3151-abcd-b9a2d64bd36f | -16.9577 | -57.6473 | 2024-11-16 12:40:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 90.2 |
| 7d09eb76-c70a-33f7-92a8-742914e24bfc | -17.235 | -57.4516 | 2024-11-16 12:40:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 107.4 |
| 147197a7-cae5-3909-a399-20d1a3a5be49 | -17.6066 | -57.551 | 2024-11-16 12:40:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 94.3 |
| 23ad0406-7afd-34c3-95c1-73c5e7e0f47d | -3.68652 | -42.65795 | 2024-11-16 12:44:00 | TERRA_M-T | MATIAS OLÍMPIO | PIAUÍ | Brasil | 2206100 | 22 | 33 | nan | nan | nan | Cerrado | 61.8 |
| 553086c0-4377-35f9-b22d-51f4ac0d3edd | -1.32898 | -47.59039 | 2024-11-16 12:44:00 | TERRA_M-T | SANTA MARIA DO PARÁ | PARÁ | Brasil | 1506609 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 60fc55aa-0824-3c93-8b68-61a818c036c8 | -3.30077 | -42.05058 | 2024-11-16 12:44:00 | TERRA_M-T | MURICI DOS PORTELAS | PIAUÍ | Brasil | 2206696 | 22 | 33 | nan | nan | nan | Cerrado | 29.8 |
| 1286218b-e6ed-3a34-8b83-5b3140160a24 | -1.61343 | -47.92571 | 2024-11-16 12:44:00 | TERRA_M-T | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 5d700897-0f7d-3acb-9bf0-25423f22142a | -1.22543 | -47.54295 | 2024-11-16 12:44:00 | TERRA_M-T | IGARAPÉ-AÇU | PARÁ | Brasil | 1503200 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 00ee806d-5700-3e60-9d2c-37126eb595b0 | -1.33782 | -47.59164 | 2024-11-16 12:44:00 | TERRA_M-T | SANTA MARIA DO PARÁ | PARÁ | Brasil | 1506609 | 15 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 2f7c3833-f2fd-3f3e-9693-b55cad01939a | -2.22028 | -46.85725 | 2024-11-16 12:44:00 | TERRA_M-T | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 045285b8-3d84-35e0-90a6-fc41256ecf6a | -4.00556 | -46.50004 | 2024-11-16 12:44:00 | TERRA_M-T | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 5c0fdb49-ca88-39c2-b52f-f7b43af5dbc6 | -0.26567 | -48.50326 | 2024-11-16 12:44:00 | TERRA_M-T | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | 16.0 |
| 78ed93c4-b74c-3802-a88f-5c2bdaf3fc48 | -3.52009 | -42.01164 | 2024-11-16 12:44:00 | TERRA_M-T | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 29.3 |
| 66867230-4228-3aac-933f-27bd85cbd7e9 | -3.68865 | -42.64282 | 2024-11-16 12:44:00 | TERRA_M-T | MATIAS OLÍMPIO | PIAUÍ | Brasil | 2206100 | 22 | 33 | nan | nan | nan | Cerrado | 52.9 |
| fced0f9b-b91f-3aac-93fc-4803c22e8cd9 | -2.90843 | -45.46931 | 2024-11-16 12:44:00 | TERRA_M-T | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 49.7 |
| 1accf63f-6008-3b69-a722-f4aa660980dd | -3.02314 | -41.80139 | 2024-11-16 12:44:00 | TERRA_M-T | PARNAÍBA | PIAUÍ | Brasil | 2207702 | 22 | 33 | nan | nan | nan | Caatinga | 14.6 |
| 8b0fc628-e9f9-33ad-8896-38e041e84e95 | -2.09195 | -48.94816 | 2024-11-16 12:44:00 | TERRA_M-T | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 163cda15-9ddc-3c6a-a685-827970da010c | -3.71797 | -41.95615 | 2024-11-16 12:44:00 | TERRA_M-T | SÃO JOSÉ DO DIVINO | PIAUÍ | Brasil | 2210052 | 22 | 33 | nan | nan | nan | Caatinga | 21.5 |
| 6feded43-1c0a-3c41-9603-a2b9533de32e | -3.48188 | -42.29588 | 2024-11-16 12:44:00 | TERRA_M-T | LUZILÂNDIA | PIAUÍ | Brasil | 2205805 | 22 | 33 | nan | nan | nan | Caatinga | 144.3 |
| 4eb8dd2f-0728-360f-a70a-ed72840b0c1e | -3.83606 | -42.15981 | 2024-11-16 12:44:00 | TERRA_M-T | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 174.0 |
| f610346f-7c96-3c71-944b-28b7b849743d | -2.13005 | -48.18095 | 2024-11-16 12:44:00 | TERRA_M-T | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 0131c176-6a9a-3e58-a8cd-2731aff66b49 | -0.77952 | -49.48673 | 2024-11-16 12:44:00 | TERRA_M-T | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 49.4 |
| 68e51d54-b763-384e-be81-e25516222ce6 | -2.08817 | -46.68193 | 2024-11-16 12:44:00 | TERRA_M-T | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| d2d9419a-b156-3095-828e-b93c04cfa80b | -3.93065 | -42.39783 | 2024-11-16 12:44:00 | TERRA_M-T | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 18.1 |
| 0ac84605-e759-3c60-acdc-a552d17a9fa3 | -1.76047 | -47.54748 | 2024-11-16 12:44:00 | TERRA_M-T | IRITUIA | PARÁ | Brasil | 1503507 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 676bf5fc-91e3-396e-9a47-8e089d3d2a1c | -4.34499 | -43.77985 | 2024-11-16 12:44:00 | TERRA_M-T | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 19.2 |
| d7296044-0ede-33a4-b886-ac91f13e9ecb | -1.01813 | -47.76287 | 2024-11-16 12:44:00 | TERRA_M-T | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 3f1a8f18-2424-3c78-8d49-205cdc9f500a | -3.11891 | -40.90346 | 2024-11-16 12:44:00 | TERRA_M-T | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 51.1 |
| 1b60345d-4229-31e6-899f-7e0b256b9f04 | -3.651 | -44.35301 | 2024-11-16 12:44:00 | TERRA_M-T | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 63.1 |
| cbfcf5df-4705-38d4-8c96-099de4218cb1 | -3.03426 | -47.98359 | 2024-11-16 12:44:00 | TERRA_M-T | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 41cb04ad-492c-3c14-a4e1-68b2567b290c | -1.62231 | -47.92696 | 2024-11-16 12:44:00 | TERRA_M-T | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 1cb24e41-0e4f-322b-81c5-e5dd72939ae2 | -1.25042 | -47.69638 | 2024-11-16 12:44:00 | TERRA_M-T | IGARAPÉ-AÇU | PARÁ | Brasil | 1503200 | 15 | 33 | nan | nan | nan | Amazônia | 20.6 |
| d1cadf1a-9635-3acc-90fe-7435d480c111 | -3.65266 | -44.34143 | 2024-11-16 12:44:00 | TERRA_M-T | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 85.6 |
| ef20da84-de18-3141-a496-5b56921530ec | -4.51415 | -43.48829 | 2024-11-16 12:44:00 | TERRA_M-T | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 20.2 |
| 67060d8d-66c3-3ed9-8605-b981408a79f5 | -2.4764 | -46.35884 | 2024-11-16 12:44:00 | TERRA_M-T | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 17.2 |
| 4db8c6ce-4e61-3e87-9e92-33c85eefce40 | -2.30967 | -48.4666 | 2024-11-16 12:44:00 | TERRA_M-T | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 86a52353-531a-3c20-8361-4774da63f0ba | -3.96167 | -42.90471 | 2024-11-16 12:44:00 | TERRA_M-T | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 27.1 |
| 0a3d6b2a-af94-38f5-80f6-ab53481608c0 | -1.68337 | -48.46204 | 2024-11-16 12:44:00 | TERRA_M-T | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 21aa7729-e960-3542-9a58-c535b5162add | -1.34011 | -46.17518 | 2024-11-16 12:44:00 | TERRA_M-T | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 19.8 |
| b867cb10-59c9-32d1-8074-3fb41e77bd38 | -3.7205 | -42.65351 | 2024-11-16 12:44:00 | TERRA_M-T | MATIAS OLÍMPIO | PIAUÍ | Brasil | 2206100 | 22 | 33 | nan | nan | nan | Cerrado | 20.8 |
| f8861317-bb25-3fe1-80da-739a7a319bd1 | -3.5232 | -41.49386 | 2024-11-16 12:44:00 | TERRA_M-T | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 23.0 |
| caa43fa9-94d9-3eee-b479-6205135e3f0b | -3.7223 | -41.96238 | 2024-11-16 12:44:00 | TERRA_M-T | SÃO JOSÉ DO DIVINO | PIAUÍ | Brasil | 2210052 | 22 | 33 | nan | nan | nan | Caatinga | 17.8 |
| fc187a77-9755-3e85-8aa5-4a8580b5df5a | -3.79548 | -43.91435 | 2024-11-16 12:44:00 | TERRA_M-T | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 5bf4e75a-5e13-3c49-a2b1-738c6474260b | -3.50864 | -42.09695 | 2024-11-16 12:44:00 | TERRA_M-T | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 41.0 |
| c0675350-9858-3e3d-8fde-4420c266f1ee | -2.72933 | -44.85665 | 2024-11-16 12:44:00 | TERRA_M-T | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 0f02aeb9-1ce5-338d-8953-0b259d8f1b26 | -2.17313 | -48.33075 | 2024-11-16 12:44:00 | TERRA_M-T | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 2eaedd91-d0de-37db-b61c-ca13bfcfc36f | -2.0324 | -48.28022 | 2024-11-16 12:44:00 | TERRA_M-T | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 75.2 |
| b2ab02a8-0c5b-365b-9026-531669ed5c91 | -3.03554 | -47.97476 | 2024-11-16 12:44:00 | TERRA_M-T | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| bef14985-5437-35a0-914f-a16bd90541c1 | -1.61472 | -47.91683 | 2024-11-16 12:44:00 | TERRA_M-T | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 17.7 |
| d22fca50-b712-3c67-a4ba-f147e404be82 | -3.66032 | -42.27643 | 2024-11-16 12:44:00 | TERRA_M-T | MORRO DO CHAPÉU DO PIAUÍ | PIAUÍ | Brasil | 2206670 | 22 | 33 | nan | nan | nan | Caatinga | 17.8 |
| bca57f5d-288b-30c6-8b2a-3099f330851e | -1.5638 | -47.38217 | 2024-11-16 12:44:00 | TERRA_M-T | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 26.1 |
| 68088ee4-10e4-3e3c-915f-1c1a49cd48b0 | -3.01542 | -45.298 | 2024-11-16 12:44:00 | TERRA_M-T | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 178.3 |
| 4c5bbf07-fa36-3303-b79f-54e3ed12149b | -3.11414 | -42.55988 | 2024-11-16 12:44:00 | TERRA_M-T | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 8295b1e4-6ac7-318b-8830-42aa11d7cc47 | -3.54091 | -42.53774 | 2024-11-16 12:44:00 | TERRA_M-T | MADEIRO | PIAUÍ | Brasil | 2205854 | 22 | 33 | nan | nan | nan | Caatinga | 18.4 |
| efe1a31a-b683-3646-baa5-62696a1dc2a9 | -3.28266 | -42.34962 | 2024-11-16 12:44:00 | TERRA_M-T | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 635e2e8b-03b8-36d2-8160-f22fdfdfb4b5 | -3.47249 | -42.30539 | 2024-11-16 12:44:00 | TERRA_M-T | LUZILÂNDIA | PIAUÍ | Brasil | 2205805 | 22 | 33 | nan | nan | nan | Cerrado | 132.4 |
| 391451ff-959e-3240-b143-338df9bef9fe | -2.52417 | -48.13381 | 2024-11-16 12:44:00 | TERRA_M-T | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 59bd3a1b-c09e-333a-96b7-b25c4759e56f | -1.55126 | -47.32931 | 2024-11-16 12:44:00 | TERRA_M-T | BONITO | PARÁ | Brasil | 1501600 | 15 | 33 | nan | nan | nan | Amazônia | 26.0 |
| 24df3ad5-0b6b-33de-b645-8bb8ff1bae6f | -3.5206 | -42.09863 | 2024-11-16 12:44:00 | TERRA_M-T | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 329.4 |
| fd5badac-45e7-3f6d-8c05-096d5d4da2de | -1.32462 | -47.75824 | 2024-11-16 12:44:00 | TERRA_M-T | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| d2896197-e444-3a2a-94ff-92bc45084262 | -3.92834 | -42.41408 | 2024-11-16 12:44:00 | TERRA_M-T | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 29.3 |
| 563a28f5-8244-3501-b8f4-d5882717c72a | -0.65304 | -49.38954 | 2024-11-16 12:44:00 | TERRA_M-T | SANTA CRUZ DO ARARI | PARÁ | Brasil | 1506401 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 3db6c7da-b9e0-37bd-a146-068f933b94bf | -3.78685 | -43.90042 | 2024-11-16 12:44:00 | TERRA_M-T | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 27.0 |
| 852926e7-0b54-3784-a8fb-30c9b88a467f | -4.6057 | -41.61574 | 2024-11-16 12:44:00 | TERRA_M-T | MILTON BRANDÃO | PIAUÍ | Brasil | 2206357 | 22 | 33 | nan | nan | nan | Caatinga | 22.6 |
| dfc93029-8dcd-34a2-b9a3-740675296028 | -1.2823 | -47.53899 | 2024-11-16 12:44:00 | TERRA_M-T | SANTA MARIA DO PARÁ | PARÁ | Brasil | 1506609 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 1cd5e4bc-160e-3c13-834f-ede95f470dbd | -2.08945 | -46.67307 | 2024-11-16 12:44:00 | TERRA_M-T | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| f5df1f23-25c4-3609-8072-3ff24ba64d70 | -2.78274 | -48.57989 | 2024-11-16 12:44:00 | TERRA_M-T | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 72d871a9-70f4-3c73-bc9b-b2f6e79385cd | -1.9138 | -48.52543 | 2024-11-16 12:44:00 | TERRA_M-T | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| a5961caf-8bc5-3874-a5a0-502fcd10f45e | -2.00641 | -48.39627 | 2024-11-16 12:44:00 | TERRA_M-T | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 2b866bf3-26b7-346f-9240-fa3a6960e608 | -3.48423 | -42.30704 | 2024-11-16 12:44:00 | TERRA_M-T | LUZILÂNDIA | PIAUÍ | Brasil | 2205805 | 22 | 33 | nan | nan | nan | Caatinga | 87.9 |
| 8d3ebff9-0aa1-37a4-80a5-3389143d11b2 | -3.51779 | -42.02878 | 2024-11-16 12:44:00 | TERRA_M-T | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 16.8 |
| db4e60d2-13d4-37fa-ba40-9ca35e91cc32 | -3.76495 | -43.24702 | 2024-11-16 12:44:00 | TERRA_M-T | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 04f60b24-03b8-3946-bdd0-774f03890ec4 | -3.37604 | -42.16872 | 2024-11-16 12:44:00 | TERRA_M-T | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Caatinga | 39.1 |
| 5f3b2372-738f-3f09-8ab7-421abe2c907a | -2.9786 | -47.99382 | 2024-11-16 12:44:00 | TERRA_M-T | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| a559c228-3d40-34d7-a1a2-c425d3936414 | -1.89058 | -47.47322 | 2024-11-16 12:44:00 | TERRA_M-T | IRITUIA | PARÁ | Brasil | 1503507 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 397ceaa1-e0ad-344b-8e45-1bb0e742ac30 | -2.21901 | -46.86607 | 2024-11-16 12:44:00 | TERRA_M-T | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 614961c4-379e-354e-b418-5e431ba6a1ef | -0.26432 | -48.51263 | 2024-11-16 12:44:00 | TERRA_M-T | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | 18.7 |
| c31aefab-7ec1-3553-aefc-de2cb6486c4b | -0.75248 | -49.47248 | 2024-11-16 12:44:00 | TERRA_M-T | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 07e86bb9-239d-3ac0-bb1a-f2ef084b17a9 | -3.65734 | -42.26506 | 2024-11-16 12:44:00 | TERRA_M-T | MORRO DO CHAPÉU DO PIAUÍ | PIAUÍ | Brasil | 2206670 | 22 | 33 | nan | nan | nan | Caatinga | 247.0 |
| 3804a070-e91c-3c33-a34a-d807ef4ee904 | -3.51832 | -42.11546 | 2024-11-16 12:44:00 | TERRA_M-T | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 28.6 |


[Clique aqui para ver as próximas entradas](README63.md)
