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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1cd0c023-e1c0-3ad2-81d2-fafb42968c50 | -7.8009 | -54.695999 | 2024-09-27 00:35:35 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5b2f343e-30e9-375b-9604-78da85aa2555 | -7.8037 | -54.709301 | 2024-09-27 00:35:35 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 652ab015-f62c-3468-91b9-f94416ae2b40 | -7.7438 | -54.7635 | 2024-09-27 00:35:36 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1c5e755a-288c-3511-81d9-b81f657f1580 | -5.753 | -45.791 | 2024-09-27 00:35:37 | METOP-B | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 61e1ac57-6bc3-3971-90e5-87bace86dd03 | -5.7549 | -45.799 | 2024-09-27 00:35:37 | METOP-B | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f326ae3d-8f94-39ff-99bb-af8786b2f99a | -5.7432 | -45.793301 | 2024-09-27 00:35:37 | METOP-B | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f0713abf-c100-3c4c-9dfa-2feb2c832ac6 | -5.7451 | -45.8013 | 2024-09-27 00:35:37 | METOP-B | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 28fec8ac-1fbb-3d0f-88ee-243dfd0dee36 | -6.1532 | -47.676601 | 2024-09-27 00:35:37 | METOP-B | MAURILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1712801 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a6919684-2b9c-38aa-b57f-0e58b13909b5 | -6.1548 | -47.683498 | 2024-09-27 00:35:37 | METOP-B | MAURILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1712801 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 14149332-ebb7-3adb-8241-cf1139546e67 | -6.1564 | -47.690498 | 2024-09-27 00:35:37 | METOP-B | MAURILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1712801 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9edb8642-afe5-39d5-98b0-5b2a90c17e8d | -5.8344 | -46.369099 | 2024-09-27 00:35:37 | METOP-B | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 317b2c71-7e20-3c9b-a2c7-6799f1e91114 | -5.8361 | -46.376701 | 2024-09-27 00:35:37 | METOP-B | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b6ef331a-eca2-31e9-bb1c-0f0f5cd7e2dd | -6.9626 | -51.639599 | 2024-09-27 00:35:38 | METOP-B | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7e7dda80-0239-397f-90fa-9e00313c7e3c | -6.9644 | -51.647999 | 2024-09-27 00:35:38 | METOP-B | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f0f122fb-8eac-3f3b-b6f4-13dd73028fba | -5.7548 | -63.1572 | 2024-09-27 00:35:39 | GOES-16 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 51.0 |
| 0525e88d-1ed8-3920-81b9-139e1cd7f45a | -5.7549 | -63.1384 | 2024-09-27 00:35:39 | GOES-16 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 09368f6b-18ad-34d3-9b90-40d32dfabec4 | -6.1185 | -48.069599 | 2024-09-27 00:35:39 | METOP-B | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7294b64d-203d-3d19-85d9-8721ecff457d | -6.12 | -48.0765 | 2024-09-27 00:35:39 | METOP-B | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 08b2a4eb-6c8c-39bf-98f7-9872b5920a1e | -5.7289 | -46.4487 | 2024-09-27 00:35:39 | METOP-B | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 73bd1773-2da6-33b3-bf03-82355e3626e5 | -6.0659 | -44.0316 | 2024-09-27 00:35:40 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 60.5 |
| 69b71911-3034-347c-aa77-d0568247e4d6 | -5.7076 | -46.445599 | 2024-09-27 00:35:40 | METOP-B | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7c83bcf4-8411-3a3d-8d72-f0f6176bf0c0 | -5.6961 | -46.4403 | 2024-09-27 00:35:40 | METOP-B | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9cc33d8b-c930-3f2e-8248-123b0dae5226 | -5.6978 | -46.4478 | 2024-09-27 00:35:40 | METOP-B | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| afdd21bd-057a-39b5-ad0b-74345daf9140 | -5.9689 | -64.85 | 2024-09-27 00:35:41 | GOES-16 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 608d4b4e-362b-3a6d-9408-0b5b1da8a46c | -5.969 | -64.8314 | 2024-09-27 00:35:41 | GOES-16 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 172.4 |
| 6f0dc8ab-ffd0-38c9-89e9-59428a8a7675 | -5.969 | -64.8128 | 2024-09-27 00:35:41 | GOES-16 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 49.1 |
| 021a1fbb-4f0e-3dab-ae64-bc12c0783d19 | -5.9873 | -64.8496 | 2024-09-27 00:35:41 | GOES-16 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 83.2 |
| ef871618-e74a-3437-81f8-7515f81ad722 | -5.9873 | -64.831 | 2024-09-27 00:35:41 | GOES-16 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 200.7 |
| e977076d-ab05-32ed-8aa6-519533a7d628 | -5.9874 | -64.8124 | 2024-09-27 00:35:41 | GOES-16 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 0fe44054-052d-36ad-a744-528116490bc1 | -6.1173 | -51.1185 | 2024-09-27 00:35:41 | GOES-16 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 50c8287b-9310-3b58-b514-7520bfd26631 | -5.0162 | -43.773701 | 2024-09-27 00:35:41 | METOP-B | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 34fabdca-a351-3eaa-b0a3-e746abd1a04a | -5.0187 | -43.784199 | 2024-09-27 00:35:41 | METOP-B | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4cad5275-29cb-3e9f-b7e2-95be23d57ed3 | -5.0212 | -43.794701 | 2024-09-27 00:35:41 | METOP-B | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ecb880ff-1f54-3c0b-aca6-5cd39ab1c6d7 | -5.0089 | -43.786499 | 2024-09-27 00:35:41 | METOP-B | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8422dffb-11c2-3898-aaeb-d6938f79685b | -5.0114 | -43.797001 | 2024-09-27 00:35:41 | METOP-B | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5d90e8f2-1674-3242-8761-ca819826e1e0 | -5.4197 | -45.463501 | 2024-09-27 00:35:41 | METOP-B | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7ce1c97a-5981-3f8d-a67a-1dfd2e2075bc | -5.4216 | -45.471901 | 2024-09-27 00:35:41 | METOP-B | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3e7a73f4-b477-3563-9877-4b451bf7c92d | -5.5752 | -46.138199 | 2024-09-27 00:35:41 | METOP-B | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4ee1574f-89e9-3c9b-afc6-29d26fda4eee | -5.577 | -46.146 | 2024-09-27 00:35:41 | METOP-B | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2e69ba62-ec84-39d4-a80d-6a5114d012ef | -5.1919 | -44.924999 | 2024-09-27 00:35:42 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 928a394e-fe61-31c6-be68-88cd552954d3 | -5.194 | -44.933998 | 2024-09-27 00:35:42 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e61d9451-2e48-3620-acfb-6e863cbe63a4 | -5.5035 | -46.3647 | 2024-09-27 00:35:43 | METOP-B | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 66f4a258-5801-3550-8a3f-8831f620fe69 | -5.5052 | -46.372299 | 2024-09-27 00:35:43 | METOP-B | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3e4cab29-1e24-3a47-b774-11f148e603d1 | -5.7226 | -47.3237 | 2024-09-27 00:35:43 | METOP-B | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7cd6fb65-e846-3dc7-8e0f-7f8393c88de4 | -5.8753 | -48.088001 | 2024-09-27 00:35:43 | METOP-B | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 75aab88f-4e2a-3c7c-9dd3-48457e430c4e | -5.8769 | -48.094799 | 2024-09-27 00:35:43 | METOP-B | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 350ab21e-6209-3d3e-9caf-1f4039e6aae5 | -5.8655 | -48.090199 | 2024-09-27 00:35:43 | METOP-B | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 900e41b9-99ee-3fbd-afcb-119b2e76a06a | -5.8671 | -48.097 | 2024-09-27 00:35:43 | METOP-B | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 48ed3daa-0f46-38be-8f69-65ed9277f206 | -4.7839 | -43.7048 | 2024-09-27 00:35:44 | METOP-B | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 405a6c80-faa9-3739-b872-a3e1f3d0f568 | -5.2359 | -45.4263 | 2024-09-27 00:35:44 | METOP-B | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8bddd9d6-eec2-340e-8290-6c1bb46c31b8 | -5.2378 | -45.434799 | 2024-09-27 00:35:44 | METOP-B | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9c8c33b1-b146-3cff-b5fd-66a69eda64e1 | -5.2398 | -45.443199 | 2024-09-27 00:35:44 | METOP-B | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 36c18cbc-f95f-36fd-95af-ecee334c25b2 | -6.8199 | -63.1651 | 2024-09-27 00:35:45 | GOES-16 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 121.5 |
| 77b44c3e-2790-3992-8ca7-41598957470c | -6.82 | -63.1463 | 2024-09-27 00:35:45 | GOES-16 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 87.3 |
| f15fbb87-f750-310c-a142-bb973d883dd6 | -4.7742 | -43.7071 | 2024-09-27 00:35:45 | METOP-B | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1f8efd2b-1c47-30c7-8735-dada0cb3bbbc | -4.7767 | -43.7178 | 2024-09-27 00:35:45 | METOP-B | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| cda7d1da-9ff2-3992-90a4-232dfa96e3dc | -7.2918 | -55.084499 | 2024-09-27 00:35:45 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d5a78843-ecf7-3492-9210-6cc5fe9556aa | -7.2947 | -55.098301 | 2024-09-27 00:35:45 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 81813d06-9201-3958-8c33-ececc36d216d | -5.2432 | -45.9496 | 2024-09-27 00:35:45 | METOP-B | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a40256cc-f37b-3c53-84c3-17b03802e59d | -5.245 | -45.9576 | 2024-09-27 00:35:45 | METOP-B | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 035ef0b2-a971-3cb1-b584-554a148665ac | -6.8383 | -63.1645 | 2024-09-27 00:35:46 | GOES-16 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 57.2 |
| 4fd10b5e-1247-331c-bba1-0f47346f62ac | -6.8384 | -63.1457 | 2024-09-27 00:35:46 | GOES-16 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 53.0 |
| a5b119b2-12ce-32b2-85cb-c4a595be0ca1 | -6.8927 | -59.6475 | 2024-09-27 00:35:46 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 53.1 |
| bba74479-98ca-33e9-8a01-f6269aaaa841 | -7.1963 | -55.018398 | 2024-09-27 00:35:46 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 07d298c6-dd9a-33e0-8896-944e7982cd22 | -7.1808 | -54.993301 | 2024-09-27 00:35:46 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3deeb591-0638-3ba8-b7dc-0b71149e5821 | -7.1837 | -55.006901 | 2024-09-27 00:35:46 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c6fa7284-f06a-35b4-87e2-bd84e2fb22f2 | -7.1865 | -55.0205 | 2024-09-27 00:35:46 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 24a28f02-35db-3e69-a71d-24f731f7be49 | -7.257 | -44.9623 | 2024-09-27 00:35:47 | GOES-16 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 68.2 |
| 617ee6d7-1605-319c-b0d6-a4acdb7c5ff8 | -6.2796 | -50.866199 | 2024-09-27 00:35:47 | METOP-B | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 514020a1-6375-3e95-8ece-14c3c1da67e8 | -5.1685 | -45.983299 | 2024-09-27 00:35:47 | METOP-B | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d51e5678-d4ca-391d-9e78-c8b8fa3554af | -7.3592 | -49.5586 | 2024-09-27 00:35:48 | GOES-16 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 33.1 |
| 9a9829e4-9e9c-39e2-84be-91166b4b5109 | -7.2905 | -61.106 | 2024-09-27 00:35:48 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 73.0 |
| c963053a-0945-3290-a7a3-4a5718038086 | -7.2906 | -61.0869 | 2024-09-27 00:35:48 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 68.5 |
| 8a9090fa-05be-3870-9a6b-e8d3906b6d0a | -7.309 | -61.0862 | 2024-09-27 00:35:48 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 83.0 |
| fd3d5cd1-9cba-36fa-ba43-05789058d3f3 | -5.1061 | -45.9809 | 2024-09-27 00:35:48 | METOP-B | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f9682a7e-c386-3d08-a267-5ccf1093dbca | -6.2045 | -50.898602 | 2024-09-27 00:35:48 | METOP-B | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b8e4fec1-f364-370f-bdee-6c04b05fc5bb | -6.2062 | -50.9063 | 2024-09-27 00:35:48 | METOP-B | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 665610bb-b7da-3494-b9d0-004b4aef1bdd | -6.1947 | -50.900799 | 2024-09-27 00:35:48 | METOP-B | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 94cb7c75-f327-36ab-b47f-3c43fe081790 | -6.1964 | -50.908501 | 2024-09-27 00:35:48 | METOP-B | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1d93eb7f-4aa4-348e-b151-a7d8b0dc1279 | -4.7668 | -44.646702 | 2024-09-27 00:35:48 | METOP-B | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 716a5042-ac0d-3fd8-a5d4-c585b45392dc | -6.1751 | -50.905102 | 2024-09-27 00:35:48 | METOP-B | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8266105a-7ee4-34cb-8d23-2d469e92b8e3 | -7.4605 | -60.4114 | 2024-09-27 00:35:49 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 78.4 |
| 7b0eff98-1610-3e79-ab1f-7d4676deb55b | -7.4606 | -60.3923 | 2024-09-27 00:35:49 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 78.8 |
| 6a2432e6-31b3-3e84-8f72-f132a8e923cd | -7.479 | -60.4107 | 2024-09-27 00:35:49 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 56.3 |
| db156a16-b53e-32ef-bedb-0d46a1c24fdf | -7.4791 | -60.3915 | 2024-09-27 00:35:49 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 27d8cb7a-eea9-3557-8a2f-4c1bf056e1d9 | -7.5289 | -61.3825 | 2024-09-27 00:35:49 | GOES-16 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 87.5 |
| d201f266-93a9-303c-b33b-4a1fa79f0e16 | -7.529 | -61.3635 | 2024-09-27 00:35:49 | GOES-16 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 66dfaae4-c611-3a52-ae24-edfd636f3621 | -5.397 | -47.523399 | 2024-09-27 00:35:49 | METOP-B | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4bc4cb06-b660-388c-9b36-e4895a381bba | -6.1328 | -50.9464 | 2024-09-27 00:35:49 | METOP-B | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d0becca3-76fb-36af-923b-d1de5f01df3b | -6.123 | -50.948502 | 2024-09-27 00:35:49 | METOP-B | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6f932056-19d9-3f03-967a-c89519f812ba | -6.1247 | -50.9562 | 2024-09-27 00:35:49 | METOP-B | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9301aa11-20da-3d26-bd37-9811642b705e | -7.5474 | -61.3818 | 2024-09-27 00:35:50 | GOES-16 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 70.0 |
| b76efb83-f572-304a-b0ec-c6b29be5a63f | -7.5703 | -60.5984 | 2024-09-27 00:35:50 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 86.8 |
| 124f1447-e3ff-38d8-8ff1-026e5122abbd | -7.5887 | -60.5976 | 2024-09-27 00:35:50 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 109.9 |
| 2578dab6-b039-310f-a629-b929db8c400f | -7.5888 | -60.5785 | 2024-09-27 00:35:50 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 68.3 |
| bfdc7c15-fc2b-37f8-bbf9-84cd336a9a49 | -4.92 | -45.665401 | 2024-09-27 00:35:50 | METOP-B | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 6349bbd6-980c-35de-bca0-561436f11114 | -4.9219 | -45.673599 | 2024-09-27 00:35:50 | METOP-B | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 7bd4ac5a-6cf2-306a-ac07-f16ba5ea874b | -6.1132 | -50.9506 | 2024-09-27 00:35:50 | METOP-B | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b92493cb-2f84-3cee-acf0-77c27592c8ae | -6.1149 | -50.958302 | 2024-09-27 00:35:50 | METOP-B | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| edd82d87-1062-3c72-b0a7-6ce0ede9c359 | -6.1166 | -50.966 | 2024-09-27 00:35:50 | METOP-B | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README15.md)
