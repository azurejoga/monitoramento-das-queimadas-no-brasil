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

## Dados Diários - Página 75

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 47d03070-ac80-31bf-afe1-c4442a633d12 | -8.8506 | -45.5086 | 2024-10-03 04:05:56 | GOES-16 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 47.2 |
| 72827fde-fd61-37eb-a15f-cace32466f97 | -8.9791 | -67.4099 | 2024-10-03 04:05:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 49.0 |
| c8653d2f-8703-312b-bea6-8b3209fcc959 | -9.0515 | -67.871 | 2024-10-03 04:05:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 46.4 |
| 4a15e9d1-b3d3-3739-b651-cd8236f335f5 | -10.6317 | -53.7011 | 2024-10-03 04:06:06 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 36.4 |
| 94ec159a-53f3-37a4-96af-0eeb5747f792 | -10.6319 | -53.6805 | 2024-10-03 04:06:06 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 43.1 |
| 74b579a6-16b0-3bd3-bf9b-7d84b8c5e757 | -10.9381 | -46.5942 | 2024-10-03 04:06:07 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 43.9 |
| c2886e0a-718b-30bd-a3fe-dbba165ca966 | -10.9384 | -46.5717 | 2024-10-03 04:06:07 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 29.4 |
| 18a996c1-c88a-3269-b96f-51cd3b14b7ae | -10.8942 | -63.8971 | 2024-10-03 04:06:08 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 6d981db4-203a-3b52-945d-23aacf828fa5 | -11.6822 | -47.7045 | 2024-10-03 04:06:12 | GOES-16 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 74.7 |
| 90d2d0a4-d5f9-33ae-8e26-c79de2080d76 | -11.6931 | -64.9974 | 2024-10-03 04:06:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 81.4 |
| 66df8171-c6c1-3911-ae64-68d3f6eb625e | -11.6932 | -64.9785 | 2024-10-03 04:06:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 61.8 |
| 4feeab6e-4649-3db8-9f53-965ebc3085f5 | -12.4038 | -63.0009 | 2024-10-03 04:06:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 137.1 |
| 2d9c5623-173d-3ee6-9421-ebc432f0cf7e | -12.404 | -62.9817 | 2024-10-03 04:06:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 85.4 |
| e39aec9e-36d4-3af5-b72a-903e65c8901f | -12.4227 | -62.9999 | 2024-10-03 04:06:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 87.2 |
| f1d58b71-71f2-3898-b3fb-abb4d8952b66 | -12.6484 | -63.1214 | 2024-10-03 04:06:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 77.8 |
| 0b4d549d-035e-37d4-928b-a871b677945b | -12.881 | -62.4538 | 2024-10-03 04:06:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 68.8 |
| 5a701949-afbf-3aeb-96ec-c7fff01f5584 | -12.8996 | -62.4913 | 2024-10-03 04:06:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 94.3 |
| 9a151bcd-34db-3e1f-ad49-f3641da862c7 | -12.8998 | -62.472 | 2024-10-03 04:06:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 112.4 |
| d69d86e2-161b-34fc-872e-5c93ebc45147 | -13.0402 | -51.1432 | 2024-10-03 04:06:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 84.2 |
| 42b33550-1c7e-34b1-b253-3a3d627987e5 | -13.0594 | -51.1409 | 2024-10-03 04:06:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 55.8 |
| bd122e3e-ae29-3474-8200-86a0b00a068c | -13.0971 | -51.1789 | 2024-10-03 04:06:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 69.5 |
| e58a3804-f06a-3eb7-be05-4f763c51c2c1 | -13.0975 | -51.1575 | 2024-10-03 04:06:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 92.7 |
| 423a27ec-e996-3112-b118-f1dcc0defc43 | -12.9741 | -62.6409 | 2024-10-03 04:06:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 73.3 |
| 03a642e2-7433-3061-bebf-d5279f47df5c | -13.5562 | -51.2489 | 2024-10-03 04:06:22 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 176.3 |
| bcbee086-cf07-3af4-92ea-8b1968c4fadd | -13.5002 | -51.1492 | 2024-10-03 04:06:22 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 57.0 |
| f48ab80b-ee03-34f7-9525-7a1c11313488 | -13.5195 | -51.1467 | 2024-10-03 04:06:22 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 181.4 |
| 29470308-1ef2-31da-801c-a33ba10a2a5e | -13.5198 | -51.1252 | 2024-10-03 04:06:22 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 102.1 |
| a12943d9-424f-3dcc-aa34-6adee6f9fc27 | -13.5387 | -51.1442 | 2024-10-03 04:06:22 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 85.6 |
| f7e364b1-c011-3e3a-8833-5460b66c3b35 | -13.5565 | -51.2275 | 2024-10-03 04:06:22 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 94.7 |
| bf883377-6bae-3462-8c92-0dc1159207bf | -13.5754 | -51.2464 | 2024-10-03 04:06:22 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 69.6 |
| 68a50841-1ede-3897-98a4-ee11cc67118d | -16.6685 | -57.3945 | 2024-10-03 04:06:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 61.0 |
| 6f34ae0d-0d70-3906-8fcb-63ba02e5592a | -16.6492 | -57.3763 | 2024-10-03 04:06:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 53.9 |
| fc82ebaa-0549-3412-aceb-2a481c0f3bf7 | -16.6688 | -57.374 | 2024-10-03 04:06:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 96.4 |
| 35bc2686-5846-3577-84c4-632fd020757a | -16.6884 | -57.3718 | 2024-10-03 04:06:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 60.3 |
| 94219c69-c01f-368f-ae86-a01a92699fed | -16.8983 | -57.6949 | 2024-10-03 04:06:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 67.1 |
| fa78ebd4-e54c-3a30-acda-e892a50883ef | -16.9176 | -57.7131 | 2024-10-03 04:06:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 59.2 |
| 6a6b9bdd-8dea-3d03-a5ad-cc15097ff19b | -16.9179 | -57.6926 | 2024-10-03 04:06:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 54.3 |
| 2fdbfbec-689f-3b37-815c-aa57d6d86f1d | -19.0344 | -43.1944 | 2024-10-03 04:06:51 | GOES-16 | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 104.4 |
| c02c824c-77e0-3bf5-8baf-40c37b041b31 | -19.9009 | -42.1074 | 2024-10-03 04:06:55 | GOES-16 | SANTA RITA DE MINAS | MINAS GERAIS | Brasil | 3159357 | 31 | 33 | nan | nan | nan | Mata Atlântica | 80.4 |
| 8bad19ac-6d45-356d-8c86-4860e50a1c90 | -21.4623 | -44.5806 | 2024-10-03 04:07:03 | GOES-16 | CARRANCAS | MINAS GERAIS | Brasil | 3114600 | 31 | 33 | nan | nan | nan | Mata Atlântica | 108.3 |
| 773390da-3053-3b5a-824a-707600849034 | -21.346 | -55.6626 | 2024-10-03 04:07:04 | GOES-16 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 68.5 |
| 9276c292-dbc4-3156-8d3b-abfa727e70bf | -4.095 | -48.4679 | 2024-10-03 04:15:29 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 60.8 |
| e8d77833-f063-3858-abf1-d8bfb4a51cf5 | -4.0949 | -48.4894 | 2024-10-03 04:15:29 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 76.7 |
| fba3cd0f-79d9-3daf-936f-8749c1665379 | -8.9791 | -67.4099 | 2024-10-03 04:15:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 41.4 |
| 1f72f314-c0e3-3356-a7ee-42ebb0db88df | -9.0149 | -67.7423 | 2024-10-03 04:15:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 39.5 |
| 171337fe-6407-3abd-b328-a32c574f1529 | -9.0515 | -67.871 | 2024-10-03 04:15:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 38.8 |
| 8f29c61a-986b-3572-8e74-7d8d39e2fb61 | -10.8942 | -63.8971 | 2024-10-03 04:16:08 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 68.2 |
| 4b165802-a9d4-32cf-bf45-4c9d5b627023 | -11.6822 | -47.7045 | 2024-10-03 04:16:12 | GOES-16 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 74.2 |
| 895fdca4-bd9a-35e7-b674-e189cbcfa02f | -11.6931 | -64.9974 | 2024-10-03 04:16:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 68.9 |
| 3ff96806-0661-381b-9a05-1e7ee3010326 | -11.6932 | -64.9785 | 2024-10-03 04:16:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 73.1 |
| 66561d27-6153-37de-bafb-c0466e21412b | -12.4038 | -63.0009 | 2024-10-03 04:16:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 219.3 |
| bcf28394-3c7f-3928-ab5f-75131bc1ac40 | -12.404 | -62.9817 | 2024-10-03 04:16:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 133.1 |
| a40482fe-bfd9-32a8-9b6a-3354dbffaedd | -12.4227 | -62.9999 | 2024-10-03 04:16:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 135.4 |
| 3e3266a1-68ce-3ebb-bbbc-c2da9875e654 | -12.4228 | -62.9807 | 2024-10-03 04:16:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 88.4 |
| 5d4c22b0-db00-329a-8255-75a650c434a2 | -12.881 | -62.4538 | 2024-10-03 04:16:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 71.6 |
| 6e35b785-dce8-3e29-a7d2-69200fb903cd | -12.8996 | -62.4913 | 2024-10-03 04:16:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 98.1 |
| 3db2ae74-f0e4-3b31-9f00-43a70a26eb99 | -12.8998 | -62.472 | 2024-10-03 04:16:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 123.4 |
| ec7adad2-d96b-3083-97af-51cd3b40096c | -12.8999 | -62.4527 | 2024-10-03 04:16:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 71.0 |
| 57a06860-2c78-334b-b055-32bc64945e3a | -13.0783 | -51.1599 | 2024-10-03 04:16:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 74.9 |
| f971bfb8-c85c-37ce-8a00-12b25fd29540 | -12.9741 | -62.6409 | 2024-10-03 04:16:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 73.5 |
| 04cb8bea-f585-3bf3-85d4-0a8128ac9209 | -13.0975 | -51.1575 | 2024-10-03 04:16:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 91.9 |
| 37e2d0bb-a0fd-33b9-9970-a697a2dec0b0 | -13.5387 | -51.1442 | 2024-10-03 04:16:22 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 118.9 |
| 3229b631-a3aa-330e-ad8f-208cda2cd305 | -13.5198 | -51.1252 | 2024-10-03 04:16:22 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 188.2 |
| 731c2065-9461-3165-9172-cf83173a0a22 | -13.5195 | -51.1467 | 2024-10-03 04:16:22 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 213.7 |
| 0e986863-83fc-3406-9bf3-77bbae84a771 | -13.5006 | -51.1277 | 2024-10-03 04:16:22 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 65.4 |
| b7bd9b95-c7e1-35f9-b678-fa299d05f0cd | -13.5565 | -51.2275 | 2024-10-03 04:16:22 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 104.0 |
| c2c94ea7-ba1d-37d6-bef7-4efe1e31cccc | -13.5562 | -51.2489 | 2024-10-03 04:16:22 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 125.2 |
| 295ee649-2639-355a-a671-d591c311bc0c | -13.5391 | -51.1228 | 2024-10-03 04:16:22 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 85.0 |
| 5eb98818-7e30-309b-9d69-eedf55650a5d | -16.779 | -57.8306 | 2024-10-03 04:16:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 55.0 |
| 49feb15c-5f92-3395-902f-66af184a4186 | -16.8983 | -57.6949 | 2024-10-03 04:16:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 59.2 |
| 1c184326-06f0-3ee6-aa8c-678132e22ed6 | -19.0344 | -43.1944 | 2024-10-03 04:16:51 | GOES-16 | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 71.2 |
| 916c5d35-3585-3285-bfc6-3f31654760b4 | -21.3882 | -47.6261 | 2024-10-03 04:17:04 | GOES-16 | SÃO SIMÃO | SÃO PAULO | Brasil | 3550902 | 35 | 33 | nan | nan | nan | Cerrado | 80.8 |
| d20fc2a7-0fa9-3e54-9f2f-0549a227995e | -21.346 | -55.6626 | 2024-10-03 04:17:04 | GOES-16 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 48.4 |
| 22f875ce-0b3d-3df9-b630-57d5551ff493 | -2.53659 | -47.23207 | 2024-10-03 04:25:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d9df1758-0abf-3e85-b11b-d0705b039b31 | -4.86893 | -38.43489 | 2024-10-03 04:25:00 | NOAA-21 | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| b0741cba-d66f-3758-9999-17482f973cab | -4.86835 | -38.43378 | 2024-10-03 04:25:00 | NOAA-21 | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| d9339b4b-7f78-3ddf-a6e8-59c4530385c0 | -4.70678 | -40.02336 | 2024-10-03 04:25:00 | NOAA-21 | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 60343558-f3cf-3ace-bb1f-2164aa5c8cb8 | -4.70256 | -40.02253 | 2024-10-03 04:25:00 | NOAA-21 | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| e9eb53ab-823c-3cb6-968f-cde4d448a7f5 | -4.70204 | -40.02606 | 2024-10-03 04:25:00 | NOAA-21 | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| c0dc9381-15ed-371f-aa64-aa4a34320412 | -2.83106 | -40.3604 | 2024-10-03 04:25:00 | NOAA-21 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 85653252-4323-3a20-9cf3-72c0816c7217 | -6.25565 | -41.85271 | 2024-10-03 04:25:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 152b900c-d59a-3d7c-856e-2301ce631eea | -6.25494 | -41.85751 | 2024-10-03 04:25:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| cada93a2-a854-3142-bf76-6727e0f67c8b | -6.8229 | -41.81495 | 2024-10-03 04:25:00 | NOAA-21 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| ce82ece5-4ca6-3fa8-bf39-37210cabf199 | -8.21569 | -41.4038 | 2024-10-03 04:25:00 | NOAA-21 | SÃO FRANCISCO DE ASSIS DO PIAUÍ | PIAUÍ | Brasil | 2209658 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| ea36976c-2d66-3f7e-97da-b45f717e55c3 | -8.21564 | -41.40493 | 2024-10-03 04:25:00 | NOAA-21 | SÃO FRANCISCO DE ASSIS DO PIAUÍ | PIAUÍ | Brasil | 2209658 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 587851df-9db7-3292-bf87-166e10dd3b3f | -8.21519 | -41.40744 | 2024-10-03 04:25:00 | NOAA-21 | SÃO FRANCISCO DE ASSIS DO PIAUÍ | PIAUÍ | Brasil | 2209658 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 58f2e207-3038-3a46-883e-528d55d5a8f4 | -8.2151 | -41.40857 | 2024-10-03 04:25:00 | NOAA-21 | SÃO FRANCISCO DE ASSIS DO PIAUÍ | PIAUÍ | Brasil | 2209658 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 7e34badd-537b-3bee-8830-08d7d55ca3d0 | -2.92341 | -41.46891 | 2024-10-03 04:25:00 | NOAA-21 | LUÍS CORREIA | PIAUÍ | Brasil | 2205706 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 0da5d39e-1b59-37ea-88ec-1d20cfbe95ab | -3.10561 | -42.63114 | 2024-10-03 04:25:00 | NOAA-21 | TUTÓIA | MARANHÃO | Brasil | 2112506 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 03f3df73-9568-3783-90d5-5da1644f2c20 | -3.10268 | -42.62656 | 2024-10-03 04:25:00 | NOAA-21 | TUTÓIA | MARANHÃO | Brasil | 2112506 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 271aef38-7e10-3b9f-be95-1518eb8ba40f | -3.41536 | -42.27186 | 2024-10-03 04:25:00 | NOAA-21 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 0bfadb58-35aa-38fc-9c69-2a3bda82c40a | -3.41469 | -42.27615 | 2024-10-03 04:25:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| bf449a29-7c97-3000-b186-18686a9865e3 | -3.41404 | -42.28038 | 2024-10-03 04:25:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 26.1 |
| bb436450-e7ff-3bdf-b433-1acc671952a3 | -3.41338 | -42.28458 | 2024-10-03 04:25:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 26.1 |
| 1dddd84a-d012-39cf-b7cf-5fb9391b167f | -3.41238 | -42.26711 | 2024-10-03 04:25:00 | NOAA-21 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 00e77fac-d634-39f7-b572-6ce4b253ac0d | -3.41173 | -42.27131 | 2024-10-03 04:25:00 | NOAA-21 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| adc2dc15-20cc-378a-879e-f5bc78dfc5eb | -3.41107 | -42.27558 | 2024-10-03 04:25:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| d830563a-ec6c-318d-a0e7-e6cce1168f90 | -3.41041 | -42.27983 | 2024-10-03 04:25:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 26.1 |
| b75d014c-2442-38e8-aa17-9b2ca1ebec41 | -3.40976 | -42.28404 | 2024-10-03 04:25:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 26.1 |
| 7bfc1190-8659-3f77-8338-4e445cf550c2 | -3.4091 | -42.28825 | 2024-10-03 04:25:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |


[Clique aqui para ver as próximas entradas](README76.md)
