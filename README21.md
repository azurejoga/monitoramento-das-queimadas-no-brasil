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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e92c1ddb-bc0a-35ea-8099-fbbf609ddac2 | -16.7575 | -56.7081 | 2024-10-09 00:46:41 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 77.2 |
| d768417f-137c-37e7-9c42-e647171c45fa | -16.777 | -56.7057 | 2024-10-09 00:46:41 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 63.4 |
| d379123e-189d-3c05-8e5f-0497b2735979 | -16.8743 | -56.7352 | 2024-10-09 00:46:41 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 88.8 |
| 114ccda1-5bf3-3012-bff7-d8c9b6b5f15c | -16.8747 | -56.7146 | 2024-10-09 00:46:41 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 79.4 |
| af370b56-e992-364e-94f6-0683ee6cb27b | -16.9518 | -56.7875 | 2024-10-09 00:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 90.8 |
| 32580ab7-0ad8-3e41-abf1-2c4f8a92dcc5 | -16.9521 | -56.7669 | 2024-10-09 00:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 78.7 |
| a840d4cf-f914-3268-aacb-27bd0dd79593 | -17.0878 | -56.8534 | 2024-10-09 00:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 98.1 |
| 082fc1e3-f2b2-3e3d-98ca-865aa1f22c2f | -17.1074 | -56.851 | 2024-10-09 00:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 86.6 |
| 23e04b10-b9de-3313-8aad-7797a0170a40 | -17.1271 | -56.8486 | 2024-10-09 00:46:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 87.5 |
| 840b7b03-b09d-3719-bf70-00aac9563308 | -17.1467 | -56.8463 | 2024-10-09 00:46:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 97.3 |
| bbfbdcb2-74f2-3d55-b960-d031bdd81c6e | -17.1471 | -56.8256 | 2024-10-09 00:46:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 88.5 |
| b2cca289-30e2-3550-a6f1-1c23efae011a | -17.1588 | -56.1222 | 2024-10-09 00:46:43 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 88.4 |
| b93c788e-5a59-37da-9597-e5d0794ae266 | -17.1591 | -56.1014 | 2024-10-09 00:46:43 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 52.7 |
| e999f17a-856c-382d-a37b-c2f2bb2d7b4e | -17.1977 | -57.333 | 2024-10-09 00:46:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 71.8 |
| bacc41f8-2166-3742-8511-436aad9434fa | -17.2173 | -57.3307 | 2024-10-09 00:46:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 84.4 |
| f01f806f-4e51-3f7a-9434-8eb6723aea7a | -17.3353 | -55.0156 | 2024-10-09 00:46:43 | GOES-16 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 51.4 |
| ed1ec8b0-b59c-32fd-879a-bc7852d4cbcf | -18.5993 | -57.2629 | 2024-10-09 00:46:50 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 90.9 |
| d1dca0ca-ed55-30fe-95fe-98d85325f77b | -18.5996 | -57.2422 | 2024-10-09 00:46:50 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 88.2 |
| 658c3755-8ee0-31f2-a45b-f5ba29c6b503 | -19.9924 | -42.4346 | 2024-10-09 00:46:56 | GOES-16 | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 143.8 |
| 867c2a2a-dde2-3385-9ed2-0cf124f33917 | -20.0006 | -42.1799 | 2024-10-09 00:46:56 | GOES-16 | MANHUAÇU | MINAS GERAIS | Brasil | 3139409 | 31 | 33 | nan | nan | nan | Mata Atlântica | 92.3 |
| 1fd5079d-2314-3ada-aa11-ec1836dfbaea | -20.0122 | -42.4541 | 2024-10-09 00:46:56 | GOES-16 | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 110.0 |
| 92352693-df8c-3cc4-8806-a23df9b11cfa | -20.013 | -42.4287 | 2024-10-09 00:46:56 | GOES-16 | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 183.4 |
| e279e40b-85d5-3191-b51b-d655e39e521f | -20.1087 | -48.8261 | 2024-10-09 00:46:57 | GOES-16 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 115.3 |
| 87cefd19-4bed-3675-bb28-eb471fa70b02 | -20.1291 | -48.8217 | 2024-10-09 00:46:58 | GOES-16 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 95.2 |
| 75e9375e-f7fa-3459-8472-23f7f8256cac | -20.2915 | -43.9444 | 2024-10-09 00:46:58 | GOES-16 | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 110.8 |
| 51712794-c72b-39c4-9666-e10e1c6ecdcd | -20.3346 | -48.7307 | 2024-10-09 00:46:59 | GOES-16 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 442.3 |
| 96ecedd0-fe14-3664-a719-5be37e62717a | -20.3352 | -48.7076 | 2024-10-09 00:46:59 | GOES-16 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 407.6 |
| 0a59e9c2-4a90-38bf-95a8-055ca6952f81 | -20.3551 | -48.7262 | 2024-10-09 00:46:59 | GOES-16 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 779.1 |
| dd1c3541-f1f2-3b8c-8d33-014aeeba22ba | -20.3557 | -48.7031 | 2024-10-09 00:46:59 | GOES-16 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 580.9 |
| 78ef80b9-0003-3d11-893b-18ac53bed420 | -20.3755 | -48.7217 | 2024-10-09 00:46:59 | GOES-16 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 186.0 |
| 905381f1-130d-363b-b89b-40f28cd35120 | -20.3761 | -48.6986 | 2024-10-09 00:46:59 | GOES-16 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 134.4 |
| be4a280b-8a9b-385e-8902-c648458ae6fb | -20.4133 | -48.8282 | 2024-10-09 00:46:59 | GOES-16 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 109.2 |
| 1e36cc6d-ed3b-3bea-acd9-3bbebbd56577 | -20.7839 | -47.2559 | 2024-10-09 00:47:01 | GOES-16 | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 357.0 |
| f7c18d12-4b93-370c-8fad-6331128c2083 | -20.7846 | -47.2323 | 2024-10-09 00:47:01 | GOES-16 | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 290.1 |
| 4b8d49be-d734-3584-b27c-aa9b5af90d87 | -20.8045 | -47.251 | 2024-10-09 00:47:01 | GOES-16 | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 181.8 |
| bcf7bfbf-3248-3d92-b662-da168584916d | -20.8052 | -47.2273 | 2024-10-09 00:47:01 | GOES-16 | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 159.5 |
| 708bf211-f66b-329f-9e38-ae95f66cdf81 | -21.6259 | -44.6329 | 2024-10-09 00:47:05 | GOES-16 | MINDURI | MINAS GERAIS | Brasil | 3141900 | 31 | 33 | nan | nan | nan | Mata Atlântica | 68.3 |
| ad8def02-44b0-3756-b979-4fbc47b6257a | -21.572 | -46.9898 | 2024-10-09 00:47:05 | GOES-16 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 119.0 |
| a3178bbf-f330-3585-afdf-3fb80681ff36 | -21.5727 | -46.9659 | 2024-10-09 00:47:05 | GOES-16 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 179.5 |
| 37038e32-9513-394f-82c1-94a5042879dd | -21.5656 | -47.8878 | 2024-10-09 00:47:05 | GOES-16 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 94.8 |
| 6faf54c8-4212-30da-818c-a57311d37675 | -21.5857 | -47.9063 | 2024-10-09 00:47:05 | GOES-16 | RINCÃO | SÃO PAULO | Brasil | 3543709 | 35 | 33 | nan | nan | nan | Cerrado | 93.4 |
| dd9a60c6-f056-3dcd-8a8a-1831fd423094 | -21.5864 | -47.8827 | 2024-10-09 00:47:05 | GOES-16 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 148.7 |
| 442beaaa-1fa5-3c6c-a00c-492357ef99a9 | -21.5871 | -47.8591 | 2024-10-09 00:47:05 | GOES-16 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 74.3 |
| 4d40f7bd-98c0-3279-8df9-c0bce5888bf2 | -21.8165 | -49.1774 | 2024-10-09 00:47:06 | GOES-16 | REGINÓPOLIS | SÃO PAULO | Brasil | 3542503 | 35 | 33 | nan | nan | nan | Mata Atlântica | 63.0 |
| 28deb968-8ba6-3444-8d3f-404c54acc4ae | -21.8172 | -49.1541 | 2024-10-09 00:47:06 | GOES-16 | REGINÓPOLIS | SÃO PAULO | Brasil | 3542503 | 35 | 33 | nan | nan | nan | Mata Atlântica | 65.8 |
| 5d24e007-b314-3e36-bb7f-3cb18c8f193e | -21.8373 | -49.1726 | 2024-10-09 00:47:06 | GOES-16 | REGINÓPOLIS | SÃO PAULO | Brasil | 3542503 | 35 | 33 | nan | nan | nan | Mata Atlântica | 62.6 |
| a2d4b42b-9b53-3623-bed7-17b4f62de2c8 | -21.838 | -49.1493 | 2024-10-09 00:47:06 | GOES-16 | IACANGA | SÃO PAULO | Brasil | 3519105 | 35 | 33 | nan | nan | nan | Mata Atlântica | 68.4 |
| d473e0a9-85c1-3aff-85bb-70012d833ebd | -22.813 | -48.4462 | 2024-10-09 00:47:11 | GOES-16 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 67.9 |
| 1058dbf8-0a8c-3111-9606-bfa1095f9a65 | -22.8137 | -48.4225 | 2024-10-09 00:47:11 | GOES-16 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 90.4 |
| 7e9ccd6c-1a3c-330a-ab33-0853365e4e96 | -1.11 | -53.6173 | 2024-10-09 00:55:12 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 111.2 |
| ac1e8fea-dc1e-3591-ae61-1b458ee0db9b | -1.1284 | -53.6171 | 2024-10-09 00:55:12 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 34a227aa-1437-30ce-b6e7-93be15f870a1 | -2.3535 | -48.9986 | 2024-10-09 00:55:19 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 47.2 |
| 697779e1-6450-30e4-93e6-92200f36ccbc | -3.8007 | -41.6229 | 2024-10-09 00:55:27 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 55.4 |
| 483318be-ea8b-30e5-9000-ea6a72bad50e | -3.8008 | -41.5989 | 2024-10-09 00:55:27 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 67.4 |
| b655c448-1062-345c-b91a-54c724e5e918 | -3.8196 | -41.5979 | 2024-10-09 00:55:28 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 86.5 |
| 784d25da-bd28-3a53-8d06-9affef9563bb | -3.9021 | -46.4689 | 2024-10-09 00:55:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 80.4 |
| 76de7fae-1096-363a-bf05-23dbcd8179d6 | -3.9023 | -46.4467 | 2024-10-09 00:55:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 95.9 |
| 4feb96fb-2677-3de1-803f-d25c64a5940a | -3.9207 | -46.468 | 2024-10-09 00:55:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 59.4 |
| a70decfa-a37a-3cbf-82a7-beb91d301dbc | -3.9208 | -46.4459 | 2024-10-09 00:55:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 97.8 |
| fed9c769-441e-33c4-b648-7da9c1269b40 | -3.9393 | -46.4672 | 2024-10-09 00:55:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 77.6 |
| 2cfae407-51ff-3faa-a1ef-6791e9b2a3fa | -3.9394 | -46.445 | 2024-10-09 00:55:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 125.7 |
| 64098651-53bb-35ba-8322-5452e2964316 | -6.7613 | -60.0751 | 2024-10-09 00:55:45 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 41.3 |
| c8b335ef-1981-3c21-a366-0359b21f822c | -6.7614 | -60.0559 | 2024-10-09 00:55:45 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 176.5 |
| fa93f99c-c1f9-33b5-88cb-8810643a3163 | -6.7615 | -60.0367 | 2024-10-09 00:55:45 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 78.9 |
| 615537b4-9e57-3b86-b0a8-53e422d3d224 | -6.7797 | -60.0744 | 2024-10-09 00:55:45 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 204cb97a-9dde-3c6c-ae87-3dc808a358c0 | -6.7798 | -60.0552 | 2024-10-09 00:55:45 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 268.2 |
| 5f1726ce-0c8f-3730-96ff-65a221503447 | -6.7799 | -60.036 | 2024-10-09 00:55:45 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 119.8 |
| 34f8e931-bd76-32e8-bca5-d1e4bcabc01d | -7.0231 | -59.4303 | 2024-10-09 00:55:46 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 22.7 |
| c0657d23-f5e1-3e82-8ae8-f5565de64cea | -7.0232 | -59.4111 | 2024-10-09 00:55:46 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 25.7 |
| ac749efe-4c9c-33f4-8218-e9e55767060f | -7.1871 | -59.7893 | 2024-10-09 00:55:47 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 39.1 |
| 87c81c0d-240d-316d-be85-b87492174290 | -7.1873 | -59.7701 | 2024-10-09 00:55:47 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 45.6 |
| d91037af-6ceb-3037-802f-7930e4a0751f | -7.2056 | -59.7886 | 2024-10-09 00:55:47 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 28.9 |
| 49484cd0-e24f-3f31-9428-fe471504c6ba | -7.2057 | -59.7693 | 2024-10-09 00:55:47 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 36.3 |
| 4a57be00-d048-3b18-8f06-b99fafdb086a | -7.2435 | -59.633 | 2024-10-09 00:55:48 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 64.2 |
| 68bdde72-1e67-3294-aae1-7151a6b47279 | -7.2619 | -59.6323 | 2024-10-09 00:55:48 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 33.5 |
| 54233518-11fa-3bb2-ae2a-888116e4bd91 | -8.4919 | -48.6476 | 2024-10-09 00:55:54 | GOES-16 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Amazônia | 240.4 |
| e4bfcca3-b12a-3b98-8754-47c072505063 | -8.4921 | -48.6259 | 2024-10-09 00:55:54 | GOES-16 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Amazônia | 165.3 |
| 6d5881da-6bd5-38fb-99db-c7526471b759 | -8.5107 | -48.6459 | 2024-10-09 00:55:54 | GOES-16 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Amazônia | 93.0 |
| 60cabf21-731e-30c3-97c4-eac3feb87c85 | -8.5109 | -48.6242 | 2024-10-09 00:55:54 | GOES-16 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Amazônia | 65.5 |
| 708bcc39-bd5a-3831-8645-fb965c945e89 | -9.9292 | -58.1301 | 2024-10-09 00:56:03 | GOES-16 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 33.5 |
| 56e4ef9d-bfc6-34d3-bf14-43c185bacfe4 | -10.3656 | -64.8262 | 2024-10-09 00:56:06 | GOES-16 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 51.8 |
| c1eefb31-7b8e-39c8-9225-cfe2779192db | -10.3894 | -61.2502 | 2024-10-09 00:56:06 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 75.0 |
| 75cac578-b415-3b74-992a-825e7595af7c | -10.3895 | -61.231 | 2024-10-09 00:56:06 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 67.8 |
| aafb6eec-0bae-34f5-9da4-493d4af13376 | -10.3843 | -64.8255 | 2024-10-09 00:56:06 | GOES-16 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 54.6 |
| b42042e2-7734-3eac-a877-c1f7dbdc3ef2 | -10.4287 | -60.9979 | 2024-10-09 00:56:06 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 8f956b47-8358-3f20-8fd9-c9065ef30a24 | -10.6256 | -55.9154 | 2024-10-09 00:56:07 | GOES-16 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 14e4bcc1-a628-3c59-9e98-765130e065cd | -10.5943 | -64.024 | 2024-10-09 00:56:07 | GOES-16 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 72.4 |
| a89d6d10-8994-3c35-98ff-dd45d05aa378 | -10.8754 | -63.9169 | 2024-10-09 00:56:08 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 124.8 |
| 42c541df-f8d9-3749-8ec1-8981e31a5b1b | -10.8755 | -63.8979 | 2024-10-09 00:56:08 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 101.8 |
| b1d058c9-dabf-364b-8e12-32466065ee22 | -10.8925 | -64.1623 | 2024-10-09 00:56:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 79.0 |
| 0964f0f4-ab78-3de7-8cd9-af245d50d6cd | -10.8926 | -64.1434 | 2024-10-09 00:56:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 70.9 |
| a34ce3f7-4d91-339f-bb1a-8dfc8491f8dd | -10.8941 | -63.916 | 2024-10-09 00:56:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 85.8 |
| fc52a765-c3fc-38f5-9962-a6bb3a33db18 | -10.9112 | -64.1615 | 2024-10-09 00:56:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 145.1 |
| 078d98dd-d26e-3e53-891f-eecf891fcaca | -10.9113 | -64.1426 | 2024-10-09 00:56:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 147.6 |
| 2569e82d-2cbe-34e9-9daa-54c37ba920a5 | -10.9299 | -64.1607 | 2024-10-09 00:56:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 76.4 |
| e4d62bc1-6bb6-3431-ad35-ffc578178eef | -10.9301 | -64.1417 | 2024-10-09 00:56:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 77.1 |
| 85e28372-cb83-3af5-912f-3734181f8a45 | -11.3283 | -50.9805 | 2024-10-09 00:56:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 46.0 |
| bb715f48-fee7-3bd9-a936-7fdc99ee1deb | -11.3286 | -50.9592 | 2024-10-09 00:56:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 53.0 |
| fe828fd6-c3c1-3105-b073-2e020afa52c0 | -11.3838 | -51.0807 | 2024-10-09 00:56:11 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 42.7 |
| 73acb912-1c5b-309a-b21a-641b554334fa | -11.464 | -49.4853 | 2024-10-09 00:56:11 | GOES-16 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 42.3 |


[Clique aqui para ver as próximas entradas](README22.md)
