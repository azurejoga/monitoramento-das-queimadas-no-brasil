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

## Dados Diários - Página 89

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 02d68290-4e47-3dfd-b422-6070c7830993 | -4.27115 | -50.77927 | 2026-10-01 05:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 18.8 |
| 38a568ae-ee72-3513-8561-6cdb02e1a3ad | -4.31537 | -50.73095 | 2026-10-01 05:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f53b34d3-de29-3abe-a5ae-1c5c67bff069 | -3.71773 | -58.79538 | 2026-10-01 05:55:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ceb603e4-0b31-317e-8bb6-65b63e4bc27b | -3.49053 | -59.52856 | 2026-10-01 05:55:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 89a628b6-4b3a-32d0-a25d-828f7b40d634 | -4.25251 | -50.75388 | 2026-10-01 05:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 27.8 |
| f2191415-a488-3f37-ada8-c9abe49f647e | -10.35715 | -55.44458 | 2026-10-01 05:55:00 | NPP-375D | NOVA GUARITA | MATO GROSSO | Brasil | 5108808 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 46944ed9-58e7-360d-8321-847eb265a9c7 | -4.03773 | -54.22857 | 2026-10-01 05:55:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3d6c588c-9460-3328-b6c3-aba4186bf8f3 | -9.70917 | -65.06258 | 2026-10-01 05:55:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f895bf25-4465-3685-aede-ff9a9b799b21 | -4.25556 | -50.77369 | 2026-10-01 05:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 89b2279d-4336-3beb-ac55-2fedfa6adb21 | -9.66607 | -65.03016 | 2026-10-01 05:55:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2898b466-44e7-370e-b365-db45e9613976 | -4.04248 | -54.22226 | 2026-10-01 05:55:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8de57fb2-aabf-3966-8eba-6f4c200787e9 | -4.25984 | -50.7448 | 2026-10-01 05:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 22.5 |
| c8dee84e-0a29-3434-8c99-e05490e4c013 | -3.98704 | -56.08581 | 2026-10-01 05:55:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| acdd2cba-eab5-3a5c-ae51-f35701bada28 | -3.28784 | -53.85966 | 2026-10-01 05:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 6a04ec7e-91d9-347f-9ae6-6f32af402166 | -4.27839 | -50.78056 | 2026-10-01 05:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 115.2 |
| bbb9ee38-aee7-3802-b359-733f44e411cf | -10.53568 | -57.78098 | 2026-10-01 05:55:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 67840b33-3e2a-3740-b89c-2b12d8b0f77f | -4.05951 | -51.09591 | 2026-10-01 05:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6d4f4d49-ab14-358d-834f-abb265131f5d | -10.53647 | -57.77508 | 2026-10-01 05:55:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c8a9c9b6-e4cd-3876-a5b3-b53165a93126 | -4.30758 | -50.73242 | 2026-10-01 05:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 88b6261b-13ef-3385-b78e-096e59dcceb6 | -4.30199 | -50.77409 | 2026-10-01 05:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 121.4 |
| 893e444e-de1a-3aec-a767-68d6fa0cd1ab | -2.88498 | -54.87631 | 2026-10-01 05:55:00 | NPP-375D | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e2ac0214-280c-35f6-8d3a-b20c454d2107 | -3.804 | -59.29995 | 2026-10-01 05:55:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cc535c41-af5c-365d-a9c5-75b20d8590a3 | -4.04014 | -54.23861 | 2026-10-01 05:55:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| ec4c09af-9f41-35bc-96dc-420e7c4eb11e | -11.17264 | -54.11251 | 2026-10-01 05:55:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8c33dd82-b952-30ec-a558-cdd13a547643 | -3.14492 | -53.73865 | 2026-10-01 05:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6556807d-4869-3d58-b1d2-e07bcbc7b094 | -4.26186 | -50.74024 | 2026-10-01 05:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 18.5 |
| d3679f75-82a6-3764-9c47-f9212e97c9cf | -4.30073 | -50.72925 | 2026-10-01 05:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 7c995add-422c-3e62-a047-f8052d891da4 | -4.30705 | -50.73735 | 2026-10-01 05:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| ebd522a0-b26e-334c-a8c6-abac30243445 | -4.30926 | -50.77513 | 2026-10-01 05:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| caaa5196-993d-39b1-b712-8a245452e671 | -9.31045 | -57.7107 | 2026-10-01 05:55:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4172da59-ccd9-3f20-8adb-0896b776ba41 | -3.1554 | -54.07886 | 2026-10-01 05:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 79966e2b-a80b-30bd-91f5-900c3f24c58b | -10.52512 | -57.78253 | 2026-10-01 05:55:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 410c6bcb-de63-3685-9a1e-89c87da75ad9 | -11.38018 | -55.12471 | 2026-10-01 05:55:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7d9764a7-d5e7-39a9-8f3d-c22a467c12ab | -4.04125 | -54.23091 | 2026-10-01 05:55:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| eb8ee6b0-9dda-3870-8a5c-af5f0f0bd946 | -3.70774 | -59.68034 | 2026-10-01 05:55:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| be9e59ec-39bf-32c6-acfa-7be038e9a434 | -4.29292 | -50.78257 | 2026-10-01 05:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 110.4 |
| 0145216d-caf0-35b3-93e3-f30ee462732a | -9.35433 | -57.17546 | 2026-10-01 05:55:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 045e296f-3d96-3df5-9def-efd2c9d98d35 | -10.77373 | -54.75469 | 2026-10-01 05:55:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 58d34b93-9927-3b8b-bb12-ed7499c6d1d8 | -7.78438 | -72.90073 | 2026-10-01 05:55:00 | NPP-375D | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f0b794c7-39e3-3ef6-b9fc-b84739ae8803 | -9.37467 | -65.46664 | 2026-10-01 05:55:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 281dbc02-0ed4-3865-a76e-e005314f5bff | -10.77432 | -54.74979 | 2026-10-01 05:55:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5f2bdc23-d3f0-3bdd-ad38-6259dd86c0e4 | -4.28778 | -50.76674 | 2026-10-01 05:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 54.2 |
| 5b4723bc-da96-3d85-8d55-1a63ca487c5d | -11.26115 | -54.82042 | 2026-10-01 05:55:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2d017f2a-4495-32ee-8b2e-5165cd95e5ee | -4.2567 | -50.7767 | 2026-10-01 05:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 38939aea-e50e-3df6-871e-7ca35e617ba2 | -4.28361 | -50.74402 | 2026-10-01 05:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 913e80da-4e04-31b4-a335-7e28b14ca48e | -9.34994 | -57.16875 | 2026-10-01 05:55:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0bdda98f-a9e7-3ce7-99ed-40e3c6cea14e | -10.56503 | -57.77345 | 2026-10-01 05:55:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1873fd6e-1af2-3563-a5c1-c815436e52d9 | -3.80766 | -51.03253 | 2026-10-01 05:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 1c961f4a-6a4a-3bbc-a94c-2bc4aad690b3 | -10.83025 | -57.20299 | 2026-10-01 05:55:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6235fccb-0bfc-3cb3-a3d7-f6abad091496 | -10.54116 | -57.77877 | 2026-10-01 05:55:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4a1e5c41-5da1-3bf0-9fe3-e73183818c4f | -2.88338 | -54.87882 | 2026-10-01 05:55:00 | NPP-375D | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 20a3b9ba-62b2-3279-a4a4-936983941a8f | -3.67469 | -62.9543 | 2026-10-01 05:55:00 | NPP-375D | COARI | AMAZONAS | Brasil | 1301209 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9a5e2f3a-858b-3391-aad7-704916723eb1 | -4.30096 | -50.78153 | 2026-10-01 05:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 73.2 |
| bdb225b1-ef48-35c6-95e1-d34154d46594 | -4.06069 | -51.10759 | 2026-10-01 05:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 03ab4077-0924-3b31-8829-4e17999eaea2 | -4.2826 | -50.75107 | 2026-10-01 05:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 21ebce74-4a91-30b7-b1de-2a56167c1f58 | -4.27741 | -50.78737 | 2026-10-01 05:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 44.8 |
| 874c6c59-0295-35c2-82ec-1e6346b26ac5 | -4.29974 | -50.73649 | 2026-10-01 05:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 1085ed17-58ce-3a3b-afbf-610fb76936d7 | -10.53726 | -57.76913 | 2026-10-01 05:55:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a3da17b6-f0c7-3d55-8d2f-50b006d93df5 | -13.66059 | -53.93383 | 2026-10-01 05:55:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 16.4 |
| cb952741-0239-3ba5-984c-8be2e0790569 | -9.96224 | -59.26129 | 2026-10-01 05:55:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 82fd1f29-9a59-35ae-8d8c-a2781315e459 | -10.07037 | -63.07632 | 2026-10-01 05:55:00 | NPP-375D | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 0c2ecb16-bd8c-3356-9588-f297a628f16a | -4.28886 | -50.75921 | 2026-10-01 05:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 54.2 |
| df0e3b25-eb42-3022-8d08-762967206b4d | -4.04362 | -54.2293 | 2026-10-01 05:55:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a5aef66c-027f-30fc-8ecc-7abcaa4c0a14 | -13.65936 | -53.94583 | 2026-10-01 05:55:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 750d8299-051d-3169-9f5e-2913f483ac35 | -13.65383 | -53.93299 | 2026-10-01 05:55:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 39869118-cabb-3a2a-a2f4-5af1415378d1 | -9.30658 | -57.7096 | 2026-10-01 05:55:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f1d70ef9-7934-3dd6-8aee-620c1e6d6e9e | -4.2608 | -50.74776 | 2026-10-01 05:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 18.5 |
| fad18a13-04d2-375d-a14e-7df5be9398b9 | -9.35476 | -57.17234 | 2026-10-01 05:55:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a66dac38-fc4e-341c-b8dc-c9e528dcef09 | -4.29921 | -50.73892 | 2026-10-01 05:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 919b01e9-aa10-3586-ad9b-5fea5f0465e3 | -13.64485 | -53.93166 | 2026-10-01 05:55:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 51f7971a-8553-3f4b-86a7-0782e54f4146 | -3.17565 | -54.10344 | 2026-10-01 05:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 1b711a31-8d9f-3816-aa6d-4479d738a84a | -10.07274 | -63.08519 | 2026-10-01 05:55:00 | NPP-375D | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8c665fc4-65b2-3ae3-97ee-cd4a99f1e8e3 | -11.26381 | -54.81414 | 2026-10-01 05:55:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 688a3b99-0720-3090-88c9-9abd146aa656 | -10.53099 | -57.77729 | 2026-10-01 05:55:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2d8fd590-71a4-3404-a040-6f2706940d05 | -3.16125 | -54.07981 | 2026-10-01 05:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f4d78bdf-3f1a-3644-804c-0ee9367c6939 | -10.53179 | -57.77132 | 2026-10-01 05:55:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 445c8ab7-4bb8-3b51-bc20-64cefbc91d31 | -10.55135 | -57.78003 | 2026-10-01 05:55:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5e074dbd-a8b1-3fc7-a8ca-74962862f315 | -3.16458 | -54.09749 | 2026-10-01 05:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e85d379b-583b-3c95-8460-9785caecca7e | -3.16187 | -54.07563 | 2026-10-01 05:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7a77a081-74de-320a-812f-064a1074d873 | -3.29507 | -53.85197 | 2026-10-01 05:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| a0978505-0e0a-3c77-9aa8-8f0be45daaac | -3.07504 | -54.37276 | 2026-10-01 05:55:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f71261fb-eb56-3142-bed7-507231b12d96 | -12.26268 | -53.99884 | 2026-10-01 05:55:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| af8ca29f-78df-30a3-b7dc-52abb4b15d65 | -4.26537 | -59.88614 | 2026-10-01 05:55:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 50bd1079-cef2-3865-a431-fbb7b0c29f4c | -13.64712 | -53.93162 | 2026-10-01 05:55:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 2b88818d-7108-3cea-954e-5f0a63fbe008 | -3.14429 | -53.74302 | 2026-10-01 05:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e9f5f9b1-1a57-3875-85a4-bc4d870babe9 | -3.01514 | -53.87793 | 2026-10-01 05:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| fc48ac48-54c8-3128-9a85-96b1ba2f3dca | -9.31161 | -57.71021 | 2026-10-01 05:55:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 88408b82-1016-306b-96d0-18efcb94031d | -3.14365 | -53.74738 | 2026-10-01 05:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 73777125-8d35-3814-b818-b1bcc1bb81d7 | -10.35122 | -55.44385 | 2026-10-01 05:55:00 | NPP-375D | NOVA GUARITA | MATO GROSSO | Brasil | 5108808 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8a86790b-de40-3ea8-95ef-38f22019017f | -10.8298 | -57.20641 | 2026-10-01 05:55:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dae53c7c-8c16-30a5-966a-984cef0d3eef | -3.62969 | -54.50339 | 2026-10-01 05:55:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1be630f1-5a9c-3b39-9fcd-887ee1ff9408 | -10.06913 | -63.08464 | 2026-10-01 05:55:00 | NPP-375D | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c9d2e35a-e3f8-3215-8d7a-d77ecb06ec38 | -4.26288 | -50.73303 | 2026-10-01 05:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 7bcb49f1-3a4a-35e6-af98-fc1714107cb0 | -3.01782 | -53.88022 | 2026-10-01 05:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7e06c200-e93a-35b7-bed9-74ed21144bc2 | -10.5654 | -57.77054 | 2026-10-01 05:55:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7e43c792-3dea-33a2-919c-0c5c46aa8495 | -10.46871 | -59.13124 | 2026-10-01 05:55:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5a903769-56ca-348a-ab49-c3fdc0b51904 | -10.55758 | -57.77227 | 2026-10-01 05:55:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 09727ded-3bf8-35af-b285-934de9ae759f | -3.0172 | -53.88448 | 2026-10-01 05:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7270de57-469c-369d-8c96-84f00d9044c1 | -4.305 | -50.75225 | 2026-10-01 05:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 9f2a4d19-eb11-3cbe-a88e-d445423c6cbb | -4.26428 | -59.88909 | 2026-10-01 05:55:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README90.md)
