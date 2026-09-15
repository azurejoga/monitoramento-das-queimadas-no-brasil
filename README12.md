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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 239bea36-625d-358f-9187-e521edfebd44 | -8.0828 | -50.971199 | 2026-09-15 00:25:00 | METOP-C | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 42d65a06-da72-3a11-8928-aea57716002f | -7.1081 | -41.799801 | 2026-09-15 00:25:00 | METOP-C | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| c4b03d80-0f6c-345c-9722-1dc68f4e38b7 | -4.6642 | -42.070801 | 2026-09-15 00:25:00 | METOP-C | NOSSA SENHORA DE NAZARÉ | PIAUÍ | Brasil | 2206753 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 5723d10e-4453-3c51-9dbb-195960ddd20f | -5.9616 | -49.260399 | 2026-09-15 00:25:00 | METOP-C | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a02ea41a-3603-34fb-8a7d-cb97825ee196 | -2.9092 | -50.3927 | 2026-09-15 00:25:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b9e33d0d-4f5e-31c9-9b9d-9e8a7f325796 | -7.6097 | -47.2878 | 2026-09-15 00:25:00 | METOP-C | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7fdf7220-9e47-31e4-9083-09cdf793a4a7 | -7.1578 | -42.0993 | 2026-09-15 00:25:00 | METOP-C | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 646360eb-5b60-3c9f-93f2-7e5547ecdb90 | -15.5823 | -48.8181 | 2026-09-15 00:25:00 | METOP-C | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| c9e6c1d0-313f-3dda-a63e-33d65f26d3fa | -12.4773 | -41.397999 | 2026-09-15 00:25:00 | METOP-C | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| b880468c-94b3-3ba0-94e0-bf13c766b925 | -8.4846 | -44.581402 | 2026-09-15 00:25:00 | METOP-C | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| f3b4eb83-df50-3031-bf31-6da569371f09 | -1.7781 | -54.4533 | 2026-09-15 00:25:00 | METOP-C | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3b3089ba-4a68-3e02-8931-5a3a18cf8a2c | -5.9637 | -49.269901 | 2026-09-15 00:25:00 | METOP-C | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a16d0dad-3723-3f56-b6c9-72f41e04fadd | -5.7233 | -46.174198 | 2026-09-15 00:25:00 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c361293b-9890-3a92-9a95-6e13f8d14eae | -4.3649 | -47.772999 | 2026-09-15 00:25:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d5593a3e-6b19-34e0-96ea-206d5c9dca1d | -7.3798 | -49.510201 | 2026-09-15 00:25:00 | METOP-C | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6755bd94-587d-3442-b9cb-a8d12980c82a | -11.8776 | -43.816601 | 2026-09-15 00:25:00 | METOP-C | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c82b43d7-1d07-3a7d-9862-b538c2322449 | -8.5947 | -44.476898 | 2026-09-15 00:25:00 | METOP-C | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 1d6f0dea-f5e5-3d1e-b875-49a921cd55d8 | -6.7379 | -43.086899 | 2026-09-15 00:25:00 | METOP-C | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2c240622-4bcf-39e7-8d12-642a368fb25a | -4.1746 | -49.396198 | 2026-09-15 00:25:00 | METOP-C | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f39ff8f9-659b-369a-add2-1ad9ac08a965 | -7.0825 | -41.8228 | 2026-09-15 00:25:00 | METOP-C | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| ef5ad610-835c-30fb-96f8-368e1c881879 | -4.9514 | -45.139 | 2026-09-15 00:25:00 | METOP-C | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| bb1bd173-fd47-3ad9-bfb0-8c858c357c55 | -10.5836 | -47.7449 | 2026-09-15 00:25:00 | METOP-C | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b90dd4f9-4757-3459-b331-9083cda0d5f5 | -7.1596 | -42.107201 | 2026-09-15 00:25:00 | METOP-C | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 6aba8590-7c07-3ae0-8700-fb6f0ebc6c9f | -4.3026 | -49.096199 | 2026-09-15 00:25:00 | METOP-C | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f1621d49-0563-3f7f-9bd3-484b09ed7fe6 | -6.9461 | -42.562302 | 2026-09-15 00:25:00 | METOP-C | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| ee0bd8cb-81e8-3ddb-86ad-5eacdd23dacf | -5.4013 | -48.494999 | 2026-09-15 00:25:00 | METOP-C | ESPERANTINA | TOCANTINS | Brasil | 1707405 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 31331eab-1b7d-3761-b5dd-445c0c2ccf5c | -10.7507 | -44.806999 | 2026-09-15 00:25:00 | METOP-C | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 26dba760-095b-3d4d-8298-06f63826e210 | -12.8493 | -44.3843 | 2026-09-15 00:25:00 | METOP-C | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 0b7fd5e0-8046-36c9-a279-8e1e1d121dd8 | -9.2571 | -48.5312 | 2026-09-15 00:25:00 | METOP-C | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 64f48d10-50c1-3015-a872-c31f0864aaaa | -8.507 | -50.136501 | 2026-09-15 00:25:00 | METOP-C | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 38cc41c5-47b9-3e47-b41d-49375d39a0d0 | -4.67 | -42.095699 | 2026-09-15 00:25:00 | METOP-C | NOSSA SENHORA DE NAZARÉ | PIAUÍ | Brasil | 2206753 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 87b4d363-5ac3-3eee-8d25-7f8ee429d49c | -6.7214 | -48.101501 | 2026-09-15 00:25:00 | METOP-C | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| c86c1ada-6f88-39e3-9e51-29ccc0f2cf00 | -8.8064 | -50.487701 | 2026-09-15 00:25:00 | METOP-C | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aa0a816a-a0c2-3423-886f-433846df7eb1 | -7.9645 | -43.974998 | 2026-09-15 00:25:00 | METOP-C | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 778ab857-d0ad-308a-86bf-d56a013c534a | -5.0284 | -43.5914 | 2026-09-15 00:25:00 | METOP-C | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| fb766c2e-a87c-3357-bb80-d20adae1053f | -13.6292 | -47.876099 | 2026-09-15 00:25:00 | METOP-C | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 666d4670-4487-36ae-ace1-92491ddcbeb2 | -7.6114 | -47.2957 | 2026-09-15 00:25:00 | METOP-C | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 544b27de-cd87-33fd-b171-f58b4b77f070 | -10.7044 | -47.496899 | 2026-09-15 00:25:00 | METOP-C | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 52c3eb8d-0362-3aa4-855a-f6b54fef81bc | -10.672 | -54.159901 | 2026-09-15 00:25:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 26a2fee8-2333-3c47-86dc-169bcf7c970b | -5.5592 | -43.432701 | 2026-09-15 00:25:00 | METOP-C | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b6f34a25-0bd4-3dc7-9ff8-e510f4096ed2 | -10.8546 | -46.298199 | 2026-09-15 00:25:00 | METOP-C | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d874cbff-c59f-3854-866e-2f32c2274fee | -4.5152 | -54.960499 | 2026-09-15 00:25:00 | METOP-C | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 41865b77-7fa0-368e-9c23-a4e100015ec0 | -12.4755 | -41.3904 | 2026-09-15 00:25:00 | METOP-C | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| f01d4950-212b-3a4e-9588-42283874621c | -7.2941 | -46.748402 | 2026-09-15 00:25:00 | METOP-C | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8e086971-699b-3ccb-a848-e0732228a8c4 | -8.794 | -50.477402 | 2026-09-15 00:25:00 | METOP-C | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 869b227b-52b0-350d-b5b4-c843352abb2a | -8.0489 | -43.758598 | 2026-09-15 00:25:00 | METOP-C | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 004d01fe-ef2b-3c30-ba7e-37a9b68af82f | -11.1229 | -40.4785 | 2026-09-15 00:25:00 | METOP-C | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| e39dd6c9-ef83-38d1-8bbb-f1d6b3d95046 | -5.7398 | -43.276901 | 2026-09-15 00:25:00 | METOP-C | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 28d1bf8e-dab5-30c2-8e3c-aab86230c9ee | -15.2845 | -42.7901 | 2026-09-15 00:25:00 | METOP-C | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 2626ac13-5994-3e20-906f-768bce056477 | -7.4576 | -46.145901 | 2026-09-15 00:25:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| fb730f7a-a7a9-3b63-b5e8-d2fc1d9c2903 | -7.37 | -49.512299 | 2026-09-15 00:25:00 | METOP-C | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f9abb8c1-7969-33d9-9919-ce98555f0d71 | -17.471901 | -43.653198 | 2026-09-15 00:25:00 | METOP-C | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| cbdbcd7f-fb6d-3226-be3d-3ba6a4f2d5c3 | 0.2195 | -51.3624 | 2026-09-15 00:25:00 | METOP-C | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 1006b174-5bdc-372f-a2dc-2380292d84e1 | -14.678 | -42.843399 | 2026-09-15 00:25:00 | METOP-C | SEBASTIÃO LARANJEIRAS | BAHIA | Brasil | 2930006 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 32161f18-8959-32ce-b18a-fa8a2f0e8d8c | -7.1677 | -43.516998 | 2026-09-15 00:25:00 | METOP-C | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 53d9dfbc-a4c2-35b7-a1bf-4e757e8dc1e4 | -9.4167 | -50.092999 | 2026-09-15 00:25:00 | METOP-C | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5a9f868d-f2bf-3c2e-99d2-cc45edaa12ee | -13.6313 | -47.886101 | 2026-09-15 00:25:00 | METOP-C | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| a35c5c7c-2c14-3f53-9f9a-91ceee26a80e | -4.2665 | -46.52 | 2026-09-15 00:25:00 | METOP-C | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 763970bf-ec20-35dd-b313-f6bd04a66f2b | -8.4697 | -46.854698 | 2026-09-15 00:25:00 | METOP-C | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| cfa65122-75bd-3126-820f-affa686a8cef | -12.5593 | -47.114799 | 2026-09-15 00:25:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 49c1cadf-8ee2-3781-9014-1ca92ebfc949 | -5.4537 | -44.0476 | 2026-09-15 00:25:00 | METOP-C | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6c6e10aa-63d2-3976-a513-934f1c801eb5 | -2.8964 | -50.427101 | 2026-09-15 00:25:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4b4174d0-041d-3a42-a731-952a0959a0cb | -15.5871 | -48.791599 | 2026-09-15 00:25:00 | METOP-C | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| a2938923-d707-3a7a-b6b4-7166852a1301 | -3.9673 | -43.108601 | 2026-09-15 00:25:00 | METOP-C | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5186b3f8-b645-3030-a26b-feae93d231fb | -7.3722 | -49.522499 | 2026-09-15 00:25:00 | METOP-C | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1322eba7-d90b-3a31-b626-5535daa9a09a | -4.3551 | -47.775101 | 2026-09-15 00:25:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b8d647b5-a206-372f-95b3-2362c1433c98 | -6.3284 | -44.127899 | 2026-09-15 00:25:00 | METOP-C | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 88336abf-92c2-3af6-b3a8-b91feb86178f | -12.4791 | -41.405701 | 2026-09-15 00:25:00 | METOP-C | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 5d53c9ef-abf5-33de-86f2-408c631316c9 | -4.1888 | -48.681 | 2026-09-15 00:25:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dc040895-1b43-3eb1-bc12-150b7812f629 | -6.6953 | -58.6903 | 2026-09-15 00:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 58.1 |
| f2db2a03-e2b8-3ad8-ae43-34754b053e64 | -5.1256 | -55.9352 | 2026-09-15 00:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 66.5 |
| 7ef91731-c2fc-3b9b-a54b-5e0978fa920e | -1.7875 | -54.4725 | 2026-09-15 00:30:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 61.6 |
| f8cf899b-b6e1-3204-b2bc-68aadd5a776e | -2.6783 | -57.5893 | 2026-09-15 00:30:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 40.5 |
| da988217-d5fd-3aa4-a834-9291b3a43e50 | -4.6589 | -42.0726 | 2026-09-15 00:30:00 | GOES-19 | NOSSA SENHORA DE NAZARÉ | PIAUÍ | Brasil | 2206753 | 22 | 33 | nan | nan | nan | Caatinga | 78.9 |
| 2ca836b9-1615-33c7-b187-6f9f39a02752 | -8.0924 | -50.9642 | 2026-09-15 00:30:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 79.8 |
| e35da8b8-8147-39c7-a7f2-77661d9f41f9 | -13.2235 | -51.6531 | 2026-09-15 00:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 96.0 |
| 30e68381-a5c9-3392-b6ab-acf662931109 | -16.1487 | -49.496 | 2026-09-15 00:30:00 | GOES-19 | ITAUÇU | GOIÁS | Brasil | 5211404 | 52 | 33 | nan | nan | nan | Cerrado | 69.9 |
| ca463fe8-c8c7-3732-96d4-93a7fdc03cc5 | -2.9209 | -50.4208 | 2026-09-15 00:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 63.9 |
| ee158fb6-446b-305b-926a-e8fb04be2093 | -4.6776 | -42.0713 | 2026-09-15 00:30:00 | GOES-19 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 93.9 |
| bb8bb355-390c-3b2c-a682-b636700bc196 | -6.7195 | -48.1201 | 2026-09-15 00:30:00 | GOES-19 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Amazônia | 86.3 |
| 9c32d1c3-897a-30ce-ad05-f67a21247f66 | -6.9612 | -44.5316 | 2026-09-15 00:30:00 | GOES-19 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 63.9 |
| ae4915ae-cdf1-3aa1-8bad-27babd3a24b5 | -2.9025 | -50.4214 | 2026-09-15 00:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 80.1 |
| 85dcd1b2-e638-31a4-8601-9913e7731ef4 | -3.1816 | -61.1235 | 2026-09-15 00:30:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 579be2de-3e85-398d-b315-cd5b4a61f1ac | -11.9033 | -43.8112 | 2026-09-15 00:30:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 84.0 |
| 2cf7c6cc-784d-3c85-80dc-3696d03ecd59 | -9.5343 | -40.3282 | 2026-09-15 00:30:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 283.8 |
| 9fbc35fb-2256-3c58-bba5-bc35e9c8d74f | -6.1109 | -57.684 | 2026-09-15 00:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 31b1f90e-34ab-3161-a8dd-9bc348a25c23 | -8.5126 | -50.1481 | 2026-09-15 00:30:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 46.9 |
| 55291045-e676-305e-95b2-c4e3feead697 | -15.2827 | -42.783 | 2026-09-15 00:30:00 | GOES-19 | SANTO ANTÔNIO DO RETIRO | MINAS GERAIS | Brasil | 3160454 | 31 | 33 | nan | nan | nan | Cerrado | 69.1 |
| 7243cfec-da04-38ea-b704-65cab5c39f81 | -6.0925 | -57.6847 | 2026-09-15 00:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 42.6 |
| abe1b11d-7a28-3731-883f-fc656ddc8703 | -6.1108 | -57.7035 | 2026-09-15 00:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 46.6 |
| 57b6a5b3-4650-3e29-bc84-64196cfd10f8 | -1.7875 | -54.4925 | 2026-09-15 00:30:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 98.5 |
| 32e6c7a6-be9f-3c57-b0b1-ac37e604327e | -2.6784 | -57.5698 | 2026-09-15 00:30:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 38.9 |
| 38433306-389a-31f8-ad60-62c6b800cdaa | -9.5347 | -40.3033 | 2026-09-15 00:30:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 79.8 |
| 301be0ee-168a-3439-abc5-581b44bf02bf | -3.382 | -61.3279 | 2026-09-15 00:30:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 57.6 |
| 102dff6e-e595-3ad7-bc2d-6f079050a23d | -5.4297 | -43.9869 | 2026-09-15 00:30:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 124.6 |
| 4bfecdb7-6d32-327b-830c-e7d10bb6e8ff | -4.6774 | -42.0951 | 2026-09-15 00:30:00 | GOES-19 | NOSSA SENHORA DE NAZARÉ | PIAUÍ | Brasil | 2206753 | 22 | 33 | nan | nan | nan | Caatinga | 144.6 |
| 2e3dd3fe-8a9e-37ea-870a-4004c5a44924 | -11.884 | -43.8142 | 2026-09-15 00:30:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 111.1 |
| 841fdd39-ed69-3c6d-9ca1-042c370e1b07 | -4.6587 | -42.0964 | 2026-09-15 00:30:00 | GOES-19 | NOSSA SENHORA DE NAZARÉ | PIAUÍ | Brasil | 2206753 | 22 | 33 | nan | nan | nan | Caatinga | 125.2 |
| 1b12795f-ee22-3bcf-8065-b76eac6d3224 | -13.2232 | -51.6744 | 2026-09-15 00:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 73.1 |
| 7971e66e-f23d-3026-80f8-24cad9ec716a | -16.1286 | -49.5215 | 2026-09-15 00:30:00 | GOES-19 | ITAUÇU | GOIÁS | Brasil | 5211404 | 52 | 33 | nan | nan | nan | Cerrado | 66.2 |


[Clique aqui para ver as próximas entradas](README13.md)
