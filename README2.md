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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f1c98f1a-3200-3362-84ee-27160d3e2842 | -17.7453 | -57.4933 | 2024-10-25 00:06:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 75.4 |
| 876dd3dd-3bfb-39d1-8599-ebb103e88a6a | -17.7671 | -57.3673 | 2024-10-25 00:06:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 61.7 |
| 9e1a1d01-9928-3565-8872-13d87b667dc7 | -17.9268 | -57.2447 | 2024-10-25 00:06:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 76.1 |
| 827f4f70-6516-33d9-99ff-00cbb2540238 | -17.9272 | -57.224 | 2024-10-25 00:06:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 81.9 |
| 00a128d2-3827-34fa-9ae1-d323d33a0ebf | -17.9275 | -57.2034 | 2024-10-25 00:06:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 62.3 |
| 515898b7-09b3-3f48-80f5-1a2f0552c29a | -17.9469 | -57.2216 | 2024-10-25 00:06:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 64.8 |
| d3f31095-c23b-3fcd-aba6-5e8d82d29a47 | -18.0056 | -57.2555 | 2024-10-25 00:06:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 91.6 |
| a8a412b6-6671-37b5-b581-3b5877e840e2 | -18.0254 | -57.253 | 2024-10-25 00:06:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 121.2 |
| 31addd77-635d-3210-a570-f44296ff328d | -18.0257 | -57.2324 | 2024-10-25 00:06:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 74.9 |
| b3aee55b-8da0-39b4-a638-185b0c38a6d8 | -18.0452 | -57.2506 | 2024-10-25 00:06:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 73.0 |
| 5744f5c9-92ca-3495-9d34-956710c1cf74 | -18.3203 | -56.2195 | 2024-10-25 00:06:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 54.5 |
| 46852255-3f8e-3235-90d8-6e90cc48f356 | -1.0445 | -47.6237 | 2024-10-25 00:15:11 | GOES-16 | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 51.8 |
| c1899883-2ac9-3766-8d47-f8340ef2cb12 | -1.0733 | -53.658 | 2024-10-25 00:15:11 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 46.4 |
| ef838dec-876b-31a2-9f38-0c5aeebdb8b0 | -1.1834 | -53.6771 | 2024-10-25 00:15:12 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 88.8 |
| 868ec03a-28fd-3a9c-bb67-3b96bdaf2478 | -1.1834 | -53.6569 | 2024-10-25 00:15:12 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 126.5 |
| fc5e0e9b-6964-3f9e-84b9-192aa9094a76 | -2.6192 | -52.4564 | 2024-10-25 00:15:20 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 90.1 |
| 4c64c6e2-19c5-34fd-9555-68af917cd4f1 | -2.6193 | -52.4359 | 2024-10-25 00:15:20 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 96.4 |
| 7ce6a38c-ef74-3def-b037-5829d020b8d4 | -2.6297 | -49.247 | 2024-10-25 00:15:20 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 98.9 |
| 08060cec-166e-3455-a221-b2740b205809 | -2.6482 | -49.2465 | 2024-10-25 00:15:20 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 132.7 |
| db9aaec9-56e0-3ddd-b0b2-c04e965ddcef | -2.796 | -49.2636 | 2024-10-25 00:15:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 168.4 |
| 6382b220-b2d6-3167-8ec2-f235174a737a | -2.796 | -49.2424 | 2024-10-25 00:15:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 201.7 |
| 6ead4a4a-1065-35c5-8bde-e26c95a90218 | -2.8144 | -49.2631 | 2024-10-25 00:15:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 257.2 |
| f25b3c35-6308-3d05-847b-1eefff3dde63 | -2.8145 | -49.2418 | 2024-10-25 00:15:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 301.9 |
| 7358a119-1200-35ce-9ab7-460189b4cd66 | -2.9578 | -50.4198 | 2024-10-25 00:15:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 68.1 |
| 2167eded-eba3-3f1e-8c67-04ae42f1eb6d | -3.1071 | -45.7232 | 2024-10-25 00:15:23 | GOES-16 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 57.4 |
| f7bb053e-8147-3487-bf30-c5902d27cb12 | -3.1072 | -45.7009 | 2024-10-25 00:15:23 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 93.0 |
| 804fab0a-e3a9-3f1e-b71d-9afc18ee1371 | -3.1257 | -45.7225 | 2024-10-25 00:15:23 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 9b2cd212-18d6-3e7a-b2b1-93a256b6ac37 | -3.1258 | -45.7002 | 2024-10-25 00:15:23 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 106.0 |
| 41492013-ec5d-31f5-8d92-febd78e79e19 | -3.2366 | -45.83 | 2024-10-25 00:15:23 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 82.4 |
| 141b297c-4247-37ca-8cfe-1883c7faaca9 | -3.2368 | -45.8077 | 2024-10-25 00:15:23 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 221.9 |
| 5e402f8d-bc7b-39c4-a290-3f5d20a1e4bd | -3.2552 | -45.8293 | 2024-10-25 00:15:24 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 92.7 |
| f89a7233-66a0-3f7a-a232-a334ff5bd94b | -3.2553 | -45.807 | 2024-10-25 00:15:24 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 258.1 |
| 875abf2d-7765-3d0b-90a8-4a47f3279cb5 | -3.3124 | -49.5235 | 2024-10-25 00:15:24 | GOES-16 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 76.7 |
| 15c757b2-387d-31d2-a140-a942a795c003 | -3.4047 | -49.5415 | 2024-10-25 00:15:24 | GOES-16 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 68.0 |
| b1ec17bd-e7a9-34eb-b7b1-3434b4494f9a | -3.4048 | -49.5203 | 2024-10-25 00:15:24 | GOES-16 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 70.3 |
| bb71eecf-43a4-3016-ab7e-6ec9a3ed5a18 | -3.4232 | -49.5409 | 2024-10-25 00:15:25 | GOES-16 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 6ad18fa6-32cc-3bdf-81e9-0fa242bef5ea | -3.4233 | -49.5197 | 2024-10-25 00:15:25 | GOES-16 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 73.0 |
| 0f35a6b2-9a43-366b-b2a4-8e215f41071c | -3.4605 | -45.6645 | 2024-10-25 00:15:25 | GOES-16 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 125.7 |
| df7db19c-2810-356f-b69b-c14335e25b51 | -3.4606 | -45.6421 | 2024-10-25 00:15:25 | GOES-16 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 74.0 |
| c01f32b4-260f-33e8-aa71-ce3992221083 | -3.4791 | -45.6637 | 2024-10-25 00:15:25 | GOES-16 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 117.2 |
| 52db3adb-1818-34d7-9dfa-297ce7265e37 | -3.4792 | -45.6413 | 2024-10-25 00:15:25 | GOES-16 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 74.1 |
| 04a0a2b1-d2ab-305d-90e9-e3ed3f847622 | -3.4951 | -54.4366 | 2024-10-25 00:15:25 | GOES-16 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 28.6 |
| 4c2bd83e-4956-3acb-9988-7581271d8c0e | -3.9394 | -46.445 | 2024-10-25 00:15:27 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 77.3 |
| d64f32ce-8d82-308e-ac31-4d3fefe8ecfd | -3.9396 | -46.4229 | 2024-10-25 00:15:27 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 92.5 |
| 039bf845-7323-3039-bf8f-946f73370ca4 | -3.958 | -46.4442 | 2024-10-25 00:15:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 87.6 |
| 8518c2dd-b0bb-31b5-927c-2f2f3c21d493 | -3.9581 | -46.422 | 2024-10-25 00:15:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 102.1 |
| aee6b52c-c817-38a9-801a-64642eeb0484 | -4.2427 | -48.5689 | 2024-10-25 00:15:29 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 615a9671-4d6b-35b1-90b6-91df112c5104 | -4.2429 | -48.5474 | 2024-10-25 00:15:29 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 117.1 |
| 1762ad51-eb6f-31b8-8629-0b7fbcaa487b | -4.244 | -48.3535 | 2024-10-25 00:15:29 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 77.2 |
| 23c0b387-a0ca-306c-8145-6851e6522fc9 | -4.2441 | -48.332 | 2024-10-25 00:15:29 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 103.0 |
| fdd38c8b-78a6-3c23-8b8f-9434a0b835cf | -4.5045 | -48.2117 | 2024-10-25 00:15:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 68.0 |
| 4af9e9ee-6c91-359c-83b7-de5ca48108c5 | -4.5231 | -48.2108 | 2024-10-25 00:15:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 60.5 |
| b048664e-50f9-32bc-a8d0-6aa88872bc23 | -4.5371 | -46.0373 | 2024-10-25 00:15:31 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 73.8 |
| e6fa1072-a229-3bc5-8a86-3ee51ed2feac | -4.58 | -48.0132 | 2024-10-25 00:15:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 96.0 |
| 26aab9e3-fee9-309a-82af-5269fc25a0f5 | -5.6589 | -47.9093 | 2024-10-25 00:15:37 | GOES-16 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 66.6 |
| 0a3909b6-d888-3909-a7ea-79f165aba0f3 | -5.8918 | -44.6418 | 2024-10-25 00:15:38 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 68.6 |
| b4ba214e-3d93-34e7-80c6-53c3f1ce6357 | -6.5219 | -60.0457 | 2024-10-25 00:15:43 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 159.6 |
| 9bca9d57-a499-35dc-9e97-5d88a67191ec | -6.522 | -60.0266 | 2024-10-25 00:15:43 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 141.2 |
| 5519a22e-d44e-3598-98a2-1a2e88f662f8 | -6.6472 | -47.8642 | 2024-10-25 00:15:43 | GOES-16 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 91.7 |
| 25c15d44-0b8f-38a4-a115-4d7f6fdf8e8d | -7.2737 | -64.6495 | 2024-10-25 00:15:47 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 77.3 |
| 741c4f47-f5fe-3686-9ed2-a2f4f290c6b2 | -7.9046 | -63.7129 | 2024-10-25 00:15:51 | GOES-16 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 51.2 |
| 6c7dea26-9956-3eb3-8c01-17696781249c | -7.923 | -63.7123 | 2024-10-25 00:15:51 | GOES-16 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 27b4bb18-b2b9-32d3-a78a-8879d246fa43 | -8.9064 | -48.544 | 2024-10-25 00:15:56 | GOES-16 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 90.3 |
| 896b8478-64fa-3fd4-a451-cdfb3b11d899 | -10.6519 | -47.9207 | 2024-10-25 00:16:05 | GOES-16 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 83.9 |
| 20cc0afb-628c-3db0-a02b-872bf7b03c1f | -11.3081 | -48.4798 | 2024-10-25 00:16:09 | GOES-16 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 63.7 |
| 334216e4-e9c2-312f-b242-745c06cf0d0a | -11.6316 | -48.4837 | 2024-10-25 00:16:11 | GOES-16 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 65.6 |
| 1993b81e-1c23-3918-bc10-b1e2c03f3f48 | -11.632 | -48.4617 | 2024-10-25 00:16:11 | GOES-16 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 75.4 |
| facce4b0-8cbe-35ab-9221-377fb2cf0961 | -11.883 | -56.4152 | 2024-10-25 00:16:13 | GOES-16 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 83.1 |
| 2f64b8f7-d826-385c-9504-19356cd0bb0b | -11.8854 | -56.2138 | 2024-10-25 00:16:13 | GOES-16 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 54.4 |
| e9c7385e-24d4-37a8-855b-ea9dcb3de3d0 | -11.902 | -56.4135 | 2024-10-25 00:16:13 | GOES-16 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 127.2 |
| c7b6e502-8c96-3ffa-805e-b14ecde56495 | -11.9022 | -56.3934 | 2024-10-25 00:16:13 | GOES-16 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 85.1 |
| 889abb88-9bb4-3d5b-a997-353e382ff4f6 | -12.4589 | -63.1895 | 2024-10-25 00:16:16 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 88.3 |
| dd258af2-a253-37bd-8077-5ccf7c65963b | -12.4591 | -63.1704 | 2024-10-25 00:16:16 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 98.3 |
| f3bdbd2c-8206-374a-8629-84c53fecb11e | -12.478 | -63.1693 | 2024-10-25 00:16:16 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 95.0 |
| 8db3aba8-fed9-3fd5-9359-cae5cc2be857 | -12.5356 | -63.051 | 2024-10-25 00:16:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 79.5 |
| 80c605bd-68af-344b-9b6e-f9c5b7118b52 | -13.1258 | -55.7147 | 2024-10-25 00:16:20 | GOES-16 | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 81.3 |
| f400bd14-58bb-3d63-af8d-9ec54bff7f4c | -13.1261 | -55.6943 | 2024-10-25 00:16:20 | GOES-16 | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 64.9 |
| edd0cd21-6f42-31ac-89b2-a12c939bec6c | -13.4769 | -61.6217 | 2024-10-25 00:16:22 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 78.2 |
| 6d3df312-cdef-395e-bc63-f91316a11002 | -13.4957 | -61.6398 | 2024-10-25 00:16:22 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 88.8 |
| efd089c8-429e-3691-95ee-4e93cdd16254 | -13.4959 | -61.6203 | 2024-10-25 00:16:22 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 136.2 |
| 36302e16-bdf6-34ce-a51c-e23fe9f8a4fa | -14.1144 | -44.3072 | 2024-10-25 00:16:24 | GOES-16 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 103.5 |
| 5d3e4177-c818-34e5-a090-0cb3f2344131 | -16.94 | -57.5268 | 2024-10-25 00:16:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 103.1 |
| e19b452e-aa10-3080-b6c7-27bd209041a7 | -16.9596 | -57.5245 | 2024-10-25 00:16:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 137.6 |
| b8dc58df-af34-30ad-a69f-7e861550505b | -16.9792 | -57.5223 | 2024-10-25 00:16:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 136.2 |
| cac87f5e-1a3e-3024-aa7b-46951cfac7b7 | -17.2147 | -57.4949 | 2024-10-25 00:16:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 67.7 |
| c1e0afa8-1095-3829-bf87-2298a5932cd3 | -17.2186 | -57.2485 | 2024-10-25 00:16:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 81.5 |
| bcbacde9-5718-3dbf-ba70-c64ee496cdb5 | -17.2537 | -57.5108 | 2024-10-25 00:16:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 125.0 |
| cbb0215d-56b4-3fe6-9bfb-8defb4006a21 | -17.254 | -57.4903 | 2024-10-25 00:16:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 75.9 |
| f087d170-a9d9-3ab9-b991-bb85626ebdbb | -17.2963 | -57.3008 | 2024-10-25 00:16:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 82.5 |
| 6b713c84-fb07-325b-8c90-98ddeceee5bd | -17.9272 | -57.224 | 2024-10-25 00:16:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 105.0 |
| 90712d50-9475-3db3-b58b-7dec75bc1cfb | -17.9275 | -57.2034 | 2024-10-25 00:16:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 87.6 |
| ca671435-13ad-3b94-bee9-959611b5befa | -17.9469 | -57.2216 | 2024-10-25 00:16:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 78.2 |
| 9101fd51-47f3-3d2a-b221-7865cdfab223 | -18.1223 | -57.3647 | 2024-10-25 00:16:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 52.4 |
| 53f43bc1-60ac-3b28-933b-e0c61d9f9aeb | -18.1421 | -57.3622 | 2024-10-25 00:16:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 70.8 |
| efa98adf-de64-3b93-a7e1-534b62aa4683 | -18.1424 | -57.3415 | 2024-10-25 00:16:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 42.2 |
| f3ce1518-8651-318d-8d1f-f83d3b4e33fa | -19.59625 | -40.72154 | 2024-10-25 00:24:00 | TERRA_M-M | COLATINA | ESPÍRITO SANTO | Brasil | 3201506 | 32 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 9dba376d-500d-36b8-bb9e-220ae40511a4 | -16.12486 | -40.6055 | 2024-10-25 00:24:00 | TERRA_M-M | ALMENARA | MINAS GERAIS | Brasil | 3101706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 45a0830a-0bb8-35af-a4dc-4ba5633b35d1 | -15.80812 | -42.5161 | 2024-10-25 00:24:00 | TERRA_M-M | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 2a492f46-299c-3e9a-b243-53e4327bc66c | -15.78348 | -41.29158 | 2024-10-25 00:24:00 | TERRA_M-M | PEDRA AZUL | MINAS GERAIS | Brasil | 3148707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| 6358a18e-4895-38e3-aec6-acd0bdfe3ba2 | -15.77421 | -41.29268 | 2024-10-25 00:24:00 | TERRA_M-M | PEDRA AZUL | MINAS GERAIS | Brasil | 3148707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.2 |


[Clique aqui para ver as próximas entradas](README3.md)
