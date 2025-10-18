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

## Dados Diários - Página 94

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dd159bf2-c8c3-33d7-aa0d-79bc890c0612 | -6.0489 | -41.9198 | 2025-10-18 14:00:00 | GOES-19 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 94.3 |
| 68979d0f-640c-3cd1-8ef7-4dad9c6d8b77 | -14.428 | -47.8851 | 2025-10-18 14:00:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 79.6 |
| d2104705-0d31-3aff-8152-e9bdc9ca9bcc | -11.379 | -45.285 | 2025-10-18 14:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 130.3 |
| 73f0bff5-0c51-34d5-9b94-bdb5fb698489 | -10.4754 | -43.4106 | 2025-10-18 14:00:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 83.4 |
| 332e183c-c4ef-3959-a24e-08e1e7835f07 | -10.1528 | -44.5289 | 2025-10-18 14:00:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 81.8 |
| 3c452f5c-d8e0-3b09-9324-490c7434a4cf | -12.9909 | -47.3217 | 2025-10-18 14:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 76.2 |
| 264d2932-16e3-3bf1-87d7-2d0f9cdd0a16 | -15.7923 | -43.643 | 2025-10-18 14:00:00 | GOES-19 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 146.4 |
| 7ac181d0-7549-3e22-a50e-368d64bbd210 | -10.6853 | -44.5506 | 2025-10-18 14:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 141.8 |
| e59d3d54-7fe6-332d-93b9-15882e46a4cc | -10.1139 | -44.5801 | 2025-10-18 14:00:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 65.9 |
| 06243f76-fb88-366a-a74a-a273a2b79020 | -6.4448 | -41.8368 | 2025-10-18 14:10:00 | GOES-19 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 95.8 |
| fe06ff52-d14e-3802-ad6b-6bddba5e7114 | -14.0287 | -44.6757 | 2025-10-18 14:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 287.1 |
| fbcc7b04-71e6-30fe-9dca-b8937720010f | -10.5136 | -43.4052 | 2025-10-18 14:10:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 167.6 |
| 8fb3ec1a-0f90-3d29-84ae-52779ed2f667 | -6.4257 | -41.8625 | 2025-10-18 14:10:00 | GOES-19 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 68.7 |
| 6853a310-891d-3846-ba57-a1287a359007 | -13.6174 | -43.9481 | 2025-10-18 14:10:00 | GOES-19 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 122.4 |
| 7461e06b-7b40-3829-8d89-b4e2ccb182f6 | -13.2644 | -47.1007 | 2025-10-18 14:10:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 208.9 |
| d42d38f1-83f8-3515-9d4f-4af3feba56b5 | -10.5327 | -43.4025 | 2025-10-18 14:10:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 85.3 |
| 8badd85b-095a-31c8-b339-c58004c95e1e | -10.1136 | -44.6033 | 2025-10-18 14:10:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 75.9 |
| a50c2423-bfd5-3e9e-8b0f-ab227e963984 | -3.0632 | -43.2161 | 2025-10-18 14:10:00 | GOES-19 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 118.6 |
| 6b6382d4-592e-3d96-b9ae-b7418c5f3af6 | -13.2005 | -46.4084 | 2025-10-18 14:10:00 | GOES-19 | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 93.9 |
| 2c796090-e32b-35d2-b083-16b2e798cc44 | -13.0106 | -47.2963 | 2025-10-18 14:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 82.4 |
| 5b3a088b-0688-3b3b-a0e7-2ac587eef29b | -10.4754 | -43.4106 | 2025-10-18 14:10:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 90.4 |
| a8b60599-1460-3e19-9d01-8bff282800bc | -11.9328 | -45.3429 | 2025-10-18 14:10:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 75.1 |
| 2e80b83b-af48-37e3-a10d-7138ac4a403a | -11.5912 | -44.0942 | 2025-10-18 14:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 68.7 |
| 2f9fbed2-5706-30dc-b601-5a1d243c55de | -15.7923 | -43.643 | 2025-10-18 14:10:00 | GOES-19 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 134.5 |
| 938a1785-ccc2-350a-91d5-7abe1bdda65b | -5.7596 | -42.7033 | 2025-10-18 14:10:00 | GOES-19 | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 63.8 |
| e8b1a6ae-be64-3640-8213-f0e0152bf903 | -13.0303 | -47.2709 | 2025-10-18 14:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 91.9 |
| 7ef6ca56-e28e-3748-a655-2167a0cc2cc2 | -11.3767 | -44.3131 | 2025-10-18 14:10:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 359.9 |
| 3c3955ac-8def-3fa9-8f1d-08598875a976 | -6.0301 | -41.9214 | 2025-10-18 14:10:00 | GOES-19 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 87.1 |
| 7995ccef-1ece-3aed-856f-8f2cbd4a169e | -15.6173 | -40.4717 | 2025-10-18 14:10:00 | GOES-19 | MACARANI | BAHIA | Brasil | 2919702 | 29 | 33 | nan | nan | nan | Mata Atlântica | 111.4 |
| 37d9fd34-6af6-3253-be91-313637101d52 | -6.3924 | -41.4569 | 2025-10-18 14:10:00 | GOES-19 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 87.5 |
| ac53c3f7-e671-3eab-97f1-818ccc7cf9ce | -11.358 | -44.2926 | 2025-10-18 14:10:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 380.3 |
| ffd10673-03b8-38ec-be94-0386130edee0 | -6.0489 | -41.9198 | 2025-10-18 14:10:00 | GOES-19 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 97.7 |
| 2ec84ee3-bb49-3edf-bffb-c31e9da2f674 | -13.6368 | -43.9446 | 2025-10-18 14:10:00 | GOES-19 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 173.9 |
| 1bb68392-20fc-3cd8-b582-cae355d03e36 | -11.6104 | -44.0913 | 2025-10-18 14:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 361.8 |
| 2f334678-58fa-33cd-98c2-7e6e227b2083 | -13.6563 | -43.9411 | 2025-10-18 14:10:00 | GOES-19 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 73.0 |
| db4d52ac-77ef-313a-b05b-c71014fcae78 | -10.7044 | -44.548 | 2025-10-18 14:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 106.9 |
| a2b505db-a103-3a6d-b705-807f35ce7616 | -10.685 | -44.5738 | 2025-10-18 14:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 62.7 |
| 058da7f4-478d-3ce6-817e-c21da4bb4ef7 | -14.09 | -43.6475 | 2025-10-18 14:10:00 | GOES-19 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 74.8 |
| 42ea2abe-23d6-384f-a18b-d87ffe7b1819 | -12.7196 | -50.8622 | 2025-10-18 14:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 87.7 |
| b3ae15b5-c70e-3de3-a0b5-917793aae255 | -13.2001 | -46.4312 | 2025-10-18 14:10:00 | GOES-19 | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 105.4 |
| d287d799-d107-33f1-881b-5a44afa8f291 | -12.1673 | -45.1003 | 2025-10-18 14:10:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 292.2 |
| 66f2adba-cd77-3cec-a3a7-5ae9a4c1ac54 | -11.3603 | -45.2646 | 2025-10-18 14:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 315.0 |
| 666fc658-471d-30a0-8e45-21f5389c01da | -12.1678 | -45.0771 | 2025-10-18 14:10:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 223.1 |
| 9385f675-b529-3d3b-bab8-b4aa5f949d60 | -11.9521 | -45.3401 | 2025-10-18 14:10:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 331.7 |
| c96d623f-f8a1-37cc-8ae3-de1a1b47d5f0 | -11.3411 | -45.2673 | 2025-10-18 14:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 179.4 |
| cce20f78-6172-3584-a823-9ca48b14d276 | -10.8097 | -43.951 | 2025-10-18 14:10:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 92.5 |
| cdb3d84e-31d6-3fdf-837a-503a3b70203a | -14.0482 | -44.6722 | 2025-10-18 14:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 87.9 |
| 8a6c9d48-9220-3d61-a342-6c00901eba53 | -11.3772 | -44.2897 | 2025-10-18 14:10:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 802.9 |
| a91771c8-760e-3be7-85ad-af1d2a46fdc0 | -7.0479 | -41.8269 | 2025-10-18 14:10:00 | GOES-19 | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 73.8 |
| c68438dd-7fee-3def-9192-2f38157e0b63 | -5.7784 | -42.7018 | 2025-10-18 14:10:00 | GOES-19 | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 69.6 |
| 85443925-b678-3fb7-93e8-7f6014c2bfdd | -11.3599 | -45.2877 | 2025-10-18 14:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 84.6 |
| c0d08dd2-00ac-3082-874a-c60204de8ec2 | -10.475 | -43.4342 | 2025-10-18 14:10:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 175.1 |
| 456c075d-5ef4-30d4-87e8-47232e3f3a35 | -10.8101 | -43.9275 | 2025-10-18 14:10:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 93.2 |
| 45b6b637-1eb5-3299-9143-526aa4515a00 | -3.7438 | -41.7456 | 2025-10-18 14:10:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 102.1 |
| f6aa3014-86e0-3f9d-9af3-89b15b3fe318 | -13.0299 | -47.2935 | 2025-10-18 14:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 82.7 |
| 6825a0c8-3207-3971-95be-552d8628ba72 | -12.1485 | -45.08 | 2025-10-18 14:10:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 93.1 |
| c3cfe28a-74a9-3a63-acf0-5d076f03860a | -10.4945 | -43.4079 | 2025-10-18 14:10:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 164.8 |
| c2a5c85e-96c1-37fb-a6b0-a2a1ca5fad58 | -13.0488 | -47.3131 | 2025-10-18 14:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 86.2 |
| fc4d00ac-cbcd-3b85-aad4-595cbe966841 | -13.2451 | -47.1036 | 2025-10-18 14:10:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 85.2 |
| d2c93963-2e2c-32ac-b606-d27f043ccfae | -4.4059 | -43.4049 | 2025-10-18 14:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 78.8 |
| e97ac103-907f-3210-b10d-a6d819e28b0c | -6.4634 | -41.8591 | 2025-10-18 14:10:00 | GOES-19 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 83.4 |
| f54a87cc-49d3-3402-a284-d210a568ff28 | -10.8289 | -43.9482 | 2025-10-18 14:10:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 97.6 |
| e87ec1a6-8fcb-3e7d-a957-cbded36d8487 | -12.1481 | -45.1032 | 2025-10-18 14:10:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 72.3 |
| a5fbeb29-2979-38e6-98f5-53efb03e91a6 | -6.4446 | -41.8608 | 2025-10-18 14:10:00 | GOES-19 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 95.0 |
| 6eec24fe-693f-350a-a3c1-a07d8c5cc3e3 | -4.6509 | -43.1337 | 2025-10-18 14:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 80.6 |
| 44920cd5-737d-3c8f-a4f9-f3dcfda3b75c | -10.7048 | -44.5248 | 2025-10-18 14:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 64.9 |
| d9f94a74-b409-3f72-873c-b83deda97bb4 | -13.0295 | -47.316 | 2025-10-18 14:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 93.3 |
| d14686d0-410f-3667-a6e3-137b0fdeef94 | -13.6373 | -43.9208 | 2025-10-18 14:10:00 | GOES-19 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 96.3 |
| a85e345d-b274-33d9-931d-a4a2566be243 | -11.7027 | -44.2879 | 2025-10-18 14:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 104.3 |
| ceb03efc-7076-3af9-9386-fbfc5f8f70e1 | -11.9709 | -45.3603 | 2025-10-18 14:10:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 225.5 |
| f943badf-9583-3712-b0b5-567fa7571ba0 | -11.9516 | -45.3632 | 2025-10-18 14:10:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 108.7 |
| 4ed21382-66ad-3a52-97dc-eac291b16d25 | -4.171 | -42.2215 | 2025-10-18 14:10:00 | GOES-19 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 99.1 |
| 2cdd692d-a576-3e90-8708-eb1b5a286ed3 | -4.0963 | -42.2021 | 2025-10-18 14:10:00 | GOES-19 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 114.1 |
| deb3f974-5cdc-3c8a-ace6-1be5c76ea3b6 | -6.2012 | -41.7389 | 2025-10-18 14:20:00 | GOES-19 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 77.5 |
| 16a6e40b-e071-39d1-9d8a-2dfc8b1042c4 | -13.2005 | -46.4084 | 2025-10-18 14:20:00 | GOES-19 | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 121.5 |
| 3f2c2cae-3506-353e-95d2-75eabfef6ef5 | -10.5327 | -43.4025 | 2025-10-18 14:20:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 86.2 |
| e1472eb6-3c96-3857-997f-506a4a9008dd | -6.0301 | -41.9214 | 2025-10-18 14:20:00 | GOES-19 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 86.4 |
| 432e9165-3c5c-3c51-b758-875131385e9e | -11.3772 | -44.2897 | 2025-10-18 14:20:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 555.6 |
| e7a30b13-a9b9-323b-aefc-d4cbcba4ac2c | -6.4443 | -41.8848 | 2025-10-18 14:20:00 | GOES-19 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 83.3 |
| 5e52bca5-a448-3a30-bd78-d6adc965438a | -11.4585 | -44.0204 | 2025-10-18 14:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 96.3 |
| 00f26d08-7177-3d5c-8b60-e019e5bbfea9 | -5.839 | -42.2472 | 2025-10-18 14:20:00 | GOES-19 | SÃO MIGUEL DA BAIXA GRANDE | PIAUÍ | Brasil | 2210383 | 22 | 33 | nan | nan | nan | Caatinga | 69.6 |
| 0c2056e1-0e5c-3724-af5f-10e9fe9b4efa | -10.514 | -43.3815 | 2025-10-18 14:20:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 98.7 |
| e6b7bfef-0b40-3275-a12e-8edd1c630a32 | -12.7196 | -50.8622 | 2025-10-18 14:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 93.8 |
| 3b46d82d-6db1-3dc3-8e2d-5e1e1b64cc1e | -5.933 | -42.2395 | 2025-10-18 14:20:00 | GOES-19 | SÃO FÉLIX DO PIAUÍ | PIAUÍ | Brasil | 2209609 | 22 | 33 | nan | nan | nan | Caatinga | 62.9 |
| 7fde753b-8ca2-3294-8c47-cd57d97106fb | -11.4384 | -44.0703 | 2025-10-18 14:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 131.8 |
| 4139bb10-d918-3d0c-9384-41551e220ed2 | -10.4596 | -44.3724 | 2025-10-18 14:20:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 66.0 |
| c7eb1c58-d37b-372c-b2f8-2d6174d589f5 | -6.3924 | -41.4569 | 2025-10-18 14:20:00 | GOES-19 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 99.5 |
| 0133cb57-62a5-3c40-aead-89e04897c5b5 | -13.2001 | -46.4312 | 2025-10-18 14:20:00 | GOES-19 | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 106.5 |
| c171fceb-bc95-3eff-9b07-9c101820c688 | -11.5058 | -43.5189 | 2025-10-18 14:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 85.6 |
| f9fed0c4-b076-3ae2-99bc-e5ec4405a8ef | -6.0489 | -41.9198 | 2025-10-18 14:20:00 | GOES-19 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 100.4 |
| 45fcd197-d702-3ac3-9425-2f31e612ccb6 | -7.1736 | -42.3638 | 2025-10-18 14:20:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 108.6 |
| 637a0ee3-1554-353c-9861-719333660200 | -6.314 | -45.5174 | 2025-10-18 14:20:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 58.4 |
| 20f41ef8-ed88-394b-b463-920c310a632a | -16.4591 | -43.037 | 2025-10-18 14:20:00 | GOES-19 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 94.4 |
| 1ead8411-bfcf-3ae3-8b67-11d373fab054 | -11.4581 | -44.0439 | 2025-10-18 14:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 132.2 |
| 4a7c3b5e-2a02-33a8-8835-42f228ba09d4 | -7.5656 | -42.7034 | 2025-10-18 14:20:00 | GOES-19 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 91.3 |
| 14f13e2d-1d84-3996-ae72-b4eec9df526b | -14.0292 | -44.6521 | 2025-10-18 14:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 99.2 |
| ded96db8-6a38-3bc5-927b-baa5a1c4497f | -11.358 | -44.2926 | 2025-10-18 14:20:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 100.2 |
| d0fcd945-41f3-3bb5-a94c-ca0c2408ae20 | -5.9518 | -42.2379 | 2025-10-18 14:20:00 | GOES-19 | SÃO FÉLIX DO PIAUÍ | PIAUÍ | Brasil | 2209609 | 22 | 33 | nan | nan | nan | Caatinga | 64.9 |
| 7d285fb7-4f40-340e-bef5-9e3aadc3c9ac | -4.3872 | -43.406 | 2025-10-18 14:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 72.5 |
| 71180a4e-bf2c-3ae9-8b97-092d5bc70457 | -6.4448 | -41.8368 | 2025-10-18 14:20:00 | GOES-19 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 84.3 |


[Clique aqui para ver as próximas entradas](README95.md)
