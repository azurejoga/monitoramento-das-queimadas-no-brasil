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

## Dados Diários - Página 74

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4de5eb9f-9c04-3c68-a5d9-ac029a7099a0 | -12.1663 | -44.1224 | 2025-09-15 13:40:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 129.1 |
| 197e3a08-de25-3d2f-aa4e-b61f00d65522 | -10.948 | -47.1753 | 2025-09-15 13:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 205.7 |
| 9096db32-f289-31db-bd4d-ee7d15bcda85 | -11.6626 | -46.5884 | 2025-09-15 13:40:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 107.0 |
| 1975a4df-2afd-3953-9c9d-087e712e36ce | -6.1504 | -41.1889 | 2025-09-15 13:40:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 225.3 |
| 80eff03a-9d89-30a1-930c-a32d3b4e15df | -11.1303 | -45.3196 | 2025-09-15 13:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 152.3 |
| 73e49942-245c-3cf0-bee0-cb720ab09804 | -12.1668 | -44.0988 | 2025-09-15 13:40:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 142.5 |
| 20c00693-5d02-3cf5-b63f-0a38df8e8792 | -9.5164 | -47.9589 | 2025-09-15 13:40:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 93.2 |
| 8dbd9992-5703-307b-b005-16a9f1b0fae9 | -6.1693 | -41.1872 | 2025-09-15 13:40:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 350.4 |
| 2a2d9bb6-c291-3f5c-b346-e0dc4021585e | -13.2031 | -47.29 | 2025-09-15 13:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 58.3 |
| df9110b5-9b1d-31a3-9552-cc6bc695253f | -9.5167 | -47.9369 | 2025-09-15 13:40:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 95.9 |
| 14dc166d-7e26-30d1-a79d-0c12f0598973 | -14.8218 | -51.6362 | 2025-09-15 13:50:00 | GOES-19 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 153.8 |
| da5bc846-da7b-3314-933a-b4163c0b7465 | -5.8399 | -44.1642 | 2025-09-15 13:50:00 | GOES-19 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 117.4 |
| 55fd54e8-e275-3c78-8454-07bf7c3a3c11 | -9.5167 | -47.9369 | 2025-09-15 13:50:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 76.0 |
| 16b34ede-1bb7-3fb0-a88c-55839684ee1e | -6.4452 | -43.6067 | 2025-09-15 13:50:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 109.1 |
| 56f052d8-58dd-397c-8963-9a2d6a04a3c7 | -5.7671 | -43.9392 | 2025-09-15 13:50:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 86.2 |
| 12a58335-d4cc-32d1-8953-e9c1469bf7c5 | -14.5168 | -47.3304 | 2025-09-15 13:50:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 63.3 |
| 18dfa36f-4b89-38e1-91ae-ce2baa1a7a87 | -6.1693 | -41.1872 | 2025-09-15 13:50:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 289.7 |
| 3b44d247-0c03-3e74-8fb6-49261c0cc3e7 | -10.8612 | -45.4477 | 2025-09-15 13:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 101.5 |
| b2d8fe5b-2ac2-3de0-9591-f8677d0d757a | -6.1504 | -41.1889 | 2025-09-15 13:50:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 119.8 |
| 39c9f80b-ee00-382b-8dba-9a5776f2fa80 | -8.7677 | -46.0823 | 2025-09-15 13:50:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 151.9 |
| 02b07865-bad2-3b0f-a07a-45ac83a0b7f1 | -15.0281 | -47.9889 | 2025-09-15 13:50:00 | GOES-19 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 64.8 |
| b78b7fab-92d5-36a6-90ab-7d8679729149 | -18.9851 | -48.5844 | 2025-09-15 13:50:00 | GOES-19 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 105.9 |
| cab7b67e-c58c-3fc4-91b5-52f9bc1b3d0c | -12.1668 | -44.0988 | 2025-09-15 13:50:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 228.8 |
| 5af53e30-0c82-3199-bfed-7caa9612d5f9 | -6.1881 | -41.1855 | 2025-09-15 13:50:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 202.1 |
| fa6530e0-8afb-36e1-8bfe-a757b3ead3ef | -12.6764 | -47.725 | 2025-09-15 13:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 80.6 |
| c4bbf152-082d-33b4-885a-55cce5b3f7e6 | -14.9416 | -46.5525 | 2025-09-15 13:50:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 68.2 |
| 8d602be9-7a94-3474-9589-783066546c96 | -12.8212 | -47.1445 | 2025-09-15 13:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 94.4 |
| f95d73de-0387-3fe7-bb44-44d65605907a | -11.1306 | -45.2966 | 2025-09-15 13:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 71.9 |
| 548e3caf-c8bd-3a7b-a6be-705d5b4bb49f | -8.651 | -46.3637 | 2025-09-15 13:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 99.3 |
| 4911ce71-7ea0-39f0-acf9-26ae664e2c95 | -10.6396 | -46.2266 | 2025-09-15 13:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 81.0 |
| 4c50edaa-fe21-3494-a8f9-91825e6e6850 | -10.948 | -47.1753 | 2025-09-15 13:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 96.4 |
| 6e3e6724-ace3-3ae5-b299-adbb9bf63c55 | -9.5164 | -47.9589 | 2025-09-15 13:50:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 71.5 |
| 114edca9-1bf1-3ffa-95f3-8c284eca8a58 | -8.9784 | -45.8344 | 2025-09-15 13:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 181.3 |
| 90975aa2-a12e-3377-bb71-8603151e583d | -5.9271 | -44.8671 | 2025-09-15 13:50:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 79.8 |
| f345fc39-2da6-340f-98ba-dc370de65747 | -11.6622 | -46.611 | 2025-09-15 13:50:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 112.1 |
| a7d03854-5546-32b7-b856-8ce6c3337dad | -7.7027 | -48.8451 | 2025-09-15 13:50:00 | GOES-19 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 100.1 |
| a8f60837-a541-3c07-82e8-df66cf1b9636 | -10.9159 | -45.6004 | 2025-09-15 13:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 151.4 |
| 6c00d06a-b38a-3150-8b6f-6cfa444a43a8 | -8.9412 | -45.7933 | 2025-09-15 13:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 132.4 |
| e8ed99c5-b3e3-35c1-9342-6cec06681cdf | -10.9452 | -47.3538 | 2025-09-15 13:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 83.1 |
| da2f03d6-817a-3b57-a039-8a442936902b | -5.7673 | -43.9161 | 2025-09-15 13:50:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 99.1 |
| 181e14cb-d725-39dd-a4ee-e7f752ec678b | -12.6533 | -47.9507 | 2025-09-15 13:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 108.0 |
| ec361be3-de02-3207-861d-70fbd52d9a53 | -6.1695 | -41.1629 | 2025-09-15 13:50:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 131.2 |
| e04ac7b5-3640-3ecf-b37b-be1e0785dffd | -6.337 | -43.1727 | 2025-09-15 13:50:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 109.7 |
| 6b3dde09-2f27-36fc-8747-db1e50031ce4 | -11.1303 | -45.3196 | 2025-09-15 13:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 176.2 |
| 09397580-6316-3c4a-812a-db540e4b17b5 | -11.3338 | -43.4979 | 2025-09-15 13:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 110.2 |
| b22aabcd-612a-32c3-a4a0-65c6e1136beb | -11.6626 | -46.5884 | 2025-09-15 13:50:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 87.6 |
| 290d5873-4864-3e5e-8b1f-f17249fb22f5 | -10.8609 | -45.4707 | 2025-09-15 13:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 78.5 |
| d47f7502-32f2-3367-968a-68baf978bbbb | -22.7817 | -46.7912 | 2025-09-15 13:50:00 | GOES-19 | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 116.9 |
| 9292c65f-6c9d-3690-babd-2167bb4aca71 | -9.2235 | -44.5052 | 2025-09-15 13:50:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 589.1 |
| 293771c5-36ff-354e-b3c4-e21a8a92d49f | -6.169 | -41.2114 | 2025-09-15 13:50:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 248.6 |
| 62a254ff-eaca-3dcb-b52d-f53ecf863ec5 | -10.935 | -45.5978 | 2025-09-15 13:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 110.4 |
| cdf14889-5c17-3923-aa1a-0731ce214ba3 | -11.3884 | -43.6548 | 2025-09-15 13:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 107.8 |
| ae734c9c-959d-3770-8eca-e262437f5135 | -12.8087 | -44.744 | 2025-09-15 13:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 92.5 |
| 2ca96b41-c5cb-35d2-8b42-d769d12c82f7 | -16.673 | -49.7615 | 2025-09-15 13:50:00 | GOES-19 | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 297.6 |
| 0f48cfdb-3bd8-330f-95be-6f78deab31da | -8.768 | -46.0598 | 2025-09-15 13:50:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 140.0 |
| 658dda43-7df4-3077-8b56-795075d74875 | -9.2691 | -51.2455 | 2025-09-15 13:50:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 79.4 |
| f084d58d-3da0-343d-a856-e3ea55197f69 | -12.8404 | -47.1417 | 2025-09-15 13:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 256.4 |
| 87a94c20-adef-332f-b7d7-1be9470d287f | -15.7973 | -53.5216 | 2025-09-15 13:50:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 120.9 |
| 06235edb-c9d5-31ad-b2fa-27df61af0352 | -10.9477 | -47.1976 | 2025-09-15 13:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 98.5 |
| 572ba8ef-6150-3ad0-b05b-23489d52cc78 | -8.9601 | -45.7912 | 2025-09-15 13:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 175.6 |
| 7ce4f271-d6ce-31a7-975a-38ec96f2c54d | -10.9346 | -45.6207 | 2025-09-15 13:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 142.6 |
| a60e8c96-388d-3386-82c0-cfbf8506ceaf | -8.9568 | -46.0398 | 2025-09-15 13:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 80.7 |
| 5a091ebd-4f6a-3337-b62c-dce12a11af5f | -11.6434 | -46.591 | 2025-09-15 13:50:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 86.1 |
| 3ea4d334-9609-3785-98e0-b4279586d832 | -8.5947 | -46.3471 | 2025-09-15 13:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 84.1 |
| eacf8b70-5ecc-37e5-8c96-6deca0666a17 | -14.8111 | -48.1367 | 2025-09-15 13:50:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 62.8 |
| 9baca509-434e-3c96-a254-9f16b6671b70 | -6.356 | -43.1476 | 2025-09-15 13:50:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 154.6 |
| 4a296108-7f19-3151-a6b2-3bbbe6e28a4a | -7.8073 | -46.1323 | 2025-09-15 13:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 67.3 |
| 0f0eb41a-e5d5-3268-9d8c-ee829c37b4f1 | -6.3989 | -42.6263 | 2025-09-15 13:50:00 | GOES-19 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 104.3 |
| af3b71fe-7454-3d1f-abfc-4aa02e104a89 | -8.9604 | -45.7686 | 2025-09-15 13:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 120.5 |
| 0c5efb17-25df-3b14-b633-01bc9a4a6294 | -3.4366 | -43.1532 | 2025-09-15 13:50:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 94.5 |
| 827c8c12-f4bc-3508-9885-feaf74081e17 | -8.7868 | -46.0578 | 2025-09-15 13:50:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 95.7 |
| 12442945-452c-3e55-a02b-6781276ddc64 | -7.8076 | -46.1099 | 2025-09-15 13:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 81.0 |
| ed44106b-00bd-3640-898e-eb6b6b59cf7c | -13.1842 | -47.2704 | 2025-09-15 13:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 47.2 |
| 4598f9f1-3230-341c-98ce-425cbef3973e | -12.1663 | -44.1224 | 2025-09-15 13:50:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 208.5 |
| df92b87e-c4fa-3785-aa9e-f1c665ff12e8 | -10.9671 | -47.1729 | 2025-09-15 13:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 95.8 |
| b076ce77-caae-3277-9935-e0892f1f493f | -6.3558 | -43.1711 | 2025-09-15 13:50:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 124.2 |
| 03dc0e4a-73ed-3fb9-b558-64e26b9d3584 | -6.3372 | -43.1492 | 2025-09-15 13:50:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 132.7 |
| 0b16533a-55a7-3c1f-b759-1ee0eb17c34d | -7.5281 | -47.642 | 2025-09-15 13:50:00 | GOES-19 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 73.8 |
| cd9adbca-0c44-36fb-8da8-9b07bca53be6 | -12.84 | -47.1642 | 2025-09-15 13:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 66.6 |
| 92eb6fe5-032a-3be9-bc25-364bc6c6f9e1 | -12.1861 | -44.0958 | 2025-09-15 13:50:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 68.5 |
| e533cd2a-379b-3f35-bfc0-65942b972b51 | -11.3338 | -43.4979 | 2025-09-15 14:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 157.6 |
| dd4739c2-717a-33f2-af7b-b44a9a41f0ee | -6.356 | -43.1476 | 2025-09-15 14:00:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 87.0 |
| dd78e809-c761-3917-b30f-cb3901f25d63 | -9.5164 | -47.9589 | 2025-09-15 14:00:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 66.0 |
| 8856c05f-80e5-383a-bac5-028605ae7a81 | -6.3989 | -42.6263 | 2025-09-15 14:00:00 | GOES-19 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 98.0 |
| 1f3e12d0-585e-3105-a2d3-f65e4c7c6ef2 | -8.4329 | -45.7337 | 2025-09-15 14:00:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 100.3 |
| 30167455-4493-3957-86c8-48556116b2d3 | -11.6434 | -46.591 | 2025-09-15 14:00:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 82.4 |
| ca709b92-8920-3956-ab51-ea160ac26dff | -18.9851 | -48.5844 | 2025-09-15 14:00:00 | GOES-19 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 100.5 |
| 8b5a0bcf-39e9-3d59-a64c-39fcf5582b94 | -5.7673 | -43.9161 | 2025-09-15 14:00:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 84.1 |
| 4f7fcdc7-6f03-3e60-9c38-1ea13262f804 | -9.2235 | -44.5052 | 2025-09-15 14:00:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 167.0 |
| 677bdbea-5ead-347d-8727-8b5d285c735c | -13.1842 | -47.2704 | 2025-09-15 14:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 56.6 |
| ceed5a88-65b8-3574-a54e-c2a34b236de1 | -11.6622 | -46.611 | 2025-09-15 14:00:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 121.2 |
| 2216aaba-971b-3a21-8aa9-173f466395e5 | -8.7868 | -46.0578 | 2025-09-15 14:00:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 82.5 |
| d5567f11-6f2d-3092-8b81-9d127534d1ed | -6.169 | -41.2114 | 2025-09-15 14:00:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 193.6 |
| 13289968-12a5-3594-b68b-1149c21e577d | -7.306 | -43.9467 | 2025-09-15 14:00:00 | GOES-19 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 127.2 |
| 1e3136d7-934b-3e85-91c9-7ea55fbefc46 | -11.3884 | -43.6548 | 2025-09-15 14:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 121.8 |
| 48fe4373-9844-33ce-ad59-196dfd297e60 | -12.6953 | -47.7446 | 2025-09-15 14:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 86.4 |
| a158d853-106a-3222-9c27-00e49c7e68cd | -6.4177 | -42.6246 | 2025-09-15 14:00:00 | GOES-19 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 97.1 |
| 0ef4219a-8a0d-3439-9603-42998a796790 | -10.8609 | -45.4707 | 2025-09-15 14:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 73.1 |
| f65cfaac-9b5f-3a7a-bf61-53317ace1e4c | -13.9463 | -44.901 | 2025-09-15 14:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 95.9 |
| 7d103426-760a-3030-8b7c-df7f9656716f | -8.9568 | -46.0398 | 2025-09-15 14:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 73.2 |


[Clique aqui para ver as próximas entradas](README75.md)
