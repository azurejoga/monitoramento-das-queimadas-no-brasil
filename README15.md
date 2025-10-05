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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 17068e5b-6878-3f5b-ab9b-6071fb827f76 | -6.3943 | -43.074 | 2025-10-05 01:10:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 64.4 |
| a6d889b8-e271-34cb-83e2-b0601e99c09f | -6.3946 | -43.0505 | 2025-10-05 01:10:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 76.2 |
| e0e75155-5259-3154-97f0-3a89cca3f49d | -5.6363 | -43.9027 | 2025-10-05 01:10:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 95.5 |
| ba143607-ab3f-3129-b065-2b217aaaef2a | -10.8379 | -57.1781 | 2025-10-05 01:10:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 47.6 |
| 5b0f1a3a-a33c-3ebb-bbc5-13d1d201439b | -6.4134 | -43.0489 | 2025-10-05 01:10:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 161.7 |
| a2ed46b1-cc93-3fb6-9736-6d1419ee661d | -13.1393 | -50.9383 | 2025-10-05 01:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 150.4 |
| eaa45f29-5e53-3f1d-86df-f38a22eef694 | -13.2741 | -47.6158 | 2025-10-05 01:10:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 70.6 |
| ece0b3e8-b69f-3336-b948-492a44875b11 | -12.4669 | -45.5155 | 2025-10-05 01:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 48.4 |
| 4ab9219c-82da-3821-b1fb-61723c316402 | -13.7102 | -51.229 | 2025-10-05 01:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 56.3 |
| 3df5a161-82b7-3aba-bdb0-f5491378d52b | -13.1397 | -50.9169 | 2025-10-05 01:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 266.4 |
| 3a3af6fa-116a-35bb-9c89-dfe644e3828f | -14.3353 | -47.6755 | 2025-10-05 01:10:00 | GOES-19 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 90.4 |
| d583d052-4084-359c-b354-0b4a3052eabd | -12.9844 | -51.0433 | 2025-10-05 01:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 66.4 |
| 6c52e252-122b-3d07-9637-d99475095cea | -11.8418 | -45.0799 | 2025-10-05 01:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 77.7 |
| e09f0fe1-4185-3548-be74-8b4ac04806a7 | -13.7098 | -51.2504 | 2025-10-05 01:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 100.2 |
| 24b80036-03b4-3151-9cda-704516a87e0b | -11.8588 | -56.8785 | 2025-10-05 01:10:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 70.8 |
| c80388d2-8a9f-381f-811d-9d51c1821572 | -11.823 | -45.0596 | 2025-10-05 01:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 86.6 |
| 458d4431-2c4e-3779-996a-e9f16a532e1a | -14.3348 | -47.6981 | 2025-10-05 01:20:00 | GOES-19 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 65.6 |
| 3c9ab3cf-3953-3eb8-9e67-4f1d57e6d92f | -15.9084 | -48.8254 | 2025-10-05 01:20:00 | GOES-19 | CORUMBÁ DE GOIÁS | GOIÁS | Brasil | 5205802 | 52 | 33 | nan | nan | nan | Cerrado | 85.0 |
| 84b26be4-4da4-33ba-b0df-07d84b133779 | -3.6013 | -51.0259 | 2025-10-05 01:20:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 49.4 |
| 184096d3-d350-3c40-879d-f6a7fce3ab60 | -6.3943 | -43.074 | 2025-10-05 01:20:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 63.9 |
| fe62b83b-1fc1-3f1e-8f28-fa2578fe0d10 | -3.6196 | -51.0461 | 2025-10-05 01:20:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 55.4 |
| 04f1b04c-e4f1-32c9-8bb7-0c1d7c11a00a | -10.4592 | -57.5029 | 2025-10-05 01:20:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 44.6 |
| 82f17f4a-1a67-36ac-958a-7a3b69e86dd8 | -8.5956 | -46.2798 | 2025-10-05 01:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 82.5 |
| 2a110d39-2b23-3330-8983-7e3ee232c43e | -6.4134 | -43.0489 | 2025-10-05 01:20:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 143.1 |
| ad4c2312-6878-3dbf-b002-7a31449d02b4 | -5.9879 | -44.3598 | 2025-10-05 01:20:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 52.6 |
| 5da2e0c3-e560-30af-becd-5396cc9e527b | -11.8588 | -56.8785 | 2025-10-05 01:20:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 75.6 |
| bb4e807a-5800-3cd9-ae35-1d8bb60d4220 | -5.6361 | -43.9258 | 2025-10-05 01:20:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 117.2 |
| 3d6bb783-92ac-320e-983b-cc7d1a5ca3af | -4.4445 | -43.2397 | 2025-10-05 01:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 100.3 |
| d23bf95e-5c98-3be8-908a-426528c75da7 | -13.1589 | -50.9144 | 2025-10-05 01:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 125.1 |
| dc878cad-2d9a-33cb-9d7d-8753e485930e | -6.3946 | -43.0505 | 2025-10-05 01:20:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 83.8 |
| 58544045-39e9-3702-a18f-b8e0c4c9148a | -13.1397 | -50.9169 | 2025-10-05 01:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 144.1 |
| 3081ed2b-e4f5-3062-b803-34bdb35b9bba | -11.8225 | -45.0827 | 2025-10-05 01:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 70.0 |
| fab439aa-9e19-389f-a1c5-4e12979edb2c | -14.6711 | -48.3381 | 2025-10-05 01:20:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 67.2 |
| 511ad09a-13e8-314c-b5b8-afb00071cf70 | -4.6505 | -43.1805 | 2025-10-05 01:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 166.4 |
| 46f05e8c-1168-364c-8c74-d635c9c6f398 | -13.14 | -50.8954 | 2025-10-05 01:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 146224d7-4ec2-3c53-9287-069b8c51509c | -4.3197 | -48.0908 | 2025-10-05 01:20:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 55.4 |
| 5c02e7e5-1c68-39c8-b835-013899a78ead | -13.1161 | -43.847 | 2025-10-05 01:20:00 | GOES-19 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 70.3 |
| bf87fd08-77d7-39c9-a116-13f29eda6cef | -13.1393 | -50.9383 | 2025-10-05 01:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 97.3 |
| 8a6048fd-e4bf-3e80-a236-ecc76a137288 | -11.8777 | -56.8769 | 2025-10-05 01:20:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 101.4 |
| 39240645-9fd5-3cb8-8585-c5a1643ceb49 | -5.6548 | -43.9244 | 2025-10-05 01:20:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 95.4 |
| e31c08d6-6b42-3796-9297-3229a30fbd68 | -4.6317 | -43.205 | 2025-10-05 01:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 74.4 |
| bbc79da1-a992-3f6e-b331-d80c1460fb42 | -14.3353 | -47.6755 | 2025-10-05 01:20:00 | GOES-19 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 126.2 |
| ad2c4629-0abb-3126-9a23-7897adabd8a4 | -14.3158 | -47.6787 | 2025-10-05 01:20:00 | GOES-19 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 64.8 |
| cb0b294d-eb5f-3d7c-8f42-7622022105a3 | -15.928 | -48.822 | 2025-10-05 01:20:00 | GOES-19 | CORUMBÁ DE GOIÁS | GOIÁS | Brasil | 5205802 | 52 | 33 | nan | nan | nan | Cerrado | 93.4 |
| 03b1f50e-344c-3f90-a800-3edd9fb111fd | -5.655 | -43.9013 | 2025-10-05 01:20:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 72.1 |
| 3236b014-b41a-3629-aacf-8d3ba6672c84 | -3.6012 | -51.0467 | 2025-10-05 01:20:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 66.5 |
| fb2ccf56-72e7-34bf-aa92-442f44bc8e39 | -4.6504 | -43.2038 | 2025-10-05 01:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 80.0 |
| 2c932fbd-a923-302a-b864-672053948dee | -13.1585 | -50.9359 | 2025-10-05 01:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 90.9 |
| ebdcfd5c-e61c-3970-9b3f-bef54ed0f1ba | -13.304 | -48.0798 | 2025-10-05 01:20:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 66.7 |
| 13eb4c86-ad83-3ba6-b199-837c7378040f | -5.6363 | -43.9027 | 2025-10-05 01:20:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 88.8 |
| 60e50272-ccfc-35e4-9680-5ac8a9457bac | -4.6318 | -43.1816 | 2025-10-05 01:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 164.1 |
| e57322cb-ac6d-30f5-a3f0-a5b6d8cdd91e | -6.4131 | -43.0724 | 2025-10-05 01:20:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 78.3 |
| 0213850d-3f73-3e95-92c1-e80cba8a9648 | -4.4445 | -43.2397 | 2025-10-05 01:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 106.9 |
| 40fe777c-e657-3a7b-a393-0c1e907e57ad | -6.1726 | -44.6432 | 2025-10-05 01:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 73.2 |
| 352f5dd8-acc0-3704-8a66-5674cf85b793 | -8.5956 | -46.2798 | 2025-10-05 01:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 67.3 |
| 80ae1188-1ece-3e1e-aacb-00c43ed6f2c9 | -17.8808 | -57.6412 | 2025-10-05 01:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 76.2 |
| 93cd33e2-8e24-3b6b-a1a8-31f4db2bcafc | -3.6012 | -51.0467 | 2025-10-05 01:30:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 68.2 |
| cc6e6bb6-f293-3bd9-8f92-59fd6e5f2fc3 | -15.9084 | -48.8254 | 2025-10-05 01:30:00 | GOES-19 | CORUMBÁ DE GOIÁS | GOIÁS | Brasil | 5205802 | 52 | 33 | nan | nan | nan | Cerrado | 75.2 |
| c1e8f59f-4ae9-334e-bc9b-41c155040613 | -5.6363 | -43.9027 | 2025-10-05 01:30:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 97.0 |
| bd267a4b-0006-32c2-a6eb-10cc570214da | -5.655 | -43.9013 | 2025-10-05 01:30:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 76.8 |
| 5e1d20bb-01b5-37af-b1bf-6785da7df6c6 | -6.1349 | -44.6689 | 2025-10-05 01:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 95.9 |
| 43bd9a82-7e02-3430-9fd7-45ae781099ce | -6.1538 | -44.6446 | 2025-10-05 01:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 216.2 |
| e14ae1b5-ac7b-371a-9f42-1a0a10e9b30c | -13.1397 | -50.9169 | 2025-10-05 01:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 75.0 |
| a933e064-ee29-3eee-b2e5-06a3460a15f5 | -4.6504 | -43.2038 | 2025-10-05 01:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 59.9 |
| 181a36b8-2abb-3021-8813-9c3d216c1931 | -14.3353 | -47.6755 | 2025-10-05 01:30:00 | GOES-19 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 117.2 |
| cf56a970-6355-37fe-bace-a4a5ef825997 | -4.6505 | -43.1805 | 2025-10-05 01:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 173.0 |
| bbdf656a-5929-3007-b6e7-9014ee2a8263 | -5.9879 | -44.3598 | 2025-10-05 01:30:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 64.5 |
| 18b59cb5-3279-3efa-9fa2-a6f8d5b1a9c9 | -6.1351 | -44.6461 | 2025-10-05 01:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 80.3 |
| c5884b6d-dcb7-3724-8a9a-c7161cea6121 | -13.1161 | -43.847 | 2025-10-05 01:30:00 | GOES-19 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 89.7 |
| 4094970e-9c3f-3df3-846d-d0f28ab6157b | -8.5384 | -46.3304 | 2025-10-05 01:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 53.4 |
| 57af1049-ab79-3f7a-bbff-ddf45fb51807 | -11.8777 | -56.8769 | 2025-10-05 01:30:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 117.6 |
| cd6bc8a1-4c7a-3485-abbb-4af3e3723c0e | -14.3158 | -47.6787 | 2025-10-05 01:30:00 | GOES-19 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 50.6 |
| 1ba760e4-0241-3f8a-8eb5-e34fd2c3e6d5 | -6.4134 | -43.0489 | 2025-10-05 01:30:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 128.3 |
| 2c465637-4cf1-3b08-905d-7633d6394f80 | -4.3197 | -48.0908 | 2025-10-05 01:30:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 64.4 |
| d725092c-c607-3e47-9643-ca1e568f2d6a | -12.4669 | -45.5155 | 2025-10-05 01:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 69.6 |
| 79d5608c-0e47-37e2-b693-62b2b32de06a | -5.6361 | -43.9258 | 2025-10-05 01:30:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 100.0 |
| 0595680e-d154-335b-a072-8616a8f5ba32 | -5.6548 | -43.9244 | 2025-10-05 01:30:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 76.0 |
| 0d9a35cf-44f4-3ba3-ba84-7fabe5693189 | -11.8225 | -45.0827 | 2025-10-05 01:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 81.0 |
| a4091fbe-fe5b-3493-a16f-84748cf9e9b5 | -14.3348 | -47.6981 | 2025-10-05 01:30:00 | GOES-19 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 72.7 |
| ffb8ab24-e3a0-3259-aa05-33a6a694ed20 | -4.6317 | -43.205 | 2025-10-05 01:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 53.3 |
| 44705d7d-96c8-35ab-a929-90ac3578acca | -11.8418 | -45.0799 | 2025-10-05 01:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 87.6 |
| db06bba9-dbbc-3828-8f99-c7e0d1d3ef43 | -6.1536 | -44.6675 | 2025-10-05 01:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 419.7 |
| 54fd805d-c9cd-39db-904b-a58b3cb87299 | -13.1589 | -50.9144 | 2025-10-05 01:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 92.0 |
| 2ba2d3ad-37ae-36fd-ae53-0c3388c0c4af | -11.823 | -45.0596 | 2025-10-05 01:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 63.9 |
| 07fc08c9-39ad-3b57-8ef4-77033177d9f4 | -13.1585 | -50.9359 | 2025-10-05 01:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 67.1 |
| 87d70fc6-f952-3b73-8188-4a8b8f774db3 | -12.9844 | -51.0433 | 2025-10-05 01:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 67.8 |
| 91ff1b8e-d055-39b1-9930-cb55f22bae7b | -3.6013 | -51.0259 | 2025-10-05 01:30:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 47.5 |
| e454aaf0-0255-326d-b150-688567fdca53 | -6.4131 | -43.0724 | 2025-10-05 01:30:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 74.2 |
| c30cf457-7ca3-34a2-b407-4f77824849ef | -4.6318 | -43.1816 | 2025-10-05 01:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 168.2 |
| f09f98e2-a28e-3a84-af12-1fa50b33bf40 | -3.6196 | -51.0461 | 2025-10-05 01:30:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 54.8 |
| a3cfe289-3083-3de2-a62a-b2b6b571faa4 | -15.928 | -48.822 | 2025-10-05 01:30:00 | GOES-19 | CORUMBÁ DE GOIÁS | GOIÁS | Brasil | 5205802 | 52 | 33 | nan | nan | nan | Cerrado | 84.5 |
| 19b2b157-cba7-31b9-a8f0-58a53e4123d2 | -6.1723 | -44.666 | 2025-10-05 01:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 167.8 |
| 90e8a9ab-fe40-3ae5-be8b-9a028c82ce7b | -6.3946 | -43.0505 | 2025-10-05 01:30:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 71.6 |
| 7d863bb5-3cf7-3f64-b831-7aa7bae95755 | -6.1538 | -44.6446 | 2025-10-05 01:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 218.5 |
| 894fea6e-52a2-34ca-9568-272b75541923 | -6.3946 | -43.0505 | 2025-10-05 01:40:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 85.0 |
| 759167cb-d2cf-314a-99e0-70e6b9ed3295 | -5.6361 | -43.9258 | 2025-10-05 01:40:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 76.1 |
| 32a8b137-9d4e-3077-ab0f-f5e3fe199420 | -11.8413 | -45.103 | 2025-10-05 01:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 72.1 |
| 4b2ed38f-ef85-3edc-89d4-c807e35e528c | -17.8808 | -57.6412 | 2025-10-05 01:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 66.8 |
| 950fb418-28ac-3003-a3fb-5b4d9c61304b | -15.6015 | -52.5102 | 2025-10-05 01:40:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 73.2 |
| 590fba63-7cf6-31e1-8be9-45208e42bf2c | -11.8777 | -56.8769 | 2025-10-05 01:40:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 114.7 |


[Clique aqui para ver as próximas entradas](README16.md)
