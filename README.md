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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5394e20e-e8e6-3118-8893-fc8940edaca8 | -3.4312 | -44.1476 | 2025-10-12 00:00:00 | GOES-19 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 28.1 |
| 557c8343-c8b6-38f5-83d6-d67ac7ecc4e6 | -4.271 | -46.9369 | 2025-10-12 00:00:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 149.2 |
| 493dbccc-568f-327b-b1db-0250b33ba9d9 | -19.0519 | -57.5356 | 2025-10-12 00:00:00 | GOES-19 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 110.6 |
| 3f756121-e064-3631-adb5-1e10176b454f | -13.6778 | -43.8424 | 2025-10-12 00:00:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 85.3 |
| ae89b332-4fe6-3e29-91e5-714b96f70b00 | -13.6583 | -43.8459 | 2025-10-12 00:00:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 71.4 |
| 0be0b8aa-82a0-3b22-a812-d53391ddd1f4 | 1.9134 | -55.7419 | 2025-10-12 00:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 117.5 |
| fcf7694b-99c9-371e-9445-a723580ac1f1 | -11.2517 | -61.163 | 2025-10-12 00:00:00 | GOES-19 | CACOAL | RONDÔNIA | Brasil | 1100049 | 11 | 33 | nan | nan | nan | Amazônia | 69.9 |
| 0f754b43-f5df-3131-ab73-b23df1849f9e | -11.752 | -54.7255 | 2025-10-12 00:00:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 81.0 |
| 6f440fb7-5e93-3e01-98dc-45d1776c4d57 | -4.2896 | -46.936 | 2025-10-12 00:00:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 93.9 |
| dee04027-16ff-3446-b7e3-e9870e8daa95 | -7.2137 | -45.4882 | 2025-10-12 00:00:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 101.4 |
| fcf1f9b8-292e-3a79-a1c3-d27c7fb61e3f | -13.6578 | -43.8697 | 2025-10-12 00:00:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 0d3527c3-ea91-3bc8-a61a-69beaf5e071e | -2.5423 | -47.811 | 2025-10-12 00:00:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 134.2 |
| 3ad1bf99-a41c-3144-aa7d-4bcec67cf26f | -9.016 | -67.446 | 2025-10-12 00:00:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 2c1db7a3-164f-3583-aff0-c90746db7756 | -14.0155 | -43.4943 | 2025-10-12 00:00:00 | GOES-19 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 115.6 |
| 3868e0aa-9965-3b0e-affa-87ef0c14c057 | -4.2711 | -46.9149 | 2025-10-12 00:00:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 109.6 |
| df81b833-9a4e-369e-aa70-58b40396892d | -14.0161 | -43.4703 | 2025-10-12 00:00:00 | GOES-19 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Cerrado | 93.4 |
| eefde989-db09-30ec-b82e-0e73c3a15e40 | -19.0515 | -57.5564 | 2025-10-12 00:00:00 | GOES-19 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 88.5 |
| d576a5a8-f337-38b2-8c7e-d7461b75435b | -7.5212 | -46.538 | 2025-10-12 00:00:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 186.1 |
| 546a7223-3e4a-3afb-9dc1-a7be9b17a0da | -9.0161 | -67.4275 | 2025-10-12 00:00:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 49.4 |
| 5c16da36-5feb-34c8-a875-31b17fd77bbe | -13.6773 | -43.8662 | 2025-10-12 00:00:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 81.0 |
| 8b742fc4-ebdc-3596-827c-97a4b64f15cc | -19.0316 | -57.5589 | 2025-10-12 00:00:00 | GOES-19 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 98.9 |
| 544c675d-cfa6-32a3-9222-817697123c59 | -5.65 | -44.4766 | 2025-10-12 00:00:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 34.5 |
| b7c38995-977d-3932-8db5-8ee3fa798b1d | -19.0319 | -57.5382 | 2025-10-12 00:00:00 | GOES-19 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 191.7 |
| 3313e248-4f71-34be-831f-c203c59b1c36 | -14.0351 | -43.4906 | 2025-10-12 00:00:00 | GOES-19 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 111.7 |
| c7eb4619-c0da-3912-9b74-588d33b9bb7c | -3.5371 | -48.9195 | 2025-10-12 00:00:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 93.6 |
| 5b3353e1-cd61-33a9-a38f-7759c042c9e6 | -2.5238 | -47.8115 | 2025-10-12 00:00:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 69.2 |
| 70461909-ec2e-3dfe-b32b-5b272af97850 | -7.521 | -46.5603 | 2025-10-12 00:00:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 76.2 |
| e5c4a0ab-f808-36ac-98c2-118e132b8d1f | -6.5851 | -44.6098 | 2025-10-12 00:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 69.1 |
| 5eb55b38-b595-3d76-aaf1-3c4fcbe05469 | -7.864 | -44.5152 | 2025-10-12 00:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 129.0 |
| 1314c2c5-f101-3fd6-bfd6-59b89716100d | -18.5756 | -50.5976 | 2025-10-12 00:00:00 | GOES-19 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 65.8 |
| 44895bf7-a2ce-337f-b495-9c810115db3f | -7.5025 | -46.5396 | 2025-10-12 00:00:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 110.4 |
| 268f1433-aabe-3b6a-b992-e1a3915b1451 | -2.5424 | -47.7893 | 2025-10-12 00:00:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 101.5 |
| 158d0213-91df-3f20-a92a-8e3ad449b268 | -7.8828 | -44.5133 | 2025-10-12 00:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 87.7 |
| 94213c09-c1d4-377a-b597-bb970421d7f3 | -15.6825 | -46.625 | 2025-10-12 00:00:00 | GOES-19 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 14800818-14a9-3744-9f0c-e104719692eb | -4.4241 | -43.4735 | 2025-10-12 00:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 62.9 |
| 94231229-812a-34a5-acba-689a8824f229 | -7.8637 | -44.5382 | 2025-10-12 00:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 86.4 |
| 3c7b19c8-3bbd-3b61-b018-e4d20fb4f642 | -13.4161 | -47.2352 | 2025-10-12 00:00:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 70.8 |
| 9e7c7cbb-3dd8-3c32-be1d-1cbef2d95dd1 | 1.9134 | -55.7221 | 2025-10-12 00:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 77.5 |
| c01888fa-227c-3498-af22-b7beb97deec1 | -7.5215 | -46.5157 | 2025-10-12 00:00:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 75.0 |
| c0aab924-f1f9-3ee6-9b7a-0cceaf115871 | -19.77037 | -42.42545 | 2025-10-12 00:09:00 | TERRA_M-M | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 15.2 |
| 9d301956-9794-3df3-b505-4035d251f1e8 | -18.3132 | -42.2636 | 2025-10-12 00:09:00 | TERRA_M-M | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 19.2 |
| 744148ee-90e0-3700-8f64-2fd56507b48e | -20.03394 | -41.66 | 2025-10-12 00:09:00 | TERRA_M-M | CHALÉ | MINAS GERAIS | Brasil | 3116001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 8a2b9f5f-423f-3c5c-a07a-75505383030c | -15.6825 | -46.625 | 2025-10-12 00:10:00 | GOES-19 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 84.1 |
| ac76f665-ae52-356a-8d9f-a03033ddaa0d | -19.0515 | -57.5564 | 2025-10-12 00:10:00 | GOES-19 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 71.9 |
| 355defb7-7107-38c2-bfea-3362b13ffb3d | -19.0316 | -57.5589 | 2025-10-12 00:10:00 | GOES-19 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 62.3 |
| da6038d7-8fff-39de-aa96-8b5c2b774c7a | -2.5423 | -47.811 | 2025-10-12 00:10:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 136.5 |
| 41e459bf-71d1-3169-a5fb-17f17710f1e6 | -11.7331 | -54.7272 | 2025-10-12 00:10:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 75.3 |
| 61291097-e177-31a4-916c-9511cdb068c5 | -14.0351 | -43.4906 | 2025-10-12 00:10:00 | GOES-19 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 95.8 |
| 8c9c8f27-1498-3ae5-a418-bc043f1898f9 | -9.016 | -67.446 | 2025-10-12 00:10:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 66.6 |
| e2c71184-7470-3b6b-8096-b798bf86e314 | -2.5424 | -47.7893 | 2025-10-12 00:10:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 99.4 |
| 5e942961-a906-3e43-9cc6-2579c370a991 | -4.271 | -46.9369 | 2025-10-12 00:10:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 136.4 |
| 025748aa-311b-39df-a02d-f22c0afc55b4 | -19.0319 | -57.5382 | 2025-10-12 00:10:00 | GOES-19 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 140.7 |
| a1dc8876-6b22-3633-9d78-4cb7cd992a12 | -7.5212 | -46.538 | 2025-10-12 00:10:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 137.1 |
| 1bfeb50f-8a20-3ef6-b770-6f8987e6a886 | -4.2896 | -46.936 | 2025-10-12 00:10:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 86.4 |
| c17051c1-2937-380e-b74c-035c0dd7645f | -18.5756 | -50.5976 | 2025-10-12 00:10:00 | GOES-19 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 64.7 |
| 92b65db5-e4e3-3ec5-b43c-8439582da3cc | -10.9668 | -61.6031 | 2025-10-12 00:10:00 | GOES-19 | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 2a29c25e-1394-3c98-b973-2d42cf94f02c | -14.0161 | -43.4703 | 2025-10-12 00:10:00 | GOES-19 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Cerrado | 98.5 |
| 76cbfd52-2355-3195-8d1b-6be723463f2c | -10.9856 | -61.6021 | 2025-10-12 00:10:00 | GOES-19 | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | 79.4 |
| fa1a1573-3315-36a9-b1ea-22bf6977cccf | -4.4241 | -43.4735 | 2025-10-12 00:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 57.6 |
| 276c0d53-06a3-32d4-93dd-d93da518f50f | -11.752 | -54.7255 | 2025-10-12 00:10:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 81.4 |
| 13168249-5167-38f4-bd1a-97479a49bfca | -9.0161 | -67.4275 | 2025-10-12 00:10:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 55.1 |
| f5c05ef9-e0c4-3554-8668-ff9b2ae4769f | -19.0519 | -57.5356 | 2025-10-12 00:10:00 | GOES-19 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 97.9 |
| acc41a3e-0c6a-3910-8ca6-01ef109a60ce | -17.5897 | -42.4246 | 2025-10-12 00:10:00 | GOES-19 | CAPELINHA | MINAS GERAIS | Brasil | 3112307 | 31 | 33 | nan | nan | nan | Cerrado | 116.5 |
| 66be14a2-5197-3034-af54-b4a807be9a4b | -3.5371 | -48.9195 | 2025-10-12 00:10:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 92.3 |
| 0effdbaa-ea4a-3215-a4d1-a248a215687c | 1.9134 | -55.7419 | 2025-10-12 00:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 94.1 |
| 6193135c-8b95-38e9-b3a3-315722d84e5e | -4.2711 | -46.9149 | 2025-10-12 00:10:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 98.2 |
| 5cf797a1-6fea-31e6-bf54-d88471a1414d | -14.0155 | -43.4943 | 2025-10-12 00:10:00 | GOES-19 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 124.8 |
| dd4f724d-55d4-3faa-8c3b-2a18e7009ce8 | -7.864 | -44.5152 | 2025-10-12 00:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 107.8 |
| 0a90a60c-ba9a-3b85-bf53-55f83885c4ab | -7.5025 | -46.5396 | 2025-10-12 00:10:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 104.6 |
| ed8fbf9a-eba1-310d-b652-4903907c7657 | -18.09944 | -42.65515 | 2025-10-12 00:11:00 | TERRA_M-M | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.2 |
| 5b8b1dd0-c052-3df0-88ba-085ffed5c3cf | -15.68721 | -46.6259 | 2025-10-12 00:11:00 | TERRA_M-M | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 29.3 |
| c518335e-8a2b-389b-b47b-f1986e2f8123 | -11.3677 | -44.00267 | 2025-10-12 00:11:00 | TERRA_M-M | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 003f8a57-2e44-336d-a50f-34e5b2eac1a8 | -15.43209 | -44.18166 | 2025-10-12 00:11:00 | TERRA_M-M | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 81a4c528-1644-3513-9db0-0ec09ae9feff | -13.38562 | -41.32372 | 2025-10-12 00:11:00 | TERRA_M-M | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 4.9 |
| a5b6f55b-6bfe-337b-8d7f-30c06e1157d5 | -16.82454 | -45.20054 | 2025-10-12 00:11:00 | TERRA_M-M | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| fffe7e5a-a159-32f4-a207-1cf41d87743d | -15.89201 | -43.69542 | 2025-10-12 00:11:00 | TERRA_M-M | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 71c24dc9-4be4-32cb-bb24-41b01e344e59 | -13.67634 | -43.84984 | 2025-10-12 00:11:00 | TERRA_M-M | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 12.1 |
| eb2b85b7-515d-3830-b51b-4edf6f70a6e1 | -12.58802 | -41.28865 | 2025-10-12 00:11:00 | TERRA_M-M | ANDARAÍ | BAHIA | Brasil | 2901304 | 29 | 33 | nan | nan | nan | Caatinga | 10.1 |
| 67aa3437-6375-3edd-8014-c0e0d02adb2a | -14.02236 | -43.48652 | 2025-10-12 00:11:00 | TERRA_M-M | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 203.5 |
| 3b64f776-5c34-3c08-9383-497a734108f0 | -10.98506 | -44.30832 | 2025-10-12 00:11:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 9.9 |
| c6e562d6-d105-3a0b-a880-9e9d52e38187 | -10.7639 | -44.10444 | 2025-10-12 00:11:00 | TERRA_M-M | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 8.8 |
| dca02b9d-232b-3cc0-8b5b-9360067c68f3 | -17.18294 | -43.09795 | 2025-10-12 00:11:00 | TERRA_M-M | BOTUMIRIM | MINAS GERAIS | Brasil | 3108503 | 31 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 363171ef-5703-3544-9777-9dd1c8bcf9a9 | -14.02176 | -47.06665 | 2025-10-12 00:11:00 | TERRA_M-M | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 83b63172-f8a3-30dc-923a-6f8425210483 | -14.02361 | -43.49562 | 2025-10-12 00:11:00 | TERRA_M-M | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 5c92114e-4094-3ec8-b05c-90932143e551 | -12.91526 | -47.0192 | 2025-10-12 00:11:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 14ec3351-a917-3c61-93de-2e37263c47e0 | -10.77273 | -44.10318 | 2025-10-12 00:11:00 | TERRA_M-M | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 41.8 |
| ac06a7e9-b895-3814-92a9-fd211c95495d | -13.66868 | -43.86024 | 2025-10-12 00:11:00 | TERRA_M-M | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 529.9 |
| 14c10786-841f-31c8-8ef7-e6e26dd7093d | -13.66103 | -43.8707 | 2025-10-12 00:11:00 | TERRA_M-M | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 21.0 |
| 6dac3045-1820-3795-8241-68197c2bf2cc | -11.95973 | -44.84307 | 2025-10-12 00:11:00 | TERRA_M-M | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 24.1 |
| e447abf4-c92d-3f6b-a647-d055d3ca85e4 | -12.78426 | -48.65263 | 2025-10-12 00:11:00 | TERRA_M-M | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| fdc3fcd9-01ac-3d90-b92b-cf215849865a | -15.76877 | -43.87416 | 2025-10-12 00:11:00 | TERRA_M-M | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Caatinga | 5.8 |
| a8e6b379-b93a-3a11-affc-aeefaf52567a | -13.64858 | -42.44579 | 2025-10-12 00:11:00 | TERRA_M-M | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 7.2 |
| 1ff4ac35-b910-3c15-927d-df1b62da1c69 | -18.56875 | -50.62294 | 2025-10-12 00:11:00 | TERRA_M-M | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 38.6 |
| bbc40e82-0466-365d-bbc1-49705a9eca4f | -15.46212 | -40.82346 | 2025-10-12 00:11:00 | TERRA_M-M | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 16.6 |
| e86cf227-e17c-374d-b71f-dc98e28deb14 | -18.56001 | -46.93487 | 2025-10-12 00:11:00 | TERRA_M-M | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 9.9 |
| f59ea772-ba77-32ec-a386-d35ac7cb2ec8 | -15.64389 | -44.46937 | 2025-10-12 00:11:00 | TERRA_M-M | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Cerrado | 10.7 |
| f763f7a2-7655-378a-b3da-6f398de9b8ed | -15.67826 | -46.64005 | 2025-10-12 00:11:00 | TERRA_M-M | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 45.3 |
| dc434085-4579-39f0-8cba-59be4d22fa8e | -10.1513 | -36.21204 | 2025-10-12 00:11:00 | TERRA_M-M | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 21.9 |
| b45df90a-7210-39cd-a48e-0d683f76cddc | -13.34117 | -43.96037 | 2025-10-12 00:11:00 | TERRA_M-M | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| d33e48c5-ed01-39cf-b116-485583dba1aa | -10.94142 | -42.27765 | 2025-10-12 00:11:00 | TERRA_M-M | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 6.2 |


[Clique aqui para ver as próximas entradas](README2.md)
