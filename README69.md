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

## Dados Diários - Página 69

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 54777dfb-b72d-3743-8df4-cfd599adae6a | -7.7881 | -47.8607 | 2026-08-17 13:30:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 85.2 |
| 3cf320fc-351e-3942-97a5-83f860022c57 | -13.5128 | -46.2219 | 2026-08-17 13:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 77.2 |
| bc518ddd-e312-300e-be09-411cb6cc8dba | -8.5212 | -54.9016 | 2026-08-17 13:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 74.3 |
| 18c6417e-7da4-399f-8672-6465254dbc85 | -9.7908 | -47.223 | 2026-08-17 13:30:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 115.8 |
| f3f5a302-f870-30ec-b3b3-4587ed5a9b21 | -9.127 | -46.0214 | 2026-08-17 13:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 144.5 |
| 0c56ab41-4526-3d8d-95b0-437c207e0ab4 | -6.6199 | -58.9643 | 2026-08-17 13:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 73.8 |
| c217926f-99ac-32e7-94b6-8a2c649e4ad5 | -12.6629 | -48.5027 | 2026-08-17 13:30:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 91.1 |
| 504dc3f9-f143-3fa4-9788-903c0d6ec02a | -11.3119 | -45.866 | 2026-08-17 13:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 90.2 |
| 6d934539-092d-3be0-bf86-21197675aa47 | -14.3926 | -51.8654 | 2026-08-17 13:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 73.6 |
| 940ae9f2-73cc-3317-b24a-f72e6891f34e | -15.8242 | -54.2114 | 2026-08-17 13:30:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 69.0 |
| d4d0cbbb-439b-3c15-a2b3-2fbac7ceee04 | -14.3733 | -51.8679 | 2026-08-17 13:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 57.5 |
| cf6677d8-e00f-306d-b9d9-fb677fdd4832 | -14.4871 | -51.9806 | 2026-08-17 13:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 142.4 |
| 9dc24063-977e-3d48-9d10-4a2182e25115 | -14.3718 | -51.9533 | 2026-08-17 13:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 84.4 |
| c89fb6da-e118-3ce0-bd03-394462f2de9b | -6.2563 | -47.7611 | 2026-08-17 13:30:00 | GOES-19 | LUZINÓPOLIS | TOCANTINS | Brasil | 1712454 | 17 | 33 | nan | nan | nan | Cerrado | 69.5 |
| 86cd96e0-cef6-3eb8-9ed7-01712c703d7f | -12.5392 | -47.9 | 2026-08-17 13:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 124.9 |
| e0e716f7-bcac-3ff3-8b38-bb75c9985e8c | -14.3912 | -51.9508 | 2026-08-17 13:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 2f37e1df-4b36-3b80-ac32-ea6469847c14 | -7.6053 | -45.7238 | 2026-08-17 13:30:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 166.9 |
| c61976db-1f4e-3244-934f-b40919c2425e | -11.5095 | -46.6092 | 2026-08-17 13:30:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 65.7 |
| 9aefedb5-200a-37ea-96e3-d82b157feb09 | -9.7905 | -47.2452 | 2026-08-17 13:30:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 102.6 |
| 692e55a3-5441-3072-ae3e-da3a6f04b7ff | -7.3824 | -55.4924 | 2026-08-17 13:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 79.5 |
| d83fcf23-6380-329a-ab86-a6c2cd934fe9 | -13.2805 | -51.6886 | 2026-08-17 13:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 156.5 |
| 7da3401a-d1ad-38c8-9e29-17aef48aa0f2 | -13.2613 | -51.691 | 2026-08-17 13:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 63.4 |
| ccdfe9d2-7517-3321-9700-bffebc99405b | -7.8068 | -47.8591 | 2026-08-17 13:30:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 231.4 |
| 80ad0992-eeac-30e4-b25b-9024253e8e12 | -14.2947 | -53.1052 | 2026-08-17 13:30:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 72.1 |
| 187da883-0e10-3964-ad7b-7ae27df358a4 | -9.3382 | -62.3344 | 2026-08-17 13:30:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 6d93e379-c5f6-32c3-a91a-27055cf3e6ab | -9.7553 | -45.7237 | 2026-08-17 13:30:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 87.8 |
| 366f0660-a2c8-36b1-8869-113e15cd7dd0 | -6.7647 | -59.4601 | 2026-08-17 13:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 125.5 |
| 45be5c2e-e6a8-3c98-a422-5770cf719fde | -14.8619 | -46.6351 | 2026-08-17 13:30:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 102.3 |
| c6cd0727-97cd-3b9d-9fc1-ed6f9df9d89a | -7.7836 | -48.2754 | 2026-08-17 13:30:00 | GOES-19 | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 87.1 |
| 35cc29fe-c5f5-3053-ab3b-84620338938d | -12.7009 | -48.5195 | 2026-08-17 13:30:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 126.9 |
| 36149519-23e3-3aa1-93f2-fd3ad6af6017 | -7.8071 | -47.8372 | 2026-08-17 13:30:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 114.9 |
| 745c7c6a-12c3-3a44-bb80-70ae387a5c94 | -11.472 | -46.5692 | 2026-08-17 13:30:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 88.0 |
| 27ac4226-fe0d-31b6-a670-babeac95b040 | -14.3915 | -51.9294 | 2026-08-17 13:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 84.0 |
| 2fd51481-b7ae-3488-a658-c32d3b941810 | -12.5588 | -47.875 | 2026-08-17 13:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 110.9 |
| 34ca061f-32eb-3364-831a-b825195180f9 | -6.2376 | -47.7624 | 2026-08-17 13:30:00 | GOES-19 | LUZINÓPOLIS | TOCANTINS | Brasil | 1712454 | 17 | 33 | nan | nan | nan | Cerrado | 86.3 |
| a444388b-6f78-326a-b5e2-868f9627ad79 | -6.6384 | -58.9636 | 2026-08-17 13:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 97.6 |
| c8aea907-37cc-3a4e-a42f-5b3e50145052 | -6.6569 | -58.9435 | 2026-08-17 13:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 104.0 |
| eaccbcc2-b1e3-3bd6-b267-b402b21312ad | -13.5124 | -46.2449 | 2026-08-17 13:30:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 73.1 |
| 8cd1315d-c773-3bdc-b76b-c96a2379781b | -14.2751 | -53.1287 | 2026-08-17 13:30:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 719357a0-83e3-38f4-948c-442f04851e32 | -11.4904 | -46.6118 | 2026-08-17 13:40:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 92.0 |
| 80c88ec7-1163-3765-8e50-7a5b0cdd3b83 | -11.5099 | -46.5866 | 2026-08-17 13:40:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 70.3 |
| 1eea3953-8f91-332e-af0b-7f4d127c2c0d | -12.5392 | -47.9 | 2026-08-17 13:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 132.5 |
| c08e2f29-e7e9-31f7-80a0-9a4a89691392 | -6.7647 | -59.4601 | 2026-08-17 13:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 135.9 |
| 579129c0-c69a-3332-a156-093b67335db1 | -14.2947 | -53.1052 | 2026-08-17 13:40:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 73.5 |
| da094780-2a6a-3655-bf39-a5b831eaa75d | -13.2805 | -51.6886 | 2026-08-17 13:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 98.4 |
| 70383ebe-51ad-3fd8-98ef-c1324cbf69ee | -11.5095 | -46.6092 | 2026-08-17 13:40:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 91.8 |
| 141f57c7-d76e-3a60-90ac-6ca7c9438395 | -14.3722 | -51.932 | 2026-08-17 13:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 342.0 |
| 5a33cd45-d6da-39f7-8640-e74b16c3df7e | -14.3718 | -51.9533 | 2026-08-17 13:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 247.9 |
| e1b60de0-938a-34b7-8ee1-f889161b2fc7 | -6.7831 | -59.4594 | 2026-08-17 13:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 94.1 |
| 737ac113-38dc-366f-a545-9f773e750577 | -11.4907 | -46.5892 | 2026-08-17 13:40:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 94.8 |
| a686e423-0a32-36be-90cf-4c6fa36ea277 | -9.127 | -46.0214 | 2026-08-17 13:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 124.2 |
| 7b822a15-6fa1-36e3-9ded-373c812b66bd | -9.3196 | -62.3353 | 2026-08-17 13:40:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 4ba48ba8-8465-3877-88b3-40261f6acbd1 | -6.6014 | -58.9844 | 2026-08-17 13:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 511600f5-d9d2-3eb8-9cc8-30a0e9913f7a | -7.7881 | -47.8607 | 2026-08-17 13:40:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 114.9 |
| fa5d1e67-abd2-38d7-b0c9-cc3f28cb81a6 | -11.3235 | -46.3182 | 2026-08-17 13:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 223.8 |
| 15b9f365-aeb5-3f20-b076-6b9a2fe6827e | -6.6568 | -58.9628 | 2026-08-17 13:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 81.5 |
| e6118bc5-b9c8-3b80-9748-526da07a337d | -14.3926 | -51.8654 | 2026-08-17 13:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 67.0 |
| 88daeb25-48ce-3f64-8bb9-51637aa2f1a9 | -12.5588 | -47.875 | 2026-08-17 13:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 104.5 |
| c9bd9287-b2d4-36c3-a4b0-bdf6429ca461 | -14.3726 | -51.9106 | 2026-08-17 13:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 75.8 |
| a3f53b0b-419d-3eee-a025-cef26c33395c | -13.5124 | -46.2449 | 2026-08-17 13:40:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 110.2 |
| 73aea62b-56cb-3c2e-b2ec-8860165c2cb0 | -7.8068 | -47.8591 | 2026-08-17 13:40:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 142.5 |
| 5e5592ed-533b-376e-9119-dc8f26b6e2d3 | -10.9322 | -57.1511 | 2026-08-17 13:40:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 78.1 |
| e38fd5f4-b819-3573-8eb7-2c3f90256a9a | -14.3912 | -51.9508 | 2026-08-17 13:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 21c16572-b7e0-3313-830c-4b5a98f6bd3e | -11.472 | -46.5692 | 2026-08-17 13:40:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 145.2 |
| ed3dc2de-ab07-3d47-8566-fcbd7da5da0f | -6.6384 | -58.9636 | 2026-08-17 13:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 114.5 |
| bb9f2144-c747-3120-99b9-49fd7e058223 | -14.2751 | -53.1287 | 2026-08-17 13:40:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 75.6 |
| f2fc3851-91b4-3e5f-bdf6-81385c2c24d2 | -6.6199 | -58.9643 | 2026-08-17 13:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 70.3 |
| 3ac6da09-bd03-381e-b291-abe70db29184 | -7.8071 | -47.8372 | 2026-08-17 13:40:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 91.1 |
| 5ab97e69-bf48-36c2-8ab4-ad10364785db | -11.1296 | -46.5244 | 2026-08-17 13:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 98.5 |
| 737eb3ce-ef59-3afc-aa07-042ce6b01314 | -14.3733 | -51.8679 | 2026-08-17 13:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 59.1 |
| 460b4dec-a401-303c-b3ef-efe787864426 | -9.3382 | -62.3344 | 2026-08-17 13:40:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 75.1 |
| ab5e2b38-e728-3bf6-b72e-17c476e43f93 | -14.4871 | -51.9806 | 2026-08-17 13:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 159.2 |
| 34c37f88-f422-39da-a79b-3b8cb5f2d378 | -10.951 | -57.1497 | 2026-08-17 13:40:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 97.6 |
| a913d352-09ff-31c5-aebd-da1aa104c806 | -12.6629 | -48.5027 | 2026-08-17 13:40:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 76.6 |
| fc22c466-4642-334d-ba56-d130369ca239 | -10.5085 | -50.0228 | 2026-08-17 13:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 159.4 |
| e1b097cf-a1d8-3246-bc34-741027c2fab8 | -7.3824 | -55.4924 | 2026-08-17 13:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 79.2 |
| d4d07a43-858a-33ed-986f-b074ace4a760 | -14.8619 | -46.6351 | 2026-08-17 13:40:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 80.8 |
| 9e62f0cc-18f0-3e9c-a473-bd07800f6e58 | -7.6053 | -45.7238 | 2026-08-17 13:40:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 166.9 |
| d09a9063-ae2b-3e5a-b241-ff9af486f940 | -6.2565 | -47.7393 | 2026-08-17 13:40:00 | GOES-19 | LUZINÓPOLIS | TOCANTINS | Brasil | 1712454 | 17 | 33 | nan | nan | nan | Cerrado | 81.0 |
| aa49d830-b339-32bd-b885-0347addbc6a9 | -11.2314 | -54.0164 | 2026-08-17 13:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 100.2 |
| b0d5b328-c193-343e-9204-3a597680c0b0 | -12.7009 | -48.5195 | 2026-08-17 13:40:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 107.7 |
| 52ff9201-7f30-3834-afe5-a179da255c21 | -14.4868 | -52.002 | 2026-08-17 13:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 90.2 |
| 62556d5c-2688-3b8e-9f6a-b5b814d6e48d | -11.7914 | -51.7767 | 2026-08-17 13:40:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 93.3 |
| c78213bd-0655-3404-b91a-63887af25e75 | -13.5128 | -46.2219 | 2026-08-17 13:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 89.9 |
| c8d03617-8e5d-34d2-bce4-478025f1234e | -11.4716 | -46.5918 | 2026-08-17 13:40:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 88.5 |
| f31e53b5-355b-3f28-9fd2-6ffb0a17d518 | -15.8246 | -54.1904 | 2026-08-17 13:40:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 75.6 |
| b1fe7c46-4025-38ae-a7a9-ea70add76a12 | -9.1998 | -60.793 | 2026-08-17 13:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 70.1 |
| c00830a1-60c3-3efb-8c4a-a381c8f54143 | -14.3906 | -53.1354 | 2026-08-17 13:50:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 85.0 |
| c03c7da6-c8c7-3b5b-aae8-7b63eb8172a7 | -6.6384 | -58.9636 | 2026-08-17 13:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 107.9 |
| ed0a8859-c84e-3786-96af-9c1f9b420bec | -9.3196 | -62.3353 | 2026-08-17 13:50:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 237424fd-2dd7-3aee-bf81-0ad8c2231aa5 | -6.6198 | -58.9836 | 2026-08-17 13:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 54.7 |
| 4262adad-3c4f-3ab0-81b4-5b5eb269a2bb | -10.9508 | -57.1696 | 2026-08-17 13:50:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 59.1 |
| cc1ce6d8-47b9-3376-8f11-9b26dfdb727f | -11.3239 | -46.2955 | 2026-08-17 13:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 92.4 |
| 467141e6-cfb7-3ed1-9336-fd6e251f5de9 | -10.9322 | -57.1511 | 2026-08-17 13:50:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 64.8 |
| b5be905e-cf94-3f2e-b072-8303779d6de3 | -22.0767 | -55.9708 | 2026-08-17 13:50:00 | GOES-19 | PONTA PORÃ | MATO GROSSO DO SUL | Brasil | 5006606 | 50 | 33 | nan | nan | nan | Cerrado | 113.3 |
| f2d17e14-72b2-3859-ae20-051ef90aa08f | -12.5392 | -47.9 | 2026-08-17 13:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 76.2 |
| 87f9ffea-9193-3340-b7e3-f46ee4aa793e | -11.3235 | -46.3182 | 2026-08-17 13:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 333.0 |
| c388a998-89c4-339e-af8d-00d1d7b5ded4 | -7.8068 | -47.8591 | 2026-08-17 13:50:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 192.0 |
| f5972fce-0c49-3606-8f73-e990a49eddd9 | -13.5128 | -46.2219 | 2026-08-17 13:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 88.9 |
| 02ef0d09-4e85-3c3e-a402-288a1a0f602e | -8.9601 | -60.5165 | 2026-08-17 13:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 65.4 |


[Clique aqui para ver as próximas entradas](README70.md)
