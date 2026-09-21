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

## Dados Diários - Página 111

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 82783174-d748-348c-9d28-73eab900bf95 | -11.04946 | -54.15031 | 2026-09-21 07:03:00 | AQUA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| d8e6a309-103c-379c-acdd-120ff0b0723d | -14.07228 | -52.12657 | 2026-09-21 07:03:00 | AQUA_M-M | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 5c6eedf5-8103-3356-ab6b-72adc0ee7231 | -17.60336 | -52.3453 | 2026-09-21 07:05:00 | AQUA_M-M | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 1069a6d0-c66a-32cd-aec4-1fb4b325d1b9 | -10.8011 | -50.7604 | 2026-09-21 07:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 104.2 |
| 9d2b9f0a-a1b6-353d-8420-5d834cc1e79e | -10.8008 | -50.7817 | 2026-09-21 07:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 51.9 |
| 2f117ae8-82b5-363e-8b2c-b4aeb0656fb8 | -10.82 | -50.7584 | 2026-09-21 07:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 48.4 |
| 560a134f-6971-3045-8c54-9beaf6fa6ee9 | -17.604 | -52.3392 | 2026-09-21 07:10:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 67.5 |
| 1459529e-f7c3-3d25-8331-6e781ea4d637 | -10.8008 | -50.7817 | 2026-09-21 07:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 81.1 |
| d82de5b7-e2cf-3295-9d06-735f7e54125f | -10.8011 | -50.7604 | 2026-09-21 07:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 185.1 |
| c6f320b2-6a7d-35e5-822c-2e811705d9ca | -10.82 | -50.7584 | 2026-09-21 07:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 191.0 |
| 6ab28ca8-335d-38df-8156-64ff81485130 | -10.8197 | -50.7797 | 2026-09-21 07:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 99.1 |
| 887057e8-f9f5-319d-bf36-e83674bf6c3f | -10.8008 | -50.7817 | 2026-09-21 07:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 91.2 |
| 44fd8a46-2a08-39c5-b8c3-42a7ddfa6646 | -12.8246 | -54.0442 | 2026-09-21 07:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 74.7 |
| 79099d29-5024-3ee3-b6e8-ce9f250e8e82 | -10.8011 | -50.7604 | 2026-09-21 07:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 223.1 |
| 2ec384c3-d696-3056-9d93-8361e531c86a | -10.82 | -50.7584 | 2026-09-21 07:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 162.3 |
| 11c8884f-72f7-3ac8-8d78-a84803ccef64 | -10.8197 | -50.7797 | 2026-09-21 07:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 97.1 |
| 21cc3f33-f891-315a-ad86-713dad49b02f | -12.8437 | -54.0422 | 2026-09-21 07:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 50.1 |
| 2571f1fd-649d-3a0e-be82-84da62e49748 | -10.8008 | -50.7817 | 2026-09-21 07:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 70.5 |
| 91960ed5-8cb6-334d-8076-044ce0c1ea74 | -10.82 | -50.7584 | 2026-09-21 07:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 130.6 |
| f626025b-71f1-39e0-8c69-7785efbbb81c | -10.8011 | -50.7604 | 2026-09-21 07:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 157.9 |
| 9c360b68-bf9d-3ae3-b6f3-99ec013a6d78 | -10.8197 | -50.7797 | 2026-09-21 07:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 75.8 |
| fa3f657e-d22e-3461-ae14-71cbabb8e1a3 | -10.82 | -50.7584 | 2026-09-21 07:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 197.8 |
| ae3fc42f-fa48-3c2a-b18e-132b552d0149 | -10.8197 | -50.7797 | 2026-09-21 07:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 110.3 |
| 832e3543-172e-3804-8b75-65eb6190fea0 | -10.8011 | -50.7604 | 2026-09-21 07:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 79.5 |
| aba26d5d-b6b3-36ad-8492-ccc469694427 | -10.8197 | -50.7797 | 2026-09-21 08:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 63.7 |
| e69c9378-9c75-351d-b5d4-f50919a3f43b | -10.82 | -50.7584 | 2026-09-21 08:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 132.3 |
| 94dbeb28-3c4d-35c3-b5cd-61e4ae92cd65 | -10.8011 | -50.7604 | 2026-09-21 08:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 79.4 |
| f0898f87-6396-366e-8998-a073b4e407ed | -9.55221 | -66.01847 | 2026-09-21 08:41:00 | AQUA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 34.9 |
| 7099d56a-48b2-3a38-89b5-24b8b36d48fa | -9.55461 | -66.02274 | 2026-09-21 08:41:00 | AQUA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 35.1 |
| ab86584c-e8cb-337e-bc50-cb7768da6858 | -6.7281 | -63.1303 | 2026-09-21 09:10:00 | GOES-19 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 38.3 |
| ac9651ee-db98-33f7-a078-8acfc07c0e3f | -7.428 | -44.7867 | 2026-09-21 10:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 84.6 |
| a4be31db-21a1-3ef9-a55b-2449437441ef | -7.4092 | -44.7885 | 2026-09-21 10:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 92.0 |
| a5698af8-9010-3da1-9e77-44ee3ddb2cdb | -7.428 | -44.7867 | 2026-09-21 10:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 251.2 |
| f64a0f91-f3a0-3aac-bd3e-89bd40ea8036 | -7.4278 | -44.8096 | 2026-09-21 10:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 85.6 |
| 9aef8de8-ffc6-3e42-b295-a458c30a18f5 | -7.4283 | -44.7639 | 2026-09-21 10:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 94.3 |
| 0fdb67e3-ab33-3cd5-a534-010bfda8adfe | -7.4092 | -44.7885 | 2026-09-21 10:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 206.0 |
| 0f0a7fe7-af3c-3c53-ba3b-49b74cee080e | -7.428 | -44.7867 | 2026-09-21 11:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 179.2 |
| a96de67f-96bb-30e6-acf3-3795e9f19ada | -10.3917 | -48.8915 | 2026-09-21 11:00:00 | GOES-19 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 110.5 |
| f86a62c5-7d67-3e74-87d4-16a2738f8956 | -7.4095 | -44.7656 | 2026-09-21 11:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 85.4 |
| dedd6aa2-3e8a-3916-ab40-5b8055997c86 | -7.4092 | -44.7885 | 2026-09-21 11:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 331.2 |
| 8a8372a2-cf02-37b2-9210-ffbc72ffebc0 | -5.3361 | -37.31118 | 2026-09-21 11:04:00 | TERRA_M-M | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 5.5 |
| ef37c879-d58c-3bbe-a0d6-136c0489f0bb | -6.39826 | -35.27062 | 2026-09-21 11:04:00 | TERRA_M-M | PEDRO VELHO | RIO GRANDE DO NORTE | Brasil | 2409803 | 24 | 33 | nan | nan | nan | Mata Atlântica | 10.0 |
| dacfa45b-91e0-3ef3-93ac-d76caea5a3cc | -5.75052 | -43.70962 | 2026-09-21 11:04:00 | TERRA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 8911ddcb-3dfb-3142-86e1-ca92974ff1d1 | -4.45907 | -37.82489 | 2026-09-21 11:04:00 | TERRA_M-M | FORTIM | CEARÁ | Brasil | 2304459 | 23 | 33 | nan | nan | nan | Caatinga | 11.0 |
| 8f2e81f2-e930-337f-9efc-7442389b05f4 | -6.40769 | -35.27183 | 2026-09-21 11:04:00 | TERRA_M-M | PEDRO VELHO | RIO GRANDE DO NORTE | Brasil | 2409803 | 24 | 33 | nan | nan | nan | Mata Atlântica | 13.0 |
| 45fc667c-192b-3dba-ab61-0e856edc69d9 | -5.75075 | -43.71565 | 2026-09-21 11:04:00 | TERRA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 484f285e-17af-3aa7-842c-09fafd06ea37 | -7.41825 | -44.79721 | 2026-09-21 11:06:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 273.7 |
| 12e130ad-b06d-3cdc-9265-89b536d1d70e | -7.42338 | -44.79179 | 2026-09-21 11:06:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 107.5 |
| dd8f6712-6011-35cc-8ac1-c69323ef447c | -8.51566 | -39.37917 | 2026-09-21 11:06:00 | TERRA_M-M | CABROBÓ | PERNAMBUCO | Brasil | 2603009 | 26 | 33 | nan | nan | nan | Caatinga | 14.3 |
| ee407a2b-448a-3598-abe1-3945e68673a1 | -9.83105 | -48.44115 | 2026-09-21 11:06:00 | TERRA_M-M | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 39.5 |
| d11a56ff-475d-35e7-928f-b91cda2fbb15 | -9.82851 | -48.43292 | 2026-09-21 11:06:00 | TERRA_M-M | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 40.3 |
| 1b983bc0-5221-3581-a972-20feea2e5788 | -6.92017 | -43.72527 | 2026-09-21 11:06:00 | TERRA_M-M | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 19.7 |
| d55c27e5-be00-310c-96f9-902b7c8a6afe | -8.08064 | -44.35852 | 2026-09-21 11:06:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 37.0 |
| 9aa96140-8445-38ea-8cf2-338d9bb1dc4f | -7.43521 | -44.77721 | 2026-09-21 11:06:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 45.6 |
| 9e8dd1ea-c5a5-3cc8-8026-623bccb9e3d4 | -8.50875 | -39.42582 | 2026-09-21 11:06:00 | TERRA_M-M | CABROBÓ | PERNAMBUCO | Brasil | 2603009 | 26 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 04c64aed-37ed-3cff-9e12-c58d62e772a9 | -7.41331 | -44.76807 | 2026-09-21 11:06:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 77.6 |
| 19e4781d-36e5-3ce8-9f2e-634a7ac167a7 | -9.92474 | -45.69168 | 2026-09-21 11:06:00 | TERRA_M-M | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 22.9 |
| 03e64367-9cf2-3927-9bc4-c1111e4156e2 | -7.88554 | -44.83572 | 2026-09-21 11:06:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 23.1 |
| e339d132-1a31-30a9-94e3-c2805a9d6610 | -8.76406 | -44.27267 | 2026-09-21 11:06:00 | TERRA_M-M | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 60.1 |
| ea20284c-d14c-3b20-9196-7844c6e38ee3 | -9.46175 | -45.40887 | 2026-09-21 11:06:00 | TERRA_M-M | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 124.9 |
| 9a24f2ce-b427-3d8d-b328-958118f0ce9c | -14.00341 | -42.13664 | 2026-09-21 11:06:00 | TERRA_M-M | LAGOA REAL | BAHIA | Brasil | 2918753 | 29 | 33 | nan | nan | nan | Caatinga | 7.2 |
| 9b6837e2-a2b6-37f3-998f-f5a9522597eb | -6.91542 | -43.73656 | 2026-09-21 11:06:00 | TERRA_M-M | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 22.8 |
| 6759ae2c-12cd-39db-822f-66fcb252944d | -13.33011 | -41.64192 | 2026-09-21 11:06:00 | TERRA_M-M | ABAÍRA | BAHIA | Brasil | 2900108 | 29 | 33 | nan | nan | nan | Caatinga | 7.9 |
| 1033ea55-c71f-318d-bf6e-1e8a521a7a41 | -7.56452 | -42.64509 | 2026-09-21 11:06:00 | TERRA_M-M | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 16.4 |
| 478f4b5e-f215-3d95-8ee2-b23696a972ac | -7.42179 | -44.7753 | 2026-09-21 11:06:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 163.0 |
| edc489b6-f7a5-36f0-bcb9-326529653c61 | -7.42672 | -44.76999 | 2026-09-21 11:06:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 62.5 |
| 922e686a-6ffd-3eb0-81ff-a43749e25e12 | -6.91827 | -43.71793 | 2026-09-21 11:06:00 | TERRA_M-M | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 20.1 |
| c683edf9-efde-3f4e-8dfa-8e3cf3e6942c | -11.2908 | -38.4972 | 2026-09-21 11:06:00 | TERRA_M-M | NOVA SOURE | BAHIA | Brasil | 2922904 | 29 | 33 | nan | nan | nan | Caatinga | 4.2 |
| f508f174-9b93-36d3-a02e-2ddf15a07de5 | -8.77661 | -44.27461 | 2026-09-21 11:06:00 | TERRA_M-M | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 20.3 |
| 9f790106-9f26-30a8-a42c-e08e5109d733 | -8.53942 | -36.6316 | 2026-09-21 11:06:00 | TERRA_M-M | PESQUEIRA | PERNAMBUCO | Brasil | 2610905 | 26 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 1fb87f8b-4b37-3adc-ac1d-60de57daa352 | -8.76106 | -44.29187 | 2026-09-21 11:06:00 | TERRA_M-M | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 22.0 |
| 3145f02b-ad1e-3288-b55b-3ec054a86787 | -8.42227 | -45.873 | 2026-09-21 11:06:00 | TERRA_M-M | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 60.0 |
| 1d5bc433-094b-3758-b1bf-d81de8265f0d | -7.03072 | -42.07248 | 2026-09-21 11:06:00 | TERRA_M-M | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 14.0 |
| 164fc705-291c-3471-a1b3-f757c5a4ecde | -6.55306 | -42.56106 | 2026-09-21 11:06:00 | TERRA_M-M | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | 11.4 |
| 718aaaad-2208-3c4f-ae5c-5d42e3df1850 | -8.73407 | -36.82158 | 2026-09-21 11:06:00 | TERRA_M-M | PEDRA | PERNAMBUCO | Brasil | 2610806 | 26 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 6e83fd83-f309-3405-9d29-a36eb86fe09a | -8.73279 | -36.83078 | 2026-09-21 11:06:00 | TERRA_M-M | PEDRA | PERNAMBUCO | Brasil | 2610806 | 26 | 33 | nan | nan | nan | Caatinga | 8.8 |
| 35ccc1f9-d021-36ed-abba-5febc60726f4 | -7.02863 | -42.08611 | 2026-09-21 11:06:00 | TERRA_M-M | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 11.6 |
| ae1f7936-5e20-3479-b2c9-36195d8cbf37 | -7.56387 | -42.65097 | 2026-09-21 11:06:00 | TERRA_M-M | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 32.3 |
| 15274586-a21b-33b9-ac67-df8fdcb06d69 | -11.29207 | -38.48828 | 2026-09-21 11:06:00 | TERRA_M-M | NOVA SOURE | BAHIA | Brasil | 2922904 | 29 | 33 | nan | nan | nan | Caatinga | 17.8 |
| bab79167-a547-3350-8897-af0b12f73281 | -8.76536 | -44.27877 | 2026-09-21 11:06:00 | TERRA_M-M | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 53.7 |
| 5025b478-8e2b-3a06-ade7-14de76028ef8 | -15.45345 | -40.33536 | 2026-09-21 11:08:00 | TERRA_M-M | MACARANI | BAHIA | Brasil | 2919702 | 29 | 33 | nan | nan | nan | Mata Atlântica | 26.4 |
| 03734336-01a9-317b-bdfe-68dab81f8e50 | -19.73245 | -41.54783 | 2026-09-21 11:08:00 | TERRA_M-M | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| e030ca7c-f9e0-33c0-b7f6-d45d58b14468 | -14.80877 | -40.95124 | 2026-09-21 11:08:00 | TERRA_M-M | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 8.2 |
| 4e97cb46-a250-37c0-be4d-87f483b298a8 | -15.45209 | -40.34467 | 2026-09-21 11:08:00 | TERRA_M-M | MACARANI | BAHIA | Brasil | 2919702 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| e0f38bd9-8efa-37fb-9d86-42954ffd977d | -15.45116 | -48.45144 | 2026-09-21 11:08:00 | TERRA_M-M | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 31.5 |
| 821a4a32-b444-3a49-a4c1-c0becd98742e | -19.66242 | -44.69762 | 2026-09-21 11:08:00 | TERRA_M-M | ONÇA DE PITANGUI | MINAS GERAIS | Brasil | 3145802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.5 |
| 0a640c66-2c7b-3ad2-918e-56267d24f9ed | -15.45451 | -48.44661 | 2026-09-21 11:08:00 | TERRA_M-M | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 29.1 |
| 1079dd5e-a015-3656-9f16-ad0b2fe9f2ac | -14.8102 | -40.94169 | 2026-09-21 11:08:00 | TERRA_M-M | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| c141b827-145b-3513-ae36-b55dd4ce94be | -19.43904 | -40.71587 | 2026-09-21 11:08:00 | TERRA_M-M | COLATINA | ESPÍRITO SANTO | Brasil | 3201506 | 32 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| a26aaee6-96a4-33c6-b3fc-37e46ceb6e38 | -7.4092 | -44.7885 | 2026-09-21 11:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 125.0 |
| 3a67b662-9970-36b2-ab54-2cb3e118035f | -7.428 | -44.7867 | 2026-09-21 11:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 118.7 |
| a0d932ab-5992-3a53-9753-3a5d7ed18fe5 | -10.3917 | -48.8915 | 2026-09-21 11:10:00 | GOES-19 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 66a29a39-35e4-3997-a7d4-986a30cf5ab7 | -7.41 | -44.78 | 2026-09-21 11:15:00 | MSG-03 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 9861c8e6-b0d3-37fc-abe2-15ffaaa3af68 | -7.4092 | -44.7885 | 2026-09-21 11:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 105.5 |
| 255c473e-4550-3ee0-9a3f-407439f5caf6 | -7.428 | -44.7867 | 2026-09-21 11:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 91.1 |
| df0755e4-9b51-3d71-9a49-f4bde13e9ae6 | -10.43 | -50.2449 | 2026-09-21 11:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 71.8 |
| 82b7b630-35e8-34e9-b49c-dd8803d20046 | -10.8011 | -50.7604 | 2026-09-21 11:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 77.2 |
| 3e0a8abe-eb0a-34ac-bda8-a6d580170e38 | -7.5661 | -42.656 | 2026-09-21 11:20:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 85.9 |
| 80b925ab-6ad2-383f-b777-4a0c0cfad40b | -11.8495 | -46.833 | 2026-09-21 11:20:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 76.9 |
| dc18070a-3cb0-3cbd-bc8e-1d5cc0e50efe | -10.3917 | -48.8915 | 2026-09-21 11:20:00 | GOES-19 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 67.4 |


[Clique aqui para ver as próximas entradas](README112.md)
