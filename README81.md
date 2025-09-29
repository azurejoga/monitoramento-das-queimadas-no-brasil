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

## Dados Diários - Página 81

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 774244f7-584f-387f-bf70-116b44c71baf | -10.99117 | -57.06499 | 2025-09-29 05:48:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 17b3f437-de73-3342-804b-081728f86fb1 | -10.26436 | -67.3379 | 2025-09-29 05:48:00 | NOAA-20 | PLÁCIDO DE CASTRO | ACRE | Brasil | 1200385 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0b798171-a7a6-373a-8101-90f13d22e926 | -8.8004 | -72.72912 | 2025-09-29 05:48:00 | NOAA-20 | MARECHAL THAUMATURGO | ACRE | Brasil | 1200351 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4702bf25-f326-3b1e-987f-9fad30f70890 | -17.89498 | -57.62061 | 2025-09-29 05:50:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.1 |
| a06f412d-6e5d-37bb-89bb-86ea72b40e67 | -17.8944 | -57.61456 | 2025-09-29 05:50:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.3 |
| c8c90ce0-6d23-3a61-84aa-7d48c90babc0 | -17.90063 | -57.61499 | 2025-09-29 05:50:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.6 |
| 6e68581d-b2d0-38c5-a9f2-314bb267f837 | -17.90697 | -57.61434 | 2025-09-29 05:50:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.6 |
| 3dea2178-2b67-39ac-9262-dcd68bbfcc44 | -15.35693 | -56.95887 | 2025-09-29 05:50:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9f6670bf-8cee-3508-a799-5c1c5cf570e0 | -17.91337 | -57.61301 | 2025-09-29 05:50:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 4dc134e8-bd2b-3be3-b0af-728833e7ec09 | -17.90888 | -57.60732 | 2025-09-29 05:50:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.7 |
| 898abd64-1488-30a1-8222-106f6806998c | -17.90621 | -57.62239 | 2025-09-29 05:50:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 9a4b0acb-140c-320c-9ad3-09760713a6a9 | -17.90843 | -57.61171 | 2025-09-29 05:50:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.7 |
| ec8e64ab-d566-3da0-9202-4446338a2cef | -17.9076 | -57.61998 | 2025-09-29 05:50:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.1 |
| 65b30c09-3984-3d64-a27d-8a3337556817 | -16.01451 | -59.50483 | 2025-09-29 05:50:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7e44d0b4-e81a-3560-a5d3-c5c8fdd35190 | -16.01413 | -59.50825 | 2025-09-29 05:50:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f0a8daec-997a-3622-8806-1084151ec4cc | -10.90346 | -68.28062 | 2025-09-29 05:50:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 36474d1f-1fac-3de2-8dae-171f8c59c4a5 | -17.90207 | -57.61248 | 2025-09-29 05:50:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 4ba38529-4f04-30f8-b766-5efb46597baf | -17.91377 | -57.60875 | 2025-09-29 05:50:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| f4a7e3bf-93e8-3ebf-a8a6-90fce3a922a2 | -17.90723 | -57.62362 | 2025-09-29 05:50:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 22fba692-d63e-31be-91b0-7212183bf799 | -17.89538 | -57.61667 | 2025-09-29 05:50:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 096af9a2-363b-3bd4-96e2-47809c07ccbd | -17.9078 | -57.60554 | 2025-09-29 05:50:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.9 |
| a89b6d42-c260-3607-b32a-0bb60d45ad06 | -17.90738 | -57.60999 | 2025-09-29 05:50:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 653fdf7d-e595-3fab-aac9-8c4042f26f2c | -16.01126 | -59.50916 | 2025-09-29 05:50:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d2ba545c-cbe2-363a-86ec-6067fae2ac5f | -17.90657 | -57.61855 | 2025-09-29 05:50:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.6 |
| 1baba4e8-bbbc-3ac3-a606-10c6ee9a18d8 | -17.8958 | -57.61243 | 2025-09-29 05:50:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.5 |
| a82a0cc2-089c-3bc1-b031-1fdb0f32ae25 | -16.01956 | -59.50849 | 2025-09-29 05:50:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3f9a1173-96a2-32de-9304-905fa3ef5db4 | -17.89401 | -57.61867 | 2025-09-29 05:50:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 5b618e0e-92df-38dd-866a-e21d12d5295d | -17.90105 | -57.61053 | 2025-09-29 05:50:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 2751609f-988e-3f28-898b-21056dcc8044 | -16.01167 | -59.50573 | 2025-09-29 05:50:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 903aeb02-3bd5-312e-a7d8-ebb6d1dc5806 | -17.90163 | -57.61691 | 2025-09-29 05:50:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 04921566-b4bb-3122-9ece-a26e55fe506e | -17.90801 | -57.61592 | 2025-09-29 05:50:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.1 |
| 9019b67a-91a7-3ed1-b4aa-7bd1543d8102 | -14.5526 | -48.4461 | 2025-09-29 07:20:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 78dd9ab8-6e11-3f8c-97ec-eaecbef6d03a | -11.925 | -48.0273 | 2025-09-29 10:40:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 91.6 |
| 15a33f15-5c27-3366-b1f8-017c4e48f538 | -12.9435 | -46.7655 | 2025-09-29 10:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 132.9 |
| 2002a340-5bef-3cff-bf13-ec9988ce3322 | -12.9628 | -46.7626 | 2025-09-29 10:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 87.9 |
| 52800f9e-02de-3f5d-965f-a7fbdff69abc | -9.7674 | -46.1971 | 2025-09-29 11:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 86.1 |
| f2ea63a7-8272-3684-8020-cd5f70bcbf48 | -14.5526 | -48.4461 | 2025-09-29 11:00:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 109.7 |
| 92078be1-5582-3595-9c1d-786cc3704695 | -12.9435 | -46.7655 | 2025-09-29 11:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 134.3 |
| 75994157-63f7-3d16-956e-2aa0b352da12 | -8.2659 | -45.5244 | 2025-09-29 11:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 88.1 |
| 96ea2c22-133d-364b-9295-9a7c479e7155 | -8.2851 | -45.4999 | 2025-09-29 11:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 156.2 |
| d8b9506d-3958-30ba-814a-5da3f726ff74 | -11.925 | -48.0273 | 2025-09-29 11:00:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 87.4 |
| f65a77b6-8d6c-3f75-bb92-eb2d4f0ffe57 | -8.2848 | -45.5225 | 2025-09-29 11:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 110.2 |
| 18fd8af9-67a7-346a-a62b-c93e1727194b | -9.7674 | -46.1971 | 2025-09-29 11:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 165.6 |
| e931c992-3413-3a71-a24d-bbc0dab275a1 | -8.2848 | -45.5225 | 2025-09-29 11:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 118.1 |
| b53a4ce2-59a2-306a-bad7-6ef9eb370b56 | -14.6049 | -45.0161 | 2025-09-29 11:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 103.9 |
| 34fc68b7-dc9d-3c06-89d9-28e3b64a4978 | -9.7677 | -46.1745 | 2025-09-29 11:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 117.1 |
| 9c76eff8-f5dc-3d76-ae5d-765e7b3b5b84 | -14.5526 | -48.4461 | 2025-09-29 11:10:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 97.6 |
| 6e104ace-69c5-3da3-bd60-a02c365f9b81 | -7.8566 | -46.7527 | 2025-09-29 11:10:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 93.8 |
| 5e7cd54b-9208-34cc-a5b1-07908e427af8 | -8.2659 | -45.5244 | 2025-09-29 11:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 87.2 |
| 441c93bb-3ea9-310f-82e7-59a8cd88220c | -12.9431 | -46.7882 | 2025-09-29 11:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 79.5 |
| b82b02c2-d677-339d-be76-cdf85c948551 | -10.8227 | -46.6763 | 2025-09-29 11:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 78.5 |
| 85d44600-b2e6-30d8-8b6a-9f99d6158e32 | -8.2851 | -45.4999 | 2025-09-29 11:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 103.4 |
| 0d69d7d2-2a7d-3f91-a2ae-e2b5a5a91b70 | -11.3634 | -45.0801 | 2025-09-29 11:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 96.4 |
| 1338aef0-39f9-3329-8d7e-8ca5526f9aa5 | -12.9435 | -46.7655 | 2025-09-29 11:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 147.2 |
| 0a207aab-f362-39a7-8628-04d12da77ee1 | -8.8229 | -46.189 | 2025-09-29 11:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 112.1 |
| 14894c5b-8ba6-3eab-a101-1afc0bd0368d | -8.2662 | -45.5018 | 2025-09-29 11:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 92.4 |
| 0a3e436e-8ed6-312e-9e6a-f5a9c39c7879 | -8.2659 | -45.5244 | 2025-09-29 11:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 154.9 |
| 96886219-ae70-3560-8032-62e62f0fa557 | -8.3039 | -45.4979 | 2025-09-29 11:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 86.6 |
| aaf52ba2-6f43-3e7f-9174-1d4bc7ffadec | -11.925 | -48.0273 | 2025-09-29 11:20:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 190.5 |
| 697df7af-debf-317b-8fc8-c817512fd85c | -8.8229 | -46.189 | 2025-09-29 11:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 88.3 |
| 2142d295-4cc5-3e58-acd7-7aa26aa61aaa | -8.2848 | -45.5225 | 2025-09-29 11:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 257.8 |
| 0f947465-2150-300c-8d0e-b756ba627b6b | -7.8163 | -47.0003 | 2025-09-29 11:20:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 86.9 |
| 3026195d-2204-3b86-a14d-dd482d4ffadd | -8.2851 | -45.4999 | 2025-09-29 11:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 212.3 |
| abe7015c-8e8b-3a1a-9cf0-99bb6fdfe7b6 | -14.698 | -45.2093 | 2025-09-29 11:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 119.1 |
| 4795d428-edd3-3171-a7e7-a42a838c4be7 | -7.8375 | -46.7766 | 2025-09-29 11:30:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 81.6 |
| d9bb8c0e-6fba-3884-ad74-4ebd2bd7ad32 | -7.8163 | -47.0003 | 2025-09-29 11:30:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 110.7 |
| 76e4ab5c-0dc4-3016-9fc9-deeb674cb2c4 | -10.823 | -46.6538 | 2025-09-29 11:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 86.6 |
| e7cb1ffe-266a-30c5-b71c-094143bf6760 | -14.6049 | -45.0161 | 2025-09-29 11:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 80.7 |
| 2ef59123-b606-3782-86ee-4ef6595315f1 | -8.2659 | -45.5244 | 2025-09-29 11:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 95.0 |
| eb80041d-99fc-300a-9c69-d1a6c28f188d | -14.7176 | -45.2057 | 2025-09-29 11:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 134.6 |
| abba0e40-0283-369f-a7a8-c7c165b3be08 | -14.5526 | -48.4461 | 2025-09-29 11:30:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 72.6 |
| 1dcdede2-0bc4-3813-bdb0-060b18010da0 | -10.8227 | -46.6763 | 2025-09-29 11:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 75.9 |
| 200aeaec-abaa-376a-a2eb-bb2f16db14ac | -11.3634 | -45.0801 | 2025-09-29 11:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 94.2 |
| 26e1fa36-32e8-3e24-9dea-b0b113a33760 | -7.8566 | -46.7527 | 2025-09-29 11:30:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 85.7 |
| a22612b8-86fb-3413-86e5-a8e0a5d6a1e8 | -11.3638 | -45.057 | 2025-09-29 11:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 91.6 |
| 54058fb7-9f75-3762-bd74-40a3594fe7bd | -9.7674 | -46.1971 | 2025-09-29 11:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 72.8 |
| 2d713e33-82b4-3db5-ad58-00ca0ef59929 | -8.2851 | -45.4999 | 2025-09-29 11:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 133.9 |
| 63864271-659c-3eee-9fe5-e96277bcf30a | -11.3826 | -45.0774 | 2025-09-29 11:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 116.3 |
| 4fb2cc09-abe0-31e5-a31b-eb10285266a3 | -12.9435 | -46.7655 | 2025-09-29 11:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 102.6 |
| 3ab2436e-af83-34f7-92ed-11db38c8ebf9 | -11.3634 | -45.0801 | 2025-09-29 11:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 216.8 |
| 9464e9d7-d425-3c3a-a657-08545093770b | -10.8227 | -46.6763 | 2025-09-29 11:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 79.1 |
| 80c17fe8-30ab-3a64-8d01-5bc5dd607b43 | -10.823 | -46.6538 | 2025-09-29 11:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 113.8 |
| df3bbe19-bec3-3a2c-a657-0b2ed784c969 | -8.2659 | -45.5244 | 2025-09-29 11:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 225.0 |
| fea9a2c5-c0d6-39fc-a526-0a51d007e430 | -11.3638 | -45.057 | 2025-09-29 11:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 124.9 |
| a71b89d1-42cd-3af6-b15b-3ee9dcd53af7 | -7.8163 | -47.0003 | 2025-09-29 11:40:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 132.6 |
| d0c6cb82-fd55-39eb-9a9a-0f7c1fb096e1 | -8.2851 | -45.4999 | 2025-09-29 11:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 124.3 |
| 4d72bde2-9001-3bdd-8813-fce66f978731 | -10.8227 | -46.6763 | 2025-09-29 11:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 97.4 |
| 0ee4d69f-bcf7-311b-8d46-01f4dc6bdb6b | -9.7674 | -46.1971 | 2025-09-29 11:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 9fcf86e3-0ba9-3264-92ee-afe68b3a2266 | -11.3634 | -45.0801 | 2025-09-29 11:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 121.0 |
| c6fa3446-9f82-3c3e-8fde-b29cdfbb0838 | -7.8163 | -47.0003 | 2025-09-29 11:50:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 131.0 |
| 416ade20-3926-33a5-befc-605f95e407d6 | -8.2848 | -45.5225 | 2025-09-29 11:50:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 133.8 |
| b0635a06-1852-354c-ade7-714608de6578 | -8.2659 | -45.5244 | 2025-09-29 11:50:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 121.9 |
| 44015935-7622-3d6a-bb97-52b515c84f06 | -7.8566 | -46.7527 | 2025-09-29 11:50:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 68.8 |
| 435f9135-3d88-3c07-bab4-3cc2ccc11cfc | -11.3638 | -45.057 | 2025-09-29 11:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 89.3 |
| ce74a358-d7b1-3b8c-973d-06c1359ce370 | -14.698 | -45.2093 | 2025-09-29 11:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 83.0 |
| 6f758458-2cd2-3db1-b9e0-527777cd66b4 | -10.804 | -46.6562 | 2025-09-29 11:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 102.8 |
| d887760b-58d8-39d8-a62a-ce2cabdfd229 | -12.9435 | -46.7655 | 2025-09-29 11:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 115.1 |
| ddd7c99a-f085-327f-b095-e0034be74c00 | -14.7176 | -45.2057 | 2025-09-29 11:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 79.1 |
| 75b58da5-e38d-3269-94d4-e3a59d023891 | -10.823 | -46.6538 | 2025-09-29 11:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 114.2 |
| 525c3555-e090-395c-a945-0524731fa399 | -13.2346 | -50.9691 | 2025-09-29 12:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 298.6 |


[Clique aqui para ver as próximas entradas](README82.md)
