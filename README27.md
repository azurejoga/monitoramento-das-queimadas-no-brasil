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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7a2132c0-5372-3d2e-9233-29f436b92a0a | -10.52581 | -43.41515 | 2025-10-19 04:12:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| d883722f-24b0-3f40-815d-b95ffd7014f8 | -11.61013 | -48.53628 | 2025-10-19 04:12:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5f678269-af85-319a-b364-0ccbc0d280b5 | -11.34544 | -44.18052 | 2025-10-19 04:12:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8b51fb9a-ee2a-3d47-bbae-371c9b3cccfc | -12.38096 | -43.17681 | 2025-10-19 04:12:00 | NPP-375D | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 3c640b94-271d-32e1-ae40-766e001bdd3d | -13.01237 | -46.95617 | 2025-10-19 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3adb2db0-2863-360d-9629-c024782cec25 | -13.9148 | -43.18477 | 2025-10-19 04:12:00 | NPP-375D | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 2ce013f6-5a7c-3579-bdd6-d2589d7b0001 | -9.75731 | -43.95475 | 2025-10-19 04:12:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 396941bc-a424-366b-bffb-5ec347313056 | -11.88167 | -45.43167 | 2025-10-19 04:12:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8a55fa81-45e4-3b71-a5c8-a6288b2df31a | -13.17756 | -46.44184 | 2025-10-19 04:12:00 | NPP-375D | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 12895a59-da46-395e-90ea-500dac582fe5 | -11.81015 | -44.41629 | 2025-10-19 04:12:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 97a7c432-2725-3dcc-974e-f7310b154729 | -8.43577 | -44.14962 | 2025-10-19 04:12:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 54102131-7597-380d-a418-92b4592ff52f | -8.58075 | -44.58474 | 2025-10-19 04:12:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8ba5f36c-25a7-3bea-88f9-c7968b7b76b5 | -13.8871 | -45.47274 | 2025-10-19 04:12:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 52916ce9-6a9d-3d36-9c70-608a2d5fbd44 | -10.88673 | -46.07815 | 2025-10-19 04:12:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| bbfbcca1-df31-35d2-a6a1-f039b0d86fc1 | -10.55875 | -45.15754 | 2025-10-19 04:12:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 7630ee3b-4502-342a-9777-2c656dba8378 | -9.13111 | -43.24777 | 2025-10-19 04:12:00 | NPP-375D | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 37404f56-d2b6-3b2d-943a-2c7b04af0d8c | -11.6389 | -44.09337 | 2025-10-19 04:12:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0e21c5b8-a155-3525-923d-c8b4d09b7f07 | -8.44714 | -44.16702 | 2025-10-19 04:12:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 7cfbdf37-1698-3396-8ecd-f72c508a7094 | -7.80525 | -46.79313 | 2025-10-19 04:12:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0cdb898b-eecb-32b5-bc00-34153dd12010 | -7.32466 | -47.25606 | 2025-10-19 04:12:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 96cced6c-d6e4-34ce-9064-8387d7744724 | -13.02068 | -46.95105 | 2025-10-19 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b41a3642-b3e6-3099-9fcd-da867dc474ca | -12.33789 | -41.38735 | 2025-10-19 04:12:00 | NPP-375D | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 0a6e71c2-c86a-3425-a664-e6338fdc7bcc | -10.53676 | -44.50661 | 2025-10-19 04:12:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 76c482f1-a40f-331e-9c28-6b9d578f8bfb | -10.22282 | -44.05664 | 2025-10-19 04:12:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cf265f75-7082-3606-b86d-457edf179aef | -13.88923 | -43.45425 | 2025-10-19 04:12:00 | NPP-375D | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c35a54a1-65c9-3605-98ba-b2f4b7ac2302 | -12.15699 | -45.0624 | 2025-10-19 04:12:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 749db143-6b6a-39a3-a059-957c03554112 | -8.12802 | -47.66619 | 2025-10-19 04:12:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4a4b9106-a0f6-343a-af66-cc1bcdf2d853 | -12.44946 | -44.86284 | 2025-10-19 04:12:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 536f9af6-8f94-3a00-be97-a574a3b3bafb | -12.98994 | -47.2826 | 2025-10-19 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| dca60804-268a-376a-86f1-660c97f58223 | -12.45609 | -45.43275 | 2025-10-19 04:12:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 27.9 |
| cc7acbad-4c73-3efe-ba49-ca94648b0ec9 | -10.88604 | -46.09476 | 2025-10-19 04:12:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 4ca3071b-244d-38b6-b0c2-174ddf1cb438 | -9.22064 | -46.05431 | 2025-10-19 04:12:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 182bf69c-3b8b-3984-9bba-9a5d4c5b178e | -12.2322 | -49.39182 | 2025-10-19 04:12:00 | NPP-375D | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| faf81428-990e-371e-9f5f-45cd8fd83ebc | -11.14004 | -44.93988 | 2025-10-19 04:12:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 884d195e-3e31-3310-8ed6-33d8ba7f46ae | -11.6508 | -44.08413 | 2025-10-19 04:12:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c8539929-2e50-3d80-8dea-f03e56934d23 | -8.25536 | -43.32782 | 2025-10-19 04:12:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 5e346c21-64a7-3db2-9cc9-271f4aded205 | -10.88138 | -47.45014 | 2025-10-19 04:12:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 89495bff-f995-3847-9884-5566fa281cfa | -8.21726 | -43.96688 | 2025-10-19 04:12:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 48121884-26ee-3da3-93a8-c75055584627 | -13.62455 | -44.10731 | 2025-10-19 04:12:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 461cc6e3-31fa-3c0d-b998-d68f9dd2f443 | -10.22622 | -44.0572 | 2025-10-19 04:12:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8b170e80-5d99-39c5-bc6e-51184f053130 | -8.46033 | -41.39928 | 2025-10-19 04:12:00 | NPP-375D | QUEIMADA NOVA | PIAUÍ | Brasil | 2208650 | 22 | 33 | nan | nan | nan | Caatinga | 0.4 |
| a62cb0f3-412a-3370-a38d-db8e342e6973 | -10.12793 | -44.53001 | 2025-10-19 04:12:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f3ce80d8-becd-3c7b-a642-737483d3eab5 | -10.1232 | -44.53719 | 2025-10-19 04:12:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8fdef2f1-9711-3c75-921a-f9d2947c4455 | -9.95108 | -44.00922 | 2025-10-19 04:12:00 | NPP-375D | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fc13cfaa-8c2a-3612-8677-e8d71e501369 | -13.91424 | -43.18833 | 2025-10-19 04:12:00 | NPP-375D | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 53157091-8657-3305-bb36-18b9fe91af43 | -11.34484 | -44.18419 | 2025-10-19 04:12:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 15752728-a65c-3a32-a483-69af899f96bb | -7.87079 | -45.71243 | 2025-10-19 04:12:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e8725b80-bcdd-3953-a66c-28b0122956b5 | -11.62835 | -44.07288 | 2025-10-19 04:12:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 010c616c-4ef4-3310-9a29-aeeca24d3dcc | -10.8868 | -46.09035 | 2025-10-19 04:12:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 11.8 |
| d8e6209c-4f9b-364d-949d-368959ec60e1 | -12.49727 | -45.42351 | 2025-10-19 04:12:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e9059fdc-2290-315e-bbf8-9dcf2df88322 | -10.5401 | -44.04066 | 2025-10-19 04:12:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 82090353-1f65-3d8d-8e64-300948d3d56f | -11.35173 | -44.29132 | 2025-10-19 04:12:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6f1450ef-624e-3b0c-8d54-3f279ccffd71 | -8.43109 | -49.59248 | 2025-10-19 04:12:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 63cde1ef-f411-3fb5-90a1-28d118b03325 | -13.88018 | -45.47152 | 2025-10-19 04:12:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 097b3494-6a02-32f5-8381-91268eec4e78 | -12.15007 | -45.06117 | 2025-10-19 04:12:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| a15dc5bf-5b11-3a60-a8e8-27457a5f69a0 | -9.53095 | -47.90794 | 2025-10-19 04:12:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b4db5906-4191-3c09-8c30-f59c3a10b28f | -13.02057 | -46.95346 | 2025-10-19 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 27289dd7-3f52-368a-9347-dcac6989b51c | -10.49589 | -43.36629 | 2025-10-19 04:12:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 436e9617-1061-3c9f-b30c-d3f701ca2642 | -11.3438 | -44.23312 | 2025-10-19 04:12:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 17eeafd8-526d-3483-b0b5-62a430557890 | -10.64229 | -48.80819 | 2025-10-19 04:12:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d4597bc5-80db-3d7f-bac7-dba2d5bfc855 | -13.71521 | -40.98452 | 2025-10-19 04:12:00 | NPP-375D | BARRA DA ESTIVA | BAHIA | Brasil | 2902807 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 8a5ec2fc-48ba-3aa6-a705-d8936ceec26b | -11.63231 | -44.0698 | 2025-10-19 04:12:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2b5da569-444b-398a-ad41-666a8bebac0f | -12.95368 | -47.29835 | 2025-10-19 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e24de3c9-3875-39c0-898e-73b9710fcd39 | -12.50999 | -40.82228 | 2025-10-19 04:12:00 | NPP-375D | IBIQUERA | BAHIA | Brasil | 2912608 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 3c2fe842-c648-3ab8-8b03-8ddbb3b31ab2 | -12.01711 | -46.48496 | 2025-10-19 04:12:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d7dcb8d4-7312-3123-b2f1-e17362e228f7 | -10.85483 | -43.93076 | 2025-10-19 04:12:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f57d04f4-f30c-3167-8db5-83d6e27e22e5 | -14.28236 | -42.32777 | 2025-10-19 04:12:00 | NPP-375D | IBIASSUCÊ | BAHIA | Brasil | 2912004 | 29 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 52c223ca-2b54-35da-80ae-99979906a5af | -10.88897 | -46.09974 | 2025-10-19 04:12:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| c4cb4068-db0b-3c95-86d8-69606e7d816e | -13.90167 | -45.53541 | 2025-10-19 04:12:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9f02f399-0776-3044-a435-fe36b33a8abf | -11.61324 | -44.05913 | 2025-10-19 04:12:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 90f41648-43fe-38a8-a8c6-ec9bafa936cf | -12.14928 | -45.05811 | 2025-10-19 04:12:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 59e1479a-b5ca-35bb-8d17-10c9ef2b30a5 | -10.85582 | -43.94594 | 2025-10-19 04:12:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 896400db-fe0a-3912-b474-63b0aeab19a5 | -10.70101 | -45.3195 | 2025-10-19 04:12:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 737d27a9-24b2-331d-8978-ff8e6935ab13 | -10.88832 | -46.08161 | 2025-10-19 04:12:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 345eaa49-65db-3b5a-914e-d0e7c80c912a | -10.52437 | -43.36003 | 2025-10-19 04:12:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| f1702577-df3c-381b-9f93-7b7232bb1a89 | -7.64737 | -46.67634 | 2025-10-19 04:12:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ddfbc4cd-cdff-3839-986d-c38f7a589f4c | -11.64414 | -47.84935 | 2025-10-19 04:12:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 46abb2e9-b7d7-37aa-8cf9-620adfc0c158 | -12.15289 | -45.06559 | 2025-10-19 04:12:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d340799f-0847-34fe-be7d-85ff047a6e6b | -13.01979 | -46.9579 | 2025-10-19 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8f257ca6-38e9-3a84-bfad-fbb17313675c | -11.65021 | -44.08778 | 2025-10-19 04:12:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c5f73515-f237-37b3-b8f1-3dd3e63c36cd | -9.89215 | -47.65263 | 2025-10-19 04:12:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d69d9629-76ab-3cf8-a5b1-195415b5c8f3 | -8.437 | -44.14216 | 2025-10-19 04:12:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 89dfa892-68d1-3be1-993d-88f91a9cfdcb | -11.13488 | -45.0795 | 2025-10-19 04:12:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4fc9be49-6c79-30f9-b113-d96c19edea15 | -13.50485 | -43.29976 | 2025-10-19 04:12:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 3.0 |
| e81b9559-f825-3fab-ac0d-e43bdd6cc5ed | -8.83372 | -44.21362 | 2025-10-19 04:12:00 | NPP-375D | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a6814c4b-6dbd-3aa6-954a-72ab49e9719e | -10.68523 | -44.54293 | 2025-10-19 04:12:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9e6e5572-1979-30eb-a597-a1ed0bbec67c | -10.68867 | -44.54352 | 2025-10-19 04:12:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b62a2519-36fe-3251-9eea-596be0e3e159 | -7.60003 | -45.85074 | 2025-10-19 04:12:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ad628c78-105c-34d1-8c43-0182a74bae9f | -9.7521 | -43.96521 | 2025-10-19 04:12:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fb0c7389-02ed-3f44-bfb7-f8f2df4765e2 | -8.21099 | -43.962 | 2025-10-19 04:12:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b54961a9-6df1-3ca7-bd78-7a87e5d07486 | -11.64832 | -47.31427 | 2025-10-19 04:12:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 32137920-2fc2-3428-9a00-885b0ed4be7b | -11.79 | -49.31956 | 2025-10-19 04:12:00 | NPP-375D | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2bc6456c-40cd-3600-9127-5a0303a75594 | -13.60441 | -43.11559 | 2025-10-19 04:12:00 | NPP-375D | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 2411b5bd-fb7b-3101-97e7-e4e1b54741c8 | -10.68585 | -44.53915 | 2025-10-19 04:12:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9b9f7e90-99b2-36fa-8880-f3a20496a386 | -9.25286 | -44.34332 | 2025-10-19 04:12:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ecb210d3-46a4-3dc9-a562-7929bcccc6d8 | -9.62369 | -49.13457 | 2025-10-19 04:12:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9fd84700-a68f-3e8c-91b8-b73ae3108b78 | -10.77913 | -40.31087 | 2025-10-19 04:12:00 | NPP-375D | PINDOBAÇU | BAHIA | Brasil | 2924603 | 29 | 33 | nan | nan | nan | Caatinga | 2.7 |
| ce0b8f1f-9496-3be2-a701-8fac3f801a36 | -7.71308 | -46.60313 | 2025-10-19 04:12:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 66548547-2546-3a20-a194-9d1418c69027 | -7.59624 | -45.85007 | 2025-10-19 04:12:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 362dcbb8-9620-3e7d-9b5f-8341eff27435 | -11.4339 | -44.93552 | 2025-10-19 04:12:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |


[Clique aqui para ver as próximas entradas](README28.md)
